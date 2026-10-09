---
id: I2MC31oyBNs
title: 'An Introduction to SAP Supply Chain Modules: A Podcast with a Supply Chain
  Expert'
url: https://www.youtube.com/watch?v=I2MC31oyBNs
date: '2025-06-04'
duration: 00:46:39
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# An Introduction to SAP Supply Chain Modules: A Podcast with a Supply Chain Expert


## Transcript

### 00:00:00 · Speaker 1

The latest version that people will hear about and probably come across is going to be what's called the SAP HANA S4 HANA platform and that is the more the latest edition. There's additional one which is called SAP IDES so IDES is Internet Demonstration and Evaluation System but you can download a system which you can install on your own computer and that one I believe is for free and it comes with some amount of company data so it's stuff it's an implementation that has data that you can play around with

### 00:00:30 · Speaker 1

So if a business is trying to take on SAP, I would honestly recommend businesses make that choice saying, okay, I want to change the way I do things today. Because if you're not trying to do that, maybe you're better off not taking SAP because you will customize it so much that you will lose value in it. And if you're looking at the overall supply chain, I would say have an understanding of demand forecasting, statistical models, how does it work, how does SNOP work, inventory management concepts, production plan,

### 00:01:00 · Speaker 1

MRP capacity planning the logistics network you know distribution centers how what kind of transportation modes and then the the aspects related to I would say order management and warehouse operations as pick-up shipping I'll give you an example where we try to use AI so the startup that I'm with we are currently developing a solution using drones that fly around autonomously in a warehouse take pictures and then there's an AI at the back end that converts those pictures into

### 00:01:30 · Speaker 1

is the item how many cartons what location now that is a pretty simple ai because it's just inferring information from looking at a picture saying it's trying to read the barcode it's counting the number of cartons stacked on a pallet and then figuring out based on the stacking pattern how many cartons sitting behind that picture right and the the interesting thing is to try and not just learn what you're doing yourself today but to understand how this what you do connects with others around you

### 00:01:56 · Speaker 1

Now that is also an important thing when it comes to going back to SAP. People tend to go and focus on one module only. So they'll do MM only, but if you don't understand how MM affects the picking and packing and dispatch operation or how MM will affect the finance side of things, you will not benefit from this.

### 00:02:18 · Speaker 2

Hello and welcome to another very exciting podcast on my channel because today we will talk about a very common question I get from a lot of you, which is how to supply chain professionals upskill themselves on SAP tools. And to talk about that, I've got someone who is probably one of the best people to talk about it. He is a very seasoned supply chain professional and leader who has worked in the consumer goods industry, in the healthcare industry, has worked as a consultant and

### 00:02:48 · Speaker 2

Apparently he is working with a startup so without further ado I would like to welcome Arsalan Sheikh to this podcast hello Arsalan how are you

### 00:02:56 · Speaker 1

Good thanks Shami, thank you for having me

### 00:02:59 · Speaker 2

So, Arslan, before we get into the actual nuts and bolts of this podcast, which is about the SAP tools, why don't you give the audience a little bit of a quick introduction about yourself and your career journey?

### 00:03:11 · Speaker 1

Sure. Okay, that's hopefully not gonna be too long. I, by background, I'm a chemical engineer. I started my career way back in 1996 with Procter & Gamble. And it was an odd one. So I was not a supply chain person. I got hired in a role which evolved me into a supply chain person. So supply chain is not a planned event. It kind of happened. But I look back at it with a lot of pride and a lot of learning. So

### 00:03:41 · Speaker 1

I started my career with Procter & Gamble in the production floor, on the production floor and worked in production, then moved to maintenance and reliability, process reliability, which people now refer to more as OEE, managed those programs, then got moved into engineering and health and safety, so managed capital projects, health and safety programs, then moved into QA, quality assurance, quality control, packaging and product development. So I spent about six and a half years with Procter, then moved to

### 00:04:11 · Speaker 1

Benkisa. With Wreck-it I moved into more I would call the front-end supply chain roles. So I was head of planning logistics with Wreck-it for about three years. And in that I was managing all levels of planning. So demand planning, production planning and scheduling, materials planning, customs clearance, warehousing, transportation. So did that role, then got posted with Wreck-it to another site. So I got posted to South Africa, did that role there for about almost two years. And then

### 00:04:41 · Speaker 1

Interestingly enough got a role with a hospital in Saudi so moved across to Saudi in a hospital environment that was a bit of a shocker uh didn't quite expect that to happen I guess but uh and then that was the start of about almost 11 years in a health in the healthcare environment so then I worked in hospitals in medical equipment companies commissioning hospitals then into medical device manufacturing one of my last roles was chief operating officer it was end-to-end

### 00:05:11 · Speaker 1

