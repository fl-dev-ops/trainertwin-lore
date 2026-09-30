---
id: -PDQA3Q5w2E
title: JavaScript Pure Functions are not that easy (Pure Functions Ep - 1)
date: '2022-02-26'
url: https://www.youtube.com/watch?v=-PDQA3Q5w2E
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Pure functions in JavaScript are one of the most ignored interview topic. It looks\
  \ very easy. So, Many candidates tend to ignore this topic. But Pure functions are\
  \ not as easy as you think. Watch both of my video's on pure functions and you will\
  \ definitely realise it.\n\n\nMy Medium Blogs - https://mevasanth.medium.com/ \n\
  Github URL which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:07:54
model: saaras:v3
transcript: true
---

# JavaScript Pure Functions are not that easy (Pure Functions Ep - 1)

## Transcript

### 00:00:01 · Speaker 1

हेलो ऑल, वेलकम टू अनकॉमन गीक्स, मैंसेल्फ वसंत। आई होप यू ऑल डूइंग वेल। टुडेज़़ टॉपिक इज़ प्योर फंक्शन्स।

### 00:00:09 · Speaker 1

pure function is considered to be one of the fundamental topic of all the programming language. same as javascript. due to its simplicity many candidates tend to ignore this topic during the interview preparation. it's a fact that pure functions are straightforward. but there can be small variations of pure function that can be created that candidate tend to confuse during the interview and they'll not be able to answer it. so to solve this problem i'm i've picked the pure functions in my series and i'll be asking you all the possible questions that can be asked in the interview and how easily

### 00:00:39 · Speaker 1

you can tackle it. I'll guarantee you. You'll be thrilled to know the variation of U functions that can be formed.

### 00:00:46 · Speaker 1

whether you are a beginner or a candidate who would take an interview and were unable to answer pure function.

### 00:00:51 · Speaker 0

functions, you'll definitely enjoy this video series. Thank you so much for watching. Let's get started.

### 00:00:57 · Speaker 1

Let us understand what are pure functions with a simple example. Okay? So let me create a function, function area of uh rectangle. It takes two arguments, length and width. Okay? So what it returns is...

### 00:01:17 · Speaker 1

length star width. Okay? So basically quite straightforward. Whoever has read the geometry are fundamentally aware of this concept where area of a rectangle is length into width or breadth. Okay? So now I'll call this function from the outside. So I'll insert a log statement itself. So area of rectangle I'm passing ten into twenty. Okay? So let's see what is the output. There is nothing fancy here. You would get two hundred twenty tensize.

### 00:01:47 · Speaker 1

is two hundred. Twenty into ten is two hundred. So you're getting two hundred. Okay. So no matter how many time you invoke the function.

### 00:01:55 · Speaker 1

with passing the same set of arguments. So you're getting same value as output. Okay. If you change the value, so thirty into forty, forty, thirty, obviously the values are gonna change. Okay. So but for the same given set of values, the function will always return same value. So no matter how many times you invoke in call the area of rectangle with ten and twenty, you're always gonna get the same same area. Okay. So pure functions in very simple words, we can tell are those functions

### 00:02:33 · Speaker 1

those functions

### 00:02:35 · Speaker 1

that are deterministic in nature. Okay? So these are the functions where you you can you can be so sure if I call this function, this is the output that I'm gonna get. So that's about the pure functions. Okay? So the concept is same, concept is straightforward, you call a function and you anticipate an output and you always get the same output. Those are the pure functions. In fact, this is not specific to JavaScript, in all the programming languages, pure functions mean the same, where

### 00:03:05 · Speaker 1

for those functions that are deterministic where if you pass the same set of values you're always gonna get the same set of values. always you're gonna return the same set of outputs. those are called as pure functions. okay? so now there are obviously there is an opposite type to this. and they are called impure functions and some places they are also called as not pure functions. okay? both both the terms are exist in the industry people refer both. okay? let's see impure or the not pure functions.

