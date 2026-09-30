---
id: 9wR466-BQ4I
title: In 30 mins, Learn How to Create a Successful BookMyshow|Ticket Booking System
date: '2022-11-28'
url: https://www.youtube.com/watch?v=9wR466-BQ4I
description: "#javascript  #interview #systemdesign #frontenddeveloper \nUncommonGeeks\
  \ is a Youtube channel dedicated to helping candidates clear their interview. There\
  \ are close to 70+ videos and new videos will be uploaded every week. If you're\
  \ seriously preparing for interviews and looking for tips and tricks, please subscribe\
  \ to my channel and press the bell icon.\n\nJoin Uncommon Geeks community to discuss\
  \ with other developers: t.me/uncommongeek. \nTo talk to me one one one book a session\
  \ here: https://topmate.io/vasanth_bhat\n\nChapters:\nConcurrent Seat booking :\
  \ https://youtu.be/9wR466-BQ4I\nDynamic Seating layouts: https://youtu.be/9wR466-BQ4I?t=844\n\
  Rendering Dynamic stadium layouts: https://youtu.be/9wR466-BQ4I?t=1388\n\nIf you\
  \ want to be part of my next video, please register here: https://forms.gle/BiCxXUepjrZDoWJH7\n\
  \nWhat is frontend system design: https://youtu.be/gN8LQTff21g\n\n\U0001F525 How\
  \ Youtube System works ?\U0001F525 Frontend High Level System Design of Youtube\
  \ #youtube #interview: https://youtu.be/QJe0cBjlgog\n\nCOMPLETE SYSTEM DESIGN OF\
  \ GOOGLE DOCS [2022 LATEST] - Concurrent editing, Version history & More \U0001F525\
  : https://youtu.be/GYVLp0ekHdM\n\nInterviewPreparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/  \nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\
  \ \n\nGithub Repository that contains presentation: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/tree/main/Frontend%20System%20Design\n\
  \nJavaScript Custom implementation|polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:28:03
model: saaras:v3
transcript: true
---

# In 30 mins, Learn How to Create a Successful BookMyshow|Ticket Booking System

## Transcript

### 00:00:00 · Speaker 1

What I'll do is I'll book these two tickets. One and two. Here also I'll come and book one and two. Hope it is clear now. Now, so basically I'm just trying to simulate where now I just opened it in two different tabs, but there is a possibility where people are sitting in two different places in the world and they are trying to book the same seats, correct? Now, actually bookmaster is allowing you to select the same seats. So back end, uh need to send you certain information regarding the each seat because you need to

### 00:00:23 · Speaker 0

It is not

### 00:00:30 · Speaker 1

know whether that seat is already booked or not. That's the primary criteria, correct? So back end cannot just send how many rows are there, how many columns are there and you populate a matrix, that is not possible.

### 00:00:40 · Speaker 0

ऑल वेलकम बैक टू अनकॉमन गीक्स मैसेल्फ फसंथ आई होप यू ऑल

### 00:00:43 · Speaker 1

doing well. In case if you're seeing me first time on the internet, I'm a content creator. I help people to clear their interview. I make videos on interview preparation, also how to face the interview, tips and tricks to clear the interview. I have made lot of series in the past which has been appreciated by many with this regard. Link to those series will be somewhere on the screen also in the description section. Please go ahead and watch it. I also very often interview some inspiring personalities on my channel like who cleared the interview in the past for a very premium company, what was their interview preparation strategy, how they moved from service computer product company.

### 00:01:13 · Speaker 1

to know more about my channel, please subscribe to my channel and press the bell icon and watch all the videos. Okay? Now without wasting further time, let's get started. So this video is regarding the system design as you already seen on the thumbnail. So where I'll be taking, I have taken a very, very interesting system design subject today that is BookMyShow. Okay? For foreigners who are watching BookMyShow, it is just like event booking platform. I believe every country has one or the other website and every platform will have a similar kind of a problems. Okay? So without wasting further time, let's get started. How to build a book my show from the scratch.

### 00:01:45 · Speaker 1

