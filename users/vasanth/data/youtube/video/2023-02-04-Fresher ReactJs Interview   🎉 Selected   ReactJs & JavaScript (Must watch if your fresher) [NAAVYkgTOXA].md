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
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# Fresher ReactJs Interview | 🎉 Selected | ReactJs & JavaScript (Must watch if your fresher)


## Transcript

### 00:00:00 · Speaker 1

Yeah, so hello to all that who are watching this video. I recently wrote a LinkedIn post asking like if any fresher is looking out for a mock interview, I said I'll be open to take mock interview. A lot of people have registered. I have planned to take a lot more interviews and today with me I have Saurav. So he registered in that particular form and he will be doing a fresher front end kind of an interview. It's going to be a real interview. There is nothing that we've already discussed about question or nothing. How a typical interview would happen for a fresher with respect to front

### 00:00:30 · Speaker 1

content same questions will be discussed in this so please watch the video till the end and sorry first of all welcome you to my channel uncommon geeks

### 00:00:38 · Speaker 2

Yeah, thank you.

### 00:00:39 · Speaker 1

Saro, let us start by your introduction. Tell me about yourself because this is also another important interview question. So introduce yourself and then we can get started with the question and answers.

### 00:00:49 · Speaker 2

Okay so hi all I am Saurabh Singh an undergraduate in computer science and engineering from Gyan Ganga Institute of Technology and Science currently I'm in a fourth year and I started my web development journey with basic technologies like HTML CSS and JavaScript and later on moved toward the JavaScript libraries and frameworks which are like React.js and Next.js I also have some hands-on experience on React and Next and also did some couple of internships using these technologies

### 00:01:19 · Speaker 2

and also worked on some projects like projects and currently I'm looking looking for the internships and full-time roles

### 00:01:29 · Speaker 1

Great, great, Saurav. And Saurav is already actually interned at Reliance Jio. So which is, I'm very happy because people in pre-final year and final year are getting internships is a good sign. Okay. So Saurav, now without wasting further time, let's get started. Okay. So let's start with the extreme basics of the web development, Saurav. Okay. I'll ask you one very basic question. So let's say you are opening a website, for example, now google.com. You entered google.com on the search bar of the browser and hit enter. Can you tell me what all happens in the background to get

### 00:01:59 · Speaker 1

Get that content and show it on the screen.

### 00:02:03 · Speaker 2

so initially if we if we talk about what is google google is a search engine which which is used to rank the website so when we are typing something like example like apple or something so it get our search query is get to that google server and then google and then google uh like process our query and and uh generate some results and then displays these results and send those results to our browser and and then

### 00:02:33 · Speaker 2

are browser partial and source UI

### 00:02:36 · Speaker 1

got it so there are two parts to it what you said is like how google search engine would take the input and give the result my question is it's not google.com any website that you search in the that search bar and hit enter right after that what would happen it's not just a google any website for that matter you hit enter right what will browser do to get the data

### 00:02:55 · Speaker 2

Okay, so imagine ourselves as a client and when we search something at the URL, it gets a request to the server and then server process the request and then respond back to our client.

### 00:03:08 · Speaker 1

Correct. So this is a very high level sorry. This is not wrong. But do you know in depth as soon as you hit enter what will happen, where the request will go, what it will do like that.

### 00:03:20 · Speaker 2

I think the browser first uh like parses the request and query and then it uh sends a request or like a HTTP request to the server and then I think it responds

### 00:03:34 · Speaker 1

Correct. No, I'll give you just an overview, maybe little bit of a hint I'll give you. See, the first thing that happens is the DNS, domain name system, correct? So where I think you might have studied in your final year that computer networks one or two, where basically we humans will understand the string or alphabetical English kind of a domain, correct? Google.com. On system, there is nothing called Google.com, correct? There is just the IP addresses which are there. So first the request goes from a browser to a server, okay? Where this

### 00:04:04 · Speaker 1

IP address to name to IP address mapping happens. Okay. Then whatever you explain is current, it goes to a dedicated server, gets the result, et cetera. But there are a lot of concepts involved in this. It's not that straightforward. There is a concept of resolver. There's a concept of authentication, private IP, public IP. So all may not be asked to a fresher level. But if you are a web developer, this is one of the primary thing to know in depth. Okay. So there are a lot of videos on this. You can just check how HTTP works, HTTPS works, how a request gets processed. So just spend some time on.

