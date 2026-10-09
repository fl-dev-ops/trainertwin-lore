---
id: 8e0072961c29
title: Solve Meta | Amazon | Google | Apple Interview Question. Write custom implementation
  for Array.flat()
url: https://mevasanth.medium.com/solve-meta-amazon-google-apple-interview-question-write-custom-implementation-for-array-flat-8e0072961c29
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

# Solve Meta | Amazon | Google | Apple Interview Question. Write custom implementation for Array.flat()

It is quite common in Tier-1 and Tier-2 companies to ask you to implement Polyfill/Custom implementation of built in methods in JavaScript. These questions have become very important because of below reasons.

1.  **Your knowledge about built-in function**: Unless you know about it, you won’t be able to write Polyfill for this.
2.  **Basics of writing PolyFills:** This is an important skill, which will determine, have you ever tried writing any custom methods of your own.

> For Beginners: What is Polyfill

A polyfill is a piece of code (usually JavaScript on the Web) used to provide modern functionality on older browsers that do not natively support it.

You can straightaway goto below video and watch my explanation. Otherwise You can also read the article.

![](https://miro.medium.com/v2/resize:fit:700/1*rLznAnsSn89iY4GxS3Q9cw.png)

First thing first, we need to understand what is Array.Flat ? and how it works ?

> Array.flat

The `flat()` method creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.

Definition taken from official Mozilla [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat).

Ex: Input:

```
const arr1 = [0, 1, 2, [3, 4]];console.log(arr1.flat());// output: [0, 1, 2, 3, 4]
```

> **Syntax**

```
flat()
flat(depth)
```

**Depth**: The depth level specifying how deep a nested array structure should be flattened. Defaults to 1.

**In simple words Array.Flat will flatten nested array into a flatten array. The depth can be specified using parameters.**

> Basic Idea

To write a custom implementation of this, first we need to be aware of broad persona of this problem. In simple ways,

1.  We will iterate through array and array index is an element push it to **result**. If not, goto **Step 2.**
2.  If array index is array then: **Goto Step 1**

> Let’s learn the Recursive approach for this problem

After learning the recursive approach we can see how to add it to custom implementation.

> **Recursive solution to Array.flat**

```
let output = []
function flattenArray(arr){
        for (let i = 0; i < arr.length; i++) {
            if(Array.isArray(arr[i])){
                flattenArray(arr[i]);
            }else{
                output.push(arr[i]);
            }
        }
        return output;
 }
```

As I explained above, we are iterating through the array above and checking if Index is array or not, if it is not array then, we are pushing value into output. In case if it is an array then we are recursively iterating that array and pushing value into array.

Simple dry run:

```
const output = []
const arr = [0, 1, 2, [3, 4]];As long as array index is element:
output = [0,1,2]When array index is array.
arr = [3,4]
output = [0,1,2,3,4]
```

> **Writing custom implementation/Polyfills for Array.flat**

```
Array.prototype.myFlat = function(){
    const output = []
    function flattenArray(arr){
        for (let i = 0; i < arr.length; i++) {
            if(Array.isArray(arr[i])){
                flattenArray(arr[i]);
            }else{
                output.push(arr[i]);
            }
        }
        return output;
    }
   const returnValue = flattenArray(this);
   return returnValue;
}const inputArray = [0, 1, 2, [3, 4, [5,6]], 7];console.log(inputArray.myFlat());
```

In case if you don’t know, how to add method to built in functions. Please read my articles [here](https://mevasanth.medium.com/how-everything-is-object-in-javascript-a4164d7e6a2d) and [here](https://mevasanth.medium.com/prototype-and-protypal-inheritance-in-javascript-bb766097ac05).

After reading above articles, you should get fair understanding of prototype inheritance. Then above code should look easy for you to understand. Except, how to write Polyfills, above explanation for recursive approach, holds good for this also.

> **Home work for you**

Try writing iterative solution for the above problem. In case if you attempt it and not able to solve, you can watch my video [here](https://www.youtube.com/watch?v=0Mmx1ri70ME&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&index=4&t=2s).

Thank you for reading catch you in the next article. In case if you not already followed me on medium then please follow, you can follow me on Linked [Here](https://www.linkedin.com/in/vasanth-bhat-4180909b/). Do not forget to subscribe to my Youtube Channel [UncommonGeeks](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos).

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

[**Book a time with Vasanth on topmate.io**
**Simplifying personalised interactions for the world's leading minds**
topmate.io](https://topmate.io/vasanth_bhat?source=post_page-----8e0072961c29-----------------------------------------)

You can watch all my custom implementation/PolyFill videos here.

If you’re preparing for a frontend developer interview, please watch the below series of mine:

Try writing iterative solution for the above problem. In case if you attempt it and not able to solve, you can watch my video [here](https://www.youtube.com/watch?v=0Mmx1ri70ME&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&index=4&t=2s).
