---
id: 5FxZkHrGgJQ
title: Lec 7 - Deep Generative Models GAN variants and Applications
date: '2024-11-23'
url: https://www.youtube.com/watch?v=5FxZkHrGgJQ
description: ''
author: prathoshap5226
duration: 03:02:27
model: saaras:v3
transcript: true
---

# Lec 7 - Deep Generative Models GAN variants and Applications

## Transcript

### 00:00:02 · Speaker 10

before we begin the class today. So I was waiting for some people to join. See, I I uh I hope that uh like the people who have joined today, uh I see seventy nine people. So uh none of you are planning to drop the course, right? Because the window for dropping the course is is going to close by tomorrow, I think tomorrow, day after tomorrow, right?

### 00:00:31 · Speaker 1

Yes, that's right.

### 00:00:33 · Speaker 3

Yes sir, 23rd

### 00:00:35 · Speaker 10

Okay, so is anybody still considering dropping the course?

### 00:00:40 · Speaker 10

So I'll tell you why I'm asking but yeah is there anybody I think you have gotten enough flavor of how the course is going to be and all that right so is there anything any concern that or rather information that you might want to know to take the decision.

### 00:00:55 · Speaker 10

Because initially we started with some hundred people now we have about eighty five I think you know some fifteen people have dropped which is okay fair. uh Anybody else considering dropping the course?

### 00:01:10 · Speaker 0

ஹாய் சார்

### 00:01:11 · Speaker 10

Right

### 00:01:13 · Speaker 0

I am considering to drop because of personal reasons.

### 00:01:15 · Speaker 10

Okay

### 00:01:19 · Speaker 10

Okay, no problem. Yeah, but you still uh want to continue attending the classes. Yeah, so that is one thing that I wanted to ask you. So once you drop the course, would these I can people allow you to continue attend classes? Or would they just remove you from all groups?

### 00:01:35 · Speaker 7

audit patient allowed for us

### 00:01:37 · Speaker 10

Auditation term avudha? Okay, I see.

### 00:01:40 · Speaker 10

Okay, so except for Miss Sharmila, right? Anybody else considering dropping the course?

### 00:01:51 · Speaker 10

Okay, I'll take that as a no. uh Okay, so this I think then this is the the final class trend that we have. uh So I need this because we need to plan the assignments right now, we can form the groups of the and also plan the exam. So the exam, the midterm exam, I'm planning to have it after two classes, which is today there is one class where I'll finish this Gyan thing and the next

### 00:02:21 · Speaker 10

next class we will look at the variation of auto encoders we will start with V A E's after that we will have the midterm exam so that would be I will tell you

### 00:02:31 · Speaker 8

Hmm

### 00:02:33 · Speaker 8

Test 24, 25

### 00:02:35 · Speaker 10

fifth. uh yeah, twelfth is the here, right? So we can have it on tenth of October if it's okay for you. It's a Thursday.

### 00:02:45 · Speaker 10

we'll have it on tenth.

### 00:02:51 · Speaker 10

Does it work for all of you? Tenth of October?

### 00:02:54 · Speaker 5

set timing

### 00:02:54 · Speaker 3

Sir, timing.

### 00:02:58 · Speaker 10

Yeah, timing we'll have to see something that works for all of you. Maybe eight thirty to nine thirty, eight thirty to ten in the night.

### 00:03:09 · Speaker 3

Sir

### 00:03:09 · Speaker 2

Sir, it doesn't

### 00:03:10 · Speaker 9

final date

### 00:03:11 · Speaker 6

submitting the first assignment, right? So normally we may extend till the day. So we may not have the time to prepare on tenth.

### 00:03:23 · Speaker 10

Oh, I see.

### 00:03:26 · Speaker 4

And sir one more thing uh not sure Thursday at this moment maybe but it is a office days for most of us and many of us have actually the US client. I mean not me but many of my friends I can see in this class so I don't know whether it will be a right time to take a exam for them.

### 00:03:48 · Speaker 5

Can we plan it on Sunday instead?

### 00:03:52 · Speaker 10

Sunday is also okay. So which means that we'll have to do it on 13th.

### 00:03:59 · Speaker 10

So twelfth is uh like Dasara

### 00:04:05 · Speaker 10

So thirteenth we should do. Thirteenth October is okay with all of you? Anybody has a problem with thirteenth October?

### 00:04:11 · Speaker 9

Sir, thirteen works out.

### 00:04:15 · Speaker 10

thirteenth is fine, huh?

### 00:04:17 · Speaker 9

Yes sir

### 00:04:17 · Speaker 10

So maybe what I'll do, no, I will write it here. Okay, so

### 00:04:22 · Speaker 2

Morning

### 00:04:22 · Speaker 9

Sir, but please don't create a poll this time, Sir. Don't create a poll.

### 00:04:22 · Speaker 3

Sir

### 00:04:22 · Speaker 2

should be better

### 00:04:25 · Speaker 10

No, I don't. I don't. I won't. I will just put it here. Meet with Sam.

### 00:04:26 · Speaker 3

Yeah, yeah.

### 00:04:33 · Speaker 10

is on thirteenth Sunday.

### 00:04:39 · Speaker 10

between ten and eleven thirty a.m. is that okay?

### 00:04:43 · Speaker 9

So can we have it on afternoon time frame because people belongs to Christian and all will go to church in the morning times including me. Is it possible afternoon Sunday?

### 00:04:54 · Speaker 10

Is it possible

### 00:04:59 · Speaker 10

ओके, वी कैन डू आफ्टरनून। हाउ अबाउट टू टू थ्री थर्टी, वन थर्टीन्थ?

### 00:05:06 · Speaker 10

Anybody has problems with two to three thirty?

### 00:05:10 · Speaker 10

on 13th of October

### 00:05:14 · Speaker 10

Okay, so if there are no problems then we will

### 00:05:18 · Speaker 10

freeze that time and putting that on the WhatsApp group, okay? Okay, so no more discussions on this. Midterm exam is fixed on, yeah, we have to say thirteenth October.

### 00:05:30 · Speaker 4

answer sorry if I missed it any quizzes in between or it will be direct thirteenth now.

### 00:05:37 · Speaker 10

No, there will be quizzes. I mean, see, quizzes are independent, right? Every fortnight there will be a quiz. So next quiz will be next Saturday.

### 00:05:45 · Speaker 8

name

### 00:05:45 · Speaker 3

That's right

### 00:05:45 · Speaker 4

ஓகே

### 00:05:45 · Speaker 8

Hello

### 00:05:47 · Speaker 10

Janam Bhaiya

### 00:05:47 · Speaker 8

Janam Bhaiya

### 00:05:48 · Speaker 0

I think it's very soft

### 00:05:53 · Speaker 10

next quiz will be next Saturday. And yeah, so every alternative Saturday we will have a quiz that is independent of this exam.

### 00:06:00 · Speaker 4

Okay and what will be the syllabus sir I mean uh from last quiz to uh next uh more classes right I mean how many classes happened or it will be total from day one.

### 00:06:12 · Speaker 10

for what?

### 00:06:13 · Speaker 4

Quiz

### 00:06:15 · Speaker 10

Yeah, quiz will be cumulative, right? I mean, if if some some portion has been covered, the next part of the portion will be for the quiz. That's all.

### 00:06:25 · Speaker 4

ओके। आई मीन फ्रॉम द डे जीरो टिल व्हाटएवर कवर्ड दैट विल बी क्विज पार्ट, राइट? दैट मीन्स टोटल सिक्स क्लासेस ऑल टुगेदर।

### 00:06:34 · Speaker 10

not day zero, I mean like you can take it from like previous quiz to this this class, right? that that way.

### 00:06:36 · Speaker 4

ticket

### 00:06:42 · Speaker 10

Yeah, I would, I should have said non-cumulative. Yeah, so it's just

### 00:06:45 · Speaker 4

ಓಕೆ ಓಕೆ ಶ್ಯೂರ್. ಥ್ಯಾಂಕ್ ಯು.

### 00:06:49 · Speaker 10

Okay, so that is settled I suppose, no more questions on that. Midterm exam is on thirteenth October between two and three thirty. So I can what I can do perhaps just you know block your calendars also, no? That would be a good thing to do. Let me do it right away.

### 00:07:05 · Speaker 3

of

### 00:07:05 · Speaker 10

Sir

### 00:07:06 · Speaker 3

R

### 00:07:10 · Speaker 3

I do that

### 00:07:15 · Speaker 4

answer this MCQ will be subjective or MCQ type I mean sorry midterm will be MCQ or subjective type I mean just a pattern of the exam looking for.

### 00:07:27 · Speaker 10

it will be a written exam.

### 00:07:30 · Speaker 4

ओके

### 00:07:31 · Speaker 0

Okay

### 00:07:32 · Speaker 3

subjective not MCQ

### 00:07:34 · Speaker 0

ओके, श्योर, थैंक्स।

### 00:07:35 · Speaker 3

calendar

### 00:07:43 · Speaker 3

13th

### 00:07:48 · Speaker 3

Supreme

### 00:08:02 · Speaker 3

What is the course number here?

### 00:08:06 · Speaker 3

E1, E1286 OZ

### 00:08:10 · Speaker 9

Yes sir

### 00:08:12 · Speaker 10

Is it even? I'm not getting this.

### 00:08:16 · Speaker 9

it's on the team's meeting talk. you can see.

### 00:08:16 · Speaker 3

LTB values

### 00:08:24 · Speaker 10

required additional

### 00:08:28 · Speaker 3

third channel okay.

### 00:08:33 · Speaker 5

Yes sir, it's E1286

### 00:08:36 · Speaker 3

Oh, correct.

### 00:08:36 · Speaker 2

Hello

### 00:08:36 · Speaker 2

Hello

### 00:08:56 · Speaker 3

Okay

### 00:09:03 · Speaker 3

How do we make it a teams meeting?

### 00:09:20 · Speaker 3

I just sent a calendar invite. Can you all see that?

### 00:09:29 · Speaker 5

Yes sir. Yes sir.

### 00:09:30 · Speaker 3

is

### 00:09:30 · Speaker 0

Yes

### 00:09:34 · Speaker 3

Okay, so great. So that is

### 00:09:35 · Speaker 10

can we practice

### 00:09:39 · Speaker 1

practice

### 00:09:41 · Speaker 1

sorry it says D G M quiz sir. is it what we meant? mid term right?

### 00:09:47 · Speaker 10

Oh God

### 00:09:48 · Speaker 3

Right

### 00:09:52 · Speaker 3

Can't edit it, but I'm going to do it.

### 00:09:59 · Speaker 3

Yeah, that is what it is. It should be, yeah.

### 00:10:05 · Speaker 3

with exam

### 00:10:10 · Speaker 3

ain't it? Okay fine. So

### 00:10:12 · Speaker 10

practice questions. Well, see this being a graduate level course, right? It's not a probability theory course or anything. So I can't give you practice questions that way.

### 00:10:24 · Speaker 10

So what I would encourage you to do is uh read the previous year's notes and also the original papers of things that we are covering, okay? It will be around that.

### 00:10:37 · Speaker 10

And also you should it would be proctored so you need to keep your cameras on and then write the exam okay.

### 00:10:37 · Speaker 8

சோ

### 00:10:44 · Speaker 10

And the way to do it is either you write it on a sheet of paper, scan it and upload. Or you can write it on your like iPad or whatever and then share us share with us the PDF. Okay?

### 00:10:58 · Speaker 6

So notes can be referred right or it's not

### 00:11:01 · Speaker 10

You mean during the exam? No. If you want an open book exam, we'll have to make it more difficult. If you want that. Because I'll have to I'll have to assume that you'll have access to notes and have to ensure that uh I should ask you things that are not there in the notes, right? So which means that it has to be made a little difficult.

### 00:11:03 · Speaker 6

you

### 00:11:20 · Speaker 4

सर, मे बी दिस क्वेश्चन इस नॉट राइट टू आस्क बट जस्ट आस्किंग इल देयर वे अ क्वेश्चन दैट वेयर वी हैव टू डिराइव दिस फार्मूलास एंड ऑल व्हिच यू आर टीचिंग अस?

### 00:11:32 · Speaker 10

Yes

### 00:11:34 · Speaker 10

I don't know how to answer it

### 00:11:36 · Speaker 4

Okay

### 00:11:40 · Speaker 10

Yeah, of course, you are supposed to know all that, right? So just

### 00:11:44 · Speaker 4

Okay

### 00:11:44 · Speaker 10

Yeah

### 00:11:46 · Speaker 10

I'll not ask you the exact thing, right? Because, you know, whatever I've done in the class, I'll not ask you the exact thing, but something similar, something around it, right?

### 00:11:55 · Speaker 4

Yeah yeah I mean definitely theory and all definitely you have to know but these formulas and all like little tough to read but

### 00:12:00 · Speaker 10

don't have to remember anything, see. It will not be reasonable. I will not ask you to remember anything other than some fundamentals, right? Then for instance, see, you can't, you can't afford to forget the definition of, let's say, a density function, right? No, no, no, that's true. I'm saying there is some, I think, obviously, I would not ask you to remember some, some formula or something. I mean, you should trust me at that level, there is some reasonability to what we do.

### 00:12:03 · Speaker 4

Okay

### 00:12:05 · Speaker 4

Okay

### 00:12:09 · Speaker 4

Okay

### 00:12:09 · Speaker 7

See

### 00:12:14 · Speaker 7

No, no, no, that's not true.

### 00:12:24 · Speaker 3

Hello

### 00:12:28 · Speaker 3

Yeah, yeah, no, no, thanks.

### 00:12:30 · Speaker 10

Right, okay. Anything else? Any other comments on the exam stuff?

### 00:12:36 · Speaker 10

start with the class.

### 00:12:40 · Speaker 9

Sir, what about results for quiz one?

### 00:12:41 · Speaker 10

Hello

### 00:12:43 · Speaker 10

I think that should have gotten right. I mean, immediately

### 00:12:52 · Speaker 3

No sir

### 00:12:54 · Speaker 10

No

### 00:12:57 · Speaker 3

No.

### 00:12:58 · Speaker 10

really okay. So was it done on like it was not Microsoft form right? Microsoft forms.

### 00:13:07 · Speaker 3

Google is better software

### 00:13:07 · Speaker 10

Google

### 00:13:08 · Speaker 4

address

### 00:13:09 · Speaker 10

Hmm

### 00:13:13 · Speaker 10

Was it Google Form or Microsoft Form?

### 00:13:16 · Speaker 10

It was

### 00:13:16 · Speaker 2

It was Microcom

### 00:13:18 · Speaker 10

Microsoft forms, no? Hold on, let let me just ask Chandan. There is some setting where you should can make the outcome visible right after because let me ask him.

### 00:13:29 · Speaker 3

to do that

### 00:13:31 · Speaker 3

should be seen immediately actually.

### 00:13:43 · Speaker 3

is not became my call. Okay, I'll I'll tell him to do that.

### 00:13:53 · Speaker 10

because generally the way I ask them to do it is once you submit your answers, you should you should get the the marks, right? because it is possible because it's a multi

### 00:14:06 · Speaker 3

choice question type. Okay.

### 00:14:18 · Speaker 3

चलिए स्टार्ट ऑल मोर क्वेश्चन

### 00:14:18 · Speaker 5

almost

### 00:14:19 · Speaker 3

Yeah

### 00:14:21 · Speaker 5

the excess

### 00:14:22 · Speaker 7

that was passed to us to write the details of the assignment teams. It was having four columns and we thought four people can join together and create a team. But you also told its size of three. So there is some confusion there.

### 00:14:27 · Speaker 10

because

### 00:14:37 · Speaker 8

I see. Okay.

### 00:14:38 · Speaker 10

सी फोर इज़ ओके लाइक आई मीन सी आई रेकमेंडेड टीम साइज़ इज़ थ्री ओके। सो इफ़ यू

### 00:14:48 · Speaker 10

See what happens is no if there are four people then uh I mean dividing work amongst four people will become too much so I would recommend a team of three okay.

### 00:15:02 · Speaker 10

But if you are four people then you should be aware of the fact that when we are grading the assignments right. We will take that into consideration that it's a team of four and look for like more work.

### 00:15:16 · Speaker 3

Okay Okay

### 00:15:16 · Speaker 10

Could that you reminded me of that. See assignment I hope that all of you have taken a look at the assignment, okay? So what you need to submit is as I have mentioned there one Jupiter notebook. So whatever has been given there as to do, right? That is the bare minimum thing that you should do, okay? But uh that will not give you hundred percent marks.

### 00:15:41 · Speaker 10

Okay, that will give you let's say seventy, seventy to eighty percent marks if you just do whatever has been asked for. Now, the remaining thirty percent uh will depend upon like what uh will be the uh the observations that you would be doing, right? And what are the kind of experiments that you have done. Okay? And also I'm planning, I mean this is not this is not fixed yet, I'll have to ask TAs if they can do it. But I'm planning to have a viva, okay? For all the assignments combined.

### 00:16:15 · Speaker 10

sometime at the end of the course, we will have a viva where we will ask you questions on the implementations that you have done right at the for the end of at the end of the course, okay? So, try to incorporate as much experimentations as possible and try out multiple ideas and it it the the total I mean evaluation depends on the the quality and the the quantity of the experiments that you have done.

### 00:16:45 · Speaker 10

Okay? So, yeah, so questions, yeah, Arijit.

### 00:16:50 · Speaker 4

सर, जस्ट अ लास्ट क्वेश्चन दैट दिस ऑल असाइनमेंट शुड बी डन इन ग्रुप, राइट? जस्ट रीकन्फर्म मी।

### 00:16:55 · Speaker 10

Correct

### 00:16:56 · Speaker 4

Yeah

### 00:16:56 · Speaker 10

Correct. I've told that so many times why questions.

### 00:16:59 · Speaker 4

No no no, I little was confused during first time, sorry.

### 00:17:02 · Speaker 10

Why why where where is the confusion? I don't understand. And what is the there should be a there should be some reason why you are confused no? I told so many times.

### 00:17:07 · Speaker 4

No actually

### 00:17:11 · Speaker 4

No, in fact, so many times. Yeah, actually I forgot that there was a no project separately, it is only assignment. I'm very sorry for that. Just reconfirm that, that's why.

### 00:17:22 · Speaker 10

Okay see an excel sheet was was circulated where themes had to be made and all that right I don't know where the confusion is. Okay no problem.

### 00:17:25 · Speaker 4

Hmm

### 00:17:34 · Speaker 9

So one more clarification the the the report or the notes on the assignments with the Jupiter notebook only right we need to write it is not any separate documentation.

### 00:17:44 · Speaker 10

Yeah, it is not a separate document. It has to be embedded with the notebook.

### 00:17:49 · Speaker 9

Thank you

### 00:17:50 · Speaker 10

Right? And uh you can all the plots, all the observations that you do has to be a part of the uh the Jupiter notebook itself, huh? What you submit is one file for assignment, that's all, nothing more.