uh obviously covering all the different aspects of supply chain and operations and then moved to uae uh with a hospital group uh did that for about two years then interestingly enough started a consulting role uh with my own outfit uh did that for about six odd years and in that time mostly was doing work in saudi uh and most of the customers that are clients that i were getting were more in the food sector so did that for about six six odd years and then moved to

### 00:05:41 · Speaker 1

Canada in January 2025 with a startup where we're developing currently a solution using drones and AI for automating the process of inventory counting.

### 00:05:52 · Speaker 2

Excellent. That's a fantastic career journey, Arslan. And I know this podcast is about SAP, but maybe if you've got time, I would love to also ask you a few questions about your experience of moving from consumer to healthcare and then from healthcare to becoming a consultant and then from the world of consultancy evolving into the cool stuff that you're doing with AI and drones. But before I get there, let's just talk a little bit about SAP. So I mean, I've made several videos about this, Arslan, but just

### 00:06:22 · Speaker 2

you know for the sake of educating our young supply chain professionals they hear all these different terms like you know flying around sap apollo ibp so educate us a little bit about what are the different modules in sap because it's basically an erp but then what are the key tools one should know and have awareness about from a supply chain standpoint

### 00:06:44 · Speaker 1

Okay, so SAP has evolved, I guess, over the years. So SAP, the latest version that people will hear about and probably come across is going to be what's called the SAP HANA, S4 HANA platform. And that is the more the latest edition. You still will find people probably running a slightly older model of SAP. It's called ECC. And between these two, I would say you probably find both of these

### 00:07:14 · Speaker 1

floating about. Customers that are not wanting to migrate are still sticking on the old platform. A lot of the customers have moved on to the new platform. The modules pretty much remain the same in terms of nomenclature. So typically supply chain guys will come across modules called MM, which is materials management, which is all the procurement activities, the goods receiving, goods issuing, inventory management. The main thing over there is that the inventory is is like a black box. You know,

### 00:07:44 · Speaker 1

how much is there, but you don't know where it is inside the warehouse. Then that evolves into the next level or layer that was that's called in warehouse management, which then starts getting into locations and storage locations and stock movements and picking strategies. And then they have the more advanced version, which I would call the best of breed warehouse management solution. It's called EWM, extended warehouse management, which is, I would say, a proper WMS. Okay. So that's more from the material side of it. There's SD.

### 00:08:14 · Speaker 1

or sales and distribution module, which is very so sometimes customer service functions, if you have it within the supply chain side will be working on the SD module. Sometimes you'll find sales teams are actually working on the SD module and supply chain is not involved. But typically that's where the sales orders are put in, the order to cash process is completely run and shipping is also happening from there. Beyond that, if you go to the manufacturing side, there's production planning or PP module. Here is where

### 00:08:44 · Speaker 1

you're managing the the the activities of production on the floor so issuing production orders uh looking at the managing the bills of materials uh doing some basic level of demand planning but most people don't use that functionality in that because it's not it doesn't have a lot of uh algorithms there it's it's very basic

### 00:09:07 · Speaker 1

And one thing that I forgot to mention is the layer of what people will be aware of called MRP. So MRP fundamentally is part of the MM module, but there's some functionality as a part of PP as well. So especially when you want to look at inventory as days of cover, that functionality I understand comes from PP.

### 00:09:24 · Speaker 1

And this kind of covers the core of the ERP side of it. Now, SAP has additional modules around the ERP. And here is where you'll have terms like APO come about. So APO was a solution that SAP put together as a standalone solution outside of the ERP. And that did a lot of the, I would say, the more focused demand planning capability, the detailed scheduling when it comes to production planning, what they have in the core SAP module does not get in.

### 00:09:54 · Speaker 1

to detailed scheduling. It used to be an APO, but what has happened is APO, I understand, is being phased out. And some of the functionality of APO has kind of been moved into S4 HANA, and some of it has been moved into IBP. And I understand that is evolution that is continuing. So what you will find probably over the next few years is APO will probably get closed. And I think the phase out date is 2027. And by that time, whatever was there in APO would be either part of S4 HANA or part of

### 00:10:24 · Speaker 1

IVP

### 00:10:26 · Speaker 1

And IBP as a layer is quite evolved. So it has demand planning, quite strong functionality. It has inventory optimization. So when you want to define safety stock parameters or levels in a single location or a multi-echelon inventory location setup, then it has SNOP. It has a control tower, which does both the collaboration outside of IBP. So within the network,

### 00:10:56 · Speaker 1

network collaborating with your suppliers and and your transportation providers uh doing analytics layers it has pre-built kpis for uh score model if people are aware of score and uh and it has collaboration capability as well within the whole system um and the last part which i would say is a lot more of the optimization capability is a layer called supply and response

### 00:11:21 · Speaker 1

