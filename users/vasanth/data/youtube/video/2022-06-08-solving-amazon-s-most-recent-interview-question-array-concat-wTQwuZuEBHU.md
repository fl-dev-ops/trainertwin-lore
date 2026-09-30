---
id: wTQwuZuEBHU
title: Solving Amazon's most recent Interview question Array.concat (JavaScript Custom
  Implementation Ep-2)
date: '2022-06-08'
url: https://www.youtube.com/watch?v=wTQwuZuEBHU
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. JavaScript \n\n Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\n\
  \nArray Concat from developer.mozilla.org: \nhttps://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat\n\
  \nMedium Blog https://mevasanth.medium.com/ \nGithub Repository that contains examples:\
  \ https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:19:29
model: saaras:v3
transcript: true
---

# Solving Amazon's most recent Interview question Array.concat (JavaScript Custom Implementation Ep-2)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself Vasant. I hope you all doing well. So as you know this this is a series where we are discussing about the custom implementation. So in this particular video I'll be discussing a particular method called array.concat. I think most of you might be using array.concat day in and day out. I'll be explaining how to write a custom implementation for that method in this particular series or this particular video. Okay? Very first, before getting started, I want to shout out which all companies have recently

### 00:00:30 · Speaker 1

this question in the interview very first. Apple, Microsoft, Facebook. Okay? So these are the three companies that recently asked this question in their different interviews. I read this across different feedback platforms. So I got to know this has been asked. So that is the reason I picked this particular topic for this video. At least now show BBCB series and watch the video till the end. In case if you're applying for tier one companies like this, custom implementation is nowadays becoming a trendy question. So most of the interviews they're asking this. Okay? Now, if you've not watched my previous two videos where

### 00:01:00 · Speaker 1

I have explained introduction about this particular series and also I have explained how a particular programming constraint will get access to built-in function like whenever you create an array how methods of array like push, pop, etcetera get access to it or same way how whenever you create a string how string methods are being accessible to that. So I have clearly explained that and how to add your methods your custom implementation method to the existing list. If you not watch that straight away if you come to this it will be little difficult for you to go along. So I would highly advise

### 00:01:30 · Speaker 1

please go ahead and watch it. Okay? Now without wasting further time, let's get started. Okay? So now we have array.prototype.concat. Okay? The person the reason why I have opened this, I'll tell you. In the interview, he'll ask you, candidate or Vasan, please write a custom implementation for array.concat method. You straight away get started with the implementation. According to you or most of us use array.concat to concatenate two arrays. array one.concat array two. So our assumption is it is used to concatenate two two arrays. Correct? But if you see the definition here, the concat method used to merge two or more arrays.

### 00:02:05 · Speaker 1

This method does not change the existing arrays but instantly returns a new array. The reason I'm showing this is

### 00:02:11 · Speaker 1

because very first it is not concatenating two arrays. So your program whatever you are writing should be able to take more than two arrays also. This method does not change the existing arrays and returns a new array. Okay, your whatever the code you are writing should return a new array, should not affect the source. Why I'm saying this is if you not read the read this definition then you straight away start the implementation, you will not be able to cover the full full implementation of array.concat and tier one companies especially will never expect half

### 00:02:41 · Speaker 1

correct solution, they'll straight away reject. So, if you are not sure how a built-in function is behaving, please request the interviewer to that I will see the definition, what all the things that are part of this function, what all it will take, I want to check, okay? Then please check that, then come back and start the implementation. With my experience, most interviewers will allow that because making you they they are not worried whether you are aware of the concat fully or not. There the thing is, can you write a complete implementation? So feel free to ask them, come and check, okay? Now. So what if I add some value into it? Okay?

### 00:03:17 · Speaker 1

like this const value as y and you are concatenating array two also and value also if you run you see value also got concatenated that is so array.concat accepts arrays two or more arrays also it accepts values and concatenate that with the source array now what if you pass a function here so value two and I am passing a function

### 00:03:47 · Speaker 1

I'm passing a function here. You see?

### 00:03:50 · Speaker 1

See, why I'm showing all this is you have to think in this direction in the interview. Okay? If you don't think in this direction, then you think you're not asking right questions. So, you have to ask. So now, before running only, you can ask interviewer, should I need to consider function and class kind of flows? If he says no, ignore it. If he says yes, then consider it. Okay? Now if I run, it is it is also it is concatenating the function also. Now, value three, what if you pass

