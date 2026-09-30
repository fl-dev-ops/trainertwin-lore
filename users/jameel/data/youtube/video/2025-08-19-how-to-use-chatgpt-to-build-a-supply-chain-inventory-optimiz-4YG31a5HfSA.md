---
id: 4YG31a5HfSA
title: How to Use ChatGPT to Build a Supply Chain Inventory Optimizer (Excel + Power
  Query)
date: '2025-08-19'
url: https://www.youtube.com/watch?v=4YG31a5HfSA
description: '🚀 Learn how to supercharge your Supply Chain Analytics with AI + Excel/Power
  Query!


  In this episode of the podcast, I sit down with Aaron K. Turkson, CSCP, an experienced
  Supply Chain Planning professional who has built a powerful Inventory Optimization
  Tool from scratch. Aaron walks us step‑by‑step through how he designed, refined,
  and optimized his code using ChatGPT—a brilliant example of how supply chain professionals
  can combine their domain knowledge with AI tools to drive real efficiency in planning
  and analytics.


  Whether you’re an aspiring supply planner, supply chain analyst, or operations professional
  looking to level up your Excel and Power Query skills, this episode gives you a
  practical view into how AI can be leveraged to streamline complex processes, reduce
  repetitive tasks, and enhance human decision making.


  🔑 What You’ll Learn in This Episode:

  How an Inventory Optimization Tool works in real-world supply planning


  The process of deep-diving into Excel/Power Query automations


  How Aaron used ChatGPT to optimize his Power Query/M code


  Why human intelligence and coding knowledge still matter in the age of AI


  Practical tips on upskilling with AI + spreadsheets for career growth


  🕒 Episode Timestamps:

  0:00 – Podcast Intro

  1:53 – Guest Introduction

  5:08 – Inventory Optimization Tool Overview

  8:00 – Tool Deep Dive

  20:50 – Using ChatGPT to Optimize the Code

  26:47 – The Importance of Human Intelligence

  30:21 – Why Knowing the Code Matters

  32:38 – How to Upskill on the AI + Power Query Combination


  🌍 Connect with My Guest:

  🔗 Aaron K. Turkson, CSCP on LinkedIn


  👍 Don’t forget to like, subscribe, and hit the notification bell for more expert
  interviews and career tips in supply chain, procurement, and business!


  Follow Jameel Hye on LinkedIn: https://www.linkedin.com/in/jameelhye/


  Preparing for your next supply chain interview or seeking career guidance? Let''s
  chat! Book a session with me today: https://calendly.com/jameel-hye



  🎯 Who Should Watch This Podcast?

  Supply Planners & Analysts


  Professionals in Supply Chain & Operations


  Excel & Power Query Enthusiasts


  Anyone exploring AI applications in analytics


  Students & practitioners looking to future-proof their supply chain career'
author: jameelhye
duration: 00:45:24
model: saaras:v3
transcript: true
---

# How to Use ChatGPT to Build a Supply Chain Inventory Optimizer (Excel + Power Query)

## Transcript

### 00:00:00 · Speaker 1

Warning, if you are not into supply chain planning and do not like working with numbers and spreadsheets, then this podcast will feel very boring to you. But if you like these things, especially spreadsheets for planning, then there will be some great Chad GPT tips for you with Arial Life example.

### 00:00:16 · Speaker 3

is able to account for inventory moving from one location to another location and from that location to another like the whole uh movement of inventory and it keeps track of all of that and makes sure that all the So it does

### 00:00:30 · Speaker 2

So, it does eighty percent of your work, but you still need to put that twenty percent human element. uh But it's still, you know, the fact that it's doing like earlier before AI tools were available, we had to do hundred percent of the work. Now it's doing, it's saving a lot of your time, but you still need to have that human element. Absolutely. Agreed.

### 00:00:32 · Speaker 3

Exactly

### 00:00:34 · Speaker 3

Human Element

### 00:00:42 · Speaker 3

How it's doing

### 00:00:45 · Speaker 3

But you still need

### 00:00:47 · Speaker 3

not to get too technical into the details but I was very intelligent in how I developed this uh piece of code. Combining

### 00:00:57 · Speaker 3

two, two different queries into one and making it dynamic such that the final query was just depending on the prior query to get the information. Like I said initially, like this is where you need to be able to be conversant with the software and the

### 00:01:12 · Speaker 1

Move

### 00:01:13 · Speaker 3

and the codes be able to get through it because if let's say I had zero idea about how it works, I wouldn't have been able to overcome some of some of the some of these problem too. So it's it's suggested to me based on my code alone that I need to add another query that checks for when I get negative balances, right? Because bear in mind it's an excel setup. It's it won't stop you like the way your ARP system will stop you from trying to take more than what's in the location

### 00:01:46 · Speaker 3

it was smart enough to look at my code and tell them that we need to add that to it.

### 00:01:53 · Speaker 2

Hello and welcome to another podcast on my channel Supply Chain Folks. And as you know that one of the topics I talk a lot about in this channel is how the power of AI is shaping the world of supply chain and the skill sets around it. And recently when I posted one of the clips from my podcast with Aileen Sandowal where we talked about how to build skills for AI in supply chain. uh one of my followers posted a comment that he has actually built an inventory system in Excel using AI for MDAC squares.

### 00:02:23 · Speaker 2

series and he believes that the performance and the functionality of the tool he has built is more or less the same what an SAP module would give you and I really got excited when I heard that so I invited him to this podcast and he was very kind enough to take the time out on his weekend to do this with us so I would like to introduce Aaron Truckson to you guys and Aaron is an experienced supply planning professional he has got a wealth of experience in the area of supply planning he has worked with some

