from __future__ import annotations

import csv
import re
from calendar import monthrange
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

from .config import TARGET_REPOSITORIES, RepoConfig
from .git_client import CSV_FIELDS
from .vector_ranker import build_java_highlight_index, rank_with_lancedb

SCORED_FIELDS = [
    *CSV_FIELDS,
    "heuristic_score",
    "lancedb_score",
    "score",
    "score_reasons",
    "lancedb_match",
    "summary_bullet",
]

IMPORTANT_AREAS = {
    "api",
    "core",
    "spark",
    "flink",
    "rest",
    "rest spec",
    "openapi",
    "open-api",
    "catalog",
    "spec",
}
STRATEGIC_TERMS = {
    "v4",
    "variant",
    "encryption",
    "row lineage",
    "partition statistics",
    "manifest",
    "catalog",
    "opendal",
    "storage",
}
FEATURE_RE = re.compile(r"\b(add|support|implement|introduce|enable|allow|expose|promote)\b", re.I)
FIX_RE = re.compile(r"\b(fix|avoid|prevent|correct|resolve)\b", re.I)
DEPENDENCY_BUMP_RE = re.compile(
    r"(^\s*(chore|build)\(deps?\)|\bbump\b.*\b(from|to|updates?)\b|\bupdate deps\b)",
    re.I,
)
ROUTINE_RE = re.compile(
    r"\b(build|dependency|dependencies|deps|maven|gradle|bump|upgrade|format|formatting)\b",
    re.I,
)
IMPORTANT_INFRA_RE = re.compile(r"\b(cve|security|release|license|notice|blocking|block)\b", re.I)
PUBLISHING_RE = re.compile(r"\b(cargo publish|publish crates?|missing crates?)\b", re.I)
CORRECTNESS_RE = re.compile(
    r"\b(correctness|data loss|corrupt|incorrect|preserve|dropping|reappear|delete-only)\b",
    re.I,
)
LOW_SIGNAL_RE = re.compile(r"\b(docs?|javadoc|readme|tests?|benchmark|benchmarks?)\b", re.I)


@dataclass(frozen=True)
class SummaryResult:
    scored_csv_paths: tuple[Path, ...]
    markdown_path: Path
    candidate_count: int
    selected_count: int
    since: date
    until: date

    @property
    def scored_csv_path(self) -> Path:
        return self.scored_csv_paths[0]


def parse_month(value: str) -> tuple[int, int]:
    if not re.fullmatch(r"\d{4}-\d{2}", value):
        raise ValueError("--month must use YYYY-MM")
    year, month = value.split("-")
    month_number = int(month)
    if not 1 <= month_number <= 12:
        raise ValueError("--month must use a month from 01 to 12")
    return int(year), month_number


def parse_iso_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def row_commit_date(row: dict[str, str]) -> date:
    parsed = parse_iso_datetime(row["committer_date"])
    return parsed.date()


def month_date_range(month: str) -> tuple[date, date]:
    year, month_number = parse_month(month)
    last_day = monthrange(year, month_number)[1]
    month_start = date(year, month_number, 1)
    next_month = month_start.replace(day=last_day) + date.resolution
    return month_start, next_month


def summary_period_label(since: date, until: date) -> str:
    return f"{since.isoformat()}_to_{until.isoformat()}"


def int_field(row: dict[str, str], field: str) -> int:
    try:
        return int(row.get(field) or "0")
    except ValueError:
        return 0


def split_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def prefix_parts(subject: str) -> set[str]:
    if ":" not in subject:
        return set()
    prefix = subject.split(":", 1)[0]
    return {part.strip().lower() for part in re.split(r"[,/]", prefix) if part.strip()}


def score_commit(row: dict[str, str]) -> tuple[int, str]:
    subject = row.get("subject", "")
    body = row.get("body", "")
    text = f"{subject}\n{body}"
    lowered = text.lower()
    reasons: list[str] = ["base"]
    score = 10
    is_dependency_bump = is_dependency_bump_subject(subject)

    if FEATURE_RE.search(subject):
        score += 25
        reasons.append("feature/api verb")
    if FIX_RE.search(subject):
        score += 8
        reasons.append("fix")

    areas = prefix_parts(subject)
    important_area_hits = sorted(areas & IMPORTANT_AREAS)
    if important_area_hits:
        score += 15
        reasons.append(f"important area: {', '.join(important_area_hits)}")

    strategic_hits = sorted(term for term in STRATEGIC_TERMS if term in lowered)
    if strategic_hits and not is_dependency_bump:
        score += 20
        reasons.append(f"strategic: {', '.join(strategic_hits)}")

    files_changed = int_field(row, "files_changed")
    churn = int_field(row, "insertions") + int_field(row, "deletions")
    if files_changed >= 20:
        score += 8
        reasons.append("large file count")
    elif files_changed >= 5:
        score += 4
        reasons.append("medium file count")
    if churn >= 1000:
        score += 8
        reasons.append("large churn")
    elif churn >= 200:
        score += 4
        reasons.append("medium churn")

    top_paths = split_values(row.get("top_level_paths", ""))
    if len(top_paths) >= 2:
        score += 5
        reasons.append("multi-area change")
    if row.get("co_authors"):
        score += 3
        reasons.append("co-authored")
    if IMPORTANT_INFRA_RE.search(text) and not is_dependency_bump:
        score += 20
        reasons.append("release/security/notice signal")
    if PUBLISHING_RE.search(text):
        score += 20
        reasons.append("publishing/release signal")
    if CORRECTNESS_RE.search(text) and not is_dependency_bump:
        score += 12
        reasons.append("correctness signal")

    author = row.get("author_name", "").lower()
    is_bot = "bot" in author or "dependabot" in author
    has_important_infra = bool(
        (IMPORTANT_INFRA_RE.search(text) and not is_dependency_bump)
        or PUBLISHING_RE.search(text)
    )
    if is_bot and not has_important_infra:
        score -= 25
        reasons.append("downrank bot")
    if is_dependency_bump:
        score -= 45
        reasons.append("downrank dependency bump")
    if LOW_SIGNAL_RE.search(subject):
        score -= 12
        reasons.append("downrank docs/tests/benchmarks")
    if ROUTINE_RE.search(subject) and not has_important_infra:
        score -= 15
        reasons.append("downrank routine build/deps")

    if row.get("pr_number"):
        score += 2
        reasons.append("has PR number")

    return score, "; ".join(reasons)


