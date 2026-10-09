---
id: 4YG31a5HfSA
title: How to Use ChatGPT to Build a Supply Chain Inventory Optimizer (Excel + Power
  Query)
url: https://www.youtube.com/watch?v=4YG31a5HfSA
date: '2025-08-19'
duration: 00:45:24
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# How to Use ChatGPT to Build a Supply Chain Inventory Optimizer (Excel + Power Query)


## Transcript

### 00:00:00 · Speaker 1

Warning, if you are not into supply chain planning and do not like working with numbers and spreadsheets then this podcast will feel very boring to you. But if you like these things especially spreadsheets for planning then there will be some great Chad GPT tips for you with Ariel Life example.

### 00:00:16 · Speaker 2

is able to account for inventory moving from one location to another location and from that location to another like the whole movement of inventory and it keeps track of all of that and makes sure that all the so it does

### 00:00:30 · Speaker 3

So it does 80% of your work, but you still need to put in that 20% human element. But it's still, you know, the fact that it's doing like earlier, before AI tools were available, we had to do 100% of the work. Now it's doing exactly the same, saving a lot of your time.

### 00:00:33 · Speaker 2

Yeah

### 00:00:45 · Speaker 3

You still need to have that human element absolutely agreed

### 00:00:47 · Speaker 2

Not to get too technical into the details but I was very intelligent in how I developed this piece of code combining

### 00:00:57 · Speaker 2

two two different queries into one and making it dynamic such that the final query was just depending on the prior query to get the information like i said initially like this is where you need to be able to be conversant with the software and the and the code to be able to get through it because if let's say i had zero idea about how it works i wouldn't have been able to overcome some of some of the some of these uh problems so it's it's

### 00:01:27 · Speaker 2

to me based on my code alone that I need to add another query that checks for when I get negative balances right because bear in mind is an excel um setup it's it won't stop you like the way your arp system will stop you from trying to take more than what's in the location

### 00:01:46 · Speaker 2

It was smart enough to look at my code and tell me that you need to add that to it

### 00:01:53 · Speaker 3

Hello and welcome to another podcast on my channel, Supply Chain Folks. And as you know that one of the topics I talk a lot about in this channel is how the power of AI is shaping the world of supply chain and the skill sets around it. And recently when I posted one of the clips from my podcast with Aileen Sandoval where we talked about how to build skills for AI in supply chain, one of my followers posted a comment that he has actually built an inventory system in Excel using AI for MDAC.

### 00:02:23 · Speaker 3

And he believes that the performance and the functionality of the tool he has built is more or less the same what an SAP module would give you. And I really got excited when I heard that. So I invited him to this podcast and he was very kind enough to take the time out on his weekend to do this with us. So I would like to introduce Aaron Turksen. uh to you guys and aaron is an experienced supply planning professional he has got a wealth of experience in uh the area of supply planning he has worked with some big

### 00:02:53 · Speaker 3

companies like Unilever and he has got his experience across Africa and now he's working in Canada and he's joining me from a very exciting place in Canada which is Whitehorse Yukon. So without further ado let me welcome Aaron to the podcast. Hello Aaron how are you?

### 00:03:07 · Speaker 2

Hi, hi Jemil, I'm good, how's it going?

### 00:03:10 · Speaker 3

Very good, very good, Aaron. And thanks a lot for contributing to my posts on LinkedIn and sharing your amazing tool that you have built, which I'm sure today the audience is going to take benefit from that whole thought process and how you have built it. But before we go there, Aaron, just give us a quick introduction about yourself. How did you get into supply chain and what has been your journey and what are you doing right now?

### 00:03:34 · Speaker 2

Yeah okay so um well I would say uh my supply chain journey started uh like back I come I'm from Ghana originally and I I started um working in uh planning departments initially doing imports exports type of operations and I got exposed to the planning department like the other aspect which is the material planning supply planning and I found some way somehow found myself like getting the opportunity

### 00:04:04 · Speaker 2

to be in these roles and develop myself so um current i i recently just completed my master's program um here in canada and like after that i started a job here and what brings me to whitehouse all the way up north here in the yukon um working with the with the one of the telcos and up here so it's a bit different from my planning experience it's now more logistics based but it's it's quite uh exciting to have a feel of another part of

### 00:04:34 · Speaker 2

like the big big supply chain field so yeah it's a little bit about myself and yeah happy to to show what's like what I came up with yeah

### 00:04:45 · Speaker 3

