# Iceberg Activity Tracker

Collect recent commit activity from Apache Iceberg repositories and write CSV files for community updates.

The first version tracks only `apache/iceberg`. Additional repositories can be added later in `src/iceberg_activity/config.py`.

## Usage

Install locally:

```bash
uv sync --group dev
```

Collect the default recent window, currently the last 45 days:

```bash
make collect
```

Backfill a specific date range:

```bash
make collect COLLECT_ARGS="--since 2026-05-01 --until 2026-05-31"
```

Useful options:

```bash
make collect OUTPUT_DIR=data/commits CACHE_DIR=.cache/repos
```

The collector fetches `apache/iceberg` over read-only HTTPS, stores a bare git cache under `.cache/repos/apache_iceberg`, and writes `data/commits/apache_iceberg.csv`.

Generate a Java highlights draft and scored CSV for a community sync meeting.
Meeting summaries default to the half-open 21-day window ending on the meeting
date. For example, a 2026-06-03 meeting includes commits from 2026-05-13 and
excludes commits from 2026-06-03, so those handoff-day commits appear in the
next meeting:

```bash
make summarize MEETING_DATE=2026-06-03
```

Summarization builds a local LanceDB index from
`data/notes/iceberg_community_sync_notes.md` and uses past Java highlight bullets
as part of the ranking.

Backfill an explicit meeting window:

```bash
make summarize SUMMARY_SINCE=2026-05-13 SUMMARY_UNTIL=2026-06-03
```

Calendar-month summaries are still available for older backfills:

```bash
make summarize MONTH=2026-06
```

Collect fresh commits and then summarize the current 21-day meeting window:

```bash
make meeting
```

`make monthly` is kept as an alias for `make meeting`.

Collect fresh commits and summarize a specific meeting:

```bash
make meeting MEETING_DATE=2026-06-03
```

Backtest ranked candidates against Java sections in the community sync notes:

```bash
make backtest BACKTEST_ARGS="--start-date 2026-05-13 --end-date 2026-06-03"
```

## CSV Fields

Each CSV row contains:

- `repository`
- `commit_sha`
- `short_sha`
- `author_name`
- `author_email`
- `author_date`
- `committer_name`
- `committer_email`
- `committer_date`
- `subject`
- `body`
- `parents`

## GitHub Actions

The workflow runs once per day and can also be triggered manually. Daily runs
collect commit data. Summary generation runs only on the 21-day Wednesday cadence
anchored at 2026-06-03, while manual runs generate a summary for the supplied
`meeting_date` input or today's UTC date.

It uses:

```yaml
permissions:
  contents: write
```

Generated CSV and summary files are committed back to `data/` when they change
and are also uploaded as workflow artifacts. The workflow uses the built-in
`GITHUB_TOKEN`; no repository secrets are required for reading the public Apache
repository.
