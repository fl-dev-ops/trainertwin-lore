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
  speaker_1: null
  speaker_2: null
---


# An Introduction to SAP Supply Chain Modules: A Podcast with a Supply Chain Expert


## Transcript

speaker_1: The latest version that people will hear about and probably come across is going to be whats called the SAP HANA S4 HANA platform and that is the more the latest edition Theres additional one which is called SAP IDES so IDES is Internet Demonstration and Evaluation System but you can download a system which you can install on your own computer and that one I believe is for free and it comes with some amount of company data so its stuff its an implementation that has data that you can play around with


So if a business is trying to take on SAP I would honestly recommend businesses make that choice saying okay I want to change the way I do things today Because if youre not trying to do that maybe youre better off not taking SAP because you will customize it so much that you will lose value in it And if youre looking at the overall supply chain I would say have an understanding of demand forecasting statistical models how does it work how does SNOP work inventory management concepts production plan


MRP capacity planning the logistics network you know distribution centers how what kind of transportation modes and then the the aspects related to I would say order management and warehouse operations as pick up shipping Ill give you an example where we try to use AI so the startup that Im with we are currently developing a solution using drones that fly around autonomously in a warehouse take pictures and then theres an AI at the back end that converts those pictures into


is the item how many cartons what location now that is a pretty simple ai because its just inferring information from looking at a picture saying its trying to read the barcode its counting the number of cartons stacked on a pallet and then figuring out based on the stacking pattern how many cartons sitting behind that picture right and the the interesting thing is to try and not just learn what youre doing yourself today but to understand how this what you do connects with others around you


Now that is also an important thing when it comes to going back to SAP People tend to go and focus on one module only So theyll do MM only but if you dont understand how MM affects the picking and packing and dispatch operation or how MM will affect the finance side of things you will not benefit from this

speaker_2: Hello and welcome to another very exciting podcast on my channel because today we will talk about a very common question I get from a lot of you which is how to supply chain professionals upskill themselves on SAP tools And to talk about that Ive got someone who is probably one of the best people to talk about it He is a very seasoned supply chain professional and leader who has worked in the consumer goods industry in the healthcare industry has worked as a consultant and


Apparently he is working with a startup so without further ado I would like to welcome Arsalan Sheikh to this podcast hello Arsalan how are you

speaker_1: Good thanks Shami thank you for having me

speaker_2: So Arslan before we get into the actual nuts and bolts of this podcast which is about the SAP tools why dont you give the audience a little bit of a quick introduction about yourself and your career journey

speaker_1: Sure Okay thats hopefully not gonna be too long I by background Im a chemical engineer I started my career way back in 1996 with Procter Gamble And it was an odd one So I was not a supply chain person I got hired in a role which evolved me into a supply chain person So supply chain is not a planned event It kind of happened But I look back at it with a lot of pride and a lot of learning So


I started my career with Procter Gamble in the production floor on the production floor and worked in production then moved to maintenance and reliability process reliability which people now refer to more as OEE managed those programs then got moved into engineering and health and safety so managed capital projects health and safety programs then moved into QA quality assurance quality control packaging and product development So I spent about six and a half years with Procter then moved to


Benkisa With Wreck it I moved into more I would call the front end supply chain roles So I was head of planning logistics with Wreck it for about three years And in that I was managing all levels of planning So demand planning production planning and scheduling materials planning customs clearance warehousing transportation So did that role then got posted with Wreck it to another site So I got posted to South Africa did that role there for about almost two years And then


Interestingly enough got a role with a hospital in Saudi so moved across to Saudi in a hospital environment that was a bit of a shocker uh didnt quite expect that to happen I guess but uh and then that was the start of about almost 11 years in a health in the healthcare environment so then I worked in hospitals in medical equipment companies commissioning hospitals then into medical device manufacturing one of my last roles was chief operating officer it was end to end


