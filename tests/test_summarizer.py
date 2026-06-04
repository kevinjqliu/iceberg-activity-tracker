from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import pytest

from iceberg_activity.config import RepoConfig
from iceberg_activity.git_client import CSV_FIELDS
from iceberg_activity.summarizer import (
    contributor_names,
    parse_month,
    score_commit,
    summarize_month,
    summarize_period,
    summary_bullet,
)


def test_parse_month_validates_shape() -> None:
    assert parse_month("2026-06") == (2026, 6)
    with pytest.raises(ValueError, match="YYYY-MM"):
        parse_month("2026-6")
    with pytest.raises(ValueError, match="01 to 12"):
        parse_month("2026-13")


def test_score_commit_boosts_features_and_downranks_routine_work() -> None:
    feature = commit_row(
        subject="Core: Add V4 location relativization utilities (#16174)",
        top_level_paths="core",
        files_changed="8",
        insertions="250",
        pr_number="16174",
    )
    docs = commit_row(
        subject="Docs: Fix typo in README (#16000)",
        top_level_paths="docs",
        files_changed="1",
        insertions="2",
        deletions="1",
        pr_number="16000",
    )
    bot_security = commit_row(
        subject="Build: Fix CVE-2026-12345 in dependency (#16001)",
        author_name="dependabot[bot]",
        pr_number="16001",
    )

    feature_score, feature_reasons = score_commit(feature)
    docs_score, docs_reasons = score_commit(docs)
    bot_score, bot_reasons = score_commit(bot_security)

    assert feature_score > docs_score
    assert "feature/api verb" in feature_reasons
    assert "downrank docs/tests/benchmarks" in docs_reasons
    assert bot_score > docs_score
    assert "release/security/notice signal" in bot_reasons


def test_score_commit_downranks_dependency_bumps_below_rust_summary_signals() -> None:
    dependency_bump = commit_row(
        repository="apache/iceberg-rust",
        subject="chore(deps): Bump reqwest from 0.12.28 to 0.13.3 (#2554)",
        body="Dependabot update for GHSA-mf9v-mfxr-j63j in a networking crate.",
        author_name="dependabot[bot]",
        co_authors="dependabot[bot]",
        files_changed="3",
        insertions="200",
        pr_number="2554",
    )
    publishing_fix = commit_row(
        repository="apache/iceberg-rust",
        subject="Use cargo publish to publish crates (#2489)",
        body="Switch to cargo publish --workspace to fix missing crates during release.",
        author_name="blackmwk",
        files_changed="17",
        insertions="23",
        deletions="17",
        top_level_paths=".github; Cargo.toml; crates",
        pr_number="2489",
    )
    correctness_fix = commit_row(
        repository="apache/iceberg-rust",
        subject="fix(transaction): preserve delete-only manifests in FastAppend (#2545)",
        body="Fix FastAppend dropping delete-only manifests and causing deleted files to reappear.",
        author_name="Liang-Chi Hsieh",
        insertions="206",
        deletions="3",
        top_level_paths="crates",
        pr_number="2545",
    )
    storage_update = commit_row(
        repository="apache/iceberg-rust",
        subject="Add Hugging Face storage option to storage/opendal/README (#2487)",
        author_name="Quentin Lhoest",
        top_level_paths="crates",
        pr_number="2487",
    )

    dependency_score, dependency_reasons = score_commit(dependency_bump)
    publishing_score, publishing_reasons = score_commit(publishing_fix)
    correctness_score, correctness_reasons = score_commit(correctness_fix)
    storage_score, storage_reasons = score_commit(storage_update)

    assert "downrank dependency bump" in dependency_reasons
    assert "publishing/release signal" in publishing_reasons
    assert "correctness signal" in correctness_reasons
    assert "strategic: opendal, storage" in storage_reasons
    assert publishing_score > dependency_score
    assert correctness_score > dependency_score
    assert storage_score > dependency_score


def test_summary_bullet_formats_thanks() -> None:
    row = commit_row(
        subject="Spark: Add feature (#123)",
        author_name="Alice",
        co_authors="Bob; Carol",
    )

    assert summary_bullet(row) == "- Spark: Add feature (#123) (Thanks Alice, Bob, and Carol!)"


def test_contributor_names_splits_compound_author_names() -> None:
    row = commit_row(author_name="Hongyue/Steve Zhang", co_authors="Gang & emkornfield")

    assert contributor_names(row) == ["Hongyue", "Steve Zhang", "Gang", "emkornfield"]


