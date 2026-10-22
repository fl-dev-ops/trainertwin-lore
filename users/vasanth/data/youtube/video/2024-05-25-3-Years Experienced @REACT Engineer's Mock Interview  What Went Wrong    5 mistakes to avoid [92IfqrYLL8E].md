---
id: 92IfqrYLL8E
title: '3-Years Experienced @REACT Engineer''s Mock Interview: What Went Wrong? |
  5 mistakes to avoid'
url: https://www.youtube.com/watch?v=92IfqrYLL8E
date: '2024-05-25'
duration: 00:30:37
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
---

speaker_1: Hello all welcome back to career with person youtube channel my name is wasan the previous channel was known as uncommon geeks as you know this is a video series where i am doing a lot of mock interview with me today i have madhan more about madhan madhan himself will be telling so this is a mock interview where its gonna be purely based on javascript we are gonna discuss two fundamental javascript questions for next 30 minutes like i always say the best way to utilize this mock interview is like after i ask a question pause the video answer or solve the problem whatever i give


then resume the video and see whether your answer and answer given by mother is matching and at the end of the video ill try to give answers to all the questions that mother might have given a wrong answer or if hes given a right answer probably i will tell what was right or what was wrong so that you can get yourself clarified so make a best use of this and if youre not subscribed to my channel carry this person please subscribe and like the video youll not regret it and lets start now mother can you please introduce yourself

speaker_2: Yeah hi everyone So my name is Madhan I did graduated in 2020 I did Im from computer science background So I have totally three and a half years experience working in JavaScript So I have experience working in full stack applications as well And currently Im working as a front end developer

speaker_1: Wonderful wonderful Madhan So Madhan which place you are from

speaker_2: Im from Turchia as well

speaker_1: Richi is in Tamil Nadu correct

speaker_2: Yeah yeah so

speaker_1: Okay sure If any audience watching and there from Tamil Nadu please comment for the session comment in the add a comment So Ive shared a link with you Madan and open that link close any other tabs that are open Just open this tab and present your screen Lets get started It is time to answer

speaker_2: The screen is visible

speaker_1: Yes now its visible okay so Madan lets start with some extreme basics

speaker_2: Yes I know what she means

speaker_1: Okay maybe let the zoom be there Give one control plus itll be easy for the audience to see


Yes So tell me like what are polyfills modern


Have you heard the term polyfills P O L Y F I L L S polyfills

speaker_2: You


All of us are nonsense

speaker_1: You might have youre not heard also okay see

speaker_2: I have heard about it yes

speaker_1: Yes yes sure See another way to put that its like the most common term that I use obviously the custom implementation of the bulletin methods Okay For example theyll ask you to write like polyfill for arraymap arrayreduce arrayforage Have you ever encountered those questions or have you practiced them

speaker_2: Uh yeah got it Uh yeah So yeah mainly we will be uh I have a written few polyfills for array methods actually Wonderful

speaker_1: Wonderful wonderful if I ask you to write you sh will you be able to write

speaker_2: Uh yes uh some basic uh questions like

speaker_1: Sure sure Now well go to the writing part first but you tell me definitely a concept itself cannot be created for the interview correct The polyfill as a concept is definitely not introduced for somebody to ask in the interview correct It might have some other significance So where Im coming from is can you tell me why are polyfills essential


Or it is a custom implementation for a built in method right why it is necessary

speaker_2: Very difficult


So uh yeah I got it so um


Right now the array methods which we have doesnt actually may not match with our business logic or okay sometimes So when we are working in our projects so everything has some standards right Every software So maybe there some developers might have implemented array methods I mean custom implementation for this and


They might use their yeah

speaker_1: I agree So one reason could be like whatever you want that may not exist already So you built right add your own correct Definitely that is a use case But with my experience it has never happened Has it happened to you Like where you wanted something and that has never existed in the built in library Has it ever happened

speaker_2: Uh yeah yeah yes I have I do havent used it

speaker_1: Yes sure I mean youre telling you also never encountered a scenario correct Where you wanted a built in function and that doesnt exist Anyways because it may not be that way All of us try to achieve what we want using the built in methods Thats the usual tendency correct So that could be one reason obvious reason okay Any other reason that you can think of Madhan Okay lets start with a very extreme simple example Madhan Okay like arraymap Right now first write arraymap and give me a small example not polyfill


the array documents

speaker_2: Sure I think so let me create a dummy array


So for now I will use this map method and inside this I will have one array element So I will use this as an arrow function Here I will


return this array array element into two so I will implement multiply


This is uh multiply by two So if I lock this I will be getting an output uh two four and a six