uh obviously covering all the different aspects of supply chain and operations and then moved to uae uh with a hospital group uh did that for about two years then interestingly enough started a consulting role uh with my own outfit uh did that for about six odd years and in that time mostly was doing work in saudi uh and most of the customers that are clients that i were getting were more in the food sector so did that for about six six odd years and then moved to


Canada in January 2025 with a startup where were developing currently a solution using drones and AI for automating the process of inventory counting

speaker_2: Excellent Thats a fantastic career journey Arslan And I know this podcast is about SAP but maybe if youve got time I would love to also ask you a few questions about your experience of moving from consumer to healthcare and then from healthcare to becoming a consultant and then from the world of consultancy evolving into the cool stuff that youre doing with AI and drones But before I get there lets just talk a little bit about SAP So I mean Ive made several videos about this Arslan but just


you know for the sake of educating our young supply chain professionals they hear all these different terms like you know flying around sap apollo ibp so educate us a little bit about what are the different modules in sap because its basically an erp but then what are the key tools one should know and have awareness about from a supply chain standpoint

speaker_1: Okay so SAP has evolved I guess over the years So SAP the latest version that people will hear about and probably come across is going to be whats called the SAP HANA S4 HANA platform And that is the more the latest edition You still will find people probably running a slightly older model of SAP Its called ECC And between these two I would say you probably find both of these


floating about Customers that are not wanting to migrate are still sticking on the old platform A lot of the customers have moved on to the new platform The modules pretty much remain the same in terms of nomenclature So typically supply chain guys will come across modules called MM which is materials management which is all the procurement activities the goods receiving goods issuing inventory management The main thing over there is that the inventory is is like a black box You know


how much is there but you dont know where it is inside the warehouse Then that evolves into the next level or layer that was thats called in warehouse management which then starts getting into locations and storage locations and stock movements and picking strategies And then they have the more advanced version which I would call the best of breed warehouse management solution Its called EWM extended warehouse management which is I would say a proper WMS Okay So thats more from the material side of it Theres SD


or sales and distribution module which is very so sometimes customer service functions if you have it within the supply chain side will be working on the SD module Sometimes youll find sales teams are actually working on the SD module and supply chain is not involved But typically thats where the sales orders are put in the order to cash process is completely run and shipping is also happening from there Beyond that if you go to the manufacturing side theres production planning or PP module Here is where


youre managing the the the activities of production on the floor so issuing production orders uh looking at the managing the bills of materials uh doing some basic level of demand planning but most people dont use that functionality in that because its not it doesnt have a lot of uh algorithms there its its very basic


And one thing that I forgot to mention is the layer of what people will be aware of called MRP So MRP fundamentally is part of the MM module but theres some functionality as a part of PP as well So especially when you want to look at inventory as days of cover that functionality I understand comes from PP


And this kind of covers the core of the ERP side of it Now SAP has additional modules around the ERP And here is where youll have terms like APO come about So APO was a solution that SAP put together as a standalone solution outside of the ERP And that did a lot of the I would say the more focused demand planning capability the detailed scheduling when it comes to production planning what they have in the core SAP module does not get in


to detailed scheduling It used to be an APO but what has happened is APO I understand is being phased out And some of the functionality of APO has kind of been moved into S4 HANA and some of it has been moved into IBP And I understand that is evolution that is continuing So what you will find probably over the next few years is APO will probably get closed And I think the phase out date is 2027 And by that time whatever was there in APO would be either part of S4 HANA or part of


IVP


And IBP as a layer is quite evolved So it has demand planning quite strong functionality It has inventory optimization So when you want to define safety stock parameters or levels in a single location or a multi echelon inventory location setup then it has SNOP It has a control tower which does both the collaboration outside of IBP So within the network


network collaborating with your suppliers and and your transportation providers uh doing analytics layers it has pre built kpis for uh score model if people are aware of score and uh and it has collaboration capability as well within the whole system um and the last part which i would say is a lot more of the optimization capability is a layer called supply and response


