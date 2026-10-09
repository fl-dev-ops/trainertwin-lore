---
id: GU7kfIDDF7k
title: "2024  @Epam(part 1) frontend interview questions and answers|3-5 year experience\
  \ |Detailed answer\U0001F525"
url: https://www.youtube.com/watch?v=GU7kfIDDF7k
date: '2024-07-05'
duration: 00:25:42
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# 2024  @Epam(part 1) frontend interview questions and answers|3-5 year experience |Detailed answer🔥


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career With Person YouTube channel. My name is Vasanth. I hope you all doing well. This is a very important video series as you all know where we are discussing about different companies interview. We have already discussed about Infosys and Capgemini. Today I am back with a new video where I am going to discuss all the interview questions and answers to the questions in EPAM Systems. So EPAM Systems is a famous software company and they are hiring quite aggressively. I have seen their holdings across multiple places in the Bengaluru. So in this particular video where I am going to ask a lot of questions that was very recently asked just 15 days back in EPAM Systems.

### 00:00:30 · Speaker 1

primarily on the front end I'm gonna divide probably into round one and round two or if more question as I have more question I might divide into round one round two and round three okay if you can just support me by subscribing to my channel liking the video without wasting further time just before we start I want to tell you about a new tool that I've been using quite aggressively last few days and it's been very handy for me and I have built a lot of application using that I wanted to give an overview I had a requirement to build a video calling application and my time frame was very limited so I was looking for a tool online with which I can build a video calling application with most of the

### 00:00:50 · Speaker 2

I

### 00:01:00 · Speaker 1

Minimal code that I could do. Okay. So I encountered a tool called Ziggo Cloud, a build powerful interaction apps with voice, video and chat API, where they provide a very different services like video call, voice call, live streaming, in-app chat, cloud recording, effect and much more. Okay. And the most beautiful part that I liked about Ziggo Cloud is they have something called a UI kit. Let's say you log in and you just click on the create project and you let's let's say you select voice slash video call and hit next. Okay. Specify the project name and choose the platform where you want to integrate your video call.

### 00:01:30 · Speaker 1

Everything is readily available. Let's say you want to build Android, you have a code ready. iOS, web, React Native, everything that you want to build, the code is readily available for you. All you have to do is just specify the project name, install the SDK, start using their code and immediately your video call starts working. And the another most important point that I liked about them is they have a video call feature as you already told and it is fully customizable. For example, now one-on-one call, you want to make a standard beautification, you can include it. You want in the group call how the users has to be shown on the group call, that also you can specify.

### 00:02:00 · Speaker 1

how the UI should look like all of that you can just specify by toggling the options here copy the code put it in your project everything works for you you don't have to worry about how to put different images on the screen for different resolution of mobile different mobilization of resolution tab all of that is taken care by the Ziggo cloud and the eyes on the top is

### 00:02:18 · Speaker 1

As soon as you register, you get 10,000 free minutes. So as soon as you register for next 10,000 minutes, you don't have to pay anything for the Zico cloud. Only after that you have to start paying. How beautiful is it? So for next video calling requirement, please go video calling or any of your media requirements actually. Please go. Let us start with access number one. So one of the common interview question, the explain, call, apply and bind. Okay. I'm sure a lot of you might have encountered this question in the interview. But including myself, a lot of us might have learned call.

### 00:02:48 · Speaker 1

apply bind by watching actual sign is video on youtube channel and that is one of the best way to understand call apply bind but only only problem is after you evolve to certain point where you need to know some practical use case for it because how we are do using it on a day to day basis correct that what makes you different from a junior developer now if you understood call apply bind let us understand little bit in depth so So I've written certain scenarios actually. So let's say you imagine a CEO of a powerful company, but you need to control who gets to make decision. Okay. So that is where.

### 00:03:18 · Speaker 1