def contributor_names(row: dict[str, str]) -> list[str]:
    names: list[str] = []
    seen: set[str] = set()
    for name in [row.get("author_name", ""), *split_values(row.get("co_authors", ""))]:
        for clean in expand_contributor_name(name):
            if not clean or clean.lower() in {"github", "codex"} or clean in seen:
                continue
            seen.add(clean)
            names.append(clean)
    return names


def expand_contributor_name(name: str) -> list[str]:
    clean = name.strip()
    if not clean:
        return []
    parts = [part.strip() for part in re.split(r"\s*/\s*|\s+&\s+", clean) if part.strip()]
    return parts or [clean]


def join_names(names: list[str]) -> str:
    if not names:
        return "the community"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"


def summary_bullet(row: dict[str, str]) -> str:
    return f"- {row['subject']} (Thanks {join_names(contributor_names(row))}!)"


def sort_key(row: dict[str, str]) -> tuple[int, str, int, str]:
    pr_number = int_field(row, "pr_number")
    return (
        int_field(row, "score"),
        row.get("committer_date", ""),
        pr_number,
        row.get("commit_sha", ""),
    )


def read_commit_rows(input_path: Path) -> list[dict[str, str]]:
    with input_path.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def write_scored_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=SCORED_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(
    sections: list[tuple[RepoConfig, list[dict[str, str]], int]],
    output_path: Path,
    *,
    since: date,
    until: date,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    total_candidates = sum(candidate_count for _, _, candidate_count in sections)
    lines: list[str] = [
        "# Iceberg Community Sync Summary",
        "",
        f"- Period: `{since.isoformat()}` to before `{until.isoformat()}`",
        f"- Review candidates: `{total_candidates}`",
        "",
    ]
    for repo, rows, candidate_count in sections:
        lines.extend(
            [
                f"## {repo.full_name}",
                "",
                f"### {repo.summary_heading}",
                "",
                f"_Top {len(rows)} of {candidate_count} scored commits._",
                "",
                *[row["summary_bullet"] for row in rows],
                "",
            ]
        )
    output_path.write_text("\n".join(lines), encoding="utf-8")


def score_rows(
    rows: list[dict[str, str]],
    *,
    notes_path: Path | None = None,
    lancedb_dir: Path | None = None,
) -> list[dict[str, str]]:
    use_lancedb = bool(notes_path and notes_path.exists() and lancedb_dir)
    indexed_examples = 0
    if use_lancedb:
        indexed_examples = build_java_highlight_index(notes_path, lancedb_dir)
        use_lancedb = indexed_examples > 0

    scored_rows: list[dict[str, str]] = []
    for row in rows:
        row = {field: row.get(field, "") for field in CSV_FIELDS} | row
        heuristic_score, reasons = score_commit(row)
        lancedb_score = 0
        lancedb_match = ""
        if use_lancedb and lancedb_dir:
            match = rank_with_lancedb(row, lancedb_dir)
            lancedb_score = match.score
            lancedb_match = match.matched_example
            reasons = f"{reasons}; {match.reason}"
            if is_low_signal_for_semantic_boost(row):
                lancedb_score = min(lancedb_score, 3)
                reasons = f"{reasons}; capped LanceDB boost for routine/low-signal commit"
        elif notes_path and not notes_path.exists():
            reasons = f"{reasons}; no notes file for LanceDB ranking"
        elif notes_path and indexed_examples == 0:
            reasons = f"{reasons}; no Java highlights indexed for LanceDB ranking"

        row["heuristic_score"] = str(heuristic_score)
        row["lancedb_score"] = str(lancedb_score)
        row["score"] = str(heuristic_score + lancedb_score)
        row["lancedb_match"] = lancedb_match
        row["score_reasons"] = reasons
        row["summary_bullet"] = summary_bullet(row)
        scored_rows.append(row)

    scored_rows.sort(key=sort_key, reverse=True)
    return scored_rows


def rows_for_period(input_path: Path, *, since: date, until: date) -> list[dict[str, str]]:
    return [
        row
        for row in read_commit_rows(input_path)
        if since <= row_commit_date(row) < until
    ]


def write_single_repo_markdown(
    rows: list[dict[str, str]],
    output_path: Path,
    *,
    since: date,
    until: date,
    repo: RepoConfig,
    candidate_count: int,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Iceberg Community Sync Summary",
        "",
        f"- Period: `{since.isoformat()}` to before `{until.isoformat()}`",
        f"- Review candidates: `{candidate_count}`",
        "",
        f"## {repo.full_name}",
        "",
        f"### {repo.summary_heading}",
        "",
        f"_Top {len(rows)} of {candidate_count} scored commits._",
        "",
        *[row["summary_bullet"] for row in rows],
        "",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_summary_index(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_dirs = sorted(
        (path for path in output_dir.iterdir() if (path / "README.md").exists()),
        key=lambda path: path.name,
        reverse=True,
    )
    lines = [
        "# Iceberg Community Summaries",
        "",
        "Generated review-candidate summaries for Iceberg community sync meetings.",
        "",
    ]
    lines.extend(f"- [{path.name}]({path.name}/)" for path in summary_dirs)
    lines.append("")
    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def summarize_period(
    *,
    since: date,
    until: date,
    input_path: Path | None = None,
    input_dir: Path = Path("data/commits"),
    output_dir: Path,
    top: int = 10,
    notes_path: Path | None = None,
    lancedb_dir: Path | None = None,
    label: str | None = None,
    repositories: tuple[RepoConfig, ...] = TARGET_REPOSITORIES,
) -> SummaryResult:
    if since >= until:
        raise ValueError("--since must be before --until")
    period_dir = output_dir / (label or summary_period_label(since, until))
    markdown_path = period_dir / "README.md"
    scored_csv_paths: list[Path] = []
    sections: list[tuple[RepoConfig, list[dict[str, str]], int]] = []

    if input_path:
        repo = repositories[0]
        rows = rows_for_period(input_path, since=since, until=until)
        scored_rows = score_rows(rows, notes_path=notes_path, lancedb_dir=lancedb_dir)
        selected_rows = scored_rows[:top]
        scored_csv_path = period_dir / f"{repo.cache_name}_scored.csv"
        write_scored_csv(scored_rows, scored_csv_path)
        write_single_repo_markdown(
            selected_rows,
            markdown_path,
            since=since,
            until=until,
            repo=repo,
            candidate_count=len(scored_rows),
        )
        scored_csv_paths.append(scored_csv_path)
        sections.append((repo, selected_rows, len(scored_rows)))
    else:
        for repo in repositories:
            repo_input_path = input_dir / repo.csv_name
            if not repo_input_path.exists():
                continue
            repo_lancedb_dir = lancedb_dir / repo.cache_name if lancedb_dir else None
            rows = rows_for_period(repo_input_path, since=since, until=until)
            scored_rows = score_rows(rows, notes_path=notes_path, lancedb_dir=repo_lancedb_dir)
            selected_rows = scored_rows[:top]
            scored_csv_path = period_dir / f"{repo.cache_name}_scored.csv"
            write_scored_csv(scored_rows, scored_csv_path)
            scored_csv_paths.append(scored_csv_path)
            sections.append((repo, selected_rows, len(scored_rows)))
        write_markdown(sections, markdown_path, since=since, until=until)

    write_summary_index(output_dir)
    return SummaryResult(
        scored_csv_paths=tuple(scored_csv_paths),
        markdown_path=markdown_path,
        candidate_count=sum(candidate_count for _, _, candidate_count in sections),
        selected_count=sum(len(rows) for _, rows, _ in sections),
        since=since,
        until=until,
    )


def summarize_month(
    *,
    month: str,
    input_path: Path | None = None,
    input_dir: Path = Path("data/commits"),
    output_dir: Path,
    top: int = 10,
    notes_path: Path | None = None,
    lancedb_dir: Path | None = None,
    repositories: tuple[RepoConfig, ...] = TARGET_REPOSITORIES,
) -> SummaryResult:
    since, until = month_date_range(month)
    return summarize_period(
        since=since,
        until=until,
        input_path=input_path,
        input_dir=input_dir,
        output_dir=output_dir,
        top=top,
        notes_path=notes_path,
        lancedb_dir=lancedb_dir,
        label=month,
        repositories=repositories,
    )


def is_low_signal_for_semantic_boost(row: dict[str, str]) -> bool:
    subject = row.get("subject", "")
    text = f"{subject}\n{row.get('body', '')}"
    if is_dependency_bump_subject(subject):
        return True
    if IMPORTANT_INFRA_RE.search(text):
        return False
    return bool(LOW_SIGNAL_RE.search(subject) or ROUTINE_RE.search(subject))


def is_dependency_bump_subject(subject: str) -> bool:
    return bool(DEPENDENCY_BUMP_RE.search(subject))
