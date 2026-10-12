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

### Speaker 1

Warning if you are not into supply chain planning and do not like working with numbers and spreadsheets then this podcast will feel very boring to you But if you like these things especially spreadsheets for planning then there will be some great Chad GPT tips for you with Ariel Life example

### Speaker 2

is able to account for inventory moving from one location to another location and from that location to another like the whole movement of inventory and it keeps track of all of that and makes sure that all the so it does

### Speaker 3

So it does 80 percent of your work but you still need to put in that 20 percent human element But its still you know the fact that its doing like earlier before AI tools were available we had to do 100 percent of the work Now its doing exactly the same saving a lot of your time

### Speaker 2

Yeah

### Speaker 3

You still need to have that human element absolutely agreed

### Speaker 2

Not to get too technical into the details but I was very intelligent in how I developed this piece of code combining


two two different queries into one and making it dynamic such that the final query was just depending on the prior query to get the information like i said initially like this is where you need to be able to be conversant with the software and the and the code to be able to get through it because if lets say i had zero idea about how it works i wouldnt have been able to overcome some of some of the some of these uh problems so its its


to me based on my code alone that I need to add another query that checks for when I get negative balances right because bear in mind is an excel um setup its it wont stop you like the way your arp system will stop you from trying to take more than whats in the location


It was smart enough to look at my code and tell me that you need to add that to it

### Speaker 3

Hello and welcome to another podcast on my channel Supply Chain Folks And as you know that one of the topics I talk a lot about in this channel is how the power of AI is shaping the world of supply chain and the skill sets around it And recently when I posted one of the clips from my podcast with Aileen Sandoval where we talked about how to build skills for AI in supply chain one of my followers posted a comment that he has actually built an inventory system in Excel using AI for MDAC


And he believes that the performance and the functionality of the tool he has built is more or less the same what an SAP module would give you And I really got excited when I heard that So I invited him to this podcast and he was very kind enough to take the time out on his weekend to do this with us So I would like to introduce Aaron Turksen uh to you guys and aaron is an experienced supply planning professional he has got a wealth of experience in uh the area of supply planning he has worked with some big


companies like Unilever and he has got his experience across Africa and now hes working in Canada and hes joining me from a very exciting place in Canada which is Whitehorse Yukon So without further ado let me welcome Aaron to the podcast Hello Aaron how are you

### Speaker 2

Hi hi Jemil Im good hows it going

### Speaker 3

Very good very good Aaron And thanks a lot for contributing to my posts on LinkedIn and sharing your amazing tool that you have built which Im sure today the audience is going to take benefit from that whole thought process and how you have built it But before we go there Aaron just give us a quick introduction about yourself How did you get into supply chain and what has been your journey and what are you doing right now

### Speaker 2

Yeah okay so um well I would say uh my supply chain journey started uh like back I come Im from Ghana originally and I I started um working in uh planning departments initially doing imports exports type of operations and I got exposed to the planning department like the other aspect which is the material planning supply planning and I found some way somehow found myself like getting the opportunity


to be in these roles and develop myself so um current i i recently just completed my masters program um here in canada and like after that i started a job here and what brings me to whitehouse all the way up north here in the yukon um working with the with the one of the telcos and up here so its a bit different from my planning experience its now more logistics based but its its quite uh exciting to have a feel of another part of


like the big big supply chain field so yeah its a little bit about myself and yeah happy to to show whats like what I came up with yeah

### Speaker 3

abs excellent that thats fantastic and yeah and then once you share your your tool with us i would love to also hear from you like how are you really keeping yourself up to date and how youre like you know blending the power of like some of these new ai tools with excel or some of the other like standard tools we use in supply chain so i would love to also learn about that uh but lets uh lets go to the tool itself aaron and before you start sharing your screen and and we get into the tool itself uh just tell us a little bit about like


what is the purpose of the tool what it does and then we can dive into how we have built it

### Speaker 2

Yeah so the tool basically is like for inventory management in sense of warehouse storage keeping track of inventory thats coming to lets say your warehouse or multiple warehouses So what I have here is we have I have different locations where inventory is kept Its able to account for inventory moving from one location to another location and from that location to another like the whole movement of inventory


