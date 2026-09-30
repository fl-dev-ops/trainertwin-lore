# TrainerTwin research pipeline

Extract three distinct, source-backed products from public content:

1. **Knowledge & methods:** claims, goals, prerequisites, ordered steps, constraints, exceptions.
2. **Teaching & interaction cases:** situation, learner cue, diagnosis, strategy, stated rationale, response, outcome.
3. **Expression examples:** observable wording, structure, tone and rhetorical moves, with original context.

Unknown information stays null/empty. A recorded exchange is not the same as a narrated exchange or illustration. Exact quotations establish source occurrence, not semantic entailment, external truth, or trainer likeness.

```text
read-only sources
  → original snapshots + bounded citation units
  → one source-local extraction → three typed record products
  → optional cached organization (episodes, named mentions, canonical topic aliases)
  → linked wiki: topics / entities / methods / episodes / expression / sources
  → attributed twin observations + separately labeled proposed adaptations
  → offline task-conditioned context / compiled research report
  → optional field-level model audit + explicit human review
```

## Start safely

There is one implementation in `pipeline/` and one normal workspace per user: `users/<slug>/workspace/`. Update this code in place; use Git history for rollback, not parallel pipeline copies.

Stored-data format checks prevent incompatible records from being misread. If a workspace needs new extraction, run `ingest` again in that same workspace before building. Old flat cards cannot recover details they discarded. Sources and review history are preserved; no separate version-named workspace is required.

```sh
uv sync
# Set OPENROUTER_API_KEY in .env; --model overrides OPENROUTER_MODEL.

# Inspect parsing first; no API calls or ingestion writes.
uv run python -m pipeline --user olga ingest --dry-run --include 'linkedin/posts/*.md' --limit 3

# Bounded end-to-end ingestion → wiki → twin → report → validation.
# Replace/add --author with exact aliases actually present in source metadata.
uv run python -m pipeline --user olga run --author olgasi \
  --model openai/gpt-4o --max-calls 20
```

Defaults are `users/<slug>/data` and `users/<slug>/workspace`, selected by `--user` (default `olga`). Explicit `--data` and `--workspace` must be supplied together and must be separate, non-nested directories.

`--max-calls` is a shared **per-invocation logical request cap**, including repairs. HTTP retries can make additional network requests. For spend control, add `--max-usd` with explicit `--input-price` and `--output-price` (USD per million tokens). The persistent ceiling in `work/spend.json` counts spending/reservations since this budget was first enabled, across subsequent commands using it—not historical billing before it was enabled. Raise that ceiling explicitly to extend it. Every HTTP attempt reserves a conservative input-byte bound plus `--max-output-tokens` (default 8192) before dispatch. Known provider cost settles the reservation; interrupted/unknown requests retain it. Provider pricing must not exceed your supplied rates; this is not an external billing guarantee.

Use `plan` before approving calls. It requires no API key and distinguishes cached, pending, failed, and blocked windows. Add token prices for conservative cost estimates and `--seconds-per-call` for a measured-rate ETA; unknown estimates stay null. Topic grouping and additional HTTP retries are not included in source-window totals.

## Individual stages

Use the same `--user SLUG` (or explicit `--data … --workspace …`) prefix for every command:

| Command | Purpose | Model calls |
| --- | --- | --- |
| `status` | Source completeness, stale revisions, and durable work states | None |
| `plan --stage ingest\|organize --model …` | Offline source/window/cache/cost preflight | None |
| `audit-grounding` | Strict read-only check of stored evidence, including legacy fuzzy quotations | None |
| `ingest --model … --max-calls N` | Extract and validate all three products; resume from cache | Budgeted |
| `build` | Render the linked wiki from existing records and any completed organization | None |
| `organize --model … --max-calls N` | Organize selected ingested sources into episodes/entities, group topic aliases, then rebuild the wiki | Budgeted |
| `browse [QUERY]` | Find wiki entries using kind/platform/activity/part/role filters | None |
| `twin --author ALIAS --model … --max-calls N` | Build attributed observation/adaptation candidates after `build` | Budgeted |
| `analyze` | Compile current wiki and optional twin into `reports/analysis.md` | None |
| `context 'QUESTION' --author ALIAS` | Emit a task-conditioned JSON packet | None |
| `audit --model … --max-calls N` | Diagnose source support for every supplied substantive field | Budgeted |
| `review --record-id ID --status supported --note '…'` | Append a human source-support review | None |
| `verify --evidence-id ID --status verified --url URL --note '…'` | Append scoped human external review of a claim/self-report | None |
| `lint` | Check records, source freshness, generated files and links | None |

