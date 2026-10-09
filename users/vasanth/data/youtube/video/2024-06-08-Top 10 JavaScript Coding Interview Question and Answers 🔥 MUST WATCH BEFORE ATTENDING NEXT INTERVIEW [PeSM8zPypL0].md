---
id: PeSM8zPypL0
title: "Top 10 JavaScript Coding Interview Question and Answers \U0001F525 MUST WATCH\
  \ BEFORE ATTENDING NEXT INTERVIEW"
url: https://www.youtube.com/watch?v=PeSM8zPypL0
date: '2024-06-08'
duration: 00:23:32
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# Top 10 JavaScript Coding Interview Question and Answers 🔥 MUST WATCH BEFORE ATTENDING NEXT INTERVIEW


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So this is a very important video where I'm going to discuss top 10 snippet driven JavaScript interview question. These questions are of medium to hard difficulty. For freshers it's again close to hard difficulty. For experienced person it could be of medium to hard difficulty. So the whole point of making this video is not that you guess an output which is right or wrong. It's probably help you to understand the concept in in depth. So most of the time whenever snippet driven questions are asked in the interview, let's say the output could be a function that returns three and four.

### 00:00:30 · Speaker 1

and you'd say the output as four which is the right answer no interviewer will shortlist you you need to be able to justify why it is four and not three that's the whole purpose of the interview this particular session where i'm gonna basically explain the snippets and in depth like why that particular output is coming okay without wasting further time let's get started if you see me first time on the internet i'm was and i create content in front of an interview preparation please subscribe to my channel carry with us and let's get started so i have access number one here so where which is very simple looks very simple so where

### 00:01:00 · Speaker 1

have a create counter and we have like two variable counter one and counter two I could zoom little bit for make you little easy so we have a counter one count like variable called counter one variable called counter two and we have function create counter and we are calling it in line number 12 13 and 14 okay so where we are calling counter one counter one and counter two okay if you know the answer okay please mention like question number one and your answer in the comment section I'll be more than happy to review and tell whether that was the right answer or not if not definitely you can wait for my

### 00:01:30 · Speaker 1

answer okay so I'm running

### 00:01:34 · Speaker 1

So the output is 1, 2 and 1 ok. Like I told it is not about output, let us dig deeper like why it is 1, 2 and 1. So whenever you create a counter 1, we are calling this function called create counter which is returning this function correct. So if you know by the property of closure, this return function will have access to the count value. In very simple words, closure means inner function having access to the value of inner function having access to the outer scope variable correct.

### 00:02:04 · Speaker 1

very fancy terms lexical scope and all if inner function can access outer scope variable that is called closing very simple words so we are returning a function and that function is basically is present on the counter correct so here if you see whenever you're calling the counter first time you're nothing but you're invoking this function correct which is actually returning the value of count after incrementing it so value of count was 0 before and after incrementing it's a post increment even if it would have been a pre increment same value i think we would have got so we are so the value of count became 1 here

### 00:02:34 · Speaker 1

We are calling the same function again because of the property of closure closure you know right consider closure like a box okay so that box knew the value of count 1 when that box was locked and whenever you call the box only then the value of box would change and you let's say the whatever was outside let's change to anything this box is unaffected okay consider it like a pilot and that whatever that one black box will be there right whenever the airport a flight crashes that black box basically captures all the information and it doesn't know what happened to flight whether it is flight landed

### 00:03:04 · Speaker 1

properly or it crash it only knows like capturing that way the closure is correct so now counter one basically giving the value of one and two because second time whenever you're working it knew the value counter go incremented by one now it's incrementing by one more which is making it to two and the thing is like counter two right counter two also returning the function the difference that you need to note here is whatever the counter one the closure formed that is different than whatever the counter two form the value of counter two whenever it is formed the count value is zero only so every time

### 00:03:34 · Speaker 1

it is creating a new instance basically okay so counter to the default value of count was 0 so it returned a value of 1 whenever you call it so let's say I call the counter to once again I would be getting the values same 1 and 2 okay I hope most of you were able to answer this correctly let's go to access number 2 okay which is slightly little more complicated but not like very complicated okay

### 00:03:58 · Speaker 1

