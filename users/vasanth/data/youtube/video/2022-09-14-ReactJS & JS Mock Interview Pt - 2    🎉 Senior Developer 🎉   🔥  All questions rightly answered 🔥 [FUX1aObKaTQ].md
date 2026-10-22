---
id: FUX1aObKaTQ
title: "ReactJS & JS Mock Interview Pt - 2 |  \U0001F389 Senior Developer \U0001F389\
  \ | \U0001F525  All questions rightly answered \U0001F525"
url: https://www.youtube.com/watch?v=FUX1aObKaTQ
date: '2022-09-14'
duration: 00:39:16
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---


# ReactJS & JS Mock Interview Pt - 2 |  🎉 Senior Developer 🎉 | 🔥  All questions rightly answered 🔥


## Transcript

speaker_1: Hello all welcome back to Uncommon Geeks Myself Fasant I hope you all are doing well In case if you are seeing me for the first time on the internet I am a content creator I help people to clear the interview Like I always have made a lot of beautiful series in the past which has been appreciated by many Ill try to add link to those series somewhere on the screen also in the description section Please go ahead and watch it Any sort of interview you are preparing this will be definitely helpful for you Okay now as you already know I have got close to 1 point 1k subscribers on YouTube As a part of the love and the blessing that you have given and I have accomplished it in a very short span


Im trying to give something back So Im taking few free mock interviews Okay And in todays episode Ill be interviewing a very senior developer His name is Deepak So Ill be interviewing him Ill be interviewing as in Ill be taking the interview of him with a basic JavaScript and React Lets see how the interview goes Lets get started


Hi Deepak as you already know this is regarding the mock interview with JavaScript and React Ill start by giving basic introduction of mine then Ill take your introduction then Ill give a brief overview about the overall interview process then we shall get started Okay as you know Im Vasanth Im a YouTuber I work as a front end developer I have a good knowledge on both web and the mobile application development


And this interview very specifically as we have decided to be mock interview of JavaScript and React we have a half an hour time where in the first half let us try to delve into concepts where Ill be asking you a few questions on JavaScript and React concepts And remaining 15 minutes to 15 20 minutes Ill share certain snippets with you and you need to be predicting the output of it So whenever you are predicting Ill touch base on some more concepts in them


So thats all from my end regarding myself and the interview process can I please get you an introduction deepak your skills your aspirations yeah

speaker_2: Yeah sure So Im Deepak Chandani and I have around eight years of experience working as a full stack developer I started my journey from jQuery days and then I worked on different frameworks as JS ecosystem kept evolving So I worked on AngularJS and then I worked on BackboneJS And from past three or four years Ive been working in ReactJS majorly


So thats a brief about my journey and Im aspiring for product based companies where I can utilize my knowledge and work on some challenging steps that they are building Wonderful Thats what I want

speaker_1: Sure sure Deepak Clean net introduction Thanks for the same Okay Lets get started with the extreme basics Deepak Okay So please tell me what is hoisting in JavaScript

speaker_2: All right hosting hosting is so what happens is when JavaScript engine gets a program to be executed it runs it it runs that program in two phases So first one is the creation phase in which it basically scans what is inside the code and then the interpreter comes into a second phase which is the execution phase in which line by line it executes all the program that we have written


So in the creation phase what happens that first when we give a program file to an interpreter then in the creation phase all the variable declarations are hoisted to the top of the program So they are basically say suppose we have 10 lines in the program and on the fifth line you are creating a variable So on those top four lines what happens is you can use that variable X


in in those four lines why because hoisting is happening so javascript union uh creates a separate space for those variables even though they are defined at the bottom of the file but it in the scanning process it creates them and and declares them or initializes them with undefined value


This is hoisting basically

speaker_1: you said is absolutely right uh deepak ill just add certain variations to it uh you confirm whether what im im saying is right or wrong so hosting is a process like you said its uh moves to the top of the block so i ill add just small one more word into it does it really move the declaration to the top of the block or it just appears to move the declaration to the top of the block

speaker_2: It appears to

