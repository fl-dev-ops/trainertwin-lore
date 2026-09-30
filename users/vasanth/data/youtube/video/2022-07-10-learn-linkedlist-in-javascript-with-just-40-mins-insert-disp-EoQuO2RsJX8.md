---
id: EoQuO2RsJX8
title: Learn LinkedList in JavaScript with just 40 mins - Insert, display Elements
  (LinkedList Part 1)
date: '2022-07-10'
url: https://www.youtube.com/watch?v=EoQuO2RsJX8
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Often most frontEnd developers consider DS/Algo as one of the tufts topics to\
  \ understand. They also get rejected in a lot of interviews, because of this. To\
  \ overcome this problem and help all frontEnd developers to pursue their dream job,\
  \ I have come up with detailed DS/Algo Tutorials in JavaScript. I will be covering\
  \ all the common data structures and problems around that in this video.\n\nIntroduction\
  \ to LinkedList in JS : https://youtu.be/5Z6tpdmtzG0\nIntroduction to DS/Algo in\
  \ JS: https://youtu.be/DkarkyD-LkQ\n\nHow add custom methods to JavaScript Prototype:\
  \ https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s \n\nHow to write custom implementation\
  \ for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU \n\nInterview Preparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  Medium Blog https://mevasanth.medium.com/ \n\nGithub Repository that contains examples:\
  \ https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:13:25
model: saaras:v3
transcript: true
---

# Learn LinkedList in JavaScript with just 40 mins - Insert, display Elements (LinkedList Part 1)

## Transcript

### 00:00:00 · Speaker 1

So first you are here. Next you came here. What is current dot next entire object? Then next iteration. Current is this entire object. What is current dot next you are here? Next what is current? This is the entire current. What is next? Current dot next is null. You end the iteration. So simple, correct?

### 00:00:20 · Speaker 1

self-assessment. I hope you all doing well. As you know there's a video series where we're discussing about data structures and algorithm in JavaScript. I've already completed two videos, one about the introduction about the entire course, another about introduction about specifically to linked list. In case if you have not watched those two videos, I would highly advise please go ahead and watch that because I would assume you already know something about the series and also about linked list and I'm going to straight away start with the video. So I would highly advise please go ahead and watch otherwise it will be slightly difficult for you to get along, okay? Now, without wasting further time, let's get started.

### 00:00:50 · Speaker 1

So now I've created a file called singly link list. As you know, link list as I showed in the last video.

### 00:00:57 · Speaker 1

First thing we need to create a node, correct? Then we need to insert the node, then we need to display the values in that particular node, correct? So as a part of this video, I'll be doing two operations, one is insertion operation into singly linked list and the display operation of the values, okay? To start off with, first you need to create a something called class node, okay? Vasant, why are you using class? We can use prototype, etcetera. Yes, there is a significant motto why I'm using the class, not using prototype. I've explained that in my first interaction video also.

### 00:01:27 · Speaker 1

every lot of problems that you want to solve in interview which are most commonly asked will be solved either in Java C# etcetera. Some are nowadays solved in JavaScript but most are solved in other object oriented programming languages. So it is good if you get along with a object oriented programming language kind of a structure in JavaScript as it already supports. So that even interviewer will be easily able to interpret your code and you will be able to get lot of solutions in other programming language and interpret easily in JavaScript. Okay? That's the way I'm using the class approach. Please stick to it and you will definitely appreciate me at the end of it.

### 00:01:57 · Speaker 1

Okay? Now, every node, what every node is having, whatever you saw, every node as per this PowerPoint also I presented, every node has a data and the next property, correct? So now if I come back here, I'm creating a constructor which takes one element, correct? Then we are doing every node will have an element whose value is element and every node will also have a next property, basically pointing to the next link. By default, every node's next link is null, correct? For when

### 00:02:27 · Speaker 1

whenever you are programming, whenever you are creating a node, where you want to insert depending on that the value of next will be determined, correct? by default its value is null. Now.

### 00:02:36 · Speaker 1

Let's this is about the node. So this node class ownership is just to create a node whenever we want. Correct? Now we have to create a class called linked list. So let's create a class.

### 00:02:46 · Speaker 1

linked list. Okay? So this is where all our operations will happen. Okay? First thing what we'll do, we'll create a constructor here as well and it has a property called this.head whose value is null. Vasanth, what is this head and you're initializing to null? If you remember from the presentation, we have one node called head which will be pointing to the first node in the linked list, correct? So we need somewhere to get started. So we are using one node head which doesn't has a value, which only has a link to point

