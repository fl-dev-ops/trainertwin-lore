---
id: NAAVYkgTOXA
title: "Fresher ReactJs Interview | \U0001F389 Selected | ReactJs & JavaScript (Must\
  \ watch if your fresher)"
url: https://www.youtube.com/watch?v=NAAVYkgTOXA
date: '2023-02-04'
duration: 00:33:41
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
---

speaker_1: Yeah so hello to all that who are watching this video I recently wrote a LinkedIn post asking like if any fresher is looking out for a mock interview I said Ill be open to take mock interview A lot of people have registered I have planned to take a lot more interviews and today with me I have Saurav So he registered in that particular form and he will be doing a fresher front end kind of an interview Its going to be a real interview There is nothing that weve already discussed about question or nothing How a typical interview would happen for a fresher with respect to front


content same questions will be discussed in this so please watch the video till the end and sorry first of all welcome you to my channel uncommon geeks

speaker_2: Yeah thank you

speaker_1: Saro let us start by your introduction Tell me about yourself because this is also another important interview question So introduce yourself and then we can get started with the question and answers

speaker_2: Okay so hi all I am Saurabh Singh an undergraduate in computer science and engineering from Gyan Ganga Institute of Technology and Science currently Im in a fourth year and I started my web development journey with basic technologies like HTML CSS and JavaScript and later on moved toward the JavaScript libraries and frameworks which are like Reactjs and Nextjs I also have some hands on experience on React and Next and also did some couple of internships using these technologies


and also worked on some projects like projects and currently Im looking looking for the internships and full time roles

speaker_1: Great great Saurav And Saurav is already actually interned at Reliance Jio So which is Im very happy because people in pre final year and final year are getting internships is a good sign Okay So Saurav now without wasting further time lets get started Okay So lets start with the extreme basics of the web development Saurav Okay Ill ask you one very basic question So lets say you are opening a website for example now googlecom You entered googlecom on the search bar of the browser and hit enter Can you tell me what all happens in the background to get


Get that content and show it on the screen

speaker_2: so initially if we if we talk about what is google google is a search engine which which is used to rank the website so when we are typing something like example like apple or something so it get our search query is get to that google server and then google and then google uh like process our query and and uh generate some results and then displays these results and send those results to our browser and and then


are browser partial and source UI

speaker_1: got it so there are two parts to it what you said is like how google search engine would take the input and give the result my question is its not googlecom any website that you search in the that search bar and hit enter right after that what would happen its not just a google any website for that matter you hit enter right what will browser do to get the data

speaker_2: Okay so imagine ourselves as a client and when we search something at the URL it gets a request to the server and then server process the request and then respond back to our client

speaker_1: Correct So this is a very high level sorry This is not wrong But do you know in depth as soon as you hit enter what will happen where the request will go what it will do like that

speaker_2: I think the browser first uh like parses the request and query and then it uh sends a request or like a HTTP request to the server and then I think it responds

speaker_1: Correct No Ill give you just an overview maybe little bit of a hint Ill give you See the first thing that happens is the DNS domain name system correct So where I think you might have studied in your final year that computer networks one or two where basically we humans will understand the string or alphabetical English kind of a domain correct Googlecom On system there is nothing called Googlecom correct There is just the IP addresses which are there So first the request goes from a browser to a server okay Where this


IP address to name to IP address mapping happens Okay Then whatever you explain is current it goes to a dedicated server gets the result et cetera But there are a lot of concepts involved in this Its not that straightforward There is a concept of resolver Theres a concept of authentication private IP public IP So all may not be asked to a fresher level But if you are a web developer this is one of the primary thing to know in depth Okay So there are a lot of videos on this You can just check how HTTP works HTTPS works how a request gets processed So just spend some time on


of that okay ill ask you just one question on the networking aspect as entire web development actually happens between the connection between client and server correct yeah do you know what is tcp and what is udp

speaker_2: Yes these are the protocols for request and response

speaker_1: So do you know the abbreviation of TCP

speaker_2: Yeah its transmission control protocol and the youth then for

speaker_1: Ill give you hint it P P P starts with protocol

speaker_2: It be be peaches


Okay it its a its a something like a datagram protocol

speaker_1: Its user datagram protocol Yeah Do you know the difference between TCP and UDP

speaker_2: Actually the main difference is the connection which is like TCP is connection definitely establish a connection and UDP is connection less

speaker_1: Definitely


