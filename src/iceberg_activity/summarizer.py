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
THEME_FIELDS = [
    "repository",
    "theme_key",
    "theme_title",
    "theme_score",
    "commit_count",
    "pr_numbers",
    "commit_shas",
    "contributors",
    "subjects",
    "summary_bullet",
]

IMPORTANT_AREAS = {
    "api",
    "core",
    "spark",
    "flink",
    "table",
    "manifest",
    "io",
    "cli",
    "cmd",
    "puffin",
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
    "v3",
    "deletion vector",
    "rewritefiles",
    "rewritedatafiles",
    "compaction",
    "conflict validation",
    "commit-conflict",
    "occ",
    "clustered",
    "maintenance",
    "copy-on-write",
    "golden round-trip",
    "round-trip",
    "puffin",
}
FEATURE_RE = re.compile(r"\b(add|support|implement|introduce|enable|allow|expose|promote)\b", re.I)
FIX_RE = re.compile(r"\b(fix|avoid|prevent|correct|resolve|retry)\b", re.I)
DEPENDENCY_BUMP_RE = re.compile(
    r"(^\s*(chore|build)\(deps?\)|^\s*(chore|build):\s*bump\b|"
    r"\bbump\b.*\b(from|to|updates?)\b|\bupdate deps\b|"
    r"\bupdated?\b.*\bdependenc(?:y|ies)\b)",
    re.I,
)
ROUTINE_RE = re.compile(
    r"\b(build|dependency|dependencies|deps|maven|gradle|bump|upgrade|format|formatting)\b",
    re.I,
)
IMPORTANT_INFRA_RE = re.compile(r"\b(cve|security|license|notice|blocking|block)\b", re.I)
PUBLISHING_RE = re.compile(r"\b(cargo publish|publish crates?|missing crates?)\b", re.I)
CORRECTNESS_RE = re.compile(
    r"\b(correctness|data loss|corrupt|incorrect|preserve|dropping|reappear|delete-only)\b",
    re.I,
)
VALIDATION_TEST_RE = re.compile(r"\b(golden round-trip|round-trip|regression)\b", re.I)
DELETION_VECTOR_RE = re.compile(r"\bdeletion[- ]vector\b", re.I)
VIEW_RE = re.compile(r"\bviews?\b|register_view|load_view|drop_view", re.I)
SUMMARY_SIGNAL_RE = re.compile(
    r"\b("
    r"deletion[- ]vector|rewritedatafiles|rewritefiles|compaction|"
    r"conflict validation|commit-conflict|occ|clustered|maintenance|"
    r"copy-on-write|golden round-trip|round-trip"
    r")\b",
    re.I,
)
COMMUNITY_SIGNAL_RE = re.compile(
    r"\b("
    r"geometry|geography|geospatial|mor|equality-rewrite|purgetable|"
    r"manifestfilter|manifestmerge|manifest filter|manifest merge|"
    r"v3 timestamp|timestampns|timestampnanos|timestamp nanosecond|"
    r"bulk delete|fileio|file io|file scan task|scan task reader|"
    r"pyiceberg-core|bindings/python|python bindings|"
    r"partition statistics scan|shredded variant|v4 content stats|"
    r"parquet/avro manifests?|unregister table|view object api"
    r")\b",
    re.I,
)
LOW_SIGNAL_RE = re.compile(r"\b(docs?|javadoc|readme|tests?|benchmark|benchmarks?)\b", re.I)
SYNC_LOW_SIGNAL_RE = re.compile(
    r"\b("
    r"backport|trim .*test|test expectations|flaky test|integration test|"
    r"test fixtures|cross-client .*tests?|typo|release notes?|issue template|"
    r"^test:|users|dependabot|release scripts?|scripts? .*release|help release|"
    r"cargo-public-api|lock check|check_standalone|toml fmt|"
    r"install headers|meson|hive option|draft prs?"
    r")\b",
    re.I,
)
CLI_ONLY_RE = re.compile(r"\b(cli|cmd)\b", re.I)
CI_ONLY_RE = re.compile(
    r"^\s*(ci|infra|build)(\([^)]+\))?:\s*"
    r".*\b(zizmor|workflow|workflows|actions?|codeql|pre-commit|permissions?|"
    r"comment tag|patch versions?|lock|fixture)\b",
    re.I,
)
DOCS_ONLY_RE = re.compile(r"^\s*docs?(\([^)]+\))?:", re.I)
TEST_ONLY_RE = re.compile(r"^\s*(test|tests)(\([^)]+\))?:", re.I)


