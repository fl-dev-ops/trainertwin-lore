# TrainerTwin: research-grounded direction

## Goal we are solving

TrainerTwin collects a person's public content, builds a source-backed person/knowledge wiki, and derives the information needed to create a useful, recognizable twin: what the person knows and teaches, how they express it, and how their communication varies with platform and situation. We must not confuse a plausible persona, public writing imitation, effective teaching, and demonstrated fidelity to a real individual.

This research pass reviews relevant methods, results and limitations from ten primary papers. It does not reproduce their experiments. Search-generated summaries were used for discovery only; claims below were checked against primary paper text. Proposed TrainerTwin design choices are explicitly recommendations, not results proved by those papers. No application code or experiment evaluator was changed during this pass.

## Executive conclusion

The evidence favors a **source-preserving, task-conditioned memory foundation**, with the wiki as a readable view, rather than a linear chain that repeatedly compresses public content until a personality description emerges.

Three distinct information products should share the same source foundation:

1. **Knowledge and methods:** concepts, claims, procedures, preconditions, steps, examples, constraints, exceptions, and stated views.
2. **Teaching/interaction cases:** situations, preceding questions or objections, responses, stated strategies and rationales, and reported/observed outcomes. Preserve whether an exchange is recorded, narrated, or illustrative.
3. **Expression examples:** original wording and structure, indexed by platform, format, audience and communicative purpose; concrete observations remain linked to original passages.

A twin should select relevant knowledge and cases for the current situation and use compatible expression examples. Summaries and profiles support this process; they should not replace the source material. Public content does not establish unobserved private behavior, and narrated expertise is not the same evidence as a recorded interaction.

## Primary papers and what transfers

### 1. LongMemEval — memory granularity and information loss

