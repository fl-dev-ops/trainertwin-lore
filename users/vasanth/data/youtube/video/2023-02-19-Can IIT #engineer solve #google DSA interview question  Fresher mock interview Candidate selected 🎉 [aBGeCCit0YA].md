---
id: aBGeCCit0YA
title: "Can IIT #engineer solve #google DSA interview question? Fresher mock interview|Candidate\
  \ selected \U0001F389"
url: https://www.youtube.com/watch?v=aBGeCCit0YA
date: '2023-02-19'
duration: 00:20:44
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# Can IIT #engineer solve #google DSA interview question? Fresher mock interview|Candidate selected 🎉


## Transcript

### 00:00:00 · Speaker 1

Yeah, hello all. Welcome back to Uncommon Geeks. My name is Vasanth. So people who don't know me, I'm a content creator. I help people to clear their interview. And this is a series where most of you know we are doing a lot of mock interviews for the freshers. And yesterday also I did one interview. I think it will be live. It's already live. Today I am interviewing Vijay. So you'll hear about more from Vijay only. Vijay, can you please introduce yourself so that we can get started?

### 00:00:24 · Speaker 2

I am Vijay from I am currently in fourth year fourth year undergrad in metallurgical and medicines engineering at IIT Madras

### 00:00:35 · Speaker 2

I am currently giving the interview for a DSA

### 00:00:41 · Speaker 1

So today we are, Vijay, I'm testing Vijay's DSA skills. So Vijay is, as he mentioned, he's in IIT and he has, we were just interacting before this recording, he has solved more than 1300 plus problems. So let's see how Vijay will face this interview. Okay. Vijay, just before we get started with the DSA round, I have this practice of asking two common questions to almost every fresher or junior developers. Can you tell me what is time complexity in general?

### 00:01:05 · Speaker 2

Time complexity is like uh it's a time required for uh for the program to run

### 00:01:14 · Speaker 1

So let me give you an example then. So let's say we have a merge sort, okay? Merge sort of yesterday, so I was saying the same. So merge sort has 10 elements passed to merge sort, correct? Before asking that, 10, can you tell me what is the time complexity of merge sort?

### 00:01:28 · Speaker 1

Correct. Absolutely. So merge sort, you pass 10 elements. It will take some time to sort that elements. Let's say some millisecond, correct? So you pass now one crore elements. Probably it will take one second to sort the entire list, entire that particular elements that you passed. So now in this case, what is the time complexity of merge sort? 10 millisecond or one second?

### 00:01:28 · Speaker 2

In love and it's

### 00:01:50 · Speaker 2

It's based on the number of input number of the input basically it's based it's based on the input sure so if it is if the input is 1 million the time complexity is

### 00:02:06 · Speaker 1

Sure, sure. That is not the answer. Okay. Please read more about it after the interview. Audience, whoever watching, yesterday also I asked this. Today also I'm saying, please chuck. That's not how the time complexity works, but that doesn't make you any less. Okay. So now I'm sharing the question with you. Which I, okay. Can you please, I'll give you shared access as well. Okay. So audience, whoever watching, the link to the question will be there in the description section. It's not an easy problem. It's a medium difficulty problem. So this problem was recently asked in Google interview.

### 00:02:36 · Speaker 1

or fresher and one to two years of experience i've taken this question from i think glassdoor or lead code interview experiences okay let's see whether vijay can solve the problem and audience if you're seriously preparing for any product based companies so you can take this question also and start along with vijay the time duration to solve this problem is around 20 minutes it's a medium difficulty question 22 maximum is 25 minutes where first five to ten minutes we spend on the approach remaining time on the coding so you guys can also start coding like how vijay would do

### 00:03:06 · Speaker 1

Can you share the screen Vijay? Please read the question Vijay. It will go like this. You read the question. You understand the question. If you have any doubts, you can ask me. If you are clear about the question, you tell the approach to me. How are you going to solve the problem? Okay. Once you both fine with the approach, then you get started with the coding. Okay. So right now at the time of recording, it's 9.25. Completing this overall, we have maximum time of 25 minutes.

### 00:03:53 · Speaker 2

I'll reiterate the question if I understand it correctly. So I have initial supplies, some ingredients, some elements. So if I need to use those supplies and make recipes.

### 00:04:21 · Speaker 2

So for each recipe for each is for each recipe we have an ingredient where if I have those ingredients only I can make

### 00:04:33 · Speaker 1

The only thing you already read it may the whatever the recipe that are prepared can become ingredient for something else.

### 00:04:41 · Speaker 1

I mean keep on uh getting added

### 00:04:44 · Speaker 2

