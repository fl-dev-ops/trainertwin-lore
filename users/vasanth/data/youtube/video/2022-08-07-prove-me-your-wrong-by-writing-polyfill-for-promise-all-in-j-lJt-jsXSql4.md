---
id: lJt-jsXSql4
title: 🔥 Prove me your wrong by writing Polyfill for Promise.All in JavaScript 🔥 Amazon
  | Apple INT QSN
date: '2022-08-07'
url: https://www.youtube.com/watch?v=lJt-jsXSql4
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Interview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nPromise video 1: https://youtu.be/1OINZhOIh0c\nPromise video 2: https://youtu.be/3V-fKuh1-8w\n\
  Promise video 3: https://youtu.be/7a3ZwYko05s\nPromise video 4: https://youtu.be/A5Az9NgncEE\n\
  Does async await block main thread in JS: https://youtu.be/c3c-LLdjlGc\n\nMedium\
  \ Blog https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nMAANG series for frontEnd Developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN"
author: careerwithvasanth
duration: 00:22:08
model: saaras:v3
transcript: true
---

# 🔥 Prove me your wrong by writing Polyfill for Promise.All in JavaScript 🔥 Amazon | Apple INT QSN

## Transcript

### 00:00:00 · Speaker 1

My way of teaching is like this. So let us try to write the bare bone of the program first. Then let's get into logic, correct? Let's say you are trying to add two numbers or basically a function that's supposed to return a boolean value. So by default return true. Then start the execution. So that one criteria is met, then keep modifying it.

### 00:00:21 · Speaker 1

all, welcome back to Uncommon Geeks. Myself, Fasant. I hope all the uncommon geeks out there are also doing well. Okay? In case if you are seeing me first time on the internet, I'm a content creator. I help lot of people to clear their interview. I'm a beautiful series in the past which has been appreciated by many. I'll try to add those videos somewhere on the screen also in the description section. Please watch the video. Any of the apart from the premium companies if you are aspiring for any of the tier two and the tier three companies, watching my video series itself, whether you are React JS, whether you are looking for React Net,

### 00:00:51 · Speaker 1

angular or any of that, your fundamentals will become very strong and you from ten to twenty percent chance of clearing an interview, easily you will go up to seventy to eighty percent chance of clearing the interview. I'll guarantee you that. So what the other videos and coming to this video. The question that I'm gonna discuss in this video is very, very important interview concept, okay? And if I say this again, most won't get interest. Everybody wants the jargon, correct? So this question recently asked in Amazon and Apple, okay? Whether you are aspiring to those

### 00:01:21 · Speaker 1

companies or any other companies this question is very very important. Why this is very important because as soon as I whenever I ask this question to candidate or whenever some interviewer ask this question to candidate candidate suddenly become frightened. uh what is happening I don't know this how to write etc. okay. So I am gonna explain this question in such a simple way where after watching the video till the end even before trying you will be able to write the code on your own like you watch the video then go back to the editor definitely you will be able to write the code on your own. Only thing you need to have a little bit idea about the concept, okay? Let's get started without wasting further time and this is the question.

### 00:01:59 · Speaker 1

Yeah. I think you got to know what is the question. The question is you have to write a custom implementation for a built-in method called promise.all. Okay? uh few might know what is promise.all does if not I'm gonna explain that in a brief and many do not know what is promise.all. Okay? See I have created a beautiful series so watch this series you will never rejected in your future interview. This is quite superficial there is a chance you still get rejected but there is a high chance you will clear the interview after watching my entire series. Okay? So here I have made four videos explaining the promise

### 00:02:29 · Speaker 1

into pin everything in depth regarding the promise I've explained here, okay? How the questions will be asked, how you need to tackle it, how you need to solve them, all of that I've explained here very much in detail. But if in case if you are not watched all the videos, I would highly advise please watch that because this I know I assume few things you are already aware when I'm explaining this video. I'll also give a brief introduction but very in detail you have to know the promise if in case if you are aspiring for a very big company so or you are seriously preparing for interview, okay? So please watch all

### 00:02:59 · Speaker 1

