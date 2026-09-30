---
id: nJhQRotbIis
title: Counter dilemma In JavaScript (Closure Ep - 1)
date: '2022-03-06'
url: https://www.youtube.com/watch?v=nJhQRotbIis
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Closure which is a part of JavaScript functions is again a tricky javaScript interview\
  \ topic. In this series we are not discussing arrow functions as mixing of arrow\
  \ functions and normal function may create lot of confusion among viewers. Watch\
  \ all videos of mine on closure and you will definitely answer questions on this\
  \ topic in upcoming interviews. \n\n\nMy Medium Blogs - https://mevasanth.medium.com/\
  \ \nGithub URL which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:09:48
model: saaras:v3
transcript: true
---

# Counter dilemma In JavaScript (Closure Ep - 1)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome to Uncommon Geeks, myself Hasanth. I hope you all doing well. So today's topic is closure. You already know I've explained closure in brief and also the function nesting. I intentionally taking closure separately than the normal function because closure itself is a very tricky topic and lot of questions on this topic can be asked in the interview. So today's topic what I'm covering is a classic problem, it's called counter dilemma. It it will be generally asked in most of the interview. The the main reason why this question has become very important is because how many different

### 00:00:30 · Speaker 1

different approaches that you can come up for a given problem. And how do we write the optimal approach? Though the problem is very simple, solution is not that straightforward, okay? Without wasting further time, let's get started.

### 00:00:42 · Speaker 1

So, we we have uh problem is very simple. I'll explain the problem. So all you have to do is uh there should be a function. Whenever you invoke the function, whatever the previous value of the count it was holding, that should get incremented. Let's say first counter was zero, then next time when you call it should print one, next it should print two, next it should print three. Just to show you here, function add, okay? Let's say I call add once. Okay? And this add function has a

### 00:01:12 · Speaker 1

log statement which will print count. Okay? I know count is not initialized, just I am explaining you how it is gonna look like. Okay? And if you call it three times, expected output is first time it should show one, second time it should show it should show two, third time it should be showing three and it goes on. That is the what the expectation is. Okay? So, in case if you're already from a JavaScript background and you know how you have already worked on different projects, your approach will be very first approach will be at least this. Okay?

### 00:01:42 · Speaker 1

where you do this, you will create a variable called let count and initialize it to zero, okay? Then what you do is inside the add, you will be doing this, count is equal to count plus one, okay?

### 00:01:55 · Speaker 1

then you will log the count, okay? And you invoke the add three times. Let's see how it comes. So one, two, three. This is quite straightforward and the easiest approach to solve this problem. Well, the main problem of this solution is, uh the let count, whatever you have declared, it's a global scope, okay? So everyone, not just the function add, which is on line number two, any function uh in in the scope will be able to access the count and it can update or modify the value, correct? So the problem with this approach is you will not have a dedicated uh

### 00:02:25 · Speaker 1

value of count. So this is something that is okay to during the interview if they're looking for a junior level they may accept this answer but it is not for a pro. Okay? Pro level or advanced level engineer they're looking definitely this is not the solution. Okay? Now then what is the solution? uh another approach after you since I've already explained the closure and the function testing another approach which you might think of is this.

### 00:02:49 · Speaker 1

where you will be using a function nesting, okay? How is this?

### 00:02:59 · Speaker 1

or before function nesting people would think another approach that also I will show you before going to function nesting okay let count is equal to zero count is equal to count plus one okay then log count okay and you will call the add

### 00:03:18 · Speaker 1

three times, okay? uh this looks like it will work and many juniors and the mid-level people will write this code also. So expectation is it will do the same but I'll let me run and show it to you. Always you are getting one one one here. Okay, people with a mid-length senior level will not make this mistake, but just for the purpose of those who might make a mistake, I'm showing this example. So you're thinking the value of count is retained in this block and when every time whenever you invoke, whatever the value with which it it was in last year, it get incremented.

### 00:03:48 · Speaker 1

doesn't work like that. Because this is a function, every time when you invoke the function, it's a new instance of the function. If you know how JavaScript engine works, you will you will know this very well. So every time when you invoke, count value will be zero and three times you invoke the add and all the time the count will start with zero and it will be incremented by one. Okay? So this is the this is the problem. So this solution doesn't work. So don't don't write this. Now I'll go to the next approach which is of a inner function. Okay? Or what we also call a closure. This is actually the expected answer. I'll tell you how to write this. In case

### 00:04:18 · Speaker 1

