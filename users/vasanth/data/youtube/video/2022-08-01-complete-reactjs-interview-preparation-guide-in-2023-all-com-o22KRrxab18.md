---
id: o22KRrxab18
title: 🔥 Complete ReactJS interview preparation Guide in 2023 | All common interview
  questions are covered
date: '2022-08-01'
url: https://www.youtube.com/watch?v=o22KRrxab18
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Interview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nMAANG series for frontEnd Developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN\
  \ \n\nPromise video 1: https://youtu.be/1OINZhOIh0c\nPromise video 2: https://youtu.be/3V-fKuh1-8w\n\
  Promise video 3: https://youtu.be/7a3ZwYko05s\nPromise video 4: https://youtu.be/A5Az9NgncEE\n\
  \nDifference between Class and Functional component: \nhttps://www.geeksforgeeks.org/differences-between-functional-components-and-class-components-in-react/\n\
  \nReconciliation in react:\nhttps://reactjs.org/docs/reconciliation.html\n\nHooks\
  \ In ReactJS: \nhttps://reactjs.org/docs/hooks-intro.html\n\nPure components in\
  \ React:\nhttps://reactjs.org/docs/react-api.html#reactpurecomponent\n\nHigher order\
  \ component in React:\nhttps://reactjs.org/docs/higher-order-components.html#gatsby-focus-wrapperhttps://reactjs.org/docs/hooks-custom.html"
author: careerwithvasanth
duration: 00:41:53
model: saaras:v3
transcript: true
---

# 🔥 Complete ReactJS interview preparation Guide in 2023 | All common interview questions are covered

## Transcript

### 00:00:00 · Speaker 2

Hello all, welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. In case if you are seeing me for the first time on the internet, I'm a content creator. I help people to clear their interview. I have made lot of beautiful series in the past which has been appreciated by many. And recently I made one video which is around forty plus minutes, which where I was explaining the all the most common interview topics or the questions that are generally asked on the plain JavaScript, okay? And I solved lot of problems live in that forty minutes video. And lot of people got

### 00:00:30 · Speaker 2

that video and they asked me can you do a similar one on the ReactJS. So I had a plan of making that and after many people requesting me uh to make a similar set of interview video for the ReactJS, I decided to make a complete interview preparation guide for the ReactJS where I'll be touch pressing upon lot of interview important interview topics in this video, okay. Definitely this video is going to be comparatively lengthy, I think thirty plus minutes, but I'll make sure all the things, all the things that I discuss in this video, I will code step by step. So there is nothing pre-written here, I will not copy paste from

### 00:01:00 · Speaker 2

somewhere and I'll paste here. I may make a mistake but I'll correct also live in the video so that you won't commit that mistake in whenever you are giving an interview. Okay? So please watch the video till the end. If in case if you are React JS developer and looking out for a job change, definitely I'll guarantee you this video will be definitely helpful for you. Okay? Without wasting further time, let's get started.

### 00:01:23 · Speaker 2

simple presentation. uh I have made a simple presentation that contains a series of topics that I'll be covering in this particular video, okay? So, to start off with the first, these are the five points that I plan to discuss in this in this video, okay? So where I'll be explaining about all the topics and the questions that are generally asked, how to approach them, all of that, okay? The first thing is the reconciliation. So reconciliation definition goes like this, it's a process of tree comparison which is used by React to update the real DOM. Very simple words I've written here, okay? So, let's go and see

### 00:01:53 · Speaker 2

what does the official information says? So reconciliation React provides a declarative API so that you don't have to worry about exactly what changes on every update. This makes writing application lot easier but it might not obvious how we implemented with React. So there is I mean so much of jargon that is present in this video and there are a lot of things given here. So I'll link this video I'll link this link in my video description. But in very simple words let me explain you. Okay? So where

### 00:02:23 · Speaker 2

maybe I'll try to draw and explain step by step. Okay.

### 00:02:37 · Speaker 2

So in let let's take it very simple example. See I have I have created one small react app here. uh empty project as you can see. All we have is one div and inside that I have a thing called welcome to uncommon geeks, correct? So if I go here and if I see the application running here, all I have is this welcome to uncommon geeks, correct? So if I have to represent this in a form of a tree. So what I will be doing is let's take uh pencil, some black color, okay? And

### 00:03:06 · Speaker 2

what we have is we will have we have one div, correct? and inside the div we have one h one, h one tag. let's say I have two.

### 00:03:15 · Speaker 2

Two H One Tax

### 00:03:16 · Speaker 1

Okay

### 00:03:17 · Speaker 1

Hope you are

### 00:03:20 · Speaker 1

Hope you are doing

### 00:03:23 · Speaker 2

well

### 00:03:23 · Speaker 1

Hello

### 00:03:23 · Speaker 2

