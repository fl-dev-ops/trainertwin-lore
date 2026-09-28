---
name: trainertwin-lore
description: >-
  Extract, ingest, and analyze trainer lore and social media content for TrainerTwin persona development.
  Provides source-grounded living wiki synthesis, TypeSafe Jev authorship validation, platform behavioral
  modeling, and offline persona reports. Use when collecting social media, ingesting trainer evidence,
  building living wikis, querying trainer lore, or analyzing communication style and decision heuristics.
license: MIT
compatibility: "Python 3.12+ via uv"
metadata:
  version: "0.1.0"
  category: ai-persona
  tags: ["trainertwin", "persona", "living-wiki", "social-media", "jev", "behavior-analysis"]
---

# TrainerTwin Lore

## Overview

TrainerTwin Lore is an empirical pipeline that extracts raw public evidence from social platforms (LinkedIn, YouTube, Instagram, Twitter/X), validates attribution and context using TypeSafe Jev decision models, constructs an attested living wiki, and compiles structured persona and behavioral analysis reports for digital twins.

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

### 3. Run Pipeline (Ingest, Build, Analyze)
```bash
# Ingest sources into atomic evidence cards with Jev authorship verification
uv run trainertwin-pipeline --user <slug> ingest --model openai/gpt-4o --max-calls 20

# Cluster topics and build living wiki pages and platform behaviors
uv run trainertwin-pipeline --user <slug> build --model openai/gpt-4o --max-calls 80

# Compile offline behavioral analysis and timeline reports
uv run trainertwin-pipeline --user <slug> analyze
```

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