and it keeps track of all of that and makes sure that all the um i have some checks that ill go through it when we when when i present to make sure that its all accurate so yeah i mean basically its its its i feel like its replicating something like what an sap sap model would do because you have different plants you have different warehouses and stuff that inventory moves around and yeah this is what i i try to achieve with with this system so yeah just a simple inventory


management system So yeah

### Speaker 3

Excellent And one question out of just pure curiosity right Because this is I mean to be very honest like this is also one of the challenges we face in our company as well right That tracking inventory across multiple warehouses whats in transit and whats not and all of that stuff So tell me a little bit about like is the tool pulling data from different sources different systems How does the data sourcing work

### Speaker 2

so its the tool at this base and what im what ill show you to you is uh its taken it from manual entries so for example um you have one person whos inputting like its like theyre doing a transaction so you see how in sap you go in there and you are you are uh receiving inventory you you put in your po number if you have a po number and all of that stuff in and you execute we have a i have a table for that its scalable to


what you are seeing where it could be pulling from different sources as well so lets see if multiple google could have different uh versions of the sheets we could we could set it up to link it to every single warehouse location and as everybody inputs in their like their data and information it can be updated it can be the locations on the inventory at the different locations could be also updated so thats that is possible but at this very base what i show today is uh its all in one sheet so you have the


the way youre putting like this in your transactions and is updating it as you move the inventory along to different different places

### Speaker 3

Awesome awesome Okay All right So lets lets dive into the tool itself Let me just add your screen here So over to you You just walk us through how its built

### Speaker 2

Yeah okay so I would start with this screen So this is more like the validation or like what Ill say

### Speaker 3

Sorry Aaron can you just zoom in a little bit more so that you know people can see that yeah

### Speaker 2

So we love that


Is it is he okay

### Speaker 3

Yeah thats perfect

### Speaker 2

Okay okay so I have it on another screen here so that you can see my head tools are perfect So this is more like somewhat like my master data screen where I have the different warehouse locations So you have warehouse two warehouse one plant A warehouse three and all of this and all of this stuff And you have your customers as well And I have this special location I call stock initial


I would explain that when I get to the full inventory view but its a special location because


Every lets say every company everywhere else will have some inventory will be completely zero from there from the start right So this is like a one time location where thats I accounted for for for that inventory


Yeah so this is like my master data for my locations Then I have another table for the status of lets say the transaction or the input you are putting in the system whether its in transit or its delivered because it might take time from point A to point B and so forth So thats also accounted for here And we come to the movement type So as I already did in a stock transfer order which is more or less the movements between the


plants or youre doing a goose issue or a sale which youre selling to a customer and this movement that bi stands for beginning inventory that ties back to what i was referring to in the initial stock so its more like a one time kind of um setup i have in place to account for initial inventory that the warehouses and plants will have then for scalability i have this table um here so this is


my lets say my transactions or the data Ill be inputting for the year 2025 it doesnt have to be just the year 2025 but you understand that Excel has a limitations up to about a million and something rules we can have multiple rules as much as you want but when you get to that limit you have to create a new table and this here this setup here is to account for that limitation so if I use up to my I dont expect us it to be used up to


one million in a very short time but if you use up to one million the the limit of the excel sheets then we can add a new one here and move on and move for move like move forward so this is for scalability


Reasons yeah and let me come to the


where the data is actually imported here let me zoom in again


you have the date of the transaction you have your movement type here you have a unique reference that that particular uh lets see transactional row youre inputting will come with i i could we could put a a formula to generate a unique reference so that you dont need to manually input this but this like i said very very rudimentary and basic but like so you can improve on that then you have the sku or the code in in some cases


You have your description in here and you input the PO number Activity this I just have as a miscellaneous rule but you dont need to really put in much there But it can be repurposed whatever you want it to be you have your unit of measure you have the quantity So now theres an important piece where its coming from and where its going to and you see here I have some drop down Ive done the data validation here so that if Im lets say for example putting


warehouse for theres nothing like warehouse for it wont let me uh input that for i dont know if you have seen it on the screen but

### Speaker 3

Yeah I can

### Speaker 2

you can see you wont let me input in the wrong warehouse so if i knew i want to add another warehouse location i have to come into my master data screen and add the warehouse here


