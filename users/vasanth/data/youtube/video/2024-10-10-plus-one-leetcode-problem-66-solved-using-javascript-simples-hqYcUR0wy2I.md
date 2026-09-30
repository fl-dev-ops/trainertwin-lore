---
id: hqYcUR0wy2I
title: 'Plus One | Leetcode problem #66 | Solved using #javascript | Simplest explanation
  ever'
date: '2024-10-10'
url: https://www.youtube.com/watch?v=hqYcUR0wy2I
description: "Get UIKits with 10,000 free mins: https://bit.ly/3ZDjRKJ\nTake Advantage\
  \ of ZEGOCLOUD: https://bit.ly/4eapJ2C\nTop 10 Video Conferencing APIs & SDKs: https://bit.ly/3Bi9LVB\n\
  \nIn this Video I have explained how to solve Plus One Leetcode problem in #javascript\
  \  (https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array).\
  \ This is an easy problem, but if you don't know the concepts very well, you cannot\
  \ solve it. I have tried explaining the simplest approach to solve this problem\
  \ in this video. \n\n @careerwithvasanth   is a Youtube channel dedicated to helping\
  \ candidates clear their interview. There are more than 150 videos and new videos\
  \ will be uploaded every week. If you're seriously preparing for interviews and\
  \ looking for tips and tricks, please subscribe to my channel and press the bell\
  \ icon.\n\nYou can get more mock interviews here : v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
  \nTo get a dedicated one on one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\
  \nJoin CareerwithVasanth community to discuss with other developers: t.me/uncommongeek.\
  \ \n\nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\n\
  Medium Blog https://mevasanth.medium.com/  \n\n\U0001F449 “Contact on WhatsApp:\
  \ 9731039408”\n\nJavaScript Interview preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:10:15
model: saaras:v3
transcript: true
---

# Plus One | Leetcode problem #66 | Solved using #javascript | Simplest explanation ever

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasant YouTube channel. My name is Vasant. I hope you all doing well. So this is a very important video where I'm going to continue to discuss more about the DSA question. So in this particular video also I'm going to discuss a lead code question. So where this looks like very easy problem to solve but it has a lot of intricacies. Okay? So if you want me to make more content about DSA videos, please mention that in the comment section. Just before we start with the question, recently I had a requirement where I was supposed to build a video calling application and we had couple of options. One is to use our in-house video

### 00:00:30 · Speaker 1

calling capability where we build things from scratch or we would use some external resources. The problem with even the using external resource was we wanted some tool that gives us the capability of video calling and the live chatting but we also wanted to make sure like that particular tool is gonna allow us to customize the UI. We don't had long a lot of time to build our own UI. So we encountered a new tool called Zigo Cloud. So I've used this in my lot of my projects where it has a UI kit makes your app building current easier. So it has so many things if you observe here the video call, voice call, live streaming.

### 00:01:00 · Speaker 1

in AppChat, Superboard, AIFX, cloud recording, probably anything a particular app that would require in terms of multimedia chatting and video call, they have it in place. And the beauty is, so you have the quick integration, few lines of code within thirty minutes. So you don't have to worry about writing the code on your own. A lot of code is built in, free credit. This is something that we really wanted. So we don't want to pay upfront and if the tool is not good, we are losing all our money. So almost ten thousand free minutes is given to you after you register with which you can build a lot of things and verify their

### 00:01:30 · Speaker 1

are they reliable or not? Only after that you can subscribe for their paid plans. Platform compatibility they integrate seemingly well whether it's React Native, Native Android, Native iOS, web. All of them it seamlessly integrates so you don't have to worry about anything. Another very important thing like was mentioned was UI kit. So we did not have so much time to build the UI on our own. Like for example on a group video call if we wanted to have multiple users with small user icons or small users on top of a larger image where we wanted that user rectangle

### 00:02:00 · Speaker 1

the corner should be rounded. All of those I don't have to write a single line of code everything we could do just by enabling and disabling the flag inside that UI kit. So it's wonderful for your next multimedia application I would highly recommend. Please go ahead and use that Zico cloud. Okay. Now without wasting further time let's get started with the project.

### 00:02:18 · Speaker 1

we have uh the problem is plus one. What is the problem? Let's read it. You are given an large integer represented as an integer array of digits where each digit of I is the Ith digit of the integer. The digits are ordered from most significant to least significant. Left to right, most significant to least significant, okay? So the larger integer does not contain any leading zeros.

### 00:02:43 · Speaker 1

increment the large number large integer by one and return the resulting array of rigid integers. Okay? So we have one two three as you might have not fully understood the problem statement let's go and look at an example. One two three output is one two four. The array represents an integer one two three. Increment the given by one two three plus one it's going to become one two four. Result by one two four as simple as that. Okay so same goes here four three two one. Four three two two because one is added here. Okay it was nine we are becoming ten.

### 00:03:13 · Speaker 1

Okay, very simple problem to look at and me also being a front end developer who is JavaScript, the simplest solution that we all think is convert the digit

### 00:03:24 · Speaker 1

array into a string. Okay, because we could merge all the numbers and make it to one string and convert that into a number and just add one to it and again you use the split and join to return another array. Correct? So that looks very tempting approach, but the problem is first you need to convert the digits into a single string. Okay, that itself is one of n complexity. After you do that, then you have to convert that into a number and then you add one to it. Number conversion is again

### 00:03:54 · Speaker 1

