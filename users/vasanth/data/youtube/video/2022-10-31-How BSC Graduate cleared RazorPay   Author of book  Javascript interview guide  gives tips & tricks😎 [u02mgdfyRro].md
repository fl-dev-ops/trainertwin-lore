---
id: u02mgdfyRro
title: "How BSC Graduate cleared RazorPay | Author of book \"Javascript interview\
  \ guide\" gives tips & tricks\U0001F60E"
url: https://www.youtube.com/watch?v=u02mgdfyRro
date: '2022-10-31'
duration: 00:33:44
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# How BSC Graduate cleared RazorPay | Author of book "Javascript interview guide" gives tips & tricks😎


## Transcript

### 00:00:00 · Speaker 1

All of you have watched ratings right it feels really bad when friends fail but it really feels worse when he comes first that's the human nature so uh we cannot avoid that right if someone just parallel to you with the same experience same degree is going for a higher package you will feel low so see when i was looking for the job right for the raise the pay i interviewed six months back for a company so uh i could name it but let's let's not so uh i interviewed for

### 00:00:30 · Speaker 1

and after the interview right I realized that I'm nowhere standing in the league so suppose if I have to compete with someone who's passing from IIT who has done very well in a product based organization and now they are looking for a team and then there's me who has come from a BSc background I'm from a service based company and I have to go to raise a pay same I think

### 00:00:49 · Speaker 2

I think when I started my career question my brother had given the same advice where basically I'm from not so popular college tier two tier three college and I did not start my career with very big firms so my brother said the same thing which you mentioned it is there is no race going on like you are not competing with someone just of your whatever who has started they may be in Amazon or very big firms but consider the journey of probably eight to ten years if you really have a potential you can go anywhere hello welcome back to uncommon geeks myself asant i hope you all doing well in case if you're saying

### 00:01:19 · Speaker 2

me first time on 19th i'm a content creator i help people to clear their interview i made a lot of beautiful series in the past which has been appreciated by many link to those series will be somewhere on the screen also in the description section in case if you're someone who's seriously preparing for an interview please go and check out those videos and coming to this video video this one one of a kind i can tell because in this video i'll be interviewing a very very interesting personality his name is prashant he works at razor pay but he is very special because he's somebody who's writing about the front-end interview preparation since almost three to four years

### 00:01:49 · Speaker 2

years and in just one one to one and a half months he's gonna come up with a unique book that contains the question and answers which contains a lot of very interesting questions and not just the questions it also contains a lot of system design training on how to clear front-end developer interview i'm very very excited to talk to prashant let's get started

### 00:02:09 · Speaker 2

Prashant thank you so much for accepting my invite and coming live on Uncommon Geeks welcome to my channel

### 00:02:17 · Speaker 1

Thank you sir I'm glad I'm here

### 00:02:19 · Speaker 2

So uh, Prashant, I've already given your introduction in my own words, but it'll be good if you introduce yourself so that audience can relate more. So yourself, the place you are from, your skills, etc.

### 00:02:31 · Speaker 1

Yeah, so I'm currently based out in Mumbai. I'm working for Reddypay as a senior front-end engineer. I'm handling the token exchange. So I'm working in the token exchange pod and majorly dealing with the payments.

### 00:02:46 · Speaker 1

That's on the professional front on the personal front I write my blog so I run a blog named lensbucket.com where I'll write about the JavaScript interview process and all those things

### 00:02:58 · Speaker 2

Yes yes which place you are from Prashant

### 00:03:02 · Speaker 1

Uh I'm currently based out in Mumbai so I'm born and brought up in Mumbai

### 00:03:06 · Speaker 2

Oh you're from Mumbai and you are living in Mumbai correct

### 00:03:09 · Speaker 1

Yes

### 00:03:10 · Speaker 2

