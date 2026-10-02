# TrainerTwin Index Architecture: Behavioral Persona Grounding

## Executive decision

TrainerTwin should use a **per-persona SQLite database as a rebuildable index over immutable source files**, with normalized relational tables for records, parent-child structure, concepts, aliases, tag assignments, entities, provenance, and retrieval traces. Add **FTS5 immediately** and add local dense embeddings as a second retrieval leg after a lexical-plus-facet baseline has been evaluated. SQLite already supplies embedded full-text search, built-in JSON functions, generated/indexable columns, transactional UPSERTs, and WAL operation; these capabilities fit a local, updateable index better than a monolithic JSON file or an analytics-oriented DuckDB database.[^1][^2][^3][^4][^5]

The correct indexed model is **multi-tier, not one-record/one-chunk**:

1. `source` — immutable raw file and integrity metadata.
2. `episode` — coherent lesson, exchange, story, or case; preserves decision flow.
3. `span` — compact verbatim retrieval unit inside an episode.
4. `move` — optional observable dialogue action, linked to one or more exact spans.

Retrieval should search the child `span`/`move` units for precision, then expand to the parent episode or adjacent spans only when needed for decision-flow context. This “small-to-big” pattern explicitly decouples retrieval precision from synthesis context and is established in hierarchical retrieval systems.[^6][^7][^8][^9]

Tags should be **typed concept references, not free-form strings and not paths**. Preserve the LLM-emitted raw label for audit, but map it in a separate normalization stage to a stable `concept_id`; maintain preferred labels, alternate labels, broader/narrower links, and versioned merge/split history. This mirrors the durable parts of controlled-vocabulary systems such as SKOS, which distinguish stable concepts from preferred, alternate, and hidden lexical labels and support broader/narrower relations.[^10][^11][^12][^13]

The final 3–5 grounding clips should come from a **hybrid candidate union**: deterministic constraints, typed-facet matches, FTS5/BM25-style lexical retrieval, and dense semantic retrieval, followed by calibrated reranking, overlap removal, source/episode diversification, and parent-context expansion. Dense and lexical methods have complementary failure modes; no one retrieval architecture dominates across datasets, while BM25 remains a strong baseline and reranking often improves top-rank quality at additional cost.[^14][^15][^16]

***

## Architectural principles

### Ground truth and derived state

The original transcript/post files remain the only textual ground truth. The index is a **materialized routing structure** that is always disposable and rebuildable. A stored quote snapshot is useful as an integrity assertion and review convenience, but the authoring handoff should re-slice the immutable source using authoritative coordinates and verify its hash before use.

Recommended invariants:

- No generated paraphrase is treated as evidence.
- Every returned evidence unit resolves to `source_id + source_hash + coordinate_system + start + end`.
- Every tag and move assignment records who/what assigned it, model or rule version, confidence, and timestamp.
- Normalization never overwrites the raw emitted tag; it adds or revises a mapping.
- Deleted or superseded records are tombstoned or revisioned, not silently reused.
- Retrieval returns evidence plus a machine-readable score explanation, never just opaque similarity scores.

### Coordinate integrity

Line ranges alone are understandable but fragile if formatting changes. Because sources are declared immutable, lines can remain the human audit coordinate, but each record should also carry:

- normalized UTF-8 byte or character offsets;
- original media timestamps when available;
- speaker/turn identifiers where available;
- source hash and extraction-version hash;
- deterministic span checksum;
- line range for inspection.

Use a named coordinate convention, for example `line_1_based_inclusive` and `char_0_based_half_open`. Ambiguous coordinate semantics cause more long-term corruption than the storage engine choice.

### Separate build stages

The pipeline should be explicitly staged:

1. **Discover and hash sources.**
2. **Parse deterministic landmarks** such as headings, timestamps, speaker turns, lists, and platform metadata.
3. **Detect episodes and candidate spans.**
4. **Assign raw observable labels** and raw entities without normalization.
5. **Normalize concepts and aliases** in a separately versioned pass.
6. **Build lexical indexes.**
7. **Build embeddings** only for changed retrieval text or embedding-version changes.
8. **Validate coordinates and verbatim reconstruction.**
9. **Publish an atomic index version.**

This preserves TrainerTwin’s single-responsibility rule: extraction emits evidence-linked observations; normalization governs vocabulary; retrieval ranks evidence.

***

## A. Storage models

### Decision matrix

