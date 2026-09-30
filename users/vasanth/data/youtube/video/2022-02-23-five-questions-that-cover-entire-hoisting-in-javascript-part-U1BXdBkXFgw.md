---
id: U1BXdBkXFgw
title: Five questions that cover entire hoisting in JavaScript Part - 1 (Hoisting
  Ep - 2)
date: '2022-02-23'
url: https://www.youtube.com/watch?v=U1BXdBkXFgw
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Hoisting is very important concept of JavaScript. Reason for that is, when you\
  \ know what is hoisting in JavaScript, you will definitely know\n\n1. Different\
  \ ways to create variables in JavaScript\n2. Local Scope, Lexical Scope and Global\
  \ Scope\n3. How JavaScript Engine works\n\nSo, just by asking one question, interviewer\
  \ can understand most of your fundamental skills. \n\nMy Medium Blogs - https://mevasanth.medium.com/\
  \ \nGithub URL which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nHoisting\
  \ Video Part 1 - https://www.youtube.com/watch?v=skkXL5QdDwk"
author: careerwithvasanth
duration: 00:12:25
model: saaras:v3
transcript: true
---

# Five questions that cover entire hoisting in JavaScript Part - 1 (Hoisting Ep - 2)

## Transcript

### 00:00:00 · Speaker 1

Hello all. Welcome welcome back to Uncommon Geek. So we were discussing hosting in the now past videos. I'm continuing the same session in this video as well. In the first video we had seen the discussions about the fundamentals of hosting. In second video we had discussed some questions on hosting. And in this third video also we are going to discuss some more questions on hosting. But this video is predominantly on the uh code snippets where some snippets I'll be showing you one after the other and then you you should be guessing the output of it. Okay. without wasting further time, let's get started.

### 00:00:33 · Speaker 1

is the first snippet, uh one of the easiest one to start off, okay? So where I've created a function named test and I've created two variables with the same with the keyword var and the name of the both the variables are same. So six and seven, so both have the variable x and in line number eight I'm trying to print the value of of x, okay? The first question would be guess the output of this. What do you think the output of this function is? Okay? um if you all if

### 00:01:03 · Speaker 1

you already know the answer please do comment that in the comment section. If not, uh I I'll explain you the answer. So we have declared the variable with a keyword var twice here. So x and x, okay? And we are trying to log the value of x here, okay? uh with if you're from any other programming language background, you you would think like this is an error because of the redeclaration. Same variable declaring twice would lead to an error, okay? uh That's quite obvious also because as you know the variables are basically point to

### 00:01:33 · Speaker 1

memory location. Since we in the programming we cannot access we cannot use a memory location for identifying a value of a variable, we use the variables which is human understandable, okay? So if we duplicate it then we start thinking like there is no way where same variable can can point to two different memory locations. Or within a same block we start getting the redeclaration error. But here actually what happens an interesting output will come, let me show you. X we get as undefined. The reason being okay. Let me declare one more time. Three times I'm declaring.

### 00:02:09 · Speaker 1

So we are getting still x is undefined. Okay? Let me do one thing. I'll assign a value of ten here. Okay?

### 00:02:16 · Speaker 1

So we are getting ten

### 00:02:18 · Speaker 1

Let's say if I add same term here.

### 00:02:22 · Speaker 1

we are getting ten. What if I do ten here and forty here? Okay?

### 00:02:30 · Speaker 1

So hope you understanding what is actually happening. So inside a given block, variable created with var keyword is having a global scope. And in entire scope, scope I mean from line number five to line number ten, there is only one variable which with which var gets created if the name is same. So var x no matter how many times you declare the variable x inside a particular block, there will be only one instance of it and the value will be keep on getting updated. So in our case var x

### 00:03:00 · Speaker 1

