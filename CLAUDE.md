# RetainIQ — Project Constitution

## PRODUCT

RetainIQ turns prepaid customer recharge and usage behaviour into a ranked, costed, explainable retention worklist, and measures incremental impact with mandatory control groups.

**MVP** = churn risk, reason codes, revenue at risk, expected-net-value ranking, offer + plan-fit suggestion, campaign with control group.

**Deferred:** survival models, network QoS, postpaid, broadband, port-out destination, multi-tenant SaaS.

## DATA LAYERS (never mix)

| Layer | Source | Permitted use |
|---|---|---|
| **L1 real** | 99,999-row Indian prepaid churn dataset | All metrics come only from here. |
| **L2** | Orange Belgium randomized uplift data | Uplift method validation only. |
| **L3** | Synthetic demo tenant from our own documented simulator | UI demo only, never metrics. |
| **L4** | TRAI aggregates | Context only. |

Rows, features, models and results from different layers are never combined into one table, model or reported figure.

## HARD RULES

- Never use label-month (`_9`) columns as features. A test enforces this.
- Never use random splits as the headline evaluation; the out-of-time backtest is the headline.
- Never report accuracy as a headline. Report PR-AUC, lift@10%, precision@10%, Brier, calibration.
- Never claim causal impact without randomized treatment data.
- Every rupee figure must trace to `configs/assumptions.yaml` and be labelled as estimate.
- Never fabricate data, sources, URLs, licences or metrics. Unknown = say unknown.
- No PII anywhere. Synthetic IDs only.
- No scraping of operator websites. Plan catalogue is hand-entered by the human with URL and date.
- Modular monolith. No Kafka, Kubernetes, Spark, Redis or microservices.
- GIT: never run `git commit`, `git push`, `git merge`, `gh pr`, or any command that writes history or remote state. Never add Co-Authored-By lines or your name to anything. End each phase with a staged-files list and suggested conventional-commit messages for the human to run.

## STACK

- **Backend / ML:** Python 3.11, uv, pandas, pandera, scikit-learn, LightGBM, CatBoost, Optuna, SHAP, MLflow (local), FastAPI, Pydantic v2, SQLAlchemy 2, PostgreSQL, Alembic, pytest, ruff, mypy.
- **Frontend:** React, Vite, TypeScript, Tailwind, TanStack Query, Recharts.
- **Runtime:** Docker Compose.

## LOCAL ENVIRONMENT

- Development machine is Windows with an Application Control policy that blocks unsigned .exe launchers (`mypy.exe` was blocked). GNU Make is not installed and will not be installed.
- Always invoke Python tools as `uv run python -m <tool>`. Never rely on console-script .exe launchers.
- The canonical task runner is `uv run python tasks.py <target>`. The Makefile exists only as a thin wrapper for Linux/CI and must call `tasks.py`.

## LAYOUT

```
data/raw/            # gitignored — original downloads, never edited
data/processed/      # gitignored — pipeline outputs
src/retainiq/
  data/              # loaders, schemas (pandera), validation
  features/          # feature engineering (time-aware)
  models/            # training, calibration, evaluation
  decision/          # revenue at risk, expected net value, offer/plan-fit
  synthetic/         # L3 demo-tenant simulator
  api/               # FastAPI app
  db/                # SQLAlchemy models, Alembic
pipelines/           # runnable entry points (data, train, evaluate)
notebooks/           # exploration only, never imported
tests/
configs/             # assumptions.yaml and run configs
catalog/             # hand-entered plan catalogue (with URL + date)
docs/
reports/             # PHASE_N_REPORT.md and evaluation outputs
frontend/
```

## WORKFLOW

- Plan first, then build in small verified steps.
- Run tests and ruff after each step (`uv run python tasks.py test`, `uv run python tasks.py lint`).
- Delegate reviews to the subagents in `.claude/agents/`: `data-auditor`, `ml-reviewer`, `code-reviewer`, `claims-checker`.
- End every phase by writing `reports/PHASE_N_REPORT.md` containing: what was built, how to run it, results with evidence, known limitations, open questions for the human, staged files, suggested commits.
