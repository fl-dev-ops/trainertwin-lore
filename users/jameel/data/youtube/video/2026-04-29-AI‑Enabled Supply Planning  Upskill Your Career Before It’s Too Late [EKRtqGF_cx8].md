---
id: EKRtqGF_cx8
title: "AI\u2011Enabled Supply Planning: Upskill Your Career Before It\u2019s Too\
  \ Late"
url: https://www.youtube.com/watch?v=EKRtqGF_cx8
date: '2026-04-29'
duration: 00:47:27
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# AI‑Enabled Supply Planning: Upskill Your Career Before It’s Too Late


## Transcript

### 00:00:00 · Speaker 1

there is always the scarcity of breakthrough thinking in our industry especially in planning because i'm you know planning is something which is very close to my heart uh and i still see that generally people are really stuck in that what i call is like the 1990s style of planning and so the more we can challenge the status quo the better

### 00:00:17 · Speaker 2

You need to know the difference between a demand review and consensus meeting, what the forecast value add is and why it matters. So in my experience, practitioners who skip this test use AI to accelerate a broken process. Okay, first what I have built is I used AI to be my DevOps engineer. I'm not using AI to be my supply chain planner.

### 00:00:47 · Speaker 2

And the beauty out of it when we are implementing those big names is it takes a lot of time to customize those reports to take them as an upload. This engine you're gonna get any file and you're gonna upload it the engine is gonna take it directly analyze it and it's gonna have the right data in it

### 00:01:09 · Speaker 1

Hello and welcome supply chain folks to another exciting podcast on my channel and today's topic is very exciting because my guest recently posted something on LinkedIn which became super viral I think it has already gotten like 90,000 plus impressions lots of different comments and what he posted was about how the AI tools are finally beginning to challenge the conventional planning tools as people reacted to the post there were a lot of different reactions some people were skeptical some people said they're wrong this is

### 00:01:39 · Speaker 1

an apples to apples comparison a lot of people ask questions but bottom line the reason i wanted to invite my guests to and have a podcast around this topic is there is clearly interest in learning or in experimenting how ai can change the world of planning so without further ado i would like to welcome alan mathar on my podcast hello alan how are you

### 00:02:00 · Speaker 2

I'm good, I'm good. Thank you, Jamil, for having me. I've been following your work for a while now. And honestly, when I first landed in Canada, you were one of the first voices I turned to. So being on this side of the conversation with you today means a lot. And thanks again.

### 00:02:24 · Speaker 1

Absolutely, Alain. It's a pleasure to have. So you, you caused quite a stir on LinkedIn, right? So the post you made and the tool you've made is, I mean, first of all, like I'm, the more I read about the tool and we also talked before this podcast, I am definitely a fan of this kind of work because I always believe that as a supply chain practitioner myself, there is always the scarcity of breakthrough thinking in our industry, especially in planning, because I'm, you know, planning is something which is very close to my heart. And I still see that generally people are really stuck in,

### 00:02:54 · Speaker 1

that what I call is like the 1990s style of planning. So the more we can challenge the status quo, the better. So first of all, for my audience, if you can just introduce yourself quickly, and then we can go into some of the specific questions around the AI tool you have built.

### 00:03:09 · Speaker 2

Thank you Jamil I'm a supply chain professional with more than 20 years of experience spanning from international humanitarian operations national retail 3PLs industrial manufacturing and now I'm in the telco business my career started in an environment most supply chain professionals will never work in I was in the peacekeeping department

### 00:03:39 · Speaker 2

in various missions across the world where a stock out is not a service failure it's a crisis it's life lives depends on you so that context shaped everything about how i approach uh supply chain risks uh process discipline and decision making under uncertainty which we live every day

### 00:04:06 · Speaker 2

I have a master's in supply chain from Shulik. I am certified from APICS CSCP. I have a black belt in Six Sigma and here I am.

### 00:04:22 · Speaker 1

Awesome, great. And thank you for all the, you know, the services you have done in the humanitarian space, right? Because I'm always admired by people who are using the supply chain skills for the betterment of humanity. So thanks for all the work that you have done here. So let's just get into the meat and potatoes of this topic, Alain. So my first question to you is that in your post and in the tool you have built, you have also talked about the enterprise versus the practitioner built tools, right? So tell the audience a little bit about the

### 00:04:52 · Speaker 1

differences between the two approaches what kind of mindset is involved and how to approach this whole new way of thinking

### 00:05:00 · Speaker 2

Most most of the companies I work for Jamil and I like to always follow the Oliver White IBP framework the class a So most of the companies I work for and these are big companies if I do a simple maturity assessment They would be sitting at 10 out of 40 which is the scale they use I be Oliver White use or maybe less So for me, it's not a technology

