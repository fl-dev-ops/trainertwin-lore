---
id: _iv8bapMLDg
title: Accept the challenge !! answer 3 questions on Deep copy - Shallow copy Part
  - 1 (Ep - 2)
date: '2022-02-26'
url: https://www.youtube.com/watch?v=_iv8bapMLDg
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Copying a value of one variable to another is considered to be one of the most\
  \ fundamental feature of every programming language. But in JavaScript Interviews,\
  \ even today, most candidates face difficulty in answering questions of deep copy\
  \ and shallow copy. In this video series, I will explain each and every concept\
  \ of deep copy and shallow copy. So, after watching this, in all of your future\
  \ interviews, you will be able to answer all questions of deep and shallow copy.\
  \ \n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains\
  \ questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nDeep\
  \ copy and Shallow copy part 1 - https://youtu.be/OFJmoIRyqw4"
author: careerwithvasanth
duration: 00:10:04
model: saaras:v3
transcript: true
---

# Accept the challenge !! answer 3 questions on Deep copy - Shallow copy Part - 1 (Ep - 2)

## Transcript

### 00:00:00 · Speaker 1

Welcome back to Uncommon Geeks. This is a continuation of my previous video where I had explained you what is deep copy and shallow copy. In this video, I'm going to extend it by asking you some interesting questions on deep copy and shallow copy, which are generally asked during the interview and how to tackle it. Okay?

### 00:00:16 · Speaker 1

If you have not watched my previous video, I would highly advise, please go back and watch it. The reason being, there I have explained you all the concept and here it's application of it.

### 00:00:26 · Speaker 1

If you have not seen that video, then it will become slightly difficult for you to answer the questions here. Okay? The link for the video I'll try to attach in the description, also somewhere on the screen as well. Please go ahead and watch it. Okay? Without wasting further time, let's get started. Question number one. Okay? So in question number one, uh so make a deep copy. So if you are someone who are fast attempt to understand the question and you know the answer, go ahead and mention question number one and put your answer in comment section. Continue watching to ensure whatever you answered is correct.

### 00:00:56 · Speaker 1

So question here is we have an array one and array two. I am assigning array one to array two and I'm adding a value at the end of array two and I'm printing it here. Same as the example that we saw in our last video. Let me execute this. So what is happening is

### 00:01:12 · Speaker 1

array two and array one are getting ten at the end of them. Okay, as you can see here. Though we had added ten only to end of array two, it is also getting added to end of array one also. So putting in very simple terms,

### 00:01:27 · Speaker 1

This behavior is not intended or it is making a deep copy where it's making a shallow copy where we want to make a deep copy, okay? We want to array two and array one.

### 00:01:37 · Speaker 1

to be disconnected. Okay, because that is how most of the day-to-day programming happens where even the reference type like arrays and objects, we want to make a deep copy. Okay. So, question is simple. In this line where a shallow copy is happening, convert that into a deep copy. If you know the answer now, at least you can go ahead and answer it in comment section. If not, I'll tell you how to make a deep copy. Okay. It is quite straightforward using the spread operator. Okay. Let me run this.

### 00:02:03 · Speaker 1

So you know now only array two got updated and array one did not get updated. So this is because of spread operator. What is spread operator? Spread operator was introduced in JavaScript in ES two thousand fifteen. What spread operator does is whenever you are using the spread operator it takes contents of the entire array one creates a new object or new array and assigns that into array two. So it makes a deep copy okay because of which array one and array two are disconnected now. Okay. So this was the question and you answered it. Now let us go to the second question. Okay?

### 00:02:39 · Speaker 1

similar to the above question but it is I can say slightly complicated but you should be able to answer it okay. Question number two. So what I'm doing here is instead of an array I'm using an object here. The reason I'm using object here is in most of the interviews interviewer will ask you object instead of an array. The reason being

### 00:02:59 · Speaker 1

very difficult to in in in object it is very easy to create a difficult question. So most interviewer would prefer objects. Okay? So user one has been name and a channel. What is happening is we are assigning user one to user two and we are changing user two's name and printing user two object and user one object.

### 00:03:17 · Speaker 1

So what output what we are getting is, though we changed only user two dot name, even user one dot name also got changed, as you can see here. You know this already, this is because of the shallow copy. How to overcome this? So my question is straightforward again, how you will solve this problem? If you know the answer, please do mention that in comment section, if not I'll tell you. So you already know the spread operator, okay? Let us spread this.

### 00:03:42 · Speaker 1

Let us spread this and see the output. Yes. So we're getting the output.

### 00:03:47 · Speaker 1

uh only the user two is getting changed and user one has no effect. So user one and user two are disconnected by using the spread operator. Some interviewer will be definitely happy by this but some still want to check your basics. So they will ask you candidate are there any other ways we can make the same same thing or how to achieve a deep copy.

### 00:04:07 · Speaker 1

without using spread operator. Yes, there is a way, let me tell you that. Okay? There is a simple way of using object.assign, okay?

### 00:04:18 · Speaker 1

and put user one here.

### 00:04:22 · Speaker 1

and run the code. Okay? Getting cool, Vasanth and Vasanth. So basically, user two and user one are disconnected even with object.assign approach. Now let me tell you what object.assign does. Basically, object.assign and spread operators are does the same job. In fact, spread operator is a successor of object.assign. So wherever object.assign was used before, now most of the places programmers use the spread operator. Okay? There are various other other areas also where object.assign can be used.