speaker_1: Why it appears to move and why it doesnt really move

speaker_2: It doesnt really moves I can say that


Um because it it doesnt really moves because we know that its not happening like the JavaScript engine is not changing the code that we have provided to him


Yeah so thats Im feeling

speaker_1: What youre saying is correct basically like you said it doesnt move because there is nobody sitting in the background who will take our variable from line number 8 and move it to line number 2 correct Just because of the memory allocation the variables can be accessed even before they are declared It seems to be like that correct So just the appearing not the actual moment Good


Please tell me what are closures sir the book

speaker_2: Yeah so closures in JavaScript happen when we have say suppose we have an outer function and we have an inner function Now that outer function is returning an inner function which will be later executed The inner will be later executed And what happens is because we know that the inner function will be executed later in some time but it can use some of the variables which were local to that outer function So the parent function


Correct And due to that JavaScript has to has to keep some closure So in this scenario closure happens where the even if the in outer function was execution was completed but still the inner function has access to the variables defined inside the outer function So thats a scenario where closures happen

speaker_1: Absolutely its absolutely right can you give me one real time example deepak where closures can be used

speaker_2: Yeah so Ive seen in some of the scenarios like


Um like there is a module pattern in JavaScript where what happens is people used to uh like we we we can create a module in which we want some private variables to be there and we want to return some of the functions which which we we want to expose them so that the user of those module can utilize those functions And in a simple example we can say that say suppose we have a function which has


counter and then it returns two functions for adding and deleting but the value of counter is accessible only to that module not to the external user


This is

speaker_1: is the right can you give me an any practical example that you think of this one you said is fine anything maybe in a little broader perspective you know anything

speaker_2: I think one example can be where we where I actually use where we all use it regularly is that in react what happens we create a hook or we create a component and in that component


we create a function or say suppose we are creating a custom component custom hook sorry


In that we we create a variable but we have access to that variable inside some of the utility functions which we are returning from that custom hook


So say suppose you are creating a custom hook to fetch something fetch from say suppose use fetch And in that you create some is loading and other variables or other state variables And those state variables can be used inside the click handlers also So what essentially we are doing is we are using a local variable of the parent function that is outer function inside an inner one

speaker_1: Yeah I mean not wrong uh can it can be little improvised but no no issues deep down can it invert its function currying in JavaScript C U R Y I N G currying

speaker_2: Okay um currying is


Yeah so in currying what happens is we say suppose we have a function which takes some arguments and then uh


we want that function to be partially executed so say suppose like it Ill take an example and that will make it easier so suppose we have an add function and add function takes multiple arguments lets say three or four arguments


And we want to curry it So in currying what happens is when you pass that function from a curried function then what we get is a new function which can be invoked with single parameter So say suppose A B C were passed to the original function and the curried function can be executed partially So you can pass one and then two


And then it will return a new function which can be invoked by passing three

speaker_1: Correct correct What you said is correct Basically currying is not like a fundamental concept Like there is not much of a documentation related to it in developer Mozilla So it doesnt have an appropriate definition Like what you explained was right I am coming that way Because many in the interview that try to find a definition there is no absolute definition as such So its more like explanation with a definition


Tell me what are pure components and reactant

speaker_2: Yeah so


components in react okay so


Yeah so in React what happens is whenever we change the props whenever a components prop is changed or a state is changed state is inside that component only but props are passed from outside So whenever the prop is changed so the parent component might be providing some prop and then later on it provided new value of that prop that time component re renders


And usually what happens is its a default behavior but sometimes what we want is we want that component to re render only when we receive a new prop a new value of the prop And we want to skip the re rendering whenever the same props are being passed


So in that case we create a component we can say that the component that we want is a pure component which only re renders when the props are changing And by default in class components there is a pure component class from which we extend and create a new component

speaker_1: In functional components how you will create your components in functional components

speaker_2: This PR behavior can be achieved in in the functional uh components in React by using React

speaker_1: reactmemo you can definitely use for creating the functional component a pure components in with the help of functional component correct ill give ill ask you in practical example tell me lets say you have a pure component inside a parent component and you are passing a prop called x


