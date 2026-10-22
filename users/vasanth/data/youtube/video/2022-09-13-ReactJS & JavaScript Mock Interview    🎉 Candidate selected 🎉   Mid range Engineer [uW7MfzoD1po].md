---
id: uW7MfzoD1po
title: "ReactJS & JavaScript Mock Interview |  \U0001F389 Candidate selected \U0001F389\
  \ | Mid range Engineer"
url: https://www.youtube.com/watch?v=uW7MfzoD1po
date: '2022-09-13'
duration: 00:37:25
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_1: null
  speaker_2: null
---

speaker_1: Hello all welcome back to Uncommon Geeks myself Asant I hope you all doing well In case if you see me first time on the internet Im a content creator I help people to clear their interview I made a lot of beautiful series in the past which has been appreciated by many And I thank you a lot Finally I have got now 1 point 1k subscriber And as a fact of 1 point 1k subscriber 1100 subscribers Im giving a free giveaway of taking a lot of mock interviews with respect to the front end And Ive posted this in my YouTube channel and I also posted it on my LinkedIn


good good number of registrations for the mock interview obviously i cannot take interview for all i picked few candidates where whom i can take a free mock interview and today im interviewing somebody called anubhu so hes im thinking hes in a junior to middle of an engineer whos aspiring for some premium companies okay lets see how the interview goes with


Hi Anubhav as you know Im Vasanth I own a YouTube channel called Uncommon Geeks Thanks for registering for the mock interview that I requested So as most of you know this is as a part of my 1k subscriber Im giving Im taking free free few mock interviews Thanks for the registering for same Can I know something about you Anubhav whatever you wish to share like what are your skill sets what sort of interview which companies that you are aspiring at the moment

speaker_2: So I have like total four years of experience as a full stack developer and the tech stacks that I work on mostly include JavaScript React HTML CSS on front end and on the back end I work usually with Nodejs and the companies that Im targeting basically Im looking forward to join some big product based companies

speaker_1: good good so that you are aspiring for big companies it is good you take some serious mock interviews like that so that you get the end to end preparation uh practice okay sure sure lets get started with extreme fundamentals okay so this is something that i generally ask in in the beginning of the interview so javascript is a single threaded interpreted programming language am i right or wrong

speaker_2: Yeah that is correct

speaker_1: So can you tell me what is interpretation in general

speaker_2: So interpretation is like one by one each line of code will get executed and then you will receive the output

speaker_1: Exactly absolutely right So can you tell me any interpreted language example other than JavaScript

speaker_2: I think Im


See

speaker_1: C is compiled C Java C Sharp all are compiled


problem okay so now if if javascript is interpreted line by line execution happens okay in general do you know how javascript code is executed the execution context and those things can you please elaborate

speaker_2: So we have this main stack wherein all the like statements that we have written in JavaScript are brought in and then we get the output basically on the terminal or browser where we want to see the output And basically event loop is the concept terminology behind all this which helps in managing and basically allocating different tasks in different queues that we have like we have the microtask queue as well as we have a other


a queue for web APIs as well so all of this is managed like if we have promises and so it will be put in the microcast queue if we have like a web API like set timeout so it is placed in a different queue and if we have console log statements so they are directly executed with the on the stack and rest are handled asynchronously and then we get the output

speaker_1: Great great

speaker_2: Yeah

speaker_1: it no event event loop concept is fine i am much interested in the uh the execution context how execution context is created how javascript lets say you create a file called one dot js okay there are some functions in it and youre calling the function some operations youre doing etc correct whenever you run this javascript on the browser correct so what all operations take place can you please try explaining that


As to what happens whenever the browser encounters yeah

speaker_2: So like from the first instance uh like so there are like two steps in which the java javascript like handles the execution of the code the first is like it will check yeah different functions and whatever variables are there so it will try to create that context and uh from the second time it will basically go over the values and all those things and then give us the output

speaker_1: Exactly

speaker_2: Its from the high level high level

speaker_1: to what you said is absolute right this is a two step execution that javascript uh takes okay so my now my question is you say interpretation is line by line execution correct so if line by line execution is happening then if the execution is happening two steps okay so theyre contradicting each other correct so thats not line by execution can you justify how line by line execution happen in this two two step execution process

speaker_2: So I will say like it is kind of a just in time kind of compilation that basically runs behind JavaScript with which JavaScript is basically able to give us the output and


Yeah I will have to read more about it I think

speaker_1: No problem so you think react is a just in time compilation

speaker_2: Oh yeah its kind of a library of JavaScript So it has a number of more concepts as well

