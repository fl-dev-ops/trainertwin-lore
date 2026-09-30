---
id: ihyet-lq9bE
title: I bet, you don’t know about JavaScript’s pure functions (Pure functions Ep
  - 2)
date: '2022-02-26'
url: https://www.youtube.com/watch?v=ihyet-lq9bE
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Pure functions in JavaScript are one of the most ignored interview topic. It looks\
  \ very easy. So, Many candidates tend to ignore this topic. But Pure functions are\
  \ not as easy as you think. Watch both of my video's on pure functions and you will\
  \ definitely realise it.\n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub\
  \ URL which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nPure\
  \ functions part 1 - https://youtu.be/-PDQA3Q5w2E"
author: careerwithvasanth
duration: 00:11:42
model: saaras:v3
transcript: true
---

# I bet, you don’t know about JavaScript’s pure functions (Pure functions Ep - 2)

## Transcript

### 00:00:00 · Speaker 1

back to Uncommon Geek. Myself Vasant. So in this video, it's an extension of my previous video on pure functions, where we'll be mainly discussing what are the questions on pure function that can be asked in the interview and how to approach it. Okay? So as I said this this topic is quite straightforward, looks very easy, but actually it is not. There could be very fancy question that can be asked around it and you get confused during the interview time and you'll not be able to answer it. Okay? So due to which I picked this topic and let's get started. So the first question

### 00:00:30 · Speaker 1

is on around console.log. So what is console.log? So in programming constraints, is it a keyword, is it a function, is it a class, what it is?

### 00:00:39 · Speaker 1

So almost you'll be using it day in and day out if you're a JavaScript or a content developer where to for either for debugging or either for logging something on the screen. So you'll be somewhere or the other you'll be using it every day. But most if I won't say most but many will not know actually what is console dot log in with respect to programming constraints.

### 00:00:59 · Speaker 1

So interviewer might ask you this question as well to understand how strong you are at fundamentals. uh basically console dot log this first question. uh you can you can mention the question number and answer that in the comment section if you already aware of it. Basically console dot log is a function. Okay? So anything basically in JavaScript starts with uh parenthesis and ends with a parenthesis is a function. Okay? So in our case question number one this is a function. Now let's slightly extend this.

### 00:01:26 · Speaker 1

you know this is a function. Second question around the same snippet, is it a pure function or not?

### 00:01:33 · Speaker 1

Okay. Tell me whether it's a pure function or not. If you know, just take the video video timing and answer your answer in the comment section. So to answer to that question, we should know what the function is returning, correct? Without that we'll not be able to tell whether it's a pure function or not.

### 00:01:48 · Speaker 1

So to understand what it is returning, let's say less output is equals to hello world, then again I'm logging

### 00:01:59 · Speaker 1

output is

### 00:02:01 · Speaker 1

output. Okay?

### 00:02:04 · Speaker 1

If I run the code, okay? So we are getting hello world and output is undefined, okay? So what is happening? uh This got printed first, then whatever the return value of this function that got assigned to output and we are printing it. So what if I increase the number of characters in this? So...

### 00:02:24 · Speaker 1

hello world let us make it like welcome to uncommon geek okay so now if I run this code still I'm getting undefined here leave this part so here still I'm getting undefined so put in simple putting it in very simple terms no matter

### 00:02:42 · Speaker 1

What is the number of characters printed inside the console.log or because of console.log? Console.log as a function always returns undefined. So if it is always returning undefined, then what type of function it is? It's a deterministic function. So we are always expecting the same value and we are getting the same value. So console.log is a pure function. Okay? You might be using it day in and day out, but day in and day out, but most of you may not know it's a pure function. Or if suddenly asked in the interview, you will get confused and

### 00:03:12 · Speaker 1

not be able to answer it. So please do note it down as like I said I may add all these things into a GitHub repository and post it there for your practice, okay? Let's go to the second question.

### 00:03:23 · Speaker 1

slight deviation of the first question and area of rectangle.

### 00:03:28 · Speaker 1

Now deviation of first question, if you have already discussed this in our previous video on pure functions, where same area of rectangle function, uh I had created and passed the length and breadth and I am returning the value, returning the area, okay? So, now let me ask you the same question, is it a pure function?

### 00:03:45 · Speaker 1

If you know the answer, please do mention that in comment, question number two and your answer. Okay? If not, listen to me. So, I am saying this is not a pure function.

### 00:03:55 · Speaker 1

Now you'll ask, Vasant, why? This is a pure function because no matter how many times I pass the same value to this function, I always and always get back the same same return. Four into two is eight. Okay?

### 00:04:07 · Speaker 1

Why it is an impure function or why it's not a pure function? The answer is pretty straightforward. So line number twenty six you have a statement called console.log. He is the culprit. Why console.log will make this an impure function I'll tell you.

### 00:04:21 · Speaker 1

So you are trying to invoke a function inside a function. Okay? So this we call side effect. Basically not exactly this this is not exactly called a side effect. Basically inside a given block you are trying to alter a value or you are trying to invoke a function.

### 00:04:35 · Speaker 1

which will cause some effect outside the block basically. In very simple words that is side effect. I will try to make a video especially on specifically on side effect in upcoming videos. For sake of this video you stick to a concept like side effect means

### 00:04:48 · Speaker 1

a function or a given block is causing some effects outside its scope. That's called side effect, okay? So now area of rectangle you're invoking console.log function and this console.log as you already know, this is this definition exists somewhere in the JavaScript engine how to I mean some like some library knows how to execute console.log. So we are invoking a function inside a block, the problem with this is what happens is you are invoking a function and you don't own that function, someone can change the definition, so rather printing area is something. it may don't do anything