speaker_1: Mm it does

speaker_2: Yeah

speaker_1: Mm

speaker_2: So basically this is creating a new array keeping this as an absolute one

speaker_1: Yeah then Im sure you are aware of the difference between map and forage What is the difference

speaker_2: Yeah forage doesnt actually create a new array map actually creates one new array

speaker_1: Absolutely Tell me a scenario like when well use a forage and when you will use map like try to come up with some practical scenario to just to differentiate

speaker_2: So uh yeah for each okay you you need some practical examples

speaker_1: Mm yeah if you know please tell me yes

speaker_2: Oh


Uh yes I dont have one practical example but the ideal scenario is when we just wanted to iterate over the array and uh do some calculations we will go with for each but we need to uh get on a new array out of that array something then we will be going with map

speaker_1: Okay sure sure Well get into these polyfills in a while Okay Ill share a small code snippet with you in the chat section Okay and I want you to look at the snippet and guess the output

speaker_2: And uh I want to


Yeah sure

speaker_1: Copy the code and put in the chat section and for the even the audience whoever is watching this you also just look at the snippet and pause the video and try to guess the output

speaker_2: so we will be removing this top yes so look at it carefully

speaker_1: Look at it carefully Take one to two minutes Okay And at the end of the day Im not expecting the right answer Im expecting a right explanation So you tell the output and I will not give you 100 marks I just want you to give a right explanation for that Okay

speaker_2: And uh


Yeah sure


Set time out it is actually an asynchronous browser API then we have a promise resolve


and okay okay listen i have

speaker_1: Yeah tell me what is output

speaker_2: so the output will be first this start log will be printed okay then we have set time out this is actually this will be going into this uh uh macro task and we will be the control will be reaching to line number five so here the promise is resolved immediately so inside promise will be logged then we will be uh the end will be printed then we this set time out log inside set time out


Printer

speaker_1: Good So start inside promise and end followed by inside set timeout correct

speaker_2: Yeah yeah

speaker_1: start inside promise and an inside timeout correct


Can you please run the code we will check start

speaker_2: Okay okay please


Okay

speaker_1: end inside promise and inside set timeout you can you can still like its no problem you tell me why do you think like this output is coming

speaker_2: Yeah okay So one thing for sure set timeout this will be moving to macro task And this promise is also I think its actually an asynchronous operation So thats why its getting logged after all the synchronous tasks are over

speaker_1: exactly so it may not be like uh giving the answers at the early like its not a process synchronously correct

speaker_2: Okay yeah okay correct

speaker_1: Okay sure Let me share another snippet with you So Im sharing the snippet here Again copy page the snippet and if you you can comment the snippet or even if you remove the snippet also no problem I can share with you after the recording the all the that Ive asked you

speaker_2: Yeah sure

speaker_1: yeah even the audience also look at the snippet try to guess the output for this

speaker_2: So I think this is kind of a closure So one we will be control will be reaching into this first outer function is called So inside outer function we are logging one And then we have one another function called inner So we are calling this inner function Inner function will also be logging one And then we are setting this variable x to two


Okay we already have variable named x equal to 1 So I think there is a possibility this might error on 8 but if not the error case the output will be 1 and 1

speaker_1: So we have two consolelog Im calling the outer function and inside outer function in line number three we are logging it And then the control would come to line number seven where we are calling the inner function Both the places we are logging the value of x only correct Yeah So in line number three you are saying what will be the output

speaker_2: Yeah so in line number three


Line number three the output will be one okay

speaker_1: Okay

speaker_2: And here as well the output will be one Then only we are logging actually x equal to two But if this suman is called after line number eight this could have been two

speaker_1: Okay run the code let us see

speaker_2: defined

speaker_1: Okay again like I told you can still check why it is undefined

speaker_2: like a tool


outer function is called


This is actually an uh this has the global scope So I dont have clear explanation Okay

speaker_1: Yeah this is something to do with the hoisting okay Concept of hoisting So you tell me explain more about hoisting Just lets stick to variable hoisting Tell me how the variable hoisting works

speaker_2: So there are actually three parts actually where a variable can be hosted at the global phase of one particular script function level and then the block level


So uh yeah and also there are

speaker_1: No so there are Im coming from is uh explain me like the hosting with respect to variable right variable with the const whether its hosted where and electric how theyre hosted please explain

speaker_2: We got it


Okay so let and const have a block scope So it cannot be actually if we declare a variable inside a block with let or const and if we try to access it outside that block we will be getting an undefined or an error out But there is actually globally posted and it can be accessed anywhere

speaker_1: So where is your global heartshot so you can access from anywhere you are saying manthan am i right