### 00:03:16 · Speaker 1

getting to the next node. Okay? And whenever a link list reaches, we reach a node whose next link is null, that's the end of link list. You have to remember these two points. Okay? So now, you created this dot head initialize to null. Okay? Now, let us do a create our first element that is

### 00:03:36 · Speaker 1

add value, correct? add element. add element function definitely takes an element, correct? Now, how add element we has to be done? So let us see again go back to our picture and let us see, okay? So this I have drawn. So here if you see, there is a head, there is ten and ten and this and there is a twenty node. So now let us assume there are two scenarios where you have only head.

### 00:04:01 · Speaker 1

correct? You have only head and it is not pointing to any value because it is just empty link list. In such cases, so you have to you have to point to the new node to head or head will point to the new node. Other scenario is where there is already a link list existing, correct? with some set of nodes. So now if you have to insert thirty, so you should loop and find the last node whose link is null, correct? And then link that node to the new node.

### 00:04:31 · Speaker 1

So two main personas or two main flows. One, when the link list has when when the link list is empty. So you have only head node. Another, when you have the link list with already some values and you have to insert the elements, correct? These are the only two ways where you will be inserting value into link list. Now let us go back to the code. So add element. First thing what you have to do? First thing you need a node. How you get the node? Let node is equals to new node above one that you created, correct? and you're passing element into it.

### 00:05:05 · Speaker 1

In case if you don't have any idea about constructor and the class in very simple words constructor is something any object created in that class will have that property. So now node we have assigned it to small node this will have the property of element and next. So hundred elements you create hundred elements will have these two properties. So rather assigning it to individual individual individual one by one we will use a constructor so that it is done at once. Okay. Now we have the node. Now we have two options. If you already discussed. This dot head is equals to null, correct?

### 00:05:38 · Speaker 1

otherwise. So two value two flows are there, correct? If this dot head is null then there is no list existing so far. So this dot head is equals to node. If list list already exists then you should iterate to reach the end node, correct? Where how do you get to know it's the end node when the link is null? That's the end node, correct? So what you will do is

### 00:05:59 · Speaker 1

Let current is equals to this dot head because you start the traversing from start. There is no way where you can go in middle like array, correct? So while current dot next

### 00:06:12 · Speaker 1

and current is equals to current, I'll explain, don't worry, current dot next. Okay? So what I'm doing here is if you observe carefully, we are getting the head, that is the starting point, correct? From there, you are doing a while loop, iterating and going till the end when current dot next is null. So that is the indication that you no longer have an LE element at the end. So that is the end node. Then what you will do, current dot

### 00:06:40 · Speaker 1

next is equals to node. New node that you have already created, correct? So if you go back to our drawing that we draw on sketch, if not for anything, like I said in my last, at least for my effort to draw this drawing and get all this content, please like the video and share this video with your friends and do not forget to subscribe to Uncommon Geeks. That will help motivate me a lot to make good content like this. As I mentioned, I want to cover all the data structures that has been most commonly asked in the interview in this part of series. Your your your help by liking the video and sharing the video will definitely motivate me to make more good content, okay? Please help me. Now, let's go back.

### 00:07:15 · Speaker 1

So we navigated the entire thing and we hit the end and we added the new node, two things. We can also do this dot size plus plus. So we have not created size, I'm creating a variable called size, okay? So this has been used in some approaches to save our time whenever you're doing search or remove operations, I'm going to explain that in a while, okay? Now adding element is done, but you will not be able to infer anything unless you print it, correct? So let us create a thing called print list.

### 00:07:45 · Speaker 1

So print list again, now you you only think, what should be the printing logic? So there are two things, one list could be empty or list as element, that doesn't matter. So we'll start from head. We go to a till a node which has the link property as null, till then you navigate, correct? And you keep printing, that's all you're doing, correct? So if you observe, same code you want. Correct?

### 00:08:07 · Speaker 1

let current. But here only one difference is

### 00:08:11 · Speaker 1

You need a value. Output is equal to initializing initializing output as an empty string, okay? Every time whenever you are navigating, what you'll do output plus is equals to uh you will be adding the current's value, okay? Current, I'm sorry.

### 00:08:28 · Speaker 1

