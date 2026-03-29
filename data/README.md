# Data Files — Machine-Readable AI Model Reference

All files are JSON. Updated daily via GitHub Actions. Accessible via GitHub Pages:

```
https://larikoz.github.io/ai-model-benchmarks/data/models.json
https://larikoz.github.io/ai-model-benchmarks/data/routing.json
https://larikoz.github.io/ai-model-benchmarks/data/embeddings.json
https://larikoz.github.io/ai-model-benchmarks/data/benchmarks.json
https://larikoz.github.io/ai-model-benchmarks/data/pricing.json
https://larikoz.github.io/ai-model-benchmarks/data/manual_capabilities.json
```

## models.json — 119 AI Models

Each model includes:

| Field                            | Type   | Description                                |
| -------------------------------- | ------ | ------------------------------------------ |
| `id`                             | string | Unique identifier (e.g. `claude-opus-4-6`) |
| `name`                           | string | Display name                               |
| `provider`                       | string | Company (Anthropic, OpenAI, Google, etc.)  |
| `tier`                           | int    | 0=free, 1=frontier, 2=mid-range, 3=budget  |
| `context_length`                 | int    | Max input tokens                           |
| `max_output_tokens`              | int    | Max output tokens                          |
| `pricing.input`                  | float  | $/million input tokens                     |
| `pricing.output`                 | float  | $/million output tokens                    |
| `capabilities.vision`            | bool   | Accepts image input                        |
| `capabilities.tool_calling`      | bool   | Function/tool calling support              |
| `capabilities.reasoning`         | bool   | Extended thinking / chain-of-thought       |
| `capabilities.structured_output` | bool   | Structured output / JSON schema            |
| `capabilities.json_mode`         | bool   | Response format control                    |
| `capabilities.logprobs`          | bool   | Log probabilities available                |
| `openrouter_id`                  | string | OpenRouter model ID for API calls          |
| `scores.<benchmark>.value`       | float  | Benchmark score                            |
| `scores.<benchmark>.measured`    | string | Date score was measured (YYYY-MM)          |
| `scores.<benchmark>.source`      | string | URL to source leaderboard                  |

## routing.json — Task Routing

| Section             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `quick_matrix`      | 25 tasks → best model (use/backup/free)                          |
| `king_picks`        | Category winners: quality_1, quality_2, budget_1, budget_2, free |
| `free_routing`      | Best free model per task (OpenRouter + CLI tools)                |
| `embedding_routing` | Best embedding per use case (best/budget/free)                   |

## embeddings.json — 26 Embedding Models

Fields: id, name, provider, dimensions, context_length, pricing, mteb_overall, mteb_retrieval, best_for, source.

## benchmarks.json — 54 Benchmarks

Fields: id, name, category, lifecycle (active/saturated/dead/planned), volatility, contamination_risk, url.

## Freshness

- Pricing: auto-updated daily from OpenRouter API
- Capabilities: auto-updated daily from OpenRouter API
- Scores: manually reviewed weekly, each with measured date
- Manual capabilities (top 15 models): reviewed quarterly, staleness flagged at >90 days