speaker_1: So tell me the difference between uh just in time compilation and ahead of time compilation


Also if if you know please tell me which which frame which popular framework uses ahead of uh fra ahead of time compilation

speaker_2: Im not very sure of the time

speaker_1: No the purpose I ask all these in the in the beginning is like these are extreme fundamentals correct You are able to answer most of them and wherever you think you are not so confident please touch base on those Okay Now let me ask you a few basic questions of the another other continuation of JavaScript only Can you tell me what are closures in JavaScript

speaker_2: So closures are basically kind of functions in JavaScript which helps the inner function to have like more control over the context of the outer function as well Like you can have certain variables which you can control with the help of inner function

speaker_1: Its its uh not wrong but not fully correct do you want to rephrase Anubha

speaker_2: Controlling the scope I would say that is what makes more sense And like inner functions has more access to the scope of outer functions

speaker_1: correct this is fine uh what this definition is fine so basically inner function have access to the lexical environment of the outer function if there is no outer function the global itself is the outer function correct that is called closure can you tell me one practical example where you might use the closures obviously interview there are many questions people ask set timeout and all those things any practical example that you think that where closures can be used

speaker_2: like basic application is like um for example you want to keep the value like in a check for all the function different calls that we have for some sort of variable but like in a practical term like if it is used somewhere i will have to check upon

speaker_1: Sure sure Ive created one video recently about function caching Okay how to cache a function with variable number of arguments That is one the good and the efficient example of using closures Whenever you you have time check out obviously there are a lot of other examples to where the practically we can use the closures Okay


So Ill ask you just couple of questions on React then well solve some snippets okay Tell me what is the reconciliation in React

speaker_2: So reconciliation is kind of the mechanism with which like the react basically does the re rendering It uses certain algorithms It compares the different because it creates a tree kind of structure like the DOM elements We have the tree structure and the different nodes They try to compare basically what was previously being rendered and what is the new set of structure in the virtual DOM So they kind of compare it and then basically


renders only those certain nodes which needs to be re rendered or which have certain amount of change

speaker_1: Exactly can you tell me which algorithm used for this tree comparison as you might know tree comparison very costly operation


Can you tell me which algorithm you used for this comparison

speaker_2: I think it is differing something like a differing

speaker_1: diffing is the algorithm name absolutely right okay i have one practical question sanabha okay think and answer lets say you have a plain html and javascript code written for example lets say you have just input box and a button nothing much same code is returning react as well


As React proposes the concept of reconciliation and it technically says it is faster than the plain JavaScript So only people should basically use You tell me whether React is faster than the vanilla JavaScript in all the scenarios or not

speaker_2: So like I think there might be certain scenarios where React wont be like faster because it does some kind of unnecessary rendering at times as well depending upon the structure we have created our file like if we have a parent or child kind of thing so we have to kind of enhance it step by step and so JavaScript might have an edge at times not necessarily and we can prevent creating React components at such times

speaker_1: Yeah answer is right but what interviewer will generally expect is you should tell an exact scenario correct Where JavaScript is faster than the React Okay please check certain scenarios What your answer is right but it can be only right when you justify it


Tell me what is a higher order components in React

speaker_2: So higher order components they are kind of created in order to reduce the redundancy which might be there in certain kind of components that we have created and in order to prevent that effort so we create a component which has certain set of executions being handled at the higher level and we pass our component to it so that it basically doesnt alter the thing but it adds certain kind of things to that particular component that we have

speaker_1: Give me a practical example in above dont give me any built in examples a practical example where you created a higher order component

speaker_2: So I had one scenario with the ref forwarding if I remember quickly and basically I was using a forward ref and herein I passed it to a higher order component I wanted I think to highlight some of the input boxes and for that I passed it because that is also kind of a higher order


Im not getting

speaker_1: I need more concrete and above can you please elaborate like why you needed higher order component without higher order component what problem you would have faced I mean what inefficiency you would have faced can you elaborate

speaker_2: So for instance I can take an example wherein I was rendering some kind of data from an API So there were two set of components and they were both again fetching data from the same API So the UI varied a little bit but the basic call the network call was same So in order to handle that so a higher order component was created and then the data was fetched in


That particular component so that it could be supplied to these components

speaker_1: So higher order component you use for making a network call am I right

speaker_2: Yeah

speaker_1: But rather making the same set of activity in both just the URL and other things might be changed So you have tried creating a hierarchy component which can handle these activities Am I right Anubhav


