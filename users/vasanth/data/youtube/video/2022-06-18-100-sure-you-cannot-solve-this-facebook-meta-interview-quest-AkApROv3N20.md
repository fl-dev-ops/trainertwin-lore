---
id: AkApROv3N20
title: 100% sure, you cannot solve this Facebook/Meta Interview Question (MAANG series
  Pt 3)
date: '2022-06-18'
url: https://www.youtube.com/watch?v=AkApROv3N20
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ At the time of this series recording, there was no video series which was discussing\
  \ MAANG (Meta, Apple, Amazon, Netflix, Google) interview questions for the frontend\
  \ developers in detail. So, I have decided to decode most of the interview questions\
  \ that were available on the internet. \nThe purpose of this series is not just\
  \ to help you to clear MAANG interview, but help you become a fundamentally strong\
  \ frontEnd Engineer. Stay tuned and watch this entire series.\n\nGithub Repository\
  \ that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \n Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\n\
  Medium Blog: https://mevasanth.medium.com/  \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation Series:\nhttps://www.youtube.com/watch?v=eGzErMUfdpk&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I"
author: careerwithvasanth
duration: 00:15:47
model: saaras:v3
transcript: true
---

# 100% sure, you cannot solve this Facebook/Meta Interview Question (MAANG series Pt 3)

## Transcript

### 00:00:00 · Speaker 1

Most of you would be thinking, Vasanth, this is very easy. So there is a function called clear all timeout and we can use that to clear all timeouts, correct? Unfortunately, there is nothing, no function called clear all timeout.

### 00:00:14 · Speaker 1

Welcome to Uncommon Geeks. Myself, Pasand. I hope you all doing well. So, as you know, this is a video series where we are discussing about MANG interview questions. MANG refers to Meta, Relash, Facebook, and Apple, Amazon, Netflix, and Google. The most common question that are asked in the front end developer interview in these questions, I'm going to discuss in this particular video series. So, it's highly beneficial if you are someone who targeting for these tier one companies, they require you to prepare in a altogether different way. The way have you prepare for a service company or a less paying

### 00:00:44 · Speaker 1

product company and these companies is totally different. So the questions they ask is also different. So unfortunately I have not interviewed by Meta so far. I have gathered lot of interview questions from the interviewing platforms like Glassdoor and Quora and other stuffs. And I'll be discussing lot of such questions along with tagging the companies. Which company is has asked these questions in the recent past and how to tackle it. Okay. So first question in this series in this particular video is from the Facebook. Okay. The question is

### 00:01:14 · Speaker 1

implement clear all timeout functionality. Okay? uh hope you all know what is clear timeout. Basically it will use to clear the timeouts that whatever is been created in the past. So whenever you do a set timeout, uh the return value of a set timeout is an integer, so that can be used as a past as an argument to clear the timeouts. So here the question is you have to clear all the timeout that is present in a component. Okay? So most of you know why clearing a timeout is necessary, uh because otherwise it will create in a memory leak.

### 00:01:44 · Speaker 1

Let's say you navigated from page X to page Y, but the whatever the set timeouts in page X are not cleared, then what it does, it will continue to take some memory location. So let's say after you navigate, the timeout is has timeout is been over and some process executing, it will still execute in the background which is unintended. Okay, so you have to clear all the timeouts before navigating to the next page. Okay. So this is the purpose the way they ask this question. Now, most of you would be thinking, Vasan, this is very easy. So there is a function called clear all timeout and we can use that to clear

### 00:02:14 · Speaker 1

timeouts, correct? Unfortunately, there is nothing no function called clear all timeout, okay? So there is only function called clear timeout. So just to start off with, I am showing you some information about the set timeout. So this is the set timeout, the global set timeout method. Set set timer which executes a function or a specified piece of code once the timer expires. So let's say you set a timer for one second, after one second, whatever the function that is inside the set timeout, that get executed, okay? What is the return value? The return is a timeout is

