---
id: r41zkTenKTc
title: Number 1 question to solve before Apple's interview - Array.reduce (JS Custom
  Implementation Ep-5)
date: '2022-06-11'
url: https://www.youtube.com/watch?v=r41zkTenKTc
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. \n\n Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \n\nMedium Blog link to flatten\
  \ given array: https://mevasanth.medium.com/flatten-array-of-array-in-javascript-microsoft-interview-question-345c71ff9ccd\
  \ \n\nArray Reduce from developer.mozilla.org: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce\n\
  \nJavaScript Function: https://www.youtube.com/watch?v=VaL5lrxX-kY&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=10\
  \ \n\nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:14:27
model: saaras:v3
transcript: true
---

# Number 1 question to solve before Apple's interview - Array.reduce (JS Custom Implementation Ep-5)

## Transcript

### 00:00:00 · Speaker 1

हेलो ऑल, वेलकम बैक टू अनकॉमन गिग्स, मैसेल्फ वसंत। आई होप यू ऑल डूइंग वेल।

### 00:00:04 · Speaker 1

So as you know there's a video series where I'm explaining about the common custom implementation related question that are asked in the interview. So if you have not watched my previous videos on custom implementation at least one two and three please go ahead and watch that that will be helpful for you understand what we are doing in the series and to understand basics about the array prototypes or different prototypes how to use the prototypes etcetera. Then probably if you come back it will be very easy for you if not it may be become slightly difficult if you don't have the basics. Okay. Now the today's topic is

### 00:00:34 · Speaker 1

array.prototype.reduce very very common question. No matter all the top companies you see everywhere they have asked custom implementation of reduce. I mean next when you go they may not ask but whatever with the interview experience wherever they have asked the custom implementation reduce has been very very common question. Okay. Why reduce has been asked so many times. uh with what I know actually I have come prepared for this video I mean I wrote already custom implementation reduce practiced it and I have come unlike other videos where I come and just do like that.

### 00:01:04 · Speaker 1

just to show how possible errors we can make in the interview. This I've come prepared. I did not feel it is very difficult if you know custom implementation of few basic methods already. This is quite straightforward, okay? I think it the interviewers are obsessed with array dot reduce because the reduce method itself is very less used in the during day to day activities. Many don't use because they don't know how it works, okay? Many don't use because they don't know when to use it properly, okay? Because of this reduce method itself

### 00:01:34 · Speaker 1

itself is not used much but it is very effective method which is which can combine uh map and filter kind of an operations two operations doing rather doing separately it can do it one step okay but you should know when to use and when not to use it okay since many doesn't know what deduce does itself so maybe interviewer think it will be difficult for them to write the implementation so they generally ask this in the interview okay but don't worry I'll explain the thing step by step but I'm not going to touch base on when to use deduce when not to use that you can always

### 00:02:04 · Speaker 1

see it from the documentation. I just touch base on what is reduce method. Gives with a simple example, explain with a simple example, then start writing the custom implementation. Okay? So, let's just get started with array.prototype.reduce, okay? uh As usual this this explanation is quite complicated to understand so I will not uh explain much about this. So this is a simple example that I'll explain, okay? Then I'll go with the syntax, then let's go back and start writing the custom implementation.

### 00:02:34 · Speaker 1

So here we have one array, okay? And this is some block. Finally, we are printing the sum with an initial overall sum. In very simple words, reduce word, whatever it indicates, array reduce does the same. That means given an array, reduce it into something. For in this case, we are adding all the values and printing the sum, correct? It could be any other operation like concatenating, anything. Basically, you are reducing an array into one chunk, no matter what operation. That is when reduce has to be used.

### 00:03:04 · Speaker 1

You can use reduce for any other methods also, any other actions also, but it's kind of slightly not been regularly done, okay? So this is the right way of using reduce whenever you have to reduce array into one value, okay? Now, I'll copy this example, okay? Let me head back to

### 00:03:22 · Speaker 1

this one. My Visual Studio Code and then let's start the explanation, okay? So here we have an array, then we have an initial value, rather having sum with initial and all, very simple words, I'll name it output, okay? Now, we have a previous value and a current value. Previous value, what I would name, just for my accumulator, okay? Just for an easy understanding, I'm naming it accumulator, okay? See, I use a spelling checker, I think.

### 00:03:52 · Speaker 1