the four videos. Now, uh I I assume you know basics of promise if not in very simple words promise basically helps you to write an asynchronous task in JavaScript. uh execute asynchronous activities in JavaScript. As you know JavaScript is a single threaded interpreter programming language. There has to be some way where JavaScript can execute asynchronous task. So promise is one such way. What are other ways? Set timeout is one way. Another way set interval is another way. There are observables. There are many other ways to where you can make JavaScript to work asynchronously but these are the few options

### 00:03:31 · Speaker 1

Now let us first understand what is in very simple words what is promise, what is promise.all, why promise.all required, then let's get into the implementation, okay? So somewhere in the middle of the video, I am gonna explain another very very important question on promise that is will be most generally asked in Amazon's phone screening round, that is the first round. If you don't clear this round, there is no chance you will get into any other rounds. So please watch the video till the end, somewhere I'm gonna reveal that, okay? Now

### 00:04:00 · Speaker 1

Let's get started. So let me create a simple promise, the easiest way of creating the promise. I've explained the various different ways of promise creation in other videos, okay? So const promise one, okay? promise.resolve one, okay? Then we have promise two where I'm resolving the promise two. Now, how to access the values of promise? So promise one dot then

### 00:04:26 · Speaker 1

data log

### 00:04:29 · Speaker 1

data, okay? Then promise two also you want to do the similar way, promise two, okay? Now you can execute the code. So you are seeing one and two. There are two promises and you resolve the promise and you got the output. Very very simple, correct? So this is the same way where you will be calling all the APIs, correct? And maybe you use async and await, but basically end of the day we have to wait until the promise is resolved and we process certain activities, correct? In fact, if you don't know whether async and await block the JavaScript main thread or not,

### 00:04:59 · Speaker 1

also another and very important question. I'll try to I've already made a detailed video. I'll try to link that on screen also in description. Please watch that video. Definitely you get confused if that question was asked to you in the interview without watching my video. Okay? Now, see, basically what we are doing, we are resolving two promises, correct? Dot then in both the places.

### 00:05:16 · Speaker 1

Now, this is taking a time like after this one and this one, they are kind of processing, they are not processing parallelly, they are processing sequentially, correct? After JavaScript compiler knows this exists, it will take this from the stack and it will move into the messages. I mean, you know the concept of event loop, right? That way. If you don't know event loop, please read about event loop. I'll try to put that link also in description. So, then it picks the second one. So it's a sequential execution. Why can't we do this in a parallel execution? Like, where both

### 00:05:46 · Speaker 1

the task happen at once. That is one way or that is one of the thing where try to achieve a parallel processing or we are trying to add lot of code, correct? Basically after dot then whatever you are trying to do is kind of similar. I mean there could be chances where they are similar. Or that could be scenarios where let's say there are two promises until both the promises are resolved successfully, you cannot process certain things, okay? So in that case what you will do? You will do promise one dot then. Inside that you will put the promise two dot then.

### 00:06:16 · Speaker 1

correct? Then probably what you will do, data one, data two. Here you have to write data one dot data two. correct? So only if both are resolved, you will be able to do something. If not, you're not going to do anything. So these are multiple scenarios where this becomes, it's forming a promise nesting, like one promise inside another and it becomes ugly as soon as we have more promises. correct? So rather doing this, is there an prop function which can take multiple promise and return the result in the form of array? correct? So that function is called promise.all. It's a built-in function, okay, which takes

### 00:06:53 · Speaker 1

promise.all and it takes array of promises okay promise one comma promise two then it will do dot then then data

### 00:07:04 · Speaker 1

log data. Okay? Now if I execute the code, you're seeing one comma two, same thing, same thing which happened before you are getting here. Rather getting input one output one after the another. So here you are getting the output in the array fashion. Okay? So in the same order, let's say promise one's output is one, promise two's output is two. Let's say you reject this promise. First promise itself you reject. Okay? Then what will happen? promise.all will stop its execution as soon as anywhere it encounters the rejection. Okay? It is not like let's say three promises you have

### 00:07:34 · Speaker 1

two promises are passed, one is rejected, it is not gonna pass. It is overall operation will be reject, okay? So here let's say I create another promise.

### 00:07:44 · Speaker 1

or let us resolve this. So two are resolved, okay? Now I'm creating promise three. Okay?

### 00:07:52 · Speaker 1

I'm sorry

### 00:07:53 · Speaker 1

