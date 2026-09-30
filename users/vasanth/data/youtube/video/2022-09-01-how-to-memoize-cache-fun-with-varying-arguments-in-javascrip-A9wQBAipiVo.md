---
id: A9wQBAipiVo
title: How to memoize/cache fun with varying arguments in JavaScript | Imp Question
  for top company Interw
date: '2022-09-01'
url: https://www.youtube.com/watch?v=A9wQBAipiVo
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ #javascript #interview #reactjs #frontenddeveloper #vasathBhat #uncommonGeeks\n\
  \n\nMemoizing a function is one of trickiest question that is generally asked in\
  \ premium company interview. There are some questions which you will never be to\
  \ answer, if you have not seen it before. This is one such kind. I have tried explaining\
  \ it very much in detail in this video. Please watch the video till the end. \n\n\
  \U0001F525 Learn Memosation in JavaScript \U0001F525 | Simplest explanation Ever\
  \ | Most important frontEnd Int topic: https://youtu.be/O7n9w_f9u9A\n\nLearn Sticky\
  \ Scroll Extension in Visual Studio Code and make scrolling very effective  https://youtube.com/shorts/VTkUjnS_y4o\n\
  \nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nMAANG series for frontEnd Developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN"
author: careerwithvasanth
duration: 00:19:26
model: saaras:v3
transcript: true
---

# How to memoize/cache fun with varying arguments in JavaScript | Imp Question for top company Interw

## Transcript

### 00:00:00 · Speaker 1

But here the question is not memoizing the previous results. Here it is to memoize the function itself. So memoizing the function might also be easy to a level but you need to memoize the function with varying arguments. Let's say there's a function called add that takes two arguments you need to cache it or memoize it. There is another function multiply which takes ten arguments you need to memoize that also. So it's not so...

### 00:00:25 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. In case if you're seeing me for the first time on the internet, I'm a content creator. I help people to clear their interview. I made a lot of beautiful series in the past which has been appreciated by many. I'll try to link them somewhere on the screen or in the description section. In case if you have not seen those series, please go ahead and watch the series. It will definitely help you to clear your interview. Now, coming to this video, it is super important video. Like you saw on thumbnail, I literally lost a very good package because I couldn't answer this question in the interview. There were three questions in the deciding round.

### 00:00:55 · Speaker 1

where one question I had answered perfectly right, second question was somewhat right. And this was a third question where interviewer was expecting me to answer fully but I couldn't answer. So whatever the number you are seeing on the thumbnail that is just subjective, that is not the exact package they offered me. I just put that so that you click down the video. But it is but it was a very decent package that I would have got if I would have cleared this if would have answered this question right. So the purpose of me making this video is in case if this question was asked to you in a very premium company, you shouldn't lose that opportunity of clearing the interview. So I'll explain this question very much in depth step by step, okay? So, this is the question.

### 00:01:40 · Speaker 2

the question

### 00:01:40 · Speaker 1

looks very easy, correct? So given a function, you uh given a function with a varying set of arguments, you need to catch that or you need to memoize that and you need to return the result. Very easy. So in case if you're someone who has a who don't know what is memoization, I tried explaining memoization very much in detail in my previous video. I'll try to link that this particular video in somewhere on the description also on the screen, okay? So please watch that video because I will not be explaining memoization very much in depth in this video because this will be only memoization of the function, okay?

### 00:02:10 · Speaker 1

watch that video and come to this video so that it will be helpful for you. Now, coming to this video, uh I'll just give a brief introduction about the memorization. In very simple words, memorization is nothing but caching the or the storing the result of the previous computation and using it for the next computation. Very simple example that I always give is factorial. Let's say you're calculating factorial of twenty and you've already calculated factorial of nineteen in the previous. So you don't have to calculate one to nineteen factorial again and then multiply that with twenty, correct? You can store the nineteen factorial and just

### 00:02:40 · Speaker 1

multiply twenty to that. That's the most easiest or the simplest explanation of the memoization. Where you catch the computation, catch the result of the previous computation and use it for the next computation. This is how the memoization works. But here the question is not memoizing the previous results. Here it is to memoize the function itself. So memoizing the function might also be easy to a level, but you need to memoize the function with varying arguments. Let's say there's a function called add that takes two arguments, you need to cache it or memoize it. There is another function multiply which takes ten arguments.

### 00:03:10 · Speaker 1

to memorize that also. So it's not super easy if in case if you already not done this in the past. So I'm gonna decode all the difficulties step by step and I explain you everything in this video. So please watch the video till the end. Definitely it will be helpful whether you apply for premium company or this will it will invoke your thought process and try to try to make it in think in a right direction. Okay? Now let's start with the coding.