So, we have a function called fetch data and we have something called a process data ok. So, fetch data as you can see I have mocked an API call implementation where I am returning a promise which basically sends a I have a set timeout inside that particular promise which wait for like one second and then I am have like constant data. So, where I am resolving the data ok and I have a process data which is again returning another promise ok and inside this what I am actually doing is whatever the data that I have resolved I am making an upper case of it ok.

### 00:04:28 · Speaker 1

zoom out so that you can see the complete snippet once and from from this here line number 19 which is basically trigger point I am calling a function called fetch data passing this URL then to then I have and then I have a catch okay again if you know the answer please mention question number 2 and you are answering the comment section uh let me answer if you don't know if you are not able to answer like question by question at least by end of the video answer like how many questions you are able to answer correctly without watching my answer okay now if I have to give a right answer to this let

### 00:04:58 · Speaker 1

First let me run

### 00:05:01 · Speaker 1

So we waited for one second and then we got like data retrieved, correct? Let's see again. One, maybe then after that a 0.5 second, which is a 500 millisecond here. So then we got like data retrieved. So what happened? So first is like this then executed after fetch data. So fetch data basically took one second and it resolved the data, which is like data retrieved string. And then we came to the another then where we actually pass, no, I'm sorry. Then we came to the first then where we pass this process data that is data retrieved.

### 00:05:31 · Speaker 1

which took another 500 millisecond which is half a second and then actually all it did was it up it converted the value whatever you pass into uppercase and returned it okay and then we'll basically log it in another the then here okay putting other way you could see like the return value of a promise is passed to another promise okay see line number fetch data is a promise and if we returned a value that was passed to this line number 20 then and process data is another

### 00:06:01 · Speaker 1

promise okay so two promise we could call uh in this particular operation where you could got the value of the data retrieved so what is the takeaway from this let's say you would have used async and await right how you would have solved it you have to call await fetch data again you have to call await process data correct instead of that we could use just one promise dot then to like you can use only one promise and then two times to achieve whatever is required correct so this is the advantage of using the promises in some cases whenever you have to do the multiple operation depending on the promise response

### 00:06:31 · Speaker 1

okay we will quickly go to access number three looks very very simple if you know the answer again mention that in the comment section so we have like function greet and function say hi correct so you are calling the greet from the line number one and from line number 12 you are calling say hi okay what is the expected output for this we could even interpret without running as well so greet is a function normal function so which is hoisted so you can call it from anywhere basically so you are calling passing it as john so hello john will be printed

### 00:07:01 · Speaker 1

Say hi is a function which is a arrow function definitely it is not hoisted. So, whenever you you can call it only after it is getting declared. So, whenever you call from here you get hi there. So, hello John and hi there will be the output ok.

### 00:07:16 · Speaker 1

Hello John and hi there is output which is exactly as expected ok. Now let us say you have you want to make like understand the property of closure properly you can mention the say hi here ok which if you run

### 00:07:32 · Speaker 1

One second I did not say maybe carefully here you are saying like say hi before the initialization because say hi cannot be accessed before it's declared because the arrow functions are the function declaration this this block is basically is not hoisted so you're able to you'll not be able to call it even before it is cleared if you don't know hosting I have a very dedicated series on basics of JavaScript that link will be there in the description please go ahead and read please go ahead and watch that particular video where I explain the hosting in detail okay that link I'll put in the description if possible also on the screen so please go ahead

### 00:08:02 · Speaker 1

watch. Now I am going to access number 4. Okay. Very simple snippet, but you have to think very carefully before answering. Okay. So let me zoom in a bit. So I have a mystery function called mystery, which takes a value x could be of any type. So where I am checking like type of x is number. If number, then I am converting it to a string. Okay. See if you see here type of x is equal to number.

### 00:08:27 · Speaker 1

Okay, and then I have type of x equal to string, then I return the parse int of x. Okay, and then finally I'm returning unknown. Okay, if you're someone who never know what is the difference between parse int and number, but at least after this video go and check the difference between parse int and number. Both are used for actually type conversion, but there is a difference. That is also another important interview question. Okay, now, so now whenever I call a mixed tree, first I'm passing the true, second I'm passing an array, third I'm passing the null. Again, by now at least you some light has

### 00:08:57 · Speaker 1

