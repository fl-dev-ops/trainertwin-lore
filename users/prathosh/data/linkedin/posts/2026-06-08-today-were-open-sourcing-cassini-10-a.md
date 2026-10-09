---
id: '7469611110539907072'
date: '2026-06-08T04:47:47.416Z'
url: https://www.linkedin.com/posts/aravind-jayendran_opensource-slm-codeintelligence-activity-7469609087719092225-gX1B
likes: 211
comments: 12
images_count: 1
---

Today we're open-sourcing Cassini-1.0.

A 4B-parameter SLM that matches the F1 of the best general-purpose models on structured code extraction, at ~18× the cost-efficiency. Apache 2.0. Live on Hugging Face right now.

Why we built it:

LatentGraph (our persistent context graph for AI coding agents) starts with running a feature extractor on every code file in your repo: imports, definitions, references, calls, type assignments. That metadata is how we resolve cross-file dependencies, build call graphs, and surface the implicit couplings static analysis misses entirely.

This LLM-based approach beat the AST-based dependency analyzers we benchmarked against, and was dramatically easier to extend to new languages.

One problem: running it on frontier models was economically catastrophic. Indexing a serious codebase ran into hundreds of dollars per repo. The math doesn't work for a product engineers should actually want to use.

So at LatentForce, we built a specialized data pipeline, collected a large training corpus, and fine-tuned our own 4B base model. The result lands on the Pareto frontier of every model we tested. 77.6% F1, matching Qwen3.7-Max at 1/18th the inference cost ($0.17 vs $3.03). Up to 43× cheaper than the closest commercial alternatives. Significantly faster runtime. Python, JavaScript, TypeScript today, more languages soon.

Specialized small models for narrow developer tasks are one of the most important shifts coming to dev tooling. If you're building anything that needs cheap, fast, structured code understanding at scale, take it, fork it, extend it.

Link: https://lnkd.in/gszfGMr2

The frontier isn't bigger models. It's specialized ones.

#OpenSource #SLM #CodeIntelligence #EngineeringBrain #LatentForce #CompanyBrain
