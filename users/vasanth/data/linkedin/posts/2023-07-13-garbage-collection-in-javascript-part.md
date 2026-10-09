---
id: '7085133936552542209'
date: '2023-07-13T05:52:45.897Z'
url: https://www.linkedin.com/posts/careerwithvasanth_javascript-javascript-frontenddevelopment-activity-7085133936552542209-9wHp
likes: 26
comments: 0
images_count: 1
---

Garbage collection in #javascript Part 1:  Reference-counting garbage collection algorithm. This is the most naive garbage collection algorithm. This algorithm reduces the problem from determining whether or not an object is still needed to determining if an object still has any other objects referencing it. An object is said to be "garbage", or collectible if there are zero references pointing to it.

Below is the explanation for the attached screenshot. 

1. Initially X has a reference to an object.
2. Y=X will assign reference of X to Y. Thus the object has 2 references now.
3. X = 2 will remove one reference to an object.
4. y = 10 will remove the last reference to the object. 

Now the object has no reference and it can be cleared from the memory. Seems very straightforward right. But no modern browser uses it and official documentation calls this approach naive. Can you tell me why it is so in the comments section ?

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview : Vasanth Bhat

#javascript #frontenddevelopment #frontenddeveloper #frontendengineer #frontend #uidevelopment #uidesigners #webdevelopment
