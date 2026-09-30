---
id: O7n9w_f9u9A
title: 🔥 Learn Memosation in JavaScript 🔥 | Simplest explanation Ever | Most important
  frontEnd Int topic
date: '2022-08-08'
url: https://www.youtube.com/watch?v=O7n9w_f9u9A
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Definition: It is an optimisation technique used primarily to speed up computer\
  \ programs by storing the results of expensive function calls and returning the\
  \ cached result when the same inputs occur again\n\nInterview Preparation series\
  \ : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMy medium blog on memoisation: https://mevasanth.medium.com/memoization-in-javascript-hot-topic-for-interview-815475544ab0\n\
  \nMedium Blog https://mevasanth.medium.com/ \n\nMemoisation Github repository: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/blob/main/Common%20JavaScript%20Interview%20Question/memoisationample.js\n\
  \nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\n\
  Github Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nMAANG series for frontEnd Developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN"
author: careerwithvasanth
duration: 00:20:59
model: saaras:v3
transcript: true
---

# 🔥 Learn Memosation in JavaScript 🔥 | Simplest explanation Ever | Most important frontEnd Int topic

## Transcript

### 00:00:00 · Speaker 1

this example. Why I write a simple example, that's my speciality. So where I am good at giving a very simple example for a complex topics. Okay, let's say if I started writing this for a factorial, most of you would have stopped watching the video, correct? And in the interview, every time they will not ask you to write a complex example, they would just want to know whether you are aware of the concept or not, correct?

### 00:00:24 · Speaker 1

Welcome back to Uncommon Geeks. Myself, Prasant. I hope you all doing well. In case if you're seeing me for the first time on the internet, I'm a content creator. I help people to clear their interviews. I have made a lot of beautiful series in the past which has been appreciated by many. And in the recent past, at least in last few weeks, I've got a lot of love. Even in less than a day, I've got more than hundred, hundred fifty subscribers on my YouTube. Thank you so much for all the love that you're showering on me. I wish you please continue doing the same. Like I always say, I have only one noble cause of helping

### 00:00:54 · Speaker 1

a lot of people to aspire to the job that they really want to go. That's the whole purpose of my channel where I make a lot of videos just by that. I make good amount of research just to come up with the good concepts which are asked in the interview and how to prepare them. So please like and share my channel and if you're not subscribed to my channel, please subscribe, okay? Now let's get started with this video topic. So that is memoization, okay?

### 00:01:18 · Speaker 1

This is one of the very very important interview topic. So whether we are looking it from the perspective of data structure and algorithm or you are looking it from the perspective of just a JavaScript concepts or itself, okay? So whether you are aspiring for plain HTML JavaScript developer, Venn developer or React developer, React Native developer, Node.js developer or Angular developer, memorization is very very important concept, okay? So there are basically two verticals of memorization, how the questions can be asked, okay?

### 00:01:48 · Speaker 1

that I'm going to explain somewhere in the middle of the video. So please watch the video till the end to know the different personas and what I'm covering in this video, all of that. Okay? Now without wasting further time, let's get get started by making our hands dirty. Let's start some coding. Okay? So first thing here, uh let's start with the definition of memorization. This is uh me where I always want to give the definition, then only I'll generally start explanation. Uh reason is I strong believer of conceptual knowledge first, then the practical knowledge. So you need to know what is happening.

### 00:02:18 · Speaker 1

what is the official definition? Because even this will be asked in the interview and they will not allow you to write the code always. So please have at least basic definition, not a bookish definition, whatever you understood, that definition you need to know, okay? Now, let's see the definition. Definition, an optimization technique used primarily to speed up computer program by storing the result of expensive function calls and returning the cache result when the same input occur again. uh most may understand, but in very simple simple words is what is memorization is is this

### 00:02:51 · Speaker 1

So whenever you're doing a big computation where the computation result is so high or the computation happened to get the result is so high, then don't do it repetitively. If there is a chance where you can catch that value, then please catch the value and return the cached value. In very simple example, the factorial program, correct? What is factorial of five? One twenty. Five into four into three into two into one, which is one twenty, correct? Factorial of ten, it's a very big number, I can't tell that. Factorial of twenty, most

