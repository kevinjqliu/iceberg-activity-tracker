from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class RepoConfig:
    full_name: str
    remote_url: str
    default_branch: str = "main"
    summary_heading: str = "Highlights"

    @property
    def cache_name(self) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "_", self.full_name).strip("_")

    @property
    def csv_name(self) -> str:
        return f"{self.cache_name}.csv"


TARGET_REPOSITORIES: tuple[RepoConfig, ...] = (
    RepoConfig(
        full_name="apache/iceberg",
        remote_url="https://github.com/apache/iceberg.git",
        summary_heading="Java",
    ),
    RepoConfig(
        full_name="apache/iceberg-python",
        remote_url="https://github.com/apache/iceberg-python.git",
        summary_heading="Python",
    ),
    RepoConfig(
        full_name="apache/iceberg-rust",
        remote_url="https://github.com/apache/iceberg-rust.git",
        summary_heading="Rust",
    ),
)
