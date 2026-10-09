---
id: UjAVRuURFNo
title: "Learn How to solve Machine coding step by step | 2 year experienced @React\
  \ mock interview \U0001F680selected\u2705"
url: https://www.youtube.com/watch?v=UjAVRuURFNo
date: '2024-08-28'
duration: 00:34:48
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# Learn How to solve Machine coding step by step | 2 year experienced @React mock interview 🚀selected✅


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Karebath Basan's YouTube channel, previously known as Uncommon Geeks. My name is Basan, I hope you all doing well. As in this video series where we are doing a lot of mock interview with me, I have Faizan today, he's from Delhi. So more about Faizan, as you know, he'll only be telling you guys. But how this interview is gonna be, I'm gonna explain. Like most of the videos, I'm gonna start with a simple system design or like scenario given sort of a question, followed by some basics of JavaScript and React. Finally, we end the video by a quick machine coding question. Okay, that's how the interview is gonna be.

### 00:00:30 · Speaker 1

some reason faizan is not able to answer some questions i'm going to answer that the end of the video if he answers all the question well then probably i will not be doing so i also don't know will there be a post video or not that depends on how faizan will perform okay please watch the video till the end so that you will get benefited now faizan if you can introduce yourself we can get started

### 00:00:48 · Speaker 2

Uh yeah so my name is Fezal I'm from Delhi I'm working as a in AT6 agency so it's a service based startup as a senior front end engineer and I have around two years of experience

### 00:01:01 · Speaker 1

Good good question so we have overall two years of experience and where the two years of experience lies in the question

### 00:01:07 · Speaker 2

So it's basically in my initial career I was working in a full stack but later I switched to front end engineer and working on a React framework

### 00:01:18 · Speaker 1

Got it. Sure, sure. So, Faizan, let's start with one of the most common interview questions. Okay. I'm presenting a whiteboard now. Okay.

### 00:01:30 · Speaker 1

Whiteboard. One of the most common interview question in the system design recently is not recently, it's been quite some time is the news feed app. Okay. So I'm just drawing on the screen. Okay.

### 00:01:47 · Speaker 1

Hope you're able to see right

### 00:01:54 · Speaker 1

let's say and this is a typical facebook app let us imagine okay and we have like we'll have multiple posts here correct like for example post one post two okay followed by the remaining posts correct and on the top we will have an option to like create post correct so here you will have an option like where you could create post

### 00:02:20 · Speaker 1

like create post and this is like post one post two post basically this post one post two can be of anything like it could be of text it could be of uh image it could be of something between all the things that are possibility if isn't correct so now my question would be well let's start with one of the most common interview question around this that is infinite scrolling correct

### 00:02:35 · Speaker 2

No no no

### 00:02:44 · Speaker 1

So right now you're able to see two cards correct and whenever you're scrolling whenever you're scrolling up

### 00:02:51 · Speaker 1

happen is you will have like more cards

### 00:02:54 · Speaker 2

Ernds

### 00:02:55 · Speaker 1

be and control v if i do after you scroll probably you will have this as like post three correct this would become post three this will become post four

### 00:03:05 · Speaker 2

Was fort

### 00:03:06 · Speaker 1

Yeah, correct. Like I can make like an arrow here, like I can make an arrow here and I can like name it as after scrolling.

### 00:03:17 · Speaker 1

or users if I I can literally users have to see I think like this I think users can see like this is the

### 00:03:26 · Speaker 1

Initial render initial render

### 00:03:32 · Speaker 1

And shield ended okay

### 00:03:36 · Speaker 1

children okay and this is more like after user scroll okay

### 00:03:42 · Speaker 1

user scroll please tell me if you have to implement the infinite scrolling of is and why what are all things comes to your mind you can start explaining step by step and if you have to implement this how you are going to do that's for the example say consider an example of facebook like we are building system similar to facebook please start yeah

### 00:04:00 · Speaker 2

yeah so like uh on the header part so create post button is fixed one so i'll choose a sticky button so if we scroll it it should uh not uh be out of the window or out of the viewport so then what i'll think according to my user uh base and user experience like uh we will fetch uh suppose if two post is in the viewport uh and we decide

### 00:04:30 · Speaker 2

to put two posts in the viewport so i'll check the viewport height and according to it i'll fetch two extra posts uh for the initial rendering after if we will check the fourth post is like uh getting into the picture in the viewport then i'll fetch the next uh uh two posts and append it to my data