### 00:03:35 · Speaker 1

let us stick to some let's make it some test function named as test because we no longer calculate the area of of our rectangle. I'm making it test you pass the length and width okay. What I'm doing here is const

### 00:03:50 · Speaker 1

temp, I'm creating a temporary variable. What I'm doing here is I'm creating a mathematical math.random, a random variable basically, okay? And I'm doing math.floor, I'll explain why I'm doing that in a while, okay?

### 00:04:07 · Speaker 1

and let me invoke the same test again, okay? And what I'm doing is along with length and breadth, I'll also start the temp, okay? So let me call the same function again, uh maybe let's call test where I'll pass ten and twenty, okay?

### 00:04:26 · Speaker 1

Let me execute this.

### 00:04:29 · Speaker 1

So we're getting zero. Okay. I'm executing this again.

### 00:04:34 · Speaker 1

we're getting zero two times. So what might be happening is, uh temporary variable whatever is getting generated, uh maybe let's

### 00:04:43 · Speaker 0

Statue

### 00:04:44 · Speaker 1

multiply by ten so that we get some higher number. Okay. So basically what's happening here is, uh, before seeing the output, let me explain the block code whatever I've written. So math.random will generate a random number. Generally that number or by default that number will be in some decimals. Okay, so point five, point six, point four, something like that. So I'm just multiplying it into ten so that it becomes a slightly a bigger number. So point eight means it becomes eight, eight point four or something. Then I'm doing a math.floor here. Math.floor

### 00:05:14 · Speaker 1

floor and math.ceil you might be already aware. What it does is it will increase the value or decrease the value. So for example, if you have a value like 0.4, math.floor, okay, let's make it 1.4. math.floor if you pass this inside math.floor, it will become one. If you if if you pass it inside math.ceil, ceil means as you know it's the top, it will become two. So this is what the math.floor and math.ceil functions do. I'm just using this because we we get the whole number rather having the

### 00:05:44 · Speaker 1

points in the decimals, okay? So you are invoking now, now we are invoking the same function twice here. Same arguments are getting passed, let's see the output. So once we got thousand eight hundred, second time we are getting thousand. If I call third time again,

### 00:05:59 · Speaker 1

Okay. So I'm getting a different value, thousand, thousand eight hundred, thousand four hundred. So basically what's happening is twenty into ten is same. In all the cases length and length into width, the twenty into ten is happening same, but the output that we are getting is different because of this temporary variable. So now you yourself know impure functions.

### 00:06:18 · Speaker 1

impure functions, those functions that are non-deterministic in nature. Okay? So you will not be able to predict the output from a given function. If you are invoking it, you are not sure what value you are going to get. It always varies. Okay? So this this example looks vague. Who is going to do like this? This example is something that may not exist all the time. Okay? In industry, we may not get such kind of example. But think in in this way where you have some network call that you are making. Okay? So depending on what type of data you are getting, sometimes you may not

### 00:06:48 · Speaker 1

data sometimes you may get a data and depending on the type of data you're getting you're gonna you you will be rendering it. So those are the actions that are non deterministic. So you are not sure. Let's say for example user X will get some set of data. User Y will get some set of data. So whatever the data that you are getting may vary. Okay? Or user X may not get same set of data all the time. So depending on his location he may get some offers and some location he may not get. Okay? So what is the what will be returned from a function is non deterministic. Okay? So this is a very important concept.

### 00:07:18 · Speaker 1

that is the reason I'm touching it here. And there could be a lot of very interesting questions that can be asked from this simple concept. This looks very straightforward and very simple, but slightly tweaking it will make it a very complicated during the interview. So those questions I'll be discussing in next video. If you have liked my video, please like it and if you if you if you want your friends also to learn from this video, please share it with them. Also subscribe to our channel. And in case you want me to make video on a particular topic, please do mention that in the comment section.

### 00:07:48 · Speaker 1

make a video on that. Catch you in next video with very interesting questions on pure and impure functions. Thank you all.