speaker_2: Yeah correct very good

speaker_1: So lets say there is a function block like line number two to line number nine Okay So there is a bad keyword inside that block

speaker_2: So that is a vacuum

speaker_1: So whether that variable is accessible throughout the block

speaker_2: And then


uh got it so the function is actually also holstered the functions are also actually posted by the time of this uh declaration of this outer function this where keyword is not actually uh declared thats why we are getting the error undefined

speaker_1: No youre not getting an error Youre not getting an error Okay So you you told about let and const hoisting right Tell me about variable hoisting variable created with the var keyword is hoisted or not

speaker_2: Youre not getting an edit


So uh yeah variable with back element is hosted

speaker_1: Okay variable contributed to where keyword is hoisted correct And what is the difference then between let const and where hoisting

speaker_2: So yeah as I mentioned let and const have a block scope where has that a global scope

speaker_1: Ill tell you another difference along with that a variable created with var keyword is hoisted and initialized with a value of undefined

speaker_2: Oh okay

speaker_1: Is that true or not

speaker_2: True or not


So that is by uh by uh by analyzing this function I think you are right actually

speaker_1: correct correct see undefined is not an error for you and the audience also im saying undefined is a value that expected value in this case


Sure So you can stop sharing Amadhan Okay So now let us understand like some some fundamentals of JavaScript Lets say now I want you to know how the JavaScript engine works The fundamentally right Lets say you wrote a code same code whatever we wrote just now and we want to execute that code Tell me step by step operations what will happen behind the scenes to execute the code

speaker_2: Uh okay So um yeah uh if we consider one script a main JS script or something so um the functions will be actually uh declared So there will be few functions and variables lets say So the variables and functions also will be declared Upon calling that uh one of the function uh the control will be going to that function


and doing that operation so it will be executed line by line and the synchronous javascript codes

speaker_1: No correct This is at a very very high level So I just wanted to understand a little bit in depth Ill give you some hints probably where Im going at mother Okay So whenever we have a JavaScript code first it goes to a parser A parser will generate an abstract syntax tree and then the further execution goes Any chance you are aware of this flow

speaker_2: Uh

speaker_1: Okay please read it You and the audience who is watching you can read more about this particular concept by going to the MDN official documentation Okay So tell me what is callback hell Madan

speaker_2: Please state it


Tell me


callback hill okay yeah so the prod the problem with this callback hills are actually the codes will be a little bit messier to uh read actually and adding any features on changes on top of it will be a bit difficult but uh and it is actually used to perform some asynchronous operations

speaker_1: Give me an example for callback Alec What is or can you give me one simple example


So call back in

speaker_2: Back in

speaker_1: No problem Ill ask you another simple question Okay Tell me what are promises in JavaScript

speaker_3: Yeah

speaker_2: So yeah promises in JavaScript is actually used to handle asynchronous operations So thats why we use promises

speaker_1: I dont want a bookish definition but give a very basic definition that you have understood what are promises

speaker_2: Okay so promises are generally used to fetch any service data HTTP calls or one main special common use cases may be this one

speaker_1: promise will thats not the exact definition you go and read after the interview okay so you are you aware of something called promiseall in javascript

speaker_2: I promise at all I know I have

speaker_1: Okay sure are are you aware of what are called higher order functions in JavaScript

speaker_2: Higher order functions uh yeah I have uh heard of them tell me what are

speaker_1: Tell me what are higher order functions

speaker_2: So there can be few functions actually Lets say some inner functions actually But we want to actually do some modification to functions Maybe I can put it as we have YouTube right YouTube application In YouTube application there will be grids actually Many grids will be present video grids


In that add section alone we will be having a few additional changes added on top of it Okay That might have been created with the higher order functions Yeah

speaker_1: Yeah I mean what youre saying is not fully wrong Madan All I want is a somewhat basic definition What do you think higher order functions are One basic definition like not bookish one Like you can give anything that you have understood right That way only you can narrate Tell me what is higher order functions

speaker_2: Adding some special capabilities or additional features to one common function is what I mean higher order functions and similar to higher order components as well

speaker_1: Okay not not fully correct Again this also you can go and check after the interview Okay So you know what is what are prototype chain in JavaScript

speaker_2: Prototype chain or prototypes

speaker_1: Or prototypes in general do you know what are prototype or prototypical inheritance

speaker_2: Uh no Im not having to no problem

speaker_1: No problem no problem you hope your average call apply by tomorrow

speaker_2: yeah it comes under a prototyping yeah

speaker_1: Yeah no yeah I mean but in general also its a very common interview topic will you be able to write an example for call apply and bind

