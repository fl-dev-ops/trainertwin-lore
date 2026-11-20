---
id: '7525950675646599168'
date: '2026-11-10T16:01:06.476Z'
url: https://www.linkedin.com/posts/areganti_who-knew-ai-agents-could-be-2x-slower-just-activity-7525950675646599168-GnLQ
likes: 117
comments: 23
images_count: 1
---

Who knew AI agents could be 2x slower just because they think in English?

Came across a cool paper called Hybrid Reasoning Agents from researchers at Stanford, Together AI and UIUC.

The paper explores whether agents need to write out every intermediate reasoning step. HybridAgent lets them work directly with internal numerical representations, then use text for tool calls and answers.

Some interesting details from the paper:

- They add an adapter called HybridLink that feeds the model’s internal state back in as its next input. This lets it continue reasoning without generating a word at every step.

- The agent keeps both text and latent reasoning across turns, along with tool results. So after calling a tool, it can continue from the work it already did.

- They train this in stages: supervised fine-tuning first teaches the model to work with the adapter, then reinforcement learning helps it learn when to reason in latent space and when to switch to text.

- You can also inspect the latent reasoning. They provide a tool that renders it as readable “pseudo-text” alongside the agent’s tool calls.

In experiments on Qwen3 models from 4B to 14B, the authors report 1.8–2.6x faster inference and roughly 35–55% fewer tokens than their text-based agent baselines.

Paper: https://lnkd.in/gV7mVKKW
Code: https://lnkd.in/ghzfFAZd
