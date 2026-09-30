---
id: c3c-LLdjlGc
title: 🔥 90% of you will fail to answer this simple JS Question - Does async await
  block JS main thread 🔥🔥?
date: '2022-06-29'
url: https://www.youtube.com/watch?v=c3c-LLdjlGc
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ JavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nPromise video 1: https://youtu.be/1OINZhOIh0c\nPromise video 2: https://youtu.be/3V-fKuh1-8w\n\
  Promise video 3: https://youtu.be/7a3ZwYko05s\nPromise video 4: https://youtu.be/A5Az9NgncEE\n\
  \nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nDoes async await block main thread in JS: https://mevasanth.medium.com/does-async-await-block-javascript-main-thread-c07db9c48c3e\n\
  \nEvent loop in JS: https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop"
author: careerwithvasanth
duration: 00:12:04
model: saaras:v3
transcript: true
---

# 🔥 90% of you will fail to answer this simple JS Question - Does async await block JS main thread 🔥🔥?

## Transcript

### 00:00:00 · Speaker 1

Let me run this code. You see it printed before async and await. Then it printed after async and await. Now observe the code carefully. So if let's say this was not there. Async and await was not there, correct? Then JavaScript crypto would have executed this in the similar way line.

### 00:00:22 · Speaker 0

all

### 00:00:22 · Speaker 1

Welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. So if you see me for the first time on the internet, I'm a content creator who help people to clear their interview. I made lot of beautiful series in the past and I'm continue to add lot of videos to the same series as well, okay? So that's all about myself and now let's get started with the content of the video.

### 00:00:40 · Speaker 1

So I what you saw on internet, what you saw on the thumbnail was maybe quite confusing for most. Does async await block the JavaScript main thread? Maybe unless you saw this line for the first time, you always had maybe whatever your mindset, but now you start getting confused. Does it block or does it does it not block?

### 00:00:59 · Speaker 1

So if I had to broadly categorize the audience at least seventy five percent who are preparing for the interview will know what is Asink and Navit. But now after looking at this question they are getting confused. Twenty five percent of the folks may not know what is Asink and Navit. I'm trying to touch base on Asink and Navit promise in this video but not very much in depth because I've already made a detailed video about promise in the past. I'll try to link that in fact more than three four videos I have made. I'll try to link that on the screen also in the description section. So watch the entire promise series so that you'll get a proper sense of how Asink and Navit are executed in

### 00:01:29 · Speaker 1

script, why promise earning required and probably what are async and await, okay? After watching those videos, if you come to this video, it will be very helpful for you, okay? Now, let's get started with the simple coding, okay?

### 00:01:41 · Speaker 1

So function test promise one okay and log no no not log return promise daughter resolve

### 00:01:57 · Speaker 1

one, okay? In case if you don't know what I'm doing here, the I would highly advise you to go and watch my promise series where I've explained all of this step by step, okay? Now, so for those of you who don't know, very simple words if you have to tell, I've created a promise. Now I'm going to call the promise from outside the function, okay? So test promise dot, you know, promise generally have then, finally, catch, etcetera. So I'm calling then.

### 00:02:20 · Speaker 1

डेटा

### 00:02:23 · Speaker 1

log data is

### 00:02:26 · Speaker 1

data. Okay? So now if I run this code,

### 00:02:30 · Speaker 1

So I'm getting data is one, correct? Which is absolutely right. You have created a promise, so you are able to get this data. So basically promise will help you to achieve versing clonity in JavaScript as most of you know. So now what I'll do, I will extend this example, okay? I'll create two more promise. So test promise two.

### 00:02:48 · Speaker 1

and promise three, test promise three, okay? So now rather printing it here, I'll do this.

### 00:02:55 · Speaker 1

So this is num one

### 00:02:59 · Speaker 1

num two, promise two, okay? And promise three.

### 00:03:08 · Speaker 1

