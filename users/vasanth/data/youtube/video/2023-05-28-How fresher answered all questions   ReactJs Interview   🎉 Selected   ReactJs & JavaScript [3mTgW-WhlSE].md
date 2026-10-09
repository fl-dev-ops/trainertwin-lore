---
id: 3mTgW-WhlSE
title: "How fresher answered all questions | ReactJs Interview | \U0001F389 Selected\
  \ | ReactJs & JavaScript"
url: https://www.youtube.com/watch?v=3mTgW-WhlSE
date: '2023-05-28'
duration: 00:34:50
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# How fresher answered all questions | ReactJs Interview | 🎉 Selected | ReactJs & JavaScript


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. My name is Vasanth. I hope you're all doing well. So in today's mock interview with me, I have Surajan. So this is going to be around 30 minutes of video where I'll be talking, I'll be interviewing Surajan with respect to front-end technologies. I'll be asking you basics of HTML, CSS, JavaScript, React. And maybe last five to 10 minutes, we'll also discuss about one DSA problem. So it's going to be a good session. So please watch the video till the end. We'll start the video by Surajan's introduction. Surajan, over to you. Can you please introduce yourself?

### 00:00:28 · Speaker 2

Yeah, so as you already have mentioned, my name is Srijan. I am in my final year of my engineering in the stream of computer science, obviously, and I am pursuing it from a college based out of Kolkata and coming to my experiences and all. So I've been into working with web technologies since like for like two years and I have had three past internship experiences as well. And right now I'm working as a full stack intern in a startup named Sprinto.

### 00:00:57 · Speaker 1

One thing

### 00:00:57 · Speaker 2

Thank you that's all from my side

### 00:00:59 · Speaker 1

Wonderful. See, whenever I interview a fresher, I ask this question, very common question. A lot of people actually struggle a lot to find an internship. Like, you know, I don't know your college. Maybe you might be from premium or you may not be from premium college. There are a lot of people who are actually not from a premium college. They find it very hard to find an internship, surgeon. So, but you said you already have done already two internship and there is a third internship by the time when you are in final year. Can you just help my audience probably what are the right means to get into internships?

### 00:01:29 · Speaker 2

So like there is no rule of thumb as such but like I've been focusing on my skills and trying to get as deep a knowledge as possible in those skills and like for like for the first six to seven months I solely focused on the practical knowledge like building projects then doing finding like internships and all and then like when I got like the foundation got strong then I tried to get more deep into the like

### 00:01:59 · Speaker 2

the topics like the code javascript concepts and all so i guess yeah so if someone does that i guess he or she can probably land a internship or a job

### 00:02:09 · Speaker 1

Wonderful. So basically you say, don't just apply. First, have a strong fundamental knowledge. Once you have acquired the knowledge, then look out for internship. I only have just one last question before we start the interview. Like, do you refer you like you, what are the right means to get internship? Is it like using internshala, sites like internshala or using LinkedIn? What are the right sources you recommend?

### 00:02:28 · Speaker 2

Okay, okay, so I have like tried my hands on many platforms. So like LinkedIn, the angel list, which is now known as Wellfound and Cubit also, which is a new platform. But yeah, actually I landed my recent internship from Cubit only. Cubit, I also.

### 00:02:45 · Speaker 1

I also have a

### 00:02:46 · Speaker 2

Any value

### 00:02:48 · Speaker 1

A spell it's a

### 00:02:48 · Speaker 2

CU yeah CU V E double T E cube it cube it dot take is the domain yeah

### 00:02:55 · Speaker 1

Wonderful, wonderful. Yeah, so yeah, like how Sujan has landed the internship, maybe you guys can also go. I don't know any of the website he said. It's no, no recommendation from my side. But just if somebody can get an internship, all my followers also get an internship if you're really having caliber. So please go ahead and check out whatever Sujan is saying. Sujan, let us start with the interview. Okay. This is how I generally start with very extreme basics of the JavaScript. Maybe my audience might have also seen in the other interviews of mine.

### 00:03:22 · Speaker 1

Can you please tell me what are promises in JavaScript version?

### 00:03:27 · Speaker 2

Okay, so like promises are basically like the objects which lets us facilitate the asynchronous tasks in JavaScript. So like if I have to explain like what promises do, so if there is a task that's not gonna happen synchronously, like an API call or something, which, but it will take some time to execute, then we can use a promise to execute that task asynchronously. And when we use a promise, then the task goes into the microtask queue.

### 00:03:57 · Speaker 2

Once it gets resolved or rejected it depends what happens then we get back the response and we can like get the response by using dot then to if it is resolved or dot catch if it is rejected or there is an error

### 00:04:12 · Speaker 1

So promise is basically used whenever we have to perform certain things asynchronously network call is one good example

### 00:04:19 · Speaker 1

There is an another function called promise.all have you heard about promise.all

### 00:04:19 · Speaker 2

No

### 00:04:23 · Speaker 2

Yeah I've heard

### 00:04:25 · Speaker 1

Please tell me what is promise dot all

### 00:04:26 · Speaker 2

So, okay, so promise.all basically helps us when we want to like perform two, three asynchronous tasks concurrently. Like if there are, so first, let's suppose there are three API calls and we want to execute them asynchronously and concurrently. So we can just pass the array of promises and it basically returns us with the response in an array as well. But if one of them fails, then whole the promise.all gets rejected.

### 00:04:56 · Speaker 1

So can you give me one right use case region with your internship experience when do you use a promise at all

### 00:05:02 · Speaker 2

Okay, okay. So like if there is an area of IDs, I guess, and we want to query for all those IDs. And like I've seen many people do it using async await, but that doesn't happen concurrently. Actually, so it happens when one ends and the other starts. So instead of that, we can do a promise.all. Like we can first get the area of promises.

### 00:05:32 · Speaker 2

we can use the promise.all object to resolve or reject them and yeah so these are some use case so if you want to like get data for an array of ids query using that we can use promise.all and i've used that in my internship as well

### 00:05:48 · Speaker 1

Wonderful, wonderful suggestion. Good that you know it in depth. Let us talk a little bit about the concurrently concurrency that you're talking multiple times. Okay. So whenever you pass multiple promises to a promise.all, after that, how the execution will happen? Can you talk more on that suggestion?

### 00:06:03 · Speaker 2

yeah so basically uh if there are three promises and uh first what will happen is three of the promises will be ex the request will be sent and like concurrently for the first request for the first promise will be sent if it is an api call the sec for the second also it will be sent and for the third also it will be sent but whenever what happens is like whenever like one of the promise or all the promises get resolved it basically gets accumulated in the

### 00:06:33 · Speaker 2

array of responses and it gets returned so the only difference between concurrency and like happening it happening sequentially is like concurrently it actually like throws the requests uh like one after the other and it gets executed like parallelly but there is a bit of difference between parallel and concurrency but yeah

### 00:06:53 · Speaker 1

Yeah I want you to talk more on that Sujan can you talk what is the difference between concurrency and parallel

### 00:06:58 · Speaker 2

Okay, so like parallelly, suppose like there are three promises and it's not like three of them are sent parallelly, like at the same time, at the same point of time, at concurrency, it's the first one is sent, the second one is sent, and then the third one is sent. And then the execution happens parallelly. Then the thing goes parallelly and once one of them or two of them gets resolved, it gets accumulated in the area of responses. And parallelly is when three of them are sent like at the same point of time. That's not what happens actually.

### 00:07:28 · Speaker 1

Why parallel is not possible situation

### 00:07:32 · Speaker 2

Okay, so I don't have too much depth on that, but I guess like it's like not possible to like push three of them in the microtask queue at the same point of time. That's not right.

### 00:07:46 · Speaker 1

got it now why parallelly cannot execute is because javascript a single thread no process can happen on that node parallelly correct at that time only one one process can be processed okay

### 00:07:53 · Speaker 2

That time only

### 00:07:57 · Speaker 1

So uh yeah let us talk a little bit about the event loop situation as we are very close to that only we are discussing talk more about event loop why event loop is necessary what is event loop

### 00:08:07 · Speaker 2

so is a event loop basically gives us the power to do the asynchronous tasks tasks and also basically when we use a set timeout and all so it goes to the macro task queue and first what happens is first the ex call the the tasks of the main thread gets executed and when like uh the event loop actually checks key uh if the main thread is empty and once it's empty it basically pushes the tasks from the

### 00:08:37 · Speaker 2

uh micro task queue or macro task queue first the micro task queue happens then the macro task queue and it gets executed so the event loop basically checks key if the main thread is empty and if it's empty then it basically pushes it to the main thread and the execution and the console logging all happens

### 00:08:54 · Speaker 1

So then let us get into little more details. So let's say there are three, one statement that is console.log. There is second statement which is set timeout. Third statement, let us again consider console.log. Okay. With the help of event loop, can you explain me how these three statements will be executed? Let's say set timeout is for three seconds.

### 00:09:12 · Speaker 2

Okay, so first, like JavaScript executes synchronously. So first it will, when encounter the first console log, it will get logged. Then what it will see that there is a set timeout, which is a, which is an OWP and it is an asynchronous task. So it will be pushed to the macro task queue.

### 00:09:30 · Speaker 1

So will it be first moved into the main queue or not? Or will it be directly taken into the web API or another queue that you use?

### 00:09:38 · Speaker 2

Yeah, it will be directly first pushed to the macro task queue, not in the like the main thread. It will push to the macro task queue. And like then the third, then the second console log, not of the third, but the second in the main thread will happen. And then after in the when the set timeout expires, like the time that we have already passed, like three seconds, as you mentioned, when it will be passed, then what will happen is the event loop will like after three seconds, it will check that if the main thread is empty.

### 00:10:08 · Speaker 2

now and if it is empty then the console log will push to the main thread and then it will happen and it will get logged I guess like pretty much console

### 00:10:17 · Speaker 1

Nothing wrong, sir, but even more clarity can be added to this. Okay. I recommend reading that official blog, official documentation at developer.mozilla.org. Now let's get to the same, let's go back to the example that we were discussing with promise.all. So promise.all, let's say you're passing three promises, they execute concurrently and the array of response comes back. All right. So with the event loop concept, where do you think the waiting is happening? Because three promises happening concurrently. All right.

### 00:10:47 · Speaker 1

after after they start triggering it's parallel like you said once only triggering is concurrent then they execute parallelly so where is the wait happening to accumulate all the result and then process it

### 00:10:58 · Speaker 2

Uh you mean like the act when the API is being called and we have to wait for the response to come back

### 00:11:03 · Speaker 1

Not that also that is fine but actually promise.all should return array of promises like all the promise that has returned correct

### 00:11:08 · Speaker 2

All the problems

### 00:11:10 · Speaker 1

So now there has to be a process that is waiting for all these promises to resolve, club it into one array and send as a response. Let's get to the positive flow where all promises are resolved. Okay. So in that case, somewhere the wait has to happen to accumulate all the promises. Do you know which layer this accumulation happens?

### 00:11:27 · Speaker 2

Okay, uh, I get your question. So, uh, this, uh, this thing basically happens, uh,

### 00:11:35 · Speaker 2

in the main thread, I guess, like I'm not fully sure, I'll be honest, but I guess that accumulation of the results, pushing it into the area and returning it happens in the main thread and not the other.

### 00:11:48 · Speaker 1

So please read a little more okay on this for this particular topics now let's let's start with some basics of reactors

### 00:11:56 · Speaker 1

Tell me one reason why do you think React is faster than plain HTML and vanilla JavaScript

### 00:12:03 · Speaker 2

So React actually has a concept of virtual DOM, which is an in-memory representation of the actual DOM. That is a tree. So basically what happens is like using the virtual DOM, a diffing process goes on under the hood in React. So when we have changed something, it basically does the diffing. There are two snapshots of the DOM, the previous one and the current one. The diffing algorithm happens, which is known as reconciliation. And when it's

### 00:12:33 · Speaker 2

is that there are like the a change in the HTML and it basically what it does is it then actually uh exhibit interacts with the actual DOM and not like not from the first times because interacting the real DOM is a bit expensive

### 00:12:50 · Speaker 1

with non-stop obviously there is a lot of research that has gone into making this video so please like the video and subscribe to my channel and press the bell icon if you're not already done so and add a comment whatever you've felt so far the reason for that i always say i have only motor of i help want to help a candidate to clear their interview so if more likes more comments video becomes visible for a lot whenever it is visible for a lot and there is a high chance i get more subscribers in the followers definitely the there is a high chance i would able to reach my cause very soon okay so please like and comment about

### 00:13:20 · Speaker 1

the video before watching the further okay now

### 00:13:23 · Speaker 2

So I guess that makes a reactor faster option

### 00:13:27 · Speaker 1

Got it. So, so Strijan, do you see that is there any flow where React might be slower than plain HTML and JavaScript?

### 00:13:37 · Speaker 2

react might be slower uh so uh like the the virtual dom is actually tree and when a parent re-renders uh the child's all the children also gets re-rendered so uh there might be some cases when like there are unnecessary re-renders happening under the hood which we can optimize but out of the box there are many unnecessary re-renders that may happen so in that cases uh it might become slow as a slower option

### 00:14:07 · Speaker 2

Of the

### 00:14:08 · Speaker 1

So whenever the program is not written properly is a problem across everything. I mean, that is not an edge case. Like even HTML says also somebody can write a program to run unnecessarily. Let's shift to ideal scenario where programs are written quite well. Okay. Do you see a scenario where plain HTML and vanilla JavaScript might work faster compared to React?

### 00:14:31 · Speaker 2

So uh

### 00:14:34 · Speaker 1

Or you can also s say I agree that the react plain HTML JavaScript will be never faster than react what is your take

### 00:14:41 · Speaker 2

Okay, so, uh, no, I'll like, I know that in some cases, uh, plain vanilla JavaScript comes out faster of the two, uh, but like the exact, uh, why, when and why it happens is, uh, so, uh, if there is an ideal case, then, uh,

### 00:14:59 · Speaker 2

It might be uh

### 00:15:03 · Speaker 2

Like when uh like when there is not much uh a interaction with DOM so their vanilla JavaScript can actually come out faster.

### 00:15:16 · Speaker 1

Sure, Sujan. You can read little more. See, these are all the not questions that generally asked by everyone. So, as you know, most interviews, they just stick to the some basics. I generally go to extreme basics, so I'm asking, but it's good to know, okay? Because when you think one is superior over another, not you, everybody thinks only people are using React. So, we should know where probably superiority is not up to the mark, okay? No problem. Now, let's get into some, some, another, other concepts of React, okay? Can you please tell me what are higher order components, Sujan, in React?

### 00:15:47 · Speaker 2

So a higher order component is a component that takes in a component as a parameter and returns an updated component. So it's like higher order functions only, but in React, it is referred in terms of component. Like it takes a component as a parameter and returns an updated component. That is basically a higher order component.

### 00:16:07 · Speaker 1

correct so give me one example susan i don't expect you to give a practical example if you know from some internship you can tell but otherwise also get try to give me one example not from built-in function some example that you think uh right use case for hierarchal component

### 00:16:24 · Speaker 2

Yeah, so like if there is a page and like I'm going to solely UI from the UI perspective and we want to attach a sidebar to all of it and some custom logic. So we can use a higher component like with sidebar and we can dump all our logic regarding the sidebar in the higher component and we can return the updated component like from that HOC.

### 00:16:49 · Speaker 1

So is it something where you can also use a normal component and put some conditions and render the sidebar components?

### 00:16:59 · Speaker 2

Uh, yeah, like the reusability of the logic can be done in many ways, uh, but HOC is one thing that can come in handy in this case.

### 00:17:08 · Speaker 1

Sure sure that is then why I ask this this one of my common question why I ask you see any optimal technique that you would use

### 00:17:16 · Speaker 1

That should give you capability which otherwise you are not getting. Because every optimal technique has its own problems. Using use memo, use callback, they have their own disadvantages also. So whenever you want to use them, you have to be sure they really add advantage. Use case, what you are saying is correct. It's not wrong. There could be even more optimal use cases for higher order components.

### 00:17:36 · Speaker 1

So now let us talk a little bit about the hooks in this region. Can you please tell me why hooks are necessary in React functional components?

### 00:17:47 · Speaker 2

Yeah so hooks gives us the power like of what class components had like with states it before hooks the function components were stateless components so hooks has given the power of using states inside functional components so some basic like hooks are we use use state to like populate the state of the component local state of the component also there are other hooks like use effect to

### 00:18:17 · Speaker 2

trigger side effects from rerenders and all

### 00:18:21 · Speaker 1

Got it. Sure. So hooks basically give work one of the capability that you mentioned is functional components or statelet stateless. So hooks have made functional components stateful. Correct decision.

### 00:18:34 · Speaker 1

Any other capability that hooks have given to functional component

### 00:18:39 · Speaker 2

Uh, yeah, like nowadays we can use custom hooks to do to like facilitate the reusability of any logic like like instead of HOCs we can all there might there will be some use cases we can go with use like custom hooks also. Correct. Yeah.

### 00:18:57 · Speaker 1

Got it

### 00:18:59 · Speaker 1

Sure, please elaborate like when do you think is the right scenario to use a custom hook?

### 00:19:05 · Speaker 2

So like personally what I have used like in each of the components we do a lot of API calls so we can make our own custom hook like use API call and we can in the in the hook custom hook itself we can like have three states like loading error or data has been returned and we can use that like to we can use that hook in the component to manage all our API calls and

### 00:19:35 · Speaker 2

And using that hook also we can get three states of the API call, it can be in like the error, the loading, or if the data has been passed. So it makes us, it makes much more intuitive to the programmer.

### 00:19:46 · Speaker 1

Got it. Got it. Sure. What example you're giving, Sajin, is absolutely right. Okay. So my question more towards is like, can you tell me on generic flow? Like, for example, when do you use a function? When you have a meaningful logic that can be clubbed together, we would use a function, right? So when do you use a custom hook?

### 00:20:05 · Speaker 2

You know to uh when we need uh need a reusability of logic like when we want to reduce reuse logic then we'll use a custom

### 00:20:14 · Speaker 1

So then in that case you can use utility functions also there is just the reusability is required

### 00:20:19 · Speaker 2

In the custom hook, we'll need some state like in a util function, we like in a normal util function, we can't have state in the custom hook, we can have states in it as well. So in that cases, yeah, you are right. In that cases, we'll use custom hook like when the custom hook will have states and all in it.

### 00:20:40 · Speaker 1

So to summarize this region oh whenever there's a requirement where you have where you want a reusability of the logic

### 00:20:48 · Speaker 1

Then you also need react capabilities re reusability of a logic plus the reusability of react capabilities you would go with the hooks mr decision

### 00:20:57 · Speaker 2

Yeah absolutely okay that's what I meant

### 00:20:59 · Speaker 1

Sure, Susan, whatever you're saying is right. So my question was like, let's come back to the first question where you were referring to hooks gave a capability of state management to functional component. And my add-on question was anything else that it would give? Custom hooks is fine. Anything else you think the hooks have given to functional component?

### 00:21:20 · Speaker 2

Like other than making it stateful some other things like

### 00:21:26 · Speaker 2

I guess it makes it makes it much more intuitive like to the programmer because component did mount and all was a bit hectic to the programmer so it's one small advantage that hooks provide cut it yeah I guess yeah

### 00:21:44 · Speaker 1

That's it. So another thing, as you already mentioned, you have to tell one is the state management, which is right. So second one is the lifecycle management, correct? Lifecycle management is also given to functional component. Otherwise, it was not there. Lifecycle methods, correct? So now hooks have given a lifecycle methods to the functional component.

### 00:21:57 · Speaker 2

I've given a life cycle

### 00:22:02 · Speaker 2

Yeah true

### 00:22:04 · Speaker 1

I'll ask you maybe one last question, then we'll go to a small DSF as well. See, in the class component, not sure whether you worked or not, maybe at least you might have read about the class components, correct? So in class component has a method called render, right? So render inside the render, you would write all the code that gets rendered. Have you at least studied it, Sajin, if not, work?

### 00:22:26 · Speaker 2

Uh yeah like I have a bit of knowledge regarding that and I have touched it in a legacy code of an internship but it was like one year ago

### 00:22:37 · Speaker 1

Yeah, sure, no worries. See, my question is this. Basically, there is a functional component. You are starting from where app J is till any component that you would write everywhere there are functions and the functions are returning something, a component.

### 00:22:50 · Speaker 1

where is the mechanism actually to render that particular code that is written have you ever given a thought where is the rendering capability happening

### 00:22:58 · Speaker 2

in React

### 00:23:01 · Speaker 1

But from your code structure whenever the client

### 00:23:03 · Speaker 2

the class it was actually a question so you are asking it is a query to the question so you are asking when the actual rendering process happens in real

### 00:23:14 · Speaker 1

My question is, see, every function is returning something. Okay. Let's say a project full of functional component. Okay. So every function is returning some or the other component. So returning something from a function will not render anything on the screen directly. Okay. So even re-rendering whatever you are talking is not at the component level. It is at a much higher level. Okay. Every component is returning something. So there has to be some mechanism to render it on the screen.

### 00:23:41 · Speaker 1

From you the code whatever the code that you have written do you know where is that exact code or exact piece that is responsible for rendering the component that are written

### 00:23:49 · Speaker 2

I guess the react-dom.render method which actually does that stuff of rendering and interacting with the DOM. There is a thing called Babel which actually transpiles J6 with code to actual the code that the browser will understand and then the rendering goes on.

### 00:24:09 · Speaker 1

not wrong but it can be more clear okay so please read a bit about this as well okay so yeah can you just open js fiddle if you want i can share the link and you can present your screen

### 00:24:23 · Speaker 2

I will share the screen too if you guys want Yes yes

### 00:24:25 · Speaker 1

Yes yes yes please share

### 00:24:34 · Speaker 2

Is it visible

### 00:24:38 · Speaker 1

So let us start with some small snippet with my experience of talking to you mostly you will answer it right but let's like let audience also get to know this

### 00:24:51 · Speaker 1

So give me a

### 00:24:56 · Speaker 1

I'm sharing a snippet with you in the chat. Please copy the snippet and paste it in the JavaScript site.

### 00:25:07 · Speaker 1

I think a little bit in the top the zoom whatever the sharing you did

### 00:25:10 · Speaker 2

Yeah yeah I got it

### 00:25:13 · Speaker 1

Sure sure

### 00:25:18 · Speaker 1

Yeah please paste yeah can you zoom in a bit

### 00:25:21 · Speaker 2

Yeah sure

### 00:25:23 · Speaker 2

Is it visible

### 00:25:24 · Speaker 1

Maybe more two yeah maybe one more maybe one more plus yeah

### 00:25:27 · Speaker 2

You want more plus

### 00:25:31 · Speaker 1

Please try to guess the output

### 00:25:33 · Speaker 2

Okay uh so uh

### 00:25:36 · Speaker 2

the we are using a bad it is a function expression yes so uh when uh

### 00:25:45 · Speaker 2

this will actually be consoled world is beautiful and next time when it will uh like encounter this thing so it will throw an error that uh c name is not a function because it gets hoisted as undefined as it is a we are using var key audio

### 00:26:03 · Speaker 1

Absolutely right. Okay, so this is the last question that I'm asking you, Stujan. Okay, you don't have to write a code to this, just copy whatever I sent in the chart and replace the existing content. We'll discuss your approach towards this DSA problem.

### 00:26:25 · Speaker 1

Maybe you can I mean make

### 00:26:28 · Speaker 1

expand the JavaScript layer so that that is in the center kind of

### 00:26:34 · Speaker 1

And maybe now we can zoom in two more times

### 00:26:37 · Speaker 1

Even though it's visibly

### 00:26:40 · Speaker 2

Is it uh Oscar Zoome more

### 00:26:41 · Speaker 1

Yeah one more zoom you do please

### 00:26:47 · Speaker 1

Please read the question okay and tell me what have you understood about the question then you can talk about then we can talk about the approach

### 00:26:56 · Speaker 2

I'm just reading it

### 00:27:19 · Speaker 2

So, uh, so there will be an, uh, what I've understood is, so there is an area of inputs and we have to find the common prefix like the number of letters that are actually similar.

### 00:27:33 · Speaker 2

we are starting with the traversing of the string so in this case afl is uh is the is a common prefix in all three of these correct uh like a likely a in this case uh actually since we have a string named other which actually does not the prefix does not match with the these three so we are returning uh empty string in this case so uh

### 00:28:00 · Speaker 2

Coming to the solution what we can do is uh

### 00:28:05 · Speaker 2

So uh we just uh

### 00:28:18 · Speaker 2

Okay, so we can actually take a, like we can actually take one of the strings, it will be better to take the largest string or the smallest string in this case, and we will use the length and traverse it from zero to that length. And what we will do is we will have the i, which will be the index, and we'll check if it is matching for all the four, like, or all the strings.

### 00:28:48 · Speaker 2

has been in the array so in this case if it is test here so we will traverse from zero to the last which will be zero to four and we'll check key if the zeroth index character is same for all this and if it is same then we will go to the next and if it is not then what we will do is we will return a empty string in that case

### 00:29:16 · Speaker 1

So yeah, just I'll reiterate whatever you said, Surajin. So what you're saying is like first to identify a string that is of the shortest length.

### 00:29:25 · Speaker 1

you will run the loop till the shortest length and you constantly check each word um in every iteration to see whether the all the characters are in that particular word all the words are same or not

### 00:29:37 · Speaker 2

Save it yeah

### 00:29:39 · Speaker 1

So let's come to the complexity part Sujan what is the complexity here

### 00:29:44 · Speaker 2

So uh

### 00:29:45 · Speaker 1

Time complexity

### 00:29:46 · Speaker 2

yeah yeah for taking out the smallest string we will uh have a of n complexity big of n and then uh also like the next part when we are actually taking out the common prefix also uh

### 00:30:02 · Speaker 2

the the general number of uh same operations it will also be big o of n in that case because uh when we are at uh the zero zeroth index we are just checking uh key uh okay uh just give us

### 00:30:28 · Speaker 2

In that case it will be a O of n squared actually because we'll also have to check that the zeroth index for all the elements are same

### 00:30:39 · Speaker 1

So we go of n square plus n so obviously it is it'll be going to be n square

### 00:30:45 · Speaker 2

Yeah yeah yeah

### 00:30:47 · Speaker 1

You can stop sharing strategy

### 00:30:50 · Speaker 1

So fine, Sajjan, like pretty much I'm done. So let us, we have almost five more minutes. Let's use it for my, my feedback session. Okay. But before I share my feedback towards your overall interview, you have any questions for me, Sajjan, just for this interview?

### 00:31:04 · Speaker 2

mm uh for this interview like uh

### 00:31:08 · Speaker 2

What do you think one area like I can be better which will already still in your feedback but still I'm asking

### 00:31:15 · Speaker 1

Same, sure, sure, Sujan. See, one thing that I like, Sujan, let's start with the positive points that with my discussion of around 25 minutes, what I feel very positive about you is one is the communication skills, very good communication skills. There's a little bit of a scope for improvement, but like finally, we are not somebody like a politician who talk all the time, correct? As long as we are able to articulate what we know, that is the communication that we look for that you have. Fluency can be improved a bit, but communication as a skill is good. Second thing is the technical knowledge to a depth that you have.

### 00:31:45 · Speaker 1

I often interview a lot of experienced people with five, six years experience. They would not know whether promise.all is a parallel execution or a concurrent execution. On that note, you really have understood the concept to a very in-depth level. So I say this to audience also who are watching this video. Please understand it at least to a level that Surajna has understood because that will give you the mastery about the overall web development. And even coming to the React concepts as Surajna, they also have good knowledge. So whenever I ask you what capability

### 00:32:15 · Speaker 1

hook use or probably when is the right scenario to build a custom hook those are something that comes only if you have built something uh if you you can study a lot of things how to build a custom hook and what are hooks etc but you wouldn't get to know a right scenario for hook unless you have worked on it okay so which see it is we don't have to judge you whether by looking at your internship certificate have you done internship or not by asking questions only we'll get to know what sort of work you have done on that one these are all the very good points

### 00:32:43 · Speaker 1

to the second part where little little bit of a things to improve is what i say is so you know concepts to a very decent depth but there's still a some scope like i mentioned in few scenarios correct where you can dig further deep and understand it so why because javascript is as you know it's not a straightforward language even for a very experienced person people get confused sometimes why this is happening etc correct you can spend little more time understanding it a point number one and point number two is a dsa problem i know we had a little bit of a time crunch still don't attempt the question directly

### 00:33:13 · Speaker 1

Like you started telling the approach straight away, right? So you should always take some time, synthesize the overall whatever the problem that is you are doing, and then you have to tell what is the solution. Okay. As you also understood, like you thought it is n, but it's n square. There will be some optimal approaches. Like even if you spend five minutes now, you may find some approach with n.

### 00:33:35 · Speaker 1

So take some time to understand and then attempt, especially the DSA. Because once you said one approach and started writing, so you are halfway already out of the interview. Because when there is an N solution, N approach is possible for an easy problem. You're writing N square approach. It's mostly that is done, correct? So be very cautious whenever you are telling an approach, especially in the DSA. But web development solution, I liked overall, whatever your skill sets are. Like if I am in a hiring panel, that I would definitely select you.

### 00:34:06 · Speaker 2

Thanks for some really feedback

### 00:34:08 · Speaker 1

Yes any other questions Regan

### 00:34:11 · Speaker 2

Uh

### 00:34:12 · Speaker 1

Just for the interview yeah

### 00:34:12 · Speaker 2

Just for the interview

### 00:34:14 · Speaker 1

One in two yeah

### 00:34:17 · Speaker 2

As of it like I got your points and what other what other things where I can probably work on to make it better yeah I guess yeah

### 00:34:24 · Speaker 1

or so yeah then nice talking to such an audience whoever have watched i think this is a very meaningful uh uh mock interview that i have taken there are very few mock interviews that i have taken but luckily i've got very competitive interview interview also whenever i'm taking the interview so i think you also practice all the questions and whatever the way such an has answered so read more about all these questions that will definitely make you fundamentally strong thank you so much for watching catch you in next video

