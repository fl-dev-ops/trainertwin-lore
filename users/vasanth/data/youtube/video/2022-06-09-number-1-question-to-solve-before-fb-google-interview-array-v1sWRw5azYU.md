---
id: v1sWRw5azYU
title: Number 1 question to solve before FB - Google interview, Array.flat (JS Custom
  Implementation Ep-3)
date: '2022-06-09'
url: https://www.youtube.com/watch?v=v1sWRw5azYU
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nCustom implementation introduction: \nhttps://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nHow add custom methods to JavaScript Prototype:\nhttps://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\n\
  \nHow to write custom implementation for Array.concat:\nhttps://www.youtube.com/watch?v=wTQwuZuEBHU\n\
  \nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\n\
  \nMedium Blog https://mevasanth.medium.com/ \n\nMedium Blog link to flatten given\
  \ array: https://mevasanth.medium.com/flatten-array-of-array-in-javascript-microsoft-interview-question-345c71ff9ccd\n\
  \nArray Flat from developer.mozilla.org: \nhttps://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat\n\
  \nJavaScript Function: https://www.youtube.com/watch?v=VaL5lrxX-kY&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=10\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:15:06
model: saaras:v3
transcript: true
---

# Number 1 question to solve before FB - Google interview, Array.flat (JS Custom Implementation Ep-3)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself Vasanth. I hope you all doing well. As you already know there's a video series where I'm explaining about the JavaScript custom implementations where we already seen how to implement a very important interview concept called array.concat. So in this video, I'll be mainly explaining another very important custom implementation method that is array.flat, okay? With my experience of reading the interviewer feedback and me giving interviews at so many companies, this has become one of the very common

### 00:00:30 · Speaker 1

question across all the top companies. You apply for any tier one companies, what we call Manc. Netflix, I haven't read this question anywhere, except that all the other companies, Microsoft, Apple, Amazon, uh Google, uh all these companies will be I have asked this question in the past. I can't guarantee they will ask this in the future or not, but definitely knowing this custom implementation will help you to write one or the other custom implementation which they may ask you in the interview, okay? So, before I starting with this particular implementation,

### 00:01:00 · Speaker 1

In case if you have not seen my previous three videos in this series where I've explained how this series is going to be, how different JavaScript methods get access to the built-in functions. So please watch those videos and come to this video. Otherwise, it will be quite difficult for you to go along because I assume certain things are known to you whenever I'm explaining, okay? Without wasting further time now, let's get started. So there's an article that I've recently written recently where I have explained how to flatten a given array, okay, in JavaScript. And this is

### 00:01:30 · Speaker 1

that time I tagged Microsoft interview question because I had read only in the Microsoft interview feedback. But later when I read different companies feedback this has been quite common across all the top companies and many startups and other companies are also asking this. So I've clearly explained how to do how to flatten the array but I haven't written a custom implementation for this. I just wrote it like a DSL go question, okay? So please read this so to just understand the logic, okay? Now I'll go step by step explanation.

### 00:02:00 · Speaker 1

how to create array.flat, okay? So coming to here array.prototype.flat is what you will be custom implementing in this video.

### 00:02:08 · Speaker 1

So what does flat method does? The flat the flat method creates a new array with all sub array elements concatenated in into it recursively up to the specified depth, okay? So coming to this example you can notice, so we have zero one two, it's an array and inside an array we have another array. So it's kind of a nested array we can tell, correct? So in the nested array what we are doing, we are trying to array dot flat and to this function no parameter is passed, okay? It has been empty. So whenever you run, you have already run this as

### 00:02:38 · Speaker 1

you can see here zero one two three four was an array now it became without an array so it became one array zero one two three four in the second example they are passing one one here refers to the depth like let's say as you see here it is a three level depth here correct three arrays and inside that we have a three comma four one of the depth will be removed so this depth will be removed okay so you have array inside an array and three comma four okay so what if you have to eliminate all the arrays

### 00:03:08 · Speaker 1

So no matter how many levels are there inside, you have to eliminate everything. So in the best way is passing infinity. Okay? Infinity is a keyword in JavaScript for those of you who don't know, which specifies for the maximum number that particular compiler can contribute or can hold. Okay? So if I run, you see, zero one two three four, zero one two three four. No matter how depth the array is, it will be able to uh flatten it, that particular array. So basically, I'll be writing an implementation for this infinity. I expect you to write an

### 00:03:38 · Speaker 1

implementation for flat with a specific depth like you let's say you pass two depth three two level depth three level depth in case many of you are not able to write that specific level uh flattening please do mention that in comment section I will definitely try to make a video or write an article and link that in the description okay now uh nothing more here flat and the depth depth they have explained by default the depth points to one okay then return value what are the alternatives to the array dot flat method they have explained