Nice, nice Prashant. Yeah, let's definitely we are going to talk more about the learner bucket thing. Yeah. So let me start with my first and this very simple question, Prashant. Okay. So there are a lot of like mid and junior level engineers who are very, very good at the web designing. This is I'm seeing myself when I was in one year and two year experience where I could build something. Let's say you want to ask me to build a form or a UI, et cetera. But I wasn't sure like what are the right materials to prepare for the interview, like where to go for the interview or how to prepare. So can you just guide us, Prashant?

### 00:03:40 · Speaker 2

what should be the starting point let's say you have one 1.5 year experience and looking for a change what should be the front-end developer interview preparation strategy

### 00:03:50 · Speaker 1

Yeah, definitely. So, see, the interview process for the front end has changed somehow in the last few years. So, currently the trend is like when you are going for a front end interview in a good product based companies, not talking about the big force, but the good product based startups based out in India or anywhere else. So, they have recently started with this trend that they are not asking the typical DSA question for the front end interviewers. So, the typical round for a front end interview or

### 00:04:20 · Speaker 1

content developer looks like the first round goes for the code JavaScript the second round goes as a machine coding then based on your experience the third round is like the system design or your past experience or you will be asked to create a small component a small application your understanding of things your knowledge of the browser the ecosystem all those and the final is the VP round or the managerial cultural code whatever you call that

### 00:04:44 · Speaker 1

So that's how the current trend is in the market. And for those, the best preparation guide I can tell you is one, if you have, if you are less experienced with the core JavaScript, right, the vanilla JavaScript itself, you should get familiar with that. And second thing, you should be more aware about the ecosystem in which the JavaScript runs, that is your browser.

### 00:04:44 · Speaker 2

Get it get it

### 00:05:08 · Speaker 1

because javascript is a language and it is executed in the browser or through the v8 engine or any javascript engine and then like the node.js itself uses the v8 to create the runtime and if you are using a desktop application or a native application so their code also runs through v8 or any other javascript engine and then it's converted to the support so having good understanding of core javascript browser fundamentals really helps apart from

### 00:05:08 · Speaker 2

Exactly

### 00:05:38 · Speaker 1

In this your core web architecture your web knowledge that also helps so the protocols HTTP works HTTP works all those things also help

### 00:05:49 · Speaker 2

Sure, sure question. I also give one simple advice whenever candidate ask this question, I just say first go for the developer.mozilla.org and pick some random topic. Probably you yourself will find out. So many different topics that will be suggested, like where you get to know where you are standing. That it sure question. So second point is not on the pure and leave on the front end, but more on the philosophical level as well. Are a lot of candidates relate to this question. So it's been tremendous push in the market, whether I don't know whether it's really required or not to join Mang and a lot.

### 00:06:19 · Speaker 2

premium companies somehow i i have talked a lot of service company engineers somehow they feel very low being a part of service company uh i personally worked for a service company and i do i did not feel back then because we were building more products probably than what product companies build okay and because of this huge push many feel very low when they are not able to clear these interviews uh like my friend has cleared and i have not cleared and i maybe i'm unfit etc so what is your advice prashant because i know you write a lot on the linkedin about interview preparation etc

### 00:06:49 · Speaker 2

What is your take on this particular topic?

### 00:06:53 · Speaker 1

It's a human nature right if you are competing so all of you have watched radius right it feels really bad when friends fail but it really feels worse when he comes first that's the human nature so we cannot avoid that right if someone just parallel to you with the same experience same degree is going for a higher package you will feel low and that's very common you know you should not worry about that that's a good feeling and that's the feeling that pushes you to work harder and actually

### 00:07:23 · Speaker 1

things right you dream about so it's a good thing it's not a bad thing second thing regarding the premium companies the service base the product base see every company is good in their expect exactly okay if if you are struggling to get a job and if a service based company is giving you opportunity to come to them learn things start working then that's a good thing right so if you are struggling you can get started with a service based company gain your knowledge learn things build things and then move to

### 00:07:53 · Speaker 1