### 00:05:30 · Speaker 2

problem. It's people and process problem. So ERPs assume and those big names, they assume you already have a functioning demand review, supply review cadence, executive sponsorship, a clean master data, and the planning team that understands what the consensus number is, what the single source of truth. So in my experience, most organizations

### 00:06:00 · Speaker 2

Beginning an IBP journey have not they have none of that.

### 00:06:08 · Speaker 2

Enterprise ERPs are architecture to the finish line. Imagine buying and I always give this example buying a Ferrari for someone who doesn't know how to drive. So they are designed to optimize a process that already exists. What I needed was something that could create the process, something planners could open one day on a day one, let's say, run a forecasting model, review

### 00:06:38 · Speaker 2

build a leadership pack and walk into a meeting with one set of numbers not 12 months 18 months after an IT deployment but on a Tuesday

### 00:06:51 · Speaker 2

So I built a single HTML file to start with

### 00:06:57 · Speaker 2

no server no installation no itt ticket covering ibp planning steps i included abc xyz segmentations i included nine statistical forecast models which they are enough for my model that stock exposure would surface and be categorized safety stock by demand segment a full management business review pack so the mindset

### 00:07:27 · Speaker 2

The difference is this ERPs solve for scale and integration. The practitioners tools solve for right now with what you actually have.

### 00:07:39 · Speaker 1

Interesting. So just based on your experience of developing and implementing this, do you think that these tools, the practitioner-built tools, at least for now, they are a good fit just for, let's say, mid-sized companies who don't have any established IBP process or S&OP process? Or do you also see some applications in bigger enterprises as well?

### 00:08:03 · Speaker 2

I think three things converged that made what I built possible. And I don't think I could have done it even back in November.

### 00:08:16 · Speaker 2

So first, the front end stack is more democratized. No build stack required. Basically, I was chatting with Claude the way I'm talking to you. Of course, I have the right skills built in it.

### 00:08:33 · Speaker 2

And I didn't need a server, I didn't need DevOps team, no deployment pipeline. A planner open it in a browser and runs a whole winter's forecast on thousands of SKU in seconds. Second, those LLMs cross the threshold of particular utility for domain specific reasoning.

### 00:08:57 · Speaker 2

Okay, I embedded an AI copilot directly into the engine. That's an extra thing I did. Planners can ask why a particular SKU is flagged as an exception, get a gain language explanation, and decide whenever to override. They need to decide whenever to override. That capability would have required a dedicated data science team to do it, and it takes a month to do it.

### 00:09:29 · Speaker 2

And I think this one doesn't get enough credit.

### 00:09:34 · Speaker 2

AI platform inside large organizations, and this is what my organization offered me, have made it possible across frontier models without navigating month of IT approval.

### 00:09:48 · Speaker 2

So that last barrier was often the hardest one. And when it falls, people just build things.

### 00:09:55 · Speaker 1

So on that point, I have a question for you because when we and, you know, there is a there's a post I will also put in in front of the screen here for the audience. And I think I shared that with you earlier today as well. So as we think about AI applications and supply chain, there is a huge view out there, which is that before you even use any AI tools, you need to work on your fundamentals like your data connectivity, the data accuracy, because there is a very

### 00:10:25 · Speaker 1

strong view out there which is if you implement AI with broken data points or garbage forecast or garbage data points it is just going to speed up your process or speed you so to it's only going to speed up your process to create more garbage out of it so what do you say to those critics is that even fair based on what you have seen and on that note my question to you also is that even the tool you have built how did you address the issue of data quality or

### 00:10:55 · Speaker 1

of not having the right connectivity different between different systems. Because I think a lot of times I've seen myself in big companies that the AI discussion starts, but it almost stops or stalls at that point where somebody with a lot of experience is gonna say, hey, we need to fix the basics first. And the basics never get fixed perfectly because you'd never get into that perfect world. So what would you first of all say to those critics, Alain, and then based on your own experience, how do you, you have addressed, how have you addressed this challenge?

### 00:11:25 · Speaker 2

Okay, first what I have built is I used AI to be my DevOps engineer. I'm not using AI to be my supply chain planner.

### 00:11:40 · Speaker 2

AI helped me speed up building the solution that I designed for my planners to be able to manage by exception

### 00:11:52 · Speaker 2

and to to have a better control on a large scale operation

### 00:11:58 · Speaker 2

No

### 00:12:00 · Speaker 2

People confuse two things

### 00:12:03 · Speaker 2

AI planning is the AI doing the calling the shots on behalf of you, or you are calling the shots. In my model, I am calling the shots as a human being. AI is flagging outliers. It's not AI. AI has been there since ever with Python. With Python, machine learning. I'm using machine learning. AI helped me build this in four weekends.