| Model | Query flexibility | Auditability | Incremental re-indexing | Operational complexity | Fit for TrainerTwin |
|---|---|---|---|---|---|
| Single `index.json` | Low to medium; convenient for complete scans, awkward for joins, aliases, hierarchy, and ranked search | Excellent in a text editor; diffs become noisy as order/format changes | Weak; commonly rewrites the whole document and risks merge contention | Lowest initially | Good interchange/export format; weak canonical query store after schema growth |
| SQLite relational + selected JSON | High; joins, constraints, recursive hierarchy, FTS5, expression/generated indexes, transactions | High with CLI/admin views and deterministic exports; binary file itself is less diffable | Strong; source-scoped transactional delete/upsert or revision replacement | Low | **Best primary store** |
| DuckDB relational/document | High for corpus analytics and batch inspection; rich JSON ingestion | High through SQL and exports | Good for bulk rebuilds, less natural for many small mutations | Low to medium | Useful secondary analytics tool, not preferred serving/index authority |
| Append-only JSONL event/record log | Low directly; high only after building a projection | Excellent history and replay; one self-contained JSON value per line supports independent processing[^17][^18] | Excellent append cost; updates require superseding events and compaction | Medium because projection, replay, idempotency, and compaction become application responsibilities | Useful audit/change feed; unnecessary as sole store |
| SQLite + FTS5 + local vectors | Highest practical retrieval flexibility; facets, exact terms, paraphrases, and reranking | High if component scores and versions are logged | Strong; FTS and vectors update only for affected spans | Medium | **Recommended target state** |
| Dedicated vector DB | Strong semantic/hybrid search and filtering | Medium; payloads are inspectable but adds another authority and service | Strong | Highest for this corpus size | Premature unless cross-persona scale, concurrency, or latency later demands it |

### Single structured file

A single JSON file is defensible while the index is only a few thousand homogeneous records and the dominant workflow is “load once, scan in memory, write once.” It is highly portable and easy to snapshot. The problem is not raw corpus size; it is **relationship growth**: aliases, many-to-many tags, episode-child edges, entity mentions, revisions, embedding versions, and retrieval diagnostics turn nested JSON into an application-managed database.

Retain a deterministic `index.export.json` for debugging, fixtures, and portability. Do not make it the sole mutable source of index truth once normalization and hybrid retrieval are introduced.

### SQLite versus DuckDB

SQLite is the better operational index because TrainerTwin performs selective upserts, source-scoped invalidation, joins over many-to-many facets, and interactive point/ranked retrieval. SQLite’s FTS5 is a native full-text virtual table; JSON functions are built in by default in modern SQLite; generated columns can be indexed; and WAL lets readers retain a stable snapshot while commits append to the log.[^2][^3][^4][^1]

DuckDB is excellent for ad hoc analytical scans, direct JSON/NDJSON ingestion, and aggregate corpus QA. However, its documentation explicitly describes it as optimized for bulk operations rather than many small transactions, and automatic multi-process writing is not a primary design goal. Use DuckDB over exported Parquet/JSONL when analyzing many personas, tag distributions, extraction drift, or evaluation results—not as the primary per-persona mutation and retrieval engine.[^19][^20][^21]

### Append-only log

JSONL’s one-value-per-line structure is easy to append, concatenate, stream, and partially process. It is valuable if requirements include a tamper-evident annotation history, offline synchronization between indexers, replayable model decisions, or forensic audit.[^17][^18]

It is not free simplicity. An event log needs stable event IDs, aggregate IDs, sequence/version checks, tombstones, replay semantics, projection rebuilds, and compaction. For TrainerTwin, the pragmatic pattern is **SQLite as current state plus an optional JSONL decision log**, rather than event sourcing the entire index from day one.

### Vector augmentation

At this corpus size, a separate vector service is not required. Store embeddings in SQLite or a sidecar array keyed by `span_id`; exact cosine scanning over a persona-sized candidate set is often operationally sufficient, especially after metadata filtering. SQLite also has local vector-extension options, including portable virtual-table implementations, but extension maturity and deployment portability must be treated as explicit dependencies rather than assumed platform features.[^22][^23]

Keep vector data disposable and versioned by:

- `embedding_model_id`;
- model revision/checksum;
- retrieval-text checksum;
- vector dimension and normalization method;
- creation time.

Never place embedding values inside the canonical record JSON export; they create giant diffs and couple semantic state to a particular model.

***

## Recommended data model

### Core relational shape

```sql
source(
  source_id TEXT PRIMARY KEY,
  persona_id TEXT NOT NULL,
  path TEXT NOT NULL,
  media_type TEXT,
  content_sha256 TEXT NOT NULL,
  parser_version TEXT NOT NULL,
  line_count INTEGER,
  duration_ms INTEGER,
  indexed_at TEXT,
  UNIQUE(persona_id, path)
);

record(
  record_id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL REFERENCES source,
  parent_id TEXT REFERENCES record,
  kind TEXT NOT NULL CHECK(kind IN ('episode','span','move')),
  ordinal INTEGER NOT NULL,
  start_line INTEGER,
  end_line INTEGER,
  start_char INTEGER,
  end_char INTEGER,
  start_ms INTEGER,
  end_ms INTEGER,
  speaker TEXT,
  span_sha256 TEXT NOT NULL,
  extraction_version TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active',
  attributes_json TEXT NOT NULL DEFAULT '{}'
);

concept(
  concept_id TEXT PRIMARY KEY,
  facet TEXT NOT NULL,
  preferred_label TEXT NOT NULL,
  definition TEXT,
  concept_version INTEGER NOT NULL,
  status TEXT NOT NULL,
  UNIQUE(facet, preferred_label)
);

concept_label(
  concept_id TEXT NOT NULL REFERENCES concept,
  label TEXT NOT NULL,
  label_kind TEXT NOT NULL CHECK(label_kind IN ('preferred','alternate','hidden','raw_seen')),
  language TEXT,
  normalized_key TEXT NOT NULL,
  UNIQUE(concept_id, label, language)
);

concept_relation(
  subject_id TEXT NOT NULL REFERENCES concept,
  relation TEXT NOT NULL CHECK(relation IN ('broader','related','replaced_by')),
  object_id TEXT NOT NULL REFERENCES concept,
  PRIMARY KEY(subject_id, relation, object_id)
);

assignment(
  record_id TEXT NOT NULL REFERENCES record,
  facet TEXT NOT NULL,
  raw_label TEXT NOT NULL,
  concept_id TEXT REFERENCES concept,
  assignment_method TEXT NOT NULL,
  confidence REAL,
  normalizer_version TEXT,
  status TEXT NOT NULL,
  PRIMARY KEY(record_id, facet, raw_label, assignment_method)
);

entity_mention(
  record_id TEXT NOT NULL REFERENCES record,
  entity_id TEXT,
  surface_form TEXT NOT NULL,
  start_char_in_record INTEGER,
  end_char_in_record INTEGER,
  resolution_confidence REAL
);
```

