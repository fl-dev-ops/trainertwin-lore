# TrainerTwin Indexing and Retrieval Architecture

## Executive recommendation

TrainerTwin should **retain its current item boundaries and immutable raw files**, but stop treating `index.json` as the serving index. Keep the JSON as the canonical, portable build artifact and compile it into a per-creator **SQLite database with normalized facets, FTS5, and locally stored embeddings**. At this corpus size—roughly 300 to 2,400 items per creator—there is no architectural reason to introduce a remote vector database, a generated wiki, or a heavyweight knowledge graph.

The core retrieval design should be:

1. Parse the requested encounter into a **scenario frame**: domain object, learner role/state, trigger or objection, trainer objective, desired pedagogical moves, constraints, and excluded meanings.
2. Run **parallel lexical and dense candidate retrieval** over compact, behavior-aware item records.
3. Fuse rankings, then rerank only the top 20–40 candidates against the full scenario frame.
4. Select a **set** of 3–8 passages for complementary evidence roles—not merely the top 5 individually relevant passages.
5. Expand local context only when needed by following source adjacency, then have deterministic code extract exact numbered lines and verify the source hash.
6. Refuse or request review when the selected set fails a formal sufficiency contract.

The most important change is therefore not a new database. It is a new **behavioral event schema** and a **set-level evidence selection step**.

## Architectural principles

TrainerTwin is not ordinary question-answering RAG. Its retrieval target is an instructional encounter consisting of several jointly necessary elements: the situation, learner behavior, trainer interpretation, trainer action, and often the expected follow-up. A passage can be topically correct yet useless for reproducing the trainer’s behavior.

This implies five design rules:

- **Items remain evidence pointers, not generated knowledge objects.** The authoritative content remains the immutable raw file plus line span.
- **Taxonomy is multi-axial.** “Closure,” “candidate hesitation,” and “ask for a concrete example” belong to different dimensions and must not compete as peer tags.
- **Hierarchy is a view, not storage.** A single topic tree cannot faithfully place one item that simultaneously concerns JavaScript closures, interview diagnosis, learner uncertainty, and Socratic prompting.
- **Retrieval optimizes passage-set utility.** The output is a coherent evidence bundle with coverage and diversity constraints.
- **Every generated claim must remain traceable.** LLMs may identify item IDs and spans, but deterministic code remains responsible for extracting citations.

## Storage decision

### Recommended pattern

Use three layers:

| Layer | Purpose | Recommended form |
|---|---|---|
| Raw evidence | Immutable source of truth | Existing numbered text files |
| Canonical build artifact | Reproducibility, debugging, export | Versioned `index.json` or JSONL |
| Serving projection | Filtering, lexical retrieval, joins, ranking features | Per-creator SQLite database |

SQLite FTS5 provides built-in BM25 ranking and allows different weights per indexed column, which is directly useful for weighting normalized behavior labels above raw excerpts or generic source titles. SQLite also supports external-content FTS tables, although such tables must be kept synchronized with the content table; triggers or deterministic full rebuilds are the documented approaches. For TrainerTwin, deterministic rebuilds from `index.json` are preferable to triggers because the index is already a generated artifact and its small size makes rebuilds simple.[^1][^2]

### Why not a hierarchy

A topic tree is useful for browsing, but poor as the canonical representation because TrainerTwin’s useful distinctions are orthogonal:

- Subject: closures, Dubai property, salary negotiation.
- Encounter: objection, misconception, weak answer, resistance to feedback.
- Learner state: vague, overconfident, hesitant, defensive, confused.
- Trainer move: probe, withhold answer, challenge assumption, model an answer, reframe.
- Intent: diagnose, practice, correct, assess, motivate.
- Evidence role: scenario setup, behavioral rule, example wording, consequence, exception.

Store these as facets and construct topic trees dynamically for navigation or analysis. Faceted systems are explicitly designed around multiple independent perspectives over the same objects rather than one fixed hierarchy.[^3]

### Why not a graph-first system

A graph can help later with explicit relationships such as `move responds_to learner_state`, `item elaborates item`, or `principle contradicted_by exception`. It should not be the initial retrieval engine. Most TrainerTwin queries are local ranking problems over a few thousand records; graph traversal adds ontology and maintenance cost before there is evidence that multi-hop graph reasoning improves passage recall.

Start with two small relational edge tables:

- `item_edges(from_item_id, relation, to_item_id, confidence)` for `adjacent_to`, `elaborates`, `example_of`, `contrasts_with`, and `same_episode_as`.
- `concept_alias(alias, canonical_type, canonical_value)` for creator-specific vocabulary and paraphrases.

