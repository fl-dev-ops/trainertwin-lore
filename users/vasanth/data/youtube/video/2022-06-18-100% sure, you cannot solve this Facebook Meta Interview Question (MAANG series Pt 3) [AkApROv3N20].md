---
id: AkApROv3N20
title: 100% sure, you cannot solve this Facebook/Meta Interview Question (MAANG series
  Pt 3)
url: https://www.youtube.com/watch?v=AkApROv3N20
date: '2022-06-18'
duration: 00:15:47
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# 100% sure, you cannot solve this Facebook/Meta Interview Question (MAANG series Pt 3)


## Transcript

### 00:00:00 · Speaker 1

Most of you would be thinking this is very easy. So there is a function called clear all timeout and we can use that to clear all timeouts. Correct? Unfortunately, there is nothing, no function called clear all timeout.

### 00:00:14 · Speaker 2

What is it They come

### 00:00:15 · Speaker 1

to uncommon geeks myself first and i hope you are all doing well so as you know this is a video series where we are discussing about a mang interview questions mang refers to metas slash facebook and apple amazon netflix and google the most common question that are asked in the front-end developer interview in these questions i'm going to discuss in this particular video series so it's highly beneficial if you are someone who targeting for these tire one companies they require you to prepare in a altogether different way the way have you prepared for a service company or a less paying product company and

### 00:00:45 · Speaker 1

these companies is totally different so the questions they ask is also different so unfortunately i have not interviewed by meta so far i have gathered a lot of interview questions from the interviewing platforms like glassdoor and cora and other stuffs and i'll be discussing a lot of such questions along with tagging the companies which company is has asked these questions in the recent past and how to tackle it okay so first question in this series um in this particular video is from the facebook okay the question is

### 00:01:14 · Speaker 1

Implement clear all timeout functionality. Okay. Hope you all know what is clear timeout. Basically, it will use to clear the timeouts that whatever has been created in the past. So whenever you do a set timeout, the return value of a set timeout is an integer. So that can be used as a passed as an argument to clear the timeouts. So here the question is you have to clear all the timeouts that is present in a component. Okay. So most of you know why clearing a timeout is necessary because otherwise it will create in a memory leak.

### 00:01:44 · Speaker 1

Let's say you navigate from page X to page Y, but the whatever the set timeouts in page X are not cleared, then what it does, it will continue to take some memory location. So let's say after you navigate, the timeout is has timeout has been over and some process executing, it will still execute in the background, which is unintended. Okay, so you have to clear all the timeouts before navigating to the next page. Okay, so this is the purpose that why they ask this question. Now, most of you would be thinking, this is very easy. So there is a function called clear all timeout and we can use that to clear all

### 00:02:14 · Speaker 1

timeouts correct unfortunately there is nothing no function called clear all timeout okay so there is only function called clear timeout so just to start off with i'm showing you some information about the set timeout so this is the set timeout the global set timeout method sets a timer which executes a function or a specified piece of code once the timer expires so let's say you set a timer for one second after one second whatever the function that is inside the set timeout that get executed okay what is the return value the return uh is a timeout is

### 00:02:44 · Speaker 1

positive integer value that identifies them that identify the timer created by the call set timeout this can be passed to clear all timeout to cancel the timeout so you pass that id to a clear all timeout so clear timeout that will that will clear the timeout okay so if you come here to the clear timeout method okay so basically it takes the timeout id to clear so there is nothing called clear all timeout okay for your reference i'm just searching and showing okay there is nothing called clear all timeout so you have to write a clear all timeout on your own now

### 00:03:14 · Speaker 1

So before we start coding, in fact, I have already tried writing this code and come here. Facebook questions are not so easy so that I can take it right away and code. Okay, I've prepared and come. So how should be a thought process? Okay, so to clear all the timeouts, whatever it is, first you should get hold of timeouts, hold of set timeouts that have been created, correct? So one easiest way that comes to everyone's mind is, so there'll be different timeouts created different function. So there has to be one global variable which will keep track of all the timeouts.

### 00:03:44 · Speaker 1

timers that have been created and whenever you are leaving a page in react you have something called componented unmount or if you're using hooks there is a return that you can write to whenever page is unmounted in angular also you have called ng on destroy so there are functions lifecycle method that get triggered on whenever you're leaving a page and from that point you can get all the ids you'll be pushing into an array and whenever you're leaving the page you will call that array you'll run the loop to the length of that array and clear all the timeouts okay this is should be one acceptable solution

### 00:04:14 · Speaker 1

Avoided, interviewer is fine, giving you some extra space. Basically, whenever you have to push array values, set timers into array, it will take some extra space. Let's start with this solution first.

### 00:04:27 · Speaker 1

What we are doing is we are creating one array called timer array