MRP people are aware is basically unconstrained planning It assumes you dont really have a problem with capacity It assumes you dont really have a problem with lead time So it does a mathematical calculation But the reality is that capacity is a constraint Machine is a constraint right People are a constraint Material availability is a constraint The number of vehicles you have is a constraint So here is where they also have the capability to do optimization looking at constraints as well as


handling when your demand is exceeding your supply So in that case typically what youd end up doing is allocating products to customers or prioritizing certain customers over the others So those kind of capabilities are all there in IBP So IBP I would say is really a kind of a layer which does a lot more intelligent planning whereas the core ERP does mathematical planning And theres a distinct difference between the two


And I would say the last module I would probably mention is SAP Ariba which is a procure platform procurement platform It covers end to end with the beauty of external collaboration


So those I would say are the key modules supply chain resources or plans or folks need to know of I guess just to be aware of that these things exist out there And


sap is continually evolving i will probably talk about a little bit more in terms of other functionality that theyre coming up with in the future

speaker_2: Just a question I mean and Ive always been curious about this R Sivanathan based on your experience on working with these things right Ariba and ABP how well do they perform if your entire ecosystem is SAP oriented So lets say you have got ECC or S4HANA at the back end and these tools are used for planning and procurement Or if youre using a completely different ERP and youre still using the SAP suite So what differences have you experienced

speaker_1: So if you are sitting on SAP core platform the connectivity with the SAP products is obviously going to be easier Its like Microsoft right If youre within the Microsoft platform or ecosystem its easier to kind of move data around So I would say implementation wise IBP and Ariba SAP IBP and Ariba would be easier if you have SAP as your core ERP They do work with other ERP systems as well So functionality wise they will still perform the same function


But there will be specific data translation requirements integration requirements which would be different But functionality wise they can work I dont expect I dont believe that there is a problem there

speaker_2: Excellent Great And just because you know most of my audience and the content I create is about like skill building and all of that right So anyone who is trying to upskill themselves on lets say something like IBP which is the bread and butter of supply chain what kind of resources are available based on your experience I mean one of the common answers I give when I get this question is that work for a company which is using this because thats probably the easiest way to get trained


But are there any other opportunities or avenues for people to get themselves upskilled

speaker_1: Okay so for as you said I mean the ideal one is you get a job in a company that is running SAP But if thats not the case then there are few ways to get the exposure to SAP prior The one thing that Ive seen a lot more in Canada is universities or colleges that have their own alliances with SAP and they offer access to SAP systems and some levels of training on that So Im aware of examples like George Brown


I have met with a couple of students from there that have talked about training that they got in SAP while at the university or college Beyond that there are kind of two three different areas So SAP itself has certain content that it is making available for free Mostly I would say the most extensive one is SAP Learning Hub It is probably the most expensive of all the options You pay a substantial amount of money could be a few thousand dollars to get access to the training as well


is the live system or a sandbox system environment to play around with uh theres an additional one which is called sap ides so ids is internet demonstration and evaluation system uh as you can so there are two versions of this ive seen and again i have not personally used them but you can download a system which you can install on your own computer and that one i believe is for free and it comes with some amount of company data so its stuff its an implementation that


has data that you can play around with uh you also find companies that are offering offering this as a solution for people to log in but obviously they charge for it uh it could range from anywhere to from 50 to like 100 per month and again if you buy bundles like three months or six months it gets cheaper a couple of examples is theres one company called sapidesandboxcom uh theres another one called professorsoftcom you can check both of them out there are examples that are


aware of but its not something Ive personally used them SAP also offers some kind of trial system access but again these are usually very short durations an hour a day maximum


There are training providers that Ive come across that are mostly out of India that Ive seen that are offering online trainings And as a part of the training solution they also offer sometimes access to an environment So those are the typical ways youll get it if youre not working Now if youre working you can actually get access in the company If your company has implementation that is going to happen the partner itself can give you access to a demo that they might have access to


