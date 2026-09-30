# memory usage

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-e59e962154945a0d"></a>
## Shallow and Deep Copy in JavaScript

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, array and object copies are shallow, while primitive types like numbers and strings are deep copies.
  - “Just if I have to digress and explain if you see the deep copy and shallow copy in JavaScript the variables created all the array and object types are actually shallow copy whereas the primitive types like number, string are deep copied.” — [lines 1110-1110](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000251`)

### Original context

**vasanth** · lines 1106-1106 · spoken_turn

> So if you are getting that much of memory then it is reserved for you then you will be able to execute it. But probably the language like Java etcetera they directly interact with hardware. They have a higher chance of getting more memory compared to the browser. So JavaScript in general is always competing for more and more memory. That's the reason why first is a memory creation phase. Just if I have to digress and explain if you see the deep copy and shallow copy in JavaScript the variables created all the array and object types are actually shallow copy whereas the primitive types like number, string are deep

**vasanth** · lines 1110-1110 · spoken_turn

> copied. Same reason why they are also shallow copied like array and object expected to be like larger in terms of size. If they keep creating a newer instances or if they keep making if a JavaScript makes a deeper copy of it it end up have consuming more memory. So unless you manually specify JavaScript engine to like make it a deep copy naturally they are all shallow copied. Okay? And if you look at the simple example variable a is equal to ten function foo foo and function test so you are calling the test test will get executed.