### 00:04:52 · Speaker 1

but I'm not going to explain that in this video. But for this video you can understand it like this object dot assign will also help you to make a deep copy. Okay? Now let's go to question number three.

### 00:05:08 · Speaker 1

Question number three, slightly complicated. So if any one of you have already worked on deep copy and shallow copy and able to predict the output of this, straight away go and mention question number three and your answer, okay? Uh if not, I'll explain you the question.

### 00:05:23 · Speaker 1

सो वी हैव क्रिएटेड एन ऑब्जेक्ट कॉल्ड यूजर वन हू हैज़ अ नेम एंड अ चैनल एंड हिज़ लोकेशन

### 00:05:29 · Speaker 1

city and state. Location is an object inside user one object which has city and state as its key and values. Okay? What I'm doing is I'm assigning user one to user two and user two's location dot city I'm changing to Mysore and I'm printing both. Let me show you the output.

### 00:05:47 · Speaker 1

What's happening is even though we are changing user two city, user one's city is also getting changed. Okay, you already know this happening because of the shallow copy. How to make a deep copy, that also you are aware using the spread operator. Okay, let us use the spread operator. Save it. Run it.

### 00:06:05 · Speaker 1

So, interesting thing to observe here is, even though use the spread operator, city is still Mysore.

### 00:06:12 · Speaker 1

though you wanted only to change the user tools location.city, even user one's location.city has also got changed. How to solve this? So there is a, you know, if if this one is not working, you know another way as well, that is object.assign. Okay, let me show you that also.

### 00:06:33 · Speaker 1

Let me run this.

### 00:06:35 · Speaker 1

still it has been Mysuru only. The value has not changed. So...

### 00:06:41 · Speaker 1

Whether you use object.assign or the spread operator, it did not work. Just for those of you who still not understand, let me just tweak it a bit. I'm doing user two dot name as cool Vasant. Okay? Let me run this.

### 00:06:55 · Speaker 1

So if you observe now only user two's name got changed, user one's name did not get changed, okay?

### 00:07:03 · Speaker 1

But the same did not happening for the location. Correct? So why this is happening? Now you might have understood a bit. You are able to change these values are deep copied but this is getting shallow copied. That means if the object is nested, I mean there if there is an object inside an object then

### 00:07:23 · Speaker 1

whenever you use object.assign or the spread operator, it is not making a deep copy of inside objects. Okay? due to which both objects, user one and user two, still point to same object location. So if you change the user two's location, user one's location also getting changed. So how to solve this problem?

### 00:07:42 · Speaker 1

So easiest way to solve this problem is with this.

### 00:07:46 · Speaker 1

Let me show you. First let me let the code, then I'll explain how.

### 00:07:55 · Speaker 1

Okay. Let me execute this.

### 00:07:58 · Speaker 1

Yeah, so now only the user two city became Mysuru and user one city is still Bengaluru. Okay? So we achieved what we wanted. Now let me explain you what JSON.parse JSON.stringify does. See, JSON.stringify will convert an object into a string.

### 00:08:12 · Speaker 1

json.parse will convert a string into an object. So technically, whichever the form that user one was there before, it is going to be same after this operation also. Only difference is json.parse and json.stringify will make a deep copy of the variable user one. Okay?

### 00:08:30 · Speaker 1

not just the outer objects, even the inner objects. So whatever there in inner objects or nested objects, even they are also deeply copied. Due to which now user two and user one are disconnected.

### 00:08:42 · Speaker 1

But there are still some areas where we cannot use JSON.pass and JSON.stringify to make a deep copy that I'll explain in the next video because we are somewhat close to the nine minutes and I don't want to stretch this video. Okay? I I believe you have understood the various different ways of making a deep copy of objects and arrays.

### 00:08:59 · Speaker 1

So using spread operator, using object.assign and using JSON.pass and JSON.stringify, I just have to say one last thing here. Many people think JSON.pass and JSON.stringify is not a standard approach, it's a jugaad approach. But it is not like that. JSON.pass and JSON.stringify is a good approach that you can use for the nested objects deep copying.

### 00:09:17 · Speaker 1

इट इज बीन डॉक्यूमेंटेड इवन इन डेवलपर डॉट मॉज़ेलो डॉट कॉम ऑन हाउ टू अचीव अ डीप कॉपी ऑफ नेस्टेड ऑब्जेक्ट्स।

### 00:09:23 · Speaker 1

So, whenever you encounter a scenario like this, feel free to use JSON.PASS and JSON.stringify. There is nothing wrong with that. Okay? If you like my video, please do like it on YouTube. If you want your friends also to get benefited by this channel, please do share the channel with them. Do not forget to subscribe to our channel, Uncommon Geeks. And I'll try to add my medium blog links related to this in in the description. Please do watch, read that, because if somebody, if you are someone who wants to read it rather than watching the video, you can read it quickly there. I'll also try to get a GitHub repository

### 00:09:53 · Speaker 1

all these questions so that you one stop you'll be able to get all the questions and practice on your own. That also those that link also I'll try to add it in the description. Okay? Thank you so much for watching. I'll catch you in the next video.
