from __future__ import annotations

import csv
import re
from calendar import monthrange
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

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
}
FEATURE_RE = re.compile(r"\b(add|support|implement|introduce|enable|allow|expose|promote)\b", re.I)
FIX_RE = re.compile(r"\b(fix|avoid|prevent|correct|resolve)\b", re.I)
ROUTINE_RE = re.compile(
    r"\b(build|dependency|dependencies|deps|maven|gradle|bump|upgrade|format|formatting)\b",
    re.I,
)
IMPORTANT_INFRA_RE = re.compile(r"\b(cve|security|release|license|notice|blocking|block)\b", re.I)
LOW_SIGNAL_RE = re.compile(r"\b(docs?|javadoc|readme|tests?|benchmark|benchmarks?)\b", re.I)


@dataclass(frozen=True)
class SummaryResult:
    scored_csv_path: Path
    markdown_path: Path
    candidate_count: int
    selected_count: int
    since: date
    until: date


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
    if strategic_hits:
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
    if IMPORTANT_INFRA_RE.search(text):
        score += 20
        reasons.append("release/security/notice signal")

    author = row.get("author_name", "").lower()
    is_bot = "bot" in author or "dependabot" in author
    has_important_infra = bool(IMPORTANT_INFRA_RE.search(text))
    if is_bot and not has_important_infra:
        score -= 25
        reasons.append("downrank bot")
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


def write_markdown(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["## Java", "", *[row["summary_bullet"] for row in rows], ""]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def summarize_period(
    *,
    since: date,
    until: date,
    input_path: Path,
    output_dir: Path,
    top: int = 10,
    notes_path: Path | None = None,
    lancedb_dir: Path | None = None,
    label: str | None = None,
) -> SummaryResult:
    if since >= until:
        raise ValueError("--since must be before --until")
    use_lancedb = bool(notes_path and notes_path.exists() and lancedb_dir)
    indexed_examples = 0
    if use_lancedb:
        indexed_examples = build_java_highlight_index(notes_path, lancedb_dir)
        use_lancedb = indexed_examples > 0

    rows = [
        row
        for row in read_commit_rows(input_path)
        if since <= row_commit_date(row) < until
    ]
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
    selected_rows = scored_rows[:top]

    period_dir = output_dir / (label or summary_period_label(since, until))
    scored_csv_path = period_dir / "apache_iceberg_scored.csv"
    markdown_path = period_dir / "java_highlights.md"
    write_scored_csv(scored_rows, scored_csv_path)
    write_markdown(selected_rows, markdown_path)
    return SummaryResult(
        scored_csv_path=scored_csv_path,
        markdown_path=markdown_path,
        candidate_count=len(scored_rows),
        selected_count=len(selected_rows),
        since=since,
        until=until,
    )


def summarize_month(
    *,
    month: str,
    input_path: Path,
    output_dir: Path,
    top: int = 10,
    notes_path: Path | None = None,
    lancedb_dir: Path | None = None,
) -> SummaryResult:
    since, until = month_date_range(month)
    return summarize_period(
        since=since,
        until=until,
        input_path=input_path,
        output_dir=output_dir,
        top=top,
        notes_path=notes_path,
        lancedb_dir=lancedb_dir,
        label=month,
    )


def is_low_signal_for_semantic_boost(row: dict[str, str]) -> bool:
    subject = row.get("subject", "")
    text = f"{subject}\n{row.get('body', '')}"
    if IMPORTANT_INFRA_RE.search(text):
        return False
    return bool(LOW_SIGNAL_RE.search(subject) or ROUTINE_RE.search(subject))
