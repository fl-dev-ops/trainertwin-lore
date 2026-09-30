---
id: FqvB_MBJae8
title: Don't ignore this JavaScript Interview Question, Array.Filter (JS Custom Implementation
  Ep-6)
date: '2022-06-12'
url: https://www.youtube.com/watch?v=FqvB_MBJae8
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. \n\n Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\n\nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\n\nMedium Blog https://mevasanth.medium.com/ \n\n\nArray Flat from developer.mozilla.org:\
  \ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter\n\
  \n\nJavaScript Function: https://www.youtube.com/watch?v=VaL5lrxX-kY&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=10\
  \ \n\n\nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:09:22
model: saaras:v3
transcript: true
---

# Don't ignore this JavaScript Interview Question, Array.Filter (JS Custom Implementation Ep-6)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Vasanth. I hope you all doing well. So today's video, as you know, we already discussing about custom implementation throughout this playlist or series. So this video, I'll be explaining mainly about array.filter method, okay? Array.filter is again one of the very, very common interview question in the custom implementation, asked in lot of companies, okay? uh But it is not that difficult to write array.filter. If you we have already written the functions for array.concat and array.map, very similar to that, okay? I think most of

### 00:00:30 · Speaker 1

you will be able to write it on your own even before I explain, okay? I'll just break it break down the question for you so that you will be able to try it on your own, okay? This consider this video more like a practice session than I explaining everything, but I'll also write, okay? Now, array.prototype, the filter method creates a new array with all elements that pass the test implemented by the provided function definition, okay? So that means you have one, two, three, four, five, six. So if element greater than twenty, so in this case it is empty. If I make element greater than two,

### 00:01:00 · Speaker 1

इट विल गिव थ्री फोर फाइव सिक्स। दिस इज नॉट द डिफॉल्ट एग्जांपल दैट वाज़ देयर हियर। दे हैड गिवन वर्ड्स लेंथ। आई विल जस्ट चेंज इट टू नंबर फॉर इजी एक्सप्लेनेशन। ओके? नाउ।

### 00:01:10 · Speaker 1

Accept this, uh, most of the things are same as that of uh map method. It takes three arguments, the callback, element, index and the array itself, okay? In case if you are someone who directly landed in this video of my custom implementation, I would highly advise watch at least first three videos of mine. So where I have explained introduction about the series, what are prototypal inheritance, how to use prototype methods, add your method to prototypes, okay? Then in the concat method where I have taken lot of time to explain lot of process step by step. After the

### 00:01:40 · Speaker 1

video straight away you can come to this video and continue. Because I assume you know many things. If you don't know then it will become difficult for you to get along. Okay? Now, I'll copy this, go to my favorite editor, Visual Studio Code, okay?

### 00:01:54 · Speaker 1

And here I'm typing, okay? So this was array.map method which I returned a custom implementation. The reason I'm opening this is, uh most of you might know how array.map behaves. Basically it takes an array as an a callback as an input, correct? Performs some actions.

### 00:02:12 · Speaker 1

whatever the callback is returning, it will push that value into an array. Finally, it returns that array. Similar thing what is happening is with respect to filter also, as you already saw in the explanation, correct? Or in the official documentation. Let's try to mimic the same behavior. Why I'm showing this is this would be my thought process if this question is asked in the interview. So I have have I implemented something a similar flow which where the custom implementation takes a callback method? Yes, I have implemented it. Where map. Can I try to use the similar behavior here?

### 00:02:42 · Speaker 1

yes. So I'll be using that. Okay? So let's not copy the code. Let's try to write from the beginning. Okay? So array.prototype.myfilter. Okay? Then we have an anonymous function.

### 00:02:58 · Speaker 1

If you don't know anonymous function, as always I will try to link that on the screen also on the description, please watch it. Before I write my custom implementation, if you are someone who is preparing for JavaScript driven interviews, React, Vue, Angular, Node, any other JavaScript text stack, you need to be very strong with JavaScript fundamentals. And you need to know what are the most common questions that are asked in the interview. I have made one specific series dedicated for most common interview questions and how to tackle them. I'll try to link that somewhere on the screen, also in the description section. Please go ahead

### 00:03:28 · Speaker 1

and watch that entire series. This is not something bushing around. It will straight away come to the topic, the question and how to answer it. Even if you lost that some information about the topic, I'll give an introduction about the topic, get into the topic and I'll ask you the question and what mistakes you do and I'll help you to solve them. Okay? So please watch that. Now let's continue with this video. Now, same similar to array.map method, what we need first is we need the input array.

