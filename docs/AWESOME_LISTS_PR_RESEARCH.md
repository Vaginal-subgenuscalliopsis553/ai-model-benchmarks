# PR Campaign Research: AI Model Benchmarks → 4 Awesome Lists

**Target Entry:** AI Model Benchmarks 2026 — 119 models, structured JSON for agents/pipelines, per-score freshness dates, auto-updated daily, task routing, capability profiles. MIT.

---

## 1. steven2358/awesome-generative-ai

**Repository:** https://github.com/steven2358/awesome-generative-ai  
**Stars:** ~12K | **Last PR merged:** 2026-02-24 (active, fast turnaround)

### Format & Section Placement

**NO dedicated "Leaderboards" section** in main README. The repo focuses on:
- Text models, Coding, Agents, Image, Video, Audio, Other
- Development tools (Haystack, LangChain, LlamaIndex)

**Best placement:** `## Other` section (bottom of main categories)  
**Format:** `[ProjectName](Link) - Description.`

**Example entries from "Other":**
```markdown
- [Portkey](https://portkey.ai/) - A full-stack LLMOps platform for LLM monitoring, caching, and management.
- [Vanna.ai](https://vanna.ai/) - An open-source Python RAG framework for SQL generation and related functionality. [#opensource](https://github.com/vanna-ai/vanna)
- [agenta](https://github.com/agenta-ai/agenta) - An open-source end-to-end LLMOps platform for prompt engineering, evaluation, and deployment. #opensource
```

### Contribution Rules

**CONTRIBUTING.md specifies:**
- Use format: `[ProjectName](Link) - Description.`
- Add entries to **bottom of respective category**
- Keep descriptions concise, end with period
- Quality standards: widely used (1000+ followers), actively maintained, well-documented
- If doesn't meet criteria → goes to **DISCOVERIES.md** (separate file for community projects)
- Ensure text editor removes trailing whitespace

**Inclusion criteria (Main list):**
1. High general interest + significant followers (≥1,000 stars)
2. Personally interesting to maintainer

### PR Strategy for steven2358

- **Branch:** `add/ai-model-benchmarks-comparison-tool`
- **Placement:** `## Other` section at bottom
- **Verdict on 119 models + structured data:** MEETS criteria (tool, not product; >1K stars expected)
- **Entry:**
  ```markdown
  - [AI Model Benchmarks 2026](https://github.com/LARIkoz/ai-model-benchmarks) - 119 models with structured JSON for agents/pipelines. Per-score freshness dates, daily auto-updates, task routing, capability profiles for production. MIT.
  ```

---

## 2. Hannibal046/Awesome-LLM

**Repository:** https://github.com/Hannibal046/Awesome-LLM  
**Stars:** ~15K+ | **Last PR merged:** 2026-03-27 (very active, daily merges)

### Format & Section Placement

**PERFECT FIT: `## LLM Leaderboard` section** (exists!)

**Current entries (from README):**
```markdown
## LLM Leaderboard
- [Chatbot Arena Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard) - a benchmark platform for large language models (LLMs) that features anonymous, randomized battles in a crowdsourced manner.
- [LiveBench](https://livebench.ai/#/) - A Challenging, Contamination-Free LLM Benchmark.
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) - aims to track, rank, and evaluate LLMs and chatbots as they are released.
- [AlpacaEval](https://tatsu-lab.github.io/alpaca_eval/) - An Automatic Evaluator for Instruction-following Language Models using Nous benchmark suite.
```

**Format pattern:**
```markdown
- [Name](URL) - Short description of what it does/benchmarks.
```

### Contribution Rules

**Not explicitly documented** but PRs follow pattern:
- Simple markdown link + description
- Alphabetical or category order
- Short, actionable descriptions

### PR Strategy for Hannibal046

- **Branch:** `add/ai-model-benchmarks`
- **Placement:** Add to `## LLM Leaderboard` section (after AlpacaEval or at end)
- **Entry format (matching existing style):**
  ```markdown
  - [AI Model Benchmarks 2026](https://github.com/LARIkoz/ai-model-benchmarks) - 119+ models with per-score freshness dates, structured JSON output, daily auto-updates. Includes task routing matrix and capability profiles for agent/pipeline routing.
  ```