### 00:04:32 · Speaker 1

So I've created one timer here. Okay. Now what I'll do, I'm creating const timer one is equal to set timeout. Okay. So here set timeout. What I'm doing here is I'm setting a timeout for one second. Okay. Then I'm creating a log inside timer one. Okay. Then what I'm doing, I'm pushing timer one dot. Sorry, timer array dot push timer one. Okay. So as you know, this will be a.

### 00:05:02 · Speaker 1

numerical number that is written by the set timeout function. Okay, so we are pushing that into the timer array. Same we will do for the second time. Okay, so inside timer two, the variable name is also timer two and you're pushing timer two. So now why I created var and not const just with the focus that it is something that is going to be accessed throughout the block, you can you can use a const also because you're not changing a reference, you're just pushing the values into it. But I have preferred var as it's a global or a function scope. Okay.

### 00:05:32 · Speaker 1

So now technically how in real time this happens is let's say this block is in one function, this block in some another function. In that case you can just create and push it into the global variable, the instance of set timeout. Now first let me execute it before I do the clear timeout.

### 00:05:49 · Speaker 1

So after one second both the timers have been printed because both have a timeout of one

### 00:05:54 · Speaker 1

have to write a functionality to clear all these timeouts how you do is very straightforward you can use for loop or while loop okay I'm using while so while timer array dot length okay what I will do then is clear clear timeout okay timer array dot pop okay you can use for loop also and iterate till the length the reason why I'm using while loop is technically there should we will not know the how many timers have been created correct so I'm running till the length of this

### 00:06:24 · Speaker 1

timer and I am extracting the last element one by one with help of timer dot pop okay so once all two two timers have been extracted it will be cleared okay just for your reference I am also showing what will be the value

### 00:06:40 · Speaker 1

timer of okay I cannot pop because since I'm popping difficult to log okay but I'll show you how the values will be

### 00:06:48 · Speaker 1

timer timer 1 is timer 1 similarly timer

### 00:06:57 · Speaker 1

timer 2 okay so now let me execute these two will not execute timer 1 and timer 2 reason being uh javascript engine is very fast so before one second only this statement will be executed i think it'll take just milliseconds to uh for these things to scan and uh it come to the while loop and it will clear all the timers very quickly okay so timer 1 was 2 timer 2 is 6 so number numerical number that is allocated to each of it and the clear timeout cleared the timeouts all the timeouts that created in a page

### 00:07:27 · Speaker 1

cleared okay this is one approach so this some interviewer will be accepting this but generally companies like Facebook would look for little optimal approach because this is something a mid-level engineer can come up with most engineers can come up with is there any optimal solution than doing this the reason is let's say you have one container component and lot of sub components in that so now different components accessing one variable to push the values and finally clearing it is not something that is scalable going for

### 00:07:57 · Speaker 1

correct when the lot of components come it will be difficult so there has to be way where you can avoid this so when you have multiple components or multiple places inside a component using this timeout concept something should run in your mind okay so many things multiple contents or multiple components need one common entity correct so easiest way to think of is utility file you have to create one utility file that will take all the timeouts okay and that should also have a reference of all the timers that have been

### 00:08:27 · Speaker 1

Whenever you call the clear timeout, whatever the functionality we did here, clearing all the timeouts should happen there. Okay. So I'll show you that approach also. And these are the two solutions that I thought of. Second approach, according to me, is the optimal one, which you should be writing in the interview. This one probably right. If any other normal companies are asking, probably you can write this approach, but not for the companies like Mangorfan. Okay. So solution is quite simple, not so complicated.

### 00:08:56 · Speaker 1

Probably what we can name timer util

### 00:09:00 · Speaker 1

So inside this, this is an object that has a function called, first you should have the timer array, correct? So timer array initialize to empty, then you have set timeout.

### 00:09:13 · Speaker 1

set timeout this is not the set timeout built in so this is the set timeout function that you are adding okay which has an anonymous function so what that does is it will create a timer every time whenever you invoke it okay so set timeout requires two things as you already saw one is a function another one is a delay so this function takes input as two things function

### 00:09:36 · Speaker 1

And here you actually create the JavaScript set timeout with function comma delay

### 00:09:43 · Speaker 1

Don't get confused. This is same as this. How you create a set timeout, correct? So where you have a function and you have a timeout number. Same is actually been copied here. Rather the function having the function, someone is passing it. So here the function itself is enclosed inside the set timeout. In this particular block, some caller will be calling the passing that function. Okay, that is only difference and delay as well.

### 00:10:09 · Speaker 1

What you will do is you have to push this ID into an array

### 00:10:14 · Speaker 1