So those are the other two ways two three ways that you can get around But primarily outside of a working environment I would say that probably the most reasonably costed ones are the sandbox environments that I mentioned and the professorsoftcom So theres two examples

speaker_2: Got you And lets say someone is working in a company that is already running the system Are there any like certifications or designations or so offered by SAP or how does that thing work

speaker_1: Yeah so SAP offers certifications and in my experience Ive seen implementation partners some of them had certifications some of them didnt But usually the certification just confirms at most that you are aware of the theory And when you are actually trying to do implementation as an example the implementation companies will look for how many implementation life cycles youve been a part of So there are people that youll find that have two or three or five


implementation lifecycle experience but dont have the certification from sap so the certification will help you get the initial entry in but getting assignments and evolving is going to be based on the exposure that youve had in implementation

speaker_2: Got it So for someone who is getting involved in the first implementation right because of course people someone who has gone through like four or five implementations they are already an expert regardless of the certification So for them to even get a job in an implementation will be easier But for someone who is starting new and is a part of an implementation project for instance what are the key skills in your opinion are that are a that are a must or they are like nice to have for us


supply chain person involved in an SAP implementation in some shape or form

speaker_1: Um so I would say look okay so there are two kinds of uh SAP uh roles that you will have right One is a user right The other one is an implementation partner or a team that is going to implement uh in a client environment So as a user I would say the roles the expectations are a bit different And as an implementation it would be different That said I have typically seen implementation folks that come in to do implementations dont have a strong


necessarily of of of supply chain management theyve gone and done a certification they know what capabilities exist in sap but the the challenge really is on how they translate uh that business requirement mapping to a functionality or capability from sap so the way i would explain sap and maybe this is my experience and my understanding of it so if i were to compare something like sap with an oracle my experience has been that saps core strength is


actually the processes theyve built in the box Oracles core strength is the database primarily but they give you a lot of flexibility in what you want to do Now both of them Mikes so Ive been involved with both implementation projects The challenge was with SAP was implementation team comes they say okay what do you want done And they will say okay but here is how well implement in SAP You need to have an understanding of what the business process should look like


And what is what are the trade offs when you choose one approach to another right so


That I would say is probably the trickiest knowledge bit that is important for making a successful implementation when we talk about implementation side which is something that I found lacking when it comes to the implementation partners Thats where I would say the business side there should be someone who fully understands what is it design wise you want the solution to do and then make sure the implementation team is selecting the right configuration from SAP to meet that functionality


As an example with Oracle you kind of tell them what you want done and theyll customize anything for you But if youre having to customize SAP a lot theres something wrong You should not have to do that a lot Now that said there are examples where SAP processes are quite rigid in terms of approaches You might need to do certain level of customization but if you find but you should make sure that you first go through SAP to understand what are the options that are there or functionality


at functionalities that you can activate in SAP which would meet your intent before you look at customization So I would say the biggest thing is have an understanding of supply chain end to end So you really understand how supply chain should flow And if youre looking at the overall supply chain I would say have an understanding of demand forecasting statistical models how does it work How does SNOP work Inventory management concepts production planning MRP capacity planning


uh the logistics network you know distribution centers how what kind of transportation modes uh and then the the aspects related to i would say order management and warehouse operations as pick pack shipping these conceptual understandings will help you when it comes to looking at using sap because sap has a lot of these pre configured but you should know which ones to select to meet your business intent

speaker_2: All right So is it safe for me to say Arsalan that lets say just talking about SAP and Oracle Oracle is more customization friendly and SAP is more configuration friendly Is that fair to say

speaker_1: Well okay so my experience and again its going back a few years hopefully Oracle has evolved but SAP was always the strength of SAP was the processes in the box and Oracles strength was the flexibility