Promote this to a graph service only if evaluation shows recurring failures that require two or more relation hops and cannot be solved by facets plus adjacency expansion.

## Behavioral indexing model

### Separate content from action

The metadata must distinguish **what is being discussed** from **what the trainer is doing**. Tutorial-dialogue research makes this same separation: dialogue acts capture the intent or action underlying an utterance, with pedagogical categories such as prompts and hints layered separately from subject matter. Multi-dimensional tutorial schemes also represent communicative action, rhetorical form, and semantic content as separate dimensions rather than one flat label.[^4][^5][^6]

Use a compact, controlled core vocabulary plus creator-specific extensions. Do not ask the indexing model to invent unrestricted tags for every item.

| Facet | Question answered | Example values |
|---|---|---|
| `domain` | What subject is involved? | `javascript.closures`, `real_estate.market_timing` |
| `encounter_type` | What kind of practice moment is this? | `objection`, `mock_interview`, `feedback_review` |
| `learner_move` | What did the learner/client do? | `argues_with_feedback`, `gives_vague_answer`, `delays_decision` |
| `learner_state` | What state is inferred or explicitly visible? | `hesitant`, `defensive`, `overconfident`, `confused` |
| `trigger` | What causes the trainer response? | `unsupported_claim`, `price_drop_objection`, `missing_example` |
| `trainer_move` | What instructional action occurs? | `probe`, `challenge`, `wait`, `reframe`, `model`, `direct_correct` |
| `trainer_intent` | Why is the move used? | `diagnose`, `surface_assumption`, `increase_specificity`, `test_transfer` |
| `response_policy` | What conditional rule is implied? | `if_vague_then_request_case`, `if_defensive_then_seek_evidence` |
| `interaction_phase` | Where in the encounter? | `open`, `diagnose`, `challenge`, `practice`, `debrief`, `close` |
| `evidence_role` | What can this span support? | `setup`, `principle`, `move_example`, `wording`, `failure`, `exception` |
| `content_mode` | Is it knowledge or behavior? | `declarative`, `procedural`, `behavioral`, `demonstration`, `meta` |

Learner state should be allowed to be `unknown`; inferred mental states should carry lower confidence than directly observable learner moves. Tutor-strategy research likewise treats the learner move/status and the tutor’s next strategy as linked but non-deterministic decisions, affected by proficiency, task difficulty, dialogue history, and prior support.[^7]

### Represent sequences, not only labels

Some trainer identity lives in short action sequences rather than isolated acts. For example:

`vague answer -> ask for example -> wait -> challenge inconsistency -> request retry`

Add `move_sequence` as an ordered list when the span contains multiple meaningful actions. Dialogue research has found value in analyzing both individual acts and adjacent act pairs, supporting this sequence-oriented representation.[^8]

Do not force every index item to contain an elaborate sequence. A single-item `trainer_move` remains valid; `move_sequence` is populated only where the evidence shows progression.

## Recommended item schema

The schema below keeps the current provenance fields and adds retrieval-oriented structure. Fields marked as controlled should use a versioned vocabulary; free-text fields are concise search surrogates, not quotes.

```json
{
  "item_id": "vasanth:src_017:00126-00167:v3",
  "source_id": "youtube-video-...",
  "path": "youtube/video/...md",
  "source_sha256": "abc123...",
  "index_schema_version": "3.0",
  "indexer_model": "google/gemini-3.8-flash",
  "indexer_prompt_version": "behavior-v4",

  "span": {
    "start_line": 126,
    "end_line": 167,
    "speaker_turn_start": 41,
    "speaker_turn_end": 46
  },
  "basis": "turn_group",
  "parent_outline_id": null,
  "prev_item_id": "...",
  "next_item_id": "...",

  "title": "Candidate argues with feedback instead of testing the critique",
  "retrieval_summary": "Mock interviewer responds to a defensive candidate by asking for evidence and a concrete counterexample before explaining.",
  "participants": ["trainer", "candidate"],

  "domain": ["frontend.interviewing", "feedback_reasoning"],
  "encounter_type": ["mock_interview", "feedback_resistance"],
  "learner_move": ["argues_with_feedback", "asserts_without_evidence"],
  "learner_state": ["defensive"],
  "trigger": ["feedback_rejected"],
  "trainer_move": ["probe_for_evidence", "request_concrete_example", "withhold_explanation"],
  "trainer_intent": ["diagnose_reasoning", "create_self_correction"],
  "interaction_phase": ["challenge", "practice"],
  "content_mode": ["behavioral", "demonstration"],
  "evidence_role": ["move_example", "wording", "response_policy"],

  "response_policies": [
    {
      "condition": "learner rejects feedback without evidence",
      "action": "ask for a concrete counterexample before explaining",
      "avoid": "debating the learner immediately",
      "confidence": 0.88
    }
  ],
  "move_sequence": [
    "acknowledge",
    "probe_for_evidence",
    "wait",
    "request_retry"
  ],

  "entities": ["JavaScript", "closure"],
  "aliases": ["pushes back on critique", "defends wrong answer"],
  "negative_cues": ["not a closure tutorial", "not direct correction"],
  "specificity": "demonstrated",
  "metadata_confidence": 0.91,
  "needs_review": false,

  "quote_hash": "sha256-of-extracted-lines",
  "quote_char_count": 1840,
  "language": "en",
  "source_date": "2026-04-08"
}
```

