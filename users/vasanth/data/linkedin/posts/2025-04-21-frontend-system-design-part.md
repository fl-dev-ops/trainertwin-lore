---
id: '7319952989031403520'
date: '2025-04-21T05:19:50.735Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-10-question-activity-7319952989031403520-qa9Q
likes: 163
comments: 13
---

Frontend system design part - 10 

Question: How to create infinite scrolling on your web application? 

Explanation: 
Most common answer is I will introduce pagination and call API at the end of each page. 

Expected answer:

1. You need to understand the frequency of data updation. 

2. If it is too frequent then you should chose cursor based pagination, if not you can use offset based pagination. 

3. If the content of the page contains images and other media then you need to implement efficient loading of it. 

4. You shouldn't make API call when you hit the end of the page. Instead you should make api call when user scrolls 60% of the page. 

let me know in comments section, how will you cache the complete contents of the page ? so that, when you open the page next time, you can load it quickly.

follow me and I will help you to find your dream job: Vasanth Bhat