### 00:02:53 · Speaker 2

big companies like Unilever and he has got his experience across Africa and now he's working in Canada and he's joining me from a very exciting place in Canada which is White Horse Yukon. So without further ado let me welcome Aaron to the podcast. Hello Aaron how are you?

### 00:03:07 · Speaker 3

Hi, hi Jamil, I'm good. How's it going?

### 00:03:10 · Speaker 2

Very good, very good, Aaron. And thanks a lot for contributing to my posts on LinkedIn and sharing your, you know, amazing tool that you have built, which I'm sure today the audience is going to take benefit from that whole thought process and how you have built it. But before we go there, Aaron, just give us a quick introduction about yourself, how did you get into supply chain, and what has been your journey and what are you doing right now?

### 00:03:34 · Speaker 3

Yeah, okay. So, um, well, I would say, uh, my supply chain journey started, uh, like back, like I'm from Ghana originally and I, I started, um, working in, uh, planning departments, initially doing import exports type of operations and I got exposed to the planning department, like the other aspect which is the material planning, supply planning and I found some way somehow found myself like getting the

### 00:04:04 · Speaker 3

opportunities to be in these roles and develop myself. So, um current I I recently just completed my master's program um here in Canada and like after that I started a job here in what brings me to Whitehouse all the way up north here in the Yukon. um working with the with the one of the Telcos up here. So, it's a bit different from my planning experience. It's now more logistics based but it's it's quite exciting to have a feel of another part of

### 00:04:34 · Speaker 3

of like the the big big supply chain field so yeah. It's given us a little bit about myself and yeah happy to to show what like what I came up with yeah.

### 00:04:45 · Speaker 2

abs excellent that that's fantastic and yeah and and once you share your your tool with us I would love to also hear from you like how are you really keeping yourself upskilled and how you're like you know blending the power of like some of these new AI tools with Excel or some of the other like standard tools we use in supply chain so I would love to also learn about that. uh but let's let's go to the tool itself Aaron and and before you start sharing your screen and and we we get into the tool itself uh just tell us a little bit about

### 00:05:15 · Speaker 2

what is the purpose of the tool what it does and then we can dive into how we have built it.

### 00:05:21 · Speaker 3

Yeah, so the tool basically is like uh for uh inventory management in sense of uh warehouse storage, um keeping track of inventory that's coming to um let's say a warehouse or multiple warehouses. So what I have here is we have I have different locations where inventory is kept. It's able to account for inventory moving from one location to another location and from that location to another like the whole um movement of inventory.

### 00:05:51 · Speaker 3

and it keeps track of all of that and makes sure that all the um I have some checks I'll go through it when we when when I when I present to make sure that it's all accurate. So yeah, I mean basically it it's it's it's I feel like it's replicating something like what an SAP model would would do because you have different plants, you have different warehouses and stuff that inventory moves around and yeah, this is what I I try to achieve with with this system. So yeah, just a simple inventory management system. So yeah.

### 00:06:24 · Speaker 2

Excellent. And and one one question out of just pure curiosity, right? Because this is I mean to be very honest like this is also one of the challenges we face in our company as well, right? That tracking inventory across multiple warehouses, what's in transit and what's not and all of that stuff. So, uh tell me a little bit about like is the tool pulling data from different sources, different systems? uh How how does the data sourcing work?

### 00:06:38 · Speaker 1

trans

### 00:06:50 · Speaker 3

So it's the two at this base and what I'm what I'll extrude to you is uh it's taken it from manual entries. So for example, um you have one person who's inputting like it's like you're doing a transaction. So you see how in SAP you go in there you are you are uh receiving inventory, you you put in your PO number if you have a PO number and all of that stuff in and you execute. We have uh I have a table for that. It's scalable to

### 00:07:20 · Speaker 3

what you are seeing where it could be pulling from different sources as well. So let's see multiple people could have different versions of the sheets we could we could set it up to link it to every single warehouse location and as everybody inputs in their like their data and information it it can be updated. It can be the locations on the inventory at the different locations could be also updated. So that's that is possible. But at this very base what I show today is is all in one sheet. So you have the

### 00:07:50 · Speaker 3

the way I put in like this your transactions and is updating it as you move the inventory along to different different places.

### 00:07:58 · Speaker 2

Awesome, awesome. Okay. All right, so let's let's dive into the tool itself. Let me just add your screen here. So over to you. You just walk us through how it's built.

### 00:07:59 · Speaker 3

Yeah

### 00:08:07 · Speaker 3

Yeah, okay. So, I would start with this screen. um So, this is more like the the validation or like uh what I was saying. Sorry, can you just zoom in a little bit?

### 00:08:17 · Speaker 2

Sorry Aaron, can you just zoom in a little bit more so that you know people can

### 00:08:20 · Speaker 3

Okay

### 00:08:22 · Speaker 2

Thank you

### 00:08:23 · Speaker 3

Is is he okay?

### 00:08:24 · Speaker 2

Yeah, this is perfect.

### 00:08:25 · Speaker 3

Okay. Okay, so I have it on another screen here so that uh so you see my head shows up a bit. So, um this is more like somewhat like my master data screen where I have the different warehouse locations. So you have warehouse two, warehouse one, plant A, warehouse three and all of that and all of the stuff and you have your customers as well. And I have this special location I call stock initial. I would explain that when I get to the full inventory view, but it's a special location because, um

### 00:09:02 · Speaker 3

every, let's say, every company or everywhere else will have some inventory will be completely zero from there from the start, right? So this is like a one-time location where that's I accounted for for that inventory. um yeah, so this is like my master data for my locations. Then I have uh another table for the status of let's say that the transaction or the inputs you are putting in the system, whether it's in transit or it's delivered, because it might it takes time from

