---
id: '6984020701796065280'
date: '2022-10-07T05:24:52.138Z'
url: https://www.linkedin.com/posts/careerwithvasanth_google-amazon-youtube-activity-6984020701796065280-EpiF
likes: 37
comments: 1
---

One of the most common system design questions during #google  and #amazon  interviews is, Do you really know how #youtube  live commenting works during live streaming of the video ? Ex: News, Sports etc. 

Question looks simple but let me explain the complexities in it. 

1. Live streaming like news will be watched by 1000's of people and 100's of people will be commenting at every given second. What is the right strategy to fetch the comments from the server ?

2. You can do polling, where you can call the get comments API periodically, but what if there are no comments in that time ? then simply server resources are wasted. 

3. Now you might think of "Sockets". But sockets are used for two way connections like chatting. If you use sockets for commenting for the scale of Youtube, you will easily run out of server space. 

4. Now at least few will think of server sent events. It might work well for applications with limited scale. For products like #youtube  who have more than 2 Billion active users, it will not work. 

If you really know the right strategy to use on the #frontend  to fetch the live comments, please mention that in the comment section. I will check and evaluate it. 
In case you don't know, I have explained it very much in detail in my Youtube video in my channel "UncommonGeeks". Links to the channel are in the comment section. Please watch and give your feedback. 

In case if you have not followed me, you can do it here, I will help you to clear your frontEnd developer interview : Vasanth Bhat
