# react and javascript

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-5027f037f5cb8c2f"></a>
## React and local storage usage

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Using 'await' with local storage operations in React is incorrect because they are synchronous.
  - “Considering the local storage is sync in nature... though knowing local storage is like actually sync in nature, still use await in React. Is it right or wrong?” — [lines 542-542](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000109`)
  - “even though it is a web API, it's not a synchronous, asynchronous, right? So we don't need to await that.” — [lines 558-558](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000113`)

### Original context

**vasanth** · lines 542-542 · spoken_turn

> Considering the local storage is sync in nature. Many people in React, I don't know how many of you checked your code basis correctly, do this actually. Await local storage set item, await local storage get item. Is it right in React or wrong? I'll repeat the question. Many people

**vasanth** · lines 546-546 · spoken_turn

> Whenever they are writing a React code, though knowing local storage is like actually sync in nature, still use await in React. Is it right or wrong? If anyone knows the answer, please raise your hand.

**vasanth** · lines 550-550 · spoken_turn

> not correct. Sada Hamma says it is not correct. Anyone wants to answer you can raise your hand. Maybe one or two of you can answer. Anybody wants to answer?

**vasanth** · lines 554-554 · spoken_turn

> क्या साधा मत प्लीज गॉट

**unknown speaker** · lines 558-558 · spoken_turn

> Yeah, what from what I know, Vasant, is that even though it is a web API, it's not a synchronous, asynchronous, right? So we don't need to await that.

<a id="record-a070ad922474988b"></a>
## React local storage sync discussion

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A discussion occurred in a JavaScript session about whether using 'await' with local storage in React is correct due to local storage being synchronous.
  - “Whenever they are writing a React code, though knowing local storage is like actually sync in nature, still use await in React.” — [lines 542-542](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000109`)

### Cue

- Speaker asks if using 'await' with local storage in React is correct or wrong.
  - “Is it right in React or wrong?” — [lines 542-542](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000109`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- A participant correctly points out that it is not necessary to await local storage actions because they are synchronous.
  - “we don't need to await that.” — [lines 558-558](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000113`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 542-542 · spoken_turn

> Considering the local storage is sync in nature. Many people in React, I don't know how many of you checked your code basis correctly, do this actually. Await local storage set item, await local storage get item. Is it right in React or wrong? I'll repeat the question. Many people

**vasanth** · lines 546-546 · spoken_turn

> Whenever they are writing a React code, though knowing local storage is like actually sync in nature, still use await in React. Is it right or wrong? If anyone knows the answer, please raise your hand.

**vasanth** · lines 550-550 · spoken_turn

> not correct. Sada Hamma says it is not correct. Anyone wants to answer you can raise your hand. Maybe one or two of you can answer. Anybody wants to answer?

**vasanth** · lines 554-554 · spoken_turn

> क्या साधा मत प्लीज गॉट

**unknown speaker** · lines 558-558 · spoken_turn

> Yeah, what from what I know, Vasant, is that even though it is a web API, it's not a synchronous, asynchronous, right? So we don't need to await that.

**vasanth** · lines 562-562 · spoken_turn

> correct
