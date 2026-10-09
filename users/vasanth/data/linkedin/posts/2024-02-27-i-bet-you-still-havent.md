---
id: '7168214935301206016'
date: '2024-02-27T12:06:59.569Z'
url: https://www.linkedin.com/posts/careerwithvasanth_javascript-interview-javascript-activity-7168214935301206016-DQ7D
likes: 88
comments: 8
images_count: 1
---

I bet you still haven't mastered the #javascript. This is one of the tricky #interview question that I have started asking recently for React JS/ JavaScript Developer openings. The right answer to this question is
"objectobject"

Explanation:
In #javascript, when you try to concatenate objects using the + operator, they are converted to strings. This conversion involves calling the toString() method on each object. Since both a and b are objects (not strings), their toString() methods are called, resulting in "[object Object][object Object]". Therefore, the output of console.log(a + b); will be "objectobject".

Now, if you want to modify the behavior so that the output becomes "HelloWorld" , how would you achieve that without directly manipulating the toString() method of the objects a and b?

Follow me and I will help you to find your dream job: Vasanth Bhat
#javascript #codesnippets #important #interviewquestions
