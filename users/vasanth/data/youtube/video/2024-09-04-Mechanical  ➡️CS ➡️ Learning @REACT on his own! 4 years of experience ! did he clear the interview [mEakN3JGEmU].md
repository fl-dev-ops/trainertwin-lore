---
id: mEakN3JGEmU
title: "Mechanical  \u27A1\uFE0FCS \u27A1\uFE0F Learning @REACT on his own! 4 years\
  \ of experience ! did he clear the interview?"
url: https://www.youtube.com/watch?v=mEakN3JGEmU
date: '2024-09-04'
duration: 00:21:32
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---


# Mechanical  ➡️CS ➡️ Learning @REACT on his own! 4 years of experience ! did he clear the interview?


## Transcript

### Speaker 1

Hello all welcome back to Khera with Vasans YouTube channel previously known as Uncommon Weeks My name is Vasan I hope you are doing well Today with me I have Praveen Praveen is from Tamil Nadu more about Praveen he himself will be saying As you know this is a series of mock interview where we are discussing various different topics and the right way to get use of this mock interview is like whenever I ask some question to Praveen you can pause the video and try to answer it by yourself Lets say I ask him a coding problem you try to solve the coding problem on your own So that way youre going to actually get benefit out of this and for some reason if Praveen do not answer any question in the video


Im going to record a post video where Im going to explain answers to that If Pravin answers all of them then post video will not be there Please vote the video till the end to get to know more about the post video is there or not And this video as a whole is going to be combination of three things One is a scenario driven question followed by basics of JavaScript and React Finally well end the video by machine coding and my feedback Okay And Pravin if you can introduce yourself we can get started

### Speaker 2

Yes sir thank you for giving me the opportunity to have a mock with you So myself G Pravin Kumar I have completed my graduation in the year of 2020 from the University College of Engineering Kanjibaram specialized in mechanical department Post the graduation I got placed in an MNC and the office space will be in Bangalore and Im working with that MNC in the networking and security field for around three years now That Im more towards the development side


So I just want to switch gather my career to the development rather than going in networking

### Speaker 1

Good So just for scanning Good good Thank you so much For the audience who are watching right the Prime Minister has completed his mechanical engineering and he has learned the React by himself by watching the videos and other thing as is it clearly while hes working on networking domain on his company And now hes trying to change his job probably or eventually want to change his job with the React and front end skills Lets see how his knowledge is there And if youre somebody whos also from a mechanical background and trying to change to IT please mention that in the comment section Again if youre from Tamil Nadu that also you can mention that in the comment section

### Speaker 2

Thats all of them

### Speaker 1

okay now let me present the whiteboard as the usual way of how i would start an interview probably okay so this time i let me ask you a very simple question where

### Speaker 2

It is a

### Speaker 1

Lets say one of the common thing that is present now on most of this e commerce e commerce application or on any other sites like social media is the typeahead system Okay The typeahead is nothing but where you will search something Okay Whenever you search something So you you start getting the results below that


Like for example


just drawing to make it little quick okay


Where


Okay


So


What will happen is lets say this is like result one result two


results two and this is the result three okay its gonna keep it very simple lets say this is the search bar probably you can unmute yourself okay lets say that yeah this is search bar of any website let us and use e commerce social media or anything okay so where user searching something here and whenever user is searching something basically we are giving a list of results that is potentially that he is looking for the simplest example is lets say you go to youtube and so search for carrier correct so the one

### Speaker 2

Yeah

### Speaker 1

carrier guidance for fresher another option is carrier guidance for experienced another option could be carrier with person which is my youtube channel correct so multiple options will be shown on the screen correct so lets say we have to build this feature for me as you know user can type something and you have to make an api call to get the results and show on the screen yes yeah im not too concerned about like uh how backend would process this and send the result that part is fine just from the client side you tell me if you have to implement this what all things comes to your mind

### Speaker 2

One okay


Yes sir So basically when the user tries to type something and we need to fetch some data like we can do it in some other like some ways like for every keystroke well be making an API call and we will be suggesting them something

### Speaker 1

Good

### Speaker 2

And I think that will not be the optimal approach Correct Because a number of API calls will be made will be large Correct So we can implement a concept of debouncing here Good So where we can reduce the number of API calls by a delay If users delays the key press event by a particular timing we can call the API and we can give them the suggestions

