# javascript objects

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-972547062fa87577"></a>
## JavaScript Object Mutation

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, objects and arrays are shallow copied, so mutations can reflect on the original object if modified.
  - “Objects and arrays are shallow copied so by nature it is not going to get mutated.” — [lines 706-706](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000150`)
  - “Yes, it's gonna get reflected. Okay.” — [lines 714-714](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000152`)

### Original context

**vasanth** · lines 706-706 · spoken_turn

> obligation arrays are shallow copied I'm very sorry. Objects and arrays are shallow copied so by nature it is not going to get mutated. If you want to mutate it you can mutate it Param.

**unknown speaker** · lines 710-710 · spoken_turn

> ओके, एंड लाइक इफ इफ आई डू आई हैव टू रिटर्न फ्रॉम दैट फंक्शन और जस्ट इफ आई चेंज सम प्रॉपर्टीज देन इट विल बी रिफ्लेक्टेड इन द

**vasanth** · lines 714-714 · spoken_turn

> Yes, it's gonna get reflected. Okay.

<a id="record-2f947b09bb866402"></a>
## Exchange on Object Mutation

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Vasanth clarifies confusion by affirming the nature of shallow copying in JavaScript when asked about object mutation.
  - “obligation arrays are shallow copied” — [lines 706-706](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000150`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 706-706 · spoken_turn

> obligation arrays are shallow copied I'm very sorry. Objects and arrays are shallow copied so by nature it is not going to get mutated. If you want to mutate it you can mutate it Param.

**unknown speaker** · lines 710-710 · spoken_turn

> ओके, एंड लाइक इफ इफ आई डू आई हैव टू रिटर्न फ्रॉम दैट फंक्शन और जस्ट इफ आई चेंज सम प्रॉपर्टीज देन इट विल बी रिफ्लेक्टेड इन द

**vasanth** · lines 714-714 · spoken_turn

> Yes, it's gonna get reflected. Okay.

<a id="record-35f5076e5da376aa"></a>
## Mutating JavaScript Objects

**Product:** cases · **Type:** recorded_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Param asks about mutating objects passed as function arguments and whether it reflects on the original object.
  - “like in the example where object was passed in an argument in a function” — [lines 690-690](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000146`)

### Cue

- do we have to return that object also if we mutate
  - “do we have to return that object also if we mutate” — [lines 690-690](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000146`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Objects and arrays are shallow copied so by nature it is not going to get mutated.
  - “Objects and arrays are shallow copied” — [lines 706-706](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000150`)

### Outcome

- If objects are modified, the changes reflect in the original object.
  - “Yes, it's gonna get reflected. Okay.” — [lines 714-714](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000152`)

### Original context

**unknown speaker** · lines 690-690 · spoken_turn

> Yeah, so like in the example where object was passed in an argument in a function. So like in that case do we have to return that object also if we mutate or if we if we do not return that object and reassign in the call caller function like will it mutate the original object?

**vasanth** · lines 694-694 · spoken_turn

> No, I I do not fully understand. Like for example, the one I explained in the beginning of the session, let's say you are you are manipulating a large object by passing it to a particular function and then getting it back param. Is that the example you are speaking?

**vasanth** · lines 698-698 · spoken_turn

> Yeah, that one also. Exactly. So, I'll repeat the question first and then I'll answer. So, I was explaining like many a times in code review etcetera people think you are passing a heavy object into a utility and transferring it and getting back. People consider it as a bad thing. So, instead of that you can just pass the object. What I was suggesting you can pass the object, only reference will be passed. You can now modify and come back. Now with respect to mutation param in JavaScript which you know, objects and arrays are deep copied.

**unknown speaker** · lines 702-702 · spoken_turn

> Yeah, that one also. Exactly.

**vasanth** · lines 706-706 · spoken_turn

> obligation arrays are shallow copied I'm very sorry. Objects and arrays are shallow copied so by nature it is not going to get mutated. If you want to mutate it you can mutate it Param.

**unknown speaker** · lines 710-710 · spoken_turn

> ओके, एंड लाइक इफ इफ आई डू आई हैव टू रिटर्न फ्रॉम दैट फंक्शन और जस्ट इफ आई चेंज सम प्रॉपर्टीज देन इट विल बी रिफ्लेक्टेड इन द

**vasanth** · lines 714-714 · spoken_turn

> Yes, it's gonna get reflected. Okay.
