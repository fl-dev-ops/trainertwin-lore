---
id: '7089473294780796928'
date: '2023-07-25T05:15:49.520Z'
url: https://www.linkedin.com/posts/careerwithvasanth_javascript-javascript-javascript-activity-7089473294780796928-3_fI
likes: 43
comments: 1
---

Hoisting is not real. And why should you care? According to me, variable hoisting could be one of the most useless features of #javascript. Unlike most, the concept of hoisting itself is not real. Variable declarations do not move to the top of the block. Because of 2 step execution it just appears to move to the top of the block.

1. Variable declared with 'var' keyword is hoisted and value initialised in undefined. So far, I never encountered a scenario where I used this feature.

2. Variables declared with let and const are hoisted but they are in a temporary dead zone. Whichever the zone they are in nutshell you cannot use it. So, hoisting did not provide any advantage here ?

3. Function hoisting is essential in #javascript is not class based language. To call a function from the line even before the function is declared function hoisting is necessary.

FYI: As Brenden Eich(creator of JavaScript) once said on twitter "var hoisting was thus [an] unintended consequence of function hoisting, no block scope, [and] JS as a 1995 rush job."

Let me know, if you ever encountered any advantage of variable hoisting in #javascript in the comments section.

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview : Vasanth Bhat
#javascript #frontenddevelopment #frontendengineer #frontend #frontenddeveloper #reactjs #reactdeveloper
