---
id: GYVLp0ekHdM
title: COMPLETE SYSTEM DESIGN OF GOOGLE DOCS [2022 LATEST] - Concurrent editing, Version
  history & More 🔥
date: '2022-10-23'
url: https://www.youtube.com/watch?v=GYVLp0ekHdM
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ #javascript #interview #systemdesign #frontenddeveloper \n\nUncommonGeeks is a\
  \ Youtube channel dedicated to helping candidates clear their interview. There are\
  \ close to 70+ videos and new videos will be uploaded every week. If you're seriously\
  \ preparing for interviews and looking for tips and tricks, please subscribe to\
  \ my channel and press the bell icon.\n\nChapters:\nConcurrent editing : https://youtu.be/GYVLp0ekHdM?t=935\n\
  Version history: https://youtu.be/GYVLp0ekHdM?t=1890\nOffline support: https://youtu.be/GYVLp0ekHdM?t=2497\n\
  \nIf you want to be part of my next video, please register here: https://forms.gle/BiCxXUepjrZDoWJH7\n\
  \nWhat is frontend system design: https://youtu.be/gN8LQTff21g\n\n\U0001F525 How\
  \ Youtube System works ?\U0001F525 Frontend High Level System Design of Youtube\
  \ #youtube #interview: https://youtu.be/QJe0cBjlgog\n\nInterviewPreparation series\
  \ : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/  \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\
  \ \n\nGithub Repository that contains presentation: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/tree/main/Frontend%20System%20Design\n\
  \nJavaScript Custom implementation|polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:50:47
model: saaras:v3
transcript: true
---

# COMPLETE SYSTEM DESIGN OF GOOGLE DOCS [2022 LATEST] - Concurrent editing, Version history & More 🔥

## Transcript

### 00:00:00 · Speaker 1

You don't have to watch this video.

### 00:00:01 · Speaker 1

If you know how more than one people can synchronously edit Google Doc at once. Like there are three people who are all editing on the same document in the same line, how does Google Doc is supporting that? Or how does Google Doc is showing the version history that you edited one year ago? Let's say same document that you edited over one year of time and you want to switch back to last year and Google Doc is showing the data as it is, how the format was there one year back. How does Google Doc is able to do that? Or let's say Google Doc is also supporting a feature called

### 00:00:31 · Speaker 1

offline support. Whenever you are not having internet, you will be able to edit the document and whenever internet is there, the document gets synced and also it will be reflected in all the different devices that you are using, your mobile, tablet, laptop, everywhere. If you already know all these things how they work, please you don't have to watch the video. If not, please watch the video. I'm going to explain step by step how the front end system design will be working with how UI solves all these problems very much in detail in this video.

### 00:01:02 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Vasanth. I hope you all doing well. In case if you are seeing me first time on the internet, I'm a content creator. I help people to clear their interview. I made lot of beautiful series in the past which has been appreciated by many. Link to those series will be somewhere on the screen also in the description section. Please go ahead and watch if you are seriously preparing for the interview. And I think you already watched my previous system design video that was on YouTube and if you in case if you have not watched the link to video will be somewhere on the screen also in description section. And I got lot of love after watching the YouTube system design and

### 00:01:32 · Speaker 1

and I created a poll what should be my next system design video. As you know in the video I mentioned I will be doing a system design of trading stock market websites like Zerodha. But I created a poll in my YouTube channel whether to do with a stock market trading like Zerodha or to do something called a Google Docs. Okay. I got a fifty fifty on both and I personally had little inclination towards the Google Docs because I see it has lot of interesting challenges to solve. So considering all I will be designing Google Docs system design in this video. Everything similar to the last video everything will be

### 00:02:02 · Speaker 1

step by step, nothing superficial, nothing is pre-built, everything I'll be building from the scratch in this video. In case if you're not pressed subscribe to my channel, please subscribe to my channel and press the bell icon because there are a lot more interesting system designs are coming like seat booking websites and the e-commerce e-commerce websites and stock market trading. So many system designs from the front end point of view because there are very few people who have done system design videos on the internet and so far nobody, I can strong I can come for sure say because I searched a lot, nobody has designed Google Docs

### 00:02:32 · Speaker 1

system design on the internet. So I I think I'll be the first one who is designing step by step for free of cost, okay? So at least for that subscribe to my channel and press the bell icon. Without wasting further time let's get started.

### 00:02:45 · Speaker 1

So, I believe you all know how the front end system design works, what are the different segments in the front end system design. If not, please watch this video. It is around fifteen to eighteen minutes where I've clearly explained what all aspects are involved in front end system design and I've explained how each section will go. Please watch the video, it will be beneficial for you because I cannot repeat that in every video. So, I am assuming you watch the video. Let's get started with the first section that is the general requirement. Okay? Let's start before probably we do the general requirement, maybe we can first go through the

### 00:03:15 · Speaker 1

Google Docs once, correct? This also tip I have given in the last video. Whenever you are not sure how the system would work, ask interviewer to show the system or if it is a free system, free as in accessible to everyone, YouTube, Google Docs, anybody can go and check, right? So ask a time for two to three minutes where you go and explore the system, okay? So let us do the same in this video. I have already seen the system multiple times, but Google Doc is not as common as YouTube. So I'm gonna show you once the entire Google Docs how the UI and other things will be, okay? So this is the Google Docs UI.

### 00:03:45 · Speaker 1

everyone who's having a Gmail ID will have Google Docs, Google Excel, etcetera, okay? So here, the first thing is starting a document. You can create a document here, and there are multiple templates. You can choose whatever the template that you want to resume and business letter, cover letter, etcetera. You can choose among the template if you wish, okay? Then, once you come down, you will see all the document that you've already prepared, okay? Come down, there are whatever the document that you've already created, those documents you can see. You can click on any document, for example,

### 00:04:15 · Speaker 1