good product based companies exactly so that's how the margin is there that's how many people have moved to the product based companies right exactly and then there are many who get opportunity in their first chance only to land a good job so everyone has their own path it's not something has to be worry about exactly and you can always always go higher okay so give yourself some time it's not like it's a it's not a race exactly everyone says that right if you ask

### 00:08:23 · Speaker 1

experienced employee will always say that it's a marathon. So give yourself some time, prepare very well. There is a lot of resources available currently. You don't have to go for the paid one. There are many free resources. Utilize it very well. And then you can definitely crack a product based company with a good pay. Not necessarily man, but there are many other product based companies in India which pay very, very good.

### 00:08:42 · Speaker 2

That's me

### 00:08:46 · Speaker 2

exactly definitely yes yes same i think when i started my career question my brother had given the same advice where basically i'm from not so popular college two three college and i did not start my career with very big firms so my brother said the same thing which you mentioned it is there is no race going on like you're not competing with someone just of your whatever who has started they may be in amazon or very big firms but consider the journey of probably eight to ten years if you really have a potential you can go anywhere whether you're somebody's from iit somebody's from iam or

### 00:09:16 · Speaker 2

are from Tiruchirappalli college if you make yourself to go the sky is the limit but if in case if you are not only willing then nobody can help you maybe land up wherever you are right

### 00:09:27 · Speaker 1

that's a really good advice and i also to add on that right see i myself i am from a bsc background i don't even have a technical degree a direct engineering degree exactly so uh and many of my colleagues whom i have worked till now in different you know organizations they themselves have their own path their own journey to reach where they are currently exactly so it's a good thing yeah and you should always cherish that i mean it's not right i'm not groomed in a typical way that you have to follow java c plus plus you know

### 00:09:57 · Speaker 1

you follow this part to get this job exactly because i did bsc i was open to opportunities i myself figure out what will be the best for me what will be suitable for me and then i'm going with that

### 00:10:10 · Speaker 2

Exactly. Definitely. Definitely. Prashant. So now this is again, I have a lot of my viewers are freshers, like who are in their pre-final year and the final year. And many ask me very often that wasn't I want to become the front-end developer? And I'm just in my pre-final year, seventh and eighth. Some message me also in second and third year, then my advice, first finish your engineering or whatever the degree you're doing. But whenever people approach me on the final year, like I want to become front-end developer and how to get started with that. Okay. I answer in a different way. I'm just

### 00:10:40 · Speaker 2

want to hear your thoughts so whoever in the final year so what are your thoughts what is the right way for them to become front-end developer

### 00:10:48 · Speaker 1

See, if you are genuinely willing to come to tech, right, if you have want to become a software engineer, not just to crack an interview and get a high-paying job, right, it's not the process. It's not the final destination. You should be willing to become a software engineer. And that journey is completely different from what all the YouTubers or all the different companies are showcasing today.

### 00:11:09 · Speaker 2

Exactly

### 00:11:10 · Speaker 1

If you are in the final year, if you aspire to become a web developer, right? So it's very simple. Get started with the free code camp. They have a very sweet and straightforward roadmap design. You will learn things step by step. After that, you will get idea about what is the web development. Once you finish the curriculum of the free code camp, you will get idea what is web development. After that, you can search for those things, particular things, like you can search for how to get good at HTML, how to get good at CSS.

### 00:11:40 · Speaker 1

Core JavaScript and then learn any framework. Yes. The core JavaScript is the most important part. Once you are strong with the base, you can learn any framework in no time.

### 00:11:49 · Speaker 1

okay that's how your focus should be apart from that the web is very large yeah when people say that right writing html css or simple javascript logic it's not like that exactly for example i'll just give you example see when someone create a product in india right if suppose amazon or is creating a website in india they are creating that website which should be available to the user in bombay or tier one cities which should be available to the people in landak also which are in you know

### 00:11:49 · Speaker 2

Got it.

### 00:12:19 · Speaker 1