### 00:04:52 · Speaker 1

Okay

### 00:04:53 · Speaker 2

So I'll use this approach.

### 00:04:55 · Speaker 1

So yeah, whatever you told, correct, Reza. So basically, infinite scrolling, the whole point of infinite scrolling is how you are going to basically track the end of the page reached and even before the end of page reached or sometimes when the end of page reached, you are going to get next set of data and show it on the screen, correct? Can you start answering me like how basically you are going to determine whether the end of page reached or not?

### 00:05:20 · Speaker 2

Okay, so we can use viewport for it. We can check if scroll is the window is in the post 4 is in viewport. I don't remember the exit. Okay. I feel like I have not implemented it.

### 00:05:40 · Speaker 2

uh nine final

### 00:05:43 · Speaker 2

But we can check viewport size and all those things and there may be some

### 00:05:50 · Speaker 1

Okay, so somehow you're gonna identify the end of page reached.

### 00:05:53 · Speaker 2

End of the main screen yeah

### 00:05:54 · Speaker 1

Yeah and you're gonna make an API call to get next set of data

### 00:05:58 · Speaker 2

Okay

### 00:05:59 · Speaker 1

So now the there is another problem as you know that the one of the big problem pagination is you should keep getting the data from the server correct so are you aware of like different pagination techniques that is used from the back end or in general what are the different pagination techniques that are available

### 00:06:18 · Speaker 2

Uh so one I uh which I followed is like a limit and page number which we use uh to fetch the data

### 00:06:26 · Speaker 1

Okay please explain how you are gonna what is what data client pass what data we get from server can you elaborate

### 00:06:33 · Speaker 2

Ah yes, so in that technique, like we pass two parameters in the URL for a get endpoint. One is limit and one is page. We will check the limit, what amount of data we are fetching for a single time when API is calling and what sequence. Suppose I'm fetching two posts at a time and I need the post number five and six. So I'll do a page three and limit will be the same too.

### 00:07:03 · Speaker 2

uh very limit and post uh I can also check if uh the scroll speed and I can increase the limit in that case as well so

### 00:07:13 · Speaker 1

So basically you are gonna pass the number of posts required and the page number

### 00:07:18 · Speaker 1

Like for example initially let's say page one and ten so you're gonna get around ten

### 00:07:18 · Speaker 2

And Like for example

### 00:07:23 · Speaker 1

Then you're gonna say 10 is more like fixed letters hypothetically and second page and then again 10 posts correct 11 to 20

### 00:07:26 · Speaker 2

the

### 00:07:29 · Speaker 2

Yeah

### 00:07:30 · Speaker 1

Correct. So if only this could be the last question, then we'll go to other problems. See, one of the biggest problem that I can think of this approach is systems like Facebook, right? They are like very dynamic sort of a data comes. Like, for example, by the time you scrolled, probably there's so much of data that has come already. For the simplicity of you and audience, I'm saying, let's say there is 100 data on the backend. Okay. And you request for 1 to 10 in the beginning rendering. Correct. You got the data and you rendered it. By the time user hit the end of the page, obviously,

### 00:08:00 · Speaker 1

is more data might have come. So where more for simplicity understanding, let's say more 10 data has come, more 10 posts. So 100, whatever the earlier database size has become 110 now.

### 00:08:13 · Speaker 1

Correct. Obviously, the new data will not be added to the end of the database. It will be added in the beginning only, because that's the whole intent. Fresh post has to be shown. So now what would happen is we had one to hundred. So one to 10 was already came to client. Now that one to 10 became 11 to 20. A new one to 10 has come.

### 00:08:33 · Speaker 1

So next time now what you would do, you would send a request to server where you are sending like page two, where you are getting 11 to 20 is something that server should send. But what has happened now?

### 00:08:33 · Speaker 2

So next

### 00:08:42 · Speaker 1

11 to 20 is same as 1 to 10. You got my point right

### 00:08:45 · Speaker 2

Exactly

### 00:08:46 · Speaker 1

so this is the problem with this approach i am assuming audience got the problem where the window has slid it one to ten became eleven to ten new one to ten has come correct only just think uh is there any way you can answer to this question if this how to overcome this problem

### 00:09:02 · Speaker 1

Have any idea

### 00:09:05 · Speaker 2