@dataclass(frozen=True)
class SummaryResult:
    scored_csv_paths: tuple[Path, ...]
    theme_csv_paths: tuple[Path, ...]
    markdown_path: Path
    candidate_count: int
    selected_count: int
    since: date
    until: date

    @property
    def scored_csv_path(self) -> Path:
        return self.scored_csv_paths[0]

    @property
    def theme_csv_path(self) -> Path:
        return self.theme_csv_paths[0]


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
    parts = {part.strip().lower() for part in re.split(r"[,/]", prefix) if part.strip()}
    scope_match = re.search(r"\(([^)]+)\)", prefix)
    if scope_match:
        parts.update(
            part.strip().lower()
            for part in re.split(r"[,/]", scope_match.group(1))
            if part.strip()
        )
    return parts


def score_commit(row: dict[str, str]) -> tuple[int, str]:
    subject = row.get("subject", "")
    body = row.get("body", "")
    text = f"{subject}\n{body}"
    lowered = text.lower()
    reasons: list[str] = ["base"]
    score = 10
    is_dependency_bump = is_dependency_bump_subject(subject)
    is_validation_test = bool(VALIDATION_TEST_RE.search(subject))
    is_subject_low_signal = bool(LOW_SIGNAL_RE.search(subject) and not is_validation_test)

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
    if strategic_hits and not is_dependency_bump and not is_subject_low_signal:
        score += 20
        reasons.append(f"strategic: {', '.join(strategic_hits)}")
    summary_signal_hits = sorted(
        {match.group(1).lower() for match in SUMMARY_SIGNAL_RE.finditer(text)}
    )
    if summary_signal_hits and not is_dependency_bump and not is_subject_low_signal:
        score += 12
        reasons.append(f"summary signal: {', '.join(summary_signal_hits)}")
    community_signal_hits = sorted(
        {match.group(1).lower() for match in COMMUNITY_SIGNAL_RE.finditer(text)}
    )
    if community_signal_hits and not is_dependency_bump and not is_subject_low_signal:
        score += 18
        reasons.append(f"community signal: {', '.join(community_signal_hits)}")
    if DELETION_VECTOR_RE.search(text) and not is_dependency_bump and not is_subject_low_signal:
        score += 20
        reasons.append("deletion vector signal")

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
    if CORRECTNESS_RE.search(text) and not is_dependency_bump and not is_subject_low_signal:
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
    if is_validation_test:
        score += 12
        reasons.append("validation/regression test signal")
    if is_subject_low_signal:
        score -= 12
        reasons.append("downrank docs/tests/benchmarks")
    if SYNC_LOW_SIGNAL_RE.search(subject) and not is_validation_test:
        score -= 35
        reasons.append("downrank low-signal sync item")
    if CLI_ONLY_RE.search(subject) and not community_signal_hits and files_changed < 5:
        score -= 8
        reasons.append("downrank narrow CLI change")
    if ROUTINE_RE.search(subject) and not has_important_infra and not community_signal_hits:
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


def grouped_contributor_names(rows: list[dict[str, str]]) -> list[str]:
    names: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for name in contributor_names(row):
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            names.append(name)
    return names


def join_grouped_contributors(names: list[str]) -> str:
    if len(names) <= 5:
        return join_names(names)
    return f"{', '.join(names[:5])}, and {len(names) - 5} others"


def pr_sort_key(value: str) -> tuple[int, str]:
    try:
        return int(value), value
    except ValueError:
        return 0, value


def theme_rule(row: dict[str, str]) -> tuple[str, str] | None:
    subject = row.get("subject", "")
    body = row.get("body", "")
    text = f"{subject}\n{body}".lower()
    if is_dependency_bump_subject(subject):
        return None

    if "rest" in text and (
        "pagination" in text
        or "page-size" in text
        or "list_namespaces" in text
        or "list_tables" in text
        or "list_views" in text
    ):
        return (
            "rest-pagination",
            "REST pagination: add pagination and page-size support for namespaces, tables, and views",
        )
    if "maintenance" in text and ("cli" in text or "command" in text):
        return "maintenance-cli", "Maintenance CLI: add and expand table maintenance commands"
    if VIEW_RE.search(text) and (
        "catalog" in text or "rest" in text or "register" in text or "load" in text
    ):
        return "catalog-view-support", "Catalog views: add and expand view support"
    if "row lineage" in text:
        return "row-lineage", "Row lineage: expand support for lineage-aware reads and writes"
    if DELETION_VECTOR_RE.search(text):
        return "deletion-vectors", "Deletion vectors: add read, write, and validation support"
    if (
        "compaction" in text
        or "rewritedatafiles" in text
        or "rewritefiles" in text
        or "rewrite data files" in text
    ):
        return "compaction-rewrite", "Compaction and rewrite data files: expand rewrite planning and execution"
    if "puffin" in text:
        return "puffin", "Puffin: add metadata, reader, writer, and validation support"
    if "encryption" in text or "kms" in text or "keymanagement" in text:
        return "encryption", "Encryption: add key management and encrypted IO support"
    if "partition statistics" in text or "partition-stats" in text:
        return "partition-statistics", "Partition statistics: add scan and metadata support"
    return None


