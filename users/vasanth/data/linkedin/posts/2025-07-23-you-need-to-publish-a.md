---
id: '7353659225971068928'
date: '2025-07-23T05:36:23.853Z'
url: https://www.linkedin.com/posts/careerwithvasanth_you-need-to-publish-a-new-update-on-banking-activity-7353659225971068928-WC4t
likes: 34
comments: 2
---

You need to publish a new update on banking application, without affecting any of the existing transaction.
This was the Question asked to me in the system design interview.

answer:

1. Most single page applications are already loaded on the client.
2. Unless user refresh the screen, the downloaded resources will be used. 
3. So, even if it's a banking application and you're in middle of transaction and ui bundle is updated, you don't see a problem.

But, backend APIs should be downward compatible. 

There is an interesting concept associated with this, can you tell me what is "cache bursting" in the comments section. 

follow me and I will help you to find your dream job: Vasanth Bhat