**Source:** Di Wu et al., *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. [Paper, inspected v2](https://arxiv.org/html/2410.10813v2), especially §§3–5 and §5.2–5.5.

**What was studied:** Memory over long, multi-session user–assistant histories, using 500 curated questions. The dataset includes LLM-simulated and human-edited sessions, plus other conversation data; it is not a study of cloning real trainers from public posts.

**Important findings:**

- Evaluates information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention.
- With GPT-4o, decomposing sessions into conversation rounds improved reading/QA performance. The advantage was not uniform across reader models.
- Replacing sessions/rounds with extracted summaries or facts generally hurt QA due to information loss. Fact decomposition did help multi-session reasoning.
- Extracted facts helped when used to expand retrieval keys, while preserving richer values.
- Retrieval and reading are separate bottlenecks: finding the right material does not guarantee using it correctly.
- The paper's QA judge was checked against human experts; it was not simply assigned a generic quality rubric and assumed reliable.

**TrainerTwin implication:** Use cards/facts as indexes and views, but keep complete explanatory passages and coherent exchanges as retrievable evidence. Check whether important source information remains answerable after ingestion and synthesis. Do not equate a high quoted-unit count with information recall.

### 2. RoleLLM — knowledge and speaking style are different targets

**Source:** Zekun Moore Wang et al., *RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models*. [Paper, inspected v3](https://arxiv.org/html/2310.00746v3), especially §§2–4.

**What was studied:** 100 predominantly fictional/script-derived roles, role profiles, structured dialogues, generated role-specific QA, and role-conditioned instruction tuning. Much of RoleBench is model-generated. It is not evidence that an ordinary person's public posts suffice for an authentic twin.

**Important findings:**

- Separates role-specific knowledge/episodic memories from speaking-style imitation.
- Uses Context-Instruct to create context-grounded questions and answers, and RoleGPT with dialogue demonstrations for style.
- Uses relevant dialogue examples rather than relying exclusively on trait adjectives.
- Results depend on training and conditioning regime: system-instruction customization outperformed retrieval augmentation in their fine-tuned role-customization experiments. This does **not** establish that retrieval always wins or that every trainer needs fine-tuning.

**TrainerTwin implication:** Preserve distinct knowledge and expression representations. A fluent stylistic response must not compensate for wrong knowledge. Synthetic QA or demonstrations can be training/evaluation aids, but never become evidence that the real person said or did something.

### 3. LaMP — personalize for the current task, not through a universal profile dump

**Source:** Alireza Salemi et al., *LaMP: When Large Language Models Meet Personalization*. [Paper, inspected v4](https://arxiv.org/html/2304.11406v4); [ACL publication](https://aclanthology.org/2024.acl-long.398/), especially §§2–4.

**What was studied:** Seven personalized classification/generation tasks, including titles, email subjects, and tweet paraphrasing. User profiles are historical user data. This is task personalization, not proof of full-person conversational replication.

**Important findings:**

- Relevant historical items can improve personalized outputs without a separately fine-tuned model for every person.
- Relevance and recency matter; there was no universally best retriever across tasks.
- Uses both user-disjoint and time-based splits, separating past profile material from later target outputs.
- Text-generation metrics include ROUGE; success on these metrics is not sufficient evidence of trainer likeness or pedagogy.

**TrainerTwin implication:** Condition the twin on the current request, relevant methods/cases, and matching expression examples. A public promotional post should not dictate every live coaching reply. Use time-held-out material for checks where appropriate; avoid using the target answer as profile evidence.

### 4. Generative Agents — preserve observations beneath derived reflections

**Source:** Joon Sung Park et al., *Generative Agents: Interactive Simulacra of Human Behavior*. [Paper, inspected v2](https://arxiv.org/html/2304.03442v2), especially §§4 and 6–8.

**What was studied:** Twenty-five simulated characters in a game-like environment. The main target is believable behavior, not matching a particular real person's ground-truth behavior.

**Important findings:**

- A memory stream, retrieval, reflection and planning support behavior in context.
- Ablations show contributions from architectural components within this simulation.
- Failures include missed memories, fabricated embellishments and overly formal model behavior.

**TrainerTwin implication:** Derived patterns should remain connected to underlying observations. Unlike a fictional simulation, TrainerTwin must not feed its own inferred reflections back as newly verified facts about a real trainer. Believability and fidelity need different acceptance criteria.

### 5. Real-person generative agents — depth of evidence matters, but results are task-specific

**Source:** Joon Sung Park et al., *LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals*; originally circulated as *Generative Agent Simulations of 1,000 People*. [Abstract/version history](https://arxiv.org/abs/2411.10109); [inspected v3 PDF](https://arxiv.org/pdf/2411.10109v3), main text pp. 1–12. v3 is dated June 2026.

**What was studied:** 1,052 U.S. participants, roughly two-hour semi-structured interviews, surveys, or both. Prediction tasks were separated from their input data. Agents used full self-report material plus model-generated expert reflections.

**Important findings and caveats:**

- On held-out GSS items, interview-only agents reached 83% of participants' own two-week test–retest consistency; combined interview/survey agents reached 86%, versus 74% for demographic-only agents.
- These are **normalized task accuracies**, not “83–86% of a human being replicated.” Interview-only raw GSS accuracy was about 65.67%.
- Brief persona descriptions were weaker than richer self-report grounding in the tested tasks.
- The latest version explicitly reports no significant differences between agent types on the incentivized economic games. Richer evidence did not establish a universal behavioral advantage.
- A summary ablation retained much of GSS performance (normalized 0.81 vs 0.83), but was lower on Big Five correlation. This reinforces that appropriate compression depends on the downstream task; it is not a blanket ban on summarization.
- This study does not establish conversational style fidelity from social-media posts alone.

**TrainerTwin implication:** If the trainer is available, targeted first-person explanations of choices, exceptions and important cases may fill gaps that more promotional content cannot. A two-hour interview is not a required recipe for our product; its value and scope must be tested. Do not infer hidden motives or broad personality claims from insufficient evidence.

### 6. TwinVoice — social expression, interpersonal response and fictional role-play are not interchangeable

**Source:** Bangde Du et al., *TwinVoice: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation*. [Paper, inspected v2](https://arxiv.org/html/2510.25536v2), especially §§3–5 and limitations.

**What was studied:** Social persona using microblog histories, interpersonal persona using Telegram-derived histories, and narrative persona using fictional materials. The paper's interpersonal label should not be read as evidence that every input was a consented private one-to-one coaching exchange.

**Important findings:**

- Distinguishes opinion consistency, memory recall, logical reasoning, lexical fidelity, persona tone, and syntactic style.
- Evaluates responding to a stimulus given historical evidence, with both multiple-choice and generative protocols.
- Narrative-role results do not directly transfer to social/interpersonal fidelity.
- Judge outputs are compared with human annotations on a limited sample; the paper notes remaining gaps and dataset constraints.

**TrainerTwin implication:** Public writing, recorded Q&A and narrated role-play should remain separate evidence classes. Evaluate content, style and interaction separately. Better lexical imitation should not hide poor memory or unsupported decisions. The benchmark motivates testing distinctions, not installing six additional agent subsystems.

### 7. InCharacter — evaluate enacted responses, but do not overclaim psychometrics

**Source:** Xintao Wang et al., *InCharacter: Evaluating Personality Fidelity in Role-Playing Agents through Psychological Interviews*. [Paper, inspected v4](https://arxiv.org/html/2310.17976v4); [ACL publication](https://aclanthology.org/2024.acl-long.102/), especially §§3–5.

**What was studied:** Mainly fictional characters, with personality labels from human perceptions and familiar annotators. Uses 14 scales and interview-style questions. These labels are not ground truth about a living trainer's private psychology.

**Important findings:**

- What a model says about its traits in a questionnaire may differ from how it responds.
- Interview-style assessment exposes behavior beyond knowledge/catchphrase imitation.
- The evaluator itself was compared with human judgments; scale results are not automatically trustworthy.

**TrainerTwin implication:** Eventually evaluate the twin in situations, not just inspect its generated profile or ask it whether it is empathetic. Borrow the idea of behavioral probes, not automatic Big Five/MBTI profiling of a trainer from public posts.

### 8. FActScore — support checks must be atomic, and precision is not coverage

**Source:** Sewon Min et al., *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation*. [ACL publication](https://aclanthology.org/2023.emnlp-main.741/); [PDF](https://aclanthology.org/2023.emnlp-main.741.pdf), especially §§3–4 and limitations.

**What was studied:** Generated biographies, principally checked against Wikipedia. The reported low estimator error concerns aggregate score estimation in the studied setup, not a universal guarantee of 98% per-claim correctness.

**Important findings:**

- A single sentence can mix supported and unsupported propositions, making holistic judgments too coarse.
- Decompose a generation into atomic claims and assess support against the chosen source.
- Presence of citations does not by itself establish factual support.
- The paper explicitly measures precision, not recall; an output can become safer by saying less while losing important information.
- Nuanced, conflicting or subjective source material requires care beyond the paper's simplifying assumptions.

**TrainerTwin implication:** Validate each substantive wiki/persona assertion against the correct original context, and separately test whether essential source information survived. Public self-reports should be represented as self-reports, not converted into externally verified truth. Unsupported embellishments such as “theoretically sound” must not pass merely because a related quote exists.

### 9. Bridge — a trainer's expertise includes what they notice, choose and intend

**Source:** Rose E. Wang et al., *Bridging the Novice-Expert Gap via Models of Decision-Making: A Case Study on Remediating Math Mistakes*. [Paper, inspected v3](https://arxiv.org/html/2310.10648v3); [NAACL publication](https://aclanthology.org/2024.naacl-long.120/), especially §§3–6.

**What was studied:** 700 real math-tutoring conversation examples and expert annotations. Four experienced teachers helped develop/validate the framework through cognitive task analysis. This was not automatic reconstruction of a named person's mind from scraped writing.

**Important findings:**

- Experts explicitly identify a learner's error, choose a strategy, and state an intention before producing a response.
- Context-sensitive expert/self-generated decisions improved some model responses in human evaluation; inappropriate/random decisions hurt performance.
- Experts used more diverse decision paths than models. A fixed “always ask a question” rule is not a substitute for situated expertise.
- The framework was checked on new tutoring conversations, with expert judgments rather than self-assigned model quality scores alone.

**TrainerTwin implication:** Build a case library, not only a list of traits or tips. A useful case can preserve situation/cue → stated diagnosis → strategy → stated rationale → response → reported/observed outcome. Only fill fields supported by the material; unknown rationale stays unknown. A trainer can clarify high-value gaps through case walkthroughs.

### 10. Tutor CoPilot — useful training behavior is a separate outcome from sounding like a person

**Source:** Rose E. Wang et al., *Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise*. [Paper, inspected v2](https://arxiv.org/html/2410.03017v2), especially §§3–6.

**What was studied:** A human-in-the-loop tutoring tool informed by Bridge, evaluated in a preregistered mathematics tutoring trial. Tutors selected/edited suggestions; it was not an autonomous clone of one named tutor.

**Important findings:**

- Guidance uses live conversation context, lesson topic and selected pedagogical strategy.
- The trial reported improved topic mastery (4 percentage points overall in its setting), while users still found inappropriate grade-level suggestions and other limits.
- Human selection of strategies matters; generating plausible tutor language alone is insufficient.

**TrainerTwin implication:** A twin needs to be useful at training as well as recognizable. Eventually evaluate whether its questions, explanations and feedback help the learner. Do not transfer the study's learning gains to our system or assume public persona imitation will produce them.

## Proposed information design for TrainerTwin (our synthesis, not a proved optimal architecture)

```text
Public content + optional trainer-reviewed case walkthroughs
                    |
                    v
Source foundation
  Original context, provenance, attribution, publication time,
  format, audience/purpose where known, repeated-content relationships
                    |
        +-----------+-------------+
        |           |             |
        v           v             v
Knowledge       Teaching /      Expression
and methods     interaction     examples
                cases
        |           |             |
        +-----------+-------------+
                    |
                    v
Person wiki / queryable memory / explicit unknowns
                    |
                    v
Current learner situation
  -> retrieve relevant knowledge and cases
  -> choose a context-appropriate response approach
  -> express it with compatible original examples
                    |
                    v
Check source support, practical usefulness and resemblance separately
```

The three products can be ordinary structured files with linked original passages. Research does not require a graph database, three autonomous agents, latent personality vectors, fine-tuning, or a particular vector store. Those are implementation options to justify with evidence later.

### Example: preserving a teaching exercise

A wiki entry should retain the objective, materials, exact time constraint, ordered steps,
expected task/output and any source-stated exceptions. “Uses creative exercises” is a topic
summary, not a usable method. A separate expression observation can describe short imperative
steps and repeated constraints. A runtime adaptation is then a labeled proposal, not an
assertion that the trainer always speaks that way.

### Example: preserving a narrated client exchange

Record that the trainer **published a narration** of a client/coaching exchange. Keep the
reported speakers and preceding objection together. Extract the strategy and any stated
rationale without adding proof of effectiveness. Separately observe how the writing uses
contrast, analogy, dialogue and takeaway. A narrated exchange must not masquerade as a
recorded live interaction in the case library or evaluation ground truth.

## How to evaluate pipeline output without repeating the failed loop

Do not collapse these into a single generic score during diagnosis:

1. **Source support:** Are individual assertions supported in their original context? Is attribution correct? Are model inferences visibly distinct from source statements?
2. **Information retention:** Can a reader/model answer source-grounded questions about steps, constraints, exceptions and cases from the processed outputs? Which important answers disappeared?
3. **Case/decision fidelity:** When actual interactions exist, do held-out responses reflect the documented context-sensitive method? Do not invent hidden rationales or assume a unique correct response where none is established.
4. **Expression fidelity:** Does a response retain observable form, tone and language choices without distorting meaning? Use original examples and human familiarity, not catchphrase frequency alone.
5. **Usefulness:** Does the output help the target learner/task? Initially use trainer/expert review; genuine learning-outcome claims require a different, later study.
6. **Memory integrity:** Test updates, temporal scope, conflicting statements and abstention. An old statement should not automatically override a newer one, and missing evidence should not become invented certainty.

A small reference set should be reviewed against originals before it becomes an optimization
target. Keep development and final checks separate by source/conversation (and time where
appropriate), validate any judge against human decisions, and report the dimensions
separately. The unchanged layers in a large packet can otherwise swamp a meaningful change
in one layer, as our previous paired scoring appeared to do.

## Practical next research-to-build step

Before another prompt loop, inspect a small cross-format source sample and define the
information each source genuinely supports: knowledge/procedure, narrated case, recorded
interaction, and written/spoken expression. Produce a few human-reviewed target records and
answerability questions from those sources. Compare the pipeline with those records, then
fix the earliest transformation losing or distorting the information.

If recorded interactions or trainer explanations are unavailable, label those capabilities
as unknown. We can still build a useful public-knowledge and expression twin, but should not
claim that we have validated how the person privately reasons or would behave in every novel
conversation.

## What this research does not establish

- A Pareto-optimal universal architecture for TrainerTwin.
- That public posts alone suffice to reconstruct an authentic live conversational partner.
- That a large, polished wiki is adequate conditioning for all downstream tasks.
- That fine-tuning is always necessary, always harmful, or categorically worse than retrieval.
- That personality scales or model-generated motives identify a real person's psychology.
- That an LLM judge's numerical improvement means information quality improved.
- That synthetic conversations count as new evidence about the trainer.
