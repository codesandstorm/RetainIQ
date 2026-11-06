# RetainIQ

Prepaid telecom retention decision engine. RetainIQ turns prepaid customer recharge and usage behaviour into a ranked, costed, explainable retention worklist, and measures incremental impact with mandatory control groups.

> **Status:** Phase 0 — project scaffold only. No product code, data, models or results yet. There are no metrics to report.

## Quick start

Requires Python 3.11 and [uv](https://docs.astral.sh/uv/). The task runner is `tasks.py` (standard library only); the Makefile is a thin wrapper for Linux/CI.

```bash
uv run python tasks.py setup        # uv sync
uv run python tasks.py all-checks   # test + lint + format check + typecheck
```

Other targets: `test`, `lint`, `format`, `typecheck`. `data`, `train`, `evaluate` and `serve` are placeholders until later phases.

## Project rules

See [CLAUDE.md](CLAUDE.md) for the product scope, data layers, hard rules, stack and workflow. Review subagents live in [.claude/agents/](.claude/agents/).