### 00:04:34 · Speaker 1

of that okay i'll ask you just one question on the networking aspect as entire web development actually happens between the connection between client and server correct yeah do you know what is tcp and what is udp

### 00:04:46 · Speaker 2

Yes, these are the protocols for request and response.

### 00:04:51 · Speaker 1

So do you know the abbreviation of TCP

### 00:04:54 · Speaker 2

Yeah it's transmission control protocol and the youth then for

### 00:05:02 · Speaker 1

I'll give you hint it P P P starts with protocol

### 00:05:02 · Speaker 2

It be be peaches

### 00:05:06 · Speaker 2

Okay it it's a it's a something like a datagram protocol

### 00:05:10 · Speaker 1

It's user datagram protocol. Yeah. Do you know the difference between TCP and UDP?

### 00:05:16 · Speaker 2

Actually the main difference is the connection which is like TCP is connection definitely establish a connection and UDP is connection less

### 00:05:23 · Speaker 1

Definitely

### 00:05:27 · Speaker 1

Correct. Absolutely. Absolutely. So now I am not sure whether you worked on any application, but there's a common sense kind of a question that I'm asking. You know what is recipient, you know what is UDP. You also know basic difference connection oriented and connection less. So given an application, they ask you to build when you would use TCP and when you would use UDP.

### 00:05:47 · Speaker 2

So basically when we want to when we want some some kind of real time kind of feature like a real time video call so then in that case we use UDP and got it and when we want some like something some kind of messaging or another kind of transmission then we use TCP here we don't we don't care about like loss of packets

### 00:06:15 · Speaker 1

Yeah, I mean your answer and your explanation is quite contradictory. See, you said TCP is connection oriented. UDP is connection less. So now you will use UDP for a video call, correct? That's what you said. TCP where you will use? It's not not TCP any example you know where exactly you would use TCP.

### 00:06:37 · Speaker 2

The uh

### 00:06:40 · Speaker 2

I can't remember

### 00:06:41 · Speaker 1

No, no problem. See, what you said is not wrong. I'll just correct considering you yourself in the audience. See, in interview, every question that you tell which is wrong will not be corrected. But I am just using this opportunity to help you and the candidates also. Generally, it is at the end when if you have any doubts, you can ask and that will get answered. See, TCP and UDP, what you said is correct. TCP is connection oriented, UDP is connection less. And the example that you gave for UDP is also very right. So, where basically the things like a video calling, correct? So, like now we both are connected over the Zoom. So, in this particular video,

### 00:07:11 · Speaker 1

collect let's say some some amount of packets are lost like uh the small microsecond when whatever i spoke is not listened to you still there is no problem the video and the recording would go on correct so that's what we call the um udp you can use udp there where some packet loss is not so much difficult so much important uh this also for example you're doing whatsapp video call there also if some some packets loss there's no problem correct but when do you use tcp is when there is a connection oriented and the every no packet uh loss is allowed correct for example you you you are a youtuber

### 00:07:41 · Speaker 1

are uploading a video to youtube correct that time some packets cannot be lost like you want all of your video to go there correct or for example you're using a file upload file download protocols whenever your file transfer protocols like gmail you're sending a video to somebody else some some portion of the video cannot be lost correct so in those scenarios you'll use tcp see these are very essential why i'm asking a lot of front-end developers just start with html and yes it's not like that the fundamentals are actually from the protocol correct tcp udp the the transportation the

### 00:08:11 · Speaker 1

the computer networks and all of that okay now i'll ask you a few basic questions on the web then we'll go to a small implementation in react also okay so um tell me uh some let's start with the extreme basics of javascript okay so javascript is a single threaded interpreted programming language am i right or wrong sir

### 00:08:30 · Speaker 2

Yeah right

### 00:08:31 · Speaker 1

Correct, correct. So see, there are a lot of languages out there which are on the market like Java, C, C sharp, C plus plus, et cetera. They're all multi-threaded programming languages. JavaScript, on the other hand, is a single-threaded programming language, correct? So I mean, whether you worked on those languages or not, I'm Java or C sharp, everyone would know multi-threading will give a lot of advantages like parallel processing would happen and a lot of things becomes parallelized and the system process the things much quicker, correct? So you know any idea why JavaScript is single-threaded?

### 00:09:01 · Speaker 1

and not multi-threaded

### 00:09:06 · Speaker 2

