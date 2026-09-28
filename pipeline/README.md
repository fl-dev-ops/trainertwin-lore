# Source-grounded living wiki

Each person's files live together under `users/<slug>/`: curated `data/<channel>/` and generated `workspace/{wiki,reports,cache,...}/`. The pipeline recursively reads only that person's `data/` and maintains a separate wiki and reports. Default `--user olga` uses the migrated Olga corpus; use a lowercase slug such as `jane-doe` for another person. It accepts `.md`, `.markdown`, `.txt`, `.csv`, `.json`, `.jsonl`, `.yaml`, and `.yml`; it ignores binaries, hidden files, and metadata-only documents. Source files are never edited.

## Run

```sh
uv sync
# Set OPENROUTER_API_KEY in .env; optionally OPENROUTER_MODEL.
uv run python -m pipeline status
uv run python -m pipeline ingest --dry-run --include 'youtube/transcripts/06.yaml' --include 'linkedin/posts/2026-09-21-which-problem-do-you-solve.md'
uv run python -m pipeline ingest --model openai/gpt-4o --max-calls 20 --include 'youtube/transcripts/06.yaml' --include 'linkedin/posts/2026-09-21-which-problem-do-you-solve.md'
uv run python -m pipeline build --model openai/gpt-4o --max-calls 80
uv run python -m pipeline lint
uv run python -m pipeline analyze  # offline; writes users/olga/workspace/reports/{analysis,timeline}.md
```

For an **Olga-only offline chronology preview**, run `uv run python -m pipeline.chronology` and open `users/olga/workspace/chronology.html` (or view `chronology.svg`). The hand-selected `pipeline/pilot-sources.txt` controls this preview; it joins source publication metadata to existing evidence JSONL when available, and shows unextracted sources explicitly. It needs no built wiki or API key. It is a sample, not a frequency chart of Olga's complete history. A selected YouTube transcript with no verified publication URL/date is withheld rather than paired with an older title-to-video mapping; the preview reports omissions.

For another person, collect into their folder and select it for every pipeline command. The unified date-bounded collector is documented in [`social/README.md`](../social/README.md):

```sh
uv run python -m social --user jane-doe --since 2026-08-01 --linkedin 'https://www.linkedin.com/in/janedoe/' --youtube 'https://www.youtube.com/@janedoe'
uv run python -m pipeline --user jane-doe status
uv run python -m pipeline --user jane-doe ingest --model openai/gpt-4o --max-calls 20
uv run python -m pipeline --user jane-doe build --model openai/gpt-4o --max-calls 80
uv run python -m pipeline --user jane-doe analyze
uv run python -m pipeline --user jane-doe lint
```

All four collection tools accept `--data-dir users/<slug>/data/<channel>`; YouTube also needs `--audios-dir users/<slug>/audios` for download/transcription. Omit `--user` only for Olga. `--include` accepts repeatable data-root-relative globs; without it, ingestion scans every supported research file in that person's `data/`. Advanced callers can override both roots together with `--data PATH --workspace PATH`. A separate workspace per corpus prevents cache, evidence, and report mixing; one lock guards each workspace independently. `analyze` retains Olga's curated persona intro only for `--user olga`; for other users it produces source-backed wiki findings, **not** an automatically inferred persona prompt. Write/review a persona specification separately before using it. `--dry-run`, `status`, and `lint` make **no API calls**. The `--max-calls` budget limits new logical requests per invocation, not provider-side retries or billing. Requests are resumable per chunk; rerun after a budget limit. Use a model/provider supporting OpenRouter strict structured output.

## How pages update

- Each source is fingerprinted by content and path; citations reference exact source units (Markdown line range, JSON pointer, or transcript turn and timestamp). Evidence records also carry `published_at` (ISO date/datetime or null), `source_url`, `author`, and `date_basis` (`source`, `sidecar`, or `unknown`). These are **publication** dates, not event dates or ingestion time. A snippet match is **not** external verification. Long values are whitespace-normalized and split into bounded units.
- The latest committed evidence version is authoritative. A changed source replaces its active cards only on successful extraction. An LLM topic map merges synonymous labels across channels (`wiki/topic-map.json`) before synthesis. The current topic page is editorial context for a new version; **only current evidence IDs may support the new page**. Unaffected topics are reused.
- `users/<slug>/data/.source-metadata.yaml` is an optional hidden path-to-metadata map for files like YouTube transcripts that lack publication data. Set `date`, `url`, `id`, `author` by relative path; record how externally obtained dates were checked (e.g. in YAML comments). Missing dates stay unknown. Updating metadata invalidates the completed evidence version but reuses cached text extraction without additional extraction calls.
- `wiki/timeline.md` lists dated sources in publication order and undated sources separately. `wiki/topics/*.md` joins related evidence across channels. `wiki/categories/{behavior,methods,knowledge,offers}.md` and `wiki/channels/*.md` are navigation; `wiki/sources/*.md` expose per-file citations. `wiki/index.md`, `wiki/overview.md`, and append-only `wiki/log.md` complete the wiki. **`build` does not write a report.** `analyze` compiles `workspace/reports/analysis.md` from wiki Markdown without an API call or new reasoning (plus Olga's existing curated intro when selecting Olga), and a separate `reports/timeline.md`. Lint marks the report stale if wiki pages change. Do not manually edit generated pages: use reviewed source corrections or `verifications.jsonl` (see `SCHEMA.md`).
- Invalid quotes or IDs are retried once; remaining unsupported individual items are dropped and logged as `rejected-item`, never published as evidence. Review the log for gaps. A raw transcription JSON and its cleaned YouTube YAML can both be discovered; they are **not independent corroboration**. For focused analysis, select the canonical copy with `--include`. New files do not enter the wiki until ingested.

### External fact review

```sh
uv run python -m pipeline verify --evidence-id '...' --status verified \
  --url 'https://example.org/primary-source' --note 'What was checked and when'
uv run python -m pipeline build --model openai/gpt-4o
uv run python -m pipeline analyze
```

`verify` records a **human assertion**, never automatically checks a URL. The generated wiki is a research draft, not a certified biography or a claim about unobserved private behavior. Refer to `SCHEMA.md` for evidence rules and caveats.

## Checks

```sh
uv run ruff check pipeline
uv run ruff format --check pipeline
uv run python -m pytest -q pipeline/tests
```

Tests use a fake model and a mocked HTTP client; no key or paid calls are needed.
