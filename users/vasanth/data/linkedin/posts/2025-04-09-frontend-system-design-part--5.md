---
id: '7315610859358117888'
date: '2025-04-09T05:45:46.348Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-5-question-activity-7315610859358117888-Ivsx
likes: 60
comments: 8
---

Frontend system design part -5 

Question: Which is the right place to save the thirdy party API keys.

Answer: Most common answer is saving it on env file and not saving it on code directly. Even senior developers say this, then I ask surely it's not a part of code base but isn't it part of the bundle and surfaces to client ? 

At this time, people gets confused and don't know what to answer. The right technique with slight additional delay is having an orchestration layer that will give the API keys. First and api call is made to that layer to get all the tokens. 

Even this approach has a problem, let me know what is that in the comments section. 

follow me and I will help you to find your dream job: Vasanth Bhat
