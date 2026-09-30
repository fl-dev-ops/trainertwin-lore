---
id: nI8TXMzeznk
title: Learn LinkedList in JavaScript with just 40 mins - Remove Elements from Index
  and by value (LL Pt 3)
date: '2022-07-11'
url: https://www.youtube.com/watch?v=nI8TXMzeznk
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Often most frontEnd developers consider DS/Algo as one of the tufts topics to\
  \ understand. They also get rejected in a lot of interviews, because of this. To\
  \ overcome this problem and help all frontEnd developers to pursue their dream job,\
  \ I have come up with detailed DS/Algo Tutorials in JavaScript. I will be covering\
  \ all the common data structures and problems around that in this video.\n\n\nLearn\
  \ LinkedList in JavaScript Part 1: https://youtu.be/EoQuO2RsJX8\nLearn LinkedList\
  \ in JavaScript Part 2: https://youtu.be/CSkwIceygEU\n\nIntroduction to LinkedList\
  \ in JS : https://youtu.be/5Z6tpdmtzG0\nIntroduction to DS/Algo in JS: https://youtu.be/DkarkyD-LkQ\n\
  \nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  Medium Blog https://mevasanth.medium.com/ \n\nGithub Repository that contains examples:\
  \ https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:17:46
model: saaras:v3
transcript: true
---

# Learn LinkedList in JavaScript with just 40 mins - Remove Elements from Index and by value (LL Pt 3)

## Transcript

### 00:00:00 · Speaker 1

In fact, this is the end of singly linked list operations. Okay? How how cool it is. See, we we according to me we have spent around forty forty five minutes from introduction to till now and we have finished all the operations of linked list.

### 00:00:15 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. So as you know there's a video series where we are discussing about the data section algorithm, especially in this couple of videos we are discussing about linked list. So in case if you have not watched my previous videos where I have given introduction about linked list and I have also done two videos about linked list operations, please do watch the video. If you have not seen this video and directly landed into this video, it will be slightly difficult for you to get along because some code is already written. I'll be extending the same code, okay? So without wasting further time, let's

### 00:00:45 · Speaker 1

get started. um Now, uh we have performed few operations as you already know, correct? So we have performed operations like adding element into link list. So searching elements at link list, searching element by index, also by element and we have also done the printing the element, correct? Now one of the very very important aspect of a link list operation, according to me is the last operation of the link list that is removing the elements from the link list, correct? So how we can remove? Remove again has two two kind of removal, removal from a index, removing of the element, correct?

### 00:01:15 · Speaker 1

Now, but before we start coding, it is very important for you to analyze this. It is not so straightforward as that of a search, okay? So, I've created a small link list in my sketch so that we save some amount of time. Let's say we have four nodes in link list now. One, two, three, four. Now,

### 00:01:33 · Speaker 1

Let's say you have to remove this node, the second node, correct? Imagine in your mind now two has to be removed, correct? There is nothing called deletion, correct? Because see there is, let's say this is a memory location of hundred, two hundred, three hundred and four hundred. Can we delete remove the memory location two hundred? No, memory location is gonna be there because it's a hardware, correct? So memory location is going to be there. So what we are doing? Basically, we will try to unlink this node, correct? So this node memory whatever we had, we'll try

### 00:02:03 · Speaker 1

to unlink this node so that this memory gets freed up. How we can do that? We can do that by uh let me pick some another color let's say yellow I'll pick okay. So what we can do this link we can establish here.

### 00:02:19 · Speaker 1

correct? So we were having one to two and two to three, rather having that one to three if you do, you'll be able to eliminate this. Correct? Let's say, let me pick some another color. So if you do that, you'll be able to eliminate this just by linking one to three, you'll be eliminating two. Correct? So that is what the idea here. There is nothing called deleting the memory, that is only deleting a node, correct? As soon as you delete the node, the garbage collecting engine itself will deallocate this memory and use it for something else.

### 00:02:49 · Speaker 1

correct? So now, so this is about the removal. So now there are two major personas for the removal, okay? Let's say, let me quickly draw now, okay? So

### 00:03:01 · Speaker 1

one minute. So if we quickly draw, so we have two boxes, okay? Two box

### 00:03:11 · Speaker 1

okay? So three elements are there, okay? So and head is pointing here. So now if we have to remove an element or remove an element by index or remove element by the element value itself, both the cases, so this is head let us say, okay?

