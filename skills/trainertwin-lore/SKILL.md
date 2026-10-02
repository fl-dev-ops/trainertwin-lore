---
name: trainertwin-lore
description: >-
  Extract, index, retrieve, and author grounded behavioral AI twin scenario prompts (SKILL.md) for TrainerTwin.
  Provides deterministic source indexing, Jev taxonomy normalization, instant scenario retrieval, and
  production-grade prompt authoring calibrated for Gemini 3.8 Flash. Use when collecting social media,
  indexing creator corpora, normalizing tags with Jev, querying scenario grounding clips, authoring persona SKILL.md prompts, or auditing prompt fidelity.
license: MIT
compatibility: "Python 3.12+ via uv"
metadata:
  version: "0.2.0"
  category: ai-persona
  tags: ["trainertwin", "persona", "digital-twin", "skill-authoring", "source-grounding", "mcp"]
---

# TrainerTwin Lore

## Overview

`trainertwin-lore` turns public posts, transcripts, and writings into authentic, grounded behavioral persona prompts (`SKILL.md`) for AI digital twins.

The pipeline enforces strict invariants:
- **Immutable Ground Truth:** Raw source files are untouched. The index stores line ranges and verbatim quote snapshots.
- **Single Responsibility:** Record indexing, taxonomy normalization, retrieval, authoring, and validation are strictly decoupled.
- **Calibrated for Gemini 3.8 Flash:** Prompts use explicit turn bounds (2–4 sentences), frequency-calibrated signature phrases, and negative boundaries.

---

## 4-Stage CLI Workflow

### 1. Collect Social Sources
Collect public posts and video transcripts since an absolute UTC calendar date:
```bash
uv run trainertwin-social --user <slug> --since YYYY-MM-DD \
  --linkedin 'https://www.linkedin.com/in/<profile>/' \
  --youtube 'https://www.youtube.com/@<channel>' \
  --instagram 'https://www.instagram.com/<profile>/' \
  --twitter 'https://x.com/<handle>'
```

### 2. Index & Prepare Corpus (Extraction + Auto-Normalization)
Index source files into `users/<slug>/workspace/index.json` with multi-axial facets, 500-char quote previews, and adjacency pointers. Automatically clusters tags into `taxonomy.json` using TypeSafe Jev upon completion:
```bash
# Dry run to inspect planned segmentation without paid calls
uv run trainertwin-pipeline --user <slug> index --dry-run

# Run full parallel indexing (automatically runs taxonomy normalization at completion)
uv run trainertwin-pipeline --user <slug> index --workers 8

# (Optional) Re-run taxonomy clustering standalone without re-indexing source files:
uv run trainertwin-pipeline --user <slug> normalize
```

### 3. Query Grounding Clips
Retrieve the exact 3–5 grounded source clips for a specific scenario using Jev choice routing and set-utility diversification:
```bash
uv run trainertwin-pipeline --user <slug> query "How to handle a client who says 'I will wait for prices to crash'?"
```

### 4. Author & Validate SKILL.md Prompts
Synthesize a deployable, grounded Agent Skill prompt for the runtime twin, and run an adversarial grounding audit:
```bash
# Author the scenario prompt
uv run trainertwin-pipeline --user <slug> author "Client says: 'I will wait until prices crash before buying'"

# Validate grounding, citation integrity, and voice authenticity
uv run trainertwin-pipeline --user <slug> validate client-says-i-will-wait-until-prices-crash-before-buying.md
```

---

## MCP Server Integration (`trainertwin-mcp`)

Run the stdio MCP server for agent harnesses (Pi, Claude Code, Cursor, Windsurf, Zed):
```bash
uv run trainertwin-mcp
```

### Registered MCP Tools:
- `get_status(user)`: Inspect total sources, item counts, taxonomy clusters, and authored scenarios.
- `query_scenarios(user, scenario_query, max_clips=5)`: Retrieve the 3–5 grounded clips with verbatim text and line coordinates.
- `author_scenario_skill(user, scenario_query, model)`: Retrieve clips and author a production-grade `SKILL.md` runtime prompt.
- `validate_scenario_skill(user, scenario_filename, judge_model)`: Run an adversarial audit checking citation validity and zero hallucination.
- `read_scenario_skill(user, scenario_slug)`: Read an authored scenario prompt from `workspace/scenarios/`.
- `list_taxonomy(user, facet)`: Inspect canonical concepts and aliases from `taxonomy.json`.
- `collect_social(user, since, ...)`: Run the multi-platform scraper.
- `normalize_taxonomy(user, threshold=0.70)`: Run the Jev-powered taxonomy clustering.
