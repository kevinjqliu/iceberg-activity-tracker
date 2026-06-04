from __future__ import annotations

import csv
import re
import shutil
import statistics
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

from .git_client import CSV_FIELDS
from .summarizer import (
    is_low_signal_for_semantic_boost,
    read_commit_rows,
    score_commit,
    sort_key,
    summary_bullet,
)
from .vector_ranker import build_java_highlight_index, rank_with_lancedb

SECTION_RE = re.compile(
    r"(?ms)^(?P<date>\d{4}-\d{2}-\d{2})[^\n]*\n(?P<body>.*?)(?=^\d{4}-\d{2}-\d{2}\b|\Z)"
)
JAVA_SECTION_RE = re.compile(
    r"(?ms)^○\s*Java[^\n]*\n(?P<body>.*?)(?=^○\s|^●\s|^\d{4}-\d{2}-\d{2}\b|\Z)"
)
NOTE_BULLET_RE = re.compile(r"^\s*■\s*(?P<text>.+?)\s*$", re.M)
PR_RE = re.compile(r"(?:\(#|\[#|#)(\d+)\)?\]?")


@dataclass(frozen=True)
class NoteHighlight:
    pr_number: str
    text: str


@dataclass(frozen=True)
class SyncSection:
    sync_date: date
    body: str
    java_highlights: tuple[NoteHighlight, ...]


@dataclass(frozen=True)
class BacktestResult:
    markdown_path: Path
    csv_path: Path
    sections_evaluated: int
    note_prs: int
    found_prs: int
    hits_at_top: int
    hits_at_comparison_top: int


DETAIL_FIELDS = [
    "sync_date",
    "previous_sync_date",
    "pr_number",
    "status",
    "rank",
    "score",
    "heuristic_score",
    "lancedb_score",
    "subject",
    "committer_date",
    "note_bullet",
    "lancedb_match",
    "score_reasons",
]


def parse_sync_sections(notes_path: Path) -> list[SyncSection]:
    notes = notes_path.read_text(encoding="utf-8")
    sections: list[SyncSection] = []
    for match in SECTION_RE.finditer(notes):
        java_match = JAVA_SECTION_RE.search(match.group("body"))
        highlights: list[NoteHighlight] = []
        if java_match:
            for bullet in NOTE_BULLET_RE.finditer(java_match.group("body")):
                text = bullet.group("text")
                for pr_number in PR_RE.findall(text):
                    highlights.append(NoteHighlight(pr_number=pr_number, text=text))
        sections.append(
            SyncSection(
                sync_date=date.fromisoformat(match.group("date")),
                body=match.group(0),
                java_highlights=tuple(highlights),
            )
        )
    return sorted(sections, key=lambda section: section.sync_date)


def parse_row_date(row: dict[str, str]) -> date:
    return datetime.fromisoformat(row["committer_date"].replace("Z", "+00:00")).date()


def score_rows_for_window(
    *,
    rows: list[dict[str, str]],
    prior_notes_text: str,
    lancedb_dir: Path,
) -> tuple[list[dict[str, str]], int]:
    prior_notes_path = lancedb_dir.parent / f"{lancedb_dir.name}.md"
    prior_notes_path.write_text(prior_notes_text, encoding="utf-8")
    indexed_examples = build_java_highlight_index(prior_notes_path, lancedb_dir)

    scored: list[dict[str, str]] = []
    for row in rows:
        row = {field: row.get(field, "") for field in CSV_FIELDS} | row
        heuristic_score, reasons = score_commit(row)
        lancedb_score = 0
        lancedb_match = ""
        if indexed_examples:
            match = rank_with_lancedb(row, lancedb_dir)
            lancedb_score = match.score
            lancedb_match = match.matched_example
            reasons = f"{reasons}; {match.reason}"
            if is_low_signal_for_semantic_boost(row):
                lancedb_score = min(lancedb_score, 3)
                reasons = f"{reasons}; capped LanceDB boost for routine/low-signal commit"
        row["heuristic_score"] = str(heuristic_score)
        row["lancedb_score"] = str(lancedb_score)
        row["score"] = str(heuristic_score + lancedb_score)
        row["score_reasons"] = reasons
        row["lancedb_match"] = lancedb_match
        row["summary_bullet"] = summary_bullet(row)
        scored.append(row)

    scored.sort(key=sort_key, reverse=True)
    return scored, indexed_examples


