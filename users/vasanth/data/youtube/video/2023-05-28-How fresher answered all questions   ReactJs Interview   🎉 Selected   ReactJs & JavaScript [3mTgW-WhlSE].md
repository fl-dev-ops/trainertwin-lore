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
  speaker_1: null
  speaker_2: null
---

speaker_1: Hello all welcome back to Uncommon Geeks My name is Vasanth I hope youre all doing well So in todays mock interview with me I have Surajan So this is going to be around 30 minutes of video where Ill be talking Ill be interviewing Surajan with respect to front end technologies Ill be asking you basics of HTML CSS JavaScript React And maybe last five to 10 minutes well also discuss about one DSA problem So its going to be a good session So please watch the video till the end Well start the video by Surajans introduction Surajan over to you Can you please introduce yourself

speaker_2: Yeah so as you already have mentioned my name is Srijan I am in my final year of my engineering in the stream of computer science obviously and I am pursuing it from a college based out of Kolkata and coming to my experiences and all So Ive been into working with web technologies since like for like two years and I have had three past internship experiences as well And right now Im working as a full stack intern in a startup named Sprinto

speaker_1: One thing

speaker_2: Thank you thats all from my side

speaker_1: Wonderful See whenever I interview a fresher I ask this question very common question A lot of people actually struggle a lot to find an internship Like you know I dont know your college Maybe you might be from premium or you may not be from premium college There are a lot of people who are actually not from a premium college They find it very hard to find an internship surgeon So but you said you already have done already two internship and there is a third internship by the time when you are in final year Can you just help my audience probably what are the right means to get into internships

speaker_2: So like there is no rule of thumb as such but like Ive been focusing on my skills and trying to get as deep a knowledge as possible in those skills and like for like for the first six to seven months I solely focused on the practical knowledge like building projects then doing finding like internships and all and then like when I got like the foundation got strong then I tried to get more deep into the like


the topics like the code javascript concepts and all so i guess yeah so if someone does that i guess he or she can probably land a internship or a job

speaker_1: Wonderful So basically you say dont just apply First have a strong fundamental knowledge Once you have acquired the knowledge then look out for internship I only have just one last question before we start the interview Like do you refer you like you what are the right means to get internship Is it like using internshala sites like internshala or using LinkedIn What are the right sources you recommend

speaker_2: Okay okay so I have like tried my hands on many platforms So like LinkedIn the angel list which is now known as Wellfound and Cubit also which is a new platform But yeah actually I landed my recent internship from Cubit only Cubit I also

speaker_1: I also have a

speaker_2: Any value

speaker_1: A spell its a

speaker_2: CU yeah CU V E double T E cube it cube it dot take is the domain yeah

speaker_1: Wonderful wonderful Yeah so yeah like how Sujan has landed the internship maybe you guys can also go I dont know any of the website he said Its no no recommendation from my side But just if somebody can get an internship all my followers also get an internship if youre really having caliber So please go ahead and check out whatever Sujan is saying Sujan let us start with the interview Okay This is how I generally start with very extreme basics of the JavaScript Maybe my audience might have also seen in the other interviews of mine


Can you please tell me what are promises in JavaScript version

speaker_2: Okay so like promises are basically like the objects which lets us facilitate the asynchronous tasks in JavaScript So like if I have to explain like what promises do so if there is a task thats not gonna happen synchronously like an API call or something which but it will take some time to execute then we can use a promise to execute that task asynchronously And when we use a promise then the task goes into the microtask queue


Once it gets resolved or rejected it depends what happens then we get back the response and we can like get the response by using dot then to if it is resolved or dot catch if it is rejected or there is an error

speaker_1: So promise is basically used whenever we have to perform certain things asynchronously network call is one good example


There is an another function called promiseall have you heard about promiseall

speaker_2: No


Yeah Ive heard

speaker_1: Please tell me what is promise dot all

speaker_2: So okay so promiseall basically helps us when we want to like perform two three asynchronous tasks concurrently Like if there are so first lets suppose there are three API calls and we want to execute them asynchronously and concurrently So we can just pass the array of promises and it basically returns us with the response in an array as well But if one of them fails then whole the promiseall gets rejected