and num three here. Okay? And I will log num one plus num two plus num three. Okay? num one plus num two plus num three.

### 00:03:20 · Speaker 1

So basically in this case if you see I have three promises created, promise one, promise two, promise three, both are resolving into a number one, two, three. And I have a use case where, I mean this use case may not happen in your day to day, but imagine a use case where you have to call multi promise one is at another, okay? So same I'm trying to mimic here with a simple example. So if I run the code I'm getting six, which is sum of one, two and three. So there are times in your real time in the in the programming also where you you have to nest the promises like this. So as you can see after third level itself it is

### 00:03:50 · Speaker 1

start looking ugly. So to avoid this you use the asink and navet. So asink and navet actually refers for a syntactical sugars. Okay? So they help you to basically code this in a much clean and neat way. Okay? So now

### 00:04:03 · Speaker 1

that most of you know. In fact, I've written a beautiful article about does async and I would block the main thread here. And this is one of the article that was a lot of people have viewed it and I think still most haven't understood this properly. So I thought of creating a video and explaining it because somebody are still debating like what you explained is right or somebody telling you know what you explained is wrong. Okay? So I've tried thought of making this video to clear all the problems that people are facing. Okay? Now, let's come back here and I what I'll do, I will make all these functions async.

### 00:04:33 · Speaker 1

Okay, because I have to if I have to use an await, then the function has to be async, okay? Now I'm creating another async function called test, okay? Function test.

### 00:04:45 · Speaker 1

So then I'm doing await.

### 00:04:48 · Speaker 1

test promise, I'm sorry, test promise one, okay? Then I'm doing await test promise two, then I'm doing await test promise three.

### 00:04:58 · Speaker 0

Okay

### 00:04:59 · Speaker 1

Okay

### 00:05:00 · Speaker 1

So here I'm doing cons number one. Okay?

### 00:05:05 · Speaker 1

same I'm doing here also cons num two. same I'm doing here also cons number three, okay? So command K F will format your code, maybe control K F will do that on the windows, okay? Now, I'm logging.

### 00:05:21 · Speaker 1

some is

### 00:05:23 · Speaker 1

or else let's not need not to have a sum. Just I'll print num one plus num two plus num three, okay? So like I mentioned async and datas intactical sugars basically they help you to they don't avoid you to do the promise nesting but they'll help you to write that in a very beautiful fashion, okay? Now. So if I run the code, let me first run the code. I haven't invoked the test, let me invoke the test from here, okay?

### 00:05:49 · Speaker 1

six. Okay. So now what I'll do, I'll put a log statement here. Okay. uh before

### 00:06:00 · Speaker 1

before a sync of it, okay? Then, I'll write a statement called after a sync of it.

### 00:06:06 · Speaker 1

Okay. So now let me run this code. You see it printed before async and await, then it printed after async and await. Now observe the code carefully. So if let's say this was not there, async and await was not there, correct? Then JavaScript crypto would have executed this in the similar way, line by line execution, correct? So where first line it will execute this, then it would do any other operation here, then it will go to the next line. Whenever there is an async and await, what was our expectation basically?

### 00:06:36 · Speaker 1

So basically the expectation is JavaScript should move that logic into the event loop like as you see here, correct? Whenever there is a main thread is been busy, it will move the things to the heap, okay? Or there is event loop concept, entire event loop concept. But in very simple words, whenever the main thread is doing some operation and there is any asynchronous activity like set term out promise etcetera, it will move into the heap memory and once they are done execution, they should they'll get back to the queue and whenever main thread is it will execute it, correct? So I guess most of you would know this. If not, please read

### 00:07:06 · Speaker 1

the developer.mozilla.org link. I'll try to put that on the description section. So now here if you now observe carefully, isn't it being a synchronous activity rather being asynchronous where this printed?

### 00:07:19 · Speaker 1

unless this entire operation was completed, this is not getting printed. So does async and await block the main thread?

### 00:07:29 · Speaker 1

