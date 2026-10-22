---
id: 7a3ZwYko05s
title: Javascript Promise interview questions in 10 mins  (part 3)
url: https://www.youtube.com/watch?v=7a3ZwYko05s
date: '2022-05-05'
duration: 00:11:39
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_1: null
  speaker_2: null
---


# Javascript Promise interview questions in 10 mins  (part 3)


## Transcript

speaker_1: Hello all welcome back to Uncommon Geeks As you already know we are just continuing with our video series on promises I hope youre all doing well So in this video we are going to just extend whatever we left in our last video that is about the promise chaining how a promise inside a promise creates a problem gradually when we have a lot of promises being chained one inside another And what are the ways in which we can avoid that Okay without wasting further time lets get started See I am on a same set of


code whatever was written in the previous video and the same code okay so now what was the problem we are facing here is we have a list of promises one inside another so multiple promises we are calling and we are waiting for that input to output to come then we go calling the second promise and it has been continuous continued so this becomes very tedious to read and debug so how i can avoid that


So I will propose one solution that is using async and await Okay So first let me write the code Then Ill explain what are async and await how they can help us to not particularly avoid promise chaining So that cannot be avoided but how at least efficiently increase the readability of the code Okay So what Ill do Ill enclose all these functions all these promises inside a function


So I have this so and Ill return the promise one okay Ill return the promise one from this and similarly Ill create another function called function two


And from this function Ill return the second promise


Return promise


Then Im writing another function


And from this function Ill return the third prize whatever you have written


So here Ill return the promise three


So now Ill create a test function This I have hidden so to because Ill not be using the same So function


First let me complete the completely write the code then Ill explain what Im doing

speaker_2: Catch you later


Yeah


Enter


Response one equals to function


Then we have response to is equals to


Response three is equals to

speaker_1: Im less trying to log

speaker_2: Response

speaker_1: So this time what Ill do I rather returning promise one two or three I will return the numbers okay resolve one


And resolve


Here what I would do response is


Response one plus response


Plus response three


So


Maybe Ill just move to a next level const


z equals 2


logging the output here okay in case if you get any error


Errors


Now I will explain step by step what I did in this entire flow Okay Basically we had already had the promises Now what I have done I have just added a enclosed them inside a function


Im returning that promise whatever the promise that Ive created now Im returning that promise from this block okay so here Im using a concept of async okay one minute I missed it and await


What async and await does Ill explain you See async and await are just what we call them as a syntactic sugars A very fancy word syntactic sugars Okay Basically just to avoid writing all this junk of code promisethen promisethen promisethen keeping one inside another What we do here is we use a keyword called async and await So if you write a function to be await so this await whenever you type it will wait for an action to complete Same way what promisethen would have done So here we are using


await actually there are some differences between promise and async and await okay im not gonna touch base much on that because that is not specific i mean relevant for this video feel free to read there are very few basic difference between what promise and the async and await okay i im taking this on a very simple note where await basically means it will await until the this function is resolved


Then we have another await which will wait for this function to be resolved So what async does is whenever JavaScript encounters an async block so it will be ready to await for something Okay If you lets say you are awaiting for something without this async keyword then it will throw an error actually when you execute So you must have an async function Then you can use await inside that So await basically waits for this to finish Okay So in simple words async and await will not help you in any performance will not help you to avoid


promise chaining all the things whatever was happening before it will happen in the very same way only difference here is they will help you to it will help you to write a very clean code so rather having probably how many lines we wrote so probably from around 42 to 56 we wrote around of 14 lines of code and here we ended up having around 10 lines of code and in a very big programs you will still save a lot of lines because there will be a lot of functionalities that happening inside each promise okay so this is about the pro how we


use a sink and a way to avoid the promise chaining okay i mean at least in a readability way we can avoid it so if i execute this block now


Nothing is exac nothing is printing on the screen


in very first video of mine i guess related to hoisting i had i had asked this question many candidates do this mistake in the interview and i actually uh i i did not do this intentionally i also did this mistake by miss only so at least we must be able to figure out why nothing is printed on the screen immediately the reason being we see we have one two three four functions and we are not invoking any function


When were not invoking any function then what will be executed nothing so lets invoke test


If I execute this now


are getting responses six that is so first what happened it came here uh to first promise so first promise took one second to resolve and what we returned here is the one okay second promise took two seconds to resolve what we returned here is two after the promise result third promise took three seconds to resolve after the three second what we returned is three so here we have response one plus response two plus response t uh three plus two plus one which is equal to six so that is what getting printed here okay so


you got the output what is printed here So if I reduce from if I make everything this as zero like the promise executes immediately I mean in zero seconds it doesnt wait for anything but still the process is asynchronous only So if I put a log statement here that get executed first before the promise is resolved


Response six is this happened much quickly


Now problem is this three promise you are waiting response one response response wasnt why you enclose them in the type try catch block what will happen if you dont enclose that in the type try catch block so I want to show you that also so Im commenting this and Im pasting here lets say there is no catch


Or I believe all of you know aware of what is try catch Basically try catch used for the handling the exceptions So you try to do something and if that doesnt happen the way you are expecting then it will throw an exception that will be catched in the catch block Like we have an array of four indexes You are trying to access the 15th index Then that array element is not there So I mean array index out of bound exception will come That exception will be handled in the catch block So now we are doing this If I execute now nothing will fail Everything works fine


what Ill do in in function number one rather resolving Ill reject it


is basically Im showing you simple examples but in network call theres always a possibility that it will fail in that case what will happen see you will see some error like error thrown by exception error unhandled rejection so some rejection was thrown and we did not handle it so that is the reason whenever you do the promise chaining okay and since you cannot have it like a then and catch so each promise you cannot have a then and catch so together you can have a try catch like this okay its the easiest and the easiest way to handle the catch


Whenever any anything fails so youll be able to catch that in the catch block So now Ill execute this again So error is one So output So whatever was resolved we are able to know which block the error came correct So now we have to write the response to if you if you reject


An interesting thing


Try to guess the output if you know please mention this and in particular video time and mention your answer Ill tell whether its right or wrong If not you can see this video


So error is one actually rejected again Okay Here in the second block but it doesnt it did not go to that level The reason being we are inside a try and catch And as soon as any try fails any line this line this line any line it fails itll go to the catch block and that is the final or that is the end of the execution of this block


It will not continue further I mean once you go to catch come back to try and continue the execution that doesnt happen Because we only explicitly handling an exception Once exception is thrown that is the end of that execution block So now we one and two both are rejecting Now you will not be able to catch you know youll not be able to see what error thrown by the two So to just to if you have to avoid then you can resolve this Then probably we will get error is two So second block we will see the error


This is about the promise chaining how to avoid the promise chaining okay or syntactically how to make it look better So code readability will increase and the usage of async under it when to use async under it and when you are using async under it how to catch the error If there are any error comes how to handle that So all of them I have tried explaining in this video In the upcoming videos now what we are doing all the promise are executed in a sequential way one after the other Is there a way where we can execute the


promise in a parallel way because if our logic doesnt compel us to use it in a sequential way can use it in parallel way and the many other topics to touch base on the promise are they always so synchronous can they be synchronous also the promises so there are many interesting topics of the interview that can be asked on promise im going to touch base on all of that do not skip future videos watch all the videos about promise and become an expert in that okay thank you so much for watching my video if you like this video please do like it on my youtube channel and do not forget to share this video with your friends and please subscribe


to my YouTube channel UncommonGeeks okay thank you so much for watching catch you in next video