### 00:03:34 · Speaker 2

hmm

### 00:03:34 · Speaker 1

So let's say you have a function add, okay? That takes two arguments. Number one, number two, all you do is very simple, you will just return number one plus number two. Okay? So let's say I log the results, add ten comma

### 00:03:54 · Speaker 1

twenty okay? twice

### 00:03:57 · Speaker 1

सो थर्टी थर्टी देयर इज नथिंग सुपरनेचुरल आई नो यू ऑलरेडी गेस्ट द आउटपुट। सो लेट्स से आई डू इट वन्स अगेन और वन मोर टाइम।

### 00:04:06 · Speaker 1

we are getting thirty four times. Obviously you got to know where I'm heading to. So, first time you calculated ten comma twenty, what is the output? There was no necessary to compute the remaining three values, correct? You could have just stored the result of the previous computation and returned it, correct? So, let's say you have another function called, I'm sorry. Let's say you have another function called multiply.

### 00:04:30 · Speaker 1

multiply that takes let's say three arguments. Number three. Number three and it will return multiplication of three arguments, okay?

### 00:04:41 · Speaker 1

So now, let's say you want to catch this as well. Rather, uh calling multiply with three arguments, let's say same function multiply with triggered with same set of arguments, ten, twenty and thirty. You don't have to compute the value again, correct? So, earlier in my last video I had shown how you will catch the result of this add function and return the result if the arguments are matching. But there is a argument so the results are matching, you will return the same same you won't calculate it again. But here the problem is you have to

### 00:05:11 · Speaker 1

you have to memorize the function add also and multiply also so you should write a general memorization function that will take different function and catch the function and return the results if it is already computed don't get confused okay I'll I'll explain the things step by step very much in detail okay to start off with to avoid confusion let's just stick to the add you have only one function called add let's learn how to memorize it

### 00:05:39 · Speaker 1

So, let's say I I write a function called function memoize, okay? Obviously as what is our requirement, we have to memoize a function. So this function should take a function as an input. Correct? Now, what we need to do here is, we need to you need to store the computation of the previous um if let's say function add ten comma twenty is passed once. Second time you pass add ten comma twenty. So what you need to do is you need to store that value somewhere.

### 00:06:09 · Speaker 1

and you need to return, correct? So the easiest way to do is use the property of closure, correct? So what I'm doing here is, I'm doing let cache

### 00:06:17 · Speaker 1

and I'm storing using an object. And how do I use a closure here? I will return the function, typical closure example basically. I'll return a function, correct? So, like we mentioned, you have already passed a function to a memoise. This function can take variable number of arguments, correct? So, for that I'm just mentioning arcs. It can take any number of arguments, correct? Then the then it is very easy. If you are able to do till here, then it is super easy. Now what we will do?

### 00:06:47 · Speaker 1

same like my last video. We'll put if and else, okay? If a value, a unique ID or unique key that exists in the cache, okay?

### 00:06:59 · Speaker 1

a unique key that exists in the cache, then you will return the cache that particular index. If not, you will actually compute the result and you will return it. If not, what I'll do, all we do is we have to call the function, correct? So we'll call the function with these varying arguments, okay? And we'll store the results in the cache, correct? But only cache here, only cache here at the moment is how do you uniquely identify the key, correct?

### 00:07:29 · Speaker 1

It was very easy if you are if you want to make it on the result basis. Let's say you are pass number one, number two, ten and twenty. If you are matching the arguments are same and return the result, then it was easy to form a key. Now here you have a function and its arguments. With its function and arguments, you need to form a unique key. That's all the task pending now. So how will I do that? So I'll do in very simple way, okay? Get unique ID, okay? This get unique ID takes a function.

### 00:07:59 · Speaker 1

arguments like we already discussed. What it will do? Let unique ID, I'm forming one array, okay? Then what I'll do is, uh it's very simple. unique ID dot concat function, I am forming, I'll explain, don't worry.

### 00:08:19 · Speaker 1

okay? Then I will return unique ID dot join. Maybe join is not required. Return ID

### 00:08:31 · Speaker 1

Okay

### 00:08:33 · Speaker 1

So, super easy. So, for example now, here function is add what we are passing. So function.name will be add. What is the arguments that we are passing? Number one, number two, okay, ten, twenty in the form of array we will be passing. So I'm concatenating all. So it will become add, comma

### 00:08:52 · Speaker 1

