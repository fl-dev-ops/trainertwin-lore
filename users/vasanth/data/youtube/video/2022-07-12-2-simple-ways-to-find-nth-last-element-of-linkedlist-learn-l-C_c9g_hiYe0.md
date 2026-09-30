---
id: C_c9g_hiYe0
title: 2 Simple ways to find nth Last element of LinkedList (Learn LL in JS Part -
  5)
date: '2022-07-12'
url: https://www.youtube.com/watch?v=C_c9g_hiYe0
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Often most frontEnd developers consider DS/Algo as one of the tufts topics to\
  \ understand. They also get rejected in a lot of interviews, because of this. To\
  \ overcome this problem and help all frontEnd developers to pursue their dream job,\
  \ I have come up with detailed DS/Algo Tutorials in JavaScript. I will be covering\
  \ all the common data structures and problems around that in this video.\n\n\nLearn\
  \ LinkedList in JavaScript Part 1: https://youtu.be/EoQuO2RsJX8\nLearn LinkedList\
  \ in JavaScript Part 2: https://youtu.be/CSkwIceygEU\nLinkedList in JavaScript Part\
  \ 3: https://youtu.be/nI8TXMzeznk\nLinkedList in JavaScript Part 4 (Find middle\
  \ element of LL): https://youtu.be/MrJEEuyDU0c\n\nIntroduction to LinkedList in\
  \ JS : https://youtu.be/5Z6tpdmtzG0\nIntroduction to DS/Algo in JS: https://youtu.be/DkarkyD-LkQ\n\
  \nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  Medium Blog https://mevasanth.medium.com/ \n\nGithub Repository that contains examples:\
  \ https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:13:28
model: saaras:v3
transcript: true
---

# 2 Simple ways to find nth Last element of LinkedList (Learn LL in JS Part - 5)

## Transcript

### 00:00:00 · Speaker 1

So finally it will reach here. Correct?

### 00:00:04 · Speaker 1

When it reaches here, the slow the second this let's consider this is first pointer, the second pointer will be pointing to the value that what we are expecting, second value from the last.

### 00:00:18 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Vasanth. I hope you all doing well. As you know, this is a video series where we are discussing about the data structures and algorithm. So in this particular part of last couple of videos, we have discussed about linked list. So we have already finished all the basic operations of a linked list and we also solved one most important interview question in last video. So in case if you've not watched all the videos, I would highly advise, please go ahead and watch that because I'm using the same code and I'm continuing. So it'll be very strange for you to get along all of a sudden. Okay? Now, if you already watched those

### 00:00:48 · Speaker 1

videos and you're already strong with the linked list and this is another challenge for you. I'll be solving this problem and at the end of this I'll give you one homework. So please do watch the video till the end so that you get to know what is the homework and you can solve that and mention in the comment section. And I'll personally validate your solution and I'll tell you whether the whatever the solution you've written is right or not. Okay? Now, what is the problem? Here is the

### 00:01:08 · Speaker 2

problem

### 00:01:19 · Speaker 2

Yeah

### 00:01:20 · Speaker 1

So I think you got the problem. It is quite simple. You have to find the nth last element from the link list. For example, you have five elements, one, two, three, four, five. So you have to find second largest element from the last is that is four, correct? So you have to find third largest element from the last that is three. You have to find ten largest element from the last that doesn't exist, correct? So always whenever a question is asked, think in this direction of the extremities. So where what is the minimum value that can be asked? That is five, four, three, two, one, correct? Let's say

### 00:01:50 · Speaker 1

in the in the if you have five elements the least that you can ask is first element from the last or fifth element from the last which points to the first element. They cannot give negative value or correct and they cannot give you a value greater than the size of the link list itself. Correct? So keep these things in your mind and let's get started. So what is the easiest approach? What is the easiest approach but not very optimal approach? Is you if you know we already maintaining a proper value called size in our link list correct? So every node whenever every node we are adding we are increasing the size value by one.

### 00:02:20 · Speaker 1

Correct? So now let's say now you have to calculate one value, one element from the last, I mean the second largest element. Correct? Sorry, second element from the last. So what you can do, you can do the size minus the element. In case if you see here, let's say we have five elements here. Correct? So we have five elements.

### 00:02:39 · Speaker 1

correct? And we have to find the second largest element. So sorry, I'm keep telling second largest largest, please avoid that, not largest, the that many elements from the last. Second element from the last is this, correct? So five minus two is three.

### 00:02:53 · Speaker 1

If you run a for loop till three indexes of a linked list, it will start from here, zero, one, two, and three, correct? So when it reaches the three, the for loop will fail, but you will be doing current is equal to current dot next in every iteration. So finally, when the for loop has failed, you have already done the current dot next, you will be pointing here. So you can return this. So this is approach is using the size property that we created. So we know the size, we know how many index from the last, so we are just subtracting and returning it. So this is acceptable solution.

