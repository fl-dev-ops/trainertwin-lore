---
id: FSohIrjKv_U
title: 'Pascal''s triangle | Leetcode problem #118 | Solved using #javascript | Simplest
  explanation ever'
date: '2024-10-25'
url: https://www.youtube.com/watch?v=FSohIrjKv_U
description: "#dsa #datastructures #algorithm #javascript #typescript \n\n@careerwithvasanth\
  \   is a Youtube channel dedicated to helping candidates clear their interview.\
  \ There are more than 150 videos and new videos will be uploaded every week. If\
  \ you're seriously preparing for interviews and looking for tips and tricks, please\
  \ subscribe to my channel and press the bell icon.\n\nIn this Video I have explained\
  \ how to solve Pascal's Triagnle Leetcode problem in #javascript  ( https://leetcode.com/problems/pascals-triangle/description/).\
  \ This is an easy problem, but it will trick you easily, if you don't read the problem\
  \ description fully and make a mistake while solving it. \n\nYou can get more mock\
  \ interviews here : https://www.youtube.com/playlist?list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD\n\
  \nTo get a dedicated one on one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\
  \nJoin CareerwithVasanth community to discuss with other developers: t.me/uncommongeek.\
  \ \n\nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\n\
  Medium Blog https://mevasanth.medium.com/  \n\nJavaScript Interview preparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:09:08
model: saaras:v3
transcript: true
---

# Pascal's triangle | Leetcode problem #118 | Solved using #javascript | Simplest explanation ever

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So this is a video series where we are discussing about DSA problem. Without wasting further time, let's get started. So in this particular video, I'm solving a very important interviewer's favorite interview question that is Pascal's triangle. What is Pascal's triangle? Given an integer number of rows, return the first number of Pascal's triangle. This is a question statement. But Pascal's triangle where each number is the sum of the two numbers directly above it. Okay? Just for the better understanding, I've taken a diagram where any given

### 00:00:30 · Speaker 1

any given row it is actually the sum of directly which is above them two rows above them like six is a combination of three plus three fifteen is a combination of this thirty five is a combination of this two okay ten is a combination of six plus four for any given row the sum is produced by the two particular columns above them okay so Pascal's triangle each number is a sum of the two numbers directly above it as it is shown like for example if you consider each of this as row so this particular column sum is actually something that is

### 00:01:00 · Speaker 1

combination of the columns above them, okay? What is the problem given the number of rows, like in this case five, should written all the combination of the numbers like one, one comma one, one comma two comma one, this complete thing is a multi-dimensional array, this is a two-dimensional array, correct? So now

### 00:01:15 · Speaker 1

if you are somebody who is from a front end developer background and you have never solved BSA problems, problems like Pascal's triangles are not very easy to solve. If you are somebody who is always solving the problem that is easy, but if you are somebody who is looking at the Pascal's triangle for the first time, it's not so easy to solve because all you are given is number of rows. So number of rows is the only thing that you are given, like for example five and with that you need to actually generate this complete thing, correct? So it's not so easy for you. So I'm going to tell you step by step how to approach this problem and if you are seeing me for the first time,

### 00:01:45 · Speaker 1

on the internet like I already told my name is Vasanth please subscribe to my channel Career with Vasanth like the video and comment whatever you are feeling so far what the lot content about front end interview preparation please watch and support. So now the problem is we only know the row and we need to populate this entire entire Pascal's triangle and before I start explaining the solution actually Pascal's triangle is used in lot of probability theory so whenever you solve such problems also do know where it is actually getting used okay. Now let's say I have to generate this one. and this one. For the easy understanding sake, let's go to this column.

### 00:02:20 · Speaker 1

four is actually sum of one plus three. Six is sum of three plus three, four is sum of again three plus one, one. So the problem what we are facing is there are like one, two, three, four columns. Here we have five columns. From four columns we need to generate the five columns or if you go to here, oh there's only one. From one we need to generate two things. That's where the problem comes in. What we can do instead is let's say I add two more columns. I make this as zero and this also as zero.

### 00:02:50 · Speaker 1

okay? So in that case, the sum of these two will produce this, sum of these two will produce this. For a better understanding I'm gonna put the zero here. Okay, I'm gonna add, let's say this is a column, right? So I'm adding a two more values or if you consider this an array, I'm adding one value at the end and one value at the end. One value in the beginning and one value at the end. So zero plus one becomes one, one plus four becomes five, six, ten, ten, four plus one five, one plus zero is one. So this is how it is easiest to solve. So there is nothing

### 00:03:20 · Speaker 1

