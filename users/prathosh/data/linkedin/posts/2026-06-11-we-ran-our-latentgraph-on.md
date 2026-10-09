---
id: '7470835622254059520'
date: '2026-06-11T13:53:33.759Z'
url: https://www.linkedin.com/posts/prathosh-a-p-50ab9511_we-ran-our-latentgraph-on-14-hard-tasks-drawn-activity-7470835622254059520-ILi4
likes: 190
comments: 2
images_count: 1
---

We ran our LatentGraph on 14 hard tasks drawn from the SWE-bench Pro corpus, across two large open-source codebases: protonmail/webclients and ansible/ansible. 

Both repositories average well over a million lines of source code. We deliberately picked hard tasks on large codebases. On small projects, modern agents already have enough room in their context window to solve most things; the differential effect of a graph layer is hard to measure. Hard tasks on million-line codebases are where the navigation cost dominates.

Four coding agents ran the same fourteen tasks twice. Without MCP, the agent was given the prompt and a working tree, nothing else. With LatentGraph, the same agent had the LatentGraph MCP server attached and could query the graph. Same model behind each agent. Same prompt. Same environment. The only variable was whether the agent could query the graph.

Test it out yourself and let us know what you find - https://lgraph.dev/auth