### 00:02:44 · Speaker 1

positive integer value that identifies the that identifies the timer created by the call set timeout. This can be passed to clear all timeout to cancel the timeout. So you pass that ID to a clear all timeout. So clear timeout that will that will clear the timeout. Okay? So if you come here to the clear timeout method, okay?

### 00:03:02 · Speaker 1

So basically it takes the timeout ID to clear. So there is nothing called clear all timeout, okay, for your reference I'm just searching and showing, okay. There is nothing called clear all timeout, so you have to write a clear all timeout on your own. Now.

### 00:03:14 · Speaker 1

So, before we start coding, in fact, I have already tried writing this code and come here. Facebook questions are not so easy so that I can take it right away and code, okay? I've prepared and come. So how should be your thought process, okay? So to clear all the timeouts, whatever it is, first you should get hold of timeouts, hold of set timeouts that have been created, correct? So one easiest way that comes to everyone's mind is, so there will be different timeouts get a different function. So there has to be one global variable which will keep track of all the timeouts, timeouts

### 00:03:44 · Speaker 1

that are been created and whenever you are leaving a page in React you have something called component unmount or if you are using hooks there is return that you can write to whenever page is unmounted. In Angular also you have called ng on destroy. So there are functions life cycle method that get triggered on whenever you are leaving a page and from that point you can get all the IDs you will be pushing into an array and whenever you are leaving the page you will call that array you will run the loop to the length of that array and clear all the timeouts. Okay. This is should be one acceptable solution provided.

### 00:04:14 · Speaker 1

interviewer is fine, giving you some extra space. Basically, whenever you have to push array values, set timeouts into array, it will take some extra space. Let's start with this solution first, okay? So, what we are doing is we are creating one array called timer array, okay?

### 00:04:32 · Speaker 1

So I've created one timer here. Okay? Now what I'll do, I'm creating const timer one is equal to set timeout, okay? So here set timeout

### 00:04:43 · Speaker 1

What I'm doing here is I'm setting a timeout for one second, okay? Then I'm creating a log inside timer one, okay? Then what I'm doing, I'm pushing timer one dot, sorry, timer array dot push timer one, okay? So as you know this will be a numerical number that is written by the set timeout function, okay? So we are pushing that into the timer array. Same we will do for the second time, okay? So inside timer two, the variable name is

### 00:05:13 · Speaker 1

also timer two and you're pushing timer two. So now why I created var and not const just with the focus that it is something that is going to be accessed throughout the block. You can you can use a const also because you're not changing a reference you're just pushing the values into it but I have preferred var as it's a global or a function scope. Okay? So now technically how in real time this happens is let's say this block is in one function this block is in some another function. In that case you can just create and push it into the global variable the instance of set timeout. Now first Let me execute it before I do the clear timeout. I'm sorry.

### 00:05:49 · Speaker 1

So after one second both the timers have been printed because both have a time out of one. Now you have to write a functionality to clear all these time outs. How you do is very straightforward. You can use for loop or while loop. Okay I'm using while. So while timer array dot length okay. What I will do then is clear clear time out okay. Timer array dot pop okay. You can use for loop also and iterate till the length. The reason why I'm using while loop is technically

### 00:06:19 · Speaker 1

there should we will not know the how many timers have been created. Correct? So I am running till the length of the timer and I am extracting the last element one by one with help of timer dot pop. Okay? So once all two two timers have been extracted it will be cleared. Okay? Just for your reference I am also showing what will be the value. Okay? Timer of okay I cannot pop because since I am popping difficult to log. Okay? But I will show you how the values will be here.

### 00:06:48 · Speaker 1

Timer, Timer one is

### 00:06:52 · Speaker 1

timer one. Similarly, timer two is timer two. Okay? So now let me execute. These two will not execute, timer one and timer two, reason being, uh, JavaScript engine is very fast. So before one second only, this statement will be executed. I think it'll take just milliseconds to, uh, for these things to scan and it'll come to the while loop and it will clear all the timers very quickly. Okay?