to solve if you took the X approach. All you do is you take up each row. You unshift it, add a zero, you push a value zero. All you have to do is just keep adding them. Like zero plus one, like I plus I plus one index if you add, the next row gets generated. It's very easy. The only catch with this approach is unshifting. As you know if you have to insert an element in the beginning of the array in JavaScript, you need to unshift it. Whenever you unshift, the problem is you are you're thinking you're adding one value in the beginning of the array, but indirectly you're pushing all the values.

### 00:03:50 · Speaker 1

in the array to the next index, correct? So when the the tree becomes bigger and bigger, this will have a performance implication, correct? Pushing a value is still fine, this is still fine, but this is something that is a problematic.

### 00:04:01 · Speaker 1

But there's one approach which you can solve with this particular approach very easily. Now let's let's take a look at a slightly extension of this solution itself which is much more capable of solving the problem, much more efficient. For example, any given column if you have to generate, right? So this will be combination of the previous columns or any particular column in a row you have to generate. It is going to be combination of previous rows, two columns above them. Correct? Let's think about the same approach that we discussed.

### 00:04:31 · Speaker 1

whenever there is no previous column. whenever there is no previous column, let's imagine that as a zero. Okay? For example, let's take this as uh I throw and this is J throw. Now, I let's say I initialize I throw as one. The very first we cannot to start a process, let's consider this as the first value of and in the array is just one. Now I have to calculate the J throw. J throw I can calculate by taking the value of of any for example the zero. the j j throw zeroth column can be computed as a sum of

### 00:05:09 · Speaker 1

I throw, correct? I throw J minus one and J. So here you can understand better. So if I name it like this is zero, one, two, three, this is zero, one and two. So this one is a sum of zero plus one. This two is a sum of one plus two. So whatever the J index, that index and the minus of that. For three, this is where the problem comes because three, we have three minus two.

### 00:05:39 · Speaker 1

this doesn't exist. For zero, you have jth column is there, but j minus one is not there. Same applies here. Here jth column is not there, j minus one column is there. All you have to do is whenever that value do not exist, just return zero. That's what we did in the last approach of unshifting. Here, that particular unshifting we are not doing, we're just returning the zero, okay? Let's solve the problem. For the overall duration point of view, this section I'm going to fast forward and I'm going to explain the solution once I complete the solution, okay?

### 00:06:25 · Speaker 1

So my solution got submitted. I did a couple of silly mistakes. I again last video also I made a small mistake. I insist you guys do not make it. I in a rush to make complete the video quickly I'm gonna do I might have made that but you guys don't make it. So once I have to complete the things just go and cross check everything one more time. So now the solution is very simple. The very first I've initialized output array with just one value. That is just one. And next if number of rows is one. So I would immediately return this only. I don't have to do further processing. If not then I'm gonna tell the number of rows. How many ever rows.

### 00:06:55 · Speaker 1

and I is one. Why I is one? Because zeroth row is already done. So I am starting from one. So then J is zero.

### 00:07:03 · Speaker 1

So J basically we are generating this row now. J is zero, J less than I plus one. Because any given row will be a combination of like whatever the row we I will be that plus one number of elements is gonna be there in every every particular uh row. So for J is equal to zero, J less than I plus one and J plus plus output of I minus one same way I explained you. I minus one means zero. Correct? So this row is actually combination of I minus one. The previous rows J minus one and J. All you have to remember is

### 00:07:33 · Speaker 1

these two lines. Output of I minus one, J minus one and output of I minus one and J. If they're not there, just return zero. That's all we are doing. Some and push it to the temporary array. Because why you have to push it to the temporary array? Because this complete row has to be populated. Correct? Like first you generate one, then you generate two, then you generate one. So this becomes one array. Correct? Once this array is generated, then you push it to the output. Finally you return the output. So if you have to, if you have to see the way of execution. you can just log the temp. Okay? I run it.

### 00:08:10 · Speaker 1

So you see first it was one and one, the first row. Next it is one to one, the second row. Next it is third row, one three three one. Next it is one four six four one, the last row. And once after every row is generated and before I go to the next row I'm going I'm actually pushing it to the output array. That's all. Okay? I hope you enjoy the video. Like I told the first solution of unshifting I have not written. If you understood this that particular approach very well I highly request you to please write that approach and put the code in the comment section. I'll validate your code and let you know whether it's right or not. Okay? Thank you so much for watching. If you like

### 00:08:40 · Speaker 1

the video please like it. If you are somebody who's seriously preparing for the DSA, keep subscribed and like the video and comment what more videos I want to bring in because front end there are very less resources about the DSA. And if you are someone who is uh preparing for any other front end developer interview or looking for mock interviews, React basics, JavaScript basics, there are so many series in the channel. All of them I will put in the description section. Please go ahead and check it out. And I read very actively on LinkedIn and Medium. Do follow me on LinkedIn and Medium. That's all for this video. Thank you so much for watching. Catch you in the next video.