where the network is not so strong exactly they are thinking so vast in such a perspective in such a domain and then building stuff so that's how vast the web is right now so you think like that you get you started you get good at javascript and then explore things slowly and slowly and it's not a race like you won't end up in your 20s that a 20 is your end you're just getting started you're just getting started it's a 40 year journey in your career

### 00:12:48 · Speaker 2

Exactly. Yes. Yes. I just second with you, whatever you said, like people, at least the most backend developers are intact as an opinion, just HTML and CSS web. Now, I recently I made one YouTube system design video where I was talking about live commenting, how live commenting works when thousands or lakhs of comments gather in about a half an hour or 30, 35 minutes. It's extremely complicated to solve. It is not just the styling or HTML and CSS. You need to be really good programmer to achieve that. So like you mentioned, have a strong fundamental knowledge on JavaScript, which will act as a

### 00:13:18 · Speaker 2

foundation for your career correct yes next thing you already touch based on this but i want a little uh more thoughts on your own saying so many material are right now available it is not just for the front end for all the other students for that matter where the courses are available for free on youtube youtube and many other social media where the content is available for free whereas there are many other paid courses where people are pushing hard for you to join it's not like you want to join but people are pushing very hard on you they'll say you have to pay less we'll convert

### 00:13:48 · Speaker 2

to EMI etc where they're I mean they want people to join there so what is give or take Prashant whether to go with a free education that is freely available or go with a paid and structured courses

### 00:14:02 · Speaker 1

So that right it's quite straightforward see if we are capable of self learning if we are disciplined if you are you know consistent you think that I can learn myself then you should go for the free resources if you are from a non-tech background if you are you know you don't have any about idea about the tech but you are willing to go into the tech then it's better to go with the offline and the paid courses as they will groom you according to the corporate the tech the ID and then they will give you

### 00:14:32 · Speaker 1

the right path they will monitor you properly they will help you with the interview all the basics so that's how you should do it and also yeah definitely if if you have you know so go for the courses that where you can do the uh what we say the salary share or the payment share so after completing the course when you get the job then you pay from your salary so that's a better chance for you to get a job through them

### 00:14:56 · Speaker 2

Exactly, exactly. Prashant, so what you say is totally makes sense because there is no one rule that applies for all, correct? Like you said, self-learning is not possible for everyone because there will not be, there sometimes there will be the first generation who has finished their engineering or BSc. There won't be anyone to guide them or they might have studied in some colleges where their seniors are also not so in a high position. Such cases, good to go with the paid courses or where somebody can guide you who already in the industry, but you already know a lot of things, how the system works, industry works, then the self-learning will

### 00:15:26 · Speaker 2

better correct so now another very common question question that i i often get is now somebody fresh or they're just of pre-final year or they're just starting their career six months experience on the framework like whether to go with the angular react view there are many frameworks like that correct so what is your take person which framework is good considering from a career point of view not a job point of view

### 00:15:48 · Speaker 1

all the frameworks are great there is no comparison only a rookie developer does the comparison right there is no comparison between the frameworks all are catered for a use case okay so there was few things that jquery could not solve that's how angular react was born right there were few things that react was bad at so view was born so then there was few things that view and react was bad at which is the virtual dom so the thread was born so that's how things are right if there is any kbr if there is any

### 00:16:18 · Speaker 1

pawns in certain frameworks people look for that opportunity grab that improve it and launch a new thing exactly now there is no particular framework but see the framework comes from the community the community support matters a lot so if you are a fresher if you are looking for a job in the i.t industry so the best thing is choose the framework that is widely adopted by the community and it is widely popular so that you will have a greater chance of getting the job which is in the current scope is the react

### 00:16:48 · Speaker 1

Got it

### 00:16:51 · Speaker 2