Okay? So now you have two H one tag here. Correct? So this is a div tag. So this is a

### 00:03:33 · Speaker 2

my drawing is not that good, bear with me, okay? So it's a div tag. And we have two H one tags, correct? We have two H one tags.

### 00:03:44 · Speaker 2

We have to H1

### 00:03:46 · Speaker 2

tax. So let's say now this is the real DOM that you're seeing on the screen, correct? Which basically DOM is nothing but T representation. Let's say you have another div at the same hierarchy, then you will have another div here and both divs will have some parent element, correct? That's in a simple representation of the DOM. Now, what happens is how React works. So I think most of you know the reconciliation, but I tell what the mistake generally candidate do in the interview. So I have copied this, okay? Let's say this is a virtual DOM and this virtual DOM is

### 00:04:16 · Speaker 2

doesn't look like this but it will have a copy just basically at the end of the day DOM is nothing but just an object correct object containing all these values so let's say now this is a real DOM let me try writing this okay so real DOM

### 00:04:33 · Speaker 2

Okay. So this is a real DOM.

### 00:04:37 · Speaker 1

Ruddy

### 00:04:41 · Speaker 2

So it's a real DOM and this is a virtual DOM.

### 00:04:44 · Speaker 1

Okay

### 00:04:49 · Speaker 2

Virtual Dom

### 00:04:50 · Speaker 1

Okay

### 00:04:50 · Speaker 2

So

### 00:04:58 · Speaker 2

one minute let me try moving it huh okay. So this is a virtual DOM and this is a real DOM. Now let's say there is some state change happened correct so we have two H one so one of the H one let's say hope you are doing well I am also doing well okay. Whenever I make this change now correct. So now this and I save this. So this H one need not to change correct there is no change in this. Only this H one has changed correct. So React should compare and update this particular thing on the screen correct. So

### 00:05:28 · Speaker 2

we have to do is if you go and see here we already have one virtual DOM. another virtual DOM is created. okay? another virtual DOM is created with the change. okay? another virtual DOM is created with the change whatever we are making. okay? so let's say here we have the same H one.

### 00:05:50 · Speaker 2

And uh what will happen is, let me quickly draw this.

### 00:05:55 · Speaker 2

H one

### 00:05:57 · Speaker 2

Let's say this H one has been changed. Okay, this is a changed H one. So how the H one was H one was before and this is a changed H one. So comparison happens between two virtual DOM. Okay, this is where most of the candidates I have seen making a mistake where they will not say the comparison is happening between two virtual DOM. They'll say comparison happened between virtual DOM and real DOM. Virtual DOM and real DOM comparison also happens, okay, but to identify which node has been updated will be identified by comparing between two virtual DOM.

### 00:06:27 · Speaker 2

Now React knows this H one has been changed, then this change is finally compared between this virtual DOM and real DOM and the H one gets updated. Okay? This is reconciliation. Reconciliation is one of the very, very important topic of the React because entire React architecture, whether you're applying for React JS interview or React native interview, this virtual DOM and the reconciliation concept is very, very important because if you don't know this literally you don't know React itself, correct? You may know, you may know how to build a beautiful website or a mobile application, but unless you know the architecture, you'll

### 00:06:57 · Speaker 2

not be a good programmer. Okay, this is the first question generally most of the interviews they will ask with respect to ReactJS. Okay, now let's go to the second topic.

### 00:07:06 · Speaker 2

So the second topic is

### 00:07:09 · Speaker 2

As you see here, class versus functional component. So this is just an ask, this is not something what you call deciding factor. This generally asks to see from how long you have been using the React. Have you seen the evolution of React? Why we are using functional component, why not the class component? All these aspects you know, then they'll think, yeah, he's working with React for a quite good time. But this is not something a deciding factor as such, okay? So I can, I will link this Gigs for Gigs article for you where they have clearly explained about difference between function and class component.

### 00:07:39 · Speaker 2

okay? So where they have written all the differences here. This is more like a theory, there is less that I could explain, okay? So I'll link this article in my video description. So please go through this and learn the differences, okay? Now, let's go to the third point, again an important point is hooks, okay? So reconciliation and I've I've also written these differences, if possible I'll try to upload this PowerPoint also to my GitHub repository so that you can read that. So now what are hooks in React? Okay? So hooks is one again very very

### 00:08:09 · Speaker 2

important topic. In case if you've already given any React interviews or if you're planning to give the interview, please bookmark this concept. I don't think your React JS or React Native interview will get over without asking any question on the hooks, okay? Hooks are a new addition React sixteen dot three, sixteen dot eight. They will let you use state and other React features without writing a class. Basically, I think we have here introducing hooks. The same, I have copied the definition from here itself. I'm nobody to give a definition for React hooks because it's Reacts, okay? Now