speaker_2: Uh no something I need to

speaker_1: No problem no problem okay so

speaker_3: No problem no problem okay


Okay

speaker_1: No no no problem Like like I always say this right Interview is just a game There are things that you know There are things that I know If you are lucky then you will know what I know Thats all Correct Like lets say you start taking the interview Ill also not able to answer some questions Correct So whatever from my understanding and what is the commonly asked interview question right From that Im trying to ask some questions primarily Okay Now lets go back to the same question that I asked Now present your screen and write a polyfill for RAmap method and well end the interview Then Ill give my feedback And for audio


who want to write and dont know how to get started with polyfills there is a series of mine dedicated for writing polyfills ill put the link in the up as well as in the description section please go ahead and check polyfills basically are like he told creating the custom implementation for built in methods okay so even i i have written implementation for map method also

speaker_2: I think uh I need to actually


a refresh on this topic

speaker_1: You want to refresh the browser

speaker_2: Oh no I need to refresh on these topics

speaker_1: You want to refer to the concept is it Ok sure

speaker_3: to refer to the content

speaker_1: stop sharing madam lets lets get uh get ill give my relief for whatever we have had so far but just before i give my honest feedback about whatever i interacted with you so far if you have any questions in your mind please tell me madam

speaker_2: Uh no Santa I think uh this is actually uh good uh I uh got on where I stand so yes I think I need to refresh the content

speaker_1: Yes I think


Yes yes sure No problem Madan Like I told like theres a different level in the interview preparation Like whatever the level that you know you can clear some interview but theres some levels that you need to prepare for clearing some other interviews correct So Im gonna like like you already told my honest opinion is like this way Madan This might applicable for even the audience who is watching So fundamental concepts of you Madan whatever you know you know it well like whatever the concept that you know to a large extent you know it well but theres some concept which you dont know or you barely


know like for example uh the hosting question that i asked you know what is hosting but uh whenever i barely you know like you dont know completely so only youre not able to predict the output for the given snippet correct and even on the the whatever the array dot map polyfill that i asked right so dont do this mistake in the interview whenever youre not so comfortable youre writing so pick up those question where your probability of answering at least 70 percent you think you will be able to solve it otherwise there will be definitely a negative mark


you not picking opting for a question but you opt and dont answer then its going to be fully negative instead you can say like probably i dont know at the moment roughly i know if you want me to do write the skeleton ill be able to write but ill not be able to write it fully okay that way you can put instead of like accepting a problem and like not solving it and also like do not debug live like this this is applicable for you and the audience are watching like this the way you start debugging ive told in multiple times in my videos where you whenever you start debugging it creates an impression youre not confident


about your code mother uh i mean im not saying like we will not make mistake like in the day to day activity everybody do the debugging like this only in interview instead of debugging this way try to do the mental debugging uh like lets say you go to one level of logging not a problem dont put into like multiple level of logging and debug point etc try to do that in mind mapping and try to get probably where youre going wrong all right so that gives you like more confidence to the interviewer like mother is really aware of the concepts maybe small mistake he did so hes able to come up with a solution


that to that by putting couple of log statements okay dont get like too much too much of a debugging in the interviews

speaker_2: Yeah sure and

speaker_1: and uh yeah these are that a very very high level mother and some concepts like i asked you right like for example a prototypical inheritance call apply bind promise uh callback hell and all of and promise definition see all of these are like extremely basic question mother and i dont think you are gonna get away without answering these questions in the interview so you have to learn and theres no escape for this so whenever you are free please read these questions carefully before going to the next interview okay any other closing notes mother


Have any questions or yeah

speaker_2: yeah only one question so even though if we if i learned the uh i mean the real time implementation so you asked about promises and prototype call i play blind has well right even though i know the concepts and know to code that i also need to know that the real uh definition of that correct yes okay ill give you

speaker_1: Correct Yes Okay Ill give you a framework to actually read to you and again published audience also The framework of reading every concept is very simple Read the concept and understand the basic definition So this basic definition is very essential because see what is hoisting Hoisting the people give a lot of definition like a moving declaration on top of the block et cetera So the ideal definition is JavaScript engine because of this concept of like two part execution right It appears to move declaration to the top of the block


See there is a difference in APS to move declaration and move the declaration to the top of the block correct So people say like a white definition is not like a graduate students It is necessary because you understand the concept very clearly So first is definition Second is a bookish example Bookish example means the one on the MDM the very basic one you understand that third one is a practical example for your experience of around two to three point five years practical examples are not like very critical but somebody whos having five plus years they need to should be able to give practical example no


