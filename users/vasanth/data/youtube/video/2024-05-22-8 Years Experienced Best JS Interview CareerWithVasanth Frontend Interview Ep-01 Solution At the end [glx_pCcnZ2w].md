---
id: glx_pCcnZ2w
title: 8 Years Experienced Best JS Interview|CareerWithVasanth Frontend Interview
  Ep-01|Solution At the end
url: https://www.youtube.com/watch?v=glx_pCcnZ2w
date: '2024-05-22'
duration: 00:24:23
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
---

speaker_1: Hello all welcome back to career with Vasant YouTube channel Previously this channel was known as uncommon geeks My name is Vasant So with me today I have Kriti Suman So this is a session where we are primarily spending on the mock interviews So in this particular session Im going to take a combination primarily a JavaScript questions Ill be asking Kriti already has seven plus years of experience Maybe I would end up asking some couple of software engineering sort of software development or software engineer sort of questions as well Okay And without wasting further time lets get started Kriti if you can introduce yourself

speaker_2: Yeah sure So I have total 7 point 0 one year of experience and totally Im working in the Angular framework and I started from Angular 2 and right now its an Angular 11 and apart from this Im just working in the banking domain and leading the team as well and I have sorts of the knowledge in the JavaScript Nodejs apart from the Angular

speaker_1: Wonderful Wonderful Yeah Kirithi Kirithi let us let me start by asking a very simple question Okay So in Angular application Im very sure you might have built something for the authentication flow Correct Ill ask you only two flows whether you built it or not but its very common interview question where a user logs in to your website and after login So basically next time lets say they close the tab and open next time definitely will not ask them to log in again Same how Facebook YouTube Instagram everything works As long as youre logged into

speaker_2: Wonderful wonderful

speaker_1: the application you continue to login correct can you just explain me this entire authentication flow kruti how do we how will we achieve this i tried presenting a whiteboard would you like to draw the basic architecture here

speaker_2: Sure

speaker_1: Yeah thank you

speaker_2: So suppose that this is the uh page where uh I am just creating a login uh page basically


Its a login here

speaker_1: That is fine yeah and Im primarily interested in the different elements that would interact with each other like it was the caching the back end Im interested in like which all system in how they interact yeah

speaker_2: Checking out


So from here we are just making some data to our caching moment cache controller And it is not here like that simply because whenever we are just passing some data from this component we are also using the salt encryptions there So we are encrypting our passwords

speaker_1: Mm mm

speaker_2: And that passport we are loading in the our cache systems And in the cache systems we have some token expirations session as well So Ill provide some token here and with some timeline


Once it is faced the cache it will go to the my server side So server will have to validate whether the token is the validity or not or expiration is there or not So that cache will be stored there So suppose second time again I am coming to my login page and since that time I dont have a cache right So if before sending my data directly to the server through the my browser is it will first go and check in the cache whether the data is available in there or not

speaker_1: Correct correct

speaker_2: So it will not repeatedly every time call the server API again and again So it will stop here itself If that is suppose expired it doesnt mean that it will again call the server because its expired Then it will just try to give some pre flight XHR to this guy Pre flight

speaker_3: No problem

speaker_2: So this pre flight XR and it will just try to knock the door on the server side whether the data is available with you or not So it will again because this data is directly integrated with the CAS system as well so the server will respond to this CAS systems And from here as we are using the Google Chrome or the V8 engines so it will directly interpret with this CAS only So it will not go to the server directly Thats how we are handling it

speaker_1: Sure So Kriti like Ill try to summarize Okay So we have a website Okay So and whenever user tries to log in Okay Lets say this is a login button As soon as user tries to log in

speaker_2: And

speaker_1: what we are doing is as soon as they log in so basically you we are making API call getting the user information correct and lets say youre getting some token that token youre sure storing it in the cache system correct


This is a cache where you are storing Okay So youre storing this cache So next time lets say user has closed the tab and opened the tab next time You will check whether in the cache whether the token is available If token is available then you will take user directly to some login screen to home screen

speaker_2: So this is a cache


Actually next

speaker_1: Correct Home or the home is just an indicator here like wherever your core of the application correct So there you will take the user whenever you have a valid token correct Lets say the token is expired Whenever the token is expired so you are saying you will make an API call Am I right Like pre flight user

speaker_2: Yeah


You will take the

speaker_1: You make an API call here is the server correct So here is server where we will make an API call Get the token back Once you get the token back youre again going to store that in the cache and the process repeats correct


