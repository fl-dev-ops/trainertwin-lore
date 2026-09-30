# programming tip

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-4270dd9ccfe942c3"></a>
## Object Reference Tip

**Product:** knowledge · **Type:** advice · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- When calling a function with an object, only the reference is passed, not the entire object, making it efficient to pass large objects to functions for transformation.
  - “We have a feeling right ... taking more processing. But that is not the case.” — [lines 446-446](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000085`)
  - “exclusively like you can pass any bigger objects to a utility get the transformation done and get it back.” — [lines 450-450](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000086`)

### Original context

**vasanth** · lines 446-446 · spoken_turn

> object to that function and that function may be processing that object or passing to another function. We have a feeling right let's say that's a very bulky object. If we send it to a function and it transforms it and sends it back. Many times during the PR reviews and other times I've seen like let us not send this heavy object to that function because it might be like um like taking more processing. But that is not the case. So this is a tip to all the senior developers out here. Whenever we are calling a function passing a argument etcetera we are just passing the references not the

**vasanth** · lines 450-450 · spoken_turn

> table itself in physicality we are not sending anything to function okay so even if you want to transform a large object within a utility function and get it back all you are doing is just passing a reference to that utility and getting these things done okay so in your programming you can use it exclusively like you can pass any bigger objects to a utility get the transformation done and get it back so you don't have to shy away from doing that okay maybe in though I wanted to give a pause later but so far whatever I explained anybody has any doubts you can raise your hand
