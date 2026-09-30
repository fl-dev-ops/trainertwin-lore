# javascript call stack and api queue

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-ae6b6c3113a041d9"></a>
## Set Timeout Mechanism in JavaScript

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Set timeout in JavaScript is initially placed in the call stack before being handed off to the web APIs, which handle timing.
  - “Whether it is set term out, whether it is a promise, whether it is any other web APIs, all of them come to call stack and JS engine gets to know this is something that I cannot handle.” — [lines 1030-1030](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000231`)
  - “then it will offload that thing to the web APIs. Okay? And web APIs eventually come into the queues and they come back to the stack and get executed.” — [lines 1034-1034](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000232`)

### Original context

**vasanth** · lines 1026-1026 · spoken_turn

> phase, first place, okay? Whenever the execution starts, will the setup mode comes to call stack or it will directly go to the queues? So, as consider like JavaScript engine is the place for executing everything.

**vasanth** · lines 1030-1030 · spoken_turn

> So any line that need to get executed will always come to call stack first. Whether it is set term out, whether it is a promise, whether it is any other web APIs, all of them come to call stack and JS engine gets to know this is something that I cannot handle.

**vasanth** · lines 1034-1034 · spoken_turn

> then it will offload that thing to the web APIs. Okay? And web APIs eventually come into the queues and they come back to the stack and get executed. Okay? Please remember that. So many people don't know like set timeout is directly going to the web APIs, no. Everything comes to call stack. The main thread determines whether can it execute it here or not. If not, it will move to the web APIs and from the queue point of view it comes to the stack. Another very very important, the JavaScript engine only owns the JavaScript here. The engine only has the heap and call stack. So anything in the call stack