So, here CEO nothing but a function and whatever who need to take like who make the decision that you are going to do using help of the call apply and bind ok. How actually call apply and bind can help you as an assistant to a CEO to do certain things I am going to explain ok. Call, call is your direct and assertive assistant you tell them who is in charge and what arguments present and they call the functions immediately ok. Let me explain with a simple example ok. Most of these jargon sometimes people do not understand.

### 00:03:48 · Speaker 1

explaining you the example okay so where let's say we have a car object so car object has make and model what is the make and what is the model okay now we have a motorcycle function to which let's say we pass this car object we should be able to log this value okay so what i have done motorcycle i have a make i have a model and a start engine okay as soon as i call the function motorcycle dot start engine dot call i'm passing the car object so i have a dong i'm doing a console dot law this dot make and this

### 00:04:18 · Speaker 1

dot model correct in this case this dot make in this dot model whenever you are passing the car object as you all know this represents to this particular object with which object you are calling that is the this referring to okay let us say you call this function by motorcycle dot start engine dot call you will be getting make in model s tesla and model s okay let us say otherwise let us say you are not passing any object here just you are calling it then by default it will refer to this okay this example is for you to again understand the things slow

### 00:04:48 · Speaker 1

quite comfortably but let us understand a practical use case where do we use it let's take a scenario where let's say you are logging whenever there is some let's say user clicks on a particular button on the screen and you want to log that on to the you are some logging logging server you have wherever you are taking you're keeping a track for example you are using let's say Swiggy has built a application where how many times they want to know people is click on checkout button correct they might have kept some common function to log the event usually in a big project what happens there will be one common place such events are

### 00:05:18 · Speaker 1

and there we invoke from multiple different places. Because of that what will happen there will be some default parameters, some optional parameters like some parameters you have to pass, some parameters are like already available correct. So, let us say you do not pass that parameters they have to pass some default values. In that case is where you can use the call like for example make in model whatever you see there could be like a default values and whatever the start engine like log something whenever you call you could pass your own make in model or you can just opt to pass whatever is already present you can you do not need to pass whatever already part of the object.

### 00:05:48 · Speaker 1

get logged okay that's how you could use it is it the only way to log the values whenever you have whenever you have fixed parameter and optional parameters no there are different ways in typescript but this is also one of the way that you could use okay now let's go to the second one second one that is apply okay apply is more formal you provide a list of arguments to your assistant to distribute during the meeting function call okay like say you have a assistant you tell like let's say do this thing in a particular meeting that is equivalent to apply i'm going to explain how it is and just before you continue

### 00:06:18 · Speaker 1

further like all these questions will be freely available for you on my github repository or my new book or my blog somewhere so you don't have to worry about noting down everything will be available in the description okay so apply so apply let us take a simple example so we have a button so where we have a document or get element by id click me okay then we have a user a big object like for example user has a name update name is a function okay we are passing like this dot name is equal to new name we are doing okay let's say we have a button with whatever the button title was click me

### 00:06:48 · Speaker 1

me. Now you want to change that button item like button.addEventListener.click. Whenever somebody clicks on that button you want to change that button's name into carrier with wasent you could achieve it using this apply bind method ok. So, that is how you can use the bind. So, this is these are some of the practical examples for bind lot of you might know how to what is call apply and this is a practical example ok. Sorry this is a practical apply example for apply I missed I am sorry. Next is the bind ok. Bind is again according to me super important.

### 00:07:18 · Speaker 1

I have used it across multiple different places. So, I am going to give you an example. So, this is not the example that I have probably used in the practical project, but you could say, let's see that two arguments and one of the argument is let's say static. In TypeScript, you could specify a default value here, but if you are using plain JavaScript, there is no direct way to specify or you could specify it also, but that is not like the most beautiful way of doing it. So, but instead what we could do, calculate bind null comma 10. So, with this what we are doing, the value of the height we are setting it as 10 in this line in the bind. Further on whenever

### 00:07:48 · Speaker 1

