from __future__ import annotations

import csv
import os
import subprocess
from datetime import date
from pathlib import Path

from iceberg_activity.collector import collect_repository, merge_commit_rows, write_commits_csv
from iceberg_activity.config import RepoConfig
from iceberg_activity.git_client import CSV_FIELDS, CommitRecord


def test_write_commits_csv_writes_headers_and_rows(tmp_path: Path) -> None:
    output_path = tmp_path / "apache_iceberg.csv"
    commit = CommitRecord(
        repository="apache/iceberg",
        commit_sha="abcdef1234567890",
        short_sha="abcdef1",
        author_name="Author",
        author_email="author@example.com",
        author_date="2026-05-01T12:00:00+00:00",
        committer_name="Committer",
        committer_email="committer@example.com",
        committer_date="2026-05-01T12:01:00+00:00",
        subject="Add table update",
        body="Detailed body",
        parents="parent1",
    )

    write_commits_csv([commit], output_path)

    with output_path.open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert rows == [commit.as_csv_row()]
    assert list(rows[0].keys()) == CSV_FIELDS


def test_merge_commit_rows_preserves_existing_history() -> None:
    older = commit_record(
        commit_sha="old1234567890",
        short_sha="old1234",
        committer_date="2026-04-01T12:00:00+00:00",
        subject="Older commit",
    ).as_csv_row()
    newer = commit_record(
        commit_sha="new1234567890",
        short_sha="new1234",
        committer_date="2026-05-10T12:00:00+00:00",
        subject="Newer commit",
    )

    rows = merge_commit_rows([older], [newer])

    assert [row["short_sha"] for row in rows] == ["old1234", "new1234"]


def test_merge_commit_rows_replaces_existing_row_with_new_metadata_for_duplicate_sha() -> None:
    existing = commit_record(
        commit_sha="same1234567890",
        short_sha="same123",
        subject="Original subject",
        parents="parent1",
        files_changed="3",
        insertions="10",
        deletions="2",
        top_level_paths="core; spark",
    ).as_csv_row()
    duplicate = commit_record(
        commit_sha="same1234567890",
        short_sha="same123",
        subject="Different subject",
        parents="parent2",
        files_changed="4",
        insertions="20",
        deletions="5",
        top_level_paths="api",
    )

    rows = merge_commit_rows([existing], [duplicate])

    assert rows[0]["subject"] == "Different subject"
    assert rows[0]["parents"] == "parent2"
    assert rows[0]["files_changed"] == "4"
    assert rows[0]["top_level_paths"] == "api"


def test_merge_commit_rows_keeps_complete_metadata_over_sparse_boundary_row() -> None:
    existing = commit_record(
        commit_sha="same1234567890",
        short_sha="same123",
        parents="parent1",
        files_changed="3",
        insertions="10",
        deletions="2",
        top_level_paths="core; spark",
    ).as_csv_row()
    sparse_boundary = commit_record(
        commit_sha="same1234567890",
        short_sha="same123",
        parents="",
        files_changed="0",
        insertions="0",
        deletions="0",
        top_level_paths="",
    )

    rows = merge_commit_rows([existing], [sparse_boundary])

    assert rows[0]["parents"] == "parent1"
    assert rows[0]["files_changed"] == "3"
    assert rows[0]["top_level_paths"] == "core; spark"


def test_merge_commit_rows_sorts_missing_backfill_into_history() -> None:
    later = commit_record(
        commit_sha="later1234567890",
        short_sha="later12",
        committer_date="2026-05-10T12:00:00+00:00",
        subject="Later commit",
    ).as_csv_row()
    backfilled = commit_record(
        commit_sha="backfill1234567890",
        short_sha="backfil",
        committer_date="2026-04-15T12:00:00+00:00",
        subject="Backfilled commit",
    )

    rows = merge_commit_rows([later], [backfilled])

    assert [row["short_sha"] for row in rows] == ["backfil", "later12"]


def test_collect_repository_from_local_git_fixture(tmp_path: Path) -> None:
    work_repo = tmp_path / "work"
    remote_repo = tmp_path / "remote.git"
    cache_dir = tmp_path / "cache"
    output_dir = tmp_path / "out"

    run(["git", "init", "-b", "main", str(work_repo)])
    run(["git", "config", "user.name", "Test User"], cwd=work_repo)
    run(["git", "config", "user.email", "test@example.com"], cwd=work_repo)

    commit_file(work_repo, "old.txt", "old\n", "Old commit", "2026-04-01T12:00:00+00:00")
    commit_file(
        work_repo,
        "recent.txt",
        "recent\n",
        "Recent commit",
        "2026-05-10T12:00:00+00:00",
        body="Body line one\n\nBody line two",
    )

    run(["git", "clone", "--bare", str(work_repo), str(remote_repo)])

    repo = RepoConfig(
        full_name="example/repo",
        remote_url=str(remote_repo),
        default_branch="main",
    )

    result = collect_repository(
        repo,
        since=date(2026, 5, 1),
        until=date(2026, 5, 31),
        cache_dir=cache_dir,
        output_dir=output_dir,
    )

    assert result.commit_count == 1
    assert result.output_path == output_dir / "example_repo.csv"

    with result.output_path.open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert len(rows) == 1
    assert rows[0]["repository"] == "example/repo"
    assert rows[0]["subject"] == "Recent commit"
    assert rows[0]["body"] == "Body line one\n\nBody line two"


def commit_record(
    *,
    commit_sha: str,
    short_sha: str,
    committer_date: str = "2026-05-01T12:00:00+00:00",
    subject: str = "Commit subject",
    parents: str = "parent1",
    files_changed: str = "1",
    insertions: str = "1",
    deletions: str = "0",
    top_level_paths: str = "core",
) -> CommitRecord:
    return CommitRecord(
        repository="apache/iceberg",
        commit_sha=commit_sha,
        short_sha=short_sha,
        author_name="Author",
        author_email="author@example.com",
        author_date=committer_date,
        committer_name="Committer",
        committer_email="committer@example.com",
        committer_date=committer_date,
        subject=subject,
        body="",
        parents=parents,
        files_changed=files_changed,
        insertions=insertions,
        deletions=deletions,
        top_level_paths=top_level_paths,
    )


def commit_file(
    repo: Path,
    relative_path: str,
    content: str,
    subject: str,
    timestamp: str,
    *,
    body: str = "",
) -> None:
    path = repo / relative_path
    path.write_text(content, encoding="utf-8")
    run(["git", "add", relative_path], cwd=repo)
    message_args = ["-m", subject]
    if body:
        message_args.extend(["-m", body])
    env = {
        **os.environ,
        "GIT_AUTHOR_DATE": timestamp,
        "GIT_COMMITTER_DATE": timestamp,
    }
    run(["git", "commit", *message_args], cwd=repo, env=env)


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