But at the same time it can be restricting in terms of and again pros and cons both ways right So if a business is trying to take on SAP I would honestly recommend businesses make that choice saying okay I want to change the way I do things today Because if youre not trying to do that maybe youre better off not taking SAP because you will customize it so much that you lose value in it

speaker_2: The buzzword these days Arslan is S4HANA right Everybodys talking about S4HANA So tell us a little bit about how does it differentiate versus the basic core model the ECC

speaker_1: Okay so one of the painful things about SAP prior version was the the user interface SAP was pretty poor at that And thats where Oracle used to always be a little bit better I would say substantially better than than SAP So the user interface was pretty clunky You had to basically know the the form numbers where you call t codes and you have to jump between t codes to try and complete a whole process So it was clunky You needed to literally learn the sequence of steps


So it was not used it was not user friendly I would say the most fundamental thing that the change that people will see when they move to Asperhanna is the user interface has changed dramatically The the graphical user interface is now web based Theyve got what they call an application layer called fury F I O R I and its made its made to to allow people to interact with a lot more easily using a web interface


That I would say is probably the most important one when the users look at it In the back of it theyve changed the architecture dramatically So I would say ECC level ERP each module was basically containing its own data tables and data moving from one module to another module was clunky as well So with the new S4HANA system theyve consolidated the database at the back end into a more holistic system which makes it


easier and faster On top of that the new database which is used in S4 HANA is whats called in memory So typically what youre having is all of the data is sitting in memory so the computation is or rather the accessing of the data is much faster So from a user level you will feel it to work faster more smoother than the previous SAP platform There has also been evolution in functionality as well at the same time So youll see a lot more


capabilities in SAP S4 HANA Mainly I would say the major chunks that have happened were migrations out of APO So functionality So as an example the extended warehouse management EWM was a separate server prior to S4 HANA Theyve now merged S4 HANA into S4 HANA itself So now its actually the same server where you have S4 HANA already containing the EWM module and youre just configuring it in that system Previously it would be a separate


system which would then need to be integrated separately for the data to move across Theyve moved a lot of other APO functionality like especially the detailed scheduling capability from APO into S4 HANA So S4 HANA is truly a step change in terms of user experience functionality and speed

speaker_2: Got it And is IBP also benefiting from some of these newer user interfaces

speaker_1: Yeah so the new interfaces that SAP are using are coming across all of the layers of SAP So all modules pretty much you will find the interface has changed to the Fury platform So IBP has the Fury but IBP has also offered a slight twist on it So theyre also allowing an integration with Excel So planners for the most part there are some things that youll have to go use the Fury layer to actually interact with the system But typically the day to day activities the planners are mostly able to do them


directly using a Microsoft Excel with a connector built into it So youll get all of your data out there You can do the the planning runs directly from Excel You can see the results in Excel You can do the analytics and graphics in Excel So IDP offers both And thats one place where I would say IDP is different to the typical SAP interface

speaker_2: Got it And I dont know if you have got any specific experience in this space Arslan but I want to ask you that all of the because I think the non user friendliness of the previous versions of SAP at least this is my opinion so I might be completely wrong here right So please feel free to correct me if Im wrong has given the rise to some of the more user friendly more customizable APSs like OMP 09 more recently and those kind of things right


Do you think all these upgrades done by SAP now brings the software in bar with competing with some of these more innovative solutions

speaker_1: Um look SAP is not always going to be best of breed right But SAP offers or tries to offer a more holistic end to end platform So


I would call it an ecosystem So SAP is offering an ecosystem which over time is evolving I think if you refer to Gartner as an example when it comes to planning IBP is not as good as a few others So it will be it is not being seen as that high end but SAP is has got the deep pockets and it is investing heavily in trying to evolve it For companies that are specialized obviously theyre best of breed So O9 OMP Kinaxis Blue Yonder I mean theyre pretty much doing


focused activity so they only have a product stack that theyre working on so for them thats their bread and butter for sap i would say its something which they realize its something they have to evolve but i think their their main uh capability right now is offering a truly end to end business management system right so if if youre typically an sap customer for you its easier to go for ibp is ibp uh capable of matching the others in some


