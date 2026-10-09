---
id: '7320321315863687169'
date: '2025-04-22T05:43:26.695Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-11-lets-activity-7320321315863687169-I_Cv
likes: 33
comments: 5
---

Frontend system design part - 11 

Let's say you have a system like Google drive where a folder is shared and multiple people can upload content at once. So, there is a chance of duplication. How to solve this problem? 

Answer: 
1. When a person is uploading the content, capture all the meta data associated with it. Ex: Media type, size etc. 

2. The best way to check whether data is same or not is using bit by bit comparison. 

3. So, once after content is uploaded successfully, compare it with all the data that has matching meta data and maintain only one file and remove the duplicate.

4.  To optimise it further, comparison can start during the upload itself.

There is one major problem with my solution above ! if you know what that is, then mention it in the comments section. 

follow me and I will help you to find your dream job: Vasanth Bhat
