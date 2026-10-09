---
id: '7182240642704531457'
date: '2024-04-06T05:00:08.799Z'
url: https://www.linkedin.com/posts/careerwithvasanth_javascript-typescript-programming-activity-7182240642704531457-j5zn
likes: 34
comments: 2
---

What is the difference between interfaces and types in JavaScript ?
Types define the structure and attributes of data, whereas interfaces outline contracts for behavior.
-------------------------------------------------------------------------------
type Person = {
 name: string;
 age: number;
};

interface Greetable {
 greet(): void;
}
-------------------------------------------------------------------------------
Here, Person is a type specifying attributes, while Greetable is an interface declaring a greet() method all implementing classes must have.
Key Differences:

Purpose:
Types specify data structures.
Interfaces declare behavior contracts.

Implementation:
Types represent concrete data.
Interfaces are abstract and define expected behavior.

Extensibility: 
Types have limited extensibility.
Interfaces can be extended by multiple classes.

Did you knew these differences ? if you know any other difference mention it on the comments section. 

Follow me and I will help you to find your dream job: Vasanth Bhat

#javascript #typescript #programming #challenges