abs excellent that that's fantastic and yeah and then once you share your your tool with us i would love to also hear from you like how are you really keeping yourself up to date and how you're like you know blending the power of like some of these new ai tools with excel or some of the other like standard tools we use in supply chain so i would love to also learn about that uh but let's uh let's go to the tool itself aaron and before you start sharing your screen and and we get into the tool itself uh just tell us a little bit about like

### 00:05:15 · Speaker 3

what is the purpose of the tool what it does and then we can dive into how we have built it

### 00:05:21 · Speaker 2

Yeah, so the tool basically is like for inventory management in sense of warehouse storage, keeping track of inventory that's coming to, let's say, your warehouse or multiple warehouses. So what I have here is we have I have different locations where inventory is kept. It's able to account for inventory moving from one location to another location and from that location to another, like the whole movement of inventory.

### 00:05:51 · Speaker 2

and it keeps track of all of that and makes sure that all the um i have some checks that i'll go through it when we when when i present to make sure that it's all accurate so yeah i mean basically it's it's it's i feel like it's replicating something like what an sap sap model would do because you have different plants you have different warehouses and stuff that inventory moves around and yeah this is what i i try to achieve with with this system so yeah just a simple inventory

### 00:06:21 · Speaker 2

management system. So yeah.

### 00:06:24 · Speaker 3

Excellent. And one question out of just pure curiosity, right? Because this is, I mean, to be very honest, like this is also one of the challenges we face in our company as well, right? That tracking inventory across multiple warehouses, what's in transit and what's not, and all of that stuff. So tell me a little bit about like, is the tool pulling data from different sources, different systems? How does the data sourcing work?

### 00:06:50 · Speaker 2

so it's the tool at this base and what i'm what i'll show you to you is uh it's taken it from manual entries so for example um you have one person who's inputting like it's like they're doing a transaction so you see how in sap you go in there and you are you are uh receiving inventory you you put in your po number if you have a po number and all of that stuff in and you execute we have a i have a table for that it's scalable to

### 00:07:20 · Speaker 2

what you are seeing where it could be pulling from different sources as well so let's see if multiple google could have different uh versions of the sheets we could we could set it up to link it to every single warehouse location and as everybody inputs in their like their data and information it can be updated it can be the locations on the inventory at the different locations could be also updated so that's that is possible but at this very base what i show today is uh it's all in one sheet so you have the

### 00:07:50 · Speaker 2

the way you're putting like this in your transactions and is updating it as you move the inventory along to different different places

### 00:07:58 · Speaker 3

Awesome, awesome. Okay. All right. So let's, let's dive into the tool itself. Let me just add your screen here. So over to you. You just walk us through how it's built.

### 00:08:07 · Speaker 2

Yeah, okay, so I would start with this screen. So this is more like the validation or like what I'll say.

### 00:08:17 · Speaker 3

Sorry Aaron can you just zoom in a little bit more so that you know people can see that yeah

### 00:08:20 · Speaker 2

So we love that

### 00:08:23 · Speaker 2

Is it is he okay

### 00:08:24 · Speaker 3

Yeah that's perfect

### 00:08:25 · Speaker 2

Okay, okay, so I have it on another screen here so that you can see my head tools are perfect. So this is more like somewhat like my master data screen where I have the different warehouse locations. So you have warehouse two, warehouse one, plant A, warehouse three, and all of this and all of this stuff. And you have your customers as well. And I have this special location I call stock initial.

### 00:08:55 · Speaker 2

I would explain that when I get to the full inventory view but it's a special location because

### 00:09:02 · Speaker 2

Every, let's say, every company everywhere else will have some inventory, will be completely zero from there, from the start, right? So this is like a one-time location where that's I accounted for, for, for that inventory.

### 00:09:16 · Speaker 2

Yeah, so this is like my master data for my locations. Then I have another table for the status of, let's say, the transaction or the input you are putting in the system, whether it's in transit or it's delivered, because it might take time from point A to point B and so forth. So that's also accounted for here. And we come to the movement type. So as I already did in a stock transfer order, which is more or less the movements between the,

### 00:09:46 · Speaker 2

plants or you're doing a goose issue or a sale which you're selling to a customer and this movement that bi stands for beginning inventory that ties back to what i was referring to in the initial stock so it's more like a one-time kind of um setup i have in place to account for initial inventory that the warehouses and plants will have then for scalability i have this table um here so this is

### 00:10:16 · Speaker 2

my let's say my transactions or the data I'll be inputting for the year 2025 it doesn't have to be just the year 2025 but you understand that Excel has a limitations up to about a million and something rules we can have multiple rules as much as you want but when you get to that limit you have to create a new table and this here this setup here is to account for that limitation so if I use up to my I don't expect us it to be used up to