### 00:08:40 · Speaker 2

So we already using the hooks on a day to day basis. So now let me explain you how questions on hooks will be asked, okay? uh Basically there are two ways how the questions about on the hooks will be asked. One, they'll ask you to write a some examples for the already built in hooks. For example, use memo, use callback, use focus effect. Use focus effect is actually from React navigation. So there are could there are many hooks which are not used on a day to day basis, but they are very very important hooks, okay? So they will ask you to know your knowledge on those hooks.

### 00:09:10 · Speaker 2

okay? That can be asked. Second, they may ask you to write a custom hook of your own, okay? And if you are applying for any premium companies, the second chance is very high where they'll ask you to write your own hook, okay? So today, let us try to write a simple hook. Let's start my tutorial of writing the code by writing a simple hook. So what is the problem statement?

### 00:09:29 · Speaker 1

Here goes the problem statement

### 00:09:47 · Speaker 1

So I know you already read the problem statement just to summarize

### 00:09:50 · Speaker 2

Basically you have to write a simple hook. It's called use counter hook which will take the initial value from the component and it will give us a method to increment the count, decrement the count and reset the count. Okay? So these are the something that we have to be writing. Let's see how do we write it. So I'll write everything from the scratch now. So you follow along with me and finally I'll also upload this project into my GitHub repository. You can download the project and practice on your own. Okay? So there are certain important things whenever you are writing the custom hooks. Okay? So

### 00:10:20 · Speaker 2

that you have to first see here. So building your own hooks. I'll try to link this link also in the description, okay? Hooks are new edition sixteen point eighteen and extracting custom hooks, okay? Using custom hooks. See, do I have to name my custom hook starting with a use? Please do. So whatever the hook so far I created, I use a convention of use followed by the hook name, okay? Because that will give a proper sense like we have created hook and not just any other function, okay? Do two components within the same hook share a state? See, no. I mean these are the important

### 00:10:50 · Speaker 2

something that you need to know before start writing the hooks. Okay? And I don't see a lot of any other guidelines as such that we need to follow. Let's start following the basic guidelines that I've already discussed. So first thing, very very important. I don't write the hooks first, but I want to ask you one question.

### 00:11:09 · Speaker 2

So let's say we have U state, okay? Ten

### 00:11:14 · Speaker 2

const

### 00:11:16 · Speaker 2

count, comma, set count, okay? So, this is the question that I generally ask for the candidates whenever I'm taking the interview, okay? See, under the hood of JavaScript, there is nothing called hooks, correct? Hooks, classes, function, there is nothing. Under the hood, everything in JavaScript is just the functions, correct? Sorry, under the hood, everything is just the objects, correct? But there is one layer above where we all call lot of things like pure components, higher order components, and of that they all has to become into some very, very minimal steps in JavaScript. So I will ask what is use state?

### 00:11:46 · Speaker 2

is it a class? is it an object? what it is? okay? in case if you someone who know the answer please mention that in the comment section and put your answer. U state is this or most of the hooks are this. okay? in case if you don't know let me answer. see anything you have a keyword you have a variable name followed by you have a parenthesis. okay? this means it is a function. please be aware of this fact. if somebody ask you what is U state and you tell whether it's a class or it is an object it shows you

### 00:12:16 · Speaker 2

foolishness that you never spent any time to understand the built-in things. You don't have to write a definition for use state. Nobody expects that. It is quite complicated or not so complicated also but comparatively complicated let's say. But they would expect you at least you might have seen the definition. Correct? So if you click on now use state, here you goes the definition. All the things that are mentioned very much in detail here. Correct? So use state or all the hooks are functions. So now if you have to write a custom hook or hook of your own, then You also need to write a function, correct? Let me write like const

### 00:12:50 · Speaker 2

use counter, this is my hook. Okay?

### 00:12:55 · Speaker 2

and what I need to be doing, I will take an initial value here. Okay? Initial value, then, then what I'll be doing, then what I'll be doing here is, same, I cannot create a use state. I have to use the whatever the use state that is already built in and I need to extend its capability. So I'll tell you how I'll do that. Okay? So whatever initial value I'm sending, I'm adding it here.

### 00:13:17 · Speaker 1

Okay

### 00:13:18 · Speaker 2

Then I have a function called increment

### 00:13:22 · Speaker 1

Okay

### 00:13:23 · Speaker 2

So how do I increment it is very simple. Set count. Count value plus one. Okay? Then I have I will add another function called decrement.

### 00:13:37 · Speaker 2

Okay, decrement, set count, counter value minus one. I'll get another simple function called reset where I'll be setting counter value into the initial value. Okay.

### 00:13:48 · Speaker 2

Then, now you know, whenever you have written U state, U state is basically getting two things from the that particular hook. I mean, this is a function that returns two values. That is one, the value, whatever you are passing initial value and the function to set that value. Similarly, let us, now we have to return four values from this function, correct? So return

