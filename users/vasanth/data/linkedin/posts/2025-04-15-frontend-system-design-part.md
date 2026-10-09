---
id: '7317791944619778048'
date: '2025-04-15T06:12:37.597Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontend-system-design-part-7-question-activity-7317791944619778048-k5dy
likes: 32
comments: 8
---

Frontend system design part - 7 

Question: You're building a social media application, which can contain textual and image posts. How to do it efficienctly. 

Explanation:

1. No, straight away compressing the image is not the right solution, as it will reduce the image quality thus user experience.

2. First make sure you have a system which provides device specific images. Ex: high resolution for browser and lower resolution for mobile. 

3. Try to have a version of image which is light weight which will load until the actual image is loaded. 

4. Using cdn/offline caching can also improve the image loading speed. 

5. After all of it, only if you think compression is needed, go for it. 

If you think, I have missed any points, mention that in the comments section.

follow me and I will help you to find your dream job: Vasanth Bhat