you invoke the calculate area method they calculate with calculate with 10 further on every time you are invoking the value of height is always set to 10 okay that's the beauty of the bind method so future every time now the call and call apply bind you are using please remember these examples especially whenever using the bind the best example that you give is partial function application let's say a function has x number of arguments but some arguments are already have a default value that is the right use case for using the bind

### 00:08:18 · Speaker 1

Okay now let's go to access number two

### 00:08:21 · Speaker 1

Explain JS execution and event loops. It is very important and I have got like lot of mixed explanation on the online. So I want to give you a proper explanation that you need to tell in the interview. Okay. So let's say this is the whatever you are seeing on the screen, right? We have a function foo and function bar and const bar is equal to bar of 7. Why I told like there are lot of things that is available on the internet. The people who say like micro task queue, macro task queue, event, so many jargons that I never read on the official documentation. So I am going to explain everything that is only there on the official documentation which you

### 00:08:51 · Speaker 1

tell without any problem in the next interview so let's say we have the function foo followed by function bar and we have a const baz we are calling the bar a 7 as most of you might know this directly taken from the official documentation so i'm calling a function called bar and i'm passing a 7 here okay so whenever javascript encountered this particular function it has created a execution context okay execution context you think you can consider like a one box that contains everything for a function to get executed okay next this is done now as i don't encounter the bar it comes inside the

### 00:09:21 · Speaker 1

So, here we have another function called foo. So, foo is above correct. So, for that now another execution context is to be created correct. Once the execution context is created if you observe here whenever the bar came it added one frame into the event loop ok into the stack and whenever it encountered the foo it added another frame into the stack ok. And what would happen is let us say execute the foo frame because you calculate this and it returns the value and when this value is returned that particular

### 00:09:51 · Speaker 1

frame is popped out from the stack okay and then whenever this bar has completed the execution that frame is also popped out from the stack there be one global execution context once complete execution over that is also actually getting popped out from the stack okay now there is another thing called heap correct as you are observing there is another thing called heap what is heap heap is a largely unstructured uh storage probably it could be from like either from the rams memory rom memory or it is from the hard disk it could be from anywhere the browser the whatever the memory that browser could access

### 00:10:21 · Speaker 1

spread across different different storages that we are calling here as a heap okay whenever any asynchronous task like set time or set interval such things come they go and sit into this heap memory it could be from any memory location putting other way once they complete the execution they come and sit in this uh this messages queue okay and whenever they come and sit in the messages queue and whenever this stack is empty javascript will start processing these messages okay a lot of people they say this do this

### 00:10:51 · Speaker 1

mistake where they say like messages are executed directly no they are not executed directly messages are actually moved from here to here they again messages are moved from queue to a stack because a fresh frame is created let's say you have a set time out instead there is a callback function like that consider that callback function as a frame that function is moved into stack and the javascript will execute that okay so don't get confused where the task will directly executed from the queue now last important point before i go to the next question is whatever the delay that you are giving into set

### 00:11:21 · Speaker 1

mode that is the minimum I think why you got the problem why it is because we have so many frames on the stack unless the stack is empty the queue will not get be getting executed correct so let's say your set time mode is completed and came as one of the messages here but the stack is not empty it will not execute after a specified duration of time okay so always remember the whatever the delay that you are passing into set time mode is not the delay it is the minimum delay that function need to get executed after which it should get executed okay now

### 00:11:51 · Speaker 1

Let us go to next question that is exit number three, where let and const okay again another super important interview question I have actually instead of like me explaining everything step by step I have actually documented them very much in this diagram I am going to put this diagram also in the repository so don't worry. So, feature scope where let and const scope where is a functional scope I think all of you know let is a block scope const is a block scope correct block scope means what which whatever the block they specified they can be only accessible within inside that block that do they can be cannot be redeclared.

### 00:12:21 · Speaker 1

Hoisting yes, where is hoisted declare at the top let is also hoisted const is also hoisted. Hoisting initialization yes, only where I have got initialized with that undefined. In case if you do not know hoisting in depth, I have made a beautiful video, the link to video in the screen also in the description section, please go ahead and check it out. Hoisting where yes, initialized to undefined let no const no. Both have hoisted but they do not have a default value. They will be as you all know in a temporal dead zone where their value cannot be accessed.

### 00:12:51 · Speaker 1

controlled zone that also I have clearly explained please watch the video and third thing is the reinitialization where can be reinitialized yes let can be reinitialized yes reinitialized here reinitialized here we mean let us say let x equal to 10 x can be later redeclared to 20 same applies for where but const we cannot do it as the very word indicates const is something constant we cannot change it correct and last thing is the initialization where required let not required const required let us say you create a variable called let x you do not have to define a value to it

### 00:13:21 · Speaker 1

You do not have to initialize it, correct? And in case of var as well, but const should have a value. Without declaring a value, you cannot use a value. You cannot create a variable. Reason for that is also again simple. It is a constant value. You cannot change it later. So, whenever you create it, you should create a, you take the value. So, everywhere wherever possible, please use const as much as possible. What is the reason? Because it already have a predefined value. So, execution is very simple with respect to this. So, JavaScript, once it creates that, as long as it has the reference, it will not be like garbage collected and the value will not

### 00:13:51 · Speaker 1

So always use const wherever possible. I think most of you might have already stopped using the wire. I am sure in couple of reasons wire might get totally removed from the support from the new versions of the ES. But I think only because of the some old apps that are still using the wire, I think it is still have support. Okay. Now.

### 00:14:08 · Speaker 1

Let's go to exercise number four. Very, very important question, okay? I'm sure like lot of you might have not aware of this particular question. First, as soon as I have encountered this question, I myself actually stand like what is this question? See, explain primitive types in JavaScript beyond the number, string, and Boolean. As soon as they ask like explain primitive types in JavaScript, the first thing that comes to our mind is like string, Boolean, and the number, correct? What are primitive data types in JavaScript? They are building blocks that represent simple indivisible piece of data, okay?

### 00:14:38 · Speaker 1

individual piece indivisible piece of data we mean what for example object has first name and last name so first name and last name can be divided and assigned to new block correct but whereas let's say if if you put like let x equal to 10 that is indivisible x is 10 no matter what x is always 10 correct that's what we are telling as a primitive data types in javascript okay so all we know most of us would know is primitive data types are just string boolean and number these are the only data types probably most of us would know but there are other primitive data types i realized okay first one is symbol

### 00:15:08 · Speaker 1

Second one is beginint, third one is undefined, fourth one is null. Okay, nobody might have thought like undefined and null is also primitive data type. Okay, I'm gonna explain now. So symbol, I being very frank, I have never used symbol so far any of in my project. I actually searched across a lot of Jani and other tools as well. Nowhere I found like lot of information about symbol. Like I don't see like most of us are using symbol. What symbol is actually a unique and immutable identifier useful for creating a private properties within an object.

### 00:15:38 · Speaker 1

or for creating unique is in an object okay why putting in very simple but let's say you have unique symbol 1 unique symbol 2 we have created a simple and we have passed this correct see what we have done we have we have two strings okay which actually have the same value if we use the same string probably this would have not probably this would have become true correct if unique symbol 1 is equal to this unique symbol unique symbol 2 is equal to this unique symbol both would have been equated to true correct but just because you are creating with the help of a symbol now both

### 00:16:08 · Speaker 1

are not equal false symbols are always unique okay so let me zoom in a bit so that for you guys reading becomes little easy so symbols are always unique so when we could actually use it is let's say in javascript we are using multiple libraries whatever the key that we are using somewhere might have been used for the other representation also for example you're using a key like username user underscore name that user underscore name might have been used by the other module also so you have if you have to be sure like nobody else is using it just

### 00:16:38 · Speaker 1

pass that to symbol. So, that symbol of user underscore name is not equal to somewhere else whatever they are representing ok that is a user symbol I have not used it again I recommend if there is any opportunity like this please use it I think again you got the point let us say you have two I uh two constant variables with not variable let us say two constant things strings with the same name ah bar you want to protect your name because there is somebody you are using a big project where somebody else might have used that. So, always pass that it within the symbol ok.

