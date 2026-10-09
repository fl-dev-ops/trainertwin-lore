---
id: '7163150157604233216'
date: '2024-02-13T12:41:22.467Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-interviewquestion-interviewexperience-activity-7163150157604233216-DXza
likes: 127
comments: 6
---

Cyclic dependency is one of the important ReactJS interview question and below is the explanation of it. Follow me and I will help you to find your dream job: Vasanth Bhat

Imagine we have two components: Parent and Child
// Parent.js
import React from 'react';
import Child from './Child';

function Parent() {
 return (
  <div>
   <h1>Parent Component</h1>
   <Child />
  </div>
 );
}
export default Parent;

// Child.js
import React from 'react';
import Parent from './Parent';

function Child() {
 return (
  <div>
   <h2>Child Component</h2>
   <Parent />
  </div>
 );
}
export default Child;

This creates a cyclic dependency, leading to a stack overflow error. To fix it, refactor by removing the dependency loop. Usually engineers make this mistake while using the utility function one inside the another. 
In case if you ever encountered this problem, mention how you solved it on comments section. 
#reactjs #interviewquestion #interviewexperience #interviews #interviewguidance