### 00:03:28 · Speaker 1

So my humble request if you are watching this video from since the beginning and you are liking whatever the content that I am making, please don't continue watching before liking and commenting about the video that whatever I have made. There is no other intention. If you like the video, YouTube will give more impressions, impression as in it will start showing my videos to a lot of people and so that the video will gradually increase, video count, number of viewers will gradually increase. That will help me motivate, that will motivate me to make more good content. So please do like the video and comment if you are liking the content and do not forget

### 00:03:58 · Speaker 1

to subscribe to my channel. Okay? Now let's continue. So we have head here. Okay? So now, so as we already seen, so there is a link, let us quickly draw. There is a link. Okay? So now, if we if we decide to remove this, so you already know, we can link from this to this, so this gets removed, correct? But there is another thing, what if we have to remove this itself, the first node? So if you have to delete the first node itself, then what you need to do is

### 00:04:25 · Speaker 1

So then what you will be doing is if you have to delete this first node, you need to point head to this node. Correct?

### 00:04:32 · Speaker 1

whether it is removing the index zero or removing the element which is present in the first node. In both the scenarios, you need to be doing this where you need to will point the head to the the next node of the first node or zeroth node, okay? That way you will be able to remove this link to this node, correct? So now while in coding you should keep this in mind. There are two type of persona. One, removing an element somewhere in the middle, correct? Second, removing the element which is which is pointing which is the first element.

### 00:05:02 · Speaker 1

where head is pointing. So we need to redirect the head, correct? Removing last element, the whole good the process remains same where you remove this and you will you you don't have to link this to anything, correct? That's all. So there is not much of a change. So there are only two major personas. Let us start implementing now, okay? So if I go here, I'll click on remove element, okay?

### 00:05:25 · Speaker 1

and element. So, as I mentioned, so many of this code, most of code already written for many other operations. Please do watch my previous videos and come to this video. Okay, otherwise you'll feel strange to this. Now we have to remove the element and our the basic operation remains same. So if head is null, then there is nothing that we can return, correct? So if head is not null, so then same thing. So this is our golden piece of code, correct? So I'm copying this.

### 00:05:51 · Speaker 1

So where this is not required, this is required. So if current element is equals to the element, okay? So we need to extend little bit. So what we need? So now, as you saw in the diagram, correct? So to if you have to link from this to this. So you need to know now this is an element, let's say one.

### 00:06:11 · Speaker 1

two and three, correct? So you want to delete the element two, correct? So now you need to know the previous index of the two, next index of the two, so that you can point previous node to the next node, correct? So same if I have to do here, what I'll be doing, I'll having something called previous whose value let us say null. Okay, by default it is null. Then what I'll be doing, I'll be doing previous is equals to current.

### 00:06:37 · Speaker 1

Correct? So what I'm doing here is, so first previous will be null, current will be pointing here. Next, previous will be pointing here, current will be pointing here. Next, previous will be pointing here, current will be pointing here and it goes on. So when you find the element, so current will be pointing to this. What you will do, you will point the previous next is equals to the current's next. So current's next is this. So previous next will be pointing to the current next and this gets disabled. Okay? Or this gets removed. So what I'll be doing, so previous dot

### 00:07:07 · Speaker 1

next is equals to current.next and you will just write the return. So you know why I'll write return so that this execution context is ended and while loop is terminated automatically, correct? So this is removing an element. So Vasanth you said something about head and you missed it. Yes. So we need to also take care of the another scenario where

### 00:07:28 · Speaker 1

If this dot

### 00:07:31 · Speaker 1

uh or we can use current already we have that current dot element if is equals to element okay so that means the first node itself is having the element in that case you need to redirect head to the current's next current dot next so what we did same as the diagram oh sorry not this so same as the diagram where this was if first element itself is the element then current next is this so this value's next is this so you're pointing head to this so if I had to explain with you with respect to an object correct

### 00:08:01 · Speaker 1

See, this is how our object notation look like, our the linked list. So in case if you don't know what is this, again you have to watch my previous videos. So now, here what we are doing, we have element as ten and next as this entire thing, correct? So now what we are doing, we are trying to remove. If first element itself is ten, correct? Then what we need to do, we need to point head to this, correct? So the same only we are doing. This dot head is equal to current's next. So this element will be gone. So now head will be pointing to this, whatever is in this, right? So if I have to cut and paste, I'm

