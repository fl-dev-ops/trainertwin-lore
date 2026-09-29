# TrainerTwin Lore

Turn public posts, transcripts and writings into source-grounded knowledge, teaching cases and communication examples for TrainerTwin.

**One pipeline:** the implementation lives in `pipeline/`, writes to `users/<slug>/workspace/`, and is updated in place. Git holds code history; there are no separate runnable pipeline versions.

## Flow

```text
social collectors → users/<slug>/data/
  → preserved originals + cited source records
      ├── knowledge & methods
      ├── teaching & interaction cases
      └── expression examples
  → deterministic wiki
  → attributed twin observations + separately labeled proposed adaptations
  → task-conditioned context, research report, optional audits/reviews
```

The pipeline preserves method steps, constraints and short answers. Unknown rationales/outcomes stay unknown. Speaker identity requires explicit metadata, never a guess from diarization numbers. A quotation proves source occurrence, not semantic entailment or external truth; the output is not a verified personality or runtime chatbot.

## Setup

Python 3.12+ and [uv](https://github.com/astral-sh/uv):

```sh
uv sync
cp .env.example .env
```

Set `OPENROUTER_API_KEY` for ingestion, twin generation and optional model audits. Pass `--model` or set `OPENROUTER_MODEL`. Build, context selection, report compilation, integrity checks and dry runs make no model calls. Collector credentials are documented in [social/README.md](social/README.md).

## Collect and process

```sh
# Only specify the platforms you need.
uv run python -m social --user jane-doe --since 2026-08-01 \
  --linkedin 'https://www.linkedin.com/in/janedoe/'

# Inspect source parsing without paid calls.
uv run python -m pipeline --user jane-doe ingest --dry-run

# Ingest → build → twin → report → validate, with one shared logical call cap.
# --author must match explicitly supplied source/speaker metadata.
uv run python -m pipeline --user jane-doe run --author janedoe \
  --model openai/gpt-4o --max-calls 20

# Offline retrieval and checks.
uv run python -m pipeline --user jane-doe context 'How should I structure this exercise?'
uv run python -m pipeline --user jane-doe lint
```

Interrupted/budget-limited ingestion retains validated caches; rerun the same command to resume. The call cap is per invocation and counts logical requests, not HTTP retries or spend. Re-extract incompatible stored records in the same workspace before rebuilding; sources and human review history are preserved.

See [pipeline/README.md](pipeline/README.md) for individual stages, budgets, attribution, reviews and workspace behavior, and [pipeline/SCHEMA.md](pipeline/SCHEMA.md) for the data contract. Collection and existing MCP entry points are separate integrations, not alternative pipeline implementations.

## Verify offline

```sh
uv run python -m pytest -q pipeline/tests social/tests
uv run python scripts/pipeline_demo.py --output /tmp/trainertwin-demo
```

The demo uses fixture-authored responses and makes no paid calls. It checks the full flow and retained details, not live-model quality or trainer resemblance.

- [Current validation results](docs/pipeline/RESULTS.md)
- [Research rationale](docs/research/TRAINERTWIN_RESEARCH.md)