### Field design notes

- `retrieval_summary` should state **actor + trigger + move + purpose**, not merely summarize the topic.
- `specificity` should distinguish `asserted`, `demonstrated`, and `inferred`. Demonstrated behavior is stronger persona evidence than a trainer’s abstract claim about what trainers should do.
- `negative_cues` help resolve collisions such as “closure explanation” versus “interviewer handling a weak closure answer.” They should be short, model-generated disambiguators, never evidence.
- `response_policies` are candidate rules for persona synthesis, not ground truth. The final persona author should cite the associated spans and require recurrence or strong explicit evidence.
- `quote_hash` detects accidental line drift. The quote itself may be cached for convenience, but it should always be reproducible from the raw source and line range.
- `metadata_confidence` should express annotation confidence, while retrieval score expresses query relevance. Never combine them into one opaque number before logging both.

## SQLite projection

A practical schema is:

```sql
CREATE TABLE source (
  source_id TEXT PRIMARY KEY,
  path TEXT NOT NULL,
  sha256 TEXT NOT NULL,
  basis TEXT,
  source_type TEXT,
  source_date TEXT
);

CREATE TABLE item (
  item_id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL REFERENCES source(source_id),
  start_line INTEGER NOT NULL,
  end_line INTEGER NOT NULL,
  title TEXT NOT NULL,
  retrieval_summary TEXT NOT NULL,
  quote_text TEXT NOT NULL,
  quote_hash TEXT NOT NULL,
  content_mode TEXT,
  specificity TEXT,
  metadata_confidence REAL,
  prev_item_id TEXT,
  next_item_id TEXT,
  metadata_json TEXT NOT NULL
);

CREATE TABLE item_facet (
  item_id TEXT NOT NULL REFERENCES item(item_id),
  facet_type TEXT NOT NULL,
  facet_value TEXT NOT NULL,
  confidence REAL,
  PRIMARY KEY (item_id, facet_type, facet_value)
);

CREATE INDEX item_facet_lookup
ON item_facet(facet_type, facet_value, item_id);

CREATE TABLE item_edge (
  from_item_id TEXT NOT NULL,
  relation TEXT NOT NULL,
  to_item_id TEXT NOT NULL,
  confidence REAL,
  PRIMARY KEY(from_item_id, relation, to_item_id)
);

CREATE VIRTUAL TABLE item_fts USING fts5(
  item_id UNINDEXED,
  title,
  retrieval_summary,
  behavior_text,
  domain_text,
  quote_text,
  tokenize='unicode61'
);
```

A starting FTS weighting can emphasize `behavior_text` and `title`, then `retrieval_summary` and `domain_text`, while leaving `quote_text` with a lower weight. FTS5 explicitly permits per-column BM25 weights. SQLite’s built-in JSON functions can retain flexible metadata while normalized facet rows handle filters and aggregation.[^9][^1]

At only 2,400 records, exact cosine comparison over local embeddings is entirely reasonable; approximate nearest-neighbor indexing is unnecessary until measurements show otherwise. A 768-dimensional float32 matrix for 2,400 items is only about 7.4 MB before metadata. If keeping all retrieval inside SQLite is operationally useful, lightweight extensions can store and query vectors locally, including `sqlite-vec` virtual tables. However, a NumPy matrix keyed by `item_id` is simpler and easier to benchmark initially.[^10]

## Retrieval pipeline

### Query compilation

Do not send the raw user sentence independently to BM25, embeddings, and a reranker. First compile it into a validated scenario frame:

```json
{
  "domain": ["frontend.interviewing"],
  "roles": {"trainer": "interviewer", "learner": "candidate"},
  "encounter_type": ["feedback_resistance"],
  "learner_move": ["argues_with_feedback"],
  "learner_state": ["defensive"],
  "trigger": ["critique_of_answer"],
  "desired_moves": ["probe_for_evidence", "request_retry"],
  "must_cover": ["trainer_behavior", "example_language", "decision_rule"],
  "must_not": ["generic technical explanation only"],
  "query_variants": [
    "candidate pushes back on interviewer critique",
    "learner defends an answer instead of considering feedback"
  ]
}
```

An inexpensive LLM can perform this parsing with strict schema output. Treat its facets as **soft preferences**, not hard filters, except for explicit creator, language, date, or source constraints. A mistaken behavioral classification should lower ranking quality, not eliminate the relevant item.

### Candidate generation

Run two independent legs:

- **Lexical leg:** FTS5/BM25 over title, retrieval summary, normalized facet text, aliases, and lower-weight quote text. Retrieve top 40–60.
- **Dense leg:** Embed a behavior-aware document string and retrieve top 40–60 by exact cosine similarity.

Recommended embedding text:

```text
Situation: mock interview; candidate receives critique.
Learner behavior: argues with feedback; gives unsupported defense.
Trainer behavior: asks for evidence; requests concrete example; delays explanation.
Purpose: diagnose reasoning and create self-correction.
Domain: frontend interviewing; JavaScript closure.
Evidence: [deterministically extracted span]
```

This is materially different from embedding raw transcripts. The embedding operates over an already grounded instructional event whose boundaries came from the working indexing pipeline. A single embedding should not be expected to preserve every aspect, so a useful experiment is to maintain two vectors per item: `situation_vector` for domain/encounter/learner state and `move_vector` for trainer behavior/policy. The query frame produces matching vectors, and both ranked lists enter fusion.

Sparse and dense retrieval are complementary: sparse systems retain exact lexical signals, while dense systems capture paraphrastic similarity. Hybrid methods combine these strengths, and rank-based fusion avoids directly comparing incompatible score scales. Reciprocal Rank Fusion is a strong no-training-data baseline, but it is not automatically optimal: research has found it parameter-sensitive and found that a learned convex combination can outperform it with a small labeled set.[^11][^12][^13]

Therefore:

- Start with weighted RRF because it is simple and calibration-free.
- Log every component score and rank.
- After collecting roughly 100–200 judged scenario-item pairs, tune a logistic or linear fusion model using BM25 score/rank, dense similarities, facet matches, source diversity, metadata confidence, and item specificity.

### Reranking

Rerank the fused top 20–40 candidates against the structured scenario frame. There are two sensible tiers:

| Reranker | Strength | Weakness | TrainerTwin fit |
|---|---|---|---|
| Local cross-encoder | Stable pairwise scores, low marginal cost, easy batching | Generic models may miss creator-specific pedagogy | Default production reranker after a suitable benchmark win |
| Small/fast LLM with strict JSON | Understands nuanced behavior and negative constraints | Higher variance/cost; requires careful candidate formatting | Good initial reranker and adjudicator |
| Large LLM listwise reranker | Strong comparative judgment | Cost, positional sensitivity, and list-size limitations | Evaluation oracle or difficult-query fallback |

The established retrieve-and-rerank pattern uses a cheap first stage to obtain candidates and a cross-encoder to score query-document pairs more precisely. LLM listwise reranking can improve zero-shot ranking by considering candidates jointly, but practical implementations face context limits and often use sliding windows. For TrainerTwin, listwise LLM reranking should see compact metadata cards plus short evidence extracts—not all source files.[^14][^15][^16][^17]

Require the reranker to return only:

```json
{
  "item_id": "...",
  "relevance": 0,
  "supported_roles": ["trainer_behavior", "example_language"],
  "exclusion_reason": null
}
```

No generated quotations and no free-form rationale are needed in production. Direct scoring also reduces token usage and avoids leaking invented language into the evidence path.

### Set selection

The best five independent scores frequently produce five redundant examples. Instead, solve a constrained selection problem over the reranked candidates.

Target evidence slots:

1. **Encounter evidence:** situation, roles, and trigger.
2. **Diagnostic evidence:** how the trainer interprets the learner’s move.
3. **Action evidence:** what the trainer does next.
4. **Language evidence:** exact wording or signature phrasing.
5. **Policy evidence:** conditional rule, boundary, escalation, or exception.

Select 3–8 items maximizing:

- Query relevance.
- Required-slot coverage.
- Behavioral specificity.
- Source and episode diversity.
- Novel information.

Penalize:

- Overlapping or adjacent spans that repeat the same content.
- Multiple passages supporting only the same evidence slot.
- Generic domain explanation without encounter behavior.
- Low-confidence inferred learner states.

Maximal Marginal Relevance was designed to trade off query relevance against novelty and reduce redundancy in retrieval and summarization. TrainerTwin can use an MMR-like greedy selector, augmented with explicit slot bonuses and constraints. This is more aligned with scenario authoring than plain top-k retrieval.[^18]