give you some spell checker some package that is available in Visual Studio you also use it so that you can avoid making spelling mistakes like this. This I did intentionally just to show you because whenever you are doing a code review somebody points out your code spelling mistake is there it will be very awkward to face. So use this library and make sure you don't make any spelling mistakes. Okay. Accumulator and current value. Okay. Now array one dot reduce accumulator and current value so I'll explain you step by step what is happening. Okay. As I mentioned

### 00:04:20 · Speaker 1

array not reduce is basically used to reduce array into one chunk, correct? So here you see two variables it takes, okay? Accumulator and the current value. Then it also takes another value that is index. It also takes another value the array itself, four arguments. Most of the time we will not use the third and the fourth, we just use the second and third argument. Now here accumulator is nothing but it holds the value what is returned from the previous calculation, okay? So very first there will not be any value that is returned from the previous calculation.

### 00:04:50 · Speaker 1

calculation as in it could be any any operation that you are doing okay so very first accumulator needs a value that you can initialize by initial value if you are not passing an initial value the initial value is arrays first index okay that is the first part so in our example as you passing an initial value so accumulator first points to zero

### 00:05:10 · Speaker 1

Next, current value will always point to what is the current value in the array. So in this case it is one. Correct? Then it goes on to three four. Now, what happens is we are adding both the values. So zero plus one

### 00:05:25 · Speaker 1

it which is one. In next step, accumulator's value is what was the result of the previous calculation, so which is one. What is the current value? That is two. So two plus one, which is three.

### 00:05:39 · Speaker 1

Next. Now accumulator value changes to three. Accumulation of so far whatever calculated. Current value is three. So three plus three, six. Correct?

### 00:05:50 · Speaker 1

last step. Now the most recent accumulator value is six. Correct? So we have six here. Last value of last current value is four. Six plus four is ten. Correct? Six plus four is ten. We are done. Okay? So this is what array.reduce does. I've explained in a very step by step format. Okay? Vasanth, what is been written? I don't see written statement anywhere. Many might ask you this. So this is an array, this is an arrow function.

### 00:06:20 · Speaker 1

If you don't use a flower bracket, if anything that you write in one line, nothing but that itself you are returning, okay? I I have made one video on about arrow function, I'll try to link that somewhere on the screen or description, that also you can watch to understand more, okay? So if you want it very clearly, you can put a flower bracket, remove the put this comma, okay? Then

### 00:06:42 · Speaker 1

do a manual return

### 00:06:45 · Speaker 1

This is only happening even if you don't write return in the arrow functions. Okay? Now whatever I I have written here, is it right or not, correct? You shouldn't believe anyone, me also. So let me put a log and show you this, show this to you. Okay? So accumulator is accumulator, okay?

### 00:07:03 · Speaker 1

Then, current value

### 00:07:07 · Speaker 1

current value is current value. Okay? Let me run this now.

### 00:07:12 · Speaker 1

So zero one three six, overall it is ten. One two three four. So last step it is skipped. So which will be the sum of the final sum. Okay? Same whatever I explained here, same is been shown here as well. Okay? So now I believe most of you understood what array dot reduce does. Okay? Now is the second part. Okay, I'll also show you one more thing. Let's say I don't pass the initial value. Okay? If I don't pass the initial value, what will happen?

### 00:07:39 · Speaker 1

So you will get this. Ten only. In this case, add works as it is, but there are some operations where it doesn't work if you don't, I mean, as it is. I mean, in this case, if you pass an initial value of zero or if it uses the arrays first index, the add works the same way. The output is ten, but there are some operations where it doesn't work the same way. If you know such operations, please do mention that in comment section. Okay? Now.

### 00:08:04 · Speaker 1

So we need to handle both the scenarios when you write our custom implementation. We should be able to see, we should be able to check if there is an initial value, use the initial value. If there is no initial value, then use the array of zero as the initial value, okay? Now, so I'm removing this as you already understood. uh yeah.

### 00:08:22 · Speaker 1

I'll start reading the custom implementation array or prototype. So now, if you are someone who is preparing for uh JavaScript driven any interviews with a different text tags, React, Angular, Vue, Node, etcetera. As you know, there will always one round that is dedicated for JavaScript. I have made a beautiful series to explain most common interview questions and how to tackle them in the interview with respect to JavaScript. I'll try to add somewhere a link on the screen also in the description section. Please do watch it, okay? Definitely it'll be helpful for you. I don't revolve around, I'll count exactly the question that is asked in the interview and how to tackle it.

### 00:08:52 · Speaker 1

