---
id: '7315243289186578433'
date: '2025-04-08T05:25:10.790Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-question-pt-4-question-activity-7315243289186578433-eE2J
likes: 51
comments: 13
---

Frontend system design question pt-4 

Question: How do you handle auto complete scenario where result for first string comes later and result of 3rd string comes first. 

Ex: let's say you searched 'ab' and api call happend then you entered 'abcd' and api call is made. What if abcd result comes quicker than 'ab' ? 

If you show the result then it is invalid, how to handle this scenario ?

Solution 1: Abort old request when a new request is made (but it is not optimal approach as there is no true api request abort) 

Solution 2: Pass time stamp with the request and maintain a local value for recent timestamp and consider only those requests with most recent timestamp. 

Solution 3: You should tell me ! which optimal then solution 1 and 2 in the comments section.

Follow me and I will help you to find your dream job: Vasanth Bhat