### 00:10:46 · Speaker 2

one million in a very short time but if you use up to one million the the limit of the excel sheets then we can add a new one here and move on and move for move like move forward so this is for scalability

### 00:11:00 · Speaker 2

Reasons, yeah, and let me come to the

### 00:11:06 · Speaker 2

where the data is actually imported here let me zoom in again

### 00:11:12 · Speaker 2

you have the date of the transaction you have your movement type here you have a unique reference that that particular uh let's see transactional row you're inputting will come with i i could we could put a a formula to generate a unique reference so that you don't need to manually input this but this like i said very very rudimentary and basic but like so you can improve on that then you have the sku or the code in in some cases

### 00:11:42 · Speaker 2

You have your description in here and you input the PO number Activity this I just have as a miscellaneous rule, but you don't need to really put in much there But it can be repurposed whatever you want it to be you have your unit of measure you have the quantity So now there's an important piece where it's coming from and where it's going to and you see here I have some drop down I've done the data validation here so that if I'm let's say for example putting

### 00:12:12 · Speaker 2

warehouse for there's nothing like warehouse for it won't let me uh input that for i don't know if you have seen it on the screen but

### 00:12:20 · Speaker 3

Yeah I can

### 00:12:21 · Speaker 2

you can see you won't let me input in the wrong warehouse so if i knew i want to add another warehouse location i have to come into my master data screen and add the warehouse here

### 00:12:32 · Speaker 2

Maybe you can just test it out to just give you an idea of some of the controls we have here so you see how well it's for here and yeah

### 00:12:32 · Speaker 3

Okay

### 00:12:42 · Speaker 3

Now you can do it okay get it

### 00:12:44 · Speaker 2

These are some of the checks and small tweaks that

### 00:12:49 · Speaker 2

been factored into the file to make sure that like the there's integrity in the data um yeah so yeah so this covers it from the plants then you have the status whether it's uh delivered or in transit because you'd see here that we have the ship dates and we have the arrival dates and we have the so so so more or less you would put in your ship dates when it ships out and this would be let's say in transit until it arrives there this would uh remain

### 00:13:19 · Speaker 2

Like in transit and then again to like these are these are also rooms for improvements you can I could put an automated formula there that would account for It's changing on its own without any human input, right? These are some of the benefits and stuff of AI like it can improve Whatever like you you create so this is at this very base So yeah, this is pretty much it for the data entry aspect of the of the tool and all of it could

### 00:13:49 · Speaker 2

into the inventory view here

### 00:13:52 · Speaker 2

Let me zoom in again

### 00:13:55 · Speaker 2

So

### 00:13:57 · Speaker 2

from all the transactions that we saw from this previous page, like all of this stock that you see here. And as I mentioned, sorry to go back a bit, but I mentioned to you, I needed to create a special location called stock initial, which is more or less the starting inventory for all the different plants per SKU. So that's why I have all of these transactions in place. Then from

### 00:14:28 · Speaker 2

Let me see. Yeah, so this is beginning inventory, the stock initial. So from here onwards, from row 30 onwards, I have the STOs and sales and all of that stuff. So the inventory is moving around and it's being deducted from one location, added to another location, moved to another location, sold, like all of that movements happen here.

### 00:14:47 · Speaker 3

goods issue is a is basically when the product is getting produced so like sto is a transfer order between two warehouses i'm assuming and goods issue is that when the production happens or like just to understand the terminology

### 00:15:02 · Speaker 2

Yeah, so I in so the the logic I use for this is the STOs are for movements between plants and warehouse. So if you're moving from one plant to a warehouse, it's an STO. So I'm treating the plants as somewhat of a storage location as well. Oh, okay. Yeah. If you're moving it to a warehouse, it's like an STO movement. Now the good issue I mean, I the logic here

### 00:15:32 · Speaker 2

There's a goose issue as well

### 00:15:33 · Speaker 3

Oh me, that fails out, got it, okay, clear.

### 00:15:35 · Speaker 2

Yeah yeah so that's why I'm using so I'm using some of the SAP technologies we are familiar with I'm not sure if you are familiar with SAP but like yeah

### 00:15:44 · Speaker 3

Yeah no no no actually I just wanted to clarify that yes

### 00:15:46 · Speaker 2

So it's yeah so this STU is movement in the plant and in the warehouse movement GIs are sales to the customer

### 00:15:57 · Speaker 2

So, um, yeah, so I think I'm, I just wanted to like point that out again. So that's, that's why the reason we have this initial stock location, then we have the movements down from road 30. So we come to the inventory view. So with the inventory view, I have two tables. Um, I'll start with the, the first, the table on the left. So the table on the left being powered from the queries that I, I, I let, I, I went with the, the,