a time of pagination as well we can take sort the data or something to new to old so we can tackle those problems

### 00:09:18 · Speaker 1

One approach is what you told is similar to that basically client takes care of it like let's say every time you got a data you check whether the data already exists or not this can be easily achieved if you are maintaining a map of like post id and actual post content we can easily check whether that post data is already present or not and if it is already present make a next request okay but the problem is how long to keep doing this this becomes recursion

### 00:09:45 · Speaker 1

I gave you simple example where 1 to 10 we can 1 to 20 it not necessarily be like that correct it might have like by the time you make level you decide to make next call next call also the data might have slid it

### 00:09:57 · Speaker 1

get you know what I'm saying you send to it becomes free but uh

### 00:09:59 · Speaker 2

I'm not too big a stretch

### 00:10:01 · Speaker 1

11 to 20 might have become 21 to 30. So you might end up getting same result, correct? Again, no right or wrong implementation depends on the system we are building. But more, you and the audience read more about this. There is two types of pagination mainly, the cursor based and the offset based.

### 00:10:05 · Speaker 2

I don't know

### 00:10:15 · Speaker 1

So right now what we decide is offset based approach. There is another thing called cursor based approach. Okay, please you and the audience, if anybody in the audience know, please mention what is cursor based approach. Okay, so Faisal and now let us start with some very basic theory questions I'll ask you and then we'll go to the some coding things. Okay. So can you present your screen Faisal with code sandbox opens? Sure, okay. I must say you already signed in, correct?

### 00:10:38 · Speaker 2

I'm sure you already

### 00:10:40 · Speaker 2

Yes yes

### 00:10:41 · Speaker 1

Please explain me uh Faizan what are fragments in uh JSX or fragments in React in general

### 00:10:47 · Speaker 2

Okay, so the React, there is a big challenge like when we want to wrap a component with some extra things, suppose we need to write a box and we don't want to use a nested divs and all so the DOM will not become a heavy. So we use the fragment. Fragment is a empty wrapper. It's kind of empty wrapper which can be used in React to used in

### 00:11:17 · Speaker 2

virtual DOM so it will not be appended in the real DOM so we call it fragment it is a feature of React

### 00:11:27 · Speaker 1

Can uh so we can

### 00:11:27 · Speaker 2

Uh so we can use the

### 00:11:29 · Speaker 1

You can give a simple example person when to use fragment

### 00:11:33 · Speaker 2

Uh yeah so uh if uh you want to append something like uh this is a project I don't want this dev to be presented on the DOM so I just need uh we can use this empty fragment in that case okay or we can import the fragment from uh uh React correct uh yes so these are the two ways

### 00:11:57 · Speaker 1

these are the two ways i get what you're saying but i think the simplest answer is a tag a group of tag cannot exist by themselves they have to be enclosed by something that's the basic logic correct you can have h1p and any other list tags so they cannot be represented just like that where it should be enclosed in something

### 00:12:08 · Speaker 2

Thank you guys

### 00:12:14 · Speaker 1

So either you could enclose them in div or either you could enclose them in fragment, correct? Or either you could enclose them like empty thing we added, empty and the empty opening and empty closing brackets. Three three possibilities of is and correct. So now can you tell me the difference of is and just using the fragment?

### 00:12:23 · Speaker 2

Three three positive

### 00:12:30 · Speaker 1

And no fragment just opening and closing what is the difference

### 00:12:34 · Speaker 2

So the main problem I face like uh in my day to day development like we cannot pass key to an empty uh fragment but we can pass the key to this fragment right

### 00:12:46 · Speaker 1

Why do you think you need to pass a key What what is the need for that?

### 00:12:49 · Speaker 2

When we need to append an array of a data or an object we need to pass a key to every element we are mapping

### 00:13:01 · Speaker 1

Um and what is the problem using the DU versus a fragment?

### 00:13:07 · Speaker 1

What is the difference of putting another fragment enclosing within a fragment and enclosing within a D? What is the difference?

### 00:13:15 · Speaker 2

So suppose if a styling is given to a parent child, it will not, if we enclose it with a div, it will not be implemented to a child tags. But if you use fragment, the parent div, if you will give the styling, so it will be reflected too.

### 00:13:34 · Speaker 1

Sure and you just then it comes to your mind uh present

### 00:13:37 · Speaker 2

