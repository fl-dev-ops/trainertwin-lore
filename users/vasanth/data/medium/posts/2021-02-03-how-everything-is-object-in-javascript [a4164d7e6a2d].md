---
id: a4164d7e6a2d
title: How everything is Object in JavaScript ?
url: https://careerwithvasanth.medium.com/how-everything-is-object-in-javascript-a4164d7e6a2d
date: 2021-02-03
author: Vasanth Bhat
platform: medium


---

We hear this a lot, everything is object is in JavaScript, okay, well, how you saying that ? how to prove everything (like function, array, class and variables) is Object in JavaScript ? Let’s get started with simple example.

Open your favourite browser (mine is Chrome) open inspect window(ctrl+shift+i is the shorcut on windows) and click on console. And create an array like the screenshot shown below.

Observe the Image carefully, we just created an array named arr and in the next line if we type arr followed by a “.” then we are listed with set of functions which can be used with the arrays like map, concat, length etc.

Wait a minute, how did all came ? every JavaScript developer with basic knowledge is using array and it’s methods everyday, but we have just created Array and how all these functions are made accessible to it ?

Answer is Prototype: All JavaScript programming constraints inherit properties and methods from a prototype.(A detailed article on prototype and prototypal inheritance is written by me in this link)

whenever we create array, function, class etc, JavaScript takes the Prototype methods of it and creates and object named __proto__ attaches it with object.

So if you try to log arr.__proto__ output will look like below.

Array was able to access methods like push, length, find etc because of this. What do we get if we try to print Array.Prototype?

The output would be same as above. That means, any array that you create in JavaScript will inherit values from Array.prototype.

This is fine, but where we got explanation for everything is Object in JavaScript ? Below is explanation for same.

If you observer carefully in above two screenshots the last parameter is __proto__. In first image we logged arr.__proto__ which has a __proto__ property within it. Let’s try logging the value of it.

Observe the constructor here, it is an object, that means Array’s prototype was derived from the Object’s prototype. What will be objects’s prototype then ? that is a.__proto__.__proto__.__proto__

the answer would be null. This is why everything is object in JavaScript. All the programming constraints like function, class, Arrays are derived from the Object’s Prototype.

Just to elucidate further consider below example with functions.

Even functions are derived from Object prototype this applies to all programming constraints of the JavaScript. Hope this clears most basic question, why everything is object is JavaScript.

Related Articles

Prototype and Protypal Inheritance in JavaScript
