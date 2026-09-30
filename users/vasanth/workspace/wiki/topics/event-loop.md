# event loop

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-4287d06859f403ff"></a>
## Event loop execution order

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Event loop executes all tasks in the call stack first, then proceeds to execute tasks from the micro task queue, one by one, until it's empty, and finally picks one task from the macro task queue and repeats the cycle.
  - “So macro task queue is not emptied at once. So if you look at the order call stack must be empty. Executes all micro tasks. Executes one macro task can repeat the cycle.” — [lines 778-778](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000182`)

### Original context

**vasanth** · lines 698-698 · spoken_turn

> if I understood Hashitha your answer correctly, first, it'll execute everything in the call stack, then it look at a micro task queue, picks one and goes into the call stack, correct?

**unknown speaker** · lines 702-702 · spoken_turn

> Yes

**vasanth** · lines 706-706 · spoken_turn

> And then after that

**unknown speaker** · lines 710-710 · spoken_turn

> after that it execute that

**unknown speaker** · lines 714-714 · spoken_turn

> And then again you have to check for if there is something more it will put it if there is something in the middle you have to take it from the micronase else it will take from the micronase. Okay.

**vasanth** · lines 718-718 · spoken_turn

> Okay. Got it. I get what. I'll I'll repeat, you can correct me if I'm wrong. So everything in the call stack executed first. Once the call stack is empty, the loop will look if there is anything in the micro task queue, it will pick from there. Like it will pick first one and it will go to call stack and execute and it will continuously keep on doing that until there is micro task queue is empty. Am I right Harshita?

**unknown speaker** · lines 722-722 · spoken_turn

> Yes, correct.

**vasanth** · lines 726-726 · spoken_turn

> And then after that what about the macro task queue? How does that work?

**unknown speaker** · lines 730-730 · spoken_turn

> Again micro dots view there would be like uh in the stack order it would be and the first we will put and put it in the stack same way.

**unknown speaker** · lines 734-734 · spoken_turn

> Hello

**vasanth** · lines 738-738 · spoken_turn

> ओके, सी, यू सी बेसिकली बोथ आर एग्जीक्यूटेड इन द सेम वे, बट फर्स्ट प्रायोरिटी इज गिवन टू माइक्रो टास्क क्यू, फॉलोड टू माइक्रो टास्क क्यू, हर्षिता, एम आई राइट? यस, यस।

**unknown speaker** · lines 742-742 · spoken_turn

> Yes, yes.

**vasanth** · lines 746-746 · spoken_turn

> Okay. It is slightly different. Anybody else wants to answer? Maybe Sonu raised his hand. Sonu, you want to answer? Or your answer was same.

**unknown speaker** · lines 750-750 · spoken_turn

> Yeah, I mean, I guess, uh JavaScript engine maintains the order of the execution, you know, in JavaScript the order matters. So, uh even if it's micro task and micro task, so as I said even loop will observe, you know, the call stack first when it's empty, the first priority will be micro task and the second priority will be macro task and in the micro task we will have the, you know, tasks by order.

**unknown speaker** · lines 754-754 · spoken_turn

> Mike

**unknown speaker** · lines 758-758 · spoken_turn

> and it will push each other and same to micro task as well. So

**unknown speaker** · lines 762-762 · spoken_turn

> you know, somewhere they maintain the order. I mean, I don't know what exact way they maintain the order. Yeah.

**vasanth** · lines 766-766 · spoken_turn

> Sure. I'll take answer from one last person then I then explain myself. Is anybody else wants to answer? The answer so far so told is not fully correct. The pieces of it are correct. Anybody wants to answer?

**vasanth** · lines 770-770 · spoken_turn

> You could raise your hand.

**vasanth** · lines 774-774 · spoken_turn

> Okay. Sure. See, uh you could consider like this is an example of the depth that you need to go through and probably not beyond this. So in system design there is a concept. You design a system as simpler as required and not simpler than that. You don't want to over simplify this or you want to like over complicate it, try to keep it as simple as required, same way. So everything in the call stack is executed first like as Harshita, Sonu and others also explained, Shikar explained. So that is the first priority and

**vasanth** · lines 778-778 · spoken_turn

> that we pick task from micro task queue and every task is from here we'll move here one after the other until the micro task queue is empty. Okay and it get executed. And then in macro task queue we don't repeat it. Macro task queue we only pick the top one and we move here and we repeat the loop. So macro task queue is not emptied at once. So if you look at the order call stack must be empty. Executes all micro tasks. Executes one macro task can repeat the cycle.

<a id="record-7a24251346a1da0a"></a>
## Complex system analogy

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker uses the analogy of system design, emphasizing keeping processes as simple as required and avoiding oversimplification or overcomplication.
  - “You design a system as simpler as required and not simpler than that. You don't want to over simplify this or you want to like over complicate it, try to keep it as simple as required, same way.” — [lines 774-774](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000181`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 774-774 · spoken_turn

> Okay. Sure. See, uh you could consider like this is an example of the depth that you need to go through and probably not beyond this. So in system design there is a concept. You design a system as simpler as required and not simpler than that. You don't want to over simplify this or you want to like over complicate it, try to keep it as simple as required, same way. So everything in the call stack is executed first like as Harshita, Sonu and others also explained, Shikar explained. So that is the first priority and

<a id="record-65a17c77e371a0a2"></a>
## Understanding task execution priorities

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker connects task execution priorities with maintaining the correct order of synchronous tasks in the call stack to ensure priority execution.
  - “So because those were the things that were supposed to be executed on priority but instead we are picking something which was not so priority.” — [lines 814-814](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000191`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 814-814 · spoken_turn

> call stack is like when once after it's while it executing the micro task queue which is according to the priority the next priority after the call stack. If it start executing everything from the macro task queue which is of least priority there could be some some other synchronous task by then they've come and sit in the call stack. Correct? So if it wants to execute this then particular order of those synchronous task might get affected. So because those were the things that were supposed to be executed on priority but instead we are picking something which was not so priority.

<a id="record-c0b46791db2d2d3d"></a>
## Explaining execution priorities in JavaScript

**Product:** cases · **Type:** recorded_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Debate occurs over whether JavaScript's event loop executes all micro tasks at once or one by one.
  - “Sure. I'll take answer from one last person then I then explain myself. Is anybody else wants to answer? The answer so far so told is not fully correct. The pieces of it are correct.” — [lines 766-766](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000179`)

### Cue

- Vasanth invites more answers before explaining the correct sequence of task executions.
  - “Is anybody else wants to answer? The answer so far so told is not fully correct. The pieces of it are correct.” — [lines 766-766](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000179`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

- Vasanth will give his understanding of task execution priorities after inviting student explanations.
  - “then I then explain myself.” — [lines 766-766](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000179`)

### Rationale

Not stated in the cited excerpt.

### Response

- Vasanth explains that the event loop executes call stack tasks first, all micro tasks next, and only one macro task at a time to maintain order and priority in execution.
  - “So call stack must be empty. Executes all micro task, executes one macro task, repeat the cycle.” — [lines 782-782](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000183`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 746-746 · spoken_turn

> Okay. It is slightly different. Anybody else wants to answer? Maybe Sonu raised his hand. Sonu, you want to answer? Or your answer was same.

**unknown speaker** · lines 750-750 · spoken_turn

> Yeah, I mean, I guess, uh JavaScript engine maintains the order of the execution, you know, in JavaScript the order matters. So, uh even if it's micro task and micro task, so as I said even loop will observe, you know, the call stack first when it's empty, the first priority will be micro task and the second priority will be macro task and in the micro task we will have the, you know, tasks by order.

**unknown speaker** · lines 754-754 · spoken_turn

> Mike

**unknown speaker** · lines 758-758 · spoken_turn

> and it will push each other and same to micro task as well. So

**unknown speaker** · lines 762-762 · spoken_turn

> you know, somewhere they maintain the order. I mean, I don't know what exact way they maintain the order. Yeah.

**vasanth** · lines 766-766 · spoken_turn

> Sure. I'll take answer from one last person then I then explain myself. Is anybody else wants to answer? The answer so far so told is not fully correct. The pieces of it are correct. Anybody wants to answer?

**vasanth** · lines 770-770 · spoken_turn

> You could raise your hand.

**vasanth** · lines 774-774 · spoken_turn

> Okay. Sure. See, uh you could consider like this is an example of the depth that you need to go through and probably not beyond this. So in system design there is a concept. You design a system as simpler as required and not simpler than that. You don't want to over simplify this or you want to like over complicate it, try to keep it as simple as required, same way. So everything in the call stack is executed first like as Harshita, Sonu and others also explained, Shikar explained. So that is the first priority and

**vasanth** · lines 778-778 · spoken_turn

> that we pick task from micro task queue and every task is from here we'll move here one after the other until the micro task queue is empty. Okay and it get executed. And then in macro task queue we don't repeat it. Macro task queue we only pick the top one and we move here and we repeat the loop. So macro task queue is not emptied at once. So if you look at the order call stack must be empty. Executes all micro tasks. Executes one macro task can repeat the cycle.

**vasanth** · lines 782-782 · spoken_turn

> Remember this very very carefully. If you can really say this in interview when interviewer ask you about the event loop. Consider like probably you have attracted that interviewer very much. So next question that he would ask, she would ask. Like you are already in the good books of them. Okay? So call stack must be empty. Executes all micro task, executes one macro task, repeat the cycle. Okay? Before I go to the next topic, if there any question on this way of execution, please ask me.

**unknown speaker** · lines 786-786 · spoken_turn

> Vasanth, Vasanth, like why that's one micro task at a time? Why, why not, you know, just execute all of the micro tasks here?

**unknown speaker** · lines 790-790 · spoken_turn

> Wasn't

**vasanth** · lines 794-794 · spoken_turn

> Yeah

**vasanth** · lines 798-798 · spoken_turn

> any question similar to that I could collectively take the end answer. Anybody else has a question?

**unknown speaker** · lines 802-802 · spoken_turn

> same

**vasanth** · lines 806-806 · spoken_turn

> So, uh, to be very honest, there is no, uh, I mean straight away answer to why for this. Why, why it only picks one from here and not all from here at once. But I'll tell you from the implementation details point of view. So as we, as I already mentioned, everything that could be executed synchronously is already part of call stack. Point number one, anything that need to be executed synchronously already executed. Now anything of higher priority after that is kept in micro task queue. And least priority things are kept in micro task queue. As you all know,

**unknown speaker** · lines 810-810 · spoken_turn

> of course

**vasanth** · lines 814-814 · spoken_turn

> call stack is like when once after it's while it executing the micro task queue which is according to the priority the next priority after the call stack. If it start executing everything from the macro task queue which is of least priority there could be some some other synchronous task by then they've come and sit in the call stack. Correct? So if it wants to execute this then particular order of those synchronous task might get affected. So because those were the things that were supposed to be executed on priority but instead we are picking something which was not so priority.

<a id="record-3918b3d9bbab4f71"></a>
## Discussion on event loop execution order

**Product:** cases · **Type:** recorded_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- The discussion is about understanding how the event loop prioritizes tasks from the call stack, micro task queue, and macro task queue.
  - “Sure. Anybody else wants to answer this? I think my question is clear. Somebody Harshita, would you want to answer? Yeah.” — [lines 686-686](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000159`)

### Cue

- Vasanth asks if anyone can answer the question about task execution order in the event loop.
  - “Somebody Harshita, would you want to answer? Yeah.” — [lines 686-686](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000159`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Harshita explains that after the call stack is empty, the event loop checks the micro task queue and executes tasks in order.
  - “if I understood Hashitha your answer correctly, first, it'll execute everything in the call stack, then it look at a micro task queue, picks one and goes into the call stack, correct?” — [lines 698-698](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000162`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 686-686 · spoken_turn

> Sure. Anybody else wants to answer this? I think my question is clear. Somebody Harshita, would you want to answer? Yeah.

**unknown speaker** · lines 690-690 · spoken_turn

> so event loop basically checks first the micro task queue okay that to the stack wise first in the priority one will event loop check that and put it into the call stack first one the priority one

**unknown speaker** · lines 694-694 · spoken_turn

> and in the stack order.

**vasanth** · lines 698-698 · spoken_turn

> if I understood Hashitha your answer correctly, first, it'll execute everything in the call stack, then it look at a micro task queue, picks one and goes into the call stack, correct?

**unknown speaker** · lines 702-702 · spoken_turn

> Yes

**vasanth** · lines 706-706 · spoken_turn

> And then after that

**unknown speaker** · lines 710-710 · spoken_turn

> after that it execute that

**unknown speaker** · lines 714-714 · spoken_turn

> And then again you have to check for if there is something more it will put it if there is something in the middle you have to take it from the micronase else it will take from the micronase. Okay.

**vasanth** · lines 718-718 · spoken_turn

> Okay. Got it. I get what. I'll I'll repeat, you can correct me if I'm wrong. So everything in the call stack executed first. Once the call stack is empty, the loop will look if there is anything in the micro task queue, it will pick from there. Like it will pick first one and it will go to call stack and execute and it will continuously keep on doing that until there is micro task queue is empty. Am I right Harshita?

**unknown speaker** · lines 722-722 · spoken_turn

> Yes, correct.

**vasanth** · lines 726-726 · spoken_turn

> And then after that what about the macro task queue? How does that work?

**unknown speaker** · lines 730-730 · spoken_turn

> Again micro dots view there would be like uh in the stack order it would be and the first we will put and put it in the stack same way.

**unknown speaker** · lines 734-734 · spoken_turn

> Hello

**vasanth** · lines 738-738 · spoken_turn

> ओके, सी, यू सी बेसिकली बोथ आर एग्जीक्यूटेड इन द सेम वे, बट फर्स्ट प्रायोरिटी इज गिवन टू माइक्रो टास्क क्यू, फॉलोड टू माइक्रो टास्क क्यू, हर्षिता, एम आई राइट? यस, यस।

**unknown speaker** · lines 742-742 · spoken_turn

> Yes, yes.

**vasanth** · lines 746-746 · spoken_turn

> Okay. It is slightly different. Anybody else wants to answer? Maybe Sonu raised his hand. Sonu, you want to answer? Or your answer was same.

**unknown speaker** · lines 750-750 · spoken_turn

> Yeah, I mean, I guess, uh JavaScript engine maintains the order of the execution, you know, in JavaScript the order matters. So, uh even if it's micro task and micro task, so as I said even loop will observe, you know, the call stack first when it's empty, the first priority will be micro task and the second priority will be macro task and in the micro task we will have the, you know, tasks by order.

**unknown speaker** · lines 754-754 · spoken_turn

> Mike
