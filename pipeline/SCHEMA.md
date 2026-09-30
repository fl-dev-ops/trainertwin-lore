# TrainerTwin data contract

The current implementation has one stored-data schema. `storage.SCHEMA_VERSION` and `sources.SOURCE_FORMAT_VERSION` are integrity markers for persisted artifacts, not selectable pipeline versions. Incompatible records must be re-extracted in the same workspace; no legacy execution path is maintained.

Sources are read-only inputs. Generated summaries, model audits and twin proposals are **not new source evidence**.

## Authoritative storage

| Path under workspace | Meaning |
| --- | --- |
| `sources/<source-id>-<revision>.json` | Original decoded source, passages, citation units and supplied metadata |
| `evidence/<source-id>-<revision>.jsonl` | All three typed source-record products for that revision |
| `manifest/<source-id>.json` | Activates one completed snapshot/record revision; hashes, model/signature, counts and diagnostics |
| `reviews.jsonl` | Append-only human source-support assertions |
| `verifications.jsonl` | Append-only human external fact-review assertions |
| `cache/<operation>/<hash>.json` | Validated raw model responses, revalidated when read |
| `usage.jsonl`, `events.jsonl`, `timings.jsonl` | Request keys/source IDs, usage, duration and local build timing |
| `work/<operation>/<key>.json` | Durable pending/completed/failed/blocked request status; failures require explicit retry |
| `work/{ingest,organize}_sources/<id>.json` | Per-source progress bound to source and metadata hashes |
| `work/spend.json` | Persistent configured spend ceiling, including unsettled request reservations |
| `rejected/<operation>/<key>-<attempt>.json` | Failed request/response/error for diagnosis; never serving evidence |

Source `original_text` retains the decoded file, including formatting/frontmatter. Each passage has original text, locator, timestamp, representation (`authored_text` or `spoken_turn`) and supplied speaker ID. Units contain whitespace-normalized citation text, exact original start/end offsets and a passage ID. Units are at most 800 characters; nonempty short turns are never discarded.

`author` is publication authorship, not identity for every embedded quote or video turn. `speakers` maps IDs to explicitly supplied names. Neither is independently authenticated. Allowed `format`: `post`, `document`, `transcript`, `interview`, `qa`, `role_play`, `lesson`. Publication time is not event time. `content_hash` groups identical normalized material, not near-duplicates or independently corroborated claims.

## Extracted products

The model returns exactly:

```json
{"knowledge": [], "cases": [], "expression": []}
```

Every item has `title` and `topic` (navigation labels, not additional factual claims), and `context_unit_ids`. On the **model wire**, each citation is `{"span_id": "u000001.s0"}`: an exact ID from the supplied `citation_spans`, or a unit ID selecting the complete unit. Code materializes the source words; the model cannot supply or edit quotations. Sentence boundaries are only an addressing aid and never remove whole-unit context or short replies.

Every substantive **stored** statement uses:

```json
{
  "text": "The exercise has a 60-second time limit.",
  "citations": [{"unit_id": "<source-id>:u000001", "quote": "Time yourself for 60 seconds."}]
}
```

Quotes must be contiguous exact substrings after whitespace normalization, at least 12 characters or the complete shorter unit. References must belong to the supplied extraction window. Every declared field is required; unknown scalar facts are `null`, unknown/absent collections are `[]`. Extra keys, malformed types and invalid references are rejected. Repeated identical context IDs and citations are deterministically deduplicated; evidence is never moved to another speaker/unit to make it match. This proves occurrence and structure, **not entailment**.

### Knowledge & methods

- `kind`: `claim`, `self_report`, `belief`, `method`, `advice`, `offering`.
- `summary`: grounded statement, required.
- `goal`: grounded statement or null.
- `prerequisites`, `steps`, `constraints`, `exceptions`: ordered arrays of grounded statements.

Do not flatten a procedure into generic advice or discard numbers, sequence, prerequisites or exceptions. No inferred scientific explanation or effectiveness claim is added.

### Teaching & interaction cases

- `kind`: `recorded_exchange`, `reported_exchange`, `illustration`, `demonstration`.
- `speaker_id`: focal recorded speaker or null for written/reported cases.
- `situation`: grounded statement, required.
- `cue`, `diagnosis`, `strategy`, `rationale`, `response`, `outcome`: grounded statements or null.