Add separate tables for `embedding`, `index_run`, `retrieval_run`, and `retrieval_hit`. Keep frequently filtered attributes relational; reserve JSON for infrequent, source-specific metadata. SQLite can query JSON directly, but JSON-array tag membership is inferior to a normalized assignment table for constraints, indexing, integrity, and statistics.[^3][^2]

### Stable identifiers

Use IDs that survive label changes:

- `source_id`: UUID or hash of persona plus canonical source identity; do not derive only from mutable path.
- `record_id`: source identity plus extraction-version namespace plus deterministic boundary identity, or a UUID with explicit revisions.
- `concept_id`: opaque stable ID, never the slug.

A label such as `handling-objections` may later be renamed without changing its concept ID. A true semantic merge creates `replaced_by`; a split creates new concepts and requires reassignment review. This prevents the old filesystem-slug collision problem from reappearing inside strings.

***

## B. Taxonomy and tags

### Use orthogonal facets

The minimum useful facets are:

| Facet | What it captures | Example |
|---|---|---|
| `topic` | Subject matter | `caching`, `market-cycles`, `cold-calling` |
| `situation` | Observable interaction context or trigger | `client-predicts-crash`, `candidate-stuck`, `price-objection` |
| `move_type` | What the trainer observably does | `counter-question`, `reframe`, `give-counterexample`, `sequence-steps` |
| `activity` | Larger task | `mock-interview`, `sales-coaching`, `portfolio-review` |
| `entity` | Mentioned real object/person/product | `Redis`, `S&P-500`, named customer |
| `role` | Speaker/addressee role when known | `trainer`, `candidate`, `buyer`, `manager` |
| `format` | Evidence form | `case-story`, `analogy`, `checklist`, `demonstration` |
| `stance_or_trigger` | Explicitly stated position, not inferred motive | `will-wait`, `concerned-about-loss`, `asks-for-discount` |

Do not place the entire scenario into one compound tag such as `sales-mindset+cold-calling+fear-of-rejection`. Store independent facets and let retrieval compose them. Use a compound concept only when it is a stable domain term with meaning beyond its components.

### Avoid “typed tag objects” as the final form

The current shape—`[{"type":"topic","name":"..."}]`—is appropriate as raw extraction output. The canonical layer should replace `name` as identity with:

```json
{
  "facet": "move_type",
  "concept_id": "mv_01J...",
  "raw_label": "answers by asking them back",
  "assignment_method": "llm:extractor-v4",
  "confidence": 0.88,
  "normalizer_version": "moves-2026-10-01"
}
```

This preserves evidence of what the extractor said while making retrieval independent of spelling and future preferred-label changes.

### Hierarchy and namespaces

Use hierarchy sparingly and facet-locally:

- `topic/software-architecture/caching`
- `situation/objection/timing-objection`
- `move/reframe/risk-reframe`

These paths are display conveniences, not IDs and not storage locations. Support polyhierarchy where justified: `cold-calling` may sit under both `sales-prospecting` and `phone-outreach`. SKOS-style broader/narrower relations are a better model than forcing every concept into one tree.[^11][^12]

Keep the hierarchy shallow until real retrieval cases demand depth. Deep LLM-generated ontologies create false precision, low agreement, and maintenance work without proving retrieval value.

### Normalization strategy

Use all three normalization moments, but give them different responsibilities:

| Stage | Responsibility | Recommendation |
|---|---|---|
| Extraction time | Emit raw candidate labels and observable evidence | Permit open vocabulary; apply only deterministic text cleanup such as Unicode normalization, whitespace, and case-folded lookup key |
| Post-processing | Resolve raw labels to stable concepts, aliases, broader terms, or unresolved queue | **Primary normalization authority**; deterministic first, LLM-assisted suggestions second, human/review rule for low-confidence merges |
| Query time | Expand aliases, hierarchy, and unresolved/raw-label matches | Recall safety net; never redefine the vocabulary during a query |

Doing semantic normalization inside record creation entangles two error sources and makes extractor changes rewrite history. Doing all normalization at query time makes results non-reproducible and repeats cost. The right division is open-vocabulary capture followed by a versioned concept-resolution pass.

### Synonym workflow

