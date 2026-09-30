# javascript storage

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-8307211946b7ea78"></a>
## Local storage sync nature

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Local storage in JavaScript is synchronous in nature.
  - “So local storage actually sync in nature.” — [lines 526-526](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000105`)

### Original context

**vasanth** · lines 526-526 · spoken_turn

> Okay. So local storage actually sync in nature. Now comes to a question if something is sync. Why it is being offloaded basically? uh Okay, Shivam saying URL. Okay, sure. So if it is

**vasanth** · lines 530-530 · spoken_turn

> synchronous in nature. There are many things actually which are sync in nature, not just the local storage. I'm just taking example of local storage. So if it is sync in nature, why can't JavaScript handle it by itself? Why it's giving that to the web APS? If you think like JavaScript engine in a nutshell is something that is responsible for executing the code, very very simple. So anything beyond execution is is is something that JavaScript engine cannot handle. I'll tell you why. So now local storage is something that where you have to store the variable for a while and like whenever you were trying to execute

**vasanth** · lines 534-534 · spoken_turn

> that need to be kept like unless there is some T T L to expire it will be kept there forever. So all those things JavaScript engine cannot handle. So don't consider web APIs like primary responsible for taking care of the async events. Web APIs are basically used for handling the any activity that is difficult for JavaScript engine to handle all of those are basically ofloaded into web APIs. Okay? So I've written few of the capabilities as an example here. Like example also I've just wrote the set timer. So JavaScript registers a timer browser web APIs

**vasanth** · lines 538-538 · spoken_turn

> handles the timer. JavaScript continues running without waiting. So JavaScript do not worry whenever this timer continues. Okay? So now

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