I'm clicking on the sample document. Okay. So you can come here. Same as your how the word works in Microsoft or pages work in Mac. So Google Docs is just an editor but only thing is it is online. Okay. You can come here. You can edit. You can enter anything. Okay. And you would also have all the different options that a typical editor has but there is also some additional features. Like you have something called share. You can share this document with somebody on the web and more than one people can edit it synchronously.

### 00:04:45 · Speaker 1

have an email option, you can email this file straight away from one Gmail account to another Gmail account or your Gmail account to any other valid email address, okay? Then you have edit options, lot of things, undo, redo, paste. There's different viewing options. You can insert so many things like drawings, clippings, images, tables, charts, all of that. And you can format the text, different ways of formatting. There are tools, extensions. This is very, very important. So, all the things, whatever the extensions are there, they will not be pre-added into the Google Docs. You can

### 00:05:15 · Speaker 1

optionally add because add-ons are not a requirement for everyone. Correct? Then you have help section where it will discuss, um we will discuss about lot of things. Okay? Now, uh so why I'm showing you all this is same way you should look at it because now you have to list the requirements. Correct? So before you list the requirement, you should know how the product is working. Correct? Now you got idea of all the things. Also one other important thing, you have a print option. If you have a printer connected, straight away you can give a print as well. Okay? So roughly I'm going through all and another one very important thing that fascinates me a lot, like I mentioned in my intro. That's a version history.

### 00:05:49 · Speaker 1

So where you can go back and see all the different versions that you edited. This document I just created before this video so I don't have lot of uh edits here. Okay? But if whereas if you look at this one you would see lot of different edits that has happened and whenever you click it will revert back to that particular version that particular day. Okay? Which is very very interesting. I'm going to discuss how this also will be built. Okay? Yeah, another important thing is you can also make your document editable offline so even when internet connectivity is not there if you are editing a document you can continue to edit and once after

### 00:06:19 · Speaker 1

point the internet is back, the same document is already edited, will be sent into server and it gets synchronized across different devices that you're using like mobile, tablets, another browser, etcetera. Okay? So roughly I walked you through the system. Now let us start by listing the requirements. So you can do parallelly with me if you are very much interested or you can look at me how I am doing. Okay? So now basically we have to list the requirements. As you know requirement mainly has two things, functional requirements and non-functional requirements. So functional requirements are those requirements that is something inherently affect the user that are using.

### 00:06:49 · Speaker 1

For example, anything that comes to the functionality, non-functional something which doesn't directly impact the user, but which are very, very important for the performance of the system. Let us look at both now, okay? So,

### 00:07:02 · Speaker 1

requirements. Okay. requirements and functional requirements in that. Okay. functional requirements and we have non-functional

### 00:07:14 · Speaker 1

requirements, okay? Now inside the functional requirement, what did you see for the first? First is the uh search. Search option was there. I don't know how many of you observed, okay? If you go here, the first is the search. I I'm not going to system design the Google search because that is very, very complicated. But search option is there. You can search actually by two things, okay? uh You can search by

### 00:07:36 · Speaker 1

file name. Okay? You can also search by file content. Okay? Next. Next we have

### 00:07:46 · Speaker 1

uh like select template options. There were a lot of templates available, correct? Templates, okay? Then we had um uh the second was the template document and like I always I have also written all the requirements that I think are important on the left hand side. Sometime once in a while I'll watch there that I don't miss out anything while listing, okay? Then we have uh next is the

### 00:08:10 · Speaker 1

document for editing. Okay.

### 00:08:13 · Speaker 1

document editing. So this is a place where you edit the document or you add things into document, delete, basically the entire editorial part of the document. This has a lot of options, correct? Like uh editing. Like editing which involves undo, redo, uh then paste.

### 00:08:33 · Speaker 1

like document paste

### 00:08:37 · Speaker 1

cut. Okay? Then you'll also have other options like coloring, changing font. Okay? Then you also have options like

### 00:08:48 · Speaker 1

where you can format the text. Correct? Format the text, etcetera. There are a lot of things like maybe inserting pictures, chart, okay? So many things can be done. You very well know what all the possibilities, like you can change the color, you can add a margin and a footer, and you can maybe bifurcate the things left hand side and right hand side where you can give the indexes, on click of index you can go to particular thing. So many things can be made with that, okay? I'm just limiting to certain aspects here. next requirement is what? version history which I already said. you already saw that. okay? next is offline support.

### 00:09:27 · Speaker 1

okay? where you can edit a document offline and it still gets synchronized, okay? then we have you might have observed the saving the document.

### 00:09:37 · Speaker 1

The document can be saved in various different formats like you can save a document in PDF, you can save it in doc, you can save it in docx. Okay?

### 00:09:48 · Speaker 1

docx. Then you can also save the document in RTF.

### 00:09:53 · Speaker 1

Okay, rich text format. There are many extensions with which you can export or create a document. This is also not that easy, okay? Where the conversion happens, client or server, if you get time, we'll discuss on that as well, okay? Then, yeah, obviously we can add the comments at the end, okay? You already saw add-ons, okay? Where you can add add-ons on top of this one. uh Lot more we can discuss actually, but maybe switching accounts.

### 00:10:19 · Speaker 1

switching the accounts. file sharing.

### 00:10:23 · Speaker 1

Okay. I mean as you know you can share the Google Doc that you created among your friends so that they among your friends or colleagues so that they can collaborate at the same time. Okay. Basically I'm just limiting myself to this. uh Definitely there are hundreds and probably thousands of very nuanced features that are present in Google Docs. Okay. So this is the functional requirement. Okay. Now let us go to the non-functional side of it. So as you all know non-functional basically means those requirements that doesn't directly impact the user most of the time but very very important as a product. point of view. What is first adaptability, correct?

### 00:10:57 · Speaker 1

So one important tip I'll give is non-functional requirements, most of the non-functional requirements remain as it is for lot of the tools. So if you remember few the non-functional requirement definitely you can fit into all. But functional requirements are not like that. For example, adaptability was one of the thing that was a part of YouTube as well, correct? So whenever I design YouTube system design, I'll I'm adding the same thing here as well. So support for

### 00:11:22 · Speaker 1

