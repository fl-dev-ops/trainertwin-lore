---
id: 3V-fKuh1-8w
title: Javascript Promise interview questions in 10 mins (part 2)
date: '2022-05-04'
url: https://www.youtube.com/watch?v=3V-fKuh1-8w
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ JavaScript being single threaded programming language needs some way  to execute\
  \ asynchronous task. Promise is one such method. It is considered be one of the\
  \ most common and tricky interview topic. I will be covering each and every aspect\
  \ of Promise in this video series. \n\nDoes async await block main thread in JavaScript:\
  \ https://medium.com/p/c07db9c48c3e\n\nPromise Video 1: https://youtu.be/1OINZhOIh0c\n\
  Event Loop - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop\n\
  Promise - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all\n\
  My Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:12:55
model: saaras:v3
transcript: true
---

# Javascript Promise interview questions in 10 mins (part 2)

## Transcript

### 00:00:00 · Speaker 1

हेलो ऑल, वेलकम बैक टू अनकॉमन गीग्स, मैं सेल्फ वसंत, आई होप यू ऑल डूइंग वेल।

### 00:00:05 · Speaker 1

As you know, today's topic is again a continuation of promise. We have already discussed what is the basics of promise and different ways of creating the promise in a very simple way in JavaScript. So in this video, we are going to slightly extend the example by asking you some very common questions in the interview. So this video, unlike my other videos in this series, is not like purely dedicated for question and answer. It's a combination of question and answer and the explanation. Okay? So without wasting further time, let's get started. Here I've written question number one. So it's it's the same example as that of the last one.

### 00:00:35 · Speaker 1

I haven't made much change. Only change that I have made is I have put a three log statements in line number two, line number nine and line number fifteen. Okay? So line number two the thing is the statement is before promise starts, line number nine after promise starts, line number fifteen after promise ends. Okay? Very very straightforward. In line number five is as you know there is already set timeout and I resolve and that promise is been used here.

### 00:00:58 · Speaker 1

My question is very clear. You all you might have already you know what is the order in which the logs are executed. Okay? So this to answer this question you should know some basic knowledge on the event loop in the JavaScript. Okay? I actually thought of making a separate video on event loop but there are already tons of information available for the event loop and my purpose of making the video series is not to explain concepts of JavaScript but just to enable you for facing a interviews. Okay? So what I'll do I'll just try to touch base a little bit about the event loop.

### 00:01:28 · Speaker 1

there is there is a beautiful documentation in the developer.mozilla.org where they explain the event loop very much in detail. I'll also touch base little bit on this but I'll also link this URL in the description. Please go through and read it is very straightforward topic and you'll be able to understand. Okay? Now, question is simple. Which order the console lot log will be executed? Like will this this statement this statement is printed first then this etcetera. That is the question. If you know the answer please mention question number one and put your answer in the comment section. If not let me execute it.

### 00:02:00 · Speaker 1

uh let it finish then let's go to the explanation. So first statement that got executed is before promise starts, which is right. Second is after promise starts. Third is after promises and the fourth one is actually what was resolved in the set timeout. Okay? If you see here console.log before promise obviously this is right irrespective of whether promise exists in this block or not because this is the first statement in the in the given file. So it will be executed. It will be executed because it doesn't has any dependencies. JavaScript totally knows how to do

### 00:02:30 · Speaker 1

this how to execute this. It's not a function called where JavaScript go and look for a function. It's just a log statement and JavaScript logged it. Then it encode promise, encountered promise, but it did not execute anything related to promise. It came here, then it printed this also after promise starts. Then it saw promise dot then and it also knew there is a promise that exists in above above statement, okay? Still it did not execute this. Then it came here and after promise ends it got printed after promise ends. After these three statements are printed, then it went back and processed this.

### 00:03:00 · Speaker 1

Correct? If I if I had to just draw some pictorial image here say here, here say here, then it went back here. Okay? So it is it is highly unlikely for a programming language to go traverse like this where you go up, come down, then go back. So obviously that is not possible for a programming language to do that way. Either you should have some threads or something to go back. Correct? So JavaScript here uses the concept of event loop to achieve this.

### 00:03:24 · Speaker 1