speaker_1: So can you give me one right use case region with your internship experience when do you use a promise at all

speaker_2: Okay okay So like if there is an area of IDs I guess and we want to query for all those IDs And like Ive seen many people do it using async await but that doesnt happen concurrently Actually so it happens when one ends and the other starts So instead of that we can do a promiseall Like we can first get the area of promises


we can use the promiseall object to resolve or reject them and yeah so these are some use case so if you want to like get data for an array of ids query using that we can use promiseall and ive used that in my internship as well

speaker_1: Wonderful wonderful suggestion Good that you know it in depth Let us talk a little bit about the concurrently concurrency that youre talking multiple times Okay So whenever you pass multiple promises to a promiseall after that how the execution will happen Can you talk more on that suggestion

speaker_2: yeah so basically uh if there are three promises and uh first what will happen is three of the promises will be ex the request will be sent and like concurrently for the first request for the first promise will be sent if it is an api call the sec for the second also it will be sent and for the third also it will be sent but whenever what happens is like whenever like one of the promise or all the promises get resolved it basically gets accumulated in the


array of responses and it gets returned so the only difference between concurrency and like happening it happening sequentially is like concurrently it actually like throws the requests uh like one after the other and it gets executed like parallelly but there is a bit of difference between parallel and concurrency but yeah

speaker_1: Yeah I want you to talk more on that Sujan can you talk what is the difference between concurrency and parallel

speaker_2: Okay so like parallelly suppose like there are three promises and its not like three of them are sent parallelly like at the same time at the same point of time at concurrency its the first one is sent the second one is sent and then the third one is sent And then the execution happens parallelly Then the thing goes parallelly and once one of them or two of them gets resolved it gets accumulated in the area of responses And parallelly is when three of them are sent like at the same point of time Thats not what happens actually

speaker_1: Why parallel is not possible situation

speaker_2: Okay so I dont have too much depth on that but I guess like its like not possible to like push three of them in the microtask queue at the same point of time Thats not right

speaker_1: got it now why parallelly cannot execute is because javascript a single thread no process can happen on that node parallelly correct at that time only one one process can be processed okay

speaker_2: That time only

speaker_1: So uh yeah let us talk a little bit about the event loop situation as we are very close to that only we are discussing talk more about event loop why event loop is necessary what is event loop

speaker_2: so is a event loop basically gives us the power to do the asynchronous tasks tasks and also basically when we use a set timeout and all so it goes to the macro task queue and first what happens is first the ex call the the tasks of the main thread gets executed and when like uh the event loop actually checks key uh if the main thread is empty and once its empty it basically pushes the tasks from the


uh micro task queue or macro task queue first the micro task queue happens then the macro task queue and it gets executed so the event loop basically checks key if the main thread is empty and if its empty then it basically pushes it to the main thread and the execution and the console logging all happens

speaker_1: So then let us get into little more details So lets say there are three one statement that is consolelog There is second statement which is set timeout Third statement let us again consider consolelog Okay With the help of event loop can you explain me how these three statements will be executed Lets say set timeout is for three seconds

speaker_2: Okay so first like JavaScript executes synchronously So first it will when encounter the first console log it will get logged Then what it will see that there is a set timeout which is a which is an OWP and it is an asynchronous task So it will be pushed to the macro task queue

speaker_1: So will it be first moved into the main queue or not Or will it be directly taken into the web API or another queue that you use

speaker_2: Yeah it will be directly first pushed to the macro task queue not in the like the main thread It will push to the macro task queue And like then the third then the second console log not of the third but the second in the main thread will happen And then after in the when the set timeout expires like the time that we have already passed like three seconds as you mentioned when it will be passed then what will happen is the event loop will like after three seconds it will check that if the main thread is empty


now and if it is empty then the console log will push to the main thread and then it will happen and it will get logged I guess like pretty much console

speaker_1: Nothing wrong sir but even more clarity can be added to this Okay I recommend reading that official blog official documentation at developermozillaorg Now lets get to the same lets go back to the example that we were discussing with promiseall So promiseall lets say youre passing three promises they execute concurrently and the array of response comes back All right So with the event loop concept where do you think the waiting is happening Because three promises happening concurrently All right


after after they start triggering its parallel like you said once only triggering is concurrent then they execute parallelly so where is the wait happening to accumulate all the result and then process it

speaker_2: Uh you mean like the act when the API is being called and we have to wait for the response to come back

speaker_1: Not that also that is fine but actually promiseall should return array of promises like all the promise that has returned correct

speaker_2: All the problems

speaker_1: So now there has to be a process that is waiting for all these promises to resolve club it into one array and send as a response Lets get to the positive flow where all promises are resolved Okay So in that case somewhere the wait has to happen to accumulate all the promises Do you know which layer this accumulation happens

speaker_2: Okay uh I get your question So uh this uh this thing basically happens uh


in the main thread I guess like Im not fully sure Ill be honest but I guess that accumulation of the results pushing it into the area and returning it happens in the main thread and not the other

speaker_1: So please read a little more okay on this for this particular topics now lets lets start with some basics of reactors


Tell me one reason why do you think React is faster than plain HTML and vanilla JavaScript

speaker_2: So React actually has a concept of virtual DOM which is an in memory representation of the actual DOM That is a tree So basically what happens is like using the virtual DOM a diffing process goes on under the hood in React So when we have changed something it basically does the diffing There are two snapshots of the DOM the previous one and the current one The diffing algorithm happens which is known as reconciliation And when its


is that there are like the a change in the HTML and it basically what it does is it then actually uh exhibit interacts with the actual DOM and not like not from the first times because interacting the real DOM is a bit expensive

speaker_1: with non stop obviously there is a lot of research that has gone into making this video so please like the video and subscribe to my channel and press the bell icon if youre not already done so and add a comment whatever youve felt so far the reason for that i always say i have only motor of i help want to help a candidate to clear their interview so if more likes more comments video becomes visible for a lot whenever it is visible for a lot and there is a high chance i get more subscribers in the followers definitely the there is a high chance i would able to reach my cause very soon okay so please like and comment about


the video before watching the further okay now

speaker_2: So I guess that makes a reactor faster option

speaker_1: Got it So so Strijan do you see that is there any flow where React might be slower than plain HTML and JavaScript

speaker_2: react might be slower uh so uh like the the virtual dom is actually tree and when a parent re renders uh the childs all the children also gets re rendered so uh there might be some cases when like there are unnecessary re renders happening under the hood which we can optimize but out of the box there are many unnecessary re renders that may happen so in that cases uh it might become slow as a slower option


Of the

speaker_1: So whenever the program is not written properly is a problem across everything I mean that is not an edge case Like even HTML says also somebody can write a program to run unnecessarily Lets shift to ideal scenario where programs are written quite well Okay Do you see a scenario where plain HTML and vanilla JavaScript might work faster compared to React

speaker_2: So uh

speaker_1: Or you can also s say I agree that the react plain HTML JavaScript will be never faster than react what is your take

speaker_2: Okay so uh no Ill like I know that in some cases uh plain vanilla JavaScript comes out faster of the two uh but like the exact uh why when and why it happens is uh so uh if there is an ideal case then uh


It might be uh


Like when uh like when there is not much uh a interaction with DOM so their vanilla JavaScript can actually come out faster

speaker_1: Sure Sujan You can read little more See these are all the not questions that generally asked by everyone So as you know most interviews they just stick to the some basics I generally go to extreme basics so Im asking but its good to know okay Because when you think one is superior over another not you everybody thinks only people are using React So we should know where probably superiority is not up to the mark okay No problem Now lets get into some some another other concepts of React okay Can you please tell me what are higher order components Sujan in React

speaker_2: So a higher order component is a component that takes in a component as a parameter and returns an updated component So its like higher order functions only but in React it is referred in terms of component Like it takes a component as a parameter and returns an updated component That is basically a higher order component

speaker_1: correct so give me one example susan i dont expect you to give a practical example if you know from some internship you can tell but otherwise also get try to give me one example not from built in function some example that you think uh right use case for hierarchal component

speaker_2: Yeah so like if there is a page and like Im going to solely UI from the UI perspective and we want to attach a sidebar to all of it and some custom logic So we can use a higher component like with sidebar and we can dump all our logic regarding the sidebar in the higher component and we can return the updated component like from that HOC

speaker_1: So is it something where you can also use a normal component and put some conditions and render the sidebar components

speaker_2: Uh yeah like the reusability of the logic can be done in many ways uh but HOC is one thing that can come in handy in this case

speaker_1: Sure sure that is then why I ask this this one of my common question why I ask you see any optimal technique that you would use


That should give you capability which otherwise you are not getting Because every optimal technique has its own problems Using use memo use callback they have their own disadvantages also So whenever you want to use them you have to be sure they really add advantage Use case what you are saying is correct Its not wrong There could be even more optimal use cases for higher order components


So now let us talk a little bit about the hooks in this region Can you please tell me why hooks are necessary in React functional components

speaker_2: Yeah so hooks gives us the power like of what class components had like with states it before hooks the function components were stateless components so hooks has given the power of using states inside functional components so some basic like hooks are we use use state to like populate the state of the component local state of the component also there are other hooks like use effect to


trigger side effects from rerenders and all

speaker_1: Got it Sure So hooks basically give work one of the capability that you mentioned is functional components or statelet stateless So hooks have made functional components stateful Correct decision


Any other capability that hooks have given to functional component

speaker_2: Uh yeah like nowadays we can use custom hooks to do to like facilitate the reusability of any logic like like instead of HOCs we can all there might there will be some use cases we can go with use like custom hooks also Correct Yeah

speaker_1: Got it


Sure please elaborate like when do you think is the right scenario to use a custom hook

speaker_2: So like personally what I have used like in each of the components we do a lot of API calls so we can make our own custom hook like use API call and we can in the in the hook custom hook itself we can like have three states like loading error or data has been returned and we can use that like to we can use that hook in the component to manage all our API calls and


And using that hook also we can get three states of the API call it can be in like the error the loading or if the data has been passed So it makes us it makes much more intuitive to the programmer

speaker_1: Got it Got it Sure What example youre giving Sajin is absolutely right Okay So my question more towards is like can you tell me on generic flow Like for example when do you use a function When you have a meaningful logic that can be clubbed together we would use a function right So when do you use a custom hook

speaker_2: You know to uh when we need uh need a reusability of logic like when we want to reduce reuse logic then well use a custom

speaker_1: So then in that case you can use utility functions also there is just the reusability is required

speaker_2: In the custom hook well need some state like in a util function we like in a normal util function we cant have state in the custom hook we can have states in it as well So in that cases yeah you are right In that cases well use custom hook like when the custom hook will have states and all in it

speaker_1: So to summarize this region oh whenever theres a requirement where you have where you want a reusability of the logic


Then you also need react capabilities re reusability of a logic plus the reusability of react capabilities you would go with the hooks mr decision

speaker_2: Yeah absolutely okay thats what I meant

speaker_1: Sure Susan whatever youre saying is right So my question was like lets come back to the first question where you were referring to hooks gave a capability of state management to functional component And my add on question was anything else that it would give Custom hooks is fine Anything else you think the hooks have given to functional component

speaker_2: Like other than making it stateful some other things like


I guess it makes it makes it much more intuitive like to the programmer because component did mount and all was a bit hectic to the programmer so its one small advantage that hooks provide cut it yeah I guess yeah

speaker_1: Thats it So another thing as you already mentioned you have to tell one is the state management which is right So second one is the lifecycle management correct Lifecycle management is also given to functional component Otherwise it was not there Lifecycle methods correct So now hooks have given a lifecycle methods to the functional component

speaker_2: Ive given a life cycle


Yeah true

speaker_1: Ill ask you maybe one last question then well go to a small DSF as well See in the class component not sure whether you worked or not maybe at least you might have read about the class components correct So in class component has a method called render right So render inside the render you would write all the code that gets rendered Have you at least studied it Sajin if not work

speaker_2: Uh yeah like I have a bit of knowledge regarding that and I have touched it in a legacy code of an internship but it was like one year ago

speaker_1: Yeah sure no worries See my question is this Basically there is a functional component You are starting from where app J is till any component that you would write everywhere there are functions and the functions are returning something a component


where is the mechanism actually to render that particular code that is written have you ever given a thought where is the rendering capability happening

speaker_2: in React

speaker_1: But from your code structure whenever the client

speaker_2: the class it was actually a question so you are asking it is a query to the question so you are asking when the actual rendering process happens in real

speaker_1: My question is see every function is returning something Okay Lets say a project full of functional component Okay So every function is returning some or the other component So returning something from a function will not render anything on the screen directly Okay So even re rendering whatever you are talking is not at the component level It is at a much higher level Okay Every component is returning something So there has to be some mechanism to render it on the screen


From you the code whatever the code that you have written do you know where is that exact code or exact piece that is responsible for rendering the component that are written

speaker_2: I guess the react domrender method which actually does that stuff of rendering and interacting with the DOM There is a thing called Babel which actually transpiles J6 with code to actual the code that the browser will understand and then the rendering goes on

speaker_1: not wrong but it can be more clear okay so please read a bit about this as well okay so yeah can you just open js fiddle if you want i can share the link and you can present your screen

speaker_2: I will share the screen too if you guys want Yes yes

speaker_1: Yes yes yes please share

speaker_2: Is it visible

speaker_1: So let us start with some small snippet with my experience of talking to you mostly you will answer it right but lets like let audience also get to know this


So give me a


Im sharing a snippet with you in the chat Please copy the snippet and paste it in the JavaScript site


I think a little bit in the top the zoom whatever the sharing you did

speaker_2: Yeah yeah I got it

speaker_1: Sure sure


Yeah please paste yeah can you zoom in a bit

speaker_2: Yeah sure


Is it visible

speaker_1: Maybe more two yeah maybe one more maybe one more plus yeah

speaker_2: You want more plus

speaker_1: Please try to guess the output

speaker_2: Okay uh so uh


the we are using a bad it is a function expression yes so uh when uh


this will actually be consoled world is beautiful and next time when it will uh like encounter this thing so it will throw an error that uh c name is not a function because it gets hoisted as undefined as it is a we are using var key audio

speaker_1: Absolutely right Okay so this is the last question that Im asking you Stujan Okay you dont have to write a code to this just copy whatever I sent in the chart and replace the existing content Well discuss your approach towards this DSA problem


Maybe you can I mean make


expand the JavaScript layer so that that is in the center kind of


And maybe now we can zoom in two more times


Even though its visibly

speaker_2: Is it uh Oscar Zoome more

speaker_1: Yeah one more zoom you do please


Please read the question okay and tell me what have you understood about the question then you can talk about then we can talk about the approach

speaker_2: Im just reading it


So uh so there will be an uh what Ive understood is so there is an area of inputs and we have to find the common prefix like the number of letters that are actually similar


we are starting with the traversing of the string so in this case afl is uh is the is a common prefix in all three of these correct uh like a likely a in this case uh actually since we have a string named other which actually does not the prefix does not match with the these three so we are returning uh empty string in this case so uh


Coming to the solution what we can do is uh


So uh we just uh


Okay so we can actually take a like we can actually take one of the strings it will be better to take the largest string or the smallest string in this case and we will use the length and traverse it from zero to that length And what we will do is we will have the i which will be the index and well check if it is matching for all the four like or all the strings


has been in the array so in this case if it is test here so we will traverse from zero to the last which will be zero to four and well check key if the zeroth index character is same for all this and if it is same then we will go to the next and if it is not then what we will do is we will return a empty string in that case

speaker_1: So yeah just Ill reiterate whatever you said Surajin So what youre saying is like first to identify a string that is of the shortest length