### 00:09:32 · Speaker 3

point A to point B and and so forth. So that's also accounted for here. And we come to the movement type. So Azaria are doing a stock transfer order which is more or less the movements between the plants.

### 00:09:47 · Speaker 3

or you're doing a goods issue or a sale which you're selling to a customer and this movement that PI stands for beginning inventory that ties back to what I was referring to in the initial stock. So it's more like a one time kind of setup I have in place to account for initial inventory that the warehouses and plants will have. Then for scalability I have this table here so this is my list

### 00:10:17 · Speaker 3

say my transactions or the data I'll be inputting for the year twenty twenty five. It doesn't have to be just the year twenty twenty five but you understand that Excel has a limitations up to about a million and something rows. We can have multiple rows as much as you want but when it gets to that limit you have to create a new table and this here this setup here is to account for that limitation. So if I use up to my I don't expect us it to be used up to that one million in a very short

### 00:10:47 · Speaker 3

time but if you use up to one million the the limits of the excel sheets then we can add a new one here and move on and move for move like move forward so it is for scalability

### 00:11:00 · Speaker 3

reasons. Yeah. And let me come to the

### 00:11:06 · Speaker 3

where the data is actually inputted here. Let me zoom in again.

### 00:11:12 · Speaker 3

you have the date of the transaction, you have your movement type here. You have a unique reference that that's particular, uh let's say transactional row you are inputting will come with. I I I could we could put a a formula to generate a unique reference so that you don't need to manually input this. But this is like I said very very rudimentary and basic but like so you can improve on that. Then you have the SKU or the code in in some cases.

### 00:11:30 · Speaker 1

you don't need

### 00:11:42 · Speaker 3

You have your description in here and you input the P O number. Activity, this I just have as a miscellaneous rule. You don't need to really put in much there but it can be repurposed whatever you want it to be. You have your units of measure, you have the quantity. So now there's an important piece, where it's coming from and where it's going to. And you see here I have some drop down. I've done the data validation here so that if I'm, let's say for example, putting

### 00:12:04 · Speaker 1

and he

### 00:12:12 · Speaker 3

seeing where I was for there's nothing like where I was for it won't let me uh input that for I don't know if you have seen it on the screen but

### 00:12:20 · Speaker 2

Yeah, I can

### 00:12:21 · Speaker 3

You can see you won't let me input in the wrong warehouse. So if I know I want to add another warehouse location, I have to come into my uh master data screen and add the warehouse here. Okay. So maybe we can just test it out to just give you an idea of some of the controls we have here. So you see how warehouse four here and yeah. Now you can do it. Okay, got it. These are some of the checks and small tweaks that um have been factored into the fault management.

### 00:12:32 · Speaker 2

Okay

### 00:12:42 · Speaker 2

now you can do it. Okay, got it.

### 00:12:51 · Speaker 3

sure that like the there's integrity in their data. um yeah. So, yeah, so this covers it from their plans. Then you have the status whether it's delivered or in transit because you see here that we have the ship dates and we have the arrival dates. And we have the so so so more or less you would put in your ship dates when it ships out and this would be the same transit until it arrives there, this would remain like in transit and then again

### 00:12:55 · Speaker 1

Yeah

### 00:13:21 · Speaker 3

it's like these are these are also rooms of improvement you can I could put an automated formula that I would account for uh it's changing on its own without any human inputs, right? These are some of the benefits and stuff of AI like it can improve whatever like you you create. So this is at this very base. So yeah, this is pretty much it for the data entry aspect of the of the tool and all of it cumulates into the inventory view.

### 00:13:35 · Speaker 2

proof

### 00:13:39 · Speaker 2

So

### 00:13:51 · Speaker 3

Okay

### 00:13:52 · Speaker 3

Let me zoom in again.

### 00:13:55 · Speaker 3

So

### 00:13:57 · Speaker 3

from all the transactions that we saw from this previous page, like all of all of this uh stock that you see here. And as I mentioned, sorry to go back go back a bit, but I I mentioned to you, we I I needed to create a special location called stock initial, which is more or less the starting inventory for all the different plants per skew. So that's why I have I'll have I have all of these uh transactions in place. Then from

### 00:14:08 · Speaker 1

I am

### 00:14:27 · Speaker 3

uh let me see yeah so this is beginning inventory stock initial so from here onwards from row thirty onwards I have the STOs and sales and all of that stuff so the inventory is moving around and it's being deducted from one location added to another location moved to another location so like all of that movements happen here.

### 00:14:47 · Speaker 2

And goods issue is a is a basically when the product is getting produced. So like STO is a transfer order between two warehouses I'm assuming. And goods issue is that when the production happens or like just to understand the terminology.

### 00:15:02 · Speaker 3

Yeah, so I in so the the logic I use for this is the STUs are for

### 00:15:09 · Speaker 3

movements between plants and warehouse. So if you are moving from one plant to a warehouse, it's it's an STU. So I'm treating the plants as somewhat of a storage location as well. Oh okay, okay, got it. And yeah, if you are moving it to a warehouse, it's like an STU movement.

### 00:15:21 · Speaker 2

Okay, okay, correct.

### 00:15:28 · Speaker 3

Now the goods issue, um, um, I, the logic here is the goods issue are sales. It's been issued.

### 00:15:33 · Speaker 2

Okay, that sells out. Got it. Okay, clear.

### 00:15:35 · Speaker 3