So timer array dot push ID. Okay. So that it get updated every time whenever you invoking set timeout, you should keep adding the new ID that is got generated. Correct. Now, now you have clear.

### 00:10:31 · Speaker 1

Here also, the same process, whatever we did in the last state, we can follow that while timer array dot.

### 00:10:38 · Speaker 1

Clear timeout

### 00:10:41 · Speaker 1

Then timer array

### 00:10:44 · Speaker 1

pop so last value basically you are popping okay so this is now just an object okay unlike the previous code this is not a function this is just an object we created what you can do is you can export this object so that every function get an access to this now what we have is const now we have to create the first timeout okay how do I do that is timer timer utility

### 00:11:12 · Speaker 1

Dot set timeout, it needs a function basically, correct? So I'm passing a function.

### 00:11:20 · Speaker 1

first timer and it requires a second argument so which is a delay so I'm passing that delay also here okay now if I run this series okay so before I run this series before I run this code so if you are someone who is seriously preparing for JavaScript driven interviews whether it is React React JS React Native Vue any other technologies I've created a beautiful two series one on the most common JavaScript interview questions how to tackle that another one is the custom implementation okay where most common custom implementation related question how to

### 00:11:50 · Speaker 1

implement array dot concat on your own how to implement array dot map string dot carrot okay so these are the implementations i've created a beautiful series please watch those two series and come to this kind of a series because it will be slightly advanced if you're preparing for the interview and all companies may not ask such questions okay so cover those two series first then come to this video i'll try to add this somewhere on the screen as in the description section okay and if you're liking the content whatever i'm making on the youtube especially helping you guys to clear the interview please do like my youtube videos do not forget to subscribe to my

### 00:12:20 · Speaker 1

channel uncommon geeks and share these videos along with your friends so that they also get benefited okay now let me run the code

### 00:12:28 · Speaker 1

So I'm running. See, I have not cleared the timeout intentionally, but I just have created a set timeout. So if I run the code, only the first timer is being printed. Okay. Similarly, I can create a second timer. Okay. Second timer. If you want for reference, you can return the ID also from here. I don't see any point, so I'm not returning an ID. Okay. So I'm running. So you get first timer and second timer also. Now what you do is you just simply invoke timer utility dot clear.

### 00:12:57 · Speaker 1

So, this will trigger this method, so which will clear all the time modes. Let me run this again.

### 00:13:04 · Speaker 1

Okay, first timer, second timer. So timer array dot length. Okay. I shouldn't be calling this dot clear all time, but I should be just calling the clear timeout. I'll tell you why. So this dot clear timeout will invoke this function only. Then it will be a recursion. So there is no point. You will not go anywhere. So you should actually call the JavaScript clear timeout. To avoid confusion, probably you can set timeout something, a function, clear timeout function. Inside this, you can use the actual JavaScript clear timeout and set timeout. Okay. So this will, to summarize, so this is a block.

### 00:13:35 · Speaker 1

you can export this utility method this is a timer utility is there right so you can write an export here okay in in react or angular in any other uh technology that you are using and you can use this variable from all the places no matter from where you're using use it from all the places let's say one one particular container you have inside which you have multiple components okay whether angular react view anywhere so whenever you're navigating from page x to page y what all things you want to unmount okay maybe the header bar remains

### 00:14:05 · Speaker 1

but only the middle portion get changed so on destroy of that or component did unmount of that just invoke this function okay so in that cases you it will clear all the timers and go to the next one if particular timeout need not to be clear so that's kind of an what if that how we can call this a little advanced kind of an approach where you can have the ids return from here and you can track the ids so for the clear timeout you can pass the ids what all ids need to be cleared okay you can extend this example to have a very profound solution so this

### 00:14:35 · Speaker 1

According to me, it's the best solution that one can write for clear all time out. So have in mind with the both the solutions. The reason being sometimes interview will have you the first one itself. So you don't have to write the second one. In case if it extends, then write the second one also. So this is like if you're taking biology in the PUC or first in the second PUC. okay where you need to know there will be a lot of terminology so you should not know just one terminology referring one thing if you know more than one at least one you'll remember in the exam similarly this so you should know more than one approaches

### 00:15:05 · Speaker 1

the interview will be definitely looking for more than one approaches okay so please practice both okay and i'll be adding the solution to my github repository feel free to copy the code from there understand once again and probably you can continue coding on your own try to optimize it further as well okay thank you so much for watching my video catch you in the next one if you're liking the content that i'm making please do again subscribe to my channel like the video share this videos along with your friends read my medium blog cell data link that also in the description i've written articles like this beautiful articles like this and our weekly

### 00:15:35 · Speaker 1

basis on a lot of javascript concepts i have a good number of followers you two follow on me and add your comments for any article if you see some improvisations can be made okay thank you again catch you in next video