As you know, this is not my first system design on the front end. I've already made a couple of videos about the YouTube, Google Docs and others. So, but you have to know certain basics about the system design if you directly land into this video. So how the pattern is going to be, what all aspects are there in the system design. So I've made a just short video for ten, fifteen minutes where I've explained all of that. Link to those video will be link to that video will be screen, also the description section. Please watch that video and come back because I assume you already know what is front end system design, what all questions will be asked in the interview, etcetera. And I'm going to straight away get started with this. Also very

### 00:02:15 · Speaker 1

important point like last my videos went beyond forty forty five minutes to where I tried explain lot of things. So this video I want to keep very short because because of which I have already prepared lot of things and come to this particular video. Okay. Now let's get started. So as you all know very first thing in the system design is the requirement where requirements are broadly categorized into two that is the functional requirement and the non functional requirement. To save some of our time I have already written down this functional requirement and the non functional requirement okay after book my show. So it's very common

### 00:02:45 · Speaker 1

from I believe all of you might have accessed as this platform is also free anybody can go now and also check out. Definitely booking a ticket cost you but checking the platform definitely doesn't cost you can go and check out the platform. What all I have listed in the functional requirement is definitely there is an authentication phase if you are booking a site or if you want to log in. So there is an authentication then user account there will be lot of system account related settings like probably your language preference or your profile picture email ID phone number all of that will come in user account section. There is also which

### 00:03:16 · Speaker 1

search based on the languages, screens, etcetera is there. Screen here you mean the let's say you want to see which movie is running in a with this mall's PVR or INOX. Those kind of search also is enabled in BookMyShow, okay? Then they also have a small OTT platform embedded into their website where you can go and check out the OTT kind of things. Then there's a ticket booking events. Ticket booking is one of the most common thing that happens in the BookMyShow. So ticket booking can be broadly categorized into two things. So ticket booking for events, okay? So event

### 00:03:46 · Speaker 1

in in simple example it could be a stand up comedy or somebody's hosting a party such kind of things where the seating layout is generally not very structured. lot of you if you've gone to some stand up comedy shows you'll know they generally happen at a pub bar restaurants etcetera where seating alignment is not so fixed. so depending on the crowd they arrange the chairs etcetera. so such such bookings do not have a seating layout. and they also have a

### 00:04:11 · Speaker 1

ticket booking for the place. Place here I mean the games. For example, whenever you might have gone to lot of sports activities that happen in India and abroad, where you have to book a seat in a stadium. So in stadium you might know which will have a capacity of fifty thousand, sixty thousand, sometimes more than one lakh people can sit in a stadium. Definitely there they cannot give you seat number and ask you to go and sit. I think some country may have it, but India as far as I have booked in a different stadiums, they only give you a zone. Like for example, this is top upper, top down, blue zone, red zone,

### 00:04:41 · Speaker 1

depending on how near you are to the players, depending on that they'll charge the amount. And you can go and sit in any seat available in this particular area. And I think they make sure it is not overbooked. Let's say the particular range has hundred seats, within that only you are kind of a hundred seats only allotted but there is no seat number that is given. Okay. And next is the

### 00:05:01 · Speaker 1

same ticket booking for place, ticket booking for kabaddi. I think this ticket booking for place here I mean place as in the the dramas and all the other activities that happen, okay? And ticket booking for activities. Activities one best example is the things like Wonderla which is in Bangalore, I think in other places in the Southern India as well. And there are could be equivalent amazing this one adventure park at different places. So they all come in the booking in the activities. So these are all the primary features of BookMyShow. If you want to quickly see

### 00:05:31 · Speaker 1

this is how the landing screen looks like. I think most already know I'm just showing and this is how the search screen would look like. So where you can search by movies, search by cinemas and there are lot more filters that you can add, okay? And whenever you scroll down you start seeing the different uh you start seeing the whatever is running. Like I mentioned this is the premiere. So there are events that are happening, okay? Then like I mentioned the OTT, you can see small small videos that uh small it has not become very big OTT as Amazon or Netflix but they also have certain content.