### 00:14:11 · Speaker 2

What and all we'll do? Count.

### 00:14:13 · Speaker 2

increment, decrement and reset. Okay? Now let's say I have to use the use counter hook here. How I'll be doing here that is same way. So I need all these values.

### 00:14:26 · Speaker 2

Okay? And I will be calling use counter. Since it is in the same function, same file, we don't have to export it. If you are keep if you want to keep this somewhere else and then you can export it as well. Okay? So use counter, then I'm passing the initial value of zero. Okay? Now, I will show the value of count in H one. I'm showing the value of count. Okay?

### 00:14:51 · Speaker 2

So then let us have something called button. Okay? Onclick.

### 00:14:59 · Speaker 2

Let me call increment. Okay? And inside this also I'll do the increment operation. Okay? Similarly I'll do for the decrement. Okay? And I'm also do the same for the reset.

### 00:15:12 · Speaker 2

Okay

### 00:15:14 · Speaker 2

Now, I think we are good. Let's see, are we good?

### 00:15:19 · Speaker 2

So I think the value that is written here is count

### 00:15:25 · Speaker 2

which is fine and also having a count here. Use counter initial value.

### 00:15:33 · Speaker 2

I think it is not showing the okay now it is showing the count value okay let's say I click increment it is incrementing let's say I click decrement it is decrementing let's say I incremented and reset or decremented and reset and the value is being reset correct so such a simple thing actually many might have not tried writing a hook of your own correct but this if you had written how easy actually in case there are many scenarios where we will be using this functionality of incrementing and decrementing correct we can easily write this simple hook

### 00:16:03 · Speaker 2

producing lot of different places. Correct? And how how much time I took? I took a two and a half minutes to write this. I have written lot of books in the past that might have made my life easier, but it is not so difficult to practice this before the interview. Correct? Now at least you know this question will be asked. Please practice this. This code will be available in my GitHub repository and the link will be available in the description. So copy that link and please practice. Okay? So so so now that was the one point. We covered now reconciliation. We also

### 00:16:33 · Speaker 2

also covered the difference between class component and functional component and third point we also covered how to write a custom hook and what are hooks. Okay? So hooks basically you already know gives state and state management and the life cycle method to the functional component. Correct? So definition other things you read. I have one simple question here. Okay? Listen to me very carefully. This is something that I won't tell answer. This is something a homework for you.

### 00:16:57 · Speaker 2

So, uh the belief is that hooks are introduced in let me again go to the documentation then I'll tell. So hooks are new edition sixteen dot date of react and first the hook okay they have not written anything like that here. So basically whenever I ask why hooks are introduced in the interview most candidates say functional components were stateless to make the functional component stateful and to give a life cycle method to it we were we were hooks were introduced okay. So whenever they say functional components are stateless. I ask one simple question, tell me what is state?

### 00:17:32 · Speaker 2

So in case if you know what a state it is good. If not in very simple words state is nothing but the memory of a component as long as the component has a life that variable whatever you created will have a life. So this is in a simple word state. Okay. Now let's say we are not using a hooks in a functional component you have created a variable called const x whose value is ten. Okay. So I I don't have to write I I let me keep it very simple so that you understand you have just one functional component you have created a variable called const

### 00:18:02 · Speaker 2

texts and whose value is ten. Please tell me whether this is a state of the component or not, state of a functional component or not. If this is a state, then before hooks, whether functional components were stateful or stateless. This is very very important topic, okay? uh Many get confused while answering that. So you in case if you are a brilliant, this is a homework for you, please mention this answer in the comment section. If most you you are not able to give the answer correctly, definitely I can answer that in the comment section. If not, this is a challenge for you, okay? Now let's go to the next topic

### 00:18:37 · Speaker 2

So we have covered with the hooks. So next most common interview question is pure components. Okay? So they will ask you what is pure component and they will also ask you can you write a working example to demonstrate the pure components. In fact, I have to mention this point when I was practicing for this video, I wanted to write some simple example for pure components. It was not that easy for me to find a working simple solution for pure components. I need to admit this, okay? Where after lot of research, why I am saying a lot of research, see I would definitely know how to write a pure component.

### 00:19:07 · Speaker 2

right? But the that will be with a lot of complexities and other things. I need a very simple example. I was checking if anybody has written it, okay? In especially in functional component using react.memo. But there weren't lot of examples, okay? So definitely watching this video on how to write a pure component will help you while answering the question in the interview, okay? Now let's first go back and see.

### 00:19:29 · Speaker 2