If you are a job specific, then probably you can learn React because there are many openings. But like again, it all goes is be a stronger JavaScript. So no matter what framework comes in future, you'll be able to adapt to it. Correct. So yeah, next question is quite specific to you, Prashant. Like as you also introduced, you work in Zepay right now. But whenever you're preparing for Zepay, probably you might have prepared for other companies also. So what is your typical interview preparation strategy, Prashant? Let's say you decide now this is the time I'll change the job. How you start preparing yourself?

### 00:17:21 · Speaker 2

extremely sorry to disturb you in middle we are going to continue our discussion with prashant and lot more interesting aspects will be discussed okay and going forward but in case if you like the video please like the video and add a comment whatever you felt so far before watching further the only reason is it takes extreme effort to get somebody like prashant on the chat and share the knowledge to you all and also by liking and commenting and subscribing to my channel pressing the like icon i'll be able to reach my goal of helping and to clear the interview as early as possible so i please

### 00:17:51 · Speaker 2

worse please uh if you're not subscribed to my channel subscribe and press the bell icon like and comment about the video before watching further

### 00:17:57 · Speaker 1

So see when I was looking for the job right for the raise the pay I interviewed six months back for a company so I could name it but let's not so I interviewed for it and after the interviews right I realized that I'm nowhere standing in the league so suppose if I have to compete with someone who is passing from IIT who has done very well in a product based organization and now they are looking for a change and then there's me who has come from a BSc background I'm from a service based company and I have to go to raise the pay so

### 00:18:27 · Speaker 1

I have to compete with them so I have to prepare really well so after the first interview I realized where I'm lacking so from there I started to learn things I designed a six-month roadmap for myself and I stick with that the first thing I did was I got very good at the core javascript so I read eloquent javascript first after that I did javascript 30 to solve all the I created 30 projects in ruby javascript after that I created 30 projects in react then i

### 00:18:57 · Speaker 1

the comparison where was react better why we use react where was vanilla javascript lagging where vanilla javascript was good so all those comparison when i had in my mind it was easy for me to saw you know give answer for the system design questions like why i'm using this why this particular framework all those things and then there was a book so which i highly recommend to everyone which is a professional javascript for web developers okay this book teaches you the end-to-end working of javascript so it

### 00:19:27 · Speaker 1

So it's in so detail, like which is it's mentioned in the book that the garbage collection works differently in the Mozilla JavaScript engine and in the V8 engine. So it's in so detail. So that book really helped me a lot to understand the language at the core. And apart from that, I did lots of problem solving on different, you know, not the DSC related, but the core JavaScript related. So I did lots of code wars kata, which helped me to, you know, develop. And also the first interview which I had filled in, which I had given.

### 00:19:57 · Speaker 1

So I also realized like what types of questions are being asked currently in the product that's why that helps me to prepare better

### 00:20:04 · Speaker 2

Great, great question. See, very rarely we see them strategize like you, where they definitely everyone realize after one interview where we stand in the market, but very few will prepare a roadmap like you. Why I'm saying this specifically is people whoever feel like they are not getting into particular company, et cetera. So there is a lot of hard work that goes in. Maybe very few get in by lucky or some reference, but most people will put in a lot of hard work to get in there, wherever they are. Correct? So, Prashant, the book that you mentioned, is it like free?

### 00:20:34 · Speaker 2

Available or it's a paired book

### 00:20:36 · Speaker 1

No it's it's a paid book I think the third edition is freely available I'm not sure but there is available on O'Reilly

### 00:20:44 · Speaker 2

Sure, I'll read that. At least for our audience, I'll link that in the description, whether paid or free, whatever it is, so that they can also read it. Okay. Yes, sure. So now, this has been your preparation strategy, Prashant, for whenever you are appearing. Now, let us talk a little bit about the resume as you're working there. What was the interview rounds? And what was the mode that you applied? Did you apply at resume or they called you? How was it, the process?

### 00:21:10 · Speaker 1

See, it was very hard for me to get my resume shortly shared, right? Because I did not have those keywords mentioned in my resume. I'm not from a big, you know, big college. I don't hold that degree. I don't have that experience. So I have read one book regarding the resume, which has really helped me a lot. I don't remember the name. I think it's one-on-one Google resume.

