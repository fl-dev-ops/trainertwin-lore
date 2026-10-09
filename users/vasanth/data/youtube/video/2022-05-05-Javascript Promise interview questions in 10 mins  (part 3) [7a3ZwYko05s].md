---
id: 7a3ZwYko05s
title: Javascript Promise interview questions in 10 mins  (part 3)
url: https://www.youtube.com/watch?v=7a3ZwYko05s
date: '2022-05-05'
duration: 00:11:39
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# Javascript Promise interview questions in 10 mins  (part 3)


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. As you already know, we are just continuing with our video series on promises. I hope you're all doing well. So in this video, we are going to just extend whatever we left in our last video, that is about the promise chaining, how a promise inside a promise creates a problem gradually when we have a lot of promises being chained, one inside another. And what are the ways in which we can avoid that? Okay, without wasting further time, let's get started. See, I am on a same set of

### 00:00:30 · Speaker 1

code whatever was written in the previous video and the same code okay so now what was the problem we are facing here is we have a list of promises one inside another so multiple promises we are calling and we are waiting for that input to output to come then we go calling the second promise and it has been continuous continued so this becomes very tedious to read and debug so how i can avoid that

### 00:00:52 · Speaker 1

So I will propose one solution that is using async and await. Okay. So first let me write the code. Then I'll explain what are async and await, how they can help us to not particularly avoid promise chaining. So that cannot be avoided, but how at least efficiently increase the readability of the code. Okay. So what I'll do, I'll enclose all these functions, all these promises inside a function.

### 00:01:18 · Speaker 1

So I have this so and I'll return the promise one okay I'll return the promise one from this and similarly I'll create another function called function two

### 00:01:32 · Speaker 1

And from this function I'll return the second promise

### 00:01:39 · Speaker 1

Return promise

### 00:01:44 · Speaker 1

Then I'm writing another function

### 00:01:49 · Speaker 1

And from this function I'll return the third prize whatever you have written

### 00:01:53 · Speaker 1

So here I'll return the promise three

### 00:01:57 · Speaker 1

So now I'll create a test function. This I have hidden so to because I'll not be using the same. So function

### 00:02:06 · Speaker 1

First let me complete the completely write the code then I'll explain what I'm doing

### 00:02:18 · Speaker 2

Catch you later

### 00:02:26 · Speaker 2

Yeah

### 00:02:29 · Speaker 2

Enter

### 00:02:33 · Speaker 2

Response one equals to function

### 00:02:42 · Speaker 2

Then we have response to is equals to

### 00:02:46 · Speaker 2

Response three is equals to

### 00:02:51 · Speaker 1

I'm less trying to log

### 00:02:53 · Speaker 2

Response

### 00:02:56 · Speaker 1

So this time what I'll do I rather returning promise one two or three I will return the numbers okay resolve one

### 00:03:05 · Speaker 1

And resolve

### 00:03:08 · Speaker 1

Here what I would do response is

### 00:03:12 · Speaker 1

Response one plus response

### 00:03:17 · Speaker 1

Plus response three

### 00:03:21 · Speaker 1

So

### 00:03:23 · Speaker 1

Maybe I'll just move to a next level const

### 00:03:28 · Speaker 1

z equals 2

### 00:03:32 · Speaker 1

logging the output here okay in case if you get any error

### 00:03:43 · Speaker 1

Errors

### 00:03:46 · Speaker 1

Now I will explain step by step what I did in this entire flow. Okay. Basically, we had already had the promises. Now what I have done, I have just added a, enclosed them inside a function.

### 00:03:58 · Speaker 1

I'm returning that promise whatever the promise that I've created now I'm returning that promise from this block okay so here I'm using a concept of async okay one minute I missed it and await

### 00:04:10 · Speaker 1

What async and await does I'll explain you. See, async and await are just what we call them as a syntactic sugars. A very fancy word, syntactic sugars. Okay. Basically, just to avoid writing all this junk of code, promise.then, promise.then, promise.then, keeping one inside another. What we do here is we use a keyword called async and await. So if you write a function to be await, so this await, whenever you type, it will wait for an action to complete. Same way what promise.then would have done. So here we are using

### 00:04:40 · Speaker 1

await actually there are some differences between promise and async and await okay i'm not gonna touch base much on that because that is not specific i mean relevant for this video feel free to read there are very few basic difference between what promise and the async and await okay i i'm taking this on a very simple note where await basically means it will await until the this function is resolved

### 00:05:05 · Speaker 1

Then we have another await which will wait for this function to be resolved. So what async does is whenever JavaScript encounters an async block, so it will be ready to await for something. Okay. If you let's say you are awaiting for something without this async keyword, then it will throw an error actually when you execute. So you must have an async function. Then you can use await inside that. So await basically waits for this to finish. Okay. So in simple words, async and await will not help you in any performance, will not help you to avoid.

### 00:05:35 · Speaker 1

promise chaining all the things whatever was happening before it will happen in the very same way only difference here is they will help you to it will help you to write a very clean code so rather having probably how many lines we wrote so probably from around 42 to 56 we wrote around of 14 lines of code and here we ended up having around 10 lines of code and in a very big programs you will still save a lot of lines because there will be a lot of functionalities that happening inside each promise okay so this is about the pro how we