### 00:04:17 · Speaker 1

undefined

### 00:04:20 · Speaker 1

वैल्यू फोर, व्हाट इफ यू पास नल? ओके?

### 00:04:24 · Speaker 1

So you have to ask all these questions to yourself in the interview, then you should also ask these questions to the interviewer. The reason being he will think, yeah, candidate is thinking in all the direction, that is what they're looking from you, okay? So now you got to know function and if and null being pushed. Now you must be, you must come with a strategy in your mind, that is, there are mainly two scenarios. One, when the input is array, I mean a parameter is array, okay? And another scenario, when parameter is non array, it is any value,

### 00:04:54 · Speaker 1

it could be a value, it could be a function, it could be undefined, it could be null or anything, okay? Whenever these second set of things are there, the value is getting just pushed into the the output, correct? Whenever it is a type one, that is array as an input, in this case, what we are doing, we are iterating the values of the array and pushing the values into it, correct? So, putting other way, two broad categories where you identify the values here and push it to the source, iterate the array, get the values and push it, here you will have values ready

### 00:05:24 · Speaker 1

available, push it. So you should think in this direction and code, okay? So and also I have to tell you very interesting point. I have also not come prepared completely to write the array.concat. I'll be like not may not be like exactly one of you who has never wrote any custom implementation. Luckily I have written few custom implementation. But for array.concat I haven't written any complete working code and come to this video. The reason being I whenever I come prepared for the video, I generally don't make any mistake, okay? That's the whole purpose of preparing I know. Okay? With that you will miss

### 00:05:54 · Speaker 1

an opportunity of seeing someone else making a mistake and learn from it. So due to which I decided to selectively pick few topics and don't prepare and come so that I can show possible errors that you can make or what will be my thought process whenever a problem comes. Okay? Sure. So this so far this has been my thought process. Now I'll start the implementation. Okay? Step by step. And I have I need to do one shout out. If anyone of you

### 00:06:16 · Speaker 1

I'm preparing for a serious front end driven interviews no matter what React Angular JavaScript anything. I prepared a beautiful series of twenty plus videos which which includes most common interview questions in this JavaScript topic and how to tackle them what are the possible mistakes a candidate does how to solve that all of that are very clearly explained I've tried to link that somewhere on the screen also in the description section. Please do watch that it will be beneficial for you okay. And if you're liking whatever the content that I'm making on the YouTube please do like my videos on YouTube channel share with your friends do not forget to subscribe common gigs. Okay? Without wasting further time, now let's get started with the implementations. Okay? So,

### 00:06:53 · Speaker 1

I have created aura.concat.js, that's the only thing I have done, okay? Nothing I have other than that I haven't done anything. So now let me try running this start with a concat implementation, okay? So I have const array one, one two three.

### 00:07:08 · Speaker 1

and const array two which is four five six five six okay then I have I will copy the same things okay

### 00:07:19 · Speaker 1

value one, value two, value one, value two, value three and value four. Okay? So you guys already know how to write a custom function or how to include your function into the built of prototype methods, correct? So array.

### 00:07:35 · Speaker 1

prototype.myconcat, okay?

### 00:07:39 · Speaker 1

on cat

### 00:07:43 · Speaker 1

not contact, okay? So here you are writing a function. So this is an anonymous function. In case if you don't know what is anonymous function, feel free to read my uh watch my video. I'll try to add the link also where I very clearly explain about anonymous function, okay? Now, array one dot my concat, okay? I'm not doing anything. For just let us make sure we are able to trigger this, okay? So log welcome to uncommon gex. Let me execute this, okay?

### 00:08:13 · Speaker 1

Yeah. So we are trying to invoke my concat. Same way you would invoke any array function. I'm invoking this and and what this function is doing is just the logging something in the screen. This is my channel name anyway. So just logging it on the screen so it is working well. Okay? Yeah. Now, generally don't avoid logging like this in the if you are applying for tier one companies, they think you are you are not confident. Tier two and all you would feel free to log. The reason I why I logged is I will have a diverse audience. I should make sure the easiest process or the beginner

### 00:08:43 · Speaker 1

process that you can follow whenever doing a custom implementation, okay? So now, what I will do is, so in for the array one, I'm concat, I'm passing array two, same way possibly how you have written here.

### 00:08:57 · Speaker 1

