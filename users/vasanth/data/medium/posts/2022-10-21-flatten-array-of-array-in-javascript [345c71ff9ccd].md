---
id: 345c71ff9ccd
title: Flatten array of array in JavaScript | Microsoft Interview question
url: https://mevasanth.medium.com/flatten-array-of-array-in-javascript-microsoft-interview-question-345c71ff9ccd
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

# Flatten array of array in JavaScript | Microsoft Interview question

Flattening array of array has become one of the most common interview question across all the elite companies like Microsoft, Walmart, LinkedIn etc. Actually it is a very easy question as long as you know basics of Recursion and JavaScript Array function. To help you to answer this question in interview, I’m writing my answer.

![](https://miro.medium.com/v2/resize:fit:275/1*MG_5YY6zxhoDoeZ8c7S_xw.png)

Pic Credits: Dot net Paris

Question: Flatten array of Array

Input: \[1,\[2,3\],4,\[5,6,7\]\]

Output: 1,2,3,4,5,6,7

You can watch my Youtube video solving this problem in detail.

**Approach:**

- First thing that you have to think while answering this question is how to determine whether given array index is an array or not. In above given input arr\[1\] (\[2,3\]) is actually an array. This can be determined by using JavaScript’s built in function **Array**. **isArray().**
- After identifying whether given index contains array or not, if it is an array then recursively pass this array as input to the same function and traverse it first before going to next array index.

Now let’s write the working snippet.

```
let arr = [1,[2,3],4,[5,[6,7]]]
let output = ''
function flatten(arr) {
  for (let i = 0; i < arr.length; i++) {
    if(Array.isArray(arr[i])){
      flatten(arr[i])
    }else{
      output += arr[i]
    }
  }
  return output
}
console.log(flatten(arr))
```

Here I’m concatenating the numbers as a string, you can use an array and push all the values (Purely what output your interviewer is expecting).

That’s all about this article, you can get more such interview questions in my YouTube channel [UnCommon Geeks.](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos) . In case if you not already followed me on medium then please follow, you can follow me on Linked [Here](https://www.linkedin.com/in/vasanth-bhat-4180909b/). Do not forget to subscribe to my Youtube Channel [UncommonGeeks](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos).

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

[https://topmate.io/vasanth\_bhat](https://topmate.io/vasanth_bhat)