take some amount of the performance. And after adding one to it again you need to form a array, correct? So this looks good for a one to three. But if you look at here, the digit length can be can go up to hundred. So digit of I can be a maximum of nine character nine. So it's going to become a massive number like hundred, uh, hundred digits number you imagine. You are getting my point, right? Probably like, uh, like so big number. So convert making all these operations on that number is going to take lot of performance, okay? So instead what we can do? So, I'm gonna show I've drawn some diagrams here for better understanding. Let me present this. Okay.

### 00:04:34 · Speaker 1

So if you look at it here, so we have like one, two, three. So we add one to the last digits and we return the complete digit array. Simple. If three is a non nine character, if it anything other than nine,

### 00:04:49 · Speaker 1

we could just make this three plus one like whatever the digit plus one we will get the complete array as simple as that. So if it is nine so we will add one to it which is going to become make it zero here and whatever the digits that is prior to that we need to make that to one. So another variation where the ninth character uh if you see if if the last digit is nine so you are adding one to that and the previous digit whatever we have we will add plus one to that. Okay?

### 00:05:19 · Speaker 1

and we would return it.

### 00:05:23 · Speaker 1

previous digit whatever it is let's say it's instead of one zero one let's say it is of one eight one. So then we are going to eight plus one is equal to nine. So there's only one catch. What if this is also nine? Correct? You might be already thinking. Third variation. Where let's say all the numbers are nine. Okay? So nine plus one we make it ten. So we are going to do the plus one here. Okay? So we'll do the plus one here. So again it'll become nine plus one which is ten. Correct?

### 00:05:52 · Speaker 1

So the nine plus one which is going to become ten. So here also the nine plus one which is making zero. Here also nine plus one which is making zero. In such case by for some reason we crossed all the numbers. Okay? So the if you have crossed all the numbers without meeting either of these two condition then it is understood the the given number is only contains nine nine nine. In that case just add one to the beginning of the array. I'll repeat it the three variations. One the last digit is something adding it that adding it to one is not

### 00:06:22 · Speaker 1

making it ten. That's the first variation. Putting other way that this digit is not nine. Second variation is where the last digit is nine. Okay? So that adding one to it is making the number as ten. In such cases, whatever the last digit minus one, you add one to it and return the digits. Okay? For some reason, if the array is complete, but still you have not encountered one case one or case two, then it is understood you have all the digits as nine nine nine. Okay? It could be like three digit, five digit and probably ninety nine, nine digit.

### 00:06:52 · Speaker 1

correct? So in such cases, you just prepend the solution by one. Okay, make all the other digits as zero. Just prepend the array with one and return the results. Let's see, let's start by coding it. I will for the considering the duration of the video, I'm gonna fast forward this. Once I complete my coding, I'm gonna explain the solution to you. Okay?

### 00:07:24 · Speaker 1

Okay, my solution is accepted now. I made a couple of typos. I highly insist you avoid making those small typos, which is gonna give you red flag in the interview. So avoid doing that. I because the video I was doing little fast, I might have made that, but you guys don't do that in the interview. Now, the same solution what we discussed, I have actually implemented this year. So where I points to the last digit, length minus one, I greater than or equal to zero, I minus minus. If digits of I, which is this, if digits of I plus one not equal to ten, in this case, yes. So three plus one is four, which is

### 00:07:54 · Speaker 1

equal to ten, correct? So just return add digit of I, digits of I plus one. So three plus one which will become four, return digits array. So it will become one to four. Only one change. What if it is like one nine nine like probably one zero nine, correct? So in such case what is happening? One zero nine plus one or the digits of I which is the last digit is nine, nine plus one.

### 00:08:17 · Speaker 1

equals to ten. So we are not going inside this if. We are making the digits of I is equal to zero. So here the this digit has become zero now. Next, so I minus minus. So I is now pointing to this particular place. So what we are doing? Digits of zero. Digit of one plus one which is actually zero plus one, correct? So which is not equal to ten, correct? Because it's just one. So I'm adding that to one and returning the digits. So it has become one one zero. Example number three, nine nine nine plus one one one. So in this

### 00:08:47 · Speaker 1

this case. First scenario digits of I plus one not equal to ten correct because it's equal to ten. Then digits of I I made it as zero. So this became zero. Next this became zero. Next this became zero. As we are checking I greater than equal to zero. So the last case is when I was zero. So we came here. I is equal to zero. So we would enter I is equal to zero like I told only when neither of these conditions are met. Such case I just unshifted the array and added one to it and returned the digits. Okay unshift as most of you know.

### 00:09:17 · Speaker 1

reverse of push. Push will add a value at the end of the array. Unshift would add a value at the beginning of the array. Okay? So in this particular example, so unshift added one here and we returned these particular digits. Okay? I'm going to show the code again for loop if in the digits and again if i is equal to zero, this is the thing. Okay? I'm sure most of you understood this problem. The whole rational behind making this video is to make your thought process in a very creative way. Do not stick to the approach which you already know that is converting array and joining it and making into

### 00:09:47 · Speaker 1

making an output by using that approach. Please don't do that. Try to think of an innovative approach. Okay? And I hope you enjoyed the video. If you enjoyed the video, please like it, share with your friends, comment whatever you felt honestly. If you want more videos about the DSA, please mention that in the comment section. If you're not already subscribed to my channel Career with Vasant, please subscribe. Follow me on LinkedIn. I have fifty three thousand plus followers on my LinkedIn where I write actively about interview and career preparation and I write actively about medium. Follow me on medium as well. Thank you so much for watching. Catch you in the next video.