### 00:21:19 · Speaker 2

So

### 00:21:34 · Speaker 1

which i mentioned like how you should create your resume so after reading that i've created different versions of my resume like if i'm applying for back end role i've created a new version of resume for that for full stack different for the front end different and i've particularly mentioned the keywords the keywords that helps me to bypass the ets which is the application tracking system so that was my first strategy after that the interview rounds at resume was very straightforward the first was code javascript second was machine coding then third was

### 00:22:04 · Speaker 1

system design and after that the cultural and recipe for recipe i think someone has approached me for the recipe interview i had not applied over there but before that i have interviewed for multiple organizations so i have interviewed for amazon germany i had interviewed for uh i think cure.feed all those big product question things

### 00:22:26 · Speaker 2

Yes, yes. In fact, I have read that Amazon's experience of you at Germany. I fed up of reading how many rounds that happened 3A, 3B, 2A. Correct, sir.

### 00:22:35 · Speaker 1

So the Amazon asked the leadership questions and that was very very direct

### 00:22:40 · Speaker 2

Yes, for those of you who have not read that blog, I'll be linking that in the description. You also can go and check. Okay. Yes. So, yeah, yeah, Prashant, yeah, almost we are coming too close to the end. So I'll just highlight little more about the work and other things. So how do you feel? Because it's a reservation company for a lot. because as far i i might be wrong as far i know it's india's biggest payment gateway and even sites like is it says biggy relay on uh zepi i mean you don't have to tell that is whatever i have read okay so so many transactions might happen

### 00:23:10 · Speaker 2

a second it is something a dream of every developer to work for such organizations so how do you feel Prashant working for that kind of an organization

### 00:23:20 · Speaker 1

I feel really privileged recipe is some kind it's a kind of organization right that really brings out the engineering out of it so it's it's a organization that works as a scale I don't work on the whole product of the recipe I work in a different team but when I started right we get started on the project in very less time we did multiple PUCs we helped to onboard banks all those things were happening and it's such an organization right my manager approached me like if you like to do the back end development

### 00:23:50 · Speaker 1

and you are open to that so i am also doing the spring boot currently in the recipe so it's really grateful of them that they have given the opportunity they have given the options to us that if you want to explore a different front right you are open to do that so that's how the recipe is it works really well

### 00:24:08 · Speaker 2

Wonderful. Yes, yes. So this is what I'm previously was talking to developer with this only we're discussing fine whatever the one or whoever is just starting the career, they think it is about money, the service product, et cetera. Finally, it's a good atmosphere and how many people you are able to impact. That is what true engineering is. All right. Definitely money is something catalyst with everybody needs it, but that is not something that should inspire you to work. Inspiration should come from your values. Like you're building something great, et cetera. All right. It's it's great, great to know that question.

### 00:24:38 · Speaker 1

It's it's for me see it's all about ambition and work so great works is what gets me going money keeps me living so that's how I decide things

### 00:24:46 · Speaker 2

Definitely, definitely. So Prashant, since you talked a little bit about the Java, you did little work on the Java Spring Hibernate as well. So this is one of the common question that I get and I have particular viewpoint. So where so much push again to become full stack developer now? Okay. Definitely this trend was not so common in past few years and now it is becoming very, very trending. At least experience level, I do get to a level. Even freshers are becoming too much obsessed to becoming full stack developer. What is your take, Prashant, on one stack front end or back end?

### 00:25:16 · Speaker 2

or the full stack

### 00:25:19 · Speaker 1

See the term itself is very vague very subjective right see when you say full stack what do you mean by full stack if he is able to do the front end or back end development so if you are talking about front end front end of what web mobile desktop back end of what right so if he is able to do the deployment or not if he is able to handle the community stuff it's a very subjective term and it's very badly presented in the market there is no role as a full stack developer in the IT industry there is only

