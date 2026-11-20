---
id: '7506728855638810625'
date: '2026-09-18T15:00:27.462Z'
url: https://www.linkedin.com/posts/areganti_headroom-is-an-open-source-repository-activity-7506728855638810625-HLdC
likes: 72
comments: 3
images_count: 1
---

😱 Headroom is an open-source repository that can reduce input tokens to your agent by up to 95%!

It compresses logs, files and tool outputs locally before they go to the model, using different compressors for JSON, source code and text. This is aimed at longer agent sessions where tool calls keep adding large amounts of context.

Details:
- They report 60–95% savings on JSON inputs and around 20% for coding agents.
- It caches the original tool output locally. The model gets a retrieval tool, so it can request the full content when the compressed version doesn't have enough detail. You can configure how long the originals stay in the cache.
- You can run it with Claude Code or Codex, use its Python or TypeScript library in your own application, or connect through MCP.
- It includes a dashboard for tracking token savings, so you can see what compression does on your own workload.

The repo also walks through how the compression pipeline works, including how it selects a compressor and retrieves the original content. Useful to study if you're building this into your own agent.

Link: https://lnkd.in/g3XHQFvW