### 00:03:21 · Speaker 1

compilers if you don't know factorial of twenty you will not get the result easily okay because it it it exceeds all the usual data types that we use in case if you know what is the data type that is used to store twenty factorial in JavaScript please mention that in comment section okay definitely if you write a let x equal to factorial of twenty then you will not get the answer okay at least what the expected answer you will not get that answer now so see let's say twenty factorial means when you are doing the five factorial you have already multiplied four into

### 00:03:51 · Speaker 1

two into two into one, correct? When you already did the ten factorial, you already multiplied ten to one. So whenever you are doing twenty factorial, again you need not to multiply twenty, nineteen, eighteen, etcetera. So whatever you have multiplied till nineteen factorial, you can store that value somewhere, just multiply twenty to that, correct? So it would save around nineteen multiplication operation that you wanted to do, correct? In simple words, this is memoization. So memoization is nothing but trying to cast the value of the previous processing, uh, and use it for the further processing. Is it possible all the time?

### 00:04:21 · Speaker 1

no. Only for repetitive actions it is possible. For those functions which you are not sure whether the same set of inputs are coming to going to come again or not, then it's an unnecessary headache of using the memoization, correct? Every optimization technique comes with its own performance problems. So just because somebody else is using, don't use that. Just make sure you have a scenario of a function which is called repetitively and there's a possibility where you could store that result somewhere. Only then go for the memoization, okay? Why you need to know this concept is not just from the

### 00:04:51 · Speaker 1

review perspective, but even when you are writing that your day-to-day code, if you start using this memorization concept, definitely you will you get appreciation by your peers whenever they are doing your code review, okay? Now let's see a very simple example.

### 00:05:04 · Speaker 1

So, let's say I have a function add, okay? It will take a number as an input, then it will return

### 00:05:12 · Speaker 1

number plus ten. Okay? All it does is this. It will take one number as an input, adds ten into it and return the result. Let's invoke that. Okay? log add twenty. Okay? So let me run the code. Nothing supernatural happens, it's very straightforward. So we added twenty to ten, which is thirty and it is got returned, correct? Now, let's call this three more time, four more times, correct? So if I run the code, again nothing special happens, we are just getting thirty four times. So by

### 00:05:42 · Speaker 1

Now you got the idea what is happening. So every time whenever you invoke the function and passing the same arguments you are trying to add it to ten and return the result. Correct? So rather adding doing the same operation four times if you can cache this value somewhere the return of this function that is num plus ten value somewhere and if you can return that result it will be much easier. Correct? That's what the memorization stands for. Now what I'll do is I'll create a variable called cache. Okay?

### 00:06:12 · Speaker 1

And here what I do is very very simple. So what I'll do I'll see if cash has a num. Okay? uh if it has then what I'll do is I'll return

### 00:06:24 · Speaker 1

I'll return cash of

### 00:06:28 · Speaker 1

cash of num, okay? If not, what I'll do is cash of num is equals to, don't worry, even if you're not understanding, I'll explain this once again. Number plus ten, okay?

### 00:06:43 · Speaker 1

Okay. So, I'll explain once again everything that I've coded here. Okay? So basically, we have created a simple JavaScript object and inside that, what we're checking is cache of num, correct? So cache of num here stands for whatever the number that we are passing. If cache of twenty exists, then because why? Because though you are adding ten all the time, number might vary, correct? Number that you're passing might vary. So you have to keep a check whether you have already added ten to that number or not. When you have

### 00:07:13 · Speaker 1

added that number already. So then it will be present here. Cash of num is equal to num plus ten. So I'll I'll also show the object notation in a while. But in very simple words, first time you call this function. So cash of num doesn't exist, it will come here. So cash of twenty is equal to twenty plus ten which is thirty. So now cash of twenty is like an object like this. Okay? Cash of twenty is an object like this with a value of thirty. Okay? Next time whenever you invoke it, so let's say you have cash of ten which is twenty like

### 00:07:43 · Speaker 1

So here you are checking whether cache of num exist. If cache of num exist you return the cache of num itself. Okay very very simple. So now let us put a log here. Log

