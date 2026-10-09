---
id: '7175741113163522050'
date: '2024-03-19T06:33:20.201Z'
url: https://www.linkedin.com/posts/careerwithvasanth_javascript-javascript-latest-activity-7175741113163522050-8CIw
likes: 130
comments: 5
---

ES15 is out and here are new features that you need to be aware. A lot of JavaScript developers still think ES6 is the latest #javascript version 😁, but ES15 is already out in 2024.

1. Well-formed Unicode Strings:  str.toWellFormed('ab\uD83D\uDE04c
') = "abEc" 

2. Await outside async block: Now you can wait on top of your module till an API call is successful.

3. Pipeline operator:  This will increase your code readability: 

// Without pipeline operator
const sentence = "hello world";
const capitalizedSentence = sentence.toUpperCase().split('').reverse().join('');

// With pipeline operator
const capitalizedSentence = "hello world"
 |> str => str.toUpperCase() // Convert to uppercase
 |> str => str.split('') // Split into array of characters
 |> arr => arr.reverse() // Reverse the array
 |> arr => arr.join(''); // Join the array back into a string

Records and Touples, decorators, Atomic waitSync are other major features that are rolled out. Pipeline operator is my favourite. Let me know what is your favourite feature in ES15 ??

Follow me and I will help you find your dream job: Vasanth Bhat

#javascript #latest #update #newfeatures #whatsnew #whatsnext