that node's value you want so that is which is present in the element. Correct? So then what you will be doing is once this entire thing is done you will be returning the output. Okay? So start from the first node keep navigating to the nodes till the end when this current node is null when till then extract the value in each node correct if you see here it is storing the value A B C D in our case it could be ten twenty thirty forty extract the value from each node

### 00:08:58 · Speaker 1

Finally, you get the value concatenated to a string, finally return the string and we can display the string. Correct? So I'm going back.

### 00:09:08 · Speaker 1

So, yeah. So now let us, all the magic is okay. So you explained that this now finally show whether it is working or not. Yes. So now how to access the code that you have written. So it's a it's a good number of code, thirty five lines of code and it is quite I have been mastered it by doing lot of problems. Still I might have made some mistake. If so, let's try to I'll try to solve on live. If not, let's try to use it, okay? Now, const link list. I'm creating an object now with linked list, okay?

### 00:09:38 · Speaker 1

Okay, then first what? We need to add the element, correct? What all we are adding? Ten, let us add. Then let us add twenty, okay? Then let us add thirty, okay? Now, we have to print it, correct? Print list.

### 00:09:56 · Speaker 1

First let us run. Then I'll show the object structure, how the object structure happening, okay? Let me run this. So you got ten, twenty and thirty. So all the values that we inserted that got printed, correct? At least the program is working well. Now let us decode this, okay? I clearly explained this in my last video. JavaScript does not behave with our data stream algorithm in similar to Java or C. So it is totally different. JavaScript runs on browser. If you want to know more, please watch my previous video, okay? There is nothing like a length list in JavaScript. It is just the object that

### 00:10:26 · Speaker 1

representing. So in this case what is happening let us see. Okay. First. So there is a variable called head. Okay. So there is a variable called head like this. Very first. Okay. Whose value by default was null. Then what we did was we inserted a new node with two property element

### 00:10:46 · Speaker 1

correct? Element whose value was ten and we inserted a link property whose link by default was null. Okay, first it was null. Correct? Then, then what we did was we added another node, so it is no longer having null. So it is having another element. Element

### 00:11:04 · Speaker 1

twenty. Correct? Then it has a link property. So link property which again first it was null. Then we added another node, correct? Where element whose value was thirty, then we added a link property whose value is null. So now, how we did the insertion, correct? So we first checked whether head was null, first case head was null, so you inserted this. Then you checked whether link is null here, yes you inserted this. Then you checked link is null here,

### 00:11:34 · Speaker 1

inserted it. Correct? Now, how you've displayed it? You started from here, correct? You head dot next, see if you see here, what you're doing? Current dot element, current is equal to current dot next. So I'm put a link, so avoid confusion, let me use the next.

### 00:11:49 · Speaker 1

Yeah. So we have first this dot head basically points to this entire object, correct? This dot head would point to this entire object there. Then what we are doing? While current, correct? So now this has some value, so while will hold good. Then what we are doing? Current is equal to current dot next. So first you are here. Next you came here. What is current dot next entire object? Then next iteration. Current is this entire object. What is current dot next? You are here. Next, what is current? This is the entire current. What is next? Current dot next is null. You end the iteration. So simple.

### 00:12:19 · Speaker 1

simple, correct? So actual link list in JavaScript is very simple compared to other languages. All you have to do is a mind mapping, correct? If you understand this video properly, okay? Definitely you will be able to implement, let's say I'll do the search in next video, search and probably remove element. After that you only will be able to do lot of access like how to insert element at a particular index, how to identify myridal element. You will be definitely able to do on your own. Have this thing running in your mind, this object concept running in your mind and basic thing, correct? See, as I mentioned this is not something

### 00:12:49 · Speaker 1

very difficult. And this is not something you can mug up. Your mind should think, okay, which node I am, how I'm inserting a node, how do I insert a node in the middle, how do I remove. So all these things should run in your mind so that you'll be able to do it properly, okay. That's all about this video. Please do like this video on my YouTube channel. Do not forget to share these videos with your friends and subscribe to my channel Uncommon Geeks, okay. This will definitely motivate me to make more and more such good content, okay. Thank you so much, catch you in next video and this this entire code snippet will be in in my GitHub. I I'll add the code and I'll put the link in the description.

### 00:13:19 · Speaker 1

you can easily get the entire code and for practicing purpose, okay? Thank you so much, catch you in next video.