mobile and browser, okay? And mobile browser also you can mention tablet. Mobile browser

### 00:11:31 · Speaker 1

and tablet, correct? That is adaptability, accessibility, how you gonna support the disabled people to use it, okay? Different disability you can support in a different way, correct? Localization.

### 00:11:45 · Speaker 1

globalization

### 00:11:48 · Speaker 1

you very well know what what both of them mean. Localization, how you're going to allow users to one is write or type in the local languages like Hindi, Telugu, Kannada, Malayalam. In case of India, every country might have their own different local languages. How they are going to type in that language. Also, how you're going to allow them to weave the entire system in different language. Like file is there, which we are seeing in the English. But whenever you go to Korean or whenever you go to Hindi, that file might change to something else, correct? So as a tool, how you're going to

### 00:12:18 · Speaker 1

support the different language and how you allow editing of the different language document in your tool. That is localization, globalization definitely stands for the international languages. Okay. After this

### 00:12:30 · Speaker 1

definitely the performance, how you make sure it works effectively. Then we also have security. Correct? So because your documents has cannot be viewed by everybody. So it is could contains very confidential information, correct? You have to make sure you give a proper security into it, okay? Architecture, then caching. We are going to talk about caching actually very much, okay? Yeah, definitely another important point, resource optimization.

### 00:12:57 · Speaker 1

Resource

### 00:13:00 · Speaker 1

optimization. Okay? I'm just sticking to this. You can list as many as possible because I want to keep this video a little short because my Google YouTube video, YouTube assistant design went quite a longer time, so I'll keep this video quite short. But still, it may go up to next fifteen, twenty minutes, so just at least have a cup of coffee while watching it, but I am guarantee you, you will not be disappointed until if you watch till the end. You'll learn a lot of different things by the time you complete this video. Okay. So these are the functional requirement and non-functional requirements. Okay?

### 00:13:29 · Speaker 1

Let me zoom out a bit. Okay, I'm making it small. So all this can be viewed in once. Okay. This is a functional requirement and non-functional requirement. Okay. Now, after the functional non-functional requirements, you know, next important aspect is the scoping. Definitely all these things cannot be designed in forty minute interview. So what all things that we are going to pick. Some hints I've already given what I'm going to pick. Definitely I will not disappoint you by picking some simple features, but I'm going to pick some difficult features and I'm going to explain how that can be built. Okay, scoping, next section.

### 00:13:59 · Speaker 1

So in scoping, let us pick very interesting aspects. The first is concurrent editing. Okay? First thing, as you also listened to that in the intro, concurrent editing. Second thing, very, very important thing is version history. Okay?

### 00:14:16 · Speaker 1

Ocean History

### 00:14:19 · Speaker 1

Third very important thing is offline support.

### 00:14:23 · Speaker 1

So these are all functional requirement that I'm scoping. uh Non-functional requirement what I'll do in offline support only I'll cover on one non-functional requirement called caching. Okay? Another non-functional requirement that I'll be covering here is uh is uh architecture. Okay?

### 00:14:39 · Speaker 1

Architecture, which architecture is better?

### 00:14:42 · Speaker 1

architecture. We have three main very common architecture that is monolithic, microfrontend and mono repo. I've already made a detailed video explaining the architecture. The link to video will be somewhere on the screen. Please watch that video if you've not already seen it. Okay? uh architecture mono

### 00:15:01 · Speaker 1

let thick versus

### 00:15:05 · Speaker 1

micro

### 00:15:07 · Speaker 1

front end versus

### 00:15:11 · Speaker 1

mono repo. Okay. mono repo. Anywhere you see a spelling, please forgive me. I'm not that expert. Okay. I think these are all fine. Micro front front end. Okay, sure. So, this is the scoping. So, I'm going to design all of this step by step very much in detail. Okay. And let us start with the first first feature that is the concurrent editing. Okay. So, what do I mean by concurrent editing? Let me close this guy version history. I don't want.

### 00:15:41 · Speaker 1

okay? So concurrent editing basically we mean where more than two people can edit a same document at the same time, correct? This is not that easy problem to solve, okay? Why I'm saying is, let me show you one very interesting thing.

### 00:15:56 · Speaker 1

So, I think you all can see there is something called jigsaw puzzle.

### 00:16:02 · Speaker 1

all of you might have played this puzzle in your childhood, correct? So this jigsaw puzzle means there will be some shapes and you have to add all the shapes and make one image, correct? It is it is easy for smaller kind of a jigsaw puzzles. But here the problem is there are ten people, everybody has access to the same shapes, okay? And finally they have to form this dog by merging. So there are two eyes. So you add this eye section on the left hand side and somebody will pick that and they'll add on the right hand side.

### 00:16:32 · Speaker 1

because let's say it has ten shapes to form one dog, this all the ten shapes can be accessed by all the ten folks. Correct? So now forming this uh dog out of all the ten shapes is very very difficult problem. It is not that easy to solve. Okay? If you're thinking Google Doc concurrent editing is an easy problem, just yeah remove that from your mind. This is extremely complicated problem to allow the concurrent editing. Okay? But I will try to explain in a as easy way as possible. Okay? But before I start solving the problem, let me

### 00:17:02 · Speaker 1

just give you a little information how the Google Cognite editing looks like because somebody might have never done that, correct? So now if you see

### 00:17:11 · Speaker 1

let me just

### 00:17:15 · Speaker 1

show you

### 00:17:18 · Speaker 1

So basically, as you can observe, let me just minimize it a bit. Okay? Yeah, basically I have opened the same document from two of my Google accounts, okay? So one in the incognito mode, one in the non-incognito where I am showing you, okay? So if you see here, this is my email ID, so where you'll see, whenever I click here, on the right hand side you will see like this has been edited by the Uncommon Geeks, okay? But whereas whenever I do here, whenever I take the cursor here, you'll see that anonymous bat, okay? Because

### 00:17:48 · Speaker 1

