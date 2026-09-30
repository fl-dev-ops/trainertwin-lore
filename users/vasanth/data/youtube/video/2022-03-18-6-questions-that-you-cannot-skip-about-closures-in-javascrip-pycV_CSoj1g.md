---
id: pycV_CSoj1g
title: 6 Questions that you cannot skip about Closures in JavaScript Pt - 1 (closure
  Ep - 2)
date: '2022-03-18'
url: https://www.youtube.com/watch?v=pycV_CSoj1g
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Closure and nested functions in JavaScript - https://www.youtube.com/watch?v=6xU_VIDB-zw&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=11&t=26s\n\
  \nCounter dilemma in JavaScript - https://www.youtube.com/watch?v=nJhQRotbIis&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=15\n\
  \nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:07:39
model: saaras:v3
transcript: true
---

# 6 Questions that you cannot skip about Closures in JavaScript Pt - 1 (closure Ep - 2)

## Transcript

### 00:00:00 · Speaker 1

All, welcome to Uncommon Gigs. Myself, Fasant. I hope you all doing well. So today's topic is continuation of our previous video on closures. So in the previous videos, as you already know, we have discussed basics of closure, inner function, the classic counter dilemma with and how to solve it with the help of a closure.

### 00:00:15 · Speaker 1

And this video we'll be discussing some more questions on closure. Maybe this video and also one more video I'll be making. This video let us say we'll be discussing some easy questions on closure and next video we'll be discussing some advanced questions on closures, okay? My only request is if you have not seen my previous videos on closures, I'll be linking that somewhere on the screen also in the description. Please go ahead and watch it so that you you know the concept of closure then answering these questions will be very straightforward for you, okay? Without wasting further time, let's get started.

### 00:00:43 · Speaker 1

The question number one

### 00:00:46 · Speaker 1

very straightforward question. Okay? If you if you've seen my previous videos, you'll be definitely able to answer. But it is slightly a tricky one, not with respect to answer, but with respect to a topic. So, for those of you who know the answer to this question, mention question number one in comment section and put your answer. If you're not sure, then let me just give a quick walk through of the question. So we have created a function called init in line number two. And in line number three, we have created a variable name and initialize this to uncommon gig. This is my channel name. And in line number four, we have

### 00:01:16 · Speaker 1

created line number four to six we have created a function which logs the name. line number seven basically we are returning the function. this one sorry we are calling the function display name. so whenever you call the init a variable with a name name is initialized and inside that there is an inner function which is getting triggered. okay. so what my question is what the value of log here.

### 00:01:38 · Speaker 1

To be very precise, the value of name which is declared outside is accessible inside this or not. So if you know the answer at least now, please mention that in comment section. If not, let me execute it and show the answer for you.

### 00:01:51 · Speaker 1

The answer is uncommon geeks. So line number five, whatever you're printing is the uh this string is getting printed. So inside the function, the variable declared outside is able uh the the function which is display name which is an inner function is able to access the variable name which is declared outside of it. Okay? So just hold your thought if you're getting anything about this question. I'll I'll show you another similar question, then let us come back to this. Okay? So this is question number two.

### 00:02:17 · Speaker 1

These two questions are very similar, so I'll just show you once again. You only identify the difference, what is the difference between the two, okay?

### 00:02:25 · Speaker 1

I won't say right away. This is quick job for you to check what is the difference. So if you know the answer to this question also take a just mention question number two in comment section and put your answer. If not again let me give a quick walk through of the question. So line number two we have a function called make function and from line number twenty five we are triggering that function, okay? And inside which we have a variable called name, same, same as above and this display name is same as above. Line number twenty eight we are returning this display name which is due to which

### 00:02:55 · Speaker 1

in line number twenty six, we are invoking it. Okay? If you know the output, tell again, at least now mention that in comment section. Otherwise also it is the same. I mean,

### 00:03:04 · Speaker 1

