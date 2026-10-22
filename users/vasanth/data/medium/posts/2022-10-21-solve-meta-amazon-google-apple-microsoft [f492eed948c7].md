---
id: f492eed948c7
title: Solve Meta, Amazon, Google, Apple, Microsoft frontEnd developer interview question
url: https://medium.com/geekculture/solve-meta-amazon-google-apple-microsoft-frontend-developer-interview-question-f492eed948c7
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

After I’m researching a lot on web, I came to a conclusion that, there is no tutorial/video series that is dedicated for MAANG(Meta, Apple, Amazon, NetFlix, Google) preparation for FrontEnd developers. So, I decided to decode most common interview questions of MAANG in my Youtube channel. In this article I will discuss a very interesting problem. So, read till the end.

Flatten an array without using Recursion.

Question: Flatten the given array

Sample Input:[1,2,[3,4],5]

Sample Output:[1,2,3,4,5]

Company where the question is asked : Meta/Microsoft/Google/Apple/Amazon

I have written recursive solution for this problem here. It is very important to know the recursive approach, as most companies expect you to know this solution. But iterative approach too is not that easy. So, in interview they may ask you to write both the solutions. So, in this article I will be explaining Iterative approach.

Crux of the logic

let arr = [1,2,[3,4]];
let last = arr.pop(); // Ex: [3,4]
arr.push(...last); // Spread operator will convert [3,4] to 3,4
console.log(arr)

Copy this code and run, you should get an insight about the crux of the logic. Below explains it in detail.

Algorithm

1. Taking the last element of the nested array,
2. In case if it is also an array then we use spread operator to eliminate the array and push it back to array.
3. If it is not an array then don’t use spread operator just push the value into array.

Complete code

function flatten(input) {
  const stack = [...input];
  const res = [];
  while (stack.length) {
    // pop value from stack
    const next = stack.pop();
    if (Array.isArray(next)) {
      // push back array items, won't modify the original input
      stack.push(...next);
    } else {
      res.push(next);
    }
  }
  // reverse to restore input order
  return res.reverse();
}

const arr = [1, 2, [3, 4, [5, 6]]];
flatten(arr);

Explanation:

const stack = [...input];
// it is just a deep copy of variable. Otherwise source array will // be modified

res variable is used to hold the final result.

return value is reversed res, because we are performing our activity from the last. So, while finally sending the result it should be reversed to make it in the actual order.

return res.reverse();

If you have not followed me on Medium, please follow. Do not forget to subscribe to my Youtube Channel,

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

Book a time with Vasanth on topmate.io
Simplifying personalised interactions for the world's leading minds
topmate.io

If your preparing for frontEnd developer interview, please watch below series of mine:

https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t

If you want to learn JavaScript custom implementations of built in method, then watch below series of mine:

https://www.youtube.com/watch?v=eGzErMUfdpk&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I
