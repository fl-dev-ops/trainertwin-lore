---
id: 282b93e535e1
title: 90% Will Fail to Solve This Facebook Interview Question
url: https://careerwithvasanth.medium.com/90-of-you-will-fail-to-answer-solve-this-facebook-interview-question-part-1-282b93e535e1
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

After researching a lot on the web, I came to the conclusion that there is no tutorial/video series that is dedicated to MAANG (Meta, Apple, Amazon, NetFlix, Google) preparation for frontend developers.

So, I decided to decode the most common interview questions of MAANG on my YouTube channel. In this article, I will discuss a very interesting problem. So, read on till the end.

Facebook interview question solved

Question

Add two really big numbers which are in the form of string and return the result in the form of String.

The company where the question was asked : Facebook/ Meta

Ex:

Sample Input:

“99999999999999999999999999999” + “1”

Sample Output

“100000000000000000000000"

Usual Approach

Most of you will think it is an easy question and can be solved with below code snippet.

function addNumbers(num1, num2){
return Number(num1) + Number(num2)
}
console.log(addNumbers("99999999999999999999999999999", "1"))

Unfortunately, this solution will not work. If you run the above code the output will be like this: 1e+29.

In case this is the first time you saw this expression, then half of your confidence will be lost in the interview. Let me help you to decode what this means.

1e+29 stands of 10²⁹ (1 * 10 power 29). Which is actually the right answer to adding the above two numbers. But interviewer expects output as 100000000000000000000000.

There are two main ways to achieve the solution to this, I will discuss one solution in this part and the next solution in the other part.

Solution 1: Using BigInt

Definition of BigInt

“BigInt is a primitive wrapper object used to represent and manipulate primitive bigint values — which are too large to be represented by the number primitive.”

The definition says it all: when a number cannot be represented in the form of a number due to its larger length, then we can use BigInt as an alternative to that.

Code snippet with solution

function addNumbers(num1, num2){
return BigInt(num1) + BigInt(num2)
}
console.log(addNumbers(“99999999999999999999999999999”, “1”))

Output will be: 100000000000000000000000000000n

The ’n’ at the end here refers to a BigInt.

But the interviewer will not expect you to write this solution as you’re using a built-in method to solve the problem. Instead, their expectation will be for you to solve this problem on your own. That will be discussed in the second part of this article, without fail please read that.

Thank you for reading catch you in the next article. In case if you not already followed me on medium then please follow, you can follow me on Linked Here. Do not forget to subscribe to my Youtube Channel UncommonGeeks.

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

Book a time with Vasanth on topmate.io

Simplifying personalised interactions for the world's leading minds

topmate.io

If you’re preparing for a frontend developer interview, please watch the below series of mine:

If you want to learn JavaScript custom implementations of built-in methods, then watch the below series of mine:

More content at PlainEnglish.io . Sign up for our free weekly newsletter . Follow us on Twitter and LinkedIn . Check out our Community Discord and join our Talent Collective .