MRP, people are aware, is basically unconstrained planning. It assumes you don't really have a problem with capacity. It assumes you don't really have a problem with lead time. So it does a mathematical calculation. But the reality is that capacity is a constraint. Machine is a constraint, right? People are a constraint. Material availability is a constraint. The number of vehicles you have is a constraint. So here is where they also have the capability to do optimization, looking at constraints, as well as

### 00:11:51 · Speaker 1

handling when your demand is exceeding your supply. So in that case, typically what you'd end up doing is allocating products to customers or prioritizing certain customers over the others. So those kind of capabilities are all there in IBP. So IBP, I would say, is really a kind of a layer which does a lot more intelligent planning, whereas the core ERP does mathematical planning. And there's a distinct difference between the two.

### 00:12:21 · Speaker 1

And I would say the last module I would probably mention is SAP Ariba, which is a procure platform, procurement platform. It covers end-to-end with the beauty of external collaboration.

### 00:12:33 · Speaker 1

So those I would say are the key modules, supply chain resources or plans or folks need to know of. I guess just to be aware of that these things exist out there. And

### 00:12:47 · Speaker 1

sap is continually evolving i will probably talk about a little bit more in terms of other functionality that they're coming up with in the future

### 00:12:54 · Speaker 2

Just a question, I mean, and I've always been curious about this, R. Sivanathan, based on your experience on working with these things, right? Ariba and ABP, how well do they perform if your entire ecosystem is SAP-oriented? So let's say you have got ECC or S4HANA at the back end and these tools are used for planning and procurement. Or if you're using a completely different ERP and you're still using the SAP suite. So what differences have you experienced?

### 00:13:25 · Speaker 1

So if you are sitting on SAP core platform, the connectivity with the SAP products is obviously going to be easier. It's like Microsoft, right? If you're within the Microsoft platform or ecosystem, it's easier to kind of move data around. So I would say implementation wise, IBP and Ariba, SAP IBP and Ariba would be easier if you have SAP as your core ERP. They do work with other ERP systems as well. So functionality wise, they will still perform the same function.

### 00:13:55 · Speaker 1

But there will be specific data translation requirements, integration requirements, which would be different. But functionality-wise, they can work. I don't expect, I don't believe that there is a problem there.

### 00:14:07 · Speaker 2

Excellent. Great. And just because, you know, most of my audience and the content I create is about like skill building and all of that, right? So anyone who is trying to upskill themselves on, let's say, something like IBP, which is the bread and butter of supply chain, what kind of resources are available based on your experience? I mean, one of the common answers I give when I get this question is that work for a company which is using this because that's probably the easiest way to get trained.

### 00:14:37 · Speaker 2

But are there any other opportunities or avenues for people to get themselves upskilled?

### 00:14:44 · Speaker 1

Okay, so for, as you said, I mean, the ideal one is you get a job in a company that is running SAP. But if that's not the case, then there are few ways to get the exposure to SAP prior. The one thing that I've seen a lot more in Canada is universities or colleges that have their own alliances with SAP and they offer access to SAP systems and some levels of training on that. So I'm aware of examples like George Brown,

### 00:15:14 · Speaker 1

I have met with a couple of students from there that have talked about training that they got in SAP while at the university or college. Beyond that, there are kind of two, three different areas. So SAP itself has certain content that it is making available for free. Mostly, I would say the most extensive one is SAP Learning Hub. It is probably the most expensive of all the options. You pay a substantial amount of money, could be a few thousand dollars to get access to the training as well.

### 00:15:44 · Speaker 1

is the live system or a sandbox system environment to play around with uh there's an additional one which is called sap ides so ids is internet demonstration and evaluation system uh as you can so there are two versions of this i've seen and again i have not personally used them but you can download a system which you can install on your own computer and that one i believe is for free and it comes with some amount of company data so it's stuff it's an implementation that

### 00:16:14 · Speaker 1

has data that you can play around with uh you also find companies that are offering offering this as a solution for people to log in but obviously they charge for it uh it could range from anywhere to from 50 to like 100 per month and again if you buy bundles like three months or six months it gets cheaper a couple of examples is there's one company called sapidesandbox.com uh there's another one called professorsoft.com you can check both of them out there are examples that are

### 00:16:44 · Speaker 1

aware of but it's not something I've personally used them. SAP also offers some kind of trial system access but again these are usually very short durations an hour a day maximum.

### 00:16:58 · Speaker 1

There are training providers that I've come across that are mostly out of India that I've seen that are offering online trainings. And as a part of the training solution, they also offer sometimes access to an environment. So those are the typical ways you'll get it if you're not working. Now, if you're working, you can actually get access in the company. If your company has implementation that is going to happen, the partner itself can give you access to a demo that they might have access to.

### 00:17:28 · Speaker 1