### 00:25:49 · Speaker 1

one role and that is software engineering and the software engineer is someone who uses language framework as a tool to solve problems exactly that's what I think personally so that's how I keep moving if you ask me to solve a problem right and we'll decide the tool to solve that problem if there is something I have to write the API about I'll choose a framework let's say Spring Boot I'll create a microservice in that I'll expose that microservice it will be consumed by the content so that's how we think there is a problem we use it

### 00:26:19 · Speaker 1

to solve it

### 00:26:20 · Speaker 2

Exactly, exactly. So you are kind of if somebody has a requirement to become whether one stack, two stack, whatever, let's say even they got an opportunity to learn DevOps, it is there whenever there is an opportunity. If you are interested to explore, please go and explore. But not because somebody forces you to become an engineer.

### 00:26:37 · Speaker 1

No, no, so it's always your preference. Don't go because it's hot topic in the market. Go because you are lacking it, okay? So that way you will be more interested in learning things and you will do much better with it.

### 00:26:50 · Speaker 2

because you have a requirement and you learn it now now what's happening the reverse you're learning it and you're looking for a requirement that's not the right way correct yes

### 00:26:59 · Speaker 1

Yeah that's not it's bad

### 00:27:01 · Speaker 2

Exactly. So, Prashant, let us talk a little more about your website and the brand new book that you are launching, because that is one of the posts that inspired me a lot. Because there are very few books which are kind of written for the interview preparation of the front-end developers. You can talk about both, Prashant. I think my audience will be really loud to hear and it will benefit them.

### 00:27:20 · Speaker 1

Now, back in 2019, right, when the full lockdown started, I was really kind of bored. So I decided to create a blog. Not a blog, because the video recording was very hard for me and everyone was at home during the lockdown. So I started with the blog where I can, you know, write about things, I can document them and then share them. And also, if required, I can look back to them for solutions. So there was very less resource regarding the print and the current trend that was happening.

### 00:27:50 · Speaker 1

market interview questions dsa all those things so that's how i started the blog i consistently write there for last three years four years i'm still writing over there and in the past four years uh through the web right i have gathered lots of different questions the interview questions questions that are really being asked in the interviews not the dry run or the brave teaser types like you know 0.1 to 0.2 yd 0.03 yeah those types of question it's a real interview questions so i have written

### 00:28:20 · Speaker 1

around 70 questions to 20 to 30 pages I have written till now in the book so that's how I'm planning to document that in the form of a book and then ship that also there is very few research as you mentioned very few research for the front end in the market there are many for the back end systems and everything so I thought it's better that I document and you know it will really help someone to practice

### 00:28:44 · Speaker 2

Correct, correct. So what is the means of presentation when you're planning to wrong launch? Is it like a hard copy, soft copy? Anything you decided as such presentation?

### 00:28:51 · Speaker 1

So it won't be a hard copy because for the hard copy I have to find a publisher, a publisher, distribute it. So it will definitely be a soft copy and I'm trying to launch that in the first week of December. So I'm working really hard for that.

### 00:29:04 · Speaker 2

Got it. So if my audience, if they want to get the access to the book, so it's best way to get is from your website.

### 00:29:10 · Speaker 1

All right yeah so I'll post the link over there so once it will launch you can add that in the blog yeah that will have access to that

### 00:29:19 · Speaker 2

great great pressure so good because like i mentioned very few are taking the sketch kind of initiative and writing a book comes with immense work because i i also write on medium from one one and a half year i'm writing so it is easy to make a 10 minute video uh if you are like if you're not camera shy it's easy to make a video because it's more like an acting i as i always say you can prepare comes and you can keep some references here and there and you can talk but extremely difficult right because you have to make them understand by what by reading it so when they you will have the freedom of expression

### 00:29:49 · Speaker 2

all the things whenever we are making a video but book is quite difficult to get it explained so you are doing great job Prashant that you are I mean it's

