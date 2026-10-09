---
id: '7312712827251671041'
date: '2025-04-01T05:50:01.651Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-scenario-driven-questions-pt-activity-7312712827251671041-IU3U
likes: 84
comments: 9
---

Frontend scenario driven questions : Pt - 1

Question: How do ensure a user never logs off from a website? 

Answer: If there is only one token then, when that is expired, user needs to logout and login. 
so, there should be 2 tokens, authorisation and access token. Usually acces token will have a short period of expiry and auth token will have a long period of expiry. 
When auth token is expired client will refresh it by passing access token. This way user sessions are kept longer. 

In comments mention, how to handle the scenario when the access token is also expired ? 

Follow me and I will help you to find your dream job: Vasanth Bhat
