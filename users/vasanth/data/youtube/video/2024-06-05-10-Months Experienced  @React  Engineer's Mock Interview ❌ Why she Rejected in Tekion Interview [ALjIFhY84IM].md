---
id: ALjIFhY84IM
title: "10-Months Experienced  @React  Engineer's Mock Interview \u274C Why she Rejected\
  \ in Tekion Interview"
url: https://www.youtube.com/watch?v=ALjIFhY84IM
date: '2024-06-05'
duration: 00:28:13
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---


# 10-Months Experienced  @React  Engineer's Mock Interview ❌ Why she Rejected in Tekion Interview


## Transcript

### Speaker 1

Paul welcome back to Keral with Vasant YouTube channel My name is Vasant With me today I have Shini As you know this is an interview series where were recording a lot of mock interview Shini is having around nine months of overall IT industry experience So this interview is primarily focused on fundamentals of JavaScript and React We are going to dig deeper into a lot of concepts So Im not going to take a lot of time on this But only the one thing that I would suggest is the best way to make utilize of this mock interview would be try to answer questions whenever asked to Shini and then go forward


I ask a question to Shiny you can pause the video you can try to answer yourself and every answer that Im giving wrong or if every answer that Shiny is struggling Im going to give all right answers to all of that at the end of the video So please watch the video till the end or end so it will be useful for everybody Okay Now Shiny if you can introduce yourself we can get started

### Speaker 2

Okay so hi my name is Shreemay and Im currently working as a front end developer at a mid site startup and I have around nine to ten months years of experience months of experience in front end development

### Speaker 1

Wonderful wonderful Shiny what is primary textbook of yours

### Speaker 2

family stack is known

### Speaker 1

Okay so youll

### Speaker 2

So they totally

### Speaker 1

You work on both front end and back end shiny

### Speaker 2

Mostly content sometimes its text

### Speaker 1

Its just a

### Speaker 2

which consists of node node and express

### Speaker 1

Yes wonderful wonderful Shani So can you share the screen Shani We can get started immediately Okay And for audience who are not subscribed to my channel I request you to subscribe to my channel So I will guarantee you do not regret Okay This is a very simple snippet Okay And my question is also very simple Lets say in line number nine you remove the hello world and you put the count What is going to be the output Line number nine Dont do it SFS you tell then we will make it

### Speaker 2

Okay okay so if I replace count here

### Speaker 1

In the meanwhile

### Speaker 2

It was the phone


It would be zero when the page loads initially and when after rendering the it will become one

### Speaker 1

Okay yeah I got in the behind this is how it work Lets say I run the code Im not gonna get a lot of differences 0 1 it will not become When I run the code Im gonna see some value on the screen What is that value


Okay please do it Line number nine Lets do it Remove hello world and put the count

### Speaker 2

Saving

### Speaker 1

I think you can refresh Yeah So we are seeing one Correct Shiny So now you explain me what happens behind this Whatever you started explaining right Please continue to that

### Speaker 2

So we


So behind the scene how use effect and use tilt works is first of all the initial value was zero The page got rendered with that zero value and it was it got rendered for very little time unless there was there and after that use effect got called as soon as it got rendered So use effect made it one and thats why we can see one and since like in use effect theres a dependency array which is empty which means only this will run once after the page


is rendered thats why only one we can see

### Speaker 1

Absolutely correct So there is a hook if you know that get executed before the use effect You know which hook is that


I tell the hook name you tell me whether that is right or not use layout effect you are have you heard the hook use layout effect

### Speaker 2

No honestly no I havent heard of this

### Speaker 1

Yeah you and the audience if you dont know what is usually out there please go ahead and read after the session So now lets do a small update to this Shani Okay Again line number nine remove the count and keep maybe again Hollowood in line number nine


So now copy paste the use effect again line number five to seven paste it again


Okay now tell me what will be the output save it you can save it and guess the output


Nothing will change yeah

### Speaker 2

And the


See both use effects will run so probably the output should be two

### Speaker 1

Hmm okay lets leave this hello world with the again count if we can yeah comment it and keep and we can keep reusing in future

### Speaker 2

Yeah

### Speaker 1

refresh on the right side

### Speaker 2

Ready for

### Speaker 1

Yeah yeah just right side Yes So were still getting one shiny You can tell me why it is still one

### Speaker 2

I suspect like the as soon as the like use effect is called both use effects will be called for sure this is for sure okay but I think the problem is with this set count like even though we are doing it on line nine it does not immediately update it update the state it takes some time thats why its coming once so suppose we are at line number six even though it updates the to one and when it comes to 10 its still not updated to one