### 00:18:03 · Speaker 1

Thanks

### 00:18:04 · Speaker 10

Okay

### 00:18:05 · Speaker 0

Hello

### 00:18:05 · Speaker 9

should it come as one submission per team or in each of the team members will submit

### 00:18:13 · Speaker 10

Submit the same thing three times

### 00:18:15 · Speaker 9

No, that's what I wanted to understand, sir, like, how will the submission look?

### 00:18:20 · Speaker 10

one submission per team

### 00:18:22 · Speaker 9

one submission per team

### 00:18:24 · Speaker 10

Yeah

### 00:18:25 · Speaker 9

Okay

### 00:18:25 · Speaker 10

So unless there is let's say that you are you are in a team of three and you know one person sends me a personal email saying that this person did not contribute to the assignment and all that. The rule is that everybody in the team will get the same marks for the assignment.

### 00:18:47 · Speaker 3

गॉट इट सर। ओके।

### 00:18:48 · Speaker 10

Okay? Yeah. So one five. Okay so you coordinate with see there is one other reason why I ask you to do it in teams right? There's need some compute resource. So I recommend all of you to like buy some resource from like Google Collab or something right? That costs some money. You can divide it amongst three of you or four of you if you make teams.

### 00:19:12 · Speaker 10

Okay, so that is uh like another reason why you should make teams. Okay. So anything about anything else about the assignment and I hope that the PyTorch PyTorch tutorial was done last last week. Did Swas do that?

### 00:19:28 · Speaker 5

Yes sir

### 00:19:29 · Speaker 10

Was it useful?

### 00:19:31 · Speaker 9

very informative sir.

### 00:19:32 · Speaker 5

Yes sir

### 00:19:34 · Speaker 10

Okay okay. So fine then I think now we have all everything that you need no to start implementing and write do the assignment. Please get started with that okay. Yeah so anything else any other logistic

### 00:19:48 · Speaker 3

thing that we need to discuss before we continue.

### 00:20:01 · Speaker 5

So one last question.

### 00:20:03 · Speaker 3

Hmm

### 00:20:04 · Speaker 6

So when we run the cells in the Jupiter notebook, do we need to it has to be saved in the export or is the code and the observations sufficient?

### 00:20:17 · Speaker 10

You don't have to export. uh It's the code, the corresponding observations. See when you write, I have asked you to plot a few things. So I have to plot them, you have to observe what you have done. And as I said, also do things that I have not asked to do or not asked for.

### 00:20:34 · Speaker 10

Right? So you can you can do more experiments than what I have asked for and you document that as well, right?

### 00:20:41 · Speaker 6

Yes sir but yeah the plots usually when we run the let's say uh matplotlib dot plot it generates the plot so if the notebook gets restarted the cells get lost for some reason then it would be lost right so is it okay to because embedding a image inside the Jupiter notebook it it increases the size of it a lot.

### 00:20:47 · Speaker 8

to

### 00:20:49 · Speaker 8

Hmm

### 00:21:04 · Speaker 6

because it embodies

### 00:21:05 · Speaker 10

That's okay, no? That's okay, embed it. I mean, it's okay. I mean, but you have to embed.

### 00:21:11 · Speaker 6

but you have to embed

### 00:21:14 · Speaker 6

ओके, इफ द रिजल्ट्स आर लॉस्ट, वी कैन एम्बेड इट एस वेल।

### 00:21:17 · Speaker 10

Yes, you you have to embed, right? Otherwise, like how do we evaluate? I mean, we will not be able to run them.

### 00:21:24 · Speaker 6

Okay. Hmm. Again.

### 00:21:25 · Speaker 10

again, right? We will run some blocks for sanity check, but it's not that we can we should we can run all cells of everybody, right? So you should embed it. You should embed all that.

### 00:21:34 · Speaker 3

you should

### 00:21:37 · Speaker 5

Okay sir, yeah

### 00:21:39 · Speaker 3

Thank you

### 00:21:45 · Speaker 3

Anything else?

### 00:21:59 · Speaker 3

Okay, shall we start then? Shall we resume?

### 00:22:16 · Speaker 3

Hello, am I there?

### 00:22:19 · Speaker 3

Yes sir. So we can start.

### 00:22:19 · Speaker 4

So we can start

### 00:22:22 · Speaker 10

Okay

### 00:22:25 · Speaker 10

Okay, a quick recall of what what we did the last time. So we were looking at the adversarial networks for generative modeling.

### 00:22:39 · Speaker 10

The idea was that you are given some data and what you need to do is

### 00:22:45 · Speaker 10

transform an arbitrary random variable into like another random variable of interest, another random variable whose distribution is going to be close to the the data distribution, that's the idea.

### 00:22:59 · Speaker 5

Idea

### 00:23:00 · Speaker 10

Now what did we do? We uh cashed it as an optimization problem which would minimize a divergence metric between the true distribution and the data distribution. So we could not uh there is no way that we can compute that divergence metric because we don't know the underlying distribution so instead of that we created a

### 00:23:23 · Speaker 10

lower bound on the divergence metric inside. So once you create that lower bound, uh you express that lower bound in terms of expectations over the true distribution and the the generated data distribution which can be computed using the uh sample estimates, right? uh and the lower bound that we created, okay, involves another optimization problem over a set of a class of functions which we called as T of

### 00:23:53 · Speaker 10

right? Now these class of functions uh we uh represented them as another neural network okay? T W of X. And therefore you have like two neural networks one that is representing the the transformation of the the random variable okay? which would generate the data. The other neural network that would approximate this T function which construct the lower bound on the the divergence that we are working with. Okay

### 00:24:25 · Speaker 10

Then what happened is that the lower bound or the so called cos function will have the difference between these two expectation. The first expectation is with respect to first expectation is of first expectation is on T of X with respect to P X of the real data. The second expectation is of F star of T of X and the X cap or this expectation is over the generated data. Okay. Now, because since the lower bound itself involves an optimization problem over

### 00:25:07 · Speaker 10

aspect I mean a class of functions. So we will end up solving what is called as a saddle point problem where you have a cost function, okay, which is a function of two variables, theta, which are the parameters of the generator network and W, which are the parameters of the T network, okay, that would construct the lower bound on

### 00:25:34 · Speaker 10

the F divergence. So we need to maximize this cost with respect to W, okay, because that is what is going to create the lower bound. And once the lower bound is created, we want to minimize that with respect to theta such that the lower bound becomes close to or rather the F divergence is minimized or the lower bound on the F divergence is minimized such that the the P theta, which is the generated distribution, get close close to P X.

### 00:26:03 · Speaker 10

Okay. uh This is the overall philosophy of what we are doing. And in fact, if you recall, right, I had shared that uh that that screenshot of a meme on the WhatsApp, right? And when it's uh on a serious note, that that's exactly how a saddle point looks. I mean, which is which is like that the I mean, uh if if you if you have seen that potato chips, right? The top of it is how a saddle point looks. So basically, there are uh the function has multiple parameters, right? So at this point what happens is if you move along one direction,

### 00:26:41 · Speaker 10

around the saddle point the function would increase. If you move along the other direction, okay, at that same point the function would decrease. That is what we are seeking, okay, which is the saddle point.

### 00:26:54 · Speaker 3

Hello

### 00:26:55 · Speaker 3

Okay, so any questions thus far?

### 00:27:04 · Speaker 5

Sir, here basically we want that generation neural network will take less cost, but the other neural network which is checking the images real or not will take more cost.

### 00:27:18 · Speaker 10

No, no, no, hold on. See, I never said that the other network is checking whether the image is real or not. Where did I say that?

### 00:27:25 · Speaker 5

Now I'm just checking is that the correct imagination what I am thinking.

### 00:27:30 · Speaker 10

No, no, first of all, when did I say that this T network is checking whether the image is correct or not?

### 00:27:38 · Speaker 5

This is discriminator.

### 00:27:40 · Speaker 10

But I never said what that is, right? I mean, see, that is an interpretation that I'm going to like give today. See, in general, this critic network is simply a neural network that would approximate this T function that creates a lower bound on if divergence.

### 00:27:48 · Speaker 5

See

### 00:27:57 · Speaker 10

So it's it's it's it's it's better to see it that way.

### 00:28:03 · Speaker 10

Okay

### 00:28:03 · Speaker 5

So this lower bound is not I'm not able to imagine that.

### 00:28:10 · Speaker 10

Five

### 00:28:12 · Speaker 10

See that's what I'm saying right?

### 00:28:12 · Speaker 5

product

### 00:28:16 · Speaker 10

See, do you, I mean, do you recall this thing that we did the one class before? This we actually derived that lower bound, right?

### 00:28:22 · Speaker 5

It

### 00:28:24 · Speaker 5

No, no, not not in that sense. Not the derivation form.

### 00:28:28 · Speaker 10

Yeah

### 00:28:30 · Speaker 5

Okay, I think maybe throughout this class we may get because you are going to explain about discriminator network.

### 00:28:37 · Speaker 10

No, I see I okay, so it's an important point which you made. See, even though I would explain like like what this thing would look like, I would do it only for a special case.

### 00:28:51 · Speaker 10

Right for the general case where you can take any f divergence this is not a classifier. You understand? See this T W network is not a classifier if you take your f divergence to be let's say the chi square distance.

### 00:29:10 · Speaker 10

Okay? The the interpretation that you see like all over the internet and all these blogs etcetera, right? They are for a special case of this where this I mean we we we took this, right? Which is if you make your the F function to be corresponding to this junction channel divergence, only in that case, right? This network becomes a classifier.

### 00:29:33 · Speaker 10

or rather this network can be interpreted as a classifier. Otherwise, this is simply a neural network that is trying to create a lower bound on the f divergence that we would want to minimize.

### 00:29:48 · Speaker 10

Is it clear? I think it's very important to have that view that the I mean why do we have that other network?

### 00:29:56 · Speaker 10

we have that other network because you you have to remember the entire story right we our goal was that's why I have written this our goal was that we need to minimize the f divergence. we cannot do that and we create a lower bound on that. Now this lower bound involves an optimization over a class of functions t of x and that t of x is what we are optimizing approximating using another neural network.

### 00:30:23 · Speaker 10

Is this clear?

### 00:30:25 · Speaker 10

So there is see so far there is no like there is nothing that is trying to like classify between the real images and the generated images. I've never said that. Only if you make your F divergence to be the Jenton Shannon divergence, this T function right which would still create a lower bound on the F divergence would take the form of a classifier and that is why that is when you can interpret it that way otherwise this T network has no meaning.

### 00:30:53 · Speaker 10

like other than just creating the lower bound on the F divergence that we want to minimize. Is this clear?

### 00:31:02 · Speaker 5

Yeah, somewhat

### 00:31:05 · Speaker 10

Why somewhat? Where is the gap?

### 00:31:09 · Speaker 5

Sir, I have gone through this time, this the last week as well another time, but I got this confusion to just interpret.

### 00:31:20 · Speaker 5

I think I think with this class I may get more clarity. Or maybe if there is confusion I will ask in next class.

### 00:31:25 · Speaker 10

if they

### 00:31:28 · Speaker 10

Okay. See, you don't have to interpret it, right? It is simply a neural network that that is approximating this T function, which is creating a lower bound on the f divergence. That's all. See, you one has to have this kind of a generalized view, otherwise, you can't go deeper than what you see in these blogs, etcetera, right? The only way to make that next level of jump is to start seeing things in an abstract way.

### 00:31:29 · Speaker 5

So

### 00:31:55 · Speaker 3

That's a great

### 00:31:55 · Speaker 10

Yeah, so these three lines that I have written, right? You start, uh I mean your goal is to minimize the f divergence between two distributions. We cannot do that. So we constructed a lower bound. Now this lower bound that we construct involves an optimization over a class of functions t of x and that class of functions t of x is what I am representing using a neural network. That's all.

### 00:32:19 · Speaker 7

Uh sir, I think the diagram which we were talking about yesterday, uh how does the graph look like when we do a lower bond on F divergence? I think that will help Divyang more to understand what is happening.

### 00:32:34 · Speaker 10

which

### 00:32:35 · Speaker 10

I am not sure

### 00:32:35 · Speaker 9

not sure

### 00:32:36 · Speaker 10

Hello

### 00:32:36 · Speaker 7

Uh yeah, you were saying yesterday, right, we'll look through a diagram that one graph that how that minimization happened, right? Once we construct a lower bond on

### 00:32:49 · Speaker 7

on the discriminator network what we get, then we plot it on a graph and then we further try to minimize it, yeah that graph. theta and

### 00:32:54 · Speaker 10

other

### 00:32:58 · Speaker 7

Sure

### 00:32:58 · Speaker 10

Sure, yeah, again, right? I mean, that would be for this case where your T network can be interpreted as a classifier.

### 00:33:08 · Speaker 10

See, I'll do all that today. That is what I'm going to do now. But as I said, the in the most general case, there is a there is a version of GAN called LS GAN, least square GAN, okay? Where this T network is not a classifier, that will become a regressor.

### 00:33:27 · Speaker 10

you get it. So it depends, it depends on what is the underlying F divergence that you have chosen for minimization. If you choose your F divergence to be of this particular form, then this T network can be interpreted as a classifier.

### 00:33:44 · Speaker 10

you understand. Otherwise it is simply a network okay or a neural network that is approximating a function T of X and what is that T of X function that T of X function is the function that constructs a lower bound on the F divergence that we would want to minimize.

### 00:34:01 · Speaker 10

Is it all right?

### 00:34:07 · Speaker 3

Yes sir

### 00:34:10 · Speaker 5

Yeah, Vivek

### 00:34:14 · Speaker 9

Yes sir. Yeah. I was just reacting. The thing is sir like does it make a difference if we do the minimization first and then the maximization? No.

### 00:34:14 · Speaker 10

Okay

### 00:34:19 · Speaker 10

Hello

### 00:34:25 · Speaker 10

No, no, no, no, no, no, no. The order does not matter, especially because you are you are doing it in a gradient based way, no? See, this thing, how do we optimize this? We optimize this using gradient based minimization, right? So it does not matter.

### 00:34:41 · Speaker 10

Okay. So then what did we do after that is that we we looked at one instance of this F Gyan, right? Which is the naive Gyan, I mean that that was that is that that you see everywhere where the F function that that you look at will be of this form, right? U log U minus U plus one log U plus one by two. In this case, the underlying F divergence is called the Jensen-Channell divergence or JS divergence. So for this particular case, right? If you

### 00:35:12 · Speaker 10

Yeah, if you for this particular case, if you plug in this particular F and F star and all that, the the final

### 00:35:21 · Speaker 10

network, right? can be represented this way, right? where the t function, uh if you represent the t function as a concatenation of the of of or rather if you break down the t function as two parts, right? one that that is a that would take the x and give you a real number and on top of it you have a sigmoid. Okay? and this sigmoid is by definition gives you

### 00:35:51 · Speaker 10

value between zero and one. The final loss function for this, right? Looks like whatever I have written within this flower brackets. uh Now in this particular case, right? You can interpret it interpret this T function as a classifier because the output of that T function, okay? is bounded between zero and one.

### 00:36:15 · Speaker 10

Okay, so that is what it is. And then we looked at that we looked at how to train this

### 00:36:23 · Speaker 10

uh this this particular network uh in practice. So you have this loss function J J cap which represents J cap theta comma W. uh first you sample I mean you are given n points from the data and uh you have you are given m points from B theta as well right. How do you get those m points? You just sample m points from the normal distribution and pass them through G theta of Z to to obtain these m points. And then uh I also

### 00:36:53 · Speaker 10

showed you how to compute, right, the gradients for both these networks and back propagate through them and try it. I don't go through this again because we did it in in in detail. Yeah, if you have any questions this far, I'll take some questions and then we'll move move on to today's content. Any questions on this?

### 00:37:15 · Speaker 10

Yeah, uh,

### 00:37:19 · Speaker 8

Hi sir, good morning. Yeah. Can you scroll a little to the top where we instantiate the junction chain and divergence as a special case of FGAN? Yeah. So sir, here this expression, J theta comma W, we have here two terms. One is the expectation over P X and one is an expectation over P theta. Correct. So, below that you said like once we put put in the values of F and F star, we get with the we get the expression

### 00:37:20 · Speaker 10

Yeah

### 00:37:28 · Speaker 10

Hmm

### 00:37:40 · Speaker 10

Correct

### 00:37:47 · Speaker 10

the

### 00:37:49 · Speaker 8

which has log of d w of x and the other term. My question was sir, how did t w x change to log of d w x because like if you're just putting the values of f and f I understand in the t session this might be a little more clear. Just to get some some like I I wanted to understand how does putting f and f star values result in this changing to a log.

### 00:37:55 · Speaker 10

I

### 00:38:06 · Speaker 10

I understood

### 00:38:18 · Speaker 10

No, see F has a U log U minus U plus one log U plus one by two, right?

### 00:38:24 · Speaker 8

Yeah

### 00:38:24 · Speaker 10

So F star for this case has a log term there.

### 00:38:30 · Speaker 8

Yes

### 00:38:31 · Speaker 10

Okay? And you have f star of t w of x, right? So there will be a log term there that will come up.

### 00:38:38 · Speaker 8

Yes sir, but that is an expectation over P theta, right? So how is it affecting a P expectation over P X star? That was my question.

### 00:38:47 · Speaker 10

you mean in the in the in the first case you are saying that in the first term how are you getting this log d w x

### 00:38:52 · Speaker 8

Hello

### 00:38:55 · Speaker 8

Yes sir

### 00:38:56 · Speaker 10

I see. Okay. Uh yeah, I'll tell you how to do it. I I think I I did this algebra in the

### 00:39:04 · Speaker 10

A

### 00:39:05 · Speaker 3

last iteration I think just give me a minute I will tell you that

### 00:39:22 · Speaker 3

Yeah, so what we did is that

### 00:39:26 · Speaker 10

See you represent this T function right? The T function as see you look at this right? So how are D and T related? So D is the sigmoid of T W of A isn't it?

### 00:39:41 · Speaker 8

Yeah

### 00:39:42 · Speaker 10

So now if you want to represent T in terms of D, what do you do?

### 00:39:47 · Speaker 10

the inverse of that e power mu ya so that's that's where you have that log. that's where you get that log.

### 00:39:47 · Speaker 8

of the team or yeah so that's

### 00:39:51 · Speaker 8

Okay

### 00:39:54 · Speaker 8

Alright sir, yeah sure that explains it. Thank you sir.

### 00:39:59 · Speaker 10

Okay. So can you please repeat?

### 00:40:00 · Speaker 9

Can you please repeat that?

### 00:40:02 · Speaker 10

See he was asking the question was that there is a T W term here right how did you get this log D W term

### 00:40:10 · Speaker 10

