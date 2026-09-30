---
id: MrJEEuyDU0c
title: 2 Simple ways to Find Middle Element of the LinkedList in JavaScript (Learn
  LL in JS Part - 5)
date: '2022-07-12'
url: https://www.youtube.com/watch?v=MrJEEuyDU0c
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Often most frontEnd developers consider DS/Algo as one of the tufts topics to\
  \ understand. They also get rejected in a lot of interviews, because of this. To\
  \ overcome this problem and help all frontEnd developers to pursue their dream job,\
  \ I have come up with detailed DS/Algo Tutorials in JavaScript. I will be covering\
  \ all the common data structures and problems around that in this video.\n\n\nLearn\
  \ LinkedList in JavaScript Part 1: https://youtu.be/EoQuO2RsJX8\nLearn LinkedList\
  \ in JavaScript Part 2: https://youtu.be/CSkwIceygEU\nLinkedList in JavaScript Part\
  \ 3: https://youtu.be/nI8TXMzeznk\n\nIntroduction to LinkedList in JS : https://youtu.be/5Z6tpdmtzG0\n\
  Introduction to DS/Algo in JS: https://youtu.be/DkarkyD-LkQ\n\nHow add custom methods\
  \ to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s \n\
  \nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:16:44
model: saaras:v3
transcript: true
---

# 2 Simple ways to Find Middle Element of the LinkedList in JavaScript (Learn LL in JS Part - 5)

## Transcript

### 00:00:00 · Speaker 1

fast pointer. So after first iteration, do blue will travel two two boxes, one and two. So blue will be here, okay? And the green will be traveling only one index, okay? We have green here which will be traveling only one index.

### 00:00:19 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. As you know this is a video series where we are discussing about mainly data structures in JavaScript and past couple of videos we have discussing about linked list. As you know in last video itself we have completed the linked list basic operations and if you have not watched my previous videos I would highly advise please watch them because all the basic operations are completed in those videos and this video I'll be discussing about some of the most common interview questions, okay? So what is the question that I'll be discussing in this video is very

### 00:00:49 · Speaker 1

interview questions, okay? And it is will create a good thought process for you to how to approach on link list, okay? The question is finding how do you find the middle element in the link list, okay? So that is the question. I'll teach you two approaches, one a normal approach and one a advanced approach in this video. So please do watch the video till the end so that you get the complete insight about the how to find the middle element in the link list. Along with that you'll also learn lot of tricks related to link list, okay? So watch the video till the end and let's get started. So If you see

### 00:01:20 · Speaker 1

So I'll just continue from my previous example itself, the entire code remains the same, okay? So here you need to find the middle element, okay? So like I mentioned, see, you see already see a lot of code. If in case if you have not seen my previous videos, it will be quite tough for you to get along. So please watch the other videos. I'll link that on the screen, also in the description section. Now, here what you need to do, find middle element, correct?

### 00:01:43 · Speaker 1

find middle element is a function. Let us start by this. So how do you find the middle element? Correct? So in case if you remember, I am using a variable called size. Correct? I am using a variable called size. Every time whenever you add an element, I am increasing the size and every time whenever we are deleting an element, we are I am reducing the size. Okay, remove an element, I am reducing the size. So many might have thought why Vasant is doing this, now you something might be flashing in your mind. So at least for those who are very

### 00:02:13 · Speaker 1

very amateur about the link list. So finding the middle element means what? So you will get the length of the whatever the data structure, you divide it by two and you get the middle element, correct? So it's very easy. So you can do array dot length divided by two, you will get the middle element and that that you can return, correct? But link list has not no predefined length, correct? So if you see in this image which I just created for this video, so every time whenever you want a node, OS will give you a node, correct? So there is no length that is predefined, correct? Unlike the array.

### 00:02:43 · Speaker 1

So what is the problem? You don't know the length of the link list unless you maintain it in a external variable. So I'm maintaining a variable called this dot size which will which will maintain the size of the array. So what is the disadvantage of this? You are allocating a variable and it is let's say you are having a one million uh node in the array. So one variable is holding the million value, correct? Not a million value, a number million, correct? Which definitely takes some space. So without that also a lot of processing is possible. But I would advise you can use this approach because

