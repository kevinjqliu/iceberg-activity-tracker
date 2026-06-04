from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

from .config import RepoConfig
from .git_client import CSV_FIELDS, CommitRecord, fetch_recent_commits, read_commits


@dataclass(frozen=True)
class CollectionResult:
    repository: str
    output_path: Path
    commit_count: int


def write_commits_csv(commits: list[CommitRecord], output_path: Path) -> None:
    write_commit_rows([commit.as_csv_row() for commit in commits], output_path)


def write_commit_rows(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: clean_csv_value(row.get(field, "")) for field in CSV_FIELDS})


def clean_csv_value(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines())


def read_commit_rows(input_path: Path) -> list[dict[str, str]]:
    if not input_path.exists():
        return []
    with input_path.open(newline="", encoding="utf-8") as csv_file:
        return [
            {field: row.get(field, "") for field in CSV_FIELDS}
            for row in csv.DictReader(csv_file)
        ]


def has_sparse_boundary_metadata(row: dict[str, str]) -> bool:
    return (
        not row.get("parents")
        and row.get("files_changed", "0") == "0"
        and row.get("insertions", "0") == "0"
        and row.get("deletions", "0") == "0"
        and not row.get("top_level_paths")
    )


def merge_commit_rows(
    existing_rows: list[dict[str, str]],
    collected_commits: list[CommitRecord],
) -> list[dict[str, str]]:
    merged_by_sha: dict[str, dict[str, str]] = {
        row["commit_sha"]: row
        for row in existing_rows
        if row.get("commit_sha")
    }

    for commit in collected_commits:
        new_row = commit.as_csv_row()
        existing_row = merged_by_sha.get(commit.commit_sha)
        if (
            existing_row is not None
            and has_sparse_boundary_metadata(new_row)
            and not has_sparse_boundary_metadata(existing_row)
        ):
            continue
        merged_by_sha[commit.commit_sha] = new_row

    return sorted(
        merged_by_sha.values(),
        key=lambda row: (datetime.fromisoformat(row["committer_date"]), row["commit_sha"]),
    )


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
    merged_rows = merge_commit_rows(read_commit_rows(output_path), commits)
    write_commit_rows(merged_rows, output_path)
    return CollectionResult(
        repository=repo.full_name,
        output_path=output_path,
        commit_count=len(merged_rows),
    )