So those are the other two ways, two, three ways that you can get around. But primarily outside of a working environment, I would say that probably the most reasonably costed ones are the sandbox environments that I mentioned and the professorsoft.com. So there's two examples.

### 00:17:44 · Speaker 2

Got you. And let's say someone is working in a company that is already running the system. Are there any like certifications or designations or so offered by SAP or how does that thing work?

### 00:17:58 · Speaker 1

Yeah, so SAP offers certifications and in my experience, I've seen implementation partners, some of them had certifications, some of them didn't. But usually the certification just confirms at most that you are aware of the theory. And when you are actually trying to do implementation, as an example, the implementation companies will look for how many implementation life cycles you've been a part of. So there are people that you'll find that have two or three or five

### 00:18:28 · Speaker 1

implementation lifecycle experience but don't have the certification from sap so the certification will help you get the initial entry in but getting assignments and evolving is going to be based on the exposure that you've had in implementation

### 00:18:43 · Speaker 2

Got it. So for someone who is getting involved in the first implementation, right, because of course people, someone who has gone through like four or five implementations, they are already an expert regardless of the certification. So for them to even get a job in an implementation will be easier. But for someone who is starting new and is a part of an implementation project, for instance, what are the key skills in your opinion are that are a that are a must or they are like nice to have for us?

### 00:19:13 · Speaker 2

supply chain person involved in an SAP implementation in some shape or form.

### 00:19:19 · Speaker 1

Um, so I would say, look, okay, so there are two kinds of, uh, SAP, uh, roles that you will have, right? One is a user, right? The other one is an implementation partner or a team that is going to implement, uh, in a client environment. So as a user, I would say the roles, the expectations are a bit different. And as an implementation, it would be different. That said, I have typically seen implementation folks that come in to do implementations don't have a strong

### 00:19:49 · Speaker 1

necessarily of of of supply chain management they've gone and done a certification they know what capabilities exist in sap but the the challenge really is on how they translate uh that business requirement mapping to a functionality or capability from sap so the way i would explain sap and maybe this is my experience and my understanding of it so if i were to compare something like sap with an oracle my experience has been that sap's core strength is

### 00:20:19 · Speaker 1

actually the processes they've built in the box. Oracle's core strength is the database primarily, but they give you a lot of flexibility in what you want to do. Now, both of them, Mike's, so I've been involved with both implementation projects. The challenge was with SAP was implementation team comes, they say, okay, what do you want done? And they will say, okay, but here is how we'll implement in SAP. You need to have an understanding of what the business process should look like.

### 00:20:49 · Speaker 1

And what is what are the trade-offs when you choose one approach to another right so

### 00:20:56 · Speaker 1

That I would say is probably the trickiest knowledge bit that is important for making a successful implementation when we talk about implementation side, which is something that I found lacking when it comes to the implementation partners. That's where I would say the business side, there should be someone who fully understands what is it design-wise you want the solution to do, and then make sure the implementation team is selecting the right configuration from SAP to meet that functionality.

### 00:21:24 · Speaker 1

As an example with Oracle, you kind of tell them what you want done and they'll customize anything for you. But if you're having to customize SAP a lot, there's something wrong. You should not have to do that a lot. Now, that said, there are examples where SAP processes are quite rigid in terms of approaches. You might need to do certain level of customization, but if you find, but you should make sure that you first go through SAP to understand what are the options that are there or functionality

### 00:21:54 · Speaker 1

at functionalities that you can activate in SAP which would meet your intent before you look at customization. So I would say the biggest thing is have an understanding of supply chain end-to-end. So you really understand how supply chain should flow. And if you're looking at the overall supply chain, I would say have an understanding of demand forecasting, statistical models, how does it work? How does SNOP work? Inventory management concepts, production planning, MRP, capacity planning.

### 00:22:24 · Speaker 1

uh the logistics network you know distribution centers how what kind of transportation modes uh and then the the aspects related to i would say order management and warehouse operations as pick pack shipping these conceptual understandings will help you when it comes to looking at using sap because sap has a lot of these pre-configured but you should know which ones to select to meet your business intent

### 00:22:50 · Speaker 2

All right. So is it safe for me to say, Arsalan, that let's say, just talking about SAP and Oracle, Oracle is more customization friendly and SAP is more configuration friendly? Is that fair to say?

### 00:23:03 · Speaker 1

Well, okay, so my experience, and again, it's going back a few years, hopefully Oracle has evolved, but SAP was always, the strength of SAP was the processes in the box, and Oracle's strength was the flexibility.

### 00:23:20 · Speaker 1

But at the same time, it can be restricting in terms of, and again, pros and cons both ways, right? So if a business is trying to take on SAP, I would honestly recommend businesses make that choice saying, okay, I want to change the way I do things today. Because if you're not trying to do that, maybe you're better off not taking SAP because you will customize it so much that you lose value in it.