### 00:03:13 · Speaker 1

finally you are using only one variable, okay? I'm going to use an advanced technique also, but this technique is also good where you can maintain a size. Now, you know the size, how many elements you have inserted, whenever you are removing you are decreasing the count. So now, here there are let's say five nodes, so five nodes you have inserted. Five divided by two, what is it? It is 2.5, correct? So 2.5 node doesn't exist, so you have to seal it, seal it means going to the next number. So 2.5 to the seal is three, so you will be able to identify, you will be able to

### 00:03:43 · Speaker 1

fine, this is the element. Correct? Whenever there are odd numbers, the middle number is the middle. That is one, two, three, four, five. So three is a middle node. But whenever there are even number of nodes, how do you determine the, how do you determine the middle element? Correct? So one, two, three, four, which is middle. Four by two is two. Okay? But with respect to something like this middle, this doesn't exist. So four, if it is, if you since the length of this is four, four by two will be two.

### 00:04:13 · Speaker 1

So it will be this node. Correct? It will be this node. So you can ask an interviewer for even number of node does it wants the second or the third as the middle element whenever there are four elements. Correct? So but technically this will be the middle element in such cases. Okay where the lower one. Okay? So this is how you can find the middle element let us code this. Please stay tuned I'll be teaching advanced technique also in a while. See if you are liking the content that I'm making on YouTube and you are watching the series from the beginning I would highly request please like

### 00:04:43 · Speaker 1

this video on YouTube and do not forget to share the videos with your friends and add a comment. If you're liking the video please add a comment. If you're not liking the video what I can improve please add a comment. By more and more likes that I get for a video YouTube will give more impressions to my video. Impressions as in it will show it to lot of people. When lot of people see it they get benefited. They will watch the video. Definitely my channel will grow but purpose is I'll be able to reach lot of people by the good content. So please don't continue watching before without liking the video. I I'll just request. Okay? Without wasting further time let's again

### 00:05:13 · Speaker 1

continue, okay? Now, you got the crux I think, correct? So what we will do? uh same, first thing to will remain same. If head is null, then there is no way we can calculate the middle element, correct? So if head is null, and if this condition is not required, if head is null, then we just return the minus one, which is straightforward, correct? So because there is no middle element. If not, then let middle

### 00:05:37 · Speaker 1

इंडेक्स इज इक्वल्स टू साइज़ डिवाइडेड बाय टू. करेक्ट? सो नॉट साइज़ डिवाइडेड बाय टू, यू ऑल्सो नीड टू डू मैथ डॉट

### 00:05:48 · Speaker 1

math.ceil. I guess most of you are aware of this function. math.ceil will just seal the number. For example, if you have 2.5, it will make it three. 2.8, it will make it three. 2.1, it will make it three. math.floor does the reverse. 2.9, it will make it to two. 2.2, it will make it to two. math.floor and ceil does the similar operation. Now here, so you got the middle index, correct? So now what you have to do, index you got, but it is not like array, correct? We are linked list of middle index, you cannot return. You have to traverse till that index, correct? So what I'm doing, I'm creating a

### 00:06:18 · Speaker 1

for loop. Why for loop? Because you could have used the while loop. Many use the while loop also. But technically, I know the index till which I need to run, correct? Then is the right use case of for for. When I don't know how far I need to traverse, then you can use the while. It's something dynamic, correct? So for is the right use case according to me here. So now I'm running the for loop till the middle index. I'll explain with this with the pictorial also, don't worry.

### 00:06:43 · Speaker 1

Then what I'll do, same thing, middle index. So you you know one other thing that we need to do. Let current is equal to

### 00:06:53 · Speaker 1

this dot head, correct? Then current is equals to current dot

### 00:07:00 · Speaker 1

next. Finally, whenever you have reached this middle index, for example, in five nodes, so you started the iteration with zero, zero, one and two. If I go to the image, so zero, one and two, correct? So we had size was five, so five by two, correct? So five by two is equal to two point five and we are ceiling it, it will becomes three, correct? So three, so we are running the fallout from zero to three, so zero, one and two, whenever it goes here, it will fail, correct? So we are here.