so basically if we start like javascript is a single thread what single threaded single thread means it execute one task at a time not parallel processing so the advantage we can say is like our task execute one by one and the developers who is working get the exposure of that code that okay so this is working i think that's uh one reason and another reason can be like

### 00:09:37 · Speaker 2

There's something called uh what we say like um

### 00:09:42 · Speaker 2

The task is scheduled one by one and everything happens one after the other. I think that could be another reason.

### 00:09:50 · Speaker 1

Sure sure what you're saying is not wrong but you read more about it okay this this is the fundamentals okay now

### 00:09:58 · Speaker 1

As as I said JavaScript is also interpreted programming language correct Do you know what is interpreted programming language in general

### 00:10:06 · Speaker 2

Okay so interpreted programming language is like one line execution and then other and compiling the whole whole code is can't get compiled and then the run set

### 00:10:15 · Speaker 1

Absolutely. I actually have asked this question to people with five, six year experience. They wouldn't know. Good that you are aware of it. Okay. And also JavaScript is a loosely typed languages, not a strong typed language. C, C plus plus are strong typed languages. JavaScript is a loosely typed programming language or weakly typed programming language. Do you know what is the difference between strongly typed and weakly typed programming language?

### 00:10:36 · Speaker 2

okay so let's say we want something called something variable declaration or something in other languages or in javascript in javascript what we do is we don't define the type that or some let's say we have some string or number or anything boolean we can store in a single variable and in other in other languages like c plus plus or c sharp anything there are like uh there they includes uh type checking also

### 00:11:06 · Speaker 2

So like if you want to in like store an integer then we need to use that int keyword. So loosely type language means here are no restrictions of like a type.

### 00:11:18 · Speaker 1

Absolutely, absolutely right, sir. Actually, I sense that you have a very good fundamentals. What you're saying is absolutely right. Loosely typed are those programming languages where the type is not defined. Like data type is not defined. So let x can be anything, correct? It can become int string or anything. Whereas a strongly typed language, it's int x. x is only int now. x cannot become float inter runtime. It is always the int.

### 00:11:42 · Speaker 1

But do you have any idea why JavaScript is weakly typed and not strongly typed?

### 00:11:47 · Speaker 1

What he said is about weekly type is right my question is why it is weekly typed and not strongly typed

### 00:11:55 · Speaker 2

I think the reason can be to give more powers to the developer like more flexible kind of thing

### 00:12:03 · Speaker 1

No, that could be one. So that is, see, language, one level, creating a language, what aspect you are saying is definitely consider how we can make it easy for the developer, correct? But there is also another very important aspect on the architecture point of view. Do you see any why from the architectural point of view, JavaScript is a weakly typed language?

### 00:12:26 · Speaker 2

I can't remember though

### 00:12:27 · Speaker 1

No worries, I'll tell why it is weakly typed language. See, JavaScript doesn't run on a system like CCC++ or Java, correct? JavaScript is technically built for running on a browser. So it doesn't directly interact with the system hardware, correct? So whenever a language like that is created, which is not directly interacting with the hardware, correct? So and what happens is these are all running in the browser. So they are not having a direct access to the memory. So if it is strongly typed int x, correct? So whenever

### 00:12:57 · Speaker 1

But if you do in-text, that also there are two reasons. Whenever you write like in-text in the browser, there is no guarantee that much memory is allocated to it from the hardware, because it's running on the browser, correct? So because of this dynamic type allocation, so the JavaScript engine can make sure. So this kind of memory can be picked, whatever is available at that point in time can be picked and allotted, and later it can be cleared also.

### 00:13:21 · Speaker 1

That's one of the main reason why JavaScript is weakly typed. There are a lot of other reasons also why it is weakly typed. Please read you and the audience both I'm telling. Okay. Now let's get a little in depth of the JavaScript concepts are up. Okay. So tell me what are closures in JavaScript?

### 00:13:39 · Speaker 2

So closures, closures means function bounding to its outer scope or a lexical environment. So when we call the inside function, it remembers the outer variables and methods.

### 00:13:54 · Speaker 1

Got it. Correct. So inner function having access to the lexical environment of the outer function can be called as closure. Correct. Yeah. This is the right definition. What you're saying is not wrong. Try to have a proper definition so that there is no cross questions to that. So that's one. So now give me one practical example why or where you can use closures.

### 00:14:15 · Speaker 2

