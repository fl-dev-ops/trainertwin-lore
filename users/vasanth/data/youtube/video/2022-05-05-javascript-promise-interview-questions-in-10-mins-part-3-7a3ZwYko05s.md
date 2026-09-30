---
id: 7a3ZwYko05s
title: Javascript Promise interview questions in 10 mins (part 3)
date: '2022-05-05'
url: https://www.youtube.com/watch?v=7a3ZwYko05s
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ JavaScript being single threaded programming language needs some way  to execute\
  \ asynchronous task. Promise is one such method. It is considered be one of the\
  \ most common and tricky interview topic. I will be covering each and every aspect\
  \ of Promise in this video series. \n\nDoes async await block main thread in JavaScript:\
  \ https://medium.com/p/c07db9c48c3e\n\nPromise video 1: https://youtu.be/1OINZhOIh0c\n\
  Promise video 2: https://youtu.be/3V-fKuh1-8w\n\n\nEvent Loop - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop\n\
  Promise - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all\n\
  My Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:11:39
model: saaras:v3
transcript: true
---

# Javascript Promise interview questions in 10 mins (part 3)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. As you already know, we are just continuing with our video series on promises. I hope you all doing well. So in this video, we are gonna just extend whatever we left in our last video that is about the promise chaining. How a promise inside a promise creates a problem gradually when we have lot of promises being chained one inside another. And what are the ways in which with which we can avoid that, okay? Without wasting further time, let's get started.

### 00:00:27 · Speaker 1

See, I am on a same uh same set of code whatever was written in the previous video. I'm with the same code. Okay? So now what was the problem we are facing here is we have a list of promises, one inside another. So multiple promises we are calling. Uh and we are waiting for that input to output to come, then we go calling the second promise and it has been continuous continued. So this becomes very tedious to read and debug. So how I can avoid that? Okay?

### 00:00:51 · Speaker 1

So, I I will propose one solution that is using async and await, okay? So, first let me write the code, then I'll explain what are async and await, how they can help us to not particularly avoid promise chaining, so that cannot be avoided, but how at least efficiently increase the readability of the code, okay? So what I'll do, I'll enclose all these functions, all these promises inside a function, okay? So, I have this, so and I'll return

### 00:01:22 · Speaker 1

the promise one. Okay, I'll return the promise one from this. And similarly, I'll create another function called function two.

### 00:01:32 · Speaker 1

And from this function, I'll return the second promise. Okay.

### 00:01:38 · Speaker 1

return promise two, okay? Then I'm writing another function, function three, and from this function I'll return the third promise, whatever you have written, okay? So here I'll return the promise three.

### 00:01:57 · Speaker 1

Okay, so now I'll create a test function. This I have hidden, so to because I'll not be using the same. So function test, okay? First let me complete the completely write the code, then I'll explain what I'm doing, okay? sync

### 00:02:13 · Speaker 1

Okay

### 00:02:16 · Speaker 0

try

### 00:02:18 · Speaker 0

catch

### 00:02:19 · Speaker 1

error. Okay.

### 00:02:25 · Speaker 1

catch error

### 00:02:28 · Speaker 1

okay error

### 00:02:32 · Speaker 1

then const response one equals to function one. Okay?

### 00:02:41 · Speaker 1

then we have response two is equals to

### 00:02:46 · Speaker 1

response three is equals to three. Okay? Then let's trying to log response is. So this time what I'll do I rather returning promise one two or three I will return the numbers. Okay? Resolve one. Resolve two. And resolve three.

### 00:03:08 · Speaker 1

Here what I would do response is uh response one plus response

### 00:03:17 · Speaker 1

टू प्लस रेस्पोन्स थ्री, ओके?

### 00:03:21 · Speaker 1

So

### 00:03:23 · Speaker 1

Maybe I'll just move to a next level. Const output is equals to this. Then I'm logging the output here. Okay? In case if you get any error,

### 00:03:38 · Speaker 1

Okay, so

### 00:03:43 · Speaker 1

error is error, okay? Now we'll explain step by step what I did in this entire flow, okay? Basically, we had already had the promises. Now what I have done, I have just added a enclose them inside a function, okay? Then

### 00:03:58 · Speaker 1

I'm returning that promise, whatever the promise that I've created, I'm returning that promise from this block, okay? So here I'm using a concept of async, okay, one moment, I missed it. And await, okay? What async and await does, I'll explain you.

### 00:04:12 · Speaker 1

See, async and await are just what we call them as a syntactic sugars. A very fancy word, syntactic sugars, okay? Basically, just to avoid writing all this junk of code, promise.then, promise.then, promise.then, keeping one inside another. What we do here is we use a keyword called async and await. So if you write a function to be await, so this await whenever you type, it will wait for a action to complete. Same way what promise.then would have done. So here we are using await. Actually, there are some differences between promise

### 00:04:42 · Speaker 1

and async and await, okay? I'm not going to touch base much on that, because that is not specific, I mean relevant for this video. Feel free to read, there are very few basic difference between promise and the async and await, okay? To be, I I'm taking this on a very simple note, where await basically means it will await until the this function is resolved.

### 00:05:04 · Speaker 1

Okay, then we have another await which will wait for this function to be resolved. So what async does is whenever JavaScript encounters an async block, so it will be ready to await for something. Okay, if you let's say you are awaiting for something without this async keyword, then it will throw an error actually when you execute. So you must have an async function, then you can use await inside that. So await basically waits for this to finish. Okay, so in very simple words, async and await will not help you in any performance, will not help you

### 00:05:34 · Speaker 1

