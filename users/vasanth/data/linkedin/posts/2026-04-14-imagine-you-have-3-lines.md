---
id: '7449690958629183488'
date: '2026-04-14T05:32:13.102Z'
url: https://www.linkedin.com/posts/careerwithvasanth_imagine-you-have-3-lines-of-code-consolelog-activity-7449690958629183488-A9ms
likes: 15
comments: 3
images_count: 1
---

Imagine you have 3 lines of code 

console.log("1")
setTimeout(()→{}, 2000)
console.log("3")

how call stack executes this ? 

most common answer 

1. First console.log goes into call stack 
2. Then setTimeout gets into webAPI section 
3. Then 3rd console.log is pushed into call stack. Then call stack execution starts. 

if so, then we will print 3 first followed by 1 right ? many candidates get confused here. 

In reality: call stack is a stack to track the order of the function execution. Function 1 calling function 2 and it calling 3, there is a need for traceability and call stack provides that.  

now tell me, how above 3 lines are executed within callstack ? 

follow me and I will help you to find your dream job: Vasanth Bhat