### Context expansion

After selecting an item, inspect `prev_item_id` and `next_item_id` only when one of these conditions holds:

- The selected span begins with an unresolved pronoun or continuation.
- The learner trigger occurs in the preceding item.
- The trainer response or consequence continues into the next item.
- The sufficiency checker reports a missing transition.

Expansion should add whole existing index items or bounded line spans; it must never rewrite or physically chunk the source. The final extraction service verifies `source_sha256`, line bounds, and `quote_hash` before returning evidence.

## Options and trade-offs

| Strategy | Recall for paraphrase | Behavioral precision | Runtime/cost | Main failure | Recommendation |
|---|---:|---:|---:|---|---|
| Flat JSON scan by LLM | Potentially high on tiny corpora | Variable | Highest per query | Attention dilution, ordering effects, inconsistent coverage | Do not use as primary retrieval |
| BM25 on titles/tags | Low–medium | Medium only if behavior tags are explicit | Very low | Vocabulary mismatch | Always include as one candidate leg |
| Dense on titles | Medium | Low–medium | Very low locally | Titles compress away evidence and behavior | Insufficient alone |
| Dense on raw quotes | Medium | Low–medium | Low | Topic similarity dominates behavior | Secondary signal only |
| Dense on behavioral cards | High potential | High potential | Low | Dependent on annotation quality | Recommended dense representation |
| Hard LLM source router | Variable | Medium–high | Medium | Early false negatives are unrecoverable | Avoid as a mandatory gate |
| Soft LLM query router | High | High | Low–medium | Facet parsing errors | Recommended for query compilation |
| Hybrid + rerank | High | Highest expected | Low at this scale | More components to evaluate | Recommended default |
| Graph-first retrieval | Useful for explicit multi-hop queries | Potentially high | Highest engineering cost | Ontology drift, sparse edges | Defer until failures justify it |

Long-context prompting is not a substitute for this pipeline. Empirical work shows that model performance can change substantially with the position of relevant information and often degrades for evidence in the middle of long contexts. That finding directly supports presenting a small, ranked evidence set rather than hundreds or thousands of index items.[^19]

## Scenario discovery

### Use two semantic views

Auto-discovery should not run one generic clustering job over item titles. It should build two views:

- **Situation view:** domain + encounter type + learner move/state + trigger.
- **Response view:** trainer move + intent + response policy + interaction phase.

Cluster each view separately, then inspect their cross-product. A situation cluster such as `buyer delays for anticipated price drop` can pair with response patterns such as `probe comparison`, `surface cost of waiting`, or `do not pitch yet`. These intersections are closer to deployable scenarios than a broad topic cluster called `real estate objections`.

BERTopic provides a modular pipeline combining embeddings, dimensionality reduction, clustering, and class-based TF-IDF for interpretable cluster labels. Its default stack uses sentence transformers, UMAP, HDBSCAN, and c-TF-IDF, but the components can be replaced independently. HDBSCAN is useful here because it can identify varying-density clusters and mark unsupported points as noise rather than forcing every item into a scenario.[^20][^21][^22][^23]

### Discovery procedure

1. Exclude items classified only as generic exposition unless they also support a scenario role.
2. Compute situation and response embeddings from structured cards.
3. Cluster situation vectors using HDBSCAN or agglomerative clustering; run a parameter stability sweep rather than accepting one result.
4. Within each situation cluster, group by trainer move sequence or cluster response vectors.
5. Generate a candidate scenario only when the intersection has adequate evidence and recurrence.
6. Ask an LLM to label each candidate from 5–10 representative item cards, returning a scenario frame and item IDs—not quotes.
7. Deterministically extract evidence, run the sufficiency checker, and queue weak or near-duplicate scenarios for review.

### Scenario confidence

Rank discovered scenarios using:

```text
scenario_score =
  recurrence
  × source_diversity
  × behavioral_specificity
  × cluster_stability
  × evidence_slot_coverage
  × metadata_confidence
```

Use a penalty when a “scenario” is dominated by one long source, one repeated anecdote, or generic topic exposition. Report both `occurrence_count` and `independent_source_count`; twelve adjacent items from one webinar do not establish the same corpus-level pattern as six examples across six sessions.

### Persona discovery

Persona rules require stronger evidence than scenario facts. Aggregate recurring `response_policies` and move sequences across scenarios, then categorize them as:

- `explicit_rule`: trainer directly states the rule.
- `repeated_behavior`: same behavior demonstrated across independent sources.
- `single_demonstration`: useful for a scenario but not safe as a global persona trait.
- `inferred_pattern`: candidate for human review only.

