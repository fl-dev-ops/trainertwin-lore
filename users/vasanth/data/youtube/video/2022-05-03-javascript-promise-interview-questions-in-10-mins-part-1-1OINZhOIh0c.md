---
id: 1OINZhOIh0c
title: Javascript Promise interview questions in 10 mins (part 1)
date: '2022-05-03'
url: https://www.youtube.com/watch?v=1OINZhOIh0c
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ JavaScript being single threaded programming language needs some way  to execute\
  \ asynchronous task. Promise is one such method. It is considered be one of the\
  \ most common and tricky interview topic. I will be covering each and every aspect\
  \ of Promise in this video series. \n\nDoes async await block main thread in JavaScript:\
  \ https://medium.com/p/c07db9c48c3e\n\nEvent Loop - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop\n\
  Promise - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all\n\
  My Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:10:29
model: saaras:v3
transcript: true
---

# Javascript Promise interview questions in 10 mins (part 1)

## Transcript

### 00:00:00 · Speaker 1

हेलो ऑल, वेलकम टू अनकॉमन गीग्स, मैसेल्फ़ वसंत। आई होप यू आर ऑल डूइंग वेल। सो टुडेज़ टॉपिक इज़ प्रॉमिस।

### 00:00:07 · Speaker 1

So promises consider to be one of the again a tricky topic for the interview because you'll be using promise in a different way in a day to day basis but in the interview they'll ask you to write the promise in a different ways. So due to which many candidates struggle to answer these topics in interview. Also many many candidates actually doesn't know the fundamentals of promise why promise existing and how to create a promise how to resolve it how to reject it. So I I I pick the promise and I want to explain the promise very depth like every aspect of promise I try to cover here because promises many functions inside it.

### 00:00:37 · Speaker 1

like all settled, resolve, reject, finally, every aspect of promise I'll try to cover so that once you finish watching my entire promise series, you should know a lot about the promises. So whether it is interview or on a day-to-day programming, you should be able to use it very well, okay?

### 00:00:53 · Speaker 1

Now without wasting further time, question number one, why promise is necessary in JavaScript, correct? You all know JavaScript is a single threaded interpreted programming language, correct? So see since it is a single threaded, there's only one thread which will execute the code one line by line, correct? So but that is not always possible, like there is some let's say we are making a API call, correct? API call is going to let's say one or two seconds. If main thread waits for one or two seconds there itself and does not execute anything after that then, then it will affect the performance.

### 00:01:23 · Speaker 1

correct? So there has to be a way to achieve asynchronity in a single threaded programming language. So that can be actually achieved with multiple ways. One such way is via promises. Okay? There is a whole concept of event loop, event callback, all of that associated with how asynchronous asynchronity is achieved in JavaScript. I I try to cover that in one next video. That's also a very important topic for the interview. But this video let us stick to the promise itself. And you now you know why promises is used? Promise is used to asynchronity in JavaScript, very simple words, okay? Now without wasting further time, let's get started with the coding.

### 00:02:00 · Speaker 1

So, here, uh very first thing that we have to know is how to create a promise, correct? See, on a day-to-day basis you'll be creating a promise via a different way, like no one uses a keyword called promise to create a promise. You'll be making a network call or you're introducing some delays, etcetera, using the promises, correct? But in interviews generally they'll ask you to write a candidate, write a promise that will be resolved after two seconds.

### 00:02:23 · Speaker 1

Okay, many candidates will not know this itself. They'll not be able to write a promise that will be resolved after two seconds. So I'll start with the extreme basics on how to create a simple promise. Okay, before that I'll also show you the what is the definition of promises from the developer.mozilla.org. Okay, a promise is an object representing the eventual completion or failure of an asynchronous operation.

### 00:02:45 · Speaker 1

Okay. A promise is an object representing eventual completion or failure of a asynchronous operation. A promise can be succeeded or a promise can be rejected. Okay. The only two states of the promise because after you make a network call it can be either succeeded or failure. So promise has three states. Pending, fulfilled and rejected. So as soon as you make a network call it go to it will go to a state of pending. Or from there it can either fulfilled or rejected.

### 00:03:12 · Speaker 1

This is about the basics of the promise, the definition and the different states of promise, okay? Now let's see how to create a simple promise. So easiest way to create a promise is const from promise one is equals to new promise, okay?

### 00:03:31 · Speaker 1

actually new promise is also not required to start off with just promise dot resolve

### 00:03:39 · Speaker 1

Welcome to Uncommon

### 00:03:43 · Speaker 1

geeks. Okay? So here what I'm doing is I've created a promise called promise.resolve and inside that what I'm resolving, welcome to uncommon geeks. Okay? So here resolve stands for something of the promise has been executed successfully. Okay? So how do you extract the value from this promise? So you might have all done this on a day-to-day basis. promise.then will give a value what happens after the success of the promise. Okay? promise.then data

### 00:04:14 · Speaker 1

console.log

### 00:04:18 · Speaker 1

promise success

### 00:04:22 · Speaker 1

data. Okay?

### 00:04:26 · Speaker 1

