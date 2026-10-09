---
id: '7325034883435630592'
date: '2025-05-05T05:53:28.778Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-13-question-activity-7325034883435630592-oGXb
likes: 54
comments: 6
---

Frontend system design part - 13

Question: How to show where you left ? on streaming platforms like youtube, netflix etc.

Explanation: Easiest way to implement it is by making an api call periodically to save the video id and watched duration aginst the user id. 

But his can be optimised further on client by catching the time stamp. Periodically, save the timestamp locally first, followed by saving it on server. Next time when user opens the video make an api call first and wait for the result to get the updated timestamp. If it is delayed then use the local timestamp for faster experience.

When you used the local timestamp do not update the server with latest watched timesmap. 

what do you think ? do you have a better solution for this ? 

Follow me and I will help you to find your dream job: Vasanth Bhat
