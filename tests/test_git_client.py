from __future__ import annotations

import os
import subprocess
from pathlib import Path

from iceberg_activity.git_client import (
    FIELD_SEPARATOR,
    RECORD_SEPARATOR,
    git_log_format,
    parse_git_log,
    parse_co_authors,
    parse_pr_number,
    read_commit_stats,
    is_shallow_boundary,
    top_level_path,
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


def test_parse_pr_number_and_co_authors() -> None:
    assert parse_pr_number("Core: Add manifest support (#12345)") == "12345"
    assert parse_pr_number("Core: Add manifest support") == ""

    body = """Detailed body

Co-authored-by: Alice Example <alice@example.com>
Co-authored-by: Bob Example <bob@example.com>
Co-authored-by: Alice Example <alice@example.com>
"""
    assert parse_co_authors(body) == "Alice Example; Bob Example"


def test_top_level_path_handles_common_paths() -> None:
    assert top_level_path("core/src/main/java/File.java") == "core"
    assert top_level_path(".github/workflows/ci.yml") == ".github"
    assert top_level_path("README.md") == "README.md"


def test_is_shallow_boundary_reads_git_shallow_file(tmp_path: Path) -> None:
    git_dir = tmp_path / "repo.git"
    git_dir.mkdir()
    sha = "abc123"
    (git_dir / "shallow").write_text(f"{sha}\n", encoding="utf-8")

    assert is_shallow_boundary(git_dir, sha)
    assert not is_shallow_boundary(git_dir, "def456")


def test_read_commit_stats_from_local_git_fixture(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    run(["git", "init", "-b", "main", str(repo)])
    run(["git", "config", "user.name", "Test User"], cwd=repo)
    run(["git", "config", "user.email", "test@example.com"], cwd=repo)

    write_commit(repo, "core/file.txt", "one\n", "Initial core")
    write_commit(repo, "spark/file.txt", "one\ntwo\n", "Add spark")
    sha = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()

    stats = read_commit_stats(repo / ".git", sha)

    assert stats["files_changed"] == "1"
    assert stats["insertions"] == "2"
    assert stats["deletions"] == "0"
    assert stats["top_level_paths"] == "spark"


def write_commit(repo: Path, relative_path: str, content: str, subject: str) -> None:
    path = repo / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    run(["git", "add", relative_path], cwd=repo)
    env = {
        **os.environ,
        "GIT_AUTHOR_DATE": "2026-06-01T12:00:00+00:00",
        "GIT_COMMITTER_DATE": "2026-06-01T12:00:00+00:00",
    }
    run(["git", "commit", "-m", subject], cwd=repo, env=env)


def run(
    args: list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        env=env,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