### 00:08:31 · Speaker 1

and paste. So it will look like this. Correct? So ten reference is gone and you just have the twenty reference and goes on. If otherwise what you are doing, we you are just removing the one particular index. Let's say now twenty and next is thirty. Correct? So what you are doing is you are taking this the forty. Correct? uh you are taking the fortieth node which is here. Correct? And replacing that here.

### 00:08:58 · Speaker 1

so that now twenty's next will be this. I think this is not required. One minute. Little bit. Basically you just remove uh one particular node and you will add the other node in that place, okay? Always remember this object manipulation in mind as a multiple time I have said in this my previous videos, correct? Because object manipulation should run in your mind then only you will be able to code it properly, okay? So wait one minute let me uncomment because I need this for other purpose, okay?

### 00:09:28 · Speaker 1

Sure. Now let us try to run this and let's see whether it is working fine, okay? So remove element. L L dot remove element. Am I giving thirty, okay? Then let us run this code.

### 00:09:42 · Speaker 1

See, we are seeing ten, twenty, okay. For to be sure, we need to run this before and after, correct? So let me run this. So you're seeing thirty, forty, fifty. In second iteration, you're not seeing thirty, correct? Let's try to run ten. Will it remove the ten? Ten is the first element. So mind should run in a way where you're trying to remove the, you're trying to re-point the head to the other node, okay?

### 00:10:03 · Speaker 1

So we got an error. What? Previous.next is equal to current.next. So

### 00:10:08 · Speaker 1

type error cannot read a property next of null. Correct? See, now let us go and see what is happening.

### 00:10:15 · Speaker 1

So, what is happening is

### 00:10:18 · Speaker 1

So current dot element is equals to element, correct, in the first case. So this dot head is equal to current dot next. I'm sorry, I did not write the return. Okay. Let us try again. Yeah. So ten got deleted. Okay. See, I am also making mistake. So, but there's not a problem in making mistake. No matter we practice or not, we end up making mistake. But I know what is happening, so that I'm able to solve this very quickly. So you also create that mindset so that you'll be able to fix this quickly. Now, let us try to delete fifty, the extremity, correct? extremities

### 00:10:50 · Speaker 1

Yeah. Middle element I've already added thirty, it worked. So this is how one way of removing. So remove by remove element. So you're passing the element, correct? Next we need to pass remove by index, correct? Let us quickly see how we can remove by index. Remove element by index. Pretty much the flow would remain same as you might have already guessed, correct? So I'm copying the same code.

### 00:11:13 · Speaker 1

So this entire code I'll be adding it to my GitHub. In fact, I've already added. So you can just copy take that from my link in the description and practice on your own. So this only thing you hear it will have index, okay? If this dot head is equals to null, we'll return minus one. Current is equal to this dot head, previous equal to null. Current dot element, no. Okay? If index

### 00:11:34 · Speaker 1

is equals to zero. Correct? If index equals to zero, then I'm if index equals to zero, means first element itself we are matching, correct? If index is equals to zero, then whatever the head was pointing to the first node, that we cannot point, correct? We should be pointing to the second node. Otherwise, while current, okay? Then current dot, this I'm slightly doubtful whether this is the way. Let us see if it fails, let us try to solve this, okay? So while current, current dot element is

### 00:12:04 · Speaker 1

equals to element, okay? Next, so not this. So what we'll be doing here is, let us create a variable called link list index, initialize that to zero, okay?

### 00:12:16 · Speaker 1

initialize that to zero and link list index will be keep incrementing. I'll explain once again, don't worry. If link list index is equals to the index passed by the thing, then we are doing the same operation here, okay?

### 00:12:30 · Speaker 1

So first let us run then probably let us see whether it is working or not. Okay. So remove by index let us give to second index. Let's see what is happening.

### 00:12:40 · Speaker 1

So second index zero one two thirty got removed correct? Remove from index zeroth index it may fail. No it also worked. Remove from index zero one two three we have five values we have added right zero one two three four five. So remove from fifth index. Extremities always you have to check zero and the last element correct? So last element was not removed if you see correct? current dot fifth element we tried in removing. Correct?

### 00:13:13 · Speaker 1

Maybe the last element did not do because of this.

### 00:13:17 · Speaker 1

