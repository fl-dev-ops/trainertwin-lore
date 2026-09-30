---
id: OFJmoIRyqw4
title: Learn Most confusing JavaScript topic Deep copy - Shallow copy - (Ep - 1)
date: '2022-02-26'
url: https://www.youtube.com/watch?v=OFJmoIRyqw4
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Copying a value of one variable to another is considered to be one of the most\
  \ fundamental feature of every programming language. But in JavaScript Interviews,\
  \ even today, most candidates face difficulty in answering questions of deep copy\
  \ and shallow copy. In this video series, I will explain each and every concept\
  \ of deep copy and shallow copy. So, after watching this, in all of your future\
  \ interviews, you will be able to answer all questions of deep and shallow copy.\
  \ \n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains\
  \ questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:09:50
model: saaras:v3
transcript: true
---

# Learn Most confusing JavaScript topic Deep copy - Shallow copy - (Ep - 1)

## Transcript

### 00:00:01 · Speaker 1

Hello all, welcome to Uncommon Geeks. Myself Fazanth. I hope you all doing well. Today's topic is deep copy and shallow copy. Copying a value of a variable from one to another is considered to be one of the most basic feature of every programming language. And JavaScript is no different.

### 00:00:17 · Speaker 1

In fact, deep copy and shallow copy are very straightforward topics. We can easily call them as copy by value and copy by reference. But the problem lies in the number of questions that can be asked around this topic. A very difficult questions can be formed easily in this topic using arrays, strings, object, nesting of object, nesting of objects and functions, which will make candidate very confused during the interview. I've seen those candidate who actually read this topic and came for the interview and they struggle to answer.

### 00:00:47 · Speaker 1

and a small variation of the simple question is asked. So I have taken this topic and I'll be covering in depth and asking all the different questions which are generally asked in the interview so that when

### 00:00:59 · Speaker 0

Such questions are asked for you during the interview, you will be able to answer them very easily. Without wasting further time, let's get started.

### 00:01:06 · Speaker 1

variable is something that is common across all the programming languages.

### 00:01:11 · Speaker 1

In JavaScript as well, we have different ways of copying variables from one to another.

### 00:01:17 · Speaker 1

It is divided mainly into two things, two two ways, one is deep copy and another one is a shallow copy. Okay.

### 00:01:24 · Speaker 1

It's one of the interviewer's hot topic. Most interviewers will ask question around this. uh The reason being it's very easy to create a tricky question in this topic, okay? So I want you to focus and understand this video thoroughly so that when I go to the next video where I'll be asking questions around this, you'll be able to answer it very well, okay?

### 00:01:44 · Speaker 1

without wasting further time, let's get started.

### 00:01:48 · Speaker 1

First let us see what is deep copy. Okay? I'm doing creating a variable x which is of time number and I'm assigning it a value of ten. Okay?

### 00:01:58 · Speaker 1

So I'm creating a variable Y which is also of type number. Y R is coming.

### 00:02:06 · Speaker 1

Okay, the annotation can be only used in TypeScript file. It's like kind of a warning. I don't think we there is any problem with this. Okay. And log

### 00:02:17 · Speaker 1

value of x is x

### 00:02:23 · Speaker 1

and value of y is

### 00:02:27 · Speaker 1

Why? Okay. Let us execute this code. I don't want you to answer because it is very straightforward. You'll be able to answer, I'm aware. Okay.

### 00:02:36 · Speaker 1

uh yeah maybe this annotation cannot be used in javascript so I'm not using okay let me just execute so value of x is ten value of y is also ten okay quite straightforward nothing fancy here because this is something that everyone are using so you people are aware of it

### 00:02:54 · Speaker 1

I'll just make it y as twenty now and rerun the code.

### 00:02:58 · Speaker 1

we got y as twenty. So, uh this is very straightforward, but what I want you to understand is we have created a variable with let x and the value initialized to it is ten. Then we created another variable y and we copied the value of x into it and again we

### 00:03:14 · Speaker 1

added a new value into y and we made it twenty. Okay and so x is ten and y is twenty. Okay. So what I want you to understand here is after you copy x to y and you updated y.

### 00:03:27 · Speaker 1

there is no connection between Y and X. So you copied here, uh X to Y and you are done.

### 00:03:33 · Speaker 1

So putting in other way from the programming constraint. So whenever you do this line, basically the compiler will allocate a memory location to the variable X and it will store the value of ten in that memory location. Okay? And whenever you did this, Y is equal to X, a new memory location is allocated to Y and whatever the value that was there in X, that is ten, is placed in that memory location. So now X and Y point to two different memory location.

### 00:04:00 · Speaker 1

So whenever you change the value of y, there is no connection to x. Okay? This is a deep copy. Why this is called deep copy means after copying the values, there is no connection between the two variables. You are done. So that is deep copy.

### 00:04:13 · Speaker 1

