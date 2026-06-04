.PHONY: all sync install collect summarize monthly backtest test clean

UV ?= uv
UV_CACHE_DIR ?= .cache/uv
PYTHON_VERSION ?= 3.12
OUTPUT_DIR ?= data/commits
CACHE_DIR ?= .cache/repos
COLLECT_ARGS ?=
MONTH ?=
TOP ?= 10
COMPARISON_TOP ?= 20
SUMMARY_OUTPUT_DIR ?= data/summaries
SUMMARY_INPUT ?= data/commits/apache_iceberg.csv
NOTES ?= Iceberg Community Sync Notes.md
LANCEDB_DIR ?= .cache/lancedb
BACKTEST_OUTPUT_DIR ?= data/backtests
BACKTEST_LANCEDB_DIR ?= .cache/lancedb-backtest
BACKTEST_ARGS ?=

all: collect

sync:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) sync --python $(PYTHON_VERSION) --group dev

install: sync

collect:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) run --python $(PYTHON_VERSION) iceberg-activity collect --output-dir $(OUTPUT_DIR) --cache-dir $(CACHE_DIR) $(COLLECT_ARGS)

summarize:
	@test -n "$(MONTH)" || (echo "MONTH is required, for example: make summarize MONTH=2026-06" && exit 1)
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) run --python $(PYTHON_VERSION) iceberg-activity summarize --month $(MONTH) --input $(SUMMARY_INPUT) --output-dir $(SUMMARY_OUTPUT_DIR) --top $(TOP) --notes "$(NOTES)" --lancedb-dir $(LANCEDB_DIR)

monthly: collect summarize

backtest:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) run --python $(PYTHON_VERSION) iceberg-activity backtest --notes "$(NOTES)" --input $(SUMMARY_INPUT) --output-dir $(BACKTEST_OUTPUT_DIR) --lancedb-dir $(BACKTEST_LANCEDB_DIR) --top $(TOP) --comparison-top $(COMPARISON_TOP) $(BACKTEST_ARGS)

test:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) run --python $(PYTHON_VERSION) --group dev pytest

clean:
	rm -rf $(CACHE_DIR) $(UV_CACHE_DIR) $(LANCEDB_DIR) $(BACKTEST_LANCEDB_DIR) .venv