Yeah, it goes out of the inventory, yeah. Yeah, so that's why I'm trying to say. So I'm using some of the SAP terminologies we are familiar with. I'm not sure if you are familiar with SAP, but like, yeah. Yeah, no, no, no.

### 00:15:44 · Speaker 2

Yeah, no, no, no. I just wanted to clarify that, yes.

### 00:15:46 · Speaker 3

Yeah, yeah, yeah, yeah. So it's yeah, so good SEO is movement in the plant and in the warehouse movement. GIs are sales to the customer.

### 00:15:56 · Speaker 3

Yeah. So, um yeah, so I think I just wanted to like point that out again. So that's that's why the reason we have the initial stock location, then we have the movements down from uh group thirty. So we come to the inventory view.

### 00:16:13 · Speaker 3

So with the inventory view, I have two tables. um I'll start with the the first the the table on the left. So the table on the left being powered from the queries that I I let the I I worked with the the AI to help me develop is is done all the additions and subtractions from the different plants in their warehouses and we have our our total live inventory view per location. So you see it's on a

### 00:16:35 · Speaker 2

India

### 00:16:43 · Speaker 3

SQ level um via the variant plants that are there. So you have plants A, plants B, warehouse one, warehouse two, warehouse three and you have the the stock that you would see in all these locations. So let me pick out one stock um because it's a pivot table, like it's a pivot table just to uh I forgot to add that it's a pivot table that is is doing the background calculation.

### 00:17:13 · Speaker 3

to like give us our total inventory. But I can pick out one skew and we see the transactions that went to it. So when you double click, you see the various uh movements that happened to give you that uh total amount, right?

### 00:17:30 · Speaker 2

Okay

### 00:17:30 · Speaker 3

So you see here that we had our initial stock, that's a B I. Let me zoom. I think it's a bit. Yeah. Remember I mentioned the initial stock that we had was two seven. So that was the amount of this Q that went into plant B.

### 00:17:40 · Speaker 1

Bruce

### 00:17:46 · Speaker 3

That was the initial stock. Then we had two STO movements that left that particular plant. So we had twenty-two leaving the plant and uh forty-four leaving the plant for this skill, skill one two five, right? So I just just to check to be sure I'll be on the same page. So this amounts to one sixty-one. That's what you should see on that. Yes, that's what you should see. You see you have the one sixty-one here, yeah.

### 00:18:10 · Speaker 2

That's what you should see on that. Yes, that's what you should see.

### 00:18:16 · Speaker 3

So, just to validate the information we are looking at, the is being accurate in calculating what's led to you having one hundred and sixty one of scale one to five under the plant.

### 00:18:29 · Speaker 3

Yeah, so this is a these

### 00:18:29 · Speaker 2

And how does it how is it capturing the inventory which might be in transit, right? So you ship let's say something from on a STO from one plant to the other. Is this table also showing what's in the pipeline or is it only showing on ground stock?

### 00:18:37 · Speaker 3

Hello

### 00:18:45 · Speaker 3

Yeah, so, um, that's uh let me add it to this file.

### 00:18:52 · Speaker 3

I wanted to also show that as well so it is under status. I would add the status to my filter.

### 00:19:02 · Speaker 3

is this status yeah. Get out the status here. Yeah so currently we are seeing every is all everything is more or less delivered right? But we could change

### 00:19:10 · Speaker 2

but

### 00:19:13 · Speaker 3

let's say we could change one of these transactions to um in transit, right? So I'll run this in transit. I would come back into my inventory view. And and there's another thing with power query and uh the queries are you have to always refresh your

### 00:19:20 · Speaker 2

right?

### 00:19:34 · Speaker 3

Yeah, of course. Yeah, you'll see the otherwise you'll see the live. So now we would see if we want to have a view of what is in transit, we could filter it out there and you would see

### 00:19:34 · Speaker 2

Yeah, of course.

### 00:19:48 · Speaker 3

that's uh S K U two T one is in transit to plant no it's being is leaving plant B and is on its way to uh warehouse. Yeah. So you have a view of that. So if you wanted to see oh you're in transit view stock movement you just uh filter this out you see everything. But the good thing is that it doesn't affect what is uh delivered because what is delivered has actually happened.

### 00:19:59 · Speaker 2

And

### 00:20:02 · Speaker 2

Well,

### 00:20:18 · Speaker 3

left one warehouse location and landed onto the the the the next warehouse destined for. So he's able to separate uh these these two things.

### 00:20:32 · Speaker 2

Excellent, excellent. So, so, so far what you have shown us and is like, you know, really like the core of Power Query, right? So how you have built this, right? Now, can you just show us a little bit more about how you use Chat GPT to facilitate some of this work?

### 00:20:38 · Speaker 3

field

### 00:20:48 · Speaker 3

Okay, let me know if we can see it now.

### 00:20:50 · Speaker 2

Yep, it came up.

### 00:20:52 · Speaker 3

Okay, so this so I will just go to some of the the conversations with I had with Chat GPT to come up with this stuff. So I started with telling them like I always thought that I can object to for why I'm having their conversation. So you see I want to work with you, we're refining a power query I created. I'm referencing to logic I got from you. And not sure if you remember and I also put in there I don't want it to use a higher level of GPT because I'm using a free version.

### 00:20:59 · Speaker 2

Hmm

### 00:21:22 · Speaker 2

Yes

### 00:21:22 · Speaker 3

Yes. When you when when you use a chat GPT at a higher level, it sort of cuts out in the middle. So like I was very specific to let it keep to the base model that I think was very sufficient for what I wanted to use it for. So, I sent this message to chat GPT.

### 00:21:41 · Speaker 3