I've allowed this document to be edited by anyone, so you are seeing like that. Otherwise, if I've given specifically to someone, you'll see their name in there, okay? So now I'll do here what I'll do, problem statement. I'm making it a hat, okay? Here I'm doing.

### 00:18:10 · Speaker 1

as you can see I'm adding hat. As soon as I edit, you see a slight delay but it reflected on the left hand side as well. Okay. Now this hat I'll make it to that and then I'll insert G here. So you can see, uh it has been formally properly getting edited on the both the sides. Okay. Definitely uh I could have shown more realistic with the two people different people because we could have tried removing and adding the same character but since I'm only the one I'm editing so I'm keeping it in the two different uh two different uh for browsers here.

### 00:18:40 · Speaker 1

Okay. So now you got a sense of parallel editing, okay? How what are the how the parallel editing would work. But definitely you might have also understood different problems that exist in the parallel editing, correct? Because same person, two persons can try to edit on the same line and the same character, so how you are gonna solve that problem, okay? Let us discuss the solutions one by one.

### 00:19:00 · Speaker 1

So, first solution that I would propose here is

### 00:19:06 · Speaker 1

taking the text document. Same same way you need to be doing in the interview as well, okay? From solutions.

### 00:19:14 · Speaker 1

for concurrent

### 00:19:16 · Speaker 1

editing problem. Okay? First thing that I would be doing is locking. Okay? So what I'll do, I'll lock the file. Okay? Once the file is locked, traditional way of doing it, I'll lock the file and until a person done edit, I'll kind of I'll slice the time period among all the editors. So for example, I'll give you three, two people are there, I'll give one second for him. So after he completes one second editing, I'll lock him his file. He cannot edit anymore. Then this person, he can whatever this person entered,

### 00:19:46 · Speaker 1

I'll take that and show for the second person. Basically, synchronize the document and the second person, now one second is given to him, he can edit anything. After one second I lock him, then I'll unlock him. Basically, at any given point in time, two people cannot edit, okay? But still it is quite real time by locking and unlocking it. But this is a pessimistic kind of an editing, correct? This is not optimistic. The purpose Google Docs why they have introduced the concurrent editing is they this is something officially I gathered from the Google developer.

### 00:20:16 · Speaker 1

particularly says is Google Docs should be is nothing but a conversation that happens in a coffee shop. Correct? Where two person if you're talking to your friend you will not be like sitting like this. Wait for him to finish his conversation then you add. Whenever they're talking in the middle only you'll cut and you'll you'll add your thoughts and they'll add their thoughts. Similar flow they wanted in the Google Docs. Correct? So locking cannot be done. Second approach is what?

### 00:20:39 · Speaker 1

very very many many might not have heard but there is a very optimal technique that is called operational transformation.

### 00:20:48 · Speaker 1

operational transformation. There is a third technique that is called differential synchronization. Okay.

### 00:20:57 · Speaker 1

referential synchronization. So two popular techniques for parallel editing. So both operational transformation, I think even differential synchronization, both are done by the Google developers itself. Second, I'm very sure, third, I'm not that sure. I'll try to add in a description who built it. But these are the very popular algorithms that are used for the parallel editing. Okay? I mean the synchronous concurrent editing from the different users on the same file. Okay? Now let us see about the second one, operational transformation, which is officially used by Google Okay

### 00:21:30 · Speaker 1

by Google Docs. But in an interview if you're not sure of which which Google is Google Doc is using, feel free to say this is one approach that can be used for concurrent editing, okay? Then probably we can discuss how actually it works, okay? To save your time what I have done, I have already drawn an image because as you know I just draw on the real time and it may not look very beautiful. So I have used this image, I have already created this image for you, okay? Now let us see how the operational transformation works, similar way you need to also do explain in the interview, okay? So you have picked operation transformation into your hands, please explain what is operational transformation and I am doing the same.

### 00:22:05 · Speaker 1

So basically there are two person Alice and Bob. I don't know why very very common these two names are used. I'm also trying to use the same name. So basically this is the initial state between the two documents. Okay? Both are having their copy as H L O H L O. Okay? So this is just the no edit has happened. Both people refresh the page. This is how they are seeing it at the moment. Then what he is doing, Alice is doing, Alice is adding E at position one, insert E at position one and what he is doing

### 00:22:35 · Speaker 1

Bob is doing is O one and O two okay. What Bob is doing is insert exclamation at the position four. That is the last position for him after O. Correct? So O one and O two here represent the local operations. Okay? I mean operation that is happening locally. Next. So hello H L L O is becoming H E L L O. Correct? Because you added E in between zeroth and the first character. You added exclamation this would look like this. Now. We have a two different copies of data. Correct? So though you saw three steps

### 00:23:05 · Speaker 1

is basically both entered only one one character each, correct? Next, this has to be synchronized between two systems, system one and system two, correct? What they are doing, let's say if I just say insert E at one, correct? So, one second.

### 00:23:20 · Speaker 1

So if you would say insert E at one and insert exclamation at four for this at four is zero one two three four. Now it is hello here correct? If you simply insert exclamation at fourth position what will happen zero one two three and four after L L you will get the four. Correct? If I if I just write. So right now we have H E L L. Maybe I'll just type only okay?

### 00:23:48 · Speaker 1

just so that you all get it clear. So right now, the user one has hello, correct? If you but here the user two has inserted exclamation at fourth. Don't get confused, this is not that easy to understand. Just stay with me for five minutes, I'll make sure you'll understand it very very much in depth, okay? I'll also repeat this entire thing once again. So basically, O two want to insert an exclamation at the fourth position, correct? Zero, one, two, three and four. So that is right now in the four you have you are having the O.

### 00:24:18 · Speaker 1

correct? uh sorry, zero one two zero one two three four. correct? So you are having O in the fourth position. If you insert straight away as a as the other person has edited, the document would look like this. correct? On the other hand, if the other user who is having

### 00:24:38 · Speaker 1

who is having

### 00:24:39 · Speaker 1