### Speaker 1

Okay see one of the technique that youre proposing for a better rendering here is a debouncing

### Speaker 2

Okay so

### Speaker 1

Im just noting it down here okay


So where one technique is debounce correct


instead of making api for every time whenever user type something we are going to give a some delay and then we are going to make an api call correct what other things comes anything else that comes to you where you could optimize

### Speaker 2

Yeah other thing what I can think of is we can use the concept of throttling as well

### Speaker 1

Thats fine Theyre basically more both out similar actually correct Anything else in your mind from it

### Speaker 2

Yes


to fetch the data and

### Speaker 1

Yeah I mean to say so as you told the simpler the thing that we need to do is whenever user type something we need to make an API call get the data and show on the screen thats the minimum that we need to do

### Speaker 2

Do they say that

### Speaker 1

What are all the ways with which you can we can optimize this or if youre building this auto auto complete as a system if youre building this what are all the ways that you think optimizing it one you told deep bone sec which is 100 percent correct anything else

### Speaker 2

Okay


Uh let me think about that

### Speaker 1

Sasha take a moment

### Speaker 2

So but for every kickstart we should not be able to be able to suggest that uh so you need to we need to optimize that that was the that was the ask right

### Speaker 1

There is no one ask as such

### Speaker 2

You can

### Speaker 1

Basically this is a system that I want to build


want to optimize anything you can optimize like that correct because the basic flow is simple enter something make an api call get the data show on the screen thats the most basic thing that we need to implement


What are the ways with which you could optimize You can please tell me

### Speaker 2

The one thing I can think about this is uh debouncing and throttling but uh I Im Im Im suspect that we can use uh something called the React lifecycle to do that

### Speaker 1

Dont be a


Yes yes I mean whatever you told is correct There are some more things as well If audience know other than debouncing what all optimizing technique can be made please mention that in the comment section Okay Now Ill ask you a couple of basic questions on the React and JavaScript in general Then probably well just give you the coding Okay Okay I have this primitive and non primitive types in JavaScript

### Speaker 2

Yes sir

### Speaker 1

Tell me what are primitive types and what are non primitive types

### Speaker 2

Yeah the primitive data types consist of number boolean string undefined and symbol

### Speaker 1

We met then

### Speaker 2

We have the non primitive data types consist of arrays object functions So basically all will be considered as objects

### Speaker 1

Yes So what is the primary difference between primitive and non primitive

### Speaker 2

Your primitive data types is used when we want to store a single value And the non primitive type is more like a diff like defined by the developer We can store multiple and the other difference is primitive will be stored in the stack but the non primitive will be stored in the heap memory

### Speaker 1

Got it Sure sure Any idea of Prabhu like why do you think there are two types primitive and non primitive where putting other way the primitive types have a individual memory location correct Like which is like they are non mutable Like basically once you allocate a memory they are non mutable whereas non primitive types are usually mutable Correct Why do you think

### Speaker 2

I like that


Yeah why I think that that is required is we are not sure about what how much memory it will take for the non primitive type and we are sure that this much memory space is required for the primitive data types So that will be stored in the stack but in heap like we can expand the memory

### Speaker 1

no but this is correct praveen keep your storing because you could you could expand because there is a liberty compared to here but why do you think this arrays and objects are necessarily kept

### Speaker 2

The buttons are

### Speaker 1

the heap like why cant array or object be a primitive type what is the problem making them a primitive type

### Speaker 2

uh we are not sure how m how much memory space it would take we can initially we cant initially tell that uh this much memory space it will take

### Speaker 1

correct i agree that is the reason why they are non primitive or even because thats one way and another another thing could be like usually the assumptions are like its like quite larger data in case of arrays and objects in a practical application so its better to keep them in a non primitive because you start storing them in primitive then we would end up like using all our memory


Sure so Pramod Nari aware of controlled components and non controlled components in react

### Speaker 2

Yes sir uh so controlled components yeah controlled components and uh non controlled components are a both way of a handling the input element

### Speaker 1

I cant control

### Speaker 2

So in the control component we will uh we will handling the input element using the reactive state