### 00:16:27 · Speaker 2

the AI to help me develop is is done all the additions and subtractions from the different plants and their warehouses and we have our total life inventory view per location so you see it on a per sku level

### 00:16:46 · Speaker 2

via the different plants that are there so you have plants a plants b warehouse one warehouse two warehouse three and you have the the stock that you would see in all these locations so let me pick out one stock and because there's a paper table like it's a paper table just to i forgot to add that it's a paper table that is is doing the background calculation to like give us our total inventory but i can't

### 00:17:16 · Speaker 2

out one skew and we see the transactions that went through it so when double click you see the various movements that happen to give you that total amount right

### 00:17:30 · Speaker 3

Okay

### 00:17:31 · Speaker 2

You see here that we had our initial stock, that's a BI. Let me zoom. I think it's a bit. Yeah. Remember I mentioned the initial stock that we had was 27. So that was the amount of this queue that went into plant B. That was the initial stock. Then we had two STO movements that left that particular plant. So we had 22 leaving the plant and 44 leaving the plant for this queue, queue 125, right?

### 00:18:01 · Speaker 2

So I just just to check to be sure I'll be on the same page so this amounts to 161

### 00:18:11 · Speaker 3

That's what you should see on that

### 00:18:12 · Speaker 2

that's what you see i say you see you have the 161 here yeah so just to validate the information you are looking at there we is being accurate calculating what led to you having 161 of sku125 under the plant

### 00:18:29 · Speaker 2

So there's the

### 00:18:29 · Speaker 3

And how does it how is it capturing the inventory which might be in transit right so you ship let's say something from a STO from one plant to the other is this table also showing what's in the pipeline or is it only showing on ground stock

### 00:18:45 · Speaker 2

Yeah so um that's uh let me add it to this one

### 00:18:52 · Speaker 2

I wanted to also like uh show that as well so that this on the status I would add the status to my filter

### 00:19:02 · Speaker 2

Is this that's yeah get out of the status here Yeah, so currently we are seeing every it's all everything's more or less delivered, right? But we could change Let's say we could change one of these transactions to

### 00:19:19 · Speaker 2

in transit right so i'll run this in transit i would come back into my inventory view and and there's another thing with power query and the the queries that you have to always refresh your yeah

### 00:19:34 · Speaker 3

Of course

### 00:19:36 · Speaker 2

get your data otherwise you don't see that live so now we would see if we want to have a view of what is in transit we could filter it out there and you would see that sku 231 is in transit to plant no it's being is leaving plant b and it's on its way to uh warehouse yeah so you have a view of that so even with this

### 00:20:06 · Speaker 2

all your in transit view stock movement you just filter this out you see everything but the good thing is that it doesn't affect what is uh delivered because what is delivered has actually happened left one warehouse location and landed onto the the the the the next where it's destined for so it's able to separate uh these these two things

### 00:20:32 · Speaker 3

Excellent, excellent. So, so, so far what you have shown us, Erin, is like, you know, really like the core of Power Query, right? So how you have built this, right? Now, can you just show us a little bit more about how you use ChatGPT to facilitate some of this work?

### 00:20:48 · Speaker 2

Okay let me know if if we can see it now

### 00:20:50 · Speaker 3

It came up mm-hmm

### 00:20:52 · Speaker 2

Okay, so this, so I'll just go through some of the conversations with I had with the chat GPT to come up with this stuff. So I started with telling them, like, I always start with an objective of why I'm having the conversation. So you see, I want to work with you, we're finding a power query I created. I'm referencing to logic I got from you and I'm not sure if remember, and I also put in there, I don't want it to use a higher level of GPT because I'm using the free version.

### 00:21:22 · Speaker 2

Yes, when you when when he uses a chat to be fab the higher level it's sort of cast out in the middle so like I was very specific to let it keep to the base model that I think was very sufficient for what I wanted to use it for

### 00:21:22 · Speaker 3

Yes

### 00:21:37 · Speaker 2

So I send this message to ChatGPT

### 00:21:41 · Speaker 2

It said it doesn't remember, which was a good thing for me. And I was happy it said it couldn't remember because I'll take us through how I modeled, I sort of communicated what I had and how where I wanted to go with it. So it asked me to share my query, which was just perfect. So I said, I have three queries that I'll share the code for each. So I took the query code. I had three queries that I was working with. I had a master table query that I had.

### 00:22:11 · Speaker 2

