# Iceberg Activity Tracker

Review-candidate summaries for Apache Iceberg community sync updates.

Start here:

- [Community summaries](summaries/)

Each period page is built to become a shared meeting summary page. Today it has
an `apache/iceberg` Java section; future Iceberg repositories can be added as
additional sections on the same page.

## Layout

- `summaries/`: human-facing summary pages and scored candidate CSVs
- `data/commits/`: collected commit metadata used by the summarizer
- `data/notes/`: historical community sync notes used for LanceDB ranking
- `data/backtests/`: ranking backtest reports
- `src/`: collector, scoring, ranking, and CLI code

## Common Commands

Install locally:

```bash
uv sync --group dev
```

Generate a Java review-candidate page for a community sync meeting:

```bash
make summarize MEETING_DATE=2026-06-03
```

Meeting summaries use half-open windows. For example, a 2026-06-03 meeting
includes commits from 2026-05-13 and excludes commits from 2026-06-03, so
handoff-day commits appear in the next meeting:

```text
2026-05-13 <= commit_date < 2026-06-03
```

Backfill an explicit meeting window:

```bash
make summarize SUMMARY_SINCE=2026-05-13 SUMMARY_UNTIL=2026-06-03
```

Collect fresh commits and then summarize the current 21-day meeting window:

```bash
make meeting
```

Collect only:

```bash
make collect
```

Backtest ranked candidates against Java sections in the community sync notes:

```bash
make backtest BACKTEST_ARGS="--start-date 2026-05-13 --end-date 2026-06-03"
```

## Pipeline Notes

The first version tracks only `apache/iceberg`. Additional repositories can be
added later in `src/iceberg_activity/config.py`.

The collector fetches `apache/iceberg` over read-only HTTPS, stores a bare git
cache under `.cache/repos/apache_iceberg`, and writes
`data/commits/apache_iceberg.csv`.

Summarization builds a local LanceDB index from
`data/notes/iceberg_community_sync_notes.md` and uses past Java highlight bullets
as part of the ranking.

The GitHub Actions workflow runs on the three-week Wednesday meeting cadence
anchored at 2026-06-24, starting around 6am Pacific with up to 20 minutes of
jitter. Manual runs generate a summary for the supplied `meeting_date` input or
today's Pacific date.

Generated commit CSVs are committed under `data/commits/`; generated summary
pages are committed under `summaries/`.