places yes and some places no so theres certain functionality youll find the others are doing better but theres also certain functionality ibp does better so its a mix and match but my understanding of it is that sap is constantly evolving uh the ibp layer and i think theres at least quarterly updates that are being pushed through uh so both for sap hana especially the cloud as well as the ibp layers they have quarterly updates sometimes even monthly information changes coming through but definitely quarterly updates coming through


functionality announcements that are happening


And now I would say the probably the most aggressive which is now trying to bring AI into play as well So now theres a platform the SAP has developed I believe already called SAP JUUL which theyre now trying to bring into the ERP and the IBP layer which should make it a lot more capable as well

speaker_2: All right That was thats a great segue or something because thats what I was going to go next anyways Right So AI is another buzzword And this is not just you know specific to supply chain or ERPs but its across the board I mean in your extensive experience and working in different industries and in consulting and now you you know this is also a good opportunity for you to talk a little bit about the the fantastic startup youre working with Right So tell us a little bit about like some practical


implementations of AI that you have seen which you think are going to be successful in the long term and how how do people really upskill to to learn these

speaker_1: Look I think were already seeing the advent of AI when it comes to and its kind of democratized right So AI now is available to people Everyone has access to ChatGPT and its not just ChatGPT I mean there are theres Grok you know theres OpenAI theres Claude theres

speaker_2: perplexity

speaker_1: Perplexity is a packaging So there are people who develop AI platforms or AI solutions and then there are people who are packaging these to offer as a consolidated layer So Perplexity I dont believe has its own AI It actually backend connects with ChatGPT and Sonnet Cloud and all of these to offer you one interface to access different ones So there are AI solution providers and there are what I would call front end packages right So theyre just an interface layer


And maybe perplexity eventually will go there as well But the amount of money needed to build an AI model and to train it and then to provide the compute capability to then answer questions is very capital intensive at this point in time So theres a lot more packaging companies that are coming through Now when it comes to supply chain I would say theres quite a bit of work that has happened in terms of this but it has been pretty high end and only I would say companies that have deep pockets


have gone to do those things


So Im aware of certain examples and Im trying to recall specific ones I would say the easiest ones that Ive seen there was a company that I came across


It was it was acquired by another company called Logility and they were in the demand planning space So they were offering a implementation of demand planning with AI where it supports the planner but doesnt take it over completely And the beauty of the system was they were offering this implementation within one day


Now that was a surprising twist and they eventually got bought out So they were a startup they got bought out by Agility And I would say that was the first example where I saw someone actually using that aggressively This was going back about three four years ago So that was the first one that I saw Ive seen of others where for example the transport network So looking at doing route planning and optimization Here is where there has been a bit of movement I believe in terms of trying to use


in there but its still not really an AI engine I believe its now coming beginning to come through but its just a mathematical optimization for the most part right


AI machine learning especially has started coming into demand planning So when you talk about the concept of demand sensing as an example right When youre trying to look at changes in behavior weather patterns stock market So when youre trying to take all of these parameters in to try and compute how you expect your demand to fluctuate or evolve thats where the application of AI has started to come through I havent seen a lot of companies really adopt it much Its still I would say early days


But I expect that to come through as people get more comfortable with it


AI Ill give you an example where were trying to use AI So the startup that Im with we are currently developing a solution using drones that fly around autonomously in a warehouse take pictures and then theres an AI at the back end that converts those pictures into what is the item how many cartons what location


Now that is a pretty simple AI because its just inferring information from looking at a picture saying its trying to read the barcode its counting the number of cartons stacked on a pallet and then figuring out based on the stacking pattern how many cartons sitting behind that picture right So its able to extrapolate information but this is not true AI This is basic inferencing Now so its not very high tech but for example the autonomous navigation component of it where the drone has to look at okay I have an obstruction coming in front of it