I shared that like I shared that code with with which I've been and this is the beauty of it because because M M is a power query is the M code which is slightly different from DAX you get to see the actual raw coding behind the query that goes into like transforming the data so it's you're able to really communicate well with the with the AI to let it picture well what you're trying to like trying to achieve so that's what we did here

### 00:22:41 · Speaker 2

I put in the three different codes and three different query codes in there the master table query so I had a master table to master table from and I had a master table query without any funny name with it yeah so these are the three codes I put there

### 00:22:59 · Speaker 2

So the tool just responded, I mean, GPT just came out and said, okay, I see the pattern there. This is what I've done. And this is what's the code, how he understands the code, right? Just going through it quickly to show you the conversation, but it's, it only told me how, what he understands from my code.

### 00:23:22 · Speaker 2

And there was something interesting happened there when I shared initially. So what I didn't see from my files are refined version of my conversation here, because it told me I repeated code, right? And it said that it could do it better by reducing the queries to one parameterized function or whatever. From just looking at the code that you shared with it. And it said, however, I wanted to refactor this code into just two queries. So I had three queries to get to where I wanted to go to. It said we could do it in two.

### 00:23:52 · Speaker 2

I said if I want we could just do into two queries. I said, I think I came back here and I said, okay, but I also gave another data point. So I copied my row columns, right? Remember the where we input the transactions for the movements and stuff. That's a very important piece of it. So I copied that and I shared it with the charge. So it now understands what the query is doing. User understands the source data table or the structure of the source.

### 00:24:22 · Speaker 2

data that is going to be worked with and that's also very important to to add there so given this both of this information to charge GPT it's it has a whole idea of the the entire program you have in the career program you have in Excel and the conversation gets more let's say interactive and more refined in what you want to do so

### 00:24:47 · Speaker 2

I sent that information to chat GPT it's it's got it and broke it down perfectly how how it is in my Excel file

### 00:24:59 · Speaker 2

Then it gave me a couple of steps of what we can do to improve the queries that we have. And that's why I've been asked here so you can basically improve what I've done.

### 00:25:14 · Speaker 2

and he said yes you can definitely improve what we are done without changing the logic you have already built which is just beautiful right so he gave me i said okay let's try and see what you want to do so this is where chat gpt comes in with their code it created this code for me based on all the information that we have we have had prior giving it what my query code was telling it the structure of my table now comes to the output from from chat gpt

### 00:25:44 · Speaker 2

Just profess

### 00:25:44 · Speaker 3

So it just processed all our conversation, even our parameters, and now it's giving you a customized code for your... So you can literally, you can literally copy this and paste.

### 00:25:47 · Speaker 2

Even our

### 00:25:50 · Speaker 2

So you guys did it

### 00:25:53 · Speaker 2

Copy it that's based on yeah yeah so that's

### 00:25:58 · Speaker 2

So perfect. It created this master table code for me. I just took it out and put it into my Empire query. And most often than not, so I'll just add a bit here. Most often than not, the code works perfect, but you have some errors and bugs that you have to kind of figure out. And I believe that's where you as a person can't 100% depend on AI because you have to be

### 00:26:28 · Speaker 2

a sense with the the query or the query code in order to find where the problems are or find what is is uh causing the error or it's not being able to run so that's why I believe and I've been looking at that your conversation you had previously on the AI that's where like the human aspect comes in because it's it's it enables you to be able to do some of these things but you yourself need to have an idea of how like the software works or or the code works

### 00:26:58 · Speaker 2

and to be able to like to guide it to where you wanted to go. So like that's really, I guess I'll say that this is an important piece in the evolution of AI and especially not just for supply chain, just like for everybody else because you need to be, I don't think where it is today personally is at a level where you can 100% depend on it. It's still very powerful, but it needs the guidance.

### 00:27:23 · Speaker 3

Yeah, I think, yeah, I mean, and that's so true, Aaron, right? Because that's also my experience. I mean, I don't write this level of code that you are writing on Excel, which is fantastic. But even like I use AI all the time for content creation and all of that. So it does 80% of your work, but you still need to put in that 20% human element.

### 00:27:39 · Speaker 2

Yeah but put in that 20 human element

### 00:27:42 · Speaker 3

But it's still, you know, the fact that it's doing like earlier before AI tools were available, we had to do 100% of the work. Now it's doing, saving a lot of your time, but you still need to have that human element. Absolutely. Agreed.

### 00:27:51 · Speaker 2

Thank you

### 00:27:56 · Speaker 2

So it's more or less gave me, so like I was saying, it more or less gave me the code that I could create. And so it was two pieces of code, two queries. Yeah, it created one query and another query. And it's, it combined it in a certain way.