Okay, so imagine we want some DOM manipulation and we have something called paragraph and we want that paragraph to change according to our conditions. So whenever some condition changes, we want some paragraph to change. So and we have a function and it has some expensive calculation. When we call that function with the DOM manipulation feature, so it execute that expensive calculation every time. If we create a closure with that function,

### 00:14:45 · Speaker 2

So we do we can like avoid that expensive calculation and we can achieve our feature

### 00:14:52 · Speaker 1

Got it. Sure. There are more examples that can be given. You can read definitely. Now let's get into slowly some of the React concepts. Again, this I'm telling to Saurabh and all the audience who are watching. So if you're a fresher, so much of in-depth React would not be asked. So some basic they would touch on and just some some small fuzzle can be asked in most of the product and the service-based companies also. Okay. So why do you think React has advantage over the basic JavaScript or basic vanilla JavaScript HTML? What are the advantages of React.js? Why somebody should use it?

### 00:15:23 · Speaker 2

So let's compare with the basic things. Okay, so let's have some, let's, we want to some build some applications. So in JavaScript, we want, we have to write some code, extra code for that some feature. Like imagine we want, we are like building a card. So we want some state management. So for that state management, we need to write code in vanilla JavaScript to achieve that functionality. While someone, if someone uses the, the React, he gets,

### 00:15:53 · Speaker 2

that's these kind of pre-built features like we can use context API or Redux for state management so and there are other advantage also like the component based architecture and and also some like they are they are also provide like routing and other kind of stuff

### 00:16:15 · Speaker 1

Great, great sorrow. So these are all true, okay? See, but the very basic quality of React that makes React to be choosable. So whatever you are saying, all the things can be done in Venla JavaScript also, correct? Because ultimately everything is actually done in Venla JavaScript only, all right? See, one main concept that everyone, you and the freshers need to know is a reconciliation, okay? Reconciliation is also called reconciliation. So that's the core difference because that is what makes React faster, okay? I'm not telling what is reconciliation to you or the audience. Please go.

### 00:16:45 · Speaker 1

and read the consolidation it's a very very important concept that's what the main foundation of react why somebody should use the react okay so now let us start with a fuzzy okay uh i'm just gonna share a link with you the chat please open this link in a fresh window of browser and present your screen okay you can only present that particular tab in the browser stop obviously there's a lot of research that has gone into making this video so please like the video and subscribe to my channel and press the bell like

### 00:17:15 · Speaker 1

if you're not already done so and add a comment whatever you've felt so far the reason for that i always say i have only motive i help want to help the candidate to clear that interview so if more likes more comments video becomes visible for a lot whenever it is visible for a lot and there is a high chance i get more subscribers in the followers definitely the there is a high chance i would be able to reach my cause very soon okay so please like and comment about the video before watching the further okay

### 00:17:39 · Speaker 2

I hope my screen is visible

### 00:17:40 · Speaker 1

Yes sir your screen is visible

### 00:17:46 · Speaker 1

Let's get started. But before starting, let me let us let I'll ask you a few very basic questions of the React days. Okay. So now so what which component is currently used in in this example?

### 00:17:58 · Speaker 2

Okay so we are using app component

### 00:18:00 · Speaker 1

Yes so it's a function component correct

### 00:18:02 · Speaker 2

Yeah function based yeah

### 00:18:04 · Speaker 1

Yes correct so do you know what is the bare main difference between functional component and a class based component?

### 00:18:11 · Speaker 2

Okay so class-based component basically uses the uh

### 00:18:15 · Speaker 2

uh class-based things like constructors static words and like setting state also have some difference in text in that

### 00:18:24 · Speaker 1

Correct, correct. There are a lot of differences and eventually we are reaching a state where a lot of people have not used class components. Somebody like you was just starting, right? They might have started itself with a functional component and this question is not so usual now to ask the difference. Okay. Yes. So React is something called JSX, correct? So can you tell me what is JSX in React?

### 00:18:47 · Speaker 2

So GFX basically stands for JavaScript XML

### 00:18:51 · Speaker 2

If you want like to explain some beginners so we can say that it's we are using inside STM8

### 00:19:02 · Speaker 1

So do do you see any advantage of using JSX over the plain HTML or something like that

### 00:19:09 · Speaker 2

I think we can do certain of things like without changing the whole whole DOM we can use some variables and keywords and like let's say we want something here

### 00:19:24 · Speaker 2

can use some some kind of variables here

### 00:19:27 · Speaker 1

Got it

