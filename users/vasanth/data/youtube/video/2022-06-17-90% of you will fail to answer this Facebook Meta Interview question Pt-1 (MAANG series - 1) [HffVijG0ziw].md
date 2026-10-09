---
id: HffVijG0ziw
title: 90% of you will fail to answer this Facebook/Meta Interview question Pt-1 (MAANG
  series - 1)
url: https://www.youtube.com/watch?v=HffVijG0ziw
date: '2022-06-17'
duration: 00:15:02
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# 90% of you will fail to answer this Facebook/Meta Interview question Pt-1 (MAANG series - 1)


## Transcript

### 00:00:00 · Speaker 1

So let me run the code and show what is happening. Okay. Then I'll tell what are the mistakes that we do in the interview. Okay. So if I run the code, so we are seeing something called 1E plus 42. If you saw this for the first time in the interview, from there itself, half of your confidence will go off because you don't know what is E. You don't know what is plus. You don't know what is 42.

### 00:00:26 · Speaker 1

Welcome back to Uncommon Geeks, myself, Azant. I hope you're all doing well. As you know, this is a playlist or a video series where we are discussing mainly the main questions. The main refers for Meta, Apple, Amazon, Netflix and Google. The most recent questions that are asked in this kind of companies are currently discussed in this video series. So this is a super important video which I have come up with. It's a question that is recently asked in the Facebook. Okay. As I mentioned in the thumbnail, I guarantee 90% at least of you will fail to answer this question correctly.

### 00:00:26 · Speaker 2

Oh

### 00:00:56 · Speaker 1

Okay, so if you prove me wrong, I'll be very happy. If most of you are able to answer in the first quiz, I'll be very happy. But I believe most of you will not be able to answer, including me. I was also not able to answer this question properly. But in the journey of learning the solving this question, I learned a lot of things. Few things which I already aware, but I got to learn that within very much in depth. So it's a super important question, not just because it is asked in the Facebook, but it the amount of thing that involves in the journey. So you have to learn a lot of things to write this problem.

### 00:01:26 · Speaker 1

correctly so this is a this in this video I'll be discussing the question and what are the sub elements required to answer that question okay I will not discuss the solution the solution I'll discuss in the next video but do not skip this video unless you watch this video till the end you will not be able to write the solution or you will not be able to understand the solution that I write in the next video okay so without wasting further time let's get started okay the question is very simple here goes the question

### 00:02:08 · Speaker 1

Yeah. So as you as you saw, the question is very simple. Okay. So given a you have to write a function or there's already a function which takes two strings as an input. Okay. Which are a potential numbers, but in the string format. All you have to do is convert the string into number and add it. Okay. Looks very easy. Okay. I've already written some code so that we won't waste a lot of time. Okay. So this is a function add two numbers that takes number one and number two, which is which takes two numbers as a

### 00:02:38 · Speaker 1

inputs to strings as an input actually which are actually numbers if we can convert them then we have to add and return okay listen this is very easy everyone will be able to write at least with one 1.5 year of experience engineer will also be able to write it correct what is that we just convert the number into a string into a number add it and return correct so i also started the approach in a similar way what i did was i did this maybe most of you would also do the same okay so where i did number

### 00:03:06 · Speaker 1

Number one

### 00:03:10 · Speaker 1

Number

### 00:03:12 · Speaker 1

number two okay this what i did uh so if i run the code i'm getting 23 which is absolutely right 22 plus one is 23 so as you know most of you know number basically converts a string into a integer okay or the number format okay there's another function called parseint so there's a slight difference between parseint and number that also i'm going to explain in a while but basically i converted number into a string into a number and added it and returned the sum okay if you want you can make it a two-step process by making

### 00:03:42 · Speaker 1

number one number two sum and then return it if you are uh just starting with but basically you end up doing the same thing

### 00:03:49 · Speaker 1

just slightly uh extend the problem okay uh and in case this question is asked to you in the interview don't write a solution like this especially if you're appearing for the companies like facebook apple whatever the man companies okay thing is you have to ask as many questions as possible to the interviewer to make sure you are going in the right path they expect that they will not give you all the things you have to understand the reading between the lines and you have to ask so number one question so what is the maximum limit that number one or number two can

### 00:04:19 · Speaker 1

be so you we if you don't ask the question interviewer will not tell he thinks you already gauge that in your mind and you're writing the code

### 00:04:27 · Speaker 1

To extend the problem what I'm doing is

### 00:04:31 · Speaker 1

Let me just increase the number

### 00:04:35 · Speaker 1

