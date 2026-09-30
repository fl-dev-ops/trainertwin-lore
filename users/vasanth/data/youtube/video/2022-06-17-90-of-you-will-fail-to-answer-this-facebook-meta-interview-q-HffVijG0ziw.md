---
id: HffVijG0ziw
title: 90% of you will fail to answer this Facebook/Meta Interview question Pt-1 (MAANG
  series - 1)
date: '2022-06-17'
url: https://www.youtube.com/watch?v=HffVijG0ziw
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ At the time of this series recording, there was no video series which was discussing\
  \ MAANG (Meta, Apple, Amazon, Netflix, Google) interview questions for the frontend\
  \ developers in detail. So, I have decided to decode most of the interview questions\
  \ that were available on the internet. \nThe purpose of this series is not just\
  \ to help you to clear MAANG interview, but help you become a fundamentally strong\
  \ frontEnd Engineer. Stay tuned and watch this entire series.\n\n Follow me on LinkedIn\
  \ -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\nGithub Repository that\
  \ contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nMedium Blog: https://mevasanth.medium.com/  \n\nInterview Preparation series :\
  \ https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation Series:\nhttps://www.youtube.com/watch?v=eGzErMUfdpk&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I"
author: careerwithvasanth
duration: 00:15:02
model: saaras:v3
transcript: true
---

# 90% of you will fail to answer this Facebook/Meta Interview question Pt-1 (MAANG series - 1)

## Transcript

### 00:00:00 · Speaker 2

So, since let me run the code and show what is happening, okay? Then I'll tell what are the mistakes that we do in the interview, okay? So if I run the code, so we are seeing something called one E plus forty two. If you saw this for the first time in the interview, from there itself half of your confidence will go off because you don't know what is E, you don't know what is plus, you don't know what is forty two.

### 00:00:26 · Speaker 2

Welcome back to Uncommon Geeks. Myself, Azanth. I hope you all doing well. As you know, this is a playlist or a video series where we are discussing mainly the MANG questions. So MANG refers for Meta, Apple, Amazon, Netflix and Google. The most recent questions that are asked in this kind of companies are currently discussed in this video series. So this is a super important video which I have come up with. It's a question that is recently asked in the Facebook, okay? As I mentioned in the thumbnail, I guarantee ninety percent at least of you will fail to answer this question correctly.

### 00:00:56 · Speaker 2

correctly. Okay? So if you prove me wrong, I'll be very happy. Most of you are able to answer in the first question, I'll be very happy. But I believe most of you will not be able to answer, including me. I was also not able to answer this question properly. um But in the journey of learning the solving this question, I learned a lot of things. uh few things which I already aware, but I got to learn that very much in depth. So it's a super important question, not just because it is asked in the Facebook, but it the amount of things that involves in the journey. So you have to learn a lot of things to write this problem correctly. So, this is a this in this video, I'll be discussing the question.

### 00:01:31 · Speaker 2

And what are the sub elements required to answer that question? Okay, I will not discuss the solution. The solution I'll discuss in the next video, but do not skip this video unless you watch this video till the end, you will not be able to write the solution or you will not be able to understand the solution that I write in the next video. Okay, so without wasting further time, let's get started. Okay, the question is

### 00:01:52 · Speaker 1

is very simple. Here goes the question.

### 00:02:08 · Speaker 1

Yeah. So as you as you saw the question is

### 00:02:11 · Speaker 2

very simple, okay? So given a you have to write a function or there's already a function which takes two strings as an input, okay? which are a potential numbers but in the string format. All you have to do is convert the string into number and add it, okay? Looks very easy, okay? I have already written some code so that we won't waste lot of time, okay? So this is a function add two numbers that takes number one and number two which which takes two numbers as the inputs, two strings as an input actually which are actually

### 00:02:41 · Speaker 2

numbers if we can convert them then we have to add and return okay. So this is very easy. Everyone will be able to write at least with one one point five year of experience engineer will also be able to write it correct. What is that we just convert the number into a string into a number add it and return correct. So I also started the approach in the similar way what I did was I did this maybe most of you would also do the same okay. So where I did number

### 00:03:06 · Speaker 2

Number one plus

### 00:03:09 · Speaker 2

Number

### 00:03:12 · Speaker 2

number two, okay? This what I did. So if I run the code,

### 00:03:17 · Speaker 2

I'm getting twenty three which is absolutely right. Twenty two plus one is twenty three. So as you know most of you would know number basically converts a string into a integer, okay or the number format, okay. There is another function called parsint. So there is a slight difference between parsint and number that also I'm going to explain in a while. uh but basically I converted number into a string into a number and added it and returned the sum, okay. If you want you can make it to two step process by making number one, number two, sum and then return it if you are just starting with. But basically you end up doing

### 00:03:47 · Speaker 2

