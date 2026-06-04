from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import pytest

from iceberg_activity.config import RepoConfig
from iceberg_activity.git_client import CSV_FIELDS
from iceberg_activity.summarizer import (
    THEME_FIELDS,
    build_theme_rows,
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
    build_bump = commit_row(
        repository="apache/iceberg-python",
        subject="Build: Bump idna from 3.11 to 3.15 (#3386)",
        body="Mentions views in dependency release notes.",
        author_name="dependabot[bot]",
        co_authors="dependabot[bot]",
        pr_number="3386",
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
    build_bump_score, build_bump_reasons = score_commit(build_bump)
    publishing_score, publishing_reasons = score_commit(publishing_fix)
    correctness_score, correctness_reasons = score_commit(correctness_fix)
    storage_score, storage_reasons = score_commit(storage_update)

    assert "downrank dependency bump" in dependency_reasons
    assert "downrank dependency bump" in build_bump_reasons
    assert "publishing/release signal" in publishing_reasons
    assert "correctness signal" in correctness_reasons
    assert "strategic: opendal, storage" in storage_reasons
    assert publishing_score > dependency_score
    assert correctness_score > dependency_score
    assert storage_score > dependency_score
    assert storage_score > build_bump_score


def test_score_commit_boosts_go_summary_signals() -> None:
    rewrite = commit_row(
        repository="apache/iceberg-go",
        subject="feat(table): add RewriteDataFiles for compaction execution (#892)",
        body="Add Transaction.RewriteDataFiles for table compaction.",
        top_level_paths="table",
        pr_number="892",
    )
    deletion_vector = commit_row(
        repository="apache/iceberg-go",
        subject="feat: Deletion vector reader (#866)",
        files_changed="16",
        insertions="944",
        deletions="4",
        top_level_paths="go.mod; go.sum; manifest.go; table",
        pr_number="866",
    )
    clustered_write = commit_row(
        repository="apache/iceberg-go",
        subject="feat(table): clustered partitioned write path (#948)",
        top_level_paths="table",
        insertions="1041",
        pr_number="948",
    )
    maintenance_cli = commit_row(
        repository="apache/iceberg-go",
        subject="feat(cli): add maintenance command wiring and stubs (#1073)",
        top_level_paths="cmd",
        files_changed="10",
        pr_number="1073",
    )
    golden_test = commit_row(
        repository="apache/iceberg-go",
        subject="test(puffin): golden round-trip a deletion-vector-v1 blob (#1041)",
        top_level_paths="puffin",
        pr_number="1041",
    )

    rewrite_score, rewrite_reasons = score_commit(rewrite)
    deletion_score, deletion_reasons = score_commit(deletion_vector)
    clustered_score, clustered_reasons = score_commit(clustered_write)
    cli_score, cli_reasons = score_commit(maintenance_cli)
    test_score, test_reasons = score_commit(golden_test)

    assert "important area: table" in rewrite_reasons
    assert "strategic: compaction, rewritedatafiles" in rewrite_reasons
    assert "strategic: deletion vector" in deletion_reasons
    assert "deletion vector signal" in deletion_reasons
    assert "strategic: clustered" in clustered_reasons
    assert "important area: cli" in cli_reasons
    assert "strategic: maintenance" in cli_reasons
    assert "validation/regression test signal" in test_reasons
    assert "downrank docs/tests/benchmarks" not in test_reasons
    assert rewrite_score > 60
    assert deletion_score > 50
    assert clustered_score > 50
    assert cli_score > 60
    assert test_score > 40


def test_summary_bullet_formats_thanks() -> None:
    row = commit_row(
        subject="Spark: Add feature (#123)",
        author_name="Alice",
        co_authors="Bob; Carol",
    )

    assert summary_bullet(row) == "- Spark: Add feature (#123) (Thanks Alice, Bob, and Carol!)"


def test_build_theme_rows_groups_python_rest_pagination() -> None:
    rows = [
        scored_commit_row(
            commit_sha="3347",
            short_sha="3347",
            repository="apache/iceberg-python",
            subject="REST: Add pagination support for list_namespaces (#3347)",
            author_name="Yuya Ebihara",
            co_authors="Kevin Liu",
            pr_number="3347",
            score="88",
        ),
        scored_commit_row(
            commit_sha="3348",
            short_sha="3348",
            repository="apache/iceberg-python",
            subject="REST: Add pagination support for list_tables (#3348)",
            author_name="Yuya Ebihara",
            co_authors="Kevin Liu",
            pr_number="3348",
            score="89",
        ),
        scored_commit_row(
            commit_sha="3349",
            short_sha="3349",
            repository="apache/iceberg-python",
            subject="REST: Add pagination support for `list_views` (#3349)",
            author_name="Yuya Ebihara",
            pr_number="3349",
            score="86",
        ),
        scored_commit_row(
            commit_sha="3377",
            short_sha="3377",
            repository="apache/iceberg-python",
            subject="REST: Add support for page-size in list_namespaces, list_tables, and list_views (#3377)",
            author_name="Yuya Ebihara",
            pr_number="3377",
            score="88",
        ),
        scored_commit_row(
            commit_sha="3335",
            short_sha="3335",
            repository="apache/iceberg-python",
            subject="Support `pa.RecordBatchReader` in Table.`{append,overwrite}` (#3335)",
            body="Ready for review. Mentions FileIO in a checklist.",
            author_name="Paul Mathew",
            pr_number="3335",
            score="90",
        ),
        scored_commit_row(
            commit_sha="3386",
            short_sha="3386",
            repository="apache/iceberg-python",
            subject="Build: Bump idna from 3.11 to 3.15 (#3386)",
            body="Mentions list_views in dependency release notes.",
            author_name="dependabot[bot]",
            co_authors="dependabot[bot]",
            pr_number="3386",
            score="20",
        ),
    ]

    themes = build_theme_rows(rows)
    pagination_theme = next(row for row in themes if row["theme_key"] == "rest-pagination")

    assert len(themes) == 3
    assert {row["theme_key"] for row in themes} == {
        "rest-pagination",
        "commit:3335",
        "commit:3386",
    }
    assert pagination_theme["theme_score"] == "113"
    assert pagination_theme["commit_count"] == "4"
    assert pagination_theme["pr_numbers"] == "3347; 3348; 3349; 3377"
    assert pagination_theme["contributors"] == "Yuya Ebihara; Kevin Liu"
    assert pagination_theme["summary_bullet"] == (
        "- REST pagination: add pagination and page-size support for namespaces, "
        "tables, and views (#3347, #3348, #3349, #3377) "
        "(Thanks Yuya Ebihara and Kevin Liu!)"
    )


def test_build_theme_rows_preserves_single_commit_fallback() -> None:
    row = scored_commit_row(
        commit_sha="solo",
        subject="Spark: Add feature (#123)",
        author_name="Alice",
        co_authors="Bob; Carol",
        pr_number="123",
        score="42",
    )

    themes = build_theme_rows([row])

    assert themes == [
        {
            "repository": "apache/iceberg",
            "theme_key": "commit:solo",
            "theme_title": "Spark: Add feature (#123)",
            "theme_score": "42",
            "commit_count": "1",
            "pr_numbers": "123",
            "commit_shas": "solo",
            "contributors": "Alice; Bob; Carol",
            "subjects": "Spark: Add feature (#123)",
            "summary_bullet": "- Spark: Add feature (#123) (Thanks Alice, Bob, and Carol!)",
            "newest_committer_date": "2026-06-01T12:00:00+00:00",
        }
    ]


def test_build_theme_rows_preserves_single_rule_match_as_commit() -> None:
    row = scored_commit_row(
        commit_sha="cli1",
        subject="feat(cli): add maintenance command wiring and stubs (#1073)",
        author_name="Go Dev",
        pr_number="1073",
        score="75",
    )

    themes = build_theme_rows([row])

    assert themes[0]["theme_key"] == "commit:cli1"
    assert themes[0]["theme_title"] == "feat(cli): add maintenance command wiring and stubs (#1073)"
    assert themes[0]["commit_count"] == "1"
    assert themes[0]["summary_bullet"] == (
        "- feat(cli): add maintenance command wiring and stubs (#1073) (Thanks Go Dev!)"
    )


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
    assert result.theme_csv_path == output_dir / "2026-06" / "apache_iceberg_themes.csv"
    with result.scored_csv_path.open(newline="", encoding="utf-8") as csv_file:
        scored = list(csv.DictReader(csv_file))
    assert len(scored) == 2
    assert scored[0]["score"]
    assert scored[0]["heuristic_score"]
    assert scored[0]["lancedb_score"]
    assert scored[0]["lancedb_match"]
    assert scored[0]["score_reasons"]
    with result.theme_csv_path.open(newline="", encoding="utf-8") as csv_file:
        theme_reader = csv.DictReader(csv_file)
        themes = list(theme_reader)
    assert theme_reader.fieldnames == THEME_FIELDS
    assert len(themes) == 2
    assert themes[0]["summary_bullet"]

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
        "_Top 1 themes from 2 scored commits._\n"
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
    assert result.theme_csv_path == (
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_themes.csv"
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
    go_repo = RepoConfig(
        full_name="apache/iceberg-go",
        remote_url="https://example.test/iceberg-go.git",
        summary_heading="Go",
    )
    cpp_repo = RepoConfig(
        full_name="apache/iceberg-cpp",
        remote_url="https://example.test/iceberg-cpp.git",
        summary_heading="C++",
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
    write_rows(
        input_dir / go_repo.csv_name,
        [
            commit_row(
                commit_sha="go1",
                short_sha="go1",
                subject="Catalog: Add maintenance CLI support (#404)",
                committer_date="2026-05-23T12:00:00+00:00",
                repository="apache/iceberg-go",
                author_name="Go Dev",
                top_level_paths="cmd; catalog",
                pr_number="404",
            ),
        ],
    )
    write_rows(
        input_dir / cpp_repo.csv_name,
        [
            commit_row(
                commit_sha="cpp1",
                short_sha="cpp1",
                subject="REST: Add namespace separator support (#505)",
                committer_date="2026-05-24T12:00:00+00:00",
                repository="apache/iceberg-cpp",
                author_name="Cpp Dev",
                top_level_paths="src; include",
                pr_number="505",
            ),
        ],
    )

    result = summarize_period(
        since=date(2026, 5, 13),
        until=date(2026, 6, 3),
        input_dir=input_dir,
        output_dir=output_dir,
        top=20,
        repositories=(java_repo, python_repo, rust_repo, go_repo, cpp_repo),
    )

    assert result.candidate_count == 5
    assert result.selected_count == 5
    assert result.scored_csv_paths == (
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_scored.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_python_scored.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_rust_scored.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_go_scored.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_cpp_scored.csv",
    )
    assert result.theme_csv_paths == (
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_themes.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_python_themes.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_rust_themes.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_go_themes.csv",
        output_dir / "2026-05-13_to_2026-06-03" / "apache_iceberg_cpp_themes.csv",
    )
    markdown = result.markdown_path.read_text(encoding="utf-8")
    assert "## apache/iceberg\n\n### Java" in markdown
    assert "- Core: Add REST feature (#101) (Thanks Java Dev!)" in markdown
    assert "## apache/iceberg-python\n\n### Python" in markdown
    assert "- Catalog: Add namespace support (#202) (Thanks Python Dev!)" in markdown
    assert "## apache/iceberg-rust\n\n### Rust" in markdown
    assert "- REST: Add catalog auth support (#303) (Thanks Rust Dev!)" in markdown
    assert "## apache/iceberg-go\n\n### Go" in markdown
    assert "- Catalog: Add maintenance CLI support (#404) (Thanks Go Dev!)" in markdown
    assert "## apache/iceberg-cpp\n\n### C++" in markdown
    assert "- REST: Add namespace separator support (#505) (Thanks Cpp Dev!)" in markdown


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


def scored_commit_row(**overrides: str) -> dict[str, str]:
    row = commit_row(**overrides)
    row.setdefault("score", "10")
    row.setdefault("summary_bullet", summary_bullet(row))
    return row


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