And if you're someone who's brushing up, I'll also explain the basics and then I'll straight away get into the questions, okay? Please do watch that series, that will definitely helpful for you. Now, let's start with the implementation. array dot, I assume you have already watched my videos, you know what is prototype and how to add your method into prototype, okay? So my reduce

### 00:09:13 · Speaker 1

So again anonymous function. There's an anonymous function if you don't know what anonymous function what it does. Again I've made one video I'll try to add that somewhere on the screen please do watch that. Okay. Now inside my reduce what you need first is the input array whatever we are passing correct. So const input array is points to this. I've explained this multiple times basically this points to the array with which you are trying to trigger this method. In this case the array one. Okay. So I'll replace that with reduce with my reduce. Now, we have input array. Next what we need is initial value, correct? So, before that.

### 00:09:52 · Speaker 1

reduce basically takes if you observe two arguments, correct? So one is a callback or a method, second one is the initial value, correct? So we'll mention the same here, callback initial value, okay? Now, const accumulator, basically the initial value very first points to the accumulator, correct? So const initial value, okay?

### 00:10:18 · Speaker 1

not null

### 00:10:21 · Speaker 1

not null, then use initial value itself. If it is a null, then use the input array of zero. Hope you got what I have done. Very simple words. There are many ways to do this. Some use the ORC and all. I kind of prefer this approach. It is very neat. So if initial value is not null, then use the initial value itself. If initial value is null, then use the input array of zero. The first argument in the first element in the array. Okay? Now we have the accumulator.

### 00:10:51 · Speaker 1

which basically holds the result, okay? Next we have the input array. Now I am writing a for loop, okay? which will run till the length of the array, okay? What we do inside that is

### 00:11:04 · Speaker 1

we will be triggering this callback. Callback as in this method itself, whatever you have written here, right? This callback itself will trigger for each method. For each method, the accumulator and the current value will change, correct? So accumulator is this accumulator. Current value will be input array of I, then very important point is accumulator should be keep updating, correct? So you're returning the sum of accumulator and current value, so that I'm assigning it to the accumulator. better. I'll explain once again if you are getting confused, okay? Now

### 00:11:39 · Speaker 1

Finally, I will return the accumulated cell. Let me run this. I'll reiterate everything that I've written once again, okay?

### 00:11:48 · Speaker 1

accumulator is equals to call back

### 00:11:54 · Speaker 1

assignment okay see problem came. What problem is I'm trying to update the constants value correct so you should be using let here. Actually I realized I wanted to show this error not by running before running only I wanted to show don't do this but I forgot and I ran it okay. So I got ten here. So I'll do the same I'll pass

### 00:12:16 · Speaker 1

this to the reduce you have already seen but just to double sure we're getting ten with a that reduce also okay and same with my reduce also correct now we'll go here and I'll again reiterate and then we'll wind this video so here what we are doing is we are doing a callback and initial value so input array basically points to this as I mentioned multiple times so if you are someone who already got a good good hold of this don't use again another variable to initialize this use this as it is in your execution like here you can

### 00:12:46 · Speaker 1

is this dot length and this dot I, okay? uh if you are just novice, please feel free to use. This doesn't uh I mean this doesn't show like you are not you are not expert. Feel free to use this also. So input array, then we have an accumulator, okay? So accumulator is nothing but as I already explained, a variable that holds the

### 00:13:04 · Speaker 1

sum of the previous calculation or whatever the calculation happened that's value is hold in the accumulator. Very first it should either hold the initial value that you pass or input array of zero. Okay? So I've written this condition. Next, we will run the loop till the length of the array and inside which every time you trigger this callback. The same callback whatever was triggered here is triggered here also. So callback requires two argument accumulator and current value. Accumulator you already know it is here.

### 00:13:34 · Speaker 1

current value you already know from the array. Accumulator needs to be keep updating for each iteration so you're initializing accumulator to whatever the value that is returned from here. Okay? So that's all you have to do about the writing the custom implementation for the reduce. Very simple question I think if you would have watched this videos before you attending the interview probably you would have cleared the interviews and already got a very high package. Okay? Thank you so much for watching this video. If you have any doubts about this video feel free to add that in comment section I'll try to answer. Okay? If you like this video please

### 00:14:04 · Speaker 1

like it on my YouTube channel. Do not forget to share this video with your friends and please subscribe to my channel Uncommon Geeks, okay? So that will definitely motivate me to make more such videos. I'll link my medium blogs, link somewhere on the description or also on the screen, okay? Where I've written beautiful article about lot of JavaScript concept, please go and read them. Follow me on medium also. Thank you again, catch you in next video.