It said it doesn't remember, which was a good thing for me. And I was happy it said it couldn't remember because I will take us through how I I modeled, I sort of communicated what I had and how where I wanted to go with it. So, it's asked me to share my query, which was just perfect. So I said, I have three queries that I'll share the code for each. So I took the query code. I had three queries I was working with. I had a master table query that I had.

### 00:22:03 · Speaker 2

So I

### 00:22:11 · Speaker 3

I shared that like uh I shared that code with with with Jachi BT and there's a picture of it because because M M is uh Power Query uses the M code which is slightly different from DAX you get to see the actual raw coding behind the the query that goes into like transforming the data so it's you are able to really communicate well with the with the AI to let it picture well what you are trying to like trying to achieve. So that's what we did here.

### 00:22:39 · Speaker 1

is

### 00:22:41 · Speaker 3

I put in the three different codes and three different query codes in there. The master table query. So I had a master table to, master table from, and I had a master table query without any funny name with it. Yeah, so these are the three codes I put there.

### 00:22:59 · Speaker 3

So, the two just responded. I mean, GPT just came and said, okay, I see the pattern there. This is what I've done. And this what's the code, how he understands the code, right? Just going through it quickly to to show you the conversation, but it's it only told me how what he understands for my code.

### 00:23:22 · Speaker 3

And it was something interesting happened there when I shared initially. So what I've even seen from my father's a refined version of my conversation here because it told me a repeated code, right? Mm-hmm. And it said that it could do it better by reducing the queries to one parameterized function or whatever. From just looking at the the code that you shared with it. And it said that if I wanted we could refactor this code into just two queries. So I had three queries to get to where I wanted to go to instead we could do it in two.

### 00:23:33 · Speaker 1

hmm

### 00:23:52 · Speaker 3

I said if I want we could just do it into two queries. I said I think I came back here and I said okay. But I also gave it another data point. So I copied my row columns, right? Remember the where we input the transactions for the movements and stuff. That's a very important piece of it. So I copied that and I shared it with uh Chat GPT. So it now understands what the query is doing. It also understands the source data table or the structure of the source

### 00:24:08 · Speaker 1

um

### 00:24:22 · Speaker 3

data that is going to be worked with and that's also very important to to add there. So given this both of this information to Chat GPT it's it has a whole idea of the the entire program you have in the query program you have in Excel and the conversation gets more let's say interactive and more refined in what you want to do. So

### 00:24:47 · Speaker 3

I sent that information to Chat GPT, it's got it and broke it down perfectly how how it is in my Excel file.

### 00:24:58 · Speaker 2

hmm

### 00:24:59 · Speaker 3

then it it gave me a couple of steps of what we can do to improve the queries that we have. And that's what I've been asked yesterday, you can basically improve what I've done.

### 00:25:13 · Speaker 3

And he said, yes, you can definitely improve over there without changing the logic you have already built, which is just beautiful, right? So, he gave me, I I said, okay, let's try and see what you want to do. So this is where Chat GPT comes in with a code. It's created this code for me based on all the information that we have we have had per, given it what my query code was, telling it the structure of my table, now comes to the output from from Chat. PT

### 00:25:44 · Speaker 2

So it is processed all our conversation even on our parameters and now it's giving you a customized code for your so you can literally you can literally copy this and paste it. Okay yes paste it yeah. Yeah that's it.

### 00:25:44 · Speaker 3

it is

### 00:25:47 · Speaker 3

even on your

### 00:25:49 · Speaker 3

cough

### 00:25:50 · Speaker 3

So you can literally

### 00:25:53 · Speaker 3

paste it, paste it, yeah. Yeah, that's it. Yeah.

### 00:25:57 · Speaker 2

I

### 00:25:58 · Speaker 3

So, perfect. It created this fun master table code for me. I just took it out and put it into my Empower query. And most often they're not, so I'll just add a bit here. Most often they're not, the code works perfect, but you have some errors and bugs that you have to kind of figure out. And and I believe that's where you as a person can't hundred percent depend on AI because you have to be

### 00:26:20 · Speaker 2

and

### 00:26:28 · Speaker 3

coherence with the the query or the the query code in order to find where the problems are or find what is is uh causing the error or it's not being able to run. So that's why I believe and I've been looking at your conversation you had previously on the AI. That's where like the human aspect comes in because it's it's it enables you to be able to do some of these things but you yourself need to have an idea of how like the software works or or the code works

### 00:26:47 · Speaker 2

Absolutely

### 00:26:58 · Speaker 3

and to be able to like to guide it to where you want it to go. So like that's that's really I I guess I'll say that this is an important piece in the evolution of AI and especially not just for supply chain just like for everybody else because you need to be I don't think where it is today personally is at a level where you can hundred percent depend on it. It's it's it's still very powerful but it needs the the guidance. So

### 00:27:23 · Speaker 2

Yeah, I think yeah, I mean and that's so true, Aaron, right? Because that's also my experience. I mean, I don't write this level of code that you are writing on Excel, which is fantastic. But even like I use AI all the time for content creation and all of that. So it does eighty percent of your work, but you still need to put that twenty percent human element. uh But it's still, you know, the fact that it's doing like earlier before AI tools were available, we had to do hundred percent of the work. Now it's doing saving a lot of your time, but you still need to have that human element.

### 00:27:35 · Speaker 3

content

### 00:27:39 · Speaker 1

put that 20% human element

### 00:27:49 · Speaker 3

Exactly

### 00:27:51 · Speaker 3

But you still need

### 00:27:53 · Speaker 2

Absolutely. Agreed.

### 00:27:54 · Speaker 3