### 00:03:56 · Speaker 1

const input array, okay, const input array is equals to

### 00:04:04 · Speaker 1

this. Okay? And I think most of you understood what this function here doing. Basically it just filter nothing but it will check the values and if a particular condition is met then return that value otherwise it will ignore. Like in this case only two three four five six meet the three four five six meet the condition that is element greater than two. Okay? Unlike map all values are not returned in this case. Only those values that meet the condition basically filtering as the word means only those are being returned.

### 00:04:34 · Speaker 1

okay? So now input array is this, then you need also need a const output array or just the output, okay? Then you have a for loop that runs till the length of the input array.

### 00:04:46 · Speaker 1

And as you can see here, you have a callback or a function that is passed the input to the filter method, correct? So you have a callback that you are reduce my filter should take. You will call that callback method from inside the for loop by passing the value, okay, input array of I. And very simple after this, you just concatenate or you just push values of this callback into the output. So, Vasanth, what is it?

### 00:05:16 · Speaker 1

returned. You're trying to push a value of callback into the output. At last video I clearly explained how arrow functions return the value. If not in very simple words, the value whatever is been condition is meant that value itself is returned from this callback that we are using here. Finally I would return the output.

### 00:05:33 · Speaker 0

Okay

### 00:05:34 · Speaker 1

Let's see if I make any mistake. I haven't come fully prepared for this video, but I know the map. I'm trying to mimic the same behavior here as well, okay? So three, four, five, six. I think even the this also will give the same. I'm sorry. I did not pass my filter at all, okay? Let me execute. Ha. Okay?

### 00:05:55 · Speaker 1

What we are getting now is false false true true true something we are getting. Correct? Num dot my filter. This mistake I did intentionally, okay? Not I did it by miss. What we are trying to do here is we are calling the callback method. If you observed what I show in the map method and here, we did the same. Correct? Then definitely we we are not mimicking the filter method here. We are mimicking the map method itself. Correct? So,

### 00:06:25 · Speaker 1

If you see in the map method, we did the same. We called the callback, got the output and we pushed the output. Same if you are trying to do here, then it will not become filter, correct? The purpose I wrote this code is to demonstrate how we do a mistake by thinking two things are similar. You thought map and filter are similar, yes they are similar, but there is a problem if you don't understand what is uniqueness about this function, correct? Now.

### 00:06:51 · Speaker 1

What we need to do here is basically for every input value you need to check does it meet the strict condition. Correct? Like input array of three is it greater than two? Yes. Then only push the value into output. Don't do it for all the things. Correct? Now why false false two two coming is different thing. Why it is coming is every time you are passing the value it is checking whether element is greater than two. I mean that check condition it is checking it is returning true and false. First two cases first it will pass

### 00:07:21 · Speaker 1

one one is greater than two false. two is greater than two false. rest all it is true. So you are not getting the value array you are getting a boolean which is written from this callback. Correct? So what you need to do now is

### 00:07:37 · Speaker 1

rather pushing like this, what you do is, you will check if

### 00:07:43 · Speaker 1

callback of input array is returning some value. So in this case, see in last four cases it returned true, correct? In such cases, you push the value of input array.

### 00:07:56 · Speaker 1

Okay

### 00:07:57 · Speaker 1

Before running, I'll explain this again. So we have array.prototype.myfilter method. These two you already know. We are running a running a loop till the till the end of the input array and we are calling the callback method in this case this, okay? For each input array, we are checking does the callback method returns a value? Correct? If it returns a value, that means if it is meeting a condition, element greater than two, if it is true, then push the value into the

### 00:08:27 · Speaker 1

output array, correct? Push the value into output array, not the whatever return from here. Return from here will be boolean. We are just checking condition. Two is greater than two will be return true or false. Two is greater than two will never return two or zero, correct? So we are pushing the value, finally you are returning the output. Let us run this now.

### 00:08:44 · Speaker 1

See you got three four five six. I made a mistake intentionally then I overcome the mistake just to demonstrate how a similar concept that we think will make you do a mistake in the interview. Okay. Thank you so much for watching this video. If you like my video please do like it on my YouTube channel. Do not forget to subscribe to Uncommon Geeks.

### 00:09:05 · Speaker 1

And please, please, please, please share these videos with your friends. Let them also watch the videos and get benefited because of this. And I've written lot of medium articles about different JavaScript concepts. I'll try to link my medium blog also in the description. Please do watch it. Follow me on medium, okay? Thank you again. Catch you next week.
