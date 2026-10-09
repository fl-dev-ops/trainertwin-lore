---
id: '7201454625529487360'
date: '2024-05-29T05:29:39.283Z'
url: https://www.linkedin.com/posts/careerwithvasanth_typescript-webdevelopment-reactjs-activity-7201454625529487360-w9Z5
likes: 50
comments: 13
---

Let me discuss an important TypeScript problem today !! let me see, how many of you can give the right answer.

********************************************************************************
interface userInformation {
         name: string; 
         id: number;
         age: number;
}

const user: userInformation = {
      name: 'test',
      id: 100
     age: 30
}
********************************************************************************
Question: Delete the id property from 'user' object. 
Answer 1: delete user['id'] 

This will surely delete the id property but you will get a typescript warning "The operand of delete operation must be optional". Which means as id is a mandatory property of userInformation you cannot delete it. 
********************************************************************************
Here goes the answer 2: Using spread operator

const { id, ...userWithoutId } = user;

This will create a new object userWithoutId excluding the id property. This will also work but you will get a TypeScript warning property id defined but never used. 
********************************************************************************

Now you tell me, without modifying the typescript rules, how to delete a property from an object ??

Follow me and I will help you to upskill to find your dream job: Vasanth Bhat

#typescript #webdevelopment #reactjs #javascript #interview #question
