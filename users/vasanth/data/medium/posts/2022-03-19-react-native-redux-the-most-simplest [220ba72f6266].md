---
id: 220ba72f6266
title: React Native — Redux, the most simplest explanation
url: https://mevasanth.medium.com/react-native-redux-the-most-simplest-explanation-220ba72f6266
date: 2022-03-19
author: Vasanth Bhat
platform: medium


---

# React Native — Redux, the most simplest explanation

![](https://miro.medium.com/v2/resize:fit:700/1*Fns3l_JVkTMtX6cO2wpSXA.jpeg)

If you’re reading this article, then you want to know about Redux in React Native and already read few blogs and watched some youtube videos but still things are not clear for you !!

Don’t worry I was also in the same place some months back when I first tried understanding the Redux, definitely it is not a complicated topic, but difficult to grasp at one go. And examples on the internet are quite complex to understand for the beginner. So I will create a simplest example so that you will understand it very clearly.

First thing first the terminologies

1.  **Action** — An action that you want to perform, example login user, get posts from API etc. Basically it is just a variable generally created with const keyword. Ex: **const INCREMENT\_COUNTER = “INCREMENT\_COUNTER”.**
2.  **Action Creator —** An Arrow function that creates the action. This is required because sometimes actions cannot be just variable, some additional details might be associated with it.
3.  **Reducer —** Is a pure function which takes current state and action as input and returns the updated state. Most of the state management logic happens here.
4.  **Store —** In simple words is the container that contains the entire state of the Application.
5.  **useSelector (Hook) —** This hook is used to subscribe to the state changes which can be used later for either rendering or for some other process.
6.  **useDispatch (Hook) —** Used to dispatch the actions. You will be passing the action creator along with it, so that the required action can be performed. Ex: If you dispatch **INCREMENT\_COUNTER** action **,** then the state variable having count value will be updated.

Now let’s get started, All the terminologies that I explained above will be used in the below example.

1.  **Creating the project (I assume your using the react-native CLI, if your using expo, just refer expo documentation** [here](https://docs.expo.io/workflow/expo-cli/) **, for the commands. )**

```
react-native init Redux_pracice (execute this command on terminal at your convenient directory)
```

2\. Change directory to newly created project

```
cd Redux_pracice
```

2a. Install redux and react-redux, these 2 packages are required to use redux inside react.

```
npm install redux react-redux
```

3\. Remove all the default contents from the App.js and retain the contents as shown below.

```
import React from 'react';import { createStore, combineReducers } from "redux";const store = createStore(rootReducer);export default App = () => {return ();};
```

Now lets start with actual redux implementation.

4\. Create a folder named **store** at the root directory.

5\. Create a folder named **actions, reducers** inside it

6\. In actions folder create a file named **modifyCounter.js,** and below are the contents of the action creator.

```
export const INCREASE_COUNTER = "INCREASE_COUNTER"; //Actionexport const DECREASE_COUNTER = "DECREASE_COUNTER"; //Actionexport const incrementCounter = () => { //Action Creatorreturn {type: INCREASE_COUNTER}}export const decrementCounter = () => { //Action Creatorreturn {type: DECREASE_COUNTER}}
```

As explained above, here we have two actions, one is INCREASE\_COUNTER and other is DECREASE\_COUNTER and two action creators named incrementCounter, decrementCounter. In this case action creator is having just type property, but in your real time project you may have many properties which you may need to associate with the action. Depending on that add the properties.

**Note: Having action creator is not compulsory !! just action is sufficient to perform the state management, but it is recommended to have action creator, as in future if any new property comes along with action, changes will be minimum.**

7\. Inside **reducer** folder create a file named **modifyCounter.js** and add below code.

```
import { DECREASE_COUNTER, INCREASE_COUNTER } from "../actions/UpdateCounter";
// Previously created actions are imported hereconst initialState = {count: 0}//reducer named modifyCounterReducer is created below.const modifyCounterReducer = (state = initialState, action) => {         switch (action.type) {             case DECREASE_COUNTER:                 let previousCount = state.count;                 previousCount--;                 return {...state, count: previousCount}             case INCREASE_COUNTER:                let nextCount = state.count;                nextCount++;                return {...state, count: nextCount}           default:              return state        }}export default modifyCounterReducer
```

In above modifyCounterReducer, a reducer function, we are taking current state and action as input and returning the new state as output. Here we are switching the action.type and incrementing or decrementing the count depending on that.

Observe the state change carefully here, we read the current state from the state variable and increment or decrement it and later return the updated value. Important thing to observe here is, the state itself is not modified, the variable **initialState** is the actual state of the application. We take it as an argument to function and modify the argument. Because of this **states are immutable in redux. Also we can debug the redux state change using** [**redux-devtools**](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=en) **chrome extension, only because we are not modifying the actual state.**

Now we are completed most important steps and left with creating store, and modifying the state of the Application.

8\. Create a folder named **screens/home.js** at the root hierarchy. And below should be the content of it.

```
import React from 'react'import { View } from 'react-native'function Home() {return (<View></View>)}export default Home
```

9\. Now import the Home page in App.js and create the store and Provider, New App.js file would look like this.

```
import React from 'react';import { createStore, combineReducers } from "redux";
import Home from '../screens/home.js'const rootReducer = combineReducers({ modifyCount: modifyCounterReducer});// CreateStore takes reducer as argument, combineReducers is not //required in our case, but I'm keeping it, so that if you have //more than one reducer you would be using above syntax. const store = createStore(rootReducer); export default App = () => {return (//Provider makes the store available to all the components across //which it is nested. In our case we had just home, so provider is // around it. If you have complex navigation then keep it at the top //of it.<Provider store={store}>   <Home /></Provider>);};
```

10\. Now let us access the store inside the Home component. Below is the updated content of Home.js

```
import { Text, View, TouchableOpacity, Alert } from 'react-native'import { useSelector, useDispatch } from "react-redux";import { decrementCounter, incrementCounter } from '../../Store/actions/UpdateCounter';export default function Home() {// as said before useSelector hook is used to subscribe to state //changes, on RHS we have state.modifyCount here modifyCount is the //alias name of reducer that we have in store creation at app.js
// If you have not used combineReducer then just use state.count const currentCount = useSelector(state => state.modifyCount.count)// This gives access to all the dispatch events available in the //store
const dispatch = useDispatch();return (<View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>// By default it will be zero. Because initialState is zero.
<Text>{currentCount}</Text>// Here your dispatching the event by passing the action creator
// Do not pass action itself !! as your switching the action.type
// in reducer<TouchableOpacityonPress={() => {dispatch(incrementCounter())}}><Text>Increment</Text></TouchableOpacity><TouchableOpacityonPress={() => {dispatch(decrementCounter())}}><Text>Decrement</Text></TouchableOpacity></View>)}
```

Follow the simple steps explained above and your react native application will get the capability of Redux. Once after you understand this example then step by step move states of different components to Redux store, create multiple action creators and reducers wherever necessary.
