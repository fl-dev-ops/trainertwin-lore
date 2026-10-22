---
id: AkApROv3N20
title: 100% sure, you cannot solve this Facebook/Meta Interview Question (MAANG series
  Pt 3)
url: https://www.youtube.com/watch?v=AkApROv3N20
date: '2022-06-18'
duration: 00:15:47
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_1: null
  speaker_2: null
---

speaker_1: Most of you would be thinking this is very easy So there is a function called clear all timeout and we can use that to clear all timeouts Correct Unfortunately there is nothing no function called clear all timeout

speaker_2: What is it They come

speaker_1: to uncommon geeks myself first and i hope you are all doing well so as you know this is a video series where we are discussing about a mang interview questions mang refers to metas slash facebook and apple amazon netflix and google the most common question that are asked in the front end developer interview in these questions im going to discuss in this particular video series so its highly beneficial if you are someone who targeting for these tire one companies they require you to prepare in a altogether different way the way have you prepared for a service company or a less paying product company and


these companies is totally different so the questions they ask is also different so unfortunately i have not interviewed by meta so far i have gathered a lot of interview questions from the interviewing platforms like glassdoor and cora and other stuffs and ill be discussing a lot of such questions along with tagging the companies which company is has asked these questions in the recent past and how to tackle it okay so first question in this series um in this particular video is from the facebook okay the question is


Implement clear all timeout functionality Okay Hope you all know what is clear timeout Basically it will use to clear the timeouts that whatever has been created in the past So whenever you do a set timeout the return value of a set timeout is an integer So that can be used as a passed as an argument to clear the timeouts So here the question is you have to clear all the timeouts that is present in a component Okay So most of you know why clearing a timeout is necessary because otherwise it will create in a memory leak


Lets say you navigate from page X to page Y but the whatever the set timeouts in page X are not cleared then what it does it will continue to take some memory location So lets say after you navigate the timeout is has timeout has been over and some process executing it will still execute in the background which is unintended Okay so you have to clear all the timeouts before navigating to the next page Okay so this is the purpose that why they ask this question Now most of you would be thinking this is very easy So there is a function called clear all timeout and we can use that to clear all


timeouts correct unfortunately there is nothing no function called clear all timeout okay so there is only function called clear timeout so just to start off with im showing you some information about the set timeout so this is the set timeout the global set timeout method sets a timer which executes a function or a specified piece of code once the timer expires so lets say you set a timer for one second after one second whatever the function that is inside the set timeout that get executed okay what is the return value the return uh is a timeout is


positive integer value that identifies them that identify the timer created by the call set timeout this can be passed to clear all timeout to cancel the timeout so you pass that id to a clear all timeout so clear timeout that will that will clear the timeout okay so if you come here to the clear timeout method okay so basically it takes the timeout id to clear so there is nothing called clear all timeout okay for your reference im just searching and showing okay there is nothing called clear all timeout so you have to write a clear all timeout on your own now


So before we start coding in fact I have already tried writing this code and come here Facebook questions are not so easy so that I can take it right away and code Okay Ive prepared and come So how should be a thought process Okay so to clear all the timeouts whatever it is first you should get hold of timeouts hold of set timeouts that have been created correct So one easiest way that comes to everyones mind is so therell be different timeouts created different function So there has to be one global variable which will keep track of all the timeouts


timers that have been created and whenever you are leaving a page in react you have something called componented unmount or if youre using hooks there is a return that you can write to whenever page is unmounted in angular also you have called ng on destroy so there are functions lifecycle method that get triggered on whenever youre leaving a page and from that point you can get all the ids youll be pushing into an array and whenever youre leaving the page you will call that array youll run the loop to the length of that array and clear all the timeouts okay this is should be one acceptable solution


Avoided interviewer is fine giving you some extra space Basically whenever you have to push array values set timers into array it will take some extra space Lets start with this solution first


What we are doing is we are creating one array called timer array


So Ive created one timer here Okay Now what Ill do Im creating const timer one is equal to set timeout Okay So here set timeout What Im doing here is Im setting a timeout for one second Okay Then Im creating a log inside timer one Okay Then what Im doing Im pushing timer one dot Sorry timer array dot push timer one Okay So as you know this will be a


numerical number that is written by the set timeout function Okay so we are pushing that into the timer array Same we will do for the second time Okay so inside timer two the variable name is also timer two and youre pushing timer two So now why I created var and not const just with the focus that it is something that is going to be accessed throughout the block you can you can use a const also because youre not changing a reference youre just pushing the values into it But I have preferred var as its a global or a function scope Okay


So now technically how in real time this happens is lets say this block is in one function this block in some another function In that case you can just create and push it into the global variable the instance of set timeout Now first let me execute it before I do the clear timeout


So after one second both the timers have been printed because both have a timeout of one


have to write a functionality to clear all these timeouts how you do is very straightforward you can use for loop or while loop okay Im using while so while timer array dot length okay what I will do then is clear clear timeout okay timer array dot pop okay you can use for loop also and iterate till the length the reason why Im using while loop is technically there should we will not know the how many timers have been created correct so Im running till the length of this


timer and I am extracting the last element one by one with help of timer dot pop okay so once all two two timers have been extracted it will be cleared okay just for your reference I am also showing what will be the value


timer of okay I cannot pop because since Im popping difficult to log okay but Ill show you how the values will be


timer timer 1 is timer 1 similarly timer


timer 2 okay so now let me execute these two will not execute timer 1 and timer 2 reason being uh javascript engine is very fast so before one second only this statement will be executed i think itll take just milliseconds to uh for these things to scan and uh it come to the while loop and it will clear all the timers very quickly okay so timer 1 was 2 timer 2 is 6 so number numerical number that is allocated to each of it and the clear timeout cleared the timeouts all the timeouts that created in a page