So let us understand yeah elaborate yeah if you want to add any more points you can add

speaker_2: If here is the again I am to get the token so that will be match here itself again with the one another service we have created so we will just take if the token is available in from the state management or not and we are only updating our expired date or expiry time okay so we know that the token is already available for entire of the system


Thats how its continues it

speaker_1: Okay sure Again Ill summarize quickly Kriti So I as a user came to your website I clicked I entered my email ID password I clicked on like login As soon as I click on login you made an API call got the token you stored the token And next time whenever I open the application you checked whether the token is available in the cache get that particular token And if it is valid you are gonna go take me to home screen If it is invalid you are gonna make an API call to server to get a new token correct So now only question that I have is


Ive stopped the whiteboard so only question I have is first of all how do you get to know like the token is valid or not next time whenever I open the website

speaker_2: So in that conditions actually the uh that is why we I just told that pre flight or exit charge mode right so every time when I open

speaker_1: So every time when I open you make an API call then with that whether to check whether the book is valid or not

speaker_2: Yeah and we are also using some interceptors in our Angular application or entire applications So that is going to make the sample pre flight mode access our call And then it is checking it there itself whether that is available or not So we can just expand our expiry time from the front end side not the back end always

speaker_1: Okay so in the overall process Kriti how many tokens are involved one token two token how many tokens are involved

speaker_2: I think there is only one token per user

speaker_1: Okay so that is the

speaker_2: That is the

speaker_1: Got it What what is that token you call Like what do you refer it as Authentications and authorization

speaker_2: Authentication that is also involved with the authentication only not with authorization things

speaker_1: Okay sure

speaker_2: Sure


So the we generally tell it as a session ID in our term and that is only for help for the


Authentication purpose

speaker_1: Okay sure Sounds good Kruti There are a lot more details required for this Probably Ill explain if time permits at the end Okay but whatever you said so far is not wrong but there like we can add more clarity into this Okay so can you like present your Chrome one window where nothing is opened only like can you open the plain Chrome window Ill share a online editor link with you and please open this link Okay


So can you tell me the difference between session storage and local storage

speaker_2: So session storage is just like suppose I have a store my data in here in the session storage and if I will close the my browser or even I close the tab my session is gone already Okay And if I will inspect it my session storage data will be not available there Okay But in case of the local storage if I will close my system as well and entire Google Chrome as well but still my storage will be a storage whatever the data I have stored


It will be available there Even I will come and log in again my data will be there

speaker_1: Okay I have two follow up questions on this Okay so session storage whatever you are storing is it accessible


Even when like multiple tabs are open from the same web application like for example this website what we open is program mscom correct I open the same website in another tab in the same browser So both the tabs can access the session storage Got my question right Kriti

speaker_2: Yeah I got your point No I think in the session storage when I just open my one tab only the data will be available here itself

speaker_1: You cannot share this between the tab

speaker_2: I dont see it this way


Yeah

speaker_1: Okay if audience who are watching like I always say the best way to get use of this mock interview is like you try answering whenever I ask a question pause the video try to answer and see what is the answer candidate giving so that you get a sense Yeah sure We will discuss Kriti Now another follow up question that I had also on the local storage Like you told local storage is storage That is like even if you close the window or even if you restart the system that storage is going to be always present unless probably we clear the browsers cache correct So now the question is lets say youre not open website like program


Ms Dole

speaker_2: Yeah

speaker_1: This website you have not opened Is there any way without opening that website you can access the local storage things the data that you have stored Got my question right

speaker_2: So yeah so you are meant to say that from what I understood you wanted to close the browser and you wanted to access somewhere else right

speaker_1: No no lets say

speaker_2: No no lets say

speaker_1: See this program iscom this saved some information in the local storage Okay And I closed that that tab I close I open googlecom now Okay So is there any way I can access the local storage values that are stored by program iscom But my question right now I think it is clear

speaker_2: I close that


I need it


Yeah its good yeah

speaker_1: Yeah thank you Without opening the website can we access the local storage data that was saved or persisted by the website

speaker_2: Yeah I think yes we can get it Okay Because our local data will be there and there right We have to just only say get the items So if that is available we can get it right

speaker_1: Okay lets say Im aware of the key with which you saved Like lets say we saved the key as like login underscore key And if I try to get access to that like localstoragegetitem login underscore key just execute that in the inspect Chrome inspect You think Ill be able to get that Got my question I think Im clear Krithi correct

speaker_2: Actually Im aware of the key


Yeah yeah yeah

speaker_1: Okay okay

