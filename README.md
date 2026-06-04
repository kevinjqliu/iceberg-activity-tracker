# Iceberg Activity Tracker

Review-candidate summaries for Apache Iceberg community sync updates.

Start here:

- [Community summaries](summaries/)

Each period page is built as a shared meeting summary page with separate
repository sections. Today it includes `apache/iceberg` and
`apache/iceberg-python`, `apache/iceberg-rust`, `apache/iceberg-go`, and
`apache/iceberg-cpp`; future Iceberg repositories can be added as additional
sections on the same page.

## Layout

- `summaries/`: human-facing summary pages and scored candidate CSVs
- `data/commits/`: collected commit metadata used by the summarizer
- `data/notes/`: historical community sync notes used for LanceDB ranking
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

Backtest reports are generated locally under `data/backtests/` and are not
committed.

## Pipeline Notes

The tracked repositories are configured in `src/iceberg_activity/config.py`.
Current targets are `apache/iceberg`, `apache/iceberg-python`,
`apache/iceberg-rust`, `apache/iceberg-go`, and `apache/iceberg-cpp`.

The collector fetches configured repositories over read-only HTTPS, stores bare
git caches under `.cache/repos/`, and writes one CSV per repository under
`data/commits/`.

Summarization builds a local LanceDB index from
`data/notes/iceberg_community_sync_notes.md` and uses past Java highlight bullets
as part of the ranking.

GitHub Actions uses two workflows:

- `collect.yml` runs commit collection daily at `13:17 UTC`, roughly 6am Pacific
  during daylight saving time.
- `summarize.yml` runs summary generation on a separate three-week Wednesday
  cadence anchored at 2026-06-24. It checks once per Wednesday at `15:17 UTC`,
  after daily collection has time to finish, then skips off-cycle Wednesdays.
  Manual runs generate a summary for the
  supplied `meeting_date` input or today's Pacific date.

Generated commit CSVs are committed under `data/commits/`; generated summary
pages are committed under `summaries/`.
