---
id: '6967351923003850752'
date: '2022-08-22T05:29:05.583Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-javascript-interview-activity-6967351923003850752-WpuJ
likes: 38
comments: 8
---

Let's learn an important ReactJS/JS interview question today. 

Question: Guess the output of below snippet. 
 
for (var i = 0; i < 3; i++) {
    setTimeout((function() { 
      console.log(i) 
    })(), 1000 * i);
  }

Looks like a classic problem, but it has a small variation. Instead of having regular function inside the setTimeout here we have self invoking function or IIFE(Immediately Invoked Function Expression).  

Answer: 
I will tell the answer for above question, when you run the code it will display, "0, 1, 2"  immediately. 

Brain teaser: 
As you all know whenever JS engine encounters setTimeout it will take it from call stack moves it to Web API (event loop concept). Then how come function inside the setTimeout is triggering immediately ?? 
Can you  try explaining what is happening under the hood in the comment section ? 

If you're not sure, you can watch my Youtube video, where I have explained it in detail. Link to My channel "Uncommon Geeks" that contains the video is in the comment section. 

If you have not followed me on LinkedIn, you can do it here: Vasanth Bhat

#reactjs #javascript  #interview #frontend #frontenddeveloper #javascript