### 00:07:55 · Speaker 1

log okay?

### 00:07:59 · Speaker 1

inside regular processing. Okay?

### 00:08:06 · Speaker 1

and this is inside, I'm sorry, below one is the regular processing, okay? inside regular processing and this is the inside cached processing, okay? let me run this.

### 00:08:17 · Speaker 1

See, once it went inside a regular processing here. Then next three calls went inside the cached processing. So that means whatever the addition operation that was happening here, that is saved, correct? So system, whatever the CPU that was allocated to this now, is can be used for some other purpose, correct? So this may not be so useful with respect to add example, but let's say you are doing a very complex example, like I said the factorial. So in that case, it will be very, very beneficial, correct? Now,

### 00:08:45 · Speaker 1

Let's say rather passing twenty, okay, one more thing I'll do, just for your understanding, I'll also try to log the cash, okay? How the object looks like.

### 00:08:56 · Speaker 1

log cache. Correct, so cache is first empty, then cache is twenty comma thirty, twenty comma thirty, twenty comma thirty. Now, you pass twenty twice, let's say you pass ten twice, okay? Ten twice, what will happen?

### 00:09:11 · Speaker 1

So here, here inside regular expression, inside cached expression. For ten, again it need to go for a regular processing once because it is not cached. So it is cached once and then it is returning the cached value, correct? So it's very very simple to understand this example. Why I write a simple example, that's my specialty. So where I am good at giving a very simple example for a complex topics. Okay, let's say if I started writing this with for a factorial, most of you would have stopped watching the video, correct? And in the interview, every time they will not ask you to write a complex example,

### 00:09:41 · Speaker 1

You just want to know whether you are aware of the concept or not, correct? Now, easy example you understood. Now let's get into complex example and see how to solve that, okay? So, before I start reading the complex example, so I think it is close to now nine minutes thirty seconds. In case if you liked so far whatever I've taught, please like this video on YouTube and comment whatever you are feeling about the video. In case if you're not subscribed to my channel, please subscribe to my channel. I always say this somewhere in middle of my video because

### 00:10:11 · Speaker 1

um as I always say, by liking lot of many likes if I get for the video, YouTube starts showing my videos for the lot of people. If lot of people start watching the video, then lot of people um start subscribing to me and following my videos. Basically, the videos become popular, when videos become popular, there's a high chance somebody clears the interview. All I have is that noble cause, helping people to clear the interview. I can succeed only if you like and comment for this video and subscribe to my channel if you're not already subscribed. So please subscribe and share these videos with your friends if they're preparing for their interview, okay? Now, let's

### 00:10:41 · Speaker 1

start with a slightly complex example which is a Fibonacci. So, Fibonacci series, everybody I think if you are any sort of a graduate whether engineering, B.Sc., M.Sc., any sort of a graduate you are, anything related to computer if you have done or maths you have done, you might have heard of Fibonacci series, correct? Fibonacci series in simple words, let me first write that. two, three, four, five, six. So this is a regular number. uh Fibonacci of zero is zero. Fibonacci of one is zero plus one which is one. Fibonacci of two is zero plus one

### 00:11:11 · Speaker 1

which is one. Fibonacci of three is this one. Fibonacci of two plus Fibonacci of one, which is two. Fibonacci of four is Fibonacci of three plus Fibonacci of four is three plus two, that is two plus one which is three. Fibonacci of five is three plus two, five. Fibonacci of six is five plus three, eight. Okay? Very simple. I think all of you might have studied Fibonacci series in your graduation time or if you're still graduating, you might have just now learning this thing in your in your graduation. See, Fibonacci series has a lot of advantages.

### 00:11:41 · Speaker 1

the golden quadrilateral etcetera and how the tree branches out there is lot of concepts beyond Fibonacci but that is out of context for my video but my video is focused on how to write a Fibonacci for a given number correct let's say you pass five you should get a Fibonacci as five Fibonacci of six is eight Fibonacci of two is one so this is what you you want to do in the example let's take a simple recursive example I'll also draw and show you how the Fibonacci works and then let us add the

### 00:12:11 · Speaker 1

