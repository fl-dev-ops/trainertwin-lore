# memory management

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-cddb7a5bbea2dd55"></a>
## Memory Heap in JavaScript

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The memory heap is used for dynamic memory allocation in the JavaScript engine and is a region in the RAM.
  - “So JavaScript heap is a region in the RAM used by the JavaScript engine for dynamic memory allocation.” — [lines 442-442](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000084`)

### Original context

**vasanth** · lines 430-430 · spoken_turn

> contains, it primarily contains two two things, memory heap and a call stack. Okay. So what is a memory heap? You could consider like it stores variable objects and function. You can look at this diagram, okay. So JavaScript engine primarily contains two things, memory heap, memory heap and a call stack. So if you look at this diagram, heap is a place where actually things are getting stored, a memory location. So it is very hard to say where exactly JavaScript stores the things because unlike Java or C++ C++ C#, the

**vasanth** · lines 434-434 · spoken_turn

> and which do not directly interact with the hardware. So JavaScript consider assuming let's assume like on the browser sort of a where we are running JavaScript. So JavaScript primarily interacts with the browser. Browser internally interacts with the hardware, correct? So but it is very safe to say primarily most of this heap memory or the memory heap is from the RAM memory itself, whatever the RAM memory that we have. So the variables are actually stored in the RAM and stack is going to have a reference to it. The call stack is going to have a reference to it. I'll repeat. So JavaScript engine, they are very popular in this.

**vasanth** · lines 438-438 · spoken_turn

> V8, Safari, Chakra, etcetera. It contains primarily two parts, memory heap and a call stack. Memory heap is where variables, function, objects are actually stored. Call stack execute JavaScript code, follows last in first out order. Only one piece of code executes at a time. Please remember that, okay? Because single threaded, we cannot do more than one at a time, correct? So only one piece of code executed at a time, okay? So, I'll give a pause probably after I explain few more because the doubts that you might get, I might cover in next five to ten minutes, okay?

**vasanth** · lines 442-442 · spoken_turn

> after I finish the JavaScript runtime encounter fully, I'll give a pause and we can spend like five to ten minutes discussing the questions. Okay? So JavaScript heap is a region in the RAM used by the JavaScript engine for dynamic memory allocation. Objects, arrays, functions, closures are typically stored there, while variables on the stack usually hold a reference to the those objects on the heap. Okay? I'll make a slight digressing while while I'm explaining this, right? Many people think, um whenever that many people think whenever they're basically calling a function and passing an