### 00:06:01 · Speaker 1

and in their website. Okay? So this is all the rough. I'm not going too much in detail. Anybody can go and check out the website is free. I'll link also in the description. Okay? Now.

### 00:06:11 · Speaker 1

So, these are all the functional requirements I've listed. Now let's quickly check out the non-functional requirement. So again, non-functional requirement pretty much remains same for all the major web applications or mobile applications where I've explained them pretty much in detail in my previous videos. But to go on, they are all like adaptability, how you make sure your website is opening in mobile web and the website, desktop, all of them in a like whenever you are in a bigger screen, it should adapt to bigger screen, whenever you are in a shorter screen, it should adapt to shorter screen. All of that has to be taken care definitely.

### 00:06:41 · Speaker 1

as a non-functional requirement. Then we have accessibility, how you make sure a blind person can come and book the ticket. Then we have the localization, actually BookMyShow if you know they have a local support of different Indian languages. So how you are gonna enable that. Globalization, I don't think is not required for BookMyShow. But in case in future if they want to expand it to different countries then globalization is required. Definitely the performance is one of the aspect that has to be taken care. Security, architecture, which architecture are you gonna go, the mono repo, micro front end or monolithic, which kind of an architecture. Then resource optimization is very very important.

### 00:07:11 · Speaker 1

important for the sites like BookMyShow, how you are going to store your resources so that you are not utilizing lot of the bandwidth while you are getting those, okay? But I'm not going to touch much on the non-functional requirement specific to BookMyShow, because I have an idea of keeping this video less than thirty minutes. So where I'll focus on very, very important problem that BookMyShow solves and all of you might have not know how these problems are solved. Let us start with the first problem. I've scoped only three things.

### 00:07:36 · Speaker 1

concurrent seat booking, dynamic layouts, booking seat for games, okay? So here games I mean booking seats for games in stadium, okay?

### 00:07:46 · Speaker 1

So I'll tell why it is very very quite interesting to know. Okay? So first thing is the concurrent seat booking. Okay? So concurrent seat booking here we mean

### 00:07:56 · Speaker 1

two persons trying to book a same seat at the same time, correct? So I've explained concurrent editing in my Google Doc system design video, how two people edit same document at the same time on the same line. Okay, it's a very interesting problem. In case if you have not watched that video, link to video will be somewhere on the screen also in the description section. Please watch that video, it's very very interesting how Google actually solves that problem. Now let us take this important thing, how BookMyShow is solving the concurrent seat booking problem, okay? So just for the sake as Kantara is one of the movies

### 00:08:26 · Speaker 1

from South India, as you all know, I also from South India. So this is one of the way just kept open, okay? So that we I can show demonstrate the bookings for you, okay? So let's say same tab actually is duplicated in two different things. I'll just refresh just to get the latest data.

### 00:08:43 · Speaker 1

Okay. So, so this is something actually I'm in the Pune, okay. I don't live in Pune but the BookMyShow has just switched to Pune. So it is something called Abhiruchi City Pride, Singa Sinhagad Road. Basically I don't know this place. If anyone of you from Pune and from this road please mention or if you already seen this place also please mention in the comment section, okay. Now here, I'm picking the two thirty show, okay.

### 00:09:09 · Speaker 1

two people I'm selecting a two thirty show, okay? Here also I'll do two thirty p.m. except for two people. So basically the same layout, whatever the layout you saw here and here are pretty much the same. Now what I'll do is I'll book these two tickets or one and two. Here also I'll come and book one and two. Hope it is clear now. Now, so basically I'm just trying to simulate where now I just opened it in two different tabs, but there is a possibility where people are sitting in two different places in the world.

### 00:09:39 · Speaker 1

they're trying to book the same seats, correct? Now, actually BookMyShow is allowing you to select the same seats. It is not restricting. Okay? Now, whenever you click on pay three twenty from one tab I am giving, okay, it is going to the next screen.

### 00:09:54 · Speaker 1

