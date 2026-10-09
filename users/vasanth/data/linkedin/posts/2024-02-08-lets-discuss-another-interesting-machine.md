---
id: '7161236926149103616'
date: '2024-02-08T05:58:52.542Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-reactnative-angular-activity-7161236926149103616-yVF-
likes: 48
comments: 5
---

Let's discuss another interesting machine coding question today in #reactjs / #reactnative / #angular 
Implement a function that takes one or more values and returns a function that cycles through those values each time it is called.

Examples
const helloFn = cycle('hello');
console.log(helloFn()); // "hello"
console.log(helloFn()); // "hello"

const onOffFn = cycle('on', 'off');
console.log(onOffFn()); // "on"
console.log(onOffFn()); // "off"
console.log(onOffFn()); // "on"

Solution: 
export default function cycle(...values) {
  let index = 0;
  return () => {
    const currentValue = values[index];
    index = (index + 1) % values.length;
    return currentValue;
  };
}

If you understand the question and answer, mention it on the comments section. 
Follow me and I will help you to clear your interview: Vasanth Bhat

#reactjs #react #reactnative #reactnativedeveloper #uidesigner #uidevelopment