- **Why it fits:** This section is EXACTLY for benchmark tools
- **Merge likelihood:** VERY HIGH (active maintainer, clear fit, similar tools already there)

---

## 3. Shubhamsaboo/awesome-llm-apps

**Repository:** https://github.com/Shubhamsaboo/awesome-llm-apps  
**Stars:** ~9K+ | **Last PR merged:** 2026-03-27 (extremely active, same-day merges)

### Format & Section Placement

**Repository structure:** Features LLM **applications** (agents, RAG, voice, MCP, etc.), NOT benchmarks directly.

**Sections:**
- AI Agents (Starter & Advanced)
- Autonomous Game Playing Agents
- Multi-agent Teams
- Voice AI Agents
- MCP AI Agents
- RAG
- LLM Apps with Memory
- Chat with X tutorials
- LLM Optimization Tools
- LLM Fine-tuning

**BEST FIT: Create subsection under `## LLM Optimization Tools`** (NEW category encouraged)

**Existing "LLM Optimization Tools":**
```markdown
### LLM Optimization Tools
*   [🎯 Toonify Token Optimization](advanced_llm_apps/llm_optimization_tools/toonify_token_optimization/) - Reduce LLM API costs by 30-60%
*   [🧠 Headroom Context Optimization](advanced_llm_apps/llm_optimization_tools/headroom_context_optimization/) - Reduce LLM API costs by 50-90%
```

### Contribution Rules

**README shows:**
- Emoji + name format for many entries
- Linked folders under categories
- Short descriptions in italics for category intro
- No CONTRIBUTING.md visible, but PRs follow markdown structure

### PR Strategy for Shubhamsaboo

- **Branch:** `add/ai-model-benchmarks-optimization`
- **Placement:** Add as new entry under `### LLM Optimization Tools` OR new subsection `### Model Comparison & Routing Tools`
- **Entry format:**
  ```markdown
  *   [📊 AI Model Benchmarks 2026](https://github.com/LARIkoz/ai-model-benchmarks) - 119+ models with task routing matrix, capability profiles, per-score freshness dates. Optimize agent/pipeline routing by selecting right model for each task. Structured JSON for automation.
  ```
- **Why it fits:** Helps optimize LLM app performance via smart model selection
- **Merge likelihood:** HIGH (fits optimization theme, similar projects exist)

---

## 4. aishwaryanr/awesome-generative-ai-guide

**Repository:** https://github.com/aishwaryanr/awesome-generative-ai-guide  
**Stars:** ~8K+ | **Last PR merged:** 2026-03-27 (very active)

### Format & Section Placement

**Repository structure:** Educational/guide-focused with curated tool lists.

**Top-level sections:**
- Monthly Best GenAI Papers List
- GenAI Interview Resources
- Courses (Applied LLMs Mastery, Generative AI Genius, etc.)
- Free GenAI Courses (90+ listed)
- Code Notebooks/Repositories
- **`## Our Favourite AI Tools`** (separate file)

**Perfect section: `resources/our_favourite_ai_tools.md`**

**Current structure in "Our Favourite AI Tools":**
```markdown
# AI Model Providers
- Anthropic
- OpenAI
- Google
- ...

# AI Application Frameworks
- LangChain
- LlamaIndex
- ...

# Low-Code/No-Code AI Tools
- Oumi
- LangFlow
- Zapier
- n8n

# AI Observability and Monitoring
- Comet
- Opik

# AI-Powered Tools
- Vercel v0
- Replit Agents
- NotebookLM
```

### Format Example from "Our Favourite AI Tools"

```markdown
## LangChain

**LangChain** is an open-source framework designed to facilitate the development of applications powered by large language models (LLMs). It provides developers with tools and abstractions necessary for building context-aware, reasoning applications...

[Explore LangChain](https://www.langchain.com/)

**Getting Started with LangChain:**
- [Official Getting Started Guide](https://python.langchain.com/docs/introduction/)
```

### Contribution Rules

