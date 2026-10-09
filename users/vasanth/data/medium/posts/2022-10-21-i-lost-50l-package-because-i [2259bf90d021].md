---
id: 2259bf90d021
title: I lost 50L+ package, because I couldn’t answer this JavaScript question.
url: https://careerwithvasanth.medium.com/i-lost-50l-package-because-i-couldnt-answer-this-javascript-question-2259bf90d021
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

# I lost 50L+ package, because I couldn’t answer this JavaScript question.

It was a deciding interview round and there were 3 questions, I answered the first question correctly and the second question was partially right. Now the third question was a deciding factor and I couldn’t answer it, due to which I lost a really good package. 50L I have written, so that you will click on my article, but it was really a good package.

What was the question ?

“How to memoize function with varying arguments in JS”

If you’re too lazy to read the article, you can watch my Youtube video below. If not, you can continue reading.

![](https://miro.medium.com/v2/resize:fit:700/1*bMTECdZPNZdSAjyFIJZ3rA.png)

> **Explanation of question:**

```
function add(num1,num2){
   return num1 + num2;
}function multiply(num1,num2, num3){
   return num1 * num2 * num3;
}console.log(add(10,20))
console.log(add(10,20))
console.log(add(10,20))
```

We are invoking the add function 3 times with the same arguments. Rather than computing addition 3 times, we can memoize the add function and use it when the same function is invoked a second time. The memoization function which you write should memoize all the functions (ex: multiply, add in above snippet).

> **What is memoization**

For those of you who don’t know what is memoization here goes the definition:

“In computing, memoization or memoisation is an optimisation technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again”

Simple ex:

Let’s say you want to calculate 20!, after computing 19! you don’t have to compute 19! again and multiply it with 20. You can just store the result of 19! and multiply it with 20. This will save a lot of time and memory.

> **How to solve above problem**

It has two basic problems

1. A strategy to uniquely identify the function with its arguments.
2. Writing memoize function

Let’s solve the problems one by one.

> **1\. A strategy to uniquely identify the function with its arguments.**

Ultimately, memoize is an object with key value pair.

Ex:

{

“key”: value

}

For memoizing a function we need to find a unique id for each function call with its argument.

Below is the code for the same.

```
function getUniqueId(fn, args){let uniqueId = [];uniqueId = uniqueId.concat(fn.name, args);return uniqueId.join("|");}
```

Ex: if you pass function and argument as \[11,22\]

uniqueId will be “ **add\|11\|22**” we are using “ **\|**” as delimiter because we need to uniquely identify arguments like \[1,222\] \[122,2\] etc, if we don’t use “ **\|**” then the key for all these values will be the same.

> **2\. Writing memoize function**

It’s very easy, here goes the code:

```
function memoize(fn){let cache = {};    return function(...args){          let uniqueId = getUniqueId(fn, args);           if(cache[uniqueId]){                  console.log('from cache');                  return cache[uniqueId];            }else{                  cache[uniqueId] = fn(...args);                  console.log('not from cache');                   return cache[uniqueId]              }        }}
let memoiseAdd = memoize(add);let memoiseMultiply = memoize(multiply);console.log(memoiseAdd(10,20));console.log(memoiseAdd(10,20));
console.log(memoiseMultiply(10,20,30));console.log(memoiseMultiply(10,20,30));
```

What we are doing above is, we have created a function called memoize which takes a function as input and returns another function which takes varying arguments as output. Returned function will have access to the function that is passed as an argument because of **closure property**.

After that it’s very simple **memoiseAdd** refers to a function and you can use it to call add function any number of times and as long as the arguments are matching it will return the cached value.

Sample cache object looks like below

```
{ 'add|10|20': 30 }
{ 'multiply|10|20|30': 6000 }
```

**Above approach has certain limitations :**

1. What if the argument also contains “\|” then pipe cannot act as delimiter.
2. It will not work for passing function as properly with anonymous functions.

**_These can be solved with multiple approaches, I have discussed them in detail in my Youtube video. Please watch it for more information._**

Thank you for reading catch you in the next article. In case if you not already followed me on medium then please follow, you can follow me on Linked [Here](https://www.linkedin.com/in/vasanth-bhat-4180909b/). Do not forget to subscribe to my Youtube Channel [UncommonGeeks](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos).

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

[https://topmate.io/vasanth\_bhat](https://topmate.io/vasanth_bhat)

If you’re preparing for a frontend developer interview, please watch the below series of mine:

If your a reactJS developer and looking for interview preparation, watch my complete interview preparation guide here:
