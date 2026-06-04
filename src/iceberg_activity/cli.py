from __future__ import annotations

import argparse
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from .backtester import backtest_java_highlights
from .collector import collect_repository
from .config import TARGET_REPOSITORIES
from .summarizer import summarize_month, summarize_period

DEFAULT_LOOKBACK_DAYS = 45
MEETING_INTERVAL_DAYS = 21


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


def resolve_summary_range(
    *,
    since: date | None,
    until: date | None,
    meeting_date: date | None,
) -> tuple[date, date]:
    if meeting_date and until and meeting_date != until:
        raise ValueError("--meeting-date and --until must match when both are provided")
    resolved_until = meeting_date or until or default_until()
    resolved_since = since or (resolved_until - timedelta(days=MEETING_INTERVAL_DAYS))
    if resolved_since >= resolved_until:
        raise ValueError("--since must be before --until")
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

    summarize = subparsers.add_parser("summarize", help="Create a Java summary")
    summarize.add_argument(
        "--month",
        help="Calendar month to summarize, as YYYY-MM. Kept for backfills; use meeting-date for sync notes.",
    )
    summarize.add_argument(
        "--meeting-date",
        type=parse_iso_date,
        help="Community sync meeting date. Defaults to today when no date range is provided.",
    )
    summarize.add_argument("--since", type=parse_iso_date, help="Start date, inclusive")
    summarize.add_argument("--until", type=parse_iso_date, help="End date, exclusive")
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
        default=20,
        help="Number of top commits to include in markdown",
    )
    summarize.add_argument(
        "--notes",
        type=Path,
        default=Path("data/notes/iceberg_community_sync_notes.md"),
        help="Community notes file used to build a LanceDB ranking index when present",
    )
    summarize.add_argument(
        "--lancedb-dir",
        type=Path,
        default=Path(".cache/lancedb"),
        help="Directory for the local LanceDB ranking index",
    )

    backtest = subparsers.add_parser(
        "backtest",
        help="Backtest Java summary ranking against community sync notes",
    )
    backtest.add_argument(
        "--notes",
        type=Path,
        default=Path("data/notes/iceberg_community_sync_notes.md"),
        help="Community sync notes to backtest against",
    )
    backtest.add_argument(
        "--input",
        type=Path,
        default=Path("data/commits/apache_iceberg.csv"),
        help="Commit CSV to score",
    )
    backtest.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/backtests"),
        help="Directory for backtest report files",
    )
    backtest.add_argument(
        "--lancedb-dir",
        type=Path,
        default=Path(".cache/lancedb-backtest"),
        help="Directory for temporary LanceDB backtest indexes",
    )
    backtest.add_argument("--top", type=int, default=10, help="Primary hit threshold")
    backtest.add_argument(
        "--comparison-top",
        type=int,
        default=20,
        help="Secondary hit threshold",
    )
    backtest.add_argument("--start-date", type=parse_iso_date, help="First sync date to evaluate")
    backtest.add_argument("--end-date", type=parse_iso_date, help="Last sync date to evaluate")
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
    has_period_args = bool(args.meeting_date or args.since or args.until)
    if args.month and has_period_args:
        raise SystemExit("--month cannot be combined with --meeting-date, --since, or --until")
    try:
        if args.month:
            result = summarize_month(
                month=args.month,
                input_path=args.input,
                output_dir=args.output_dir,
                top=args.top,
                notes_path=args.notes,
                lancedb_dir=args.lancedb_dir,
            )
        else:
            since, until = resolve_summary_range(
                since=args.since,
                until=args.until,
                meeting_date=args.meeting_date,
            )
            result = summarize_period(
                since=since,
                until=until,
                input_path=args.input,
                output_dir=args.output_dir,
                top=args.top,
                notes_path=args.notes,
                lancedb_dir=args.lancedb_dir,
            )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    print(
        f"scored {result.candidate_count} commits from {result.since} before {result.until} "
        f"and wrote {result.selected_count} highlights to {result.markdown_path}"
    )
    print(f"scored CSV: {result.scored_csv_path}")
    return 0


def run_backtest(args: argparse.Namespace) -> int:
    if args.top < 1:
        raise SystemExit("--top must be at least 1")
    if args.comparison_top < args.top:
        raise SystemExit("--comparison-top must be greater than or equal to --top")
    result = backtest_java_highlights(
        notes_path=args.notes,
        input_path=args.input,
        output_dir=args.output_dir,
        lancedb_dir=args.lancedb_dir,
        top=args.top,
        comparison_top=args.comparison_top,
        start_date=args.start_date,
        end_date=args.end_date,
    )
    print(
        f"backtested {result.sections_evaluated} sections: "
        f"found {result.found_prs}/{result.note_prs} note PRs, "
        f"hits@{args.top}={result.hits_at_top}/{result.found_prs}, "
        f"hits@{args.comparison_top}={result.hits_at_comparison_top}/{result.found_prs}"
    )
    print(f"report: {result.markdown_path}")
    print(f"details: {result.csv_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "collect":
        return run_collect(args)
    if args.command == "summarize":
        return run_summarize(args)
    if args.command == "backtest":
        return run_backtest(args)
    parser.error(f"unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