Now guess the output what will be the output

### 00:04:39 · Speaker 1

So I see now there are two broad category of evers. One category of evers are like in a state where you're thinking this is plus one. Let's say let's it was just 99 plus 100. So whatever this number stands for, that kind of 100, like next number it is going. OK, I mean, it will become one here and remaining these many digits of zero. Some are thinking in this direction. Some got now fully confused. You thought that was the answer, like one followed by all the zeros. But now so much of a,

### 00:05:09 · Speaker 1

Big number what will happen

### 00:05:12 · Speaker 1

So these are the two broad category of the people. So I was also one of this. I thought the same thing, like it will become one followed by all the zeros. But then again, the doubt is running in my mind. What if so much such a big number, can it be added in JavaScript or not? Correct. So let me run the code and show what is happening. OK, then I'll tell what are the mistakes that we do in the interview. OK, so if I run the code. So we are seeing something called 1e plus 42. If you saw this for the first time in the interview from

### 00:05:42 · Speaker 1

There itself, half of your confidence will go off because you don't know what is E, you don't know what is plus, you don't know what is 42. So half of your confidence is gone as soon as you see this and you will not be able to write the further solution. So what are the mistakes that I did in this, this, at least till this point in the interview? Number one, I thought I came with a prejudice and I started writing the code assuming this number will be able to convert any string into a number, correct? Which was wrong. Second, I did not ask the interview.

### 00:06:12 · Speaker 1

What is the length of number? What is the maximum length of number? What is the minimum length of number? What if number one or number two can be empty? In that state, how to do? Let's say I'm not passing this number. In that case, what is the default value? So these are the questions that I did not ask for the interview. So which you have to ask and make sure that you have all the information required before starting the solution.

### 00:06:34 · Speaker 1

Let me explain what is happening here. This is a very large number. I even I nobody I think most of you are including me also will not be able to tell what is number like 9,999, something we don't know what is the number. It's very big number. So now here at least I'll tell you what is E plus 42 stands for. E plus 42 stands for 10 power 42.

### 00:06:54 · Speaker 1

10 power

### 00:06:56 · Speaker 1

So one star ten power forty two

### 00:07:00 · Speaker 1

doesn't make any difference basically 10 power 42 will be 10 power 42 only that is the big big number that we formed from this computation so javascript is not representing that in the number format rather it is representing that in a 10 power format so e refers here that okay first we should know this now there are some more very very interesting thing that you need to know that i'll explain from the official documentation

### 00:07:23 · Speaker 1

Very first, there is something called max safe integer. Okay. Frankly, these are the terminologies I also learned when I started solving this problem. Okay. So I want to explain all of these things to you guys first before I start the actual coding. Okay. So max safe number, the number dot max safe number constant represents the maximum safe integer in JavaScript. So what is the maximum number that can be safely represented as number in JavaScript? Okay. So here if you see 2 power 53 minus 1 is the max.

### 00:07:53 · Speaker 1

safe integer so if you run here so this is the number max safe number so here they have done plus one plus two etc but even if you don't do the log basically is pointing printing just the max safe number if I run so this is the maximum safe number two power 53 minus one so this is the number that can be represented as number in JavaScript anything beyond this correct anything beyond this it will be slightly difficult to represent in the number format so what they do is they try to represent in some other format

### 00:08:23 · Speaker 1

etc okay that whatever the acronym you saw so that basically explained in this documentation okay so where

### 00:08:32 · Speaker 1

Different types of numbers are notated. As you can see here, one is with E and there are some octal numbers, there are some hexagonal numbers. How those numbers are actually converted also is explained in this documentation of parseint. I'll link that also in the description. Also, I want to explain you what is the basic difference between parseint and number. So I've taken this from this, this, that, dot, Dave. So I thought it is useful. So share here.

### 00:08:57 · Speaker 1

number you already saw which was converting the string into a number. Parsint also does a similar thing. Why I'm explaining this is an interviewer ask you why you are not using Parsint and why you are using number. So you should know the explanation to explain you should know the difference, correct? So Parsint basically number converts the type whereas a Parsint parses the value of input. It tries to parse the input. If you see here 32 pixel Parsint is passing that into 32. Same pass to the number. Number is converting that in not a number. So 32 pixel

### 00:09:27 · Speaker 1

cannot be converted to number from string to number it is not not possible correct parse int will kind of parsing it trying to iterate through it and try to extract the value out of it okay so in our example can we use the parse int instead of number yes there was no problem okay but usage you got to know when to use parse int and when to use the number

