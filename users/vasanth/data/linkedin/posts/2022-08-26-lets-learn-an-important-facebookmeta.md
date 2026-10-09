---
id: '6968801958023368704'
date: '2022-08-26T05:31:00.872Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-interview-developer-activity-6968801958023368704-7dKS
likes: 62
comments: 2
---

Let's learn an important Facebook/Meta ReactJS/JS developer interview question today. 

Question 1 :
What is the return value of setTimeout() in JS

Answer: 
With my experience, still many struggle to answer this in the interview. But to answer the question it returns a numerical identifier for timeout, which can be used later to clear the timeout. 

Question 2: 
Can you write a function to clear all timeouts present in a screen. 

Junior developer answer (generally): 

There is a function called "clearAllTimeout()" you can use it to clear all the timeouts present in a screen. 

"In reality there is no function called clearAllTimeout()". So, if you're not sure about an answer, please don't say it in the interview. If you still want to guess, then say it like "I guess the answer could be". Otherwise it shows your foolishness. 

Good Answer: 
To clear all timeouts present in a screen first we need to know how many timeouts present in a screen. As I explained above, the setTimeout returns numerical value. Store that value in a global array and when the user leaves the page iterate that array and call clearTimeout() with the values.

"Best Answer:"
Above answer works good for Tier 2 / 3 companies but not for Meta/Facebook. They will expect some better solution for the same problem. I have tried explaining that in my Youtube video.  Link to the video is in the comment section, please watch it and give your feedback. 

In case if you have not followed me, you can do it here, I will help you to clear your frontEnd developer interview : Vasanth Bhat

#reactjs #interview #developer #frontenddeveloper #facebook #javascript