me how do I go around it do I go above it do I go below it do I go on the side uh you have things that are fixed right so you have for example you have the rack that is fixed not moving about but then you have someone uh walking around with a uh forklift right driving a forklift around thats a mobile obstacle so now you have to look at a dynamic issue and say okay how do I handle this this is where I would say AI is getting more interesting but it has to compute


in real time how it handles new challenges right

speaker_2: Excellent

speaker_1: So its I said its so there are two different applications one is more a static one which is not that uh interesting I would put it this way its its more straightforward another one which is a little bit more challenging

speaker_2: Got it Yeah Yeah And of course like you know anyone would love to see drones in a warehouse because its like you know not only sounds cool but you know imagine like if drones can do the regular cycle counting autonomously how much time it saves right How much manpower

speaker_1: I mean look the application is amazing So the idea itself is great The challenge is obviously is in the physical work of getting it out there right But it is it is and again going back its not a new technology What were trying to do is not brand new Others have done it The way were trying to come to the problem is to say this problem someone has solved but were not seeing adoption And one of the things that we figured out was the adoption is missing because the price point is still tricky Its still a


heavy capex projects So companies have kind of shied away from it because it requires as if you if you imagine yourself as a white house ops guy someone comes and says you know what I have the solution Its going to cost you 150 to 250 thousand dollars Youll have to go and make a capex approval Youll have to go convince people then wait for the next time the budget is issued And again you lose the fizzle It kind of fizzle out completely Right What we were trying to do and were hoping to achieve is that we are trying to get it to a price point which is comparable to the cost of an FTE


And that for us is gonna change adoption fundamentally right Because if Im the ops manager you can come and tell me heres a solution that costs you 50000 and heres one that actually is comparable to your cost of your employees So if you have the human resource budget dont hire an additional resource just take this right So that we believe would be the adoption point So AI people you see AI has come out a lot with a lot of flashy stuff At the end of the day it has to make sense at a business level right So when its making sense at a


The business level is only when it actually gives you value and is competitive It cant be expensive So you know I mean as an operations you dont want some flashy toy You need something that delivers you value And thats where adoption will truly drive So thats where I see theres still some time where companies are coming up with applications where theyre making it valuable from a benefit perspective but also trying to bring the price point down


So the equation becomes more reasonable

speaker_2: Excellent And maybe getting you know translating all this to like the skill building point right So when I look at for instance generative AI like for me the easiest example to think about you know how the skills will transform is because Ive been a planner for the longest amount of time in my life right So when we even interview today for lets say jobs in planning or data analysis right You ask those cliched questions around Excel right You know do you know VLOOKUPS HLOOKUPS


and you know pivot tables and all of that stuff and I can clearly see now with what co pilot and Microsoft is like doing with co pilot right very soon those questions are going to get transformed to like you know hey can you write a prompt in Excel with co pilot which will generate a pivot table versus asking pivot table questions themselves right how do you see what is the what is the robotics and AI version of that upskilling going to look like inside a warehouse or for an ERP like SAP going back to our original talk

speaker_1: When you look at what AI can do AI basically can speed up the work of analysis It can speed up the work of and its now getting towards more thinking capability right So the challenge I would say is we dont know where how far AI will go right Now what technology seems to be capable of and its not just AI and again the conversation is now gonna shift probably substantially away from SAP I guess but


Weve got classical computers right now running AI algorithms right Were actually using a


basically a neural network that is learning from the information that we provide to it and that basically is able to give us responses and some basic level of analysis Now weve already got what we have and again thats something which people are already using right chat GPT Then weve got the additional layer which is now that its not just doing analysis but is now taking action So now we have AI agents that are coming up which will actually function like small robots which will look at information will make a decision will actually go and execute


decision right so theyll act on your behalf