### 00:17:08 · Speaker 1

Next is Beginint. I have made a beautiful video about Beginint where one of the Facebook interview question that I have asked again link to that I put here also in the description section. So where Beginint

### 00:17:19 · Speaker 1

By default whenever we use number right we represent a 64 bit number 64 bit floating point number whenever we are we are telling about a number. But whenever we are telling about a big int it is actually a much bigger number whenever we have to represent a very big number right we will be using the big int. So, this is also a primitive type ok this is actually this is introduced in the ES 2020. So, primarily where we could use let us say we what is the factorial of 10 I am sure most of you cannot tell because a very big number such numbers cannot be kept within the ah number variable ok. So, we have to use

### 00:17:49 · Speaker 1

the begin in that case. Undefined and null they are also primitive types because they are unchangeable correct or indivisible. What is undefined and null difference that also I am going to quickly tell. Undefined whenever you create a variable and it is not initialized with anything then that particular variable is undefined. Null is not like that. Null you are defining a value you are telling like there is nothing. Undefined you are not saying so by default it is we are considering you are not defined anything. Null is the exact value that you are telling ah that is the only difference okay both probably

### 00:18:19 · Speaker 1

represent nothing but they don't have a they both have a different ASCII value and they both also represent the different thing so undefined you are not defined when you value null in very simple words represent you specifically saying there is nothing okay let's go to excel number five quickly so discuss begin and symbol data types in JavaScript their purpose and how use them again I've already explained this one of the other question that was asked in the interview okay now before I go to sixth question I'm sure you might have liked so far whatever the content I made if so please like the channel subscribe to my channel carry with us and that will help me

### 00:18:49 · Speaker 1

to make more content if you like the video more people would more impression I would get more impression means more view that will really help me to grow my channel that's the whole purpose of creating a channel is to help people to clear the interview that I put a lot of effort making such video and I don't I don't expect anything just other than your love so please love or show your love by following me and subscribing okay now let's go to exit number six

### 00:19:11 · Speaker 1

Explain the concept of sets, weak set, maps and weak maps in JavaScript and their use case for managing the collection. See, I am sure very few of you might have used sets in the very first place. Map also I think the same way. Array is something that all of us are using very extensively, correct? Now, let's go to thing like when to use sets and when to use maps. Then I explain the weak sets and the sets and weak set and weak map both. See, in very simple words, set is nothing but a unique collection of elements, correct?

### 00:19:41 · Speaker 1

For example, if you come here we have 1 2 3 1 2, it is an array, correct? So, array allows duplication of elements. Let us say you put the same value into set, set of numbers, then it actually becomes a unique array, only unique elements will be kept on the set, okay? So, where there is no duplication, duplication is not allowed in case of sets. But set only holds the primitive types, not primitive types actually it only holds like putting it only holds the primitive types, there is no object that can be kept on the set, it is not a key value.

### 00:20:11 · Speaker 1

It's only a value that you're gonna store on the sets. Okay, so what is a weak set? Weak set and set are almost the same. The only difference is with respect to the garbage collection. Set is like when I let's say you created a set and JavaScript would not immediately clear it from the memory. Whereas whenever you create a weak set, weak set scope is a small only within that particular scope like within this scope. Okay, so JavaScript let's say whenever it sees like there is no reference then it there is a chance that it

### 00:20:41 · Speaker 1

would clear certain elements within the set or the set itself. The only difference between weak set and a set is like how the garbage collection happens. In a set, as long as there are reference to any key within the set, the set reference is not removed or it is not garbage collected. Not necessarily like the entire set need to have any one key in the set if it is still having a reference also, it will not clear. But in case of the weak set, there is a chance where let us say there is one key is not having any reference.

### 00:21:11 · Speaker 1