Maybe you can just test it out to just give you an idea of some of the controls we have here so you see how well its for here and yeah

### Speaker 3

Okay


Now you can do it okay get it

### Speaker 2

These are some of the checks and small tweaks that


been factored into the file to make sure that like the theres integrity in the data um yeah so yeah so this covers it from the plants then you have the status whether its uh delivered or in transit because youd see here that we have the ship dates and we have the arrival dates and we have the so so so more or less you would put in your ship dates when it ships out and this would be lets say in transit until it arrives there this would uh remain


Like in transit and then again to like these are these are also rooms for improvements you can I could put an automated formula there that would account for Its changing on its own without any human input right These are some of the benefits and stuff of AI like it can improve Whatever like you you create so this is at this very base So yeah this is pretty much it for the data entry aspect of the of the tool and all of it could


into the inventory view here


Let me zoom in again


So


from all the transactions that we saw from this previous page like all of this stock that you see here And as I mentioned sorry to go back a bit but I mentioned to you I needed to create a special location called stock initial which is more or less the starting inventory for all the different plants per SKU So thats why I have all of these transactions in place Then from


Let me see Yeah so this is beginning inventory the stock initial So from here onwards from row 30 onwards I have the STOs and sales and all of that stuff So the inventory is moving around and its being deducted from one location added to another location moved to another location sold like all of that movements happen here

### Speaker 3

goods issue is a is basically when the product is getting produced so like sto is a transfer order between two warehouses im assuming and goods issue is that when the production happens or like just to understand the terminology

### Speaker 2

Yeah so I in so the the logic I use for this is the STOs are for movements between plants and warehouse So if youre moving from one plant to a warehouse its an STO So Im treating the plants as somewhat of a storage location as well Oh okay Yeah If youre moving it to a warehouse its like an STO movement Now the good issue I mean I the logic here


Theres a goose issue as well

### Speaker 3

Oh me that fails out got it okay clear

### Speaker 2

Yeah yeah so thats why Im using so Im using some of the SAP technologies we are familiar with Im not sure if you are familiar with SAP but like yeah

### Speaker 3

Yeah no no no actually I just wanted to clarify that yes

### Speaker 2

So its yeah so this STU is movement in the plant and in the warehouse movement GIs are sales to the customer


So um yeah so I think Im I just wanted to like point that out again So thats thats why the reason we have this initial stock location then we have the movements down from road 30 So we come to the inventory view So with the inventory view I have two tables Um Ill start with the the first the table on the left So the table on the left being powered from the queries that I I I let I I went with the the


the AI to help me develop is is done all the additions and subtractions from the different plants and their warehouses and we have our total life inventory view per location so you see it on a per sku level


via the different plants that are there so you have plants a plants b warehouse one warehouse two warehouse three and you have the the stock that you would see in all these locations so let me pick out one stock and because theres a paper table like its a paper table just to i forgot to add that its a paper table that is is doing the background calculation to like give us our total inventory but i cant


out one skew and we see the transactions that went through it so when double click you see the various movements that happen to give you that total amount right

### Speaker 3

Okay

### Speaker 2

You see here that we had our initial stock thats a BI Let me zoom I think its a bit Yeah Remember I mentioned the initial stock that we had was 27 So that was the amount of this queue that went into plant B That was the initial stock Then we had two STO movements that left that particular plant So we had 22 leaving the plant and 44 leaving the plant for this queue queue 125 right


So I just just to check to be sure Ill be on the same page so this amounts to 161

### Speaker 3

Thats what you should see on that

### Speaker 2

thats what you see i say you see you have the 161 here yeah so just to validate the information you are looking at there we is being accurate calculating what led to you having 161 of sku125 under the plant


So theres the

### Speaker 3

And how does it how is it capturing the inventory which might be in transit right so you ship lets say something from a STO from one plant to the other is this table also showing whats in the pipeline or is it only showing on ground stock

### Speaker 2

Yeah so um thats uh let me add it to this one


I wanted to also like uh show that as well so that this on the status I would add the status to my filter


Is this thats yeah get out of the status here Yeah so currently we are seeing every its all everythings more or less delivered right But we could change Lets say we could change one of these transactions to