The DOM become heavy like if we use div multiple divs we are some of the divs are not used even to any container or something

### 00:13:47 · Speaker 3

So but if you use fragment we can

### 00:13:50 · Speaker 1

Got it. So fragment you say lightweight compared to div and as we feel like div is not at all necessary it is just a necessary requirement as div is something a meaningful tag a division basically.

### 00:13:56 · Speaker 3

Hmm

### 00:14:01 · Speaker 1

we don't want that that time we could use the fragments okay sure so um you want to say anything present or

### 00:14:10 · Speaker 1

Sure sure so now probably we can get started with the problem but just before that I have only one question what are children children prop in do you can you please explain children prop

### 00:14:22 · Speaker 2

Okay, so suppose in a component, let's, should I show you an example as well?

### 00:14:31 · Speaker 1

No I think roughly you can explain if I needed I like uh so

### 00:14:33 · Speaker 2

So if we are children is a inbuilt prop in JavaScript. So suppose if we are we are creating a component, suppose we are creating a button component to reuse it everywhere. So if we wrap that component. So for if suppose this is a component we created for React. So inside all the code, all the code inside that component will be passed to its children prop.

### 00:15:01 · Speaker 1

Mm

### 00:15:02 · Speaker 2

So we can access those children prop inside that component

### 00:15:07 · Speaker 1

Okay, let's say you want to render the children. So everything that is inside that particular component gets can be used, correct?

### 00:15:14 · Speaker 2

Yes

### 00:15:15 · Speaker 1

Can you give me one practical example of where you felt like you used this when is the right scenario to use a children plot

### 00:15:22 · Speaker 2

So one example I already gave like when we create a bot button component, so there we use multiple times like a children prop. Suppose I created a component called app button. So I can reuse that component and the text inside it, I can pass it as a children. So I'll track those children and I can pass an empty button. Like I can use a button tag inside my component and pass it inside that.

### 00:15:52 · Speaker 2

children inside the curly bracket I can use the children prop and append the text

### 00:15:57 · Speaker 1

Okay, sure. I'll send a question to you in the chat section now, Faisal. You have around 15 to 20 minutes to solve the problem. Copy the question based on the here on the editor. And you can maybe zoom in this for a while, a little bit so that audience can see it better. If any question regarding the problem, you can ask me. Others, you have to get started.

### 00:16:17 · Speaker 2

So search filter display a list of posts implement a search bar and filter the list based on user input get okay so okay here I need to implement a display a list of posts using this API

### 00:16:34 · Speaker 2

and I'll use a and need to implement a search bar. Correct. If a search bar is mentioned, like we need to search the M, whatever we search, according to it, we need to append the post.

### 00:16:52 · Speaker 1

Can you open that URL once the JSON placeholder URL can you open it

### 00:16:55 · Speaker 2

Newfoundland

### 00:16:57 · Speaker 1

So here let us search by the title

### 00:17:01 · Speaker 1

as I think that is little lesser length. So let's say in the first case, I search S-U-N-T and let's for the simplicity sake, let's imagine any title that starts with S-U-N-T should show.

### 00:17:16 · Speaker 2

Okay so any type of chart a query yeah

### 00:17:17 · Speaker 1

Any type of data query. Yeah, sure. No, they're not going to give that. They're only giving that post. I don't, okay, you can chuck if they're giving. Otherwise, that's that filtering is something that you need to do, not on the API.

### 00:17:31 · Speaker 2

Okay

### 00:17:32 · Speaker 1

So you have any questions

### 00:17:32 · Speaker 2

We have to implement them

### 00:17:33 · Speaker 1

Whenever you do the search, it's more like not like search, it's more like local search, not like the global like search.

### 00:17:38 · Speaker 2

Sorry

### 00:17:39 · Speaker 1

In the data that you already got perform a search okay

### 00:17:42 · Speaker 2

Okay okay

### 00:17:43 · Speaker 1

Sure get started

### 00:17:46 · Speaker 2

Okay so I'll create a post uh state

### 00:17:51 · Speaker 1

Okay

### 00:17:51 · Speaker 2

so that I can store the states I can store the data in a state so I'll use the u state to store the state and for initial I'll use the empty state

### 00:18:06 · Speaker 1

Good

### 00:18:07 · Speaker 2

So uh I'll create a function uh

### 00:18:14 · Speaker 2

