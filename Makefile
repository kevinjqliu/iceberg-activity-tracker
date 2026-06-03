.PHONY: all sync install collect test clean

UV ?= uv
UV_CACHE_DIR ?= .cache/uv
PYTHON_VERSION ?= 3.12
OUTPUT_DIR ?= data/commits
CACHE_DIR ?= .cache/repos
COLLECT_ARGS ?=

all: collect

sync:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) sync --python $(PYTHON_VERSION) --group dev

install: sync

collect:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) run --python $(PYTHON_VERSION) iceberg-activity collect --output-dir $(OUTPUT_DIR) --cache-dir $(CACHE_DIR) $(COLLECT_ARGS)

test:
	UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV) run --python $(PYTHON_VERSION) --group dev pytest

clean:
	rm -rf $(CACHE_DIR) $(UV_CACHE_DIR) .venv