No

### 00:13:21 · Speaker 1

Let's see why last element did not get removed, okay? So but otherwise it seems to work fine. So we are passing index as now zero, one, two, three, four. Okay, in fact I need to pass four, not five.

### 00:13:33 · Speaker 1

Okay. I need to pass four. Yeah, fourth if I pass the last element is also getting removed, okay. So see, I did not get panic when record did not work, okay. I am in a mindset, I know what I'm doing, correct. And I know if there is something goes wrong, I know pin to pin what is happening with my object flow. I'll be able to fix it, correct. That's the confidence I have. You don't see me frightened. So I want you to also get that into that same notation. You know what is happening. So you are in the into the head. You are going to the next elements and you are reaching the end, etcetera, correct. So be confident, don't get panic. So by now

### 00:14:03 · Speaker 1

I think you might have gained some confidence about entire structure, correct? Now, in case if somebody of you not understood the remove element by index, I'm gonna reiterate quickly once again, okay? Similar to the above one only remove element, only thing rather having element we are trying to do this with the help of index, correct? So what we are doing this dot head is equal to null, this you already know. When head is null, there is no point we can remove because linked list itself is empty. So we are returning minus one. Then we have current node and the previous node. From here you know what is current and what is previous, correct? Previous will

### 00:14:33 · Speaker 1

always points to one before to the current. Okay? Now, then what we are doing? If index equal to zero, why you are doing this? So when will be index equal index is equal to zero means you are trying to delete the first element, correct? That is

### 00:14:46 · Speaker 1

this element you are trying to delete. So when you are trying to delete this element, what you need to do is, so you need to repoint the head to the first node, not to the zeroth node. From it will be pointing here, you need to repoint it to the first node. So same I have done here. So zero is equal to index, then you are doing this. It's not what you are doing, your operation is same. You will be keep iterating the link list. Whenever there is a match between the link list index and the index that you have passed. So you are doing this. Previous index equal to current dot next and return previous and current. So this you

### 00:15:16 · Speaker 1

already know where previous will be always updating current will also be always updating it will be both will be going to the next indexes this index also you are incrementing so that every time when you are iterating the index is increasing you can keep another check as well okay if this dot head is equal to null and or in fact or if this dot size

### 00:15:38 · Speaker 1

index greater than size, then also we cannot delete, correct? If index greater than size, then we also we cannot delete. And we can also do one more important thing in both the deletion operation, okay? So this dot

### 00:15:51 · Speaker 1

size minus minus. So we are removing an element, right? So we can decrease the size. Don't keep it everywhere, okay? Keep it only in successful delete operations. Not here. It's not a successful delete operation, okay? So even here. So you are decreasing the size, okay? So even here. So why size is important? The why size is important is basically because we are keeping a track in whatever the videos that we discuss next, you will see it on live, okay? So that's all about this video. If you like my entire content of this, please do like this. In fact, this is the

### 00:16:21 · Speaker 1

end of singly linked list operations. Okay? How how cool it is? See, we we according to me we have spent around forty forty five minutes from introduction to till now and we have finished all the operations of linked list. So we have finished uh insertion, deletion, search, displaying. These are the primary operations of linked list. That too with a variety of flows we tried. Like delete is not just the removal, removing and removing at element and the index. Search is element and the search at index, correct? So if you can spend one hour to watch the videos and maybe

### 00:16:51 · Speaker 1

three to four hours to practice it and remaining half of the day. So you spent half day watching in remaining half of day I'll be discussing problems now. If you do you'll be get a fair understanding about the entire link list then you can go to any programming platform and practice the questions. Correct? How cool is it? So don't be scared about the link list. So in just with more less than forty minutes you are able to get most of the link list knowledge by my series. Okay? Thank you so much for watching. If you like the video please please like this video on my YouTube channel. Do not forget to subscribe to my channel Uncommon Geeks. Share the videos with your friends so that they can learn.

### 00:17:21 · Speaker 1

to get benefited and copy all the code that are present on Github. Okay, this entire code will be available so you can copy and practice. In case if there are any mistakes, feel free to mention that in comment section, I'll accept it. Okay, because I will be I have seen all the different flows I made to make sure before coding and it is covering. Okay, in case if there are any mistakes, please feel free to mention so that others get benefited than learning the wrong thing. Thank you so much for watching. Catch you in next video.
