---
id: R5vbUc0uB7E
title: Learn how to add custom methods to JavaScript Prototype (Custom implementation
  Ep-1)
date: '2022-06-08'
url: https://www.youtube.com/watch?v=R5vbUc0uB7E
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. JavaScript \n\nInterview Preparation series :\
  \ https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\n\
  \nMedium Blog https://mevasanth.medium.com/ \nGithub Repository that contains examples:\
  \ https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:08:11
model: saaras:v3
transcript: true
---

# Learn how to add custom methods to JavaScript Prototype (Custom implementation Ep-1)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself Vasanth. I hope you all doing well. So today's topic as you already know, we are discussing a custom implementation. And then in this video, I will not be writing custom implementation for any built-in method, rather, I would say how a programming constraint like array, string, function, class, they get access to JavaScript's built-in methods, okay? And how to add any custom method into this existing list so that you get a fair understanding about how to start with a custom

### 00:00:30 · Speaker 1

custom implementation. This video is very very important unless you know these concepts you will not be able to write a custom implementation of your own. Okay? So do not skip this. Watch this video till the end. Okay? As you already know I'm making lot of videos on the front end developer interviews. I've made one detailed playlist with twenty one videos or twenty plus videos on the most common interview questions on JavaScript and I'm making this another series where I'm explaining you

### 00:00:55 · Speaker 1

the concepts of custom implementation. If you like whatever the work that I'm doing, please do like this video, share the content with your friends. Do not forget to subscribe to Uncommon Geeks, okay? Now, let's get started with the most basic concept, how a particular programming constraint is getting access to the built-in methods, okay? So this is my medium URL, miwasanth.medium.com, okay? So where I've explained you lot of various articles I've written on different topics, okay? My purpose of coming taking this

### 00:01:25 · Speaker 1

opening medium blog is because you need to know two very important topics that is how everything is object in JavaScript and prototype and prototypal inheritance in JavaScript. These two are the very fundamental topics for you to understand how built-in functions are accessible for a particular programming constraint. For example,

### 00:01:43 · Speaker 1

Let me zoom in a bit. Okay?

### 00:01:46 · Speaker 1

and okay I I zoomed in too much.

### 00:01:50 · Speaker 1

Let's say I create a variable called array and I am initializing it with one two three four. Okay? And I'm hitting enter and whenever I do array dot I start seeing lot of methods. concat, find last, for each, has own property, sum, sorts, splice, etcetera. So you created just a variable called array with one two three four. How come all these methods and the properties are accessible to this variable? Okay? So that is the first question that you need to get an answer.

### 00:02:20 · Speaker 1

Okay, before starting writing any custom implementation. So that I have explained here. How everything is object in JavaScript. Please read these two articles very much in detail. I'll link that in somewhere in the description, okay? I cannot go through each and everything of every bit of it due to time constraint, okay? Now, same example I have given here. So the answer to my question, how these programming constraints are getting access to the different method is, all JavaScript programming constraints inherit properties and methods from a prototype, okay? So in our example

### 00:02:52 · Speaker 1

See, whenever you do array dot and whenever you do array dot, you are seeing different methods of array, correct? So if I say let S equals to uncommon geeks, okay? And if I do S dot, you start seeing different methods of a string and not of an array, okay? This is happening because there are different prototypes that exist in JavaScript that contains different methods associated with a particular programming constraint like array, there are different

### 00:03:22 · Speaker 1

that string there are different methods and different uh constraints have different methods. Those are part of that prototype. For example, if I now type array dot prototype, okay? So you would see lot of methods. Whatever you saw for this array, okay? Whenever you do array dot, whatever the method suggested here and whatever this prototype contains, both are same. Putting other way, JavaScript when it understand this variable is of array type,

### 00:03:52 · Speaker 1

it will get all the methods from array prototype and attaches it to this variable with a property called array dot underscore underscore proto. okay? so this proto is responsible for attaching all the array methods into the variable called array.

### 00:04:12 · Speaker 1

Okay? So why dot underscore underscore proto dot proto underscore underscore only very few people will get this question. Most will not get. So whatever Basant is explaining that is right. Yes, what I am explaining is right. But you should keep asking question why only underscore underscore proto and not anything else. I have read about it, there is nothing significant reason. The reason why it is underscore underscore proto is because

### 00:04:37 · Speaker 1

This cannot be generally used for any other purpose. I mean this is not a typical programming convention in JavaScript. So kind of a this they are using as a reserved keyword underscore underscore proto underscore I mean you can use it for any other purpose also but usually any nobody will be using this that is the reason they are using this this way of using it. Okay. So hope now you understood how array is getting ARR variable I have created here is getting access to the array methods. Okay. Because JavaScript is identifying this ARR variable of array type.

### 00:05:07 · Speaker 1

then it is going to array.prototype, getting all the methods of array.prototype and attaching that into this array variable with a keyword called underscore underscore underscore underscore proto. Okay? Now you got how methods are already existing. If you have to attach a new method into this prototype, it's very straightforward. So let us consider the same example, array.prototype. Okay? I'm writing a method called test method. Okay? test method in JavaScript as you

### 00:05:37 · Speaker 1

of first character is small. So what I'm doing here is I'm writing a function that does nothing other than just logging something. console.log

### 00:05:48 · Speaker 1

console.log

### 00:05:51 · Speaker 1

I think my syntax is right. C O sorry console

### 00:05:58 · Speaker 1

dot long, sorry,

### 00:06:03 · Speaker 1

console.log

### 00:06:06 · Speaker 1

welcome to uncommon gigs. Okay? So what I'm doing is array.prototype as you know contains all the methods. Dot I'm adding a new method and that method definition I'm writing here which is a function which does nothing other than just printing a statement. Okay? welcome to uncommon gig that is my channel please do subscribe. Okay? And if I hit enter so it went successful. Okay? Now if I go to elements and console and here if I

### 00:06:36 · Speaker 1

start seeing this again array dot okay prototype and if I hit enter see along with all the built in methods now I also have access to a new method that I created which is test method now from array one array a variable that I created above one two three four I am I can access this variable that is test method okay if I hit enter I see welcome to uncommon geeks okay so this is undefined because

### 00:07:06 · Speaker 1

because there are two things here. One, this test method function doesn't return anything. So, return value is undefined. Whenever you invoke it, it is printing something, so that is also been printed here. Okay? So now you got to know how to add a custom method into existing list of prototype methods.

### 00:07:27 · Speaker 1

This is a very key aspect of custom implementation. If you master this, now on all you have to do is, let's say you have to write a custom implementation for concat. So now you can write a method called my concat and you know how to invoke that from an existing array. Correct? Now all you have to know is how to get a reference or how to perform that concat operation inside this function. So fifty percent of your implementation is done. Next fifty percent is logical part. Okay? That I'll be explaining for different methods in a different way. Okay? So thank you so much for watching this video.

### 00:07:57 · Speaker 1

If you like this video, please do like it on my YouTube channel. Do not forget to subscribe to Uncommon Geeks and please read my medium blogs and follow me on Medium also. I'll be writing interesting articles on a weekly basis, okay? Thank you again for watching this video. Catch you in my next video.