A practical default is to admit a behavior into `persona.md` only when it is either explicitly stated once with clear evidence or demonstrated in at least three independent encounters across at least two sources. This is an operating policy to validate, not a universal scientific threshold.

## Sufficiency contract

Relevance is necessary but not sufficient. Before scenario generation, construct a machine-readable evidence plan:

```json
{
  "scenario_query_id": "sq_042",
  "required_slots": {
    "encounter": ["item_17"],
    "learner_position": ["item_17", "item_88"],
    "trainer_move": ["item_88", "item_91"],
    "decision_rule": ["item_91"],
    "signature_wording": ["item_103"]
  },
  "unsupported_slots": [],
  "source_count": 3,
  "independent_episode_count": 2,
  "contradictions": [],
  "decision": "sufficient"
}
```

### Proposed gate

A set is `sufficient` only if:

- Every mandatory scenario claim maps to at least one exact span.
- Encounter, learner stance, and trainer action are directly supported.
- At least one passage demonstrates behavior rather than merely naming a principle.
- The evidence includes three or more usable spans and no more than eight.
- No citation exceeds the 40-line rule.
- Source hashes and line bounds validate.
- Any inferred persona rule has recurrence or is explicitly marked as provisional.
- Contradictory advice is surfaced instead of silently merged.

Return `insufficient` with missing slots such as `trainer_move_not_demonstrated` or `only_generic_domain_explanation`. This is preferable to asking the authoring model to “make the scenario complete.”

### Claim ledger

Generation should produce structured claims before rendering Markdown:

```json
{
  "claim": "When the candidate becomes defensive, ask for evidence before correcting them.",
  "claim_type": "behavior_policy",
  "supporting_item_ids": ["item_88", "item_91"],
  "support_strength": "repeated_demonstration"
}
```

A deterministic validator checks that every externally attributed claim has supporting item IDs and that every quoted block equals the extracted raw lines. An LLM verifier may assess semantic entailment between claims and passages, but exact-quote integrity, span validity, and citation presence must remain deterministic.

Evaluation frameworks commonly separate context recall, context precision, and generated-answer faithfulness. Context recall asks whether all necessary reference evidence was retrieved; context precision asks whether relevant evidence is ranked above irrelevant material. Faithfulness evaluates whether generated claims can be supported by the supplied context. TrainerTwin should adopt these concepts but add behavioral-slot coverage and exact-span integrity because ordinary RAG metrics do not capture scenario completeness.[^24][^25][^26]

## Evaluation benchmark

### Gold-set construction

Create a versioned `trainertwin-qrels` benchmark with **120 initial information needs: 40 per creator**. This number is a practical starting budget rather than a statistical guarantee. Stratify each creator’s set across:

- 8 exact terminology/domain queries.
- 8 paraphrased scenario queries.
- 8 behavior-first queries with weak topical cues.
- 6 compositional queries requiring situation plus trainer move.
- 4 hard-negative pairs where topic matches but pedagogy does not.
- 3 persona-pattern queries requiring recurrence.
- 3 deliberately unsupported or under-supported scenarios.

For every query, have a domain-aware assessor label pooled candidates on a four-grade scale:

- `3`: directly supports a required scenario slot and is highly usable.
- `2`: relevant supporting evidence but incomplete or indirect.
- `1`: topically related but not useful for the requested behavior.
- `0`: irrelevant or contradictory.

Build the judgment pool from the union of top results from BM25, dense situation, dense move, hybrid, and LLM reranking. TREC-style pooling combines top-ranked outputs from diverse systems for human relevance judging and is a standard way to build reusable IR test collections without exhaustively judging the corpus. Preserve unjudged status rather than automatically treating every unpooled item as a confirmed negative during error analysis.[^27][^28]

### Metrics by stage

| Stage | Primary metrics | Why |
|---|---|---|
| Index annotation | Facet precision/recall, span-boundary acceptance, inter-annotator agreement | Determines whether behavior is represented correctly |
| Candidate generation | Recall@20, Recall@50 | Relevant items cannot be recovered after this stage |
| Ranking | nDCG@5, nDCG@8, MRR | Rewards graded relevance and early useful results |
| Set selection | Required-slot coverage, redundancy rate, source diversity | Measures evidence-bundle quality |
| Generation | Claim support rate, exact-quote accuracy, citation validity | Measures grounding |
| End product | Blind trainer-style preference, scenario fidelity rubric | Measures whether the `SKILL.md` output is useful |

