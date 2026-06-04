from __future__ import annotations

import argparse
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from .collector import collect_repository
from .config import TARGET_REPOSITORIES
from .summarizer import summarize_month

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

    summarize = subparsers.add_parser("summarize", help="Create a monthly Java summary")
    summarize.add_argument("--month", required=True, help="Month to summarize, as YYYY-MM")
    summarize.add_argument(
        "--input",
        type=Path,
        default=Path("data/commits/apache_iceberg.csv"),
        help="Commit CSV to summarize",
    )
    summarize.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/summaries"),
        help="Directory for generated summary files",
    )
    summarize.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of top commits to include in markdown",
    )
    summarize.add_argument(
        "--notes",
        type=Path,
        default=Path("Iceberg Community Sync Notes.md"),
        help="Community notes file used to build a LanceDB ranking index when present",
    )
    summarize.add_argument(
        "--lancedb-dir",
        type=Path,
        default=Path(".cache/lancedb"),
        help="Directory for the local LanceDB ranking index",
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


def run_summarize(args: argparse.Namespace) -> int:
    if args.top < 1:
        raise SystemExit("--top must be at least 1")
    try:
        result = summarize_month(
            month=args.month,
            input_path=args.input,
            output_dir=args.output_dir,
            top=args.top,
            notes_path=args.notes,
            lancedb_dir=args.lancedb_dir,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    print(
        f"scored {result.candidate_count} commits and wrote {result.selected_count} "
        f"highlights to {result.markdown_path}"
    )
    print(f"scored CSV: {result.scored_csv_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "collect":
        return run_collect(args)
    if args.command == "summarize":
        return run_summarize(args)
    parser.error(f"unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