H L L O and exclamation. If he adds E on the first position, it would look like this. Hello followed by an exclamation here, hell exclamation and O, correct? So how this will happen if as it is if you're trying to insert a particular characters at a different places, this is how it would happen, correct? So this is not the right technique, correct? So definitely this cannot be done in simple words, correct? So this cannot be done, like you cannot whatever the operation happening

### 00:25:09 · Speaker 1

left hand side if you do the operation on the right hand side definitely the do both documents will not be in sync. Correct? So there has to be optimal technique which will overcome these barriers and create a better performance. Correct? So that is happening by the algorithm called operational transformation. Okay? So here if you see client apply transformation function T received operation T T of received operation comma local operation to receive the changes from the other clients. Okay? Very simple don't get too much into this formula. I

### 00:25:39 · Speaker 1

I know the formula very well but I will not explain too much because this video becomes very difficult for you to get along, okay? Just see like what is happening insert exclamation at five, insert E at one. So basically what it does is it will analyze the operations on both the sides and the operation transformation algorithm will identify the right character in the right place, okay? How operation transformation does this is it is very complicated to explain, not that I don't know, but this operation transformation algorithm is something proprietary by Google. You can you can get certain

### 00:26:09 · Speaker 1

gist of it by reading their white papers, but how they do is not completely explained anywhere. So for the explanation purpose, you can understand that whatever the different positions that are there,

### 00:26:19 · Speaker 1

that cannot be done as it is in the new document. Google operational transformation algorithm will help you to identify the right position in different documents and insert, delete and update the values. Okay? This how the operational transformation will work, but if you are curious to know how exactly it works, please mention that in the comment section. I'll try to make a separate video just explain the operational transformation as a technique. Okay? So if you are someone who is liking my system design content and would like to take a part in this series, then I've created a Google form in the description.

### 00:26:42 · Speaker 0

So

### 00:26:49 · Speaker 1

section, please go and register there. So you can come to my video where I'll be explaining certain techniques and you can ask me question like Vasanth why you are picking this, why can't we do that or I can ask you some questions, what is your suggestion. So we can make it more interactive. Just with if you are fundamentally strong with whether JavaScript, React, Vue, Angular, anything, you can just fill that fill out this form. I'll pick some whoever are more inclined towards the system design in my upcoming videos and I'll give you an opportunity to be part of my channel. So now you understood how the concurrent editing would work. Locking

### 00:27:19 · Speaker 1

cannot be done. Right technique for using uh doing the um concurrent editing is the operational transformation algorithm. Okay? What is the third one? Differential synchronization. This is something that is getting popular in recent days. So differential synchronization is basically same way how the Git would work. Git difference will work, right? So where two people are there and you'll merge the things whenever by checking the diff of the different people, that is how the differential synchronization work. So if you ask me whether operational transformation versus the differential synchronization, anything can be used. Both are actually

### 00:27:49 · Speaker 1

optimal techniques itself and both have their own trade-offs. So anything can be used. If you ask me since I know Google Doc is using operational transformation, I'll go with it. Now, next important question here is, let's say we have one document. Ten people are editing the same document. Now tell me what should be the means of connection between the client and server? What is the right way to connect between the client and server?

### 00:28:11 · Speaker 1

I'll list few options for you, okay? So, one second. Client server interaction. Client server interaction.

### 00:28:22 · Speaker 1

interaction techniques. What is a what all the techniques that we can use? One is sockets.

### 00:28:28 · Speaker 1

Okay. Second one is the server sent events. Okay.

### 00:28:34 · Speaker 1

where you will expect the server to send certain events. The third thing is socket, server send event, third thing is the polling, okay? I mean I've explained pretty much this in my last video also, I'll quickly give a gist of what each means. So basically sockets are nothing but an independent collection and exclusive connection that exists between the client and the server, okay? So it's a two way. Server can send something to client, client can send something to server, that's the sockets. Another one is server send events where server will send certain events and accordingly the client will act. Like this is the new

### 00:28:37 · Speaker 0

the

### 00:29:04 · Speaker 1

document baba you have to add it and the client will update the document and add the document. That is how server sentiments work. Third thing is the polling. Polling means client periodically fetches values from server and updates it. Okay? Polling again has a short polling and long polling where short polling means you call the server immediately server should send the response to you. Long polling means the server will wait for a particular duration of time and if see if anything has changed in that course of a time and combine all the things and send. So this is much efficient in some scenarios compared to the short polling.

### 00:29:34 · Speaker 1

Now, which one do you think is efficient for the Google Docs? I'll answer that. In case if you already know, mention that in the comment section. This is the technique that is used for in in case of Google Doc. And definitely I'll I'll check it and clarify whether whatever you guessed was right or not. But answering my question, answering that question, Google Doc, if I am designing the Google Doc, definitely I'll go with the sockets. The reason being it's a two way connection. It is not one way connection. Like whenever you edit certain things, it should go to the server and whenever server receives certain edits

### 00:30:04 · Speaker 1

some other user that should also come to you. So it's a two way connection. So sockets are best utilized here. Okay, socket is the right approach. Okay.

### 00:30:14 · Speaker 1

So last video I have given you example on which on Google live commenting I've said polling can be used. For Google dogs, sockets can be used. Okay, I'll send I'll explain where server sent events can be used in my upcoming videos. Okay. Now this is about the solving the first problem. Now the second problem that we wanted to solve was the version history. I will I assume you all saw the version history whenever I showed you in the first beginning of this video. Okay. So now let's start with the second problem of version history. Okay.

### 00:30:45 · Speaker 1

Wash

### 00:30:48 · Speaker 1

So but before I starting about the version history, my only request is, uh to make a video like this will take immense effort, okay? You won't get right information available everywhere. You sometimes I have to read a lot, watch the videos and even for the Google Docs I even posted in my LinkedIn to get some information from some some resource persons. I did not get much, but I am trying hard to make a content like this. So if you can you can appreciate me by just by liking and commenting about the video how you are feeling. So in middle of the video only if you do, it will be visible for a lot of people and

### 00:31:18 · Speaker 1