The value of x was ten before


The parent component has re rendered Due to some reason the value of x has been changed from 10 to 10 again Some processing happened but x is still 10 But theres a set state of x has happened Okay Now will the pure component re render or not

speaker_2: Ill Ill need a a repeat of that sorry

speaker_1: So you have yeah theres a parent component and a child component inside that parent component

speaker_2: Oh you have

speaker_1: the child component is a pure component okay so child component is taking a prop called x okay whose value by default was 10 and during some processing uh the x value is recomputed but the even the recomputed value is also 10 okay but there is a set set state has been called for that x with a new value of 10 okay old also 10 new also 10 will the pure component re render or not

speaker_2: Okay so we have a child component which was previously also receiving 10 as a prop value And then again after later some computation 10 value was again passed to it

speaker_1: I got a problem


Correct correct

speaker_2: And that child component is a pure one Correct Okay So in this case it wont be re rendered I think

speaker_1: So Ill extend this example a little bit Lets say youre passing an object to the child component and the object is again reset to the same object value Will it re render or not

speaker_2: Yeah in case of objects what happens is if that object coming from the parent component is memoized or memoized one or not If its a memoized one so that means referentially the previous object and the new object that is being passed are equal Correct In that case it wont re render But if youre creating a new object referentially they are not equal then that will re render

speaker_1: What a what about functions


Youre passing function as a

speaker_2: the same yeah the same applies to functions also uh so if that function is the memoized one uh we can say its uh referring or pointing to the same function which was previously passed then uh re rendering will not happen

speaker_1: Wonderful what you say

speaker_2: is but if uh yeah youve got the answer

speaker_1: Yes exactly can you tell me what is component composition in react

speaker_2: All right component composition so in React what happens is


we can have a component which has uh generally what we do we create a component say suppose a list component and we create lis in uh ul and then inside that li this is all html composition


what in react the beauty is that we can create our own list component which can have list items a custom component so in a way what we are doing is we are creating a parent list list component and then we can create list items in that so those are custom components and the parent component can receive those children in a children prop

speaker_1: Can you give me one one realistic example where component composition can be used

speaker_2: Can you give me one one


Um


Generally I have seen in in some of the UI kits if I can say like in in react bootstrap or in material UI we see a lot of rows and then columns and then table so we create a parent table and inside that we create a row and then inside it we create a column this is a real example

speaker_1: But this is a real example More from the project point of view or something like that if you have to say whenever we are having kind of an embedding process lets say one is creating the entire container and somebody will embed the things inside that Correct For example some cards or some shopping related items So the one who create a container he doesnt bother Who will come tomorrow and insert the things Hell only worry about the containers So that with the help of compositions we can allow that Like if you dont pass anything Ill render this If you wish to pass something you can pass So just make sure my layout doesnt break


Correct good can you please open JS fiddle and

speaker_2: Yeah just one example I remembered is of the accordion So accordion can be a parent one and inside accordion we have different panels And accordion itself takes care of whichever panel is open or closed

speaker_1: Yes yes Deepak correct Yeah can you please open GS Fiddle and present your screen

speaker_2: Yeah just one second


Um


Spreading the screen


Its actually giving me error that um Im not the host thats why I cant

speaker_1: One sec one sec let me give you permission yeah can you try now


Zoom has added a lot of securities last year after the breach right Zoom has made it so so complicated to join

speaker_2: Alright


Not sure

speaker_1: Yes I can see your screen


So Im presenting Im sharing a code snippet in the zoom chart Please copy the snippet and paste that in the JavaScript editor Dont run the code


Can you zoom in a bit so that me and the audience can see it much better


Yeah maybe two more Two more times


Last one more one more yes


Please guess the output it can take two minutes and try to guess the output


Sorry to disturb you in the middle So in case if youre enjoying the session like how Deepak is answering and how Im asking the question please like the video and comment whatever you feel Like are you liking the mock interview or this could have been improved further Please add your comment By more likes and comment I get more impressions More impression means more people have a chance of watching my video When more people watch obviously this channel becomes popular and Ill be able to reach a lot of people So please like and comment about the video and continue watching further Thank you so much

