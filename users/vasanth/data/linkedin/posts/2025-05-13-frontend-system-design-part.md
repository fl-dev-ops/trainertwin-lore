---
id: '7327929617997058049'
date: '2025-05-13T05:36:07.279Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-15-question-activity-7327929617997058049-UTX-
likes: 26
comments: 3
---

Frontend system design part - 15 

Question: Streaming applications like youtube, how do they effectively play the video on change of the network speed ? 

explanation: 
1. During the start of the video playing few seconds of video is already buffered. 
2. Continuously an observer keeps track of network speed. 
3. As and when it changes, in accordance to that, the best quality portion of the video is fetched. 

Ex: If you're in 100mbps network speed then a high quality video is surfaced. If you're speed reduced to 10mb, lower quality video is surfaced. 

mention in comments section, how does backend is able to provide videos of different resolution?

follow me and I will help you to find your dream job: Vasanth Bhat