I will be able to achieve my goal of reaching to a lot of people very early. Okay? So please like the video and comment whatever you felt so far and if you're not subscribed, please subscribe to my channel and press the bell icon. Okay? Now let's start.

### 00:31:31 · Speaker 1

version history. Okay?

### 00:31:33 · Speaker 1

Let us start with the version history. So version history has a like I already shown you if you go here, I'm quickly showing you again. Version history, see version history. You can click back to any date and you will start seeing the difference what all been added in that particular date, okay? So if I expand probably September if I go, you will see what all things has been added on that particular day and you always have an option to restore to this version, okay? Vasant, why you are highlighting this this problem so much? Is it that difficult to solve?

### 00:32:04 · Speaker 1

you only think, okay? Let's say you are keeping one document, okay? to maintain your expenses, how much you are spending on each month. And the document is as old as two years, okay? Now, let's say today is when I'm recording this video is October fifteenth, and whenever you decide to go back and check, let's say you click on a particular date, and in in that particular date, let's say last year fifteenth, and you are seeing the version of the document last year fifteenth. So how do you think server is maintaining so many versions?

### 00:32:34 · Speaker 1

What are the what are the different options? It is not an easy problem to solve. Okay, let us explore the options what among are possible. Okay. First, first easiest technique is multi store multiple copies.

### 00:32:48 · Speaker 1

Okay. Second is Merkle tree.

### 00:32:52 · Speaker 1

So first easy solution is you store as many copies as possible, as many copies as required on your server. Whenever you switch to a date, you load the document. Very easy, correct? So basically you don't do you don't have a lot of problem because you pass the date as an argument, you get the document, you load the document, very straightforward, correct? That's on the storing multiple copies. But you very well know the disadvantage. Let's say today is October fifteenth, on October fourteenth I might have just added hello to a document which is of hundred page, only one word.

### 00:33:22 · Speaker 1

is added. Just for the one word, would you like to store another copy of the entire document? This is possible maybe whenever user base is very less. Let's say you're just hundred user, fifty user and you have efficient, you have enormous amount of the storage, then probably you can use it. If not, system like Google definitely cannot use the version in the store multiple copies, correct? So what they use, I really don't know. But what can be used and most efficient technique, one of the most efficient technique is the Merkle tree, okay? Don't worry like Vasanth, I don't know, I am UI developer, I don't

### 00:33:52 · Speaker 1

about tree, don't worry. Whatever you have learnt in the basics in the engineering, same thing I'm gonna explain here as well, okay?

### 00:33:59 · Speaker 1

So basically, uh I have already drawn a simple tree for you, okay? Now let us go and check the Google document, one sample document I showed you, right?

### 00:34:09 · Speaker 1

So where I've created four lines here, one, two, three and four. So let's see now how Merkle tree works, okay? So Merkle tree is one of the very very popular tree algorithm and it is used across lot of different systems and one beautiful use case of Merkle tree is for the Google Docs or any Docs version history, okay? What happens I'll tell you. So I'm showing you simple document of one, two, three, four, okay? There are four lines, four characters, this I'm taking for the easy explanation purpose, okay? So where now for each

### 00:34:39 · Speaker 1

given document, whenever a document is given, what Merkle tree algorithm does is, divide that into equal character chunk, okay? In this case, you can try to divide it on a equal character means one O N E one, three characters in one chunk, okay? Then two, inside the three you can make T H R as one chunk, E E F in another chunk, O U R in another chunk, okay? So like that you can form the chunk or for the easy understanding sake if you if you if you take it, let's say each line is one chunk, okay?

### 00:35:09 · Speaker 1

each line is divided into one chunk, okay? Then what we do is we'll calculate a hash for that particular chunk. Hash is what? Basically you you take that string as an input and you transform it and generate some particular hash, like you'll generate some value out of it, okay? Like for example, one represent one, like you did some computation internally and represent one, two and three and four. Basically how anything can be used. There are a lot of popular hashing algorithms you can check on the web. Some hashing you use and you will reduce them you will reduce that particular given string into some some value okay that is called the hashing

### 00:35:46 · Speaker 1

So now if I go back here, so what I'll do is now I will I have the hash here, correct? So where here I have one, here I have two, here I have three, here I have four. Then what I'll do, from one and two, one and two I have, this one and two again I'll pass to hashing algorithm to get another hash value that is one two. Three and four, I'll get another hash three four. Then I have final hash as one two three four. I'll pass one two and three four to the same hashing algorithm, then I'll get

### 00:36:16 · Speaker 1

one two three four. Okay, definitely this will be connected. Let me see quickly, can I draw? Yeah. I'm drawing it.

### 00:36:24 · Speaker 1

So this is a typical binary tree example, okay? So should it be always a binary tree? Not necessarily. You can decide to not to go with binary tree. You can have more number of leaf node at each each level, okay? So binary tree basically has two nodes. You can opt to go for a more number of nodes as well, okay? So this is a simple representation of the entire our entire document, okay?

### 00:36:48 · Speaker 1

So, now what happens is, let's say after a point, now I'm switching back to particular version. Let's say this is October fourteenth, okay?

### 00:36:56 · Speaker 1

October

### 00:36:59 · Speaker 1

October fourteenth. Okay? October fourteenth. Let me select the entire thing. Okay?

### 00:37:07 · Speaker 1

So October fourteenth and I'm making another version for October fifteenth, okay? So let's say you I was in the yesterday's version and I'm switching to today's version. In today's version what has happened is, so we had one, two, three, four, right? What I have made here is four is good. So basically I have changed the last character, last line some characters, correct? So four become to four is good. Definitely the hash will change, correct? It will not be just four now because hash is purely dependent on the values.

### 00:37:37 · Speaker 1

that you're passing into it. Let's say now four becomes five. See these are all I'm giving you for the easy understanding. They will not be like this. They will be in some terms of some hashed value, some x, y, z, question mark, etcetera. Okay? So I'm I'm making it five. So what will happen is in October fifth hash

### 00:37:53 · Speaker 1

This is fifth, this is five.

### 00:37:56 · Speaker 1