### 00:12:31 · Speaker 1

So let me let me ask you there that that's a that's a good kind of comparison you have drawn there. So if I just compare like the way you have built and implemented this tool to let's say an implementation of a more, let's say, widely known industry tool, and I'm not going to take any names here. You are saying that AI has helped you speed up the portion which typically like the IT takes care of like the development of the code and all of that stuff, but you are not letting that tool drive your decision. So at the end of the day, if you

### 00:13:01 · Speaker 1

a demand planner or a supply planner you are the ones who's looking at that data and making those calls ai is not doing that but it's just that the journey to get to that level of sophistication technologically through whether you know it's that visualization of the data or it's the crunching of the numbers that's the piece where ai is really helping you so it it's almost like refuting that argument where you know people are saying though let's fix the data first before we go to ai you are actually saying that no you could still do it with broken data but you need to be very

### 00:13:31 · Speaker 1

careful that you are using AI to speed up your your connectivity and making sure that those you know connection points are seamless or the the the process of assimilating the data is faster but at the end of the day who makes the decisions based on the output is still a human being is that fair to say

### 00:13:48 · Speaker 2

Yes, and as you're gonna see in the tool, I included a tab for data cleaning. And it's important for a planner to go into that tab and look for outliers and clean the data, remove the zeros, whatever. And I wanna highlight thing. Those models, they became so clever. So any mistake they do, they are able to convince you about that mistake.

### 00:14:18 · Speaker 2

never admit that and and that question that you ask is is a hundred percent valid that we need to be careful of what we are doing with AI the gap between the attention intelligence and the reality is becoming big that those models are able to convince you about anything

### 00:14:41 · Speaker 1

makes sense so i think this is a very good segue for us to get into the tool itself right because i can keep asking you all these interesting questions but i think for the audience it'll be really you know powerful to see the tool itself so why don't you share your screen alan and we can go into the tool let me just uh add it over here and i will hand it over to you before you get into the tool itself alan if you can just give an overview so my understanding is that and you correct me if i'm wrong that this is basically a distribution management tool so you are trying to manage your inventory and your

### 00:15:11 · Speaker 1

to optimize your transfers across multiple warehouses that's the primary goal is that right

### 00:15:17 · Speaker 2

It's it's a forecasting engine. It it's also helps you build your IBP process right It doesn't replace I just want to highlight this and we didn't touch base on that This tool doesn't replace any of the big players in the in the market and this is important

### 00:15:39 · Speaker 2

for for for big companies and they will always go to those big names this tool is for young teams and i mean by young teams the one that they're starting their ibp journey

### 00:15:56 · Speaker 2

don't know what is ibp people think that ibp is some kind of software that's gonna you're gonna bring it in and it's gonna solve them that make them solve their problem why it's a process discipline it's people process then technology so this engine is gonna help them understand that process so i'm gonna walk you through some of the features of it and uh i hope i hope you you will see how much it's

### 00:16:26 · Speaker 2

is it's the thought process of it and from there you're gonna say okay this guy builds it in in four weeks i think i can do the same anybody can do the same with the right setup

### 00:16:42 · Speaker 2

The engine

### 00:16:46 · Speaker 2

And the beauty out of it, when we are implementing those big names is it takes a lot of time to customize those reports to take them as an upload. This engine, you're gonna get any file and you're gonna upload it. The engine is gonna take it directly, analyze it, and it's gonna have the right data in it. And I already-

### 00:17:06 · Speaker 1

So, so, sorry to interrupt you, Alon. Like, so, so one common thing which I see, for instance, you know, you like your first file is a consumption history file. Imagine, because I've, I've seen this myself. This is, it's a personal story, right? Uh, imagine this file is coming from your customer, you know, let's imagine that for a second. Right. And what I've seen is that sometimes the customers would, you know, on a random week, they will decide that now instead of using this ordering of columns, I'm just going to add another column.

### 00:17:36 · Speaker 1

around I'm gonna just you know shuffle my excel organization and then you receive a file and then you know all your v lookups and h lookups are normally like messed up so is this tool smart enough to detect those kind of things yeah

### 00:17:49 · Speaker 2

Yeah, the system is gonna soup is gonna flag what's important, which is plant, SKU, month, quantity, and value.

### 00:17:58 · Speaker 1

Awesome

### 00:17:58 · Speaker 2

And if there's something wrong it's gonna it's gonna it's gonna say it

### 00:18:04 · Speaker 2

So you have the consumption history, I built a visibility tool that has lead times, plants, on-hand quantity, cost, ABC, stocking, min-maxes, everything. I have this file from SAP.