whenever our JavaScript engine scanned this function variable x got hoisted, okay, to the top. Then it encountered line number six during the second run, initialized to ten and it came here, so x became undefined. No, no, x did not become undefined here because there is only one x. So value of x whatever you initialize here, that value still holds good. Then it goes to the line number eight, okay, where it updated the value to forty. So just to clarify I'm removing this line so that you will be able to understand much better. See still exists ten. So

### 00:03:30 · Speaker 1

With our common sense we would have thought like x equal to it here it became ten then when it comes here again x become undefined no because there is only one instance and x got already hoisted so whatever the value that we have encountered that value is gonna remain and it's only gonna replaced whenever there is a new value initialized to it until then the execution continues the same way okay

### 00:03:52 · Speaker 1

See this is about the question number one, okay? Looks pretty straightforward, but the concept involved here where the variable declared with var keyword will be having a global scope and no matter how many times you redeclare it, there will not be any error and it will be only using the most recent value in the given scope, okay? I'm just commenting this. Let us go to the question number two.

### 00:04:16 · Speaker 1

Question number two is almost the same as the question number one. I I intentionally have taken this example so that you'll be able to think in the same direction. So we have created two functions now, var test and let test, okay? It is pretty much the same. We have created a variable with var keyword x here. Then in the twenty one twenty two, I am updating the value, okay? And here I am again printing the value of x.

### 00:04:42 · Speaker 1

Let me first call this var test. Since you already have seen the first example and you are aware of the execution cycle how it's going to execute. I guess most of you will be able to answer it. Please do mention that in the comment section. I'll let me execute this.

### 00:04:57 · Speaker 1

So we're getting two twice because as you know variable created with a var keyword is having only one instance redeclaration is allowed inside a block. So what is happening is there is only one instance of x. So first was in line number nineteen then it came here inside then it became two. So same variable so which was pointing to one now pointing to two. So here the value got printed two it came outside. As you know same variable x is for the entire block so here also it is pointing to

### 00:05:27 · Speaker 1

as two. Now an interesting question here I am using let variable. Okay. Rest of the execution is same rest of the things are same. Can you guess the output of this? Okay. If you know the answer please do mention the video timing and your answer let me execute it.

### 00:05:45 · Speaker 1

two and one, okay? This is a slight difference. So what happened is let is not having a global scope. Let is having a local scope or a lexical scope uh to the block wherever it belongs. So line number twenty nine to thirty two is the scope of this uh scope of this particular variable, okay? And line number twenty eight what you have declared, uh this let x, so this scope is from twenty seven to thirty four. So this whatever you are seeing here, one execution context get created for this block.

### 00:06:15 · Speaker 1

and it will it will be removed as soon as it encounters the end of the scope, all line number thirty two. So what's happening, the compiler is coming here, let x equal to one, then going inside let x equal to two, console.log x, then this let x whatever created inside this, that is that memory is totally removed. When you come out, we are only having one x. Okay? Where we are getting the value as here it has two, here it has one. Okay? Now, if you remove this uh bracket, what's going to happen or parenthesis

### 00:06:48 · Speaker 1

flower bracket what's going to happen guess the output. So this is also another again another important interview question okay.

### 00:06:56 · Speaker 1

So what we are getting is X has already been declared. So re-declaration error we are getting. So only variable declared with var keyword is going to have one instance, but the variable defined with let keyword cannot will not have one uh will only variable with var keyword will have only one instance for the entire block. So it's a global scope. But let keyword will have a local scope. That means inside a given block you cannot define the same variable twice. Okay? So this will throw you an error. So hope you are clear.

### 00:07:26 · Speaker 1

believe on these two questions. If possible I will be adding all these questions into my Github repo and try to link it in the description. Okay, please do check it. And this is third question.

### 00:07:37 · Speaker 1

quite straightforward question, okay? The reason I introduce this is I wanted you also to win sometimes by answering some easy questions. So this do something, so I'm calling this function. So here we are trying to log the value of variable bar above it and below it. So this is the same almost the same example that I gave in the introduction video of the hosting. Let me run it. If you know the answer as usual do comment video timing and your answer. So we're getting undefined and eleven.