Right, when you just there is no F here, how did you get this log D W term? See, how are this D and T related? See, again, see, the reason it is it looks a little complicated here is that the people, the Gyan people just wrote down this loss function in terms of one network called D W, okay? Now, in the terminology that we developed in this according to the Gyan terminology, what Gyan people have

### 00:40:40 · Speaker 10

called as D W is simply the sigmoid of our T T function. It is simply a fixed sigmoid of the T function. Now there is T here right? Now if you want to write it in terms of T how are T and D related?

### 00:40:56 · Speaker 9

by the sigmoid relation.

### 00:40:57 · Speaker 10

by a sign point, right? Which is which involves a negative exponentiation. So if you want to write T in terms of D, then there will be a logarithm, right?

### 00:41:10 · Speaker 1

Yes sir

### 00:41:11 · Speaker 10

That's all. So you have to invert the sigmoid basically. If you invert that sigmoid, T will be written in terms of log of D. That's all.

### 00:41:21 · Speaker 9

Okay

### 00:41:23 · Speaker 9

And sir, in the in the above term

### 00:41:23 · Speaker 10

Sir

### 00:41:25 · Speaker 10

actually you can do yeah tell me

### 00:41:28 · Speaker 9

in the above term we are doing f star of t w of x x hat. So basically we are replacing u in the divergence function with t w of x hat. Correct.

### 00:41:33 · Speaker 10

So basically

### 00:41:40 · Speaker 10

Correct. Correct.

### 00:41:41 · Speaker 9

Correct. And then we are trying to simplify like like replacing T W with D as we have mentioned before using the sigmoid relation. Correct.

### 00:41:48 · Speaker 10

correct. Correct. Correct. So you if you complete that algebra you will get this expression. And if I have to do that algebra it will take me thirty minutes. Not worth it. It's simply algebra that's all. Yeah.

### 00:41:57 · Speaker 9

Private Sir

### 00:41:59 · Speaker 9

understood

### 00:42:01 · Speaker 10

Is this all right now?

### 00:42:04 · Speaker 10

Okay and I suppose that uh that uh like this uh this training part right the forward pass backward pass everything for both these networks are okay. Any questions on this? Like how do you train these?

### 00:42:20 · Speaker 10

because this is exactly what I have asked you to implement in your in your assignments. So I hope that these are clear.

### 00:42:27 · Speaker 10

Okay, so if it's clear then

### 00:42:28 · Speaker 3

we'll go to start with the next

### 00:43:15 · Speaker 3

Okay, so today's agenda is that I will

### 00:43:18 · Speaker 10

talk further about the the GANs and the naive interpretation of of how can you interpret it for this particular case, okay? And then we will look at like a couple of applications of adversarial optimization for this task called domain adaptation and like image to image translation, okay? There are multiple applications of GANs I'll talk about it but we'll look at two of applications. And then if there is time we will start the variational auto encoder part also today. Okay.

### 00:43:56 · Speaker 3

Let's start. So let's start with interpreting.

### 00:44:10 · Speaker 3

Knife Gyan

### 00:44:17 · Speaker 3

as classifiers

### 00:44:32 · Speaker 3

classifier guided generator training.

### 00:44:47 · Speaker 3

So this is simply interpreting

### 00:44:51 · Speaker 10

the naive GAN, right, which is, which is with the Jensen-Chanon divergence as a classifier guided generative model, okay? What do I mean by that? Okay, let us recall that what are what are our setting? So setting

### 00:45:04 · Speaker 3

is that we have

### 00:45:04 · Speaker 10

Hello

### 00:45:05 · Speaker 3

Data Points

### 00:45:12 · Speaker 3

coming from P X. Okay. We have this particular setup.

### 00:45:24 · Speaker 3

where we have a neural network of some function that would transform

### 00:45:31 · Speaker 3

Question right

### 00:45:32 · Speaker 10

table

### 00:45:34 · Speaker 10

to some other random variable which is random variable of interest P theta, right? Now, let's say that

### 00:45:42 · Speaker 3

what is our goal? Remember that our goal

### 00:45:48 · Speaker 3

is to make

### 00:45:52 · Speaker 3

P theta

### 00:45:56 · Speaker 3

close to px, right? That is that is what our goal is. Okay? Now suppose that there is a classifier.

### 00:46:18 · Speaker 3

classifier, okay?

### 00:46:22 · Speaker 3

which is this let's call that as so d w of

### 00:46:32 · Speaker 3

is equal to one if x comes from px it is zero if

### 00:46:42 · Speaker 3

Okay, I should go back to make it.

### 00:46:51 · Speaker 3

Okay, not condition.

### 00:46:55 · Speaker 3

Fuse Invocation T W

### 00:46:59 · Speaker 10

x or x not. So it will take either x or x cap, okay? It's one if x is coming from x cap or it's then it is zero if it is coming from p theta.

### 00:47:10 · Speaker 10

So you understand what we are doing?

### 00:47:12 · Speaker 3

So there is a classifier, okay, a binary classifier.

### 00:47:22 · Speaker 9

सर, व्हाट अबाउट द अदर केसेस व्हेन एक्स इज नॉट कमिंग फ्रॉम पी एक्स और एक्स हैट इज नॉट कमिंग फ्रॉम पी थीटा?

### 00:47:32 · Speaker 10

Come again

### 00:47:34 · Speaker 9

Sir, we are saying that the this classifier will be one if x comes from px, right? Correct. What if x does not comes from px?

### 00:47:38 · Speaker 10

com

### 00:47:40 · Speaker 10

Correct

### 00:47:45 · Speaker 10

That's all, no? It will give zero.

### 00:47:48 · Speaker 10

See this classifier takes either x or x cap as input. Okay? And it will give you one if x is from px, it will give you x cap if it comes from p theta.

### 00:47:59 · Speaker 9

it will give us zero if x cap comes from p theta

### 00:48:02 · Speaker 10

Correct

### 00:48:05 · Speaker 9

No, what if x or x cap which we have drawn does not come from px or p theta? Like...

### 00:48:12 · Speaker 10

No, it should either come from P X or from V theta, right? Because D W is, yeah, D W has been set up in such a way that it either takes X as input or it takes X cap as input.

### 00:48:15 · Speaker 8

because

### 00:48:24 · Speaker 10

Right?

### 00:48:24 · Speaker 3

ओके ओके

### 00:48:25 · Speaker 10

So, so it's basically what is this? This is a

### 00:48:32 · Speaker 3

Binary Classifier, Okay.

### 00:48:37 · Speaker 3

between samples of

### 00:48:42 · Speaker 3

samples of

### 00:48:44 · Speaker 3

P.S.

### 00:48:44 · Speaker 10

and p theta

### 00:48:48 · Speaker 3

Okay

### 00:48:48 · Speaker 10

is this all right? Yeah, it's actually a binary classifier that would classify between the samples of P X and P theta. Is that okay?

### 00:48:59 · Speaker 1

Yes sir

### 00:49:01 · Speaker 3

That's fine, right? Okay. Now here is the question, here is the question.

### 00:49:11 · Speaker 3

Sir

### 00:49:18 · Speaker 3

um

### 00:49:21 · Speaker 5

Motorview

### 00:49:28 · Speaker 10

Yeah. Yeah, this reminds me of something, just a slight off-topic thing. See, the reason I erased it off is because if you look at the way I have written no, it is

### 00:49:42 · Speaker 10

it is all the letters like are not aligned along a straight line, correct?

### 00:49:51 · Speaker 10

uh that's why I erased it off. I wanted to write it again. I remember once like three four days back, uh I have a daughter, school going daughter, okay? So she's she's eight years old. She was writing something on a sheet of paper and she was not writing it along a straight line and I told her, you know, this is not the way to write it. So I just reminded that to myself and said, oh if I have to tell somebody to do something, I'll have to first adhere to that. So

### 00:50:24 · Speaker 10

Yeah, so writing along a straight line when you don't have ruled thing is a skill.

### 00:50:32 · Speaker 10

Anyway

### 00:50:35 · Speaker 10

If my daughter sees, if my daughter sees that she'll ask me, right? I mean, you ask me to write it.

### 00:50:40 · Speaker 3

straight line and what are you doing?

### 00:50:48 · Speaker 10

Yeah, so that reminds me of another joke. So, uh I I told her that she asked me what is that you teach? So I told her that I teach math. So then she asked me to like show me what I write, okay? So I just showed her one day I had like taught back propagation. uh and you know filled the board with lot of these equations of back propagation, derivatives and all that. She looks at that picture, right? The question she asks is, you tell

### 00:51:18 · Speaker 10

that that you teach maths but all that you have written is English right so there is no maths here there are no numbers. So everything that you have written is English here there is no maths. Okay so anyway so the question that we

### 00:51:34 · Speaker 3

should ask now is, can the classifier

### 00:51:46 · Speaker 3

used to

### 00:51:52 · Speaker 3

tweak

### 00:51:55 · Speaker 3

theta, okay? Such that, such that P theta becomes close to

### 00:52:03 · Speaker 3

P X. This is the question that we will ask now.

### 00:52:08 · Speaker 3

So let's say that I'll write that classifier here. Let's say that we have this classifier.

### 00:52:19 · Speaker 3

D W. So this will take X or X

### 00:52:23 · Speaker 10

as input, okay? And gives you a number between zero and one.

### 00:52:30 · Speaker 10

Okay? So the question that we are asking is, can this classifier be used to tweak theta, okay? Such that P theta becomes close to P H.

### 00:52:40 · Speaker 3

Do you appreciate the question? Does all of you understand the question?

### 00:52:52 · Speaker 10

Okay

### 00:52:53 · Speaker 3

Can somebody answer that question?

### 00:52:55 · Speaker 10

So now I have given you a classifier, okay, which would tell you whether this the the output of this or rather, uh it will tell you whether uh the sample that it is seeing is from P X or P theta. Now I have to tweak theta, okay, by using this classifier in such a way that uh

### 00:53:18 · Speaker 3

the distribution P theta becomes close to P X. Can this be done?

### 00:53:28 · Speaker 3

Can somebody answer that? Can somebody think of a way to do that?

### 00:53:33 · Speaker 9

Yes, so that is the way we do it, right? Like we train both the classifier and the discriminator. No, no, no, I have

### 00:53:39 · Speaker 10

No no no I have

### 00:53:40 · Speaker 9

No no no okay okay sorry. I have never told you that okay.

### 00:53:41 · Speaker 10

not okay sorry. I've never told you that so basically. Yeah as far as as per as per as far as we have seen it now we are simply constructing lower bounds on f divergence and minimizing them that's all. Now the question that I'm asking is forget about everything that we have done so far right I'm simply asking you whether in this setup right where there is a neural network that would take the samples from from arbitrary distribution and and giving you

### 00:53:45 · Speaker 8

Yes

### 00:54:11 · Speaker 10

some other distribution. I've given you a classifier that would classify between the samples of true data and the output of this neural network. Now the question is by using this classifier can you make your g theta such that whatever it outputs is close to px. That is the question. Now don't think about f diagonals now for a while.

### 00:54:32 · Speaker 10

Okay, thank you

### 00:54:32 · Speaker 3

சரி

### 00:54:35 · Speaker 10

I think please raise your hands virtually because otherwise it will become sort of chaos. Sanchit, you wanted to say something?

### 00:54:43 · Speaker 9

Yes sir what uh so if the samples are drawn from X we will get a one but if X hat is like drawn then we will get a zero so what we can do is we can try to maximize uh the overall like we we can go for a cumulative sum of DW outputs and try to maximize that.

### 00:55:05 · Speaker 9

like

### 00:55:06 · Speaker 10

I've maximized with respect to what? See, what are you tweaking here by the way?

### 00:55:08 · Speaker 6

What

### 00:55:12 · Speaker 9

सर, लाइक व्हाट आई एम लाइक ट्राइंग टू सी इज लाइक

### 00:55:15 · Speaker 10

No no, I'm not asking you what I'm trying to say. The question that I'm asking is what is what handle do we have here? What is that we can tweak? See, we can tweak theta, nothing else. The classifier is fixed.

### 00:55:29 · Speaker 10

Okay, so what we need to do is simply use this classifier to tweak theta. You understand?

### 00:55:38 · Speaker 3

Okay

### 00:55:38 · Speaker 10

I'm asking you a philosophical question at a very high level, how do you use this classifier to tweak this theta such that your P theta goes close to P X is what I'm asking.

### 00:55:53 · Speaker 10

Yeah, Divya

### 00:55:57 · Speaker 5

Sir, somehow can we use back propagation? I don't know how we can, but is it help us?

### 00:56:04 · Speaker 10

Yeah, of course. See, whenever we try neural networks, we always use back propagation. That is, see, don't go to details, details we will work out. I'm just asking you at a philosophical level. So now that I've given you a classifier, I want you to use this classifier to tweak theta such that your P theta becomes close to P X, that is all. Think about it, no? Yeah, Abhitosh.

### 00:56:27 · Speaker 2

I think if the classifier has uh already approx approximated P X uh during the classification training, uh then you can use the classifier to actually provide back inputs for the generator.

### 00:56:47 · Speaker 2

What do you mean by

### 00:56:48 · Speaker 10

Uh what do you mean by that? What do you mean by see again don't think of back proclamation nothing right? I mean just think think of it at a philosophical level. I just want you to tell me how to use this classifier to tweak theta. Okay let me maybe answer because it will take some more time. I'm sorry yeah that's okay. So what what is what I would do is I would tweak theta okay let me write that down.

### 00:56:53 · Speaker 2

um

### 00:57:04 · Speaker 3

Yeah

### 00:57:11 · Speaker 10

answer to that is

### 00:57:13 · Speaker 3

bus

### 00:57:14 · Speaker 3

But keep

### 00:57:18 · Speaker 3

changing theta

### 00:57:22 · Speaker 3

Theta, Right? Till

### 00:57:25 · Speaker 3

the classifier fails.

### 00:57:34 · Speaker 3

Okay. So, what is that what do I mean?

### 00:57:37 · Speaker 10

by that. So what I do is I will take a theta, okay? And I will see the performance of the classifier. Now classifier is doing pretty well, okay? So then it's not useful for me. What I'll do is I'll keep changing theta till such a point, okay? where my classifier completely fails.

### 00:57:58 · Speaker 10

You understand?

### 00:58:00 · Speaker 10

Now, when would my classifier fail? So now the next

### 00:58:03 · Speaker 3

this question is, this implies that if

### 00:58:07 · Speaker 3

the classifier file, okay?

### 00:58:15 · Speaker 3

Then, okay, then, P theta is actually equal to P X, that's my claim. Do you

### 00:58:20 · Speaker 10

agree with that

### 00:58:22 · Speaker 10

See if this classifier cannot distinguish between the samples of P X and P theta, when would that happen? That would happen only when P X is equal to P theta, isn't it?

### 00:58:37 · Speaker 10

You understand?

### 00:58:40 · Speaker 10

Yes sir. The classifier would fail only if P X is equal to P theta. So now what I'll use I'll just simply use that I'll invert this logic and say that okay now if I have a classifier that would classify between the samples of P X and P theta I would keep training or rather tweaking my theta okay till a point

### 00:58:40 · Speaker 3

Yes sir

### 00:59:00 · Speaker 3

where my classifier starts failing

### 00:59:05 · Speaker 3

Do you understand this?

### 00:59:10 · Speaker 1

Yes sir

### 00:59:13 · Speaker 3

Okay

### 00:59:13 · Speaker 10

So this is how like you know a lot of these blog posts etcetera would motivate Gyaans okay they'll say that oh there's a classifier and you want to make that classifier fail because only when when that classifier fails then your P theta will go close to P X. will will be exactly equal to P X okay.

### 00:59:33 · Speaker 10

But there is a catch here. I'll tell you what what the catch is. Yeah, I think there are some questions. Raghavendra.

### 00:59:40 · Speaker 5

Yes, are we saying that in at this stage the classifier

### 00:59:44 · Speaker 7

is perfect that is able to distinguish between X or X not all the time

### 00:59:48 · Speaker 10

what what stage at what stage

### 00:59:50 · Speaker 7

So so now I mean with this assumption that the classifier is able to do that right so are we already saying that it is perfect at doing it

### 00:59:55 · Speaker 10

when we start, when we start, right? I mean, we are assuming that okay, the classified

### 01:00:00 · Speaker 5

disable to classify.

### 01:00:02 · Speaker 2

Okay

### 01:00:02 · Speaker 5

right? But the argument that I'm going to give you in a while will tell you that it is not enough if you just make the classifier fail. See, this thing that I said, no, that if the classifier fails, then P theta equal to P X, right? is is not completely true.

### 01:00:18 · Speaker 5

Okay, I don't know if you can see that failure case already, but I I'll show you that. I'll show you that in a while. But yeah, any other questions, Sanchit? Yeah.

### 01:00:28 · Speaker 3

Sir, I'm not sure if you are going to cover this question ahead but just asking. uh So, change tweaking the theta randomly, it will take like really, really long time. So, do don't we have some parameter that will govern or that will tell us, okay, in which direction we have to tweak theta?

### 01:00:33 · Speaker 5

uh

### 01:00:49 · Speaker 5

हां, हां, हां, दैट इज करेक्ट, दैट इज करेक्ट। बट हां, यू विल सी हाउ टू डू दैट।

### 01:00:54 · Speaker 5

Yeah, it will it will see the direction now is simply that it it it should be in such a way that the P theta should be close to equal should be close to P X. That is the direction that we are talking about. Anyway, so now, I mean, if all of you are convinced that if the classifier fails that P theta equal to P X, this is this may not be true always, right?

### 01:00:54 · Speaker 3

Okay

### 01:01:15 · Speaker 4

I'll tell you why

### 01:01:16 · Speaker 5

Sir

### 01:01:18 · Speaker 4

However,

### 01:01:23 · Speaker 4

Okay

### 01:01:24 · Speaker 0

classifier failures, okay? Classifier

### 01:01:30 · Speaker 0

failing, okay?

### 01:01:35 · Speaker 0

need not imply

### 01:01:47 · Speaker 0

p theta is equal to px, okay? I'll show you a counter example for this.

### 01:01:58 · Speaker 4

Okay. So let's say that our features are in two dimensions, okay?

### 01:02:01 · Speaker 5

the data is in two dimensions. Let's say that my true data is like this, it is.

### 01:02:11 · Speaker 5

This is clustered somewhere here. This is only for representations, okay? So this is this is samples from P X. Okay? Now let's say that when we start arbitrarily with uh with some uh G theta, okay? I will have data or rather uh P theta X cap. This is my X cap.

### 01:02:36 · Speaker 5

Okay. X cap is now sampled from P theta, okay? Now let's say that there exists a classifier that would classify between them. This is the decision boundary, this is my D W.

### 01:02:48 · Speaker 5

Okay. Now, uh okay, so first of all, please note that in practice, neither P X nor P theta would be nicely clustered like this and they are not linearly separable.

### 01:03:01 · Speaker 5

