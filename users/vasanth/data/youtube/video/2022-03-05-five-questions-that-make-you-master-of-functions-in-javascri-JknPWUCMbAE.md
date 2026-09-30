---
id: JknPWUCMbAE
title: Five questions that make you master of functions in JavaScript Pt -2 (Functions
  Ep - 4)
date: '2022-03-05'
url: https://www.youtube.com/watch?v=JknPWUCMbAE
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ If you know how to call functions and what it returns, you can clear half of JavaScript\
  \ interviews. \n\nJavaScript functions could be the topic, on which most interview\
  \ questions can be formed. Because it contains other subtopics like closure, currying,\
  \ nesting of functions etc. Most tricky questions can be easily formed in this topic.\
  \ I will cover each and every topic of functions in this series, watch it carefully\
  \ and practice well, you will definitely answer all questions on this topic in upcoming\
  \ interviews\n\n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which\
  \ contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nNormal\
  \ Function Part 1: https://www.youtube.com/watch?v=VaL5lrxX-kY&t=3s \nNormal Function\
  \ Part 2 : https://www.youtube.com/watch?v=6xU_VIDB-zw\nNormal Function Part 3 :\
  \ https://www.youtube.com/watch?v=zrSg1kVEc9U"
author: careerwithvasanth
duration: 00:06:36
model: saaras:v3
transcript: true
---

# Five questions that make you master of functions in JavaScript Pt -2 (Functions Ep - 4)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome to Uncommon Gigs. Myself Vasant. I hope you all doing well. As you know this is my continuation of video on where I where we are discussing the function. We have already created close to completed close to three videos where all the fundamentals of function are discussed. And we also spent one video where I've already explained some question and answers. This is a part two of the question and answer. This is quite a short video. I have only two questions to discuss, okay? Without wasting further time, let's get started. Only one thing, if you have not watched my previous videos, I would highly advise please go ahead and watch it because without

### 00:00:30 · Speaker 1

watching that if you straight away come to this video now you will face a difficulty in understanding the topics. Okay? I will try to link somewhere on the screen those links to those videos also in the description. Please go ahead and watch it. Okay? Now

### 00:00:41 · Speaker 1

We have a function. So my question, first question is this, question number four. I'm putting question number four because already three questions are discussed in the past video, okay? So this video we are discussing question number four. So we have a function called add square. For those of you who want to glance at a question, pause the video, glance at the question, okay? And copy the question from my GitHub URL and read through it. And if you know the answer, mention question number four, put your answer in comment section. I'll validate it. If it is right, I'll tell you it is right, okay? Otherwise, obviously you can watch the video.

### 00:01:11 · Speaker 1

For those of you who's still struggling, I'll just give a walk through of the function or question. So we have a function called add square which is an outer function. We have a function called square which is an inner function. And in the line number seven, what we are doing is we are return outer function is returning inner function but not once but twice. I don't say it's returning twice, basically it is performing some options operations in the inner function and it returning the value, okay? It's not that difficult actually, but just because of the array

### 00:01:41 · Speaker 1

arrangement of the the question or the different entities inside a function it it looks little tricky okay now if you know the answer again you can mention the question in the comment section and put your answer still if you are not sure let me walk through step by step okay so yeah let me do this

### 00:02:00 · Speaker 1

sometimes it works if you're not using the strict mode, right? You don't have to declare a variable. So otherwise, let us better to declare. I mean, with const where or let. Now, what is happening here is here you are calling a function called add square. So whenever you invoke this, A becomes two, correct? Then B becomes three. And you have a what it does is it will return square of A. Square of A means first time it is two. Two star two, so it will become four, correct? Next, you invoke B.

### 00:02:30 · Speaker 1

which is three. So here it will be three star three which is nine. Correct? So it will be nine. Here.

### 00:02:40 · Speaker 1

So nine plus four it will become thirteen. Correct? So I'll walk through again the on the example. So for another example so we have add square three comma four. Whenever you invoke this function A becomes three. B becomes

### 00:02:55 · Speaker 1

फोर, ओके? एंड यू इन्वोक्ड स्क्वेयर ऑफ थ्री, दैट इज नाइन, ओके? स्क्वेयर ऑफ फोर, व्हिच इज सिक्सटीन.

### 00:03:04 · Speaker 1

So sixteen plus nine is twenty five. Correct? So this is how the execution is happening. The reason why I explained to you like this is in case if you are someone who's preparing for interviews of these Fang companies. Nowadays now it is Mang companies which funds for which stands for Meta, Amazon, Apple, Netflix and Google. So those are the companies who doesn't give you an editor like this which is which can run the program to write your code. They try to ask you to write a code in Word or Google Docs etc.

### 00:03:34 · Speaker 1

etcetera, where there is no compilation engine. You have to predict what the output comes and you have to explain it to them. You have to do a dry run. So this is how you will do a dry run. I wanted to show that to you. So I showed that in this video. So now let me run this and show what is the output.

### 00:03:50 · Speaker 1

So thirteen twenty five and forty one you already know this. So where two square plus three square is thirteen. Three three square plus four square is twenty five. Four square plus five square is forty one. Straightforward. Correct? So now let us go to the next question.

### 00:04:06 · Speaker 1

This looks very tricky, huh, this question. Actually, it is a very straightforward question, but just because of the align arrangement of this different function calls, it becomes quite tricky to guess the output. So, if you're someone who know the answer, already mention question number five and put answer, or if in the comment section, or you want sometime to analyze it, so go to my GitHub repository, copy the question, analyze the question, then also you can mention your answer in comment section, okay? If you are someone who is struggling, let me explain it to you. So, we have basically we have three nesting.

### 00:04:36 · Speaker 1

function A, function B and function C. I explained in the first video like I have never gone to extent in in my experience to a third level of inner function nesting. But here it's something that is happening. So interview obviously they will ask you some question which you might not be doing on a day to day basis, okay? So what is happening here is you are invoking a function A and you are passing one. So X becomes one.

### 00:04:58 · Speaker 1

Then inside this block of A in line number twenty eight you are invoking B because that is the only statement that you have written for the function A. So B you are passing to so Y becomes

### 00:05:11 · Speaker 1

two. Correct? Then inside the function B, what you are doing is you are calling C. So Z becomes three.

### 00:05:20 · Speaker 1

console.log x plus y plus z you already know what is closure. So inner function will have access to the outer function, correct? So one plus two plus three which will become three plus two is five, y plus one is six, correct? So this this is a combination of closure, function nesting

### 00:05:37 · Speaker 1

those two properties basically. Okay, let me run this and let me remove this.

### 00:05:43 · Speaker 1

remove this

### 00:05:46 · Speaker 1

this

### 00:05:50 · Speaker 1

we got six. The same we have explained. Now you know the inner function, the basics of closure and some fundamental properties of function with respect to hosting, name how named function was, how anonymous function work, correct? You also know how to do a dry run and explain that in the interview, correct? So, thank you so much for watching my video. Please do like it on YouTube if you like my video, share it with your friends if you want them also to get benefited. Do not forget to subscribe to my channel Uncommon Geeks. I will link my medium blog where I've written lot of articles.

### 00:06:20 · Speaker 1

on JavaScript and React, please do follow me on Medium. I will link my GitHub URL, where I've created these projects for the this Q and A. Copy those questions from there and answer and do not forget to subscribe me on GitHub as well. Thank you so much for watching. Catch you next video.