### 00:03:23 · Speaker 1

this this might be of a complexity n itself like because we need to kind of we need to navigate till some length from the last so n minus something at the end it is n itself correct so what is the other solution that is available and most preferred on the internet I don't know why that solution is a two pointer approach okay you already seen two pointer approach in my last video correct where you did a two pointer for the

### 00:03:48 · Speaker 1

finding the middle element in the linked list, correct? So this also you can do a two pointer approach, but this is not like a fast and slow pointer. It is just two pointer approach. I'll tell how we can do that, okay? So, let's say we have two pointers. I'll use two colors to represent. So this is first color.

### 00:04:03 · Speaker 1

let me pick some orange or yellow I'll pick, okay? So this is my another pointer. So now what I need to do, we have I have two pointers. First thing what I'll do is the first pointer what I have, let's consider this as blue, the first pointer what I have, that one I will move so many indexes that is equivalent to given index. So I need to calculate second element from the last, correct? So what I'll do now is I will move this blue to two indexes. One minute.

### 00:04:34 · Speaker 1

So I'll move this blue to two elements from the start. So one and two, not here, one and two here, okay? I'll move it here.

### 00:04:44 · Speaker 1

Now first pointer will be still pointing here itself, correct? Then from now onwards, we'll be keep iterating one one one value. So from here, I'll go here. Even the the the first, this is let's say the first pointer, even the second pointer will also be moving in a similar way. So finally, it will reach here, correct?

### 00:05:04 · Speaker 1

When it reaches here, the slow the second this let's consider this is first pointer, the second pointer will be pointing to the value that what we're expecting, second value from the last, correct? Let's say you are trying to calculate third value from the last. So in that case what will happen? First pointer will be pointing here initially and this will be pointing here, the third value, correct? Third from the last. Then what will happen? Every time we'll be keep iterating one. So this will come here.

### 00:05:30 · Speaker 1

and this will go here. Correct?

### 00:05:33 · Speaker 1

and next iteration. This will the second pointer will come here and the first pointer will go here. So when the first pointer reach the end of the link list, the second pointer is pointing to the value that we are looking, correct? Zero, one, two and three, third element from the last, which is whatever the value that the first pointer is pointing. Correct? The second pointer is pointing. So summarize, first pointer will be incremented to number whatever is given. Second pointer will be always following that. Both will iterate one one index. So now you know

### 00:06:03 · Speaker 1

conceptually are clear. In case if you are able to write the code, please try it, pause the video, try the code and come back and watch the video till the end to get the whether whatever you typed is matching with the whatever the code that I have written, okay? Because like I always mention my whole purpose of making the video is to make sure you are able to code on your own and not to follow me always, correct? Now.

### 00:06:22 · Speaker 1

In case if you're someone who watched the entire series and liking the content that I'm making, see please like this video and do not forget to comment something. You're liking the video, comment like you're liking the video. If you're not liking, what can I improve? Please comment that. So by more like and comment, the YouTube consider this video is been appealing to lot and it will giving start giving more impression. More impression means more people will be able to see the video become popular. When video becomes popular, lot of people get benefited from this. Okay, that's the whole purpose I'm making the video series. So please like and comment the video to the video and then

### 00:06:52 · Speaker 1

continue watching, okay? That's my humble request. Now, I've already created a function called find nth last. So if you don't know what and all happening here, please watch my previous videos, I've clearly explained them, okay? Find nth last and they have passed the index. So now what I'll do,

### 00:07:08 · Speaker 1

So one first thing to this I'll anyway can keep, correct? If head is null,

### 00:07:13 · Speaker 1

additional you can return one or if index so if index is greater than size

### 00:07:20 · Speaker 1

So if it is greater than size, then also I cannot, we cannot find the index because it is already beyond the size, then I cannot get that element in the linked list, correct? Or also what if index is negative?

### 00:07:35 · Speaker 1

If index is negative, see, these are the conditions I'm deliberately adding because interviewer will be expect you to cover all the edge cases. So, please be mindful. If you're not sure, ask the interviewer, get all the edge cases. Always start by thinking the edge cases. Happy flows, most of you will be able to write. Edge cases you will miss and interviewer consider you are not considered all the scenarios. Okay, so please be specific. Next. If none of this has happened, then what we'll do? We'll have a first pointer.

### 00:08:02 · Speaker 1

first pointer which is pointing to head. Okay. Also we have a second pointer which is also pointing to head. Okay. Like we discussed what we'll do is we will

### 00:08:14 · Speaker 1

what we'll do is first pointer you need to traverse the number of indexes that is required, correct? So for

### 00:08:22 · Speaker 1

four

### 00:08:24 · Speaker 1

