# Historical pipeline evaluation

This is a record of a completed experiment, not setup instructions or a maintained pipeline version. Frozen implementation copies and their runner have been removed; use Git for code history and `pipeline/` for execution. Original measurements and artifact paths below describe that past experiment.

## What was frozen before editing

- [Old flow and flaw ledger](BASELINE.md).
- [Baseline inventory and SHA-256 fingerprints](baseline-inventory.json).
- [Pre-change tests](baseline-tests.txt): 23 passed.
- Original Python implementation: `.pi/pipeline-v2/before/pipeline/`.
- Five unchanged pilot source files: `.pi/pipeline-v2/data/`.

The pre-existing data move into `users_backup/`, collector edits, HTML profile edits, and dependency changes were not reverted. Comparisons use separate local workspaces. `.pi/` artifacts are local/ignored; the records in this directory are the durable review summary.

## Same offline failure probes, before and after

Run by `scripts/pipeline_contract_probe.py`, using temporary fixtures and a fake model:

| Selected regression probe | Before | After |
| --- | --- | --- |
| No paid authorship decision at zero extraction budget | Fail | Pass |
| Preserve a short answer such as “Never.” | Fail | Pass |
| Do not rewrite a literal self-report from objection keywords | Fail | Pass |
| Enforce semantic entailment of statement from quote | Fail | **Still unresolved** |
| Reject mixed valid/invalid citation IDs | Fail | Pass |
| Require rebuilding after source re-ingestion | Fail | Pass |
| Invalidate interpretation after author changes | Fail | Pass |
| Retain the scope of human verification | Fail | Pass |

Machine-readable results: [before.json](before.json), [after.json](after.json).

**0/8 → 7/8 is not an overall application-quality score.** These are eight deliberately selected failure cases from the audit. Exact quote occurrence still cannot establish that an interpretation is correct; new cards explicitly carry `semantic_status: not_reviewed`.

The new regression tests additionally exercise original source snapshots, existing caption-only transcript compatibility, unchanged-chunk reuse, bounded synthesis repair, partial-ingestion diagnostics, malformed-file isolation, representative selection mechanics, repeated-content grouping, explicit target attribution, empty-persona behavior, and twin artifact freshness.

## Live smoke comparison

The live pilot uses **two** of the frozen files, both with declared LinkedIn author `olgasi`:

1. `linkedin/posts/2023-06-19-my-favourite-exercise-for-training.md`
2. `linkedin/posts/2026-01-19-why-i-never-tell-clients.md`

This small selection allows both complete flows to fit a bounded budget; it is not a cross-platform/persona-quality benchmark. The remaining frozen files are not silently ingested into either pilot.

- Provider/model: OpenRouter `openai/gpt-4o`.
- Persistent lifetime cap: 12 logical requests per version, including failed requests and reruns. HTTP retries are not a monetary cap.
- Before workspace: `.pi/pipeline-v2/before-workspace/`.
- After workspace: `.pi/pipeline-v2/after-workspace/`.
- Revised implementation is frozen separately under `.pi/pipeline-v2/after/` before live execution.
- Before: ingestion → old wiki/behavior build → report → lint.
- After: ingestion → knowledge wiki → separate twin stage (`--author olgasi`) → report → lint.
- Both runs record input/code hashes, stage outcomes, actual logical requests, provider usage and errors. A budget-limited run is incomplete, not a successful quality result.

Both live runs completed successfully and passed their respective lint checks. Results: [live-before.json](live-before.json), [live-after.json](live-after.json). Final tests: [after-tests.txt](after-tests.txt), **38 passed**. Ruff checks/format checks passed for the modified implementation, tests and comparison scripts. The current implementation's file hashes matched the frozen live-tested revision.