BEIR identifies nDCG@k as a suitable balance for tasks with binary or graded relevance judgments and also reports precision, recall, and MAP. For TrainerTwin, candidate Recall@20 is the most important diagnostic metric, while nDCG@5 or nDCG@8 measures whether the final shortlist is ordered usefully.[^29]

### Sufficiency labels

For each query, assessors should also complete a slot rubric independent of overall relevance:

| Slot | 0 | 1 | 2 |
|---|---|---|---|
| Encounter | Missing | Inferred | Explicit |
| Learner stance | Missing | Partial | Explicit/demo |
| Trainer action | Missing | Named | Demonstrated |
| Rationale | Missing | Weak | Explicit/repeated |
| Wording | Missing | Generic | Distinctive verbatim evidence |
| Boundary/exception | Missing | Optional | Required and supported |

Compare the system’s sufficiency decision with the human decision using precision and recall. A false `sufficient` result is more harmful than a false `insufficient` result because it invites hallucinated completion, so tune this gate for high precision.

### Ablation matrix

Run the same qrels through:

1. BM25 on current title/tags.
2. BM25 on enriched behavioral fields.
3. Dense on title plus quote.
4. Dense on behavioral card.
5. BM25 plus dense with RRF.
6. Hybrid plus cross-encoder.
7. Hybrid plus LLM reranker.
8. Winning reranker plus set-level coverage/MMR selection.

This isolates whether gains come from the metadata, retriever, reranker, or selector. Also report results separately for behavior-first queries; a strong aggregate score can hide failure on the exact query type that motivated TrainerTwin.

### Regression tests

Add deterministic tests for every index build:

- All spans are within source line counts.
- `start_line <= end_line` and span length is at most 40 lines for citation candidates.
- Extracted quote hashes match.
- No item references an unknown source or edge.
- Controlled facet values belong to the active taxonomy version.
- Rebuilding from unchanged sources produces equivalent item IDs and provenance.
- Modified source hashes invalidate stale spans.
- Gold-query metrics do not regress beyond an agreed tolerance.

## Minimal implementation plan

### Phase 1: schema and baseline

1. Keep the existing indexing boundaries unchanged.
2. Add the multi-axis behavioral fields and `retrieval_summary` in a second enrichment pass over each existing span.
3. Preserve `index.json`; compile it into SQLite tables plus FTS5.
4. Implement BM25 retrieval and a transparent scoring log.
5. Build the first 120-query pooled benchmark before selecting an embedding model.

This phase proves whether explicit behavior metadata fixes the original failure better than another retrieval model alone.

### Phase 2: hybrid retrieval

1. Benchmark several local sentence-transformer-class models on `situation_card` and `move_card` representations.
2. Add exact cosine search; no ANN server.
3. Fuse top-50 lists using weighted RRF.
4. Rerank the top 30 with one local cross-encoder and the current Gemini Flash path.
5. Select final passages with slot coverage plus MMR and source-diversity constraints.

Models that support dense, sparse, and multi-vector representations in one family exist—BGE-M3 is one example and supports inputs up to 8,192 tokens. It is worth benchmarking, not adopting by assumption. ColBERT-style late interaction preserves token-level matching and can improve fine-grained retrieval, but it carries a larger storage and operational footprint than single-vector retrieval. At TrainerTwin’s scale, neither is necessary unless the qrels demonstrate a material win over simpler hybrid retrieval.[^30][^31][^32]

### Phase 3: discovery and learning

1. Cluster situation and response views separately.
2. Generate scenario candidates from stable intersections.
3. Require evidence-slot sufficiency before publishing a scenario.
4. Capture author accept/reject, passage removal/addition, and final selected spans.
5. Use those judgments to tune fusion weights and eventually train a small domain reranker.

### Stop conditions

Do not add a graph database, ANN service, or multi-agent router unless one of these measured conditions occurs:

- Exact dense scanning becomes a verified latency bottleneck.
- Corpus growth reaches a scale where memory or scan cost matters.
- More than 10% of benchmark failures demonstrably require graph expansion.
- Hard source routing improves Recall@20 rather than only reducing tokens.
- A complex model produces a statistically and operationally meaningful gain over the simple hybrid baseline.

## Concrete next step

The smallest high-value experiment is a **behavioral-schema retrieval bake-off on one creator**, preferably Vasanth because the long mock interviews provide the clearest distinction between technical topic and trainer behavior:

1. Hand-label 40 scenario queries and pooled relevance judgments.
2. Enrich the existing 2,339 items with `learner_move`, `learner_state`, `trainer_move`, `trainer_intent`, `interaction_phase`, `evidence_role`, and `retrieval_summary`.
3. Compare current retrieval, enriched FTS5, behavioral-card dense retrieval, and their hybrid.
4. Add reranking only after candidate Recall@20 is strong.
5. Add the set-level sufficiency gate before generating any `scenario.md`.