So now I'm creating promise three, okay? Promise three I am rejecting, okay? Now I'm passing promise three as here. So it will not give you output as one comma two comma error, okay? It will give you error in general as you saw, okay? So this is how the promise.all works. Why I'm explaining this in detail, before knowing how the built-in function works, definitely we cannot write our own function, correct? So now you got to know what is promise. Promise is basically used to achieve asynchronity in JavaScript. So whenever

### 00:08:23 · Speaker 1

process taking lot of time generally the network all we go for the promise. Now you know why promise.all is used how promise.all works correct. Very very simple words I've tried explaining for more information like already mentioned watch the detailed videos but this is good enough to continue with the example okay now.

### 00:08:40 · Speaker 1

Before I start writing the custom promise.all method or a polyfill promise.all, uh in case if you like the video so far and you think the further whatever I'm going to explain is informative to you, please like the video. uh Like I always say by liking the video the my video thumbnail appears through a lot of walls, what YouTube calls it impression. More impression, more chance of clicking on the video and the channel becomes popular. Like I always mention I have a noble cause of helping people to clear their interview. If the video becomes popular, I could reach to more people and help

### 00:09:10 · Speaker 1

help them to clear their interviews, correct? So please like the video and comment whatever you felt so far, okay? And subscribe to my channel if you're not subscribed and let please watch continuing after doing all this, okay? Thank you. Now let us continue. So what I'll do now is let me comment this for a while.

### 00:09:29 · Speaker 1

Now, I need to write a custom function. Or basically a function, correct? Function promise all, okay? So promise.all takes a list, correct? Promise list.

### 00:09:42 · Speaker 1

correct? This is very simple. So far you know because promise.all was taking a list. So you are taking a list here. correct? What is promise.all returning? So it is also returning a promise. So only you are able to do dot then console dot like etcetera. correct? promise.all returning a promise. This is very very important. Let's return a promise. return

### 00:10:00 · Speaker 1

So my way of teaching is like this. So let us try to write the bare bone of the program first. Then let's get into logic, correct? Let's say you are trying to add two numbers or basically a function that's supposed to return a boolean value. So by default return true. Then start the execution. So that one criteria is met, then keep modifying it. Same way I'll teach you this. So first we need to return

### 00:10:22 · Speaker 1

return a new promise, correct? We need to create a promise. Return new promise, okay? So what will promise will have? Promise will have resolve, comma, reject, two activities a promise can have, correct? Very simple word. So first thing promise.all should return a promise, so that activity is completed here. Correct? Now let us go to the further processing. What is further processing? So we need to iterate through the promise one after another and we should see what the output we have got and we should keep

### 00:10:52 · Speaker 1

getting that output into a some array and return that array at the end. Correct? Let us see. So I'm creating a let output which is an array because you saw the promise.all was also returning the values in the form of an array. Correct? So so I'm returning creating a variable called output initializing this with a empty parenthesis. Now, we have a promise list. We need to iterate it. Correct? So how do we iterate? promise list promise list dot for each

### 00:11:21 · Speaker 1

Why for each, uh, can't we use a map? This also I've explained in multiple videos, why we should use for each and when we should use map. In simple words, this is also important interview question. For each, use for each when you don't expect, when you are not expecting a new array as an output. Use map when you are expecting a transformed array as an output. So for each doesn't return anything, map returns a new array, okay? So please remember these things and use them wisely because this is very, very important and interviewer, in case let's

### 00:11:51 · Speaker 1

use map here still you can write a code but interviewer will give you less credit for using map. Okay? Now, what all things for each will have for each will have two arguments. One is the element itself, second one is the index. Okay?

### 00:12:04 · Speaker 1

Don't worry, even if I make a mistake, I'll fix them live, okay? So that you don't commit that mistake in the interview. Now, promise list for each we have, each promise we need to resolve, correct? So, let's put a try catch block.

### 00:12:19 · Speaker 1

try catch and you have an exception E, okay?

### 00:12:24 · Speaker 1

Fine

### 00:12:26 · Speaker 1

I think catch doesn't require arrow function. So try catch you wrote, I'm not tracking any specific exception like array out of wound, null pointer exception, I'm tracking exception E in general, okay? So here now in the try catch block what you will do? You have a promise. So in our case what is the promise? So promise one is the first promise that for each will have, correct? How do I resolve that? You know you how you would have done first promise.one.then.data, correct? Let's do the similar thing here. here as well, promise