Okay, so I'm simply, you know, this is for illustration purpose, I'm assuming that they are linearly separable and there exists a linear disjunction boundary between them, okay? But it did not be the case. Okay. Now, what are we saying that we have to change theta such that the classifier fails, correct?

### 01:03:20 · Speaker 5

Is that is that okay? Now what is the decision that this classifier is making?

### 01:03:24 · Speaker 4

So

### 01:03:28 · Speaker 0

above the line

### 01:03:32 · Speaker 0

PX

### 01:03:36 · Speaker 0

below the line

### 01:03:39 · Speaker 0

P theta correct?

### 01:03:42 · Speaker 0

This is

### 01:03:42 · Speaker 4

the way the classifier is classifying

### 01:03:44 · Speaker 5

point. So do you agree?

### 01:03:46 · Speaker 5

whatever this above and below means.

### 01:03:49 · Speaker 5

Okay, this is what the classifier has learnt. Now, this has to fail. What do I do? So I am I I want to tweak my P theta such that the classifier fails, no? What I will do

### 01:04:00 · Speaker 0

I will just move this

### 01:04:01 · Speaker 5

Hello

### 01:04:02 · Speaker 0

Here

### 01:04:14 · Speaker 0

let me call this as P theta one and this is coming from P theta two. Okay. Now here

### 01:04:29 · Speaker 0

DW would fail, do you agree?

### 01:04:37 · Speaker 0

Does all of you agree that DW would fail here?

### 01:04:44 · Speaker 0

Yes, social

### 01:04:52 · Speaker 0

Yeah

### 01:04:52 · Speaker 4

But now DW has failed, but has it ensured that

### 01:04:57 · Speaker 5

θ2 is equal to px

### 01:05:03 · Speaker 5

p theta two is not equal to px

### 01:05:04 · Speaker 4

is not equal

### 01:05:07 · Speaker 5

You see that, right? So now

### 01:05:11 · Speaker 5

It's not enough if you simply make the classifier fail. The classifier can fail, right? Not only when P theta

### 01:05:21 · Speaker 5

is equal to P X. Of course, when P theta is equal to P X, classifier would obviously fail. However, if classifier fails, that does not imply that P theta of X, P theta is

### 01:05:33 · Speaker 5

is P X. Do you see that?

### 01:05:37 · Speaker 5

Now this implies

### 01:05:39 · Speaker 0

Start

### 01:05:41 · Speaker 0

p theta equal to px okay

### 01:05:46 · Speaker 0

employees

### 01:05:50 · Speaker 0

classifier fail

### 01:05:55 · Speaker 0

Okay? But classifier failure

### 01:06:03 · Speaker 0

does not imply

### 01:06:05 · Speaker 0

p theta being equal to px.

### 01:06:11 · Speaker 4

Is this clear? Any questions on

### 01:06:12 · Speaker 5

Indrajit

### 01:06:14 · Speaker 1

Yeah, when you are moving x hat above the line, will discriminator not adjust the line to again differentiate between these two?

### 01:06:22 · Speaker 5

Good question. We have not done that yet, right? Have we done that?

### 01:06:26 · Speaker 1

No but discriminator will do na

### 01:06:29 · Speaker 5

No, no, no, we have said the classifier is fixed here, right? And by the way, I have not used the word discriminator. I'm simply saying it's a classifier.

### 01:06:37 · Speaker 5

So, I mean, I told this in the first class, you know, please use the terminologies and the names that I've been using. I mean, I understand that it is difficult because you already know all this, right, from other sources, but it's good to use because there's a reason why I'm using those names. For now, this is a classifier, okay? So, classifier is fixed. I'm not changing the classifier.

### 01:06:59 · Speaker 5

Okay. Now the uh the if the classifier is fixed then simply moving theta such that the classifier fails does not uh uh you know does not suffice. Does not serve our purpose.

### 01:07:00 · Speaker 4

Oh

### 01:07:15 · Speaker 1

Yeah, but when you say classifier is fixed, do you mean this line is fixed? Because otherwise he will try to classify when he has simple different sample.

### 01:07:19 · Speaker 5

exactly

### 01:07:22 · Speaker 5

simple different sample. This this line is fixed.

### 01:07:27 · Speaker 5

I don't know who he is. Yeah, but yeah, so classifier is fixed. When I say classifier is fixed, this of course this is the classifier that I'm talking about. It is fixed.

### 01:07:37 · Speaker 5

Okay

### 01:07:38 · Speaker 5

ஹரீஷ்

### 01:07:40 · Speaker 2

Sir, one question. So, our goal is to make P theta equal to P X, right? Correct. Correct. In that case, why do we need a classifier, for example? So, we can just use a regression problem to find the loss and just use the the generator, right?

### 01:07:46 · Speaker 5

Correct, Correct.

### 01:07:58 · Speaker 5

No, what what do you regress over? See, what do you regress over? X cap comes, right? Do you match every X cap to some X? Is that what you do?

### 01:08:08 · Speaker 5

So what are you suggesting that I I just make this, take a squared error loss and then minimize this? See if I do this, then what will happen is, uh the this neural network would simply generate whatever is there in your data. It will not generate anything new.

### 01:08:25 · Speaker 5

So you want to do it at a distributional level, no? That's why we are doing all this, yeah?

### 01:08:28 · Speaker 4

Dui

### 01:08:30 · Speaker 2

Yeah. So we need to understand the distribution rather than just using the samples.

### 01:08:35 · Speaker 5

absolutely that is that is been our problem from day one isn't it? we want it to be done at the distribution level.

### 01:08:41 · Speaker 2

Yeah, got it.

### 01:08:42 · Speaker 5

not at sample level, right? Okay. So now the thing is, yeah, so all of you got this, right? I mean, using the classifier and trying taking your P theta such that the classifier fails is not enough. You need to do something more. What do you think is that something more that you can do?

### 01:09:00 · Speaker 3

maybe the discriminator should dynamically learn

### 01:09:05 · Speaker 5

Yeah, so you move the line. What you should do is you move the line, okay? If this line, okay, so what you do is first you have make this, this is D W one. Under this D W one,

### 01:09:19 · Speaker 5

this happened, okay? What I'll do is I will learn another line here.

### 01:09:23 · Speaker 0

I'll learn another classifier, okay? This is now

### 01:09:33 · Speaker 0

by DW2

### 01:09:39 · Speaker 0

Okay? Now,

### 01:09:40 · Speaker 4

have to move this P theta again.

### 01:09:42 · Speaker 5

टू एन्श्योर दैट दिस इस मिसक्लासिफाइड अंडर डी डब्ल्यू टू एस वेल।

### 01:09:49 · Speaker 5

You get it?

### 01:09:51 · Speaker 5

which means that this P theta two now cannot go to P theta one place, okay? It has to go somewhere else. So let's say

### 01:09:58 · Speaker 0

this will move somewhere here

### 01:10:11 · Speaker 0

So now the idea is, so this will become

### 01:10:14 · Speaker 5

P theta three na

### 01:10:16 · Speaker 5

The idea is, you know, keep moving your theta cluster distribution, right? So till a point where these two overlaps. Now, how do you do that? You do that by tweaking this classifier, okay, all the time. Maybe I should have written this classifier in a

### 01:10:32 · Speaker 0

different color

### 01:10:55 · Speaker 0

These are our axes. And you have

### 01:10:59 · Speaker 0

the first classifier

### 01:11:05 · Speaker 0

P W one, okay? And you have another classifier which is

### 01:11:13 · Speaker 0

like this this is T W two.

### 01:11:18 · Speaker 4

Is that all right? You see what's happening? So basically we are so

### 01:11:25 · Speaker 0

Therefore, okay.

### 01:11:26 · Speaker 0

the classifier, okay?

### 01:11:32 · Speaker 0

has to be

### 01:11:36 · Speaker 0

change

### 01:11:40 · Speaker 0

or tweet simultaneously

### 01:11:57 · Speaker 0

Does it make sense?

### 01:12:00 · Speaker 0

Now you might ask, right? So now what is the guarantee?

### 01:12:03 · Speaker 5

that

### 01:12:08 · Speaker 5

Yeah, what is the guarantee that when I keep doing this, I will I will go I will I will ensure that my P theta is exactly overlapping on P X, right? It can actually play a cat and mouse game, right? Where the classifier place moves this to some place and then the generator tries to avoid the classifier and it they keep kind of playing that game between those two, correct?

### 01:12:35 · Speaker 5

You understand? So in this case what can happen no this cluster moves here and then it will come back. So then when you try in the new classifier it will go again here and it will come back and it will keep it can keep moving around. Can all of you see that? That this moving around can happen.

### 01:12:52 · Speaker 5

So that is exactly what is called as mode collapse.

### 01:12:55 · Speaker 5

okay? Where the the the Gyan training, right? Is is very unstable. You will actually see that when you are training. So what happens is that the so-called classifier, right? When you are training, the classifier tries to avoid the discriminator and the discriminator or rather the generator and generator tries to avoid the classifier and it keeps happening happening alternatively. Now, what is actually happening underneath under the hood is, every time you construct this classifier, right? You are creating a lower bound on the FW.

### 01:13:25 · Speaker 5

You understand? So what do you mean by creating a lower bound on the F divergence is uh learning a new classifier. Now you can see that right? The tighter the lower bound is, the better the minimization would be, isn't it?

### 01:13:43 · Speaker 5

obviously, right? The tighter the lower bound is on F divergence, the better the minimization would be. What do you mean by creating a tighter lower bound? Is that you create a classifier that is close enough or a very good classifier and in this example I've created a very degenerative case where the classifier is linear and the data is very nicely clustered. But in practice, right? You will have these points here and you will have X points here and the classifier will be a non-linear classifier, right? So classifier will do misclassification, okay? However, the tighter the lower bound is, the better this classifier would be.

### 01:14:17 · Speaker 5

That's how the translation happens in the sense that when the case you consider the F divergence to be Jensen-Chanell divergence, right? You can you can look into this as interpret this as a classifier, right? And because you can interpret it as a classifier, constructing a tighter lower bound translates to creating a classifier that is very good. Okay? Now if your generator function has to like make that very good classifier misclassified, okay? It would better move the

### 01:14:47 · Speaker 5

cluster close to P X because if there is a perfect overlap between these two right P X and P theta there is no classifier that is able to classify these two you understand that

### 01:15:00 · Speaker 5

Do you see that? If there exists if if if P X completely overlaps with P theta, then no classifier can classify between P X and P theta, right? Points from P X and P theta. Do you agree?

### 01:15:14 · Speaker 5

So what would that translate to? That would translate to saying that your T function, right, or the script T function is is representative enough to give you a T X such that the lower bound that we have created on the F divergence becomes tight. There is no approximation here, the lower bound becomes exactly equal to the F divergence. Now it becomes exactly equal to the F divergence, then then minimizing that would make P X to be equal to P theta, right? And which means in this case of junction channel divergence, there is no classifier that would that would classify between the points of P X and P J.

### 01:15:52 · Speaker 5

Is this clear?

### 01:15:55 · Speaker 5

So constructing a lower bound is equivalent to finding this class new classifier, right? Given a particular P X and P theta, constructing the lower bound on F divergence,

### 01:16:05 · Speaker 5

is equivalent to finding out this classifier that would classify between these two.

### 01:16:11 · Speaker 5

ओके? एंड मिनिमाइजिंग द लोअर बॉन्ड इज इक्विवेलेंट टू मूविंग दिस पी थीटा

### 01:16:18 · Speaker 5

इन दिस स्पेस ऑफ डेटा सच दैट इट विल गो इट विल मेक दिस क्लासिक वेयर फेयर।

### 01:16:21 · Speaker 3

Are you using a pointer, sir?

### 01:16:23 · Speaker 5

using a

### 01:16:26 · Speaker 5

Unfortunately, there is no pointer in this. It would have been so nice if there is a pointer. Does anybody know if there is a pointer here?

### 01:16:34 · Speaker 2

No sir

### 01:16:34 · Speaker 0

Sir

### 01:16:35 · Speaker 2

iPad it's not there.

### 01:16:38 · Speaker 5

Yeah, so, yeah, I'm not because I don't I can't use a pointer. Is this clear?

### 01:16:45 · Speaker 5

So before you ask your questions, right, let me just complete this story and then. So now instead of writing f divergence and all that, right? Now we can if we have to optimize this, so I mean write this as a cost function, right? So what we have to do is, uh let's say that my x is coming from uh px, right? Then I want the log like okay. So this

### 01:17:15 · Speaker 5

Let

### 01:17:17 · Speaker 4

Okay, let me write what I'm trying to write. So this is like formulating

### 01:17:25 · Speaker 4

formulating

### 01:17:26 · Speaker 0

the cost, okay? via this interpretation. This is what I will do now.

### 01:17:40 · Speaker 0

Okay. Suppose we still have the exact same setup.

### 01:17:43 · Speaker 5

okay? setup has not changed. So Z comes from normal zero one and you have G theta of Z and what you get here is X cap that comes from P theta. Okay? Suppose, suppose.

### 01:17:58 · Speaker 5

CW, okay?

### 01:18:01 · Speaker 5

is a function from X to

### 01:18:04 · Speaker 0

space of zero and one. Okay. Now let

### 01:18:10 · Speaker 0

PW represent

### 01:18:19 · Speaker 0

Let D W represent

### 01:18:24 · Speaker 0

the likelihood of

### 01:18:30 · Speaker 0

likelihood of a sample

### 01:18:41 · Speaker 0

coming from

### 01:18:42 · Speaker 4

Hello

### 01:18:42 · Speaker 0

p x. Okay, this is the way I have defined

### 01:18:44 · Speaker 4

T W, right? It simply gives you the likelihood of a sample coming from P X. So what do we need? So whenever

### 01:18:56 · Speaker 0

it comes from uh

### 01:19:01 · Speaker 0

px

### 01:19:03 · Speaker 0

we want

### 01:19:03 · Speaker 5

want it to be maximized no

### 01:19:06 · Speaker 5

A classifier should maximize the likelihood, okay? uh Or let's say P X or P theta. It simply gives you the likelihood of P X or P theta. Okay? So whenever whenever uh X comes from P X, I want to maximize that likelihood under the expectation. Do you agree?

### 01:19:29 · Speaker 0

So this is

### 01:19:31 · Speaker 0

I'll write a max here. So I have to maximize, maximize.

### 01:19:39 · Speaker 0

the likelihood of

### 01:19:44 · Speaker 0

Okay, X

### 01:19:47 · Speaker 0

coming from P X. This is that term. Do you agree?

### 01:19:52 · Speaker 5

Let me write it as P X for a volume. Is this okay? So this term is simply maximizing the likelihood of log likelihood of, okay? uh X coming from P X. Is that alright? Yes, over W.

### 01:20:11 · Speaker 0

Hello. Is this all right?

### 01:20:19 · Speaker 0

Now, now. So what is log of

### 01:20:31 · Speaker 0

Okay. Right, this first.

### 01:20:36 · Speaker 0

What is one minus T W of X? What is this?

### 01:20:44 · Speaker 0

system is

### 01:20:47 · Speaker 0

What is this term?

### 01:20:56 · Speaker 2

the likelihood that it comes from the

### 01:20:59 · Speaker 0

like

### 01:21:00 · Speaker 0

Okay

### 01:21:00 · Speaker 4

directly hurt

### 01:21:02 · Speaker 2

from p theta

### 01:21:03 · Speaker 4

is not from P X

### 01:21:10 · Speaker 0

Right? Or in this case,

### 01:21:13 · Speaker 0

comes from P θ

### 01:21:18 · Speaker 0

Correct?

### 01:21:21 · Speaker 0

Correct? Is it okay?

### 01:21:26 · Speaker 4

Now what do we have to do? We'll have to

### 01:21:31 · Speaker 0

speed theatre.

### 01:21:34 · Speaker 4

So, maximum that x cap is not from px. Oh yeah, this is from v theta, correct. Thanks.

### 01:21:45 · Speaker 4

We need to maximize this as well, right? We need to maximize. Okay,

### 01:21:48 · Speaker 0

to write that this thing also

### 01:21:55 · Speaker 4

Now when X is coming from X cap is coming from B

### 01:22:00 · Speaker 5

Heater

### 01:22:03 · Speaker 5

we need to maximize this with respect to W. So this DW which is a classifier has to do two things. Whenever X comes from PX, it has to maximize the the likelihood of X coming from PX. Whenever X is not coming from PX or rather X cap is coming from P theta, it needs to maximize the

### 01:22:25 · Speaker 5

inverse of the log likelihood rather one minus the likelihood of x coming from p.

### 01:22:28 · Speaker 4

to you. You see this point?

### 01:22:37 · Speaker 0

So

### 01:22:38 · Speaker 4

the

### 01:22:41 · Speaker 4

Objective

### 01:22:44 · Speaker 4

for

### 01:22:45 · Speaker 4

classify

### 01:22:46 · Speaker 0

ಟ್ರೈನಿಂಗ್

### 01:22:52 · Speaker 0

case

### 01:22:54 · Speaker 0

whenever the x is coming from

### 01:22:57 · Speaker 4

P X

### 01:22:59 · Speaker 5

just maximize that likelihood

### 01:23:03 · Speaker 4

Okay

### 01:23:04 · Speaker 5

and whenever x is

### 01:23:08 · Speaker 5

not coming from P X or rather it's coming from P theta.

### 01:23:11 · Speaker 4

Matchi Mice

### 01:23:14 · Speaker 0

See

### 01:23:16 · Speaker 0

log of one minus that likelihood.

### 01:23:26 · Speaker 0

Right I need to maximize this with respect to W.

### 01:23:35 · Speaker 0

Is this clear to all of you?

### 01:23:44 · Speaker 0

Okay

### 01:23:46 · Speaker 0

Okay

### 01:23:47 · Speaker 0

How

### 01:23:47 · Speaker 4

Now what do we have to do? See now the

### 01:23:50 · Speaker 0

Objective

### 01:23:55 · Speaker 0

for

### 01:23:57 · Speaker 0

Generator Training

### 01:24:04 · Speaker 0

What is it? What is the objective for generator training now?

### 01:24:11 · Speaker 0

simply

### 01:24:14 · Speaker 0

Invert

### 01:24:16 · Speaker 0

the objective for classified training.

### 01:24:28 · Speaker 0

Because what do we why do we have to do that? The here the objective is to make the classifier fail, no?

### 01:24:41 · Speaker 4

How do we do that?

### 01:24:45 · Speaker 0

classifier is

### 01:24:46 · Speaker 4

classifier

### 01:24:47 · Speaker 5

classifier is maximizing something, it is minimize that. You just completely undo whatever the classifier has done. So if I call this as some J, okay, of theta comma W.

### 01:25:01 · Speaker 0

you need to

### 01:25:04 · Speaker 0

If

### 01:25:10 · Speaker 0

classifiers

### 01:25:12 · Speaker 0