### 00:04:08 · Speaker 1

here. Okay? Now, you know what array.flat method does. So you know the syntax and what is the property that it is taking. Now we shall first write, since it is not that easy, we have to write a recursive solution. First let us try to write a just like consider like a dsl go propon, let's try to write a function which will flatten the given array. Then let us try to embed that into a custom implementation. Okay? So, I have come prepared for this video, unlike my last video of concat where I just came like that, no, this video I have come prepared, reason being this is

### 00:04:38 · Speaker 1

recursion, there's a chance that where I may make a mistake and I don't want to misguide you guys also. So come prepared for this video, okay? And before I start coding, in case you if you are someone who is looking uh who is preparing for a JavaScript driven interviews like React, React JS, React Native or Angular, Node, etcetera, I've created a beautiful series with twenty plus videos in my another playlist where I've explained all the most common interview questions and how to solve them, okay? So please do watch that series, it will be definitely helpful for you in facing the upcoming interviews, okay? then feel free to continue with this video. Okay? Now.

### 00:05:13 · Speaker 1

array dot flat like I said first let us try to write a flat method itself which will take nested array as an input and it will make it into a straight array without any nesting okay function

### 00:05:28 · Speaker 1

flatten array okay. It takes array as an input. Okay then what we do for um for. So what we are doing here is we'll iterate till the length of the array okay. Then

### 00:05:43 · Speaker 1

just so that you can come along with me I will do this. I'm invoking the flatten array method, okay? And I'll pass the same input as that of this. Okay?

### 00:06:00 · Speaker 1

same input as that of the that particular example I'm passing here, okay? So what we'll be doing here is in the input, in the array whenever we are traversing, okay? If it is not an array, like zero is not an array, it's just a value, in that case, push it to the output value.

### 00:06:17 · Speaker 1

and one is also not an array, two is also not an array, so push it to the output. If it is an array, like three comma four is an array, correct? So, so array index is an array, like array of zero, array of one, array of two, array of three. Is array of three an array? In this case, yes. If array of an index is an array, then we cannot directly copy the values because we don't know the length of it. So in that case, what we'll do, we'll recursively invoke the same function, the flatten array with three comma four as an array.

### 00:06:47 · Speaker 1

Okay, so let's say we have three comma four, then we had another array inside this, like five comma six, which is next next nested array, correct? So right now output will look like this. So one, two, three is already, zero, one, two is already pushed into the array, correct? Don't worry if you're not getting, after I write the code also, I'll once again explain, but I'm just trying to explain my approach before I write the code. So zero, one, two, three, zero, one, two is a part of the array.

### 00:07:17 · Speaker 1

okay? Output next, uh you will see like array dot zero one two three array of third index is an array, correct? So we check that. In that case, we will pass this array to the flatten array, same method recursively. Then three comma four is not an array, so we will push three comma four.

### 00:07:37 · Speaker 0

Okay

### 00:07:38 · Speaker 1

and then we will we will get to know that five comma six is an array which is inside the array correct then we invoke the same function flatten array by passing five and six okay now array points to just five and six so it will iterate the array and it will put five comma six okay and then since it's a recursion call the stack is popped off if there are no more arrays it is popped off it will come out then it will come out of this array also so if there are any elements outside this five comma six let's say here you have seven now seven

### 00:08:08 · Speaker 1

is added into my array. Okay, this is what my approach. So now I'll tell how do I write this code. So first thing as I said, first I need to check whether the array index is an array, correct? For that we have an array prototype method that is array.isArray of

### 00:08:27 · Speaker 1

array of I. Correct? So this index is an array or not I'm checking. If it is not an array, okay? Then what I would do? I have created output, okay? const output, then I'll push the value into the output. output dot push array of I, okay? In case if it is an array, then what I'll do is I'll call the flatten array method with array of I.

### 00:08:54 · Speaker 1

same thing whatever I've explained I've tried doing here. Okay? Once this entire thing is execution is done then uh finally you can return the output or since it's a global variable the function itself can access this also. Let me try running this and I'll explain the entire block once again. Okay?

### 00:09:13 · Speaker 1

So as you can see here, we had two level nesting here and one element outside the nesting also. These elements also outside the nesting. Output is it is a unnested or in a flattened array. The nested array become a flattened way. Okay, I'll explain once again what I'm doing quickly. So I'm calling the flatten array method, passing the nested array, okay, let me do a dry run. So for I is equal to zero, I less than array.length I plus plus. So zero, array of is array of zero, no. So what I'm doing, I'm pushing zero into my output array.