in transit right so ill run this in transit i would come back into my inventory view and and theres another thing with power query and the the queries that you have to always refresh your yeah

### Speaker 3

Of course

### Speaker 2

get your data otherwise you dont see that live so now we would see if we want to have a view of what is in transit we could filter it out there and you would see that sku 231 is in transit to plant no its being is leaving plant b and its on its way to uh warehouse yeah so you have a view of that so even with this


all your in transit view stock movement you just filter this out you see everything but the good thing is that it doesnt affect what is uh delivered because what is delivered has actually happened left one warehouse location and landed onto the the the the the next where its destined for so its able to separate uh these these two things

### Speaker 3

Excellent excellent So so so far what you have shown us Erin is like you know really like the core of Power Query right So how you have built this right Now can you just show us a little bit more about how you use ChatGPT to facilitate some of this work

### Speaker 2

Okay let me know if if we can see it now

### Speaker 3

It came up mm hmm

### Speaker 2

Okay so this so Ill just go through some of the conversations with I had with the chat GPT to come up with this stuff So I started with telling them like I always start with an objective of why Im having the conversation So you see I want to work with you were finding a power query I created Im referencing to logic I got from you and Im not sure if remember and I also put in there I dont want it to use a higher level of GPT because Im using the free version


Yes when you when when he uses a chat to be fab the higher level its sort of cast out in the middle so like I was very specific to let it keep to the base model that I think was very sufficient for what I wanted to use it for

### Speaker 3

Yes

### Speaker 2

So I send this message to ChatGPT


It said it doesnt remember which was a good thing for me And I was happy it said it couldnt remember because Ill take us through how I modeled I sort of communicated what I had and how where I wanted to go with it So it asked me to share my query which was just perfect So I said I have three queries that Ill share the code for each So I took the query code I had three queries that I was working with I had a master table query that I had


I shared that like I shared that code with with which Ive been and this is the beauty of it because because M M is a power query is the M code which is slightly different from DAX you get to see the actual raw coding behind the query that goes into like transforming the data so its youre able to really communicate well with the with the AI to let it picture well what youre trying to like trying to achieve so thats what we did here


I put in the three different codes and three different query codes in there the master table query so I had a master table to master table from and I had a master table query without any funny name with it yeah so these are the three codes I put there


So the tool just responded I mean GPT just came out and said okay I see the pattern there This is what Ive done And this is whats the code how he understands the code right Just going through it quickly to show you the conversation but its it only told me how what he understands from my code


And there was something interesting happened there when I shared initially So what I didnt see from my files are refined version of my conversation here because it told me I repeated code right And it said that it could do it better by reducing the queries to one parameterized function or whatever From just looking at the code that you shared with it And it said however I wanted to refactor this code into just two queries So I had three queries to get to where I wanted to go to It said we could do it in two


I said if I want we could just do into two queries I said I think I came back here and I said okay but I also gave another data point So I copied my row columns right Remember the where we input the transactions for the movements and stuff Thats a very important piece of it So I copied that and I shared it with the charge So it now understands what the query is doing User understands the source data table or the structure of the source


data that is going to be worked with and thats also very important to to add there so given this both of this information to charge GPT its it has a whole idea of the the entire program you have in the career program you have in Excel and the conversation gets more lets say interactive and more refined in what you want to do so


I sent that information to chat GPT its its got it and broke it down perfectly how how it is in my Excel file


Then it gave me a couple of steps of what we can do to improve the queries that we have And thats why Ive been asked here so you can basically improve what Ive done


and he said yes you can definitely improve what we are done without changing the logic you have already built which is just beautiful right so he gave me i said okay lets try and see what you want to do so this is where chat gpt comes in with their code it created this code for me based on all the information that we have we have had prior giving it what my query code was telling it the structure of my table now comes to the output from from chat gpt


Just profess

### Speaker 3

So it just processed all our conversation even our parameters and now its giving you a customized code for your So you can literally you can literally copy this and paste

### Speaker 2

Even our


So you guys did it


Copy it thats based on yeah yeah so thats