that uh that code will be stored in the react so that input will be stored in the react and where in the uncontrolled component that will be stored in the html like whenever we are clicking on the submit but a submit button we can able to perform the actions which we required but uh in the controlled component we can do some uh other things like in field validation like conditional rendering of the submit button and dynamic input so theres much more thing we can do with the control


component

### Speaker 1

Correct So putting another controlled component is more like react way of handling uncontrolled or non controlled is like how traditional HTML JavaScript way of handling the forms Correct Yeah

### Speaker 2

Yeah it will yeah in uncontrolled the the input will be directly kept to the DOM So when controlled we will be having it in the variable which we are storing that

### Speaker 1

Good good sure can you present your screen Pravin lets start with a simple problem now

### Speaker 2

Okay thats sure

### Speaker 1

So having the problem is very simple Im gonna orally explain it to you and I can put it in the chat section as well Okay You can just copy the question from chat section if you wish and you can use it The question is simple calculator build a basic calculator that can perform addition subtraction multiplication and division as simple problem as that Okay So where it requires something similar to a Google calculator or a typical calculator UI where theres one search box on top

### Speaker 2

Okay

### Speaker 1

We have the buttons 1 2 3 4 5 6 7 8 9 and 0 And therell be is equal to button and we have like plus minus star and divide by four operations

### Speaker 2

plus minus multiply and divide

### Speaker 1

addition subtraction multiplication division four operations will be performing Okay Okay So as youre just traversing yourself or transitioning yourself from network to react problem Ill give you a few hints while solving this problem Divide the problem entire problem solving into two parts One is building the basic calculator UI Thats part one Thats going to take some time And the another thing is where how to take the right input from user and storing it Third thing is where you are going to evaluate an expression


Im sure probably the evaluating expression you might need some help First complete these things and let me know during the evaluate expression where we could discuss further

### Speaker 2

Okay so so I have some questions on that So user needs to enter a value and he need to click on the plus button and again he need to enter some value to add that

### Speaker 1

Nothing like how a typical calculator would work right Like if I like I can click on button two two and I can click on plus button and I can click on the two again it become two plus two is my expression

### Speaker 2

Okay

### Speaker 1

Not my policy further so I need to

### Speaker 2

So I need to evaluate the result I need to return

### Speaker 1

To begin with lets not use a calculator help Lets see imagine everything user types on the button only Like 1 2 3 1 plus 2 plus 3 Then it becomes like expression is 1 2 3 All the expressions are created just by manually pressing on those buttons which are actually numbers

### Speaker 2

Okay

### Speaker 1

Can we start this

### Speaker 2

Me too

### Speaker 1

I told like lets start with the UI building first once Ive built the UI with like button click events and etc where how to take the like the finally showing whatever user has typed but then we could discuss further okay I dont think there is input is not required because user manually user only press this button to form input okay

### Speaker 2

Okay


So I need a buttons from one to nine and the operation of four

### Speaker 1

Yeah you should first build that calculator layout complete calculator layout

### Speaker 2

Okay

### Speaker 1

Like how a typical calculator would look like it The top is where the expression would show Below is where 987 654 and 123 will have a 0 also is equals to And the right hand side we can have plus minus star multiplication button I mean Ill give you liberty of the UI however you want Okay

### Speaker 2

Okay so

### Speaker 1

And audience who are watching this is a very interesting question You can also solve the problem in parallel You can pause the video for a while go back solve the problem and come back and see how Prabhuvin has solved it


Our last five minutes probably okay

### Speaker 2

Okay so Im just improving it


Here I need to show it


But I got to have that


Yes sir

### Speaker 1

style


There are multiple problems as you also know like we could keep entering multiple operations here like plus minus thats okay


I know that clock in hell

### Speaker 2

Yeah I think


You can have a farm yeah you can have a farm on your glit

### Speaker 1

Lets try to evaluate the expression from lets say we are ignoring all the potential errors


or probably the evaluating expression would take more time Lets look at something that is very easy that we could do Okay At least see the is equal to whatever you are doing that is equal to should not be visible on the screen Thats not the intent correct Whenever it is entered we need to actually perform some things

### Speaker 2

Nobody

### Speaker 1