Yes

### 00:04:46 · Speaker 1

Take one or two minutes come with the right approach and let me know what you're gonna do

### 00:05:04 · Speaker 2

So currently I'm thinking of like a DFS kind of approach where where initially I have some supplies I can start with them I'll I'll iterate with the recipes

### 00:05:22 · Speaker 2

uh recipes let's say I I'll refer recipes as RR

### 00:05:29 · Speaker 2

I'll iterate through the R array. So R. So if I have for each for each R for each recipe, if I'll see the ingredients, if they're already in supplies, then I can prepare that. Correct. And I can I can add this recipe to the supplies.

### 00:05:52 · Speaker 2

And then I'll read it, I'll iterate again, like I'll keep on iterating. If I find, if I find, if I can, if I have all ingredients for that particular recipe, then I can prepare and I can add into the recipe.

### 00:06:08 · Speaker 1

What is the complexity that you're thinking time complexity of algorithm

### 00:06:16 · Speaker 2

say

### 00:06:18 · Speaker 2

Firstly I'm thinking I'm I'm reiterating to the to the

### 00:06:24 · Speaker 1

So basically you iterate through recipes correct

### 00:06:27 · Speaker 1

So let's talk about it

### 00:06:27 · Speaker 2

So let's talk about the honor of it let's talk about the recipes

### 00:06:30 · Speaker 2

and for each for each one i need i am checking for the supplies i'm i'll be checking in the supplies if it is present or not basically i'll i'll have one multi set or one set set of string to check whether the whether it's present in some supplies or not

### 00:06:50 · Speaker 1

So minimum in in the complexity of this would be R into N

### 00:06:51 · Speaker 2

I'm sorry

### 00:06:54 · Speaker 1

Minimum whatever you're asking for ingredients again you already know the ingredients correct

### 00:06:55 · Speaker 2

Yeah

### 00:07:00 · Speaker 1

You will extract the ingredients and you will check the ingredients in the the disarray.

### 00:07:05 · Speaker 1

But again I think it's not r into n r into i into n

### 00:07:10 · Speaker 2

R into I into log in basically like if I if I check in the in the in a set set of string it will be log in

### 00:07:18 · Speaker 1

A very set of strings supplies are also array right you will for converting

### 00:07:18 · Speaker 2

Where is set of strings

### 00:07:22 · Speaker 2

Like I can ah I can convert that into uh set up set right

### 00:07:27 · Speaker 1

You will convert that into a set you are all unique correct

### 00:07:30 · Speaker 2

Yes yes yes

### 00:07:32 · Speaker 1

So you are in right direction Vijay, but I would say probably you can optimize it even little further. Can you think of something? You are not totally wrong, but there is still scope for optimization.

### 00:07:47 · Speaker 2

So let me present some graph here. Let's say British

### 00:07:54 · Speaker 2

Independent

### 00:07:58 · Speaker 2

If I have some dependency directed graph

### 00:08:02 · Speaker 2

But it is dependent on

### 00:08:28 · Speaker 2

So can I do like this Can I do kind of stop a sort

### 00:08:34 · Speaker 2

So I'll have dependencies for each

### 00:08:39 · Speaker 2

each recipe correct so initially i have this initial initially i have supplies correct so if i try if i start with supplies whenever whenever

### 00:08:54 · Speaker 2

I'll be right back

### 00:08:57 · Speaker 2

Okay, so whenever whenever I traverse through the that particular supply if that is if the particular recipe is dependent on that I'll remove that it's

### 00:09:08 · Speaker 2

And if the dependency of that particular recipe is zero then I can actually prepare that

### 00:09:16 · Speaker 2

It's kind of directed graph and it's basically topological sort in the directed.

### 00:09:23 · Speaker 1

Are you comfortable implementing this in fifteen twenty minutes

### 00:09:26 · Speaker 2

S I think I can win

### 00:09:29 · Speaker 1

What will be the complexity do you think this is better than the previous one that you proposed

### 00:09:33 · Speaker 2

I should be better it's it's kind of for preparing the for making the graph it will be order of n okay I guess for each recipe I need to have ingredients it's order of n only and for uh for traversal for for the topological sort it's order of n only so it should be order of n

### 00:09:53 · Speaker 1

Sure get started then

### 00:10:46 · Speaker 2

Let me run uh three

### 00:10:52 · Speaker 2

Then yeah yeah please submit

### 00:10:53 · Speaker 1

Yeah yeah please submit yes yes please submit then we'll discuss the solution in detail

### 00:11:04 · Speaker 1

Let's let's get back to the pro solution again now. Okay, let's go through the solution step line by line. Explain me what is happening.

