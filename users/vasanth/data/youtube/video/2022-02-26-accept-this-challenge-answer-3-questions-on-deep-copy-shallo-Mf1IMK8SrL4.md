---
id: Mf1IMK8SrL4
title: Accept this challenge !! answer 3 questions on Deep copy - Shallow copy Part
  - 2 ( Ep - 3)
date: '2022-02-26'
url: https://www.youtube.com/watch?v=Mf1IMK8SrL4
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Copying a value of one variable to another is considered to be one of the most\
  \ fundamental feature of every programming language. But in JavaScript Interviews,\
  \ even today, most candidates face difficulty in answering questions of deep copy\
  \ and shallow copy. In this video series, I will explain each and every concept\
  \ of deep copy and shallow copy. So, after watching this, in all of your future\
  \ interviews, you will be able to answer all questions of deep and shallow copy.\
  \ \n\n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains\
  \ questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nDeep\
  \ copy and Shallow copy part 1 - https://youtu.be/OFJmoIRyqw4\nDeep copy and Shallow\
  \ copy part 2 - https://youtu.be/_iv8bapMLDg"
author: careerwithvasanth
duration: 00:17:00
model: saaras:v3
transcript: true
---

# Accept this challenge !! answer 3 questions on Deep copy - Shallow copy Part - 2 ( Ep - 3)

## Transcript

### 00:00:00 · Speaker 1

Welcome to Uncommon Geeks, myself Vasant. I hope you all doing well. As you know this is a continuation of my previous video where I have explained you deep copy and shallow copy. In case if you landed directly into this video, I would highly advise you to go back and watch my previous videos. I will try to add the link somewhere on the screen or also in the description.

### 00:00:18 · Speaker 1

The reason being I have explained the fundamentals of deep copy and shallow copy in my previous videos and I have also asked some common interview questions there so do not skip that video please do watch it. Without wasting further time let's get started.

### 00:00:30 · Speaker 1

So if you remember guys in the end of the last video I had shown you how to make a deep copy and shallow copy using JSON.pass and JSON.stringify. Okay? And if you remember I had also mentioned there are some scenarios where we cannot use JSON.pass and JSON.stringify.

### 00:00:43 · Speaker 1

This video revolves around those. So and how to handle such scenarios where JSON or passenger JSON or stringify cannot work. Okay? So I'll explain all of that in this video.

### 00:00:54 · Speaker 1

it may be slightly longer like my usual videos are around nine to ten minutes this may go up to thirteen to fourteen minutes is what I'm thinking. So please stay with me guys but I'll ensure by end of this video you will totally understand how JSON or passing JSON or stringify works and when to use it when not to use it.

### 00:01:11 · Speaker 1

and when you cannot use JSON.pass and JSON.stringify, which one to use? All of that I'll clearly explain in this video, okay? Without wasting further time, let's get started. This is my first example, question number one, okay? Where I'm printing the values of both the test object one and test object two. If I had to run through the example, what I'm doing is I've created one sample simple object with name test object where that has a key called sample date to which I'm assigning the value of new date. Basically, you know, new date returns the today's or

### 00:01:41 · Speaker 1

the current date, okay? And what I'm doing is here is, as you already know, if I do this test object one is equal test object two is equal test object one, this will obviously make a shallow copy and if I modify the test object two, it will modify the test object one also. I'm not going to repeat the same thing that I've done in my previous videos.

### 00:01:59 · Speaker 1

So straight away to avoid that shallow copy, we are trying to use JSON.parse and JSON.stringify, okay?

### 00:02:06 · Speaker 1

So where I'm passing test object one, I'm logging test object one and test object two. Looks very simple and straightforward. If you any of you, if you know already know the answer to this, please do mention question number one in comment section and put your answer before I run the program, okay? Now, those of you who still not sure what is the output, let me run it for you.

### 00:02:26 · Speaker 1

But I believe most of you would be thinking this straightforward and what you would get is sample date contains a date object since we are just doing JSON or parsing JSON or stringify

### 00:02:34 · Speaker 1

And after that we were not modifying test object two. So value of this and this should be same like when you log test object one and test object two you are expecting a same output. Let's see what the output actually is.

### 00:02:48 · Speaker 1

So it is actually looks like a same input if you are not a keen observer you will not be able to figure it out. So where both actually having the same value. Only difference is data type. First one is an object. Second one is a string. Okay? So in the hurry of making converting a shallow copy into deep copy.