A `recorded_exchange` requires explicitly labeled Q&A/interview source format, multiple recorded speaker IDs, a focal speaker, and that speaker's cited response. Focal response citations cannot be someone else's words. A narrated client exchange remains reported, even when written in dialogue form. Absence of a stated rationale/outcome never licenses inferring one.

### Expression examples

- `form`: `structure`, `wording`, `tone`, `rhetorical_move`.
- `speaker_id`: focal recorded speaker or null for authored text.
- `observation`: grounded statement, required.
- `purpose`: grounded statement or null; must be stated/supported, not mind-reading.

Preserve the original wording and its mechanics, not generic traits such as “authentic” or “engaging.” Focal spoken observations must cite the named speaker's units.

## Stored record envelope

Each accepted item becomes a record with:

- `id`: source/product/revision-and-content-derived identity.
- `product`, `source_id`, `source_hash`, `metadata_hash`, `content_hash`.
- `source_format`, `source_url`, `published_at`, `author`, `category`.
- `title`, `topic`, `topic_slug`, `content` (the normalized typed item).
- `semantic_status: "not_reviewed"`, `external_status: "not_checked"`.
- `extraction_scope: "source_excerpt"`.

Context IDs are expanded to include intervening supplied units, preserving their order. Original context returns exact spans, constituent unit texts, locators and separate author/speaker attribution. Full passages remain available in snapshots even when a record's span covers only part of a long passage. Identical records from overlapping windows are deduplicated; different paraphrases are not silently merged.

A window gets at most one budgeted repair. Item-local errors retain the rejected response separately, request only the failing items with relevant source context, preserve valid siblings, and revalidate the complete result. Structural errors without item locations use a full-response repair with the previous response included. Persistent failed requests require `--retry-failed`; interrupted or budget/provider-blocked work remains resumable. Unresolved invalid output prevents source activation rather than silently dropping its invalid items. Explicit empty output can activate an empty revision with `quality.status: "empty"`. Manifest diagnostics include empty-window and cited/total-unit counts; these are not extraction recall or confidence.

## Derived views

| Path | Contract |
| --- | --- |
| `wiki/{knowledge,cases,expression}.jsonl` | Separate serving products with human review overlays |
| `wiki/sources/`, `wiki/topics/`, category/channel/timeline pages | Deterministic rendering of all accepted fields, quotes and original context; no model resummarization |
| `twin/examples.jsonl` | All eligible cases/expression records from selected, content-deduplicated, date/channel-balanced publications |
| `twin/profile.json` | Config, actual coverage, patterns, `observation_review: "unreviewed"`, `adaptations_status: "proposed_not_observed"` |
| `twin/profile.md` | Readable observations, proposed adaptations and original examples |
| `audit/checks.json`, `audit/report.md` | Field-level source-support diagnostics, explicitly model-only |
| `reports/analysis.md` | Offline wiki/twin compilation, not another inference step |
| Each generated directory's `build.json` | Version/input fingerprints and exact owned-file hashes |

Twin patterns contain `dimension`, `scope`, `situation`, `observation`, `qualification`, `support_ids`, `counter_ids`, `citations`, and `proposed_adaptation` (null or `{when, action, limits}`). IDs refer to original examples. Every declared support/counterexample needs an exact quotation from its cited unit. Interaction observations require recorded cases; teaching-strategy observations require cited case strategies. General scope requires different content families from multiple channels. All proposals remain unreviewed; a count does not confer confidence.

Explicit aliases gate twin examples; known channel ownership is insufficient for recorded speech. Role-play is excluded. Author-filtered spoken knowledge requires all cited units to map to requested aliases. The full research corpus remains available without pretending every source belongs to the target person.

`context` returns three separately labeled product arrays, complete selected records and original spans, filters, omission counts and an abstention flag. Lexical relevance ranks records; oversized records are omitted intact. The serialized packet respects the requested character limit, or errors if the query/metadata alone exceed it. It is a downstream context packet, not an answer generator.

## Linked wiki organization