you will run the loop till the shortest length and you constantly check each word um in every iteration to see whether the all the characters are in that particular word all the words are same or not

speaker_2: Save it yeah

speaker_1: So lets come to the complexity part Sujan what is the complexity here

speaker_2: So uh

speaker_1: Time complexity

speaker_2: yeah yeah for taking out the smallest string we will uh have a of n complexity big of n and then uh also like the next part when we are actually taking out the common prefix also uh


the the general number of uh same operations it will also be big o of n in that case because uh when we are at uh the zero zeroth index we are just checking uh key uh okay uh just give us


In that case it will be a O of n squared actually because well also have to check that the zeroth index for all the elements are same

speaker_1: So we go of n square plus n so obviously it is itll be going to be n square

speaker_2: Yeah yeah yeah

speaker_1: You can stop sharing strategy


So fine Sajjan like pretty much Im done So let us we have almost five more minutes Lets use it for my my feedback session Okay But before I share my feedback towards your overall interview you have any questions for me Sajjan just for this interview

speaker_2: mm uh for this interview like uh


What do you think one area like I can be better which will already still in your feedback but still Im asking

speaker_1: Same sure sure Sujan See one thing that I like Sujan lets start with the positive points that with my discussion of around 25 minutes what I feel very positive about you is one is the communication skills very good communication skills Theres a little bit of a scope for improvement but like finally we are not somebody like a politician who talk all the time correct As long as we are able to articulate what we know that is the communication that we look for that you have Fluency can be improved a bit but communication as a skill is good Second thing is the technical knowledge to a depth that you have


I often interview a lot of experienced people with five six years experience They would not know whether promiseall is a parallel execution or a concurrent execution On that note you really have understood the concept to a very in depth level So I say this to audience also who are watching this video Please understand it at least to a level that Surajna has understood because that will give you the mastery about the overall web development And even coming to the React concepts as Surajna they also have good knowledge So whenever I ask you what capability


hook use or probably when is the right scenario to build a custom hook those are something that comes only if you have built something uh if you you can study a lot of things how to build a custom hook and what are hooks etc but you wouldnt get to know a right scenario for hook unless you have worked on it okay so which see it is we dont have to judge you whether by looking at your internship certificate have you done internship or not by asking questions only well get to know what sort of work you have done on that one these are all the very good points


to the second part where little little bit of a things to improve is what i say is so you know concepts to a very decent depth but theres still a some scope like i mentioned in few scenarios correct where you can dig further deep and understand it so why because javascript is as you know its not a straightforward language even for a very experienced person people get confused sometimes why this is happening etc correct you can spend little more time understanding it a point number one and point number two is a dsa problem i know we had a little bit of a time crunch still dont attempt the question directly


Like you started telling the approach straight away right So you should always take some time synthesize the overall whatever the problem that is you are doing and then you have to tell what is the solution Okay As you also understood like you thought it is n but its n square There will be some optimal approaches Like even if you spend five minutes now you may find some approach with n


So take some time to understand and then attempt especially the DSA Because once you said one approach and started writing so you are halfway already out of the interview Because when there is an N solution N approach is possible for an easy problem Youre writing N square approach Its mostly that is done correct So be very cautious whenever you are telling an approach especially in the DSA But web development solution I liked overall whatever your skill sets are Like if I am in a hiring panel that I would definitely select you

speaker_2: Thanks for some really feedback

speaker_1: Yes any other questions Regan

speaker_2: Uh

speaker_1: Just for the interview yeah

speaker_2: Just for the interview

speaker_1: One in two yeah

speaker_2: As of it like I got your points and what other what other things where I can probably work on to make it better yeah I guess yeah

speaker_1: or so yeah then nice talking to such an audience whoever have watched i think this is a very meaningful uh uh mock interview that i have taken there are very few mock interviews that i have taken but luckily ive got very competitive interview interview also whenever im taking the interview so i think you also practice all the questions and whatever the way such an has answered so read more about all these questions that will definitely make you fundamentally strong thank you so much for watching catch you in next video