I can execute and show it to you, but a precise question is the variable name which is declared in line number nineteen is able to is a function display name can access it or not? That's the question. Okay. Let me execute it for you. So we're getting uncommon gex. So both the program, both the question, question number one and question number two, the output is uncommon gex itself. I mean basically whatever was declared in line number nineteen can be accessed inside both the functions, both the questions. So then, where is the difference? Some of you might have already figured it out. For those of you who are still

### 00:03:34 · Speaker 1

not identified. See here we have a return statement here there is no return statement. From the outer function you're triggering the inner function but here from the outer function you're returning the inner function which here you're triggering. So make my function basically has a reference of display name which is getting triggered in line number twenty six. So this is the difference. So what one is returning so depending on returning there is another difference. So this is actually not a closure.

### 00:04:00 · Speaker 1

to very important to observe this is a lexical scope. Okay? There's a concept of lexical scope in JavaScript due to which whenever the display name is triggered from the inner function it is able to access the name. And then now question number two, this is a closure where you are returning a function from a function and that function has access to the variable declared in the outer function. This is a closure. So Vasanth what is the difference between lexical scope and the closure? See I have a quite limited time in my videos where this series is mainly dedicated for interview preparation. So I'll not be able to

### 00:04:30 · Speaker 1

explain that in depth. So this is the official URL of developer.mozilla.org where closures are explained. The first topic itself is lexical scoping. I'll link this URL in the description section of this video. Please go ahead and read it where they very clearly explain what is lexical scoping and what is the closure difference between them and how closure uses the lexical scoping. All those things are very clearly explained here. The intention of me picking this question is

### 00:04:55 · Speaker 1

You should not miss this in interview stating whenever there is a function inside a function everything is a closure nothing like that. So there is a difference between function and closure and the lexical scoping I want you to know that. That is the reason I pick these two questions. Okay? Let me quickly go to question number three.

### 00:05:14 · Speaker 1

So question number three is again a very straightforward question. If you have seen my previous videos, you will be able to answer it very easily. So if you know the answer,

### 00:05:24 · Speaker 1

Again, if you know the answer, mention question number three in comment section and put your answer. If not, let me just give a quick walk through of question. So, basically we have a function called make adder which is defined in line number thirty three. So, it takes an argument, okay? And whenever it takes an argument, it returns a function.

### 00:05:43 · Speaker 1

and that function is getting invoked in line number forty for add five. Add ten also the same thing happening in line number forty one. Okay. Question here remains the same. Basically whenever here whenever you whenever you invoke add five and pass two, obviously that will be acceptable here. But whenever that is happening, the x which is defined outside is acceptable inside or not, that is the question. Okay. So if you can solve that small piece, you'll be definitely able to answer this entire question.

### 00:06:11 · Speaker 1

So if you know the answer at least now, put that in comment section. If not, let me execute the question for you. So we're getting seven and twelve. Let me give a code walk through for you what is happening, okay? Or how we'll do a dry run. So here, in case of make adder five, you're passing five, so x becomes five here.

### 00:06:28 · Speaker 0

Okay

### 00:06:29 · Speaker 1

and it's returning this entire function which is getting assigned to addify. addify basically points to this function.

### 00:06:35 · Speaker 0

Okay

### 00:06:35 · Speaker 1

Now, whenever you invoke add five and pass two, so in this case, y becomes two.

### 00:06:42 · Speaker 1

So, and this inside this function block, x is already known due to the property of closure. So this outer function is returning an inner function. So all the properties of outer function are available inside the inner function. So due to which now this inner function knows the value of x. Inner function knows the value of y, so five plus two becomes seven. Same way if you pass ten into it will become twelve. That's it about this this particular question. Thank you so much for watching. If you would have liked my video, please do like it on my YouTube channel. If you want your

### 00:07:12 · Speaker 1

and also to get benefited, please do share the videos with them. Do not forget to subscribe to Uncommon Geeks, please subscribe to Uncommon Geeks. And I will be linking my GitHub URL where all these questions are being added, so you can download that project and practice on your own. I've also linked my medium blog in the description where I've written articles on various different JavaScript topics, you can go ahead and read that as well, okay? Thank you, thank you so much again for watching the video. Catch you in my next video.
