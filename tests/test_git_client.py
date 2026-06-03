from __future__ import annotations

from iceberg_activity.git_client import (
    FIELD_SEPARATOR,
    RECORD_SEPARATOR,
    git_log_format,
    parse_git_log,
)


def test_git_log_format_contains_expected_placeholders() -> None:
    fmt = git_log_format()

    assert "%H" in fmt
    assert "%P" in fmt
    assert fmt.endswith(RECORD_SEPARATOR)


def test_parse_git_log_handles_merge_commit_and_multiline_body() -> None:
    record = FIELD_SEPARATOR.join(
        [
            "abcdef1234567890",
            "abcdef1",
            "Author Name",
            "author@example.com",
            "2026-05-01T12:00:00+00:00",
            "Committer Name",
            "committer@example.com",
            "2026-05-01T12:01:00+00:00",
            "Merge branch feature",
            "First body line\n\nSecond body line",
            "parent1 parent2",
        ]
    )

    commits = parse_git_log(record + RECORD_SEPARATOR + "\n", "apache/iceberg")

    assert len(commits) == 1
    assert commits[0].repository == "apache/iceberg"
    assert commits[0].subject == "Merge branch feature"
    assert commits[0].body == "First body line\n\nSecond body line"
    assert commits[0].parents == "parent1 parent2"


def test_parse_git_log_rejects_malformed_record() -> None:
    try:
        parse_git_log("only-one-field" + RECORD_SEPARATOR, "apache/iceberg")
    except ValueError as exc:
        assert "Expected 11 fields" in str(exc)
    else:
        raise AssertionError("malformed git log record should fail")
