---
id: '7322489011938168832'
date: '2025-04-28T05:17:05.713Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-13-question-activity-7322489011938168832-MxEi
likes: 34
comments: 13
---

Frontend system design part - 13 

Question: Why Javascript's event loop has stack ? 

explanation 

console.log("hello")
SetTineout // for 3 seconds 
console.log("world")

if I run this code, most common event loop explaintion is, first, console.log is pushed into call stack, SetTineout goes into web api followed by call back queue. Last console.log also moves to call stack and then execution starts from call stack.

But, if you know how stack works, it's last in first out (LIFO) in that case, 'world' will be printed before 'hello' right ? 

but, output will be 'hello' followed by 'world'
why is it ? mention you're answer in the comments section.

follow me and I will help you to find your dream job: Vasanth Bhat