def theme_sort_key(row: dict[str, str]) -> tuple[int, str, int, str]:
    pr_numbers = [part.strip() for part in row.get("pr_numbers", "").split(";") if part.strip()]
    first_pr = min((pr_sort_key(pr)[0] for pr in pr_numbers), default=0)
    return (
        int_field(row, "theme_score"),
        row.get("newest_committer_date", ""),
        first_pr,
        row.get("theme_key", ""),
    )


def build_theme_rows(scored_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, tuple[str, list[dict[str, str]]]] = {}
    for row in scored_rows:
        rule = theme_rule(row)
        if rule:
            theme_key, theme_title = rule
        else:
            theme_key = f"commit:{row.get('commit_sha', '')}"
            theme_title = row.get("subject", "")
        if theme_key not in grouped:
            grouped[theme_key] = (theme_title, [])
        grouped[theme_key][1].append(row)

    theme_rows: list[dict[str, str]] = []
    for theme_key, (theme_title, rows) in grouped.items():
        rows = sorted(rows, key=sort_key, reverse=True)
        if len(rows) == 1:
            row = rows[0]
            theme_rows.append(
                {
                    "repository": row.get("repository", ""),
                    "theme_key": f"commit:{row.get('commit_sha', '')}",
                    "theme_title": row.get("subject", ""),
                    "theme_score": row.get("score", "0"),
                    "commit_count": "1",
                    "pr_numbers": row.get("pr_number", ""),
                    "commit_shas": row.get("commit_sha", ""),
                    "contributors": "; ".join(contributor_names(row)),
                    "subjects": row.get("subject", ""),
                    "summary_bullet": summary_bullet(row),
                    "newest_committer_date": row.get("committer_date", ""),
                    "_render": str(not is_render_suppressed(row)).lower(),
                }
            )
            continue

        max_score = max(int_field(row, "score") for row in rows)
        theme_score = max_score + min(24, 8 * (len(rows) - 1))
        pr_numbers = sorted(
            {row.get("pr_number", "") for row in rows if row.get("pr_number", "")},
            key=pr_sort_key,
        )
        commit_shas = [row.get("commit_sha", "") for row in rows if row.get("commit_sha", "")]
        contributors = grouped_contributor_names(rows)
        subjects = [row.get("subject", "") for row in rows if row.get("subject", "")]
        newest_committer_date = max((row.get("committer_date", "") for row in rows), default="")
        pr_text = f" ({', '.join(f'#{pr}' for pr in pr_numbers)})" if pr_numbers else ""
        theme_rows.append(
            {
                "repository": rows[0].get("repository", ""),
                "theme_key": theme_key,
                "theme_title": theme_title,
                "theme_score": str(theme_score),
                "commit_count": str(len(rows)),
                "pr_numbers": "; ".join(pr_numbers),
                "commit_shas": "; ".join(commit_shas),
                "contributors": "; ".join(contributors),
                "subjects": "; ".join(subjects),
                "summary_bullet": (
                    f"- {theme_title}{pr_text} "
                    f"(Thanks {join_grouped_contributors(contributors)}!)"
                ),
                "newest_committer_date": newest_committer_date,
                "_render": str(any(not is_render_suppressed(row) for row in rows)).lower(),
            }
        )

    theme_rows.sort(key=theme_sort_key, reverse=True)
    return theme_rows


def sort_key(row: dict[str, str]) -> tuple[int, str, int, str]:
    pr_number = int_field(row, "pr_number")
    return (
        int_field(row, "score"),
        row.get("committer_date", ""),
        pr_number,
        row.get("commit_sha", ""),
    )


def select_theme_rows(theme_rows: list[dict[str, str]], top: int) -> list[dict[str, str]]:
    return [
        row
        for row in theme_rows
        if row.get("_render", "true") == "true"
    ][:top]


def read_commit_rows(input_path: Path) -> list[dict[str, str]]:
    with input_path.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def clean_csv_value(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines())


def clean_csv_rows(rows: list[dict[str, str]], fields: list[str]) -> list[dict[str, str]]:
    return [
        {
            field: clean_csv_value(row.get(field, ""))
            for field in fields
        }
        for row in rows
    ]


def write_scored_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=SCORED_FIELDS,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(clean_csv_rows(rows, SCORED_FIELDS))


