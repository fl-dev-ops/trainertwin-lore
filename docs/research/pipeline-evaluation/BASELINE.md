# TrainerTwin pipeline: historical baseline

This is a past research record, not current workflow instructions. Frozen implementation copies and the comparison runner have been removed. Use Git for old code and `pipeline/README.md` for the single current pipeline. Original measurements and paths below describe the experiment at capture time.

## Purpose and scope

Record the implementation **before this migration**, so its behavior can be compared against the proposed two-stage TrainerTwin flow. MCP, collectors, HTML profile rendering, and existing user workspaces are outside the edit scope. Existing user changes must not be reverted.

TrainerTwin's intended outputs are (1) a source-backed person/knowledge wiki and (2) a separate, evidence-backed communication/interaction specification with original examples. Public behavior is not proof of private personality. A useful twin and resemblance to its trainer require separate evaluation.

## Repository state at capture

- Git HEAD: `189595b` (`Store YouTube transcripts as Markdown`). This is not a clean baseline: existing changes include `pipeline/sources.py`, `pipeline/profile.py`, collectors, dependency files, and data.
- Earlier in this conversation, Olga's workspace was at `users/olga/workspace`; it is now under `users_backup/olga/workspace`. Thousands of pre-existing deletions/moves are unrelated to this migration.
- The parser already has an uncommitted change accepting Markdown transcripts with introductory caption text and without timestamped turns. Preserve that compatibility.
- Original implementation copies and a frozen input pilot are saved under `.pi/pipeline-v2/` (local, ignored). Machine-readable fingerprints and measurements accompany this document.
- Earlier tests: 23 passed. Earlier full workspace lint passed: 773 sources, 2,755 evidence cards, 14 topic pages. These demonstrate existing checks, not semantic quality.

## Current flow

```text
public content collected by social/
  -> users/<user>/data/<channel>/
  -> read_source(): flatten/normalize into <=800-character units
  -> conditional authorship screening (heuristics/Jev)
  -> chunks (~15,000 characters)
  -> OpenRouter structured evidence extraction
  -> exact-quote/unit/type validation; one repair; item salvage
  -> per-chunk cache
  -> versioned evidence JSONL + source Markdown + active manifest
  -> build(): group topic labels, synthesize topic findings, overview
  -> build(): platform behavior from FIRST 70 cards per channel
  -> category/channel indexes and publication timeline
  -> analyze(): compile platform behavior, decision rules, phrases
```

Existing workspace artifacts:

- `cache/`: raw extraction/grouping/synthesis checkpoints.
- `evidence/`: versioned cards; no independently stored source-context documents.
- `manifest/`: selects each completed source's active evidence.
- `wiki/sources/`: generated source summaries and card quotes.
- `wiki/topics/`, `overview.*`, `topic-map.json`: topic grouping and synthesis.
- `wiki/behavior/`: platform descriptions, rules, phrases without per-pattern citations.
- `reports/analysis.md`: primarily behavior-based report; `timeline.md` is separate.
- `verifications.jsonl`: human assertions; `usage.jsonl`: provider usage.

## Observed corpus baseline (earlier audit)

| Channel | Active cards | Active source files | Behavior input cards | Behavior input source files |
| --- | ---: | ---: | ---: | ---: |
| Instagram | 60 | 24 | 60 | 24 |
| LinkedIn | 1,841 | 533 | 70 | 16 |
| Twitter | 5 | 1 | 5 | 1 |
| YouTube | 849 | 215 | 70 | 16 |

LinkedIn's selected publication range was 2018-02-28 through 2023-05-22, but the behavior artifact received the full count of 533 sources and declared `high` confidence. Of its 70 input cards, three were declared authored by `oxana-kukharchuk`; author/context/date/IDs were then removed from the behavior payload.

Across all 2,755 cards, 853 lacked an original URL and 909 lacked an author. Twenty-seven LinkedIn cards declared authors other than `olgasi`; this is not automatically invalid research, but is not automatically Olga's own speech either. YouTube `shorts-run/transcripts/s189.yaml` and `s195.yaml` contain identical normalized transcript text with different upload identities/dates: retain publication history while grouping repeated content.

## Flaw ledger and acceptance checks