maximizing J theta comma W with respect to W

### 01:25:16 · Speaker 4

you then

### 01:25:19 · Speaker 4

Generator

### 01:25:22 · Speaker 4

minimize exact same objective with respect to theta. Therefore,

### 01:25:30 · Speaker 5

complete Gyan training is

### 01:25:34 · Speaker 5

that you have this J theta comma W, okay? The classifier has to maximize this while the generator has to

### 01:25:42 · Speaker 0

So again we came into the saddle point problem.

### 01:25:55 · Speaker 0

this is

### 01:25:56 · Speaker 5

what you see in a lot of blog posts and you know the popular explanation of what Gyan is. Including the original Gyan paper they say that okay we have a classifier. So we need to tweak the this is what is called as the discriminator right because it's basically a classifier.

### 01:26:16 · Speaker 5

discriminator is it just discriminates or classifies between the points from P X and P theta, okay? And now you have to tweak the classifier in such a way that P X is going to go to P theta. It is not enough if you just try in the G theta because the classifier can fail even without making P X equal to P theta. So you have to tweak try in the classifier also along with the generator alternatively and the classifier objective is given by just maximizing. This is the cross entropy objective, right?

### 01:26:46 · Speaker 5

and the generator has to invert what the discriminator is doing and that's how you get into a saddle point problem.

### 01:26:52 · Speaker 5

Okay? However, remember that this is this interpretation is only when you assume your F divergence to be the Jensen channel divergence in which case the T network, right, that would create a lower bound on the F divergence happens to be a classifier. It can be interpreted as a classifier.

### 01:27:11 · Speaker 3

Sorry

### 01:27:12 · Speaker 5

Now you can see the nice connect, right? See this objective function, right? Is not some magical thing that just emerged. Okay? It had a very nice grounded mathematical interpretation where this maximization is actually creating the lower bound between the f divergence between uh lower bound on the f divergence between px and p theta, right? So once you create that lower bound, you minimize that and you alternate between creating a tighter lower bound and then minimizing

### 01:27:42 · Speaker 5

Okay, if you see that from, you know, if you take one particular if divergence and interpret this DW as a classifier, in that case you can, you know, you can write it this way, but it is not, see this way of interpreting is not, I'm not a big fan of this because it's too hand maybe, right? I mean

### 01:28:03 · Speaker 5

I don't know but it's just my choice. uh See I would see like more value and more more principle of understanding in saying that oh you start with an f divergence you want to minimize that and to minimize that you want you don't know px and p theta therefore you construct a lower bound express them as expectations over these two because you can compute them and that lower bound happens to be an optimization over another class of neural networks okay and you construct the lower bound and

### 01:28:33 · Speaker 5

is that you keep alternating between these two. So that's my way of looking at it. But if you make your f divergence to be one particular f divergence called Jensen-Sanon divergence, then this t function that is used to create the lower bound on the f divergence can be interpreted as a classifier and the rest of the story follows.

### 01:28:52 · Speaker 5

Okay? Is that okay? It is just one other interpretation or rather the popular interpretation of what the general case of feverish minimization is. And again you can see why it is called adversarial optimization right? You have like a saddle point problem right? Adversity saddle point problem or

### 01:29:08 · Speaker 4

first

### 01:29:10 · Speaker 4

adversarial optimization

### 01:29:17 · Speaker 4

because there are two neural networks, one which is trying to undo what the other does.

### 01:29:21 · Speaker 5

Okay, it is adversarial optimization.

### 01:29:26 · Speaker 5

Okay? So finally, right, uh like post training, I'll take questions after this. Post training, I don't know if I do if I told you this last time, post training, inference, what how do you do, how do you use GAN for inference?

### 01:29:41 · Speaker 5

is that you take

### 01:29:44 · Speaker 4

the

### 01:29:45 · Speaker 4

tried generator.

### 01:29:48 · Speaker 4

throw away the discriminator completely.

### 01:29:54 · Speaker 5

Discriminator is like a poor teacher, right? Once you learn from them, you just throw them away.

### 01:30:00 · Speaker 5

Yeah. So then this x cap comes from p theta. Now this p theta has become close to px.

### 01:30:12 · Speaker 5

In fact, there's a nice Zen saying, okay, and this Buddhist Zen saying which I which I uh which I hold very close to my heart, which I keep telling to telling all my students, I don't know if I've told you this. It says that a good teacher, okay, is one who becomes redundant or useless after some time.

### 01:30:36 · Speaker 5

Right so that is the definition of a good teacher or a mentor. So you should make your mentees right or your students independent of yourself after some time. Now if you if you keep you know keep your students your students or keep your subordinates or mentees your mentees for all your life. You will become a boss right not a good leader or a teacher a teacher should become useless after some time so after you after this course is done you should not be coming back to me because

### 01:31:06 · Speaker 5

Like you have actually got everything that you want, you have become so independent that you can do things without a teacher. My teacher told me this, right? And I'm just passing that to you. In fact, there is another nice saying that says that that if when a student is ready, the teacher appears.

### 01:31:25 · Speaker 5

ओके। व्हेन अ स्टूडेंट इज़ रियली रेडी, द टीचर डिसअपीयर्स।

### 01:31:31 · Speaker 5

It's very nice, right? It's very deep actually, right? So the the goal of a teacher is to ensure that the student is ready, which is that you know your P theta is what the distribution that the students are in, right? And you want them to go to P X. Once you have used whatever methods, you know, you can become like an adversary, you can scold them, do whatever and you just invert whatever they are saying in an adversarial manner. Once they become theta star, right? Go away, there is no use for you, right?

### 01:32:01 · Speaker 5

So that is what it is, right? During inference what you do is you sample a point from Z. uh you get a you get a sample from a normal distribution. Pass it to the generator, you get a sample X cap, right? That is from P theta now which is close to P X. So uh I mean if you remember I showed you that no this person does not exist dot com, right? Every time you do an inference or rather the refresh of the page, what is happening is a sample from Z is coming and it is going through a train generator and and a new sample is getting generated from P.M.S. Okay? So now ideally

### 01:32:39 · Speaker 5

ideally, right? X cap, okay? is not in D. Okay, the data set that you have given, no. Your new generated sample will not be in X. So if you take C Z one through Z K, you'll get corresponding X one cap through X K cap, okay? None of these, okay? are in D. So there are new samples that are not in D. That's how you do inference.

### 01:33:05 · Speaker 4

is also called

### 01:33:07 · Speaker 4

generation

### 01:33:13 · Speaker 4

Okay? See,

### 01:33:15 · Speaker 5

we have still we have still not done what is called as unconditional generation. This is still sorry we have not done what is called as conditional generation. It is still unconditional generation because uh it is not that okay you give a text and a corresponding image gets generated right? It is simply an image gets generated okay or a data point gets generated without any conditioning. So in the next part of the class I will talk about how to try in this or how to convert this into a conditional generator in a while. Okay? But yeah so this is how you

### 01:33:45 · Speaker 5

inference. So we are done with training, we are done with inference. This is how we do training of again and an inference. I have asked you to do both of these in your assignment. So to implement them. So one other detail, uh see there is I have asked you to implement something called a

### 01:34:03 · Speaker 4

if convolutional beyond, okay?

### 01:34:11 · Speaker 4

abbreviated as DC Gyan

### 01:34:15 · Speaker 4

What is the

### 01:34:15 · Speaker 5

Please

### 01:34:16 · Speaker 4

Hello

### 01:34:17 · Speaker 5

simple thing, right? So you start with you build a neural network, right? G theta network. You start with Z, okay, that is let's say in some thirty two dimensional space. Okay, let me write that. So you sample Z from a Gaussian distribution.

### 01:34:33 · Speaker 5

Okay? And that Gaussian distribution is in some sixteen dimensional space, let's say.

### 01:34:43 · Speaker 5

sixteen dimensional space, okay? So now you take a vector that is sixteen dimensional, okay? Then you have to go to let's say that your data X is in some R hundred cross hundred. Now how do you convert this sixteen dimensional into hundred cross hundred? See one thing that you can do is you can have sixteen and then you have let's say thirty two, then you have sixty four and you know you keep increasing the dimensions till you have like a ten thousand dimensional vector, okay?

### 01:35:13 · Speaker 5

So this is your X cap, this is your neural network G theta. And then after you get this X cap, no, then you can do a reshaping.

### 01:35:21 · Speaker 5

So X cap

### 01:35:24 · Speaker 5

six cap is in R ten thousand ten thousand cross one dimensional right which is a vector and once you get this you reshape

### 01:35:36 · Speaker 5

into hundred by hundred. So that you know it will look like a grid of images. Okay? And you have to do the same thing for x you know x is in hundred by hundred right?

### 01:35:48 · Speaker 4

So when you send it to the discriminator, you should reshape that.

### 01:35:58 · Speaker 4

இன்டு டென் தௌசண்ட் க்ராஸ் ஒன்

### 01:36:01 · Speaker 5

reshape x into ten thousand cross one and you reshape x cap into hundred by hundred. This is one thing that you can do and this neural network is a is a multi layer perceptron right or a fully connected neural network. Okay. You have seen how to do this fact propagation and all that. This is one way to do it. The other way to do it is that you start with a sixteen dimensional vector okay and then do what is called as transpose

### 01:36:25 · Speaker 4

convolution or upsampling

### 01:36:33 · Speaker 4

Does all of you know about convolutional neural networks here, C N Ns? Is there anybody who does not know about C N Ns?

### 01:36:47 · Speaker 4

Okay, I'll take that as an S. So,

### 01:36:49 · Speaker 5

assuming that all of you know about CNNs, right? So what you can do is, see what does a CNN does? A convolutional network does. It will take a grid of images like this and you have a kernel which is let's say three by three kernel. You place that three by three kernel on this grid, okay? And take the inner product and you get another grid, okay? So every point in this smaller grid will now become an inner product between these two and one number and you you

### 01:37:17 · Speaker 5

move this three by three grid again and you get the next uh thing and so on right that is how you do it so this is convolution. There is something called transpose convolution where you start from a lower dimensional uh vector right and then you create a grid okay by doing inwards of convolution that operation is called transpose convolution. See I will I mean you can ask T A's to do it in the next T A session okay how to do transpose convolution.

### 01:37:47 · Speaker 5

However, there is a, there is a paper called, paper or a

### 01:37:51 · Speaker 4

I write up called convolutional arithmetic

### 01:38:00 · Speaker 4

Okay? So please refer to that.

### 01:38:03 · Speaker 5

they have given how transpose convolution works. So if you use transpose convolutions, right? You can finally get uh

### 01:38:13 · Speaker 5

at the final layer, right? You actually get a grid of

### 01:38:19 · Speaker 5

You can actually make it the grid of whatever size that you want. I mean if you are using a color image, that is what I've given you, it will be like hundred cross, hundred cross, like three channels, right? R G B.

### 01:38:33 · Speaker 5

Okay, by using transpose convolutions, you can get into get that into a three hundred cross hundred cross three. You don't have to uh like uh reshape it. And the discriminator that you have here, right?

### 01:38:48 · Speaker 5

will simply become a C N N. So it will take a hundred cross hundred cross three vector itself. Okay? And give you a number between zero and one. This will be a proper C N N. Okay you can use a resnet or whatever network that you want.

### 01:39:02 · Speaker 5

Okay, so

### 01:39:04 · Speaker 5

not resent this net

### 01:39:11 · Speaker 5

You can ask T S to cover this if you want, right? What is transposed convolution and so this if you use instead of using multilayer perceptrons, if you use transposed convolutions, this entire thing, no, this is what is called as a deep convolutional DC GAN where for discriminator you are using a C N N, okay? And for the generator you are using transposed convolutions, you are not flattening them all, okay? That's your DC GAN.

### 01:39:36 · Speaker 5

Okay

### 01:39:37 · Speaker 5

Okay, so that's that. So we will take a break now, uh and then maybe, you know, go to I'll talk about the conditional Gyan and uh I mean, uh the some of the applications of Gyan as I promised. Before that, I'll take questions on this if there are any. Raghavendra.

### 01:39:55 · Speaker 2

Yeah, so there's a two questions. One thing you mentioned is this classifier interpretation holds true only for this JS divergence. Why is that so?

### 01:40:03 · Speaker 5

wise that

### 01:40:05 · Speaker 2

Why is that specific only for G S time visions?

### 01:40:05 · Speaker 5

because

### 01:40:08 · Speaker 5

for others, okay

### 01:40:10 · Speaker 5

for others, this will become a the the I mean this thing right will not be a classifier between zero and one right this network will give you a real number. See depends if you recall the output of that T network should come from domain of F star isn't it?

### 01:40:29 · Speaker 4

Hmm

### 01:40:30 · Speaker 5

So that domain of X star for this case will become zero to one. For the other cases it will become a real number. So in which case the output of that network will become a regressor. It will not I mean whatever the case might be you know it is not a you cannot interpret that as a classifier.

### 01:40:36 · Speaker 4

S

### 01:40:39 · Speaker 4

not

### 01:40:46 · Speaker 2

Okay, but I mean it is it is still trying to distinguish, right? It is still trying to distinguish between the other cases. No, no, no. No. So how can we interpret it in that case? What output of the discriminator, how can we interpret that?

### 01:40:49 · Speaker 5

No no no no. No no no no. No. So how can we interpret

### 01:40:55 · Speaker 5

What output

### 01:40:57 · Speaker 5

I understood

### 01:41:00 · Speaker 5

understood the question. So he said to me, you cannot interpret that at all.

### 01:41:05 · Speaker 5

So there is no classification that is happening. That is why I don't give this as the, you know, uh the uh the ultimate interpretation. Because only with distance and divergence this becomes a classifier. For other divergences, no, it is not a classifier. For instance, there is a paper called as I said, no, LS Gyan where what is getting minimized is chi-square distance. Let me just show you my screen and that will become like maybe more apparent.

### 01:41:39 · Speaker 0

Do you see my screen?

### 01:41:40 · Speaker 4

Yes

### 01:41:45 · Speaker 0

Yeah. Look at this, na?

### 01:41:49 · Speaker 5

if for different divergences the final output activation is different for PS and chi square distance the output activation is a linear function so which is a regressor

### 01:41:59 · Speaker 5

You understand? Yeah. So only with Jensen Chan and divergence you have this kind of thing which is bounded between zero and one which becomes a classifier. Now if you use K and divergence etcetera right you will just have a line that's all. So which cannot be interpreted anywhere.

### 01:42:00 · Speaker 2

Yeah

### 01:42:16 · Speaker 2

Okay

### 01:42:18 · Speaker 2

Yeah, and the second question, See, hold on, hold on.

### 01:42:18 · Speaker 5

right?

### 01:42:19 · Speaker 5

See, hold on, hold on. The way to, the way to interpret that is if you want to, right? It is simply a neural network that is creating a lower bound on the underlying F divergence.

### 01:42:30 · Speaker 2

Mm-hmm, okay.

### 01:42:33 · Speaker 2

Yeah, and the second question is uh again with respect to lowering this, I mean or tightening this lower bound. Um you mentioned that uh the ultimate aim is not really to get uh back the samples which we trained, right? I mean we want something different. So you also mentioned that the X hat that comes out is is not in the D. Yeah. Yeah. Can we really ensure that? Uh or or the question is if you

### 01:42:52 · Speaker 5

okay

### 01:42:53 · Speaker 5

Yeah

### 01:42:56 · Speaker 5

or the question is if you... Of course, it depends on, it depends on how tight your lower bound is.

### 01:43:02 · Speaker 2

If it is very tight

### 01:43:05 · Speaker 5

If it's very tight then actually you will get to P X, no? Which means that you will get very diverse samples.

### 01:43:12 · Speaker 2

Okay, but not the same samples as what you trained with.

### 01:43:16 · Speaker 5

No, because you are you are meaning you are doing it at a distributional level, that's the whole point.

### 01:43:20 · Speaker 2

Okay, okay. The whole point is that you have you have

### 01:43:21 · Speaker 5

The whole point is that you have you have made the distribution same. See why did we even start with all this F divergence etcetera is that we don't want to overfit right? I mean overfitting in in the case of generating models is when you match the distributions exactly sorry when you only match the samples not at the distribution level.

### 01:43:25 · Speaker 2

white

### 01:43:40 · Speaker 2

Okay. So even if you if you ensure the the distributions are same, because we are doing a random sampling you wouldn't get the same

### 01:43:40 · Speaker 5

Okay

### 01:43:40 · Speaker 5

So even if you

### 01:43:47 · Speaker 5

Absolutely, absolutely. Random sampling is happening because your input, right? It's actually converting one random variable to the other. You're still, yeah. So, but you have to ensure that the distributions are matched. So if the lower bound that you are that you are constructing is very weak, right? Then you will not match distribution because you have you have anyway minimized a very low, very loose lower bound on the F divergence.

### 01:43:48 · Speaker 2

Training points okay

### 01:43:52 · Speaker 2

actually

### 01:43:55 · Speaker 4

Exactly

### 01:44:04 · Speaker 4

hmm

### 01:44:04 · Speaker 2

hmm

### 01:44:06 · Speaker 2

correct

### 01:44:12 · Speaker 2

Okay. Yeah, understood.

### 01:44:13 · Speaker 5

Yeah

### 01:44:14 · Speaker 5

That is why people say that GAN training is very difficult. One because you are solving that shadow point optimization problem. The other thing is the lower bound that you might get, no, might be very very loose. If it's very loose, then if you look at that classifier interpretation, your classifier is simply, you know, trying to move it in different places without ever overlapping it with PX.

### 01:44:15 · Speaker 2

by

### 01:44:26 · Speaker 2

Hmm

### 01:44:39 · Speaker 0

Mm, yep.

### 01:44:40 · Speaker 5

And also I didn't tell you last class, right? What is the stopping criteria in training this? There is actually no not well known stopping criteria for this, okay?

### 01:44:48 · Speaker 3

stop

### 01:44:51 · Speaker 5

the the only stopping criteria is is when you know people just eyeball the quality of the images or the data that is generating they just have some pseudo metric to to generate what it is I mean the pseudo metric to measure the goodness of the samples and then they use that to stop. There is no one good stopping criteria. So is that because we

### 01:45:13 · Speaker 2

Is that because we, Is that because we do not know what is the really the tightest bound that we can get?

### 01:45:19 · Speaker 5

Exactly. And also we don't know the what the underlying distribution is, no?

### 01:45:23 · Speaker 2

Okay

### 01:45:26 · Speaker 5

Got it. See also no next part of the class I'll talk about this versus strains distance and uh and uh F I D right there is a score called Faschets inception distance which I'll talk about the next time. That is one thing that is used to monitor the goodness of the generated images. But stopping criteria is just that you eyeball the images and see the data and use some surrogate classes and just stop there.

### 01:45:53 · Speaker 2

Yeah, thank you, sir.

### 01:45:54 · Speaker 5

Okay. Yeah, Sanjay.