def median_rank(ranks: list[int]) -> str:
    if not ranks:
        return ""
    return f"{statistics.median(ranks):.1f}"


def write_detail_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=DETAIL_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def backtest_java_highlights(
    *,
    notes_path: Path,
    input_path: Path,
    output_dir: Path,
    lancedb_dir: Path,
    top: int = 10,
    comparison_top: int = 20,
    start_date: date | None = None,
    end_date: date | None = None,
) -> BacktestResult:
    sections = parse_sync_sections(notes_path)
    commit_rows = read_commit_rows(input_path)
    for row in commit_rows:
        row["_date"] = parse_row_date(row).isoformat()

    commit_prs = {row["pr_number"]: row for row in commit_rows if row.get("pr_number")}
    detail_rows: list[dict[str, str]] = []
    markdown: list[str] = [
        "# Java Summary Backtest",
        "",
        f"- Notes: `{notes_path}`",
        f"- Commits: `{input_path}`",
        f"- Hit thresholds: top {top}, top {comparison_top}",
        "",
    ]

    total_note_prs = 0
    total_found = 0
    total_hits_top = 0
    total_hits_comparison = 0
    sections_evaluated = 0

    if lancedb_dir.exists():
        shutil.rmtree(lancedb_dir)
    lancedb_dir.mkdir(parents=True, exist_ok=True)

    for index, section in enumerate(sections):
        if not section.java_highlights:
            continue
        if start_date and section.sync_date < start_date:
            continue
        if end_date and section.sync_date > end_date:
            continue

        previous_date = sections[index - 1].sync_date if index > 0 else None
        window_rows = [
            row
            for row in commit_rows
            if (previous_date is None or date.fromisoformat(row["_date"]) > previous_date)
            and date.fromisoformat(row["_date"]) <= section.sync_date
        ]
        prior_notes_text = "\n".join(prior.body for prior in sections[:index])
        ranked_rows, indexed_examples = score_rows_for_window(
            rows=window_rows,
            prior_notes_text=prior_notes_text,
            lancedb_dir=lancedb_dir / section.sync_date.isoformat(),
        )
        ranks_by_pr = {
            row["pr_number"]: (rank, row)
            for rank, row in enumerate(ranked_rows, start=1)
            if row.get("pr_number")
        }
        note_prs = {highlight.pr_number for highlight in section.java_highlights}

        found: list[tuple[NoteHighlight, int, dict[str, str]]] = []
        missing_window: list[NoteHighlight] = []
        missing_csv: list[NoteHighlight] = []
        for highlight in section.java_highlights:
            if highlight.pr_number in ranks_by_pr:
                rank, row = ranks_by_pr[highlight.pr_number]
                found.append((highlight, rank, row))
            elif highlight.pr_number in commit_prs:
                missing_window.append(highlight)
            else:
                missing_csv.append(highlight)

        ranks = [rank for _, rank, _ in found]
        hits_top = sum(rank <= top for rank in ranks)
        hits_comparison = sum(rank <= comparison_top for rank in ranks)
        false_positives = [row for row in ranked_rows[:top] if row.get("pr_number") not in note_prs]

        total_note_prs += len(section.java_highlights)
        total_found += len(found)
        total_hits_top += hits_top
        total_hits_comparison += hits_comparison
        sections_evaluated += 1

        markdown.extend(
            [
                f"## {section.sync_date.isoformat()} Java",
                "",
                f"- Previous sync date: `{previous_date.isoformat() if previous_date else ''}`",
                f"- Candidate commits: `{len(window_rows)}`",
                f"- LanceDB prior examples: `{indexed_examples}`",
                f"- Note PRs: `{len(section.java_highlights)}`",
                f"- Found in sync window: `{len(found)}`",
                f"- Hits@{top}: `{hits_top}/{len(found)}`",
                f"- Hits@{comparison_top}: `{hits_comparison}/{len(found)}`",
                f"- Median found rank: `{median_rank(ranks)}`",
                "",
                "### Found Note PRs",
                "",
            ]
        )
        if found:
            for highlight, rank, row in sorted(found, key=lambda item: item[1]):
                markdown.append(
                    f"- rank `{rank}` score `{row['score']}` "
                    f"(heur `{row['heuristic_score']}`, lancedb `{row['lancedb_score']}`) "
                    f"#{highlight.pr_number}: {row['subject']}"
                )
                detail_rows.append(
                    detail_row(
                        section=section,
                        previous_date=previous_date,
                        highlight=highlight,
                        status="found",
                        rank=rank,
                        row=row,
                    )
                )
        else:
            markdown.append("- None")

        if missing_window:
            markdown.extend(["", "### Outside Sync Window", ""])
            for highlight in missing_window:
                row = commit_prs[highlight.pr_number]
                markdown.append(
                    f"- #{highlight.pr_number}: {row['committer_date'][:10]} {row['subject']}"
                )
                detail_rows.append(
                    detail_row(
                        section=section,
                        previous_date=previous_date,
                        highlight=highlight,
                        status="outside_sync_window",
                        rank=None,
                        row=row,
                    )
                )
        if missing_csv:
            markdown.extend(["", "### Missing From Commit CSV", ""])
            for highlight in missing_csv:
                markdown.append(f"- #{highlight.pr_number}: {highlight.text}")
                detail_rows.append(
                    detail_row(
                        section=section,
                        previous_date=previous_date,
                        highlight=highlight,
                        status="missing_from_csv",
                        rank=None,
                        row=None,
                    )
                )

        markdown.extend(["", f"### False Positives In Top {top}", ""])
        if false_positives:
            for row in false_positives:
                markdown.append(f"- score `{row['score']}` #{row.get('pr_number')}: {row['subject']}")
        else:
            markdown.append("- None")
        markdown.append("")

    summary = [
        "# Java Summary Backtest",
        "",
        f"- Sections evaluated: `{sections_evaluated}`",
        f"- Note PRs: `{total_note_prs}`",
        f"- Found in sync windows: `{total_found}`",
        f"- Hits@{top}: `{total_hits_top}/{total_found}`",
        f"- Hits@{comparison_top}: `{total_hits_comparison}/{total_found}`",
        "",
    ]
    markdown = summary + markdown[6:]

    output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = output_dir / "java_summary_backtest.md"
    csv_path = output_dir / "java_summary_backtest.csv"
    markdown_path.write_text("\n".join(markdown), encoding="utf-8")
    write_detail_csv(detail_rows, csv_path)
    return BacktestResult(
        markdown_path=markdown_path,
        csv_path=csv_path,
        sections_evaluated=sections_evaluated,
        note_prs=total_note_prs,
        found_prs=total_found,
        hits_at_top=total_hits_top,
        hits_at_comparison_top=total_hits_comparison,
    )


def detail_row(
    *,
    section: SyncSection,
    previous_date: date | None,
    highlight: NoteHighlight,
    status: str,
    rank: int | None,
    row: dict[str, str] | None,
) -> dict[str, str]:
    return {
        "sync_date": section.sync_date.isoformat(),
        "previous_sync_date": previous_date.isoformat() if previous_date else "",
        "pr_number": highlight.pr_number,
        "status": status,
        "rank": str(rank or ""),
        "score": row.get("score", "") if row else "",
        "heuristic_score": row.get("heuristic_score", "") if row else "",
        "lancedb_score": row.get("lancedb_score", "") if row else "",
        "subject": row.get("subject", "") if row else "",
        "committer_date": row.get("committer_date", "") if row else "",
        "note_bullet": highlight.text,
        "lancedb_match": row.get("lancedb_match", "") if row else "",
        "score_reasons": row.get("score_reasons", "") if row else "",
    }