cashing and I'll explain why cashing necessary, how it will definitely help the execution of the program. This is again very very important topic for the interview. Please watch the video till the end, do not skip. Okay? Now, let's first write a normal Fibonacci function. Fibo Fibonacci. Somebody calls it Fibonacci. I I'm calling it Fibonacci. I don't know which is right pronunciation but I've heard both in the internet people saying. So I'm just signing to Fibonacci. In case if I'm wrong, please add the comment. Probably in future I'll just correct myself.

### 00:12:41 · Speaker 1

Okay. So Fibonacci, this series takes a number, okay? So what are the possibilities? Let's say, see, I would have not erased that number. So zero, one, two, three, four. So Fibonacci of zero is zero. Fibonacci of one is one. Fibonacci of two is Fibonacci of one plus Fibonacci of zero, that is one. So Fibonacci of three is one plus one, two, goes on, correct? So now we have certain conditions here. So I'm writing a recursive solution. I'll explain step by step, don't worry. So recursion means always there should be

### 00:13:11 · Speaker 1

a base condition which is satisfied then only the recursion will close the execution stop the execution. So if num is equals to zero then what you are doing you are returning zero correct. If number is because Fibonacci of zero is zero Fibonacci of one and if Fibonacci is one or two is one okay. num is one

### 00:13:35 · Speaker 1

or num is two. Then you are returning one. If not what you are returning? If not you are returning Fibonacci, you are calling the above function again, okay? Fibonacci of n minus two plus Fibonacci of Fibonacci of n minus one, okay? I'm just commenting this.

### 00:13:56 · Speaker 1

So you you got to know why I'm doing n minus two plus n minus one. We already discussed Fibonacci of four is Fibonacci of three plus two. Fibonacci of four is uh four minus two is two. Four minus one is three. So we are doing the same here as well. Okay? So Fibonacci of n minus two and Fibonacci of n minus one. Let's first run the code and make sure we are getting the output as expected. Then only let us start the explanation. So Fibonacci of uh four is three, correct? Let's see are we getting

### 00:14:25 · Speaker 1

Fibonacci of n minus two, n is not a number, I'm sorry. I think you all might have noticed this and waiting for me to correct, I'm sorry. Okay. n and m, I I missed. So Fibonacci of four is three. Fibonacci of five is five. Fibonacci of six is eight. Okay.

### 00:14:45 · Speaker 1

So let's say Fibonacci of six I want to calculate.

### 00:14:50 · Speaker 1

Okay, let's calculate the extremities Fibonacci of zero.

### 00:14:54 · Speaker 1

of one

### 00:14:59 · Speaker 1

Fibonacci of two

### 00:15:03 · Speaker 1

Vasant, why you are doing zero, one, two and all again and again? See, why I do this is we always have to track the extremities. No matter how confident you are, the least values and the highest values, whatever your input, please validate that in the even in the interview because other case it will work but the extremities it will fail. Now, so Fibonacci basics you understood, correct? But let me give you the explanation. The code is working, let me give you the explanation. So, let me draw, as you always know my drawing is not that good, okay? So now you have to calculate Fibonacci cough

### 00:15:35 · Speaker 1

Fibonacci of

### 00:15:37 · Speaker 1

three, correct? What is Fibonacci of three? Fibonacci of three is Fibonacci of

### 00:15:45 · Speaker 1

Trigonometry of two

### 00:15:48 · Speaker 1

plus Fibonacci of

### 00:15:51 · Speaker 1

Fibonacci of one, correct? What is Fibonacci of two? You already saw. Fibonacci of two from the code is one. Fibonacci of one from the code is also one, correct? So, if you go back here, Fibonacci of two is one. Fibonacci of one is one. So, Fibonacci of three is one plus one, two. So, Fibonacci of three is two, correct? So, Fibonacci of three is two. Even if you see in here in the example, Fibonacci of three is

### 00:16:21 · Speaker 1

two. Simple words, I am not taking five and six because difficult to draw for me. Definitely you can try and draw and analyze this. Now, now you might have got some idea why we need memoization here, correct? Because let's say now Fibonacci of two, let's say I have not put that if condition, like Fibonacci of two, then return something.

