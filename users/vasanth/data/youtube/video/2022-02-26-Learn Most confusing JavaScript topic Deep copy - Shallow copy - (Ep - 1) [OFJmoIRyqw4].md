---
id: OFJmoIRyqw4
title: Learn Most confusing JavaScript topic Deep copy - Shallow copy - (Ep - 1)
url: https://www.youtube.com/watch?v=OFJmoIRyqw4
date: '2022-02-26'
duration: 00:09:50
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# Learn Most confusing JavaScript topic Deep copy - Shallow copy - (Ep - 1)


## Transcript

### 00:00:01 · Speaker 1

Hello all, welcome to UncommonGeeks, myself Fajandh. I hope you all doing well. Today's topic is deep copy and shallow copy. Copying a value of a variable from one to another is considered to be one of the most basic feature of every programming language, and JavaScript is no different. In fact, deep copy and shallow copy are very straightforward topics. We can easily call them as copy by value and copy by reference. But the problem lies in the number of questions that can be asked around this topic. A very difficult questions

### 00:00:31 · Speaker 1

can be formed easily in this topic using arrays strings object and nesting of object nesting of objects and functions which will make candidate very confused during the interview I've seen those candidate who actually read this topic and came for the interview and they struggle to answer when a small variation of the simple question is asked so I'm they have taken this topic and I'll be covering in depth and asking all the different questions which are generally asked during the interview so that when such questions are asked for you during the interview

### 00:01:01 · Speaker 1

You'll be able to answer them very easily. Without wasting further time, let's get started.

### 00:01:06 · Speaker 2

variable

### 00:01:07 · Speaker 1

It's something that is common across all the programming languages

### 00:01:11 · Speaker 1

In JavaScript as well we have different ways of copying variables

### 00:01:15 · Speaker 2

from one to another

### 00:01:18 · Speaker 2

divided mainly into two things two two ways one is deep copy and another one is a shallow copy okay it's one of the interviewers hot topic most interviewers will ask question around this uh that the reason being it's very easy to create a tricky question in this topic okay so i want you to focus and understand this video thoroughly so that when i go to the next video where i'll be asking questions around this you'll be able to answer it very well okay without wasting further time let's get started

### 00:01:48 · Speaker 2

First let us see what is deep copy okay I am doing creating a variable x which is of time number and I am assigning it a value of 10.

### 00:01:58 · Speaker 2

So I'm creating a variable y which is also of type number mm y is coming

### 00:02:07 · Speaker 2

Annotation can be only used in TypeScript file it's like kind of a warning I don't think we there is any problem with this

### 00:02:15 · Speaker 2

And long

### 00:02:17 · Speaker 2

Value of X is X

### 00:02:23 · Speaker 2

And value of Y is

### 00:02:29 · Speaker 2

Let us execute this code I don't want you to answer because it is very straightforward you'll be able to answer I'm aware

### 00:02:36 · Speaker 2

Uh yeah maybe this annotation cannot be used in JavaScript so I'm not using

### 00:02:42 · Speaker 2

Let me just execute. So value of x is 10, value of y is also 10. Okay. Quite straightforward, nothing fancy here because this is something that everyone are using so you people are aware of it. I'll just make it y as 20 now and I rerun the code.

### 00:02:58 · Speaker 2

got y as 20. So, this is very straightforward, but what I want you to understand is we have created a variable with let x and the value in cell S to it is 10, then we created another variable y and we copied the value of x into it and again we added a new value into y and we made it 20. So, x is 10 and y is 20. So, what I want you to understand here is after you copy x to y and you updated y, there is no connection

### 00:03:28 · Speaker 2

between y and x so you copied here x to y and you are done so putting in other way from the programming constant so whenever you do this line basically the compiler will allocate a memory location to the variable x and it will store the value of 10 in that memory location okay and whenever you did this y is equal to x a new memory location is allocated to y and whatever the value that was there in x that is 10 is placed in that memory location so now x and y point to two different

### 00:03:58 · Speaker 2

memory location so whenever you change the value of y there is no connection to x okay this is a deep copy why this is called deep copy is after copying the values there is no connection between the two variables you are done so that is deep copy there is another one copy shallow copy but before going to shallow copy i'll tell on which all types you can make a deep copy okay we call them primitive types okay primitive types you will be able to make a deep copy that is number