I is equals to zero. First pointer, correct? First pointer is equals to first pointer dot next. Correct? So first thing that we are doing. So we are initializing basically, if you remember. So this blue has come here, the yellow is here. And the blue has come here now, correct? Now, next what we'll do? Next is, as you know, both will iterate, correct? Next is our usual while.

### 00:08:49 · Speaker 1

while first pointer, then what we'll do? first pointer is equals to, first pointer is equals to

### 00:08:57 · Speaker 1

first pointer dot next, correct? Then same, second pointer is equals to second pointer dot next, correct? Then finally when this iteration has ended, the first pointer has reached the end, what you will do? You will return the second pointer dot element, correct? Because second pointer will be at the value like this, correct? In in so when the first pointer will reach here, the second pointer will be here, correct?

### 00:09:25 · Speaker 1

That's all we want, correct? Now if you come back, so we are trying to return the second pointer element, correct? I'm only concerned about maybe this would be first pointer or first pointer dot next not equal to null, let us see will it work. So find nth last element.

### 00:09:40 · Speaker 1

So log

### 00:09:42 · Speaker 1

log l l dot find nth last element

### 00:09:48 · Speaker 1

find

### 00:09:55 · Speaker 1

nth largest element, okay? I'm trying to calculate now second largest element. Let's see what we'll get.

### 00:10:01 · Speaker 1

We got error array dot length something I have written which is wrong. Okay. Let's see find nth last element array no there is no array. So we need to run the loop I think most of you might have observed this and you haven't you are just waiting Vasanth why you haven't observed. I'm sorry. Okay. So I was trying to get the second largest second from the last so which is forty. Correct this is the first from the last this is second from the last. Let's say I want to get the third from the last. So one two three thirty should be the output. Okay

### 00:10:33 · Speaker 1

Let's check the extremities, don't worry. So I have to find the first from the last, which means fifty I should get. Will I get? Let us see. Fifty I'm getting. I also need to get uh what I have? Five, four, three, two, one. One, uh means fifth, which will be pointing to ten. Fifth from the last, which is one. Sorry, which is ten. I'm getting, correct? Extremities I checked, middle I checked, all the values I'm getting, correct? So what is the homework for you? Homework for you are two. One, implement that approach that I said here, correct? Where you can use this π - 2 = 3 this approach that is first homework

### 00:11:06 · Speaker 1

Second, in this you see, I have created for remove and search and other things, search by index and search by element, remove by index and remove by element. For add, I have only added at the end. Can you just try to implement add at the add at the somewhere in the middle, like add at a index, you will add the element in the middle. Now I think after remove, you know a lot of things, the previous and next concept, you should be able to do that. So please finish this homeworks and mention that either in the comment section your code or write the code in your GitHub just and add the link here.

### 00:11:36 · Speaker 1

I'll definitely validate, me or my team will validate and we'll get back to you whether whatever the code that you have written is right or not. Okay? So this about this video, find nth largest element, nth largest element, so this link will be in the GitHub repository. And if you already got the entire gist or the entire thing that I explained in this video, feel free to end the video, but do not forget to like this video and share the video with your friends and subscribe to my channel Uncommon Geeks. Thank you. But for those of you who have not fully understood, I am also going to explain this with the help of this object thing. Okay? So please stay tuned. whoever have not understood

### 00:12:09 · Speaker 1

Now here what we are trying to do is we are trying to iterate um the we are trying to calculate the last element, correct? Nth last element. So what we are doing here is so we need two pointers, first and second, correct? Let's say second last element we we need to find. So which is forty basically. So what we are doing here is first will be point second will be pointing to the first node, I mean the starting wherever. First will be pointing to the two nodes after that. So first will be pointing here.

### 00:12:37 · Speaker 1

correct? To whenever before we start the iteration itself, first is pointing here, second is pointing here. What is after that? Then we keep incrementing, correct? Finally the first will reach here.

### 00:12:49 · Speaker 1

second will be here.

### 00:12:52 · Speaker 1

So second will be here and you'll return the second segment which is forty. Correct? That's all we are doing. It's actually very simple. uh When if you as long as you remember this object thing in your mind like I mentioned in my previous videos also, even if you face any difficulty, definitely you'll be able to overcome very easily, okay? So that's all about this. If you watch like the video, please like it on my YouTube channel and comment whatever you are feeling about the entire series and about my overall other tutorials also I've created. Do not forget to subscribe to Uncommon Geeks. This code will be present on my GitHub. You can download my GitHub.

### 00:13:22 · Speaker 1

प्रोजेक्ट स्टार माय गेटअप प्रोजेक्ट एंड प्रैक्टिस इट ऑन योर ओन। थैंक यू सो मच फॉर वाचिंग। कैच यू इन नेक्स्ट वीडियो।
