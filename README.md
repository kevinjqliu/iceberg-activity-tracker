# Iceberg Activity Tracker

Collect recent commit activity from Apache Iceberg repositories and write CSV files for monthly community updates.

The first version tracks only `apache/iceberg`. Additional repositories can be added later in `src/iceberg_activity/config.py`.

## Usage

Install locally:

```bash
python3 -m pip install -e ".[dev]"
```

Collect the default recent window, currently the last 45 days:

```bash
iceberg-activity collect
```

Backfill a specific date range:

```bash
iceberg-activity collect --since 2026-05-01 --until 2026-05-31
```

Useful options:

```bash
iceberg-activity collect --output-dir data/commits --cache-dir .cache/repos
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
  contents: read
```

The generated CSV is uploaded as a workflow artifact. The workflow does not commit generated files back to the repository and does not require secrets for reading the public Apache repository.