| ID | Before | Desired behavior / scope |
| --- | --- | --- |
| F01 | First-70 behavior sampling; confidence based on full-corpus counts | Separate twin stage; time/platform-balanced, source-diverse bounded examples; disclose actual selected counts and omissions; no automatic high-confidence persona |
| F02 | Missing author/provider failure can pass authorship gate; rejected existing source remains active | Keep research separate from target-person attribution; no paid heuristic gate; twin examples require explicit exact author aliases or supplied speaker attribution |
| F03 | Speaker IDs 2–5 and objection phrases rewrite context/kind | Remove those guesses; preserve supplied speaker IDs and model classifications as unreviewed observations |
| F04 | Real quote can validate an unrelated statement | Keep structural validation honest: label semantic support unreviewed, require original context and human review; automatic semantic entailment is NOT claimed solved |
| F05 | Short transcript answers such as “Never.” are discarded; writing/conversation structure is lost | Retain nonempty short turns and original passages; persist a versioned source snapshot with original source text and ordered passage links |
| F06 | Path identity treats repeated content as independent support | Record normalized content-family fingerprints; preserve distinct publications and avoid duplicate content inflating twin support counts |
| F07 | Partial extraction and synthesis degradation can look complete | Record rejection/empty-chunk/coverage diagnostics; repair or fail invalid synthesis instead of substituting the first card or silently truncating |
| F08 | Author changes reuse old interpretations; any text change invalidates all chunk caches | Extraction cache includes interpretation-relevant metadata and exact chunk input; publication-only metadata may reuse extraction if absent from the extraction prompt |
| F09 | Lint cleans bad IDs in memory; can accept re-ingestion without rebuilding | Strict, non-mutating finding validation; bind completed wiki/twin/report artifacts to active evidence and artifact fingerprints |
| F10 | Human verification notes disappear and status can overstate review scope | Preserve and display note, URL and checked time; older review records remain history, not applicable to new evidence revisions |
| F11 | Eager parsing aborts before per-source handler; Jev bypasses budget; model default loaded before .env | Parse/catch per source, report incomplete runs, remove unbudgeted gate, load model configuration before CLI defaults |
| F12 | Tests cover mechanics, not attribution/recall/persona resemblance | Add structural regression checks and explicit unresolved quality limitations; trainer likeness requires separate held-out, human-reviewed comparison |

### Offline reproductions recorded during review

All were performed using temporary fixtures/fake models, not paid calls:

- An unrelated billion-dollar-sales statement paired with a real buyer-question quote was accepted.
- “I am not interested in buying a house this year.” changed from self-report to hypothetical teaching move.
- A failing authorship provider returned acceptance.
- A zero extraction budget still permitted one Jev call.
- An explicitly rejected previously ingested source retained one active evidence card.
- `[valid_id, nonexistent_id]` passed lint and the invalid ID remained on disk.
- Re-ingestion with stable evidence IDs passed lint without a rebuild.
- Changing the author via metadata reused extraction with zero new calls.
- The verification note was absent from the overlaid card.
- A transcript answer “Never.” was absent from parsed units.

## Proposed flow

```text
immutable collected files
  -> context-preserving source documents + declared metadata
  -> source-local evidence (knowledge + communication observations)
       -> knowledge wiki
       -> original examples + scoped, cited twin specification
  -> optional offline compiled report
  -> held-out twin conversations and human review
```

A wiki is a view, not the sole gateway to the original evidence. Keep the existing file-based architecture, OpenRouter client, per-call budgets and resumable caches. Do not add vector databases, fine-tuning, external telemetry, or hosted evaluation services for this migration.

## Comparison protocol

1. Freeze implementation fingerprints and a small source selection before edits. Record original paths/content hashes and do not modify the original corpus.
2. Run the existing tests and a repeatable offline contract probe against the before implementation.
3. Implement the changes and run the same probe against the after implementation, plus new regression tests.
4. Use separate workspaces for any live pilot. Keep the same sources/model, explicitly record call budgets, calls, token usage, selected evidence counts, and errors. Cached/fake results must never be described as live model quality evidence.
5. Treat source coverage, valid citations, correct freshness rejection, and provenance preservation as structural metrics—not extraction recall or trainer resemblance.
6. Review semantic support and realistic conversations separately. No reviewed goldens/trainer ratings have been supplied; no automatic claim of improved persona fidelity is justified.

## Non-goals / known ceilings

- No automatic proof of semantic entailment or external fact verification.
- No private-personality inference or claim that public content fully captures the trainer.
- No automatic real identity assignment to diarization IDs.
- No full corpus re-ingestion or changes to `users_backup/`.
- No MCP or collector changes; preserve pre-existing parser compatibility.