So perfect It created this master table code for me I just took it out and put it into my Empire query And most often than not so Ill just add a bit here Most often than not the code works perfect but you have some errors and bugs that you have to kind of figure out And I believe thats where you as a person cant 100 percent depend on AI because you have to be


a sense with the the query or the query code in order to find where the problems are or find what is is uh causing the error or its not being able to run so thats why I believe and Ive been looking at that your conversation you had previously on the AI thats where like the human aspect comes in because its its it enables you to be able to do some of these things but you yourself need to have an idea of how like the software works or or the code works


and to be able to like to guide it to where you wanted to go So like thats really I guess Ill say that this is an important piece in the evolution of AI and especially not just for supply chain just like for everybody else because you need to be I dont think where it is today personally is at a level where you can 100 percent depend on it Its still very powerful but it needs the guidance

### Speaker 3

Yeah I think yeah I mean and thats so true Aaron right Because thats also my experience I mean I dont write this level of code that you are writing on Excel which is fantastic But even like I use AI all the time for content creation and all of that So it does 80 percent of your work but you still need to put in that 20 percent human element

### Speaker 2

Yeah but put in that 20 human element

### Speaker 3

But its still you know the fact that its doing like earlier before AI tools were available we had to do 100 percent of the work Now its doing saving a lot of your time but you still need to have that human element Absolutely Agreed

### Speaker 2

Thank you


So its more or less gave me so like I was saying it more or less gave me the code that I could create And so it was two pieces of code two queries Yeah it created one query and another query And its it combined it in a certain way


Not to get too technical into the details but I was very intelligent in how I developed this piece of code combining


two two different queries into one and making it dynamic such that the final query was just depending on the prior query to get the information so i dont know if im i explain as well but like its

### Speaker 3

So basically youre saying it optimized the query quite smartly So what you thought were two separate queries it actually collapsed it into one So it made the code very efficient basically

### Speaker 2

Yeah so maybe to give a basic example right you had maybe had two Excel formulas and its instead of you instead of you having two Excel formulas lets say you combine it into one Thats the longest shot of it yeah

### Speaker 3

Yeah

### Speaker 2

Yeah

### Speaker 3

You know there are so many examples I can think of you know you I remember I used to when back in like early days I used to write like a V lookup H lookup

### Speaker 2

Exactly yeah

### Speaker 3

I brought in new formulas where you dont need to write that long of a like I you know I remember writing like seven line formulas in Excel at one point in time now you can do it with like you know a couple of lines but now this is like the next level you dont even need to write those couple of lines you can use chat GB to do it for you and then you just refine and make sure that your parameters are customized and thats it

### Speaker 2

It was nice yeah

### Speaker 3

So you then just you just took copied this code and pasted it on our query uh Aaron

### Speaker 2

So I copied it and put it on the power query and and also to also point out It was kind of new to me that the Technique is used to create this query right So you can see I asked it What what do you enter for the parameter It was a whole different view I didnt get what it was saying Then it breaks it down to me to tell me what exactly is trying to achieve right Yeah so this is where I talk about being confident of with the with the code right so


I get this error and normally I put in the errors into chat GPT to tell it that Im getting this specific error like what what does it mean sometimes Im not being Im not able to figure out why so I would go back and take a snapshot of it or take a text of it and and and tell it and talk chat GPT then it will explain to me why what the error is and give me some solutions right


It gives me a quick fix I tried a quick fix it still doesnt work So what I then do is I get my own fix and put it in there and I come back and tell her that hey what you told me didnt work but this is what I did So it was a naming problem Like no one can have the same exact name with your work in Excel Cant have the exact name in your worksheets right If you have a worksheet A you also can have another worksheet A in it So that was the error that I was getting but I was on a query level


was it was saying I was replicating reusing the same name twice where I shouldnt be so I just added a one the number one to the the where I was getting the error from or else and I came back and told that like this is what I did and it worked


Its what did it see Is that something interesting about it


I just added a number one so that works too yeah now your function query is called function master table one and as long as they have this blah blah so so it sort of solved the problem and like I said initially like this is where you need to be able to be conversant with the software and the and the code to be able to get through it because if lets say I had zero idea about how it works I wouldnt have been able to overcome some of some of the some of these uh problems so yeah


So this basically the not to go through the entire conversation but this basically how I communicate with the chat GPT to achieve what I want to do with my with my code right and and sometimes it will give me suggestions so there was one last piece in the Excel file that I didnt show its its suggested to me based on my code alone that I need to add another query that checks for when I get negative balances right because bear in mind theres an Excel


Its it wont stop you like the way your ARP system will stop you from trying to take more than whats in a location


But with this in Excel theres nothing like some internal tool that will stop that Maybe not that I know of yet but it was smart enough to look at my code and tell me that we need to add that to it So its youd see theres another part of it I didnt show but maybe Ill get there a bit later But its recommended a whole new idea a whole new query to check for these things


And it helped me develop that career as well in inputs in it so this is how powerful its its gonna become it can

### Speaker 3

So this can this is this is really becoming your coding assistant right Its like giving you everything and you just need to know the business problem you are solving

### Speaker 2

Oh yeah

### Speaker 3

So in this case you showed us a very good live example where you were trying to create this inventory visibility system lets call it or set of spreadsheets and data is coming from different sources Some of the data is manually entered but using this query you have made it smart enough that its basically wiring all the data properly

### Speaker 2

And you see the stock in each cell here just to point it out to you its all negative because thats where the starting point of the inventory but I just Ill just I could hide it here or I could hide it on the query level but just to show you what it looks like So we are back to seeing the view for plants and the integrity check is here So its a two way there are two separate queries but they all achieve the same thing


So this is actually what I came up with to check if there will be negative balances And thats to be honest with you that was originally on Chachi Pitis suggestion


In my second conversation in my conversation with the ChatGPT I gave it this particular code that I had done and they said we could do it better So just go back to the point of what I was saying about checking for negative balances It improved on itself more or less This was what it gave me the very the first time that I ran through this system and going through it again with ChatGPT said okay actually we can do


better than this so ill lets do a live example right i would want to create a negative uh stock balance for a particular plant so lets see this one like this ill just put some crazy number i know it wont have that amount can you see my screen

### Speaker 4

Yeah I can

### Speaker 2

Yeah so thats SKU A64 for plant A Im taking 600 out I know definitely doesnt have that amount in there and Im moving it to warehouse too right So Ill run the query again and lets see You should see a negative balance for

### Speaker 4

Yeah there you go 864 is negative

### Speaker 2

So it pops out right at you Now my data integrity check also tell me that I have negative stock on plant A which is where we did the change on right Whats this would do So lets go through So let me click it to tell me what happened So it will tell me that this particular SKU on plant A has your negative minus 366 This just tells me that I have a negative value


on the plant it doesnt tell me when that happened right and the second query that jg suggested was showing me when exactly i made a mistake

### Speaker 4

Wow okay so so that thats fantastic

### Speaker 2

Sure sure


Yeah so Ill come in oh I already loaded I didnt want it to load automatically but let me clear it out here


So this table is more or less like a replication of all our transactions So every single time we put in information in our main like the main sheet it does a check here Every single one is you can see that every single one is okay apart from the one right So if I just filter out here

### Speaker 4

Yeah

### Speaker 2

negative stock Ill see that that is the plant E that we are referring to right


So this is the line somebody

### Speaker 3

Somebody messes around with the data you can easily go

### Speaker 2

Please be go by the fine here

### Speaker 3

So this could be a great tool for like inventory reconciliation as well right when youre reconciling different systems

### Speaker 2

Theres another comment

### Speaker 3

Redemption problem right so

### Speaker 2

So to point out exactly where you made a mistake and


It you know the reference So this will just show you that this particular line you put in there its wrong So you could go and take the reference number and coming back here


So this was where we made a change you remember was 600 yeah So you have a whole setup to kind of go back and find where he made mistakes in terms of like the movements around and figure it out Otherwise youd have to now go through a tall list of transactions and see do some small analysis see where the mistakes come from But with this its all more or less automated

### Speaker 3

This is fantastic So just maybe thanks again for sharing this Aaron And for the benefit of the audience if someone wants to really in the supply chain space wants to like blend this AI tools with the existing tools how did you have the initiative to learn this Was it just your inquisitiveness you were trying to find out stuff on ChatGPT Or is there any other route you would recommend to people who are watching this podcast