| Measured smoke-test result | Before | After |
| --- | ---: | ---: |
| Same selected source files | 2 | 2 |
| Input files unchanged | Yes | Yes |
| Active evidence cards | 7 | 12 |
| Original source/context snapshots | 0 | 2 |
| Knowledge topic pages | 3 | 4 |
| Old uncited platform behavior pages | 1 | 0 |
| Separate original twin examples | Not implemented | 2 |
| Cited, scoped twin patterns | Not implemented | 2 |
| Logical model calls | 8 | 9 |
| Prompt tokens | 8,193 | 13,952 |
| Completion tokens | 2,228 | 3,540 |
| Total tokens | 10,421 | 17,492 |
| Provider-reported usage cost | $0.0427625 | $0.07028 |
| End-to-end run time | 21.62 s | 29.85 s |
| Lint | Pass | Pass |

The revised run cost about 64% more in this one small trial. It extracted more cards and generated a separate cited artifact; **more cards are not proof of better recall, accuracy, or usefulness**. These timings are pipeline timings, not chat latency. Costs are returned provider usage metadata, not an audited billing statement. One unseeded LLM run per version is not a statistically controlled quality comparison.

A subsequent unchanged rerun of ingest, build, and twin used a model stub that fails on any attempted call: **zero new model calls**, unchanged usage log, and lint passed. See [resume-check.json](resume-check.json).

### Actual output review

The old behavior page produced broad provisional descriptions such as giving direct advice and using rhetorical questions, plus signature phrases without per-item citations. It did correctly warn that two sources were a sparse sample.

The revised twin artifact produced two **LinkedIn expression** observations, not a claim about real conversational behavior:

1. Guiding clients to self-discovery through strategic questioning. Qualification: the method is explained in posts/narrative illustration, not established by observed practice.
2. Presenting creative exercises as step-by-step instructions. Qualification: this is a descriptive exercise shared in writing, not an observed dialogue.

Both observations cite original example IDs, disclose one content family of support each, and remain unreviewed. Original line breaks and inline learner/trainer dialogue are retained in the example library. This demonstrates better traceability and explicit scope in this sample—not independently validated semantic correctness or trainer resemblance.

Saved structured outputs: [old behavior](pilot-before-behavior.json), [new twin specification](pilot-after-twin.json).

Local readable artifacts:

- Before: `.pi/pipeline-v2/before-workspace/reports/analysis.md`.
- After wiki: `.pi/pipeline-v2/after-workspace/wiki/index.md`.
- After twin with original examples: `.pi/pipeline-v2/after-workspace/twin/profile.md`.
- After combined report: `.pi/pipeline-v2/after-workspace/reports/analysis.md`.

## What improved structurally

1. Research ingestion no longer uses an unbudgeted probabilistic author filter. Original material is retained with uncertainty; only explicitly attributed eligible passages can support target-person twin observations.
2. Original files, passages, short turns and passage links are saved alongside normalized evidence. Numeric speaker IDs and objection phrases no longer rewrite meaning.
3. Cache keys track interpretation metadata and neighboring chunk context. Source/evidence/derived-artifact hashes protect active versions and detect stale or edited outputs.
4. Knowledge synthesis is separate from twin generation. The old first-70 platform behavior branch is no longer executed by `build`.
5. Twin output contains actual selection counts/omissions, original examples, scoped situations/patterns, qualifications and exact example references—not a high-confidence label inferred from full-corpus volume.
6. Unsupported synthesis fails after bounded repair instead of publishing the first evidence card as a substitute. Human fact-review notes remain visible.

## Not yet demonstrated or implemented

- Semantic correctness of the extracted statements or generated patterns.
- Extraction recall or completeness on a reviewed dataset.
- Recognizable conversational resemblance to Olga.
- A real-time chat agent or A/B learner conversations.
- Trainer approval or calibrated confidence.
- A protected human editing/approval workflow for behavioral patterns.
- Full-corpus migration, comprehensive cross-platform sampling, or inferred speaker identities.

No new dependency, vector database, fine-tuning workflow, hosted telemetry or external evaluation platform was added. The result is a testable research foundation, not a claim that an authentic twin has been achieved.