So Ill ask you one simple question around this So I got the scenario where you used cant you just use a utility class to do this activity Just a file which will export a function which will obviously do post get et cetera And you pass the URL and the parameters in and it will return the result to you Cant you use that approach instead of using the variable That is also possible correct

speaker_2: Plus it would cut it

speaker_1: The purpose I asked this question Anubhav is every efficient technique like Hierarchical component comes with its own complexities Hierarchical component use memo use call web anything that give you efficiency comes with its own set of a trade off in the performance correct so it is good to use them only when required correct so I generally ask some practical scenarios many people say like Redux connect correct Redux connect is one of the most common usage of the hierarchical component but it is not something that we want to use that is inherently like you cannot avoid using it so you are using correct so


as the practical examples just around that


Now lets spend around 15 minutes and above on some snippet driven questions Okay Ill share link with you Please open this link and present your screen Okay You can also open JS Fiddle Can you open JS Fiddle and present your screen


Sure can you please open now JS Fiddle


So Im adding the question in the Zoom chat


So please open this question and add it in the JavaScript the third window Okay But dont run the code


The my expectation is can you please predict the output of it Guess the output you have a minute to guess


So there are three locks basically type of A type of B and type of C All the three are undefined


Uh type of A B C R undefined correct thats what you are saying


Top left you see a run icon Can you please click on that and above top left run


And bottom right you see something called console beta and you click on that


And that white area you can expand Can you expand the white area White area


It is not all the three are undefined One is undefined and rest two are number Okay Can you try deducing Why remaining two are numbers and above


Its not an easy question Its a medium to hard question only Okay I mean even first time when I looked at it I also answered all the three as undefined only Okay Thats why I thought of putting it so that somebody else will not do that mistake


So do you would like to guess or well go to the next question

speaker_2: Likewise

speaker_1: Now what and what I did not hear

speaker_2: Uh I said like uh yeah we can move to the next one

speaker_1: So so


Let me Ill share another snippet with you


Please copy the snippet and paste dont run the code


In comment the above one


Think its the duplication line number fifteen to nineteen you can remove


Yeah yeah eleven two that yeah this is the question yes maybe can you try zooming in a bit


recorded yeah little huh this is good

speaker_2: No


And then both those two

speaker_1: Can you please run now top left


What is coming


First is its printing world is beautiful but hello world is not printing it is getting the uncaught type error


Yeah can you just deducing again why youre getting the type error


Would you like to guess and about what is happening


Can you be a little louder and above Im not clearly hearing

speaker_2: Yeah so I said like I think something to do with the

speaker_1: You want to convert var into const or let entray

speaker_2: Yeah I think the lets should

speaker_1: Please please try

speaker_2: No no no that will not work because uh


The call is before the definition of the

speaker_1: K well go to the next question and above or you want to still guess


No problem See its a simple hosting concept Okay Ive tried explaining very much in detail in my hosting videos Ill share the links personally with you for audience whoever watching Ill try to link that on the screen You can watch the hosting videos Okay This is the last tip that Ill share with you Most common one I like asking this question So I ask in almost all the interviews


Please copy the snippet and paste


you get the output see i hope you are enjoying the content like how anvabhi is responding and how im asking the question and please like and comment about the video as you as you very well know i have a noble cause of helping people to create the interview just by liking and commenting i can reach out to more audience because the youtube will give more impressions so please like this video and comment whatever youre thinking okay that will really really help my channel thank you so much and after doing that please continue watching further

speaker_2: the print five five times

speaker_1: So prints five five times with what interval Anubha will print five at a time or there is some

speaker_2: I do that

speaker_1: One second So you mean you run the code no delay Immediately all the file printed or there is one second delay then the file printed or after printing all there is some delay How is it

speaker_2: There should not be delay because by the time like these things the set time would get executed the loop has like already entered


So it should be like all at once


without being

speaker_1: Are you sure Can you uh just to justify why there is no delay between printing or during the beginning of printing why there is no delay Can you justify that just that thing

speaker_2: So Im

speaker_1: So overall how many set timers are created on above

speaker_2: So uh only uh like there will be total of five only

speaker_1: Exactly what you said is right so five timeouts are created

speaker_2: What do you citizens

speaker_1: Each having delay of what


I mean time out of

speaker_2: Yeah it says uh like thousand milliseconds so one second

speaker_1: All the so there are five timers created with one second delay each


Youre telling when you run the code there is no delay in printing

speaker_2: And this for Moby

