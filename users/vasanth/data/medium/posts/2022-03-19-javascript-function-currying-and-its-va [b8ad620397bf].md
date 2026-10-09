---
id: b8ad620397bf
title: JavaScript — Function currying and it’s variations
url: https://mevasanth.medium.com/javascript-function-currying-and-its-variations-b8ad620397bf
date: 2022-03-19
author: Vasanth Bhat
platform: medium
---

# JavaScript — Function currying and it’s variations

![](https://miro.medium.com/v2/resize:fit:700/1*3jzXe1Q6rJOBM3V9P_tLNg.jpeg)

### **Function currying definition:**

_“Currying is a process in functional programming in which we can transform a function with multiple arguments into a sequence of nesting functions. It returns a new function that expects the next argument inline.”_

Let’s start with a simple example where we will write a function that adds two numbers and returns the sum.

```
function add(a, b){
   return a + b;
}
let output = add(10,20);
console.log(output) // output will be 30
```

As most of you know, above is a simple function that takes 2 arguments, adds it and returns the sum. This function is fine when we know two arguments well in advance and we want to compute it’s sum.

What if we have a scenario, where two arguments will be known at two different places in the code block ? once after both numbers are available we will call the add function ? There are few approaches to solve this problem we can use JavaScript bind for the same purpose, but the most preferred way to do it using **currying**.

Let’s modify the above example so that it takes two arguments at two different parts of the program.

```
function add(a){
  return function(b){
    return a + b;
  }
}let fnCall = add(10);
console.log(fnCall(20)); //output will be 30
```

Observe the above code snippet carefully, we have an outer function add, that takes one argument and when you call it, it will return a function that takes an other argument. By JavaScript closure property, the inner function will have access to variable “a” passed to add function. If your not aware what is closure, read my article regarding it( [JavaScript Clousures — Tricky Interview Topic](https://mevasanth.medium.com/javascript-clousures-tricky-interview-topic-3e129435083e))

Now whenever we get the second argument we call the inner function whose reference is present on variable fnCall, so the output of above code will be **30**.

Now let’s see a small deviation of it, which is very commonly asked in the interview.

Write a function that adds two numbers and function call should look something like this — **add(10)(20).**

Don’t panic, this is also function currying, where at one stretch your invoking two functions, which are nested. The code snippet looks like below.

```
function add(a){
  return function(b){
    return a + b;
  }
}let output = add(10)(20);
console.log(output); //output will be 30
```

### **What are the main use cases of function currying?**

1. Like you already saw, when the arguments required for a function will be available at different places inside a code, then we can use function currying.
2. Best suited for performing mathematical operations related to Mathematical functions, which involves common sequences like **f(g(x)) (** I will write an example for it below **).**
3. Function currying can be also extended to take infinite arguments (obviously until there is space available in memory for computing). This is helpful when we have to perform a particular task, irrespective of the arguments passed to the function, then we can use function currying. (There is an example below for same)

### **Writing Mathematical functions using Function currying**

```
const f = x => x + x
const g = y => y * ylet output =  f(g(10))
console.log(output) //output will be 200
```

In above code block, we have written two functions named **“f”, “g”.** When we write the function call f(g(10)) we are passing value 10 to the function g(), which multiplies the arguments passes, so the value will be 10\*10 = 100.

This 100 is passed to function f() as an argument, and passed value is added inside function f(), so the output is 100 + 100 = **200\.** This can be nested to any hierarchy depending upon the mathematical computation that your performing.

Note: For those of you who are wondering **const g = y => y \* y** how this will multiply the value of y and return, it is default behaviour of the arrow function when you do not specify the brackets, the value is computed and returned. If you add the flower braces then the value should be manually returned.

### **Extending currying to add infinite numbers inside a function**

Let’s extend the above function add so that it takes infinite arguments and adds it and returns the sum.

**For ex function call would look like this:**

`add(10)(20)(30)()`

`add(10)(20)(30)(40)(50)(60)()`

`add(10)(20)()` etc.

### **This is one of the most common and tricky interview question asked in JavaScript interview.**

Your currying function should be able to compute the sum in case of all these different function calls. As soon as you look at this question, your mind should think recursively, here the delimiter for the function call is the last empty parenthesis, in recursion terms it is the base case.

There is no built in property inside function currying to handle this scenario, we need to combine the concept of currying and recursion to solve this problem. The working code snippet is below.

```
function add(a){
  return function(b){
    if(b){
      return add(a+b)
    }else{
      return a
    }
  }
}
let output1 = add(10)(20)();
let output2 = add(10)(20)(30)(40)();
console.log(output1); //output will be 30
console.log(output2); //output will be 100
```

In above recursive code, we are running the function until we encounter an empty parenthesis and if it is not then we will calculate the sum and store it in variable a, which is returned at the end.

### **Puzzle for readers**

Now that you know how to use recursion and currying together. Now some brilliant interviewers will ask you a question like below.

Write a function add which gives the sum when it is invoked like below,

`add(10)(20)`

`add(10,20)`

As you can observe first one is how you call function currying and second is how you call a normal function, so the function you write should behave in both the ways.

I won’t answer this question, but will give you a hint. Use the JavaScript arguments property which will give you the set of arguments passed to the function and use it inside a condition to differentiate whether function is invoked like currying or like normal function.

**Other interesting articles by the same author**

1. [How everything is Object in JavaScript ?](https://mevasanth.medium.com/how-everything-is-object-in-javascript-a4164d7e6a2d)
2. [Hoisting in JavaScript : Hot topic for Interview](https://mevasanth.medium.com/hoisting-in-javascript-hot-topic-for-interview-43b463a6a77)
3. [Memoization in JavaScript — Hot topic for Interview](https://mevasanth.medium.com/memoization-in-javascript-hot-topic-for-interview-815475544ab0)

Click [here](https://mevasanth.medium.com/) for all the articles by the author.

_More content at_ [**_plainenglish.io_**](https://plainenglish.io/)
