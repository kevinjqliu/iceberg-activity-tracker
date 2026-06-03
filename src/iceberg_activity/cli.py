from __future__ import annotations

import argparse
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from .collector import collect_repository
from .config import TARGET_REPOSITORIES

DEFAULT_LOOKBACK_DAYS = 45


def parse_iso_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"expected YYYY-MM-DD, got {value!r}") from exc


def default_until() -> date:
    return datetime.now(UTC).date()


def resolve_date_range(since: date | None, until: date | None) -> tuple[date, date]:
    resolved_until = until or default_until()
    resolved_since = since or (resolved_until - timedelta(days=DEFAULT_LOOKBACK_DAYS))
    if resolved_since > resolved_until:
        raise ValueError("--since must be on or before --until")
    return resolved_since, resolved_until


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="iceberg-activity",
        description="Collect Apache Iceberg commit activity into CSV files.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    collect = subparsers.add_parser("collect", help="Collect commit activity")
    collect.add_argument("--since", type=parse_iso_date, help="Start date, inclusive")
    collect.add_argument("--until", type=parse_iso_date, help="End date, inclusive")
    collect.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/commits"),
        help="Directory for generated CSV files",
    )
    collect.add_argument(
        "--cache-dir",
        type=Path,
        default=Path(".cache/repos"),
        help="Directory for local bare git repository caches",
    )
    return parser


def run_collect(args: argparse.Namespace) -> int:
    try:
        since, until = resolve_date_range(args.since, args.until)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    for repo in TARGET_REPOSITORIES:
        result = collect_repository(
            repo,
            since=since,
            until=until,
            cache_dir=args.cache_dir,
            output_dir=args.output_dir,
        )
        print(f"{result.repository}: wrote {result.commit_count} commits to {result.output_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "collect":
        return run_collect(args)
    parser.error(f"unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