If you see here, uh this is the stack and this is the heap and this is the queue. I'm keeping it very simple uh explanation here, okay? What happens is everything that is has to be executed in in sequentially without having any further dependencies or asynchronity will be part of this stack and it will be executed one after the other, okay? Whenever JavaScript encounters a asynchronous task like set timeout, set interval or um promises, it will move that from main stack to this heap memory, okay? Or this also some

### 00:03:54 · Speaker 1

places it is explained as web APIs. So here they take their own time, they execute it. Once they are done, they'll come back to this queue. Okay? So once JavaScript executes everything which are inside the stack, it will start picking the items from the queue.

### 00:04:08 · Speaker 1

Okay. So actually there is no order guaranteed here in this queue. Depending on however the tasks are completed, asynchronous tasks are completed and when the main thread becomes free, it starts picking the task from this queue. Okay. So what happened in this example is, so it saw promise, got to know, okay, it's promise. So I cannot execute it straight away because this involves some amount of work. It will involve some amount of delay. So let us skip this from here. Then it came here after promise, okay, I don't have to wait for anything, executed. It's a promise.then,

### 00:04:38 · Speaker 1

Okay, this it knows there is a promise which is executing in the top and here they are trying to do the dot then method. So after the promise is resolved, they want to perform certain activity. Okay, what JavaScript does is okay, this is an asynchronous task. So let us wait for this until this asynchronous task is completed, I cannot execute this dot then. So it will wait for. Then it will go it will skip this line or move it to the heap memory or web API and go to the next line and print it. After all these statements have been executed, then at certain point in time this also

### 00:05:08 · Speaker 1

sequential execution that is after two second. Then they come back to the queue and JavaScript main thread is free now because it has executed all the sequential operations. Then it will pick this.

### 00:05:16 · Speaker 1

and it will show on the screen. Okay? This is the order of execution. Now, this people with the concept of event loop will be able to answer this because this is very explicit, there is a two second delay. So whenever JavaScript encounter this JavaScript execution or unlike JavaScript every programming language is very fast. It doesn't take two seconds to print these things. They will be in some micro second they will be able to print all the three. So obviously this promise will be resolved after this these statements are printed. Okay? Because in a common sense also you can tell two

### 00:05:46 · Speaker 1

seconds it has to wait if it has to execute this promise so it will execute all the other three and come back here. What if I change from two seconds to zero seconds?

### 00:05:57 · Speaker 1

Now what will be the output?

### 00:06:00 · Speaker 1

So, why I'm asking this question is, uh only if you know the understand the concept very much in depth, then only you'll be able to answer for the variations of questions. Correct? Everybody will be able to answer the classical problems like this. So they would know, they would have read somewhere and they'll try to answer. Now set timeout is set to zero second. Correct? So, whenever set timeout is set to zero second, what is the expectation is executed immediately.

### 00:06:23 · Speaker 1

Correct? There is no time, you don't have to wait anything. So then JavaScript comes here, it looks at a promise which will be resolved in a zero second. So immediately, then it can, then it will come here after promise, promise.then it is already resolved by the time it comes here because it is not waiting for anything. Correct? But let me execute. If you know the answer, please do mention that in comment section, otherwise I'll execute it.

### 00:06:44 · Speaker 1

You see after promise, after promise starts and after promise ends and welcome to Uncommon Geeks. If you observe keenly the order in which the logs were printed did not get changed. The order remained same. Okay? Why because JavaScript doesn't bother much about what is the delay here.

### 00:07:01 · Speaker 1

JavaScript just see whether it is an asynchronous task or synchronous task. If it is synchronous then execute it. If it is asynchronous then move it to the web API section or heap memory, okay, where they have to wait until the processing is done. In this case it might be immediate, but still JavaScript has no special logic to differentiate between something with a delay of ten seconds, something with a delay of five seconds or no delay. It has a generic logic where all the asynchronous tasks are taken away from the stack and they are put in heap memory or web APIs. So then only after

### 00:07:31 · Speaker 1

JavaScript executes everything that is in a sequential or can be executed immediately only after that JavaScript picks this task. So due to which you might have seen here there is no delay here. Immediately this got printed because there is no delay. But still it has to wait for all the sequential tasks to complete. That will be the flow. Okay? So I also want to explain one last topic in this video that is

### 00:07:54 · Speaker 1

What is promise chaining? Okay, how to resolve promise chaining probably I'll take in the next video but you want I want you to answer what is promise chaining? Okay, we have one promise here. Then let let us have this as a two seconds of delay or one second delay and I'm just naming this as promise one. Okay, promise one.