reference like nobody's asking that value then there's a chance JavaScript might garbage collect it and next thing is a map map is a key value pair as the very word says in JavaScript or if you're from a Java background you know like there's a key value pair that we call it hash map same goes to the JavaScript where let's say you want to store a key value pair you created a map and you want to select one and the whatever the value that you need to store again is that one so one is a key here this is the value again you're storing a case Bob and you're storing the value the beauty of map is both not the

### 00:21:41 · Speaker 1

both not the both the key can be of any primitive type it's need not to be like a number he can be of type number he can be of type string okay or other other different primitive types but actually makes sense is actually number and string are the one that makes sense as a key value can be again object any anything actually it can be object it can be array it can be any of the primitive type non-primitive type all of that are allowed so when you would use it I'll give you a beautiful example let's say you have a list of users like 100 users are there and let's say user is searching something every

### 00:22:11 · Speaker 1

Every time whenever you perform the search you need to extract certain values and show it correct. If you use an array every time you need to perform filter. Instead if you use a map you could exactly go and pick that key the operation is big of 1. In case of array the operation is big of n ok. In all the cases please use the map. Use extensively so that your code will looks more and more proficient by using the map. Again what is the weak map? Again the primary difference is that only where the garbage collection where as long as any particular element is not having

### 00:22:41 · Speaker 1

reference in a weak map that can get removed from the can be garbage collected here it is not it will not be like as long as at least one is having a reference no keys or in the entire map itself is also is not removed from the memory that's all about map weak map sets and a weak set this is very important for interview also for your day-to-day activity i highly recommend like please understand this concept in depth so that it's not just for the interview just for your day-to-day learning now let's go to question number seven a very important question again so demonstrate removing duplicates from the sorted

### 00:23:11 · Speaker 1

using both set and well and javascript method let's understand like how actually this question works so basically what is asked let's say we have given an array that has the duplicate elements what we need to do is we need to return a array that has only unique elements correct what we are doing is the one approach is set as i already explained set basically contains only unique elements correct so where we have one two three one two four we are creating just new set of numbers we pass it to it okay then we are getting unique numbers array whatever the set we had we're just spreading it to make it into array and we are returning it very simple so the only thing that is set

### 00:23:41 · Speaker 1

advantages with this approach is you are creating a new set. So, the memory is doubled correct because almost except the duplicate elements whatever the memory that numbers would take the same is also taken by the set as well correct. And we are also forming another array here and to return maybe this can be avoided or sometimes the integer this cannot be considered like the space complexity, but definitely it is another big of n plus big of n that much space which again n space complexity is required to process this. The second approach is filter which is again interesting thing there are multiple ways actually

### 00:24:11 · Speaker 1

you how you could find using the default methods here I am using the filter and index of ok. So, how we are doing is let us say we are filtering value index and self value basically represent this index basically represent the index of the value self basically represent number itself ok. Now, what we checking a return self dot index of value is equal to index this is very interesting if you observe. So, index of will return the index of the value what where where it is present actually or the occurrence of it like for example, 1 right. So, it will tell like it is occurred on the

### 00:24:41 · Speaker 1

So it is having the one index. Let us say it is present in two indexes, correct? Then it index would index of it return two indexes where it is present. And if it is not at all present, it will return the minus one. So let us say if index of one is not one or that particular index, correct? So in that case, it is understood that the element is already present. So that is how we are doing the filter approach. Reduce we could use. We could use a simple for loop to remove the duplicate elements. Bubble sort also we could use. Many other approach. Not bubble sort. Actually, you could use any sorting techniques and then also

### 00:25:11 · Speaker 1

remove multiple approaches are there one approach i thought of explaining so this is round one of epam where they've asked around seven different questions in the interview i've already made round two and round three questions also it's already available on my folder all i want is the comment like if you want like me to make a round two and round three video again there are more very interesting questions this is just around around javascript round two and round three is also having the react js and some amount of the system design also if you want me to make video please mention in the comment section like the video subscribe to my channel that i'd be more than happy

### 00:25:41 · Speaker 1

make ma uh more such video about that