react pure component. So react pure component similar to react component, the difference between them is react component doesn't implement should component update, but react pure component implement it with a shallow prop and state comparison. Okay? Let me give you a very simple definition for pure components. Pure components are those components which will rerender only when state or props passed it will change. Okay? Until then they will not change. I'm going to show the example in a while. Okay? Let's say you have a parent component

### 00:19:59 · Speaker 2

and a child component inside that. Whenever parent's component state is updated, child state child component will also is rerendering unnecessarily. Even though that is that whatever the variable that you're passing to the component if that uh state or the prop has not changed, still the child component is rerendering which is unnecessary. To avoid this problem, uh you can use the pure component selectively. Okay? So I'm gonna show how to use the pure component in the functional component also with a very very simple example. Okay? Now let's get started.

### 00:20:29 · Speaker 2

all this react counter wala thing I'm removing, okay? I'll be only posting this code in the github repository, so rest whatever required to do here, please do it on your own, okay?

### 00:20:41 · Speaker 2

So here or else let us do one thing. Let me try to comment this section, okay? So that all the code is readily available for you, rather you facing a difficulty.

### 00:20:55 · Speaker 2

Okay. Use counter example.

### 00:21:02 · Speaker 2

example code. Okay? Use counter example code

### 00:21:08 · Speaker 2

Okay

### 00:21:08 · Speaker 1

Suppose

### 00:21:08 · Speaker 2

So next let's probably now we'll go to the pure component thing. Okay?

### 00:21:13 · Speaker 2

pure component

### 00:21:17 · Speaker 2

pure component example. Okay? So here, let's see the pure component example. So basically what we will do, pure component means component should not re-render when a state or prop passed it are not changed, correct? So let me create now three variables. uh for example, you state

### 00:21:40 · Speaker 2

Let me create three variable like const, salary

### 00:21:45 · Speaker 2

salary, set salary, okay? And I'm creating use state salary, okay? It's a by default I'm keeping it a thousand value, okay? salary and then I have something called age, okay?

### 00:21:59 · Speaker 2

age I'm having, let's say by default I'm keeping age as thirty. And let me also create another variable called ID. Okay? ID

### 00:22:09 · Speaker 2

ID I'm keeping by default ID as one. Okay. Now, let's say we have a scenario where

### 00:22:17 · Speaker 2

I'm writing a use effect, okay?

### 00:22:20 · Speaker 2

use effect. See, this is not like absolute beginner video. You need to know few aspects of uh React and other things. I'm just helping you to clear the interviews, okay? In case if you don't know what is use effect, let me answer that. Um use effect is basically lifecycle hook that will give you methods like component read mount, component read update, component read unmount, all of the activities that you have done in class component can be made in this this particular component can be implemented in similar way with help of this use effect hook. Okay? Let's say, see, I have I have created one set interval here.

### 00:22:53 · Speaker 2

the set interval triggers for every one second. What it does is it will do the set ID to always to

### 00:23:04 · Speaker 2

no, maybe, yeah, set ID what I'll do is ID plus one I'll do. Every one second I am doing an ID plus one. I'll tell why I'm doing all these things or how this will differ in real time. Okay? Now let us create a component, okay? Where let me name it as a parent component, okay? parent.js.

### 00:23:23 · Speaker 2

So here I'm going. I I have already built in the installed snippets, okay? So I'm adding RFC. And snippet came for me, okay? So here I'll take three values, that is same, ID, ID, age, maybe in the same order, let me write, ID, salary and age, okay?

### 00:23:42 · Speaker 2

ID, salary and age, okay? ID, salary and age. So what I'll do is in this component, okay? Let's say I have one div tag and I need only ID here, okay? Which is actually changing every second. So H one

### 00:24:04 · Speaker 2

I D is I D, okay? Let me create a pure component now, okay?

### 00:24:12 · Speaker 2

purecomponent.js okay? So same I'll do RFC again. So this will take two more values that is salary and age. okay?

### 00:24:22 · Speaker 2

Bear with me, it's not that difficult, okay? I'll explain all the things once again in case if you're getting confused, okay? So here, now same, let's say I have again a div tag, okay? And here I have H one, okay? So where inside

### 00:24:38 · Speaker 2

pure component, okay? And inside that let's say I have H two.

### 00:24:44 · Speaker 2

H two. Okay.

### 00:24:47 · Speaker 2

and let me display the salary.

### 00:24:50 · Speaker 1

Okay

### 00:24:51 · Speaker 2

salary, salary

### 00:24:53 · Speaker 1

Okay

### 00:24:53 · Speaker 2

Then let me also display the age

### 00:24:58 · Speaker 2

Don't worry, even this code also will be available in my GitHub. In case if you get confused, you can download and practice it. Okay, don't worry. But I'm also going to explain all the things once again. So now let me add a pure component here.

### 00:25:11 · Speaker 2

pure component. And I need to pass salary, I need to pass the props, salary and age prop from here, okay? Salary is salary, okay? And I also pass age is age, okay?