### 00:16:41 · Speaker 1

सो, लेट मी डिलीट, सॉरी, आई कांट डिलीट। वन सेकंड, लेट मी सेलेक्ट इट।

### 00:16:49 · Speaker 1

So Fibonacci of two again if you if I had not put the if condition it is Fib of one. Correct? Fib of one plus Fib of Fib of

### 00:17:03 · Speaker 1

So here fib I mean the function. Fib means the Fibonacci recursion function that I'm invoking. Okay? Fib of two is Fib of one plus Fib of zero. See here also you have Fib of one, correct? Here also you have Fib of one.

### 00:17:17 · Speaker 1

And when this tree extends, there are a lot of different scenarios where these values will repeat. And we unnecessarily calculate this again and again. So there has to be a way where we can eliminate this computation and and catch this, correct? So how we can do that, I'll show you. This is where memorization will come into picture. Why I gave a factorial example and not showing factorial example is factorial I already explained, that is something of homework for you. Write to write a memorization function for factorial. At the code in the comment section, I

### 00:17:47 · Speaker 1

always leave the code that is posted by the candidate uh the viewers. No matter how much I get I will streamline and do something on a daily basis and give my feedback. Please write a memorization code for the factorial and add it in the comment section. Okay? Now, what I'll do here is

### 00:18:03 · Speaker 1

So we need to catch the value, correct? As it's a recursion, the catch should be something that is passed every time, correct? Rest is very simple. You know it. If same how we did, if catch of number return catch of

### 00:18:18 · Speaker 1

cash of number. Correct? Then what we have to do somewhere the cash of num has to initialized. Here you are initializing it.

### 00:18:28 · Speaker 1

That's all. Very very simple. Just two lines of a code, normal function become a very optimized function, correct? This is about the explanation. Let me explain this again, okay? Now, if cache of num return cache of num, cache of num we are adding a value. First let us run and see we are getting the right value. I think let me try running ten. I think ten should be fifty five.

### 00:18:49 · Speaker 1

fifty five. So the code is working well. Basant, why you are not passing cash here? It is taking two arguments. In year six, I think you all know. I'm initializing this in default value of empty empty object in case if caller has not passed anything, okay? So cash is empty now. What we are doing is same. So whatever the value we got right here, the fib of two probably, we are caching it. Fib of one, we are caching it. Fib of three, we are caching. So whenever next time when fib of three comes, we don't do fib of two plus fib of one, again fib of one and fib of zero.

### 00:19:19 · Speaker 1

Fibonacci is already cash, just return that value. So this will save so much of a computation whenever you are doing a very big number Fibonacci. uh So this is this is about this video. uh To summarize all the things that we have discussed here, first thing, you need to know what is memoization definition. Simple memoization example like the add one which I showed. Slightly complex memoization example like the Fibonacci series I explained or the factorial homework that I gave you. You have to write a factorial homework, huh? Otherwise you will not master it because I have mastered this.

### 00:19:49 · Speaker 1

you have to you will master only when you try to attempt it. Write a factorial function without recursion. Sorry, without a memorization. Then try to add memorization layer on top of it. That is the right way of learning it. Write the code, make a gist or make a write a medium blog, get the link, put in the comment section or add the code itself as it's a small function. I'll validate the code and give my feedback whether this is right or not. Okay? I think that's all about this entire Fibonacci series. If you like the video, please like it on my YouTube channel, share the

### 00:20:19 · Speaker 1

video with your friends, let them also get benefited from this. Do not forget to comment if you like whatever I made, comment. If you not liked whatever I made, please comment. I think that as a positive feedback for me to improvise further. If you not subscribed to my channel, please subscribe. This code, I don't think any special code is here, but still I'll try to add this code into my GitHub repository and link in the description. Please copy the code and practice on your own. My medium handle is in description. Follow me on medium. Lot of beautiful articles I have written. In fact, the memorization I wrote this article almost an year back. Okay.

### 00:20:49 · Speaker 1

So many followers are there for that article as well. So you can read my medium articles also and like follow me on medium and star my GitHub projects as well. Thank you so much for watching. Catch you in next video.
