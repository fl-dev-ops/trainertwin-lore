---
id: 5Z6tpdmtzG0
title: Learn LinkedList in JavaScript in 40 mins (LinkedList Introduction)
date: '2022-07-10'
url: https://www.youtube.com/watch?v=5Z6tpdmtzG0
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Often most frontEnd developers consider DS/Algo as one of the tufts topics to\
  \ understand. They also get rejected in a lot of interviews, because of this. To\
  \ overcome this problem and help all frontEnd developers to pursue their dream job,\
  \ I have come up with detailed DS/Algo Tutorials in JavaScript. I will be covering\
  \ all the common data structures and problems around that in this video.\n\n\nIntroduction\
  \ to DS/Algo in JS: https://youtu.be/DkarkyD-LkQ\n\nHow add custom methods to JavaScript\
  \ Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s \n\n\nHow to write\
  \ custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\n\nMedium Blog https://mevasanth.medium.com/ \nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:11:42
model: saaras:v3
transcript: true
---

# Learn LinkedList in JavaScript in 40 mins (LinkedList Introduction)

## Transcript

### 00:00:00 · Speaker 1

first if you create, let's say you will use this memory location first, the one. Then, then you will not use two, you will use the second memory locations. So let's say you stored ten value ten here, okay? Then you have stored value twenty here, correct? And you have a link from this to this.

### 00:00:21 · Speaker 1

Welcome back to Uncommon Geeks. Myself, Asant. I hope you all doing well. As you know, this is a video series where we're discussing about data structure and algorithm. I've already made one introduction video. I've clearly explained how difficult or how painful the data structures and algorithm for front end developers and how this series is going to be. Please watch the introduction video if you have not watched so that you'll be more prepared mentally when coming to this video. Okay? So, what is this video is about? So, this video is about introduction to linked list. Okay? So, one important trivia I'll tell. Actually, JavaScript

### 00:00:51 · Speaker 1

doesn't have a link list of its own. Okay? What do I mean by that? So why JavaScript doesn't have a link list of its own? Somewhere in the video I'm going to decode that. So this is also one of the very important interview questions. So please do watch the video till the end. Okay? Without wasting further time, let's get started with the link list introduction. Okay? I've created a I've created a small presentation, okay? To show about the link list. So I'm just starting with that. So link list is a linear data structure in which elements are not stored at a contiguous memory location. The elements in a link list are linked using the

### 00:01:21 · Speaker 1

pointers. So this definition is not mine as most of you guess. This I've taken from the gigs for gigs. And this is a typical definition anybody would write similar. So since I have read by already many so I tried taking it from some all the crates gigs for gigs. So now this what is link list, okay? In very simple words, so you have a memory chunks, okay? But they are not in a contiguous location, they can be accessed within the link list. How? I'm going to explain in in a while, okay? Next. So why link list, correct? So you know what is link list at least basics now.

### 00:01:51 · Speaker 1

Now why linked list? Linked list offers some important advantage over other linear data structures. Unlike array, they are a dynamic structures. Resizable at run time. Also the insertion deletion operations are efficient and easily implemented, okay? Why this is? Why they are better than array in some cases? Let me explain you that, okay? So, so this is a sketch that I have already prepared some rectangles for you to represent a memory locations, okay? So here if you see we have one two three four five. Let's say we have

### 00:02:21 · Speaker 1

five memory locations. As you all know, array is a contiguous memory allocation, correct? Array means you have a chunk of block already allocated. There are dynamic arrays, but mostly arrays are static. So you would use array when you know the size of whatever you are processing, correct? Let's say the number of students in a class or number of employees in an org, they are not dynamic, they are static, you know. Whenever they grow, then probably you link is the arrays. That's how it is done. Arrays are generally picked for the static size, correct? So now let's say you have an array and you needed a five memory location.

### 00:02:51 · Speaker 1

for the array. What would the compiler do or how generally execution works is they'll the compiler or the system would look for five memory locations that are continuously available. Let's say int, I think it is eight bytes. So four values means thirty two bytes. So anywhere thirty two bytes are readily available, then that particular chunk is allocated for the array. So what is the advantage? So even before the program starts execution, the memory location allotted. So it is very fast. Because you don't have to look for the location, correct? Whereas link list, so let's say it needs now

### 00:03:21 · Speaker 1

actually the linked list has nothing called a predefined size it's going to be dynamic. So wherever the space is available it will be keep picking that. Correct so so linked list can better utilize the memory compared to the array. So there are disadvantages too that I'm going to explain in a while. So look at this one let's say there are five memory locations. Okay. So like I said if array wanted now five memory locations you have only five locations here. Out of which the second location is already picked by somebody. Okay. If second location is already picked by some some other processing now array can be created either for

### 00:03:51 · Speaker 1

one location like one element array or three element array. You cannot create five element array, correct? So now. So now but you have to utilize the memory well, correct? Because you you cannot leave the memory like that, you have to utilize it well. So what you will do? You will create a link list. So link list if you create, let's say you will use this memory location first, the one. Then, then you will not use two, you will use the second memory locations. So let's say you store ten value ten here, okay? Then you have stored value twenty here, correct?

### 00:04:21 · Speaker 1

and you have a link from this to this. and then you have a link from this to this. then you have a link from this to this. okay? then let's say due to some operations the memory location two got free. okay? so in that case let's say let me decolor it. so let's say due to some reason uh this one also become free. so let me give some gray color. so due to some reason the memory location two also become free. what you can do in that case from five you can link back to two. okay?

### 00:04:51 · Speaker 1