to avoid the promise chaining, all the things whatever was happening before, it will happen in the very same way. Only difference here is they will help you to it will help you to write a very clean code. So rather having probably how many lines we wrote. So probably from around forty two to fifty six. We wrote around fourteen lines of code and here we ended up having around ten lines of code. And in a very big programs, you will still save lot of lines because there will be a lot of functionality that happening inside each promise, okay? So this is about the

### 00:06:04 · Speaker 1

how we can use O-Sync and away to avoid the promise chaining. Okay? I mean at least in a readability way we can avoid it. So if I execute this block now,

### 00:06:14 · Speaker 1

Nothing is executed. Nothing is printing on the screen. Tell me why.

### 00:06:18 · Speaker 1

in very first video of mine I guess related to hosting I had asked this question. Many candidates do this mistake in the interview and I actually uh I did not do this intentionally. I also did this mistake by miss only. So at least we must be able to figure out why nothing's printed on the screen immediately. The reason being we see we have one two three four functions. And we are not invoking any function.

### 00:06:42 · Speaker 1

correct? When we're not invoking any function, then what will be executed? Nothing. So, let's invoke test now. Okay? If I execute this now,

### 00:06:57 · Speaker 1

So we are getting response is six that is. So first what happened it came here uh to first promise. So first promise took one second to resolve and what we returned here is the one. Okay? Second promise took two seconds to resolve what we returned here is two after the promise resolved. Third promise took three seconds to resolve after the three second what we returned is three. So here we have response one plus response two plus response three uh three plus two plus one which is equal to six. So that is what getting printed here. Okay?

### 00:07:27 · Speaker 1

So you got the output what is printed here. So if I reduce from if I make everything this as zero like the promise executes immediately I mean in zero seconds it doesn't wait for anything but still the process is asynchronous only. So if I put a log statement here that get executed first before the promise is resolved okay. I print response is six this happened much quickly okay. Now problem is this. Three promise you are waiting response one response two response three wasn't why you enclose them in the tri catch

### 00:07:57 · Speaker 1

ब्लॉक. व्हाट विल हैपन इफ यू डोंट एन्क्लोज़ दैट इन अ ट्राई कैच ब्लॉक? सो आई वांट टू शो यू दैट आल्सो।

### 00:08:03 · Speaker 1

So I'm commenting this and I'm pasting here. Let's say there is no catch. Okay? Or I believe I'm I believe all of you know aware of what is tri-catch. Basically tri-catch is used for the handling the exceptions. So you try to do something and if that doesn't happen the way you're expecting then it will it will throw an exception that will be cached in the catch block. Like you're we we have an array of four indexes you're trying to access the fifteenth index. Then that array element is not there so I mean array index out of bound exception will come. That exception will be handled in the catch block.

### 00:08:33 · Speaker 1

So now we are doing this if I execute now nothing will fail everything works fine but what I'll do in in function number one rather resolving I'll reject it

### 00:08:44 · Speaker 1

See, basically, I'm I'm showing you simple examples, but in network call, there's always a possibility that it will fail. In that case, what will happen? See, you will see some error, like uh error thrown by exception, error unhandled rejection. So some rejection was thrown and we did not handle it. So that is the reason whenever you do the promise chaining, okay? And since you cannot have it like a then and catch, so each promise you cannot have a then and catch. So together you can have a try catch like this. Okay, so easiest and the easiest way to handle the catch. Okay?

### 00:09:14 · Speaker 1

So, whenever any anything fails, so you'll be able to catch that in the catch block. So now I'll execute this again. So error is one. So output. So whatever was resolved, you are able to know which block the error came, correct? So now we have to put the response to if you if you reject now.

### 00:09:33 · Speaker 1

an interesting thing. Now, try to guess the output if you know, please mention this and in particular video time and mention your answer, I'll tell whether it's right or wrong. If not, you can see this video.

### 00:09:45 · Speaker 1

So error is one, actually rejected again, okay, here in the second block. But it doesn't, it did not go to that level. The reason being, we are inside a try and catch and as soon as any try fails, any line, this line, this line, any line it fails, it will go to the catch block and that is final or that is the end of the execution of this block. Okay. It will not continue further. I mean, once you go to catch, come back to try and continue the execution, that doesn't happen. Because we only explicitly handling an exception, once exception is thrown, that is the end of

### 00:10:15 · Speaker 1

that execution block. So now we one and two both are rejecting. uh now you will not be able to catch you know you will not be able to see what error thrown by the two. So to just if you have to avoid then you can resolve this then probably we will get error is two. So second block we will see the error. Okay? This about the promise chaining how to avoid the promise chaining okay or syntactically how to make it look better. So code readability will increase and usage of async and await when to use async and await.

### 00:10:45 · Speaker 1

And when you are using async and await, how to catch the error? If there any error comes, how to handle that? So all of them I have tried explaining in this video.

### 00:10:55 · Speaker 1

In the upcoming videos, now what we are doing, all the promise are executed in a sequential way, one after the other. Is there a way where we can execute the promise in a parallel way? Because if our logic doesn't compel us to use it in a sequential way, can we use it in parallel way? And the many other topics to touch base on the promise, are they always asynchronous? Can they be synchronous also the promises? There are many interesting topics of the interview that can be asked around promise. I'm going to touch base on all of that. Do not skip future videos. Watch all the videos about promise and become an expert in that. Okay?

### 00:11:25 · Speaker 1

Thank you so much for watching my video. If you like this video, please do like it on my YouTube channel and do not forget to share this video with your friends and please subscribe to my YouTube channel Uncommon Geeks, okay? Thank you so much for watching. Catch you in next video.