def write_theme_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=THEME_FIELDS,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(clean_csv_rows(rows, THEME_FIELDS))


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
        renderable_count = sum(1 for row in rows if row.get("_render", "true") == "true")
        lines.extend(
            [
                f"## {repo.full_name}",
                "",
                f"### {repo.summary_heading}",
                "",
                f"_Top {renderable_count} themes from {candidate_count} scored commits._",
                "",
                *[
                    row["summary_bullet"]
                    for row in rows
                    if row.get("_render", "true") == "true"
                ],
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
    renderable_rows = [row for row in rows if row.get("_render", "true") == "true"]
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
        f"_Top {len(renderable_rows)} themes from {candidate_count} scored commits._",
        "",
        *[row["summary_bullet"] for row in renderable_rows],
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
    review_data_dir = period_dir / "review-data"
    scored_csv_paths: list[Path] = []
    theme_csv_paths: list[Path] = []
    sections: list[tuple[RepoConfig, list[dict[str, str]], int]] = []

    if input_path:
        repo = repositories[0]
        rows = rows_for_period(input_path, since=since, until=until)
        scored_rows = score_rows(rows, notes_path=notes_path, lancedb_dir=lancedb_dir)
        theme_rows = build_theme_rows(scored_rows)
        selected_rows = select_theme_rows(theme_rows, top)
        scored_csv_path = review_data_dir / f"{repo.cache_name}_scored.csv"
        theme_csv_path = review_data_dir / f"{repo.cache_name}_themes.csv"
        write_scored_csv(scored_rows, scored_csv_path)
        write_theme_csv(theme_rows, theme_csv_path)
        write_single_repo_markdown(
            selected_rows,
            markdown_path,
            since=since,
            until=until,
            repo=repo,
            candidate_count=len(scored_rows),
        )
        scored_csv_paths.append(scored_csv_path)
        theme_csv_paths.append(theme_csv_path)
        sections.append((repo, selected_rows, len(scored_rows)))
    else:
        for repo in repositories:
            repo_input_path = input_dir / repo.csv_name
            if not repo_input_path.exists():
                continue
            repo_lancedb_dir = lancedb_dir / repo.cache_name if lancedb_dir else None
            rows = rows_for_period(repo_input_path, since=since, until=until)
            scored_rows = score_rows(rows, notes_path=notes_path, lancedb_dir=repo_lancedb_dir)
            theme_rows = build_theme_rows(scored_rows)
            selected_rows = select_theme_rows(theme_rows, top)
            scored_csv_path = review_data_dir / f"{repo.cache_name}_scored.csv"
            theme_csv_path = review_data_dir / f"{repo.cache_name}_themes.csv"
            write_scored_csv(scored_rows, scored_csv_path)
            write_theme_csv(theme_rows, theme_csv_path)
            scored_csv_paths.append(scored_csv_path)
            theme_csv_paths.append(theme_csv_path)
            sections.append((repo, selected_rows, len(scored_rows)))
        write_markdown(sections, markdown_path, since=since, until=until)

    write_summary_index(output_dir)
    return SummaryResult(
        scored_csv_paths=tuple(scored_csv_paths),
        theme_csv_paths=tuple(theme_csv_paths),
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


def is_render_suppressed(row: dict[str, str]) -> bool:
    subject = row.get("subject", "")
    text = f"{subject}\n{row.get('body', '')}"
    subject_has_important_infra = bool(IMPORTANT_INFRA_RE.search(subject))
    if PUBLISHING_RE.search(text):
        return False

    author = row.get("author_name", "").lower()
    top_paths = set(split_values(row.get("top_level_paths", "").lower()))
    if is_dependency_bump_subject(subject):
        return not subject_has_important_infra
    if "dependabot" in author:
        return not subject_has_important_infra
    if subject_has_important_infra:
        return False
    if CI_ONLY_RE.search(subject):
        return True
    if DOCS_ONLY_RE.search(subject):
        return True
    if TEST_ONLY_RE.search(subject):
        return True
    if top_paths and top_paths <= {".github"}:
        return True
    if top_paths and top_paths <= {"docs"}:
        return True
    if re.search(
        r"\b("
        r"test expectations|flaky test|trim .*test|test fixtures|"
        r"cross-client .*tests?|typo|release notes?|issue template|"
        r"release scripts?|scripts? .*release|help release|cargo-public-api|"
        r"lock check|check_standalone|toml fmt|install headers|meson|"
        r"draft prs?|zizmor|workflow|actions/upload-artifact|gitignore"
        r")\b",
        subject,
        re.I,
    ):
        return True
    if re.search(r"^\s*(build|chore|infra)(\([^)]+\))?:", subject, re.I) and ROUTINE_RE.search(
        subject
    ):
        return True
    return False


def is_dependency_bump_subject(subject: str) -> bool:
    return bool(DEPENDENCY_BUMP_RE.search(subject))
