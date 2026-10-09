---
id: e99c94a47ca5
title: The Problem with Returning Values from Async Await Functions
url: https://mevasanth.medium.com/problem-with-returning-values-from-async-await-function-javascript-e99c94a47ca5
date: 2021-08-07
author: Vasanth Bhat
platform: medium
---

# The Problem with Returning Values from Async Await Functions

In JavaScript it’s quite annoying sometimes when you’re not aware of how things work, you start scratching your head but you will not find solution to it. In this article I’m going to discuss one interesting problem of that kind. This article is based on async and await.

![](https://miro.medium.com/v2/resize:fit:700/0*FAxQZjUWXEL2LS6t.png)

### **What are async and await?**

In simple words they are syntactic sugars for promise nesting. In case you’re not aware of it, read my article that explains async and await [here](https://medium.com/geekculture/does-async-await-block-javascript-main-thread-c07db9c48c3e).

Assuming you have read above article and know what is async and await let’s take up a simple example.

```
async function foo() {
   const result1 = await new Promise((resolve) => setTimeout(() =>   resolve('1')))
   console.log(result1); //Output is 1
}
```

Output of above functions is 1, pretty straight forward and self explanatory, Where await will block the main thread until the promise is resolved. Now let’s check an interesting version of above code snippet.

### **Can you guess the output of below snippet?**

```
async function foo() {
   const result1 = await new Promise((resolve) => setTimeout(() => resolve('1')))
   return result1;
}
let output = foo();
console.log('Output is' + JSON.stringify(output) );
```

For those of you who have guessed the output as 1, you’re wrong. Copy the code and try running it on any online compilers, the output is {}.

### **Why is it so?**

Because an async function always returns a promise and rather resolving the promise in above example we are trying to extract the value out of it.

### **What’s the solution?**

```
async function foo() {
   const result1 = await new Promise((resolve) => setTimeout(() =>    resolve('1')))
   return result1;
}
let output = foo().then(data => {
 console.log('Result is' + JSON.stringify(data))
});
```

Since async function returns a promise in above code snippet we are resolving it with the help of **.then** method and extracting the value out of it.

### **A better approach**

We use async and await because we want to avoid promise chain or .then expression, so rather using .then we can use async and await itself to resolve the promise, below snippet will represent that.

```
async function foo() {
   const result1 = await new Promise((resolve) => setTimeout(() => resolve('1')))
   return result1;
}async function test(){
 let output = await foo();
 console.log('Result is' + JSON.stringify(output)); // Output is 1
}test()
```

Happy reading, catch you in my next article.

_More content at_ [**_plainenglish.io_**](http://plainenglish.io/)
