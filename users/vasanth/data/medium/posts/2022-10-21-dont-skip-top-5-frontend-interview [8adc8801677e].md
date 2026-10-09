---
id: 8adc8801677e
title: Don’t skip | Top 5 frontEnd Interview topics to prepare in 2022
url: https://mevasanth.medium.com/dont-skip-top-5-frontend-interview-topics-to-prepare-in-2022-8adc8801677e
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

# Don’t skip | Top 5 frontEnd Interview topics to prepare in 2022

With my experience of taking interviews to hundreds of candidates, many frontEnd developers still don’t know what all topics to prepare for the interview. They are all good developers, if you ask them to build beautiful websites or mobile applications, they will be able to build it in a short duration. But they will not be strong conceptually. So, I decided to list all the most common interview questions of frontEnd developer interviews with some example snippets.

If you’re too bored to read, you can watch my video on Youtube here. If you have not subscribed to my channel, please subscribe and let me know what you think about my video in the comment section. You can also continue to read the article below.

![](https://miro.medium.com/v2/resize:fit:700/1*X28Fsim51D5-G3pLOGh15Q.png)

> Core topics to prepare for frontEnd developer interview

1. Hoisting
2. Closures
3. SetTimeout
4. Promise
5. Currying

> **Hoisting**

JavaScript Hoisting refers to the process whereby the interpreter appears to move the _declaration_ of functions, variables or classes to the top of their scope, prior to execution of the code.

To know more about hoisting you can watch my videos [here](https://www.youtube.com/watch?v=skkXL5QdDwk&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=2). Or you can also read my medium blog [here](https://mevasanth.medium.com/hoisting-in-javascript-hot-topic-for-interview-43b463a6a77). After watching this, you should get a fair understanding of hoisting. Now, try answering the questions below.

Common questions:

**Simple one:**

```
function test(){
    console.log('X is ' + x);
    var x;
}
test();
```

output for above is **undefined**.

**Tricky one**

```
var rate = 10
function getRate() {
    if (rate == undefined) {
        let rate = 6;
        return rate;
    } else {
        return 10;
    }
}
console.log("Rate is", getRate());
```

Try guessing output for this, if you fail, you can watch my video [here](https://www.youtube.com/watch?v=U1BXdBkXFgw&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=3), that clear explains why it is so.

> **Closures**

_A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time._

> **setTimeout**

_The global_`setTimeout()` _method sets a timer which executes a function or specified piece of code once the timer expires._

It has become a deadly combination to use the combination of closures and setTimeout questions in most of the interviews. In case you’re not sure of the basics, please watch videos [here](https://www.youtube.com/watch?v=pycV_CSoj1g&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=15) and [here](https://www.youtube.com/watch?v=nJhQRotbIis&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=15).

After watching these videos I think, you will get a fair understanding about the above topics. try guessing the output of the below snippet.

// Snippet 1

```
function example1(){
  for (var i = 0; i < 3; i++) {
    setTimeout(function() { console.log(i); }, 1000 * i);
  }
}
```

As it has become a classic snippet everybody guesses the output as 3 which will be printed 3 times. But do you really know what interval ?? Many don’t know this, because it is not taught in most videos or blogs. So, please don’t learn the question, learn the concept. If you have learnt the concept correctly, you will be able to guess the answer correctly. Right answer for this is, 3 is printed 3 times with 1 second interval.

```
// Snippet 2function example2(){
 for (var i = 0; i < 3; i++) {
 setTimeout((function() {
 console.log(i)
 })(), 1000 + i);
 }
}// Snippet 3function example3(){
 for (var i = 0; i < 3; i++) {
 setTimeout(function(k) {
 return function() { console.log(k); }
 }(i), 1000 + i);
 }
}
```

Try guessing the output of above 2 snippets, if you don’t get the right answer, watch my detailed explanation [here](https://www.youtube.com/watch?v=mrhYod2W_V0).

> Promise

The `Promise` object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

With my experience, Promises don’t have any common tricky interview questions. Mostly you need to understand what are promises and when to use promise.all and promise.allSettled etc. To learn more, watch my video series starting from [here](https://www.youtube.com/watch?v=1OINZhOIh0c&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=19)

> Currying

Currying simply means **evaluating functions with multiple arguments and decomposing them into a sequence of functions with a single argument.**

Currying is not a common interview topic. But it is a very important interview concept. General questions asked on currying are as below.

1. Write a currying function with infinite arguments. Ex: sum(10)(20)(30)(). In case you don’t know the answer to this, read it [here](https://mevasanth.medium.com/javascript-function-currying-and-its-variations-b8ad620397bf).
2. Write a function that behaves both as currying and non-currying. Ex: sum(10)(20) and sum(10,20). In case you don’t know the answer to this, watch it [here](https://www.youtube.com/watch?v=uaYnUiyCWII&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=18).

Thank you for reading catch you in the next article. In case if you not already followed me on medium then please follow, you can follow me on Linked [Here](https://www.linkedin.com/in/vasanth-bhat-4180909b/). Do not forget to subscribe to my Youtube Channel [UncommonGeeks](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos).

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

[https://topmate.io/vasanth\_bhat](https://topmate.io/vasanth_bhat)

If you’re preparing for a frontend developer interview, please watch the below series of mine:

If you want to learn JavaScript custom implementations of built-in methods, then watch the below series of mine:
