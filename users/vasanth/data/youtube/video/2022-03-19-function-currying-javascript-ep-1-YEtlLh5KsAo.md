---
id: YEtlLh5KsAo
title: Function currying JavaScript Ep - 1
date: '2022-03-19'
url: https://www.youtube.com/watch?v=YEtlLh5KsAo
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Function currying is a sub-topic of function, to be specific extension of function\
  \ nesting. Currying as a topic has good weightage  when it comes to interview. Calling\
  \ a function infinite times and using same function to implement both currying and\
  \ normal implementations are common questions asked in the interview. \n\nCounter\
  \ Dilemma Closure: https://www.youtube.com/watch?v=nJhQRotbIis\nQuestions on closures\
  \ Part 1: https://youtu.be/pycV_CSoj1g\nQuestions on closures Part 2: https://youtu.be/j4KRg0RBY5Q\n\
  My Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:06:35
model: saaras:v3
transcript: true
---

# Function currying JavaScript Ep - 1

## Transcript

### 00:00:00 · Speaker 1

all, welcome to Uncommon Geeks. Myself, Vasanth. I hope you all doing well. So today's topic is function currying. We have already seen different aspects of function already, the functions, the closure, the inner functions, okay? There's another beautiful property of function which are generally asked in the interviews, function currying. In fact, it has become very so common that almost every frontend developer in the JavaScript, they ask you one question of the property of function currying. They just straight away don't tell it's a currying, but they give you some weird

### 00:00:30 · Speaker 1

expression of I mean weird question which you if you're looking at for the first time you'll not be able to identify how to do this. But it is actually very simple if you know the concept of closure, currying is very straightforward. Okay? So let us start with the definition first which is generally the difficult part to understand. So currying is a process in function programming in which we can transform a function with a multiple arguments into a sequence of nesting functions. It returns a new function that expects a next argument in line. Okay? I know this is

### 00:01:00 · Speaker 1

too much too much to understand but I'll explain that in depth. So the reason why I show the definition for most of the things is so that you read it and if some interviewers expect an actual definition and you can mug it and answer in those questions, answer in those interviews, okay? I'll explain in in simple words what is function carrying.

### 00:01:20 · Speaker 1

Let us create a function called add which takes one argument and it has another inner function which is anonymous which takes another argument called y and basically it returns a sum of x plus y okay so with a property of closure as you know the value of x which is which is actually passed to the outer function can be accessed in inner function also okay so the traditional way of doing getting adding the two numbers with this is so we'll do ten then what you do is output of twenty

### 00:01:53 · Speaker 1

log

### 00:01:56 · Speaker 1

Okay. So most of you would know what is the output for this. This is thirty. Okay. So where you passed add and x became ten here. Okay. And this entire block was returned and you are invoking output of twenty. So twenty is here it is twenty now. So twenty plus ten which is thirty. So quite obvious. So this is how the function closure works. Where the the value declared outside the function can be accessed inside the function due to property of closure. So now the variation of this is rather making it a two

### 00:02:26 · Speaker 1

step process. So you are making it a two step process, correct? To invoke the function in a function or basically to add two values, you are calling it twice, calling add ten here, then output of twenty here. Can we make it at one step? Okay, it is possible with the property of closure. So what I'll do is rather doing this way, I'll just put output here and here I'll pass twenty.

### 00:02:51 · Speaker 1

observe this expression carefully. So where first bracket I'm having I'm sending ten and inside the second bracket I'm passing twenty. So what is happening here is so the same expression you can tell also like a shorthand notation of what happened previously. So add ten is getting triggered and this function is returned to that function you're passing twenty and you're getting the output. Let me execute it. So you're getting the same output that is thirty. So interviewer will not ask you what is function carrying etcetera generally because it is not

### 00:03:21 · Speaker 1

officially documented in the developer.mozilla.com, mozilla.org. It's kind of an evolved topic. So just like a shorthand notation over the closure and function, they will, what they will do is they'll give you just this.

### 00:03:33 · Speaker 1

add ten comma twenty and they'll ask you to write a function that gives a sum of both the numbers. Okay? So only if you know the closure property and how it works you'll be able to answer this. Okay? Now we'll go to another explanation of currying which most commonly used. So it actually to solve mathematical equations the function currying is very handy. So for example const f is equals to x

### 00:04:00 · Speaker 1

x plus x, okay? And const g is equals to

### 00:04:08 · Speaker 1

Why

### 00:04:10 · Speaker 1

y star y, okay? What we'll do now is f of g of ten and we'll log it, okay?

### 00:04:22 · Speaker 1

one of the main purpose of using the closure is due to this where we will be using the

### 00:04:29 · Speaker 1

using it for the mathematical expression of this kind f of g of x, g of f of x. You can hierarchy it to any level. So what will happen in this case, okay? is we are calling g of 10. So y becomes 10. So 10 star 10 is 100. And then so this expression become 100. f of 100, 100 plus 100 becomes 200, okay? So if you have to do achieve this with the help of a normal closure or a function, this is again tedious job where you create a function, call that function, get the output, then pass it out.

### 00:04:59 · Speaker 1

put the second function that can be easily solved with the help of this property of function carrying. Okay? Let me execute and hit it and show the output for you which is two hundred. You know why it is two hundred. Ten star ten is hundred, hundred plus hundred is two hundred.

### 00:05:13 · Speaker 1

For those of you who are very new to the arrow function, I have a separate section that I'll be preparing in future. For just for the quick explanation, what is happening is X and this is a function. Since we have only one expression and we don't have multi-line expression, so we are adding it and returning at the same time. Okay? So there is no return statement required. So whenever you call F and pass one argument, what will be returned is the sum of that, I mean, the what will be returned is that argument plus that argument again. So X plus

### 00:05:43 · Speaker 1

in this case y star y, okay? So basically we are getting the value of 200 here. So such mathematical equations and the closures whenever there's a two to three function nested one inside another, so rather calling it in a multiple steps will be with the help of a currying property you'll be able to invoke it at once. So that's all about the function currying, quite straightforward topic but there are very interesting questions which are generally asked in the interview, which I'll ask in my next videos. Thank you so much for watching this video. If you would have liked my video please do like it on my YouTube channel. Please share it with your friends.

### 00:06:13 · Speaker 1

want them also to get benefited from these videos. Do not forget to subscribe to Uncommon Geeks. Please, please subscribe to my channel. And my medium blogs about function carrying is linked in the description. Please go ahead and read it. I have written lot of questions which are generally asked in the interview. They are also. My GitHub project URL is also there. Download the project, practice all these questions. Thank you so much for watching. Catch you in next video.