### 00:09:46 · Speaker 1

Let me get back to this again, the safe integer. Okay, now here. There is a, for a larger number, consider using a begin. There is something called begin, which is exceeding the max safe integer. If it is exceeding the max of integer, so there has to be some data type that can hold these big numbers, correct? So that is actually a begin. So begin is a primitive wrapper object used to represent and manipulate primitive begin values, whereas too large to be represented by the number.

### 00:10:16 · Speaker 1

So anything that cannot be represented by number can be represented easily with the help of big inter

### 00:10:23 · Speaker 1

begin can be used in types in term whenever you're trying to do the computations like this whatever you saw very big numbers okay so to come back here rather having a number if you use the begin

### 00:10:36 · Speaker 1

begin here also begin

### 00:10:39 · Speaker 1

See you got the solution

### 00:10:42 · Speaker 1

So getting the solution here, but the problem is interviewer will not be expecting you to use the begin because he knows the begin will give you the solution, correct? But you should be able to write without using the begin, okay? So now we got to know when to use the begin, correct? And about regarding the solution. One last thing I want to explain is unary plus operator, okay? This is not relative directly to any of the concept I explained, but this is important for the solution that I write in the next video, okay?

### 00:11:12 · Speaker 1

if most of you would not know the output for this okay that is the reason i'm explaining this here so so we have a console.log plus plus a string unity plus and the string and few more unity plus but true false and hello if you know the answer to this please pause the video mention that in the comment section i believe most of you would not be will not know the answer to this okay in fact id also did not knew i ran it i understood why it is printing so okay so i thought of explaining that as a part of this video

### 00:11:42 · Speaker 1

Before I run this in case if you are someone who is preparing seriously for the front end developer interview whether it is for Mang or for any other companies so JavaScript is one of the core fundamental skill set for the front end developer interviews

### 00:11:56 · Speaker 1

I have prepared two beautiful series. One contains 20 plus videos with lot of basic questions, normal questions that are asked in the front end development interview and how to solve it. And what mistakes you generally do, how to tackle it. So that series I'll add in the somewhere on the screen also in the description section. I'm at another series where I explain a lot of custom implementations. This has become very trendy question in the interview where they'll ask you to implement your own implementation for the built-in methods like write a custom implementation for array.map.

### 00:12:26 · Speaker 1

map behaves you have to write a function that behaves in a similar way so that also written in the description also in the screen okay please watch those two video series okay then come to this max series the reason why i'm saying max series is kind of an advanced level of interview correct if we hear it it discusses a quite complicated questions so after watching those two series you get a good amount of basic sense so that you can be easily able to track these things yeah understand these things without without before without watching those if you come to this video i believe most of you would not encounter these questions only in the manga

### 00:12:56 · Speaker 1

interview because they'll ask you basics first if you can answer the basic then only they'll ask you advanced correct so learn the basics then continue with this advanced reviews okay now let me run it and explain the output for each

### 00:13:09 · Speaker 1

So the plus one and the and the this one empty string is actually zero okay unary operator plus one and the true is one plus one sorry not plus one just the plus plus and the false is zero plus and the string with the value is a not a number plus and an empty string is zero actually plus and the hello is a not a number why these are so filthy to read in the description I'll try to link this also in the video description okay but these

### 00:13:39 · Speaker 1

The points which are quite important for a solution that we are writing in our next video, okay? So, to summarize.

### 00:13:46 · Speaker 1

JavaScript has a limit, what we call the max safe integer, the maximum number that can be safely represented, number one. Number two, anything that goes beyond this, it is good to use begin int. Okay? That is the second part. The third part is when to use number and the brackets and when to use the parse int. Third point. Fourth point is unary operator with plus, how it's gonna behave. So this is something out of the box, not related to the concept, but required for my solution that I explain in the next video. Okay?

### 00:14:16 · Speaker 1

So that's all about this video. Please watch my next video. Do not skip it where I'll actually explain you the solution how to write the code to this problem and solve it efficiently. Okay. So thank you so much for watching. Catch you in the next video. If you are liking the content that I am making on the YouTube, please do like it and do not forget to subscribe to uncommon geeks. Please share these videos with your friends so that they also get benefited. Okay. I have written a lot of beautiful medium blogs where I explain this concept step by step. I linked that my media blog in the description. Please read the

### 00:14:46 · Speaker 1

articles and follow me on medium and my solution whatever i'm i'm gonna write i'll also add that my github so copy the projects or download the project use those code and practice them okay and give a start to those projects on github thank you so much for watching the video catch you in the next one