Yeah. Yeah. So it's more or less gave me so like yeah I was saying it more or less gave me the the code that I could I could create. And so it was two pieces of code two queries yeah it created one query and another query and it's it combined it in in a in a certain way so.

### 00:28:14 · Speaker 3

not to get too technical into the details but I was very intelligent in how I developed this piece of code. Combining

### 00:28:25 · Speaker 3

two, two different queries into one and making it dynamic such that the final query was just depending on the prior query to get the information. So...

### 00:28:35 · Speaker 2

current

### 00:28:36 · Speaker 3

I don't know if I'm and explain as well but like it's, So basically you're

### 00:28:39 · Speaker 2

So basically you're saying it optimized the query uh quite smartly so what you thought were two separate queries it actually collapsed it into one so made the code very efficient basically.

### 00:28:42 · Speaker 3

Yeah

### 00:28:47 · Speaker 3

into

### 00:28:48 · Speaker 3

So, mainly

### 00:28:50 · Speaker 3

Yeah. So so maybe to give a basic example, right? You had maybe you had two excel uh uh formulas and is instead of you instead of you having two excel formulas, let's say you combine it into one. That that's the longest shot of it, yeah. Yeah. Yeah. Yeah. You don't need to have

### 00:29:08 · Speaker 2

Yeah, yeah, yeah. And we don't need to have, you know, there are so many examples I can think of, you know, you I I remember I used when back in like early days, I used to write like a V lookup, H lookup combination formula, but then like Excel brought in new formulas that you don't need to write that long of like I I remember writing like seven line formulas in Excel at one point in time. Now you can do it with like, you know, couple of lines, but now this is like the next level. You don't even need to write those couple of lines, you can use chat, GBT,

### 00:29:20 · Speaker 1

Yeah

### 00:29:21 · Speaker 3

format

### 00:29:22 · Speaker 1

but then like

### 00:29:25 · Speaker 1

to

### 00:29:27 · Speaker 1

Hello

### 00:29:30 · Speaker 3

Hello

### 00:29:33 · Speaker 3

this is

### 00:29:35 · Speaker 3

don't even

### 00:29:38 · Speaker 2

do it for you and then you just refine and make sure that your parameters are customized and that's it.

### 00:29:39 · Speaker 3

and then

### 00:29:42 · Speaker 3

customize yeah

### 00:29:44 · Speaker 2

So so you you then just you just took copied this code and pasted it on Power Query, Aaron?

### 00:29:50 · Speaker 3

Yeah. So I copied it and put it on a par query and and also to also point out uh it was kind of new to me the the technique used to create this query, right? So you can see here I asked it what what do you enter for the parameter? It was a whole different view. I didn't get what it was saying. Then it breaks it down to me to tell me what exactly it's trying to achieve, right? Yeah, so this is where I talk about being conscious of with the with the code, right? So

### 00:30:20 · Speaker 3

I get this error and and normally I put in the errors into Chat GPT to tell it that I'm getting this specific error like what what does it mean. Sometimes I'm not being I'm not able to figure out why so I I would go back and take a snapshot of it or take a text of it and and and tell it and through Chat GPT then it will explain to me why what the error is and give me some solutions right.

### 00:30:46 · Speaker 3

It gives me a quick fix. I tried a quick fix, it still doesn't work. So what I then do is I get my own fix and put it in there and I come back and tell her that hey, what you told me didn't work but this is what I did. I so so it was a naming problem like you know you can't have the same exact name with your work in Excel, you can't have the exact name in your worksheets right? If you have worksheets A, you also can't have another worksheets A in it. So that was an error that I was was getting but I was on a query level.

### 00:30:54 · Speaker 2

Mm-hmm

### 00:31:16 · Speaker 3

it was it was saying I was replicating, reusing the same name twice where I shouldn't be. So I just added a one, the number one to um the the where I was getting the error from more or less. And I came back and told that like this is what I did and it worked. And it's what did it say? Is there something interesting on that journey with the one?

### 00:31:21 · Speaker 2

students

### 00:31:25 · Speaker 2

the number

### 00:31:32 · Speaker 1

packing

### 00:31:43 · Speaker 3

I just added a number one. It said that works too, yeah. And your function query is called function master table one and as long as you have this blah blah blah. So, so it sort of solved the problem and I said initially like this is where you need to be able to be conversant with the software and the and the code to be able to get through it because if let's say I had zero idea about how it works, I wouldn't have been able to overcome some of some of the some of these problems. So,

### 00:31:58 · Speaker 1

Hmm

### 00:32:13 · Speaker 3

so this basically the not to go through the entire conversation but this basically how I communicate with the Chat GPT to achieve what I want to do with my with my code. Right? And and sometimes it will give me suggestions. So there was one last piece in the Excel file I didn't show. It's it suggested to me based on my code alone that I need to add another query that checks for when I get negative balances, right? Because bear in mind there's an Excel

### 00:32:24 · Speaker 2

Excellent

### 00:32:43 · Speaker 3

setup. It's it won't stop you like the way your ARP system will stop you from trying to take more than what's in a location.

### 00:32:51 · Speaker 3

But with this, with Excel, there's nothing like some internal tool that will stop that. Maybe not that I know of yet, but it was smart enough to look at my code and tell me that we need to add that to it. So, it's you would see there there's another part of it I didn't show, but maybe I'll get there a bit later. But it's it's recommended a a whole new idea, a whole new query to check for these things.

### 00:33:03 · Speaker 1

So

### 00:33:17 · Speaker 2

Okay

### 00:33:18 · Speaker 3

Right. And it helped me develop that query as well in inputs in it. So this is how powerful it it's it's can become. It can

### 00:33:25 · Speaker 2