Okay. So if I execute this one now, so you would see promise success welcome to Uncommon Geeks. Correct? So you got promise success and welcome to Uncommon Geeks. So you created a promise and the actually the promise got resolved. Resolved as I mentioned is promise happened successfully. So this is a manual promise, manually you are making a promise to be successful, but on a day to day basis when you are making API call, there is a chance, fair chance of it is getting successful or a failure. Okay? Let's say same, uh this API call or whatever the promise I am created, it is not resolved.

### 00:04:56 · Speaker 1

or putting other way whenever you are trying to execute a promise there is some error. So that can be mimicked via function called reject. Okay? So promise.then to catch whatever the error that has come that you can put in the catch block. Okay?

### 00:05:13 · Speaker 1

console.log

### 00:05:16 · Speaker 1

promise failure, okay? promise failure.

### 00:05:21 · Speaker 1

Okay, I'm sorry. So here, it should be error, okay?

### 00:05:27 · Speaker 1

promise failure welcome to uncommon case. This is the one first one and the most simplest way of creating a promise. In interview they'll ask you candidate please create a promise. This is the easiest way to create a promise. Okay. Sometimes interviewer will not be interested to dig deeper. He just want to know can you create a promise or not. Because the only way you know promise is via network call or you also know simply how to create a promise. Okay. So this will just this should cover that particular topic if interviewer ask like that. Now there is another question what is the other way see. They will ask you to mock a promise that will execute

### 00:05:57 · Speaker 1

execute for two to three seconds. Typical network call they'll ask you to mock because every interviewer doesn't come prepared with an URL which will take two seconds to resolve because that all I mean interviewer also sometimes come at the last moment. So they'll simply ask you candidate create a promise that will take three seconds to resolve. So that cannot be achieved directly this via this this approach, okay? How to create that promise also I'll show you.

### 00:06:19 · Speaker 1

See this video is as I said is to explain very basics of promise. In further videos we'll get into deeper and try to solve some complex flows as well. So how to create that promise? I'll do this. I'll use a new keyword. Then promise takes two arguments. So resolve and reject which you already know, correct? This is in a different way. Rather putting promise dot resolve, I'm adding those functions into the uh an argument here, okay? Now here what I'll do, I'll create one set timeout.

### 00:06:49 · Speaker 1

Set timeout for two seconds

### 00:06:54 · Speaker 1

inside the set timeout block, I will resolve, again, welcome to

### 00:07:00 · Speaker 1

uncommon gigs. Okay? So here what I will do, promise same. The further process remains same. Promise dot then data

### 00:07:12 · Speaker 1

log promise success okay. Then you are printing the data and here you have as usual catch block error.

### 00:07:25 · Speaker 1

log

### 00:07:28 · Speaker 1

error is

### 00:07:30 · Speaker 1

error. Okay? So, what will happen in this case? Okay? What we are doing is we have created a promise and inside our promise we have created a timeout. Okay? This timeout will execute after two seconds as we already know. So, after two seconds this resolve will be triggered and this resolve will return some values. In typical network response this could be an object or a complex JSON or just the status code it could be anything. Okay? So in our case we are just mocking it as a string. Resolve this. So this will execute only after two seconds. So if I

### 00:08:00 · Speaker 1

run this code one two Now you're seeing the output promise success welcome to uncommon gigs Hope you are able to see what is happening correct So if if interviewer ask let's create a promise that takes ten seconds okay You can just easily change by putting ten seconds here okay same any seconds The why interviewer ask is let's say you have to create three different promises with a different time to resolve like two second three second and five second and there are methods like promise.all settled and etcetera which will help you to call

### 00:08:30 · Speaker 1

all the promise at once and if can interview is in the mood to ask such questions then you should know first to create this then to create some other promise with the different times okay

### 00:08:41 · Speaker 1

So this is about the basics of the promise. So how to create a promise just with a promise dot promise dot resolve promise dot reject or with a profound way with a particular delay you can use this approach. So I'll also show you how to reject a promise, okay? In this case I'm rejecting a promise after the timeout. So ten second is too much so I'm creating again two seconds, okay?

### 00:09:03 · Speaker 1

two seconds

### 00:09:08 · Speaker 1

So here you see error is welcome to Uncommon Geeks. Okay? As you all know Uncommon Geeks is my channel name. So I just try to put that sentence somewhere here and there so that you are always remembered to that channel. Remember that channel. Okay? Fine, this is about the basics of promise creation, two different ways of promise creation I said. Okay? There were many other things that we want to see around the promises like if I put a log above the promise, below the promise, what's going to happen? What is the order of execution? Those those things let us study in detail in the next video. Okay? So as

### 00:09:38 · Speaker 1

takeaways from this video is how to create a promise, how to create a promise with a specific delay. Okay, two different ways of promise creation. Just practice these things properly, be sure of whatever the syntax, how to create a new promise, how to create promise.resolve. Be be clear about that. In further videos, let us well in detail about these concepts. Okay. Thank you so much for watching this video. I'll catch you in my next video. I'll try to link my medium blogs if I've written anything about the promise or any other related topics related to the asynchronity, please read that. So, whatever the question that I'll be asking,

### 00:10:08 · Speaker 1

upcoming videos that also I'll add in my GitHub repository that link also will be in the in there in the description okay. Thank you so again for watching this video. Do please do like the video if you liked it and do not forget to share this with your friends and please please please please subscribe to my channel Uncommon Geeks. Thank you so much. Catch you in next video.