`organize` adds `organization/sources/<source-id>.json` and `organization/topics.json`, published with a completion receipt. These are model-organized navigation data, not replacements for immutable extraction evidence. Each source checkpoints only after all its windows validate; completed sources survive failures in later sources or topic grouping. The wiki is rendered once at normal/error stage exit, not after every source. A hard kill may leave the wiki stale until `build` runs. Until topic grouping completes, original labels remain accessible. A source fingerprint binds each document to its original text and supplied metadata. Stale documents are excluded from the next wiki build, with their IDs reported in coverage.

- Topics have stable IDs, display names, one optional parent and exact input-label aliases. Models return names and parent names; code generates safe IDs and reuses existing IDs for unchanged names. Validation rejects missing/duplicate aliases, unsafe IDs and hierarchy cycles. New unmatched labels remain visible rather than disappearing.
- Episodes have ordered contiguous unit references, a cited summary, subject labels, activity labels and cited observable moves with tentative roles. Each episode stays within one content part. Moves may share a unit but cannot run backward. Unknown voices keep numeric IDs; roles do not assign identity. `source_window` means the input did not contain the whole source.
- Entities contain literal cited name mentions; the model selects an inclusive range of numbered words within one supplied unit. Code copies the original substring and derives the display name from the first validated mention, not generated text. Short names such as R, SAP or React are valid. A mention is not an employment, endorsement or other relationship. People/projects are source-scoped to avoid merging unknown identities.
- New organization summaries/moves select source span IDs, just like extraction; code materializes exact quotes. Organization citations require literal occurrence after whitespace normalization. A wrong unit ID is relocated only to a unique immediate-neighbor match. An exact quote spanning two adjacent same-speaker/content-part units retains both `unit_id` and `end_unit_id`; episode context expands to contain that verified span. Ambiguous, fabricated, and cross-speaker stitched quotes are rejected. No fuzzy matching or editorial ellipses are used. Unsupported optional entity candidates are excluded, with omission counts retained in source organization and wiki coverage. Unsupported episode summaries/moves still fail source publication. Raw cached discovery candidates are revalidated on every read; rejected entity candidates never enter the serving wiki. These checks are not semantic entailment or human approval.
- Supplemental `extra-*` unit IDs address captured Markdown frontmatter title/description, otherwise omitted hashtags, and comments in the same immutable original. Existing extraction-unit IDs and records do not change. Supplemental text is available for organization/navigation, not silently promoted to extracted knowledge or verified attribution.

`wiki/catalog.json` links topics, entities, methods, episodes, expression and sources with actual organization coverage. Existing `wiki/{knowledge,cases,expression}.jsonl` remain the serving projections of the original records. Markdown pages are deterministic views; canonical record links now target anchors on source pages so topic regrouping does not break record references. Source pages retain citation-unit anchors and original text formatting. `wiki/activities/` and `wiki/channels/` are navigation views, not separate evidence stores.

Reports and twins are not regenerated by organization. Wiki receipts include the organization fingerprint; `lint --wiki-only` checks the source/wiki layer without claiming that downstream artifacts are current.

## Audit and human review

An audit enumerates every substantive field (including each ordered step), providing original context. Each field must receive exactly one `supported`, `unsupported`, or `uncertain` diagnostic with a reason and valid source unit references. Model output neither rewrites records nor grants human approval.

`reviews.jsonl` entries: `{record_id, status, note, checked_at}`, with status `supported`, `unsupported`, or `uncertain`. Latest active-ID review wins. Unsupported records are retained historically but excluded from serving views; `--reviewed-only` requires human-supported records. `verifications.jsonl` entries: `{evidence_id, status, url, note, checked_at}`, with status `verified` or `contradicted`. CLI external review is restricted to knowledge claims/self-reports and never fetches/authenticates the URL.

Review overlays do not mutate immutable extraction records. Changed source/metadata-derived IDs prevent silent transfer of old approvals. Rebuild affected views after changes; stale/modified artifacts fail `lint`. Legacy cards are rejected, not automatically upgraded into fields they never contained. File receipts detect incomplete multi-file publication; they are not database transactions or cryptographic protection against a malicious local editor.

## Limits

No semantic-support guarantee, automatic external fact verification, real speaker identification, semantic near-duplicate detection, calibrated confidence, runtime agent, or proof of trainer resemblance. Generic structured-source flattening, lexical retrieval, excerpt-sized extraction and independently generated twin batches have explicit limits. Manually annotated real-source targets and a separately budgeted live evaluation remain necessary to measure extraction quality.
