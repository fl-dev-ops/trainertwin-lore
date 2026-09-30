---
id: O0GtdIItMhM
title: String.charAt custom implementation (JS Custom Implementation Ep-6)
date: '2022-06-13'
url: https://www.youtube.com/watch?v=O0GtdIItMhM
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. \n\n Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nJavaScript Standard built-in objects: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt\n\
  \n\nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\n\nMedium Blog https://mevasanth.medium.com/ \n\n\nString.charAt from developer.mozilla.org:\
  \ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt\n\
  \n\nJavaScript Function: https://www.youtube.com/watch?v=VaL5lrxX-kY&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=10\
  \ \n\n\nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:08:39
model: saaras:v3
transcript: true
---

# String.charAt custom implementation (JS Custom Implementation Ep-6)

## Transcript

### 00:00:00 · Speaker 1

ऑल, वेलकम बैक टू अनकॉमन गीक्स. मैसेल्फ वसंत. आई होप यू ऑल डूइंग वेल.

### 00:00:05 · Speaker 1

So as you know there's a video series where we are discussing about custom implementation. We have already discussed few custom implementations method related to array, okay? I decide to pick a different prototype, a string prototype in this particular video where I'll be explaining you how to implement a custom string method, okay? The method that I'm picking here is char at, basically it will return the character at a particular location, okay? I'll explain that in a while. So in case if you are someone who directly landed into this video and you have not watched my previous videos, then I would highly recommend please go

### 00:00:35 · Speaker 1

forward and watch at least first three videos in the series. I'll try to link that on the screen also in the description section. So where I've explained how this series is going to be and basics about the prototype, how to add your methods to the prototype. And also first video concat I have made it very elaboratively to explain each bit of the custom implementation. After watching those if you come to this video you will feel very comfortable to going forward. Okay? Without wasting further time let's get started.

### 00:00:59 · Speaker 1

So this is a video series like I mentioned it is a string prototype dot caret method. Caret it refers to character at at a particular index, okay? So very straightforward method. The reason I'm picking this is how to write a custom implementation for any methods other than array. We have only written so far for array. I'll now I'll show you how to do a custom implementation for other prototypes. But it's quite straightforward. I may not continue to do for a multiple prototypes. I'll show what are the prototypes available. You yourself can try writing custom implementation for those methods going onwards.

### 00:01:29 · Speaker 1

okay? So now, so string.prototype.charat, so the what is the charat method? Returns a new string consisting of a single UTF sixteen code unit located at the specified offset of the index. As it is, it is quite difficult to understand the first go. Basically, in very simple words, what it does is, so given a string, index four, the sentence dot the string basically, string.charat index, okay? For example, now fourth index.

### 00:01:59 · Speaker 1

will return the Q. Okay? If you don't pass anything, then it will pick the first character. Okay? What if you pass a negative index?

### 00:02:09 · Speaker 1

Okay, if you pass a negative index,

### 00:02:13 · Speaker 1

just nothing is I mean not not undefined just an empty string is displayed what if you have a upper higher most limit which is not available okay

### 00:02:23 · Speaker 1

Again, you you get a just an empty string, okay? This is about the carrot, what it does. So now you got to know what it does. Now if you come below, the same is been explained here. But there are some additional information about the carrot. What if you have some characters like

### 00:02:39 · Speaker 1

multilingual plane, there are some other characters other than the typical ASCII or the basic characters that we use on a day-to-day basis, like the string format or ASCII code, etcetera. How do you handle that? Non-BMP characters, what they call it, okay? I am not going to touch base much upon all these things because that is not purpose of my video series, but you guys feel free to read and understand about more about this non-BMP characters, okay? Now, without wasting further time, let's get started with the implementation, okay? So I'm copying the same code.

### 00:03:10 · Speaker 1

So I've written this file. Actually this is very very very simple. So I mean even if you are writing the custom implementation for the first time, you'll be easily able to write. So I haven't come prepared anything specific for this video, but I'm damn sure I'll be able to write a proper working code for this. Okay? So now we have

### 00:03:27 · Speaker 1

this one, I just changed it to my channel name, welcome to Uncommon Geeks, okay? The character at an index is a sentence character at the index, okay? So now