In lambda your brain and you're able to answer please mention the question before and your answer if not let me run the code okay

### 00:09:06 · Speaker 1

So the answer for all is unknown definitely it is very straightforward lot of some of the times the snippets are unnecessarily complicated just to make you think like how calm your mind whenever you are interpreting the code mystery of passing the true if x is equal to x the type of x which is boolean is not equal to number it is not equal to string so we return this. So type here is an array again do not match both you are returning here type null null is also not a number not a string type of null so basically because of which we are returning as unknown all the cases only one.

### 00:09:36 · Speaker 1

question I have for you if you know the that mention question number four and tell what is the type of null in the comment section okay I'm not answering I want you to answer what is the type of null in the comment section okay so access number five is where we have something called a create increment so create increment returns two functions one is increment another one is log if you see here we have two functions one is increment another one is log okay we are calling the increment three times followed by we are calling the log okay so increment what we are doing we're incrementing the count every time and every

### 00:10:06 · Speaker 1

calling log your printing this message okay so if you know the answer mention question number five and put your output whatever the answer that you were able to interpret okay now let's look at the snippet carefully for those who have unable to answer it properly so the count which is deferred outside can be accessed inside because of the simple property of closure so whenever you call the create element the increment method whatever was written definitely it is having access to this outer variable count so every time whenever incrementing the value of count is

### 00:10:36 · Speaker 1

always incrementing correct so which is like it was 0 first like it remember the box example I told it was 0 first you call it again it became 1 you call it again it became 2 okay now now we'll go to let's let's run the code

### 00:10:51 · Speaker 1

X is number 5. Okay. So the count is 0 is coming which is little different than probably what you thought. Correct. Because the count was supposed to be we called it 1 which was became 1. Second time we called it became 2. Third time we called it became 3. So the log whenever you are printing it was supposed to be 3. Correct. Why it's not 3? So that is see these snippets lot of people ask me why you ask such snippets in the videos when we are not going to use it in the day to day activity.

### 00:11:21 · Speaker 1

this answer very carefully it is not like the same snippet you are going to use in your day to day work these snippets are created to understand how depth actually you are thinking correct or how keenly you are observing at something because let's say tomorrow you start you join the company and then you start working the most important point for you to like debug quickly and fix a bug if you cannot observe the snippets carefully you cannot debug carefully or you cannot debug debug quickly that is the whole point of asking such snippets in the interview okay now let us say what was happened whenever you call create increment

### 00:11:51 · Speaker 1

It returned two things, this and this. Meanwhile, even this line got executed, correct? Where the message was initialized with a value of count, which is the value 0. During the log, you are not printing the count, you are printing the message. So this is the observation that you need to have. So message was never updated. Only here it got called and message value remained as it is. So we are getting the value as 0. If you replace message by count, then probably the value...

### 00:12:21 · Speaker 1

So the value was 3, you got the point, y it was 0 and y it is 3, okay. Now let us go to another import nexus, access number 6.

### 00:12:34 · Speaker 1

Okay, so now x is number 6 we are. So where we are calling a function called test, we are trying to log a variable a which is dependent line number 5 whose value is 1. Okay, and then we have a function foo which is returning a value 2. Okay, and we are calling that function as well from line number 3. Okay, so we are calling that test. As soon as you call a test, the first thing that happens is console log of a whose value is actually

### 00:13:01 · Speaker 1

have to tell if you know the answer mention question number six and put that in the comment section i am going to explain in a while and then you are calling the function foo which is actually returning two so there is no doubt line number three would print two only because you are returning a numerical value so there is no brainer line number six will be printing two only line number two what it will be returning is the question as you know the variable created as var keyword is hoisted obviously hoisted and initialized the value of undefined so whenever this block is coming a actually went to the top and value of a

### 00:13:31 · Speaker 1

the undefined correct I think most of you are aware of this hoisting concept if you don't know again I'll link my video in the description section please go and watch it so undefined and 2 will be the output let's see whether I am I am right or not

### 00:13:44 · Speaker 1

As as I told it is undefined and 2 okay. Now let's go to the next snippet X is number 7.

### 00:13:51 · Speaker 1