And from here whenever I click screen, see what it is showing? Sorry, something is not right. Sorry, that seems to be the seat is no longer available. Please, uh, again, uh, please try again with the other seats. See, basically, I haven't booked the seat here. I even haven't paid yet, correct? But still BookMyShow has kind of reserved the seat for you. Now you might have got how the concurrent booking happens. But let me talk about a little bit about different approaches of the concurrent editing, okay? So concurrent booking can happen in, sorry,

### 00:10:24 · Speaker 1

if I say concurrent editing, I wanted to say concurrent booking. Okay? Concurrent booking can happen in two way. One is a pessimistic way. Okay? Pessimistic way and another one is the optimistic way.

### 00:10:39 · Speaker 1

So what is pessimistic way? Pessimistic way will be a way where we will allow customers to book the tickets. Like both of both the places we will select the tickets and whenever they click on next, right? So whenever you click on next, it will take you to the next screen. So I can also select this ticket and somebody else can also select the same ticket. Then come to this screen. So here again you'll get like what is the total amount that I'm supposed to pay. Here also again it will not block. Only during the payment whenever you have gone to the payment, right?

### 00:11:09 · Speaker 1

exactly during the payment payment creation phase it will whomsoever basically do the first payment so for them the seat is allotted whomsoever does the payment later for them it says like no no longer the seat is available so this is a pessimistic pessimistic way of giving the seat booking so but the advantage of this is let's say what happened you saw now I just took I I just clicked on two seats and I hit next and actually I may not book the ticket at all but still the seat is blocked for me whereas the other person

### 00:11:39 · Speaker 1

person could be genuine where who is trying to get the real actual tickets but seat is no longer available for that person correct so uh but I think they have analyzed the pros and cons of both the both the things and they might have stick to the optimistic way what is optimistic way here where as soon as you select a ticket and click next button the ticket is locked for you for a particular duration of time I whatever I analyze it is around five to ten minutes for that duration of the time the seat is allotted for you so if in case by that time you go

### 00:12:09 · Speaker 1

add all your details and confirm the booking, then the seat will be allotted for you. If not, after ten minutes, if another user refreshes the screen, those two seats will be again available for them. I believe this ten minutes is configurable, whenever depending on the situation and the scenarios, they might be keep changing it. Let's say there is a mover which has lot of attention and they cannot wait for ten minutes, if the seat is already locked, they may reduce the duration to some some second minutes, but or it could be standard as well. I don't know, but I'm just saying this could be configurable number, okay? So this was about the concurrent seat booking.

### 00:12:39 · Speaker 1

booking problem. So concurrent seat booking problem, BookMyShow is actually solving in optimistic way by locking the seats for a particular duration of time. Okay, if two person trying to edit take the same seats, so whomsoever clicks the next first after selecting the seat, for them the seat is locked. Okay, for a particular duration of time and in that duration if they finish, finish their order by paying the money and other thing, the seat will be allocated for them. Okay, this is an interesting problem but this has a different narration from the back end point of view where they'll ask like where you're going to store this information.

### 00:13:09 · Speaker 1

of seat booking etcetera like cash storage or actual database etcetera but as it's a front end system design I'm not dwelling deep into that. Now let's go to the next problem which is according to me is one of the very very interesting problem that BookMyShow has solved that is the dynamic layouts correct. What is dynamic layout here I mean see I have I'm showing you the three different screens in the BookMyShow okay since randomly I have drawn here. So these are nothing but the movie halls correct. So movie halls could be like

### 00:13:39 · Speaker 1

VR, INOX, very popular malls or there could be also local theaters also there, correct? Each theater, I may not say each theater but most of the theaters are unique in one or the other way, correct? They do not have the layout same as the another. Same like our house, every house is kind of a unique one or the other way, correct? So layouts also will be layouts of each theater will be unique. Now, BookMyShow has to build a very generic logic to render all the different sitting layouts like whenever you get a layout like this, this or

### 00:14:09 · Speaker 1