### 00:25:26 · Speaker 2

Let let's put some logs here, okay? Log inside a parent component, okay?

### 00:25:34 · Speaker 2

And let's keep a log here as well inside pure component.

### 00:25:39 · Speaker 1

Okay

### 00:25:41 · Speaker 2

inside pure component

### 00:25:43 · Speaker 1

Okay

### 00:25:44 · Speaker 2

So now I need to add the parent into this, correct? So where

### 00:25:52 · Speaker 2

parent, okay? Let me pass all the values, whatever we have, right?

### 00:25:57 · Speaker 2

So ID is equals to ID. Okay. Then we have salary which is salary. Then we also have a variable called age which is age. Correct? So let me reiterate, there could be some errors, let us fix that also in case if we get any errors. To be very simple words what we have done is we have created a function component called parent component which actually takes three props, ID, salary and age out of which it also has a child component called pure component.

### 00:26:27 · Speaker 2

which takes the salary and the age. Okay? As per our current logic, only ID will be changing at an interval of one second. Okay? Salary and age are gonna be constant throughout the instance of the application. Okay? So in that case, right now let us go and see what is happening on the UI. Okay?

### 00:26:45 · Speaker 2

So let me refresh this. If you see inside parent component, inside pure component, parent component, pure component. Okay?

### 00:26:53 · Speaker 2

and if I refresh this again.

### 00:26:57 · Speaker 2

Hello

### 00:27:01 · Speaker 2

export default. I think it need to log more times. Like every time whenever the ID is changing, right? It need to be logging. So ID, let's see, in case even if there is a mistake, let us fix this. Inside set interval.

### 00:27:21 · Speaker 2

Maybe there is some problem in logging the things. Now if you see, we are getting like inside a set interval, inside parent component, inside pure component. So it's keep on happening. So, so parent component we are seeing a log inside parent component, then we are seeing a log inside pure component also, correct? See, parent component has to rerender. The reason for that is ID which is used in the parent component is changing every second. So it is there is a point in updating this. But the pure component which is taking salary and

### 00:27:51 · Speaker 2

there is no change in the value of those. So it need not to rerender every time, correct? So what I will do is I am making this pure component actual pure component now. How do I do that? So I will be using something called react dot memo, then I'm passing pure component inside that, okay? In case if you're using the class component, you can extend the pure component class and implement the same. But since most of the companies are using the pure component functional components now, the questions are mainly related to the functional components. That is where I

### 00:28:21 · Speaker 2

the difficulty in finding an easy example. In internet I did not find easy examples to get a pure component. I thought I'll search and I'll get hundreds of results but that did not happen. Okay? So now I'm making this a pure component. Let me refresh once again. Okay? So if you see here, uh inside set interval, inside parent component,

### 00:28:44 · Speaker 2

I don't know why this is not re-rendering. Sometimes locks do give a problem. Technically now what should happen only inside set interval and inside parent component should be triggered but inside this pure component whatever we have that should not be rendered. Okay?

### 00:29:02 · Speaker 2

Yeah, let's continue probably uh I I think where is the I got to know where is the problem. So what is happening this somehow due to some reason the set interval is triggered one after two times it is not triggering. Let's try to remove this and let's try to reflect it uh user effect as component did update every time let it reference re-render, okay? If you go and if you refresh now. So you would see like parent component, pure component, all the things have been re-rendered. So now if I make this a memo component. Now if you see, let me refresh.

### 00:29:32 · Speaker 2

only parent component, pure component only first time. Rest all is only the set interval and the parent component. So you are not seeing a pure component log. Observe here, you are not seeing the pure component log here, correct? Which is very very important and that is the whole purpose of pure components. As long as the states or props passed to that component are not changed, the component should not re-render, correct? So that is what happening in this as well. So pure component is not re-rendered. Okay? So you got a very very simple example for the pure component. I'll

### 00:30:02 · Speaker 2

this also add this also into my GitHub repository copy it but I'll do a last iteration as something was not working in the middle I'll do a last iteration. Very simple example so we have three three attributes and out of which all the three attributes are passed to component called parent component and in the parent component we are using only one one property that is ID remaining two properties are passed to child component called pure component. In pure component we are make you are making it a pure component by with the help of react dot memo okay this is a way of making of

### 00:30:32 · Speaker 2

functional component, a pure component. So we are making this a pure component. So which will re-render only if states or props passed to it are changed, okay?

### 00:30:40 · Speaker 2

Now. So ID is this pure component. Now what we are doing is inside the use effect we are running a set interval. You all know what is set interval. It is it is a mechanism of running a certain piece of code at a particular interval of time. So at every one second we are increasing the ID, okay, by one. And whenever the ID is increased, obviously the parent component has to rerender because the props state props to it props passed to it have been changed, right? Whereas in pure component need not to rerender because salary or age has been not changed. So this is all about the simple

