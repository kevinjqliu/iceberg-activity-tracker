from __future__ import annotations

import subprocess
from dataclasses import dataclass
from datetime import date, time
from pathlib import Path

from .config import RepoConfig

FIELD_SEPARATOR = "\x1f"
RECORD_SEPARATOR = "\x1e"


class GitCommandError(RuntimeError):
    """Raised when a git subprocess exits unsuccessfully."""


@dataclass(frozen=True)
class CommitRecord:
    repository: str
    commit_sha: str
    short_sha: str
    author_name: str
    author_email: str
    author_date: str
    committer_name: str
    committer_email: str
    committer_date: str
    subject: str
    body: str
    parents: str

    def as_csv_row(self) -> dict[str, str]:
        return {
            "repository": self.repository,
            "commit_sha": self.commit_sha,
            "short_sha": self.short_sha,
            "author_name": self.author_name,
            "author_email": self.author_email,
            "author_date": self.author_date,
            "committer_name": self.committer_name,
            "committer_email": self.committer_email,
            "committer_date": self.committer_date,
            "subject": self.subject,
            "body": self.body,
            "parents": self.parents,
        }


CSV_FIELDS = list(CommitRecord.__dataclass_fields__)


def run_git(args: list[str], *, git_dir: Path | None = None, cwd: Path | None = None) -> str:
    command = ["git"]
    if git_dir is not None:
        command.extend(["--git-dir", str(git_dir)])
    command.extend(args)

    completed = subprocess.run(
        command,
        cwd=cwd,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise GitCommandError(f"{' '.join(command)} failed: {detail}")
    return completed.stdout


def ensure_bare_cache(repo: RepoConfig, cache_dir: Path) -> Path:
    git_dir = cache_dir / repo.cache_name
    if not (git_dir / "HEAD").exists():
        git_dir.parent.mkdir(parents=True, exist_ok=True)
        run_git(["init", "--bare", str(git_dir)])

    try:
        existing_url = run_git(["remote", "get-url", "origin"], git_dir=git_dir).strip()
    except GitCommandError:
        run_git(["remote", "add", "origin", repo.remote_url], git_dir=git_dir)
    else:
        if existing_url != repo.remote_url:
            run_git(["remote", "set-url", "origin", repo.remote_url], git_dir=git_dir)

    run_git(["config", "remote.origin.promisor", "true"], git_dir=git_dir)
    run_git(["config", "remote.origin.partialclonefilter", "blob:none"], git_dir=git_dir)
    return git_dir


def fetch_recent_commits(repo: RepoConfig, cache_dir: Path, since: date) -> Path:
    git_dir = ensure_bare_cache(repo, cache_dir)
    refspec = f"+refs/heads/{repo.default_branch}:refs/remotes/origin/{repo.default_branch}"
    run_git(
        [
            "fetch",
            "--filter=blob:none",
            "--no-tags",
            "--prune",
            f"--shallow-since={since.isoformat()}",
            "origin",
            refspec,
        ],
        git_dir=git_dir,
    )
    return git_dir


def iso_start(day: date) -> str:
    return f"{day.isoformat()}T{time.min.isoformat()}+00:00"


def iso_end(day: date) -> str:
    return f"{day.isoformat()}T{time.max.isoformat()}+00:00"


def git_log_format() -> str:
    fields = [
        "%H",
        "%h",
        "%an",
        "%ae",
        "%aI",
        "%cn",
        "%ce",
        "%cI",
        "%s",
        "%b",
        "%P",
    ]
    return FIELD_SEPARATOR.join(fields) + RECORD_SEPARATOR


def parse_git_log(output: str, repository: str) -> list[CommitRecord]:
    commits: list[CommitRecord] = []
    for raw_record in output.split(RECORD_SEPARATOR):
        record = raw_record.strip("\n")
        if not record:
            continue
        parts = record.split(FIELD_SEPARATOR)
        if len(parts) != 11:
            raise ValueError(
                f"Expected 11 fields in git log record for {repository}, found {len(parts)}"
            )
        commits.append(
            CommitRecord(
                repository=repository,
                commit_sha=parts[0],
                short_sha=parts[1],
                author_name=parts[2],
                author_email=parts[3],
                author_date=parts[4],
                committer_name=parts[5],
                committer_email=parts[6],
                committer_date=parts[7],
                subject=parts[8],
                body=parts[9].strip(),
                parents=parts[10],
            )
        )
    return commits


def read_commits(repo: RepoConfig, git_dir: Path, since: date, until: date) -> list[CommitRecord]:
    ref_name = f"refs/remotes/origin/{repo.default_branch}"
    output = run_git(
        [
            "log",
            ref_name,
            "--reverse",
            f"--since={iso_start(since)}",
            f"--until={iso_end(until)}",
            f"--format={git_log_format()}",
        ],
        git_dir=git_dir,
    )
    return parse_git_log(output, repo.full_name)