1. Canonicalize the lexical lookup key deterministically: Unicode normalization, case fold, punctuation/space normalization, and conservative singularization only if language-safe.
2. Resolve exact preferred/alternate/hidden label matches.
3. Apply curated alias and replacement rules.
4. Retrieve candidate concepts from the same facet using lexical and embedding similarity.
5. Ask an LLM or reviewer only whether the candidate is equivalent, broader, narrower, merely related, or genuinely new.
6. Auto-merge only above a validated threshold; queue ambiguous mappings.
7. Version every vocabulary mutation and re-run only affected assignments.

The distinction between preferred and non-preferred labels is a proven controlled-vocabulary mechanism; alternate labels create additional retrieval entry points without duplicating the underlying concept.[^13][^24][^10]

### Cross-cutting discoverability

Cross-cutting retrieval should rely on **set composition**, not tag multiplication:

- OR within a facet: `topic IN (cold-calling, prospecting)`.
- AND across facets when explicit: `topic:cold-calling AND situation:rejection`.
- Soft boosts for uncertain facets instead of hard intersections.
- Ancestor expansion with decay: an exact concept match scores more than a broader-parent match.
- Alias expansion before lexical retrieval.
- Raw verbatim FTS and dense retrieval as independent recall paths.

A clip tagged `topic:cold-calling`, `topic:sales-mindset`, `situation:rejection`, and `move:reframe` remains one record with four assignments. There is no combinatorial record duplication.

***

## C. Indexed-unit granularity

### Why no single granularity wins

Small chunks concentrate the matching signal and improve pinpoint retrieval, but can omit antecedents, the client’s trigger, and the trainer’s multi-step response. Large episodes preserve logic and voice but dilute search signals and consume the authoring context budget. Recent hierarchical approaches explicitly frame this as a precision-versus-context trade-off and retrieve children before reconstructing parent context.[^25][^9]

Fixed line counts are also semantically unstable: 40 lines may be a short rapid exchange, a long monologue, or formatting noise. Transcript research treats topical segmentation as identifying coherent discourse regions and boundaries where topics shift, often using lexical, conversational, and prosodic cues.[^26][^27][^28][^29]

### Recommended hierarchy

#### Episode

An episode is the **unit of behavioral coherence**. It should contain enough contiguous discourse to reconstruct:

- the trigger or problem;
- the trainer’s sequence of moves;
- examples or counterexamples;
- the outcome, recommendation, or unresolved ending.

Episode boundaries should prefer, in order: explicit source landmarks; speaker/scene changes; headings/chapters; sustained topic shifts; discourse markers; and finally size caps. Natural landmarks are strong priors but not absolute boundaries—one chapter may contain several cases, and one case may cross a timestamp marker.

#### Span

A span is the **primary retrieval unit** and must remain verbatim. It should be bounded by utterances/sentences, not arbitrary character cuts, and should usually express one locally understandable claim, exchange, example, or response. The existing ≤40-line constraint is acceptable as a safety cap, not as the segmentation objective.

Recommended adaptive rules:

- Never split a speaker turn unless it exceeds the hard token cap.
- Include the client/question turn with the answer when the answer depends on it.
- Store one preceding/following span pointer rather than copying overlap into many records.
- Permit nested spans when a concise “signature phrase” lies inside a longer explanatory response.
- Flag spans that require parent expansion because pronouns or references make them locally ambiguous.

#### Move

A move records an observable action and role relation, for example:

```json
{
  "actor_role": "trainer",
  "move_type": "counter-question",
  "target_role": "buyer",
  "span_ids": ["sp_17", "sp_18"],
  "sequence_index": 2
}
```

This is not a psychological intent. Dialogue-act standards similarly distinguish communicative function from semantic content and cover dimensions such as task, feedback, turn management, and discourse structuring. TrainerTwin need not adopt the full standard, but it should preserve the same separation: **what action occurred** versus **what subject it concerned**.[^30][^31][^32]

### High-level flow without summaries

Do not create an LLM prose summary for an episode. Represent flow structurally:

- ordered child spans;
- ordered moves;
- speakers and roles;
- explicit entity mentions;
- typed topics/situations;
- source landmarks;
- deterministic first/last verbatim snippets only if copied by code.

The authoring agent can retrieve a precise child span, then request its parent’s ordered moves and selected neighboring spans. That provides high-level decision flow and exact phrasing without a synthetic summary layer.

### Embedding text

Embed a deterministic retrieval projection, not generated context:

```text
[facet topics] market-cycle; timing-objection
[facet situation] buyer says they will wait for a crash
[roles] buyer -> trainer
[source title] ...
[verbatim]
...
```

The facet labels are derived index metadata; the evidence returned to authoring remains only the source-sliced verbatim text. Contextual-retrieval work shows that adding chunk-specific context to lexical and dense indexes can improve retrieval, but its published approach uses model-generated context. That conflicts with TrainerTwin’s anti-summary constraint, so use only deterministic context: source title, chapter, participants, canonical tags, timestamps, and neighboring-turn labels.[^15][^33]

***

## D. Retrieval for authoring

### Query contract

Do not let the LLM browse raw tables or invent SQL freely. Give it a typed retrieval API and allow an LLM planner to emit a validated query plan:

```json
{
  "persona_id": "olga",
  "query_text": "client says I will wait until the market crashes",
  "facets": {
    "situation": ["timing-objection", "predicts-market-drop"],
    "topic": ["market-cycle"],
    "move_type": []
  },
  "required": {"record_kind": ["span", "move"]},
  "preferences": {
    "include_trigger_and_response": true,
    "max_per_episode": 2,
    "result_count": 5
  }
}
```

Validate concept IDs, limits, persona scope, and permitted fields. Treat LLM-selected facets as soft evidence unless the scenario has an explicit hard constraint.

### Retrieval stages

#### Stage 0: deterministic scope

Apply only safe hard filters:

- persona;
- active index/source versions;
- permitted media types or date bounds if the caller explicitly asks;
- required record kind;
- coordinate and integrity validity.

Do **not** hard-filter all candidate records by inferred topic tags. A missing or wrong tag would make the correct clip unrecoverable.

#### Stage 1: parallel candidate generation

Produce independent ranked lists:

1. **Facet list** — exact concepts, aliases, ancestors, and related concepts with decaying weights.
2. **FTS list** — scenario text, quoted objection, important entities, phrases, and alias-expanded terms against verbatim plus deterministic metadata.
3. **Dense list** — semantic similarity over the same deterministic retrieval projection.
4. **Optional episode list** — episodes with multiple moderately matching children, useful for multi-step behavior.

FTS5 provides full-text `MATCH` retrieval inside SQLite. Lexical search is especially valuable for exact phrasing, names, identifiers, and distinctive trainer language, while dense retrieval captures paraphrases but can underweight exact strings.[^34][^35][^1][^14][^15]

#### Stage 2: candidate fusion

Take the union rather than the intersection. Reciprocal Rank Fusion is a sound initial method because it operates on ranks rather than incomparable raw score scales; hybrid systems commonly combine dense and sparse result lists this way. It is a baseline, not a dogma: benchmark the result against normalized weighted fusion because optimal fusion varies by corpus and query type.[^36][^37][^38][^39]

#### Stage 3: reranking

Rerank the top candidate pool using features that are all inspectable:

- lexical score;
- dense similarity;
- exact/ancestor/alias facet matches;
- trigger-response completeness;
- move match;
- entity match;
- span self-containment;
- assignment confidence;
- evidence integrity;
- episode-level support from neighboring matching children.

A cross-encoder or constrained LLM relevance grader can be tested here because it only ranks verbatim candidates; it must not rewrite them. BEIR found that reranking and late-interaction approaches often delivered strong zero-shot quality but at higher inference cost, reinforcing a retrieve-many/rerank-few design.[^16]

#### Stage 4: evidence-set selection

Selecting 3–5 clips is a **set optimization problem**, not merely “top five scores.” Apply:

- overlap deduplication by coordinate intersection;
- maximum per episode/source unless repeated evidence is essential;
- diversity across example, heuristic, signature phrase, and counterexample where available;
- coverage of both the client trigger and trainer response;
- preference for complete exchanges over isolated aphorisms;
- adjacent-span or parent expansion only after the winning children are known.

Return a package such as:

```json
{
  "query_id": "rq_...",
  "index_version": "...",
  "hits": [
    {
      "record_id": "sp_...",
      "source_id": "src_...",
      "coordinates": {"start_line": 412, "end_line": 427},
      "parent_episode_id": "ep_...",
      "reason": {
        "fts_rank": 2,
        "dense_rank": 5,
        "matched_concepts": ["situation:timing-objection"],
        "expanded": ["previous_client_turn"]
      }
    }
  ]
}
```

The application then verifies the source hash and slices the text. The retriever never supplies a model-authored quotation.

### Two-stage LLM routing

An LLM can inspect a compact concept catalog and propose candidate facets or episode IDs, but this must be **one candidate generator, not the gatekeeper**. Hard two-stage routing suffers from early-commitment error: if the planner chooses the wrong synonym, concept, or episode, downstream retrieval cannot recover. Run lexical and semantic retrieval in parallel with tag routing and fuse the lists.

### Failure modes by mechanism

| Mechanism | Where it works | Characteristic failures |
|---|---|---|
| Pure facet filtering | Stable repeated scenarios with excellent annotation | Untagged clips, taxonomy drift, wrong normalization, novel scenario phrasing, over-strict intersections |
| FTS/BM25 | Exact objections, names, technical terms, signature phrases | Paraphrases, implicit situations, vocabulary mismatch, ASR errors |
| Dense retrieval | Paraphrases and semantically similar cases | Exact identifiers/quotes may be diluted; generic thematic matches; embedding-model drift |
| LLM catalog routing | Human-like decomposition of rich scenarios | Hallucinated concepts, inconsistent routing, early commitment, token cost |
| Hybrid + reranking | Mixed exact and semantic cases; best recovery path | More components, score calibration, versioning, and evaluation burden |

Pure tag filtering particularly fails for “I will sit this out until prices collapse” when the indexed raw tag is `timing-objection` and the clip never says “market crash”; lexical search may also miss it, while a suitable dense model may recover it. Conversely, semantic search may return generic market-risk coaching and miss Olga’s exact memorable sentence, where FTS should dominate. Hybrid retrieval exists precisely because dense and sparse legs address different failures.[^39][^36][^14]

