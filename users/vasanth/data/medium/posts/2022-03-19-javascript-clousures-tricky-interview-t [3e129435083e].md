---
id: 3e129435083e
title: JavaScript Clousures — Tricky Interview Topic
url: https://mevasanth.medium.com/javascript-clousures-tricky-interview-topic-3e129435083e
date: 2022-03-19
author: Vasanth Bhat
platform: medium


---

# JavaScript Clousures — Tricky Interview Topic

![](https://miro.medium.com/v2/resize:fit:700/1*Wpu_JOeX_j3BfdAgbs42YA.jpeg)

Sometimes I feel JavaScript weird, if your from the background of Java, C, C++ or C# where everything works as per your expectations, JavaScript it isn’t.

consider a simplest example:

```
function add(x,x){console.log(x+x)
}add(10,30)
```

can you guess the output of this ? In most language code block would throw a syntax error. In case of JavaScript the output is 60. Wonder how ? since priority of execution is from left to right, the last value of x in function add will be 30, so 30 + 30 will be 60.

There are many such tricky aspects in JavaScript, one of the most important when it comes to interview is closures.

**Definition of Closures (Source: developer.mozilla.org)**

A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function.

Before taking a look at closure example it is better to know about inner function.

```
function one(){
   function two(){
     console.log("Inside two")
   }   two(); //call should be B();
}one() // output will be "Inside two"
```

As you can see in the above code snippet, there are two function nested one inside the another, this is called as inner functions in JavaScript. The inner function can be triggered in many ways, one such way is to trigger it from the outside function like shown above.

Let’s extend the example now

```
function one(){
  let num = 10;
   function two(){
     console.log("value of numb is " + num)
   }
  return two();
}
let test =  one()
console.log(test) //output will be "value of num is 10"
```

Here what we are doing is, when you call the outer function, the inner function is returned. And later, we are invoking the inner function and what is interesting to observe is the output,

```
value is num is 10
```

observe the execution carefully, when we invoke the outer function, inner function is not executed just reference to it is returned, in absolute JavaScript terms, there is no execution context created for function two, still when we invoke it later, it can access the value of num which is 10.

**How is this possible ?**

This is possible because of the closure in JavaScript, where variables declared outside the function can be accessed inside the function.

**Why it is required ?**

**Example 1**

Let’s take a simple example where a function should increment the counter. (This is very common question asked in the interview)

```
var count = 1;
const increment = function() {
  console.log(count++)
}
increment() // prints 1
increment() // prints 2
increment() // prints 3
```

Above code will serve the purpose, if you answer this, the interviewer will add 2 more constraints don’t use global variable and don’t pass count as an argument. Now the problem get’s tricky, how would you achieve it ?

Again using the closure, look at the answer below.

```
const increment =  (function() {
  var count = 1;
  return function(){
    return count++;
  }
}())console.log(increment())
console.log(increment())
console.log(increment())
```

Here we have used something called self invoking function it’s also called as iffy in some organisation as a short form. The purpose of it it, it executes automatically. The main purpose of writing this is, it will create a closure for inside return function which will get the value of count.

**Example 2:**

Another most commonly asked interview question is print 1,2,3,4,5 each at an interval of 1,2,3,4,5 seconds. When you hear this question you would think of something similar below, using loop.

```
function printCount() {
  for (var i = 0; i < 5; i++) {
    setTimeout(() => {
      console.log(i)
    },i*1000)
  }
}
printCount()
```

Where we have created 5 timeout functions and they start getting executed at 1 sec, 2 sec, 3 sec, 4 sec and 5 sec. But the actual output will be

```
5 // which will be printed at the proper interval mentioned above
```

**Why this happens ?**

As most of you know, setTimeout function takes two arguments, one is the function and other one is the delay. So the function defined inside the setTimeout will be using a property of closure, at the time of setTimeout creation, it will have a reference of i and fetches the value from that reference for the usage once the delay is completed.

Since var is function/Global scoped all the timeouts will be having reference of the same variable i, since for loops gets executed very fast as compared to setTimeout, when setTimeout starts it’s execution the value stored in the reference of i will be 5.

**How to solve this problem ?**

Easiest solution to this problem would be, using **let** instead of **var**, since **let** is block scoped, when loop runs the reference of i for each instance will be different.

**How can you solve this problem without using let / Since let is not available in ES5 how do you design a Transpiler that converts let to var equivalent in ES5**

When any of the above question asked, the solution is simple, as you might know, in JavaScript functions are first class members, that means they are like any other variable, we can pass it as an argument and return as an argument. So we can use the same concept here, enclose the for loop inside a function like shown below.

```
function printCount() {
  for (var i = 1; i <= 5; i++) {
    function test(k){
    setTimeout(() => {
      console.log(k)
    },k*1000)
    }
  test(i)
  }
}
printCount()
```

Here, we have created 5 functions inside for loop and for the function the value is passed as an argument.

There are plenty of examples like this, using object and it’s reference. But if your conceptually clear about above example, then you will be able to solve all the questions, happy reading.
