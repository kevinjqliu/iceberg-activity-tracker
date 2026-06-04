# AGENTS.md

This file is context for future coding agents working in this repository.

## Project Purpose

This repo builds commit-highlight candidate summaries for Apache Iceberg
community sync meetings. It is intentionally focused on commit highlights across
Iceberg repositories, not full meeting notes. Release status, dev-list topics,
and discussion items may be tracked elsewhere and should not be inferred from
commit data unless explicitly requested.

The project should help Kevin review recent commits quickly and manually choose
what to mention in community sync updates.

## Current Repositories

Configured in `src/iceberg_activity/config.py`:

- `apache/iceberg` -> Java section
- `apache/iceberg-python` -> Python section
- `apache/iceberg-rust` -> Rust section
- `apache/iceberg-go` -> Go section
- `apache/iceberg-cpp` -> C++ section

Each repo has its own commit CSV under `data/commits/`. Each generated summary
README combines all configured repos into one page with per-repo sections.

## Important Design Decisions

- Use Python and `uv` for everything in this repo.
- Read Apache repos over read-only HTTPS. Do not require GitHub tokens for
  public Apache repository reads.
- Parse commit history locally with `git`; do not scrape GitHub HTML.
- Keep local git caches under `.cache/repos/`.
- Commit CSVs are generated under `data/commits/`.
- Human-facing summaries live under `summaries/<period>/README.md`.
- Review artifacts live under `summaries/<period>/review-data/` to avoid
  cluttering the summary README folder.
- Scored and themed CSVs remain complete audit/review artifacts.
- README output suppresses obvious routine noise, but CSVs should still retain
  those rows for manual review.
- Meeting windows are half-open: `since <= committer_date < until`.
- It is acceptable for commits on the meeting date to appear in the next
  summary rather than trying to model meeting timestamps.

## Summary Generation Philosophy

The generated README is a review-candidate page, not a final polished community
sync script.

Do not add score thresholds for README rendering unless Kevin asks. Kevin wants
to manually filter during review. The current preferred behavior is:

- Rank and theme commits.
- Keep top candidate themes broad enough for review.
- Hard-suppress only obviously routine README items.
- Keep all scored/theme data in CSVs.

Hard-suppressed README items currently include:

- Dependabot/dependency bumps.
- CI-only workflow/zizmor/action updates.
- docs-only changes.
- test-only cleanup.
- release-script chores.
- `.gitignore` chores.
- similar low-signal sync items.

Security/CVE/license/notice/blocking and publishing/release-critical items may
still render.

## Theming And Scoring

Main summarizer code is in `src/iceberg_activity/summarizer.py`.

Commit scoring uses transparent heuristics plus optional LanceDB similarity
against historical notes in `data/notes/iceberg_community_sync_notes.md`.

Theme grouping is deterministic and intentionally conservative. Recurring theme
rules include REST pagination, catalog/view support, row lineage, deletion
vectors, compaction/rewrite data files, Puffin, encryption, partition
statistics, and maintenance CLI.

Avoid making theme grouping too aggressive. Kevin specifically called out that
themes should only group commits that are highly related.

## LanceDB Context

LanceDB is used as a local similarity helper, not as the source of truth. The
best current mental model is:

- deterministic scorer produces candidates;
- LanceDB provides similarity against previous human-highlight bullets;
- humans still review the generated README and review-data CSVs.

Do not introduce external LLM or GitHub API dependencies unless Kevin asks.

## Common Commands

Use `uv` through Make targets whenever possible:

```bash
make sync
make collect
make summarize MEETING_DATE=2026-06-03
make summarize SUMMARY_SINCE=2026-05-13 SUMMARY_UNTIL=2026-06-03
make meeting
make backtest BACKTEST_ARGS="--start-date 2026-05-13 --end-date 2026-06-03"
make test
```

Direct verification commands used during development:

```bash
UV_CACHE_DIR=.cache/uv uv run --python 3.12 pytest -q
UV_CACHE_DIR=.cache/uv uv run --python 3.12 ruff check .
git diff --check
```

## Workflows

There are two GitHub Actions workflows:

- `.github/workflows/collect.yml`
  - Runs daily.
  - Cron: `17 13 * * *`.
  - Comment says this is about 6:17am PT during daylight saving time.
  - Runs `make collect`.
  - Commits changes under `data/commits`.

- `.github/workflows/summarize.yml`
  - Runs weekly on Wednesday but gates to every 3 weeks.
  - Cron: `17 15 * * 3`.
  - Comment says this is about 8:17am PT during daylight saving time.
  - Cadence anchor: `2026-06-24`.
  - Runs `make summarize MEETING_DATE=<date>` on in-cadence Wednesdays or on
    manual dispatch.
  - Commits changes under `summaries`.

The workflows use `contents: write` because they commit generated files back to
the repository.

## Existing Summary Periods

Current generated period READMEs:

- `summaries/2026-04-01_to_2026-04-22/README.md`
- `summaries/2026-04-22_to_2026-05-13/README.md`
- `summaries/2026-05-13_to_2026-06-03/README.md`

The top-level `summaries/README.md` links to generated periods.

## Backtesting Notes From This Session

The generated summaries were compared against
`data/notes/iceberg_community_sync_notes.md` for the three available periods.
Key lessons:

- Python REST pagination benefits from grouping related commits into one theme.
- Rust and Go scoring needed tuning to keep dependency bumps and routine chores
  below feature/correctness work.
- Java summaries can still surface some lower-value chores if they score highly;
  use hard README suppression only for obvious routine cases, not broad score
  thresholds.
- Boundary misses on the meeting day are acceptable because the next half-open
  period includes them.

## Repository Structure

- `README.md`: user-facing overview and command reference.
- `Makefile`: preferred command surface.
- `pyproject.toml`: package metadata and dependencies.
- `src/iceberg_activity/cli.py`: CLI entry point.
- `src/iceberg_activity/collector.py`: collection orchestration.
- `src/iceberg_activity/git_client.py`: local git fetch/log parsing.
- `src/iceberg_activity/summarizer.py`: scoring, theme grouping, README/CSV
  output.
- `src/iceberg_activity/vector_ranker.py`: LanceDB similarity ranking.
- `src/iceberg_activity/backtester.py`: historical comparison support.
- `tests/`: pytest coverage for collector, CLI, summarizer, vector ranker, and
  backtester.
- `data/notes/iceberg_community_sync_notes.md`: historical notes used for
  ranking/backtesting.

## Git And Editing Notes

- Preserve generated CSVs and summary READMEs unless explicitly cleaning or
  regenerating them.
- Do not delete `_scored.csv` or `_themes.csv`; they are review artifacts and
  still useful.
- Prefer scoped changes and update tests for summarizer behavior.
- After changing summarizer logic, regenerate affected summary periods.
- Before commit, run tests, ruff, and `git diff --check`.
- Use normal git commits with concise messages. Recent useful commit messages:
  - `Tune community sync scoring`
  - `Regenerate April and May summaries`
  - `Suppress routine items in summary README`

## Current State At Time Of Writing

The latest pushed commit before adding this file was:

- `676e78a` `Suppress routine items in summary README`

That commit added hard README suppression for routine items and regenerated the
three existing summary READMEs. The worktree was clean before creating this
`AGENTS.md` file.
