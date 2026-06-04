from __future__ import annotations

import csv
from pathlib import Path

from iceberg_activity.backtester import backtest_java_highlights, parse_sync_sections
from iceberg_activity.git_client import CSV_FIELDS


def test_parse_sync_sections_extracts_java_prs(tmp_path: Path) -> None:
    notes = tmp_path / "notes.md"
    notes.write_text(
        """2026-06-01
● Highlights
○ Java
■ Core: Add V4 feature (#123) <Thanks A!>
■ Spark: Fix bug [#456] (Thanks B!)
○ Python
■ Ignore this (#999)
""",
        encoding="utf-8",
    )

    sections = parse_sync_sections(notes)

    assert len(sections) == 1
    assert sections[0].sync_date.isoformat() == "2026-06-01"
    assert [highlight.pr_number for highlight in sections[0].java_highlights] == [
        "123",
        "456",
    ]


def test_backtest_java_highlights_writes_reports(tmp_path: Path) -> None:
    notes = tmp_path / "notes.md"
    commits = tmp_path / "commits.csv"
    output_dir = tmp_path / "backtests"
    lancedb_dir = tmp_path / "lancedb"
    notes.write_text(
        """2026-05-01
● Highlights
○ Java
■ Core: Add V4 location utilities (#1) <Thanks A!>

2026-06-01
● Highlights
○ Java
■ Spark: Support row lineage (#2) <Thanks B!>
■ Flink: Fix older issue (#3) <Thanks C!>
""",
        encoding="utf-8",
    )
    write_rows(
        commits,
        [
            commit_row("1", "Core: Add V4 location utilities (#1)", "2026-04-20T12:00:00+00:00"),
            commit_row("2", "Spark: Support row lineage (#2)", "2026-05-20T12:00:00+00:00"),
            commit_row("3", "Flink: Fix older issue (#3)", "2026-04-15T12:00:00+00:00"),
            commit_row("4", "Docs: Fix typo (#4)", "2026-05-21T12:00:00+00:00"),
        ],
    )

    result = backtest_java_highlights(
        notes_path=notes,
        input_path=commits,
        output_dir=output_dir,
        lancedb_dir=lancedb_dir,
        top=1,
        comparison_top=2,
        start_date=None,
        end_date=None,
    )

    assert result.sections_evaluated == 2
    assert result.note_prs == 3
    assert result.found_prs == 2
    assert result.hits_at_comparison_top >= 1
    markdown = result.markdown_path.read_text(encoding="utf-8")
    assert "Hits@1" in markdown
    assert "Outside Sync Window" in markdown
    assert "#3: 2026-04-15 Flink: Fix older issue (#3)" in markdown

    with result.csv_path.open(newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))
    statuses = {row["pr_number"]: row["status"] for row in rows}
    assert statuses["1"] == "found"
    assert statuses["2"] == "found"
    assert statuses["3"] == "outside_sync_window"


def commit_row(pr_number: str, subject: str, committer_date: str) -> dict[str, str]:
    row = {field: "" for field in CSV_FIELDS}
    row.update(
        {
            "repository": "apache/iceberg",
            "commit_sha": pr_number * 8,
            "short_sha": pr_number,
            "author_name": "Author",
            "author_email": "author@example.com",
            "author_date": committer_date,
            "committer_name": "GitHub",
            "committer_email": "noreply@github.com",
            "committer_date": committer_date,
            "subject": subject,
            "body": "",
            "parents": "parent",
            "pr_number": pr_number,
            "is_merge_commit": "false",
            "files_changed": "3",
            "insertions": "30",
            "deletions": "1",
            "top_level_paths": subject.split(":", 1)[0].lower(),
        }
    )
    return row


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
