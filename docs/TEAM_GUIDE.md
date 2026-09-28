# TrainerTwin Lore — Team Testing & Feedback Guide

Welcome to the **TrainerTwin Lore** test suite! This guide explains how to run, test, and provide feedback on the source-grounded persona extraction and living wiki engine.

---

## 1. Quick Start (5 Minutes)

### Prerequisites
- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/) (Astral's fast Python package manager):
  ```bash
  # macOS / Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation
```bash
git clone https://github.com/fl-dev-ops/trainertwin-lore.git
cd trainertwin-lore
uv sync
```

### Configure Credentials
Copy the template and fill in your keys:
```bash
cp .env.example .env
```
* **Required for Pipeline & Wiki**: `OPENROUTER_API_KEY`
* **Optional (for collecting new data)**: `HARVEST_API_KEY` (LinkedIn), `TWITTER_API_KEY` (Twitter/X), `APIFY_API_KEY` (Instagram), `SARVAM_API_KEY` (YouTube transcription).
*(If you just want to test querying and analyzing Olga's pre-ingested corpus, you only need `OPENROUTER_API_KEY`!)*

---

## 2. Using with Pi Coding Agent (Harness)

You can use TrainerTwin Lore with any Pi harness in two ways:

### Option A: MCP Server (Recommended)
Add TrainerTwin Lore to your Pi configuration (`~/.pi/agent/mcp.json` or project `.pi/mcp.json`):

```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": ["run", "trainertwin-mcp"],
      "cwd": "/path/to/trainertwin-lore",
      "env": {
        "OPENROUTER_API_KEY": "your-key-here"
      }
    }
  }
}
```

Once configured, Pi will automatically have access to these tools:
- `get_status(user)` — Check source and evidence counts.
- `lint_workspace(user)` — Offline integrity audit.
- `read_report(user, report_name)` — Read `analysis.md`, `timeline.md`, or `persona-prompt.md`.
- `get_wiki_topic(user, topic_slug)` — Read living wiki topic syntheses or platform behaviors.
- `analyze_persona(user)` — Compile behavioral intelligence reports offline.
- `collect_social(...)` — Collect new trainer social content.
- `run_ingest(...)` & `build_wiki(...)` — Ingest sources and build living wikis.

**Example Prompts to Try in Pi:**
> *"What is Olga's communication style on YouTube vs LinkedIn?"*
> *"Audit the evidence cards for Olga and tell me if there are any lint errors."*
> *"Show me Olga's core decision heuristics from reports/analysis.md."*

---

### Option B: Pi Skill
To give Pi deep semantic knowledge of the workflow and CLI:
```bash
cp -r skills/trainertwin-lore ~/.pi/agent/skills/
```
Pi will automatically load the skill when you ask about TrainerTwin lore, persona extraction, or running the pipeline.

---

## 3. Using as a CLI Tool

TrainerTwin Lore installs standalone console binaries via `uv`:

### Ingest & Build the Wiki
```bash
# Ingest sources into evidence cards
uv run trainertwin-pipeline --user olga ingest --model openai/gpt-4o --max-calls 20

# Maintain living wiki & platform behaviors
uv run trainertwin-pipeline --user olga build --model openai/gpt-4o --max-calls 80

# Compile offline persona report
uv run trainertwin-pipeline --user olga analyze

# Audit integrity offline
uv run trainertwin-pipeline --user olga lint
```

### Collect New Social Profiles
```bash
uv run trainertwin-social --user my-trainer --since 2026-08-01 \
  --linkedin 'https://www.linkedin.com/in/username/' \
  --youtube 'https://www.youtube.com/@channel'
```

---

## 4. What to Test & Review

We specifically need feedback on:

1. **Attribution & Hallucination Guardrails**:
   - Check `users/olga/workspace/reports/analysis.md`.
   - Are client objections (e.g. *"I don't have time"*, *"Can you just send me options"*) properly identified as roleplay teaching moves, rather than Olga's personal beliefs?
2. **Platform Behavioral Nuance**:
   - Read `users/olga/workspace/wiki/behavior/linkedin.md` and `youtube.md`.
   - Does the analysis accurately capture formatting patterns, tone shifts, and content structures?
3. **Tool & MCP Usability**:
   - Did the MCP server connect cleanly in Pi?
   - Did tool descriptions and arguments feel intuitive?
4. **Speed & Latency**:
   - How fast did the offline commands (`lint`, `analyze`, `status`) respond?

---

## 5. Feedback Template

Copy and paste this into our team channel or PR with your notes:

```markdown
### TrainerTwin Lore Test Feedback
- **Tester**: [Your Name]
- **Environment**: [Pi / CLI / Cursor / Claude Code]
- **OS**: [macOS / Linux / Windows WSL]

#### Findings:
1. **Persona Analysis Accuracy**: (1-5 stars) — [Notes on tone and authenticity]
2. **MCP / CLI Ergonomics**: [Were commands/tools easy to run? Any setup issues?]
3. **Attribution Quality**: [Did you spot any misattributed quotes or comments?]
4. **Suggestions / Missing Features**: [What should we add or improve?]
```