speaker_1: Else lets come to the output part separately and both just tell me now whenever this runs right tell me what will happen like as soon as this statement is encountered how many seconds does for loop will take to execute then how set time it will step by step can you just explain no dont want to get into very depth like execution context and all the things just the basics how the things will execute probably we can take little bit of event loop and explain

speaker_2: Okay so uh like this is a browser APS so they will be put in a separate queue as and when the loop is iterating so they nothing will be executed until their execution is completed


So once the execution is over in that particular this delay is over like of thousand millisecond then they will be brought back to the main stack and then they will be executed

speaker_1: So what you said is absolutely right and above Okay One one add on question Ill ask This is also a common question So set timer to will it guarantees the delay whatever is given Lets leave this case in general Lets say three second delay is given for set timer mode Will it for sure execute after a three second

speaker_2: Uh under in this loop you meant in this loop

speaker_1: In general in general Im asking not inside the for loop in general will it guarantee it will execute after that second that many seconds

speaker_2: Uh no I think it is not always a penalty it depends

speaker_1: Why it is not guaranteed can it tell a little bit

speaker_2: I think because of the asynchronous nature

speaker_1: Because only the main thread is executing things correct So finally all these activities has to go to main thread when main thread is free So though the set time out after three second elapsed it can come to the stack but there could be other task in the stack


So the main thread may not be able to execute it the exact time when it was supposed to execute


that is a trade off using the set timeout please run the code zoom out and please run the code and well see what is the output


So you expand the that white area yeah expand the white area yeah and clear the console


Yeah run once again expand and run


I see a delay Anubha you are not seeing a delay


Second delay

speaker_2: Yeah there it is

speaker_1: Yeah thats the reason I asked this question People generally get confused with the delays 5 times 5 is absolutely right And you also mentioned there is no delay between each printing That was also absolutely right But there is one second delay in the beginning


would like to guess why there is one second delay

speaker_2: But its

speaker_1: Ill give one hint okay basically five timeouts are created almost at the same time


Core loop will take microseconds to execute


As much as I can tell further you need I guess

speaker_2: By the time I think the loop executes so one of the set timer I guess gets that delay

speaker_1: You are right you are close See this is pretty much the what I wanted to say is for loop will execute much faster Obviously it is not going to take one second correct So but five timeouts are created in less than lets say a few microseconds or milliseconds Lets say five millisecond is taken to execute this it will run the loop So by that time already the five set timeouts are created


High set timeouts are already created So now at least one second has to elapse before running a faster timeout


So that there is a delay If for loop would have taken one second to execute this code then what your answers gave was right Like it will immediately execute because one second already elapsed Since for loop is faster than whatever the set timeout interval that we have given due to that nature we get the initial one second delay


So yeah thats all about the snippet driven question that I want to ask Anubhav Okay so we are at almost half an hour we are finished I do not know how the time flew Okay you can stop sharing


Yeah so Anbo let us spend last five to ten minutes whatever we left now on the feedback and any questions you have First let us start with any questions that you have Then Ill try to give my feedback Tell me if you have any questions ask me

speaker_2: So like I had not for these concepts like how do we prepare for machine coding round kind of like are they are these rounds very frequent or it depends on the years of experience we have or yeah

speaker_1: So machine coding is very common in the premium companies probably whatever youre aspiring like lets say Microsoft you are aspiring or Amazon you are aspiring Swiggy you are aspiring So machine coding is mandatory in all the premium companies whatever the big product companies we call right So machine coding and routing route is mandatory So you have to prepare for machine coding interview if youre aspiring for that But there are a lot of companies which I can tell I cant name the companies but there are many tier two kind of companies which dont have the machine coding route as separate


It depends on your preparations Anubha if you are preparing for the taller one


The first few components in tier two then obviously you need to prepare for machine coding if not then probably it is not necessary

speaker_2: And then one more question related to data structure and algorithms So like in general like if youre a backend developer so we cover like TP and all those topics as well But as a front end or like because even if we are working on Nodejs we are more commonly referred as front end only stuff Exactly So what all topics we need to like lay emphasis on if we have like one or two weeks

speaker_1: Exactly

speaker_2: time to prepare for it

speaker_1: So my advice is this lets say youre preparing for companies like Apple Google Apple Google Facebook or Meta what we call If youre preparing for these companies then skys the limit whether youre front end developer or back end developer they hire the generalist not specialist correct so all the topics you need to cover but in case if youre preparing i this includes amazon as well okay amazon apple facebook all these companies you have to prepare almost all the data structures but if youre preparing for some other companies with my experience like microsoft sap and this kind of


