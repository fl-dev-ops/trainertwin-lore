---
id: CSkwIceygEU
title: Learn LinkedList in JavaScript with just 40 mins - Search Elements (LinkedList
  Part 2)
date: '2022-07-10'
url: https://www.youtube.com/watch?v=CSkwIceygEU
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Often most frontEnd developers consider DS/Algo as one of the tufts topics to\
  \ understand. They also get rejected in a lot of interviews, because of this. To\
  \ overcome this problem and help all frontEnd developers to pursue their dream job,\
  \ I have come up with detailed DS/Algo Tutorials in JavaScript. I will be covering\
  \ all the common data structures and problems around that in this video.\n\n\nLearn\
  \ LinkedList in JavaScript Part 1: https://youtu.be/EoQuO2RsJX8\nIntroduction to\
  \ LinkedList in JS : https://youtu.be/5Z6tpdmtzG0\nIntroduction to DS/Algo in JS:\
  \ https://youtu.be/DkarkyD-LkQ\n\nHow add custom methods to JavaScript Prototype:\
  \ https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s \n\n\nHow to write custom implementation\
  \ for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU \n\n\nInterview\
  \ Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  Medium Blog https://mevasanth.medium.com/ \n\n\nGithub Repository that contains\
  \ examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:13:45
model: saaras:v3
transcript: true
---

# Learn LinkedList in JavaScript with just 40 mins - Search Elements (LinkedList Part 2)

## Transcript

### 00:00:00 · Speaker 1

So I am not going to teach you how to code, you know that. I'm going to teach you the mindset, how you proactively think and try to code it, okay? If you understand at least this searching, definitely you'll be able to decode most of the things by your own in the my next video.

### 00:00:18 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself Vasanth. I hope you all doing well. As soon as there's a video series where we're discussing about data structure and algorithm in JavaScript, I've already explained in the introduction how this series is going to be and what is linked list and I've also shown basic operations of linked list in my previous video. In case if you've not watched those videos, I'll try to put that link on the screen also in description section. Please watch because without that if you come directly this video will be utter waste. You'll not be able to cope up because I've already written adding element to linked list, printing list, printing the elements of

### 00:00:48 · Speaker 1

link list etcetera. Correct? So please watch the videos then let us you can continue with this video. Now, for those of you already watched my two previous videos in this video, we already know we have added the elements and we have displayed the elements, correct? Now, the third most basic operation is searching. Searching can happen in two ways. One, searching an element and searching the element at an index, correct? Both the searching I'm going to show you in this video, okay? But before I we start coding, let's go back and first look at the single link list structure.

### 00:01:18 · Speaker 1

correct? So this is our basic. So I am not going to teach you how to code, you know that. I'm going to teach you the mindset, how you proactively think and try to code it, okay? If you understand at least this searching, definitely you'll be able to decode most of the things by your own in my next video, that is removing elements, okay? Now,

### 00:01:36 · Speaker 1

If you see, so searching, searching like I mentioned, let's start with basic searching, whether it element or at the index. First thing, what is the possibility? Head could be null. So in that case, the element doesn't exist because the linked list itself is empty, correct? In that case, directly we can return minus one. The next scenario. Next scenario is you can in case of searching an element from an index, correct? If you send an index in negative, then we will not be able to give you any value. If you send an index beyond the

### 00:02:06 · Speaker 1

last value, correct? Whatever the element, then also there will not be any value, correct? So those are two things. If you are trying to send an search by element, when that element doesn't exist, then also we will not be able to send anything. In all the cases, I try to return minus one whenever the head itself is empty, false wherever we are not finding to time getting we are getting the elements, okay? So, let us now try to decode the logic. So what is happening? So it's a linked list. All one node is connecting to other node. There is no way where we suddenly

### 00:02:36 · Speaker 1

going to a node and see whether it exists. So can we do the binary search? Yes, if the link list is sorted, otherwise you have to sort it and do. It may save some time but not too much like an array, correct? The easiest way is let's do a linear search where we go element by element and try to find where the element is present, correct? So what you do, you already know how to traverse the link list, you just check whether in that particular index the element present or that element is present in the current node. That's all, correct? I think most of you would be thinking if you watched my previous video,

### 00:03:06 · Speaker 1

Let's start coding. So you can code along with me and in case if somewhere you feel confident try to stop video, code on your own, come back and check whether the code whatever we both have written is matching, okay? Now let's first start by

### 00:03:20 · Speaker 0

