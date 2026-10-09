---
id: ff4011afb27a
title: Don’t skip | Top 5 ReactJS Interview topics and detailed solution
url: https://careerwithvasanth.medium.com/dont-skip-top-5-reactjs-interview-topics-and-detailed-solution-ff4011afb27a
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

# Don’t skip | Top 5 ReactJS Interview topics and detailed solution

With my experience of taking interviews to hundreds of candidates, many ReactJS developers still don’t know what all topics to prepare for the interview. They are all good developers, if you ask them to build beautiful websites or mobile applications, they will be able to build it in a short duration. But they will not be strong conceptually. So, I decided to list all the most common interview questions of ReactJS developer interviews with some example snippets.

If you’re too bored to read, you can watch my video on Youtube here. If you have not subscribed to my channel, please subscribe and let me know what you think about my video in the comment section. You can also continue to read the article below.

![](https://miro.medium.com/v2/resize:fit:700/1*--2F9EVGqXqzhEyrDotc3A.png)

Complete ReactJS interview topics discussed

> _Core topics to prepare for ReactJS developer interview_

1. Reconciliation
2. Class V/S Functional component
3. Hooks
4. Pure Components
5. HOC

> Reconciliation

As per react’s official [documentation](https://reactjs.org/docs/reconciliation.html) “React provides a declarative API so that you don’t have to worry about exactly what changes on every update. This makes writing applications a lot easier, but it might not be obvious how this is implemented within React. This article explains the choices we made in React’s “diffing” algorithm so that component updates are predictable while being fast enough for high-performance apps.”

**In simple words, React maintains a copy of real DOM called Virtual DOM. Whenever there is a change in the UI, another copy of Virtual DOM is created and it is compared with the original Virtual DOM and changes are reflected on the real DOM.**

> Class V/S Functional component

This question has lost its significance as a deciding factor in the interview. But this question is asked just to understand how long you’re using ReactJS. Are you aware of both class and functional components or not ?

Read this beautiful article of [GeeksForGeeks](https://www.geeksforgeeks.org/differences-between-functional-components-and-class-components-in-react/) to know more about it.

> Hooks

Hooks are a new addition in React 16.8. They let you use state and other React features without writing a class. In simple words it will make functional components stateful and give re-rendering capabilities.

There are two main types of questions asked on hooks

1.  **Questions on various different types of hooks:** This interviewer will ask you to give examples for different hooks like useMemo, useLayoutEffect, useCallback etc. Generally those hooks which you don’t use on a day to day basis but are very important from a performance perspective will be asked in the interview.
2.  **Building Custom hooks:** Interviewer might give you a scenario and ask you to build a custom hook for the same. Ex: Implement a counter hook with increment, decrement, reset capabilities which also returns current counter value. Below is a complete code for the same, for explanation you can watch my [Youtube video here.](https://www.youtube.com/watch?v=o22KRrxab18)

```
import { useState } from 'react';import './App.css';const useCounter = (initialValue) => {const [count, setCount] = useState(initialValue);const increment = () => setCount(count + 1);const decrement = () => setCount(count - 1);const reset = () => setCount(initialValue);return {count, increment, decrement, reset}}function App() {{/* Use counter example code */}const {count, increment, decrement, reset} = useCounter(0)return (<div className="App">{/* Use counter example code */}<h1>{count}</h1><button onClick={increment}>increment</button><button onClick={decrement}>decrement</button><button onClick={reset}>reset</button></div>);}export default App;
```

> Pure Components

These are the components which do not re-render as long as the state, props passed to it are not changed. You can use them to avoid re-rendering.

Let’s look at a simple working snippet below. for explanation you can watch my [Youtube video here.](https://www.youtube.com/watch?v=o22KRrxab18)

**App.js**

```
import { useEffect, useState } from 'react';import './App.css';import Parent from './Parent';function App() {// Pure component sectionconst [id, setId] =  useState(1);const [salary, setSalary] =  useState(1000);const [age, setAge] =  useState(30);useEffect(() => {setInterval(() => {console.log('Inside setInterval');setId(id + 1);}, 1000);})return (<div className="App">{/* Pure component example */}<Parent id={id} salary={salary} age={age}/></div>);}export default App;
```

**Parent.js**

```
import React from 'react'import PureComponent from './PureComponent'export default function Parent({id, salary, age}) {console.log('Inside parent component');return (<div><h1>Id is: {id}</h1><PureComponent salary={salary} age={age}/></div>)}
```

**PureCompoennt.js**

```
import React from 'react'function PureComponent({salary, age}) {console.log('Inside Pure Component ');return (<div><h1>Inside Pure component</h1><h2>salary: {salary}</h2><h2>age:{age}</h2></div>)}export default React.memo(PureComponent);
```

> HOC: Higher order component

HOC’s are the components that take components as an input and return mostly components as output.

Let’s look at a simple working snippet below. for explanation you can watch my [Youtube video here.](https://www.youtube.com/watch?v=o22KRrxab18)

**App.js**

```
import './App.css';import Container from './Container';import Hello from './Hello';function App() {// HOCconst SampleComponent = Container(Hello);return (<div className="App"><SampleComponent /></div>);}export default App;
```

**Container.js**

```
const Container = (Component) => {return () => (<div><h1>Inside HOC</h1><Component /></div>)}export default Container;
```

**Hello.js**

```
import React from 'react'export default function Hello() {return (<div>Welcome to Uncommon geeks</div>)}
```

Thank you for reading catch you in the next article. In case if you not already followed me on medium then please follow, you can follow me on Linked [Here](https://www.linkedin.com/in/vasanth-bhat-4180909b/). Do not forget to subscribe to my Youtube Channel [UncommonGeeks](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos).

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

[https://topmate.io/vasanth\_bhat](https://topmate.io/vasanth_bhat)

If you’re preparing for a frontend developer interview, please watch the below series of mine:

If you want to learn JavaScript custom implementations of built-in methods, then watch the below series of mine:
