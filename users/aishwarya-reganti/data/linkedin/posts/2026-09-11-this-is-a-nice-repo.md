---
id: '7504003305715576833'
date: '2026-09-11T02:30:05.722Z'
url: https://www.linkedin.com/posts/areganti_this-is-a-nice-repo-desktop-app-that-automates-activity-7504003305715576833-runx
likes: 210
comments: 5
images_count: 1
---

This is a nice repo + desktop app that automates building and updating an LLM wiki from your sources.

Feed it PDFs, articles, notes, etc., and it builds linked pages around the concepts and entities in those sources.

Some nice highlights:

- When a new document comes in, it finds connections to existing wiki content and creates or updates the relevant pages. It can also flag contradictions for human review.
- Each generated page links back to its original sources. There’s even a mode for answering questions using only the source documents.
- A `purpose.md` file defines what the wiki is for and the questions it should help answer. The agent reads this when adding information and answering questions.
- It watches source folders for changes and skips unchanged files, so it doesn’t keep processing the same material.
- It includes an MCP server, so Claude Code, Codex and other compatible agents can search the wiki and read its files.
- Everything is stored as Markdown, and the wiki folder also works as an Obsidian vault. People and agents can work with the same knowledge.

Repo: https://lnkd.in/gAC4GYmy