### 00:29:56 · Speaker 1

It's it's

### 00:29:57 · Speaker 2

inspire others, correct? So like whatever I see, the at least last two to three years back, there was not so much push for the front end, like at least from the interim preparation and all those things. It was just considered a subset overall. But now there is a lot of demand, like people, even because a lot of people are getting placed into big firms. And whenever you are in a privilege, you should make sure you get back, give back to the community that everyone get it and clear well, correct? Yes, yes, yes. Yes, Prashant. So yeah, we are pretty much at the end.

### 00:30:27 · Speaker 2

So it was great talking to you but I have one last question which I typically ask for everyone who I interview so you know like currently the market is really downtrending a lot of people are being laid off and or even people who are in the company they're not getting good projects okay everyone processes through this phase and you are one of the right person to answer because you have seen the struggles before joining the this organization so what is your advice whenever people are feeling low in such kind of situations what should be their mindset and how to face such situations

### 00:30:37 · Speaker 1

Well I'll be

### 00:30:59 · Speaker 1

See, I'm not an expert, but I can tell you one thing. It's, it's, see, there was a time when there was, you know, a quote like survival of the fittest. Right now, it's the survival of the skilled. So the more skilled you are, the better chance for you to survive in the corporate. So if you have time, right, if you are not on a good project, if you are on a bench, if you have some time, utilize that time to learn something new. Get yourself upskilled and get yourself up to ready to the new skill, to the new technology that is being

### 00:31:29 · Speaker 1

ask in the corporate world so that you can get the job you can have your job running if you have one otherwise you can't get a job

### 00:31:36 · Speaker 2

Got it. So don't don't think like whether you're in bench or worst case you are fired. Don't rush to join something new. Practice well and spend utilize this time basically to upskill yourself so that you can land in good. That's what you are referring. Correct.

### 00:31:50 · Speaker 1

Yeah, it's hard to, you know, it's easy to say that and to be done because when you are on a job, you are fired, that's a very bad feeling. But I would still recommend it's not, you know, even if you are getting fired, if you are getting a job in that domain, that's perfectly fine. If you are struggling, then yeah, definitely upskill yourself.

### 00:32:09 · Speaker 2

Sure, sure, Prashant. So it was nice conversation with you, Prashant. We are already close to 35 minutes now. And like I mentioned, very, very rarely we get an opportunity to talk to someone who writes very actively on LinkedIn and the interview preparation. Like I am one such kind and I've seen very few actually actively doing that on LinkedIn. Some start and they expect some immediate return and they'll stop. And especially you writing a blog for such a long time requires a lot of perseverance. Everybody cannot do. There are many with the knowledge, but everyone cannot share that so consistently. So I purely appreciate your effort, Prashant.

### 00:32:39 · Speaker 2

Thank you so much for coming and talking sharing your knowledge

### 00:32:41 · Speaker 1

Thank you thank you Vasant for having me

### 00:32:43 · Speaker 2

okay nice talking it was a great session and talking to prashant and i'm very very excited to read his book which will be published in in the december and i'm one of the vivid reader i often read his blogs and his linkedin post very frequently he writes and i have personally got a lot of benefit by following him on the linkedin and i would be linking his linkedin profile somewhere on the description please go ahead and follow him read his articles and read his uh read his book that is upcoming in the december i will guarantee definitely that will help you to clear your interview and in case

### 00:33:13 · Speaker 2

If you're not already subscribed to my channel, please subscribe to Uncommon Leaks because there are a lot more interesting personalities coming in the channel who share their thoughts regarding the interview preparation and overall front-end persona. So subscribe to my channel and if you're not pressed the bell icon, please press the bell icon and like the video if you're liking it and comment whatever you felt so far. And do not forget to share the video with your friends because there are a lot of things that is spoken about the interview that might help lot of candidates who are out there. So please share the video too with your friends and thank you so much for signing.

### 00:33:43 · Speaker 2

See you in the next video

