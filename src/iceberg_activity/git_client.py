from __future__ import annotations

import subprocess
import re
from dataclasses import dataclass, replace
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
    pr_number: str = ""
    is_merge_commit: str = "false"
    co_authors: str = ""
    files_changed: str = "0"
    insertions: str = "0"
    deletions: str = "0"
    top_level_paths: str = ""

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
            "pr_number": self.pr_number,
            "is_merge_commit": self.is_merge_commit,
            "co_authors": self.co_authors,
            "files_changed": self.files_changed,
            "insertions": self.insertions,
            "deletions": self.deletions,
            "top_level_paths": self.top_level_paths,
        }


CSV_FIELDS = list(CommitRecord.__dataclass_fields__)
PR_NUMBER_RE = re.compile(r"\(#(\d+)\)\s*$")
CO_AUTHOR_RE = re.compile(r"^Co-authored-by:\s*(.*?)\s*<[^>]+>\s*$", re.IGNORECASE)


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


def parse_pr_number(subject: str) -> str:
    match = PR_NUMBER_RE.search(subject)
    return match.group(1) if match else ""


def parse_co_authors(body: str) -> str:
    co_authors: list[str] = []
    seen: set[str] = set()
    for line in body.splitlines():
        match = CO_AUTHOR_RE.match(line.strip())
        if not match:
            continue
        name = match.group(1).strip()
        if name and name not in seen:
            seen.add(name)
            co_authors.append(name)
    return "; ".join(co_authors)


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
                pr_number=parse_pr_number(parts[8]),
                is_merge_commit=str(len(parts[10].split()) > 1).lower(),
                co_authors=parse_co_authors(parts[9]),
            )
        )
    return commits


def top_level_path(path: str) -> str:
    normalized = path.strip()
    if " => " in normalized:
        normalized = normalized.split(" => ", 1)[1].rstrip("}")
        if "{" in normalized:
            prefix, suffix = normalized.split("{", 1)
            normalized = prefix + suffix
    normalized = normalized.strip("/")
    if not normalized:
        return "[root]"
    if normalized.startswith(".github/"):
        return ".github"
    return normalized.split("/", 1)[0]


def read_commit_stats(git_dir: Path, commit_sha: str) -> dict[str, str]:
    if is_shallow_boundary(git_dir, commit_sha) or has_missing_parent(git_dir, commit_sha):
        return {
            "files_changed": "0",
            "insertions": "0",
            "deletions": "0",
            "top_level_paths": "",
        }
    output = run_git(
        ["show", "--format=", "--numstat", "--find-renames", commit_sha],
        git_dir=git_dir,
    )
    files: set[str] = set()
    insertions = 0
    deletions = 0
    top_paths: set[str] = set()
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added, removed, path = parts[0], parts[1], parts[-1]
        files.add(path)
        top_paths.add(top_level_path(path))
        if added != "-":
            insertions += int(added)
        if removed != "-":
            deletions += int(removed)
    return {
        "files_changed": str(len(files)),
        "insertions": str(insertions),
        "deletions": str(deletions),
        "top_level_paths": "; ".join(sorted(top_paths)),
    }


def is_shallow_boundary(git_dir: Path, commit_sha: str) -> bool:
    shallow_path = git_dir / "shallow"
    if not shallow_path.exists():
        return False
    return commit_sha in {line.strip() for line in shallow_path.read_text(encoding="utf-8").splitlines()}


def has_missing_parent(git_dir: Path, commit_sha: str) -> bool:
    output = run_git(["rev-list", "--parents", "-n", "1", commit_sha], git_dir=git_dir)
    parents = output.strip().split()[1:]
    for parent in parents:
        completed = subprocess.run(
            ["git", "--git-dir", str(git_dir), "cat-file", "-e", f"{parent}^{{commit}}"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if completed.returncode != 0:
            return True
    return False


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
    commits = parse_git_log(output, repo.full_name)
    enriched: list[CommitRecord] = []
    for commit in commits:
        enriched.append(replace(commit, **read_commit_stats(git_dir, commit.commit_sha)))
    return enriched