### 00:23:45 · Speaker 2

The buzzword these days, Arslan, is S4HANA, right? Everybody's talking about S4HANA. So tell us a little bit about how does it differentiate versus the basic core model, the ECC?

### 00:23:57 · Speaker 1

Okay, so one of the painful things about SAP prior version was the the user interface. SAP was pretty poor at that. And that's where Oracle used to always be a little bit better. I would say substantially better than than SAP. So the user interface was pretty clunky. You had to basically know the the form numbers where you call t-codes and you have to jump between t-codes to try and complete a whole process. So it was clunky. You needed to literally learn the sequence of steps.

### 00:24:27 · Speaker 1

So it was not used it was not user friendly I would say the most fundamental thing that the change that people will see when they move to Asperhanna is the user interface has changed dramatically The the graphical user interface is now web-based They've got what they call an application layer called fury F I O R I and it's made it's made to to allow people to interact with a lot more easily using a web interface

### 00:24:59 · Speaker 1

That I would say is probably the most important one when the users look at it. In the back of it, they've changed the architecture dramatically. So I would say ECC level ERP, each module was basically containing its own data tables and data moving from one module to another module was clunky as well. So with the new S4HANA system, they've consolidated the database at the back end into a more holistic system, which makes it

### 00:25:29 · Speaker 1

easier and faster. On top of that, the new database which is used in S4 HANA is what's called in-memory. So typically what you're having is all of the data is sitting in memory, so the computation is, or rather the accessing of the data is much faster. So from a user level, you will feel it to work faster, more smoother than the previous SAP platform. There has also been evolution in functionality as well at the same time. So you'll see a lot more

### 00:25:59 · Speaker 1

capabilities in SAP S4 HANA. Mainly, I would say the major chunks that have happened were migrations out of APO. So functionality. So as an example, the extended warehouse management EWM was a separate server prior to S4 HANA. They've now merged S4 HANA into S4 HANA itself. So now it's actually the same server where you have S4 HANA already containing the EWM module and you're just configuring it in that system. Previously, it would be a separate

### 00:26:29 · Speaker 1

system which would then need to be integrated separately for the data to move across. They've moved a lot of other APO functionality like especially the detailed scheduling capability from APO into S4 HANA. So S4 HANA is truly a step change in terms of user experience, functionality and speed.

### 00:26:50 · Speaker 2

Got it. And is IBP also benefiting from some of these newer user interfaces?

### 00:26:55 · Speaker 1

Yeah, so the new interfaces that SAP are using are coming across all of the layers of SAP. So all modules pretty much you will find the interface has changed to the Fury platform. So IBP has the Fury, but IBP has also offered a slight twist on it. So they're also allowing an integration with Excel. So planners for the most part, there are some things that you'll have to go use the Fury layer to actually interact with the system. But typically the day-to-day activities, the planners are mostly able to do them.

### 00:27:25 · Speaker 1

directly using a Microsoft Excel with a connector built into it. So you'll get all of your data out there. You can do the the planning runs directly from Excel. You can see the results in Excel. You can do the analytics and graphics in Excel. So IDP offers both. And that's one place where I would say IDP is different to the typical SAP interface.

### 00:27:48 · Speaker 2

Got it. And I don't know if you have got any specific experience in this space, Arslan, but I want to ask you that all of the, because I think the non-user-friendliness of the previous versions of SAP, at least this is my opinion, so I might be completely wrong here, right? So please feel free to correct me if I'm wrong, has given the rise to some of the more user-friendly, more customizable APSs like OMP 09 more recently and those kind of things, right?

### 00:28:18 · Speaker 2

Do you think all these upgrades done by SAP now brings the software in bar with competing with some of these more innovative solutions?

### 00:28:28 · Speaker 1

Um, look, SAP is not always going to be best of breed, right? But SAP offers or tries to offer a more holistic end-to-end platform. So

### 00:28:41 · Speaker 1

I would call it an ecosystem. So SAP is offering an ecosystem, which over time is evolving. I think if you refer to Gartner as an example, when it comes to planning, IBP is not as good as a few others. So it will be, it is not being seen as that high end, but SAP is, has got the deep pockets and it is investing heavily in trying to evolve it. For companies that are specialized, obviously they're best of breed. So O9, OMP, Kinaxis, Blue Yonder, I mean, they're pretty much doing,

### 00:29:11 · Speaker 1

focused activity so they only have a product stack that they're working on so for them that's their bread and butter for sap i would say it's something which they realize it's something they have to evolve but i think their their main uh capability right now is offering a truly end-to-end business management system right so if if you're typically an sap customer for you it's easier to go for ibp is ibp uh capable of matching the others in some

### 00:29:41 · Speaker 1

