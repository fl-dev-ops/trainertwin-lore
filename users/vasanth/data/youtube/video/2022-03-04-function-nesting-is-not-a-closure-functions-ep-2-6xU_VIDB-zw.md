---
id: 6xU_VIDB-zw
title: Function nesting is not a closure (Functions Ep - 2)
date: '2022-03-04'
url: https://www.youtube.com/watch?v=6xU_VIDB-zw
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ If you know how to call functions and what it returns, you can clear half of JavaScript\
  \ interviews. \n\nJavaScript functions could be the topic, on which most interview\
  \ questions can be formed. Because it contains other subtopics like closure, currying,\
  \ nesting of functions etc. Most tricky questions can be easily formed in this topic.\
  \ I will cover each and every topic of functions in this series, watch it carefully\
  \ and practice well, you will definitely answer all questions on this topic in upcoming\
  \ interviews\n\n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which\
  \ contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nNormal\
  \ Functions part 1-  https://www.youtube.com/watch?v=VaL5lrxX-kY&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=11"
author: careerwithvasanth
duration: 00:06:32
model: saaras:v3
transcript: true
---

# Function nesting is not a closure (Functions Ep - 2)

## Transcript

### 00:00:00 · Speaker 0

हेलो ऑल, वेलकम टू अनकॉमन गीक्स, मैसेल्फ वसंत। आई होप

### 00:00:03 · Speaker 1

you all doing well. So it's a continuation of my previous video where I had explained basics of function. In this video, uh as you know most of my series I have only one video where I explain the concept and the second video I generally start off with a quick Q and A that I generalize in the interview. But functions is something that is very important topic so I'm extending another video uh in this topic where I'll be explaining two things. So one is closure. Another one is function nesting. So these two topics I'll cover this is going to be quite short video. After this definitely let us start with the question and answer on the functions. Okay? without wasting further time let's get started

### 00:00:37 · Speaker 1

So, uh in JavaScript there's a concept of function nesting as the very word indicates you can have one function inside another. Okay, let me first show you how to do that. Okay? So you have a function called one that takes some parameter, okay? And you can have a function called function two which is inside function one, okay? And you can keep on adding any number of functions one inside another, okay? So for example if I do it here, function three, okay? So keep on doing,

### 00:01:07 · Speaker 1

can do it to any level but with my experience of building beautiful web application and mobile application I have never gone in the function hitting for the third level. I've always stick to the first and the second level. You may encounter some scenario where third level is also required. Okay so please learn that. But application wise I haven't seen anywhere. Okay. So two functions are there. Now Vasanth it is I know how to invoke num function one. I'll invoke like this. Correct? And let's say I put a log statement.

### 00:01:34 · Speaker 1

welcome to Uncommon Geeks. Okay? I always do some amount of marketing by just putting my channel name. Okay? So if I execute it, welcome to Uncommon Geeks you are getting, so which is right. uh thing is, uh you one you are able to invoke because one is in a global scope. So you have access to that even outside, so you are able to invoke it. Two is something that is intrinsic to one, correct? So which is inside this block. You cannot invoke two just by itself. uh So the way how you can invoke two is, Whenever you invoke one, you return two.

### 00:02:08 · Speaker 1

you return two. Okay? Then what you do is basically you return two means you are returning the reference to that function, correct? Then use that reference, that second function's reference, okay? And call that function. So to show you const output is equals to one, okay? You have invoked it. Now this statement actually returns two, so now output is basically pointing to statement two, correct? So output if you do this, then if you do console.log और वेलकम टू

### 00:02:41 · Speaker 1

Outer function

### 00:02:44 · Speaker 1

Okay

### 00:02:47 · Speaker 1

inner function. Got it? So let me run this and see what is the output we are getting. So welcome to uncommon gifts outer function and welcome to uncommon gifts in the inner function. Okay? So what has happened is whenever you are invoking this uh the one, okay? When you invoke the function one, first the line number two is executed, okay? Then like this is this does not execute because someone should invoke a function to execute, right? Just by itself it doesn't invoke. At least the all the named and the anonymous function, okay?

### 00:03:17 · Speaker 1

function as you know definitely it get executed without anyone invoking. So but two cannot invoke by itself. So we are returning two here and the output has a reference to two from here I'm invoking it so it is getting executed. Okay. This is about the function nesting. You already got the as a very word says function one function inside another this is the function nesting. Okay. Then I let's now let's go to the concept of closures. Okay. What I'll do is I'll create a variable here.

### 00:03:44 · Speaker 1

const count is equals to ten okay? then what I'll do is I'll try to print value of count here okay?

### 00:03:55 · Speaker 1

value of count is value of count is count. Okay? First let me execute it, then let's see what is happening. So value of count is ten, correct?

### 00:04:07 · Speaker 1

So, why value of count is ten let us see. Obviously whenever you invoke the function number one, so you function number one has access to value of count in line number ten. So if you print anywhere in the in the function one scope, the value of count becomes ten which is obvious, right? But function two which is inside it, so this itself is a block, correct? So if you know lexical scoping, global scope, this itself is a different scope. So, but still it is able to access the value which is declared outside it, correct? So that is due to the proper

### 00:04:37 · Speaker 1

of closure. For those of you who don't know the standard definition I'm showing that here. It also forms a closure maybe wait let me remove this.

### 00:04:45 · Speaker 1

A closure is an expression, most commonly a function, that can have a free variable together with an environment that binds those variables, that closes the expression. I know this is heavy. Let's go to the second statement. Since a nested function is a closure, this means that a nested function can inherit the argument and variables of its containing function. In other words, the inner function contains the scope of the outer function. So if you are someone from the engineering background or someone BCIMC or any other bachelor degree in the computer science, if you are appearing for exam, this is your definition.

### 00:05:15 · Speaker 1

So if you are someone who is looking for an interview then this is your definition. Okay? The inner function contains a scope of the global scope, global scope that itself is a closure. Okay?

### 00:05:26 · Speaker 1

So now you know what is inner function and in my previous videos you already know what are named function, anonymous function, parameterized function, self invoking function, non parameterized functions, correct? So and now you also know what is closure. So now since you already have a good gist of the entire function, at least the all the named function or the normal function what we call except the arrow function, whatever the other functions are there. Now you know all the concepts in those functions. So now in my next videos I'm good to start with the question and answer. So thank you so much for watching this video.

### 00:05:56 · Speaker 1

If you like my video, please do like it on my YouTube channel. If you want your friends also to get benefited from this, please do share the video with them. Do not forget to subscribe to Uncommon Geeks. And if you want me to make a video on any particular topic, please do let me know. I'll make a video on that particular topic. And my medium blogs are linked in the description. Please go ahead and read. They have written a lot of articles on React, Angular, and Ionic, JavaScript, etcetera. And I also link my GitHub URL where I've added all these projects and there is a lot of questions to practice also. Follow me on

### 00:06:26 · Speaker 1

and download those projects and practice on your own. Again, thank you so much for watching. Catch you in next video.
