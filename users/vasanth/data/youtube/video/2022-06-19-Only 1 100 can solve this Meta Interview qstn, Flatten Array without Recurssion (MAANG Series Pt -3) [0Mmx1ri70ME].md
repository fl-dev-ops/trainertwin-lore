---
id: 0Mmx1ri70ME
title: Only 1/100 can solve this Meta Interview qstn, Flatten Array without Recurssion
  (MAANG Series Pt -3)
url: https://www.youtube.com/watch?v=0Mmx1ri70ME
date: '2022-06-19'
duration: 00:10:18
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# Only 1/100 can solve this Meta Interview qstn, Flatten Array without Recurssion (MAANG Series Pt -3)


## Transcript

### 00:00:00 · Speaker 1

So today I have picked up a question which is asked in Facebook or Facebook or Meta, Amazon, Apple, Google, also in Microsoft. Okay, five companies have asked this. Don't think it is very old. Even in last April, 2022, April also they have asked this question.

### 00:00:20 · Speaker 2

Hi all welcome back to uncommon geeks myself Vasanth I hope you all doing well

### 00:00:25 · Speaker 1

So as you already know, this is a video series where we are discussing about the most common interview questions that are asked in MANG. MANG stands for Meta or Facebook, Apple, Amazon, Netflix and Google. Okay. So today I have picked up a question which is asked in Facebook or Facebook or Meta, Amazon, Apple, Google also in Microsoft. Okay. Five companies have asked this. Don't think it is very old. Even in last April, 2022, April also they have asked this question. Okay. So it's not, I have already discussed.

### 00:00:55 · Speaker 1

solution to this question in different ways in my articles and also in one of my video but in this particular video I am gonna give a all altogether different approach towards that problem this is very very important video if you are preparing for man interviews please watch this video till the end okay without wasting further time let's get started

### 00:01:15 · Speaker 1

This video is mainly on flattening the array in JavaScript. Okay, so in my medium blog, I've already written a beautiful article to explain how to flatten a given array in JavaScript. Okay, so to be very precise, if given this as an input, 1, 2, 3, 4, 5, 6, 7, which is a nested array or array of array, so you should flatten it. That's the requirement. Okay, I've written a recursive solution here. In my previous video, where I have explained a custom implementation of array.flat, even there, I have written a recursive approach itself.

### 00:01:45 · Speaker 1

In Facebook interviews, they have asked both solutions like an iterative solution, also a recursive solution. Okay. So in this video, I'll be discussing the iterative approach. So in same interview for the same candidate, they'll ask both approaches to it. The reason being how many different solutions that you can come up for a single problem. Okay. That's very, very important when you're applying for companies like this. Okay. Let me start by explaining you the flat first. So it is here as you can see. So if you run, so this three comma four,

### 00:02:15 · Speaker 1

away if you don't pass anything inside the flat it is considered as zero hierarchy okay so one level of hierarchy it will remove not zero hierarchy one hierarchy one array inside of this array will be removed one level of hierarchy if you pass infinity then it will remove all the hierarchy no matter how many array inside an array it will remove all the arrays and it will just make sure the entire array is flattened okay so this is about the array dot flat

### 00:02:42 · Speaker 1

And what recursive approach for this I've already shown you here, how we can write a recursive approach. So there is also iterative approach, which I've taken from here. Okay. I have not written this logic. I've taken this logic from here itself. I assume if it is documented here, this could have gone through a lot of iterations and best minds of the world might have approved this. So I am also picking the same and I'll be explaining you how to do that. Okay. I'll link this also in the description so that you can go ahead and read by yourself as well. Okay. Also my blog where I've explained the

### 00:03:12 · Speaker 1

approach very clearly also i'll link my youtube video where i've explained the recursive approach now without wasting further time let's get started but before i start writing the any code for the flattening if you are someone who is seriously preparing for javascript related interviews like vue angular node react etc so i would highly advise you to go ahead and watch my basic interview questions so i've linked that on the screen also in the description so 20 plus videos which are most commonly asked across all the companies okay and how to

### 00:03:42 · Speaker 1

approach that problem what mistakes can they do how to avoid that all of that i've explained the series if you don't watch that and directly landed here the problem is this is advanced level questions so companies like manga are asking it correct so if you are not watching that and directly landed in this video problem is you may not go to to this level only in the interview because every interview starts the basic question if you are answering the basic he would go for the advanced if you are not answering basic question itself then there is no point correct so watch that series and come to this video okay also i have created another video series from the

### 00:04:12 · Speaker 1

Custom implementation

### 00:04:14 · Speaker 2

So how to write your

### 00:04:15 · Speaker 1