speaker_2: we have a function here we have object object length and we have this function


increments of zero and then we are calling it


so we are calling objectmethod


And method inside this method we are passing fn to this fn and we call this fn


and this is called using this object so here this will be pointing to this object


So the length here length here could I think it should be five because this might be pointing to object


Uh okay


And then here we have arguments of zero and then we are calling it


So we are calling that function


Oh dear


Alright


inside we dont have this and here


This should go


Take care


Ive quickly done it Ill try to explain my thought process what I


First first can

speaker_3: First first confirm the output yeah first confirm what will be the output

speaker_2: So for for this first call


passing the function so inside this we are calling from here


So here the


We dont have anything


but by default it will be where it is being called so its being called from here so this will be fine


Cheers


This is again being called from here only not from the event


And inside is this is pointing to this object


This will also be fine Yeah so I think I should return

speaker_3: I am Shu

speaker_2: Yeah the yeah this will return five and this will also return time but I might be wrong

speaker_1: Here top left you see Ive done it

speaker_2: Excellent

speaker_1: Extreme left extreme left


Now top say left we have the URL


Yes yes please


So youre seeing the in bottom right youre seeing the output

speaker_2: Yeah ten and then two

speaker_1: Any idea why it turned into you can try to take a minute and try to deduce

speaker_2: So 10 I understand like this is returning 10 So what this means is this here is pointing to window actually I was thinking that its pointing to this object but this is pointing to window and the length variable is coming from the parent window object

speaker_4: Ready for this

speaker_2: Ready for this


Was that the right one

speaker_1: Yeah that is correct yes what youre saying is right


Basically it doesnt take objects reference because youre calling a function which is completely external Lets say there is a method inside the object like a method two which has a function and that you are invoking That time it will look for the reference in the object correct So now youre calling somewhere something altogether an external function So there is nothing of this objects this you are not passing So there this rep points to window okay Any idea why two is the print

speaker_2: Yeah so this one is interesting so we have fn and what its saying is we have two arguments passed to this


saying arguments of zero and invoking it


In arguments of zero we see that its fn


Can I finish


FN is called this way


So here what I see is this might be referring to that function


Yeah this might


referring to


Arguments of zero is an fn and fn is this


when this function is called its saying this functions length


Yeah what I can guess right now Im not sure Im right or wrong but I think in this case this is pointing to the function

speaker_1: Okay function as in the one that youre passing line number fourteen


The function that you are passing in line number fourteen is which is on line number two


I mean I dont know

speaker_2: I mean

speaker_1: How two can come


Do one thing in line number 14 after function comma 1 add comma 2


And number forty


After one day

speaker_3: Yeah one comma two

speaker_1: Now you get a sense

speaker_2: Exactly yeah so this is the method which is being tested

speaker_1: No objectmethod is in line number eight

speaker_2: Theyre taking

speaker_1: That only youre calling


So now how two became three you got a sense right how two is two turned into three

speaker_2: Or this is actually the ar arguments

speaker_1: So thats what I say Maybe even if you work with JavaScript our whole life not that you couldnt get none of us will be able to master it Im thinking There will be somewhere or the other edge case where we all miss Okay Good Ill share one last snippet with you Okay So that will


This is uh one moment Ill share


You just copy the snippet and paste there


Again you do please dont run

speaker_2: I can remove this

speaker_1: Yeah yeah


Please guess the output much straightforward

speaker_2: So we are creating a function self invoking it so


right to form here so well get one first of all


or straight away


Then these two will go in queue


as this is having both us at time out


So


Put us at time out this first one is zero so this should execute first


And then two that is after one second

speaker_1: Oh please


Youre confident in that

speaker_2: I know that

speaker_1: Its dark eh

speaker_2: Yeah I think I dont see any ticky thing here

speaker_1: Listen listen

speaker_2: Listen