### 00:07:30 · Speaker 1

and it will come out of the for loop. Then what you will do? You will just return the current dot element. You are done, that's it. Let's try to see in case if I miss something, okay? uh print a list.

### 00:07:45 · Speaker 1

log

### 00:07:47 · Speaker 1

L L dot find middle element, okay? I'm running. So it came forty. uh Maybe if I floor what I'll get? Let's see.

### 00:07:59 · Speaker 1

if I floor I'm getting thirty if I seal I'm getting so why because we have five so five divided by two is two point five two point five two we are making it a three so zero one two three so middle index is what

### 00:08:16 · Speaker 1

So this five by two is two point five and middle index is three now. So zero one two three times it is going so zero one two but current dot next has also executed. Okay. So problem if you see here what what was happening. So we are trying to do math dot floor correct math dot seal math dot seal means moving the number to the next number. So in this case zero one two three four five correct. So in this case what is happening so we are getting the five by two as two point five and we are making it to three.

### 00:08:46 · Speaker 1

So this this is running fine but what is happening by the time it fails current even in that scenario so current is pointing to its next node. So due to which this is kind of going to one level up so I'm just making the method out floor. So in that case even if given if it goes to the next index I'll not have a problem. But now we need to test with even index also correct?

### 00:09:08 · Speaker 1

So it is coming as thirty now instead of the twenty. Okay? So now whether twenty is correct or thirty is correct, it is something that the interviewer should answer you. Okay? So ask the interviewer in case of even number of elements, what is the expectation, which is the middle element. Okay? Ask the interviewer and code accordingly. So this was one of the I know it's not so preferred approach on the internet because nobody uses the size. The preferred approach on the internet or what many will be doing is a two called two pointer approach. So what is two pointer approach is there will be two pointers.

### 00:09:38 · Speaker 1

one pointer will be one pointer will be traveling two points at a time. Another pointer will be pointing to one point at a time. Okay, don't get confused. Let us start with here. So they will be having two pointers. So both the pointers initially point here. Okay. Both the pointers initially point here. Now, what will happen is this low pointer will be pointing every iteration one index. Okay. So let us maybe let us use two crayons. Okay. So green for slow and

### 00:10:10 · Speaker 1

which color let us take let us take some blue okay? the blue for the fast pointer okay? so blue I'm taking for the fast pointer. so after first iteration do blue will travel two two boxes one and two so blue will be here okay? and the green will be traveling only one index okay? we have green here which will be traveling only one index. now in the second iteration again so blue this blue okay? so this blue will be traveling

### 00:10:39 · Speaker 1

So this blue will be traveling

### 00:10:44 · Speaker 1

So this blue will be traveling two indexes. So it is here, correct? This blue has traveled here. Whereas our green will travel to again one index, correct? So which is here.

### 00:10:56 · Speaker 1

So now hope you're getting a sense where

### 00:10:59 · Speaker 1

whatever when the blue index reaches the end, the green index or the whenever the fast pointer has reached the end, the slow pointer will be pointing to the middle element, correct? Let us try to mimic that in below as well, okay?

### 00:11:12 · Speaker 1

So both here, okay? Pointing here in the beginning. Next, uh this will be pointing to the two elements after, correct? Which is here.

### 00:11:24 · Speaker 1

in the first go. And this will be pointing here. Only one index it has moved. Correct? And after that, there is no index to go to the two pointers. Correct? Somewhere it will go beyond or next of next. Correct? Whereas this on the other hand will come here to the third index. Correct?

### 00:11:43 · Speaker 1

become on the third index. So this is considered to be middle. Got the point, right? So just a simple two-pointer approach. So this is this is considered to be slightly efficient than the the the iterative approach. We did not do iterative approach. Iterative approach is just like nothing but you go through each of the block, calculate how many elements are there, correct? Then you get the length, divide that by two, iterate the array again or linked list again and go to the middle element. That we did not do because we are brilliant, we have used the size concept. If not used the size concept, we have to travel it linearly.

### 00:12:13 · Speaker 1

So consider that as a homework for you. Try to implement the linear approach where you can find the middle element. Traverse once, get the length, divide that by two, then traverse that to the again to the that length. So now let us decode the two pointer approach. Okay? So, so find element, find middle element, two pointer approach.