### 00:11:13 · Speaker 2

Yeah, yeah. So basically what I'm doing here is like, so for each of I have I have initial supplies. Correct. So for each recipe, there is one there is some ingredients which which that particular recipe is depending on.

### 00:11:30 · Speaker 2

So I'll have a I need to make that recipes

### 00:11:37 · Speaker 2

with the help of the supplies

### 00:11:41 · Speaker 2

So what I am basically doing here is like I know that each recipe is depending on the ingredients depending on something

### 00:11:50 · Speaker 2

So so I'm building the directed graph where the particular node is pointing to that their parents let's say here the breadth is here in the first example

### 00:12:06 · Speaker 2

In the first example here the recipe says bread and the ingredients are yeast and flour

### 00:12:12 · Speaker 2

So let's say I have three notes as bread yeast and flour

### 00:12:18 · Speaker 2

So I will be pointing that it just has east to bread and floor to bread. Basically what it means is like for bread it has two in edges.

### 00:12:31 · Speaker 2

That means two e two depends where they're for bread

### 00:12:37 · Speaker 2

So yeah, so I have the supplies. I'm starting with the supplies first. I'm basically for each for each supply if I encounter, I'll basically remove the the edges which is point pointing outward from there.

### 00:12:51 · Speaker 2

If I remove if I remove that the basically so for that for that particular parent for that particular parent I'm removing the dependency one one dependency dependency

### 00:13:04 · Speaker 1

Okay this part I'm not clear can you elaborate a little more like eastern floor have an inward edge to the bread that part I'm clear when you're gonna remove the edges

### 00:13:12 · Speaker 2

So let's say I'm actually I'm I'm given with the east floor and cone right? Correct. So I'll in the queue in the initial queue here I'll be having all supplies. So I'll have I'll have east floor and cone.

### 00:13:27 · Speaker 2

So now I'm I if I if I pop here I'll get uh east

### 00:13:33 · Speaker 2

So I'll see whether uh what all edges it's going uh it's uh it's pointing to what uh what are uh nodes it's pointing to

### 00:13:44 · Speaker 2

So let's say uh here east is pointed to bread

### 00:13:49 · Speaker 2

Here I use the degree, the map to store the degree where it stores that like for each node, what are the number of incoming nodes? Yeah. Pointing to that. That D represents the incoming, the number of incoming nodes. So for it, let's say I have east in my hand now, like let's say the S is east.

### 00:14:14 · Speaker 2

So now the from east it's pointing to bread

### 00:14:19 · Speaker 2

So that means bread is depending on the yeast

### 00:14:23 · Speaker 2

I I if I if I uh traverse the east if I if I traverse the east I can remove that edge from the edge from the bread so basically I'm removing one one edge which is pointing to bread I'm decreasing one dependency for for the bread

### 00:14:41 · Speaker 1

Got it got it tell me now what is it

### 00:14:43 · Speaker 2

I'm sorry.

### 00:14:44 · Speaker 1

I I got the gist yeah please please

### 00:14:46 · Speaker 2

Yeah

### 00:14:48 · Speaker 2

So if I if I have all if I if I had removed all the dependencies all the ingredients then I'll have the dependency as degree as zero that means there is no incoming edges to the particular node that means this implies there is no ingredient which is prepared I have all ingredients yeah so that I can prepare that recipe

### 00:15:11 · Speaker 1

got it so whenever one particular recipe is already done like eastern floor say you did the bread correct so the bread can be used for the secondary sub for making something else

### 00:15:20 · Speaker 1

So that how it is taken care hmm

### 00:15:20 · Speaker 2

Exactly

### 00:15:22 · Speaker 2

Yeah, that is taken care of because I added that particular element which is already prepared in the queue. So now if I encounter that, if I traverse that element, I remove those, the edges which is depending on that recipe.

### 00:15:40 · Speaker 1

Got it, got it. So now the line number 10 to 17, right? So this is the follow-up where you are forming the basic graph.

### 00:15:49 · Speaker 2

Yes yes

### 00:15:50 · Speaker 1

And actual processing is happening in after line number 20

### 00:15:53 · Speaker 2

Yes yes

### 00:15:55 · Speaker 1

So tell me now what do you think is the time complexity here

### 00:15:58 · Speaker 2

Yeah, here I'm using map here. I can use unordered map, but map is basically unordered map sometimes give order of n square order of n complexity to check that. Yeah, yeah. It depends on the implementation. It's hashing basically. Unordered map is implemented in hashing. Yeah. So I can trust that because it can give sometimes often time complexity. So I'm using map here, which is built on

