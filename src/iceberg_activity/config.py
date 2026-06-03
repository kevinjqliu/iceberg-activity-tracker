from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RepoConfig:
    full_name: str
    remote_url: str
    default_branch: str = "main"

    @property
    def cache_name(self) -> str:
        return self.full_name.replace("/", "_")

    @property
    def csv_name(self) -> str:
        return f"{self.cache_name}.csv"


TARGET_REPOSITORIES: tuple[RepoConfig, ...] = (
    RepoConfig(
        full_name="apache/iceberg",
        remote_url="https://github.com/apache/iceberg.git",
    ),
)