### 00:12:33 · Speaker 1

Okay, two-pointer approach.

### 00:12:36 · Speaker 1

Don't get confused. I'll explain once again if you anyone of you getting confused, okay? So this remains same.

### 00:12:43 · Speaker 1

And then I have two pointers. One is let slow pointer

### 00:12:48 · Speaker 1

Okay? Same, like the explanation, it will point to the head itself. Then we have fast.

### 00:12:56 · Speaker 1

we have fast pointer, okay, which is equals to again this dot head. Now, we have slow pointer and fast pointer. We you know what needs to be done. So you need to run till when the till the fast pointer is not null, you will be learning, correct? Fast pointer not equal to null or and actually. Fast pointer dot next should also be not null, correct? Where you shouldn't go beyond the the list length, correct? What happened in the even case scenario, correct? Now here, what we have

### 00:13:26 · Speaker 1

doing here is again fast pointer is equals to fast pointer dot next dot next that's all if you have to travel two times correct slow pointer on the other way is very easy slow pointer is equals to slow slow pointer dot next

### 00:13:43 · Speaker 1

Okay, finally what you will return? Return

### 00:13:48 · Speaker 1

slow pointer dot element. Correct you already know when the fast pointer has exceeded the list or it has reached the last element the slow pointer is pointing to the middle element correct. So now find middle element with this approach let us see what we will get.

### 00:14:05 · Speaker 1

So we got thirty, correct? Same as the previous example. If I uncomment this, what I'm getting? I'm getting thirty, correct? uh In this scenario also, let's say I have added sixty, correct? So sixty I am adding here. Okay? Sixty I am adding here.

### 00:14:22 · Speaker 1

So you're getting forty, correct? So it's a even number basically, correct? So again I'll do the find middle element, both the cases I should be getting the same value, okay? Forty forty I'm getting. So I'm sticking to this approach of forty, so whenever you have even numbers you can just ask the interviewer to get some confirmation and modify it accordingly. But now I think you know all the things, so if you have only the five, so thirty should be the middle element, correct? So thirty you are getting here as well and here even two pointer approach as well, correct? So that's all.

### 00:14:52 · Speaker 1

about the different techniques. One last time I'll explain you with the objects and I'll end, okay? In case if you watched already and got the point already, please like the video, share the video with your friends, subscribe and you can stop watching. For those of you who are still not clear, I'll just explain with object. So now here you have the object, correct?

### 00:15:10 · Speaker 1

So what we are doing here is a fast pointer and the slow pointer. So first both are pointing to here, okay? Fast pointer now points here. First it will be, I mean both will be pointing to this node, okay, the head. Then the fast pointer will be pointing to one and two here, okay? Fast will be pointing here. Slow will be pointing here, okay? Next fast will go to the next two things, this one and two. So the fast will reach here, okay? In that case, the slow will be coming again here.

### 00:15:39 · Speaker 1

correct? Slow has traveled from there to here. So now slow is the element. So slow is the element I'm retaining which is thirty. That's all, okay? So always keep this object things in your mind and you can start coding. Anywhere you stuck, don't get panic, there is nothing wrong can go here, correct? Because this is like a coding is nothing but a writing like a writing a novel, correct? So you know what is everything, you know everything what has happened, you have created the characters, correct? So you know who is doing what, who is who will be doing what. So you can modify the things, you can see, let's say I haven't created this one, it may fail, correct?

### 00:16:09 · Speaker 1

where there is a use odd number it may not fail, even number it will fail. Just add the check. Just you should be able to figure out where there could be a problem and just fix it. Correct? That's all about this video. I'll catch you next video with another very very interesting problem, okay, about single linked list itself. Thank you so much for watching. Please like the video on my YouTube channel. Do not forget to comment if you're liking or not liking or whatever the improvements that you want. If I've made some mistake, please add that also in the comment section. I'll try to correct it in the upcoming videos. Do not forget to subscribe to Uncommon Geeks. This entire code is available on

### 00:16:39 · Speaker 1

my GitHub, you can copy that code and practice on your own. Thank you so much for watching. Catch you in next video.