speaker_1: So one four three two correct Lets do this In line number four whatever you have for line number four set time would just be basically a function right Can you convert that into a self invoking function

speaker_2: Alright so

speaker_1: Yes so you have to add one more brackets in the starting and the end


Now can you guess that

speaker_2: So basically this will be invoked immediately


Um


So well have one as previous and then


This will be immediately executed So this will give us three


then well have four and then well have two

speaker_1: Please explain why that will be immediately executed

speaker_2: Yeah so we what we have done is this part is creating a function and these two parameter parentheses are immediately executing that function

speaker_1: Sure as per event loop concept what should happen whenever set timeout is encountered

speaker_2: Thats pretty good


I missed that can you repeat it

speaker_1: As per event loop concept whenever a set timeout is encountered what should the JavaScript engine do Will it take it from call stack and move somewhere else or what is the process

speaker_2: Yeah so whenever set timeout is encountered


And whatever function is provided


that set timeout executes but this callback is moved into an queue and its a its a queue in which which will wait for this particular time to complete and then uh it the event loop will check if this if the call is the execution stack is empty or not if its empty then it will bring that pending callback into the stack and that will be executed

speaker_1: So now in this case set timeout is there inside that there is a self invoking function correct How come the function will execute immediately


Yeah directly into a call stack right it cannot directly take into call stack

speaker_2: Yeah

speaker_1: As per the explanation

speaker_2: So what I see here is like in the difference between line number three and four is that this is a reference to a function Consider it as a callback Got it But this is actually executed immediately

speaker_1: So in line number four instead of zero make it three second


Three double zero three second


Im not asking the output in this case now after three seconds something has to happen what will happen


So will a set time have to be registered or no

speaker_2: So this is a function and its written So the output of this expression would be undefined actually And what what what set timeout will be receiving is basically once this is executed it will be receiving undefined or void as we can see


So there is a chance that it might check that if undefined is passed as a callback to set timeout then it wont do anything

speaker_1: True true Correct What you said is absolutely right Deepak Okay Many get confused in this process First of all many will not be able to guess the output only the order of Even if theyre able to guess the order whenever a self involving function comes they get confused Okay Even after self involving function whenever this undefined kind of a concepts come they further get confused Youre able to answer all the things well Can you stop sharing


Yeah Deepak so we I mean I did not get to know how the time flew We almost finished half an hour already Okay So first please feel free to ask me Deepak if you have any questions for me


Not specifically from interview if you have any other questions also generally also you can ask yeah

speaker_2: I dont have any question right now

speaker_1: Just shed the

speaker_2: The car

speaker_1: good good i ill just give pass on my feedback every viewer also got my feedback i dont have to explicitly say it yeah uh i mean it was a very clean neat interview in not just the mock into that i take for the channel overall in my interview process very few will have very in depth knowledge okay and i think you will also be taking interviews a lot of candidate we there is a concept of the breadth and depth where people touch base on a lot of topics and they get in whenever they feel candidate might not be confident okay with my breadth and depth whatever i applied with you have good


of knowledge on all the concepts okay like a first thing always i say is the technical communication communication is one thing technical communication is very very important correct lets say when i ask you function currying you should you do not say like ill type and explain correct because as a developer our job is not just the coding we have you should be able to articulate our thoughts to a lot of folks correct so the technical communication part is very very good and the second part is the conceptual knowledge this is something that you uh upload in an engineer after a point like senior


engineer like you eight year ten year whenever some concepts come they should be able to articulate it well i mean explain the with help of concept like the pure component example which i might have asked like youre passing a function youre passing an object you clearly know what is happening under the hood that is something that will give a respect to engineer after a point correct just because if somebody becomes an architect people will not respect only because he has that kind of a knowledge then only people respect so fundamental knowledge is very very good third point is the uh the guessing the output the way the snippet


thing so first you were able unable to answer i mean partially you were right second you were able to answer clearly okay first question uh with my experience i havent seen anyone answering in the first go including me okay its not uh straightforward i mean obviously i i also dont say it is something with that we can judge an engineer but uh it also depends on how depth you have understood thats the only thing uh just because somebody says one gets the output wrong that doesnt mean theyre bad all right but only thing we just try to uh evaluate how depth they are able to understand or