if some of you already know this counter dilemma problem and you know the answer also, please do mention counter dilemma in the comment section and put your code. If I I can validate it and I can also revert back to your comment, okay? Let's I'll I'll quickly write the code. How we do is this.

### 00:04:33 · Speaker 1

I'll let a inner function called add, okay? Then what I'll do, I'll create a outer, I mean I'll create a variable called counter, okay? And I'll initialize it to a value of zero. And what I will do is from the outer function that is test, I will return add, which is a inner function, okay? Then what I will do is...

### 00:04:59 · Speaker 1

const output is equals to test. Okay? And now output basically refers points to this add function. Okay? Then what I'll do is log

### 00:05:13 · Speaker 1

output. Okay.

### 00:05:17 · Speaker 1

Let me write the code and I'll I'll do a detailed walk through as well, okay? Then what I'll do here is count is equals to count plus one

### 00:05:28 · Speaker 1

then I will return the count.

### 00:05:32 · Speaker 1

Okay. Let me not execute it. I'll tell what is happening first. So we we have a function called test now, okay? Test function returns a function called add. That's the first and simplest one. Now add is actually a reference. uh I mean whenever we do return add, this will point to this function. What we are doing, we are assigning that to a variable which will have actually function reference and we we are invoking that function three times. So inside this add function what we are doing is whatever the count that was present outside the function, we can access that inside the function as well due to

### 00:06:02 · Speaker 1

property of closure. All the values which are outside the function can be also outside inside the function due to property of closure. That's itself the definition of closure as you already know.

### 00:06:13 · Speaker 1

So what we are doing is we are incrementing the counter then we are returning the counter. So first time you invoke it, okay? And as soon as you invoke the test, add is returned, okay? Then this whatever the let count is equal to zero you have, that is something that is enclosed in the function add, okay? So now add knows there is a variable called count, no matter whether outer function is still executing or it done execution. There are something like self invoking function. You already know that. So if this outer function or self invoking function which has no life, still the inner function will

### 00:06:43 · Speaker 1

have access to that whatever the initial value that the during the initial whenever this function got initialized right what value it had at that time that value will be stored inside this block okay now whenever first time whenever you invoke it add was zero we increment I mean count was zero we increment it by one then we are returning the count okay so we are seeing first output here it will be one next time you invoke it counter value doesn't change I mean I mean it doesn't get initialized to zero again the reason being it doesn't have a count of its own it is taking

### 00:07:13 · Speaker 1

it from the outer scope. So now count will become next time whenever you invoke it will be one, one plus one becomes two. Again when you invoke count will be two. Two plus one will become three and it can goes on. Let me run this code for you. So getting one two three. Okay. So this is this is how you can actually this is the expectation from the interview, okay, where whenever they ask you counter dilemma problem, this is the solution they expect. There is another solution where see if you look at it, we have created a function called test, which is an outer function except initializing the value of count it has no nothing to do

### 00:07:48 · Speaker 1

So this this is still a not optimal solution because whenever you're creating a function called test, it will going to be persistent throughout the uh JavaScript execution of this file. Actually we don't need this except this initialization. So rather using the test, we can also use a self invoking function. So that is something homework I'm giving. You just read it somewhere and try to add that in comment section and I'll approve or I'll tell if it is a right or wrong, okay? I'll also want to show you from where I picked this problem, okay? This is a very common problem but actually it is taken

### 00:08:18 · Speaker 1

develop this one W3 schools okay W3 school if you go to the function closure you will be seeing this okay a counter dilemma a standard problem but preferably or mainly this is taken most of people have got this idea only from this documentation I'm showing this documentation as you know I have a habit of showing all the official documentation the reason being if you go and try to read this you may get some more interesting topics for example now function definition function parameters

### 00:08:48 · Speaker 1

location, call apply bind. So you may get an idea of all those things due to which I'll I'll generally show the official documentation itself. Okay. That's all about this video. Okay. So just to quickly summarize, this is a this this video was dedicated to closure.

### 00:09:03 · Speaker 1

and a classic counter dilemma, how you resolve it, okay? Thank you so much for watching my video. If you like my video, please do like it on YouTube channel. Do not forget to subscribe to my channel. If you like, if you like our video and if you also want our friends, your friends to get benefited out of it, please do share it with them. And if you want to make, if you want me to make a video on a particular topic, please do mention that in comment section. I'll be more than happy to make videos on the topic that you have requested. And I'll be linking my medium blogs on closure. I'll also link

### 00:09:33 · Speaker 1

my github urls github projects where I have added these example problems. even follow me on medium and download those github repository and practice on your own. okay? thank you so much for watching catch you in next video.