search element

### 00:03:21 · Speaker 1

okay? Comparatively easier one. For those of you who have not watched my previous video, I've clearly decoded how the uh how linked list is not as linked list in any other programming language. Linked list in JavaScript totally different. How it is represented in object, okay? If you're not, don't please watch my first and second videos, okay? Now in search element, you have to pass an element, correct? So do I have a trace of it? Yeah, let me delete. So these are things that I was practicing to make sure I do the right coding. So here, I have a search element, I'm passing the element, okay? Now,

### 00:03:51 · Speaker 1

You know the process, so same, same as the add element. So if head is null, okay? That means there is no element, then there is no way we can search. So you're returning minus one, correct? Now.

### 00:04:04 · Speaker 1

In case if uh the the element no there's only two ways actually this is not on index right so now what we are gonna do. So what we'll be doing is let

### 00:04:15 · Speaker 1

current. Same, same, maybe that also we can copy from here. Let current this dot head while current current dot next. So this is one way I think kind of a similar step that gonna be for most of the logic that we'll be writing. Okay? Now. So here, what we are we'll trying to do here is, so we we are iterating. What we need to do now is if

### 00:04:38 · Speaker 1

So current dot element is equals to element. That's it, correct? So return true, it present, otherwise outside the while return false.

### 00:04:51 · Speaker 1

So simple, correct? So what we did, I'm going to explain once again, correct? So, uh if I go back to the sketch, let me select this all and delete. So basically we have uh if I have to draw in very simple words, we have one node, correct? We have one node.

### 00:05:08 · Speaker 1

correct, where we have a value of ten, let us say, correct. Next we have another node with a value of twenty, correct. Next we have another node with a value of thirty, correct. So what we are doing, we are trying to iterate this, correct. So head is pointing to this, correct. Head is pointing to this, correct. Head is pointing to this and this is linked to this, this is linked to this, correct. So now what we are doing, we are trying to

### 00:05:38 · Speaker 1

First first come to this node and see this is as you know this is an element field and this is the link field. So if I had changed my crayon color. So color.

### 00:05:51 · Speaker 1

maybe make it green. Okay. So if you see, so this is a link, correct? So this is a link and this is the link. So every node has a link field or the next property to navigate to the next node. It also has a value. All we are doing is go to the node, compare its value with the value passed. If it is yes, return true. If it is not present even in the entire list, by default we'll send it as false, correct? So inside here if you see while current, so here I'm returning true. As you know, as soon as you return the the execution context is

### 00:06:21 · Speaker 1

ended, control will go back from this code. So no longer the while loop will run. If this condition never became true, then definitely the value doesn't exist or we return it as false. Let's see whether it works, okay? So

### 00:06:35 · Speaker 1

So log LL.search element, okay, we have ten in the this one, correct? So I'm sending ten. Let's see, ten is present, correct? Let us send thirty.

### 00:06:48 · Speaker 1

thirty is present? No, thirty is not present. Why it is coming as not present? In fact, to show you only I am doing this, okay? See, we are doing current is equal to current dot next. So while of you are doing current dot next. If you see in this example, so this is null, correct? In the last case, this is null. What is happening? While is not running this one because the last node is null, correct? So whenever you are doing some operations, you shouldn't run current dot next, you should just run

### 00:07:18 · Speaker 1

the current. Current anyhow becomes null at a point, correct? Even in the last node the value should run. So if you run now, now also it came empty, yeah. Let's try to decode, okay? So LL search element, we are passing thirty. Actually thirty is present? Yes, thirty is already present. That we can confirm by

### 00:07:39 · Speaker 1

login l l dot print list okay

### 00:07:45 · Speaker 1

present, correct? Then we are trying to do search, search element, correct? So now we are doing current dot next below itself.

### 00:07:54 · Speaker 1

current.element is equal to element we are doing return true. Correct? And we are returning false here. The last one I'm saving. Let's try once again.

### 00:08:04 · Speaker 1

Yeah, it's coming true. I don't know whether there was a mistake. I did not check it properly. So as you see, we are getting the true. So thirty is present. Let us send hundred. Let's see if we get any error.

### 00:08:18 · Speaker 1

false hundred doesn't exist, correct? So, maybe we let's not insert any values, correct?

### 00:08:27 · Speaker 1