It may seem easy like they'll just send like some matrix information etcetera. But it is not so easy like they cannot send you the entire information of this theater in few variables. It is not that easily possible. In case if you are someone who already know how this problem can be solved please mention that in the comment section right away, okay? Sorry to disturb you in middle. I believe you are enjoying the content that I am sharing so far and lot more interesting problems of BookMyShow are gonna be solved in next couple of minutes. But just please in case

### 00:14:39 · Speaker 1

If you like the content that I have made so far, please like the video on the YouTube and comment whatever you felt so far. So by liking and commenting, my video becomes more popular and becomes more visible to a lot of people. More visibility definitely gives me more impressions and more impression will in turn help me to reach my goal of helping a lot of people to clear the interview very soon. So please like and comment about the video and if you're not subscribed, subscribe to my channel and press the bell icon before watching further. Thank you. Otherwise, let me explain. So,

### 00:15:08 · Speaker 1

definitely. I have worked a lot to know the solution, but let us look at the system design if the same questions asked to you in the interview, how your thought process should be. So basically now you have to design a dynamic layouts like this, correct? So where each each theater is a unique, correct? Each theater is kind of let us take a scenario, definitely some PRs and INOX are similar, but let us take a scenario where each theater is unique, correct? So back end need to send you certain information about regarding the each seat because

### 00:15:38 · Speaker 1

You need to know whether that seat is already booked or not. That's the primary criteria, correct? So back end cannot just send how many rows are there, how many columns are there and you populate a matrix, that is not possible. Be practical, okay? Reason being there is a gap here, correct? And there is a gap here, two row gap here. And there is a two row gap here. So back end cannot send you just the rows and columns and you populate the matrix, matrix I think all of you are aware, to just the two directional one. You cannot populate the matrix on your own.

### 00:16:08 · Speaker 1

be very careful about that. So that option you need to propose to say interviewer if they ask and you need to rule out because that is not possible. Next what do you think? So definitely to show entire system layout, the theater layout.

### 00:16:22 · Speaker 1

You need to get information about each of the seats that exist in the theater, correct? So what do I mean by each of the seats? So for example, now let us take this example, this particular theater. So you have to send me how many rows are there and in each row how many tickets are there, how many seats are there? That's for example, let me just make it three, okay? So I'm just making it

### 00:16:45 · Speaker 1

three for the sake of example, okay?

### 00:16:53 · Speaker 1

there are three seats now. Okay, there are three seats in that particular row. Book my show back end or if you're desiring the system, your back end should send you information about the these three tickets and are they already booked or not. Let's say this is already booked. They need to give you an information, are they already booked or not. Only in that case, you can show the different layouts like this. Where you see right, there is a grayed out. All the tickets that are taken are grayed out. All the tickets that are not taken are in the green and they can be selected.

### 00:17:23 · Speaker 1

correct? So my point here is back end cannot send you just a couple of values where you populate everything on your not possible. Every seat information has to flow from the back end. Now you got to know this this point till this point you are clear. Now

### 00:17:39 · Speaker 1

So next thing is how do we show this empty things, correct? Definitely between each row there could be some gap. As you know most malls, last row will be like only one row, okay? Where it is kind of exclusive seat. After the further further rows might have certain divisions like this where there's a way to walk in middle or certain malls I've seen they have way on the left hand side entry or right hand side entry, all of that, correct? Now how do we do this dynamic layout? So if same question is given to you in the interview,

### 00:18:09 · Speaker 1

So how should be thought processes? See, now we are getting information about each of the seats. So whether that seat is selected or not. Then you have also should get the information about the the places that are not occupied or where there is a gap, okay? So now let us say you got one, two, three, okay? Let us take like this is a row A, okay? So this is A one, A two, A three and this is A four, okay? Now A4 is like a

### 00:18:43 · Speaker 1

space, correct? A four is a space which is not actually a ticket.

### 00:18:48 · Speaker 1

getting my ticket as in it is not a not a seat. Same way even here, this let's say this is like B four now. B four is also not a seat, correct? It is a space. So what if there are two spaces like this, correct? So where you kind of have this many number of information, let's say four ticket width which is actually not seats, okay? So in UI or the back end will send you in values in a certain way.

