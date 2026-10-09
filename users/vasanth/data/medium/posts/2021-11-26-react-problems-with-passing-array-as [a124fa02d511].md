---
id: a124fa02d511
title: React — Problems with passing array as a prop
url: https://mevasanth.medium.com/react-problems-with-passing-array-as-a-prop-a124fa02d511
date: 2021-11-26
author: Vasanth Bhat
platform: medium


---

# React — Problems with passing array as a prop

As you all know, properties which are shortly called as **props** is one of fundamental blocks of React. Props will allow you to pass the parameters between the components, they could be strings, numbers, object or arrays.

![](https://miro.medium.com/v2/resize:fit:700/1*NEW5IvXHXRCmneYGgPvDnA.jpeg)

Source- [https://unsplash.com/](https://unsplash.com/)

Here is the simple example of using the props.

```
import React from 'react'
import {View, Text} from 'react-native'export function Greetings(props){return (<Text>Hello {props.name}</Text>)}
export default function Home() {return (<Greetings name='meVasanth Medium blog readers' />)}
```

Home component is using Greetings component as a child component which takes name as the prop. If you execute this code output will be

```
Hello meVasanth Medium blog readers
```

> **How does react props works ?**

Many of you might have not asked this question while learning react. It will become very important, when you start working on a complex project and you face difficulty in understanding certain issues related to props (One mentioned in the article title).

Let me explain, how react props works. **In very simple words props behave the same way as arguments to a function. In the above example we can consider Greetings is a function that takes name as the argument and renders it wherever you use it.**

This explanation is very essential because everything works fine in case of **primitive** data types (Integers, string and boolean). But when you pass **reference** **types** as props, you start facing few unwanted scenario’s.

Let’s consider below example; Home.js is having two props Child1 and Child2 and both take user array as a prop. Child1 modifies the array and renders the items, where as child2 just renders the items.

> **Home.js**

```
import React from 'react'import {View} from 'react-native'import Child1 from './Child1';import Child2 from './Child2';export default function Home() {const user = [{name: 'User 1'},{name: 'User 2'},{name: 'User 3'}]return (<View><Child1 userDetails={user}/><Child2 userDetails={user}/></View>)}
```

> **child1.js**

```
import React from 'react'import { View, Text } from 'react-native';export default function Child1({userDetails = [{}]}) {userDetails.forEach(item => {item.name =  ' Test Name' + item.name})return (<View><Text>Child 1</Text>{userDetails.map(item => {return (<View><Text>{item.name}</Text></View>)})}</View>)}
```

> **child2.js**

```
import React from 'react'import { View,Text } from 'react-native';export default function Child2({userDetails = [{}]}) {return (<View><Text>Child 2</Text>{userDetails.map(item => {return (<View><Text>{item.name}</Text></View>)})}</View>)}
```

Try to guess the output ?

Ideal expectation is, Child1 should render all the names with **Test Name** prepended to it and Child2 should render all the names as it is in the array.

**But What happens is both Child1 and Child2 will render the names prepended with Test Name.**

Since, now you’re aware how the props actually work inside React, you can guess why this is happening. As we are passing same array reference to both the props, changing values in one component is affecting the other.

> **How to solve this problem**
>
> **Solution 1**

In the above snippet, we have made a mistake of modifying the props sent to a component. One of the unsaid rules about using props is do not modify it inside a component. If you have to perform some changes to the props, then make a copy of it inside the component.

For example:

Create a state variable inside Child1 and modify that state variable.

```
import React, { useEffect, useState } from 'react'import { View, Text } from 'react-native';export default function Child1({userDetails = [{}]}) {const [userInfo, setUserInfo] = useState([])useEffect(() => {const temp = []for (let i = 0; i < userDetails.length; i++) {temp.push({name: 'Test Name' + userDetails[i].name})}setUserInfo(temp)}, [])return (<View><Text>Child 1</Text>{userInfo.map(item => {return ( <View>    <Text>{item.name}</Text> </View>)})}</View>)}
```

If list contains less data then this approach works fine. But, Problem occurs when list is very big. In that case this will increase the memory used during the run time.

> **Solution 2**

**Deep copy —** Rather sending same reference to both the components we can send unique reference to each component. This will solve the problem. You can create deep copy either using

1. [**Loadash library**](https://www.npmjs.com/package/lodash)— I recommend this approach because loadash is popular library, their way for deep copying is less CPU intensive and it is used in many popular applications.
2. **JSON.parse(JSON.stringify(user))**— This works fine when list contains less number of items and list doesn’t contain function calls. If contains function call then this approach will fail.

There are multiple other approaches that can also be followed to avoid this problem. If you’re aware of any such approach please do mention it in the comments.

Happy reading ..