### 00:03:06 · Speaker 1

If you use JSON.pass and JSON.stringify on those objects which contains date

### 00:03:14 · Speaker 1

then it will convert date into a string. rather keeping date object as it is after the deep copy, okay? so my first advice is whenever interviewer ask you how you convert a

### 00:03:26 · Speaker 1

how you convert a shallow copy into a deep copy in those cases when there is a date is involved.

### 00:03:33 · Speaker 1

Do not use JSON.parse and JSON.stringify. It will not work. Why it will not work and in such cases which method to use I'll explain in a while. Okay? But please keep this in mind. Interviewer will not ask you straight away in a simple example like this. What they will do there will be a very big object.

### 00:03:50 · Speaker 1

something like user details, some user location, there will be deeply nested object. Somewhere they will be inserting this date just to confuse you. So be very cautious about this. Now we'll go to the second question.

### 00:04:05 · Speaker 1

Second question also is pretty much same as the first question but it is a there are some more attributes I'm considering here. Okay? So where there is a test object one a an object which has two keys sample function and sample undefined. So first key actually points to a function.

### 00:04:20 · Speaker 1

second key actually points to an undefined. Okay, undefined in JavaScript you already know stands for nothing. If you declare a variable and haven't initialized with anything, then the value of that will be undefined. console.log, most of you know this is a function.

### 00:04:35 · Speaker 1

I have explained clearly explained this in my pure function series in case if you have not watched pure function I'll try to add the link somewhere on the screen also in the description please do watch it okay. Now we have object which two keys one points to function another points to undefined same we are trying to make a deep copy of it using JSON.pass and JSON.stringify.

### 00:04:55 · Speaker 1

Then we are logging both. If you know the answer, please do mention in comment section, mention in question two and your answer before I execute the program, okay? In case if you are not sure what is the value, I'll show it.

### 00:05:08 · Speaker 1

So this is very interesting, huh? In case if you're seeing this for the first time, you'll be astonished. What is happening whenever I log the object one, you are seeing sample function which actually has a function on the right hand side. Sample undefined, you have initialized it to undefined, same is getting print. But test object two after JSON.parse and JSON.stringify, test object two is nothing, just an empty parenthesis.

### 00:05:29 · Speaker 1

So we lost both the values. So why I specifically took this example is again in a hurry of doing a converting a shallow copy into deep copy in your very important project you may end up doing the same thing. Okay? Once you do this it will become very difficult for you to debug if you do not understand how JSON or JSON or string if I works.

### 00:05:48 · Speaker 1

Now probably you will be trying to do test object two dot sample undefined and it will it will throw a runtime exception. Because it doesn't contain uh sample undefined. Okay? So now second important takeaway from this video is if a deeply nested object or a normal object contains uh functions or normal objects keys.

### 00:06:09 · Speaker 1

point to a function

### 00:06:11 · Speaker 1

or to a variable called a value of undefined, then do not use JSON.parse and JSON.stringify to deep copy that object. Okay, this is second takeaway. First takeaway was if it wants to date, do not use JSON.parse and JSON.stringify. Now let's go to the third. Okay.

### 00:06:30 · Speaker 1

third question

### 00:06:33 · Speaker 1

So I'm invoking the function. Same here also I'm in in the first

### 00:06:38 · Speaker 1

key in the inside the object is pointing to a function same above function itself. And the second is pointing to infinity, third is pointing to N N. N N you might know already not a number. Any number anything that is not a number will get an N N. Like if you try to sometimes whenever you're trying to do string and adding it to a number.

### 00:06:58 · Speaker 1

In such cases you will get some errors like this is not a number, okay? So N N stands for that. Infinity you might know already it's something from the math class where there are scenarios where you want to compare some a number to the highest number or to the lowest number, in such cases we'll use infinity. These are all J S E S six built in

### 00:07:16 · Speaker 1

built in symbols, okay? Now test object two, same I'm doing, JSON.pass JSON.string if I have test object one, logging both, okay? By now you might have a fair understanding what will be the output.

### 00:07:30 · Speaker 1

You see sample function did not return anything in case of test object two. And infinity and not a number are pointing to null. Okay?

### 00:07:41 · Speaker 1

I believe most of you might have guessed this uh at least for function you might have guessed infinity and N I N you are seeing we are getting null. Okay? So again third takeaway from this video is whenever there is an object which is nested or deeply nested which contains infinity N I N or function or new date object okay or undefined.

### 00:08:01 · Speaker 1

then do not use JSON.parse and JSON.stringify to make a deep copy out of it. Okay? You know it's it's normal way if you do it will be a shallow copy. I you want a deep copy and do not use this. Okay? Now you know when not to use JSON.parse and JSON.stringify. Next question is, why this is happening?

### 00:08:21 · Speaker 1

Okay, I believe most of you, if not most, at least sixty to seventy percent of you are happy now when not you know now when not to use JSON.pasting JSON.stringify. But very few of you would think why we cannot use it. Okay.

### 00:08:34 · Speaker 1

Why this becomes very essential is unless you ask why, why, why in your mind, you will never find answer for all the question. And there is a limitation someone can teach you but there is no limitation on you yourself learning, correct?

### 00:08:46 · Speaker 1

So unless you ask this question you'll not be you'll not read about it and when you when you not read about it you will not know more topics which are around this. Okay? So I'll now I'll explain why this is failing or why JSON.password.json.stringify is unable to convert unable to make a deep copy of those objects.

### 00:09:04 · Speaker 1

that contain function, infinity, n i n, date, undefined etcetera. Okay, I found very interesting and wonderful article on the web.

### 00:09:12 · Speaker 1

So this is from free code camp dot org, okay? JSON object example, stringify and parse method explained. I would have explained the gist of it but I wanted to promote whoever has written it because it's wonderful article. Please do read it thoroughly, okay? So, let's see what is actually JSON stringify.

### 00:09:30 · Speaker 1

The JSON.stringify method converts a JSON safe JavaScript value to a JSON complement string. What are JSON safe values one may ask? Let's make a list of all JSON unsafe values and anything that isn't on the list can be considered as JSON safe. Okay?

### 00:09:47 · Speaker 1

very simple way I will come back here.

### 00:09:51 · Speaker 1

See you are trying to convert a function in this case into a string. With your common sense you think can you convert a function into a string if it is converted it will be of which form? Correct obviously we cannot convert a function into string. So JSON or stringify cannot convert a function into string.

### 00:10:06 · Speaker 1

same in case of undefined, same in case of infinity and n n. Basically a value which has a potential of getting converted into string, definitely we can convert. But there are some values which we cannot convert into string, okay?

### 00:10:19 · Speaker 1

When you cannot convert it into a string, how will you parse it? So this entire operation will not be able we cannot perform on certain objects like they mentioned here, undefined, function, and ES6 symbols and an object with a circular reference, like an object inside referring to object outside that is called a circular reference.

### 00:10:38 · Speaker 1

in all of these things you will not be able to use JSON.parsing JSON.stringify to make a deep copy. In fact you will not be able to use JSON.stringify itself. So there is no point of using JSON.parse. Okay? This article is very well written and they have clearly explained with the various different examples.

### 00:10:54 · Speaker 1

I can run through it and I can try explaining but my motto of this video series is not explaining the topics in depth. So I will pass on that responsibility to you. Please read it in depth, okay? Because this you you will understand lot of things about JSON.parse and JSON.shrinkify after reading this wonderful article, okay?

### 00:11:12 · Speaker 1

Now let me come back to my series. So you saw you saw all the three questions. Now you know why JSON.js parse and JSON.stringify cannot be used on certain objects. Now my last question for this video is how to make a deep copy of JSON unsafe values, okay?

### 00:11:30 · Speaker 1

Now you know some objects are JSON unsafe like undefined function and date

### 00:11:40 · Speaker 1

and infinity n n. So these are are JSON unsafe and we cannot convert it into JSON not stringify. I mean JSON not stringify cannot convert that into a string. Then JSON not parse and JSON not stringify approach will fail. To when to make it a deep copy. Now question is

### 00:11:56 · Speaker 1

how you can overcome because obviously there will be some objects which have function infinity n n inside them and we want to convert, we want to make a deep copy of it, correct? How do you convert? Interviewer will definitely ask this question. Answer to that is one, you copy all values manually one after the other.

### 00:12:13 · Speaker 1

simple example is like this where you do test object sorry test object one dot sample function is equals to test object two dot sample function something like this where you manually copy one value after another okay this will definitely work

### 00:12:33 · Speaker 1