### 00:04:29 · Speaker 2

number, string and boolean. So these are the three types on which you will be able to make a deep copy. Whenever you create a variable with these three types and you copy to another variable of same type, then you will be you are making a deep copy.

### 00:04:48 · Speaker 2

Now let us understand what is a shallow copy or a shallow copy. So let array1 is equals to 1 2 3 4 log array1 I am printing array1 okay and what I am doing is array2 is equals to array1 array2 dot push 5 log array2

### 00:05:16 · Speaker 2

Also, I am logging array 1. So, quite straightforward, I created an array and I added initialize that with the 4 values of integer type, then I am logging array 1, then I am copying array 1 to array 2 and for array 2, I am adding, I am pushing a value 5 as you know push as a JavaScript operation, array operation which will add element at the end of the array. So, now array 2 contains 5 values, 5 at the end, I am logging array 2, then I am logging array 1 again. Okay, let me run this.

### 00:05:44 · Speaker 2

So after running what we are getting is array1 we got 1234 which is fine because whatever the value we add into array1 that is getting printed here okay and in case of after that we are doing array2 is equal to array1 so we copied here then for only to array2 you have to observe this line here only to array2 you added the you pushed the value of 5 or you added a value 5 at the end of the array so we printed array2 it became 12345 but even array1 if you print after that that also is getting becoming 12345

### 00:06:14 · Speaker 2

for five just to extend what I'll do array one dot to push ten I am doing or six I am doing okay then what I'll do I'll print both the arrays

### 00:06:27 · Speaker 2

If you want we can make it array 1 and array 2. Okay. Let's see the output. See both arrays getting updated. So putting other way. We whatever the array 2 variable we created. Okay. It is not totally new variable. It is not it is it is not disconnected from array 1. There is some connection. Okay. I will tell you what is that connection. But before that I will give you some standard bookish bookish definition for both. Because some interviewers would expect you to tell

### 00:06:57 · Speaker 2

standard definition so I'm giving you this deep copy means that all the values of the new variable are copied and disconnected from the original variable like I already explained shallow copy means that certain or sub values are still connected to the original variable actually there is no standard definition for deep copy and shallow copy that is mentioned in developer.mozilla.com different authors have formed a definition according to their understanding but mainly whatever I'm showing you this definition that it means the same okay you you you're

### 00:07:27 · Speaker 2

free to tell tell this in your interview or wherever you want to tell this answer okay now I'll I'll explain this with the help of this uh uh image much in a very easy way

### 00:07:39 · Speaker 2

If you see him

### 00:07:42 · Speaker 2

have a shallow clone and deep clone or we can tell you shallow copy and deep copy and for your information this image is I have taken it from a medium blog I'll link I will mention that link of that medium blog in the video description and all the rights of this image goes to whoever has created it okay I'm just using it so in case of a shallow clone what's happening is first let us understand deep clone original object and reference object cloned object and reference clone so you can consider like this two are some

### 00:08:12 · Speaker 2

independent entities so after you copy right there is no connection they have disconnected but for the shallow clone both the cloned object and the original object basically pointing to the referenced object or in this case whenever I created let array okay array one as one two three four what happened was we were we allocated a four memory locations and starting location was a with with was with array okay array one what is happening whenever you copy array

### 00:08:42 · Speaker 2

to whenever you copy array 1 to array 2 basically both refer to the same memory location so because of which whenever you modify either array 2 or either array 1 you are technically modifying the same memory location due to which no matter which variable you modify

### 00:09:00 · Speaker 2

the both arrays are getting modified. So, this is a shallow copy ok. So, I believe now you are clear what is deep copy and what is shallow copy and in the next video I will be explaining you or I will be asking you various different question that can be asked on this topic, but I want you to understand this topic very clearly because 10 out of 8 interviews definitely they will ask you some question some or the other question on deep copy and shallow copy ok.

### 00:09:26 · Speaker 2

If you are like my video, please do like it on my YouTube channel. If you want your friends to learn from this, please share it with them. Do not forget to subscribe to our channel, Uncommon Geeks. And I have also linked my medium blog where I have explained deep copy and shallow copy. Please do read that. So you will get a lot of examples handy there. So you can just copy and go to your favorite editor and execute them. Okay. I'll see you in next video. Thank you.

