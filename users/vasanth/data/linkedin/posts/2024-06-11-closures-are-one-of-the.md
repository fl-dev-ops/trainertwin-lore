---
id: '7206166379530506240'
date: '2024-06-11T05:32:28.977Z'
url: https://www.linkedin.com/posts/careerwithvasanth_javascript-interview-careerwithvasanth-activity-7206166379530506240-gSlz
likes: 44
comments: 6
---

Closures are one of the most important #javascript #interview topics, despite the topics looks very easy, it's not always easy to answer all the questions. Ex: the snippet below, if you know the answer mention it with the right explanation in the comments section. 
*******************************************************************************
function createCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

const counter1 = createCounter();
const counter2 = createCounter();

console.log(counter1()); 
console.log(counter1()); 
console.log(counter2()); 

********************************************************************************
If you don't know the answer or unsure of explanation watch my latest video on YouTube channel #careerwithvasanth.  "Top 10 JavaScript Developer interview questions and answers " (Link in the comments section).

Follow me and I will help you to up-skill in frontend and help in finding your dream job: Vasanth Bhat

#frontend #interview #important #questions #answers #javascript
