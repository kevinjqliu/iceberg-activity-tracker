.PHONY: all install collect test clean

PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
OUTPUT_DIR ?= data/commits
CACHE_DIR ?= .cache/repos
COLLECT_ARGS ?=

all: collect

install:
	$(PIP) install .

collect: install
	iceberg-activity collect --output-dir $(OUTPUT_DIR) --cache-dir $(CACHE_DIR) $(COLLECT_ARGS)

test:
	$(PYTHON) -m pytest

clean:
	rm -rf $(CACHE_DIR)
