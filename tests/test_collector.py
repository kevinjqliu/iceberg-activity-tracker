from __future__ import annotations

import csv
import os
import subprocess
from datetime import date
from pathlib import Path

from iceberg_activity.collector import collect_repository, write_commits_csv
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