### Speaker 1

Mm

### Speaker 2

It will think its still zero thats why it is making it one

### Speaker 1

So so problem

### Speaker 2

So problem with state updating delay

### Speaker 1

Got it Got it Got it Lets lets understand a little bit in depth Ashrini Okay So we have like two use effects now correct Use effect one and use effect two And both the use effects will run synchronously or asynchronously you tell me


Got my question right

### Speaker 2

Yeah I got your question


They run synchronously like one after the other

### Speaker 1

Okay so youre saying like line number five whatever user effect we have that is executed first followed by the user effect in line number nine correct One after another If execution is synchronous one after another then definitely the count value should be two right In line number 10 because that is completed the execution user effect because we are not doing any asynchronous operation correct So in line number 10 when it comes the value of count should be two like value of count should be one so it should become two the output of line number 10

### Speaker 2

Yeah right

### Speaker 1

Anyways like see the whole purpose of asking this question is not to you also First time when actually Im uploading a video today which is a first of June around 1pm the video is going to live I also where I myself discovered a lot of things about user effect in the video The first question is around this only So a lot of asking you or and the audience to just start thinking So its not like if you dont know answer to this you cannot build a good app correct Its just that like how we all understand the things to a level where which is comfortable enough to

### Speaker 2

Its like

### Speaker 1

correct sometimes you dont dig deeper and understand that is the reason so after the interview you and the candidates please go ahead and like understand depth i will also try to explain in the end like how probably this is working okay yeah now lets the that is how the use effect works but only one extension to this question i ask and then probably we will go to the next question lets say i want two now like by the execution of two use effects the value of count should be two do you think you can do some modification to make it two because right now though it is becoming one any modification


do you think of doing

### Speaker 2

Like here it should become one and then it should be here too Like if I do it two then also it can be on the screen it will appear two but thats not a good way right Thats not what youre expecting You want me to change something in this function five six seven

### Speaker 1

Yeah

### Speaker 2

Oh

### Speaker 1

Yeah either of the functions you make some correct change so that the count becomes actually two

### Speaker 2

What if I like stop the flow at line number six and force it to become one

### Speaker 1

how how youre gonna stop the execution at line number six

### Speaker 2

I think our in JavaScript helps with that

### Speaker 1

Okay you you want to make the set count operation you want to await until set timeout is done right

### Speaker 2

Yes yes yes

### Speaker 1

Actually we came into a good segue You tell me now actually how set timeout works behind the scenes sorry set state works behind the scenes right Is it a synchronous operation a synchronous operation How its gonna work behind the scenes

### Speaker 2

I think it is an asynchronous operation as we saw it was not updating the count immediately it was taking some time

### Speaker 1

So lets get into a little bit of the practical questions Sashrani Okay why do you think the set state operation is synchronous and not synchronous


In line number six we have that right Line number six Lets say do you do one enter there after line number six do an enter Lets say you put a consolelog here and try to log the value of count to what its gonna be


Divide it by zero

### Speaker 2

It wont it wont update it directly because said state is an asynchronous function every

### Speaker 1

Exactly So what we will do is 100 percent right chain I think most of audience might have experienced this because we all might have tried accessing the value of something immediately after it is set correct And we would not got the updated then we would have used user effect and update it correct You tell me now what is the problem Why you think React update the states in a synchronous way not in a synchronous way Okay no problem

### Speaker 2

So obviously because of it the agent does not want to block the main thread if he keeps on doing all the operations synchronously the main thread will be blocked it will become slow thats why asynchronous operations are done I guess

### Speaker 1

Okay sure sure Ill share another small snippet with you okay Copy the snippet and try to paste Very interesting snippet I think you can carefully copy only what is required okay

### Speaker 2

Uh okay so if I click on the click me button uh the zero is there it will become one okay and after three seconds I will get the alert which will say

### Speaker 1

Okay lets do click me once only click the button once

### Speaker 2

Let me say that

### Speaker 1

So were getting like embedded pieces and the value coming as zero correct Yeah The count is one on screen but on alert it is zero And its okay You look at the snippet and tell And if end goal is not getting the right answer end goal is giving the right explanation for the output Just look again and tell why zero is coming

### Speaker 2

Maybe its because rev it it is probably referencing the old state of


And why is it not updating it

### Speaker 1

Yeah so look at this snippet again and tell like probably why that is happening