`ingest` and `run` accept repeated `--include` globs and `--limit`. `ingest`, `run`, and `twin` accept `--dry-run`; `run --dry-run` inspects source parsing only. `twin` also accepts `--max-sources`, repeated `--author`, and `--reviewed-only`. `--chunk-chars` bounds extraction windows or downstream batch items; a complete downstream example larger than the limit fails rather than being silently trimmed. Increase the limit explicitly.

`context` accepts `--platform`, `--as-of YYYY-MM-DD`, `--max-records`, `--max-chars`, and `--reviewed-only`. It uses lexical relevance, returns the products separately with original source spans, preserves complete selected records, and abstains if nothing fits/matches. It is not semantic retrieval or a runtime chatbot. Undated sources are excluded when an as-of filter is supplied.

`audit --record-id ID` can be repeated to select records. Audit responses must cover every field exactly once. Model verdicts remain diagnostics and do not mark records as human-reviewed or automatically remove them.

## Structured wiki pilot

Organization does not re-ingest sources, replace extraction records, generate a persona, or rebuild reports. Select ingested files with repeated `--include` globs; successful calls are cached and an identical rerun needs zero new calls. Each fully processed source is checkpointed before moving on, so later failures retain completed source organization. The wiki renders once when the stage exits, including ordinary budget/provider failures, rather than after every source. Hard kills may leave a stale wiki; `build` restores it from completed checkpoints. Unchanged files are not rewritten. Invalid source organization is rejected and logged, then later sources continue; the command still exits unsuccessfully if any source failed. Provider and budget failures stop immediately. If the topic pass is incomplete, original labels remain navigable and coverage marks topic organization incomplete.

```sh
uv run python -m pipeline --user vasanth organize \
  --include 'youtube/video/*2026-06-09*' \
  --model openai/gpt-4o --chunk-chars 60000 --max-calls 8
uv run python -m pipeline --user vasanth browse --kind episodes --activity teaching
uv run python -m pipeline --user olga browse --kind sources --part caption
uv run python -m pipeline --user olga lint --wiki-only
```

Start at `workspace/wiki/index.md`. Each of the six entry directories has an index; `catalog.json` supplies machine-readable links and metadata. Topic pages group aliases and show methods, episodes, named mentions, and original records. Method/expression pages are source-local variants, not automatically merged behavioral patterns. Source pages expose the original citation passages plus captured Markdown titles, descriptions, omitted hashtags, and comments as distinct parts. Numeric voices and third-party comments never inherit publisher identity.

`organize` processes whole units in bounded, single-content-part windows; captions, descriptions, transcripts, and comments never share a model window. Separating parts can require more calls than text-size chunking alone; `organize --dry-run` shows the actual window count. Episodes from multi-window sources are explicitly marked `source_window`, not complete-session analysis. Activity and role labels remain unreviewed. Unsupported optional entity candidates are omitted and counted in coverage; unsupported episode evidence still fails its source. Entity mentions do not establish relationships. People/projects remain source-scoped; other equal names are grouped as mention labels, not verified identity resolution. Coverage reports which sources have not been organized. Source changes suppress stale episodes/entities until reorganization.

`browse` supports `--kind`, `--platform`, `--activity`, `--part`, `--role`, and `--limit`. Activity/role filters select organized episodes; absence of a match is not proof of absent behavior. This is navigation, not a report generator. Normal `lint` still reports stale downstream reports; `lint --wiki-only` deliberately checks only source/wiki integrity while reports remain a later step.

## Resumption and grounding migration

```sh
# Read-only, no network calls:
uv run python -m pipeline --user olga audit-grounding
uv run python -m pipeline --user olga plan --stage ingest --model openai/gpt-4o
uv run python -m pipeline --user olga plan --stage organize --model openai/gpt-4o --chunk-chars 60000
uv run python -m pipeline --user olga status
uv run python -m pipeline --user olga lint --wiki-only --require-complete
```

- `work/<operation>/<key>.json` tracks pending/completed/failed/blocked requests. Source checkpoints live in `work/{ingest,organize}_sources/`. Failed validation is not automatically paid for again: use `--retry-failed` deliberately. Budget/provider-blocked and interrupted work can resume, reusing validated windows.
- `rejected/<operation>/` keeps failed requests/responses for offline diagnosis, never as serving evidence. Item-local repairs send only failed items and relevant source units; valid sibling items are preserved, and the complete result is revalidated. At most one repair per window per attempt.
- `usage.jsonl` includes request duration, source ID and request key. `timings.jsonl` separates wiki validation and rendering time. `status` and `lint` distinguish completeness from artifact integrity; `--require-complete` also requires linked-wiki organization and topic grouping.
- New extraction/organization requests select supplied citation span IDs. Code copies exact original quotations. Entity mentions select a bounded range of numbered source words; topic IDs are generated in code. Statements and activity/role labels still require semantic review.
- Stored quotations now require literal occurrence in their named unit after whitespace normalization; no fuzzy matching, capitalization correction, omitted negations, or invented ellipses. Existing evidence is **not rewritten or silently approved**. Run `audit-grounding` first: it lists incompatible records without changing them. New prompt/schema signatures intentionally have distinct cache keys; old caches and snapshots remain on disk. A full `ingest` using the new contract may therefore require new calls—inspect `plan` before running it.