to get the state

### 00:18:19 · Speaker 2

Okay

### 00:18:23 · Speaker 2

I'll be needing a exos I can use it to fetch the data exos exos as a API client so I'll use exos.get

### 00:18:39 · Speaker 2

I'll use uh the async function to let uh be more clear like

### 00:18:45 · Speaker 1

Hmm

### 00:18:45 · Speaker 2

I can get more clear I'll fetch the data

### 00:18:51 · Speaker 2

Watch the response

### 00:18:55 · Speaker 2

I'll use async await

### 00:19:01 · Speaker 2

Let me first console the other set I believe we should get inside the response dot data so set hosts

### 00:19:22 · Speaker 2

Very loose

### 00:19:24 · Speaker 2

I'm gonna play now the boss

### 00:19:39 · Speaker 2

function literally

### 00:19:46 · Speaker 2

Such things

### 00:19:56 · Speaker 2

Almost

### 00:20:08 · Speaker 2

Interesting

### 00:20:14 · Speaker 2

Okay sorry

### 00:20:17 · Speaker 2

Um

### 00:20:24 · Speaker 2

Um there I do is

### 00:20:31 · Speaker 2

And here I'll give what key is

### 00:20:35 · Speaker 2

Gosh

### 00:20:40 · Speaker 2

Yes okay but my post is not visible yet

### 00:20:55 · Speaker 2

use in the use effect i'll call the get data function so that if when my component get mounts uh the get post will call and data will be stored in this so i have not imported that zeros

### 00:21:24 · Speaker 2

Okay so currently I'm getting all the data

### 00:21:31 · Speaker 2

I prefer to

### 00:21:36 · Speaker 2

So we need to create a search bar

### 00:21:44 · Speaker 2

will be a type of text and I'll create the another state with input

### 00:21:55 · Speaker 2

Right

### 00:21:57 · Speaker 2

With a memory stream

### 00:21:59 · Speaker 1

I think that input spelling mistake yeah input

### 00:22:04 · Speaker 2

Oh yeah so I'll give a value to it as input

### 00:22:12 · Speaker 2

And if uh on on on change event I'll

### 00:22:21 · Speaker 2

on it as E

### 00:22:26 · Speaker 2

set input and set e dot target value

### 00:22:34 · Speaker 2

So this is a control component now

### 00:22:36 · Speaker 1

Uh

### 00:22:42 · Speaker 2

I'll change it

### 00:22:44 · Speaker 1

Styling we'll check later okay basic one you give next we'll check the styling later yeah

### 00:22:56 · Speaker 2

Uh yes, so suppose this is working fine as of now. So I'll do one more thing, like I'll write a use effect.

### 00:23:07 · Speaker 2

where I'll give a dependency as input so whenever input will render so it will change so my this use effect will be called so and now I'll check

### 00:23:26 · Speaker 2

input is suppose

### 00:23:34 · Speaker 2

I need to do the filtering in in filter logic as well

### 00:23:42 · Speaker 2

exposes

### 00:23:45 · Speaker 2

I'll create a function

### 00:23:54 · Speaker 2

So every time this will call I will

### 00:23:58 · Speaker 2

do a filter data

### 00:24:04 · Speaker 2

And I'll write another state

### 00:24:09 · Speaker 2

get that

### 00:24:16 · Speaker 2

So this query data I'll use to pass suppose if the input box is empty so I'll try to get the filter from all the posts suppose if I'll search for S U M T so it will all posts will be stored there and I'll show the filter state here only so I'll pass it here for now.

### 00:24:45 · Speaker 2

So for the initial rendering like uh

### 00:24:51 · Speaker 2

And suppose data if uh if post is also changing

### 00:24:58 · Speaker 2

And if inside if input is empty

### 00:25:04 · Speaker 2

That is a falsy value so I'll set query data as post

### 00:25:11 · Speaker 2

so i'll show all the data if input is empty the code will get uh

### 00:25:19 · Speaker 2

Uh I'll get uh

### 00:25:21 · Speaker 1

I get it

### 00:25:21 · Speaker 2

Something in the input first time when it is empty

### 00:25:23 · Speaker 1

First time minute is empty we are gonna return all our next time

### 00:25:26 · Speaker 2

Next and all the things

### 00:25:29 · Speaker 2

