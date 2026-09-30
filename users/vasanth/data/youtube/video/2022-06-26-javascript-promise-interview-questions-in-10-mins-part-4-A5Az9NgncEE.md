---
id: A5Az9NgncEE
title: Javascript Promise interview questions in 10 mins (part 4)
date: '2022-06-26'
url: https://www.youtube.com/watch?v=A5Az9NgncEE
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ JavaScript being single threaded programming language needs some way  to execute\
  \ asynchronous task. Promise is one such method. It is considered be one of the\
  \ most common and tricky interview topic. I will be covering each and every aspect\
  \ of Promise in this video series. \n\nDoes async await block main thread in JavaScript:\
  \ https://medium.com/p/c07db9c48c3e\n\nPromise video 1: https://youtu.be/1OINZhOIh0c\n\
  Promise video 2: https://youtu.be/3V-fKuh1-8w\nPromise video 3: https://youtu.be/7a3ZwYko05s\n\
  \nEvent Loop - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop\n\
  Promise - Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all\n\
  My Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:09:51
model: saaras:v3
transcript: true
---

# Javascript Promise interview questions in 10 mins (part 4)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Gigs. Myself Fasant. I hope you all doing well. So today's topic is, as you already know, we are continuing with the promises and this video also we're going to discuss about promises. Some important aspects of promise I'll be discussing. This is not mainly on a Q and A kind of a video. Definitely there are good, I'll be asking some questions and I'll also be answering. But it's more like question and the concept explanation both. I'll try to give you scenario and in that scenario what concept you have to be used. So it's a preparation for interview only, but I'll also touch base a little bit about the different concepts.

### 00:00:30 · Speaker 1

Okay? If you have not watched my previous videos about the promise, I'll try to link somewhere on the screen and also in the description section. Please go ahead and watch it. If you have not watched those and suddenly landed in this video, then it may be slightly difficult for you to understand, digest everything. Okay? Without wasting further time, let's get started. See, I'm starting from the same same block wherever we we we stopped in the last video. Okay? And continuing from there itself.

### 00:00:55 · Speaker 1

So we have three promises and we have output of the three promises added and we are showing the output and if it goes to error we are showing the error. Now very first question here is you know in every every website or a mobile application whenever the API calls are happening we kind of show loaders on the screen. Correct as spinners what we call. So until a API call is successful or it becomes failure we continue to show the loader. My question here is which is the right place to start showing the loader and which is the right place to stop showing the loader.

### 00:01:25 · Speaker 1

So the implementation of how you use the loader could vary across ReactJS, Vue.js, React Native or any other JavaScript framework like how do you bind that variable to a loader etcetera. But the fundamental concept remains same and everywhere you will have a similar way of invoking the promises. Okay when there are more than one etcetera. What most people would do is they will have a let show loader and they'll set it to true. Okay?

### 00:01:49 · Speaker 1

And what they do after the promise is resolved, they'll set it to false. They would do the same in the catch block also. Okay? This is a typical implementation of show loader by most of the engineers and whatever the code review I have done, everywhere I do see this.

### 00:02:04 · Speaker 1

So, this is fine, it will absolutely works well. But the question here is, we this line cannot be avoided because somewhere it has it should start and we should set it to true. But this line number thirty five and thirty nine, we have a same code, correct? So, very first thing as a developer, what should come to should come to your mind is, any block you are using more than once, is there a way to remove from the both the place and put it in a function?

### 00:02:30 · Speaker 1

or in some utility file anything. See, the hundred percent we cannot do that. There will be sometimes we can we have to rewrite the code, but there are many times where we can avoid this. So we can easily avoid this by a small concept of graduation. Most of you might have studied try catch and you might have also studied finally and on a day to day practice will miss out finally. So rather keeping the code in both try and catch, you can easily put this code in finally.

### 00:02:57 · Speaker 1

Right? What we have to do is when whether whether AP call is successful or a failure, finally we cannot show the loader, correct? Whatever on the failure like you have to show error state that you do here. If you have to show data, you do that here. But loader to you have to stop. Try catch whatever happens. So that is something can be easily achieved via finally. Why interviewer would ask this question is very first to understand your knowledge of exception handling. Do you still just know try catch or you know anything else also, number one. Second, how you are how hard you are trying to avoid

### 00:03:27 · Speaker 1

of code. Okay? So these are these these are not the theoretical skills, these are the practical skills. Only if you have done on a day-to-day basis coding in a particular concept, you will be able to answer this. Okay? Now, this is about the question number one. Question number two.

### 00:03:40 · Speaker 1

See here three awaits we are doing for three promises, correct? And this execution is sequential, after one we are going to two, then we are going to three, okay? Let's take a practical example of a website, of a e-commerce website. So first they'll show the banner where something should be sliding. Second we will have a recommendations, our recommendation depending on our past purchase history. Then we'll have a third block where they'll be showing hot topics, hot things that are being sold today. Okay, three sections are there. Now, these three blocks can be loaded parallelly.