### 00:31:10 · Speaker 2

very simple example for the pure component. Definitely you can write this in the interview and get full credit for whatever you have written. Okay? Now, let's go to the next topic and another very very very interesting and important interview concept. Okay? So what is that? Let us go and see.

### 00:31:27 · Speaker 2

So, the last point is higher order component or what we also call as H O C. So higher order component is an advanced technique in React for reusing the component logic. Higher order components are not a part of React library per se, they are a pattern that emerges from React's compositional nature. Okay? Same, this definition is also again I've taken from the official documentation itself. This is very very important topic. Okay? In fact, we already used one higher order component. In case if you know which higher order component we already used, let me know that in the comment.

### 00:31:57 · Speaker 2

section, okay? So friends, without I start explaining the higher order component, I have one simple request. So I think it has been already close to thirty five minutes or thirty to thirty three minutes you have watched the video. I think it has definitely been useful for at least most of you guys. I'm trying to I'm putting lot of hard work to make this video. All I expect from you to do is please like the video. At least now you like the video if you're not liked so far. And add a comment stating like are you liking the video? Something would have been better or whatever I have done is already good. Please mention that in comment section. It will help

### 00:32:27 · Speaker 2

me a lot to improve my upcoming videos and by liking the videos you are helping me to get more impressions on YouTube. So more impression means a lot of my videos will be visible in so many people walls and whenever it is visible there is a chance they would click it and the videos become popular. When videos become popular there is a high chance like lot of people watch it and they get a chance to clear their interview. That's a noble cause that I'm actually trying to make the videos. So please like and comment about the video without continue watching further. Okay? Now, let's continue with the higher order component.

### 00:32:56 · Speaker 2

Basically, a higher-order component, in very simple words, the definition is a component that takes a component as an input and returns a component as an output. So this returned component, here's one important mistake people do. Return a component as an output, not always, okay? Majority of the time it takes a component as an input and returns a component as an output. It need not return a component as an output, okay? There's no mandatory as such, it can return just empty, okay? So let me give you a simple example where higher-order component can be used so that you can relate it well.

### 00:33:26 · Speaker 2

Let's say you are trying to open a website or a mobile application. In case if you have a valid authentication token, then you will have to go to a home page. If you're not having a valid authentication token, that means you have been not logged in user, you should be taken into login screen. Correct? So you can keep a check, you can pass the condition and a component and the higher order component will decide which component to render depending on the condition. Correct? So this is the easiest and the simplest way example that I could give for higher order component. Let's look at a complex example.

### 00:33:56 · Speaker 2

example which we already used. See in pure component example you saw react.memo right? So here memo is a hirador component. Why memo is a hirador component? It's very simple. Definition you already heard. It's a it's a function or a component that takes another component as an input and returns a new component as an output. Memo is taking a component as an input, correct? And returning a new component so that you are able to use pure component here. That's all that's the simplest example. What other things there are methods like connect in Redux that's a hirador component. There are many such examples.

### 00:34:26 · Speaker 2

But in interview I generally ask the things like what is the example that you used Hirador component. Don't tell me any bookish example. So in such cases you can tell the one example that I gave for the auth card. Or there are many other UI related examples where there Hirador component and lot of child components are passed to it and the Hirador component manipulates the component and returns back. For example you have same button across multiple places with certain additional attributes. Like a login button has a login text and some other style. Register also has a button with some additional styles.

### 00:34:55 · Speaker 2

So in such case you can pass a component, the button component into a higher order component and that will return a slightly modified version of the component. Okay. Now let us see how to write a higher order component. This is again very very important concept. Again this is not so easy to find a working example, a simple working example. It's always tough to find a simple working example. In interviewer all the time they will not be expecting you to write a complex example, they want you to write a simple example and demonstrate, correct? So I will write a simple example for you, so please bear with me, again this code will be available in GitHub.

### 00:35:25 · Speaker 2

to practice along. Okay? So now I'm commenting the pure component part. Okay? So pure component part. This also I'm commenting. Okay?

### 00:35:36 · Speaker 2

Okay, see.

### 00:35:39 · Speaker 2

Let me properly comment them and make a separate section, okay? So where this is a pure component section, okay? So whenever you want to practice certain things, activate them accordingly. Pure component section, okay?

### 00:35:57 · Speaker 2

So this is also pure component example. So enable pure component here and enable pure component here as well. So enable I meaning just un-component. So that they become uh usable. Now let us see higher order component. Let's see higher order component you already got the definition. It should basically take a component. Correct?

### 00:36:16 · Speaker 2

So it's a it's a component or a function that takes a component as an input and returns a new component, correct? So what I'm doing here is, let's say const, I created a file called container. So const container is equals to

