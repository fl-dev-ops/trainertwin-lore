---
id: '7480636840216109057'
date: '2026-07-08T15:00:06.219Z'
url: https://www.linkedin.com/posts/areganti_memory-might-have-to-be-treated-as-a-first-activity-7480636840216109057-pFSj
likes: 143
comments: 5
images_count: 1
---

Memory might have to be treated as a first class citizen if we’re going to build always-on agents according to this paper.

The paper argues that always on agents shouldn’t be treated as normal agents with memory bolted on. They’re persistent state systems, because past interactions can directly shape future behavior and actions.

Some highlights I liked:

1. The authors widen the definition of state beyond memory. State includes task ledgers, permissions, credentials, commitments, provenance, audit records, trigger conditions, shared state, and external effects.

2. They propose six axes for thinking about any state item: authority, scope, mutability, provenance, recoverability, and actionability.

3. They frame agent state as a lifecycle: observe, write, validate, organize, retrieve, act, update, forget, audit, rollback. The field is strong on the first half and much weaker on the second half.

4. Larger context windows and better retrieval don’t solve the core problem. They help the agent read more, but they don’t answer what should persist, what’s authoritative, what should change, or what a user can revoke.

5. Ungoverned memory can become worse than no memory over long horizons. The paper cites studies where memory systems degrade below a no memory baseline as stored state accumulates.

Overall, I thought this was a very nice paper with a lot of useful frameworks.

That said, given how much emphasis there is on cost right now, I’m not fully sure how quickly always on agents become a total reality. A lot of companies are trying to reduce token usage, not max it out with persistent agents running all the time.

For now, it's a nice futuristic paper: https://lnkd.in/dce6tw9B
