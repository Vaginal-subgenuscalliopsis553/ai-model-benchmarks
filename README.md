# AI Model Benchmarks 2026

> **You need to pick an AI model for your task and budget. You want data you can trust is current.**

[![Daily Prices](https://github.com/LARIkoz/ai-model-benchmarks/actions/workflows/daily-prices.yml/badge.svg)](https://github.com/LARIkoz/ai-model-benchmarks/actions/workflows/daily-prices.yml)
[![Validation](https://github.com/LARIkoz/ai-model-benchmarks/actions/workflows/validate.yml/badge.svg)](https://github.com/LARIkoz/ai-model-benchmarks/actions/workflows/validate.yml)
[![Models](https://img.shields.io/badge/models-119-green)](data/models.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-48-blue)](data/benchmarks.json)
[![Embeddings](https://img.shields.io/badge/embeddings-26-purple)](data/embeddings.json)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

**119 models · 48 benchmarks · 26 embeddings · auto-updated pricing · task routing**

[Browse the portal](https://larikoz.github.io/ai-model-benchmarks/) · [View the data](data/) · [Methodology](docs/METHODOLOGY.md)

## The problem

Benchmark tables go stale the day they're published. Prices change weekly. New models appear monthly. Most comparisons show a single score per model with no date, no source link, and no way to know if the number is still valid.

## What this solves

- **Per-score freshness dates** — every benchmark value has a `measured` date and a `source` URL. You can verify any number yourself
- **Auto-updated pricing** — fetched daily from OpenRouter API via GitHub Actions ([see the workflow](.github/workflows/daily-prices.yml))
- **Task routing** — not just "best model" but "best model for your specific task at your budget" (25 task categories, 4 tiers: quality, budget, free)
- **Benchmark lifecycle** — which benchmarks still separate models (active) vs which are noise (saturated/dead/contaminated)
- **No self-reported scores** — all data from [16 independent sources](docs/METHODOLOGY.md) (Scale AI SEAL, Artificial Analysis, BFCL, LM Arena, LiveBench...)

## Why trust this data

Every score is auditable:

1. **Source URL** — click through to the original leaderboard or paper
2. **Measured date** — know exactly when the score was collected
3. **Automated validation** — `scripts/validate.py` enforces schema, catches missing sources, flags stale scores
4. **Git history** — every change is tracked, every update has a commit
5. **CI pipeline** — daily price updates + PR validation via GitHub Actions

## Quick start

- **Browse the data:** `data/models.json`, `data/embeddings.json`, `data/benchmarks.json`
- **Find the right model:** `data/routing.json` — KING picks by category, quick decision matrix
- **Understand the methodology:** `docs/METHODOLOGY.md`

## Data structure

```
data/
  models.json       — 119 chat/completion models with scores, pricing, metadata
  embeddings.json   — 26 embedding models with MTEB scores and use-case routing
  benchmarks.json   — Registry of all tracked benchmarks with lifecycle status
  routing.json      — Task routing: KING picks, FREE routing, quick decision matrix
  pricing.json      — Cache pricing by provider (updated via script)

docs/
  METHODOLOGY.md    — Sources, freshness policy, benchmark lifecycle
  CONTRIBUTING.md   — How to submit scores and report errors
  FRESHNESS.md      — Why freshness matters, staleness indicators

scripts/
  fetch_openrouter_prices.py  — Fetches current prices, detects changes
  validate.py                 — Schema validation, duplicate check, freshness warnings
  generate_md.py              — Generates markdown tables from JSON data
```

## How to use

### Find the right model for a task

Check `data/routing.json`, section `quick_matrix`. Example entries:

| Task                  | Use                 | Backup          | Free              |
| --------------------- | ------------------- | --------------- | ----------------- |
| Write/review code     | Claude Sonnet 4.6   | MiniMax M2.5    | MiniMax M2.5 FREE |
| Complex reasoning     | Claude Opus 4.6     | Gemini 3.1 Pro  | Gemini CLI        |
| Batch classification  | Qwen CLI            | MiniMax M2.5    | Both free         |
| Long document (>200K) | Gemini 3.1 Pro (1M) | MiniMax 01 (1M) | Gemini CLI (2M)   |
| EU compliance         | Mistral Large       | Mistral Medium  | —                 |

Full routing table: `data/routing.json` → `quick_matrix` (25 task categories).

```bash
# Generate the full markdown reference
python scripts/generate_md.py > MODEL_BENCHMARKS.md
```

### Stay current on pricing

Pricing is updated by running the fetch script:

```bash
python scripts/fetch_openrouter_prices.py
```

### Validate data integrity

```bash
python scripts/validate.py
```

## How to contribute

Pull requests welcome. Requirements:

1. **Source link required** — every score must have a `source` URL pointing to the leaderboard or paper
2. **Measured date required** — use `YYYY-MM` format minimum, `YYYY-MM-DD` preferred
3. **No self-reported scores** — scores must come from independent benchmarking (not the model provider's own blog)
4. Run `python scripts/validate.py` before submitting — PRs should pass validation before submission

See `docs/CONTRIBUTING.md` for full guidelines.

## Update schedule

- **Daily (06:00 UTC):** Prices fetched from OpenRouter API via [GitHub Action](.github/workflows/daily-prices.yml)
- **On every PR:** Schema validation via [GitHub Action](.github/workflows/validate.yml)
- **Weekly (manual):** Benchmark scores reviewed against leaderboards, freshness dates updated

## Sources

Scores come from: LM Council, Artificial Analysis, Scale AI SEAL, BFCL V4, BenchLM.ai, RankSaga/Kaggle, Z.ai, MiniMax, OpenRouter official, AIModelsMap, Awesome Agents, MedQA, VALS.ai, FDA, PricePerToken, MTEB Leaderboard, Prem.ai, Mixpeek.

See `docs/METHODOLOGY.md` for full source list and trust hierarchy.

## License

MIT — see [LICENSE](LICENSE)