and

### 00:12:35 · Speaker 1

This manual copying cannot be used always. It can be used in those scenarios where uh you you it can be used in those scenarios where object is static. In such cases you can use if it is a dynamic then this this may not work all the time. Second way...

### 00:12:48 · Speaker 1

is using basically doing the same rather doing it manually you will try do it via recursive approach where you can actually iterate through key and values where you create a new key in the new object and copy the key's value into that object one after the other. I'm not going to explain that in this video but that is another approach.

### 00:13:07 · Speaker 1

third is using the built-in libraries like Lodash. Not built-in libraries, they are some third-party libraries like Lodash, okay?

### 00:13:14 · Speaker 1

So I'm not going to explain that also how Lodash works. You can just search it on Google. You get lot of videos on how Lodash works and how to implement that in ReactJS, React Native, Angular, Vue, etc. In all these frameworks you'll be able to use Lodash. Basically Lodash uses a recursive approach itself.

### 00:13:30 · Speaker 1

And since it is very common library used across lot of projects, you need not worry about the implementation, you can straight away go and use it. But all these approaches, they will add some complexity into the program. I mean, they are costly.

### 00:13:42 · Speaker 1

basically whether you check the object recursively and copy one after the another or use low dash or you copy value one after the other manually all of this is gonna be some costly operation. So use it mindfully make a deep copy only whenever it necessary.

### 00:13:58 · Speaker 1

I did not have this question in my mind but I did not plan for it but I'm going to ask you. Why

### 00:14:05 · Speaker 1

arrays and objects are deep copied.

### 00:14:11 · Speaker 1

and primitive types. Okay, this is shallow.

### 00:14:17 · Speaker 1

primitive types are deep copied. So primitive type you know example is number, string, okay?

### 00:14:29 · Speaker 1

this uh arrays and objects, why they are made a deep copy and why primitive types are made shallow copy. Sorry, why primitive types made a deep copy and why array objects are are actually getting shallow copied. This is also another important question should come to your mind as soon as I start explain this topic.

### 00:14:46 · Speaker 1

whole purpose of my video series is to make you inquisitive about the topics you read so that you read a lot and you learn lot of things stuffs by yourself. Okay? The most simplest and the common sense answer to this even if you are not read you can think of it.

### 00:14:59 · Speaker 1

arrays and primitive tests like number and strings are been deep copied. So let x equal to let y, let x equal to y where x and y are numbers. After you copy y value into x, x and y are disconnected. They are altogether different memory locations is allocated for that. They are different.

### 00:15:14 · Speaker 1

But whereas arrays and objects they point to the same reference if you do is equal to like this. Correct? Without using JSON or parsing JSON or stngify. If you just have this, this is a shallow copy. Correct? Why this is made is

### 00:15:26 · Speaker 1

See JavaScript is a language which doesn't have a memory of its own. Unlike C, Java or C++ which directly interact with memory, JavaScript is something that generally runs on a browser, correct? Where compilers are written with C++, Python, etcetera which internally interact with the memory. So, kind of we can say they have some amount of memory shortage.

### 00:15:44 · Speaker 1

So where copying an object into another object, if it is, let's say it's a very big object, if you every time if you start making a deep copy of objects and arrays, you end up using lot of memory space. Correct? So to avoid that, JavaScript's default behavior towards objects and arrays when it comes to copying is shallow copy.

### 00:16:04 · Speaker 1

only when needed by you, you make it a deep copy. Okay? That's the JavaScript approach. So, it somewhat saves the memory for whenever the application is running. Okay?

### 00:16:14 · Speaker 1

So five questions we have learnt in this video series, they are very very important questions. Please do practice them. I'll try to add all of this to my Git repository so that you can copy the question directly and execute it on your machine. Okay? Thank you so much for watching my video. I know it extended close to fifteen to sixteen minutes, but I had no go other than explaining all the topics in one video.

### 00:16:33 · Speaker 1

Thank you so much for watching. If you like my video, please do like it on YouTube. If you think it is very informative and you want your friends to get benefited out of it, please do share it with them. Do not forget to subscribe to my channel Uncommon Geeks on YouTube.

### 00:16:46 · Speaker 1

If you want me to make any videos on a particular topic that that you have not seen on my channel so far, please do mention that in comment section. I'll try to make video on it. Thank you so much for watching. Catch you in my next video.