### 00:12:59 · Speaker 1

dot then, okay?

### 00:13:02 · Speaker 1

Data

### 00:13:04 · Speaker 1

output.push

### 00:13:07 · Speaker 1

Data

### 00:13:09 · Speaker 1

Okay? In case if we get a rejection, try catch, let's say it go to catch due to any reason, then what you should do, promise dot all you observed carefully, it is not going to process whenever there is an rejection, it will stop and it will no matter there are ten promises and the tenth promise got failed and nine promises successful, still it returns a error itself, it will not resolve the promise, correct? So, what we will do, whenever it goes to catch, we will reject it.

### 00:13:34 · Speaker 1

okay? We will reject the promise itself. Maybe you can pass E as well as like an exception that you are sending, okay? Now, I mean all this can be improvised further by throwing and handling it properly. I'm trying to keep it very simple so that the beginners don't get too much frightened by looking at my very enhanced example. So I'm trying to write a very simple minimalistic working code, okay? Now, so you're trying to do output.push.data. So reject you did. When to resolve? Resolve, as you know, it's whenever there is a success, you're going to resolve it, correct? So when is the success. So you are taking the index here. Let's say if the index is equals to promise list

### 00:14:14 · Speaker 1

dot length. Okay? I put a comma. So if it reaches the dot length, that means the index has reached the last index of the promise list, correct? So that's an indication that the complete promise list is traveled and now you can resolve the

### 00:14:30 · Speaker 1

output. So whatever the output you got, output was an array, correct, which is containing all the results and you are finally returning the output. Now, there was a small mistake that I did here. In case if somebody noticed it even before I saying, please mention the video timing and put your answer in the comment section, okay? I I think you will be the most super brilliant interview preparation who already done good amount of preparation and able to identify the errors that are in the given code, okay? For those who did not identify so far, don't worry, I'll explain that. See you are trying to do index is

### 00:15:00 · Speaker 1

equal to promise list dot length index always starts from zero. So we have let's say in our case we have three three promises. Okay for first let us resolve all. We have three promises arrayed will be zero one and two. What is promise list length? Promise list length is three. So this if will never becomes true. Correct? So you have to do index one index plus one

### 00:15:22 · Speaker 1

or promise list dot length minus one somewhere but basically you should know what is happening okay you will identify this even after running the code for the first time but then the interviewer will think you are not clear about what you are writing so don't run the code many times I've said this in multiple videos of mine run as minimalistic as possible that shows your confidence so you are not writing you are acting as a compiler or interpreter whenever you are writing the code itself okay so now you will resolve in this case and you will reject in in this case okay

### 00:15:52 · Speaker 1

I think mostly it looks good to me in case if there are any issues let us resolve them, okay? First let us start. So we have three promise, correct? And const

### 00:16:03 · Speaker 1

output is equals to my pro okay promise dot all what I wrote function name. Let's do my promise or dot all okay. Let's not mess with the keyword.

### 00:16:14 · Speaker 1

my promise all. So basically it takes an array. What is the array? promise one, promise two, promise three. I'm sorry. promise

### 00:16:24 · Speaker 1

three, correct? Then what will be the output? Output. It returns a promise, so you cannot log the output itself because it's a promise. Output dot then

### 00:16:34 · Speaker 1

Data

### 00:16:37 · Speaker 1

In case if it is difficult for somebody, don't worry, I'm going to explain this once again very much in depth, okay? So, we are logging the data. Shall we run and see what does happen? I think it will work because I practiced once before doing this video. Not like first time I'm doing it. Let's see whether it will work or not. It worked, one, two, three, okay? Let's say in case I reject any promise.

### 00:16:59 · Speaker 1

कि सर रिजेक्ट एनी प्रॉमिस

### 00:17:01 · Speaker 1

it got rejected, overall rejected. So one two, but that is not the one, but overall whenever you processing, you will get the rejection. Okay? So that is what because the previous output, there is no resolve, it got rejected. So if you are using the throw catch properly, you will get a rejection. So for those who still want further explanation, let me summarize the things step by step once again. So we have

### 00:17:24 · Speaker 1