### 00:19:18 · Speaker 1

there only if it is a actual seat you will render it in a seat seat UI like this. if if you get a seat information you render it as a seat UI like this. if it is a space

### 00:19:30 · Speaker 1

whatever the value that is back and descending. In such cases you keep it as an empty and it is non clickable. Okay? With that you kind of technically build any layout, any possible layout you can build in such a simple way. Actually I was astonished after I studied BookMyShow in depth. I thought this is very very complicated problem to solve but BookMyShow has solved it in a such a easy way. Okay? Let me show that with a proof because you guys need a proof how it is actually happening. So, same this again I have opened the same

### 00:20:00 · Speaker 1

same movie and I have been the inspector window, okay? So where whenever, uh, whenever I clicked on this particular API, okay, which gives you the get data, not the get data, init screen, yeah. init screen footer.

### 00:20:16 · Speaker 1

do secure yeah. So this is the API whatever they are calling okay and they are giving you a preview with this particular soap information okay. where they have something called STR data.

### 00:20:28 · Speaker 1

all this information is available, rather I show you here, I've just copied this information and I've pasted it in my Google Docs, okay? So where for the same theater, as you can see this theater has three layouts, one is balcony, another one is a mini balcony, another one is a first class. For the all the three layouts, they have clearly shown here, okay? So where balcony is a they have categorized into mini balcony and for every row they are sending you the information. Actually they are not using a rest, they are using soap. I don't know the reason why.

### 00:20:58 · Speaker 1

why they are using soap and not the rest. There could be some rationale because the sites like BookMaker will have very brilliant engineers and they might have found a way why they are using the soap. Okay. So then

### 00:21:09 · Speaker 1

This is the first row how it look like and this is the second row. Okay? Now let us go to the second row and see after the tenth ticket you see a two space. Correct? So after the tenth seat here, okay? They send the empties like this a zero plus zero colon a zero plus zero, okay? I can try interpreting all these values what do they mean like a one zero one one, a one zero two plus two. Definitely I can tell what does it mean what is a one, what is zero thirty two all of that.

### 00:21:39 · Speaker 1

But I don't whatever I say it is a half truth because I have not built the system. But one thing is definitely clear whenever you observe every blank that you see in the screen they kind of notated by this zero zero notation. Okay? So here if you see this is a three zero which is the zero. Same place they are it also has an empty rows. So it is represented like this. Zero plus zero zero plus zero. Whenever UI is getting this kind of a value it is not rendering those and it is just showing the empty. Correct? So such a easy problem actually to solve.

### 00:22:09 · Speaker 1

but unless you have to spend a lot of time to analyze and understand. Okay? So basic, now I think I'll just summarize quickly.

### 00:22:17 · Speaker 1

the dynamic layout of different theaters can be easily solved with an approach where back end will send you information about every seat available in the theater and every blank seat that is available in the system and this blank seats are kind of populated okay and this blank seats are kind of populated I believe whenever a person their book my show executive goes and takes a pick and that kind of they may have some picks to data analysis etcetera or they may manually also add this depending on how much ever space they have and obviously

### 00:22:47 · Speaker 1

that only the layout is populated. Okay? Such an easy problem. I believe at least you like this explanation of how bookmash is actually handling the dynamic layouts. Now, we have another interesting problem to solve. Third problem. Okay? What is the third problem? Booking a seats for a games in the stadium. This is an again very very interesting problem. Why because every stadium is again unique. Okay? Let me show you the example.

### 00:23:13 · Speaker 1

So, where it is. Every stadium is unique again, okay? I this is actually the diagram of the pro kabaddi, okay? Pro kabaddi if foreigners watching pro kabaddi, kabaddi is like a game, just like volleyball and other things. It is played by fourteen people, okay? And this is a one of Pune's pro kabaddi stadium. If you are following the pro kabaddi at the moment, you know it is happening in Pune. When it happened in Bangalore, actually I had gone and seen it, okay? So this particular stadium will have a different layouts. Every stadium will have

### 00:23:43 · Speaker 1

