from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .config import RepoConfig
from .git_client import CSV_FIELDS, CommitRecord, fetch_recent_commits, read_commits


@dataclass(frozen=True)
class CollectionResult:
    repository: str
    output_path: Path
    commit_count: int


def write_commits_csv(commits: list[CommitRecord], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for commit in commits:
            writer.writerow(commit.as_csv_row())


def collect_repository(
    repo: RepoConfig,
    *,
    since: date,
    until: date,
    cache_dir: Path,
    output_dir: Path,
) -> CollectionResult:
    git_dir = fetch_recent_commits(repo, cache_dir, since)
    commits = read_commits(repo, git_dir, since, until)
    output_path = output_dir / repo.csv_name
    write_commits_csv(commits, output_path)
    return CollectionResult(
        repository=repo.full_name,
        output_path=output_path,
        commit_count=len(commits),
    )
