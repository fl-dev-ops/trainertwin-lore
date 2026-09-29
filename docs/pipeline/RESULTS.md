# Pipeline implementation and validation

## One current implementation

- Runtime code lives in `pipeline/`; update it in place and use Git for rollback.
- Normal commands use `--user SLUG` and `users/<slug>/workspace/`. Incompatible stored records are re-extracted in that same workspace, not routed to another pipeline.
- `scripts/pipeline_demo.py` runs an offline fixture demonstration. `scripts/run_pipeline_pilot.py` always imports the current repository code; it no longer accepts a code-version selector.
- Frozen implementation copies, the obsolete comparison probe and the retired auto-iteration runner were removed. Past evaluation measurements remain under `docs/research/pipeline-evaluation/` and `.auto-iterate/`; they are research records, not runnable implementations. Paid-run meter/history files are preserved.
- Schema markers, source hashes, immutable source revisions and artifact receipts remain: these prevent stale-data interpretation and partial publication, not select alternate code.

## Implemented behavior

Three distinct cited products cover knowledge/methods, teaching/interaction cases, and expression examples. The wiki renders their fields deterministically, without a second LLM paraphrase. Twin observations and proposed adaptations remain separate. Offline context retrieval preserves complete selected records; field-level model audits are distinct from human reviews.

All source formats use one record validator. The chronology display uses the same current record reader, not a legacy card branch. Per-field citations, explicit speaker attribution, unknown rationales/outcomes, preserved short turns, review exclusions, cache/resume and artifact freshness are covered by regression tests.

## Validation evidence

**63 tests passed.** Ruff, formatting, compilation, source parsing and the offline end-to-end demo passed. The demo produced eight records across all three products and rebuilt with zero new fixture-model calls. No paid calls were made.

- [`tests.txt`](tests.txt): pipeline and collector regression results, including same-workspace rebuilding, no legacy chronology fallback, and a persistent pilot call cap across reruns. Pilot tests mock the API client.
- [`lint.txt`](lint.txt): Ruff checks and formatting for the 16 active pipeline/test/script files in this check.
- [`demo.txt`](demo.txt): offline end-to-end fixture run, plus a cached rebuild with zero additional fixture-model calls.
- [`parser-dry-run.txt`](parser-dry-run.txt): parsing three posts through the normal `--user olga` CLI, without ingestion writes or model calls.
- Compilation: `python -m compileall -q pipeline scripts`.

No paid API calls are needed for these checks. The fixture audit verdicts are authored test output, not independent evidence of source support.

## Inspect or reproduce

The generated demonstration is under `.pi/pipeline-demo/`:

- `workspace/wiki/index.md` and `workspace/wiki/{knowledge,cases,expression}.jsonl`
- `workspace/twin/profile.md`
- `workspace/audit/report.md` and `workspace/reports/analysis.md`
- `context.json` and `result.json`

```sh
uv run python -m pytest -q pipeline/tests social/tests
uv run python scripts/pipeline_demo.py --output /tmp/trainertwin-demo
```

Use a new **demo output directory**, since the fixture generator refuses to overwrite existing files. This is test isolation, not a second implementation or a requirement to create versioned user workspaces. For real ingestion, use the normal commands in `pipeline/README.md`.

## Limits

These checks verify contracts, attribution/budget safeguards, retained extracted details and end-to-end machinery. They do not establish live-model extraction recall, semantic entailment, external truth or trainer resemblance. Those require annotated real-source targets and separately metered live evaluation; no synthetic score improvement is claimed.

Lexical retrieval, excerpt-sized extraction, generic structured-text flattening, exact-content deduplication and independent twin batches retain known limits. Per-invocation CLI budgets count logical requests, not HTTP retries or spend. Existing user data/workspaces, MCP code, the profile UI and collector implementation are untouched by this cleanup.
