# Thin wrapper for Linux/CI. The canonical task runner is tasks.py.
.PHONY: setup test lint format typecheck data train evaluate serve all-checks

setup:
	uv run python tasks.py setup

test:
	uv run python tasks.py test

lint:
	uv run python tasks.py lint

format:
	uv run python tasks.py format

typecheck:
	uv run python tasks.py typecheck

data:
	uv run python tasks.py data

train:
	uv run python tasks.py train

evaluate:
	uv run python tasks.py evaluate

serve:
	uv run python tasks.py serve

all-checks:
	uv run python tasks.py all-checks