You can click on you can close the alert click on okay hit close alert go back check again

### Speaker 2

Okay so as we know this is an async function So after some time interval update the state So its when it entered the set timeout set timeout it was still zero

### Speaker 1

Correct Which famous property of the JavaScript is used here

### Speaker 2

JavaScript property um

### Speaker 1

or JavaScript concept Tell me a few JavaScript concepts that you know One Ill give an example like hosting promises Give me some more examples

### Speaker 2

Closures

### Speaker 1

correct so you are able to guess so what is happening now now weve got to know it is happening because of closure and the previous value can you please elaborate shani

### Speaker 2

Whats happening is um okay so


It is entering this set timeout and it is taking this alert is forming a closure with the count value of the parent which is still zero which is still not updated

### Speaker 1

Yeah yeah

### Speaker 2

That that is right was giving us zero

### Speaker 1

Sure See whenever the closure get start the execution right Closure is nothing but what we are forming a execution context and keeping it aside Correct So whenever that time is done whatever is the callback function inside that block thats actually executing Correct So no matter now by the time the three second over even if you make count from zero to one million that block do not know what happened Correct This is the same as like popular that for loop and set timeout example Correct Same happens this way where the count value is only whatever it


noun at that time because of which we are getting the previous value okay now just as a little bit tickling the brain ill ask again lets say you click the button three times now dont click tell me what will happen

### Speaker 2

If I click it three times uh instead of zero it will be


that timeout


because its final closure with zero that timeout will probably you know give us zero three times in alert

### Speaker 1

Okay lets do it


F click three times


zero one two right not zero now you can again look back and explain what is happening

### Speaker 2

Gives it over


Okay so I clicked the button value was zero it entered here

### Speaker 1

Mm

### Speaker 2

So set timeout of somewhere running in the background to make it to one we entered set timeout alert was shown with zero

### Speaker 1

Mm hmm

### Speaker 2

In the meanwhile set count made it one

### Speaker 1

Perfect

### Speaker 2

Yes Yeah Count made it one in the meanwhile and then again button was pressed So it formed the closure now with the value one of the count

### Speaker 1

Correct Correct So basically every time whenever Im pressing one handle click multiple closures are getting not multiple every time one new closure is getting formed Correct The number of times you click the number of times the closure has formed Correct As simple as that So one practical question again Ill ask


What is the value that is returned from set timeout


Set timeout is a function right End of a day set timeout is a function set timeout set interval use state user if theyre all functions correct What is the value returned from set timeout

### Speaker 2

This alert is returned from here

### Speaker 1

Now alert is what is the callback function thats not return that is happening after three second right

### Speaker 2

that timeout okay I think it returns


timer something id timer id

### Speaker 1

Okay so Ill ask like one last question on this particular topic and we will move forward Lets say now every time whenever a new you are clicking a button like you told like its going to be just zero right I want to basically clear the timeout if the timer already exists and I should go forward How do you do that Lets say click the button once Okay that is the timeout as you could see line number seven to nine Correct That timer I want to clear And our second time whenever I click if that timer


Already there Only when timer is not there Im going to set the timer If timer is not already there Im just going to clear it

### Speaker 2

But its dark

### Speaker 1

How can we do that

### Speaker 2

So basically if timer is there clear it and then again set a set timer which is what you want me to do

### Speaker 1

Yes yes so every time you click like eight times

### Speaker 2

Everything alright by the way

### Speaker 1

You are actually gonna get only one alert because all the four you are cleared now Only fifth alert is gonna actually persist correct All the four timeouts have been cleared How can we do that

### Speaker 2

Again well need closures here

### Speaker 1

Mm hmm the closure already there September already there how we are gonna do yeah

### Speaker 2

The closure already there September


So what Ill do is Ill have make a timer first of all


which will be empty for now

### Speaker 1

Okay

### Speaker 2

And this is a timeout


is uh returning us a timer every time

### Speaker 1

Correct

### Speaker 2

And before this we need to see like if the timer exists just you know clear interval timer


But theres a catch we need to wrap this inside a function

### Speaker 1

Uh what

### Speaker 2

Because yeah because this timer we need to make the count of that timer right

### Speaker 1

No we need to mention only one instance right we have we need only one instance of timer we dont need like multiple instance like

### Speaker 2

No we have to maintain only one instance


to maybe make and make it have global

### Speaker 1

Okay sure So now

### Speaker 2

But not global

### Speaker 1