### 00:09:43 · Speaker 1

same happens for zero one two. Next, I encounter this series, this index of the array, which is an array. So array dot is array true. Then what I'll do, flatten array, I'm calling this entire block, okay? Next, in this case, the array whatever we are pointing is this three four five comma six, okay? So it it started with three, three is not an array, pushed into flat output, four is not an array, pushed into output. Now, five comma six is again an array, then you're calling the flat method again by passing five comma six. So this condition becomes true.

### 00:10:17 · Speaker 1

Then you're pushing the value again five comma six, okay? Once five comma six is done, we no longer need a recursion. So we are done with all the nesting. So as you know, stack is popped out. Finally, we are back outside and now next we encounter seven that is pushed into the array. Okay? So this is about just implementing the flatten array method. So this is the crux of the logic. So adding into custom implementation definitely I think you already know, correct? So what I do is array dot prototype dot my flat, okay? function

### 00:10:47 · Speaker 1

this an anonymous function. If you're not sure what is an anonymous function, feel free to check out my video where I have explained this in very much in detail. I'll try to add that on the description, okay? So then return output, okay? So now flatten array, I'm invoking from inside, okay? So where I'll pass this as a reference, okay?

### 00:11:09 · Speaker 1

if I go here and see array dot flat correct. So same way I need to do okay. So flatten array basically I made it inner function actually you can keep this outside also on trigger. I've just made it an inner function and I'm trying to invoke this from this I'll I'll again tell what is this etcetera in case if you have not watched my previous video okay.

### 00:11:32 · Speaker 1

So what I will be doing now is uh const

### 00:11:38 · Speaker 1

input array

### 00:11:40 · Speaker 1

is equals to this, okay?

### 00:11:43 · Speaker 1

const input array. Now, log, what I'm logging is input array.

### 00:11:51 · Speaker 1

Okay

### 00:11:52 · Speaker 1

dot my flat. That's it. Okay. Now input array dot my flat we are doing. When by default as you know our logic it works for infinity. Okay. By default I'm considering infinity and trying to sort everything. Like I mentioned it is just a small homework for you. Try to write a function that takes that navigates only to a particular level and flattens it. Okay. If you if you are able to write the code I will be very happy please do mention that in the comment section. Okay. So now my flat you are triggering. Okay.

### 00:12:22 · Speaker 1

So here what you are doing is here this points to the array with which you triggered this my flat. So in this case the array will be this. Okay? I've also explained this in my previous video. Whenever you are invoking a prototype method always this refers to the array or the programming constraint with which you triggered the prototype method. Okay? So what I'm doing is I'm passing this array into this the flatten array. Okay?

### 00:12:47 · Speaker 1

Rest the explanation remains same. Once the values calculated, okay? So what we are doing here is we are calling this and values computed, okay? This is returning the output, okay? What I can do is this output I can take inside, okay?

### 00:13:07 · Speaker 1

Then what also what I can do is flatten the array. I can do this. Return flatten array, okay? I invoke the flatten array by passing this as the array, okay? Then this will compute, it will flatten the array, correct? And it will return the output, whatever the above one, okay? Then I am also returning that whatever the output was returned. I can break it into two level if you want, like const

### 00:13:36 · Speaker 1

return value. Okay, is equals to flatten array. Then I can return the return value. Okay.

### 00:13:47 · Speaker 1

return value. This also I can do two step process. So inside the my flat method, I actually have a function which is responsible for flattening the array with a recursive approach, correct? And then what I'm doing, I'm trying to calculate that value by invoking that function inside my prototype function, then finally I'm returning the value, okay? So I think this should work, if not let us try to debug and fix it quickly. It worked.

### 00:14:14 · Speaker 1

Okay? So this is my solution about how to flatten the array. uh I think you enjoyed the video. If you liked my video, please do like it on my YouTube channel and share the videos with your friends as it is very important. Like I said, this has been asked in multiple companies like Apple, uh Google, Amazon, um I don't know Netflix, but all the other top companies it has been asked. So this is very important and very simple actually. If you try to get a gauge of this, you'll be able to write lot of recursive programs on your own. Okay? In fact, this was asked in my current company also in the interview and

### 00:14:44 · Speaker 1

and I had solved the problem. So due to which I I got a high chance of clearing my first round. um So please do subscribe to my YouTube channel Uncommon Geeks. And as I said my medium blogs I've written lot of beautiful articles about this programming things. Please do follow me on LinkedIn, follow me on medium and share those articles also with your friends. Thank you so much for watching. Catch you in next video.