This is very tricky, huh? I am sure at least some of you will not be able to answer it properly. If you are able to answer answer number seven correctly, please mention that in the comment section. Without taking much time, let's say in a minute you are able to guess this answer absolutely right with proper reasoning, consider you are like almost fit for most of the JavaScript related interviews. Okay? So where we have a simple object called person and person has a name which is Alice and we have a function called greet which is actually a function. Okay? What we are doing in line number seven, line number eight, we are calling

### 00:14:21 · Speaker 1

we are assigning person number greet to greet and then we are calling the greet okay function greet is basically printing hello my name is this dot name which is actually alice this my name is alice okay so now where basically this always refers to a caller as you very well know there is a priority of this i am not going to dig very most of you might have answered hello my name is alice as the answer let us see what is actually the output okay

### 00:14:39 · Speaker 2

Not going to take it

### 00:14:49 · Speaker 1

See output if you see here hello my name is undefined okay which is very important and very tricky I want you to like look at it carefully why like my name is undefined correct my name is undefined because whenever you int i like initialize person dot greet into this greet a separate variable right you understand things carefully like how this object is actually defined you see a name right this name is is basically person is an object where you are having a name and whose value is Elise

### 00:15:19 · Speaker 1

Then you have a grid which is actually referencing a function. So this function is actually referencing to a particular memory location. I hope you agree.

### 00:15:28 · Speaker 1

And that memory location is basically assigned to a variable called greet. Correct. So this memory location of this greet and name, they are all inside the person. Correct. So let's say whenever you call person.greet, not this way, I'm going to tell in a different way. That time it would reference the name which is a part of that object. The this would reference. In this case, what will happen is person.greet, whenever you're extracting, it is just like any other normal function, function reference. So variable greet will...

### 00:15:58 · Speaker 1

hold person dot reach which is pointing to a memory location in that case there is no this

### 00:16:05 · Speaker 1

So we are getting the value of this dot name is undefined. So we are getting hello my name is undefined. If you want the greet actually to know that you are a part of person then what you could do is we could bind it. Okay. We could bind this to a person. Let's say whenever we do this then it knows that that greet function belongs to the person object. In that case it would know name is actually Alice. Let me run the code. Okay. So you see like hello my name is Alice in this case. I hope you got the

### 00:16:35 · Speaker 1

the difference whenever you just assign person dot greet you are referencing actually a global function but whenever you bind it to that person then you are referencing to this particular object where the this dot name is defined okay so if you if you really answer this question properly with right explanation please mention that in the comment section like I told let us go to access number 8 very simple snippet looks very simple okay so where we are calling x equal to 1 and we have a function console dot log of 2 let x equal

### 00:17:05 · Speaker 1

to 2 ok we have 2 x here one is a global x one is a local x ok so whenever we have 2 x's or whenever you have 2 variable with same name which is also present on the global scope and which also present on the local scope you very well know the priority is given to the local scope. So, line number 5 whatever you define x equal to that has highest priority than this. So, now in line number 4 whatever console dot log of x we have it is definitely running with respect to the inside x. So, outer x you totally ignore. So, inner x is

### 00:17:35 · Speaker 1

probably producing the value what value it is producing is something you need to tell if you know the answer please mention that in the comment section if not let me execute the code okay

### 00:17:45 · Speaker 1

We are getting a reference error cannot access X before initialization you all know this ok. Property of hoisting again if you do not know watch my video. So, where I where it is clearly told like X is defined in line number 5 if you try to access it in line number 4 we get a reference error correct. Let us let us make a small tweak here which is like just for you to ah

### 00:18:05 · Speaker 1

Check like how much you know I am doing this. In this case, what will be the output? Can you try guessing?

### 00:18:12 · Speaker 1

I have not changed anything. I have not initialized x with anything. I have just written x in line number 4. I am trying to log it in line number 5. Okay. What will be the output? In that case, it is undefined. Correct. So, all variables that are declared and not initialized will give a value of undefined. Okay. I will go to access number 9. I have two variations of it just to like little bit tickle your mind. So, now I am actually doing a simple object destructuring here. A colon X, B colon Y and here I have A is equal to 1, B is equal to 1 and C is equal to 3. If you know the answer, I am sure.

### 00:18:42 · Speaker 1