store some memory let's say forty fifty sixty some number you can store here as well okay guys if not for anything at least for my effort to do this drawing or creating this one you should please like my videos and subscribe to my channel and common geeks okay now please please do that if you're not already done so that will definitely motivate me to make make more good content okay so now so if you look internally so one three four five and two it looks like quite jumbled correct but from the program perspective if you don't know what is

### 00:05:21 · Speaker 1

happening in the inside or in the hardware, correct? But we know what is we only know that all memory locations whatever we are requesting is available to us, correct? So one three four five two we are able to access that and write the code, correct? So that is the beauty so anywhere the memory is available so link list can actually go and grab that memory and store the values, correct? So that is the beauty of link list.

### 00:05:43 · Speaker 1

Now, I was telling one point where the linked list is is not a data structure or typically how linked list is persona linked list persona in other language and JavaScript was different. Why? See, JavaScript or let's take an example of Java or C++ where the programs are written in a compilers, correct? And the in in the any editor and they directly interact with the hardware with in Java there may be some middle engine but technically they directly interact with the system hardware, correct? See as the C compiler is interact with the

### 00:06:13 · Speaker 1

Java has uh Java Java C etcetera which will interact with the device compiler or the system hardware directly. But JavaScript is not like that. JavaScript runs on a browser, correct? Now I run generally with the help of Node server but Java is prepared to run on a browser, correct? Browser is a software. So browser is a software has access to the hardware. But JavaScript as a programming language has no direct access to hardware, correct? So how JavaScript can get the memory location and try to link it?

### 00:06:43 · Speaker 1

that doesn't happen. So this is very very important concept you have to remember. In JavaScript all the data structure operation we do are kind of mimicking the behavior because finally JavaScript everything is object in JavaScript, correct? So even the link list has to convert into an object in JavaScript to work well. So I'm going to explain that now how it going to look like in JavaScript, okay? Now, let's go back to the presentation.

### 00:07:08 · Speaker 1

See, this is a typical singly linked list structure. So we have a value, we have a link. You already saw this from a sketch example. So link is one in this case, the value is ten. So link is twenty in this case and the link is three in this case and the value is thirty. Value is twenty, correct? So that goes on. Every node has two parts in single link singly linked list. One is the value, another is the link. So now this first node has point into the second. So link part of the first node

### 00:07:38 · Speaker 1

will be holding the value twenty. Value part holding the ten. So if I have to draw in a similar fashion where have you saw in PowerPoint, correct? So now, in this case, we have first one memory location is one. Value is ten, okay? Next, I'm drawing another block where

### 00:07:55 · Speaker 1

we have a value of twenty, correct? And a memory location of two. So now this ten is

### 00:08:05 · Speaker 1

So value is ten, the link is one. So now this ten value and this next node links which is two are interlinked. Okay? So due to which whenever you are trying to access this next value from this node, you'll be able to access it. I'm going to show that also in a while in with respect to object notation how we can access that. Okay? So but in very simple words as you saw every node has a value and a link in singly linked list. Okay? So how it will become the entire linked list? So you can see here, so we have a data and a next is having the link of this node.

### 00:08:35 · Speaker 1

and we have a data again next is having the link of this it goes on until when the next is null it's an end of a link list. So next is null is the end of the next I mean that node which doesn't have any next node is the end of link list. The head we generally use for head we generally use for uh accessing the first node okay so there has to be somewhere we need to start so we use the head node and whenever the last node reaches null then there is no longer a link list. So this is these are the concept that has to be there in your mind.

### 00:09:05 · Speaker 1

Now let's decode the object part of a linked list. Okay? See, now what you saw, we have a in linked list what we have, we have a element or a value, correct? So we have an element.

### 00:09:18 · Speaker 1

So let's say the element has a storing a value of ten. Next what we had? We had a link property or next property. Next basically here points to link, let me name it link only. Okay? Now the link should point to the next element, correct? So here you also if you go, there is another element twenty and this will have another link, correct? Now this link points to another element, element thirty, correct? Element thirty. Again we have a link property.

### 00:09:48 · Speaker 1

Correct? So this process goes on. So end of the day you are trying to mimic just this as a part of link list. You are not creating a typical link list that happens in other programming languages like where this link will be actually holding a memory location of the next node. Correct? That is not happening in JavaScript because JavaScript is an interpreter programming language it is not directly interacting with the hardware. So at end of the day everything is object in JavaScript. So you are trying to

### 00:10:18 · Speaker 1

decode this or implement this as a part of link list. Okay? Please, please be careful about this point. Okay? Most don't know this and they think it is still holding the memory. Under the hood, yes. Under the hood, every time whenever node is created, it is allocated with a memory. But actually, whenever you are programming or whenever you are implementing JavaScript site, say all you are doing is this. Compiler, even now if you let's say you create a variable called let x, compiler will allocate a memory with the help of an hardware, correct? Let's say for example, take an example of

### 00:10:48 · Speaker 1

Google Chrome. Google Chrome has a compilation engine called V8. V8 is written in C++. So C++ JavaScript code will be compiled by C++. C++ internally interacts with the system hardware to allocate a memory for that variable, correct? So this is a two step process. So, uh memory will be allocated. uh under the hood we may be having some memory allocated for this. But on top layer or finally what we as a developers are implementing is just this, okay? Let's decode how to do this step by step in upcoming videos, okay?

### 00:11:18 · Speaker 1

That's all for this video. If you like this video, please do like this video on YouTube channel because I have a bigger ambition of making an entire series about algorithm which will be helping for a lot of candidates to push their barriers and crack interviews at a very big firms, okay? I can do only that, I can do that only if I get a good motivation from you all. So like the videos, do not forget to subscribe to Uncommon Geeks, that's my humble request. Share these videos with your friends, let them also get benefited. Thank you so much, catch you next video.