***

## E. Pattern trade-offs

### End-to-end comparison

Scores are relative architectural assessments for the stated 100–500-file, per-persona offline corpus; they are design judgments, not benchmark results.

| Pattern | Storage complexity | Build token cost | Exact 3–5 precision potential | Maintenance/debuggability | Verdict |
|---|---:|---:|---:|---:|---|
| Flat JSON + raw tags + application scan | 1/5 | 2/5 | 2/5 | 3/5 initially, 1/5 after schema growth | Keep only as export or MVP baseline |
| JSONL append log + in-memory indexes | 3/5 | 2/5 | 2–3/5 | 3/5 with disciplined replay; otherwise 1/5 | Add only for audit/sync requirements |
| SQLite normalized facets only | 2/5 | 2/5 | 3/5 | 5/5 | Strong deterministic baseline, insufficient recall alone |
| SQLite + facets + FTS5 | 2/5 | 2/5 | 4/5 | 5/5 | **Recommended first production milestone** |
| SQLite + facets + FTS5 + embeddings + rerank | 3/5 | 3/5 | 5/5 if evaluated | 4/5 | **Recommended target architecture** |
| DuckDB-centered hybrid | 3/5 | 3/5 | 4/5 | 3/5 | Better for analytics than serving/mutation |
| Dedicated vector DB + metadata store | 5/5 | 3/5 | 5/5 | 3/5 | Defer until scale/concurrency proves need |
| Generated wiki/files + summaries | 4/5 | 5/5 | 2/5 for verbatim behavior | 1/5 | Correctly discarded |

“Build token cost” separates storage from LLM work. Moving JSON to SQLite does not itself cost tokens. The main token drivers are episode boundary detection, raw facet/move assignment, synonym adjudication, and optional reranking. Embedding inference is compute cost rather than LLM authoring-token cost unless a metered API is used.

***

## Incremental indexing design

### Change detection

Track independent version keys:

| Layer | Invalidation key |
|---|---|
| Source parsing | `source_hash + parser_version` |
| Episode/span extraction | `source_hash + segmenter_version` |
| Raw tags/moves | `span_hash + extractor_prompt_hash + model_id` |
| Normalization | `raw_label + facet + vocabulary_version + normalizer_version` |
| FTS | `retrieval_text_hash + tokenizer_config` |
| Embedding | `retrieval_text_hash + embedding_model_revision` |
| Reranker | Query-time version logged; no corpus rebuild unless features change |

When one source changes, build its replacement records in a transaction, validate all coordinates, update FTS/embeddings, tombstone the prior source revision, and commit atomically. SQLite UPSERT supports conflict-driven insert-or-update behavior for uniquely keyed records. For immutable-source policy violations, preserving both source revisions is safer than mutating old evidence in place.[^5]

### Reproducible exports

Generate these artifacts from SQLite:

- `index.export.json` — deterministic, sorted, human-readable current state;
- `records.export.jsonl` — one current record per line for streaming/tools;
- `vocabulary.export.json` — concepts, aliases, and relations;
- `retrieval-eval.jsonl` — scenario, expected record IDs, retrieved IDs, component scores;
- optional `decisions.jsonl` — append-only extraction/normalization decisions.

This gives text-level auditability without sacrificing an indexed relational runtime.

***

## Evaluation and acceptance

### Build a persona-specific gold set

Before tuning vectors or fusion, create a reviewed set of realistic authoring scenarios spanning:

- exact phrases and named entities;
- paraphrased situations;
- cross-cutting topic/situation combinations;
- sparse evidence;
- repeated advice across multiple sources;
- negative controls where no authentic evidence exists;
- cases needing a full exchange rather than one sentence;
- ASR/noisy transcripts.

For each scenario, label relevant `span_id`s and episode-level relevance, with graded judgments such as `essential`, `useful`, and `irrelevant`. Evaluate retrieval separately from SKILL authoring so failures can be assigned to indexing, ranking, or generation. A stable golden dataset and component-level retrieval tests are standard methods for making RAG changes attributable and reproducible.[^40]

### Metrics aligned to the task

Use:

- `Recall@20` or `Recall@30` for first-stage candidate coverage;
- `nDCG@10` for ranked graded relevance;
- `Precision@5` for the actual evidence budget;
- `MRR` for whether at least one excellent grounding clip appears immediately;
- `episode coverage` for trigger-to-response completeness;
- `duplicate-overlap rate` for wasted context;
- `source diversity` and `episode diversity` as diagnostics, not unconditional objectives;
- `unsupported-scenario abstention` for cases with no adequate evidence.

Recall@K measures relevant-item coverage, nDCG rewards highly relevant items placed near the top, and MRR measures the rank of the first relevant result. Report scores by scenario type because one aggregate can conceal failures in rare but important behaviors.[^41][^42][^40]

### Required ablations

Benchmark on the same gold set:

1. tags only;
2. FTS only;
3. dense only;
4. tags + FTS;
5. FTS + dense fusion;
6. facets + FTS + dense;
7. the above plus reranking;
8. child-only retrieval versus child-to-parent expansion.