own array dot map method array dot flat method array dot concat all of this okay so please watch that series also that has become very very trendy question across all the high paying jobs now implement your own functions watch that series also and come to this as a next level of further preparations okay now without wasting further time now let's get started so crux of the logic i'll explain first so you have an array a nested array

### 00:04:41 · Speaker 1

1 2 3 comma 4 okay so 3 comma 4 is a nested array

### 00:04:48 · Speaker 1

the entire array what you would do is you will get the last element of this okay by just array dot

### 00:04:56 · Speaker 1

Okay, array.pop would give you the last element, correct? So you can log last. Then what you would do is you will push that value, push that array back into the source array, but without using the array brackets. So how you do that is array.push, you will just spread the last.

### 00:05:19 · Speaker 1

What this does is three comma four will turn into three comma four.

### 00:05:26 · Speaker 1

the array bracket will be eliminated due to which the output will be if you log it now array it will be 1 comma 2 comma 3 comma 4

### 00:05:36 · Speaker 1

that array bracket will be gone. So, this is the crux of the logic. So, what you would do is you will take the last element and insert it back to the array if it is an array. If it is not an array in the case of 1 and 2 it is not an array then just push this values into a result. Okay. Let me run this. So, you are seeing 3 4 was the last correct this was the last.

### 00:05:59 · Speaker 1

one two three four is the array that is the final output so this is the crux okay first you should always try to find out the crux or a repeating pattern in the question with which you can form a solution so now you know the crux with this logic you will be implementing the actual implementation okay so I don't need these so I'm removing I would need this the two statements I'll I'll keep them okay function now I'll create flatten array flatten array is

### 00:06:29 · Speaker 1

my function okay which will take input as the input array so I would call flatten array from this log okay what I would do is I'm using a variable called stack actually it's a stack based approach only stack I think most of you know first in last out okay arranging of plates you pick the last plate in the first

### 00:06:52 · Speaker 1

reason a spread operator okay so here usage of spread operator is because not because of anything any significant reason it is mainly because this input is used uh not to use the same reference of this array okay they want to use a different array reference here so you're using dot dot dot input here okay as array passed always arrays passed as a reference and not by value okay now now it's very simple what you would do is you also need an a variable to hold the output cons response is this okay then

### 00:07:22 · Speaker 1

Then you have a while loop inside which you will check and you will run this till stack is not empty

### 00:07:31 · Speaker 1

Then what you do is very simple same like you will get the last element from the stack by using the stack dot pop

### 00:07:39 · Speaker 1

two two things are possible one array is one one the last value is an array second last value is not an array correct so if

### 00:07:49 · Speaker 1

And else, see, I have practiced this solution before giving explaining you guys. But otherwise also, I will have a solid bifurcation of the problem, correct? So first I know the crux. Then I know what are the major two conditions. If this condition what I do, this condition what I'll do. An algorithm should think, algorithm should run in your mind. Then only you will be able to write an efficient code, okay? So please do follow in this direction whenever you are thinking in the interview. Now, if first you need to check whether last element is an array,

### 00:08:19 · Speaker 1

So you know array.ezarray method is available which will help you to identify that. So I'm passing last here.

### 00:08:26 · Speaker 1

So if it is not an array in this case 1 and 2 are not an array you can directly push it into the result correct result dot push you are pushing the array of sorry you are pushing the last value correct if it is an array then also you know by the crux what you need to do correct you will push the value back into the stack only thing is you will extract it only thing is you will use a dot operator just to get the remove that array brackets spread operator you will use to get the values out of the array okay.

### 00:08:56 · Speaker 1

Then you have to return the result. Only thing that you have to make a change here is you have to reverse the return. The reason being you are popping the values, putting other way, you are iterating the array from the last. So you have to reverse it and you have to send it as a response. Okay. First let us run, then we'll see what is happening. So 3, 4 is happening. Let's say I put 5 here.

### 00:09:20 · Speaker 1

So it is flattening. Okay. So that's about the crux of the logic and how to flatten the array in a iterative approach. Okay. So, so was and why you pop? Can we now do this by using the first, like rather using the last element? Can't we use from the first element? Obviously, you can do that also. Like you would start iterating from this, keep pushing the values. Then whenever an array is encountered, then you can, you can follow the similar approach. Even that is also possible. Okay. I'm just sticking to the Mozilla approach considering that could be the best.

### 00:09:50 · Speaker 1

approach possible okay so if you like the content that i have made in this video please do like this video on youtube channel do not forget to share the videos with your friends and please do subscribe to my channel uncommon geeks that will help me to make more such good content i also link my medium blog this in this video link in the description please do subscribe to please do follow me on the medium as well okay i'll be putting the solution in my github repository you can copy that and practice on your own okay thank you again for watching this video catch you in the next one