cleared okay this is one approach so this some interviewer will be accepting this but generally companies like Facebook would look for little optimal approach because this is something a mid level engineer can come up with most engineers can come up with is there any optimal solution than doing this the reason is lets say you have one container component and lot of sub components in that so now different components accessing one variable to push the values and finally clearing it is not something that is scalable going for


correct when the lot of components come it will be difficult so there has to be way where you can avoid this so when you have multiple components or multiple places inside a component using this timeout concept something should run in your mind okay so many things multiple contents or multiple components need one common entity correct so easiest way to think of is utility file you have to create one utility file that will take all the timeouts okay and that should also have a reference of all the timers that have been


Whenever you call the clear timeout whatever the functionality we did here clearing all the timeouts should happen there Okay So Ill show you that approach also And these are the two solutions that I thought of Second approach according to me is the optimal one which you should be writing in the interview This one probably right If any other normal companies are asking probably you can write this approach but not for the companies like Mangorfan Okay So solution is quite simple not so complicated


Probably what we can name timer util


So inside this this is an object that has a function called first you should have the timer array correct So timer array initialize to empty then you have set timeout


set timeout this is not the set timeout built in so this is the set timeout function that you are adding okay which has an anonymous function so what that does is it will create a timer every time whenever you invoke it okay so set timeout requires two things as you already saw one is a function another one is a delay so this function takes input as two things function


And here you actually create the JavaScript set timeout with function comma delay


Dont get confused This is same as this How you create a set timeout correct So where you have a function and you have a timeout number Same is actually been copied here Rather the function having the function someone is passing it So here the function itself is enclosed inside the set timeout In this particular block some caller will be calling the passing that function Okay that is only difference and delay as well


What you will do is you have to push this ID into an array


So timer array dot push ID Okay So that it get updated every time whenever you invoking set timeout you should keep adding the new ID that is got generated Correct Now now you have clear


Here also the same process whatever we did in the last state we can follow that while timer array dot


Clear timeout


Then timer array


pop so last value basically you are popping okay so this is now just an object okay unlike the previous code this is not a function this is just an object we created what you can do is you can export this object so that every function get an access to this now what we have is const now we have to create the first timeout okay how do I do that is timer timer utility


Dot set timeout it needs a function basically correct So Im passing a function


first timer and it requires a second argument so which is a delay so Im passing that delay also here okay now if I run this series okay so before I run this series before I run this code so if you are someone who is seriously preparing for JavaScript driven interviews whether it is React React JS React Native Vue any other technologies Ive created a beautiful two series one on the most common JavaScript interview questions how to tackle that another one is the custom implementation okay where most common custom implementation related question how to


implement array dot concat on your own how to implement array dot map string dot carrot okay so these are the implementations ive created a beautiful series please watch those two series and come to this kind of a series because it will be slightly advanced if youre preparing for the interview and all companies may not ask such questions okay so cover those two series first then come to this video ill try to add this somewhere on the screen as in the description section okay and if youre liking the content whatever im making on the youtube especially helping you guys to clear the interview please do like my youtube videos do not forget to subscribe to my


channel uncommon geeks and share these videos along with your friends so that they also get benefited okay now let me run the code


So Im running See I have not cleared the timeout intentionally but I just have created a set timeout So if I run the code only the first timer is being printed Okay Similarly I can create a second timer Okay Second timer If you want for reference you can return the ID also from here I dont see any point so Im not returning an ID Okay So Im running So you get first timer and second timer also Now what you do is you just simply invoke timer utility dot clear


So this will trigger this method so which will clear all the time modes Let me run this again


Okay first timer second timer So timer array dot length Okay I shouldnt be calling this dot clear all time but I should be just calling the clear timeout Ill tell you why So this dot clear timeout will invoke this function only Then it will be a recursion So there is no point You will not go anywhere So you should actually call the JavaScript clear timeout To avoid confusion probably you can set timeout something a function clear timeout function Inside this you can use the actual JavaScript clear timeout and set timeout Okay So this will to summarize so this is a block


you can export this utility method this is a timer utility is there right so you can write an export here okay in in react or angular in any other uh technology that you are using and you can use this variable from all the places no matter from where youre using use it from all the places lets say one one particular container you have inside which you have multiple components okay whether angular react view anywhere so whenever youre navigating from page x to page y what all things you want to unmount okay maybe the header bar remains


but only the middle portion get changed so on destroy of that or component did unmount of that just invoke this function okay so in that cases you it will clear all the timers and go to the next one if particular timeout need not to be clear so thats kind of an what if that how we can call this a little advanced kind of an approach where you can have the ids return from here and you can track the ids so for the clear timeout you can pass the ids what all ids need to be cleared okay you can extend this example to have a very profound solution so this


According to me its the best solution that one can write for clear all time out So have in mind with the both the solutions The reason being sometimes interview will have you the first one itself So you dont have to write the second one In case if it extends then write the second one also So this is like if youre taking biology in the PUC or first in the second PUC okay where you need to know there will be a lot of terminology so you should not know just one terminology referring one thing if you know more than one at least one youll remember in the exam similarly this so you should know more than one approaches


the interview will be definitely looking for more than one approaches okay so please practice both okay and ill be adding the solution to my github repository feel free to copy the code from there understand once again and probably you can continue coding on your own try to optimize it further as well okay thank you so much for watching my video catch you in the next one if youre liking the content that im making please do again subscribe to my channel like the video share this videos along with your friends read my medium blog cell data link that also in the description ive written articles like this beautiful articles like this and our weekly


basis on a lot of javascript concepts i have a good number of followers you two follow on me and add your comments for any article if you see some improvisations can be made okay thank you again catch you in next video
