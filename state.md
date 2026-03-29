## Handoff — 2026-03-29 (session 3)

### Phase: Data complete. Portal rebuilt. Capabilities synced. Ready for PR campaign.

### Done (session 3)

- SEO: removed noindex/nofollow, added Schema.org JSON-LD, OG/Twitter meta, canonical
- Discoverability: llms.txt, CITATION.cff, robots.txt, sitemap.xml
- README rewritten: JTBD hero section, "Why trust this data", CI badges
- Repo description updated (119 models × 48 benchmarks)
- **Capability sync script** (`sync_capabilities.py`): pulls modalities, parameters, limits from OpenRouter API
- Fixed 27 broken openrouter_ids (dots vs dashes, missing suffixes)
- **97/119 models** have structured capabilities: vision, tool_calling, reasoning, structured_output, json_mode, logprobs, max_output_tokens
- **Manual capabilities** (`manual_capabilities.json`): 15 top models with knowledge_cutoff, effective_context, caching type, training_data_date
- **Staleness tracking**: validate.py warns on >90d manual data, CI runs daily
- **Portal rebuilt from JSON**: capabilities column (V/T/R/S/A/I badges), max output column
- **CI pipeline complete**: daily sync_capabilities → fetch_prices → generate_portal → auto-commit
- generate_portal.py bug fixed (same-date replacement)

### Anti-staleness architecture

| Layer               | Auto-updated             | Frequency | Staleness detection             |
| ------------------- | ------------------------ | --------- | ------------------------------- |
| Pricing             | Yes (OpenRouter API)     | Daily CI  | validate.py warns >7d           |
| Capabilities        | Yes (OpenRouter API)     | Daily CI  | Auto-refreshed                  |
| Portal HTML         | Yes (generate_portal.py) | Daily CI  | Regenerated from JSON           |
| Benchmark scores    | No (manual)              | Weekly    | validate.py warns by volatility |
| Manual capabilities | No (manual)              | Quarterly | validate.py warns >90d          |

### Open tasks

- [ ] PR campaign: 4 awesome lists + 3 functional repos (langchain, litellm, open-compass)
- [ ] Russian README (README_ru.md)
- [ ] Auto-scrapers: fetch_mteb.py, fetch_swebench.py, fetch_arena.py
- [ ] History snapshots (data/history/YYYY-MM-DD/)
- [ ] Capability filter in portal (filter by vision, tools, etc.)

### Research done (session 3)

- **PR targets researched**: 4 awesome lists (103K+ combined stars) + 3 functional repos (langchain 131K, litellm 41K, open-compass 6.8K)
- **GitHub profile cleaned**: removed bio, blog, Discord. Kept name + Twitter only