def test_summarize_month_writes_scored_csv_and_markdown(tmp_path: Path) -> None:
    input_path = tmp_path / "apache_iceberg.csv"
    output_dir = tmp_path / "summaries"
    notes_path = tmp_path / "notes.md"
    lancedb_dir = tmp_path / "lancedb"
    notes_path.write_text(
        """2026-05-01
● Highlights
○ Java
■ Core: Add V4 location relativization utilities (#16174) <Thanks A!>
""",
        encoding="utf-8",
    )
    rows = [
        commit_row(
            commit_sha="1",
            short_sha="1",
            subject="Core: Add V4 location relativization utilities (#16174)",
            committer_date="2026-06-03T12:00:00+00:00",
            author_name="Anoop Johnson",
            top_level_paths="core",
            files_changed="8",
            insertions="250",
            pr_number="16174",
        ),
        commit_row(
            commit_sha="2",
            short_sha="2",
            subject="Docs: Fix typo (#16000)",
            committer_date="2026-06-02T12:00:00+00:00",
            author_name="Doc Writer",
            top_level_paths="docs",
            pr_number="16000",
        ),
        commit_row(
            commit_sha="3",
            short_sha="3",
            subject="Spark: Implement row lineage support (#16100)",
            committer_date="2026-05-30T12:00:00+00:00",
            author_name="Spark Dev",
            top_level_paths="spark",
            pr_number="16100",
        ),
    ]
    write_rows(input_path, rows)

    result = summarize_month(
        month="2026-06",
        input_path=input_path,
        output_dir=output_dir,
        top=1,
        notes_path=notes_path,
        lancedb_dir=lancedb_dir,
    )

    assert result.candidate_count == 2
    assert result.selected_count == 1
    assert result.since == date(2026, 6, 1)
    assert result.until == date(2026, 7, 1)
    with result.scored_csv_path.open(newline="", encoding="utf-8") as csv_file:
        scored = list(csv.DictReader(csv_file))
    assert len(scored) == 2
    assert scored[0]["score"]
    assert scored[0]["heuristic_score"]
    assert scored[0]["lancedb_score"]
    assert scored[0]["lancedb_match"]
    assert scored[0]["score_reasons"]

    markdown = result.markdown_path.read_text(encoding="utf-8")
    assert markdown == (
        "# Iceberg Community Sync Summary\n"
        "\n"
        "- Period: `2026-06-01` to before `2026-07-01`\n"
        "- Review candidates: `2`\n"
        "\n"
        "## apache/iceberg\n"
        "\n"
        "### Java\n"
        "\n"
        "_Top 1 of 2 scored commits._\n"
        "\n"
        "- Core: Add V4 location relativization utilities (#16174) (Thanks Anoop Johnson!)\n"
    )


def test_summarize_period_uses_meeting_window_output_dir(tmp_path: Path) -> None:
    input_path = tmp_path / "apache_iceberg.csv"
    output_dir = tmp_path / "summaries"
    rows = [
        commit_row(
            commit_sha="1",
            short_sha="1",
            subject="Spark: Implement row lineage support (#16100)",
            committer_date="2026-05-13T00:00:00+00:00",
            author_name="Spark Dev",
            top_level_paths="spark",
            pr_number="16100",
        ),
        commit_row(
            commit_sha="2",
            short_sha="2",
            subject="Core: Add V4 location relativization utilities (#16174)",
            committer_date="2026-06-03T23:59:59+00:00",
            author_name="Anoop Johnson",
            top_level_paths="core",
            files_changed="8",
            insertions="250",
            pr_number="16174",
        ),
        commit_row(
            commit_sha="3",
            short_sha="3",
            subject="Docs: Fix typo (#16000)",
            committer_date="2026-05-14T23:59:59+00:00",
            author_name="Doc Writer",
            top_level_paths="docs",
            pr_number="16000",
        ),
    ]
    write_rows(input_path, rows)

    result = summarize_period(
        since=date(2026, 5, 13),
        until=date(2026, 6, 3),
        input_path=input_path,
        output_dir=output_dir,
        top=10,
    )

    assert result.candidate_count == 2
    assert result.selected_count == 2
    assert result.scored_csv_path == (
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_scored.csv"
    )
    assert result.markdown_path == output_dir / "2026-05-13_to_2026-06-03" / "README.md"
    assert (output_dir / "README.md").read_text(encoding="utf-8") == (
        "# Iceberg Community Summaries\n"
        "\n"
        "Generated review-candidate summaries for Iceberg community sync meetings.\n"
        "\n"
        "- [2026-05-13_to_2026-06-03](2026-05-13_to_2026-06-03/)\n"
    )
    with result.scored_csv_path.open(newline="", encoding="utf-8") as csv_file:
        commit_shas = {row["commit_sha"] for row in csv.DictReader(csv_file)}
    assert commit_shas == {"1", "3"}