Correct Absolutely Absolutely So now I am not sure whether you worked on any application but theres a common sense kind of a question that Im asking You know what is recipient you know what is UDP You also know basic difference connection oriented and connection less So given an application they ask you to build when you would use TCP and when you would use UDP

speaker_2: So basically when we want to when we want some some kind of real time kind of feature like a real time video call so then in that case we use UDP and got it and when we want some like something some kind of messaging or another kind of transmission then we use TCP here we dont we dont care about like loss of packets

speaker_1: Yeah I mean your answer and your explanation is quite contradictory See you said TCP is connection oriented UDP is connection less So now you will use UDP for a video call correct Thats what you said TCP where you will use Its not not TCP any example you know where exactly you would use TCP

speaker_2: The uh


I cant remember

speaker_1: No no problem See what you said is not wrong Ill just correct considering you yourself in the audience See in interview every question that you tell which is wrong will not be corrected But I am just using this opportunity to help you and the candidates also Generally it is at the end when if you have any doubts you can ask and that will get answered See TCP and UDP what you said is correct TCP is connection oriented UDP is connection less And the example that you gave for UDP is also very right So where basically the things like a video calling correct So like now we both are connected over the Zoom So in this particular video


collect lets say some some amount of packets are lost like uh the small microsecond when whatever i spoke is not listened to you still there is no problem the video and the recording would go on correct so thats what we call the um udp you can use udp there where some packet loss is not so much difficult so much important uh this also for example youre doing whatsapp video call there also if some some packets loss theres no problem correct but when do you use tcp is when there is a connection oriented and the every no packet uh loss is allowed correct for example you you you are a youtuber


are uploading a video to youtube correct that time some packets cannot be lost like you want all of your video to go there correct or for example youre using a file upload file download protocols whenever your file transfer protocols like gmail youre sending a video to somebody else some some portion of the video cannot be lost correct so in those scenarios youll use tcp see these are very essential why im asking a lot of front end developers just start with html and yes its not like that the fundamentals are actually from the protocol correct tcp udp the the transportation the


the computer networks and all of that okay now ill ask you a few basic questions on the web then well go to a small implementation in react also okay so um tell me uh some lets start with the extreme basics of javascript okay so javascript is a single threaded interpreted programming language am i right or wrong sir

speaker_2: Yeah right

speaker_1: Correct correct So see there are a lot of languages out there which are on the market like Java C C sharp C plus plus et cetera Theyre all multi threaded programming languages JavaScript on the other hand is a single threaded programming language correct So I mean whether you worked on those languages or not Im Java or C sharp everyone would know multi threading will give a lot of advantages like parallel processing would happen and a lot of things becomes parallelized and the system process the things much quicker correct So you know any idea why JavaScript is single threaded


and not multi threaded

speaker_2: so basically if we start like javascript is a single thread what single threaded single thread means it execute one task at a time not parallel processing so the advantage we can say is like our task execute one by one and the developers who is working get the exposure of that code that okay so this is working i think thats uh one reason and another reason can be like


Theres something called uh what we say like um


The task is scheduled one by one and everything happens one after the other I think that could be another reason

speaker_1: Sure sure what youre saying is not wrong but you read more about it okay this this is the fundamentals okay now


As as I said JavaScript is also interpreted programming language correct Do you know what is interpreted programming language in general

speaker_2: Okay so interpreted programming language is like one line execution and then other and compiling the whole whole code is cant get compiled and then the run set

speaker_1: Absolutely I actually have asked this question to people with five six year experience They wouldnt know Good that you are aware of it Okay And also JavaScript is a loosely typed languages not a strong typed language C C plus plus are strong typed languages JavaScript is a loosely typed programming language or weakly typed programming language Do you know what is the difference between strongly typed and weakly typed programming language

speaker_2: okay so lets say we want something called something variable declaration or something in other languages or in javascript in javascript what we do is we dont define the type that or some lets say we have some string or number or anything boolean we can store in a single variable and in other in other languages like c plus plus or c sharp anything there are like uh there they includes uh type checking also


So like if you want to in like store an integer then we need to use that int keyword So loosely type language means here are no restrictions of like a type

speaker_1: Absolutely absolutely right sir Actually I sense that you have a very good fundamentals What youre saying is absolutely right Loosely typed are those programming languages where the type is not defined Like data type is not defined So let x can be anything correct It can become int string or anything Whereas a strongly typed language its int x x is only int now x cannot become float inter runtime It is always the int