### 00:19:28 · Speaker 2

I thought it can't be

### 00:19:29 · Speaker 1

Correct. What you're saying is correct. Otherwise, you would have actually, you have to fetch an ID and append or change the values, et cetera. Correct. That is one, but the little more also the advantages of JSX. Please read that. Okay. Now, see, I'm not asking so many questions on React, but I just want you to know how fundamentally you're strong in building the UI in React. Okay. Question is very simple, Sarub. Basically, you need to create four input fields. Okay. The first name, the last name, email ID, and the phone number. Okay. And just one submit button.

### 00:19:59 · Speaker 1

Okay, so now to start off with, let us keep it this way. You have to validate this form basically. First name and last name cannot be empty.

### 00:20:08 · Speaker 1

and phone number has to be 10 digit email actually meet the regular expression of the email okay whenever user click submit you will get all the values but that user has entered and you will validate and any any error is there let us just alert it like invalid email id if there are more than one errors are there like uh first name is also not entered and email id is also invalid then let us try to show whatever whatever the first alert is like first first only first name is not there then let us show that and stop okay after they enter and hit submit let us show the second error this is what

### 00:20:38 · Speaker 1

I want you to build we would have around 10 to 15 minutes to solve this completely sorry okay please get started

### 00:26:33 · Speaker 3

I'm the last fighter

### 00:26:34 · Speaker 1

It doesn't matter

### 00:26:35 · Speaker 3

Four five

### 00:27:15 · Speaker 3

Is it a good state of the art so

### 00:29:53 · Speaker 1

Let's just validate for the first name uh sorry considering the time constant let's say have you will do okay if first name is not there you have to show the alert

### 00:30:40 · Speaker 1

It's triggering even before you click right

### 00:30:47 · Speaker 2

So let me see

### 00:30:49 · Speaker 1

Exactly good you figured it out

### 00:30:54 · Speaker 2

Now I see there's nothing in it

### 00:30:58 · Speaker 1

Very good very good

### 00:31:02 · Speaker 2

reload it will reload because like we haven't said that event.preventDefault

### 00:31:08 · Speaker 1

Exactly

### 00:31:10 · Speaker 1

Sure, Saurav. We can stop sharing. Okay. As we have almost last five minutes now, we'll spend some more time on overall feedback that I want to pass it on to you. Okay. You can stop sharing. I'll also tell whether you're select or reject from mine.

### 00:31:25 · Speaker 1

If this arrow, that's what, like I mentioned, whatever, I'll just tell mistakes that you did in the problem solving. This will help you and the audience. First thing, get little more clarity regarding the requirement. Interviewer themselves may not tell everything to start off whether there is importance for the styling or not. Like you coded a very basic and very neat UI, but you did not ask whether the interviewer expectation is that or not, correct? For example, he want a more stylish kind of a UI, but you did not ask. He also, interviewer may not.

### 00:31:55 · Speaker 1

say this and whenever you say that was the expectation then he would ask you did not ask what is the requirement correct that's one second uh this is maybe you know this but some people may not know what is the regular expression to validate email that's quite common and all interviewer do not expect candidate to know that so be vocal don't think like interviewer will feel bad or he will reject if i ask him can i search the email id a regular expression on the internet most interviewer will be fine with that because regular expression do not define you correct ask in such

### 00:32:25 · Speaker 1

scenarios okay then coming to the functionality whatever you did was good so plan for the duration that you have let for example you have like 10 minutes right so divide the deliverables into modules so that at least one module can be delivered so only ask you to stop at the first name correct every interviewer will not tell that so you decide the code in such a way where at least one module can be catered in the given time if something is not catered still we can tell this is we are able to give this much okay so that interviewer happy not having at least rather not having anything interviewer

### 00:32:55 · Speaker 1

happy something something is there at least all right so plan in that way in the practical coding uh interviews okay done from my end so tell me how was the overall interview experience

### 00:33:07 · Speaker 2

It was quite good I learned a new tons of new things like how to prepare and how to like organize myself

### 00:33:15 · Speaker 1

Correct, correct, sir. So I always say this not to you, to all the freshers. So don't start web development at the front end just from the point of the development. Start from the extreme fundamentals of network protocols and understanding the language so that you can build anything on top of it whenever it is required.

### 00:33:34 · Speaker 1

Sure sorry that's all from my end nice talking to you have a good day bye

### 00:33:39 · Speaker 2

Yeah, thank you