ten, twenty. Okay? It will be little look like this. Then I am joining all, okay? Then it will become after the join, how it will become? Add ten, twenty. So this is the unique key that I have formed now, correct? So this what I will do is I will call this from here.

### 00:09:14 · Speaker 1

Okay. Let unique ID, I don't have to do it here, I can do here. Let unique ID is equals to get unique ID, okay, you will pass function, comma arguments, okay.

### 00:09:26 · Speaker 1

Then, what you'll do is cash of unique ID, correct? Then you will return, don't worry if you're getting confused, I'll explain all these things once again, okay? Then you'll return cash of unique ID, if not, cash of unique ID is equals to this, again you will return the cash of unique ID only, okay?

### 00:09:46 · Speaker 1

Now, don't worry, I'll explain this once again step by step what is happening. Okay? So this you already know simple add function, correct? Now you are inside the memo is block, okay? So into into the memo is because as we have to memo is a function, you are passing a function into this memo is block. Then you are creating a simple local variable called cash. Then you form the closure. Why we are forming a closure? Because we need to have access to this cash even after the function is returned, okay? Now we have function that takes variable number of arguments, that was another requirement for us.

### 00:10:16 · Speaker 1

correct? A function that takes variable number of argument has to be cached. So we are taking variable number of arguments then we need a unique key in to form this cache object. So we have a key value pair like in the last last video as well. To form a key what we are using we have created a function called get unique ID, correct? So this get unique ID takes a function and arguments and it will form a unique ID like this and it will send it to us with no array actually.

### 00:10:42 · Speaker 1

and it'll send it to us. First let us go step by step. Okay? Let's call the get unique ID. Get unique ID with add function and ten comma twenty. Okay? Let's see what is the output that is returned from here just for your information. Okay? Then we will actually get into the complete block.

### 00:11:02 · Speaker 1

So we are seeing same like at ten comma twenty. So if you are really serious about preparing the interview by now you will see one problem happening here in the calculation of this unique ID. Can you guess what is happening in case if someone already noticed before I asked please mention that in comment section. If not I'll explain you. Let's say you are passing twelve comma thirteen. Okay twelve comma twenty three it became. So now this became a unique unique ID of the function correct. What all problems here

### 00:11:32 · Speaker 1

See, now this is same for add one twenty two comma three. A function add with one twenty two three also unique ID is same or a function with one comma two twenty three also it will happen the same way, correct? So, we have to enhance little bit by keeping some delimiter between the arguments, correct? So I am keeping a delimiter as pipe. So now if you see, so add twelve comma thirteen, twelve comma twenty three.

### 00:12:02 · Speaker 1

Okay. This one I'm removing, avoid confusion, Okay. So add twelve comma twenty three is never different key. Add one comma two twenty three is a different key now. Okay. Add one comma two twenty three is a different key. Then there is let's say one twenty two comma three is also different key.

### 00:12:25 · Speaker 1

correct? So why I'm showing this is this is super important because if you don't keep this delimiter like I said all the three combination will be treated as one one function with our arguments like the our code will not be able to differentiate between the three and it will return the memoized result for all of this which is unintended or wrong. Okay?

### 00:12:44 · Speaker 1

Now, let's go to the actual implementation. How to use this, okay? So I'm creating a variable called memoize add, okay? Then I call memoize, memoize and I'm passing the function of what? Add function I'm passing, okay? Now I do is very simple. Log, see, first you have to understand here. So I'm calling this memoize function with the function called add, okay? Then it is returning me another function, correct? So memoize add now basically a function.

### 00:13:14 · Speaker 1

That can take varying number of arguments, correct? So memo is add what I'll do now, I'll pass ten comma twenty, okay? I'll call it twice and here I'm I'm logging a value, I'm sorry, I should log out upper side log

### 00:13:33 · Speaker 1

returned from cache. Okay?

### 00:13:41 · Speaker 1

return from cash

### 00:13:43 · Speaker 1

not from cache. Okay? So, because first time it will go into the not returned from cache, second time onwards it will go to returned from cache. I'll explain again step by step, don't worry if you're not understanding, okay? Let me run the code to just to make sure we are having the right value. So not from the cache, returned from cache. Or else just to avoid confusion, just not from cache and from cache, okay? Fine. It is working well. Now I'll again explain step by step. If you're not understood so far, please listen to me once again and don't, don't stop watching here because I'll show how to add

### 00:14:13 · Speaker 1

another function also in the similar way. So now, we have a function called memoize add. So memoize and you're passing the add function to this block, okay? So you called memoize and you passed the function add, okay? So and it returned you another function. So this is invocable function. So now memoize add basically holds this function, okay? And as you know this function takes arguments, varying arguments, you can pass any number of arguments that has been passed here, ten comma twenty and ten comma twenty. And how this function is executed depending on the arguments you pass, first it will get the unique ID.