But do you have any idea why JavaScript is weakly typed and not strongly typed


What he said is about weekly type is right my question is why it is weekly typed and not strongly typed

speaker_2: I think the reason can be to give more powers to the developer like more flexible kind of thing

speaker_1: No that could be one So that is see language one level creating a language what aspect you are saying is definitely consider how we can make it easy for the developer correct But there is also another very important aspect on the architecture point of view Do you see any why from the architectural point of view JavaScript is a weakly typed language

speaker_2: I cant remember though

speaker_1: No worries Ill tell why it is weakly typed language See JavaScript doesnt run on a system like CCC plus plus or Java correct JavaScript is technically built for running on a browser So it doesnt directly interact with the system hardware correct So whenever a language like that is created which is not directly interacting with the hardware correct So and what happens is these are all running in the browser So they are not having a direct access to the memory So if it is strongly typed int x correct So whenever


But if you do in text that also there are two reasons Whenever you write like in text in the browser there is no guarantee that much memory is allocated to it from the hardware because its running on the browser correct So because of this dynamic type allocation so the JavaScript engine can make sure So this kind of memory can be picked whatever is available at that point in time can be picked and allotted and later it can be cleared also


Thats one of the main reason why JavaScript is weakly typed There are a lot of other reasons also why it is weakly typed Please read you and the audience both Im telling Okay Now lets get a little in depth of the JavaScript concepts are up Okay So tell me what are closures in JavaScript

speaker_2: So closures closures means function bounding to its outer scope or a lexical environment So when we call the inside function it remembers the outer variables and methods

speaker_1: Got it Correct So inner function having access to the lexical environment of the outer function can be called as closure Correct Yeah This is the right definition What youre saying is not wrong Try to have a proper definition so that there is no cross questions to that So thats one So now give me one practical example why or where you can use closures

speaker_2: Okay so imagine we want some DOM manipulation and we have something called paragraph and we want that paragraph to change according to our conditions So whenever some condition changes we want some paragraph to change So and we have a function and it has some expensive calculation When we call that function with the DOM manipulation feature so it execute that expensive calculation every time If we create a closure with that function


So we do we can like avoid that expensive calculation and we can achieve our feature

speaker_1: Got it Sure There are more examples that can be given You can read definitely Now lets get into slowly some of the React concepts Again this Im telling to Saurabh and all the audience who are watching So if youre a fresher so much of in depth React would not be asked So some basic they would touch on and just some some small fuzzle can be asked in most of the product and the service based companies also Okay So why do you think React has advantage over the basic JavaScript or basic vanilla JavaScript HTML What are the advantages of Reactjs Why somebody should use it

speaker_2: So lets compare with the basic things Okay so lets have some lets we want to some build some applications So in JavaScript we want we have to write some code extra code for that some feature Like imagine we want we are like building a card So we want some state management So for that state management we need to write code in vanilla JavaScript to achieve that functionality While someone if someone uses the the React he gets


thats these kind of pre built features like we can use context API or Redux for state management so and there are other advantage also like the component based architecture and and also some like they are they are also provide like routing and other kind of stuff

speaker_1: Great great sorrow So these are all true okay See but the very basic quality of React that makes React to be choosable So whatever you are saying all the things can be done in Venla JavaScript also correct Because ultimately everything is actually done in Venla JavaScript only all right See one main concept that everyone you and the freshers need to know is a reconciliation okay Reconciliation is also called reconciliation So thats the core difference because that is what makes React faster okay Im not telling what is reconciliation to you or the audience Please go


and read the consolidation its a very very important concept thats what the main foundation of react why somebody should use the react okay so now let us start with a fuzzy okay uh im just gonna share a link with you the chat please open this link in a fresh window of browser and present your screen okay you can only present that particular tab in the browser stop obviously theres a lot of research that has gone into making this video so please like the video and subscribe to my channel and press the bell like


if youre not already done so and add a comment whatever youve felt so far the reason for that i always say i have only motive i help want to help the candidate to clear that interview so if more likes more comments video becomes visible for a lot whenever it is visible for a lot and there is a high chance i get more subscribers in the followers definitely the there is a high chance i would be able to reach my cause very soon okay so please like and comment about the video before watching the further okay

speaker_2: I hope my screen is visible

speaker_1: Yes sir your screen is visible


Lets get started But before starting let me let us let Ill ask you a few very basic questions of the React days Okay So now so what which component is currently used in in this example