filtered uh data now i'll i'm gonna filter it so i'll filter from the post so that i'll get the filter from all the posts so i'll filter it post dot

### 00:25:47 · Speaker 2

And I'll check uh with the post and if post dot title

### 00:25:58 · Speaker 2

begin with like uh post.title will be a string so i'll use include i can use uh so i need to return all the things or it will only start suppose s and p is in the bit

### 00:26:12 · Speaker 1

That begins with the given search string that you return complete title

### 00:26:20 · Speaker 2

Okay we're gonna do this one

### 00:26:31 · Speaker 2

That may be a

### 00:26:34 · Speaker 2

starts with

### 00:26:40 · Speaker 2

I don't know

### 00:26:46 · Speaker 2

So to start with we have a function

### 00:26:49 · Speaker 2

start

### 00:26:55 · Speaker 2

starts with okay we have a function called starts with

### 00:27:00 · Speaker 2

I'll use it as an input. If so, this will give me a filtered data. So I'll put set in set.

### 00:27:10 · Speaker 2

query data as

### 00:27:14 · Speaker 2

Uh

### 00:27:18 · Speaker 2

to data

### 00:27:22 · Speaker 1

We have last three to four minutes okay

### 00:27:24 · Speaker 2

Okay uh yeah so now if I'll check uh with this is S-U-N-T

### 00:27:30 · Speaker 1

Good

### 00:27:32 · Speaker 2

getting this but I'm not sure why I'm getting this as well

### 00:27:37 · Speaker 1

Try EXA also let's see

### 00:27:40 · Speaker 1

exe

### 00:27:44 · Speaker 1

It's not coming correct

### 00:27:50 · Speaker 2

feature

### 00:27:57 · Speaker 2

Okay, I need to figure it out like, uh, is this working correctly?

### 00:28:08 · Speaker 2

Okay post dot title we have a post dot title

### 00:28:17 · Speaker 2

S U N T is working fine. Q U I is working fine.

### 00:28:26 · Speaker 1

I think it's a completely one string I think this is completely one string

### 00:28:26 · Speaker 2

I think that's a complete hub

### 00:28:29 · Speaker 2

Okay yeah okay okay yeah

### 00:28:31 · Speaker 1

It's got exactly that a good try could be

### 00:28:34 · Speaker 2

cycle be better a cycle yeah

### 00:28:35 · Speaker 1

Yeah

### 00:28:38 · Speaker 2

you

### 00:28:46 · Speaker 2

And yeah I can't get it

### 00:28:53 · Speaker 2

Okay I'm not getting the due to stability okay

### 00:28:57 · Speaker 1

Anyway, I think that is fine. Most of the things are working as expected, correct? Looks fine.

### 00:29:09 · Speaker 1

Anything else you want to make change person or we can discuss

### 00:29:13 · Speaker 2

Ah yeah I am King Bang

### 00:29:15 · Speaker 1

Sure so yeah uh can you just uh I mean zoom out the right side portion a bit I mean like the minimize the post this side

### 00:29:24 · Speaker 1

I mean except the code minimize everything so that audience can also look at the complete code once

### 00:29:29 · Speaker 1

Sure can you zoom in again maybe control plus command plus

### 00:29:34 · Speaker 1

So basically, I'll just quickly summarize for you. What we are trying to do here is we have two functions. One is get post and another is filter data. So get post is where we are making API call to get the data. Filter data is where actually we are filtering the data to match whatever the user has searched. Are we matching with that or not? Correct. We have two use effect we have used. One for can you scroll down? Yeah. So one for like filter the data and the one is for the getting the post. first anyhow line number 37 gets triggered where we get the post and we are line number 33 that every time whenever the

### 00:29:55 · Speaker 2

Mm

### 00:30:04 · Speaker 1

input whatever your typing is changed or every time another post is changed basically only the first time the post would change we are calling the

### 00:30:11 · Speaker 1

Finally whatever we are rendering on the UI is the filter data

### 00:30:15 · Speaker 1

That's what we are rendering on the page. So now where do you think actually the posts are getting used in line number 25 for filtering purpose? Correct. The posts are used only.

### 00:30:15 · Speaker 2

Thank you

### 00:30:16 · Speaker 2

on the page

### 00:30:23 · Speaker 2

Yes exactly got it

### 00:30:24 · Speaker 1

