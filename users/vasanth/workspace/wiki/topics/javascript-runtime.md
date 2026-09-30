# javascript runtime

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-caa96ed3d58cff69"></a>
## Concurrency vs. Parallelism in JavaScript

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript executes operations concurrently, not in parallel, due to its single-threaded nature. IO and memory-intensive operations can occur concurrently.
  - “On contrary, JavaScript executes thing in a uh there are two things. It's not parallel. It executes things in a concurrent way.” — [lines 1014-1014](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000227`)
  - “There are two differences, okay? Parallel and concurrent are different. Parallel means in Java you can spin up four threads to do four independent tasks at given point in time.” — [lines 1018-1018](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000228`)

### Original context

**vasanth** · lines 1014-1014 · spoken_turn

> On contrary, JavaScript executes thing in a uh there are two things. It's not parallel. It executes things in a concurrent way. There are two differences, okay? Parallel and concurrent are different. Parallel means in Java you can spin up four threads to do four independent tasks at given point in time. In JavaScript you cannot do that. There is only one thread. So as it's only one thread, you can do certain things concurrently. Concurrently means there'll be IO intensive operation and memory intensive operation. What do I mean by that is, IO means

**vasanth** · lines 1018-1018 · spoken_turn

> put output and uh memory intensive means IO means like basically you are asking CPU to do something let's say you want to do one plus two then you are asking CPU to add that and give back the result. Then there will be memory intensive operation let's say you want to set something into local storage. That is the time where you are adding a value into your storage it's not a CPU intensive operation. So these things can be parallelized or you can say it's a concurrent both things can happen memory uh IO intensive and memory intensive can happen in parallel but two things cannot be executed in parallel. Please remember this. तो जाबास्क्रिप्ट एग्जीक्यूट थिंग्स कॉनकरेंटली, कॉनकरेंटली नॉट इन पैरेलल वे। ओके। नेक्स्ट,

**vasanth** · lines 1022-1022 · spoken_turn

> I think I explained why call stack is stack and about the queues, why queues are designed such a way. And event loop whenever it is asked in the interview, you can explain event loop as an algorithm also and event loop as a process as well, how overall it's going to do. Now comes a very important question, okay? If you look at this example, I have the example. So now, I explained like JavaScript engine has call stack and queues and everything, right? Now, does the set time out really gets into call stack or no? In the first

<a id="record-02f1232c2d410a79"></a>
## JavaScript Execution Model

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript executes code sequentially because it operates on a single thread, meaning parallel processing cannot occur.
  - “See JavaScript executes code, there is no code in JavaScript can be executed in parallel.” — [lines 1010-1010](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000226`)
  - “parallel processing cannot happen in JavaScript, the reason being there is only one thread that executes everything.” — [lines 1010-1010](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000226`)

### Original context

**vasanth** · lines 1010-1010 · spoken_turn

> See JavaScript executes code, there is no code in JavaScript can be executed in parallel. Okay, parallel processing cannot happen in JavaScript, the reason being there is only one thread that executes everything. Okay. So it is only sequential execution.

**vasanth** · lines 1014-1014 · spoken_turn

> On contrary, JavaScript executes thing in a uh there are two things. It's not parallel. It executes things in a concurrent way. There are two differences, okay? Parallel and concurrent are different. Parallel means in Java you can spin up four threads to do four independent tasks at given point in time. In JavaScript you cannot do that. There is only one thread. So as it's only one thread, you can do certain things concurrently. Concurrently means there'll be IO intensive operation and memory intensive operation. What do I mean by that is, IO means

**vasanth** · lines 1018-1018 · spoken_turn

> put output and uh memory intensive means IO means like basically you are asking CPU to do something let's say you want to do one plus two then you are asking CPU to add that and give back the result. Then there will be memory intensive operation let's say you want to set something into local storage. That is the time where you are adding a value into your storage it's not a CPU intensive operation. So these things can be parallelized or you can say it's a concurrent both things can happen memory uh IO intensive and memory intensive can happen in parallel but two things cannot be executed in parallel. Please remember this. तो जाबास्क्रिप्ट एग्जीक्यूट थिंग्स कॉनकरेंटली, कॉनकरेंटली नॉट इन पैरेलल वे। ओके। नेक्स्ट,

<a id="record-3f55c33b33aaa98f"></a>
## Distinction between Parallel and Concurrent Execution

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker contrasts parallel and concurrent execution, noting that Java can execute multiple tasks in parallel due to multiple threads, while JavaScript handles tasks concurrently on a single thread.
  - “Parallel means in Java you can spin up four threads to do four independent tasks at given point in time. In JavaScript you cannot do that.” — [lines 1014-1014](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000227`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1014-1014 · spoken_turn

> On contrary, JavaScript executes thing in a uh there are two things. It's not parallel. It executes things in a concurrent way. There are two differences, okay? Parallel and concurrent are different. Parallel means in Java you can spin up four threads to do four independent tasks at given point in time. In JavaScript you cannot do that. There is only one thread. So as it's only one thread, you can do certain things concurrently. Concurrently means there'll be IO intensive operation and memory intensive operation. What do I mean by that is, IO means