same thing, okay? Now, I'll just slightly uh extend the problem, okay? uh And in case this question is asked to you in the interview, don't write a solution like this, especially if you're appearing for the companies like Facebook, Apple, whatever the man companies, okay? Thing is, you have to ask as many questions as possible to the interviewer to make sure you are going in a right path. They expect that. They will not give you all the things. You have to understand the reading between the lines and you have to ask. So number one question. So what is the maximum

### 00:04:17 · Speaker 2

limit that number one or number two can be. So you we if you don't ask the question interpreter will not tell. He thinks you already gauge that in your mind and you are writing the code. So to extend the problem what I am doing is

### 00:04:31 · Speaker 2

Let me just increase the number.

### 00:04:34 · Speaker 2

Okay. Now, guess the output. What will be the output? Okay. So, I see now there are two broad category of viewers. One category of viewers are like in a state where you're thinking this is plus one. Let's say let it was just ninety nine plus one hundred. So whatever this number stands for, that kind of a hundred, like next number it is going, okay? I mean it will become one here and remaining these many digits of zero. Some are thinking in this direction. Some got now fully confused.

### 00:05:04 · Speaker 2

You thought that was the answer like one followed by all the zeros, but now so much of a big number, what will happen? Correct? So these are the two broad category of the people. So I was also one of this. I thought the same thing, like it will become one followed by all the zeros, but then again the doubt is running in my mind, what if so much such a big number, can it be added in JavaScript or not? Correct? So, let me run the code and show what is happening, okay? Then I'll tell what are the mistakes that we do in the interview, okay?

### 00:05:34 · Speaker 2

So if I run the code, so we are seeing something called one E plus forty two. If you saw this for the first time in the interview, from there itself half of your confidence will go off because you don't know what is E, you don't know what is plus, you don't know what is forty two. So half of your confidence is gone as soon as you see this. And you will not be able to write the further solution. So what are the mistakes that I did in this this at least till this point in the interview. Number one, I thought I I came with a prejudice and I started writing the code assuming

### 00:06:04 · Speaker 2

this number will be able to convert any string into a number, correct? Which was wrong. Second, I did not ask the interviewer what is the length of number or the maximum length of number, what is the minimum length of number, what if number one or number two can be empty, in that state how to do? Let's say I'm not passing this number, in that case what is the default value? So these are the questions that I did not ask for the interview, so which you have to ask and make sure, so you have all the information required before starting the solution, okay? Now, let me explain what is

### 00:06:34 · Speaker 2

happening here. So it's a very large number. I even I nobody I think most of you including me also will not be able to tell what is number like nine lakh nine thousand something we don't know what is the number it's very big number. So now here at least I'll tell you what is E plus forty two stands for. E plus forty two stands for ten power forty two. Okay?

### 00:06:53 · Speaker 2

So ten power forty two, okay? So one star ten power forty two, okay? So here doesn't make any difference, basically ten power forty two will be ten power forty two only. That is the big number that we form from this computation. So JavaScript is not representing that in the number format, rather it is representing that in a ten power format. So E refers here that, okay? First we should know this. Now, there are some more very very interesting things that you need to know that I'll explain from the official documentation, okay?

### 00:07:23 · Speaker 2

very first. There is something called max safe integer, okay? Frankly, these are the terminologies which I also learned when I were when I started solving this problem, okay? So I'm I want to explain all of these things to you guys first before I start the actual coding, okay? So max safe number, the number.max safe number constant represents the maximum safe integer in JavaScript. So what is the maximum number that can be safely represented as number in JavaScript, okay? So here if you see two power fifty three minus one is the max

### 00:07:53 · Speaker 2

safe integer. So if you run here, so this is the number. Max safe number. So here they have done plus one, plus two, etcetera. But even if you don't do, uh the log basically is pointing uh printing just the max safe number if I run. So this is the maximum safe number, two power fifty three minus one. So this is the number that can be represented as number in JavaScript. Anything beyond this, correct? Anything beyond this, it will be slightly difficult to represent in the number format. So what they do is they try to represent in some other format.

### 00:08:23 · Speaker 2

PF etcetera. Okay, that whatever the acronym you saw. So that basically explained in this documentation, okay? So where how different types of numbers are notated. As you can see here, with one is with E and there are some octal numbers, there are some hexagonal numbers, okay? How those numbers are actually converted. Also is explained in this documentation of parsint. I'll link that also in the description, okay? Also I want to explain you what is the basic difference between parsint and number. So I've taken this from this this.dev. So I thought it is useful so share here

### 00:08:55 · Speaker 2

So number you already saw which was converting the string into a number. Parseint also does a similar thing. Why I'm explaining this is interviewer ask you why you are not using parseint and why you are using number. So you should know the explanation. To explain you should know the difference, correct? So parseint basically number converts the type whereas a parseint parses the value of input. It tries to parse the input. If you see here thirty two pixel, parseint is parsing that into thirty two.

### 00:09:22 · Speaker 2