### 00:04:10 · Speaker 1

And once the data comes, they will be rendered in a particular section. They do not have to be loaded in a sequential way. Correct? So, say similar example, let us apply here. We have three functions, three three promises, and we can avoid calling them sequentially and we can call them parallelly. So how to do that? This is my question.

### 00:04:27 · Speaker 1

Okay. So only if you know the concept of only if you know much about promise you'll be able to answer. Since I haven't explained that in any of my previous video, I'll explain that concept to you. But question you got. You have multiple promises and you don't have to call them sequentially. Problem calling sequentially is this takes two second, this take two second, this take two second, so you end up having six seconds. Okay. Rather, if you call all the three at once, they end up taking they start at same time, so they would take up around three second two seconds. Because each promise takes around two seconds, so

### 00:04:57 · Speaker 1

everything called in a parallel way and they all end up taking two seconds each. Okay, approximately not exactly, each two second. Now, what there is a way in there is a way in JavaScript how this can be achieved. Okay, that is with a concept called

### 00:05:16 · Speaker 1

promise, uh, promise.all, okay? It takes

### 00:05:22 · Speaker 1

it takes promise array as an input, okay? I'll explain you in detail after I type.

### 00:05:29 · Speaker 1

Then I have three. Okay. So what I'm trying to do here is rather calling each promise one by one. I have a function called promise.all and this will execute and it will take input as array of promises. It will call all the promises and whatever the output that has come for one, two and three that will be passed to output and will show the output. If there is an error, it will go to the error block. Let us see what is the output.

### 00:05:58 · Speaker 1

So output is one, two and three because all the promises got resolved. So we got one, two and three as our output. Okay? Let's say if any promise fails, third promise I'm failing. Okay? I'm rejecting, then what will happen is

### 00:06:14 · Speaker 1

error is three. So either promise.all behavior is this, either you get output for all the promise or you don't get output for any promise. So putting other way, let's go back to the same website example where we have banner, favorites or recommendations and the hot hot picks of the day. So if any data is not there, then don't show any other data. Like banner doesn't come, then don't show below two. This doesn't come, then show don't show above and below. So if that is your logic, then promise.all is a best suitable for you. So there are a lot more things to read.

### 00:06:44 · Speaker 1

promise.all, you can read that here. I'll try to add this link also in the description. Method takes iteratable promise as an input and returns single promise that resolves an array of results as an input promises. It's if I start explaining line by line here it will become difficult for you to understand, but I've already explained the practical use case how you can use the promise.all. Okay? But there is a scenario where I'm going back.

### 00:07:08 · Speaker 1

where you don't have to wait for all the promises to be resolved. Okay? There is a nice example is same, the same website with three sections. What most website do is they don't stop loading other two section if one section is not loaded. Correct? What they try to do is they try to show loader in that particular section, then maybe retry option etcetera and show the whatever the block that has been come. Correct? So in that case you don't have to do all, there is another function called all settled. Okay? So what all settled does is

### 00:07:38 · Speaker 1

it will wait for each promise to be resolved. And whatever the value of each promise, like whether promise is successful or a promise is rejected, it will give that summary. So if you see here,

### 00:07:51 · Speaker 1

So status, this is the first promise. So value one, it got fulfilled. This is the fulfilled value two. Third one is rejected, reason is three. So advantage of using this is, it doesn't wait for any promise to be completely resolved or rejected. It will wait for, I mean, it doesn't wait for any promise to be resolved or rejected. Whatever happens, it will, it will take that value and store it and finally returns that as a array. So now we know third one is rejected. So you can have a logic to identify which promise got rejected, then handle it.

### 00:08:21 · Speaker 1

separately. Okay? That's how you can use promise.all and promise.all settled. Okay? There are few more functions inside promise. So all we have discussed, all settled we have discussed. reject, resolve and then we have already discussed. Okay? catch and finally also we have already discussed. And there is something called any and raise. Actually we haven't resolved promise, catch and finally but they are quite similar to whatever the try catch we are using. And we have promise.any and promise.raise. These are something that I'm not asking because I haven't seen

### 00:08:51 · Speaker 1

seen this asking, I haven't seen anywhere in the recent interview people asking this. Feel free to read, they are very short topics. If you are aware of promise all and all setter, they should be very straightforward for you to understand. Okay? So, that's all about this video.

### 00:09:05 · Speaker 1

I I'll just scan through the entire promise section again. There are few questions that I have to ask you. Probably I'll try to do one more video to summarize different question about all all settled and I'll try to ask you in my next video. Okay? If you like this video, please do like it on my YouTube channel. Don't forget to share this video with your friends. They may also get benefited from this. Please subscribe to my channel Uncommon Geeks and I'll try to add my medium blogs where I've explained Ursing Kavit and promises in a very detailed way and that is one of

### 00:09:35 · Speaker 1

my highest read medium article, please you also read that. That's the link my GitHub URL where I've added all these question and answers. You can you can also read you can download that project and solve all the problems, okay? Thank you again, catch you next video.