### 00:05:21 · Speaker 1

you don't know because when you whenever you are writing a very bigger project there will be multiple teams involved and you are trying to invoke a function from another team and another team decides to change the definition of it. So your program is your function whatever you have written is no longer deterministic because it depends on some other function. Okay? So as soon as you write a console dot log inside area of rectangle this becomes undeterministic or indeterministic. So this is an impure function now. Okay?

### 00:05:48 · Speaker 1

So, uh why do interviewer ask this question? You might be thinking.

### 00:05:52 · Speaker 1

So it is not on this is not going to change the way you work day to day. But thing is you know pure functions but are you able to imply it or are you able to derive some value out of it by applying it to a given block. So this is the same quality that I would expect from any engineer. So you know a concept so given an example or given a problem you must be able to apply to it. That's the reason these questions will be asked during the interview. Okay.

### 00:06:15 · Speaker 1

Next let's go to the third block, the third question. Okay? So, the question remains same. Okay?

### 00:06:22 · Speaker 1

Uh I have created a words array with some words and in line number forty one I am trying to filter it out words dot filter or array dot filter function which is a filter function uh available defaultly for an array and we are trying to get those words whose length is greater than six. A character length is greater than six.

### 00:06:41 · Speaker 1

So here only the destruction will be output. I've also written the output. Tell me now only one thing. Whether words dot filter is a pure function or not? It's it's quite straightforward. Okay? The reason I'm asking this question is just to ensure you have understood all the topics and you are able to answer. Okay? Just mention question number three in comment section and mention your answer. Okay?

### 00:07:02 · Speaker 1

The answer for this is words.filter is a pure function. Okay? Why is it a pure function? Because no matter how many times you pass the same array to it, it's always going to return the same set of results to you. Okay? So words.filter is a pure function. How about other array methods? Like maybe words

### 00:07:23 · Speaker 1

words.length or words.map, etcetera, some other array functions. So, I just want you to get this trick trick of determining whether a function is a pure or not by understanding these examples. First thing what you check, okay?

### 00:07:42 · Speaker 1

is this function is pure means is it deterministic

### 00:07:45 · Speaker 1

Yes. So words.filter is deterministic, it always returns the same value. So we can tell this is a pure function. But there is also another check that you have to do. Is it causing side effect? See, words.filter itself is only one function, okay? So it is not inside any other function at the moment. So it is not causing any side effect. So as you know it is not enclosed inside any, it is not enclosed inside any function. So since it is not enclosed inside any function, so words.filter itself is pure, okay? Now if I enclose this inside a function,

### 00:08:15 · Speaker 1

something um uncommon geek. If I if I enclose this inside this function. Now, uncommon geek is not a pure function. The reason being we are invoking another function inside this function which will cause a side effect, okay? So this will make uncommon geek as a

### 00:08:35 · Speaker 1

impure function. But words dot filter is a pure function. So the trick is simple. So given a function, you check are there any function inside that or are you trying to modify some variables which can cause side effect, first thing. If they are doing if you if they are causing side effect,

### 00:08:53 · Speaker 1

then that it is not a pure function. If it is not causing a pure function, then check the flow of the block. Is the value is always deterministic? Like there is no random value, there is nothing that we are waiting from network response. So where the value can change? So there is nothing as such is happening.

### 00:09:09 · Speaker 1

So line number forty uncommon we can tell this an impure function. Okay. So these are the only two things. Does it cause a side effect whether the output return value is deterministic. So just stick to these two things and you'll be able to solve any question on a pure and impure functions. So now one last question. Question four. I'll keep it short. Why pure functions are essential?

### 00:09:35 · Speaker 1

Okay, this is just a theoretical question that can be asked in the interview. Pure functions are essential because, number one, pure functions are deterministic. So those functions that are deterministic, right, they will give they will be very useful during the long run of a project. So because they are not going to change and you can be you can use it in across multiple places. So that's the first advantage.

### 00:09:57 · Speaker 1

second advantage, the first advantage deterministic.

### 00:10:02 · Speaker 1

Second advantage memoization. Okay?

### 00:10:06 · Speaker 1

memoization. What is what is memoization? Memoization in very simple terms is where the value returned basically we store certain values in the some some computation which we have already done, we store that value in the memory. So that whenever you call it for the next time, rather in doing the same things again, we will just use the value that is stored in the memory. For example, if you if I'm calling this area of rectangle ten times with same two and four, I can store it in my local storage or some global array and if same value passed four and two, do not compute it. just return eight. Okay? So we can

### 00:10:39 · Speaker 1

use that if it is if it's a pure function we can try to use the memorization concept also. There are many other advantages also if you know that please do mention that in the comment section. So this about the pure functions first video where I explained the fundamentals and second video I explained the question that can be asked. I don't see there is there could be any other question that can be asked around this topic. All you have to know is how to determine if a given function is pure or not and when to use pure functions and when when not to okay these are the things that you have to these are the things

### 00:11:09 · Speaker 1

taken away that has to be taken away from this video tutorial. Okay. So thank you so much for watching my video. If you like the video please do like it on YouTube channel. If you want your friends also to learn from it, share it with them and subscribe to our channel. Okay. And the I I've also written the medium blog around this topic. Okay. The link to the medium blog is mentioned on my comment section, sorry, mentioned on my description section. Just go ahead and read in case if you want to get the examples they are readily available there. You can go ahead and check it. Okay. Thank you so much. Catch you in next video.