### 00:28:15 · Speaker 2

Not to get too technical into the details but I was very intelligent in how I developed this piece of code combining

### 00:28:25 · Speaker 2

two two different queries into one and making it dynamic such that the final query was just depending on the prior query to get the information so i don't know if i'm i explain as well but like it's

### 00:28:40 · Speaker 3

So basically you're saying it optimized the query quite smartly. So what you thought were two separate queries, it actually collapsed it into one. So it made the code very efficient, basically.

### 00:28:50 · Speaker 2

Yeah, so maybe to give a basic example, right, you had maybe had two Excel formulas and it's instead of you, instead of you having two Excel formulas, let's say you combine it into one. That's the longest shot of it, yeah.

### 00:29:08 · Speaker 3

Yeah

### 00:29:09 · Speaker 2

Yeah

### 00:29:10 · Speaker 3

You know, there are so many examples I can think of, you know, you, I remember I used to when back in like early days, I used to write like a V lookup, H lookup.

### 00:29:20 · Speaker 2

Exactly yeah

### 00:29:21 · Speaker 3

I brought in new formulas where you don't need to write that long of a like I you know I remember writing like seven line formulas in Excel at one point in time now you can do it with like you know a couple of lines but now this is like the next level you don't even need to write those couple of lines you can use chat GB to do it for you and then you just refine and make sure that your parameters are customized and that's it

### 00:29:43 · Speaker 2

It was nice yeah

### 00:29:44 · Speaker 3

So you then just you just took copied this code and pasted it on our query uh Aaron

### 00:29:51 · Speaker 2

So I copied it and put it on the power query and and also to also point out It was kind of new to me that the Technique is used to create this query, right? So you can see I asked it. What what do you enter for the parameter? It was a whole different view I didn't get what it was saying Then it breaks it down to me to tell me what exactly is trying to achieve, right? Yeah, so this is where I talk about being confident of with the with the code, right? so

### 00:30:21 · Speaker 2

I get this error and normally I put in the errors into chat GPT to tell it that I'm getting this specific error like what what does it mean sometimes I'm not being I'm not able to figure out why so I would go back and take a snapshot of it or take a text of it and and and tell it and talk chat GPT then it will explain to me why what the error is and give me some solutions right

### 00:30:46 · Speaker 2

It gives me a quick fix. I tried a quick fix, it still doesn't work. So what I then do is I get my own fix and put it in there and I come back and tell her that, hey, what you told me didn't work, but this is what I did. So it was a naming problem. Like no one can have the same exact name with your work in Excel. Can't have the exact name in your worksheets, right? If you have a worksheet A, you also can have another worksheet A in it. So that was the error that I was getting, but I was on a query level.

### 00:31:16 · Speaker 2

was it was saying I was replicating reusing the same name twice where I shouldn't be so I just added a one the number one to the the where I was getting the error from or else and I came back and told that like this is what I did and it worked

### 00:31:38 · Speaker 2

It's what did it see Is that something interesting about it

### 00:31:43 · Speaker 2

I just added a number one so that works too yeah now your function query is called function master table one and as long as they have this blah blah so so it sort of solved the problem and like I said initially like this is where you need to be able to be conversant with the software and the and the code to be able to get through it because if let's say I had zero idea about how it works I wouldn't have been able to overcome some of some of the some of these uh problems so yeah

### 00:32:13 · Speaker 2

So this basically the not to go through the entire conversation but this basically how I communicate with the chat GPT to achieve what I want to do with my with my code right and and sometimes it will give me suggestions so there was one last piece in the Excel file that I didn't show it's it's suggested to me based on my code alone that I need to add another query that checks for when I get negative balances right because bear in mind there's an Excel

### 00:32:43 · Speaker 2

It's it won't stop you like the way your ARP system will stop you from trying to take more than what's in a location

### 00:32:51 · Speaker 2

But with this, in Excel, there's nothing like some internal tool that will stop that. Maybe not that I know of yet, but it was smart enough to look at my code and tell me that we need to add that to it. So it's, you'd see, there's another part of it I didn't show, but maybe I'll get there a bit later. But it's recommended a whole new idea, a whole new query to check for these things.

### 00:33:19 · Speaker 2

And it helped me develop that career as well in inputs in it so this is how powerful it's it's gonna become it can

### 00:33:25 · Speaker 3

So this can this is this is really becoming your coding assistant, right? It's like giving you everything and you just need to know the business problem you are solving.

### 00:33:36 · Speaker 2

Oh yeah

### 00:33:37 · Speaker 3