that only I will paste here. Okay?

### 00:09:00 · Speaker 1

So array two

### 00:09:03 · Speaker 1

value, value one, value two, value three and value four, okay? All these I am passing to this particular method, okay? To array.concat function. So now, here we have a two possibility like I said. First, it could the the input could be, the argument could be of array type or any other individual value, okay? Now, before that, you should you should get access to the array with which you are invoking this, correct?

### 00:09:33 · Speaker 1

and second bond you should get access to the list of arguments that you are passing here. So I think most of you would know how to get access to a function or to get arguments of a function access to arguments of a function that is simply using the arguments keyword. This is provided by the JavaScript which will give us all the arguments that are passed to this function okay. So what I'm doing const argument bunch is equal to I'm just initial in that argument. In case if any one of you are not aware of this there is a very important interview question that asked around arguments I'll try to link that

### 00:10:03 · Speaker 1

also in the description. Please go ahead and watch that, okay? So next question, next point. So now you should also get a reference to this array one, correct? The input array. So what you can do, input array.

### 00:10:16 · Speaker 1

is equals to this. So basically here this refers to the reference with which you invoked the my concat method. Okay? So in this case the reference is array one. So now just for you you I mean since I'm explaining I will show uh I will show log the value and I'll show input array is input array. Okay? Then argument bunch.

### 00:10:43 · Speaker 1

is argument bunch, okay? Don't do this in the interview, just for explanation purpose I'm doing. So input arrays one two three, argument bunch did not print. So JSON dot stringify

### 00:10:58 · Speaker 1

Okay, let us see. uh Argument bunch you see. So zero with is four five six, one is y, four is null. So it's a different it's an object basically that contains a list of arguments passed over function. Okay. So now you know

### 00:11:11 · Speaker 1

uh how to get access to input array and how to get access to the arguments okay. Next what is the process. The next process is so you you will create a for loop okay. And you will iterate the argument bunch. And you will check if

### 00:11:28 · Speaker 1

The

### 00:11:31 · Speaker 1

arguments argument bunch okay of I is an array okay how do you check it many many ways there are there I generally use this array dot is array of this okay if not okay else then what I do is input array dot push

### 00:11:52 · Speaker 1

whatever the arguments of I because we already seen there are right so far whatever we analyze there are only two categories okay don't think my implementation is complete okay someone come with a flow where wasn't you haven't considered a particular flow whatever came to my mind I considered that by the time I ask these many questions to interviewer he might will definitely say if any scenario I missed or he is expecting that scenario from me okay now next is

### 00:12:17 · Speaker 1

in this case what we need to do basically do is same we need to push the value into input array okay but how we do that is I'm just naming it let okay how we need to do that is whatever the argument values are there that we need to push into input array okay just for the simplicity I'm creating a function okay function push values

### 00:12:40 · Speaker 1

So it takes two arguments, one is source, another is destination. Okay? So how we invoke this is push values, okay? What is the source here? The source here is input array. The destination would be arguments of I, okay?

### 00:12:59 · Speaker 1

So what it does is, so to the input array, it should print, it should add the destination. Okay, what I would do here is for if it is fast, don't worry, I'll explain the step by step once again all the things, okay? Destination length, okay? Then I plus plus, then what I'm doing here is

### 00:13:19 · Speaker 1

source dot push what I'll do is destination of

### 00:13:24 · Speaker 1

I. Okay? Then I will return the SRC. Actually, we don't have to do this, but just on us, just to be double sure, I'm just assigning here input array is equal to push values. Otherwise also it should work well because we are passing here as a reference, okay? Just to be double sure in the interview, I'm just adding this. Maybe if it works well, if you give me some more time, the interviewer give me some more time, then I would remove this, this line. I would only keep the push values. And once all of this is done, I will return the input array, okay? And return the input array so that I will be logging here. console.log

### 00:14:02 · Speaker 1

the entire thing I'm putting inside a log, okay? Whatever the value returned from this particular concat method, we are printing here, okay? This could throw some errors or possibly there could be some flow that went missing, but I'm just finger crossed. I think it will work well whatever I've analyzed, but I'll do a dry run before I run the code, okay? Because less number of times you run the code to check your correctness, the more chance you clear the interview, because your mind should be calculating what is happening whenever you are writing a thing, not the

### 00:14:32 · Speaker 1