places yes and some places no so there's certain functionality you'll find the others are doing better but there's also certain functionality ibp does better so it's a mix and match but my understanding of it is that sap is constantly evolving uh the ibp layer and i think there's at least quarterly updates that are being pushed through uh so both for sap hana especially the cloud as well as the ibp layers they have quarterly updates sometimes even monthly information changes coming through but definitely quarterly updates coming through

### 00:30:11 · Speaker 1

functionality announcements that are happening

### 00:30:15 · Speaker 1

And now I would say the probably the most aggressive which is now trying to bring AI into play as well. So now there's a platform the SAP has developed, I believe already called SAP JUUL, which they're now trying to bring into the ERP and the IBP layer, which should make it a lot more capable as well.

### 00:30:34 · Speaker 2

All right. That was that's a great segue or something because that's what I was going to go next anyways. Right. So AI is another buzzword. And this is not just, you know, specific to supply chain or ERPs, but it's across the board. I mean, in your extensive experience and working in different industries and in consulting and now you, you know, this is also a good opportunity for you to talk a little bit about the the fantastic startup you're working with. Right. So tell us a little bit about like some practical

### 00:31:04 · Speaker 2

implementations of AI that you have seen which you think are going to be successful in the long term and how how do people really upskill to to learn these

### 00:31:17 · Speaker 1

Look, I think we're already seeing the advent of AI when it comes to, and it's kind of democratized, right? So AI now is available to people. Everyone has access to ChatGPT and it's not just ChatGPT. I mean, there are, there's Grok, you know, there's OpenAI, there's Claude, there's...

### 00:31:35 · Speaker 2

perplexity

### 00:31:37 · Speaker 1

Perplexity is a packaging. So there are people who develop AI platforms or AI solutions, and then there are people who are packaging these to offer as a consolidated layer. So Perplexity, I don't believe has its own AI. It actually backend connects with ChatGPT and Sonnet Cloud and all of these to offer you one interface to access different ones. So there are AI solution providers and there are what I would call front-end packages, right? So they're just an interface layer.

### 00:32:07 · Speaker 1

And maybe perplexity eventually will go there as well. But the amount of money needed to build an AI model and to train it and then to provide the compute capability to then answer questions is very capital intensive at this point in time. So there's a lot more packaging companies that are coming through. Now, when it comes to supply chain, I would say there's quite a bit of work that has happened in terms of this, but it has been pretty high end and only I would say companies that have deep pockets

### 00:32:37 · Speaker 1

have gone to do those things

### 00:32:41 · Speaker 1

So I'm aware of certain examples and I'm trying to recall specific ones. I would say the easiest ones that I've seen, there was a company that I came across.

### 00:32:52 · Speaker 1

It was it was acquired by another company called Logility and they were in the demand planning space. So they were offering a implementation of demand planning with AI where it supports the planner, but doesn't take it over completely. And the beauty of the system was they were offering this implementation within one day.

### 00:33:12 · Speaker 1

Now, that was a surprising twist and they eventually got bought out. So they were a startup, they got bought out by Agility. And I would say that was the first example where I saw someone actually using that aggressively. This was going back about three, four years ago. So that was the first one that I saw. I've seen of others where, for example, the transport network. So looking at doing route planning and optimization. Here is where there has been a bit of movement, I believe, in terms of trying to use

### 00:33:42 · Speaker 1

in there but it's still not really an AI engine I believe it's now coming beginning to come through but it's just a mathematical optimization for the most part right

### 00:33:54 · Speaker 1

AI, machine learning especially has started coming into demand planning. So when you talk about the concept of demand sensing as an example, right? When you're trying to look at changes in behavior, weather patterns, stock market. So when you're trying to take all of these parameters in to try and compute how you expect your demand to fluctuate or evolve, that's where the application of AI has started to come through. I haven't seen a lot of companies really adopt it much. It's still, I would say, early days.

### 00:34:24 · Speaker 1

But I expect that to come through as people get more comfortable with it.

### 00:34:29 · Speaker 1

AI, I'll give you an example where we're trying to use AI. So the startup that I'm with, we are currently developing a solution using drones that fly around autonomously in a warehouse, take pictures, and then there's an AI at the back end that converts those pictures into what is the item, how many cartons, what location.

### 00:34:48 · Speaker 1

Now, that is a pretty simple AI because it's just inferring information from looking at a picture, saying it's trying to read the barcode, it's counting the number of cartons stacked on a pallet, and then figuring out based on the stacking pattern how many cartons sitting behind that picture, right? So it's able to extrapolate information, but this is not true AI. This is basic inferencing. Now, so it's not very high-tech, but for example, the autonomous navigation component of it, where the drone has to look at, okay, I have an obstruction coming in front of it.

### 00:35:18 · Speaker 1