There is another one copy, shallow copy. But before going to shallow copy, I'll tell on which all types you can make a deep copy. Okay? We call them primitive types. Okay? Primitive types you will be able to make a deep copy. That is number.

### 00:04:29 · Speaker 1

number, string, and boolean.

### 00:04:34 · Speaker 1

So these are the three types on which you'll be able to make a deep copy. Okay? Whenever you create a variable with these three types and you copy to another variable of same type, then you'll be you are making a deep copy. Okay? Now let us understand what is a shallow copy or a shallow copy.

### 00:04:52 · Speaker 1

So let array one is equals to one two three four log array one I'm printing array one okay and what I'm doing is array two is equals to array one array two dot push

### 00:05:10 · Speaker 1

five log array two. Okay? Also, I'm logging array one.

### 00:05:18 · Speaker 1

So quite straightforward, I created an array and I added initialized that with a four values of integer type, then I'm logging array one. Then I'm copying array one to array two and for array two I'm adding, I'm pushing a value five as you know push is a JavaScript operation array operation which will add element at the end of the array. So now array two contains five values, five at the end. I'm logging array two, then I'm logging array one again. Okay, let me run this.

### 00:05:44 · Speaker 1

So after running what we are getting is array one we got one two three four which is fine because whatever the value we add into array one that is getting printed here okay.

### 00:05:52 · Speaker 1

And in case of after that we are doing array two is equal to array one. So we copied here. Then for only to array two you have to observe this line here. Only to array two you added the you pushed the value of phi or you added a value phi at the end of the array.

### 00:06:07 · Speaker 1

So we printed array two, it became one two three four five. But even array one if you print after that, that also is be getting becoming one two three four five. Just to extend what I'll do, array one dot push ten I am doing or six I am doing, okay? Then what I'll do, I'll print both the arrays.

### 00:06:27 · Speaker 1

if you want we can make it array one and array two. Okay? Let's see the output. See both the arrays getting updated. So putting other way we whatever the array two variable we created. Okay?

### 00:06:41 · Speaker 1

It is not totally new variable. It is not it is it is not disconnected from R A one. There is some connection. Okay? I'll tell you what is that connection. But before that I'll I'll give you some standard bookish bookish definition for both because some interviewers would expect you to tell a standard definition. So I'm giving you this.

### 00:06:59 · Speaker 1

Deep copy means that all the values of the new variable are copied and disconnected from the original variable, like I already explained. Shallow copy means that certain or sub values are still connected to the original variable. Actually, there is no standard definition for deep copy and shallow copy that is mentioned in developer.mozilla.com.

### 00:07:17 · Speaker 1

different authors have formed a definition according to their understanding, but mainly whatever I've showing you this definition that it means the same, okay? You you are free to tell this in your interview or wherever you want to tell this answer, okay?

### 00:07:32 · Speaker 1

Now I'll I'll explain this with the help of this image much in a very easy way, okay? If you see here,

### 00:07:42 · Speaker 1

We have a shallow clone and deep clone or we can tell you shallow copy and deep copy.

### 00:07:45 · Speaker 1

And for your information, this image is I have taken it from a medium blog. I'll I'll link I will mention that link of that medium blog in the video description. And all the rights of this image goes to whoever has created it. Okay, I'm just using it. So in case of a shallow clone, what's happening is, first let us understand deep clone, original object and referenced object, cloned object and referenced clone. So you can consider like these two are some independent entities. So after you copyright, there is no connection. They have disconnected.

### 00:08:15 · Speaker 1

But for the shallow clone, both the cloned object and the original object basically pointing to the referenced object or in this case, whenever I created let array

### 00:08:27 · Speaker 1

Okay, array one as one two three four. What happened was we were we allocated a four memory locations and starting location was with with was with array. Okay, array one. What is happening?

### 00:08:40 · Speaker 1

whenever you copy array two, whenever you copy array one to array two, basically both refer to the same memory location. So because of which, whenever you modify either array two or either array one, you're technically modifying the same memory location. Due to which, no matter which variable you modify,

### 00:09:00 · Speaker 1

the both arrays are getting modified. So this is a shallow copy. Okay? So I believe now you are clear what is deep copy and what is shallow copy.

### 00:09:08 · Speaker 1

And in the next video I'll be explaining you or I'll be asking you various different questions that can be asked on this topic. But I want you to understand this topic very clearly because ten out of eight interviews definitely they'll ask you some question some or the other question on deep copy and shallow copy. Okay?

### 00:09:26 · Speaker 1

If you liked my video, please do like it on my YouTube channel. If you want your friends also to learn from this, please share it with them. Do not forget to subscribe to our channel, Uncommon Geeks. And I've also linked my medium blog where I've explained

### 00:09:39 · Speaker 1

deep copy and shallow copy. Please do read that so you will get lot of examples handy there so you can just copy and onto your favorite editor and execute them, okay? I'll see you in next video. Thank you.
