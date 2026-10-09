---
id: -PDQA3Q5w2E
title: JavaScript Pure Functions are not that easy (Pure Functions Ep - 1)
url: https://www.youtube.com/watch?v=-PDQA3Q5w2E
date: '2022-02-26'
duration: 00:07:54
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# JavaScript Pure Functions are not that easy (Pure Functions Ep - 1)


## Transcript

### 00:00:01 · Speaker 1

Hello all, welcome to Uncommon Geeks, myself Fasent. I hope you all are doing well. Today's topic is pure functions. Pure function is considered to be one of the fundamental topic of all the programming language, same as JavaScript. Due to its simplicity, many candidates tend to ignore this topic during the interview preparation. It's a fact that pure functions are straightforward, but there can be small variations of pure function that can be created that candidate tend to confuse during the interview and they'll not be able to answer it.

### 00:00:31 · Speaker 1

this problem I pick the pure functions in my series and I'll be asking you all the possible questions that can be asked in the interview and how easily you can tackle it. I'll guarantee you you'll be thrilled to know the variation of pure functions that can be formed whether you are a beginner or a candidate who to take an interview and were unable to answer pure functions you'll definitely enjoy this video series. Thank you so much for watching let's get started.

### 00:00:58 · Speaker 2

Let us understand what are pure functions with a simple example

### 00:01:02 · Speaker 2

So let me create a function function area of a rectangle it takes two arguments length and width

### 00:01:14 · Speaker 2

So what it returns is

### 00:01:17 · Speaker 2

length star width okay so basically quite straightforward whoever has read the geometry are fundamentally aware of this concept where area of a rectangle is length into width or breadth okay so now i'll call this function from the outside so i'll insert a log statement itself so area of rectangle i'm passing 10 into 20 okay so let's see what is the output there is nothing fancy here you will get 220 tensi is

### 00:01:47 · Speaker 2

200 20 into 10 is 200 so you're getting 200 okay so no matter how many time you invoke the function with passing the same set of arguments so you're getting same value as output okay if you change the value so 30 into 40 40 30 obviously the values are gonna change okay so but for the same given set of values the function will always return same value so no matter

### 00:02:17 · Speaker 2

many times you in call the area of rectangle with 10 and 20 you're always going to get the same same area okay so pure functions in very simple words we can tell this are those function

### 00:02:33 · Speaker 2

Those functions

### 00:02:35 · Speaker 2

that are deterministic in nature okay so these are the functions where you you can you can be so sure if i call this function this is the output that i'm gonna get so that's about the pure functions okay so the concept is same concept is straightforward you call a function and you anticipate an output and you always get the same output those are the pure functions in fact this is not specific to javascript in all the programming languages pure functions mean the same where

### 00:03:05 · Speaker 2

For those functions that are deterministic, where if you pass the same set of values, you're always gonna get the same set of values. So always you're gonna return the same set of outputs. Those are called as pure functions. Okay. So now there are, obviously there is an opposite type to this. And they are called impure functions. And some places they are also called as not pure functions. Okay. Now both the terms exist in the industry. People refer both. Okay. Let's see impure or the not pure functions.

### 00:03:35 · Speaker 2

uh let us uh stick to some let's make it some test function ms test because we no longer calculate the area of our rectangle i'm making it test you pass the length and width okay what i'm doing here is const temp i'm creating a temporary variable what i'm doing here is i'm creating a mathematical math.random a random variable basically okay and i'm doing math.floor i'll explain why i'm doing that in a while

### 00:04:07 · Speaker 2

And let me know the same test again okay and what I'm doing is along with the length and breadth I'll also start the temp

### 00:04:17 · Speaker 2

So let me call the same function again

### 00:04:20 · Speaker 2

Maybe let's call test where I'll pass 10 and 20

### 00:04:27 · Speaker 2

Let me execute this

### 00:04:29 · Speaker 2

So we're getting zero okay I'm executing this again

### 00:04:34 · Speaker 2

getting zero two times so what might be happening is uh temporary variable whatever is getting generated uh maybe let's multiply by 10 so that we get some higher number okay so basically what's happening here is uh before seeing the output let me explain the block of code whatever i've written so math dot random will generate a random number generally that number or by default that number will be in some decimals okay so 0.5 0.6 0.4 something like that so i'm just imagining

### 00:05:04 · Speaker 2

multiplying it into 10 so that it becomes a slightly a bigger number so 0.8 means it becomes 8 8.4 or something then I'm doing a math.floor here math.floor and math.seal you might be already aware what it does is it will increase the value or decrease the value so for example if you have a value like 0.4 math.floor okay let's make it 1.4 math.floor if you pass this inside math.floor it will become 1 if you if you pass it inside math.seal

### 00:05:34 · Speaker 2

as you notice to the top it will become 2. So, this is what the math.floor and math.ceil functions do. I am just using this because we get the whole number rather having the points in the decimals. So, you are invoking now and now we are invoking the same function twice here. Same arguments are getting passed. Let us see the output. So, once we got 1800, second time we are getting 1000. If I call third time again,

### 00:06:00 · Speaker 2

So I'm getting a different value, 1000, 1000, 1000, 400. So basically what's happening is 20 into 10 is same. In all the cases, length and length into width, that 20 into 10 is happening same. But the output that we are getting is different because of this temporary variable. So now you yourself know impure functions, impure functions, those functions that are non-deterministic in nature. Okay. So you will not be able to predict the output from a given function. If you're invoking it, you're not sure what value you're going to get. It always varies.

### 00:06:30 · Speaker 2

Okay, so this this example looks vague. Who is going to do like this? This example is something that may not exist all the time Okay, in industry we may not get such kind of example But think in in this way where you have some network call that you are making Okay, so depending on what type of data you're getting sometimes you may not get a data Sometimes you may get a data and depending on the type of data you're getting you're gonna you are you will be rendering it So those are the actions that are non-deterministic. So you're not sure Let's say for example user X will get some set of data user Y will get some set of

### 00:07:00 · Speaker 2

data so whatever the data that you are getting may vary okay or user x may not get same set of data all the time so depending on his location he may get some offers and some location he may not get okay so what is the what will be returned from a function is non-deterministic okay so this is a very important concept uh that is the reason i'm touching it here and there could be a lot of very interesting questions that can be asked in this simple concept this looks very straightforward and very simple but slightly tweaking it will make it a very complicated during the interview so those questions i

### 00:07:30 · Speaker 2

discussing in next video if you have liked my video please like it and if you if you if you want your friends also to learn from this video please share it with them also subscribe to our channel and in case you want me to make video on a particular topic please do mention that in the comment section i'll make a video on that catch you in next video with very interesting questions on pure and impure functions thank you all