### 00:07:17 · Speaker 1

So timer one was two, timer two is six. So number numerical number that is allocated to each of it and the clear timeout cleared the timeouts. All the timeouts that created in a page got cleared, okay? This is one approach. So this some interviewer will be accepting this, but generally companies like Facebook would look for a little optimal approach because this is something a mid-level engineer can come up with, most engineers can come up with. Is there any optimal solution than doing this? The reason is

### 00:07:44 · Speaker 1

Let's say you have one container component and lot of sub components in that. So now different components uh accessing one variable to push the values and finally clearing it is not something that is scalable going uh forward, correct? When the lot of components come it will be difficult. So there has to be way where you can avoid this. So when you have multiple components or multiple places inside a component using this timeout concept, something should run in your mind, okay? So many things, multiple containers or multiple

### 00:08:14 · Speaker 1

components need one common entity. Correct? So easiest way to think of is utility file. You have to create one utility file that will take all the timeouts, okay? And that should also have a reference of all the timers that have been created. Whenever you call the clear timeout, whatever the functionality we did here, clearing all the timeout should happen there, okay? So I'll show you that approach also. And these are the two solutions that I thought of. Second approach according to me is optimal one, which you should be writing in the interview. This one, uh, probably you write if any other normal companies are asking.

### 00:08:44 · Speaker 1

probably you can write this approach, but not for the companies like Mangor fan. Okay? So solution is quite simple, not so complicated. Const

### 00:08:53 · Speaker 1

timer okay

### 00:08:56 · Speaker 1

probably what we can name timer util. Okay. So inside this this an object uh that has a function called first you should have the timer array, correct? So timer array initialize to empty. Then you have set timeout, okay? You have set timeout. This is not the set timeout built in. So this is the set timeout function that you are adding, okay? Which has an anonymous function. So what that does is it will create a timer every time whenever you invoke it, okay?

### 00:09:26 · Speaker 1

So set timeout requires two things as you already saw. One is a function, another one is a delay. So this function takes input as two things, function and delay, okay? And here you actually create the JavaScript set timeout with function comma delay. Okay?

### 00:09:43 · Speaker 1

Don't get confused. uh This is same as this. How you create a set timeout, correct? So where you have a function and you have a timeout number. Same is actually been copied here. Rather the function having the function, someone is passing it. So here the function itself enclosed inside the set timeout. In this particular block some caller will be calling the passing that function. Okay? That is only difference and delay as well. Okay? Now, what you will do is you have to push this ID into an array. Okay?

### 00:10:13 · Speaker 1

So, timer array dot push ID, okay? So that it get updated. Every time whenever you invoking set timeout, you should keep adding the new ID that is got generated, correct? Now. Now you have clear timeout, okay? Function

### 00:10:31 · Speaker 1

Here also the same process whatever we we did in the last state we can follow that while timer array dot length okay. Clear timeout. Okay. Then timer array.

### 00:10:44 · Speaker 1

dot pop. So last value basically you are popping. Okay? So this is now just an object. Okay? Unlike the previous code, this is not a function. This is just an object we created. What you can do is you can export this object so that every function get an access to this. Now, what we have is const. Now, we have to create the first timeout. Okay? How do I do that is timer timer utility. Okay?

### 00:11:12 · Speaker 1

dot set timeout. It needs a function basically, correct? So I'm passing a function log

### 00:11:20 · Speaker 1

first timer and it requires a second argument. So which is a delay. So I'm passing that delay also here. Okay. Now if I run this series, okay. So before I run this series, before I run this code, so if you are someone who is seriously preparing for JavaScript driven interviews, whether it is React, React JS, React Native, Vue, any other technologies, I've created a beautiful two series. One on the most common JavaScript interview questions, how to tackle that. Another one is the custom implementation, okay, where most common custom implementation related question,