speaker_2: Okay so we are using app component

speaker_1: Yes so its a function component correct

speaker_2: Yeah function based yeah

speaker_1: Yes correct so do you know what is the bare main difference between functional component and a class based component

speaker_2: Okay so class based component basically uses the uh


uh class based things like constructors static words and like setting state also have some difference in text in that

speaker_1: Correct correct There are a lot of differences and eventually we are reaching a state where a lot of people have not used class components Somebody like you was just starting right They might have started itself with a functional component and this question is not so usual now to ask the difference Okay Yes So React is something called JSX correct So can you tell me what is JSX in React

speaker_2: So GFX basically stands for JavaScript XML


If you want like to explain some beginners so we can say that its we are using inside STM8

speaker_1: So do do you see any advantage of using JSX over the plain HTML or something like that

speaker_2: I think we can do certain of things like without changing the whole whole DOM we can use some variables and keywords and like lets say we want something here


can use some some kind of variables here

speaker_1: Got it

speaker_2: I thought it cant be

speaker_1: Correct What youre saying is correct Otherwise you would have actually you have to fetch an ID and append or change the values et cetera Correct That is one but the little more also the advantages of JSX Please read that Okay Now see Im not asking so many questions on React but I just want you to know how fundamentally youre strong in building the UI in React Okay Question is very simple Sarub Basically you need to create four input fields Okay The first name the last name email ID and the phone number Okay And just one submit button


Okay so now to start off with let us keep it this way You have to validate this form basically First name and last name cannot be empty


and phone number has to be 10 digit email actually meet the regular expression of the email okay whenever user click submit you will get all the values but that user has entered and you will validate and any any error is there let us just alert it like invalid email id if there are more than one errors are there like uh first name is also not entered and email id is also invalid then let us try to show whatever whatever the first alert is like first first only first name is not there then let us show that and stop okay after they enter and hit submit let us show the second error this is what


I want you to build we would have around 10 to 15 minutes to solve this completely sorry okay please get started

speaker_3: Im the last fighter

speaker_1: It doesnt matter

speaker_3: Four five


Is it a good state of the art so

speaker_1: Lets just validate for the first name uh sorry considering the time constant lets say have you will do okay if first name is not there you have to show the alert


Its triggering even before you click right

speaker_2: So let me see

speaker_1: Exactly good you figured it out

speaker_2: Now I see theres nothing in it

speaker_1: Very good very good

speaker_2: reload it will reload because like we havent said that eventpreventDefault

speaker_1: Exactly


Sure Saurav We can stop sharing Okay As we have almost last five minutes now well spend some more time on overall feedback that I want to pass it on to you Okay You can stop sharing Ill also tell whether youre select or reject from mine


If this arrow thats what like I mentioned whatever Ill just tell mistakes that you did in the problem solving This will help you and the audience First thing get little more clarity regarding the requirement Interviewer themselves may not tell everything to start off whether there is importance for the styling or not Like you coded a very basic and very neat UI but you did not ask whether the interviewer expectation is that or not correct For example he want a more stylish kind of a UI but you did not ask He also interviewer may not


say this and whenever you say that was the expectation then he would ask you did not ask what is the requirement correct thats one second uh this is maybe you know this but some people may not know what is the regular expression to validate email thats quite common and all interviewer do not expect candidate to know that so be vocal dont think like interviewer will feel bad or he will reject if i ask him can i search the email id a regular expression on the internet most interviewer will be fine with that because regular expression do not define you correct ask in such


scenarios okay then coming to the functionality whatever you did was good so plan for the duration that you have let for example you have like 10 minutes right so divide the deliverables into modules so that at least one module can be delivered so only ask you to stop at the first name correct every interviewer will not tell that so you decide the code in such a way where at least one module can be catered in the given time if something is not catered still we can tell this is we are able to give this much okay so that interviewer happy not having at least rather not having anything interviewer


happy something something is there at least all right so plan in that way in the practical coding uh interviews okay done from my end so tell me how was the overall interview experience

speaker_2: It was quite good I learned a new tons of new things like how to prepare and how to like organize myself

speaker_1: Correct correct sir So I always say this not to you to all the freshers So dont start web development at the front end just from the point of the development Start from the extreme fundamentals of network protocols and understanding the language so that you can build anything on top of it whenever it is required


Sure sorry thats all from my end nice talking to you have a good day bye

speaker_2: Yeah thank you
