# TrainerTwin Lore

Extract public posts, transcripts, and writings to generate source-grounded behavioral persona prompts (`SKILL.md`) for AI digital twins.

---

## Architecture Flow

```text
[ Social Collectors ] (YouTube transcripts, LinkedIn, Instagram, X)
        │
        ▼
users/<slug>/data/ (Raw, immutable source files)
        │
        ▼ (Stage 1: Indexing — Gemini 3.8 Flash)
users/<slug>/workspace/index.json
  ├── Deterministic landmarks & line coordinates (start_line, end_line ≤ 100)
  ├── 500-character verbatim quote previews
  ├── Adjacency pointers (prev, next) for small-to-big context expansion
  └── Multi-axial facets: topic, situation, activity
        │
        ▼ (Stage 2: Normalization — TypeSafe Jev)
users/<slug>/workspace/taxonomy.json
  ├── Dynamic LLM domain background stopword detection (0 hardcoded terms)
  └── High-speed parallel Jev clustering into canonical concepts + aliases
        │
        ▼ (Stage 3: Scenario Retrieval — Jev Choice Routing)
Matched 3–5 Grounded Source Clips
  ├── Jev choice decision over canonical situations
  └── Set-utility diversification (max 2 clips per source file)
        │
        ▼ (Stage 4: Prompt Authoring — Gemini 3.8 Flash)
users/<slug>/workspace/scenarios/<scenario-slug>.md (SKILL.md)
  ├── YAML Frontmatter (name, description, activation triggers)
  ├── Adult-to-Adult relational stance & power dynamics
  ├── Verbatim signature phrases & cadence bounds (2–4 sentences per turn)
  ├── Priority-ordered decision heuristics (Trigger → Action → Avoid)
  ├── Exact file path and line citations
  └── Negative boundaries ("What the persona NEVER does")
        │
        ▼ (Stage 5: Adversarial Audit — Dual-Model Validation)
Validation Scorecard (Citations integrity, zero-hallucination check)
```

---

## Installation & Setup

### Prerequisites
* Python 3.12+
* [uv](https://github.com/astral-sh/uv) package manager

### 1. Clone & Sync
```bash
git clone https://github.com/foreverlearning/trainertwin-lore.git
cd trainertwin-lore
uv sync
```

### 2. Environment Setup
Copy the template and configure your OpenRouter API key:
```bash
cp .env.example .env
```
Ensure `.env` contains:
```bash
OPENROUTER_API_KEY=sk-or-v1-...
```

---

## CLI Usage (5 Stages)

### 1. Collect Social Sources
Extract date-bounded posts and video transcripts into `users/<slug>/data/`:
```bash
# Only specify the platforms you need
uv run trainertwin-social --user olga --since 2026-08-01 \
  --youtube 'https://www.youtube.com/@olga_sinenko' \
  --linkedin 'https://www.linkedin.com/in/olgasi/'
```

### 2. Index & Prepare Corpus (Indexing + Auto-Normalization)
Index raw transcripts into `index.json` with multi-axial facets and automatically cluster canonical taxonomy concepts in `taxonomy.json`:
```bash
# Dry run to inspect planned segmentation without paid calls
uv run trainertwin-pipeline --user olga index --dry-run

# Run full parallel indexing (8 workers on Gemini 3.8 Flash)
# Automatically normalizes tags into taxonomy.json at the end
uv run trainertwin-pipeline --user olga index --workers 8

# (Optional) Re-cluster taxonomy without re-indexing source files:
uv run trainertwin-pipeline --user olga normalize
```

### 3. Query Grounding Clips
Search the catalog by scenario to retrieve the top 3–5 grounded clips:
```bash
uv run trainertwin-pipeline --user olga query "How does Olga handle a client who says 'I will wait until prices crash'?"
```

### 4. Author & Validate SKILL.md Prompts
Synthesize a deployable `SKILL.md` runtime prompt and run an adversarial grounding audit:
```bash
# Author the scenario prompt
uv run trainertwin-pipeline --user olga author "Client says: 'I will wait until prices crash before buying'"

# Run adversarial audit against source lines
uv run trainertwin-pipeline --user olga validate client-says-i-will-wait-until-prices-crash-before-buying.md
```

---

## MCP Server Installation

The Model Context Protocol (MCP) server runs over `stdio` and complies with the latest `mcp v2.2.0` specification. It allows any MCP host to query the catalog, retrieve grounded clips, author prompts, and validate persona skills.

### Direct Test / Launch
```bash
uv run trainertwin-mcp
```

### Host Configurations

#### 1. Claude Desktop (`claude_desktop_config.json`)
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ABSOLUTE/PATH/TO/trainertwin-lore",
        "trainertwin-mcp"
      ],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-..."
      }
    }
  }
}
```

#### 2. Cursor (`.cursor/mcp.json` or Settings → MCP)
```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ABSOLUTE/PATH/TO/trainertwin-lore",
        "trainertwin-mcp"
      ],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-..."
      }
    }
  }
}
```

#### 3. Claude Code CLI
```bash
claude mcp add trainertwin-lore -- uv run --directory /ABSOLUTE/PATH/TO/trainertwin-lore trainertwin-mcp
```

#### 4. Pi Coding Agent (`~/.pi/agent/mcp.json`)
```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ABSOLUTE/PATH/TO/trainertwin-lore",
        "trainertwin-mcp"
      ],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-..."
      }
    }
  }
}
```

---

## Offline Unit Testing

Run all unit tests across indexing, normalization, retrieval, authoring, and validation:
```bash
uv run python -m pytest -q pipeline/tests
```