If only one architectural decision is implemented, it should be this: **convert each indexed span into a typed interaction event and retrieve evidence sets against a typed scenario frame**. SQLite, embeddings, and rerankers then become replaceable execution components rather than the source of TrainerTwin’s semantics.

---

## References

1. [1. Overview of FTS5](https://sqlite.org/fts5.html)

2. [SQLite FTS5 Extension](https://www.sqlite.org/fts5.html)

3. [[PDF] Dynamic Taxonomies and Faceted Search - ReadingSample - NET](https://beckassets.blob.core.windows.net/product/readingsample/9874479/9783642269257_excerpt_001.pdf)

4. [An Analysis of Human Tutors’ Actions in Tutorial Dialogues](https://cdn.aaai.org/ocs/15491/15491-68637-1-PB.pdf)

5. [CMR8](https://aclanthology.org/W11-0133.pdf)

6. [Question Ranking and Selection in Tutorial Dialogues](https://aclanthology.org/W12-2001.pdf)

7. [TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring](https://arxiv.org/html/2608.03952v2)

8. [LNCS 8474 - Identifying Effective Moves in Tutoring: On the Refinement of Dialogue Act Annotation Schemes](https://akvail.github.io/pubs/vail_its2014.pdf)

9. [The json_insert...](https://sqlite.org/json1.html)

10. [raw.githubusercontent.com](https://raw.githubusercontent.com/asg017/sqlite-vec/main/README.md)

11. [Out-of-Domain Semantics to the Rescue! Zero-Shot Hybrid ...](https://arxiv.org/html/2201.10582v1)

12. [An Analysis of Fusion Functions for Hybrid Retrieval](https://arxiv.org/abs/2210.11934) - by S Bruch · 2022 · Cited by 173 — we examine fusion by a convex. Reciprocal Rank Fusion (RRF) metho...

13. [CheckThat! Lab at CLEF 2026](https://arxiv.org/html/2607.24803)

14. [sentence-transformers/examples/sentence_transformer/applications/...](https://github.com/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/README.md) - State-of-the-Art Embeddings, Retrieval, and Reranking - huggingface/sentence-transformers

15. [sentence-transformers/examples/sentence_transformer/applications/retrieve_rerank/README.md at master · UKPLab/sentence-transformers](https://github.com/UKPLab/sentence-transformers/blob/master/examples/sentence_transformer/applications/retrieve_rerank/README.md) - State-of-the-Art Text Embeddings. Contribute to UKPLab/sentence-transformers development by creating...

16. [Hugging Face](https://huggingface.co/papers/2305.02156.md)

17. [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/html/2308.07107v4)

18. [[PDF] (1) USING MMR FOR DIVERSITY- BASED RERANKING AND (2 ...](https://www.cs.cmu.edu/~jgc/publication/MMR%20Diversity.pdf)

19. [Lost in the Middle: How Language Models Use Long Contexts](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf)

20. [BERTopic — BERTopic latest documentation](https://bertopic.readthedocs.io/en/latest/index.html)

21. [BERTopic Documentation - Read the Docs](https://bertopic.readthedocs.io/_/downloads/en/latest/pdf/)

22. [hdbscan - PyPI](https://pypi.org/project/hdbscan/) - Clustering based on density with variable density clusters

23. [API Reference — hdbscan 0.8.1 documentation](https://hdbscan.readthedocs.io/en/latest/api.html)

24. [Context Recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/) - Evaluation framework for your AI Application

25. [Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/) - Evaluation framework for your AI Application

26. [Ragas: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/html/2309.15217v2)

27. [[1504.06868] Autonomy and Reliability of Continuous Active Learning …](https://ar5iv.labs.arxiv.org/html/1504.06868) - We enhance the autonomy of the continuous active learning method shown by Cormack and Grossman (SIGI...

28. [Creation of Reliable Relevance Judgments in Information ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC4055211/) - Test collection is used to evaluate the information retrieval systems in laboratory-based evaluation...

29. [BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of ...](https://arxiv.org/html/2104.08663v2)

30. [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://arxiv.org/abs/2112.01488v2) - Neural information retrieval (IR) has greatly advanced search and other knowledge-intensive language...

31. [ColBERT: Efficient and Effective Passage Search via ...](https://arxiv.org/abs/2004.12832) - by O Khattab · 2020 · Cited by 3248 — ColBERT introduces a late interaction architecture that indepe...

32. [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) - Multi-Functionality: It can simultaneously perform the three common retrieval functionalities of emb...