### 00:18:19 · Speaker 2

It's an open PO in transit. We can change it. And on top of that, I added the confirmed orders because confirmed orders, they override any forecast. Now.

### 00:18:30 · Speaker 1

So just before you move on, I just want to go step by step here so that people can follow, right? So basically your consumption history is just showing your history, which is basically, I'm sure that the model is using that history to generate like projections as well. Your visibility tool is basically your kind of, you know, IP parameters, basically, right? So that's about all your supply chain parameters and your open POs and in transit is basically showing you like a snapshot of what is really like in transit and on PO right now. Got it. Perfect.

### 00:18:56 · Speaker 2

Confirmed orders, what you have actual orders. I added the budget section because your goal is to link it to financials.

### 00:19:10 · Speaker 2

Apply and run we have the number of materials we have how many plants which is warehouses and we have 24 months of of data

### 00:19:19 · Speaker 1

Right when you say when you say materials two seven three six uh Alan that means that's the number of SKUs

### 00:19:26 · Speaker 2

Yes, number of SKUs. And this is important for the planning and I'm going to explain why. Because I've seen this a lot in companies. We do planning based on material, which if you have 10 warehouses, you don't follow the right demand signal. And I'm going to show you how I mitigated that. So the first thing, I am a planner. I have my, let's say, program.

### 00:19:54 · Speaker 2

I have my workbench in the morning I come here I have my to-do list

### 00:20:00 · Speaker 2

overdue to do due this week planned confirm POs transfer savings and capital budget I can hover also in this now I added something for the network opportunities which is if you have a lot of warehouses you need to look into the in the opportunities within your inventory so you don't grow your excess stock and your debt stock and this is the opportunity here then

### 00:20:32 · Speaker 2

I move to exception report

### 00:20:37 · Speaker 2

I have built 20 exceptions for every demand, supply, demand, supply, inventory analysis to look at. Also, you have what's critical, high, and of course, the global filter applies also here for every planner.

### 00:20:56 · Speaker 2

I have built a stocking policy most companies they do gut feel stocking

### 00:21:01 · Speaker 1

I know

### 00:21:02 · Speaker 2

We don't know what we don't know

### 00:21:03 · Speaker 1

I can I can make a video about that right So there's like how many companies use peanut butter spread models yeah

### 00:21:09 · Speaker 2

Yeah and and your smile like told me everything about it

### 00:21:13 · Speaker 2

Like basically here we're putting some parameters that we can adjust, we can update. And I'm telling with this tab what we wanna have, where we wanna have, and how much we wanna have. Now I included ABC, XYZ. We can come up with a later on part of our continuous improvement journey. We can come up with a different policy based on every

### 00:21:41 · Speaker 2

every business and I can tell you right now if you come up with a policy now while we're talking I will go to Claude I will change it and put it before the session ends

### 00:21:55 · Speaker 2

This is how much became easy

### 00:21:58 · Speaker 1

Amazing. And this stock modeling policy in this tool, Alain, like how complex is it? Is it, you know, taking your history and calculating your demand variability and adjusting your safety stock target accordingly? Wow. Okay.

### 00:22:13 · Speaker 2

I'm using always in my calculation the average demand interval and the coefficient of variance which is

### 00:22:19 · Speaker 1

Gotcha

### 00:22:19 · Speaker 2

I'm staying class right now

### 00:22:21 · Speaker 1

The COE yeah yeah

### 00:22:22 · Speaker 2

Yeah yeah

### 00:22:24 · Speaker 2

Segmentation, it's like, this is my dashboard. I wanna see what's smooth, erratic, lumpy, irregular. I wanna see ABC also. And you can drill down into every, every segment. And what I talked before about combining the plant and the material to follow the demand signal, that's why you have a new material in this engine.

### 00:22:54 · Speaker 2

So you have plant and material number to get the right demand signal, to follow the right demand signal.

### 00:23:02 · Speaker 2

cleaning and this is where most concerns are about AI planning and this is not an AI planning but I added a cleaning tab to clean our data so this this is gonna plan gonna flag our outliers an SKU for example that was that had a demand for the last three four months most 24 months we were demanding 10 units per month suddenly we see a spike

### 00:23:32 · Speaker 2

of 40 this cleaning tab is going to flag it the planner is going to have the right conversation with the right stakeholder with marketing with whatever you're dealing with to get

### 00:23:44 · Speaker 2

to get some info enrichment about that because otherwise the system is gonna forecast new quantities

### 00:23:51 · Speaker 1

Is that is that getting flagged here or is this this kind of anomaly uh feeding like an exception report because you showed some of the exception reports earlier?

### 00:23:59 · Speaker 2