different layouts to be practical, correct? Where there'll be different zones and where where the game happens, the direction could be different. So putting other way this entire thing can be totally dynamic. The layout is totally dynamic. Definitely if you take a move cricket booking or a football booking, the stadium will be again in a different fashion, correct? So this particular layout has to be drawn on the screen and whenever you click on a particular section,

### 00:24:07 · Speaker 1

Okay? Let's say I'm selecting two seats.

### 00:24:11 · Speaker 1

And see, there's certain animation that is happening. Whenever you click right, you are seeing that zooming in all those things, okay? Or if you a little zoom out and if you select the general or here also you can go. There are actually categories, okay? Choose band, block A.

### 00:24:28 · Speaker 1

block B, okay?

### 00:24:32 · Speaker 1

all of that that can be done. I don't want to refresh because I have set information on the right hand side, later I'll refresh. Okay? So in very simple words like it is a very dynamic canvas that is drawn on the screen. At least now you might have got the hint how this particular thing is happening. At least now you know how the dynamic stadiums are drawn on the screen, please mention your that answer in the comment section. If not, definitely I'll answer. So basically, this is a canvas. Correct? Whatever you're seeing on the screen currently is a canvas. But and the canvas need lot of

### 00:25:02 · Speaker 1

things to draw it, correct the points, where which color to fill, all of that. And all the information is flowing here from the back end. Okay? As you can see, all the information it is flowing from the back end. Okay? I'm not getting too much deep into it, like what is sending what. So this color represents where. uh You can always go and check that. I don't infer all the things from the their website because it's a half truth, because I want to build this. I can only relate and analyze if this is the way this can this problem can be solved, just as a proof.

### 00:25:32 · Speaker 1

I'm showing you they are also doing the similar way. Okay? Now. Where the entire canvas information is shared from the back end and that information is used in the UI to draw different kind of a sites layout. Okay? Now let me refresh it as I've already shown you. Okay? Let me refresh the page.

### 00:25:50 · Speaker 1

Okay

### 00:25:51 · Speaker 1

So where as you can see now, let's say you select the block B now, you get the zooming effect. Or here also you can go and select the price price range, like uh five hundred rupees the range, three thousand rupees which range, thousand five hundred which range, correct? So this way the this in a big stadium, the drawing of the big stadium can be done on the canvas and how you can select the different kind of a layouts, okay? Now.

### 00:26:17 · Speaker 1

So these are all the main problems that I wanted to cover in this particular video. Okay? Now let us also think about the technology or the framework. So as you know already we have three different three or four different technologies currently much popular on the UI. Angular, React, Vue and the vanilla JavaScript and HTML, correct? So which which technology can be choose? Any of the any of the three can be choose. But I would go with Angular or React because considering the problem, considering the the scale of the website, you may end up having lot of problems whenever you

### 00:26:47 · Speaker 1

building it. Definitely you have a broader community support in either of them. Anything is faster or anything is slower, as you all know it has been proven React or Angular performance oriented in one or the other way. Both have a disadvantages, both have their own advantages, correct? Only considering the community support I'm recommending a React, but if you wish to build an Angular, always you can build, okay? That's all from this video. I hope you enjoy the video and tried I tried keeping it less than thirty minutes as an overall video. And I'll be I would like to do lot of more front end

### 00:27:17 · Speaker 1

system design videos, please mention which system you think is complicated and that is worth designing from end to end in the comment section. I'll try to pick that and do a video in my upcoming sessions. Okay? And in case if you're interested to be a part of my system design videos where I we both will interact and build a system together. I have created a Google form and link is in the description section. Please go and register yourself and in future whenever you are so much interested and the topic that I choose will match both of us, we can pick that. Okay? So in case if you're not already subscribed

### 00:27:47 · Speaker 1

to my channel, please subscribe to my channel, press the bell icon because I'm coming up with lot of lot more system design videos, lot more DSA videos, lot more interview preparation videos. I'll be also interviewing lot more interesting personalities on my channel. So at least for that, please subscribe to my channel, press the bell icon. Thank you so much. Catch you in next video.
