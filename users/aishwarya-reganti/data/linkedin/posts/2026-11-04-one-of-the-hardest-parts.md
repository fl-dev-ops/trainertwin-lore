---
id: '7523776348595871744'
date: '2026-11-04T16:01:06.510Z'
url: https://www.linkedin.com/posts/areganti_one-of-the-hardest-parts-of-building-self-improving-activity-7523776348595871744-Oi2O
likes: 18
comments: 2
images_count: 1
---

One of the hardest parts of building self-improving agents is knowing which failures to fix and which ones are just noise.

SPAR, a new paper from Alibaba, explores this in multi-session B2B sales. It treats strategies as testable hypotheses and improves them through two learning loops, without updating model weights.

A few details from the paper:

- The inner loop maintains merchant-specific episodic memory: previous interactions, outcomes and what to try next. The outer loop evolves a shared strategy playbook across merchants.

- Each strategy has preconditions, action steps, rationale and supporting evidence. Selection considers the merchant’s context, previous outcomes and exploration priority.

- Before updating the playbook, an LLM labels outcomes as strategy-driven, external or uncertain. Only strategy-attributed evidence updates confidence. A rejection caused by a budget cut, for example, gets recorded without counting against the strategy.

- Confidence uses a Beta-Bernoulli estimate, so limited evidence doesn’t immediately produce high confidence. Evidence thresholds govern when tentative strategies become active or failing ones get deprecated. Updates can revise preconditions, add strategies or merge overlapping ones.

The authors report a 15.8% relative conversion lift over direct prompting in a live A/B test across 200,000+ merchants on Alibaba’s 1688 platform. Attribution still relies on LLM judgment, so errors in that judgment can feed into subsequent updates.

Paper: https://lnkd.in/gRVd3xza