### 01:45:57 · Speaker 3

Sir in this example which you had mentioned right? Where we are considering this classifier D W one, D W two, D W three. uh Why not keep the uh existing classifiers when going for a newer classifier? Like what I mean to say is instead of uh going for this single layer perceptron method, why not for a multi layer perceptron here? So that we have the other classifier.

### 01:46:00 · Speaker 5

B.

### 01:46:05 · Speaker 5

Uh

### 01:46:24 · Speaker 5

I'm sorry I didn't follow your question. Can you repeat it again?

### 01:46:29 · Speaker 3

ओके। व्हाट आई एम सेइंग इज, वन्स वी मूव फ्रॉम डी डब्ल्यू वन टू डी डब्ल्यू टू, राइट? यू आर सेइंग दैट इट इज लाइकली पॉसिबल दैट पी थीटा टू माइट टेक द पोजीशन्स ऑफ पी थीटा वन, करेक्ट?

### 01:46:35 · Speaker 5

You are staying

### 01:46:42 · Speaker 5

Correct, Correct.

### 01:46:44 · Speaker 3

Now, if we have DW1 intact and then we go for DW2.

### 01:46:49 · Speaker 5

No, there is no intact, no, we have changed the classifier.

### 01:46:52 · Speaker 3

That's what sir, that's what I am trying to say. If if we are going for a change, right? Let's let's instead of going for single layer perceptron, we go for multi layer perceptron.

### 01:46:55 · Speaker 5

If

### 01:47:01 · Speaker 5

No no no. See multilayer perceptron will not will not prohibit the the decision boundary to go somewhere else not go to the previous layer no that has nothing to do with single layer multilayer. See multilayer single layer will simply tell you whether the decision boundary is what is the range of decision boundaries that you can learn.

### 01:47:25 · Speaker 5

See there is no remembering of the classic previous classifier that is happening here. You are just reiterating it completely.

### 01:47:33 · Speaker 3

No sir, what I'm what I'm saying is, we we go for a multi-layer perceptron approach. Like, we we say that okay we

### 01:47:41 · Speaker 5

Okay, we see again, please understand what a multilayer perceptron is. A multilayer perceptron is simply a deep neural network that has multiple layers, that's all.

### 01:47:50 · Speaker 3

Yes sir

### 01:47:50 · Speaker 5

So it does not mean that you are remembering something and all that here. It is simply a neural network.

### 01:47:58 · Speaker 0

and then

### 01:47:58 · Speaker 5

NMLP is a neural network, that's all.

### 01:48:01 · Speaker 0

Key

### 01:48:04 · Speaker 5

You understand? It is simply a multilayer perceptron. Did you under did you attend the tutorials?

### 01:48:12 · Speaker 3

Yes sir

### 01:48:13 · Speaker 5

In tutorials they talked about multilayer perceptrons and training them no?

### 01:48:19 · Speaker 3

Yes sir

### 01:48:20 · Speaker 5

So a multilayer perceptron is a neural network. I actually talked about a multilayer perceptron in the last class if you remember. What is a multilayer perceptron? You start with take data, okay, you multiply it with W transpose X and then you make that go through a non-linear. This is the first layer. The second layer is you take W two and then you do another non-linear. This is the second layer. This is the third layer and so on. This is an MLP. So the architecture will look like this, no? You start with this, have a fully connected and

### 01:48:50 · Speaker 5

you have W two, you have W one, then you have W two, this is an MLP, which is a deep neural network.

### 01:48:57 · Speaker 5

It has nothing to do with uh the classifier remembering what the previous state is and all that. That is not what we are doing. Do you see the difference?

### 01:49:06 · Speaker 3

Yes sir, I agree on that. But maybe, maybe the terminology I used was not correct. What I'm trying to say here is that...

### 01:49:07 · Speaker 5

on that but maybe

### 01:49:13 · Speaker 2

I think

### 01:49:15 · Speaker 5

Why not remember what the classifier was at the previous state, right?

### 01:49:18 · Speaker 3

Yes sir. It might not remember but if we go with this approach of multilayer perceptron then we might have a tighter No. tighter bound on the like the We are using multi

### 01:49:24 · Speaker 5

please

### 01:49:26 · Speaker 5

No

### 01:49:27 · Speaker 5

later found on the like the We are using multilayer perceptrons. We are using multilayer perceptrons. We are not using the linear discriminator anywhere here, right? So these are neural networks. These are deep CNNs. Even if you are using deep CNNs, see, note that your data is in some very high dimensional space and it can always go to a place where the classifier misclassifies.

### 01:49:50 · Speaker 3

Okay

### 01:49:51 · Speaker 5

Right? So it has nothing to do with the capacity of the classifier. You know, the the we are we are talking about data in some ten thousand dimensional space here.

### 01:50:02 · Speaker 5

Okay

### 01:50:03 · Speaker 0

Okay

### 01:50:04 · Speaker 5

Okay, any other question as Sarvesh?

### 01:50:10 · Speaker 3

Yes sir so this transpose convolution that you mentioned. Yeah. So for this the input the Z should it also be in a grid format or we can use one D convolution is it a right decision?

### 01:50:13 · Speaker 5

So

### 01:50:20 · Speaker 5

is it a right decision? Yeah, yeah, yeah, that is a right decision. People have seen both happening. But generally take people take Z to be a vector. Right? Not a grid.

### 01:50:33 · Speaker 5

Generally

### 01:50:35 · Speaker 2

Okay. Okay, so in general like

### 01:50:36 · Speaker 5

Let me just hold on, just hold on. Let me share that show the TC paper with you.

### 01:50:45 · Speaker 3

Appreciated

### 01:50:47 · Speaker 5

And also this convolutional arithmetic also is something that I'll show you. Hold on.

### 01:50:54 · Speaker 0

we are talking now convolutional arithmetic

### 01:51:07 · Speaker 0

Arithmetic

### 01:51:12 · Speaker 0

Guide to Convolutional Arithmetic

### 01:51:13 · Speaker 4

for deep learning. Yeah. I'll show you both of them.

### 01:51:19 · Speaker 4

Do you see my screen? Not yet.

### 01:51:25 · Speaker 4

You see my screen

### 01:51:27 · Speaker 0

Yes sir

### 01:51:28 · Speaker 4

this is that

### 01:51:29 · Speaker 5

convolutional arithmetic thing, okay? So, have a look at it.

### 01:51:34 · Speaker 5

they talk about all kinds of convolutions with striding, without striding, zero padding, without zero padding. Then you have pooling arithmetic. You see there is there is transpose convolution here.

### 01:51:48 · Speaker 5

Okay? So please have a look at this.

### 01:51:51 · Speaker 5

this is one thing

### 01:51:53 · Speaker 4

Other thing is

### 01:51:55 · Speaker 0

Sir

### 01:51:57 · Speaker 0

web start

### 01:52:01 · Speaker 0

PC Gyan paper

### 01:52:08 · Speaker 0

such as the T C Gyan paper

### 01:52:13 · Speaker 0

Yeah

### 01:52:14 · Speaker 5

This is how they do it. So at hundred dimensional Z and then then you reshape and then you have transverse convolutions, transverse convolutions and then you get to sixty four cross sixty four cross three.

### 01:52:28 · Speaker 5

start with a hundred dimensional uniform distribution Z is projected you got it no

### 01:52:34 · Speaker 3

Yeah, so vector only is converted into, Start from vector and then you, Yeah, then you do

### 01:52:36 · Speaker 5

start from vector and then you yeah then you do trans correct then you do up sampling transverse convolutions and then get to the final image dimensions

### 01:52:45 · Speaker 3

Okay

### 01:52:47 · Speaker 3

Thank you

### 01:52:50 · Speaker 5

Okay

### 01:52:51 · Speaker 4

anything else?

### 01:52:52 · Speaker 3

Sir, can you please share these uh documents which you were presenting?

### 01:52:58 · Speaker 0

Police

### 01:52:59 · Speaker 4

one country

### 01:52:59 · Speaker 0

conference

### 01:53:00 · Speaker 0

Six

### 01:53:09 · Speaker 0

We can't type anything here.

### 01:53:16 · Speaker 0

Hello

### 01:53:26 · Speaker 0

Nothing

### 01:53:37 · Speaker 0

ओके डन। ओके।

### 01:53:39 · Speaker 4

let's take a break no it is eleven five no let's come back at eleven twenty. okay and yeah. continue from here.

### 01:53:47 · Speaker 0

Russia

### 01:53:49 · Speaker 0

Okay, see you in about fifteen minutes.

### 02:10:39 · Speaker 0

Hello all

### 02:10:45 · Speaker 5

Sir

### 02:10:46 · Speaker 5

Yeah, you can hear me? Can you see my screen?

### 02:10:51 · Speaker 0

No sir

### 02:10:51 · Speaker 5

No, so

### 02:10:54 · Speaker 5

So which one should I shape this one?

### 02:10:57 · Speaker 5

share screen. Start broadcast.

### 02:11:04 · Speaker 5

Shall we resume?

### 02:11:06 · Speaker 0

Yes sir. Yes sir. Yes sir.

### 02:11:09 · Speaker 6

Now you can see my screen is paused, right?

### 02:11:09 · Speaker 4

Bowl

### 02:11:10 · Speaker 4

What's our own correction in the notes? That's a P theta it's missing instead of mentioning a P. It's before the objective for classifier training, right? That was.

### 02:11:14 · Speaker 6

Hello

### 02:11:16 · Speaker 6

being

### 02:11:23 · Speaker 6

come again? Where is this?

### 02:11:25 · Speaker 4

before the objective for certificate that likelihood that extra before that line

### 02:11:33 · Speaker 4

before that

### 02:11:34 · Speaker 0

Ah

### 02:11:35 · Speaker 4

Can you go above a little? Yeah, here it's mentioned comes from P you mentioned the P type P theta, right?

### 02:11:41 · Speaker 0

ஆ ஓகே ஓகே ஓகே

### 02:11:45 · Speaker 0

யா கரெக்ட் தேங்க்ஸ்

### 02:11:52 · Speaker 0

Okay, shall we continue?

### 02:11:56 · Speaker 0

So if we look at some of the

### 02:12:03 · Speaker 6

See there are after this Gyan thing came, you know, too many improvisations over it. A lot of papers, you know, a lot of applications and all that. So in the interest of time I'll only cover a few of it, a few of them.

### 02:12:19 · Speaker 6

I mean, uh, nevertheless, Gyan is now not the state of the art for, uh, like generative modeling, right? I mean, people have moved to diffusion models and so on. But anyway, so I will cover a few of them, uh, and rest you can read with this kind of a background. The first thing that we will do is what is called as the conditional Gyan.

### 02:12:39 · Speaker 5

Okay

### 02:12:49 · Speaker 0

conditional plan

### 02:12:50 · Speaker 5

Okay, what is the objective here? The data is

### 02:12:54 · Speaker 0

like this

### 02:12:55 · Speaker 5

So

### 02:12:56 · Speaker 0

So you have

### 02:13:00 · Speaker 0

samples like this you know x one comma y one

### 02:13:08 · Speaker 0

Next i2

### 02:13:12 · Speaker 0

and so on

### 02:13:13 · Speaker 6

सॉरी, स्मॉल लिटिल इसके अंदर एक्स

### 02:13:16 · Speaker 6

x n, y n, okay? So you have data this way where I'll tell you what this y is, okay? So this coming from let's say p x y some distribution. Now, the x example can be like this, you know, x can be let's say images, okay?

### 02:13:37 · Speaker 5

Now why can we class labels

### 02:13:44 · Speaker 5

can be glass labels or okay some textual embedding

### 02:13:48 · Speaker 5

six

### 02:13:51 · Speaker 6

we will actually make this idea a little more concrete when we go to text condition diffusion models and all that. But yeah, so for now let us say

### 02:13:59 · Speaker 5

that these are

### 02:14:05 · Speaker 5

textual embeddings

### 02:14:09 · Speaker 5

for

### 02:14:11 · Speaker 6

X

### 02:14:13 · Speaker 6

it's class labels for x, right? Or textual embeddings for x. If you have data like this, the objective is, objective is

### 02:14:25 · Speaker 0

to sample from, sample or generate, slash generate

### 02:14:32 · Speaker 0

from

### 02:14:34 · Speaker 0

the conditional distribution.

### 02:14:49 · Speaker 0

just P of

### 02:14:52 · Speaker 6

x given y. So this means that you know there is you need to get x given y equal to let's say some class.

### 02:15:00 · Speaker 6

or some text

### 02:15:03 · Speaker 6

Okay. So this is class conditional generation, right? Given a particular text or a prompt or a class label, you need to generate the corresponding image. How do you do this is the question. Okay. So,

### 02:15:23 · Speaker 0

we are doing. So now to do it is, the problem is now.

### 02:15:29 · Speaker 0

Model

### 02:15:32 · Speaker 0

model, okay?

### 02:15:36 · Speaker 5

p of x given y okay

### 02:15:39 · Speaker 5

Instead of

### 02:15:43 · Speaker 5

instead of P X, okay? using P theta. So now the thing is the setup is exactly the same. You have this

### 02:15:56 · Speaker 5

T theta

### 02:15:56 · Speaker 0

Okay

### 02:15:58 · Speaker 0

Viewers

### 02:16:02 · Speaker 0

found this um

### 02:16:08 · Speaker 0

X cap okay.

### 02:16:11 · Speaker 0

Now, this takes Z

### 02:16:23 · Speaker 0

she was some working offline

### 02:16:25 · Speaker 6

is my screen still visible?

### 02:16:29 · Speaker 0

Yes sir

### 02:16:30 · Speaker 4

Yes sir. Yes sir.

### 02:16:32 · Speaker 6

Okay. Now you need to generate from like P X given by right. So what you need to do first is that you condition this generator generation okay. Which Y.

### 02:16:33 · Speaker 12

It's okay.

### 02:16:44 · Speaker 6

Now how do you do that is that just add Y as another input here. So Y goes as another input to this.

### 02:16:54 · Speaker 6

Now what happens is that you need to

### 02:16:57 · Speaker 5

the P function

### 02:17:05 · Speaker 0

or the discriminator

### 02:17:13 · Speaker 0

Astu

### 02:17:16 · Speaker 0

classify between

### 02:17:22 · Speaker 0

samples of

### 02:17:26 · Speaker 0

P X Q 1 Y, okay? And

### 02:17:32 · Speaker 6

P X cap given wave forces depends on theta.

### 02:17:37 · Speaker 6

Okay. Now this is now sampled from P X cap given Y. So now how do you do that is that for the same T network that you have, the discriminant network.

### 02:17:52 · Speaker 0

E W of X, right? This network.

### 02:17:57 · Speaker 5

what you do is simply

### 02:18:04 · Speaker 5

you have this x or x cap that is going on as input anyway.

### 02:18:08 · Speaker 6

you know, you add additional y as input to this.

### 02:18:12 · Speaker 6

That's all. That's all it is. Now, everything else remains the same. So now the cost which is J theta comma W, right? Will be will look like this. So now expected value of log of

### 02:18:26 · Speaker 6

D W, okay, so this D W now takes X and Y both as input. The expectation is now with respect to X given Y sampled from P X given Y. Okay? Plus that other term which is expectation of one minus.

### 02:18:47 · Speaker 6

What was that term?

### 02:18:47 · Speaker 5

log of 1 minus right or

### 02:18:51 · Speaker 5

One minus

### 02:18:54 · Speaker 5

T W of X cap, comma

### 02:18:57 · Speaker 0

Okay

### 02:19:00 · Speaker 0

where

### 02:19:07 · Speaker 0

Yeah, I can actually say that x and y comes from this. Yeah.

### 02:19:12 · Speaker 5

x and y

### 02:19:13 · Speaker 6

coming from this and you have

### 02:19:16 · Speaker 6

x cap comma y coming from p x cap given by conditional theta.

### 02:19:24 · Speaker 6

It's all

### 02:19:27 · Speaker 6

So this is a

### 02:19:28 · Speaker 0

additional gap. Now, during inference, right, or inference post-training,

### 02:19:44 · Speaker 0

what you do is that

### 02:19:47 · Speaker 0

to take t theta

### 02:19:51 · Speaker 0

G theta star. Okay.

### 02:20:12 · Speaker 0

Now sample a Z from normal zero one, okay? And you give a a class label.

### 02:20:24 · Speaker 0

or text embedding as input.

### 02:20:31 · Speaker 0

which is your y. Okay? And generate x q one y equal to some class label.

### 02:20:42 · Speaker 0

or text study

### 02:20:49 · Speaker 0

That's all. Now this y, right, can be represented as a one-hot vector.

### 02:20:58 · Speaker 0

if it's a class.

### 02:21:01 · Speaker 0

Okay. Now it can be represented as some embedding vector.

### 02:21:11 · Speaker 0

If it's

### 02:21:12 · Speaker 6

Text

### 02:21:14 · Speaker 6

So basically there are these embedding vectors, you know, T F I D F or like, you know, some bird embedding or something. Don't worry about this. So basically you represent a text as some sort of a vector, right? We'll talk about all this bird embedding, how do you generate all this later in the course anyway. But yeah, so it's some vector that is representing a label. Just give that as an input to both the generator and the discriminator and solve the same optimization problem. And post training you just take that and give it as an input to the

### 02:21:44 · Speaker 6

train generator and this will do what is called as conditional generation. Let me just show you some examples of this.

### 02:21:51 · Speaker 0

But C क्या मतलब कंडीशनर क्या

### 02:22:12 · Speaker 5

See my screen

### 02:22:16 · Speaker 0

is

### 02:22:17 · Speaker 0

Yes sir

### 02:22:18 · Speaker 6

see this right? is exactly what I had written here. X given Y and you have like write it as Z given Y. I mean it's basically G generator network takes Z right? and given Y. That's what it means. So what happens in terms of network you have Z, you concatenate Y to that and give it as an input. And the discriminator you it takes both X and Y concatenated together. Okay? Now look at the results right? So this is for MNIST. So MNIST is a generated data. every row corresponds to one particular digit so they have conditioned it on the class labels

### 02:22:55 · Speaker 6

And yeah, so they have again conditioned it on uh text. This was a very old paper, a two thousand fifteen paper. So they are the fourteen paper, right? The embeddings were not, textual embeddings were not that great there. So this they have done class conditional generation for MS. And I think in your assignment I have also asked you to do a class conditional generation for the data set that I have given.

### 02:23:19 · Speaker 6

Okay, so that is about C Gyan. Okay, any questions on this?

### 02:23:26 · Speaker 6

Yeah, Sanchit, Sanchit, Talwar.

### 02:23:28 · Speaker 11

सर, या, सर, हेयर एक्स इज जस्ट लिमिटेड टू इमेजेस और इट कैन बी सम...

### 02:23:32 · Speaker 6