three promises, the most easiest way of creating promises, promise.resolve reject, okay, three promises I've created, okay. Then, uh I've created a my custom function called my promise all and I'm passing an array of promises into it, okay. If you wish you can create an array here, cons promise array, then you can initialize these values into that array, okay. I'm not doing that as it is again, uh very evident what I what I'm doing. Then promise.all I invoked, it is taking a promise list. What it is returning? First is returning it

### 00:17:54 · Speaker 1

returning a new promise. So try to code in the same way I coded. How I did? First return the new promise. Done. So promise takes two things resolve reject. If you don't know this again you have to watch my four videos at least first a couple of videos to understand what is resolve what is reject etcetera. So now you got first return the promise done. So no matter what you write inside you are going to return a promise. Correct? Next. So we need an output array of output so you created a variable called output whether it should be let or const actually it can be both. Okay?

### 00:18:24 · Speaker 1

because we are any of its an array, we are not changing the value, we are only changing the reference. So const also is right use case in this. So promise list for each, then you are iterating each promise. What is each promise? Like each of these promises.

### 00:18:37 · Speaker 1

Then you're trying to do dot then, correct? uh then okay, one mistake I did here. So you shouldn't be putting index outside this chuck. It is good if you put this chuck inside. Okay? uh I don't know if somebody already stopped watching, but this is the right use case. Why? Because if you put the if condition outside, there is a chance where sometimes it can go outside and take up that. So it's good to keep the dot then expression and if chuck inside the dot then. Okay? Then

### 00:19:07 · Speaker 1

and you will reject it. So what you are doing, each promise you are doing the dot then, then you are pushing the output data into the output variable, okay? Whenever it reaches the end of the output, end of the promise list length, that means all the promise that are passed it are processed, then you are sending resolve output. So resolve means it's a success, reject as you know it's a rejection, okay? That is what you are getting here as an output.

### 00:19:31 · Speaker 1

I think you understood the thing clearly. Now, it's a straight whatever you saw so far, correct? Don't copy code or anything, whatever you saw so far, go to Visual Studio Code or any of your favorite editor, try to replicate it. I tried explaining already two to three times, correct? Something has already flashed in your mind. If you are someone who know promise already, definitely you'll be able to write the complete code on your own. Let's say you miss something, don't worry. Don't come back to video. Come back to video later, but don't come back to video suddenly. Try to think whatever I explained.

### 00:20:01 · Speaker 1

and try to code on your own. Okay? And let's say you do a mistake, put a log and you know what is the concept of promise, right? And try to mimic it and try to see my explanation is not the eternal. There could be some other explanations or some other function that you can come up with. You can even optimize the code that I have written. So try to do that. Worst case if nothing is working, my code is always available in GitHub repository. I'll put that link in the description. You can go and get that. If not, try to once go and solve this completely solve this problem on your own. Okay?

### 00:20:31 · Speaker 1

come back in case follow up on the video watch the code and make sure you have written the right code. Okay? So now another very very important aspect that I wanted to mention is

### 00:20:41 · Speaker 1

In Amazon interview question I said there is a very important question that was asked, correct, regarding the promise in the telephonic interview. What is that question? That question is they will ask you to create complete promise implementation on your own. So here you wrote a definition for only promise.all, correct? So they will ask you to write the complete promise structure on your own, like we created new promise, correct? New promise returned a promise for us. So where you are supposed to write a complete promise on your own. So in

### 00:21:11 · Speaker 1

if you want me to make a video on that, please let me know in the comment section. I'll try to make a detailed video that's going to be maybe quite lengthy, twenty twenty five minutes, but that will be worth watching. Lot of companies ask that and it is not after watching that you just not just you know how to create a promise. You'll be able to create lot of things on your own. Okay, please mention that in the comment section. If you want me to make a video on that, definitely I would love to make a video on that. Okay. So that's all about this video. If you like the video, please like the video on my YouTube channel, comment about the video and share the videos with your friends so that

### 00:21:41 · Speaker 1

Anybody who's preparing for the interview, it will be beneficial for them. If you're not subscribed to my channel, please subscribe to Uncommon Geeks. Like I mentioned, this code will be available in my GitHub repository. Go copy the code and practice on your own. I will tag my medium handle also in the description. You have a little lot of beautiful articles about JavaScript, React JS, Node JS, React Native, everything in my medium. Please go there and watch my article, read my articles and follow me on medium as well. Thank you so much for watching. Catch you in next video.