### 00:14:48 · Speaker 1

So first time when you had called ten comma twenty it formed add I'm doing a dry run now it formed a unique ID add ten and twenty as unique ID okay. So how okay just in case if you want to know I can log that also. So log

### 00:15:05 · Speaker 1

log cache object I'm logging for your reference, okay? So that you will only get to know how it has been computed. So basically first time the cache block was empty, the entire cache block was empty so we got not from cache. Second time we have added a key, this key and this value.

### 00:15:22 · Speaker 1

So now let's say you invoke the third time, okay? What will happen is it will just look whether this particular key exists. If the key exists, it will just return the value. It need not to calculate again, correct? Not from cache, from cache and from cache. So, so simple, correct? Now, Vasant's problem was not just this, not to just cache, add, you can cache all the other functions, correct? So just before I show how to cache other function, in case if you're liking the content I'm making, see this is not so easy to make a content like this. We have to, I have to do a lot of preparation.

### 00:15:52 · Speaker 1

make this content. So there is nothing wrong if you like this video on the YouTube. So please like the video. Add a comment what you are feeling is it the you are you getting benefited or something can be improved. Please add the comment. Just because you like and comment YouTube will give a lot of impressions to my video. So more impression then I can reach to more people that will help me to reach out I mean achieve my noble cause of helping people to clear their interview. So please like and comment to the video then continue watching. This is a humble request. Okay?

### 00:16:18 · Speaker 1

Now, so I will create another function now, multiply, okay? Multiply, multiply that takes three arguments, number three, okay? So number one star, number two

### 00:16:33 · Speaker 1

star number three. Okay? Number three. Now, same way what I'll do memo is add, I'll just replace with memo is multiply. Okay? Multiply. Memo is multiply. Okay?

### 00:16:51 · Speaker 1

Then what I'll do

### 00:16:54 · Speaker 1

just to avoid confusion I'm commenting I'll uncomment them okay. Then I'll have memoize multiply

### 00:17:00 · Speaker 1

I'll pass ten comma twenty

### 00:17:04 · Speaker 1

comma thirty, okay? Let me run the code. See same, multiply ten comma twenty comma thirty which is six thousand. So only once it is not from cache, rest of the two it is from cache, okay? So just to be sure, it is working well on both the functions, I'm showing you this, okay?

### 00:17:23 · Speaker 1

Okay

### 00:17:26 · Speaker 1

So it is working well on the both the functions. So this is this is the most simplest memorization concept that you can apply on the functions with a varying number of arguments. Lot of you who are coding JavaScript on a day to day might not be using memorization concept. I would highly advise please use this concept, okay? This will get you good review comments during your peer review and you also get lot of respect because you are introducing new things into the code, okay? And it will also save lot of computation. Let's say here it looks very simple, add and multiply with ten and twenty. What if we have so many

### 00:17:56 · Speaker 1

many different very large values. It will definitely save a lot of computation. Now, one last thing I want to mention is there are certain catch to this. Like this solution whatever I'm showing will not work for all the problems, okay? Let's say you are passing some anonymous functions here, instead of multi functions like this, if you pass anonymous function, this may not behave the similar way. And what if the you are passing a string argument and that contains the delimiter as pipe itself. So in that case there is an ambiguity in forming the unique ID, correct?

### 00:18:26 · Speaker 1

So I mean you can enhance it in the interview depending on whatever the feedback you will get, okay? I've tried writing one of the most simplest approach as possible, okay? And one more thing you might be observing whenever I'm scrolling, right? the my function header sticks at a place and rest I can scroll.

### 00:18:41 · Speaker 1

So this will help me in debugging lot of my code easily whenever the number of lines in the function increases. So how you can enable that in Visual Studio I've made a simple uh sixty minute YouTube shorts to explain that. I'll link that on the screen also in the description section watch that short if you also want to achieve this particular feature. Okay? So that's all about this video in case if you're not subscribed to Uncommon Geeks I highly advise and also request please subscribe to Uncommon Geeks I'll make lot of content like this which will help you to for sure help you to clear your front end developer interview. Okay? Thank you so much for watching if you're not subscribed like

### 00:19:11 · Speaker 1

said again, please subscribe. Read my medium blogs. I'll link to the medium blogs in the description. Lot of interview concepts like this I have discussed there. And all these questions I'll be adding into my GitHub repository. You can download the it from there and practice on your own. Thank you so much for watching. Catch you in next video.
