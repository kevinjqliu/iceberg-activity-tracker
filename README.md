# Iceberg Activity Tracker

Collect recent commit activity from Apache Iceberg repositories and write CSV files for monthly community updates.

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

The workflow runs once per day and can also be triggered manually. It uses:

```yaml
permissions:
  contents: write
```

The generated CSV is committed back to `data/commits/` when it changes and is also uploaded as a workflow artifact. The workflow uses the built-in `GITHUB_TOKEN`; no repository secrets are required for reading the public Apache repository.