Just connect between the thoughts Only that I can tell Maybe more snippet driven questions you can solve Rest seems to be good I mean if you are applying for tier 2 and tier 3 you are already there Maybe if you are applying for tier 1 you very well know Maybe you may have to practice if you are not done machine coding and the DSA Thats all I have to say Any other questions you have Deepak

speaker_2: No it was it was really good to communicate with you and doing this


Actually yeah actually the general thing is its always good to listen to someone who can give a feedback to you so Im Im happy with that

speaker_1: Yes yes Share Deepak Like I mentioned definitely Ill share a detailed feedback over the email And hope youre watching uncommon geeks Deepak my YouTube channel How are you thinking How the videos are coming

speaker_2: Its good And I would say most of us with most of us what happens is we we really we try very hard to understand things and then come up with our answers But we we dont know where a mistake is happening and where we need to work upon So this is and this this very much happens when you are in an early phase when youre learning some


and trying and Im hustling and doing all those things so that information is very valuable which you are passing in your channel that this is something which should you should work upon and this is your thought process this should be your thought process to explain a solution to any interviewer this is very valuable thing Im getting from your videos

speaker_1: Thank you thank you so much


the bug then we are almost at the end of the interview it was very nice talking to you i mean um you you are a senior engineer good that i could explore and i also learned a lot of things from you generally sometimes i get kind of very fast sometimes now now ive reduced a lot but even before the questions are people try to jump in and try to answer i had that attitude long way back but i see you whenever you come reading you are very matured like you wait until the question is fully asked that is one of the very important quality in interview you should never jump in correct you should fully listen to the question because interviewer


then say I was still explaining you jumped in correct so that we should have that patience um and the whenever total listening skills how the communication skills are important in the interview listening skills are also equally important I I that is something that I still working on and I I got to learn that from you further


Thank you very nice talking thank you have a good day bye

speaker_2: Thank you bye

speaker_1: Again welcome back I think hope you enjoyed the interview session with Deepak Deepak is a very senior engineer and he was able to answer all the different areas that I was asking the question whether it is conceptual whether it is technical communication or whether it is the problem solving depending on the snippets getting the output He was absolutely on top notch So like I mentioned he is almost at the he could easily clear most of the type two and type three interviews if he appeared to So Im very happy I could interview him as a senior to me as well I learned the sense like I mentioned I was a I got that


knowledge of being very calm in the interview Im still trying to be more better at it Sometimes I get quite enthu and Ill try to answer much quickly So but Deepak was very calm throughout the interview Might have absorbed him So where he he he waited for the question to complete He took his time Then he was trying to give a right answer So this is the strategy Some of you who are at least in junior and mid level will have a little more enthusiasm where they will not listen for the question completion So please dont do that Like how Deepak did properly in the interview


please follow this method of comment compost okay and if youre someone who is also looking for a free mock interview like this okay please register in the google form which is there in the comment section its very obvious ill not be able to take interview for all but whomsoever possible ill definitely try to take if not now in future like whenever i need some partners for my video ill definitely reach out to you i take very basic minimal details to contact you okay and if the form is inactive its an indication because somebody may watch this video after one year if the form is inactive its an indication im no longer taking the mock interview at that point in time


Okay thank you so much for watching If youre not like with that video please like the video comment whatever you felt in the mock interview Was it beneficial for you et cetera The question that I snipped that I asked in the interview that snippets are available in my GitHub repository Ill try to link that in the description Please go ahead and download the questions and practice on your own My medium blog URL is also in the description Please follow me on medium Almost every week I write a very interesting article which will be helpful for you to clear your interview in the front end domain So please follow me on medium and subscribe to my newsletter Star my GitHub project so that I can


Ill be able to make more add more content to my project and the project becomes visible whenever people search in the Google etc Okay Thank you so much for watching Catch you next video