most of you would be able to answer this correctly please mention that in the comment section so the answer would be very straightforward 1 and 2 because a we are assigning the value of a to a new variable called x we are assigning the value of b to a new variable called y so here in the right hand side a is 1 b is 2 so console.log x comma y which is like 1 comma 2 which is no-brainer correct let's do one very interesting thing here okay the second snippet

### 00:19:11 · Speaker 1

Let me zoom in a bit so that you could see it properly. So now you have a is equals to like again ax here you see 10. Most of you know it is a default value. Whenever a particular object you are not getting the actual value you are assigning it to a default value. Lot of cases you will be doing that in TypeScript whenever you have a variable function taking a variable you will define a default value to it. Let's say it's a string you define like empty string. It's a boolean you define like true or false as a default value. Okay so those arguments are actually not mandatory.

### 00:19:41 · Speaker 1

default value you could skip them ok. Now, a is equal to x you are assigning the value of a into x if there is no a then it will become 10 ok. But if there is a exist which is 1. So, value of x would be 1 here and we have y whose value is actually default values 20 but let us say b is also defined here with a value of undefined. So, b is undefined here. So, the value of y should be what you guess and we have a c who is actually which is actually

### 00:20:11 · Speaker 1

referencing the value of c is assigned to z but there is no c here correct c is not exist so default value is 30. So, x and z are already defined which is the value of x is 1 value of z is 30 because c has not present on the object. The only tricky part is y actually y is we are assigning the value of b b value is undefined. So, what will be the output you mentioned in the comment section if not please check my code now.

### 00:20:40 · Speaker 1

It is 1, 20 and 30. Okay. See, we have b here whose value is undefined. Still, it is not getting added to the object or the y here. The reason for that is the whole point of as a default value is whenever the value is undefined or like value is not at all passed, use the default value. Okay. Lot of people do not know this. So, because of which the we are, we are, though we present here, we are making, we are initializing the value as 20. But things from the practical

### 00:21:10 · Speaker 1

point of view why JavaScript somebody who developed this has made this feature would be

### 00:21:14 · Speaker 1

If it has a legit value of 20 or legit value of something there is a high chance the program would execute properly then initializing it with undefined because of which value of y is 20. Now let's go to last snippet, the tenth snippet.

### 00:21:29 · Speaker 1

So we have a return, we have a nursing function, okay, where we are awaiting inside that, where we are resolving the promise or resolve of hello. Immediately, almost immediately we would do this, but definitely JavaScript takes into event loop and all the concepts exist as you very well know. So where we are doing console.log of result and console.log of ubald, okay. So this is returning almost immediately because we are not keeping any set timeout or anything. This particular promise is written immediately, correct. So in this, the problem here is, or the crux of the problem,

### 00:21:59 · Speaker 1

is which log is executed first. This is almost an easy question for most of the middle level engineers. For a fresh head you can still think and tell what the order it would execute. Let me execute the code for you.

### 00:22:12 · Speaker 1

So it is world followed by hello. First we are printing the world and then we are printing the hello. That's the difference. The reason for that is despite it is returning almost immediately, JavaScript has certain keywords that have noun to it. Whenever such keywords appear, JavaScript thinks that these are the keywords that I need to process asynchronously. Because of which it will be keep moving those things to asynchronous block and it will execute the synchronous things first and then it will take that. Because of which world is printed first followed by the result. As simple as that.

### 00:22:42 · Speaker 1

snippet that I whatever I asked in the whatever I asked in the particular video I'm going to put that in my github repository or the new book that I'm publishing I'm going to part of that book and I put the link in the description section so that you can copy the snippets and practice on your own and that's all for the video if you like the video please like the video comment whatever you felt honestly please share the video with your friends so that they can also get benefited and if you're not subscribed to my channel carry with us more such content I'll be always putting you see videos are made once in a while but lot of such contents I'll be keep putting on my linkedin so you're not

### 00:23:12 · Speaker 1

my linkedin account please follow link in the link in the description section where i put lot of technical concepts on a day-to-day basis okay be a part of our telegram group where we have 3 900 plus front-end developers all across the world i'm going to share a lot of interesting things day-to-day and discussions cannot be we cannot make a video on that a lot of such good discussions happen in the group so be a part of that thank you so much for watching catch you in the next video