So definitely this will also become five. This will also become one two three five. Okay? So now October fifth document is like this, October fourteenth document is like this, okay? Let compare this with a very very big document. Let's say we you have a document of four pages or forty pages where every ten page, simply I'm give an example, every ten page basically constitutes of this one child node, okay? And now you we you have to get to take a difference, correct?

### 00:38:26 · Speaker 1

So what has happened is in the last node, correct? We have we have been the changed. Now what we are doing here is we will compare this parent node one two three four and one two three five, correct? Very very simple. Now what I'll do, I got to know hash is not matching.

### 00:38:42 · Speaker 1

Okay, I'll explain this once again if if anybody of you getting confused. So I'm on October fourteenth and this is how my Merkle tree look like. And I click on on next next day in the version history that is October fifteenth and this is how my fifteenth fifteenth Merkle tree look like, okay? See still now I have not update the thing on the UI, remember this, okay? I've called the API, I have got the new Merkle tree. Now what I'll do locally, I'll compare the two Merkle trees. So it was one two three four and it is one two three five. Now I

### 00:39:12 · Speaker 1

know that the document has been updated. So whatever the document that existed on October fourteenth is no longer the same in October fifteenth. So now what I'll do, I need to identify where the document has changed. So now I got to know one two three four and one two three five. So document has changed. I'll go to the next leaf node that is twelve and twelve.

### 00:39:30 · Speaker 1

remains as it is so I'm not gonna check anything on the down of the twelve it could be thousand notes but I'm not gonna check because I'm sure left side part is right now I'll go on the right hand side thirty four and thirty five yes so right hand side there is a change after that again I'm gonna check

### 00:39:46 · Speaker 1

three comma five. Where it has changed, the fifth node has changed. Now what I will do is, I will call an API just to get the fifth node. Okay? So you get obviously all these will have some hash value, unique ID, etcetera. So you will get just the fifth node and you get the document and update it in your file. You will replace four with the five.

### 00:40:08 · Speaker 1

Got my point? So now because of this your API calls have reduced. The storage on the server has reduced so server can just store this entire merkle tree, most updated merkle trees for each day or in a day different edits it can keep storing just the merkle trees and you can get the diff and you can get whatever you want. Correct? It is so easy to maintain the version with this approach. Okay? Now one one important thing you need to notice here is whatever the hash that you calculate that should not be more than the

### 00:40:38 · Speaker 1

character itself. Hope you're getting what I'm saying. Let's say for one, if your hash points to one two three four five, basically you are trying to store more values than the text itself, then you can store the text also, correct? So you shouldn't be storing your hashing algorithm should be efficient enough to give less number of characters than what you already have. That is number one.

### 00:40:58 · Speaker 1

And the second most important point is if you make the nodes, if you make each node out of less number of characters, then the tree becomes very big. Correct? Because if you make it more number of characters per each each node, then the tree becomes smaller, but the problem here is you may get very often edits and you have to make more network call. So you have to find a right balance between number of characters and the each chunk size. Okay? So this is how the version history problem can be solved with the help of the mock call tree. Okay? Now,

### 00:41:28 · Speaker 1

Let's go to the last problem. Again, before I solve the last problem, my humble request, if you're liking the content I'm making, please like and comment about the video and subscribe to Uncommon Geeks. Okay? Now, let's solve the last problem that I said I'll be solving. That is the offline support.

### 00:41:42 · Speaker 0

Okay

### 00:41:43 · Speaker 1

Let's start with offline support.

### 00:41:45 · Speaker 0

Okay

### 00:41:46 · Speaker 1

offline support. So Google Doc as I very well said if you disconnect internet and edit for a while Google Doc stores the data locally and whenever internet is back it will update the document into the server. Correct? So how you can do the offline support? Definitely only one way is that offline support that is store documents locally. Correct?

### 00:42:07 · Speaker 1

store documents

### 00:42:11 · Speaker 1

store documents

### 00:42:14 · Speaker 0

locally

### 00:42:15 · Speaker 1

So how you're gonna store the document locally? This is very very important problem. Why? Because you cannot take all the text and save it in your document, correct? No matter whatever the index DB you are using or watermiller DB you are using, any DB for that matter if you are using, you cannot take the text and store as it is. Why wasn't we can do it? The problem here is every text has a metadata. For example, if you see in my document, let's say I make it bold. Okay? Now the bolded character has to be stored and somewhere there has to be reference that this character is bold, correct?

### 00:42:45 · Speaker 1

And again, you can colorize it, you can insert table, etcetera, correct? But just for the explanation purpose, I'm not making it very complicated. If you want to know the answer, mention that in comment section, I'll explain. But just for the this particular example, let us say the document is very plain document, okay? Just one, two, three, four, how you saw that document, okay? After you enter five, six and seven, eight, the internet is gone.

### 00:43:07 · Speaker 1

What happens is, just before I explain the offline support, let us see how the online support will work. Like whenever the internet connectivity is there, and whenever you are typing, what will happen is, let's say you have a hundred line file, correct? And you added the one not one line and some character. So what do you think? Will Google Doc send the one not one lines into the server or the entire document into the server? Definitely no, correct? Google Doc will be sending only the changes, whatever the changes that you did to the server with help of the operational transformation technique.

### 00:43:37 · Speaker 1

which I already explained. So new changes sent to server. The document is actually formed on the server by taking these changes. Okay? So multiple people can be doing the same thing. Only the changes will be sent chunk by chunk. So will the Google send every character when you type? It could be or it will send on a particular time basis like every one second send all the changes that might also be happening with help of sockets. Okay? So now you sent all the data into server chunk by chunk whenever you are doing even the online support. Now you got to know how I will be solve this problem. Even the offline support as well

### 00:44:09 · Speaker 1

I will be, you know how much portion is already there on the server, correct? How much portion is not there on the server? What you will be doing is, you will take all the data, whatever is, whenever you get to know internet connectivity is gone. You will store all the data locally, okay? You'll store all the data locally and whenever the internet connectivity is back, you will fetch that data or as you already know there are a lot of observers to check whether internet connectivity is there or not. You will get the data, break it into chunks, upload it to server, same way how the operation transformation

