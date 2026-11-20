---
id: '7521044303876423680'
date: '2026-10-28T03:04:56.290Z'
url: https://www.linkedin.com/posts/areganti_how-do-you-slash-token-costs-by-up-to-70-activity-7521044303876423680-dcji
likes: 431
comments: 97
images_count: 1
---

How do you slash token costs by up to 70% when building AI products, without having to host models yourself? Ans: Fix your agent harness, and do it well!

A lot of teams focus on model pricing when trying to reduce inference costs. But there's so much optimization you can do at the application layer, without changing models or managing your own inference infrastructure.

Here's a cheat sheet I put together. Think of it as a process:

1. Measure first: Track cost per successful task, not just cost per million tokens. Build an eval set so you can measure whether your optimizations are actually saving money without compromising quality.

2. Reuse and reduce context: Take advantage of prompt caching by keeping stable prefixes consistent. Load tools on demand rather than passing every tool definition, and filter or aggregate tool responses before adding them to context.

3. Build custom compaction: Instead of repeatedly passing entire conversation histories, compact them into structured working states that preserve important facts, decisions, and next actions (this might be different for different applications so don't rely on the model vendor). 

4. Spend selectively: Not every task needs your most expensive model or the highest reasoning effort. Route simpler tasks to smaller models, constrain output lengths, and move nonurgent work into asynchronous workflows. Decision models have made this much easier. 

Before spending weeks evaluating smaller models, fine tuning, or moving to your own inference infrastructure, look at how your agent harness manages context, tools, memory, and execution.
You might find that a lot of your unnecessary spending is happening right there.