It's another layer of exception report, but here it's based on spikes, zero demand, seasonal peak, data error, low outlier, unclassified. So the planner is gonna be able either to accept or to reject or to override with a quantity and add a note.

### 00:24:25 · Speaker 2

Visualization, another layer of dashboard. We have our forecast accuracy, inventory health, open exceptions, consensus. And again, for every planner and every, you can do it for managers, you can do a selection for them. We have the cycle where we are, SKUs, plants, all kind of dashboards, all dynamic, they change. Forecast, this is the forecast engine.

### 00:24:55 · Speaker 2

the tournament of the forecasts so every sku in every plant you can see how much we're what's the what's the best model for it i included nine models but they were enough for this business

### 00:25:13 · Speaker 2

And it will pick the best model based on 80% training and 20% validation.

### 00:25:22 · Speaker 1

Interesting okay and those like picks and chooses those models based on the

### 00:25:23 · Speaker 2

Those like

### 00:25:27 · Speaker 1

Specific data variations okay

### 00:25:28 · Speaker 2

Yes. Variations. Okay. Yes. I have a table of what algorithm we need to use for every, let's say, every supply chain model. You have CPG, you have pharma, you have healthcare, you have engineered order, infrastructure, whatever. So there are different algorithms which they are recommended by the industry.

### 00:25:54 · Speaker 1

Right, which is also like, you know, you actually answered one of the questions I was gonna ask you, because sometimes your choice of your forecasting model is dependent on your manufacturing policy. So if you are make to order versus make to stock or make to forecast, you may choose a different model, but you have already answered that question.

### 00:26:10 · Speaker 2

This is an engineer to order model here

### 00:26:12 · Speaker 1

Got it, okay.

### 00:26:14 · Speaker 2

Error analysis, also the engine is gonna error, it's gonna analyze, do analysis, analysis on all these errors. It's gonna flag everything for you. This is an FYI. You can hover between. I included this one, which is one of the new data scientists, he likes to use it. It's MAE plus bias. It's proven, it's a good, it's a good metric.

### 00:26:42 · Speaker 1

I'm not gonna I'm not gonna ask questions on that because then we can have a podcast on that itself because this is such a an interesting topic but yeah keep going

### 00:26:42 · Speaker 2

Not even

### 00:26:51 · Speaker 2

Scenario planning

### 00:26:54 · Speaker 2

Consensus and here we add after we send the forecast to the different stakeholders this is a forecast by program or by demand or by category and you have the budget for it we send it to our internal stakeholder in our before our demand review we get the enrichment of the forecast and we put it here we upload the consensus and you will have new numbers for it

### 00:27:24 · Speaker 2

We're gonna get the rolling plan based on lead times. We can upload the lead times, the new lead times, because sometimes lead times change and especially in our industry, everything is changing now.

### 00:27:36 · Speaker 1

So this is this is then fetching from the latest file you stored at the beginning of the visit

### 00:27:41 · Speaker 2

Beginning of yes visibility

### 00:27:44 · Speaker 2

So you have your frozen zone, slushy zone and liquid zone. And this is only to show what you can do adjustment and what you cannot.

### 00:27:55 · Speaker 2

You'll have a final program forecast that it's gonna cascade to the demand to the supply planners.

### 00:28:03 · Speaker 2

Decomposition, this is only statistical to see seasonality, to see trends.

### 00:28:11 · Speaker 2

Safety stock calculations

### 00:28:14 · Speaker 2

individual SKUs and you can adjust the service level because it's based on service level

### 00:28:19 · Speaker 1

And these safety stock targets are getting updated based on every like data signal is changing. So yes. So one day you may be saying, okay, the right target is, I don't know, 15 days of safety stock, but then the next data point might say, okay, now you need to increase it to 16. So it's almost like dynamic safety stock.

### 00:28:20 · Speaker 2

He's

### 00:28:26 · Speaker 2

Help yes

### 00:28:36 · Speaker 2

It's dynamic. You don't you don't want to have the same safety stock the whole year. Otherwise, you're going to end up with with excessive inventory also for the min maxes also for everything.

### 00:28:48 · Speaker 1

You can have

### 00:28:48 · Speaker 2

You can have aggregate

### 00:28:52 · Speaker 2

Safety stock calculations multi echelon because you're dealing with a lot of

### 00:28:57 · Speaker 2

warehouses and you want to capture those internal transfers so you won't account those for as a demand

### 00:29:08 · Speaker 2

DDMRP and this is I added as an indicative because this is where we're going after IBP it's gonna be DDMRP and it's only

### 00:29:18 · Speaker 1

I really yeah just one question before we get into DDMRP, Alan. So I know you have designed this for like an MEIO, right? But if I had to adapt this model to a single echelon supply chain, how difficult would it be to change this model?