spiler. Okay, now let us do a dry run. So these values are there, value four, array one dot concat, I'm passing all the values. Okay.

### 00:14:40 · Speaker 1

Now here, argument bunch contains list of all the argument that you have passed. Input array basically points to this array one, whatever the reference with which you invoked it, okay? Next we have a for loop with arguments bunch. Next we are checking if array dot is array of argument bunch of I, in case if whatever the, for example in this case it will be true, but in this case it will be false, correct? So we are checking whether argument bunch is an array, if so, we are passing the source array and the destination array.

### 00:15:10 · Speaker 1

And we are pushing the destination values into the source and returning the source. So in our case, if I do a dry run, very first, the value will be one, two, three in the array one. Next, whenever what you do here is, here you check, okay, the argument one is array, that is four, five, six an array, yes. But then what we'll do, we'll call this push values method, which source has one, two, three, destination has four, five, six, okay, then here what we are trying to do is we are pushing destination of I, that is is four into one two three array. one two three first iteration four

### 00:15:47 · Speaker 1

Next iteration five

### 00:15:49 · Speaker 1

next iteration six then you will finally return the value okay so now input array is one two three four five six okay input array is one two three four five six next you come next will be y so here it checks whether array.is array of y no it is not an array so it will come here you push the value of y here and this and this undefined null goes in a similar way for me at least in the dry run whatever the code I have written seems to work well okay

### 00:16:19 · Speaker 1

think I have made a mistake in this step somewhere itself, please do mention that in the comment section, okay? Otherwise, let me run the code.

### 00:16:26 · Speaker 1

Okay. Luckily it is working well, okay? It doesn't happen always the same way in the interview. We end up making some mistake. Maybe I'm in a very relaxed state as I'm making a video, I was able to write a proper working code, okay? So where one two three four five six why, okay? But we need to compare, correct? Just for the comparison sake, I am also running the concat.

### 00:16:47 · Speaker 1

Okay, see. So whatever the concat was doing, my concat function is also doing the absolutely similar thing. Okay? So now I think I have covered all the scenarios here. To be more, what you call, if you want to make it more aligned, you can include this entire block in a function, okay? And trigger that function first and inside the function you can trigger another function, etcetera. Okay? But this works well for me and whatever the modularity that you want to take, I'll leave it up to you guys in the interview however you want to do.

### 00:17:17 · Speaker 1

to do that way. Okay? uh This is all about the array.concat. Okay? I maybe if you want last time I'll quickly iterate what everything that I did. So, these are the very first whenever a problem is given to you, first analyze what all uh whenever custom implementation given, first go to the official documentation, see the possibility, what all values it can take, how and how and all it can work. And then come here and try to segregate. So, as I did, so it takes arrays and non-arrays. So, one flow for the arrays,

### 00:17:47 · Speaker 1

one flow for the non arrays. Okay? So then code accordingly. One flow for the arrays and one flow for the non. So by looking at the different values you you will be able to categorize your solution. Okay?

### 00:17:58 · Speaker 1

Then start implementing first, write a method and make sure your whatever the prototype that you are trying to trigger is triggering it properly. Then start writing a definition, okay? So whatever the code that I written is the optimal solution, I don't think so. There could be some more optimal solutions also. This came to my mind in the interview and it is I know I will be able to write a fully working code with this. Given some more time, if I have to optimize, probably I would try to optimize in few areas, okay? And my whole point of implementing is accept the

### 00:18:28 · Speaker 1

push, I haven't used any built-in methods, okay? You can see this length is a property that we can that also we can skip, I mean we can write a custom. Length and push, I haven't array.is array, this I'm checking. Only three things, array.is array, push and the length property, three things I'm using, other than that I haven't used any built-in methods. There are so many ways you can optimize the code by using the built-in methods like join and flatten etcetera, but I am not, I'm trying to avoid as many built-in functions as possible.

### 00:18:58 · Speaker 1

So due to which I've written this particular solution. uh That's all from this video. If you like this video, please do like it on YouTube channel and share the video along among with your friends. Do not forget to subscribe to Uncommon Geeks. I've written very beautiful article about lot of JavaScript concept in my medium blogs. I I showed few few of my blogs in my last video also. I'll try I'll try to link my medium blog in the description. Please do read lot of articles. Follow me on link follow me on medium. Okay. Thank you again for watching the videos. See you in next one