So this can this is this is really becoming your coding assistant, right? It's like giving you everything and you just need to know the business problem you are solving. So and in this case you showed us a very good like live example where you were trying to create this inventory visibility system, let's call it you know or set of spreadsheets and data is coming from different sources, some of the data is manually entered but using this query you

### 00:33:32 · Speaker 3

and

### 00:33:36 · Speaker 3

So

### 00:33:46 · Speaker 3

Yeah

### 00:33:53 · Speaker 3

Yeah

### 00:33:55 · Speaker 2

made it smart enough that, you know, it's it's basically wiring all the data properly.

### 00:34:00 · Speaker 3

And you see the stock initial here, just to point it out to you, it's all negative because that's where the starting point of the inventory, but I I just I'll just I could hide it here or I could hide it on the query level, but uh just to show you what it looks like. So we are back to seeing the view the plants and the integrity check is here.

### 00:34:12 · Speaker 1

uhm

### 00:34:23 · Speaker 3

So, it's it's a two way is a there are two separate queries, but they all achieve the same thing. So this is actually uh what I came up with to check if there will be negative balances. And as to be honest, that was originally on Chat GPT's suggestion.

### 00:34:31 · Speaker 2

this

### 00:34:43 · Speaker 3

in my second conversation in my in my conversation with uh Chat GPT, I gave it this particular code that I had done and he said we could do it better. So just to go back to the point of what I was saying about uh checking for negative balances. It improved on itself more or less. This was what it gave me the very uh the first time that I I ran through this uh this system and going through it again with Chat GPT said okay actually we can

### 00:34:54 · Speaker 2

Mm-hmm

### 00:35:13 · Speaker 3

do it better than this. So I would let's do a life example, right? I would want to create a negative

### 00:35:20 · Speaker 3

stock balance for a particular plan. So let's see this one like this. I'll just put some crazy number there. I know it won't have that amount. Can you see my screen?

### 00:35:31 · Speaker 2

Yeah, I can.

### 00:35:33 · Speaker 3

Yeah, so that's S P A six four. uh for plant A. I'm taking six hundred out. I know definitely it doesn't have that amount in there and I'm moving it to warehouse two. Right?

### 00:35:46 · Speaker 3

So, I'll run the query again and let's see. We should see a negative balance for one. Yeah.

### 00:35:55 · Speaker 2

Yeah, there you go. Eight sixty four is negative.

### 00:35:56 · Speaker 3

I think

### 00:35:58 · Speaker 3

so negative yeah so it pops out right at you. Now my data integrity check also tell me that I have negative stock on plant A. which is which is where we did the the change on right?

### 00:36:07 · Speaker 2

which is

### 00:36:13 · Speaker 3

What's what's this? So let let's go through. So let me click it to tell me what happened. So it's to tell me that this particular S K U on plant A has your negative minus three six six. This this just tells me that I have a negative balance on the plant. It doesn't tell me when that happened, right? And the second query that Chatify suggested was showing me when exactly I made a mistake.

### 00:36:39 · Speaker 2

Wow, okay. So show us that. That's fantastic.

### 00:36:40 · Speaker 3

show us that

### 00:36:43 · Speaker 3

Yeah, so I'll come in. Oh, I've already loaded. I didn't want it to load automatically, but let me clear it out here.

### 00:36:50 · Speaker 3

So this table is more or less like a replication of all our transactions. So every single time we put in information in our main like the main sheets, it does a check here. Every single one is, you can see that every single one is okay apart from the one, right? This negative stock. So if I just filter out here for negative stock, I'll see that that is the plant A that we are referring to, right?

### 00:37:08 · Speaker 2

Okay

### 00:37:12 · Speaker 2

Yeah

### 00:37:20 · Speaker 2

Correct

### 00:37:20 · Speaker 3

So this is the line I

### 00:37:23 · Speaker 2

somebody somebody messes around with the data you can easily go and

### 00:37:27 · Speaker 3

is we go back and find clear

### 00:37:28 · Speaker 1

Yeah

### 00:37:29 · Speaker 2

So this could be a great tool for like inventory reconciliation as well, right? When you are reconciling different systems, which is another common industry problem, right? So

### 00:37:29 · Speaker 3

could be a great

### 00:37:32 · Speaker 3

direct

### 00:37:34 · Speaker 3

because another common

### 00:37:37 · Speaker 3

Yeah.

### 00:37:38 · Speaker 2

Okay

### 00:37:39 · Speaker 3

Yeah. So to point out exactly where you made a mistake and you it you know the reference. So this will just show you that this particular line you put in there is wrong. So you could go and take the reference number and coming back here.

### 00:38:00 · Speaker 3

Yeah. So this was where we made a change, you remember. Oh, six hundred, yeah. So you have a whole setup to kind of go back and find where he made mistakes in terms of like the the movements around and figure it out. Otherwise, you'd have to now go through a tall list of transactions and see do some small analysis, see where the mistakes come from. But with this, it's it's all more or less to meet it. So, yeah.

### 00:38:28 · Speaker 2

Oh, this is fantastic. So, just maybe, uh, thanks again for sharing this, Aaron. And for the benefit of the audience, um, if someone wants to really in the supply chain space, wants to like blend this AI tools with the existing tools, um, how did you have the initiative to learn this? Uh, was it just your inquisitiveness you were trying to find out stuff on Chat GPT or is there any other route you would recommend to people who are

### 00:38:55 · Speaker 3

the

### 00:38:58 · Speaker 2

watching this podcast.

### 00:39:00 · Speaker 3