it can be it can be anything. See I've been telling this from class one right? Gyaans are not restricted to images. uh it can be like speech. People do text people have done text to speech using Gyaans no that is some of these models. So condition it on text and generate speech. So that can be done as well.

### 02:23:54 · Speaker 11

Okay, like, like, can you share the screen? Like we have the transformer algorithms, right? Like where we give a prompt of text and

### 02:23:55 · Speaker 10

Can you share the screen?

### 02:24:04 · Speaker 6

No no no that is not see that is not adversarily trained those are uh uh auto regressive models okay so G P T etcetera are auto regressive models we will talk about that as well.

### 02:24:04 · Speaker 11

like

### 02:24:17 · Speaker 6

later in the course we talk about. This is different from that. This is not, see this is adversarial learner. This is a GAN. This is not a auto regressive model. This is not a GPT.

### 02:24:18 · Speaker 11

This is different from that

### 02:24:29 · Speaker 0

Okay

### 02:24:30 · Speaker 6

So this is text conditional generation of images, right? I mean, it's a GAN that is trained which is which is minimizing the underlying F divergence.

### 02:24:42 · Speaker 6

set okay

### 02:24:42 · Speaker 5

ओके सर

### 02:24:47 · Speaker 6

Okay, another question by

### 02:24:52 · Speaker 6

Karthik Kumar

### 02:24:54 · Speaker 7

Yes sir. I just wanted to know about Y. While we training Y, is it like a range of values in the sense that we will give all the classes that it need to, for example, if it is class labels, we will give all the classes to which it need to train itself so that during inference, we will be giving one among that class. So why would what would be the range of Y? I mean like

### 02:25:21 · Speaker 7

How

### 02:25:22 · Speaker 6

I did not understand your question

### 02:25:25 · Speaker 0

Hello

### 02:25:26 · Speaker 7

So for example if we are training at the case of images right and we are giving a next prompt as you shown in the video like in the paper that okay find the mountains in it or something in that sense. That can be why right? Is my understanding there correct?

### 02:25:45 · Speaker 6

no, see why, okay, so for now let's say that it's class type.

### 02:25:51 · Speaker 7

Hmm

### 02:25:52 · Speaker 6

இது சிம்பிளி எ கிளாஸ் லேபல்

### 02:25:54 · Speaker 7

Okay, so it can be something like, is it a human or is it a animal?

### 02:25:58 · Speaker 6

Yeah, represent represent that as a one hot vector. So you know what one hot representation means, right?

### 02:26:04 · Speaker 7

Yeah

### 02:26:06 · Speaker 6

uh so if it's MNIST you have ten classes represent that as a ten dimensional like binary vector with one zeros right so whenever you get from the class one then you get you give like one like one zero zero zero zero concatenate that otherwise you get zero one zero zero zero concatenate that and so on.

### 02:26:29 · Speaker 6

Does it make sense?

### 02:26:29 · Speaker 5

makes sense? Got it. Yeah.

### 02:26:32 · Speaker 12

Yeah

### 02:26:32 · Speaker 5

Okay. Thanks.

### 02:26:35 · Speaker 6

Okay

### 02:26:37 · Speaker 6

Vivek

### 02:26:38 · Speaker 12

So one question. So, when we are

### 02:26:42 · Speaker 12

uh okay suppose this is something like uh BERT embedding could also have been some clip embedding or some such text embedding here. Yeah yeah. But my question is how do we how do we join this X

### 02:26:50 · Speaker 6

Yeah, yeah. I'm pretty clear. But my question

### 02:26:56 · Speaker 6

concatenate, concatenate. Make them like vectors. Just concatenate that with x and then give it as an input.

### 02:27:06 · Speaker 12

Okay, I'm sorry, that was the same question. Thank you, sir.

### 02:27:09 · Speaker 6

Yeah

### 02:27:11 · Speaker 6

So for the discriminator you are saying how do we concatenate that with x or something. Yeah yeah yeah. Just concatenate that. Yeah. Just concatenate that.

### 02:27:14 · Speaker 12

Yeah, yeah, yeah. It's just a connected

### 02:27:18 · Speaker 10

across

### 02:27:20 · Speaker 6

flat on that and concatenate all

### 02:27:20 · Speaker 10

flat on that and concatenate all

### 02:27:24 · Speaker 6

no attention see why is a vector why do you have attention or anything see why is a vector given a text it is a vector that corresponds to a text take that and concatenate with your x that's all what is the difficulty

### 02:27:38 · Speaker 12

ಓಕೆ

### 02:27:39 · Speaker 6

See, it's a vector, right? Given a text, you get a vector. All these words will give you a vector for its sentence, isn't it?

### 02:27:41 · Speaker 12

getup

### 02:27:46 · Speaker 12

Yes. So take that

### 02:27:47 · Speaker 6

So take that

### 02:27:49 · Speaker 12

But yeah, but it comes from a completely different vector space.

### 02:27:53 · Speaker 6

How does it matter? How does it matter? I just want pairs of images and vectors for my training. So look at this. No, what I am given is pairs of images and vectors.

### 02:27:55 · Speaker 12

Okay

### 02:28:03 · Speaker 6

Okay

### 02:28:03 · Speaker 5

So you're screening

### 02:28:03 · Speaker 0

So your screen is not visible

### 02:28:06 · Speaker 5

is that

### 02:28:13 · Speaker 5

Okay, so basically I have pairs of images

### 02:28:16 · Speaker 5

and vectors, right? And those vectors can be anything, they can come from like some embedding or it can be

### 02:28:22 · Speaker 6

one hot vector for class labels it can be anything

### 02:28:27 · Speaker 0

ஓகே

### 02:28:35 · Speaker 0

Okay, so she

### 02:28:36 · Speaker 5

Okay

### 02:28:36 · Speaker 0

Okay

### 02:28:38 · Speaker 3

Sir, when we concatenate, do we have the same dimension size for text embedding and the image in

### 02:28:45 · Speaker 6

Not no definitely not. See then how would you see concatenation can be done in many ways no. See you you add one more channel for your image right and just repeat all this so many times.

### 02:28:59 · Speaker 12

okay this is just a discriminator network we are not generating anything here so maybe concatenation is sufficient to do that

### 02:29:08 · Speaker 6

Correct. We are not generating Y, we are not generating embeddings, we are just using embeddings to generate from X conditionally.

### 02:29:18 · Speaker 5

Okay

### 02:29:18 · Speaker 6

given a text or given a one hot vector we need we want to generate from it. We are not generating embeddings here.

### 02:29:25 · Speaker 6

There is no attention, retention, nothing. I mean it's simply taking a vector corresponding to a text. You don't even have to do but. Okay, sorry, maybe I wrote this and you got confused. See, embedding can come from anything, no? Let's say that it is simply a

### 02:29:42 · Speaker 6

Take TFIDF okay

### 02:29:47 · Speaker 6

You understood, right? I mean, it is some vector corresponding to this vector, this thing, you concatenate that. You have a pair of data or image and vector. You concatenate that vector with this and then try the C-GAN. Nothing complicated at all.

### 02:29:51 · Speaker 5

Okay

### 02:29:52 · Speaker 3

concrete

### 02:30:03 · Speaker 3

Okay

### 02:30:06 · Speaker 6

But sir, what is

### 02:30:06 · Speaker 8

What's the what is the difference between the Seagan and normal GaNs that we use?

### 02:30:13 · Speaker 6

Nothing, the the Gyan cannot do conditional generation, conditional Gyan can do conditional generation. See in a normal Gyan, right? Suppose you build a normal Gyan on MNIST, you can't control what digit you generate when you do inference. Here you can control what digit you generate during inference.

### 02:30:32 · Speaker 0

Okay

### 02:30:39 · Speaker 0

Yeah, okay, sir.

### 02:30:40 · Speaker 5

is it all right?

### 02:30:41 · Speaker 0

Yeah yeah thank you sir

### 02:30:46 · Speaker 6

In fact, in the data set that I have given you, there are some ninety classes, different animal faces, okay? So now I've asked you to build a C-GAN on say twenty class, there's some ten or twenty subclass of the this data set. So what you will see is that when you give that particular, the way you should do it, to take those ten classes, represent them as one-horned vectors like this, zero zero zero one wherever the class is, concatenate this with the Z vector.

### 02:31:16 · Speaker 6

okay? and give that as an input to your generator and also the discriminator. During inference when you concatenate, this is like a switch. So whatever class you want, you take that particular class and it will generate. And you understand that?

### 02:31:32 · Speaker 12

Yes, it is the headache of the back propagation to find out what uh in how in which ways these vectors have to be combined and uh the image has to be generated.

### 02:31:45 · Speaker 3

யா

### 02:31:45 · Speaker 6

See, don't say it that way. See, the thing is remember what we are doing. We are trying to minimize the distributional divergence. See, if we do it well, then the distribute divergence between P X given Y and P of P P X cap given Y and P X given Y will be minimized, you know. What do you mean by that? I mean that is why I spent two full classes on trying to make you appreciate what does it mean to minimize distributions.

### 02:32:14 · Speaker 6

No, no, no, no.

### 02:32:14 · Speaker 12

No no, the reason why we concatenate is what I was talking about. So the the the if we concatenate also or maybe if we do something some complicated thing like some cross attention or some such neural formal neural network.

### 02:32:27 · Speaker 6

just add if you want if you want you can add no problem

### 02:32:30 · Speaker 12

Yeah, okay. So, okay.

### 02:32:31 · Speaker 6

combine them any way you want, any way you want.

### 02:32:35 · Speaker 12

ओके ओके या

### 02:32:39 · Speaker 0

Yes

### 02:32:42 · Speaker 5

Okay, shall we move on?

### 02:32:44 · Speaker 0

is

### 02:32:46 · Speaker 5

Okay, so we'll go to like, yeah, one other application of this.

### 02:32:51 · Speaker 0

So next thing that we will do is

### 02:33:20 · Speaker 0

So we already saw right

### 02:33:21 · Speaker 6

that we can do conditional generation and one other advantage of doing conditional generation is that suppose you are solving a classification problem okay and you have less less data what you can do is you can build a GAN a conditional GAN okay and generate class specific data using conditional GANs and use that for augmenting your classifiers

### 02:33:46 · Speaker 6

You understand?

### 02:33:47 · Speaker 6

So if you can do a class conditional generation, then you can use that to like augment your uh classifier for your downstream task. Does that make sense?

### 02:34:02 · Speaker 8

सर, प्लीज़ रिपीट अगेन।

### 02:34:06 · Speaker 6

Uh see uh suppose you have a classifier okay and you want to train a classifier and you don't have data from one of the classes what you do is you build a GAN on that on that data okay the conditional GAN and generate more data from that conditional GAN so if you do it in an unconditional way what happens is you will not know what the label of the generated data is if you build a conditional GAN you already know what label the data is coming from right and you can use to augment your classifier and retrain your classifier with more data.

### 02:34:41 · Speaker 8

Yeah, correct sir, correct.

### 02:34:42 · Speaker 6

Aditya

### 02:34:45 · Speaker 9

Sir, wouldn't so but the the GAN generated images wouldn't it basically already be able to so the second half of the GAN anyway can

### 02:34:57 · Speaker 9

So wouldn't it like my doubt was the data set the amount of information we have in the images we are just creating instances of that right so the classifier should be able to learn the same amount from the No no no

### 02:35:08 · Speaker 6

No

### 02:35:10 · Speaker 6

No, no, no, you will generate new data, right? It's like augmenting your data. Suppose you have more data in your data set, the classifier would anyway become better.

### 02:35:21 · Speaker 2

Okay

### 02:35:23 · Speaker 6

Right? I mean again this is under the assumption that you have you have trained your Gyan well so that the underlying distribution is correctly estimated. If it's not estimated then what you're saying is true. I mean then classifier will only see some noise. But if the underlying distribution has been correctly estimated via Gyan training, good Gyan training. Not only Gyan, you can use it for any kind of classifier, I mean any kind of generative model, right? Take a generative model, train it well and you can use that data. Of course you need to do it in a conditional way. Use data augment your classifier, always do that.

### 02:35:56 · Speaker 9

Okay, so my my my doubt was if we had sufficient images in order to actually I mean generate the actual distribution required of that images, then wouldn't that be sufficient to directly give a good classifier because we have enough to even estimate.

### 02:36:14 · Speaker 6

not not not necessarily, not necessarily, but your question is valid. What you're saying is if we can anyway estimate the underlying distribution, would classifier would anyway do that, no? Not necessarily. Sometimes, sometimes what you're saying is true in a sense. But sometimes, you know, what happens is, you know, you are let's say that your classifier is restrictive in the sense that you can't make your classifier large enough, right? In that case, even if you have a lot of data because of restrictions on the architecture of the classifier, unless you have like

### 02:36:24 · Speaker 3

sometimes

### 02:36:44 · Speaker 6

more diverse data you can't try the classifier well.

### 02:36:47 · Speaker 9

Okay, okay.

### 02:36:49 · Speaker 6

So in those cases you can or the other thing, other thing that you can do is let's say that you have class imbalance, right? Then to sample from the tail of the distribution you can use conditional gaps and then augment your classifier.

### 02:36:49 · Speaker 9

Okay

### 02:37:01 · Speaker 9

Understood. Okay, sir.

### 02:37:02 · Speaker 6

Hello

### 02:37:04 · Speaker 6

That's a good question by the way. Yeah. Sachin.

### 02:37:08 · Speaker 10

Hi sir. So, uh the original data must have a must have some data from a class, right? The generator cannot

### 02:37:14 · Speaker 6

generator cannot Of course, of course, of course, of course, of course. Otherwise you can't do a conditional generation, right? Yeah, it should have some data from all classes, yeah, or rather the class that you would want to sample from.

### 02:37:18 · Speaker 10

Right

### 02:37:20 · Speaker 10

some data

### 02:37:26 · Speaker 0

Okay

### 02:37:27 · Speaker 6

Okay, so let's move on. So I'll talk about, you know, two applications of GANs and then we will, uh like move to the next topic in the next class. The first thing that I want to talk about is what is called as like image to image

### 02:37:40 · Speaker 0

Translation Okay

### 02:37:58 · Speaker 0

Image to Image Translate

### 02:37:59 · Speaker 5

Okay, what is the thing here is, the objective here is, let's say that we have two data sets.

### 02:38:12 · Speaker 5

X one through X N given by let's say P X

### 02:38:20 · Speaker 5

and there is Y is not

### 02:38:25 · Speaker 0

What do we call it?

### 02:38:27 · Speaker 0

set is also taken. Okay, let me change the notation.

### 02:38:37 · Speaker 0

S one, S two

### 02:38:38 · Speaker 5

two

### 02:38:39 · Speaker 5

to send some data that is coming from some distribution P S. And you have like

### 02:38:49 · Speaker 5

T one, T two, T N that is coming from T T.

### 02:38:56 · Speaker 5

Okay? So the objective is that

### 02:39:05 · Speaker 0

Just a second, Anna.

### 02:39:21 · Speaker 0

show some examples so that you appreciate it better. Just opening that paper.

### 02:39:33 · Speaker 0

Now the objective, objective

### 02:39:38 · Speaker 0

Easton

### 02:39:39 · Speaker 5

Okay, Translate

### 02:39:43 · Speaker 5

what that means. Translate from translate from

### 02:39:50 · Speaker 5

PS to PT

### 02:39:54 · Speaker 5

Okay, what does that mean? Simply show you an example then you will understand that easily.

### 02:40:04 · Speaker 5

Do you see my screen?

### 02:40:09 · Speaker 0

Yes sir

### 02:40:10 · Speaker 6

Yeah, this is what it is, right? So I suppose I want to do a style transfer. Meaning that I have some style image and I want to convert it to some other style. And I mean this is another example, right? If I have zebra images, I want to convert them into horses. If I have this, you know, these are different styles, you know, photograph to Monet to Van Gogh paintings, etcetera. You have winter images you want to convert into summer. There are more examples. You have, let's say that you have sketches, you want to convert that into the full images.

### 02:40:40 · Speaker 6

other examples that are given. Yeah. This is like you have uh you have maps or rather satellite images you want to convert it into map and and and the other way around. You have the segmentation maps. You want to convert that into full images and so on. Okay? So this is what I mean by translation. So basically in my notation you have been given data from two different distributions PS and PT. The objective is to convert from one distribution to the other.

### 02:41:09 · Speaker 6

Hmm

### 02:41:10 · Speaker 5

Did you understand the objective? Is it clear?

### 02:41:16 · Speaker 0

Yes sir, it's true.

### 02:41:18 · Speaker 5

Okay. Now how do we do that? Is that so recall

### 02:41:21 · Speaker 6

Hello

### 02:41:24 · Speaker 6

recall that again, right? So what does it do? It will it will take an arbitrary random variable and project it to random variable of interest. So this is arbitrary, right?

### 02:41:41 · Speaker 5

This is data of interest.

### 02:41:47 · Speaker 5

So there is no other no reason why is he to be arbitrary, right? So what you

### 02:41:52 · Speaker 6

you can do is. you can build a

### 02:41:55 · Speaker 6

ज्ञान ओके

### 02:41:57 · Speaker 6

to take data from the source distribution

### 02:42:01 · Speaker 6

S coming from PS

### 02:42:04 · Speaker 6

And now this converts it into the T coming from P T. So let's call that T cap coming from P T cap.

### 02:42:13 · Speaker 6

Now have a distribution. So what you are trying to do is you are trying to start from the the source distribution, okay? And generate the target distribution. Does it make sense? You can do that, right? So basically you can start from any random variable and go to any random variable as long as this f divergence, okay? That you minimize the divergence between the true target distribution and the generated target distribution.

### 02:42:39 · Speaker 6

Oh yeah, this Gyan. This you can do. Of course, there will be a discriminator here, right? Because it's a Gyan that we are talking about. There is a discriminator. Okay?

### 02:42:50 · Speaker 6

that to take the generated image, T cap or the real image from the target distribution T and gives you a number between zero and one. Now but this will so this entire thing right?

### 02:43:02 · Speaker 5

Well

### 02:43:05 · Speaker 5

convert

### 02:43:11 · Speaker 5

P S, right, to P T. Agree? So here, right, what is this doing? This is

### 02:43:18 · Speaker 5

Convert

### 02:43:20 · Speaker 5

P Z 2

### 02:43:24 · Speaker 5

P X. Similarly, this is converting P S to P T. Do you understand this?

### 02:43:33 · Speaker 12

Yes, in that case, G theta of S will look like auto encoder, right?

### 02:43:39 · Speaker 6

No, no, no, there is auto encoder here. I mean, simply take

### 02:43:41 · Speaker 12

I mean, in the sense like

### 02:43:43 · Speaker 6

there is nothing. No no no no no no. There is no auto encoding nothing is happening right? Simply again instead of taking Z it will take S as input and it will give you T cap as output that's all.

### 02:43:43 · Speaker 12

there will be a

### 02:43:56 · Speaker 12

