---
id: '7523950265885167618'
date: '2026-11-05T03:32:11.623Z'
url: https://www.linkedin.com/posts/areganti_you-could-be-spending-50-more-on-inference-activity-7523950265885167618-ysqO
likes: 293
comments: 87
images_count: 1
---

You could be spending 50% more on inference costs simply because you're not using prompt caching properly, most model providers already support it. 

...you just need to know how to take advantage of it :)

When you're building AI agents, you're repeatedly sending system prompts, tool definitions, conversation history, and other context to the model. But how you structure your prompts makes a huge difference to how much you actually save.

Here's a cheat sheet I put together. Think of it as a process:
- Structure your prompts for reuse: Keep stable information like system instructions, tool definitions, and reference documents at the beginning. Move frequently changing information toward the end. Even a small change early in your prompt can affect cache reuse for everything that follows.
- Understand what breaks the cache: Reordering tool definitions, adding timestamps to your system prompt, or rewriting conversation history can cause unnecessary cache misses. Keep your prompts consistent and append new turns wherever possible.
- Optimize your agent loops: Agents make multiple model calls to complete a task, so caching can be especially useful here. Preserve your existing context across calls, keep tool schemas consistent, and remember that subagents start their own contexts. Even compaction can sometimes work against caching if you're constantly rewriting the history.
- Understand the economics: Cache writes and reads can have different costs, and the savings depend on how frequently the same context gets reused. Sometimes a longer prompt with good cache reuse can actually be cheaper than a shorter prompt that's processed from scratch every time.
- Measure your savings: Track cached input tokens, effective input cost, latency, and cache reuse across different agent steps. Look at where cache misses happen rather than assuming that enabling caching means you're getting all the benefits.


I've found that a lot of inference optimization comes down to how you manage context in your application.

Before changing models, reducing context windows, or investing in your own inference infrastructure, take a look at how your agent constructs and reuses its prompts.
You might find there's quite a bit of unnecessary spending happening right there.