Okay so Ill only give you around three more minutes where whenever is equal to entered is equal to should not be shown on the screen Okay so where you you have another paragraph tag that will tell like the result of the operation definitely we cannot compute but that should be visible whenever somebody presses is equal to Okay and as soon as they start typing again that result of the operation should become hidden


But we should also show what I want

### Speaker 2

Yeah I need to yeah I need to pass this uh in this arrow in this function I need to pass this value everywhere like set the state to false


So that it will be hidden


So can I do that sir

### Speaker 1

see what youre doing is youre setting a value everywhere line number 17 like 20 what youre doing is youre starting to set the value correct and then press the is equals to what i want to show is the result of the operation


N where user press is equal to youre doing that and whatever the set to value that is already stored in the part of the value


anyway you can keep showing that like line number 12 uh can you scroll right scroll right

### Speaker 2

Yes yes

### Speaker 1

Right So where the result of the operation will be value


where im coming from is whatever the expression that you are showing right whatever user type something that and the result show should not be like mutually exclusive you can show both like for example earlier what we are showing one plus two star three we were showing one plus two star three when a user click on is equal to we can share gesture the result will be below that correct user starts typing again you remove that the result of the operation and you can just show the expression

### Speaker 2

Okay

### Speaker 1

Let me point out a problem

### Speaker 2

Uh Im bit confused there

### Speaker 1

Let us keep it very simple Lets say you you you are making it very even more simple Whenever you type something you show like one plus two start three youre gonna show and whenever youre is equals to youre showing the result of the value Okay Result is the result


Can we just do that


Right now we can you refresh on the right hand side

### Speaker 2

I think this button any doors

### Speaker 1

Just you can yeah you can just refresh on the can you click on that here and


So now click on like one plus two

### Speaker 2

Yes sir

### Speaker 1

Can you make sure it shows whatever youre typing it shows on the screen

### Speaker 2

It is even not so


Yes sir

### Speaker 1

Okay 1 plus 2 is shown correct So its coming as a result of the operation will be 1 plus 2 Whenever you hit the is equal to it is shown correct Yes Earlier whenever you type data by showing

### Speaker 2

Yes sir uh like we have a state value which will change to false uh which will change to true when we are clicking on this equal button

### Speaker 1

Sure sure promise We can stop sharing Okay Okay Well discuss the things in detail like what collectively feedback I can Ill give you


coming to the interview feedback pravin right uh basically i was not expecting you to be fundamentally this strong being very honest but all the theoretical questions that i told pravin you were able to answer them fairly good which is i feel like you have studied good amount of the basics very well which is something expected to clear the interview which is very good the other things where i feel the area of improvements pravin is i think this i told multiple times every time whenever a machine coding question is asked ask the question about extremities i i told an expression

### Speaker 2

Okay so thats true

### Speaker 1

you have to usually type an expression and you have to evaluate that expression correct what if user type 30 digit number and they they ask you to evaluate will the calculator would work what is the extremity how many number can be added you should ask that question

### Speaker 2

Okay

### Speaker 1

whatever the minimum what such question should be asked okay and the number that you rendered one two three that can be like further optimized by using a component correct and third very most most important thing not just you have seen many making this mistake where they do not think uh the complete solution in their mind before starting they start coding and eventually they figure out there is a problem and lets use another variable or another thing to solve this so try to figure figure out the complete problem in your mind and then start coding from it okay and even the result


portion that i told i wanted to see that expression and followed by the result probably there is bit of a confusion with which you are not able to build that okay so overall machine i feel probably theres a decent scope for improvement solving more problem will definitely help you there otherwise the rest of the the presence looks good to me so im not making a post video where im going to explain answers to something that you did not answer okay thats all from mayan pravin uh i hope you you also enjoyed the session a mock interview have any questions

### Speaker 2

Yeah sure Yeah Yes sir I enjoyed it a lot I yeah I know I know I made a further improvement in the coding So Ill do that sir Im more towards learning about the fundamentals of the JavaScript So I was a smart black

### Speaker 1

Good But I feel like you as an inspiration to a lot of people who are basically looking for transition from mechanical to IT I think they will look up to this video and audience who watch the video if you like the video please like the video and comment whatever you felt honestly share the video with your friends so that they can also get benefited Ill catch you in the next video Thank you so much for watching