So in this case, you showed us a very good live example where you were trying to create this inventory visibility system, let's call it, or set of spreadsheets, and data is coming from different sources. Some of the data is manually entered, but using this query, you have made it smart enough that it's basically wiring all the data properly.

### 00:34:01 · Speaker 2

And you see the stock in each cell here, just to point it out to you, it's all negative because that's where the starting point of the inventory, but I just, I'll just, I could hide it here or I could hide it on the query level, but just to show you what it looks like. So we are back to seeing the view for plants and the integrity check is here. So it's a two-way, there are two separate queries, but they all achieve the same thing.

### 00:34:31 · Speaker 2

So this is actually what I came up with to check if there will be negative balances. And that's, to be honest with you, that was originally on Chachi Piti's suggestion.

### 00:34:43 · Speaker 2

In my second conversation, in my conversation with the ChatGPT, I gave it this particular code that I had done and they said we could do it better. So just go back to the point of what I was saying about checking for negative balances. It improved on itself more or less. This was what it gave me the very, the first time that I ran through this system and going through it again with ChatGPT said, okay, actually we can do

### 00:35:13 · Speaker 2

better than this so i'll let's do a live example right i would want to create a negative uh stock balance for a particular plant so let's see this one like this i'll just put some crazy number i know it won't have that amount can you see my screen

### 00:35:31 · Speaker 4

Yeah I can

### 00:35:33 · Speaker 2

Yeah, so that's SKU A64 for plant A. I'm taking 600 out. I know definitely doesn't have that amount in there and I'm moving it to warehouse too, right? So I'll run the query again and let's see. You should see a negative balance for.

### 00:35:55 · Speaker 4

Yeah, there you go, 864 is negative.

### 00:35:58 · Speaker 2

So it pops out right at you. Now my data integrity check also tell me that I have negative stock on plant A, which is where we did the change on, right? What's this would do? So let's go through. So let me click it to tell me what happened. So it will tell me that this particular SKU on plant A has your negative minus 366. This just tells me that I have a negative value.

### 00:36:28 · Speaker 2

on the plant it doesn't tell me when that happened right and the second query that jg suggested was showing me when exactly i made a mistake

### 00:36:39 · Speaker 4

Wow okay so so that that's fantastic

### 00:36:40 · Speaker 2

Sure sure

### 00:36:43 · Speaker 2

Yeah so I'll come in oh I already loaded I didn't want it to load automatically but let me clear it out here

### 00:36:50 · Speaker 2

So this table is more or less like a replication of all our transactions. So every single time we put in information in our main, like the main sheet, it does a check here. Every single one is, you can see that every single one is okay apart from the one, right? So if I just filter out here.

### 00:37:12 · Speaker 4

Yeah

### 00:37:13 · Speaker 2

negative stock I'll see that that is the plant E that we are referring to right

### 00:37:21 · Speaker 2

So this is the line somebody

### 00:37:24 · Speaker 3

Somebody messes around with the data you can easily go

### 00:37:27 · Speaker 2

Please be go by the fine here

### 00:37:29 · Speaker 3

So this could be a great tool for like inventory reconciliation as well right when you're reconciling different systems

### 00:37:34 · Speaker 2

There's another comment

### 00:37:35 · Speaker 3

Redemption problem right so

### 00:37:39 · Speaker 2

So to point out exactly where you made a mistake and

### 00:37:44 · Speaker 2

It you know the reference. So this will just show you that this particular line you put in there, it's wrong. So you could go and take the reference number and coming back here.

### 00:38:00 · Speaker 2

So this was where we made a change, you remember, was 600, yeah. So you have a whole setup to kind of go back and find where he made mistakes in terms of like the movements around and figure it out. Otherwise, you'd have to now go through a tall list of transactions and see, do some small analysis, see where the mistakes come from. But with this, it's all more or less automated.

### 00:38:28 · Speaker 3

This is fantastic. So just maybe thanks again for sharing this, Aaron. And for the benefit of the audience, if someone wants to really, in the supply chain space, wants to like blend this AI tools with the existing tools, how did you have the initiative to learn this? Was it just your inquisitiveness, you were trying to find out stuff on ChatGPT? Or is there any other route you would recommend to people who are watching this podcast?

### 00:39:00 · Speaker 2

Well, um, personally I, I, I got into using AI like, uh, I think maybe two years ago, give or take, and I was using it for very rudimentary things like maybe for example, a very long text you want to summarize and that basic stuff. And it just occurred to me like, okay, if this is it, you can ask that GPT literally anything. And I started playing around inputs in like, asking it like opinions.

### 00:39:30 · Speaker 2