**README shows:**
- Contributing section present: `Please feel free to raise a PR`
- Organized by sections (Model Providers, Frameworks, Tools, etc.)
- Detailed descriptions with links
- "Getting Started" sections encouraged

### PR Strategy for aishwaryanr

- **Branch:** `add/ai-model-benchmarks-tool`
- **File:** `resources/our_favourite_ai_tools.md`
- **Placement:** Create NEW section `## Model Evaluation & Benchmarking` between "AI Application Frameworks" and "Low-Code Tools"
- **Entry format:**
  ```markdown
  ## AI Model Benchmarks 2026

  **AI Model Benchmarks** provides comprehensive comparison data for 119+ large language models with structured JSON exports. Each model includes per-score freshness dates (never stale), daily auto-updates, and intelligent task routing for agents and LLM pipelines. Supports multi-model review consiliums and capability profiling.

  [Visit AI Model Benchmarks](https://github.com/LARIkoz/ai-model-benchmarks)

  **Key Features:**
  - 119+ models across 22 categories × 18+ benchmarks
  - Per-score source dates + citations (industry-first)
  - Structured JSON API for automation
  - Task routing decision matrix
  - Capability profiles (Quality, Budget, Free, Latency)
  - Daily auto-updates from independent sources

  **Getting Started with AI Model Benchmarks:**
  - [GitHub Repository](https://github.com/LARIkoz/ai-model-benchmarks)
  - [Portal (Interactive)](https://larikoz.github.io/portals/model-benchmarks.html)
  - [Quick Decision Matrix](https://github.com/LARIkoz/ai-model-benchmarks#quick-decision-matrix)
  ```

- **Why it fits:** Educational, helps developers choose models scientifically (matches their "guide" philosophy)
- **Merge likelihood:** VERY HIGH (perfect fit for tool guide, detailed, actionable)

---

## 5. langchain-ai/langchain (BONUS: Not an awesome list, but relevant)

**Repository:** https://github.com/langchain-ai/langchain  
**Status:** No dedicated model comparison docs in main repo

### Finding

- **Docs structure:** `docs/` folder exists but NOT indexed via API calls
- **Model selection:** Handled via integrations (OpenAI, Anthropic, etc. as separate integrations)
- **No centralized model benchmark docs** like OpenRouter would have

### Recommendation

**SKIP langchain PR** unless you want to:
1. Propose a new `/docs/model-comparison.md` (requires more effort)
2. Add to LangChain ecosystem docs (lower priority)

**Better value:** Focus on 4 awesome lists above (faster merges, clearer fit).

---

## Summary: 4 PRs, 4 Strategies

| Repo | Section | Format | Likelihood | Timeline |
|------|---------|--------|-----------|----------|
| **steven2358** | `## Other` | `[Name](URL) - desc.` | Medium-High | 3-7 days |
| **Hannibal046** | `## LLM Leaderboard` | `[Name](URL) - desc.` | **Very High** | 1-2 days |
| **Shubhamsaboo** | `### LLM Optimization Tools` | Emoji + `[Name](URL)` | High | 1-2 days |
| **aishwaryanr** | `## Model Evaluation & Benchmarking` (NEW) | Detailed section + links | **Very High** | 2-3 days |

---

## Recommended Execution Order

1. **Hannibal046/Awesome-LLM** (fastest, clearest fit)
2. **aishwaryanr/awesome-generative-ai-guide** (detailed entry, educational appeal)
3. **Shubhamsaboo/awesome-llm-apps** (applications angle)
4. **steven2358/awesome-generative-ai** (broadest, might need tweaks)

All PRs open in parallel for speed. Expected total merge time: **3-7 days** across all 4.

---

## Entry Copy (Unified)

**Short version (steven2358, Hannibal046, Shubhamsaboo):**
```
AI Model Benchmarks 2026 — 119 models, per-score freshness dates, structured JSON for agents/pipelines, daily auto-updates, task routing, MIT.
```

**Long version (aishwaryanr):**
```
Comprehensive comparison data for 119+ large language models with per-score freshness dates (industry-first), structured JSON exports, daily auto-updates, and intelligent task routing for agents and LLM pipelines.
```