### 00:11:50 · Speaker 1

implement array.concat on your own, how to implement array.map, string.charat, okay? So these are the implementations I've created a beautiful series. Please watch those two series and come to this kind of a series because it'll be slightly advanced if you're preparing for the interview and all companies may not ask such questions, okay? So cover those two series first, then come to this video. I'll try to add this somewhere on the screen as in the description section, okay? And if you're liking the content whatever I'm making on the YouTube, especially helping you guys to clear the interview, please do like my YouTube videos. Do not forget to subscribe.

### 00:12:20 · Speaker 1

my channel Uncommon Geeks and share this videos along with your friends so that they also get benefited. Okay? Now let me run the code.

### 00:12:28 · Speaker 1

Okay, so I'm running. See, I have not cleared the timeout intentionally, but I'm just have created a set timeout. So if I run the code, only the first timer is being printed. Okay, similarly, I can create a second timer. Okay, second timer. If you want for reference, you can return the ID also from here. I don't see any point, so I'm not returning an ID. Okay, so I'm running. So you get first timer and second timer also. Now, what you would do is you just simply invoke timer utility.

### 00:12:54 · Speaker 1

dot clear timeout. Okay? So this will trigger this method. So which will clear all the timeouts. Let me run this again.

### 00:13:04 · Speaker 1

Okay, first timer, second timer. So, timer array dot length. Okay. I shouldn't be calling this dot clear all timeout. I should be just calling the clear timeout. I'll tell you why. So this dot clear timeout will invoke this function only, then it will be a recursion. So there is no point, you will not go anywhere. So you should actually call the JavaScript clear timeout. To avoid confusion, probably you can set set timeout something, function, clear timeout function. Inside this, you can use the actual JavaScript clear timeout and set timeout. Okay. So this will, uh, to summarize, so this is a block.

### 00:13:34 · Speaker 1

where you can export this utility method. This is a timer utility is there, right? So you can write an export here, okay? In React or Angular, any other technology that you are using. And you can use this variable from all the places, no matter from where you're using, use it from all the places. Let's say one, one particular container you have inside which you have multiple components, okay? Whether Angular, React, Vue, anywhere. So whenever you're navigating from page X to page Y, what all things you want to unmount, okay? Maybe the header bar image,

### 00:14:04 · Speaker 1

same but only the middle portion get changed. So on destroy of that or componented unmount of that just invoke this function. Okay? So in that cases it will clear all the timers and go to the next one. If particular timeout need not to be clear so that's kind of an what you what how we can call this a little advanced kind of an approach where you can have the IDs returned from here and you can track the IDs. So for the clear timeout you can pass the IDs what all IDs need to be cleared. Okay? You can extend this example to have a very profound solution.

### 00:14:34 · Speaker 1

according to me is the best solution that one can write for clear all time out. So have in mind with both the solutions. The reason being sometimes interview will happen with the first one itself. So you don't have to write the second one. In case if it extends then write the second one also. So this is like if you have taken biology in the your PUC or first and the second PUC, okay? Where you need to know there will be lot of terminology. So you should not know just one terminology referring one thing. If you know more than at least one you will remember in the exam. Similarly this, so you should know more than one approaches.

### 00:15:04 · Speaker 1

the interview will be definitely looking for more than one approaches. Okay? So please practice both, okay? And I'll be adding the solution to my GitHub repository. Feel free to copy the code from there, understand once again, and probably you can continue coding on your own. Try to optimize it further as well. Okay? Thank you so much for watching my video. Catch you in the next one. If you're liking the content that I'm making, please do again subscribe to my channel, like the video, share this video along with your friends. Read my medium blogs. I'll take the link that also in the description. I've written articles like this, beautiful articles like this on a

### 00:15:34 · Speaker 1

basis on lot of JavaScript concepts. I have good number of followers. You too follow on me and add your comments for any article if you see some improvisations can be made, okay? Thank you again, catch you in next video.