See, the purpose of asking this is to trick basically. But now at least by now if you are thinking what is the right answer, please do mention that in comment section, okay? If not, then I'm going to explain in a while, okay? So, now let me decode this, let me make this a little more trickier, okay?

### 00:07:46 · Speaker 1

So what I'll do, I'll put this here before calling test.

### 00:07:53 · Speaker 1

after calling test. Now guess the output, what will be the output? The order of logs, what is the order of logs now?

### 00:08:02 · Speaker 1

I know it is get might be making a little confusing. The purpose of making this is to you should have a very solid understanding of async and await or a promises. So by the end of this definitely you will get that. Okay so please please stay tuned with me. So now let me run this. Okay definitely you will get to know what is the answer. So before calling test. Okay. Then before async and await. Okay. Then after calling test. Then after async and await. Correct and this log and after async and await. So order is one.

### 00:08:33 · Speaker 1

Two

### 00:08:35 · Speaker 1

थ्री

### 00:08:37 · Speaker 1

four. Am I right? So, this was the one and this is two, this is three and this is four. Now you're still thinking it is blocking main thread? I don't know how many of you thought it is blocking main thread, but it is not blocking the main thread to clarify, okay? So where this is a you are calling the this one.

### 00:08:56 · Speaker 1

before calling obviously that gets printed first. As soon as you call test this get printed because main function can main thread can directly execute it doesn't need any computation. So it executed and this is a nursing block. So main thread came back from this out of the function and it gave it created a separate context let us for it to finish the execution. It printed it then the main thread is free and this asynchronous task also got completed okay so it came back then it added this the log and it printed. Okay it

### 00:09:26 · Speaker 1

printed its log and after that it printed this also. So now the quite confusing question is if where is why these two lines are getting printed after the execution? Because this can be printed immediately, correct? This doesn't require a processing. uh the whatever the promise happening, that that order is is not actually required, correct? But technically what is happening because of the async and await and the promise whatever we have, correct? It is similar to this.

### 00:09:53 · Speaker 1

promise, let me write here. So test promise, I'm sorry, test promise one dot

### 00:10:03 · Speaker 1

then and you have the number one, correct? So similarly if you nest this with test promise two and with test promise three,

### 00:10:13 · Speaker 1

Test Promise

### 00:10:15 · Speaker 1

two and test promise three. Okay?

### 00:10:20 · Speaker 1

So, now what is happening, these two log statements whatever you are seeing, okay? So, async and await are kind of making the execution block to wait until something processed, correct? So definitely the that main thread will not pass through this and come here. So, it is similar to having these two statements here.

### 00:10:38 · Speaker 1

Okay? And this statement is here.

### 00:10:43 · Speaker 1

Okay? Now I think you got the analogy. Like I mentioned before also, async and await will not uh block the main thread. And whatever the promise nesting that is happening, right? Even that is also not stopped because of async and await. Async and await will only syntactical sugars. Rather writing it in a three nested way, it will help you to write in a three lines one by one like this, okay? That's all happening. So the reason I'm asking is lot of candidates get confused with this question in the interview, okay? I don't know any big

### 00:11:13 · Speaker 1

company asking this but definitely if anybody asks you definitely candidates get confused. Especially with the two of these logs where this requires a value of computation of the async activity and this doesn't require anything can be logged directly what is the process how the execution happens. Correct? So this is the purpose of my video I guess most of you got async and await does not block the main thread okay please read my medium article also where I've clearly explained this this concept step by step okay but this might be having a lot more working code compared to there okay. So that's all about

### 00:11:43 · Speaker 1

this video. If you're liking my content that I'm making on the YouTube, please do like my videos. Do not forget to subscribe to Uncommon Geeks. This this question I'll try to put in GitHub. Download the project from GitHub and practice this question. Try to start my GitHub project. Read all my medium blogs. I've written a lot of beautiful articles and follow me on medium also. Okay? Thank you so much. Catch you next video.