speaker_2: I think you cannot get it

speaker_1: It is tis then youre saying it is stored in the

speaker_2: Stored

speaker_1: Yeah we are saying it is stored persistently but you cannot access without opening the website correct

speaker_2: Yes yes

speaker_1: So are you aware of call apply bind Kriti

speaker_2: Yes

speaker_1: Uh can you write an example for all the three call apply and yeah you can remove whatever is here and write the yes remove everything and you can start giving an example call apply and

speaker_2: So suppose that uh

speaker_1: You write it fully then well discuss

speaker_2: So I just have created the two users and I wanted to because that is available in some other function so what I can do


I can uh


Think the reference of this print will mess up the


and then Ill apply with the call method here and then I can just pass the user one or two whatever it is So this will reference to this with the help of the this keyword actually is happening here

speaker_1: Mm

speaker_2: and uh what the here right ill forget to mention that this keyword here that this dot


first name and this dot last name here so it will try to refer this guy and now it is asking which one is referring so this will refer whoever immediate objects are there calling

speaker_1: Yeah

speaker_2: So it will give the output like this And with the help of the apply method and the call method most things that I suppose I wanted to pass multiple arguments like here


I have some kind of like a country as well


CT as well


So here I can just pass


Yeah


And then Bangalore


Like this individually elements I can create and I can pass it as an argument a particular parameter But in the apply method what is happening I can just create one array type and inside that I can just do that So same thing will happen there With the bind method what is happening like same way its bind here but bind is always available for your future reference not for current


So suppose that you wanted to call that functions in the futures so you are you can just only pass some reference to that the bind method

speaker_1: Okay sure So Kruti whatever explanation you gave is good I think most when I ask in the interview everybody gives this example only But you have seven years of experience Kruti Tell me the practical use case When did you use call apply bind

speaker_2: was creating one functions okay and then I got to know that I have to create a one utility class of the functions as well but since whatever the items I had here right Im not so sure what is the argument someone is passing there because that was using some split and rest operator as well so only I came here written functions and then I use the the functions which Im passing here I use the generate dot apply method here itself so it was taken


the function as a callback functions and whatever the arguments or parameters we were passing it was referring to this guy again that this keyword with the help of the apply method

speaker_1: Got it sure sure okay Kriti I am sending a code snippet in the chat section okay copy the snippet and paste the snippet


in the same window and try to guess the output for the same And audience whoever watching you can also just look at the snippet and try to guess the output

speaker_2: So when I will try to invoke it it should print like this


For one


And if I will just try to print it it should print as a zero because this guy is taking the scope will be the same quantum method here So again it will become zero

speaker_1: Please run the code good

speaker_2: Im not sure

speaker_1: Can you can stop sharing Kati okay So Im done from my end Kati and uh this is the time where I give my feedback to you But before I give my feedback you have any questions for me like primarily around the interview have any questions

speaker_2: Now its all good go far uh very good I am very much interested in this

speaker_1: Yeah please

speaker_2: So yeah I would like to ask more than we can just discuss more on the local store system that you asked


Yeah

speaker_1: Yeah sure Kirti Like probably if time permits we can discuss any other topics that I asked in the interview But let me this is an important case for me to give feedback to you And its also applicable with a lot of candidates who are watching the video See primarily everybody whos watching the video consider a fact like if youre somebody whos having an experience of more than six years

speaker_2: Yeah

speaker_1: Then you are considered like a senior developer in an organization So the primary expectation from you is like how do you basically create a system and manage it So that is the reason I ask you authentication flow right There is no one right way or wrong way I dont even consider that like a system design a deep system design sort of a question but very basic level question correct What you explained was not wrong But there can there was an opportunity where you could have induced more clarity like step by step probably how we can proceed further


Okay so thats a small feedback for anybody who goes for interview or who are having like six plus years of experience Make sure you go with an extreme clarity about the things that you explain Im not saying like you dont know the concepts but interviewer will have a very short time and within that time frame only they need to judge you So try to give very crystal clear answers And then next so next question like whatever I asked in the local search and session storage right So by looking at those answers quickly like what can we infer is you knew the concepts Like for example


Like would if I ask you to like question like how to create a session storage how to create a local storage you could have created the questions that I asked probably you were not anticipating


So where Im coming from is like my advice to all basically who are watching this video is have the temperament of why in your mind like why basically this is happening So whenever you keep asking why then only you will identify discover some questions because reading an article or reading an article reading the official documentation or YouTube video may not trigger that So you should start asking why multiple times So probably then you will get into that temperament of reading Okay And snippet you are able to interpret excellently