me how do I go around it do I go above it do I go below it do I go on the side uh you have things that are fixed right so you have for example you have the rack that is fixed not moving about but then you have someone uh walking around with a uh forklift right driving a forklift around that's a mobile obstacle so now you have to look at a dynamic issue and say okay how do I handle this this is where I would say AI is getting more interesting but it has to compute

### 00:35:48 · Speaker 1

in real time how it handles new challenges right

### 00:35:53 · Speaker 2

Excellent

### 00:35:54 · Speaker 1

So it's I said it's so there are two different applications one is more a static one which is not that uh interesting I would put it this way it's it's more straightforward another one which is a little bit more challenging

### 00:36:08 · Speaker 2

Got it. Yeah. Yeah. And of course, like, you know, anyone would love to see drones in a warehouse because it's like, you know, not only sounds cool, but, you know, imagine like if drones can do the regular cycle counting autonomously, how much time it saves, right? How much manpower.

### 00:36:22 · Speaker 1

I mean, look, the application is amazing. So the idea itself is great. The challenge is obviously is in the physical work of getting it out there, right? But it is, it is, and again, going back, it's not a new technology. What we're trying to do is not brand new. Others have done it. The way we're trying to come to the problem is to say, this problem someone has solved, but we're not seeing adoption. And one of the things that we figured out was the adoption is missing because the price point is still tricky. It's still a

### 00:36:52 · Speaker 1

heavy capex projects. So companies have kind of shied away from it because it requires as if you if you imagine yourself as a white house ops guy, someone comes and says, you know what, I have the solution. It's going to cost you 150 to 250 thousand dollars. You'll have to go and make a capex approval. You'll have to go convince people, then wait for the next time the budget is issued. And again, you lose the fizzle. It kind of fizzle out completely. Right. What we were trying to do and we're hoping to achieve is that we are trying to get it to a price point, which is comparable to the cost of an FTE.

### 00:37:22 · Speaker 1

And that for us is gonna change adoption fundamentally, right? Because if I'm the ops manager, you can come and tell me, here's a solution that costs you $50,000, and here's one that actually is comparable to your cost of your employees. So if you have the human resource budget, don't hire an additional resource, just take this, right? So that we believe would be the adoption point. So AI, people, you see, AI has come out a lot with a lot of flashy stuff. At the end of the day, it has to make sense at a business level, right? So when it's making sense at a,

### 00:37:52 · Speaker 1

The business level is only when it actually gives you value and is competitive. It can't be expensive. So, you know, I mean, as an operations, you don't want some flashy toy. You need something that delivers you value. And that's where adoption will truly drive. So that's where I see there's still some time where companies are coming up with applications where they're making it valuable from a benefit perspective, but also trying to bring the price point down.

### 00:38:22 · Speaker 1

So the equation becomes more reasonable

### 00:38:25 · Speaker 2

Excellent. And maybe getting, you know, translating all this to like the skill building point, right? So when I look at, for instance, generative AI, like for me, the easiest example to think about, you know, how the skills will transform is because I've been a planner for the longest amount of time in my life, right? So when we even interview today for, let's say, jobs in planning or data analysis, right? You ask those cliched questions around Excel, right? You know, do you know VLOOKUPS, HLOOKUPS?

### 00:38:55 · Speaker 2

and you know pivot tables and all of that stuff and I can clearly see now with what co-pilot and Microsoft is like doing with co-pilot right very soon those questions are going to get transformed to like you know hey can you write a prompt in Excel with co-pilot which will generate a pivot table versus asking pivot table questions themselves right how do you see what is the what is the robotics and AI version of that upskilling going to look like inside a warehouse or for an ERP like SAP going back to our original talk

### 00:39:26 · Speaker 1

When you look at what AI can do, AI basically can speed up the work of analysis. It can speed up the work of, and it's now getting towards more thinking capability, right? So the challenge I would say is we don't know where, how far AI will go, right? Now what technology seems to be capable of, and it's not just AI, and again, the conversation is now gonna shift probably substantially away from SAP, I guess, but.

### 00:39:54 · Speaker 1

We've got classical computers right now running AI algorithms, right? We're actually using a

### 00:40:01 · Speaker 1

basically a neural network that is learning from the information that we provide to it and that basically is able to give us responses and some basic level of analysis. Now we've already got what we have and again that's something which people are already using right chat GPT. Then we've got the additional layer which is now that it's not just doing analysis but is now taking action. So now we have AI agents that are coming up which will actually function like small robots which will look at information, will make a decision, will actually go and execute

### 00:40:31 · Speaker 1

decision right so they'll act on your behalf

### 00:40:36 · Speaker 1

And then, I mean, how far will AI go, right? There's the whole discussion around artificial superintelligence, which is for those of us that have the memory of a Terminator series, right? So if you remember the Terminator, they talked about this big AI called Skynet, right? We're actually not there yet, but we are trending in that direction.