same pass to the number. Number is converting that into not a number. So thirty two pixel cannot be converted to number from string to number it's not possible. Correct? parse int will kind of parsing it trying to iterate through it and try to extract the value out of it. Okay? So in our example can we use the parse int instead of number? Yes, there was no problem. Okay? But usage you got to know when to use parse int and when to use the number. Okay? Now, let me get back to this again the safe integer. Okay? Now here. There is a for a larger

### 00:09:52 · Speaker 2

number consider using a big int. That is something called big int which is exceeding the max safe integer. If it is exceeding the max safe integer, so there has to be some data type that can hold these big numbers, correct? So that is actually a big int.

### 00:10:07 · Speaker 2

So big int is a primitive wrapper object used to represent and manipulate primitive big int values whereas too large to be represented by the number. So anything that cannot be represented by number can be represented easily with the help of big int. Okay? So that big int can be used in types in terms whenever you're trying to do the computations like this whatever you saw very big numbers. Okay? So to come back here rather having a number if you use the big int.

### 00:10:35 · Speaker 2

Okay, big int, here also big int.

### 00:10:39 · Speaker 2

See, you got the solution. Correct? So getting the solution here, but the problem is interviewer will not be expecting you to use the big int. Because he knows the big int will give you the solution. Correct? But you should be able to write without using the big int. Okay? So now you got to know what when to use the big int, correct? And the about regarding the solution.

### 00:11:01 · Speaker 2

One last thing I want to explain is unary plus operator, okay? This is not related directly to any of the concept I explained, but this is important for the solution that I write in the next video, okay? And I believe most of you would not know the output for this, okay? That is the reason I'm explaining this here.

### 00:11:17 · Speaker 2

So, so we have a console.log plus plus a string. Unity plus and the string and few more Unity plus plus true false and hello.

### 00:11:26 · Speaker 2

If you know the answer to this, please pause the video, mention that in the comment section. I believe most of you would not be, will not know the answer to this, okay? In fact, I also did not know. I ran it, I understood why it is printing so, okay? So I thought of explaining that as a part of this video. Now, before I run this, in case if you are someone who is preparing seriously for the front end developer interview, whether it is for Mang or for any other companies, so JavaScript is one of the core fundamental skill set for the front end developer interviews. So,

### 00:11:56 · Speaker 2

I have pre-cricket now prepared two beautiful series. One contains twenty plus videos with lot of basic questions, normal questions that are asked in the front end level interview and how to solve it, okay? And what mistakes you generally do, how to tackle it. So that series I'll try to add in the somewhere on the screen, I'll see in the description section. I'm at another series where I explain lot of custom implementations. This has become very trendy question in the interview where they'll ask you to implement your own implementation for the built-in methods, like write a custom implementation for array.map.

### 00:12:26 · Speaker 2

how the map behaves, you have to write a function that behaves in a similar way. So that also tried to add in the description also in the screen, okay? Please watch those two video series, okay? Then come to this mang series. The reason why I'm saying mang series is kind of a little advanced level of interview, correct? Here we discuss quite complicated questions. So after watching those two series, you get a good amount of basic sense so that you can be easily able to track these things. Yeah, understand these things. Without before without watching those if you come to this video, I believe most of you would not encounter these questions.

### 00:12:56 · Speaker 2

only in the MAG interview because they'll ask you basics first. If you can answer the basics then only they'll ask you advanced, correct? So learn the basics then continue with this advanced videos, okay? Now let me run it and explain the output for each.

### 00:13:08 · Speaker 2

So, for the plus one and the and the this one empty string is actually zero. Okay, unary operator. Plus one and the true is one, plus one, sorry, not plus one, just the plus. Plus and the false is zero. Plus and the string with the value is a not a number. Plus and an empty string is zero actually. Plus and the hello is a not a number. Why these are so, feel free to read in in the description. I'll try to link this also in the video description, okay?

### 00:13:38 · Speaker 2

okay? But these are the points which are quite important for solution that we are writing in our next video, okay? So to summarize. So JavaScript has a limit, uh what we call as the max safe integer, the maximum number that can be safely represented, number one. Number two, anything that goes beyond this, it is good to use bigint, okay? That is the second part. So third part is when to use number and the brackets and when to use the parsint, third point. Fourth point is unary

### 00:14:08 · Speaker 2

operator with plus how it gonna behave. So this is something out of the box not related to the concept but required for my solution that I explain the next video. Okay? So that's all about this video. Please watch my next video. Do not skip it where I'll actually explain you the solution. How to write the code to this problem and solve it efficiently. Okay? So thank you so much for watching. Catch you in the next video. If you are liking the content that I'm making on the YouTube, please do like it and do not forget to subscribe to Uncommon Geeks. Please share these videos with your friends so that they also get benefited.

### 00:14:38 · Speaker 2

okay? I have written lot of beautiful medium blogs where I explain these concepts step by step. I'll link that my media blog in the description. Please read those articles and follow me on medium and my solution whatever I'm I'm gonna write I'll also add that my github. So copy the projects or download the project, use those code and practice them, okay? And give a star to those projects on github. Thank you so much for watching the video. Catch you in the next one.