### Speaker 2

Well um personally I I I got into using AI like uh I think maybe two years ago give or take and I was using it for very rudimentary things like maybe for example a very long text you want to summarize and that basic stuff And it just occurred to me like okay if this is it you can ask that GPT literally anything And I started playing around inputs in like asking it like opinions


to actual Excel problems I saw it go solve my Excel problems like the formulas that youre seeing you had like three or four back in the past I said this is my formula how can we make it better its to give me something and Im like okay so its more of like a built in like experiences Ive had with the tool and I keep pushing it to see how far I can go with the its usefulness and like what I just what we just went through and had a conversation with the with the with Chaggy


It really boils down to how well you can communicate what you have and what you want to achieve So for example I wanted to build an inventory management tool I had something ongoing from my knowledge of Power Query And Ill say this it understands code best If you give these tools programming code its not just M or DAX C plus plus whatever


you want to use it understands it very very well so i would suggest if youre using excel you have some problem you want to optimize copy the code and put it in tell it that these are the the columns in my table that im working with and this the formula i have but this is what i want to do thatll be an example of how to use it in your everyday supply chain um life if you want to create a tool like this you need to get a bit confident with the code a bit you dont need to be an expert


Im not an expert in the DAX or OM but Ive used it well enough to be able to understand how the code works and how it flows because a lot of you Ill say that a lot of the code language is very similar to basic English youre able to tell summarize filter you see all of those small small codes inside these these languages that you can make sense of right and yeah so as much as you are dependent on it when you get


the outputs learn what its trying to do try and understand the logic behind what you get back from the AI because thats the only way you can guide it to improve onto what you want to like achieve so yeah

### Speaker 3

build the basic a


just skipping my mind you you should be basically like understand the fundamentals of the coding language so that then you can use ai to its uh to your advantage and then ai does like 80 of the work and then you just refine it and then fix it last question uh aaron is i mean microsoft is trying to do a lot of this with copilot as well right but ive tried it once uh maybe ive not tried enough like i was not very impressed or maybe you know they still need to improve the code itself because what you are doing is youre taking

### Speaker 2

Thank you

### Speaker 3

all like youre doing all the AI work in chat GPT or then bring it back to Excel


Any any perspective on


Because maybe in the next couple of years youll be able to do it within the Excel environment itself using the compiler as well So any perspective on that

### Speaker 2

environment itself using


I think it would I hope that it does get to that level of integration between the AI like co pilots because its Microsoft and and Excel and their whole suite of programs especially we have Power BI too there thats also quite powerful but I would my only concern with that direction is the that space of the human intelligence clean into it because it can


only be as useful as what you want it to be right and im just interested to see how that integration will happen how it will be set up in such a way that you can still guide the ai to achieving what you want it to do not basically do what it thinks is best because its not its not necessarily whats the ai comes out with that is the most like uh refined or or best output of what you want to achieve right you


youve asked like we are we have different professions like the finance person might look at this and want to work it in such a way that it suits them right and a supply chain person will look at it in such a way that wants to develop it to look out for these parameters or these tools and come up with an output that makes that has useful information for me so i i i do hope that theres that allowance for the human intelligence aspect of it and hopefully


I would want it to to get to that level of integration so yeah Im hoping that we get there in the next couple of years especially with copilot because Microsoft Office is one of the most used softwares and organizations too so its its quite important that you get it right and I think chat GPT is integrated into copilot some funny way

### Speaker 4

Yeah of course they are using their own LLM I mean Im not an expert

### Speaker 2

Oh yeah

### Speaker 3

Absolutely great Well I mean this was very educational personally for me and very useful And I think I really love the part where you just showed how you are using AI to optimize the code for your power queries And then you know putting it in the context of a real life supply chain example is always very powerful Thanks a lot for your time again Thanks a lot for taking the time on the weekend to do this So really really appreciate your


your willingness to come and show us the tool and hopefully you know well stay in touch and you know as you do more of this fantastic stuff with AI I may invite you once more to the podcast another time

### Speaker 2

Yeah of course yeah thank you for having me too Jamil yeah

### Speaker 3

Absolutely all right thank you

### Speaker 2

Okay thanks bye