companies then probably you can limit yourself to strings arrays linked list and binary search trees there is very few occasions where these companies ask graphs or dynamic programming ready approach backtracking all these questions to a front end developer


So where they will have a machine coding down to test your skills right So they will not spend lot on the data session algorithm But obviously my find I simple if you are appearing for a not at all premium companies then limit yourself to strings and arrays If you are applying for a semi premium then go till the linked list If you are applying for premium excluding the main okay Excluding the main there are a lot of premium companies Then go till linked list and the binary search trees also In fact I have already made tutorials all the linked list and linked list I have come


word uh if you wish you can watch that ill try to link that on screen for the audience


Any other questions regarding the interview you have any other questions or oral or

speaker_2: Or else thats all yeah thats all from

speaker_1: Sure Anubha so it was a nice interview from my side whatever I felt Ill tell


So with whatever the answer that you are giving fundamentally you are strong like conceptually you were able to explain very good technical communication skills are good So there is two things communication and technical communication There are many whenever I ask what is hosting they start writing the code or whenever I ask closure they start writing the code So code writing is one part of the development the developer job correct You should know how to articulate whatever you know So in that way you are able to technically communicate what you know


And the react concepts also fundamentally are good Many still dont know what is reconciliation itself React reconciliation your higher order component you are able to answer well So conceptual knowledge Ill give full marks Whatever things that you can improvise that I notices whenever I in the beginning also mentioned theres a breadth and the depth concept in the interview where you touch base on a lot of topics and we get into depth wherever we feel it is essential Okay So in the depths I feel you need to work a little more For example the interpretation question that I asked So you may have to dig a little deeper to answer


understand what is the interpretation etc correct or example the set timeout one or the hoisting question which I asked snippet driven snippet drivers are very very common in the interview okay why because all the snippet driven question will have one tricky part obviously one tricky part will be there you need to be able to unlock it so that is the uh important part of the snippet driven questions so if but if you fundamentally become strong lets say you already know what are closures but if you spend more time and understand in depth of closure you will be able to easily answer the for loop and that set timeout what I asked correct


answer was right but im telling in depth so why when why in depth is necessary whenever you are applying for the tier one companies so they always look for the in depth in depth uh question in depth concepts correct because obviously theyll have problems inside which somebody who has in depth knowledge only can solve mediocre cannot solve okay thats the only feedback that ill give like i mentioned ill send one detailed email to you as well to which consolidates all all whatever everything that i explained


So thats all from my end Anubha it was nice talking to you okay any questions you have Anubha

speaker_2: I would say like it was a good experience I think it will surely help me as well in my future

speaker_1: Oh hope youre watching uncommon geeks uh and above my videos and other things

speaker_2: Yeah yeah surely I am doing that on daily basis

speaker_1: great great anime Obviously like I always mention if you watch and I have 60 plus videos obviously if youre preparing right now you cannot watch all the videos But even if you watch my summary videos where Ive explained Reactjs complete Reactjs interview preparation JavaScript complete interview preparation couple of those videos if you fully watch a lot of concepts will be clear to you So there are around 30 35 minute videos 30 35 40 minute videos So two videos you watch it is hardly one hour If you spend one hour and watch those two videos your fundamental becomes much much stronger Okay I would advise watching that


Thats all Alhamdulillah very nice talking to you have a good day then bye

speaker_2: Thank you

speaker_1: Welcome back guys I hope you enjoyed the mock interview with Anubhav So it was nice interview he was able to articulate a lot of thoughts and wherever the small correction that he can do I have already communicated that to him in the interview And certain things that I think personally I can convey Ill be sharing it over the email In case if you are someone who also want a free mock interview please suggest it in the Google form that is present in the description section Its not like obviously its not like Ill be able to take interview for all but definitely Ill keep your contact I only ask very basic details to contact you If not now


in future whenever I want to do mock interviews or whenever I want someone to partner with me in the interview process definitely Ill consider your profile okay thank you so much for watching in case if you are not like the video please like the video comment whatever you felt about the the mock interview process and please subscribe to uncommon geeks this will help me a lot into spreading this thought of helping people to clear the interview and please share the information with your friends and whatever the question that the rest in the interview are present in my github repository Im linking the github repository in the comment section you can always go and check that out and practice on your own some


questions are very tricky so please find the answer for yourself if youre still not able to find please mention that in comment section ill try to explain why it is so okay and please follow me on medium i write a lot of medium articles i i got decent followers on medium also recently okay please follow me on medium too and uh star my github projects thank you so much for watching catch you in next video