### 00:16:28 · Speaker 2

of uh red black trees and banana trees so it it always its complex trees are log in or

### 00:16:37 · Speaker 2

So here the time complexity login into into the

### 00:16:44 · Speaker 2

order of n the number uh the number of recipes into the number uh the number of uh ingredients are in each recipe

### 00:16:54 · Speaker 1

So

### 00:16:54 · Speaker 2

Mm-hmm

### 00:16:56 · Speaker 1

log in into the recipes into the ingredients correct r into i into r into i into log in

### 00:17:00 · Speaker 2

I

### 00:17:02 · Speaker 2

Okay yes yes

### 00:17:04 · Speaker 1

Got it. And about what about the second part? The line number 20. So there you're processing.

### 00:17:09 · Speaker 2

Yeah, uh, it's it's order of n, it's basically order of n. Again, guess that's order of n.

### 00:17:13 · Speaker 1

I didn't get that

### 00:17:16 · Speaker 2

Plus order of it plus order of it

### 00:17:18 · Speaker 1

Right so supply is basically here in this case

### 00:17:20 · Speaker 2

Yes

### 00:17:21 · Speaker 1

kind of s plus r into n of log n

### 00:17:26 · Speaker 2

Yes yes yes

### 00:17:27 · Speaker 1

Okay, okay, got it. Which I just checked after the interview. I think it can be further optimized, I believe, as far as I have solved this in the past. Okay, definitely can check it out. But whatever you have come with is better than the initial solution that you proposed. You can stop sharing. Okay, so we'll discuss few things that which I honestly feel that there's scope for improvement and what you're doing good.

### 00:17:48 · Speaker 2

Yeah yeah

### 00:17:49 · Speaker 1

Yeah yeah please please stop sharing

### 00:17:53 · Speaker 1

So like I mentioned, this is a problem by Google. I have read this and I have also read it by Google engineer only posting it some places where this equation was asked. So good that you are able to solve. Couple of points on what are positive, Vijay. You very well know you already solved a lot of problems. So your problem solving intuition is very good. Like whenever you look at a problem, you can think of a multiple approaches because you have already solved so many problems, which is good. So you have to keep it up. Okay. And second, also the way you quickly

### 00:18:23 · Speaker 1

able to turn out from one approach to another approach correct so one probably propose i said you can optimize it further you thought to totally different approach and you are able to solve the problem in that approach which is very good third your typing abilities so a lot of times people undervalue this but you are able to write a solution after a discussion less than 10 minutes which is very good because many people are vocal enough to explain the solution but whenever they have to type right they start imagining where to put what and they will not be able to type so quickly okay so these are all very positive points which i the

### 00:18:53 · Speaker 1

which I think because of your tremendous practice of 1300 plus problems, you might have acquired it. One main thing that I suggest you to improve our audience whoever in in your particular level, communication vis-a-vis. Okay. Why I say is especially since you are from IIT, probably you would be targeting quite premium companies. Let's say Google, Amazon, et cetera. Simply I'm saying or you may not be. I'm just giving an example. So what happens is there's always you may not get an interview from our time zone, Indian time zone. All right. So we may get some some interview from US or some foreign.

### 00:19:23 · Speaker 1

interviewers as well. So in such scenarios, what happens is they would expect little bit of a more clear communication. You really know the answer viz. But sometimes like I also struggled with understanding. Then finally, I was able to understand the entire graph approach. But they will have even less limited time. As you know, Google, 45 minutes, you have to solve two problems. Correct. Medium, sometimes one hard or sometimes a medium and another medium also. So you have to communicate it so clearly that they understand the things. Correct. So rather the solution, the way you articulate matters.

### 00:19:53 · Speaker 1

matters a lot. First, if your articulation is good, they know what you are explaining, then they wouldn't ask a lot of questions when you're writing, correct? They are because they already know what you have said. Otherwise, they have to go through each line by line and ask questions to you for understand the solution. Okay. These are my honest feedback, Rajiv. If you have any questions, feel free to ask me.

### 00:20:12 · Speaker 2

Uh thank you for the

### 00:20:15 · Speaker 1

You have any other questions

### 00:20:21 · Speaker 2

Uh

### 00:20:22 · Speaker 1

Okay, nice talking to you Vijay. Okay, thank you. So audience, whoever have watched the video, in case if you solved the problem, please paste the link of the solution that you have done. Whatever Vijay has done, I'll take the link and I'll paste it so that you can refer to his solution. If you have solved, you'll paste the link. Vijay also will, I'll also review and we'll let you know in case the solution is good or there can be further optimizations possible. Thank you all for watching. Catch you in the next video.