Hmm okay so you made it global you clicked on handle click function now correct were checking whether if if timer exist

### Speaker 2

I dont think so

### Speaker 1

If timer exists youre clearing the interval Why why for what reason clear interval function is used in line number nine

### Speaker 2

So if already a timer is set this function helps us to clear all the it is a cleaner function for that timer it clears all the side effects of that timer

### Speaker 1

Does it have a clear interval or clear time out

### Speaker 2

Kansas is a state


I think it should be clear timeout

### Speaker 1

Okay good job

### Speaker 2

Clear interval will probably use be used for set intervals we have another function

### Speaker 1

Yes I was setting the over Okay sure So now one last question I ask which you did not answer correctly was what is the return value of set timeout right Its not a timer or anything as such Its actually a numeric identifier

### Speaker 2

ID unique ID unique ID of that time

### Speaker 1

numerical it returns like zero one two three etc and youre gonna clear all of them uh like actually the clear timeout will clear only that interval that particular number if you want to clear all you can just click clear uh clear all timeout then youre gonna create all the numerical identifiers okay fine um ill share a small javascript snippet in the chat section copy the snippet and paste the snippet in the


Mm one second


Pay the simple in the other editor

### Speaker 2

Create counter one right

### Speaker 1

Exactly yes please paste the snippet on the JavaScript editor


Yeah you can remove everything thats here and paste it Again dont click on run Analyze the code carefully and I want to guess the output

### Speaker 2

Output would be um


One two one

### Speaker 1

One two one

### Speaker 2

One two one

### Speaker 1

Yeah yeah so

### Speaker 2

So reasonably lets just consider line number 11 We called a function create counter which is returning a function So counter one has a function there Okay And now we are calling counter one two times


So initially count value was zero

### Speaker 1

Correct

### Speaker 2

line number 14 we came inside line number six made it one and uh uh made it one and one was returned so this line will print one okay now this count value will have one because this is uh like this count value you know its forming a closure here again closure is used in this thing

### Speaker 1

So you just comment and type okay here its the one Second time youre invoking the same function where counter is already incremented So youre saying two correct And from counter two whenever youre trying

### Speaker 2

its one because again we are creating a new instance of that counter which will not have reference to the old values of count because a new instance is created so it will be one

### Speaker 1

Okay please run top center you see the run button there


whatever you told is correct shreeni okay so if you have to little dig deeper and understand so in line number 11 and line number 12 we are forming a two variables counter one and counter two correct both having a reference to create counter function itself but in line number 14 whenever you call the counter we actually the counter one is basically nothing but returning the function in line number five returning a function which has access to the outer scope because of the property of closure correct so whose value is actually initially zero so and it is


the updated count as its a post increment not a pre increment correct so we will be incrementing and well be getting the value as one and then whenever we invoke it to the second time we still have the access to the count that was declared in the outer scope which is already incremented correct so putting other way the closure of one is not affecting the closure property of the another sheen


Okay sure so yeah you can you can stop we can stop sharing the shini okay

### Speaker 2

Yeah


Just a minute yeah the screen sharing stopped

### Speaker 1

yeah screen shot okay now lets discuss some practical questions training okay so let me present a whiteboard okay see now the question here would be one lets take a practical example shini well like you might have not worked on it directly but there are a lot of uh one of the common interview question is how do you basically maintain a infinite scrolling list okay in a typical social media application okay lets say you have to build a list where the list is can be


continuously scrolled Tell me what are all things comes to your mind like what are all the problems that comes to your mind and how youre gonna solve the problems

### Speaker 2

Okay um


Infinite scrolling means infinite content infinite content means infinite calls to the server

### Speaker 1

Correct yes

### Speaker 2

Yes Right Yeah This is what comes to my mind right now Obviously we cannot you know just make it in the first go and then you know we have to do it on runtime The user scrolls and on runtime well probably try to make calls and bring data and display data This is what Im thinking of

### Speaker 1

Okay so just to unlock like as a basic UI Im drawing Okay lets say this is your website where this is the segment Like lets take a typical example of Facebook where we have like the center portion correct So this is the portion where we would be basically just rendering the colors correct

### Speaker 3

Its not looking good

### Speaker 1

Uh one second


So this is the center portion Im just drawing so this is the portion basically where we will be showing the content