Okay, so

### 02:43:56 · Speaker 6

Why is there an auto encoder here?

### 02:43:59 · Speaker 12

so will there be a need to have a equal sized image? I mean so initially we sampled Z and we got G theta of Z.

### 02:44:09 · Speaker 6

That's a different question. That's a different question. So what should be the architecture of this? Architecturally changes of course. You start with an equal sized input. Yeah.

### 02:44:21 · Speaker 6

But there is no auto encoding, only the size of this network changes, that I agree.

### 02:44:21 · Speaker 12

is

### 02:44:25 · Speaker 5

ओके

### 02:44:28 · Speaker 6

Okay

### 02:44:29 · Speaker 5

Yes

### 02:44:31 · Speaker 6

Yeah, any other questions on this?

### 02:44:34 · Speaker 8

And sir, one more thing. Sir, how we can identify or calculate the performance of this GANs, like how it's performing well on the data?

### 02:44:45 · Speaker 6

this question does not fit into what we are discussing right now. It is a good question but it is not I'm talking about this image to image translation right like not talked about evaluating as yet. So I request all of you to like ask questions that are relevant to what is being discussed right now okay. But I'll answer that question how do we evaluate I actually hinted that in the previous session I told you that there are metrics called F I D etcetera which I will describe but yeah.

### 02:45:15 · Speaker 6

Any question that is like relevant to what we are discussing right now, please raise your hands before you ask any questions, please. Yeah, Harish.

### 02:45:23 · Speaker 2

So while sampling this distribution, the samples from P S from the distribution S here. So we really don't know the distribution, right, underlying distribution in this case.

### 02:45:29 · Speaker 6

ம்

### 02:45:33 · Speaker 6

We don't know, it's just like Z, yeah. We don't know, we neither know P S nor we know P T. We just have samples from it.

### 02:45:35 · Speaker 2

I don't

### 02:45:41 · Speaker 2

So what are we given a data

### 02:45:41 · Speaker 6

So what have we given a data

### 02:45:43 · Speaker 2

Okay. So how do we convert that to like for example, in the general one the Z is of the form of like sixteen or thirty two point. That I already told you.

### 02:45:54 · Speaker 6

that I already told you, right? You start with it's a it's a C N N. So it's basically a C N N, right? Of the same size. If you want, I can write it this way.

### 02:46:04 · Speaker 6

It's of the same size.

### 02:46:09 · Speaker 6

is okay, the input and the output, I mean the intermediate layers can be anything, but you can actually make it a unit if you want to, okay, just let it be.

### 02:46:22 · Speaker 6

It's an architecture choice. What you can do is start from PS, okay, and reduce the dimensionality and just increase the dimensionality again.

### 02:46:31 · Speaker 6

and then get your P. This is from P S. This is your G theta of S.

### 02:46:38 · Speaker 6

It's it's an architectural choice. You can do it anyway. So you can reduce the dimension and increase the dimension again to get to T. And T and S have same dimensions. Is that all right?

### 02:46:49 · Speaker 6

Okay. Sushil?

### 02:46:51 · Speaker 3

uh sir, to the discriminator, you have T cap or T, it should be and if there any specific reason you inviting or

### 02:47:00 · Speaker 6

I mean like by R I mean see when you are looking at the first term you need to give T when you are looking at the second term you need to give T T cap.

### 02:47:10 · Speaker 3

Okay

### 02:47:11 · Speaker 6

Right? That is how we have been doing that, no? Discriminant. Either it T cap goes as input or T goes as input depending upon what term you are evaluating.

### 02:47:23 · Speaker 5

Okay? Yeah, Sarvesh.

### 02:47:28 · Speaker 11

Yes sir, for this image to image translation, so shouldn't there be a need of a mapping from which S is mapped to which T or like...

### 02:47:36 · Speaker 6

good question. good question. good question. Yeah, see there was a paper called pics to pics that actually pair, I mean this is called pairing. So now how do you, I mean the question that you are asking basically is that how do you ensure that one corresponding S goes to that same T, right? I mean the example that I showed, how does the semantic semantics preserve get preserved? That's a very good question. That is why you know, in the in the first paper called pics to pics.

### 02:47:57 · Speaker 1

Hello

### 02:48:06 · Speaker 6

okay? It's called pics to pics. Here there was pairing.

### 02:48:11 · Speaker 6

Okay. So pairing was there and pairing was an issue because when you get the data, you would you wouldn't get pairing. There was another paper that came which was called Cycle Gyan where there was no pairing. Okay, what they do is...

### 02:48:27 · Speaker 6

they do this trick called what they do na

### 02:48:30 · Speaker 5

If you want to convert from S to T, okay? So they have a GAN, okay?

### 02:48:36 · Speaker 5

from S to T

### 02:48:41 · Speaker 0

then they also have another gang from T to S.

### 02:48:49 · Speaker 0

Okay

### 02:48:50 · Speaker 0

Now what they do is in addition to

### 02:48:57 · Speaker 0

in addition to two GAN losses.

### 02:49:06 · Speaker 5

cycle yarn also has

### 02:49:12 · Speaker 0

Style Loss

### 02:49:13 · Speaker 5

No, no, no. As what is called as a cycle consistency loss.

### 02:49:24 · Speaker 5

cycle consistency loss. Now what do you mean by

### 02:49:26 · Speaker 6

cycle consistency loss. What they do is, so for gang from S to T, so you have this no? You have expectation of log of uh D S uh image that you get is from T and you have T coming from PT plus that expectation of log of

### 02:49:49 · Speaker 6

one minus T S. T cap. T cap coming from that generator no? P T cap theta okay. In addition to this they will have another loss okay. That would say that

### 02:50:07 · Speaker 5

the

### 02:50:12 · Speaker 5

if you take the uh

### 02:50:18 · Speaker 5

actually yeah. So there is another

### 02:50:21 · Speaker 6

Gyan here, right, which is similar to this. Expectation of log of D T on S.

### 02:50:29 · Speaker 6

S coming from P S. So they do are the other direction, they do translation in other direction also they have this and S cap coming from P S cap, let's call this P, right? So what they do is they'll say that if I take, I will write that maybe. So there are two generators here. So generator one is taking S and giving T, let's call this G one. There is another generator.

### 02:50:57 · Speaker 6

Of course there are two discriminators also. This is taking T. Okay? And it is giving you S. Now what they say is that if I take an image, okay? uh that has been

### 02:51:12 · Speaker 6

generated, okay, if I take G one, okay, and pass a T.

### 02:51:18 · Speaker 6

through it, sorry, G one takes S, you know, if I take an S and pass through it,

### 02:51:23 · Speaker 6

What should I get?

### 02:51:25 · Speaker 6

I'll get an image in T, correct? Now I will take this image T and pass it through G two.

### 02:51:29 · Speaker 0

Yes

### 02:51:34 · Speaker 6

What should I get?

### 02:51:37 · Speaker 0

against the same image. S prime. S prime.

### 02:51:38 · Speaker 5

again the same image. S prime.

### 02:51:39 · Speaker 6

explain. I get I get S, right? I should get S. So I minimize this loss.

### 02:51:45 · Speaker 6

This is called cycle consistency law. Similarly they do this. They take G one, okay? And G two pass it pass through a T you will get an S. You pass it through T you will get another T. So take that corresponding T and

### 02:52:00 · Speaker 6

this is what is a cycle gap.

### 02:52:06 · Speaker 6

the claim that if you do this

### 02:52:08 · Speaker 0

in addition to trying to glance then the pairing will happen. Let me just show you that.

### 02:52:26 · Speaker 0

Is my screen visible?

### 02:52:30 · Speaker 0

Yes sir

### 02:52:31 · Speaker 6

Yeah, you see that, right? There are

### 02:52:34 · Speaker 6

three objectives here, right? One is one is the two GAN objectives, of course. And there's the cycle consistency objective. What is cycle consistency objective here? So they they call this T and S as X and Y by the way. So and two generators as G and M. So when X goes through G, you get an image from Y and then you have to go make it pass through the other generator and match that with X one, X the input image and you do this for the other generator and add that as another loss.

### 02:53:04 · Speaker 6

right? This is what they get, no? Input, output of the generator and the reconstruction that is happening. So you have to ensure that this also happens and they show that if you do this, then the the I mean you can use this for image to image translation.

### 02:53:21 · Speaker 6

Okay, so that's about the cycle here. Let me

### 02:53:22 · Speaker 5

cycle

### 02:53:25 · Speaker 6

share that.

### 02:53:32 · Speaker 6

See as I said no there are so many applications that Gyan sir have been used for and you know I can teach a full course on Gyan. But yeah so we don't have that time unfortunately. Yeah questions are Vivek.

### 02:53:45 · Speaker 12

so I'm sorry but I did not understand the pairing that the question that was asked. I mean like

### 02:53:49 · Speaker 6

There is no pairing. What's the question that was asked? I mean like... There is no pairing. See, the question was, while while doing this, do you need the corresponding S and Y? See, in the example that I showed, uh if you if you take a sketch and you want the corresponding field image, no, while training this Gant, do you need the pairing is the question.

### 02:54:11 · Speaker 12

we should write we need

### 02:54:11 · Speaker 6

in India

### 02:54:13 · Speaker 6

No, we don't. That is what I'm saying. In pics to pics paper, pairing was needed. But in cycle GAN, pairing was taken, I mean they they gave up pairing. They said pairing is not needed. Then how do you ensure that the corresponding image gets generated is through having these two different generators. Even though you want S to be converted to T, you also have another GAN that is T from S and then you have the cycle consistency rule.

### 02:54:37 · Speaker 12

and then you have the cycle system.

### 02:54:39 · Speaker 12

convert it back and then the difference between them should be minimal. Okay. Yes. Okay. Okay.

### 02:54:41 · Speaker 6

difference between them should be

### 02:54:44 · Speaker 6

Yes

### 02:54:47 · Speaker 6

Okay. Sanjit?

### 02:54:50 · Speaker 11

Sir so in cycle GAN we we eventually come up with uh two GANs which uh you know help us to translate from S to T and the other one from T to S.

### 02:54:57 · Speaker 6

Batch

### 02:55:03 · Speaker 6

Correct

### 02:55:05 · Speaker 6

Okay

### 02:55:07 · Speaker 6

What's your question? You're just clarifying, right?

### 02:55:11 · Speaker 11

Yes sir. So I thought that the other GAN was just for, you know, learning up the first one.

### 02:55:12 · Speaker 6

Okay

### 02:55:17 · Speaker 11

Uh

### 02:55:17 · Speaker 6

you can say it that way, right? It is aiding the learning of first one, but it also gives you one additional advantage that you can have conversion back also, no, T to S as well.

### 02:55:28 · Speaker 5

Okay

### 02:55:30 · Speaker 6

Right?

### 02:55:31 · Speaker 5

ओके सर

### 02:55:32 · Speaker 6

Yeah. Yeah, Sachin.

### 02:55:36 · Speaker 10

सर, सो व्हेन पेयरिंग इज़ गिवन, इट्स मोर लाइक कंडीशनल गैन।

### 02:55:40 · Speaker 6

it becomes like a conditional gap. That's a good observation. Yes, it becomes like a conditional gap. Correct.

### 02:55:41 · Speaker 10

condition

### 02:55:46 · Speaker 10

Hmm

### 02:55:47 · Speaker 6

That's a good observation. Instead of having uh like a text as a one hot vector or as a conditioning variable, you have this image as a conditional variable. That's a good observation, yes. In fact, you can see this, right? You can use GAN for in painting now, image in painting. Because you can use the input image or the or the like masked image as input and you can train a GAN to complete the image. See, you can imagine any any of the applications now because what is GAN doing at the end of the day?

### 02:56:17 · Speaker 6

That is why you need to have that abstraction that's taking starting from arbitrary distribution it converts it into distribution of interest and it does that via minimizing the f divergence. Now you take your input to be anything that you want and output to be anything that you want and imagine whatever application you want there right.

### 02:56:36 · Speaker 10

Correct

### 02:56:38 · Speaker 6

Yeah

### 02:56:38 · Speaker 10

So sir in basically these like mobile phones and everything we see many photo editing tools like which convert the image or enhances the image.

### 02:56:47 · Speaker 6

Yeah. They can be GaNs. Yeah. They can be GaNs but right now the state of the art is not GaN. They use diffusion models as generating models. But the fundamental idea is the same. They use diffusion models because they are more easy to train and you know robust. We will come to diffusion models later in this course. Okay?

### 02:56:47 · Speaker 10

in can be dance

### 02:56:49 · Speaker 10

Okay

### 02:57:07 · Speaker 10

Thank you

### 02:57:07 · Speaker 6

Okay, yeah. Ankush,

### 02:57:11 · Speaker 1

Uh so uh when we say that S is translated to G uh by passing to G one it gives you T and in the G two when we are passing T so my question is when when we are passing through this there will be like coefficient added by G one right? Will it will be uh converted

### 02:57:29 · Speaker 6

What do you mean by coefficient added by achieving height of? What do you mean by that?

### 02:57:35 · Speaker 1

Okay, so when you say that we can we find a loss function by passing it to G one S minus S, right? And that gives you the value of it, right? What is the loss function happening?

### 02:57:48 · Speaker 6

not loss function. Yaar G one of S is simply an image.

### 02:57:52 · Speaker 1

Okay

### 02:57:53 · Speaker 6

G two of G two of G one of S is another image. So just looking at the differences of the images.

### 02:58:00 · Speaker 6

See, GEM is a generator, no?

### 02:58:00 · Speaker 1

Yeah, but

### 02:58:02 · Speaker 1

हा जनरेटर। सो द इमेज इज सेम व्हिच इज पास्ड लाइक एस इज सेम एंड व्हाटएवर वी आर गेटिंग आउटपुट ऑफ

### 02:58:07 · Speaker 6

whatever we are getting. Hold on. Hold on, hold on. Please hold on. Yeah. I'll tell you what is happening. Take an image S, pass it through G one, you get another image T, right? Correct. Take that T and pass it through G two, you will get some other image S.

### 02:58:11 · Speaker 1

Yeah

### 02:58:18 · Speaker 1

Correct

### 02:58:24 · Speaker 6

that team may be I should

### 02:58:27 · Speaker 1

Okay, that's not the original state, right?

### 02:58:29 · Speaker 6

Why is it the original image? Why is it the original image? It is output of the generator. It is something. Right, that's it. You you are matching that to the original image. Yeah.

### 02:58:34 · Speaker 1

Right, that's You you are matching that to the original image. Yeah. Okay, that's what I was confused. I thought you were telling like we are reversing the process and finding out the loss function after that. Like it's simply impossible.

### 02:58:44 · Speaker 6

Hello

### 02:58:44 · Speaker 6

it's simply passing. No, you understood what I'm saying, right? So it's, yeah, it's more. Okay, so it's a different image. It's not the because it is the generator, right? You have actually another one discriminator here.

### 02:58:50 · Speaker 1

ओके सो नेक्स्ट

### 02:58:54 · Speaker 5

Yeah, yeah, another description.

### 02:58:58 · Speaker 6

P W S. So there will be another discriminator here.

### 02:59:06 · Speaker 6

Is it E W T? Yes, go on, Mukesh.

### 02:59:09 · Speaker 8

Sir, when we are talking about the differences between these two images like G two T and G one S.

### 02:59:14 · Speaker 6

pixel level differences, pixel level differences.

### 02:59:17 · Speaker 8

Oh, it's a pixel level. Yes, sir. Okay. Correct. Thank you, sir.

### 02:59:18 · Speaker 6

Yes, okay.

### 02:59:21 · Speaker 6

Yeah

### 02:59:23 · Speaker 6

Thank you sir

### 02:59:23 · Speaker 3

Thank you sir, I got it.

### 02:59:25 · Speaker 2

So one question. So from this we can see that any arbitrary distribution can be converted by by training to one more other distribution, right? To make it close to the one. Correct. Correct. But is there are there any cases where we cannot do that? Like for example, there are two distributions which we cannot train again to for them to convert to one more distribution.

### 02:59:34 · Speaker 12

Correct Correct Correct

### 02:59:47 · Speaker 6

theoretically no. You can convert anything to anything theoretically.

### 02:59:52 · Speaker 6

Yeah, practically what happens is if you do not have like strong preference on data, for instance if you have let's say data like

### 03:00:00 · Speaker 2

tabular data or data like you know where you have compositional data and all that now it's difficult to try and get. But theoretically speaking you can do it anything is possible.

### 03:00:12 · Speaker 1

Thank you

### 03:00:16 · Speaker 2

Okay, I think all these questions

### 03:00:19 · Speaker 2

Yeah, it's okay, I'm not discrediting that, but yes, the time is twelve ten now. See, there is one other thing that I wanted to do, which is like

### 03:00:28 · Speaker 1

main

### 03:00:30 · Speaker 1

adversarial networks.

### 03:00:38 · Speaker 1

just

### 03:00:43 · Speaker 1

way to solve domain solve the problem of domain adaptation.

### 03:01:00 · Speaker 2

Okay

### 03:01:00 · Speaker 1

Vaya Gans

### 03:01:03 · Speaker 1

So

### 03:01:03 · Speaker 2

Oil

### 03:01:03 · Speaker 1

I want

### 03:01:03 · Speaker 2

wanted to do that it'll take fifteen minutes. People like complain if I extend. Shall I'll do that in the next class, okay? I wanted to finish this and go to variation of auto encoders in the next class. But anyway, so it'll take me fifteen minutes, I'll do it in the next class then, okay?

### 03:01:22 · Speaker 2

Okay that's all for today. So we'll have the we'll have the quiz next next class. uh starting at nine. After the quiz we will look at the domain adaptation with Gyaans and then we'll move to V A E's okay.

### 03:01:23 · Speaker 1

Thank you

### 03:01:37 · Speaker 1

Yeah, thanks.

### 03:01:37 · Speaker 2

Please see I what I recommend you is that now that we have come to the thick of the things, please start reading the papers that we have discussed in the class in the original and if you have questions you can either contact me or T S and get your doubts cleared.

### 03:01:54 · Speaker 2

ओके

### 03:01:56 · Speaker 2

See you then. See if I like you know while asking questions you know I'm just trying to moderate it a little so that there is relevance so don't get me wrong. So yeah questions are always encouraged. Okay see you next week then. Bye bye.

### 03:02:11 · Speaker 0

Thank you sir. Thank you sir.

### 03:02:14 · Speaker 1

and

### 03:02:14 · Speaker 1

Thank you sir. Thank you sir. Thank you sir.

### 03:02:14 · Speaker 2

Thank you sir. Thank you sir. Thank you sir.

### 03:02:17 · Speaker 0

Thank you sir

### 03:02:17 · Speaker 2

Thank you so much

### 03:02:17 · Speaker 1

Correct

### 03:02:18 · Speaker 2

Bye

### 03:02:20 · Speaker 0

Thank you, sir.