### 00:08:13 · Speaker 1

Let's say there is another promise. Okay? Which is called promise two.

### 00:08:19 · Speaker 1

It has around two second delay. Okay? um Let me rename this as

### 00:08:26 · Speaker 1

promise this is promise one and this is promise two. I'm removing all the locks not required for this video.

### 00:08:33 · Speaker 1

So this is not a question actually, this is just a concept that I'm trying to explain in this video, okay? Which is a promise chaining. uh So, let's say you have a you have a requirement where you first you want to get the user data, after you have the user not uh skip this example, I'm speaking generally. So unless you have a user data, you cannot make a call to get whatever the user's preferences are, okay? Like you want to know what is the what is the let's say e-commerce site, first you need to have a user data, after you have a user data, you can

### 00:09:03 · Speaker 1

You can look for his recommendations, what he's most likely to uh interested in, so that let us show that on the top. So it's like only if a first API call is successful, we can make the second API call, correct? This is called the promise chaining. One promise is resolved, then we are gonna uh call the next promise, okay? So this is a promise one and promise two. So I'm just trying to mock that here. So here we have a console.data, then I'm gonna put promise

### 00:09:27 · Speaker 1

to okay or to be precise

### 00:09:31 · Speaker 1

I'm just copy this and I'll put here promise to dot then so to be just be separating it this is a promise one correct promise one

### 00:09:44 · Speaker 1

promise to. Okay, data to data to one. Just to avoid confusion, I'm renaming the variables. You can just still have the data because it's a functional scope variable, okay? And catch error. promise to

### 00:10:00 · Speaker 1

error here. So promise one error, okay? So now, why it is called chaining is because there is a one promise inside another promise. First let us execute, then let us see other answers. So promise one, promise one, promise two, promise two, okay? So whatever basically returned here. So promise inside

### 00:10:21 · Speaker 1

So

### 00:10:22 · Speaker 1

this console.log promise one and data one is also promise one whatever returned here. promise two and data two whatever is returned here. So promise two promise two. So why I I thought of showing you this is so this is just the two level of API calls correct. So there could be a possibility where you have a multiple hierarchy. So after you get this one user first you got the user information then you got the user recommendations. So in user recommendations could be general like what you would like in electronics and what you would like in food etcetera.

### 00:10:52 · Speaker 1

But in electronics, let's say he likes some Samsung phone. In Samsung phone, there are hundreds of category. Correct? Like maybe basic phone, feature phone, or any advanced tablets, etcetera. So now which category is interested? Let's say you have to make another call here. Promise two dot then. So inside this, you'll have a promise three.

### 00:11:10 · Speaker 1

So where you'll have a promise three, um, inside this and you want to make a call inside this after promise two dot is successful, then you will make a promise three. Okay? So where you make it data.

### 00:11:24 · Speaker 1

data three. Okay? So here you make it promise three and promise three. So now this is the third level of the promise. So promise is kind of getting chained one inside another, okay? There if you have worked on e-commerce or something highly scalable applications, maybe e-commerce, OTT streaming, you might have definitely encountered some scenarios like this where you have to call X API only after the voice output has come. Like there are multiple API calls you have to make there but you cannot make them in a

### 00:11:54 · Speaker 1

parallel way you have to make them in a sequential way. So you end up having this promise chaining one inside the another. See by now the way we started the example and if you look at it now code has already become clumsy. It is difficult to read this code. Correct? Because with a multiple hierarchies. And if you have to debug also it will become very difficult to put a break points and check. So to avoid this problem there are multiple ways. Okay? That is the first topic that we'll be discussing in next video. Okay? So thank you so much for watching. If you like this video please do like it on my YouTube channel.

### 00:12:24 · Speaker 1

and do not share, do not forget to share this video with your friends. And please, this is my humble request to subscribe to my YouTube channel and I'll try to add my medium links where I've written a lot of articles about JavaScript and React and Angular concepts.

### 00:12:38 · Speaker 1

I'll also link my GitHub URL where a lot of questions that are asked in this video, in this video there's only one question, but there are multiple questions that are asked across multiple video series of mine. So all of them are documented there. You can pick those questions and practice them, okay? So thank you so much for watching. Catch you in next video.