No embedding model, chunk size, fusion formula, or reranker should become architectural doctrine without this ablation. Retrieval research finds that no single method dominates every dataset and that BM25 remains a robust baseline, so TrainerTwin’s own scenarios must decide the final weights.[^16]

***

## Concrete implementation roadmap

### Phase 1: relationalize without changing behavior

- Keep current extractor and immutable raw files.
- Introduce SQLite tables for source, record, assignment, and run metadata.
- Import current raw typed tags unchanged.
- Add deterministic JSON/JSONL exports.
- Add coordinate validation and source-hash verification.
- Create parent `episode` and child `span` links, even if initial episodes follow natural landmarks.

**Exit criterion:** every current index record round-trips through SQLite and re-slices identical verbatim text.

### Phase 2: controlled vocabulary

- Add stable concept IDs, labels, aliases, broader/related relations, and concept status.
- Implement deterministic exact/alias normalization.
- Preserve unresolved labels instead of forcing matches.
- Add an LLM-assisted review queue for merge/broader/narrower/new decisions.
- Version mappings and vocabulary changes independently from extraction.

**Exit criterion:** slug spelling changes do not alter retrieval identity; all mappings are reversible and auditable.

### Phase 3: lexical retrieval baseline

- Build FTS5 over authoritative verbatim plus deterministic metadata projection.
- Implement typed query plans and soft facet scoring.
- Add candidate traces and evidence-set deduplication.
- Establish the gold scenario suite and baseline metrics.

**Exit criterion:** measurable `Precision@5`, candidate recall, and exact score explanations for every returned clip.

### Phase 4: semantic augmentation

- Embed child spans and optionally episode-level deterministic projections.
- Run exact local vector search first; introduce ANN only if measured latency requires it.
- Fuse FTS and dense candidates; benchmark RRF and calibrated weighted fusion.
- Add parent/neighbor expansion after selection.

**Exit criterion:** semantic augmentation improves target metrics on paraphrase and cross-cutting cases without degrading exact-phrase cases.

### Phase 5: reranking and authoring contract

- Add a constrained cross-encoder or LLM relevance reranker for a small candidate pool.
- Select a diverse 3–5 evidence set rather than the five highest independent scores.
- Pass only verified source-sliced text, coordinates, and structured retrieval reasons to the authoring agent.
- Require abstention when evidence quality falls below a validated threshold.

**Exit criterion:** the authoring agent receives sufficient trigger, behavioral flow, and authentic phrasing without loading irrelevant corpus sections.

***

## Final architecture

```text
immutable source files
        |
        v
hash + deterministic parsing --------> source revisions
        |
        v
LLM/rule segmentation and observation
(raw boundaries, raw tags, moves, entities; no summaries)
        |
        v
SQLite current-state index
  source -> episode -> span -> move
  concept <- assignment -> record
  labels/aliases/relations
  FTS5 + versioned embedding side table
        |
        +----> deterministic JSON/JSONL exports
        +----> optional append-only decision log
        |
        v
validated query plan
        |
        +--> facets/aliases
        +--> FTS lexical search
        +--> dense semantic search
        +--> optional episode evidence
        |
        v
fusion -> rerank -> overlap removal -> diversity/coverage selection
        |
        v
3–5 record IDs + exact coordinates + score trace
        |
        v
application verifies hash and slices verbatim source text
        |
        v
SKILL.md authoring agent
```

The core pivot is sound: **grouping belongs in indexed relationships and facets, not in filesystem topology**. The important refinement is that “flat records” should describe the logical model, not force flat physical representation. A normalized SQLite graph-of-records gives multi-membership, stable identities, hierarchy, provenance, transactional incremental updates, lexical search, and local semantic augmentation while preserving the raw files as the sole evidence authority.

---

## References