### 00:29:36 · Speaker 2

Or we can do it uh 15 minutes 20 minutes

### 00:29:41 · Speaker 1

Awesome, okay, great

### 00:29:44 · Speaker 2

So after this you'll get a supply plan.

### 00:29:49 · Speaker 2

by supplier and you can see your cash flow how is it going and you're gonna be able to share the the the forecast with your top vendors based on 6 12 18 24 month

### 00:30:05 · Speaker 2

I added something which I always like to have which is plant compare I like to if I'm dealing with a lot of distribution centers I like to compare my my warehouses to a benchmark internally to my best performing warehouse and here you can choose from your warehouses and you can see the metrics that I included also adjustable for any kind of

### 00:30:35 · Speaker 2

industry you want you have the performance radar you have the ABC how they're doing days on hand inventory health excess and obsolete inventory now

### 00:30:49 · Speaker 2

DNC planning, which is the SNOP, but in infrastructure, because you don't sell stuff, I call the DNC. You have all these metrics and people spend hours on building

### 00:31:03 · Speaker 2

Presentations

### 00:31:05 · Speaker 2

IBP

### 00:31:07 · Speaker 2

The first rule is to have a standard presentation

### 00:31:11 · Speaker 2

Executives come to it they struggle the first time second time but then they will know what to do the system

### 00:31:21 · Speaker 2

is gonna have a presentation ready

### 00:31:23 · Speaker 1

Nice

### 00:31:24 · Speaker 2

It's gonna be shared automatically, let's say every Thursday of every week to a different audience. This is the NCDC planning, demand signal review, demand review, supply review, and this all can be adjusted.

### 00:31:45 · Speaker 2

Capacity alignment which is the supply review executive review

### 00:31:53 · Speaker 2

Now, last but not least, we can always add things to it. I added a new product introduction.

### 00:32:02 · Speaker 2

And this is important in in in engineer to order you need to have what is the material number description Is it under review by design program ID program? When is the program is it going to start? What is the lead time for that material? And if is it phasing out is the is the projects gonna end so So you won't end up with a lot of inventory and

### 00:32:32 · Speaker 2

your warehouse is the program driven is it only for a certain program or or is it an S curve and you can select the predecessor to have the same forecast to allocate

### 00:32:47 · Speaker 1

Not sure

### 00:32:49 · Speaker 2

Portfolio lifecycle, you'll be able to track where are you and to have a meaningful conversation with different stakeholders. So about your inventory and you have the demand forecast, how it's interacting with the new and the old one.

### 00:33:07 · Speaker 1

Very interesting like a phase in phase out kind of thing right so

### 00:33:10 · Speaker 2

Yeah, now the AI part that can interact with this one is the AI copilot. It's only informative. You'll ask the AI, you link it to Claude, you link it to any AI you want.

### 00:33:25 · Speaker 2

You'll ask the AI what is my next step because we're gonna include the code in this and he's the AI would be able just to guide you through the steps. It doesn't have any planning authority.

### 00:33:42 · Speaker 2

I added a debugging assistant so if I'm away I'm managing this the system is gonna help debug by itself

### 00:33:51 · Speaker 1

And then does this IBP co-pilot also have the capability of doing like investigations? So for example, you know, a lot of times planners need to find out that, okay, my PO number this, you know, it's late or like, you know, what's the latest date? Like, can I can I do like more chat GPD kind of stuff on this data itself or not yet?

### 00:34:14 · Speaker 2

Not I didn't include this 'cause most of the feedback I got would this be linked directly to your main ERP

### 00:34:27 · Speaker 2

I don't want at this point to this AI goes into SAP and ask it for stuff

### 00:34:35 · Speaker 1

Okay but that's possible

### 00:34:37 · Speaker 2

Yeah, like, like you can have with the with the PO in transit, you can have, okay, you can have late POs. Like, for example, this PO is supposed to come today. It's going to tell you, okay, this PO is late.

### 00:34:52 · Speaker 1

Awesome. Got it. One question I have, Alain, like, so you, you, thanks for walking through all the steps, right? So it's very clear that it's a, it's a forecasting tool, it's an inventory calculation tool, it's basically feeding all of that information into your SNOP or IBP process. It's, you know, generating dashboards, it's all fantastic. One of the questions I asked you earlier, which I want to go back is, show me the screen where it's also doing the inventory optimization across multiple where

### 00:35:22 · Speaker 1

houses. So for example, if I want to now see, do I need to transfer stock between my DCs to rebalance my inventory? Where do I do that?

### 00:35:31 · Speaker 2

Network cleanup

### 00:35:33 · Speaker 2