to actual Excel problems I saw it go solve my Excel problems like the formulas that you're seeing you had like three or four back in the past I said this is my formula how can we make it better it's to give me something and I'm like okay so it's more of like a built-in like experiences I've had with the tool and I keep pushing it to see how far I can go with the its usefulness and like what I just what we just went through and had a conversation with the with the with Chaggy

### 00:40:00 · Speaker 2

It really boils down to how well you can communicate what you have and what you want to achieve. So, for example, I wanted to build an inventory management tool. I had something ongoing from my knowledge of Power Query. And I'll say this, it understands code best. If you give these tools programming code, it's not just M or DAX, C++, whatever.

### 00:40:30 · Speaker 2

you want to use it understands it very very well so i would suggest if you're using excel you have some problem you want to optimize copy the code and put it in tell it that these are the the columns in my table that i'm working with and this the formula i have but this is what i want to do that'll be an example of how to use it in your everyday supply chain um life if you want to create a tool like this you need to get a bit confident with the code a bit you don't need to be an expert

### 00:41:00 · Speaker 2

I'm not an expert in the DAX or OM but I've used it well enough to be able to understand how the code works and how it flows because a lot of you I'll say that a lot of the code language is very similar to basic English you're able to tell summarize filter you see all of those small small codes inside these these languages that you can make sense of right and yeah so as much as you are dependent on it when you get

### 00:41:30 · Speaker 2

the outputs learn what it's trying to do try and understand the logic behind what you get back from the AI because that's the only way you can guide it to improve onto what you want to like achieve so yeah

### 00:41:44 · Speaker 3

build the basic a

### 00:41:51 · Speaker 3

just skipping my mind you you should be basically like understand the fundamentals of the coding language so that then you can use ai to its uh to your advantage and then ai does like 80 of the work and then you just refine it and then fix it last question uh aaron is i mean microsoft is trying to do a lot of this with copilot as well right but i've tried it once uh maybe i've not tried enough like i was not very impressed or maybe you know they still need to improve the code itself because what you are doing is you're taking

### 00:42:01 · Speaker 2

Thank you

### 00:42:21 · Speaker 3

all like you're doing all the AI work in chat GPT or then bring it back to Excel

### 00:42:27 · Speaker 3

Any any perspective on

### 00:42:31 · Speaker 3

Because maybe in the next couple of years you'll be able to do it within the Excel environment itself using the compiler as well. So any perspective on that?

### 00:42:35 · Speaker 2

environment itself using

### 00:42:39 · Speaker 2

I think it would I hope that it does get to that level of integration between the AI like co-pilots because it's Microsoft and and Excel and their whole suite of programs especially we have Power BI too there that's also quite powerful but I would my only concern with that direction is the that space of the human intelligence clean into it because it can

### 00:43:09 · Speaker 2

only be as useful as what you want it to be right and i'm just interested to see how that integration will happen how it will be set up in such a way that you can still guide the ai to achieving what you want it to do not basically do what it thinks is best because it's not it's not necessarily what's the ai comes out with that is the most like uh refined or or best output of what you want to achieve right you

### 00:43:39 · Speaker 2

you've asked like we are we have different professions like the finance person might look at this and want to work it in such a way that it suits them right and a supply chain person will look at it in such a way that wants to develop it to look out for these parameters or these tools and come up with an output that makes that has useful information for me so i i i do hope that there's that allowance for the human intelligence aspect of it and hopefully

### 00:44:09 · Speaker 2

I would want it to to get to that level of integration so yeah I'm hoping that we get there in the next couple of years especially with copilot because Microsoft Office is one of the most used softwares and organizations too so it's it's quite important that you get it right and I think chat GPT is integrated into copilot some funny way

### 00:44:32 · Speaker 4

Yeah of course they are using their own LLM I mean I'm not an expert

### 00:44:36 · Speaker 2

Oh yeah

### 00:44:37 · Speaker 3

Absolutely great. Well, I mean, this was very educational personally for me and very useful. And I think I really love the part where you just showed how you are using AI to optimize the code for your power queries. And then, you know, putting it in the context of a real life supply chain example is always very powerful. Thanks a lot for your time again. Thanks a lot for taking the time on the weekend to do this. So really, really appreciate your

### 00:45:07 · Speaker 3

your willingness to come and show us the tool and hopefully you know we'll stay in touch and you know as you do more of this fantastic stuff with AI I may invite you once more to the podcast another time.

### 00:45:17 · Speaker 2

Yeah of course yeah thank you for having me too Jamil yeah

### 00:45:21 · Speaker 3

Absolutely all right thank you

### 00:45:22 · Speaker 2

Okay thanks bye