will ask you hosting like you create like variable x and try to do consolelog and tell x and x that is not an example for five plus years like you know the concepts where did you use it correct for example closure everybody know inner function has access to outer function variable that is not the use right so you are not learning for interview where you use it in your project so one definition one practical example one bookish example if you learn these three for every topic that you are studying you should be good for interview as well as your day to day work

speaker_2: Yeah Im sure

speaker_1: okay sure so it was very nice talking to you mother like i got to know a lot about you and whatever the interview question that i ask every interview i feel like a lot of learning for me also i assume you also like the session now mother

speaker_2: Yeah some tips are helpful I gotta know where I stand actually

speaker_1: Yes thank you so much Madhan So for audience who have watched the video and whoever were able to answer all the questions that I asked wonderful If you dont know the answer like Im going to answer all the questions that I asked in the next part of the video And if you not like the video please like and subscribe to my channel and comment Thank you so much Ill watch you in the next video So I think you have already watched the session with Madhan And in this particular short video post video where Ill be primarily explaining your answers to all the most of the questions that I asked Okay Let me start the explanation Ill not be answering


every basic question that I asked but primarily around the questions on the snippet driven or some of the important question that I asked in the video Im trying to answer here So this was the first snippet that I asked for Madhan So if I run the code the output for this is Im running the snippet So the output for this as you see like its start end inside promise and inside set timeout Okay The answer that Madhan had given initial answer was he had not considered he had given in a different order like start end and then he told inside


Sorry he had told start inside promise then end and inside timeout Because we consider like promiseresolve is resolving immediately Lets consider that as the next thing to be printed But right answer is whatever you are saying That is start end inside promise and inside timeout The reason for is very simple Like Ive told in multiple other videos of mine also where inside promise is basically executed first because it is an asynchronous task And even set timeout


also is an asynchronous task okay so whenever basically the browser or the js engine encounter this particular the promise line it will be executing that in asynchronous way as it is already resolved its going to be executed first compared to the set timeout okay so thats a simple explanation for this so keep this in your mind okay and another snippet that ive given to madan was this ive tried to explain this to a certain level in the uh in the video itself but im just giving you a little more explanation here so variable kit


with where keyword is hoisted and initially with the default value of undefined correct so variable created with latin cons are also hoisted but they are not issued with any value so you cannot use them unless they are declared as simple as that okay now if you look at this block i am calling a function called outer here and inside which in line number five i have a consolelog and in line number six i have an inner function in line number nine i have a method called inner okay and line number 10 i have variable x equal to two so if you look at a block from line number four to line number 11 i have a


variable called variable x okay and like i told whenever you have a variable inside a block that variable will be hoisted and the value of that variable will be initialized with a value of undefined only variable with wire keyword so anywhere in this block if you want to access the variable x you can access so the value of x would be undefined so there is also variable outside this corporate line number three thats the global variable whenever we have a global variable and a local variable always the prior is given to the local variable lets say local variable


is not there then the period will be given to the global variable so lets say if i run this code undefined why both are undefined is so in this entire block it knows the value of x as it has not come to line number 10 and line number 10 is the last line so that where the actual definition or variable x getting defined till that all are actually it is only declared with a value of undefined so here also it is 2 and here also it is undefined here also it is undefined lets say if this is not there then both


Both of them I might have printed the value of one Okay as you can see here Now the other important question that I asked in the interview was like polyfills correct So I asked like what are the reasons for creating the polyfills One right isnt he already gave in the video that we write the polyfills because lets say there is some implementation not readily available We will use the polyfills for that That is a right But in most cases that is not true because whatever you want is most of the cases are available The ideal reason why we would use polyfills is


there are browsers which dont support the newer methods of whatever is coming in Lets say we have a explorer and we have a new function that has been introduced and that particular function may not be supported in the old browser In such situations well try to mock those behavior by writing the polyfills So remember this And I ask you to write a forum custom implementation of arraymap method that Ive clearly explained in my playlist So were writing the custom implementation for built in methods


arraymap itself ive written here ive opened the video ill try to put this link somewhere in the description also in the seven the top of the video so please check this out another thing that i was asked in the interview was regarding the hosting concept that ive already explained but you want to understand hosting in detail you can go and check out this particular playlist document again i put this link also in the in the screen as well as in the chat section description section please go ahead and check it out and all the other question that i asked like prototypical inheritance closure related questions all of them are like readily available in this playlist this is the one place that you


refer 31 videos where you will should be able to clear most of the interview okay in this playlist please refer again im going to put this in chat section on also on the top of the screen thank you so much for watching if you still have any questions that are unclear for you mention that in the comment section ill be more than happy to answer them thank you so much catch you in the next video