### 00:08:07 · Speaker 1

one one one. So the design for this also you know already. So inside a given block whenever you encounter a VAD keyword it get hoisted onto the top and the default value of it will be undefined. Okay. Like this it happens during the first run and during second run whenever its execution happens in line number forty three we print the undefined and forty four in line number forty five we print whatever the actual value of bar that is one one one because here the initialization is over or the declaration of the variable got completed. So

### 00:08:37 · Speaker 1

here we are getting one one one. Till then we in the in the given block we the value of variable bar will be undefined. Okay. Quite straightforward. Okay let me go to the another question. Last question for this video. Okay. Very common interview question. Ninety nine percent of the people will fail to answer this if they are looking at it the first time. Okay. Let's see how brilliant you are. Look at this code and whoever answers first to this question definitely reply to that comment. Okay. So line number fifty nine. So

### 00:09:07 · Speaker 1

we are trying to invoke this function get rate. uh here we have declared a variable called rate. I'm not going to explain further on this. I just want you to guess the output if you know I mention it. Otherwise I'll run it. Okay. uh yeah.

### 00:09:20 · Speaker 1

So we're getting rate as six. Okay. What happened is we we know the function get rate. And whether rate is equal to undefined. So rate is already declared as ten here, right? So rate is equal to undefined will be false. So it will come to the else and we'll return the value as ten, okay? But we are getting the value as six, not ten. So most people will tell the same answer like how I explained, they will tell answer as ten. But what happens is you know the concept of hoisting, but you will miss to

### 00:09:50 · Speaker 1

inculcate or use it in this particular given function. What will happen is so as I said variable declared with var keyword is having a global scope. Okay entire parent scope it will be there. So inside this block there is only one variable rate no matter how many times you declare it. So what happens is here it will go like this. Here it will go like this. And here it will be initialized undefined during the first run. This is the hosting right. So then this statement becomes true and so it will come inside and it will

### 00:10:20 · Speaker 1

specialize the value of rate as six and it will return that particular variable which whose value is six. Okay.

### 00:10:28 · Speaker 1

That's what happening. Now, obviously you start asking a question, I already have a rate here in line number fifty eight, I already have a rate. Correct? Why not that has been used here? Obviously it's a global variable, correct? And we are trying to access that variable here, correct? So, but the problem what's happening is we have a same variable name, fifty eight and line number sixty. Whenever there is a local scope and a global scope conflict, always local scope is given priority. So if you are having same variable

### 00:10:58 · Speaker 1

outside the function and inside the function. So whatever the variable declared inside the function will be given a priority. That's what happening here as well. Okay. I mean if you make it as a rat and this also as a rat, okay. Then this becomes false. We would get probably ten. See. What happened was there is no conflict now. So this function is able to use the able is able to use the outside variable rat. And rat is equal to one defined is false because rat is ten. We are getting the value as ten.

### 00:11:28 · Speaker 1

So these are the some tiny variations of hoisting which can be asked during the interview. So I have I have come up with some common questions that can be asked. There could be some deviation to the same concept. So there will not be any brand new question that can be introduced in hoisting. This is only the variation maybe they would loop it in multiple functions or multiple blocks to just to make you confuse. But you are fundamentally clear about the concept there is no way where you will go wrong. Okay. Please do please do execute all this code in your

### 00:11:58 · Speaker 1

local and try to vary do a variations of it like how I did and analyze it thoroughly. Okay. So if you like my video please subscribe to our channel Uncommon Geek and also like our video on YouTube channel and share it with your friends if you are liking it and also subscribe to our channel. If you want video on any particular topic that was asked you in any particular interview and you are not able to answer please do mention that in the comment section I will try to make a video out of it. Thank you all for watching catch you in next video.