### 00:06:05 · Speaker 1

use a sink and a way to avoid the promise chaining okay i mean at least in a readability way we can avoid it so if i execute this block now

### 00:06:14 · Speaker 1

Nothing is exac nothing is printing on the screen

### 00:06:18 · Speaker 1

in very first video of mine i guess related to hoisting i had i had asked this question many candidates do this mistake in the interview and i actually uh i i did not do this intentionally i also did this mistake by miss only so at least we must be able to figure out why nothing is printed on the screen immediately the reason being we see we have one two three four functions and we are not invoking any function

### 00:06:42 · Speaker 1

When we're not invoking any function then what will be executed nothing so let's invoke test

### 00:06:50 · Speaker 1

If I execute this now

### 00:06:57 · Speaker 1

are getting responses six that is so first what happened it came here uh to first promise so first promise took one second to resolve and what we returned here is the one okay second promise took two seconds to resolve what we returned here is two after the promise result third promise took three seconds to resolve after the three second what we returned is three so here we have response one plus response two plus response t uh three plus two plus one which is equal to six so that is what getting printed here okay so

### 00:07:27 · Speaker 1

you got the output what is printed here. So if I reduce from if I make everything this as zero, like the promise executes immediately. I mean, in zero seconds, it doesn't wait for anything, but still the process is asynchronous only. So if I put a log statement here that get executed first before the promise is resolved.

### 00:07:47 · Speaker 1

Response six is this happened much quickly

### 00:07:50 · Speaker 1

Now problem is this three promise you are waiting response one response response wasn't why you enclose them in the type try catch block what will happen if you don't enclose that in the type try catch block so I want to show you that also so I'm commenting this and I'm pasting here let's say there is no catch

### 00:08:08 · Speaker 1

Or I believe all of you know aware of what is try catch. Basically try catch used for the handling the exceptions. So you try to do something and if that doesn't happen the way you are expecting, then it will throw an exception that will be catched in the catch block. Like we have an array of four indexes. You are trying to access the 15th index. Then that array element is not there. So I mean array index out of bound exception will come. That exception will be handled in the catch block. So now we are doing this. If I execute now, nothing will fail. Everything works fine.

### 00:08:38 · Speaker 1

what I'll do in in function number one rather resolving I'll reject it

### 00:08:44 · Speaker 1

is basically I'm showing you simple examples but in network call there's always a possibility that it will fail in that case what will happen see you will see some error like error thrown by exception error unhandled rejection so some rejection was thrown and we did not handle it so that is the reason whenever you do the promise chaining okay and since you cannot have it like a then and catch so each promise you cannot have a then and catch so together you can have a try catch like this okay it's the easiest and the easiest way to handle the catch

### 00:09:15 · Speaker 1

Whenever any anything fails, so you'll be able to catch that in the catch block. So now I'll execute this again. So error is one. So output. So whatever was resolved, we are able to know which block the error came, correct? So now we have to write the response to if you if you reject.

### 00:09:33 · Speaker 1

An interesting thing

### 00:09:36 · Speaker 1

Try to guess the output if you know please mention this and in particular video time and mention your answer I'll tell whether it's right or wrong. If not you can see this video.

### 00:09:45 · Speaker 1

So error is one actually rejected again. Okay. Here in the second block, but it doesn't, it did not go to that level. The reason being we are inside a try and catch. And as soon as any try fails, any line, this line, this line, any line it fails, it'll go to the catch block and that is the final or that is the end of the execution of this block.

### 00:10:06 · Speaker 1

It will not continue further. I mean, once you go to catch, come back to try and continue the execution, that doesn't happen. Because we only explicitly handling an exception. Once exception is thrown, that is the end of that execution block. So now we one and two both are rejecting. Now you will not be able to catch, you know, you'll not be able to see what error thrown by the two. So to just to, if you have to avoid, then you can resolve this. Then probably we will get error is two. So second block, we will see the error.

### 00:10:33 · Speaker 1

This is about the promise chaining, how to avoid the promise chaining, okay, or syntactically how to make it look better. So code readability will increase and the usage of async under it, when to use async under it, and when you are using async under it, how to catch the error. If there are any error comes, how to handle that. So all of them I have tried explaining in this video. In the upcoming videos, now what we are doing, all the promise are executed in a sequential way, one after the other. Is there a way where we can execute the,

### 00:11:03 · Speaker 1

promise in a parallel way because if our logic doesn't compel us to use it in a sequential way can use it in parallel way and the many other topics to touch base on the promise are they always so synchronous can they be synchronous also the promises so there are many interesting topics of the interview that can be asked on promise i'm going to touch base on all of that do not skip future videos watch all the videos about promise and become an expert in that okay thank you so much for watching my video if you like this video please do like it on my youtube channel and do not forget to share this video with your friends and please subscribe

### 00:11:33 · Speaker 1

to my YouTube channel UncommonGeeks okay thank you so much for watching catch you in next video