So it flags the opportunities within your network, it flags what you don't need to stock and consolidate the to hubs. In this model.

### 00:35:45 · Speaker 1

And this as well

### 00:35:47 · Speaker 1

So basically it's saying like 903 opportunities for you to move stuff around the network to optimize your availability. And then there is one item which you probably don't need to like you can get rid of it. And then there are 99 items where you can basically put them together in a hub. Very interesting.

### 00:35:47 · Speaker 2

Wait so basically

### 00:36:04 · Speaker 1

Okay, this is awesome. This is awesome. No, this is a great overview.

### 00:36:06 · Speaker 2

Awesome. No, this is just a great overview. I didn't show you this. This is excess and obsolete aging. It will show you what's aging for 24 months. It will show you projected inventory, how much you're going to buy. It will show you plant summary, how much you're buying for every plant.

### 00:36:29 · Speaker 1

Very interesting. Very interesting. One question on that, which is coming to my mind is like, it's doing your aging analysis as well. But in our input, at least we didn't see anywhere where you have, is the age or the shelf life of the product also part of the parameters you are entering?

### 00:36:47 · Speaker 2

For this no, but I included in the in the new product introduction, I included in the material how much you're gonna be able to use it.

### 00:37:01 · Speaker 2

For example, the program starts here, when is the phase out? So we can customize that to be a shelf life. Again, this is for infrastructure engineer to order. We can customize it for other models, for example, FMCG, for a CPG, to have a shelf life, which is important in that domain.

### 00:37:29 · Speaker 1

Very interesting. Now this is an excellent overview Alain. Is there anything else you want to share on the tool because now I already want to ask you some capability related questions.

### 00:37:37 · Speaker 2

Uh I'm I think I think we showed everything in the tool

### 00:37:41 · Speaker 1

Yeah that's also

### 00:37:41 · Speaker 2

There's also another clock to see who who did what

### 00:37:46 · Speaker 1

Of course, makes a lot of sense. Yeah. So basically, obviously, the impressive part of all of this, Alain, is like the speed at which you were able to build this and where the technology is taking us, right? But my next question to you is more about if someone wants to upskill themselves on this one, you know, which is... it may be easy it may not be easy i don't know you tell me uh but what are the technical skills one need to know to get to this level of proficiency where you are

### 00:38:16 · Speaker 1

Where you were able to build this thing from scratch in you know literally like several weeks

### 00:38:26 · Speaker 2

I think for that like in in what I do

### 00:38:30 · Speaker 2

Three skills in priority order

### 00:38:34 · Speaker 2

And the order matters really. You need to understand the business. Like in this case, we need to understand what is IBP process literacy. Before we automate anything, we need to understand what a good integrated business planning cycle looks like.

### 00:38:51 · Speaker 2

I follow Oliver White Class A framework, which for me, it's the benchmark. You need to know the difference between a demand review and consensus meeting, what the forecast value add is, and why it matters, how a constrained supply plan gets built.

### 00:39:09 · Speaker 2

So in my experience, practitioners who skip this test use AI to accelerate a broken process.

### 00:39:18 · Speaker 2

And the faster broker's broken process is still broken. Second,

### 00:39:24 · Speaker 2

AI fluency as a practitioner, not as a developer. This is not about learning how to code, it's about understanding how to work with LM, LM, and to solve real planning problems. We always tell the AI what to do, but we don't tell it what not to do. And this is where it makes or breaks a good answer.

### 00:39:51 · Speaker 1

So let me let me stop you there Alana and I want to clarify a very important point here which I've been thinking about and I'm you know it would be great to get your perspective. Is it fair to say that like until now we have been saying that in order to work in supply chain the number one skill you need to have on the technical side is you at least need to know how to manage a spreadsheet and it starts with Excel and then you know Excel of course you know in every job interview people ask that question. Do you think we are quickly moving to a world

### 00:40:21 · Speaker 1

where a big part of a supply chain practitioner's toolkit should be LLM knowledge or you know like you said not being a coder but knowing those LLM models as a practitioner

### 00:40:39 · Speaker 2

I say it's an important part but it's not a big part a big part is still to understand processes discipline

### 00:40:48 · Speaker 1

Got you which is your first point the business process knowledge and the literacy of the processor which is

### 00:40:54 · Speaker 2

And I can tell you a secret, I don't know how to prompt.

### 00:41:00 · Speaker 2

I still don't know how to prompt and I will never learn how to prompt

### 00:41:05 · Speaker 2

I created and this is a secret for your audience and it's a secret soft I created a prompting skill

### 00:41:16 · Speaker 2

I ask Claude to prompt for me

### 00:41:21 · Speaker 1