Well, um, personally I I I had gotten to using AI like uh I think maybe two years ago, give or take, and I was using it for very rudimentary things like maybe for example a very long text you want to summarize and that basis of and it just okay to me like okay if they say you can ask such things literally anything and I started playing around inputting like asking it like opinions then

### 00:39:30 · Speaker 3

got to actual Excel problems. I sort of go solve my Excel problems. Like the formulas that you're seeing, I had like three or four back in the past. I'll say this is my formula, how can we make it better? It'll give me something and I'm like, okay. So it's it's more of like a built on experiences I've had with it too and I keep pushing it to see how far I can go with the its usefulness. And like what I just what we just went through another conversation with the with the with charging

### 00:40:00 · Speaker 3

it's it's really boils down to how well you can communicate what you have and what you want to achieve. So for example, I wanted to build an inventory management tool. I had something ongoing from my knowledge of power query. I and and and I'll say this like it understands code best. If you give the these tools like programming code, it's not just M or DAX C++ or whatever.

### 00:40:21 · Speaker 2

If

### 00:40:30 · Speaker 3

code you want to use. It understands it very, very well. So I would suggest if you're using Excel, you have some problem, you want to optimize, copy the code and put it in. Tell it that these are the the columns in my table that I'm working with and this the formula I have, but this is what I want to do. That will be like an example of how to use it in your everyday supply chain um life. If you want to create a tool like this, you need to get a bit confidence with the code a bit. You don't need to be an expert.

### 00:41:00 · Speaker 3

I'm not an expert in the DAX or or or M, but I've used it well enough to be able to understand how the code works and how it flows, because a lot of you I'll say that a lot of the code language is very similar to basic English. You're able to tell summarize, filter, you see all of those small small codes inside these these languages that you can make sense of, right? And yeah, so as much as you're dependent on it, when you

### 00:41:30 · Speaker 3

the outputs, learn what it's trying to do, try and understand the logic behind what you get back from your AI, because that's the only way you can guide it to improve onto what you want to like achieve, so yeah.

### 00:41:44 · Speaker 2

So build build the basic basic uh I would say what is the right word I'm just skipping my mind. You you should be basically like understand the fundamentals of the coding language so that then you can use AI to its to your advantage. And AI does like eighty percent of the work and then you just refine it and and fix it. Last question uh Aaron is I mean Microsoft is trying to do a lot of this with Copilot as well, right? But I've tried it once.

### 00:41:53 · Speaker 3

BPS

### 00:41:56 · Speaker 3

language

### 00:42:01 · Speaker 3

I think she

### 00:42:04 · Speaker 3

Right

### 00:42:05 · Speaker 3

last

### 00:42:12 · Speaker 1

but

### 00:42:12 · Speaker 3

I have

### 00:42:14 · Speaker 2

uh maybe I've not tried enough like I was not very impressed or maybe you know they still need to improve the code itself because what you are doing is you're taking all like you're doing all the AI work in chat GPT and then bring it back to Excel. Any any perspective on uh because maybe in the next couple of years you'll be able to do it within the Excel environment itself using Copilot as well. So any any perspective on that?

### 00:42:18 · Speaker 1

in the

### 00:42:26 · Speaker 3

um

### 00:42:35 · Speaker 3

environment itself using

### 00:42:39 · Speaker 3

Yeah, um I I I think it would I I hope that it does get to that level of integration between the AI like Copilot, of course it's Microsoft and and Excel and their whole suite of programs, especially we have Power BI too there that's also quite uh powerful, but I would my only concern with that direction is the that space of the human intelligence playing into it because

### 00:43:09 · Speaker 3

can only be as useful as what you want it to be, right? And I'm just interested to see how that integration will happen, how it will be set up in such a way that you can still guide the AI to achieving what you want it to do, not basically do what it thinks is best, because it's not necessarily what the AI comes out with that is the most like refined or best output of what you want to achieve, right? You

### 00:43:39 · Speaker 3

you've asked I we are we have different professionals like the finance person might look at this and want to work it in such a way that it suits them right and a supply chain person will look at it in such a way that want to develop it to look out for these parameters or these tools and come up with an output that's mix that that's useful information for me so I I I do hope that there's that's allowance for the human intelligence aspect of it and hopefully

### 00:43:48 · Speaker 1

and

### 00:44:09 · Speaker 3

I would wanted to to get to that level of integration so yeah. hoping that we get there in the next couple of years especially with Copilot because Microsoft Office is one of the most used softwares and organizations too so it's it's quite important that you get it right and I think Chat GPT is integrated into Copilot company

### 00:44:32 · Speaker 2

Yeah, so of course they are using their own LLM. I mean I'm not an expert. LLM, yeah, yeah. Absolutely. Great. Well, I mean this was very educational personally for me and very useful and I think I really loved the part where you just showed how you are using AI to optimize the code for for for your power queries and then you know putting it in the context of a real life supply chain example is always very powerful. Thanks a lot for your time again. Thanks a lot for taking the time.

### 00:44:32 · Speaker 3

Of course

### 00:44:35 · Speaker 3

Yeah, yeah.

### 00:45:01 · Speaker 1

Right

### 00:45:02 · Speaker 2

on the on a weekend to do this. uh So really really appreciate your uh your willingness to come and show uh us the tool and hopefully you know we'll stay in touch and you know as you do more of this fantastic stuff with AI I may invite you once more to the podcast another day.

### 00:45:17 · Speaker 3

Yeah, sorry, yeah. Thank you for having me too, Jamil, yeah.

### 00:45:21 · Speaker 2

Absolutely. All right, thank you.

### 00:45:22 · Speaker 3

Thanks. Bye.

### 00:45:24 · Speaker 2

Bye