Nikruti which is good I think whatever you know at least whatever you answered so far So you have clarity on some complete clarity Some you are having little bit of mediocre clarity So where I want you to just polish your skills


My honest feedback is you tell me if there are any closing questions for our last two minutes

speaker_2: Uh like uh I just really would like to work more on the authentication authorization since I didnt get a much more chances as from the we are building a product for some other product based company So we dont have that much control over

speaker_1: Got it Yes Yes I understand Kriti But like I told you your experience these things matter So even if youre not got an opportunity please try to learn on your own So that next interview when this is asked youre able to answer and clear that interview Okay


Sure So yeah we are closing the session Kruti I hope the session was useful You like the question that I asked

speaker_2: Yeah sure obviously its very helpful for me and I I can also always practice on those

speaker_1: on it sure sure thank you so much for joining the session kruti and uh taking the market with me and audience whoever watch the video please like the video if you think it is useful for your friends also share with them if youre not already subscribed to my channel carry with us please subscribe and whatever the question that i asked to kruti in the video ill try to make a short extension to this video but i try to explain answers to that thank you so much for watching catch you in the next video yeah hello all im sure you liked the session with kruti and in this particular video its a very short video post video basically im discussing the


question that I asked in the interview okay that uh Kriti did not answer properly the first question is the local storage and session storage where I asked like uh the data between session storage in between two tabs is it shared so answer is no the data cannot be shared between the two tabs of the same website lets say you have uh googlecom and googlecom slash home so in googlecom you stored some value in the session storage and you want to access it from googlecom slash home youll not be able to access okay second question I asked is


local storage the value that you are storing in the local storage can you access it even when the website is not opened yes you can access it use if you know the right keys to the local storage whatever you are storing okay so it is a security concern so if you are storing some information in the local storage make sure you are not storing the sensitive information even if you are storing sensitive information then make sure it has a quite proper expiry date or you also at least you are encrypting it so that somebody some random person is not able to access those


information okay now the another important question that I asked was the authentication flow okay let me try to uh present a whiteboard and see if I can uh show that okay so like I asked therell be like your website is here and you have a local storage or a session storage depending on your requirement and you have a server okay so let me name it as like this is your website and this


is your cache okay and this is your server this is your this is your server


So now


Important thing to know here is how actually the authentication would work Okay so if I have to draw a line


between the three okay first whenever you log in what the what the website will do is it will it will make a call to the server okay and from server it will get back a valid token okay and that valid token will be stored in the cache okay and next time whenever you user trying to log in the web will ask the token from the cache and see if the token is available in the cache and if it is available then it will not make any api call okay it lacks a token from there for some reason if it knows the token is expired


here then again we get back to this flow where we would make a first we would make a call to we will check from server and we will get back and well check from server well store it in the cache and well use so now the very important thing to know is like how many uh how many tokens are actually involved so again there are multiple implementations one of the most common implementation ill tell so therell be two tokens one is authorization token another one is the access token okay access token will uh usually last for a very long duration


of time so whenever you log in the first you will get one token using that token youre going to make an api call and you will get an authorization token so whenever you log in the first token that backend sends will be access token using access token you will get an authorization token authorization token usually have a timestamp depending on the different website but let us consider like like one hour of validity after one hour auth token is expired and using the access token you make an api call because your backend cannot be reached without any valid token correct so you keep getting the access token using the you keep getting the


authorization token using the access token okay and there will be a time when your access token also will expire like usually the access token will expire in a long after long duration it could be like 10 days 20 days or 30 days depending on the sensitivity of the website or how critical information that we are being storing okay when the access token is expired a lot of website log out the user and you have to freshly log in and the process continues some websites whenever access tokens expire right even in that time they will have a separate api call to get the access token so they get back


access token and then they get the authentication token and the process continues and a lot of these websites how they handle this is theyll have a centralized place for making the api call so we call them interceptors or like one particular library for making api call all the calls will be usually going through there and whenever token expiry happens both access token and authentication token these services or interceptors make sure they call the calls are waiting and they get a fresh token and then they will um like theyll fast follow all the api calls that have been pending okay


This is how an authorization entire authorization flow can be handled Again multiple different ways are there If how you are handling in your organization mention that in the comment section If youre not already subscribed to my channel carry this person please subscribe In case if I missed answering some of the important question that you wanted to know please mention that in the comment section Ill answer Thank you so much for watching Thank you for watching
