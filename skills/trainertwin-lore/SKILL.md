---
name: trainertwin-lore
description: >-
  Extract, ingest, and analyze trainer lore and social media content for TrainerTwin persona development.
  Provides cited knowledge/methods, teaching cases, expression examples, deterministic wiki rendering,
  and attributed twin observations with separately labeled proposed adaptations. Use when collecting social media, ingesting trainer evidence,
  building living wikis, querying trainer lore, or analyzing communication style and decision heuristics.
license: MIT
compatibility: "Python 3.12+ via uv"
metadata:
  version: "0.1.0"
  category: ai-persona
  tags: ["trainertwin", "persona", "living-wiki", "social-media", "source-evidence"]
---

# TrainerTwin Lore

## Overview

Use the single current implementation in `pipeline/` and the normal `users/<slug>/workspace/`. Update code in place; Git holds history. Do not create frozen code copies or version-named pipelines/workspaces.

The pipeline extracts cited knowledge/methods, teaching cases and expression examples, renders them without model resummarization, and separately generates attributed observations/proposed adaptations. Speaker names require explicit metadata, not diarization-ID guesses. Exact quotes establish occurrence, not semantic truth or a faithful personality.

## Workflow

### 1. Ingestion Status & Lint
Check active evidence cards and verify integrity:
```bash
uv run trainertwin-pipeline --user <slug> status
uv run trainertwin-pipeline --user <slug> lint
```

### 2. Collect Social Sources
Collect date-bounded posts from an absolute UTC start date to today:
```bash
uv run trainertwin-social --user <slug> --since YYYY-MM-DD \
  --linkedin 'https://www.linkedin.com/in/<profile>/' \
  --youtube 'https://www.youtube.com/@<channel>' \
  --instagram 'https://www.instagram.com/<profile>/' \
  --twitter 'https://x.com/<handle>'
```

### 3. Run the Current Pipeline
```bash
# Inspect parsing without paid calls.
uv run trainertwin-pipeline --user <slug> ingest --dry-run

# Extract the three cited products; resume in this workspace if the budget runs out.
uv run trainertwin-pipeline --user <slug> ingest --model openai/gpt-4o --max-calls 20

# Render the wiki offline, then generate separately scoped twin candidates.
uv run trainertwin-pipeline --user <slug> build
uv run trainertwin-pipeline --user <slug> twin --author <exact-alias> --model openai/gpt-4o --max-calls 8

# Compile and validate offline.
uv run trainertwin-pipeline --user <slug> analyze
uv run trainertwin-pipeline --user <slug> lint
```

Keep paid calls explicitly budgeted. Re-ingest incompatible stored records in the same workspace; never invent missing fields to convert old records. Consult `pipeline/README.md` and `pipeline/SCHEMA.md` from the repository root for the current contract.

### 4. MCP Tools
When running with the `trainertwin-lore` MCP server enabled, use the registered MCP tools:
- `get_status(user)`: Inspect ingestion counts and stale manifests.
- `lint_workspace(user)`: Run offline integrity audit.
- `read_report(user, report_name)`: Read `analysis`, `timeline`, or `persona-prompt`.
- `get_wiki_topic(user, topic_slug)`: Read living wiki topic pages or platform behaviors (`linkedin`, `youtube`, `instagram`, `twitter`).
- `analyze_persona(user)`: Recompile persona reports offline.
- `collect_social(user, since, ...)`: Run multi-platform scraper.
- `run_ingest(user, model, max_calls)`: Run evidence extraction.
- `build_wiki(user, model, max_calls)`: Run wiki synthesis.