### 00:03:44 · Speaker 1

You know, I think all of you know if how to write a add your method to the prototype. If you don't know, please watch my previous videos where I've explained how to add your methods to the custom or or built-in prototype methods, okay? So this is string, so it belongs to string prototype, okay? So my char at and we have a function, okay? So now I'll trigger this my array function from here, okay? It is very very simple this this implementation, okay? So const

### 00:04:14 · Speaker 1

right index. So why I'm checking the right index is what if you don't pass anything in that case I need to pick the index as zero, okay? So if index not equal to

### 00:04:26 · Speaker 1

null. Then use the

### 00:04:30 · Speaker 1

index itself. If index is null, then use the

### 00:04:36 · Speaker 1

then use the index as zero. Okay? Now, if then you have to check one important condition, okay? So,

### 00:04:44 · Speaker 1

you already saw if index is zero. Sorry if right index is if right index is lesser than zero negative index okay basically negative index never exist as you know in array. Or if right index is greater than

### 00:05:04 · Speaker 1

right index is greater than the array length basically. Okay, array I haven't I think or string. const string input string is equals to this. I think most of you know

### 00:05:17 · Speaker 1

what this refers here. This basically refers to the reference with which you're invoking this function. So in this case, this is the sentence. Welcome to Uncommon Geeks. Okay, I've explained this again in my previous videos, please do watch that to get more insights. So input string, okay, if it is greater than input string.length, then return

### 00:05:37 · Speaker 1

this. Okay? This or this. So basically what you are doing here is, in case if your

### 00:05:44 · Speaker 1

there are two possibilities, two extremities. One, an index is lesser than zero, negative index never exist, in that case you send the empty. In index could be greater than the length of the string, so in that case also you will send the empty. Otherwise it is very simple, return

### 00:05:59 · Speaker 1

input string, okay? input string of right index. That's all, correct? So you can actually like an array, you can also put this across the string, the brackets and get the index. If not, you can you can create a for loop and go to that index and return that also. Both works the same way, okay? So now, my character, my character, let me run this. Okay? At four, character four is zero distilling, one, two, three, four.

### 00:06:30 · Speaker 1

zero, one, two, three, four. So it is O, okay? So I'll make the index as four thousand. Technically I should be printing just an empty string.

### 00:06:39 · Speaker 1

So I'm printing empty string. I'll I'll make it negative four thousand in that case also I should be printing empty string. So same is been happening in both the cases, okay? So this was it's a very small video to explain the char at. So this all about this this particular video. See going forward I may not make a video on each and every prototype. So I'll I'll take couple of minutes to explain how you can check the different prototypes and write custom implementation of your own for the practice sake. See this link I'll be adding in the description.

### 00:07:07 · Speaker 1

So these are the different methods for which prototype methods exist. Okay. So one minute. So standard built-in methods, yes. So array, byte, date, then we have many other methods. Okay. So this link I'll add, wherever you see there are prototype methods available, try practicing it on your own. So for example, now I did the carrot. What if you have, you want to write another thing like probably ends with. Very simple. You can just check whether the last character is

### 00:07:37 · Speaker 1

whatever the input passed. So in my example, S is the last character. So they will ask like sentence dot ends with S. Only thing you do is input string of listing's length. Is it the whatever the character passed then you can return. Very simple question. So you need to have a very basic sense of data structure and algorithm. Then all you need is the uh I mean you know the basic stuff. Half of the things already you know how to add your method to the prototype method. Second is the basic logic. So all these methods involve quite basic implementations only.

### 00:08:07 · Speaker 1

So you can read the implementation how they have done and you will be able to do. So only thing is are you able to write an optimal code or not that comes with a little bit of expertise. So you have to practice well to see is there any way to you can optimize then you will be able to write. Okay? That's all about this video. If you like my video please do like this video on YouTube YouTube and share this videos along with your friends. Do not forget to subscribe to Uncommon Geeks and I have written beautiful medium blogs about lot of JavaScript concepts please do read that. Okay? Do not forget to subscribe me me on medium. all about this video. Catch you in the next one.