## Sources and attribution

Supported: Markdown/text, CSV text, JSON/JSONL, YAML, collector transcript turns and diarized entries. Hidden files, symlinks, binaries and recognized collection indexes are excluded. Generic structured documents use text-leaf flattening, not a complete platform adapter.

- Preserve decoded originals, original passages, all nonempty turns (including **“Never.”**), locators, timestamps, supplied metadata and normalized content-family hashes.
- Citation units are bounded to 800 characters and retain exact offsets into their original passage. Extraction includes adjacent units; contiguous record context is reconstructed without rewriting its wording. Complete passages remain in snapshots even when a record uses only a span.
- Every substantive extracted field carries citations. A bad window receives at most one budgeted repair; persistent failure activates no partial source revision. Explicitly empty extraction is recorded as empty, not disguised as missing processing.
- Written authorship does not identify the speaker of quoted dialogue. Numeric diarization IDs never establish identity. No objection-keyword rules reinterpret literal statements.
- Twin generation requires explicit aliases, normalized only for whitespace, case and a leading `@`. Spoken examples require supplied speaker mappings; a channel owner is not assumed to speak every turn. Role-play is excluded from personal-behavior examples.
- Author-filtered spoken knowledge requires all cited speech to be explicitly attributed to the requested aliases. Unknown or mixed attribution is withheld, not guessed.

Optional `data/.source-metadata.yaml` (illustrative identities only):

```yaml
youtube/video/example.md:
  date: '2026-09-01'
  url: https://www.youtube.com/watch?v=EXAMPLE
  format: qa
  speakers:
    '1': interviewer-name
    '2': target-author-alias
```

Formats: `post`, `document`, `transcript`, `interview`, `qa`, `role_play`, `lesson`. Do not infer publication dates from filenames or identities from speaker numbers. Verify mappings before supplying them.

## Twin observations are not a personality certificate

The twin stage retains **all eligible case/expression records from selected publications**, deduplicates identical normalized content families, and balances selected publications across channels and dates. Actual selection/exclusion counts are reported; they are not confidence scores or extraction recall.

Each observation includes a dimension, source scope, situation, qualification, support/counterexample IDs and exact quotations. `interaction` requires recorded Q&A/interview cases; narrated cases can support appropriately qualified teaching-strategy observations, not claims of recorded interaction. Cross-platform `general` scope requires distinct content from multiple channels. Adaptations have their own `when`, `action`, and `limits`, explicitly marked **proposed, not observed**. Batches are not globally reconciled into a personality model.

## Storage, reviews and rebuilding

See [SCHEMA.md](SCHEMA.md) for the record contract. Source snapshots and record files are content-addressed; a final manifest activates a completed source revision. These preserve provenance and interrupted-run safety, not alternative pipeline implementations. Publication-only metadata corrections reuse interpretation caches when possible, but new record IDs prevent old human reviews silently transferring to new evidence.

Generated wiki/twin/audit/report directories have `build.json` receipts binding their files to inputs. Human/unmanaged files are not silently deleted; only obsolete files owned by an earlier receipt are pruned. CLI mutations use a single-writer lock. Direct library writers must use `storage.one_writer(workspace)`.

Human `review` statuses: `supported`, `unsupported`, `uncertain`. Unsupported records remain in history but are withheld from serving views. External `verify` statuses: `verified`, `contradicted`; these assertions retain their URL/note/date but are not automatically authenticated. Contradiction is shown, not silently converted into a different claim.

After ingestion/review changes, regenerate `build`, `twin` if used, `audit` if present, and then `analyze`. `lint` rejects stale/modified outputs. Do not edit generated Markdown; correct inputs or record a scoped review. Old `wiki/behavior/` and legacy summaries are not consumed as evidence.

## Verify without paid calls

```sh
uv run python -m pytest -q pipeline/tests social/tests
uv run python scripts/pipeline_demo.py --output /tmp/trainertwin-demo
```

The demo refuses an existing output directory. It builds all views, a twin candidate, field audits, task context and a report using **fixture-authored model responses**, asserts retained method/case details, then rebuilds with zero new calls. It is an integration check, not evidence of live extraction quality.

Research rationale: [TRAINERTWIN_RESEARCH.md](../docs/research/TRAINERTWIN_RESEARCH.md). The chronology preview uses the same current record reader. MCP feature work, collectors and the profile UI are outside this refactor.
