# HN "Show HN" Draft

**Submit:** Tuesday Apr 1, 8am PT (optimal HN timing)

---

## Title options (pick one):

1. `Show HN: AI Model Benchmarks – 119 models with per-score freshness dates, auto-updated daily`
2. `Show HN: Structured AI model data for agent routing – benchmarks, pricing, capabilities`
3. `Show HN: We track when each AI benchmark score was measured, not just the number`

**Recommended: #3** — curiosity-driven, highlights the unique angle.

---

## Post URL:

https://github.com/LARIkoz/ai-model-benchmarks

---

## First comment (by OP, post immediately after submission):

Hi HN, I built this because I was tired of benchmark tables that go stale.

The problem: most AI model comparisons show a single score per model with no date, no source link, and no way to know if the number is still valid. Prices change weekly, capabilities differ across providers, and new models appear monthly.

What this does:

- Every score has a `measured` date and a `source` URL pointing to the actual leaderboard
- Pricing and capabilities auto-update daily from OpenRouter API via GitHub Actions
- Task routing: "I need a model for X at budget Y" → structured JSON answer
- 97/119 models have capability profiles (vision, tools, reasoning, structured output)

The data is in JSON so agents and pipelines can consume it directly:

```
https://larikoz.github.io/ai-model-benchmarks/data/models.json
https://larikoz.github.io/ai-model-benchmarks/data/routing.json
```

Built with: Python scripts for scraping/syncing, GitHub Actions for daily updates, static HTML portal generated from JSON.

Feedback welcome — especially if you spot stale scores or missing models.

---

## Talking points for comments:

- **"Why not just use Artificial Analysis / LM Arena?"** → They measure different things. AA measures independently but isn't structured JSON. LM Arena is crowdsourced preference, not benchmark scores. We aggregate 16 sources and track freshness.

- **"How do you prevent contamination?"** → We track benchmark lifecycle (active/saturated/dead) and contamination risk per benchmark. Dead benchmarks like MMLU/HumanEval are flagged and excluded from routing.

- **"Why per-score dates?"** → A GPQA score from January means something different than one from March when new models release. Without dates, you can't tell if a "92%" is current or 6 months old.

- **"How is this different from leaderboards?"** → Leaderboards show rankings. We provide structured data you can query programmatically. `routing.json` tells you "for coding, use X; for reasoning, use Y; for free, use Z" — ready for agent pipelines.