### 00:40:59 · Speaker 1

Now, so what skill set do you need will depend on what is AI capable of at that point in time, right? So at this point in time, AI cannot really do the execution properly or completely, right? So here is where the role within supply chain of doing the strategic thinking and using AI to assist you in automating portions of the processes that can be automated would work. And as time goes by, I would say there's a

### 00:41:29 · Speaker 1

conceptual need to understand supply chain and how to design supply chain and how to run a supply chain, but then slowly look at automating portions of it that AI can take over. And over time as AI evolves to look at how the role will get changed, I would say the human creativity will not completely go away. I would say the strategic thought process, the human interactions, robots will take over some physical activities but cannot do all activities.

### 00:41:59 · Speaker 1

It's going to be a tricky mapping to try and do of how the reality would look like over the next five, 10 years. But I would say till 2030, at least artificial superintelligence is not coming about. But that said, quantum computing is also going far. So bringing together quantum computing and AI, I believe truly is going to be...

### 00:42:23 · Speaker 1

A real game changer

### 00:42:26 · Speaker 1

And hopefully that doesn't happen soon

### 00:42:28 · Speaker 2

That's right. So, uh, just as we come towards the end of the broadcast, uh, Aslan, and I mean, with your experience, I want to go back to, you know, your initial introduction where I think you are one of those very few, uh, you know, experienced individuals in supply chain who have worked in a CPG, who have worked as a consultant in healthcare, now working with a startup. So as you have moved from these different industries and different types of, uh, you know, works, um, what is your advice to someone fresh

### 00:42:58 · Speaker 2

who is coming into supply chain uh in 2025.

### 00:43:02 · Speaker 1

So depending on how companies have structured their supply chain model, it is a pretty wide spectrum of roles and functions and capabilities, right? The only way to learn all of this is by being curious. Now, at the time when I came into the career, there was no degree for it, right? Now there are degrees where you can actually go and go and get a supply chain certification program or a master's degree program. That didn't exist when I came into the career.

### 00:43:32 · Speaker 1

into the role and for me I would say curiosity was the most important thing

### 00:43:39 · Speaker 1

Then with that obviously comes the hard work behind it. I mean, you have to put the effort in it to learn it. And the interesting thing is to try and not just learn what you're doing yourself today, but to understand how this, what you do connects with others around you.

### 00:43:56 · Speaker 1

Now that is also an important thing when it comes to going back to SAP. People tend to go and focus on one module only. So they'll do MM only, but if you don't understand how MM affects the picking and packing and dispatch operation or how MM will affect the finance side of things, you will not benefit from this. So try and understand cross-functionally how what you do affects others and how what they do affects you. And I would say that knowledge of how looking at

### 00:44:26 · Speaker 1

the supply chain as a kind of a continuum and not just focusing on where you sit is important because the connectivity is where supply chain is actually enabled

### 00:44:39 · Speaker 1

So curiosity, connectivity, and lastly, I would say persistence. Supply chain is a job where there are days you'd get beaten down because things didn't go well. A lot of days. That can happen. That can happen a lot. So having the ability to get out of bed the next day and say, you know what, I'm going to go get this fixed.

### 00:44:51 · Speaker 2

A lot of business

### 00:45:00 · Speaker 1

and keep at it. So persistence, patience, perseverance. Those are the combination of qualities that I would suggest.

### 00:45:08 · Speaker 2

Excellent. I like the three P's, right? So this is, this is awesome. Great. Excellent. Now, uh, once again, Arsalan, I think thanks a lot for, uh, coming on this, uh, this channel. Uh, I'm sure like what you have shared in the context of general ERP, SAP, and I know towards the end, a discussion, uh, you know, went into, uh, AI and a lot of different interesting stuff that you are doing was super helpful. And the reason I keep asking, you know, these questions that these are the kind of questions I get every single day.

### 00:45:38 · Speaker 2

Like, you know, it's even on my channel as I've started focusing on supply chain every morning, I wake up to like 10 different questions. Some of them are about, Hey, all of this is changing. What does that mean for you? All the way to, OK, I'm just starting in supply chain. I just graduated. And to your point, even in my time, like there was no degree offered. Right. So now. uh younger professionals who are aspiring to take supply chain as a career they've got much better options to study supply chain as a subject which of course gives them a good opportunity to learn but

### 00:46:08 · Speaker 2

are still things you and I know very well. Nobody's going to teach you in a university. And that is where people like myself and yourself come in. Like we are trying to create this content, which is going to be helpful for people about things which are not typically taught in educational institutions. So on that note, Rusalan, thanks a lot for your time again. I really appreciate you taking the time to come on the show. And I'm sure, you know, as the questions come out of this podcast, we'll probably set up another session sometime soon.

### 00:46:36 · Speaker 1

Sure great Javial thank you for having me