minus one. Correct? So all the scenarios that we discussed is covered in the program. So be mindful whenever doing the current.next, don't do it for the sake of doing, okay? Run this object in your mind. So whenever you're hitting the last object, correct? Last object's next is null. But last object has an element, correct? So that has to be tracked. So due to which you are doing the while current and while not current.next. Now let us do another search operation quickly, okay? That is search at.

### 00:08:57 · Speaker 1

search at index. So you have to pass the index, correct? Again, if you go back to the link list,

### 00:09:04 · Speaker 1

the the flow would remain the same you are the index cannot be beyond negative index cannot be beyond the length of the link list correct index has to be some valid index in the link list only then we can return if head is null again you return minus one because there is no index as such correct all the basic operations of the previous code also remain same here I'm copying this correct so if this is null return minus one correct this also correct

### 00:09:30 · Speaker 1

And then. So somebody also used this this concept where

### 00:09:37 · Speaker 1

Elseif

### 00:09:39 · Speaker 1

So I I use the size right? So size

### 00:09:44 · Speaker 1

if index size is greater than this dot size, correct? So then also I'm returning minus one. So either it could in case if it is negative, that also you can do. uh else if

### 00:09:57 · Speaker 1

So the I mean you can put all these checks. So I'm just adding few. Index is less than zero. Then also you will return minus one. Because negative index so we cannot return anything. We have to only can return the positive indexes correct? Now if none of this.

### 00:10:12 · Speaker 1

okay? So if none of this then we are using the else. So where the operation is quite much similar. So this as I already said is the same, correct? for a lot of things. So where here if current.element is equal element, no. What we need to do is here we need to keep a variable.

### 00:10:31 · Speaker 1

Let LL index, so which means link list index as zero, okay? Then what I'll do, I'll be incrementing the link list index. Okay, plus plus. What I'll do is if linked list index

### 00:10:44 · Speaker 1

is equals to the past index. Correct? Whatever the index that you have passed. If they are matching, then return the element present in that. Correct?

### 00:10:55 · Speaker 1

that's all we are doing because similar to what we did rather matching the element here we are matching the index if index are matching then return the value present in that index correct if nowhere it got matched correct if nowhere it got matched then you will return false so technically we are writing three states here minus one in all the exception case like when no link list is present or it is beyond the length of the link list or less than the negative number we are returning the value itself whenever we are having the we have

### 00:11:25 · Speaker 1

found what is the value in that index. We are sending false whenever there is no value in the given index or they have passed a sum index that doesn't exist in that kind of a scenario, okay? Or to avoid we can keep minus one here only to just two states whether you return the element or minus one in all the extremities, okay? I don't know let me just check again is whether I have written all correctly or not.

### 00:11:46 · Speaker 0

L L

### 00:11:47 · Speaker 1

index. Let me run probably, then probably we'll quickly come back and see, okay? So search element, no, search

### 00:11:57 · Speaker 0

at

### 00:11:57 · Speaker 1

Is there a search what I gave the name for it? Search element search at, correct? Search at, search at let me give zeroth index, okay? If I print search at, I'm just for the, I'm just commenting this to avoid the confusion.

### 00:12:15 · Speaker 1

So search at zeroth index is ten. Let's see search at the two index which should be thirty, correct? Thirty, search at two hundred index, it should be minus one as the index doesn't exist, correct?

### 00:12:26 · Speaker 1

should be minus one, let's say minus ten, where doesn't exist that index, minus one, okay? Or same, again let us confirm by not having any values in the link list, correct?

### 00:12:38 · Speaker 1

minus one. So basically we we kind of covered all the two basic search criteria, one with searching at index, another one is searching the element. So both are covered fine, correct? So now if you see, how easily we did it, correct? All you needed to understand is this object structure and this while loop, correct? Now in the next video whenever I do removing an element from index, that is slightly complicated because of some operations, but you will be able to do it very easily, I'll guarantee you that, okay? So

### 00:13:08 · Speaker 1

practice this maybe three four times this entire structure, be familiar with this block, then all the linked list operation will be very very easy for you, I'll guarantee you that, okay? If you like this content, please like this video on YouTube channel, so when more people like this will be promoted to so many people and I'll I'll become popular and moreover the video will become popular and so many people will be able to get this important knowledge. So do not forget to share this videos with your friends and please, please, please, please subscribe to Uncommon Geeks. So that will truly motivate me to make more good content. I'll add this entire code into my GitHub,

### 00:13:38 · Speaker 1

download it from Github project link will be in the description and you can also practice the questions all these on your own, okay? Thank you so much for watching catch you in next video.