got it sure sure so um we'll discuss phazon this and the overall about how what are all how the things went well see regarding this uh phazon the very clean implementation i have so many mock interviews on my channel this is one of the cleanest mock machine coding ground i know the question is fairly easy it's not i'm not saying it's very hard but still the approach you took step by step you are able to do which is very clean and neat which is kudos to you okay few things as i as an interviewer see that could have improved was one is the api call

### 00:30:54 · Speaker 1

Correct if you go to the get post can we go to get post please

### 00:30:59 · Speaker 1

So here in line number 17 is, you know, we are not handling any error here. The app can easily crash.

### 00:31:03 · Speaker 2

I can see you

### 00:31:04 · Speaker 1

All right, if you're doing this. And another thing, one of the common mistake almost everybody does in the machine coding interview is like not asking the obvious question. See, I shared you an API and there is some X number and you started your implementation. What if that API tomorrow returns 1 million data?

### 00:31:22 · Speaker 1

getting appointed then the filter will filter sufficiency will be totally degraded line number 25. right this is not a problem this is just where probably in next interview whenever some questions are asked you can think around it. right because always make sure you ask the extremities what is an extremity

### 00:31:34 · Speaker 3

So it's all based

### 00:31:38 · Speaker 1

What is the minimum value? What is the maximum value in the interview so that always you're gonna be safe, correct? Otherwise, there could be chance. Now, this is fine, it's a mock interview. Then interview has like 1 million data is there, then the filter would fail, correct? It's not if it would fail, the performance is awful, obviously, it will get reduced, correct? And another thing that I noticed.

### 00:31:53 · Speaker 2

Thank you

### 00:32:01 · Speaker 1

I think rest look good to me it's some very clean approach but only couple of suggestion that I give you can stop sharing Faizan and I have like some couple of other feedback not specifically on the problem solving around the basics like the couple of questions that I ask like newsfeed correct where we started with yes newsfeed I'm not expecting a two-year guy to like know all of it about the newsfeed like I always say in my mock interviews like think look at every system like how do you develop it like just before we we actually we dream

### 00:32:24 · Speaker 2

Like you

### 00:32:31 · Speaker 1

entire thing in there that whiteboard or the drawing board correct so next time whenever we look at the drawing board don't look at it like a user look at it like a developer if you have to build a drawing board how we are going to do same applies for the facebook newsfeed right that is the easiest way to start understanding the systems like how you become so whatever answers you told was not fully correct or not even wrong one approach you told whatever you would build it but i would highly suggest you to you and all the young developers that starting journey two to three years of experience to look at every system like

### 00:32:47 · Speaker 2

But this

### 00:33:01 · Speaker 1

do you build it so that whenever such questions are asked in the interview most likely you'll be able to answer i'm sure most companies do not have system design for two to three experience but they would have some of a scenario driven question like some portion of the system just how do you guess the output for example that's i think that's something that you could improve on and regarding fragments and other things what i feel one common thing around the theory questions is you know answers to many you are able to give answers but the initial answer that you are saying is not the answer eventually you are coming to that answer

### 00:33:31 · Speaker 1

So for example fragments

### 00:33:32 · Speaker 1

What is the use of fragments? Basically, the list of tags has to be enclosed in something. So you are using the tags, correct? So you told it actually, but you came there eventually, correct? You can tell that to the point answer to you and the candidate also, because some interviewers are like have time enough time to like discuss and extract the answer. Some interview will be in rush where they'll not have time to like extract answers out of your sentences, Faisal. Okay. That's all I wanted to say. You have any questions you can ask me, Faisal, or you can share your interview experience also.

### 00:33:42 · Speaker 2

Does it

### 00:34:04 · Speaker 2

Yeah, so it was a nice experience for me. Like, uh, I have been interviewing after a very long time. So, uh, it, it is a great experience. And the questions I didn't expected, like, uh, these type of questions. I didn't watch a lot of video of yours. I have watched some of them.

### 00:34:22 · Speaker 3

And so

### 00:34:23 · Speaker 2

uh it met with my expectations so i got a very good feedback i got a very good questions and this will help me to like improve and how i can structure my answers and all those things

### 00:34:35 · Speaker 1

Thank you so much, Faisal. I hope like all the audience who watch the video, like the video, like how Faisal told you, if you like the video, please like the video, comment whatever you felt honestly, please share the video with your friends so that they can also get benefited. That's all for this video. See you in the next.

