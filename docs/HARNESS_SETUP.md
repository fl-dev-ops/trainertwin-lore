# Harness Setup Guide — Interacting with TrainerTwin Lore

This guide explains how to connect **TrainerTwin Lore** to your preferred AI coding harness or desktop app (**Claude Desktop, Claude Code, Codex, OpenCode, Pi, Cursor, Windsurf, Zed**).

---

## The Interaction Architecture

```text
       ┌────────────────────────┐
       │          User          │
       └───────────┬────────────┘
                   │  "Collect Olga's LinkedIn posts and summarize her decision rules"
                   ▼
       ┌────────────────────────────────────────────────────────┐
       │   AI Harness (Claude / Codex / OpenCode / Pi / Cursor)  │
       └───────────────────────────┬────────────────────────────┘
                                   │  Model Context Protocol (JSON-RPC over stdio)
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │           TrainerTwin Lore MCP Server (FastMCP)         │
       └─────┬─────────────────────┼──────────────────────┬─────┘
             │                     │                      │
             ▼                     ▼                      ▼
    [ Social Scrapers ]    [ TypeSafe Jev Gate ]   [ Living Wiki & Reports ]
    • LinkedIn (Harvest)   • Repost Filter (<0.35) • evidence/*.jsonl
    • YouTube (yt-dlp)     • Comment Cutoff        • wiki/topics/*.md
    • Twitter/X (Twitter)  • Roleplay Tagging      • reports/analysis.md
    • Instagram (Apify)                            • reports/persona-prompt.md
```

---

## 1. Quick Harness Configuration

### A. Pi Coding Agent (`pi`)
Add to `~/.pi/agent/mcp.json` (global) or `.pi/mcp.json` (project-local):
```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": ["run", "trainertwin-mcp"],
      "cwd": "/absolute/path/to/trainertwin-lore"
    }
  }
}
```

### B. Claude Code (CLI)
Run in your terminal:
```bash
claude mcp add trainertwin-lore uv --directory /absolute/path/to/trainertwin-lore run trainertwin-mcp
```

### C. Claude Desktop
Add to your Claude Desktop configuration file:
* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": ["run", "trainertwin-mcp"],
      "cwd": "/absolute/path/to/trainertwin-lore",
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-..."
      }
    }
  }
}
```

### D. OpenCode / Codex
Add to your project's `opencode.json` or Codex configuration:
```json
{
  "mcp": {
    "servers": {
      "trainertwin-lore": {
        "command": "uv",
        "args": ["run", "trainertwin-mcp"],
        "cwd": "/absolute/path/to/trainertwin-lore"
      }
    }
  }
}
```

### E. Cursor / VSCode
Add to `.cursor/mcp.json` or `.vscode/mcp.json`:
```json
{
  "mcpServers": {
    "trainertwin-lore": {
      "command": "uv",
      "args": ["run", "trainertwin-mcp"],
      "cwd": "/absolute/path/to/trainertwin-lore"
    }
  }
}
```

---

## 2. Tools Available to the Harness

| Tool | Purpose | Example Natural Language Trigger |
| :--- | :--- | :--- |
| `collect_social` | Scrapes public posts from LinkedIn, YouTube, Twitter/X, and Instagram since a specific UTC date. | *"Scrape Olga's LinkedIn posts from 2026-08-01 onwards."* |
| `run_ingest` | Chunks sources, extracts verbatim evidence cards, and filters reposts with TypeSafe Jev. | *"Ingest the new YouTube transcripts for Olga."* |
| `build_wiki` | Clusters topics and synthesizes living wiki topic pages & platform behavioral profiles. | *"Rebuild the living wiki for user olga."* |
| `analyze_persona` | Compiles `analysis.md` and `timeline.md` offline without API calls. | *"Compile the persona analysis report for Olga."* |
| `read_report` | Directly reads `analysis.md`, `timeline.md`, or `persona-prompt.md`. | *"Show me Olga's communication style and tropes from the analysis report."* |
| `get_wiki_topic` | Inspects specific topic syntheses or platform behaviors (`linkedin`, `youtube`, `instagram`, `twitter`). | *"What does Olga's wiki say about client objection handling?"* |
| `lint_workspace` | Audits evidence card hashes, citations, and locators offline. | *"Run a lint check on Olga's corpus to verify attribution."* |
| `get_status` | Inspects source files, ingested manifests, and stale documents. | *"What is the ingestion status for Olga?"* |
| `run_full_persona_pipeline` | Automates the entire cycle: Social Collection $\to$ Ingest $\to$ Build $\to$ Analyze. | *"Run the full persona pipeline for John Doe on LinkedIn since 2026-08-01."* |

---

## 3. Direct MCP Resources

Your harness can directly read living lore via MCP URIs without executing code:
* `trainertwin://users/{user}/analysis` — Full behavioral and persona report.
* `trainertwin://users/{user}/overview` — Living wiki cross-topic synthesis.
* `trainertwin://users/{user}/persona-prompt` — Production-ready digital twin system prompt.

---

## 4. Example Conversations to Test

### Example 1: Inquiring about a Trainer's Behavior
> **User**: *"How does Olga adapt her communication style between LinkedIn and YouTube?"*  
> **Harness**: *Calls `get_wiki_topic(user='olga', topic_slug='linkedin')` and `get_wiki_topic(user='olga', topic_slug='youtube')`.*  
> **Harness**: Summarizes Olga's shift from short, punchy 1-2 sentence line-break frameworks on LinkedIn to didactic roleplays with simulated client objections on YouTube.

### Example 2: Verifying Authenticity & Attribution
> **User**: *"Did Olga actually say 'I only invest in prime central London real estate'?"*  
> **Harness**: *Calls `read_report(user='olga', report_name='analysis')` and queries evidence cards.*  
> **Harness**: Verifies that Olga focuses exclusively on Dubai and UAE off-plan and secondary investments, flagging London claims as a hallucination not present in the 2,755 verified cards.

### Example 3: End-to-End Extraction for a New Trainer
> **User**: *"I have a new trainer Jane Doe. Can you scrape her LinkedIn posts at https://www.linkedin.com/in/janedoe/ since 2026-08-01 and build her persona wiki?"*  
> **Harness**: *Calls `run_full_persona_pipeline(user='jane-doe', since='2026-08-01', linkedin='https://www.linkedin.com/in/janedoe/')`.*  
> **Harness**: Returns a summary of the collected posts, ingested evidence cards, and synthesized behavioral profile.
