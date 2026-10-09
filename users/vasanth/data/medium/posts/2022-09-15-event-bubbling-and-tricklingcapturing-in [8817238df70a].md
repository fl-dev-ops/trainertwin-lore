---
id: 8817238df70a
title: Event Bubbling and Trickling/Capturing in JavaScript — Common interview question
url: https://careerwithvasanth.medium.com/event-bubbling-and-trickling-capturing-in-javascript-common-interview-question-8817238df70a
date: 2022-09-15
author: Vasanth Bhat
platform: medium


---

# Event Bubbling and Trickling/Capturing in JavaScript — Common interview question

![](https://miro.medium.com/v2/resize:fit:700/1*VciTFlQGDwPfjXiICLTpag.jpeg)

Say you have a basic HTML page where 3 div’s are nested and there is a click event associated with each div, (Refer example code below)

```
<html><body>
<div id="GrandParent" onClick="grandParentFunction()">      <h1>Grand Parent</h1>
     <div id="Parent" onClick="parentFunction()">             <h1> Parent</h1>
             <div id="child" onClick="childFunction()">              <h1> Child</h1>
            </div>
      </div>
</div><script src="./index.js" />
</body>
<html>
```

index.js contents

```
document.getElementById("GrandParent").addEventListener('click', () => {console.log("Grand Parent clicked")})document.getElementById("Parent").addEventListener('click', () => {console.log("Parent clicked")})document.getElementById("Child").addEventListener('click', () => {console.log("child clicked")})
```

Before reading further guess what will the output when you click on the child div ?

Whenever you click on the child div, internally you're also clicking the Parent and GrandParent div (as they are nested). So when you click on the child div, click events of Parent and Child will also be triggered. So the output will be

```
Child clicked
Parent clicked
Grand Parent clicked
```

Now in the same way guess what will be the output if Parent div is clicked ?

The output will be,

```
Parent clicked
Grand Parent clicked
```

Observe this output carefully, “child clicked” statement is not logged when you click on the Parent div. The reason is straight forward, when we click on Parent div, your not clicking on the block where child is present.

Similarly the output when you click on GrandParent div will be

```
Grand Parent clicked
```

If you observe the pattern how events are propagated, I,E when you click on child div, first click event associated with child is triggered and later with the parent and finally the grand parent. **Can you relate it to water bubbles that come out of a glass when you blow air into it. This process is called as event bubbling. You can also understand it as bottom up approach.**

What if you wanted the events to propogate in other way ? I,E when you click child div, first grand parent event triggered and then parent and lastly child event. The reverse of the above process, it is called **event trickling or Capturing**. Before demonstrating how to achieve it, you must ask a question to yourself **why there is a possibility of event trickling and capturing ?**

Earlier bubbling was only way to propagate events, for certain functionalities developers wanted event trickling, so browsers rather restricting users to a particular approach they gave a freedom to use both. By default most browsers, events are propagated in event bubbling fashion. addEventListener function takes second argument where we can specify events to bubble or trickle.

```
document.getElementById("GrandParent").addEventListener('click', () => {console.log("Grand Parent clicked")}, false)document.getElementById("Parent").addEventListener('click', () => {console.log("Parent clicked")}, false)document.getElementById("Child").addEventListener('click', () => {console.log("child clicked")}, false)
```

As you can see in the above code snippet, if you set the value to false, events will bubble from bottom to top, which is default behaviour which was saw at first. **So if you do not specify the second parameter then it is considered as false.**

**Event Trickling**

In Above example consider the same HTML and modify the JavaScript as shown below.

```
document.getElementById("GrandParent").addEventListener('click', () => {console.log("Grand Parent clicked")}, true)document.getElementById("Parent").addEventListener('click', () => {console.log("Parent clicked")}, true)document.getElementById("Child").addEventListener('click', () => {console.log("child clicked")}, true)
```

By setting the second argument to addEventListener method as true we are asking JavaScript browser to trickle the event. In this case if you click on the child div the output will be as shown below.

```
Grand Parent clicked
Parent clicked
Child clicked
```

And if you click on the Parent Div then the output will be,

```
Grand Parent clicked
Parent clicked
```

And lastly if you click on the grand parent div then output remains the same,

```
Grand Parent clicked
```

If you have understood the concept well, now try answering below question, what will be the output if you click on the child div.

```
document.getElementById("GrandParent").addEventListener('click', () => {console.log("Grand Parent clicked")}, false)document.getElementById("Parent").addEventListener('click', () => {console.log("Parent clicked")}, true)document.getElementById("Child").addEventListener('click', () => {console.log("child clicked")}, false)
```

I know it is little confusing the answer will be,

```
Parent clicked
Child clicked
Grand Parent clicked
```

That means priority is given for trickling and once all the events with trickling are triggered then bubbling events will get started. Try to nest more div’s and play with true and false argument to understand it better.

**Last question the interviewer will ask would be how to stop event propagation ?**

Click event has an argument called event, we can use that to stop propagating the event.

```
document.getElementById("GrandParent").addEventListener('click', () => {console.log("Grand Parent clicked")}, false)document.getElementById("Parent").addEventListener('click', () => {console.log("Parent clicked")}, false)document.getElementById("Child").addEventListener('click', (e) => {e.stopPropagationconsole.log("child clicked")}, false)
```

Now if you click the child the output would be just,

```
Child clicked
```

Event will not propagate further from that point. This can be added at any level, and from there, event will not be propagated.