1. [1. Overview of FTS5](https://sqlite.org/fts5.html)

2. [The json_insert...](https://sqlite.org/json1.html)

3. [Generated Columns - SQLite](https://sqlite.org/gencol.html)

4. [Write-Ahead Logging](https://www.sqlite.org/wal.html)

5. [UPSERT](https://sqlite.org/lang_upsert.html)

6. [Recursive retriever](https://developers.llamaindex.ai/python/framework-api-reference/packs/recursive_retriever/)

7. [Metadata References...](https://developers.llamaindex.ai/python/framework/integrations/retrievers/recurisve_retriever_nodes_braintrust/)

8. [Auto Merging Retriever - LlamaParse documentation](https://developers.llamaindex.ai/python/framework/integrations/retrievers/auto_merging_retriever/)

9. [Hierarchical Parent–Child Retrieval for Multi-Turn RAG ...](https://arxiv.org/html/2605.00631v1) - Our approach implements a hierarchical parent–child RAG pipeline that separates fine-grained child-l...

10. [SKOS Simple Knowledge Organization System Primer](https://www.w3.org/2006/07/SWD/SKOS/primer/primer-20080826.html)

11. [SKOS Simple Knowledge Organization System Primer](https://www.w3.org/TR/skos-primer/)

12. [SKOS Simple Knowledge Organization System Reference - W3C](https://www.w3.org/TR/skos-reference/)

13. [Simple Knowledge Organization System (SKOS) (IEKO)](https://www.isko.org/cyclo/skos.htm) - SKOS (Simple Knowledge Organization System) is a recommendation from the World Wide Web Consortium (...

14. [landing_page/qdrant-landing/content/documentation/search ...](https://github.com/qdrant/landing_page/blob/master/qdrant-landing/content/documentation/search-tuning/hybrid-search.md) - Landing page for qdrant.tech. Contribute to qdrant/landing_page development by creating an account o...

15. [Contextual Retrieval in AI Systems \ Anthropic](https://www.anthropic.com/engineering/contextual-retrieval) - Explore how Anthropic enhances AI systems through advanced contextual retrieval methods. Learn about...

16. [BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/html/2104.08663)

17. [JSON Lines](https://jsonlines.org/)

18. [Why JSON and JSON Lines - NCBI](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/file-formats/metadata-files/why-jsonl/) - Here are some explanations and justifications for using JSON and JSON Lines formats for delivering m...

19. [JSON](https://duckdb.org/docs/0.8/extensions/json) - The json extension is a loadable extension that implements SQL functions that are useful for reading...

20. [Loading JSON](https://duckdb.org/docs/lts/data/json/loading_json.html) - The DuckDB JSON reader can automatically infer which configuration flags to use by analyzing the JSO...

21. [concurrency.md](https://duckdb.org/docs/stable/connect/concurrency.md)

22. [raw.githubusercontent.com](https://raw.githubusercontent.com/asg017/sqlite-vec/main/README.md)

23. [Vec1: Vec1 Vector Extension - sqlite.org](https://sqlite.org/vec1/doc/trunk/doc/vec1.md)

24. [Taxonomies and controlled vocabularies best practices for ...](https://link.springer.com/content/pdf/10.1057/dam.2010.29.pdf?error=cookies_not_supported&code=fcdc8770-3726-4bec-9bb8-e27057366d49)

25. [Passage Segmentation of Documents for Extractive ...](https://arxiv.org/html/2501.09940v1)

26. [A Comparative Study of Mixture Models for Automatic Topic ...](https://aclanthology.org/I08-2133.pdf)

27. [An Empirical Study of Topic Transition in Dialogue](https://ar5iv.labs.arxiv.org/html/2111.14188) - Transitioning between topics is a natural component of human dialog. Although topic transition has b...

28. [1](http://www.eecs.qmul.ac.uk/~mpurver/papers/purver11slu.pdf)

29. [With a Little Help from my (Linguistic) Friends: Topic Segmentation of Multi-party Casual Conversations](https://ar5iv.labs.arxiv.org/html/2402.02837) - Topics play an important role in the global organisation of a conversation as what is currently disc...

30. [ISO 24617-2:2020 - ISO 24617-2:2020 - cdn.standards.iteh.ai](https://cdn.standards.iteh.ai/samples/76443/f6269d64a09443c691ff4831ce33e8ab/ISO-24617-2-2020.pdf)

31. [ISO-Standard Domain-Independent Dialogue Act Tagging ...](https://iris.unitn.it/retrieve/e3835195-0d3c-72ef-e053-3705fe0ad821/C18-1300.pdf) - by S Mezza · Cited by 56 — This annotation scheme proposes a taxonomy of 42 tags, describing both se...

32. [Towards an ISO standard for dialogue act annotation](https://people.ict.usc.edu/~traum/Papers/lrec2010-iso-dacts-paper.pdf)

33. [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval?_bhlid=a960fa4c634372a583b1aa394fd584d859fc4447) - Anthropic is an AI safety and research company that's working to build reliable, interpretable, and ...

34. [Overview of FTS5](https://sqlite.org/docsrc/raw/9eca0ea509ae3e4d7b3cc279f4a18ead20604d4c?at=fts5.in)

35. [Qdrant Overview](https://qdrant.tech/documentation/overview/) - Qdrant overview covering vector embeddings, hybrid retrieval with dense and sparse vectors, client-s...

36. [Hybrid Search - Qdrant](https://qdrant.tech/documentation/search/text-search/hybrid-search/) - Build hybrid search pipelines in Qdrant by combining dense semantic vectors and sparse lexical vecto...

37. [From BM25 to Corrective RAG: Benchmarking Retrieval ...](https://arxiv.org/html/2604.01733v1)

38. [BIT.UA at CLEF 2026](https://arxiv.org/html/2609.04999v1)

39. [Hybrid and Multi-Stage Queries](https://qdrant.tech/documentation/search/hybrid-queries/) - Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer cu...

40. [How to test your RAG pipeline (before and after you ship) - Braintrust](https://www.braintrust.dev/articles/how-to-test-rag-pipeline) - A six-step runbook for testing RAG pipelines: build a golden dataset, evaluate retrieval and generat...

41. [Evaluation Measures in Information Retrieval](https://www.pinecone.io/learn/offline-evaluation/) - Evaluation of information retrieval (IR) systems is critical to making well-informed design decision...

42. [Retrieval Evaluation | MongoDB University](https://learn.mongodb.com/learn/course/retrieval-evaluation/retrieval-evaluation/retrieval-evaluation-metrics)