def test_summarize_period_writes_multiple_repo_sections(tmp_path: Path) -> None:
    input_dir = tmp_path / "commits"
    output_dir = tmp_path / "summaries"
    java_repo = RepoConfig(
        full_name="apache/iceberg",
        remote_url="https://example.test/iceberg.git",
        summary_heading="Java",
    )
    python_repo = RepoConfig(
        full_name="apache/iceberg-python",
        remote_url="https://example.test/iceberg-python.git",
        summary_heading="Python",
    )
    rust_repo = RepoConfig(
        full_name="apache/iceberg-rust",
        remote_url="https://example.test/iceberg-rust.git",
        summary_heading="Rust",
    )
    write_rows(
        input_dir / java_repo.csv_name,
        [
            commit_row(
                commit_sha="java1",
                short_sha="java1",
                subject="Core: Add REST feature (#101)",
                committer_date="2026-05-20T12:00:00+00:00",
                repository="apache/iceberg",
                author_name="Java Dev",
                top_level_paths="core",
                pr_number="101",
            ),
        ],
    )
    write_rows(
        input_dir / python_repo.csv_name,
        [
            commit_row(
                commit_sha="py1",
                short_sha="py1",
                subject="Catalog: Add namespace support (#202)",
                committer_date="2026-05-21T12:00:00+00:00",
                repository="apache/iceberg-python",
                author_name="Python Dev",
                top_level_paths="pyiceberg",
                pr_number="202",
            ),
        ],
    )
    write_rows(
        input_dir / rust_repo.csv_name,
        [
            commit_row(
                commit_sha="rust1",
                short_sha="rust1",
                subject="REST: Add catalog auth support (#303)",
                committer_date="2026-05-22T12:00:00+00:00",
                repository="apache/iceberg-rust",
                author_name="Rust Dev",
                top_level_paths="crates",
                pr_number="303",
            ),
        ],
    )

    result = summarize_period(
        since=date(2026, 5, 13),
        until=date(2026, 6, 3),
        input_dir=input_dir,
        output_dir=output_dir,
        top=20,
        repositories=(java_repo, python_repo, rust_repo),
    )

    assert result.candidate_count == 3
    assert result.selected_count == 3
    assert result.scored_csv_paths == (
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_scored.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_python_scored.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_rust_scored.csv",
    )
    markdown = result.markdown_path.read_text(encoding="utf-8")
    assert "## apache/iceberg\n\n### Java" in markdown
    assert "- Core: Add REST feature (#101) (Thanks Java Dev!)" in markdown
    assert "## apache/iceberg-python\n\n### Python" in markdown
    assert "- Catalog: Add namespace support (#202) (Thanks Python Dev!)" in markdown
    assert "## apache/iceberg-rust\n\n### Rust" in markdown
    assert "- REST: Add catalog auth support (#303) (Thanks Rust Dev!)" in markdown


def commit_row(**overrides: str) -> dict[str, str]:
    row = {field: "" for field in CSV_FIELDS}
    row.update(
        {
            "repository": "apache/iceberg",
            "commit_sha": "abcdef",
            "short_sha": "abcdef",
            "author_name": "Author",
            "author_email": "author@example.com",
            "author_date": "2026-06-01T12:00:00+00:00",
            "committer_name": "GitHub",
            "committer_email": "noreply@github.com",
            "committer_date": "2026-06-01T12:00:00+00:00",
            "subject": "Core: Add feature (#1)",
            "body": "",
            "parents": "parent",
            "pr_number": "1",
            "is_merge_commit": "false",
            "co_authors": "",
            "files_changed": "1",
            "insertions": "1",
            "deletions": "0",
            "top_level_paths": "core",
        }
    )
    row.update(overrides)
    return row


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