### 00:44:39 · Speaker 1

would work. Okay? But here only one important thing is you in during the whenever you did not have the internet, others might had internet and the document might have been updated, correct? Again the problem is solved in a very simple way with the help of the operational transformation itself. Like you are whatever the change you did will go to the server. What changes are already done, they're also present and operation transformation will decide the order of inserting and the order of deletion and it will form a complete document and update the client again what all need to be updated, okay? So the local

### 00:45:09 · Speaker 1

offline support is simply handled with the help of the chunking approach and with the help of the operational transformation. Okay?

### 00:45:16 · Speaker 1

So these are the three main problems that I wanted to solve and I explained you very well how to solve each of these problem. Any particular problem you want more explanation please mention that in the comment section. I'll be more than happy to make a video or elaborate further. Now, one important point that we missed before I started with the design was, so like I always say this this can be done prior or after design or before the design. That is the technology. Okay?

### 00:45:43 · Speaker 1

So what technology do you use for solving this problem? Technology here I mean framework.

### 00:45:49 · Speaker 1

technology slash the framework, okay? Why I'm asking this question is very very important and will be asked in the interview and you must be able to uh answer this. Like whether you go with angular.

### 00:46:01 · Speaker 1

or react or view

### 00:46:06 · Speaker 1

or vanilla JS and HTML. So basically you can uh choose any of these techniques but you should be able to justify why you are using. Uh so in uh I have already explained this in my last video also there are two kind of a problems one is a project need another one is a organizational need. So organization might have a developers of specific skill sets in such cases you have to maybe compromise little bit on the technology. Okay let's say we are full of React developer team though Angular has certain advantages though I propose there may

### 00:46:36 · Speaker 1

not be I may not get a chance to work on angle because we don't have any angular developers. Correct? But that should not be the first priority but that is an organization dependency. Technological dependency was which which tech is good? I I suggest I prefer we can go with angular. Okay? If you if you are an angular developer you can go with angular. If you are a react developer you can go with react also. Either of the have advantages as you very well know react is used

### 00:46:58 · Speaker 1

in most used web applications like Netflix. So there is no problem that React would face in the scaling. And Angular as well, it's a framework built by Google and though Google may not directly using Angular, but definitely some aspects of Angular, but already present in different Google products, it can also scale to very high user base and it is already proven as Google is using it across different products. So you can either go with Angular and the React, there shouldn't be any problem. Can you go with a view? As you already know, the penetration of view is quite less.

### 00:47:28 · Speaker 1

after a point if you end up in some problem you may not get lot of material considering the scale of Google Docs. Like where millions of people are using it on a day to day basis. If you get into problem you may not have a lot of support for that. So I'm just on that note I would not be going with UJS. Can I use Vanilla JS and HTML? No, I will not be doing that because frameworks give lot of capability and I'll be able to build the product much quickly if I use the frameworks. So I'll not be going with a Vanilla JS or HTML. Angular or React anything that you pick considering the user base of Google Docs they'll be good enough. Okay?

### 00:48:01 · Speaker 1

I think these are all the points that I wanted to cover. Caching also I already covered. Google uses actually index DB for the caching purpose in in the in their website, okay? So whenever you're editing, a real version of it will be maintained in the cache with the help of the index DB, okay? Now, architecture, last point and very important point which I want to cover, which architecture does suits for Google Docs? So monolithic, microfrontend and the mono repo, okay? If you don't know any of these three, like I mentioned, the link will be on the screen also in description section. You can go ahead and watch the videos. So,

### 00:48:31 · Speaker 1

inserting the scale of the Google if I am a part of Google and building this product obviously I'll go with a mono repo because I very well know Google uses mono repo because Google will be coming up with lot of innovative algorithms to optimize whatever they are building correct so if I go with mono repo all the different innovation that are part of the entire Google repository can I can achieve it I can also utilize it correct so I would be going with mono repo let's say but if I am given only the Google doc to design and it's separate product it is not a part of Google it is some X docs

### 00:49:01 · Speaker 1

In such scenarios, I would be going with a micro front end. Reason being I get a lot of flexibility in building it. I can divide the different task among different teams and take their bundles and form into one document. Such scenario I'll be going with a micro front end. Like if I have a freedom of just building Google Docs, considering ecosystem of Google, I'll be going with a mono repo. Monolithic I'll not be going in either of the cases. Okay? If you think you'll go with some other architecture, please mention that in the comment section and mention why. Okay?

### 00:49:27 · Speaker 1

I think these are all the things that I wanted to explain in this video. Thank you so much for watching. And if you're not subscribed to my channel, please subscribe and like and comment about the video. Whatever the things that I discussed in the video, the requirements, the images, all of that I'll be adding into my GitHub repository. You can go and refer. And you yourself can pick some more complicated features from this and try to design on your own. Add in a comment section if you're facing any difficulty, I'll definitely try to help you, okay? And for if you if you have not followed me on LinkedIn, please follow me on LinkedIn. Some question that you cannot

### 00:49:57 · Speaker 1

asking comments, YouTube comments, you can always ping me on LinkedIn, I'll try to answer. And in follow me on medium, I'll write at least one article every week which will help you to clear your interview. And all these things will be available in my GitHub repository, download and start my GitHub repository. Thank you so much for watching. Catch you in next video.

### 00:50:14 · Speaker 1

If you are someone who is liking my system design content and would like to take a part in this series, then I've created a Google form in the description section. Please go and register there. So you can come to my video where I'll be explaining certain techniques and you can ask me questions like, Vasant, why are you picking this? Why can't we do that? Or I can ask you some questions, what is your suggestion? So we can make it more interactive. Just with if you are fundamentally strong with whether JavaScript, React, Vue, Angular, anything, you can just fill that fill out this form. I'll pick some whoever are more inclined towards the system design in my upcoming video. videos and I'll give you an opportunity to be part of my channel.