And then I mean how far will AI go right Theres the whole discussion around artificial superintelligence which is for those of us that have the memory of a Terminator series right So if you remember the Terminator they talked about this big AI called Skynet right Were actually not there yet but we are trending in that direction


Now so what skill set do you need will depend on what is AI capable of at that point in time right So at this point in time AI cannot really do the execution properly or completely right So here is where the role within supply chain of doing the strategic thinking and using AI to assist you in automating portions of the processes that can be automated would work And as time goes by I would say theres a


conceptual need to understand supply chain and how to design supply chain and how to run a supply chain but then slowly look at automating portions of it that AI can take over And over time as AI evolves to look at how the role will get changed I would say the human creativity will not completely go away I would say the strategic thought process the human interactions robots will take over some physical activities but cannot do all activities


Its going to be a tricky mapping to try and do of how the reality would look like over the next five 10 years But I would say till 2030 at least artificial superintelligence is not coming about But that said quantum computing is also going far So bringing together quantum computing and AI I believe truly is going to be


A real game changer


And hopefully that doesnt happen soon

speaker_2: Thats right So uh just as we come towards the end of the broadcast uh Aslan and I mean with your experience I want to go back to you know your initial introduction where I think you are one of those very few uh you know experienced individuals in supply chain who have worked in a CPG who have worked as a consultant in healthcare now working with a startup So as you have moved from these different industries and different types of uh you know works um what is your advice to someone fresh


who is coming into supply chain uh in 2025

speaker_1: So depending on how companies have structured their supply chain model it is a pretty wide spectrum of roles and functions and capabilities right The only way to learn all of this is by being curious Now at the time when I came into the career there was no degree for it right Now there are degrees where you can actually go and go and get a supply chain certification program or a masters degree program That didnt exist when I came into the career


into the role and for me I would say curiosity was the most important thing


Then with that obviously comes the hard work behind it I mean you have to put the effort in it to learn it And the interesting thing is to try and not just learn what youre doing yourself today but to understand how this what you do connects with others around you


Now that is also an important thing when it comes to going back to SAP People tend to go and focus on one module only So theyll do MM only but if you dont understand how MM affects the picking and packing and dispatch operation or how MM will affect the finance side of things you will not benefit from this So try and understand cross functionally how what you do affects others and how what they do affects you And I would say that knowledge of how looking at


the supply chain as a kind of a continuum and not just focusing on where you sit is important because the connectivity is where supply chain is actually enabled


So curiosity connectivity and lastly I would say persistence Supply chain is a job where there are days youd get beaten down because things didnt go well A lot of days That can happen That can happen a lot So having the ability to get out of bed the next day and say you know what Im going to go get this fixed

speaker_2: A lot of business

speaker_1: and keep at it So persistence patience perseverance Those are the combination of qualities that I would suggest

speaker_2: Excellent I like the three Ps right So this is this is awesome Great Excellent Now uh once again Arsalan I think thanks a lot for uh coming on this uh this channel Uh Im sure like what you have shared in the context of general ERP SAP and I know towards the end a discussion uh you know went into uh AI and a lot of different interesting stuff that you are doing was super helpful And the reason I keep asking you know these questions that these are the kind of questions I get every single day


Like you know its even on my channel as Ive started focusing on supply chain every morning I wake up to like 10 different questions Some of them are about Hey all of this is changing What does that mean for you All the way to OK Im just starting in supply chain I just graduated And to your point even in my time like there was no degree offered Right So now uh younger professionals who are aspiring to take supply chain as a career theyve got much better options to study supply chain as a subject which of course gives them a good opportunity to learn but


are still things you and I know very well Nobodys going to teach you in a university And that is where people like myself and yourself come in Like we are trying to create this content which is going to be helpful for people about things which are not typically taught in educational institutions So on that note Rusalan thanks a lot for your time again I really appreciate you taking the time to come on the show And Im sure you know as the questions come out of this podcast well probably set up another session sometime soon

speaker_1: Sure great Javial thank you for having me