### 00:36:29 · Speaker 2

So what I'll do, I will take a component as an input. Correct? I'll take a component as an input, then I would return

### 00:36:38 · Speaker 2

a better component or a modified component basically, correct? So what I'm doing, I'm I will let me create one div.

### 00:36:46 · Speaker 2

okay? And H one, then what I'll do inside higher order component and this is very important. Whatever the component you pass, I'm also rendering that component, okay? You can do any other things like passing props etcetera. I'm keeping a very minimalistic example where whatever the component that has been passed to it that is rendered along with a new title. So the component has basically changed from the way it has come to this container.

### 00:37:12 · Speaker 2

Now, let us export it for default container, okay? Now, now what we'll do is, so we have done this export default container, okay? And let's create one another component because you need to pass an input, correct? So let's maybe let's create like a component called hello.js rfc. And what I'll I do don't do anything here, I'll just write welcome to uncommon geeks. Don't worry if you're getting confused, again I'll step by step slowly iterate everything that I've typed so far. Okay. Then. So now here

### 00:37:49 · Speaker 2

Here let me again comment and write higher order component. Okay. So basically now I'm look I want a sample component from container.

### 00:38:00 · Speaker 2

container. So container is taking what? container is taking a component. Which component? I've created a hello component, right? Let me pass the hello component, okay? And I'm getting a new component. And that new component I am rendering here.

### 00:38:14 · Speaker 2

where here. First let us see in case if it working well, then immediately let us go back and step by step let us check what is happening, okay? Is it rendering? I think it requires a refresh.

### 00:38:30 · Speaker 2

So I think it is not rendering well. So where we have a sample component, okay? And I think there needs to be a small modification in the brackets. Okay? Let us see.

### 00:38:46 · Speaker 2

So it is working. Now let me explain step by step what is happening, okay? So very very simple, not at all complicated. You saw what is higher order component here, right? So basically higher order component is a function that takes a component as an input and returns an enhanced component. So why enhanced component? Because we already have a good component. So something extra need to be done from the higher order component, that function, correct? So in this case in very simple example what we are trying to achieve is, whatever the component you pass, that components will be rendered and along with it

### 00:39:16 · Speaker 2

are also adding a title and returning a new component. So definitely it can be called an enhanced component, correct? Rest remains the same. In parent not this parent is not required.

### 00:39:26 · Speaker 2

And basically you need to pass one component into it, correct? So we have created another component called hello component. So in app.js if you see, you have a container, so this is the container that takes a component as an input and we are passing hello component to this and we are getting whatever what is the return? Return value is a new component, correct? So that you are keeping it in sample component and that is that is the since it's a component you are trying to render it in this way, correct? And you already got the output here, correct? Very very simple, correct? I mean definitely I put

### 00:39:56 · Speaker 2

to create, uh, pick the simple examples for different concepts because in internet if you go there you keep getting lot of difficult solutions which are difficult to analyze or write in the interview. Follow the simple steps because interviewer will be more interested in knowing very simple examples where you can explain them very well, correct? So, I think that's all about this particular video. I think I'm done with my presentation as well, okay?

### 00:40:18 · Speaker 2

So, but these are not the only important topic. I've tried covering five topics. There are a lot of other topics for the important for the interview like there is a React JS, sorry, there is a Redux concepts and many other concepts of React JS which are very very important for the interview. I've not covered them in this video. In case if you like this video and comment a lot about it and you want me to make a part two covering more topics, definitely I'll make. But don't worry, even if you don't make that video, these are all the very important topics, the top, let's say there are ten important concepts, top

### 00:40:48 · Speaker 2

I am coming in this video, but in case if you are applying for very big firms like Google, Netflix, Amazon and all, definitely you need to know the remaining five items as well. So please comment if you want me to make a video on that, definitely I'll be more than happy to make a detailed video explaining all those concepts with very, very simple explanation. So whole of my funda is to explain things in a very simple way so that all of you get benefited. Okay? So that's all about this video. Please like the video, like I already requested, all I want is to help people to clear the interview. Like the video, comment about the video, how it is

### 00:41:18 · Speaker 2

coming. Are you liking the video, not liking the video, anything it is, please comment and do not forget to subscribe to Uncommon Geeks. This is a humble request of mine. By subscribing more and more people subscribe, the channel becomes more and more visible to the people and lot of people get benefited from this. So if you have not subscribed, please do subscribe. The source code for this is in my GitHub repository. I'll link the GitHub repository in the description. Please download my GitHub repository and I have written lot of beautiful articles about React and JavaScript concepts in my medium. I'll try to link my medium blog also in the description. Please, please read.

### 00:41:48 · Speaker 2

my medium articles and follow me on medium as well. Thank you so much for watching. Catch you next video.