So now lets say we have like multiple cards here right Like lets say theres one image one video and one problem textual content and users keep scrolling all right So we will have like a lot of data that should be flowing in Tell me like uh if you have to store so much of data what all things comes to your mind Shiny How youre gonna actually store the data efficiently Because you might know typical Instagram scrolling happens for about at least 10 to 15 minutes By that time we might have looked at easily like 50 40 50 reels


Correct If you start storing all the information in an array the array becomes bulkier What do you think should be the right way to store the information

### Speaker 2

First of all your question is are we getting a whole data like you tell me all of the

### Speaker 1

You tell me like Im telling I have to build a social media you should tell me what is the right way to store the data

### Speaker 2

okay yeah right so array we cannot use continuous it will take continuous memory space and you we dont know how much memory well you know well use because its runtime so one thing coming to my mind if we can use linked list okay where you know at least continuous memory space will not be used okay so and we can have nodes with where which will help us to backtrack also so if you scroll down you can go to the previous


which you were watching so the link this would be I think ideal thing here

### Speaker 1

Sure sure Shiny Okay And Im stopped Im stopped the whiteboard Shiny Okay Im mostly done from my end Before I give feedback if you have any questions Shiny regarding the interview you can ask me

### Speaker 2

no no major questions as such for the interview but you can tell me any one of the interesting most interesting thing you worked on in react or maybe you know like it just boggled you like oh this exists in react

### Speaker 1

So in the past I worked on a project where it was a mobile application using React Native which had a video call feature Okay So building a video call feature is very easy because nobody builds it from scratch There are so many open source libraries or paid libraries where they give you step by step instruction to integrate it So that portion of integrating video call is very easy but mobile has a lot of modes Like mobile has a when the app is in the foreground when the app is in the background when the app is killed Okay And all the three states should happen for both Android and iOS


So whenever you have to handle so many states lets say your screen is locked you cannot open your video call things because somebody need to unlock the screen correct So background foreground killed and screen locked four states available And all the four states need to be handled in the same way in both in case of both Android and iOS okay So this is around 2016 and 2017 when React Native did not have so much of documentation and not many are using it So we have to undergo a lot of things to understand like probably how it works under the whole window


a lot of native mobile code as well to unblock this but it took a good amount of time but end result was good we were able to achieve but probably if you do it now people do not take so much time because of jenny and so many other things its much straightforward but back then it was something very major thing okay


Considering the time concept Ill give my honest feedback whatever I felt regarding the interview right Some you might already know One thing that I ask you and most of the audience to look at it like from the system design point of view right I know you just have nine months of experience Its not like too much But dont look at any system as a consumer As you are a developer look at every system as a developer Lets say we are using Facebook or we are using Instagram right Lets look at it sometimes like how probably they might have solved this problem Like I gave a very common example


of book my show where book my show we render the different screen layouts like for example one one theater has more seat on the left no seat on the right we they have been just a walking path or all the seats on right or theres somewhere gap in the middle and theres sections like lower premium super premium there are some gaps in middle so to render this dynamic layout on the screen is a very tedious task correct but book my show solved it in a very simple way like only when you think from that point of view probably go and inspect their response and see how theyre sending


data correct same happened with the social media question i asked so you and everybody whos watching spend time as a developer whenever looking at product like that okay thats one simple feedback another feedback she needs dont jump to answer especially when the question looks simple


This is a trick that is used by most of the interviewers to keep a very simple snippet The second snippet where I extended the use effect right That snippet looks very simple and most obvious answer is two Our mind also says like we should not say two but we will not get a right justification for not saying it as two correct The two use effects that you used So my advice is whenever you think the snippet is simple and the answer is most obvious right Try to just think what is an unobvious thing because interviewer is also not that dumb He might not have given a very simple question correct


if again some simple question there could be some trick in that so try to decipher that and try to give the answer okay and the small feedback could be on a little bit on the analytical thinking like set interval set time out all of this right so probably working more towards it will help you to like master that uh these are all my my very basic feedback for you and whoever the audience watch and just in case for the audience who are watching all the question that i discussed are actually part of my video in the top 10 reactjs question that video im going to link in the comments


So this video is not going to have an extension where Im going to answer the question that video itself answers all your doubts Okay Any closing thoughts Shreene


Hope you like the video and whatever

### Speaker 2

Yeah I just enjoyed it I got to know about so many things about use effect and set in terms

### Speaker 1

Yeah


Thank you so much thank you all the audience who watched the video if youre not already subscribed to my channel Kare Bhai Thassam please subscribe and like the video and share it with your friends if you liked it thank you so much for watching catch you in the next video

### Speaker 2

Yes thank you so much
