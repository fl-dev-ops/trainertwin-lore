---
id: 9d44e0487987
title: How Hoisting works in JavaScript if it is interpreted ? — Hot topic for interview.
url: https://medium.com/geekculture/how-hoisting-works-in-javascript-if-it-is-interpreted-9d44e0487987
date: 2022-02-23
author: Vasanth Bhat
platform: medium
---

# How Hoisting works in JavaScript if it is interpreted ? — Hot topic for interview.

In JavaScript, variable and function Hoisting are one of the most important topic that you need to prepare for interview. In case if you’re new to JavaScript world, please read my [article](https://mevasanth.medium.com/hoisting-in-javascript-hot-topic-for-interview-43b463a6a77) which explains what hoisting in JavaScript.

![](https://miro.medium.com/v2/resize:fit:700/1*Qd3gSkeUOhrrYBBjGXi3FA.png)

Source — dev.to

Before getting into Hoisting let us understand some of the basic programming paradigms, which are necessary to understand the hoisting concept in detail.

**What are the differences between compiled and interpreted programming language ?**

One can find detailed differences in this [link](https://www.geeksforgeeks.org/difference-between-compiled-and-interpreted-language/). I’m sticking into layman terms, In a compiled language, the target machine directly translates the program. In an interpreted language, the source code is not directly translated by the target machine. Instead, a _different_ program, aka the interpreter, reads and executes the code. Interpretation is always line by line. ( In case of Google V8, the engine it is written in c++ which will interpret the JavaScript. )

**Ex for compiled languages**: Java, c# etc.

**Ex for interpreted languges**: JavaScript, Python etc.

As per official definition, **JavaScript is interpreted, single threaded programming language**. Now we already know what is interpreted language, **when program is executed line by line how feature like hoisting is achieved ?** Keeping in mind of larger audience I’m giving definition of hoisting below.

**What is Hoisting in JavaScript ?**

“Hoisting is JavaScript’s default behavior of moving declarations to the top.” One can relate it with flag hosting, where flag will be hoisted to the top of the pole. Find detailed article [here](https://mevasanth.medium.com/hoisting-in-javascript-hot-topic-for-interview-43b463a6a77).

Assuming, by now all of you know what is hoisting in JavaScript, let us understand,

**Why hoisting is implemented in JavaScript ?**

In JavaScript when you have to call a function which is defined above or below a particular block, the main thread must know where the function definition exists. (Guess the output of below code)

Ex:

```
function one(){console.log('Inside function one')}function two() {one();three();}function three(){console.log('Inside function Three')}two()
```

As you guessed the output is :

```
Inside function one
Inside function Three
```

This works because JavaScript main thread knows where is function one and three. This is achieved by hoisting the functions or all the function definitions are placed on top of the block so that main thread is aware of it.

**JS creator Brendan Eich** the creator of JavaScript once said on Twitter, they wanted to implement function hoisting for above mentioned reasons and hoisting variables defined with var key word (Ex: var x) was unintended and happened in rush **. I believe later it was not removed because var has a global scope. So, team might have decided not to remove var hoisting.**

**Now let us get into title of the topic, how hoisting is achieved in JavaScript**

After you write the JavaScript code, the interpretation happens in two phases.

**Completion or compilation.**

During first run there is no execution, the interpreter goes through the code line by line while looking for functions or variable declarations. As soon as it finds them it moves it to the top of the block.

This is how the interpreter will get an idea about which functions and variables are going to be used in the current context, also how much approximate memory it will be needing to execute the current function. Further, it also helps in creating variableObject for Execution Context right before execution of function starts.

_Below things are skipped during this phase:_

1\. Variable and functional assignments.

2\. ‘class’ declarations.

3\. code statements.

4\. function calls

**Execution**

This the phase where actual execution happens, calling the functions, making network calls, taking input from user, allocating memory all of that happens in this step.

Because of this 2 step interpretation approach in JavaScript, hoisting is possible.

In next interview if they ask this question, you will be able to answer it confidently, happy reading.