You ask AI you ask you ask AI to give you an AI prompt basically

### 00:41:21 · Speaker 2

Nice

### 00:41:24 · Speaker 2

He will do a better prompt every time every single time than any human

### 00:41:31 · Speaker 2

Once you get a good description and again we tell AI what to do but we don't tell it where to stop and what not to do

### 00:41:41 · Speaker 2

And this is what got me here fast

### 00:41:46 · Speaker 1

And is it just Claude that you used, Alain, to build this or there were other software involved in this as well?

### 00:41:53 · Speaker 2

I have access to Claude, to Gemini, to ChatGPT. Okay. But I've been using personally Claude for the last two years. I'm happy with it.

### 00:42:08 · Speaker 1

Got you. And then maybe this is getting towards the end of this podcast. So if someone, so you talked about the business process literacy, you talked about the AI fluency, any other tools or techniques one needs to know in order to accelerate their learning in this space? Because one of the issues I've seen is that in supply chain, generally people are so busy executing the day-to-day. It's almost like that analogy of that you are using a broken saw.

### 00:42:38 · Speaker 1

and but you're just using it harder and people don't have enough time to sharpen the saw and get more skillful but for someone who is in that predicament what would your advice be how they can upskill themselves in this world of ai

### 00:42:54 · Speaker 2

Okay, I'll, there's not a single recipe, but I'm gonna tell you what I do. I have 20 minutes allocated every day when I wake up to check on what's new in AI. And I can tell you since December until now, it's moving very fast.

### 00:43:16 · Speaker 2

for me the most important thing i audit the skills that i built in in in in cloud because in in cloud you can build those skills every two weeks i audit those skills i do a gap analysis i ask cloud to do a gap analysis again with a good prompt he does the prompt he does the gap analysis and then i just upload the skill that's it

### 00:43:43 · Speaker 1

Got it

### 00:43:44 · Speaker 2

And so getting better

### 00:43:45 · Speaker 1

So

### 00:43:47 · Speaker 1

Got you. So basically the crux of this, this part of the conversation, if I'm getting you right, is that you need to understand the process well enough so that you can ask AI the right questions and give it the right input to get to the right prompts. And then everything else basically flows from there because you don't need to code. You don't need to know how to code itself, but it's going to basically guide you that, okay, if you are using this data set, then use this particular tool and that's where you go from. So it's really like going

### 00:44:17 · Speaker 1

to that whole business process conversation but now basically my takeaway from this podcast is that if someone is an expert at that business process they just can use ai to a significant advantage to speed up a lot of the works that traditionally used to take like months and months sometimes years to implement

### 00:44:37 · Speaker 2

I think you're 100% right. I feel that AI is a big enabler for us, for people like, like, I'd like to think that I'm a professional in supply chain, although I keep on reading new stuff, I keep the continuous improvement journey doesn't stop. So AI expedited all these ideas, all these, and also it helped me figure out new things.

### 00:45:07 · Speaker 1

I'm sure it did. Awesome. Well, I think this was a really eye-opening session for me, at least, Alan. I mean, you've just basically shown me how you have built in four weeks a tool, which is basically the demand planning module, a supply optimization module, and an SNOP module without investing millions of dollars in a tool. Now, I understand that, you know, this is more of a standalone tool and you are working on like what could be the next

### 00:45:37 · Speaker 1

part of this journey, which I totally get. But even what you have built and what you have shown us, like if I, someone told me this is going to be possible even maybe two years ago, I would never have believed that. But now we are in this world where this is actually a reality, not just an idea. So thanks for coming on the podcast. I know it's like a weekend, Alonzo. Thanks for taking the time. I'm sure this is a super educational session for any supply chain professional around the world, especially the

### 00:46:07 · Speaker 1

ones who are very passionate like myself about building their AI skills. So thanks a lot for taking the time. Any last advice you would like to give in general to anybody in the supply chain world watching this podcast, Alain, before we close?

### 00:46:20 · Speaker 2

I can think that my last message to anybody watching us I just want to say I'm not a software developer I'm just a supply chain enthusiast I brought to this work 20 years of experience I put them all in in a planning tool I did this in three four weekends sometimes from my phone

### 00:46:47 · Speaker 2

holding my kid on my other arm sometimes at night

### 00:46:54 · Speaker 2

I think the opportunities are better for these people who understand supply chain

### 00:47:02 · Speaker 2

The only skill we need to have from now on is the skill to identify problems

### 00:47:11 · Speaker 2

And solving those problems is gonna deliver value to the place we're working in.

### 00:47:18 · Speaker 2

Thank you Jamil I appreciate this conversation like always I appreciate your show and thanks a lot

### 00:47:18 · Speaker 3

Awesome thank you

