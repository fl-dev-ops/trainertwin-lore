---
id: 5FxZkHrGgJQ
title: Lec 7 - Deep Generative Models GAN variants and Applications
url: https://www.youtube.com/watch?v=5FxZkHrGgJQ
date: '2024-11-23'
duration: 03:06:37
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 7 - Deep Generative Models GAN variants and Applications

## Transcript

### 00:00:02 · Speaker 1

we begin the class today so i was waiting for some people to join see i i uh i hope that uh like the people who have joined today uh i see as 79 people so uh none of you are planning to drop the course right because the window for dropping the course is uh is going to close by tomorrow i think tomorrow day after tomorrow right

### 00:00:32 · Speaker 2

Yes that's right

### 00:00:35 · Speaker 1

Okay, so is anybody still considering dropping the course? So I'll tell you why I'm asking, but yeah, is there anybody, I think you have gotten enough flavor of how the course is going to be and all that, right? So is there anything, any concern that, or rather information that you might want to know to take that decision?

### 00:00:56 · Speaker 1

Because initially we started with some hundred people, now we have about 85, I think, you know, some 15 people have dropped, which is okay, fair. Uh, anybody else considering dropping the course?

### 00:01:13 · Speaker 2

Considering to drop

### 00:01:15 · Speaker 3

because of personal reasons

### 00:01:19 · Speaker 1

Okay, no problem. Yeah, but you still want to continue attending the classes. Yeah, so that is one thing that I wanted to ask you. So once you drop the course, would these ICANN people allow you to continue attend classes? Or would they just remove you from all groups?

### 00:01:35 · Speaker 4

Audit isn't allowed for us

### 00:01:37 · Speaker 1

audit isn't allowed okay i see okay so except for uh mr billa right anybody else considering dropping the post

### 00:01:51 · Speaker 1

Okay, I take that as a no. Okay, so this, I think then this is the final class trend that we have. So I need this because we need to plan the assignments right now. We can form the groups of three and also plan the exam. So the exam, the midterm exam, I'm planning to have it after two classes, which is today there is one class where I'll finish this GAN thing and the next

### 00:02:21 · Speaker 1

class we will look at the variational autoencoders we'll start with vae's after that we'll have the bitum exam so that would be i will tell you

### 00:02:33 · Speaker 1

okay it's 20 for 25th uh yeah 12th is the hell right so we can have it on 10th of uh october if it's okay for you it's a thursday

### 00:02:45 · Speaker 1

Uh we'll have it on 10th

### 00:02:51 · Speaker 1

Does it work for all of you 10th of October?

### 00:02:54 · Speaker 4

Okay

### 00:02:58 · Speaker 1

Yeah, timing we have to see, something that works for all of you. Maybe 8.30 to 9.30, 8.30 to 10 in the night.

### 00:03:09 · Speaker 4

I'm sure it doesn't final date for submitting the first assignment right so normally we may send till the day so we may not have the time to prepare on then

### 00:03:09 · Speaker 2

So it doesn't

### 00:03:22 · Speaker 4

Okay

### 00:03:24 · Speaker 1

Oh oh I see

### 00:03:28 · Speaker 2

And then one more thing, not sure, Thursday at this moment, maybe, but it is office days for most of us and many of us have actually the US client. I mean, not me, but many of my friends I can see in this class. So I don't know whether it will be a right time to take an exam for them. Can we plan it on Sunday instead?

### 00:03:52 · Speaker 1

Sunday is also okay uh so which means that we'll have to do it on 13th

### 00:03:59 · Speaker 1

So dwell this uh like Tahirah

### 00:04:05 · Speaker 1

13th we should do 13th October is okay with all of you? anybody has a problem with 13th October?

### 00:04:15 · Speaker 1

13th is fine, huh? Yes sir. So maybe what I'll do, no, I will write it.

### 00:04:22 · Speaker 1

Okay so

### 00:04:22 · Speaker 2

You want them to be

### 00:04:23 · Speaker 3

create a poll this time sir

### 00:04:25 · Speaker 1

No, I don't. I won't. I will just put it here, make it a mixam.

### 00:04:33 · Speaker 1

is on thirteenth Sunday

### 00:04:39 · Speaker 1

Between 10 and 11 30 a.m. Mr. Koken

### 00:04:43 · Speaker 2

So can we have it on afternoon time

### 00:04:59 · Speaker 1

Okay we can do afternoon how about two to three thirty one thirteen

### 00:05:06 · Speaker 1

Anybody has problems with 22330?

### 00:05:11 · Speaker 1

On 13th of October

### 00:05:14 · Speaker 1

Okay so if there are no problems then we will

### 00:05:18 · Speaker 1

that time I'm putting that on the WhatsApp group okay okay so no more discussions on this midterm exam is fixed on yeah we have to say 13th October

### 00:05:30 · Speaker 2

Sorry if I missed it any quizzes in between or it will be direct 13th now

### 00:05:37 · Speaker 1

Oh there will be quizzes I mean see quizzes are independent right every uh fortnight there will be a quiz so next quiz will be next Saturday

### 00:05:48 · Speaker 1

That'll be it

### 00:05:50 · Speaker 3

No no no

### 00:05:53 · Speaker 1

Next quiz will be next Saturday. And yeah, so every alternative Saturday we'll have a quiz that is independent of this exam.

### 00:06:02 · Speaker 1

Syllabus said I mean uh from last quiz to

### 00:06:09 · Speaker 1

many glasses

### 00:06:12 · Speaker 1

Or what

### 00:06:15 · Speaker 1

Yeah which will be cumulative right I mean if some people some portion has been covered the next part of the portion will be for the quiz that's all

### 00:06:26 · Speaker 2

I mean uh from the day zero till whatever cover that will be quiz

### 00:06:31 · Speaker 4

total six classes

### 00:06:34 · Speaker 1

not day zero i mean like you can take it from like previous quiz to this this class right that that way yeah i would i should have said non-cumulative yeah so it's just

### 00:06:45 · Speaker 4

Okay okay

### 00:06:49 · Speaker 1

Okay, so that is settled, I suppose. No more questions on that. Midterm exam is on 13th October between 2 and 3.30. So I can what I can do perhaps is to block your calendars also. That would be a good thing to do. Let me do it right away so that all of us are.

### 00:07:10 · Speaker 1

They do that

### 00:07:15 · Speaker 4

And so this MCQ will be subjective or MCQ type, I mean sorry, midterm will be MCQ or subjective type, I mean, just as pattern of the exam looking for.

### 00:07:27 · Speaker 1

It will be a return exam

### 00:07:30 · Speaker 4

Okay okay

### 00:07:32 · Speaker 1

Objective not MCQ

### 00:07:36 · Speaker 1

It does

### 00:07:43 · Speaker 1

13

### 00:07:48 · Speaker 1

hopefully

### 00:08:02 · Speaker 1

What is the closest number here?

### 00:08:06 · Speaker 1

E one E one two eight six O Z

### 00:08:12 · Speaker 1

Is it even I'm not getting this

### 00:08:16 · Speaker 4

It's on the Teams meeting top

### 00:08:24 · Speaker 1

I require additional

### 00:08:28 · Speaker 1

Hard channel maker

### 00:08:33 · Speaker 2

Yes sir it's E1286

### 00:08:36 · Speaker 1

Correct

### 00:09:03 · Speaker 1

How do we make it a Teams meeting that's not a field

### 00:09:20 · Speaker 1

I just sent a calendar in email and you all see that

### 00:09:30 · Speaker 2

Yes

### 00:09:34 · Speaker 1

Okay, so great, so that is done now.

### 00:09:38 · Speaker 1

Can we have a second please

### 00:09:39 · Speaker 4

Yeah sorry it says DGM Q sir is it what we meant midterm right

### 00:09:47 · Speaker 1

Oh car

### 00:09:52 · Speaker 1

Uh can't edit it for some reason

### 00:09:59 · Speaker 1

Yeah that is what it is it should be yeah

### 00:10:05 · Speaker 1

We don't exactly

### 00:10:10 · Speaker 1

Enter it. Yeah, fine. So practice questions. Well, see this being a graduate level course, it's not a probability theory course or anything, so I can't give you practice questions that way.

### 00:10:24 · Speaker 1

So what I would encourage you to do is read the previous year's notes and also the original papers of things that we are covering. Okay, it will be around that.

### 00:10:37 · Speaker 1

And also you should it would be proctored so you need to keep your cameras on and then write the exam okay

### 00:10:44 · Speaker 1

And the way to do it is either you write it on a sheet of paper scan it and upload or you can write it on your like ipad or whatever and then share us share with us the pdf

### 00:10:58 · Speaker 4

So notes can be different right Or it's not

### 00:11:01 · Speaker 1

You mean during the exam? No. If you want an open book exam, I have to make it more difficult.

### 00:11:03 · Speaker 4

If you want an open

### 00:11:07 · Speaker 1

If you want that, because I'll have to assume that you'll have access to notes and have to ensure that I should ask you things that are not there in the notes, right? So which means that it has to be made a little bit difficult.

### 00:11:20 · Speaker 2

Uh, sir, maybe this question is not right to ask, but just asking the, ill there be a question that where we have to derive these formulas and all which you are teaching us

### 00:11:32 · Speaker 1

And this

### 00:11:37 · Speaker 1

I don't know how to answer it

### 00:11:41 · Speaker 1

Yeah of course you are supposed to know all that time for this

### 00:11:46 · Speaker 1

I'll not ask you the exact thing right because you know whatever I've done in the class I'll not ask you the exact thing but something similar something around it right

### 00:11:55 · Speaker 2

Yeah yeah I mean definitely theory and all definitely I don't know but these formulas are not like little

### 00:12:00 · Speaker 1

See don't have to remember anything not be reasonable not ask you to remember anything other than some fundamentals right for instance see you can't you can't afford to forget the definition of let's say a density function right no no that's for sure i'm saying there is some

### 00:12:15 · Speaker 2

No no no that's

### 00:12:19 · Speaker 1

Obviously I would not ask you to remember some some formula or something I mean you should trust me at that level with some reasonability to what we do

### 00:12:28 · Speaker 2

Yeah yeah no

### 00:12:30 · Speaker 1

Right okay anything else any other comments on the exam stuff

### 00:12:36 · Speaker 1

Start with the class

### 00:12:40 · Speaker 4

So what about results for quiz one?

### 00:12:44 · Speaker 1

I think that should have gotten right I mean uh immediately

### 00:12:52 · Speaker 2

No no no

### 00:12:58 · Speaker 1

really okay so was it done on uh like it was on microsoft form right microsoft forms

### 00:13:07 · Speaker 4

I think it's got to be

### 00:13:13 · Speaker 1

Was it Google Farm or Microsoft Farm

### 00:13:16 · Speaker 2

It was microchip

### 00:13:18 · Speaker 1

Microsoft forms no hold on let let me just ask Chidanand if there is some setting where you should can make the outcome visible right after the curse let me ask him to do that

### 00:13:31 · Speaker 1

Should be seen immediately actually

### 00:13:44 · Speaker 1

not became my call okay i'll i'll tell him to do that

### 00:13:53 · Speaker 1

Because generally the way I ask them to do it is once you submit your answers no you should you should get the the marks right because it is possible because it's a multi

### 00:14:07 · Speaker 1

First question type okay

### 00:14:18 · Speaker 1

So you just double no

### 00:14:18 · Speaker 4

That's all

### 00:14:21 · Speaker 1

Uh the Excel sheet that was passed to us to write the details of the assignment teams it was having four columns and we thought four people can join together and create a team but you all

### 00:14:32 · Speaker 4

so told it's a size of three so there is some confusion there

### 00:14:38 · Speaker 1

Okay, see a four is okay. Uh, like I mean see a recommended team size is three. Okay, so if you

### 00:14:48 · Speaker 1

See what happens is, no, if there are four people, then I mean, dividing work amongst four people will become too much. So I would recommend a team of three, okay?

### 00:15:02 · Speaker 1

But if you are four people, then you should be aware of the fact that when we are grading the assignments, right, we will take that into consideration that it's a team of four and look for like more work.

### 00:15:16 · Speaker 4

Okay

### 00:15:17 · Speaker 1

Good that you reminded me of that. See, assignment, I hope that all of you have taken a look at the assignment. Okay. So what you need to submit is, as I've mentioned, there is one Jupyter notebook. So whatever has been given there as to do, right, that is the bare minimum thing that you should do. Okay. But that will not give you 100% marks.

### 00:15:41 · Speaker 1

Okay, that will give you, let's say, 70 to 80% marks if you just do whatever has been asked for. Now, the remaining 30% will depend upon like what will be the observations that you would be doing, right? And what are the kind of experiments that you have done? Okay, and also I'm planning, I mean, this is not fixed yet. I'll have to ask the TAs if they can do it. But I'm planning to have a Vaibhav, okay, for all

### 00:16:11 · Speaker 1

The assignments combined

### 00:16:15 · Speaker 1

Sometime at the end of the course, we will have a Vaibhav where we will ask you questions on the implementations that you have done right at the end of the course. So try to incorporate as much experimentations as possible and try out multiple ideas and the total evaluation depends on the quality and the quantity of the experiments that you have done.

### 00:16:46 · Speaker 1

Okay, so yeah, so questions, yeah, I did it.

### 00:16:50 · Speaker 2

Ah sir just a last question that this all assignments should be done in group right just reconfirming

### 00:16:56 · Speaker 1

Correct I've told that so many times why questions

### 00:17:00 · Speaker 2

No no no I uh little kid was confused reading first

### 00:17:02 · Speaker 1

But why why where is the confusion I don't understand and what is the there should be a there should be some reason why you are confused no no so many times

### 00:17:07 · Speaker 2

No answer

### 00:17:11 · Speaker 2

No, it was so many times. Yeah, actually I forgot that there was a no project separately. It is only assignment. I'm very sorry for that. Just reconfirm that. Sorry.

### 00:17:22 · Speaker 1

Okay, see an Excel sheet was was circulated where teams had to be groomed and all that, right? I don't know where the confusion is. Okay, no problem. Yeah, where was I?

### 00:17:44 · Speaker 1

Yeah it is not a separate document it has to be embedded in the notebook

### 00:17:50 · Speaker 1

Right. And all the plots, all the observations that you do has to be a part of the Jupyter notebook itself. So what you submit is one file for assignment. That's all. Nothing more.

### 00:18:06 · Speaker 4

Should it come as one submission per team or in each of the team members will submit

### 00:18:13 · Speaker 1

It's about the same thing three times huh

### 00:18:15 · Speaker 4

No that's what I wanted to understand sir like uh how will the submission look

### 00:18:20 · Speaker 1

One submission per team

### 00:18:22 · Speaker 4

One submission per team

### 00:18:25 · Speaker 1

So unless there is, let's say that you're in a team of three and one person sends me a personal email saying that this person did not contribute to the assignment and all that, the rule is that everybody in the team will get the same marks for the assignment.

### 00:18:48 · Speaker 1

Okay, yeah, so one file. Okay, so you coordinate with, see there is one other reason why I ask you to do it in teams, right? Just need some compute resource. So I recommend all of you to like buy some resource from like Google Collab or something, right? But cost some money. You can divide it amongst three of you or four of you if you make teams.

### 00:19:12 · Speaker 1

So that is like another reason why you should make teams. Okay. So anything above anything else about the assignments? And I hope that the Python tutorial was done the last last week. Did you guys do that?

### 00:19:30 · Speaker 1

Was it in school

### 00:19:34 · Speaker 1

Okay, okay. So fine then, I think now we have all everything that you need to start implementing and write the assignment. Please get started with that, okay? Yeah. So anything else, any other logistic thing that we need to discuss before we continue?

### 00:20:01 · Speaker 4

Just one last question

### 00:20:17 · Speaker 1

You don't have to export. It's the code, the corresponding observations. See, when you write, I have asked you to plot a few things. So I have to plot them, to observe what you have done. And as I said, also do things that I have not asked to do or not asked for.

### 00:20:34 · Speaker 1

Right So you can you can do more experiments than what I have asked for and you document that as well, right?

### 00:20:41 · Speaker 4

Yes sir but yeah the plots usually when we run the let's say uh matplot lib.plot

### 00:20:52 · Speaker 1

restart or the cells get lost for some reason then it would be lost right so is it okay to because embedding a image inside the jupyter notebook

### 00:21:03 · Speaker 4

I use it a lot because I'm a

### 00:21:05 · Speaker 1

That's okay, no? That's okay, embedded. I mean, it's okay, I mean, uh... But you have to embed.

### 00:21:12 · Speaker 4

But you have to

### 00:21:14 · Speaker 4

Okay if the results are lost we can embed it uh as a

### 00:21:17 · Speaker 1

Yes you should have to embed right otherwise like how do we evaluate it I mean we'll not be able to run them

### 00:21:25 · Speaker 1

Again, right, we'll run some blocks for sanity check, but it's not that we can we should we can run all cells of everybody, right? So you should embed it, you should embed all that.

### 00:21:45 · Speaker 1

Anything else?

### 00:21:59 · Speaker 1

Okay shall we start then shall we resume

### 00:22:16 · Speaker 1

Hello am I dead

### 00:22:19 · Speaker 4

So we can just go

### 00:22:25 · Speaker 1

Okay, a quick recall of what we did the last time. So we were looking at the adversarial networks for generative modeling.

### 00:22:39 · Speaker 1

The idea was that you are given some data and what you need to do is

### 00:22:45 · Speaker 1

transform an arbitrary random variable into like another random variable of interest another random variable whose distribution is going to be close to the the data distribution that's the idea now what did we do we cast this as an optimization problem which would minimize a divergence metric between the true distribution and the data distribution so we could not uh there is

### 00:23:15 · Speaker 1

No way that we can compute that divergence metric because we don't know the underlying distribution so instead of that we created a

### 00:23:23 · Speaker 1

lower bound on the the divergence metric inside. So once you create that lower bound, you express that lower bound in terms of expectations over the true distribution and the generated data distribution, which can be computed using the sample estimates, right? And the lower bound that we created, okay, involves another optimization problem over a set of a class of functions, which we called as T of x.

### 00:23:53 · Speaker 1

Now these class of functions we represented them as another neural network at T w of x. And therefore you have like two neural networks, one that is representing the transformation of the random variable which would generate the data. The other neural network that would approximate this T function which construct the lower bound on the divergence that we are working with.

### 00:24:23 · Speaker 1

okay then what happened is that the lower bound uh or the so-called cost function will have the difference between these two expectations the first expectation is with respect to first expectation is of uh first expectation uh is on t of x with respect to uh px of the real data the second expectation uh is of f star of t of x uh and the x uh cap or this uh data expectation is over

### 00:24:53 · Speaker 1

the generated data okay now uh because uh since the lower bound itself involves an optimization problem over

### 00:25:07 · Speaker 1

uh i mean a class of functions so we will end up solving what is called as a saddle point problem where you have a cost function okay which is uh a function of uh two variables uh theta which are the parameters of the the generator network and w which are the parameters of the p network okay so that would construct the lower bound on

### 00:25:34 · Speaker 1

the m divergence. So we need to maximize this cost with respect to w okay because that is what is going to create the lower bound and once the lower bound is created we want to minimize that with respect to theta such that the lower bound becomes close to or rather the m divergence is minimized or the lower bound on the m divergence is minimized such that the p theta which is the generated distribution get close to close to px.

### 00:26:04 · Speaker 1

This is the overall philosophy of what we are doing. And in fact, if you recall, I had shared that screenshot of a meme on the WhatsApp. On a serious note, that's exactly how a saddle point looks. I mean, which is like that, I mean, if you have seen that potato chips, right, the top of it is how a saddle point looks. So basically, there are the function has multiple

### 00:26:34 · Speaker 1

parameters right so at this at the point what happens is if you move along one direction

### 00:26:44 · Speaker 1

around the saddle point the function would increase if you move along the other direction okay at that same point the function would decrease that is what we are seeking okay which is the saddle point uh okay so any questions thus far

### 00:27:18 · Speaker 1

No no hold on uh see I never said that the other network is checking whether the image is real or not where did I say that

### 00:27:25 · Speaker 2

I'm just uh checking is that the correct imagination what I am

### 00:27:31 · Speaker 1

Okay, first of all, when did I say that this T network is checking whether the image is correct or not?

### 00:27:38 · Speaker 2

This is discriminator

### 00:27:40 · Speaker 1

But I never said what that is, right? I mean, see, that is an interpretation that I'm going to like give today. See, in general, this critic network is simply a neural network that would approximate this p function that creates a lower bound on entropy. So it's better to see it that way.

### 00:28:03 · Speaker 2

I said this lower bound is not I'm not able to imagine that

### 00:28:12 · Speaker 1

That's what I'm stating right Huh

### 00:28:12 · Speaker 2

That's funny

### 00:28:16 · Speaker 1

See do you I mean do you recall this thing that we did the the one class before this we actually derived that law of bone right

### 00:28:34 · Speaker 2

you are going to explain about discriminator network

### 00:28:37 · Speaker 1

No, I see, I, okay. So it's an important point which you made. See, even though I could explain like, like what this thing would look like, I would do it only for a special case, right? For the general case where you can take any F divergence, this is not a classifier. You understand? See, this T-W network is not a classifier if you take your F divergence to be, let's say, the chi-square distance.

### 00:29:10 · Speaker 1

Okay, the interpretation that you see like all over the internet and all these blocks, et cetera, right? Therefore, a special case of this where this, I mean, we took this, right? Which is if you make the f function to be corresponding to this Jensen channel divergence, only in that case, right, this network becomes a classifier. Or rather, this network can be interpreted as a classifier. Otherwise, this is simply a neural network.

### 00:29:40 · Speaker 1

That is trying to create a lower bound on the up divergence that we would want to minimize

### 00:29:48 · Speaker 1

Is it clear? I think it's very important to have that view that the I mean, why do we have that other network? We have that other network because you have to remember the entire story, right? Our goal was that's why I've written this. Our goal was that we need to minimize the F divergence. We cannot do that and we create a lower bound on that. Now, this lower bound involves an optimization over a class of functions T of X. And that T of X is what we are optimizing.

### 00:30:18 · Speaker 1

Assessing using another network

### 00:30:23 · Speaker 1

Is this clear? So there is see so far there is no like there is nothing that is trying to like classify between the real images and the generated images. I've never said that. Only if you make your f divergence to be the general channel divergence, this t function, right, which would still create a lower bound on the f divergence would take the form of a classifier. And that is why that is when you can interpret it that way. Otherwise, this t network has no meaning.

### 00:30:53 · Speaker 1

Other than just creating the lower bound on the F divergence that we want to minimize. Is this clear?

### 00:31:03 · Speaker 2

Yeah somewhat

### 00:31:05 · Speaker 1

Why so much where is the gap

### 00:31:09 · Speaker 2

I have gone through this uh time this the last week as well another time but I got this confusion to just interpret

### 00:31:20 · Speaker 2

I think I think with this class I may get more clarity or maybe if there is confusion I will ask in next class

### 00:31:28 · Speaker 1

Okay, see, you don't have to interpret it, right? It is simply a neural network that is approximating this t function, which is creating a lower bound on the up divergence. That's all. See, one has to have this kind of a generalized view. Otherwise, you can't go deeper than what you see in these blocks, et cetera, right? The only way to make that next level of jump is to start seeing things in an abstract way.

### 00:31:55 · Speaker 1

That's a glitch. Yeah, so these three lines that I have written, right, you start, I mean, your goal is to minimize the F divergence between two distributions. We cannot do that. So we constructed a lower bound. Now this lower bound that we construct involves an optimization over a class of functions T of X. And that class of functions T of X is what I am representing using a neural network. That's all.

### 00:32:34 · Speaker 1

I'm not sure

### 00:32:36 · Speaker 2

Yeah, you were saying yesterday, right? We'll look through a diagram that one graph that how that minimization happened, right? Once we construct a lower bound on

### 00:32:50 · Speaker 4

the discriminator network what we get then we plot it on a graph and then we further try to minimize it yeah that graph theta and

### 00:32:58 · Speaker 1

Sure. Yeah, again, right. I mean, that would be for this case where your T network can be interpreted as a classifier.

### 00:32:58 · Speaker 4

Because you know

### 00:33:08 · Speaker 1

See, I'll do all that today, okay? That is what I'm going to do now. But as I said, the most general case, there is a version of GAN called LS-GAN, a least square GAN, okay? Where this T network is not a classifier, that will become a regressor.

### 00:33:28 · Speaker 1

So you get it. So it depends. It depends on what is the underlying F divergence that you have chosen for minimization. If you choose your F divergence to be of this particular form, then this T network can be interpreted as a classifier.

### 00:33:44 · Speaker 1

You understand? Otherwise, it is simply a network, okay, or a neural network that is approximating a function T of x. And what is that T of x function? That T of x function is the function that constructs a lower bound on the F divergence that we would want to minimize.

### 00:34:01 · Speaker 1

Is it alright

### 00:34:10 · Speaker 1

Yeah

### 00:34:14 · Speaker 4

Yes, sir. Yeah, I was just reacting. The thing is, sir, like, does it make a difference if we do the minimization first and then the maximization?

### 00:34:25 · Speaker 1

no no no no no no the order does not matter especially because you are you are doing it in a gradient uh based way no this thing how do we optimize this we optimize this using gradient uh based minimization right so it does not matter okay so then what did we do after that is that we looked at one instance of this f can right which is the naive uh uh can i mean that uh that was uh that that that you see everywhere where the f function

### 00:34:55 · Speaker 1

that that you look at will be of this form right u log u minus u plus 1 log u plus 1 by 2 in this case the underlying m divergence is called the Jensen channel divergence or JS divergence so for this particular case right if you

### 00:35:12 · Speaker 1

yeah if you for this particular case if you plug in this particular f and f star and all that the the final uh uh network right can be represented this way right where the t function uh if you represent the t function as a concatenation of uh uh the of of rather if you break down the t function as two parts right one that that is a that would take the x

### 00:35:42 · Speaker 1

and give you a real number and on top of it you have a sigmoid okay and this sigmoid is by definition gives you value between 0 and 1 the final loss function for this right looks like whatever I have written within this flow brackets uh now in this particular case right you can interpret interpret this t function as a classifier because the output of the t function okay is bounded between 0 and 1

### 00:36:15 · Speaker 1

Okay, so that is what it is. And then we looked at how to train this particular network in practice. So you have this loss function, J, J cap, which represents J cap theta comma W. First you sample, I mean you are given n points from the data and you have, you are given m points from p theta as well, right? How do you get those m points? You just sample m

### 00:36:45 · Speaker 1

points from the normal distribution and pass them through g theta of z to get to obtain these m points and then uh i also showed you how to compute right the gradients for both these networks and back propagate through them and train it okay i don't go through this again because we did it in in in detail yeah uh if you have any questions this far i'll take some questions and then we'll move on to today's content uh any questions on this

### 00:37:15 · Speaker 1

Yeah, uh, that's a good point.

### 00:37:19 · Speaker 2

Hi I said good morning

### 00:37:40 · Speaker 4

And so

### 00:37:51 · Speaker 4

log of dw of x and the other term

### 00:37:58 · Speaker 4

How did

### 00:38:06 · Speaker 1

Oh

### 00:38:18 · Speaker 1

No see f has a u log u minus u plus 1 log u plus 1 by 2 right Yeah f f star for this case has a log term there

### 00:38:31 · Speaker 1

Okay and you have s star of t w of x right so there will be a log term there that will come up

### 00:38:38 · Speaker 4

but that is an expectation over p theta right so how is it affecting a p expectation over p extra that was my question

### 00:38:47 · Speaker 1

You mean in the in the in the first case you are saying uh in the first term how are you getting this log d wx?

### 00:38:56 · Speaker 1

Ah I see okay uh yeah I'll tell you how to I I think I did this algebra in the

### 00:39:05 · Speaker 1

Last iteration I think just give me a minute I'll tell you that

### 00:39:22 · Speaker 1

yeah so what we did is that see you represent this t function right the t function as see you look at this right so how are d and t related so d is the sigmoid of tw of isn't it

### 00:39:42 · Speaker 1

So now if you want to represent T in terms of D what do you do?

### 00:39:47 · Speaker 1

The inverse of the T form yeah so that's that's where you have that log

### 00:39:47 · Speaker 2

I'm not the T ball

### 00:39:51 · Speaker 1

That's where you get that

### 00:39:54 · Speaker 4

All right sorry I sure uh that that explains so thank you so much

### 00:39:59 · Speaker 1

Okay so can you please repeat

### 00:40:00 · Speaker 2

So can you please repeat that

### 00:40:02 · Speaker 1

He was asking the question was that there is a T W term here, right? How did you get this log D W term? Right when it is there is no F here. How did you get this log D W term? See, how are this D and T related? See, again, see the reason it is it looks a little complicated here is that the people the Gyan people just wrote down this loss function in terms of one network called D W. Okay. Now,

### 00:40:32 · Speaker 1

in the terminology that we developed in this according to the NTK terminology, what GAN people have called as DW is simply the sigmoid of our T function. It is simply a fixed sigmoid of the T function. Now there is T here, right? Now if you want to write it in terms of T, how are T and D related?

### 00:40:56 · Speaker 2

by the sigmoid relation

### 00:40:58 · Speaker 1

a sigmoid right which is which involves a negative exponentiation so if you want to write t in terms of d then there will be a logarithm right

### 00:41:10 · Speaker 2

Yes sir

### 00:41:11 · Speaker 1

That's all. So you have to invert the sigmoid basically. If you invert that sigmoid, T will be written in terms of log of T. That's all.

### 00:41:21 · Speaker 2

Okay

### 00:41:23 · Speaker 2

Answer in the in the above term

### 00:41:23 · Speaker 1

Seven eight

### 00:41:25 · Speaker 1

Actually you can do yeah tell me

### 00:41:28 · Speaker 2

In the above term, we are doing f star of t w of x x hat. So basically, we are replacing u in the divergence function with t w of x hat.

### 00:41:42 · Speaker 2

And then we are trying to simplify like replacing TW with D, as we have mentioned before using the synchronized relay.

### 00:41:48 · Speaker 1

correct correct so you if you complete that algebra you will get this expression and if i have to do that algebra it will take me 30 minutes not worth it it's simply algebra itself yeah

### 00:42:02 · Speaker 1

Is this all right now

### 00:42:04 · Speaker 1

Okay, and I suppose that that like this training part, right? The forward pass, backward pass, everything for both these networks are okay. Any questions on this? Like how do you train these?

### 00:42:21 · Speaker 1

Because this is exactly what I've asked you to implement in your in your assignment so I hope that these are clear

### 00:42:27 · Speaker 1

Okay so if it's clear then we will go to start with the next

### 00:43:15 · Speaker 1

Okay, so today's agenda is that I will talk further about the GANs and the naive interpretation of how can you interpret it for this particular case. Okay, and then we will look at like a couple of applications of adversarial optimization for this task called domain adaptation and like image to image translation. Okay, there are multiple applications.

### 00:43:45 · Speaker 1

of GANs I talked about it but we'll look at two applications and then if there is time we will start the variation autoencoder part also today okay that is what it is okay let's start so let's start with interpreting

### 00:44:11 · Speaker 1

Knife young

### 00:44:17 · Speaker 1

as classifiers

### 00:44:32 · Speaker 1

Classifier guided generator training

### 00:44:48 · Speaker 1

So this is simply interpreting the naive GAN, right, which is which is which is GAN and divergence as a classifier guided generative model. Okay. What do I mean by that? Okay. Let us recall that what are what are our setting. So setting is that we have data points.

### 00:45:12 · Speaker 1

coming from PX okay we have this particular setup

### 00:45:24 · Speaker 1

you have a neural network or some function that would transform

### 00:45:31 · Speaker 1

The Gaussian random variable

### 00:45:35 · Speaker 1

some other random variable which is random variable of interest p theta right now let's say that what is our goal remember that our goal

### 00:45:48 · Speaker 1

is to make

### 00:45:52 · Speaker 1

E theta

### 00:45:56 · Speaker 1

to peaks right that is this is what our goal is okay now suppose that there is a classifier

### 00:46:18 · Speaker 1

Does it classify it okay

### 00:46:23 · Speaker 1

which is just let's call that as DW of

### 00:46:32 · Speaker 1

is equal to one

### 00:46:36 · Speaker 1

X comes from Px. It is zero if.

### 00:46:42 · Speaker 1

Um okay I should actually make it

### 00:46:52 · Speaker 1

that not conditioned

### 00:46:55 · Speaker 1

Yes in occasion DW

### 00:46:59 · Speaker 1

x or x naught so it will take either x or x cap okay it's one if x is coming from x cap or it's then it is zero if it is coming from p theta

### 00:47:10 · Speaker 1

Do you understand what we are doing? So there is a classifier okay a binary classifier

### 00:47:22 · Speaker 2

what about the other cases when x is not coming from px or x hat is not coming from p theta

### 00:47:34 · Speaker 2

We are saying that the this classifier will be 1 if x comes from px right correct. What if x does not comes from px

### 00:47:46 · Speaker 1

That's all it'll give zero. See this classifier takes either x or x cap as input. Okay. And it will give you one if x is from px. It will give you x cap if it comes from p theta.

### 00:47:59 · Speaker 2

It will give us zero if x cap comes from p theta.

### 00:48:05 · Speaker 2

No, what if X or X cap which we have drawn does not come from PX or PHI theta like

### 00:48:12 · Speaker 1

it should either come from px or from v theta right because dw is yeah dw has been set up in such a way that it either takes x as input or it takes x cap as input

### 00:48:24 · Speaker 2

Okay okay

### 00:48:25 · Speaker 1

So so it's basically what is this this is a

### 00:48:32 · Speaker 1

Binary classifier okay

### 00:48:37 · Speaker 1

between samples of

### 00:48:42 · Speaker 1

samples of Vx and V theta

### 00:48:48 · Speaker 1

Is this all right? Yeah, it's actually a binary classifier that would classify between the samples of p and p data. Is that okay?

### 00:48:59 · Speaker 2

Yes sir

### 00:49:01 · Speaker 1

That's fine right okay now here is the question here is a question

### 00:49:21 · Speaker 3

What do you mean you

### 00:49:30 · Speaker 1

Yeah, this reminds me of something. It's just a slight off topic thing. See, the reason I erased it off is because if you look at the way I have written no, it is...

### 00:49:43 · Speaker 1

It is all the letters like are not aligned along a straight line, correct?

### 00:49:51 · Speaker 1

That's why I erased it up, wanted to write it again. I remember three, four days back, I have a daughter, a school-going daughter. Okay, so she's eight years old. She was writing something on a sheet of paper and she was not writing it along a straight line. And I told her, no, no, this is not the way to write it. So I just reminded that to myself and said, oh, if I have to tell somebody to do something, I have to first adhere to that.

### 00:50:24 · Speaker 1

So writing along a straight line when you don't have ruled thing is a skill.

### 00:50:32 · Speaker 1

Anyway

### 00:50:35 · Speaker 1

If my daughter sees if my daughter sees that she'll ask me right I mean she you asked me to write a finger slide right there what are you doing

### 00:50:48 · Speaker 1

So that reminds me of another joke. So I told her that she asked me what is that you teach? So I told her that I teach math. So then she asked me to like show me what I write. Okay. So I just showed her one day I had like taught back propagation and filled the board with a lot of these equations of back propagation, derivatives and all that. She looks at that picture and the question she asks is, you tell me

### 00:51:18 · Speaker 1

that that you teach math but all that you have written is English right so there is no math here there are no numbers so everything that you have written is English here there is no math okay so anyway so the question that we should ask now is can this classifier

### 00:51:46 · Speaker 1

used

### 00:51:52 · Speaker 1

week

### 00:51:55 · Speaker 1

theta okay such that such that p theta becomes close to

### 00:52:03 · Speaker 1

So this is the question that we will ask now

### 00:52:08 · Speaker 1

So let's say that I'll write the classifier here let's say that we have this classifier

### 00:52:19 · Speaker 1

dw so this will take x or x cap as input okay and gives you a number between 0 and 1.

### 00:52:30 · Speaker 1

Okay, now the question that we are asking is, can this classifier be used to tweet theta, okay, such that p theta becomes close to ph? Do you appreciate the question? Does did all of you understand the question?

### 00:52:52 · Speaker 1

Okay, can somebody answer that question? So now I have given you a classifier, okay, which would tell you whether this, the output of this, or rather, it will tell you whether the sample that it is seeing is from px or p theta. Now I have to p theta, okay, by using this classifier in such a way that the distribution p theta becomes close to px. Can this be done?

### 00:53:28 · Speaker 1

Can somebody answer that Can somebody think of a way to do that

### 00:53:34 · Speaker 2

So that is the uh way we do it right like we train both the classifier and the discriminator

### 00:53:39 · Speaker 4

No no no I have

### 00:53:39 · Speaker 1

No no no I have

### 00:53:40 · Speaker 2

No no not okay sorry

### 00:53:41 · Speaker 1

Okay that's funny I've never going to the top of the top of the top

### 00:53:43 · Speaker 2

That's still F five

### 00:53:46 · Speaker 1

as far as as per as per as far as we have seen it now we are simply constructing lower bounds on f divergence and minimizing them that's all now the question that i'm asking is forget about everything that we have done so far right i'm simply asking you whether in this setup right where uh there is a neural network that would take the samples from a from arbitrary distribution and i'm giving you some other distribution i've given you a classifier that would classify between the samples of true data and the

### 00:54:16 · Speaker 1

of this neural network. Now the question is, by using this classifier, can you make your G theta such that whatever it outputs is close to Px? That is the question. Now don't think about m-dimensions now for a while.

### 00:54:32 · Speaker 1

Okay so

### 00:54:35 · Speaker 1

I think please raise your hands virtually because otherwise it will become sort of chaos. Sanchit, you wanted to say something?

### 00:54:43 · Speaker 2

Yes, sir. So if the samples are drawn from X, we will get a 1. But if X hat is drawn, then we will get a 0. So what we can do is we can try to maximize the overall, like we can go for a cumulative sum of DW outputs and try to maximize that.

### 00:55:06 · Speaker 1

Why maximize with respect to what See what are you tweaking here by the way

### 00:55:12 · Speaker 2

Sir like what I'm uh like trying to see is like

### 00:55:15 · Speaker 1

No, no, I'm not asking you what I'm trying to say. The question that I'm asking is what is what handle do we have here? What is that we can tweak? See, we can tweak theta, nothing else. The classifier is fixed.

### 00:55:29 · Speaker 1

Okay, so what we need to do is simply use this classifier to tweak theta. Tweak theta, you understand?

### 00:55:38 · Speaker 1

I'm asking you a philosophical question at a very high level. How do you use this classifier to tweak this theta such that your p theta goes close to px is what I'm asking.

### 00:55:53 · Speaker 1

Yeah diva

### 00:56:05 · Speaker 1

of course see whenever we try neural networks we always use back propagation that is see i don't go to details now details will be worked out i'm just asking you at a philosophical level so now that i've given you a classifier i want you to use this classifier to tweak theta such that your p theta becomes close to px that is all think about it no yeah abhishek

### 00:56:48 · Speaker 1

what do you mean by that what do you mean but see again don't think of back propagation nothing right i mean just think think of it at a philosophical level i just want you to tell me how to use this classifier to tweet theta okay let me maybe answer because it will take some more time i'm sorry here this okay so what what is what i would do is i would tweet theta okay let me write that down

### 00:57:11 · Speaker 1

to answer to that is that keep

### 00:57:18 · Speaker 1

Changing theta

### 00:57:22 · Speaker 1

data right till

### 00:57:25 · Speaker 1

The classifier trades

### 00:57:34 · Speaker 1

Okay, so what is that? What do I mean by that? So what I do is I will take a theta, okay, and I will see the performance of the classifier. Now classifier is doing pretty well, okay? So then it's not useful for me. What I do is I'll keep changing theta till such a point, okay, where my classifier completely fails.

### 00:57:58 · Speaker 1

Understand

### 00:58:00 · Speaker 1

Now, when would my classifier fail? So now the next question is this implies that if

### 00:58:07 · Speaker 1

Classify a failure

### 00:58:15 · Speaker 1

Then okay then P theta is actually equal to P that's my claim do you agree with that

### 00:58:22 · Speaker 1

If this classifier cannot distinguish between the samples of px and v theta, when would that happen? That would happen only when px is equal to v theta, isn't it?

### 00:58:38 · Speaker 1

You understand

### 00:58:40 · Speaker 1

Yes sir. The classifier would fail only if px is equal to p theta. So now what I'll use, I'll just simply use that. I'll invert this logic and say that okay now if I have a classifier that would classify between the samples of px and p theta, I would keep trying or rather tweaking my theta okay till a point where my classifier starts failing.

### 00:59:05 · Speaker 1

You understand this

### 00:59:10 · Speaker 2

Yes sir

### 00:59:13 · Speaker 1

Okay, so this is how like a lot of these blog posts, et cetera, would motivate GANs. Okay, they'll say that, oh, there's a classifier and you want to make that classifier fail because only when that classifier fails, then your p theta will go close to px, will be exactly equal to px. Okay.

### 00:59:34 · Speaker 1

But there is a catch here. I'll tell you what the catch is. Yeah, I think there are some questions.

### 00:59:40 · Speaker 4

Yes uh are we saying that now at in at this stage the classifier is perfect that it's able to distinguish between x or x naught

### 00:59:48 · Speaker 1

What's what stage at what stage

### 00:59:50 · Speaker 4

So so now I mean with this assumption that the classifier is able to do that right So are we already saying that it is perfect at doing this

### 00:59:56 · Speaker 1

So when we start when we start right I mean we are assuming that okay the classifier is able to classify

### 01:00:02 · Speaker 1

Right. But the argument that I'm going to give you in a while will tell you that it is not enough if you just make the classifier fail. See, this thing that I said, no, that if the classifier fails, then p theta equal to px, right, is not completely true.

### 01:00:18 · Speaker 1

Okay, I don't know if you can see that failure case already, but I'll show you that. I'll show you that in a while. But yeah, any other questions, Sanchit? Yeah.

### 01:00:28 · Speaker 2

I'm not sure if you are going to cover this question ahead but just asking so change tweaking the theta randomly it will take like really really long time so do don't we have some parameter that will govern or that will tell us okay in which direction we have to tweak theta

### 01:00:49 · Speaker 1

Yeah, that is correct. That is correct. But yeah, we'll see how to do that. Yeah, it'll see the direction now is simply that it should be in such a way that the p theta should be close to equal or should be close to px. That is the direction that we are talking about. Anyway, so now I mean, if all of you are convinced that the classifier fails that p theta equal to px, this is this may not be true always. I'll tell you why.

### 01:01:18 · Speaker 1

However that

### 01:01:24 · Speaker 1

Okay uh classifier fail you okay classifier

### 01:01:30 · Speaker 1

Feeling okay

### 01:01:35 · Speaker 1

need not imply

### 01:01:47 · Speaker 1

P theta is equal to Px. Okay, I'll show you a counter example for this.

### 01:01:58 · Speaker 1

Okay, so let's say that our features are in two dimensions, okay? The data is in two dimensions. Let's say that my true data is like this, it is.

### 01:02:11 · Speaker 1

is clustered somewhere here this is only for representations okay so this is the samples from px okay now let's say that when we start arbitrarily with uh with some uh g theta okay i will have data or rather p theta x cap this is my x cap

### 01:02:36 · Speaker 1

X cap is now sampled from P theta. Okay. Now let's say that there exists a classifier that would classify between them. This is the decision boundary. This is my DW.

### 01:02:48 · Speaker 1

Now, okay, so first of all, please note that in practice, neither Px nor P theta would be nicely clustered like this and they are not linearly separable.

### 01:03:01 · Speaker 1

Okay, so I'm simply, you know, this is for illustration purpose, I'm assuming that they are linearly separable and there is a linearization boundary between them, okay? But it did not be the case, okay? Now, what are we saying? That we have to change theta such that the classifier fails, correct?

### 01:03:20 · Speaker 1

Is that okay? Now, what is the decision that this classifier is making? So,

### 01:03:28 · Speaker 1

A gold design

### 01:03:36 · Speaker 1

Below the line

### 01:03:39 · Speaker 1

We did that correct

### 01:03:42 · Speaker 1

This is the way the classifier is classifying so do you agree

### 01:03:46 · Speaker 1

Whatever this E1 below means

### 01:03:50 · Speaker 1

Okay, this is what the classifier has learned. Now this has to fail. What do I do? So I am, I want to tweak my p theta such that the classifier fails, no? What I will do is I will just move this.

### 01:04:14 · Speaker 1

Let me call this as p theta 1 and this is coming from p theta 2. Okay, now here.

### 01:04:29 · Speaker 1

DW would fail, do you agree?

### 01:04:37 · Speaker 1

Some of you agree that DW would fail here

### 01:04:44 · Speaker 1

Yes sir

### 01:04:52 · Speaker 1

Yeah, but now DW has failed, but has it ensured that p theta 2 is equal to px?

### 01:05:03 · Speaker 1

P theta so does not equal to P x

### 01:05:07 · Speaker 1

You see that right so now

### 01:05:12 · Speaker 1

It's not enough if you simply make the classifier fail. The classifier can fail, right? Not only when p theta is equal to px. Of course, when p theta is equal to px, classifier would obviously fail. However, if classifier fails, that does not imply that p theta of x, p theta is

### 01:05:33 · Speaker 1

is px do you see that

### 01:05:37 · Speaker 1

this in place

### 01:05:42 · Speaker 1

P theta equal to Px okay

### 01:05:46 · Speaker 1

In place

### 01:05:50 · Speaker 1

Actually play it for me

### 01:05:55 · Speaker 1

But classifier failure

### 01:06:03 · Speaker 1

Does not imply

### 01:06:05 · Speaker 1

theta being equal to bx

### 01:06:11 · Speaker 1

Is this clear Any questions on this in the mid

### 01:06:15 · Speaker 4

Here, when you are moving X hat above the line, will discriminator not address the line to again differentiate between these two?

### 01:06:22 · Speaker 1

Good question we have not done that yet right have we done that

### 01:06:27 · Speaker 2

No but discriminator will do no

### 01:06:29 · Speaker 1

No no no we have said that the classifier is fixed here right and by the way I have not used the word discriminator I am simply saying it is a classifier

### 01:06:37 · Speaker 1

So when I told this in the first class, I said, you know, please use the terminologies and the names that I've been using. I mean, I understand that it is difficult because you already know all this, right, from other sources, but it's good to use because there's a reason why I'm using those names. For now, this is a classifier, okay? So classifier is fixed. I'm not changing the classifier.

### 01:06:59 · Speaker 1

Okay, now if the classifier is fixed, then simply moving theta such that the classifier fails does not, you know, does not suffice, does not serve our purpose.

### 01:07:19 · Speaker 1

Those are the ones

### 01:07:19 · Speaker 4

Exactly

### 01:07:22 · Speaker 1

Yeah, simple different sample. This line is fixed.

### 01:07:27 · Speaker 1

I don't know who he is yeah but yeah so classifier is fixed or when I say classifier is fixed this is of course this is the classifier that I'm talking about it is fixed

### 01:07:38 · Speaker 1

Uh Harish

### 01:07:41 · Speaker 4

Sir uh one question so our goal is to make p theta equal to px right

### 01:07:46 · Speaker 1

Correct correct

### 01:07:47 · Speaker 4

In that case why do we need a classifier for example so we can just use a regression problem to find the loss and just use

### 01:07:57 · Speaker 2

generator right

### 01:07:58 · Speaker 1

Now what what do you regress over? See what do you regress over? X cap comes right. Do you match every X cap to some X? Is that what you do?

### 01:08:08 · Speaker 1

So what are you suggesting that I just make this take a split or loss and then minimize this? See if I do this then what will happen is the this neural network would simply generate whatever is there in your data. It will not generate anything new.

### 01:08:25 · Speaker 1

So you want to do it at a distributional level no That's why they are doing all this yeah

### 01:08:31 · Speaker 2

So we need to understand the distribution rather than just using the samples

### 01:08:35 · Speaker 1

Absolutely, that is that has been our problem from day one, isn't it? We want it to be done at the distribution level.

### 01:08:42 · Speaker 1

Not at sample level, right? Okay. So now the thing is, yeah, so all of you got this, right? I mean, using the classifier and trying to take in your p theta such that the classifier fails is not enough. You need to do something more. What do you think is that something more that you can do?

### 01:09:00 · Speaker 3

Maybe the dye or the discriminant should dynamically learn

### 01:09:05 · Speaker 1

Yeah, so you move the line. What you should do is you move the line, okay? If this line, okay, so what you do is first you have to make this, so this is DW1. Under this DW1.

### 01:09:19 · Speaker 1

This happened. Okay. What I will do is I will learn another line here. I will learn another classifier. Okay. This is now.

### 01:09:33 · Speaker 1

I TW two

### 01:09:39 · Speaker 1

Okay, now I have to move this P theta again to ensure that this is misclassified under DW2 as well.

### 01:09:49 · Speaker 1

Good idea

### 01:09:51 · Speaker 1

Which means that this P theta 2 now cannot go to P theta 1 place okay it has to go to somewhere else so let's say that this will this will move somewhere here

### 01:10:11 · Speaker 1

Okay, so now the idea is, so this will become P theta three now. The idea is, you know, keep moving your P theta cluster distribution, right? So till a point where these two overlaps. Now, how do you do that? You do that by tweaking this classifier, okay? All in time, maybe I should have written this classifier in a different color.

### 01:10:55 · Speaker 1

These are the axes and you have

### 01:10:59 · Speaker 1

The first classifiers

### 01:11:05 · Speaker 1

TW1 okay and you have another classifier which is

### 01:11:14 · Speaker 1

Like this this is TW2

### 01:11:18 · Speaker 1

that all right you see what's happening so basically we are so

### 01:11:25 · Speaker 1

Therefore okay the classifier okay

### 01:11:32 · Speaker 1

stoopid

### 01:11:37 · Speaker 1

change

### 01:11:40 · Speaker 1

tweet simultaneously

### 01:11:57 · Speaker 1

Does it make sense

### 01:12:00 · Speaker 1

Now you might ask right so now what is the guarantee that uh

### 01:12:08 · Speaker 1

What is the guarantee that when I keep doing this, I will ensure that my p theta is exactly overlapping on px, right? It can actually play a cat and mouse game, right, where the classifier places, moves this to some place and then the generator tries to avoid the classifier and they keep kind of playing that game between those two, correct?

### 01:12:36 · Speaker 1

You understand? So in this case, what can happen? No, this cluster moves here and then it'll come back. So then when you try in the new classifier, it'll go again here and it'll come back and it'll keep, it can keep moving around. Can all of you see that? That this moving around can happen?

### 01:12:52 · Speaker 1

So that is exactly what is called as mode collapse. Okay. Where the the the the GAN training, right, is very unstable. You will actually see that when you are training. So what happens is that the so-called classifier, right, when you are training, the classifier tries to avoid the discriminator and the discriminator rather the generator and the generator tries to avoid the classifier and it keeps happening happening alternatively. Now, what is actually happening underneath you under the hood is every time you

### 01:13:22 · Speaker 1

this classifier right you are creating a lower bound on the f divergence you understand so what do you mean by creating a lower bound on the f divergence is uh learning a new classifier now you can see that right the tighter the lower bound is the better the minimization would be isn't it

### 01:13:43 · Speaker 1

Obviously, right, the tighter the lower bound is on F divergence, the better the minimization would be. What do you mean by creating the tighter lower bound is that you create a classifier that is close enough or a very good, good classifier. And in this example, I've created a very degenerative case where the classifier is linear and the data is very nicely clustered. But in practice, right, you will have these points here and you will have X points here and the classifier will be a nonlinear classifier, right? So classifier will do misclassification, okay?

### 01:14:13 · Speaker 1

However, the tighter the lower bound is, the better this classifier would be. That's how the translation happens in the sense that when the case you consider the F divergence to be general channel divergence, right, you can you can look into this as interpret this as a classifier, right. And because you can interpret it as a classifier, constructing a tighter lower bound translates to creating a classifier that is very good. Okay. Now, if your generator function has to like make

### 01:14:43 · Speaker 1

very good classifier misclassified okay it would better move the cluster close to px because if there is a perfect overlap between these two right px and p theta there is no classifier that is able to classify these two you understand that

### 01:15:00 · Speaker 1

Do you see that? If there exists if if px completely overlaps with p theta then no classifier can classify between px and p theta right points from px and p theta do you agree?

### 01:15:14 · Speaker 1

So what would that translate to? That would translate to saying that your t function, right, or the script t function is representative enough to give you a t x such that the lower bound that we have created on the f divergence becomes tight. There is no approximation here. The lower bound becomes exactly equal to the f divergence. If it becomes exactly equal to the f divergence, then minimizing that would make p x to be equal to p theta, right? And which means in this case, objective channel divergence,

### 01:15:44 · Speaker 1

is no classifier that would uh that would classify between the points of px and pj

### 01:15:52 · Speaker 1

Is this clear

### 01:15:55 · Speaker 1

So constructing a lower bound is equivalent to finding this class new classifier right given a particular px and p theta constructing the lower bound on f divergence is equivalent to finding out this classifier that would classify between these two.

### 01:16:11 · Speaker 1

Okay and minimizing the lower bound is equivalent to moving this p theta

### 01:16:18 · Speaker 1

in this space of data such that it will go very easily to the last one

### 01:16:21 · Speaker 2

Are you using a pointer sir

### 01:16:26 · Speaker 1

Unfortunately there is no pointer in this it would have been so nice if there is a pointer does anybody know if there is a pointer here

### 01:16:38 · Speaker 1

Yeah so yeah I'm not because I don't I can't use a pointer is this clear

### 01:16:45 · Speaker 1

So before you ask your questions, right, let me just complete this story and then. So now instead of writing f-divergence and all that, right, now we can, if we have to optimize this, so I will write this as a cost function, right. So what we have to do is.

### 01:17:02 · Speaker 1

Let's say that my X is coming from

### 01:17:08 · Speaker 1

appears right then I want the log like okay so this

### 01:17:17 · Speaker 1

Okay let me write what I'm trying to write so this is like formulating

### 01:17:25 · Speaker 1

formulating the cost okay via this interpretation so what I will do now

### 01:17:40 · Speaker 1

Okay, of course, we still have the exact same setup, okay? Setup has not changed. So Z comes from normal 0, 1 and you have G theta of Z and what you get here is X cap that comes from P theta. Okay, suppose, suppose.

### 01:17:58 · Speaker 1

DW okay

### 01:18:02 · Speaker 1

is a function from x to space of zero and one. Okay now let

### 01:18:10 · Speaker 1

PW represent

### 01:18:19 · Speaker 1

Let DW represent

### 01:18:24 · Speaker 1

the likelihood of

### 01:18:30 · Speaker 1

likelihood of a sample

### 01:18:41 · Speaker 1

coming from px okay this is the way i have defined pw right it simply gives you the likelihood of a sample coming from px so what do we need so whenever

### 01:18:56 · Speaker 1

It comes from

### 01:19:03 · Speaker 1

We want it to be maximized, no? A classifier should maximize the likelihood, okay? Or let's say P is our P theta. It simply gives you the likelihood of P is our P theta, okay? So whenever X comes from P is, I want to maximize that likelihood under the expectation. Do you agree?

### 01:19:29 · Speaker 1

This is

### 01:19:31 · Speaker 1

I'll write a max here so I have to maximize maximize

### 01:19:39 · Speaker 1

likelihood of

### 01:19:44 · Speaker 1

Okay X

### 01:19:47 · Speaker 1

coming from VX this is that term do you agree

### 01:19:52 · Speaker 1

Let me write it as Px for a by u. Is this okay? So this term is simply maximizing the likelihood of log likelihood of x coming from Px. Is that tolerant? It is lower w.

### 01:20:12 · Speaker 1

Hello is this alright

### 01:20:19 · Speaker 1

Now now so what is log of

### 01:20:31 · Speaker 1

And I discuss

### 01:20:36 · Speaker 1

What is one minus T W of X What is this

### 01:20:44 · Speaker 1

Thomas

### 01:20:48 · Speaker 1

What is this term

### 01:20:56 · Speaker 4

likelihood that it comes

### 01:20:59 · Speaker 3

Mm

### 01:21:00 · Speaker 1

I clean up

### 01:21:02 · Speaker 3

Yeah

### 01:21:03 · Speaker 1

XGAR is not from VX

### 01:21:10 · Speaker 1

Right or in this case

### 01:21:14 · Speaker 1

comes from P J Ta

### 01:21:22 · Speaker 1

Correct is it okay

### 01:21:27 · Speaker 1

Now what do we have to do we'll have to

### 01:21:31 · Speaker 4

speed theta

### 01:21:35 · Speaker 1

So maximum that x cap is not from px oh yeah this is from v theta correct thanks

### 01:21:45 · Speaker 1

We need to maximize this as well, right? We need to maximize. Okay, I'll have to write that in the same notes.

### 01:21:55 · Speaker 1

Now when X is coming from X cap is coming from B theta

### 01:22:03 · Speaker 1

need to maximize this with respect to w so this dw which is a classifier has to do two things whenever x comes from px it has to maximize the the likelihood of x coming from px whenever x is not coming from px or rather x cap is coming from p theta it needs to maximize the

### 01:22:25 · Speaker 1

inverse of the log likelihood rather one minus the likelihood of x coming from px to u. You see this point.

### 01:22:37 · Speaker 1

So the

### 01:22:41 · Speaker 1

Objective

### 01:22:46 · Speaker 1

Classifier training

### 01:22:54 · Speaker 1

Whenever the X is coming from PX this maximise that likelihood

### 01:23:04 · Speaker 1

And whenever excess

### 01:23:08 · Speaker 1

not coming from P so rather it's coming from P theta you maximize

### 01:23:16 · Speaker 1

log of one minus that likelihood

### 01:23:26 · Speaker 1

And I need to maximize this with respect to W

### 01:23:35 · Speaker 1

Is this clear to all of you

### 01:23:46 · Speaker 1

Okay now now what do we have to do see the are now the objective

### 01:23:57 · Speaker 1

Generator training

### 01:24:04 · Speaker 1

What is it what is the objective for generator training now

### 01:24:11 · Speaker 1

Simply

### 01:24:14 · Speaker 1

You know what

### 01:24:16 · Speaker 1

the objective for classified landing

### 01:24:28 · Speaker 1

Because what do we why do we have to do that? The here the objective is to have made the classifier fail no

### 01:24:41 · Speaker 1

Now how do we do that

### 01:24:46 · Speaker 2

It's a

### 01:24:46 · Speaker 1

classifier is yeah if classifier is maximizing something you just minimize that you just completely undo whatever the classifier has done so if i call this as some j okay of theta comma w now you need to

### 01:25:10 · Speaker 1

classifier is maximizing J theta comma W with respect to W then

### 01:25:19 · Speaker 1

generator

### 01:25:22 · Speaker 1

will minimize the exact same objective with respect to theta therefore the complete GAN training is

### 01:25:34 · Speaker 1

you have this j theta comma w okay the classifier has to maximize this while the generator has to minimize this so again we came into the saddle point problem

### 01:25:56 · Speaker 1

this is what you see in a lot of blog posts and you know the popular uh explanation of what gan is including the original gan paper they say that okay we have a classifier so we need to for tweak the this is this what is called as the discriminator right because it's basically a classifier discriminator is it just discriminates or classifies between the points from px and p theta okay and now you have tweaked the classifier in such a way that px is going

### 01:26:26 · Speaker 1

to go to p theta it is not enough if you just try in the g theta because the classifier can fail even without making px equal to p theta so you have to tweak try in the classifier also along with the generator alternatively and the classifier objective is given by just maximizing this is the cross entropy objective right and the generator has to invert what the discriminator is doing and that's how you get into a saddle point problem okay however remember that this

### 01:26:56 · Speaker 1

is this interpretation is only when you assume your f divergence to be the Jensen channel divergence in which case the t network right that would create a lower bound on the f divergence happens to be a classifier it can be interpreted as a classifier now you can see the nice connect right see this objective function right is not some magical thing that just emerged okay it had a very nice grounded mathematical interpretation

### 01:27:26 · Speaker 1

where this maximization is actually creating the lower bound between the m divergence between uh a lower bound on the m divergence between px and p theta right so once you create that lower bound you minimize that and you alternative between creating a tighter lower bound and then minimization okay if you see that from you know if you take one particular m divergence and interpret this dw as a classifier in that case you can you know you can write it this way but it is not

### 01:27:56 · Speaker 1

this way of interpreting is not i'm not a big fan of this because it's too hand wavy right i mean you

### 01:28:03 · Speaker 1

yeah i don't know but it's just my choice uh see i would see like no more uh value and more in a more principled way of understanding in saying that oh you start with an f divergence you want to minimize that and to minimize that you want you don't know px and p theta therefore you construct a lower bound express them as expectations over these two because you can compute them and that lower bound happens to be an optimization over another class of neural networks okay and you construct the lower bound and minimize that

### 01:28:33 · Speaker 1

you keep alternating between these two so that's my way of looking at it but if you make your net divergence to be one particular f divergence called Jensen Shannon divergence then this t function that is used to create the lower bound on the f divergence can be interpreted as a classifier and the rest of the story follows

### 01:28:52 · Speaker 1

Is that okay? It is just one other interpretation or rather the popular interpretation of what the general case of F divergence minimization is. And again, you can see why it is called ad hoc serial optimization, right? You have like a saddle point problem, right? Ad hoc saddle point problem or

### 01:29:10 · Speaker 1

Adversarial optimization

### 01:29:17 · Speaker 1

Because there are two neural networks, one which is trying to undo what the other does, okay, it is adversarial optimization.

### 01:29:26 · Speaker 1

Okay, so finally, right, like post-training, I'll take questions after this. Post-training, I don't know if I told you this last time, post-training, inference. What, how do you do, how do you scan for inference?

### 01:29:42 · Speaker 1

is that to take the

### 01:29:45 · Speaker 1

Try the generator

### 01:29:48 · Speaker 1

Throw away the discriminator completely

### 01:29:54 · Speaker 1

Discriminator is like a poor teacher right once you learn from them you just throw them away

### 01:30:02 · Speaker 1

And this X cap comes from P theta now this P theta has become close to Px

### 01:30:12 · Speaker 1

In fact, there's a nice Zen saying, okay, this Buddhist Zen saying, which I hold very close to my heart, which I keep telling all my students, I don't know if I've told you this. It says that a good teacher, okay, is one who becomes redundant or useless after some time.

### 01:30:36 · Speaker 1

So that is the definition of a good teacher or a mentor. So you should make your mentees, right, or your students independent of yourself after some time. Now, if you keep, you know, keep your students, your students, or keep your subordinates or mentees, your mentees for all your life, you will become a boss, right? Not a good leader or a teacher. A teacher should become useless after some time. So after this course is done, you should not be coming back to me because

### 01:31:06 · Speaker 1

Like you have actually got everything that you want, you've become so independent that you can do things without a teacher. My teacher told me this, right? And I'm just passing that to you. In fact, there is another nice saying that says that if a student is ready, the teacher appears. Okay. When a student is really ready, the teacher disappears.

### 01:31:31 · Speaker 1

very nice it's very deep actually right so the the goal of a teacher is to ensure that the student is ready which is that you know your p theta is what the distribution that the students are in right and you want them to go to px once you have used whatever methods now you can become like an adversary you can score them do whatever and you just invert whatever they are saying in an adversarial manner once they have become theta star right go away there is no use for you right

### 01:32:01 · Speaker 1

So that is what it is, right? During inference, what you do is you sample a point from Z, you get a sample from a normal distribution. Passing to the generator, you get a sample X cap, right? That is from P theta, now which is close to P X. So, I mean, if you remember I showed you that, no, this person does not exist, dot com, right? Every time you do an inference, or rather the refresh of the page, what is happening is a sample from Z is coming, and it is going through a trying generator.

### 01:32:31 · Speaker 1

And a new sample is getting generated from PMX. Okay, so now ideally

### 01:32:39 · Speaker 1

ideally, right, X cap, okay, is not in D. Okay, the data set that you have given, no, your new generated sample will not be in X plus, you take C, Z1 through ZK, you'll get corresponding X1 cap through XK cap, okay, none of these, okay, are in D. So there are new samples that are not in D. That's how you do inference. This is also called generation.

### 01:33:13 · Speaker 1

Okay, see, we have still not done what is called as unconditional generation. This is still, sorry, we have not done what is called as conditional generation. It is still unconditional generation because it is not that, okay, you give a text and a corresponding image gets generated, right? It is simply an image gets generated, okay, or a data point gets generated without any conditioning. So in the next part of the class, I will talk about how to train this or how to convert this into a conditional generator in a while, okay?

### 01:33:43 · Speaker 1

But yeah, so this is how you do inference. So we are done with training. We are done with inference. This is how you do training of a Dyan and an inference. I've asked you to do both of these in your assignment. So to implement them. So one other detail.

### 01:33:59 · Speaker 1

Uh see there is I have asked you to implement something called a deep convolutional neural network okay

### 01:34:11 · Speaker 1

So abbreviated as DCGAN

### 01:34:15 · Speaker 1

What is this? A simple thing, right? So you start with, you build a neural network, right? G theta network. You start with G, okay, that is, let's say in some 32 dimensional space. Okay, let me write that. So you sample G from a Gaussian distribution.

### 01:34:33 · Speaker 1

Okay and that Gaussian distribution is in some 16 dimensional space let's say.

### 01:34:43 · Speaker 1

16 dimensional space okay so now you take a vector that is 16 dimensional okay then you have to go to let's say that your data x is in some r 100 cross 100 now how do you convert the 16 uh dimensional into 100 cross 100 see one thing that you can do is you can have 16 and then you have let's say 32 then you have 64 and you know you keep increasing the dimensions till you have like a 10 000 dimensional vector okay

### 01:35:13 · Speaker 1

So this is your X cap, this is your neural network G theta. And then after you get this X cap, then you can do a reshaping.

### 01:35:21 · Speaker 1

So it's got

### 01:35:24 · Speaker 1

X cap is in R 10,000 cross one dimensional, right, which is a vector. And once you get this, you reshape.

### 01:35:36 · Speaker 1

into 100 by 100 so that you know it will look like a grid of images okay and you have to do the same thing for x no x is in 100 by 100 right so when you send it to the discriminator you should reshape that

### 01:35:58 · Speaker 1

into 10,000 cross 1. So you reshape X into 10,000 cross 1 and you reshape X cap into 100 by 100. This is one thing that you can do and this neural network is a multi-layer perceptron net or a fully connected neural network. Okay. We have seen how to do this back propagation and all that. This is one way to do it. The other way to do it is that you start with a 16 dimensional vector okay and then do what is called as transpose convolution or upsampling.

### 01:36:34 · Speaker 1

Does all of you know about the convolutional neural networks here, CNNs? Is there anybody who does not know about CNNs?

### 01:36:47 · Speaker 1

Okay, I'll take that as an X. So assuming that all of you know about CNNs, right? So what you can do is, see what does a CNN does, a convolutional network does? It will take a grid of images like this, and you have a kernel, which is let's say a 3 by 3 kernel. You place that 3 by 3 kernel on this grid, okay? And take the inner product, and you get another grid, okay? So every point in this smaller grid will now become an inner product between these two and one number. And you, you, uh, move this,

### 01:37:17 · Speaker 1

3.3 grid again and you get the next uh thing and so on right that is how you do it so this is convolution there is something called transpose convolution where you start from a lower dimensional uh uh uh vector right and then you create a grid okay by doing inverts of convolution that operation is called transpose convolution see i will i mean you can ask ts to do it in the next ts session okay how to do transpose convolution

### 01:37:47 · Speaker 1

However, there is a there is a paper called a paper on a write-up called convolutional arithmetic

### 01:38:00 · Speaker 1

Okay, so please refer to that. There they have given how transpose convolution works. So if you use transpose convolutions, right, you can finally get

### 01:38:13 · Speaker 1

uh at the final layer right you actually get a grid of

### 01:38:19 · Speaker 1

You can actually make it uh the grid of whatever size that you want I mean if you are using a color image that is what I've given you it will be like 100 cross 100 cross like three channels right RGB

### 01:38:33 · Speaker 1

Okay, by using transpose convolutions, you can get into get that into a 300 cross 100 cross 3. You don't have to like reshape it. And the discriminator that you have here, right?

### 01:38:48 · Speaker 1

simply become a CNN so it will take a 100 cross 100 cross 3 vector itself okay and give you a number between 0 and 1 this will be a proper CNN okay you can use a ResNet or whatever network that you want

### 01:39:02 · Speaker 1

Okay so let me not present this next

### 01:39:11 · Speaker 1

You can ask TS to cover this if you want, right? What is transpose convolution? And so this, if you use, instead of using multilayer perceptrons, if you use transpose convolutions, this entire thing, no? This is what is called as a deep convolutional GAN, DCGAN, where for a discriminator, you are using a CNN, okay? And for the generator, you are using transpose convolutions. You are not flattening them out. That's your DCGAN.

### 01:39:38 · Speaker 1

Okay, so that's that. So we will take a break now and then maybe go to I'll talk about the conditional GANs and I mean, the some of the applications of GANs as I promised. Before that, I'll take questions on this if there are any.

### 01:39:56 · Speaker 2

So two questions. One thing you mentioned is this classifier interpretation holds true only for

### 01:40:00 · Speaker 4

for this JS divergence. Why is that so

### 01:40:05 · Speaker 4

Why is this specific only for GST tax regions?

### 01:40:05 · Speaker 1

Big fat

### 01:40:08 · Speaker 1

For others, okay, for others, this will become a the the I mean this thing right will not be a classifier between 0 and 1 right this network will give you a a real number see depends on if you recall the output of the t network should come from the way of f star isn't it

### 01:40:30 · Speaker 1

So that domain of f star for this case will become 0 to 1. For the other cases, it will become a real number. So in which case, the output of that network will become a regressor. It will not, I mean, whatever the case might be, you know, it's not a, you cannot interpret that as a classifier.

### 01:40:49 · Speaker 1

No distinguish between in the other cases no so how can we interpret

### 01:40:49 · Speaker 4

No distinguish between in the other cases no so how can we interpret

### 01:40:55 · Speaker 1

But what about

### 01:40:55 · Speaker 4

What the

### 01:40:57 · Speaker 1

I understand

### 01:40:57 · Speaker 4

I understand

### 01:41:00 · Speaker 1

I understood the question so did it to me you cannot interpret that at all

### 01:41:05 · Speaker 1

So there is no classification that is happening. That is why I don't give this as the, you know, the ultimate interpretation. Because only with Jensen and Diversen, this becomes a classifier. For other diversen, it is not a classifier. For instance, there is a paper called, as I said, no, LSGAN, where what is getting minimized is chi-square distance. Let me just show you my screen and that will become like maybe more apparent.

### 01:41:39 · Speaker 1

You see my screen

### 01:41:46 · Speaker 1

Look at the sun

### 01:41:49 · Speaker 1

For different divergences the final output activation is different for Pearson's chi square distance the output activation is a linear function so which is a regessor

### 01:41:59 · Speaker 1

You understand? Yeah. So only with Jensen's channel divergence you have this kind of thing which is bounded between 0 and 1 which becomes a classifier. Now if you use the KL divergence etc. right you just have a line that's all so which cannot be interpreted anyway.

### 01:42:18 · Speaker 2

Yeah and the second question

### 01:42:20 · Speaker 1

See hold on hold on the way to the way to interpret that as if you want to right it is simply a a neural network that is creating a lower bound on the underlying f divergence

### 01:42:20 · Speaker 4

Hey hold on hold on

### 01:42:30 · Speaker 2

Mm okay

### 01:42:46 · Speaker 2

want something different. So you also mentioned that the X hat that comes out is is not in the D.

### 01:42:52 · Speaker 1

Yeah yeah

### 01:42:53 · Speaker 2

Can we really ensure that Or but the question is if you

### 01:42:56 · Speaker 1

But the question is if it depends on if it depends on how tight your lower bound is

### 01:43:05 · Speaker 1

If it's very tight then actually you will get two pairs no which means that you will get very diverse samples

### 01:43:16 · Speaker 1

No, because you are meaning we are doing that at the distributional level. That's the whole point. Okay. Okay. The whole point is that you have you have made the distribution same. See, why did we even start with all this F divergence, et cetera, is that we don't want to overfit, right? I mean, overfitting in in the case of generating models is when you match the distributions exactly. Sorry, when you only match the samples, not at the distributional level.

### 01:43:21 · Speaker 3

What do you want me to do?

### 01:43:40 · Speaker 1

So you're actually

### 01:43:41 · Speaker 2

If you ensure the distributions are same, because we are doing a random sampling you wouldn't get the same.

### 01:43:47 · Speaker 1

Absolutely yeah random sampling is happening because your input right it's actually converting one random variable to the other you're still yeah

### 01:43:48 · Speaker 2

Three new points okay

### 01:43:55 · Speaker 2

Exactly yeah

### 01:43:56 · Speaker 1

so but you have to ensure that the distributions are matched so if the lower bound that you are that you are constructing is very weak right then you will not match distribution because you have you have you anyway minimized a very low very loose lower bound on the f divergence

### 01:44:13 · Speaker 2

I understood

### 01:44:15 · Speaker 1

That is why people say that the end training is very difficult. One, because you're solving that saddle point optimization problem. The other thing is the lower bound that you might get might be very, very loose. If it's very loose, then if you look at that classifier interpretation, your classifier is simply trying to move it in different places without ever overlapping it with PX.

### 01:44:40 · Speaker 1

And also I didn't tell you last class, right? What is the stopping criteria in training this? There is actually no not well-known stopping criteria for this, okay? The only stopping criteria is when people just eyeball the quality of the images or the data that is generating. They just have some pseudo metric to generate what it is. I mean, the pseudo metric to measure the goodness of the samples and then they use that to stop.

### 01:45:10 · Speaker 1

one good stopping criteria so is that because we

### 01:45:13 · Speaker 2

Is that because we is that because we do not know what is the really the tightest bound that we can get

### 01:45:19 · Speaker 1

Exactly and also we don't know the what the underlying distribution is no

### 01:45:26 · Speaker 1

it see also now next part of the class i'll talk about this vessel strains distance and uh uh and uh uh fid right there is a score called fischett's inception distance which i'll talk about the next time that is one thing that is used to monitor the goodness of the generated images but stopping criteria is just that you eyeball the images and see the data and use some surrogate losses and just stop there

### 01:45:53 · Speaker 2

Yep thank you so much

### 01:45:55 · Speaker 1

Yeah sunjet

### 01:45:57 · Speaker 2

in this example which you had mentioned right where we are considering this classifier dw1 dw2 dw3 why not keep the existing classifiers when going for a newer classifier like what i mean to say is instead of going for the single layer perceptron method why not for a multi-layer perceptron here so that we have the other classifier

### 01:46:24 · Speaker 1

I'm sorry, I didn't follow your question. Can you repeat it again?

### 01:46:30 · Speaker 2

Okay, what I am saying is, once we move from DW1 to DW2, right, you are saying that it is likely possible that P theta 2 might take the positions of P theta 1, correct?

### 01:46:42 · Speaker 4

Correct correct

### 01:46:44 · Speaker 2

Now if we have DW1 intact and then we go for DW2

### 01:46:49 · Speaker 1

No there is no impact no we have changed the classifier

### 01:46:52 · Speaker 2

what sir that's what i am trying to say if if we are going for a change right let's let's instead of going for single layer perceptron we go for multi-layer perceptron

### 01:47:01 · Speaker 1

no no no see multi-layer perceptron will not tell will not uh prohibit the class the decision boundary to go somewhere else not go to the previous layer no that has nothing to do with single layer multi-layer see multi-layer single layer which will simply tell you whether the decision boundary is what is the range of decision boundaries that you can learn

### 01:47:25 · Speaker 1

See there is no remembering of the classi previous classifier that is happening here you are just reiterating it completely

### 01:47:33 · Speaker 2

No sir, what I'm saying is we go for a multi-layer perceptron approach like we say that okay we

### 01:47:41 · Speaker 1

Okay see again please understand what a multi-layer perceptron is a multi-layer perceptron is simply a deep neural network that has multiple layers that's all

### 01:47:50 · Speaker 2

Yes sir

### 01:47:50 · Speaker 1

So it does not mean that you are remembering something and all that here it is simply a neural network

### 01:47:58 · Speaker 1

An MLP is a neural network that's all

### 01:48:04 · Speaker 1

Understand it is simply a multi-layer perceptron did you under did you attend the tutorials

### 01:48:12 · Speaker 2

Yes sir

### 01:48:14 · Speaker 1

In tutorials they talked about multilayer perceptrons and training them huh

### 01:48:19 · Speaker 2

Yes it is

### 01:48:20 · Speaker 1

so a multi-layer perceptron is where a neural network i actually talked about a multi-layer perceptron in the last class if you remember what is a multi-layer perceptron you start with take data okay you multiply it with w transpose x and then you make that go through a nonlinear this is the first layer the second layer is you take w2 and then you do another nonlinear this is second layer this is the third layer and so on this is an mlp so the architecture will look like this now you start with this have a fully connected network

### 01:48:50 · Speaker 1

You have W2, you have W1, then you have W2. This is an MLP, which is a deep neural network. It has nothing to do with the classifier remembering what the previous state is and all that. That is not what we are doing. Do you see the difference?

### 01:49:06 · Speaker 2

Yes, sir, I agree on that. But maybe, uh, maybe I, the terminology I used was not correct. What I'm trying to say here is that why not?

### 01:49:15 · Speaker 1

Why not remember what the classifier was at the previous state right

### 01:49:18 · Speaker 2

Yes, sir, it might not remember, but if we go with this approach of multi-layer perceptron, then we might have a tighter

### 01:49:27 · Speaker 2

Hydrophobic on the surface

### 01:49:28 · Speaker 1

We are using multi-layer perceptron. We are using multi-layer perceptrons. We are not using the linear discriminator anyway here, right? So these are neural networks. These are deep CNNs. Even if you are using deep CNNs, see the note that your data is in some very high dimensional space and it can always go to a place where the classifier misclassifies.

### 01:49:50 · Speaker 2

Okay

### 01:49:51 · Speaker 1

Right? So it has nothing to do with the capacity of the classifier. We are talking about data in some 10,000 dimensional space here.

### 01:50:04 · Speaker 1

Okay uh any other question S Sarvek?

### 01:50:10 · Speaker 4

Yes, so this transpose conversation that you mentioned. So for this the input in the Z, should it also be in a grid format or we can use 1D?

### 01:50:21 · Speaker 2

It's a fantastic

### 01:50:21 · Speaker 1

That is a design choice. People have seen both happening. But people generally take people take Z to be a vector right not a grid.

### 01:50:36 · Speaker 1

Let me share that show the DC current paper with you

### 01:50:36 · Speaker 3

It doesn't look

### 01:50:44 · Speaker 1

But uh he's appreciated

### 01:50:47 · Speaker 1

And also this convolutional uh arithmetic also is something that I'll show you hold on

### 01:50:54 · Speaker 1

We are talking now about convolutional automatic

### 01:51:07 · Speaker 1

therapeutic

### 01:51:12 · Speaker 1

So into convolutional arithmetic for deep learning class I'll show you both of them

### 01:51:19 · Speaker 1

You see my screen? No not yet

### 01:51:25 · Speaker 1

You see my screen?

### 01:51:28 · Speaker 1

Now this is that convolutional arithmetic thing, okay? So have a look at it. They talk about all kinds of convolutions with striding, without striding, zero padding, without zero padding. They have pooling arithmetic. You see there is this transpose convolution here.

### 01:51:48 · Speaker 1

Okay, so please have a look at this. Okay, this is one thing. The other thing is this, let me start.

### 01:52:01 · Speaker 1

EC can't type up

### 01:52:09 · Speaker 1

just the DC can paper

### 01:52:14 · Speaker 1

This is how they do it. So at 100 dimensional Z and then you reshape and then you have transverse convolutions, transverse convolutions and then you get to 64 cross 64 cross 3.

### 01:52:28 · Speaker 1

Start with a hundred dimensional uniform distribution Z is projected you caught it no

### 01:52:34 · Speaker 4

Yeah so vector only is converted to start from vector and then you yeah then you do

### 01:52:36 · Speaker 1

from vector and then you yeah then you do the trans correct then you do upsampling transpose convolutions and then get to the final page dimensions

### 01:52:51 · Speaker 1

Okay, anything else?

### 01:52:53 · Speaker 2

Sir can you please share these uh documents which you are presenting

### 01:52:58 · Speaker 1

What did he miss

### 01:52:59 · Speaker 2

We'll be right back

### 01:53:09 · Speaker 1

We can't like

### 01:53:37 · Speaker 1

Okay, done. Okay, let's take a break. It is 11.5. Let's come back at 11.20. And yeah, continue from here.

### 01:53:49 · Speaker 1

Okay see you in about 15 minutes

### 02:10:46 · Speaker 1

Yeah you can hear me Can you see my screen

### 02:10:51 · Speaker 4

No no no no

### 02:10:51 · Speaker 2

No

### 02:10:54 · Speaker 1

So which one should I show this one

### 02:10:57 · Speaker 1

See you on screen start broadcast

### 02:11:04 · Speaker 1

I'll be right you

### 02:11:07 · Speaker 4

Yes yes

### 02:11:09 · Speaker 1

No you can see my screen as a boss right

### 02:11:11 · Speaker 4

That's the p theta it's next thing we should have mentioned as p it's before the objective for classic classifier training site that was

### 02:11:23 · Speaker 1

Uh come again

### 02:11:25 · Speaker 4

Before the object before saturation that's likely to be that X before that light

### 02:11:34 · Speaker 4

before that

### 02:11:36 · Speaker 4

Can you go above a little bit Yeah here if you mention comes from P you mention the P deta to deta right

### 02:11:46 · Speaker 1

Okay thanks

### 02:11:52 · Speaker 1

Okay shall we continue

### 02:11:56 · Speaker 1

So we can look at some of the

### 02:12:03 · Speaker 1

See there are after the scan thing came, too many improvisations over it, a lot of papers, a lot of applications and all that. So in the interest of time, I'll only cover a few of it, a few of them.

### 02:12:19 · Speaker 1

I mean, nevertheless, GAN is now not the state of the art for like generative modeling, right? I mean, people have moved to diffusion models and so on. But anyway, so I will cover a few of them and rest you can read with this kind of a background. The first thing that we will do is what is called as the conditional GAN, okay?

### 02:12:49 · Speaker 1

conditional plan okay what is the objective here the data is is given like this so you have

### 02:13:00 · Speaker 1

Samples like this you know X one comma Y one

### 02:13:08 · Speaker 1

Let's talk now I do

### 02:13:12 · Speaker 1

and so on sorry it's not small it's got the x x and comma y in okay so you have data this way where i'll tell you what this y is okay so this uh coming from let's say p x y some distribution now the x example can be like this you know x can be let's say images okay

### 02:13:37 · Speaker 1

Now why can't we class labels

### 02:13:44 · Speaker 1

with glass labels or okay some textual embeddings

### 02:13:52 · Speaker 1

We will actually make this idea a little more concrete when we go to text condition diffusion models and all that. But yeah, so for now, let us say that these are

### 02:14:05 · Speaker 1

Textual embeddings

### 02:14:09 · Speaker 1

But for

### 02:14:13 · Speaker 1

Or is it it's class labels for X right or textual embeddings for X and if you have data like this the objective is objective is

### 02:14:25 · Speaker 1

To sample from sample or generate slash generate

### 02:14:34 · Speaker 1

The conditional distribution

### 02:14:49 · Speaker 1

Just P of

### 02:14:52 · Speaker 1

x given y so this means that you know there is you will get x given y equal to let's say some class or some text

### 02:15:03 · Speaker 1

Okay, so this is class conditional generation, right? Given a particular text or a prompt or a class label, you need to generate the corresponding image. How do you do this is the question. Okay, so

### 02:15:23 · Speaker 1

are doing so now to do it is the problem is now

### 02:15:30 · Speaker 1

Modernly

### 02:15:33 · Speaker 1

Okay

### 02:15:36 · Speaker 1

P of x given y okay instead of

### 02:15:43 · Speaker 1

instead of px using p theta so now the thing is the setup is exactly the same so you have this

### 02:15:56 · Speaker 1

Z theta of Z clear

### 02:16:02 · Speaker 1

found this um

### 02:16:08 · Speaker 1

Thanks guys

### 02:16:11 · Speaker 1

Now this takes Z

### 02:16:23 · Speaker 1

It shows some working offline is my screen still visible

### 02:16:30 · Speaker 4

Yes yes

### 02:16:33 · Speaker 1

Now you need to generate from a like px given y, right? So what you need to do first is that you condition this generator generation, okay, with y. Now how do you do that is that just add y as another input here. So y goes as another input.

### 02:16:55 · Speaker 1

Now, what happens is that you need to the p function

### 02:17:05 · Speaker 1

the discriminator

### 02:17:13 · Speaker 1

Pass two

### 02:17:16 · Speaker 1

Classify between

### 02:17:22 · Speaker 1

samples of

### 02:17:26 · Speaker 1

P x cubed y okay and

### 02:17:32 · Speaker 1

P x cap given away of course there's dependence on theta okay now this is now sampled from P x cap given away so now how do you do that is that for the same P network that you have the discriminative network

### 02:17:52 · Speaker 1

PW okay sorry it is network

### 02:17:57 · Speaker 1

What you do is simply

### 02:18:05 · Speaker 1

have this x or x cap that is going on as input anyway now you add additional y as input to this that's all that's all it is now the everything else remains the same so now the cost which is j theta gamma w right we will look like this so now the expected value of log of dw okay so this dw now takes x and y both as input the expectation is now with respect to x given y

### 02:18:35 · Speaker 1

sample from P X given Y okay plus that other term which is expectation of 1 minus

### 02:18:47 · Speaker 1

What's that term log of one minus right

### 02:18:52 · Speaker 1

I don't like this

### 02:18:54 · Speaker 1

PW of X cap comma Y okay

### 02:19:07 · Speaker 1

I can actually say that x and y comes from this yeah

### 02:19:12 · Speaker 1

x and y are coming from this and we have x cap x cap comma y coming from p x cap given y conditional theta

### 02:19:24 · Speaker 1

Next slide

### 02:19:27 · Speaker 1

So this is a conditional GAN now during inference right or inference post training

### 02:19:44 · Speaker 1

So what you do is that

### 02:19:47 · Speaker 1

take T theta

### 02:19:51 · Speaker 1

GT dash dash OC okay

### 02:20:12 · Speaker 1

Now sample a Z from normal 0 1 okay and you give a a class label

### 02:20:25 · Speaker 1

or text embedding as input

### 02:20:31 · Speaker 1

is your y and generate x given y equal to some class table

### 02:20:42 · Speaker 1

Our text editor

### 02:20:49 · Speaker 1

Now this y right can be represented as a one hot vector.

### 02:20:58 · Speaker 1

So if it's a class

### 02:21:01 · Speaker 1

Okay now it can be represented as some embedding vector

### 02:21:11 · Speaker 1

If it's a text

### 02:21:14 · Speaker 1

basically there are these embedding vectors no tf-idf or like you know some bird embedding or something don't worry about this so basically you represent a a text as some sort of a vector right i will talk about all this bird embedding how do you generate all this later in the course anyway but yeah so it's some vector that is representing the label just give that as an input to both the generator and the discriminator and solve the same optimization problem and post training you just take that and give it as an input to the

### 02:21:44 · Speaker 1

the train generator this will do what is called as conditional generation it will just show you some examples of this so also all c g m conditional

### 02:22:12 · Speaker 1

Can you see my screen

### 02:22:18 · Speaker 1

See this right is exactly what I had written here. X given Y and you have like you write it as Z given Y. I mean it's basically G generator network takes Z right and given Y that's what it means. So what happens in terms of network? You have Z, you concatenate Y to that and give it as an input. And the discriminator, it takes both X and Y concatenated together.

### 02:22:42 · Speaker 1

Now look at the results, right? So this is for MNIST. So MNIST is our generated data. Every row corresponds to one particular digit. So they have conditioned it on the class labels.

### 02:22:55 · Speaker 1

And yeah, so they have again conditioned it on text. This was a very old paper, it is 2015 paper. So there the 14 paper, right? The embeddings were not, textual embeddings were not that great there. So this, they have done class conditional generation for MNIST. And I think in your assignment, I have also asked you to do a class conditional generation for the data set that I have given. Okay, so that is about CGM. Okay, any questions on this?

### 02:23:26 · Speaker 1

Yeah Sandhya Sandhya Tana Mohan

### 02:23:28 · Speaker 2

Sir, yeah, sir, here X is just limited to images or it can be some

### 02:23:33 · Speaker 1

So it can be it can be anything. See I've been telling this from class one right, GANs are not restricted to images. It can be like speech. People do text people have done text to speech using GANs. No, that is some of these models. So condition it on text and generate speech. So that can be done as well.

### 02:23:54 · Speaker 2

Okay like like

### 02:23:55 · Speaker 1

Can you share the screen

### 02:23:56 · Speaker 2

Like we have the transformer algorithms right like where we give a prompt of text and

### 02:24:04 · Speaker 1

No no that is not see that is not adversarial trained those are

### 02:24:10 · Speaker 1

autoregressive models okay so gpt etc are autoregressive models we will talk about that as well later in this is different this is not see this is adversarial learning this is a gam this is not a autoregressive model this is not a gpt

### 02:24:18 · Speaker 2

This is different

### 02:24:30 · Speaker 1

So this is text conditional generation of images, right? I mean, it's a GAN that is trained, which is minimizing the underlying GAN divergence.

### 02:24:42 · Speaker 1

Okay

### 02:24:47 · Speaker 1

Uh okay one other question by

### 02:24:52 · Speaker 1

Cartik Kumar

### 02:24:54 · Speaker 4

Yes, I just wanted to know about why. Why are we training? Why is it like a range of values in the sense that we will give all the classes that it need to, for example, if it is class labels, we will give all the classes to which it need to train itself so that during inference, we will be giving one among that class. So why would, what would be the range of why? I mean, like.

### 02:25:22 · Speaker 4

A how come

### 02:25:22 · Speaker 1

I did not understand your question

### 02:25:26 · Speaker 4

So for example, if we are training at the case of images, right, and we are giving a next prompt as you shown in the video, like in the paper that, okay, find the mountains in

### 02:25:38 · Speaker 2

Or something in that sense, that can be why, right? Is my understanding there correct?

### 02:25:45 · Speaker 1

Uh no see why okay so uh for now let's say that it's class 10

### 02:25:52 · Speaker 1

It is simply a class label no

### 02:25:55 · Speaker 2

Okay so it can be something like is it a human or is it a yeah

### 02:25:58 · Speaker 1

Yeah represent represent that as a one hot vector so you know what one hot representation means right

### 02:26:05 · Speaker 2

Mm yeah

### 02:26:06 · Speaker 1

So if it's MNIST data, you have 10 classes, represent that as a 10 dimensional like binary vector with one zeros, right? So whenever you get from the class one, then you get, you give like one, like one zero zero zero, concatenate that. Otherwise you'll get zero one zero zero zero, concatenate that and so on.

### 02:26:29 · Speaker 1

Does it make sense

### 02:26:30 · Speaker 2

Got it yeah

### 02:26:38 · Speaker 2

So one question. So when we are, okay, suppose this is something like word embedding could also have been some clip embedding or some such text.

### 02:26:50 · Speaker 1

Yeah

### 02:26:50 · Speaker 2

I'm a bit clear but my question is how do we con how do we join this X

### 02:26:56 · Speaker 1

Concatenate, concatenate, make them like vectors. Just concatenate that with x and then give it as an input.

### 02:27:06 · Speaker 2

Okay I'm sorry that was the same which thank you so much

### 02:27:12 · Speaker 1

So for the discriminator you're saying now how do we concatenate that with X yeah just concatenate that yeah just concatenate

### 02:27:14 · Speaker 2

It's just concatenate that yeah just concatenate

### 02:27:21 · Speaker 1

Oh

### 02:27:21 · Speaker 2

Oh okay

### 02:27:24 · Speaker 1

no attention see y is a vector why do you have attention or anything see y is a vector given a text it is a vector that corresponds to a text take that and concatenate with your x that's all what is the difficulty

### 02:27:39 · Speaker 1

See it's a vector right given a text you get a vector all these words will give you a vector for its sentence isn't it

### 02:27:46 · Speaker 2

Yes

### 02:27:47 · Speaker 1

So did that

### 02:27:47 · Speaker 2

Oh

### 02:27:49 · Speaker 2

But yeah but it comes from a completely different vector space

### 02:27:53 · Speaker 1

How does it matter how does it matter I just want pairs of images and vectors for my training so look at this now what I am given is pairs of images and vectors

### 02:27:53 · Speaker 2

No no no just like

### 02:28:03 · Speaker 2

So your screen is not visible

### 02:28:03 · Speaker 1

Fastest you can do it

### 02:28:14 · Speaker 1

Okay, so basically I have pairs of images and vectors, right? And those vectors can be anything. They can come from like some embedding or it can be a one-hot vector for class labels. It can be anything.

### 02:28:35 · Speaker 1

Okay so she

### 02:28:38 · Speaker 2

So when we concatenate do we have the same dimension size for text embedding and the image in

### 02:28:45 · Speaker 1

not no definitely not see then how would you see concatenation can be done in many ways no see you add you add one more channel for your image right and just repeat all this so many times

### 02:28:59 · Speaker 2

Oh okay this is just a discriminator network we are not generating anything here so maybe concatenation is sufficient to do that

### 02:29:09 · Speaker 1

We are not generating y, we are not generating embeddings, we are just using embeddings to generate from x conditionally. Given a text or given a one-hot vector, we need we want to generate from it. We are not generating embeddings here. There is no attention potential, nothing. I mean, it's simply taking a vector corresponding to a text. You don't even have to do word. Okay, sorry. Maybe I wrote this and you got confused. See, embedding can come from anything. No, let's say that it is simply a

### 02:29:43 · Speaker 1

TDF IDF okay

### 02:29:48 · Speaker 1

you understood right i mean it is some vector corresponding to this vector this thing is concatenate that you have a pair of data or image and a vector you concatenate that vector with this and then try this again nothing complicated at all

### 02:30:03 · Speaker 2

Okay

### 02:30:06 · Speaker 2

But so what is the difference between the CGAN and normal GANs that we use

### 02:30:13 · Speaker 1

Nothing. The GAN cannot do conditional generation. Conditional GAN can do conditional generation. See, in a normal GAN, right, suppose you build a normal GAN on MNIST. You can't control what digit you generate when you do inference. Here, you can control what digit you generate during inference.

### 02:30:40 · Speaker 1

Is it Is it all right

### 02:30:42 · Speaker 2

Yeah yeah thanks

### 02:30:46 · Speaker 1

In fact, in the data set that I have given you, there are some 90 classes, different animal faces, okay? So now I've asked you to build a CNN on say 20 class, there's some 10 or 20 subclass of this data set. So what you will see is that when you give that particular, the way you should do it, to take those 10 classes, represent them as 100 vectors like this, 0, 0, 0, 1, wherever the class is, concatenate this with the z vector, okay?

### 02:31:16 · Speaker 1

and give that as an input to your generator and also the discriminator during inference when you concatenate this is like a switch so whatever class you want you take that particular class and it will generate and do you understand that

### 02:31:32 · Speaker 2

Yes it is the headache of the back propagation to find out what in how in which ways these vectors have to be combined and the image has to be generated

### 02:31:45 · Speaker 1

Yeah, see, don't say it that way. See, the thing is, remember what we are doing. We are trying to minimize the distributional divergence. See, if we do it well, then the divergence between P of P cap given Y and P of P cap given Y will be minimized, no? What do you mean by that? I mean, that is why I spent two full classes on trying to make you appreciate what does it mean to minimize distributions.

### 02:32:14 · Speaker 2

The reason why we concatenate is what I was talking about so the the the if we concatenate also or maybe if we do something some complicated thing like some cross attention or some such neural

### 02:32:14 · Speaker 1

I didn't mean to say that.

### 02:32:27 · Speaker 1

Just add if you want you i if you want you can add no problem

### 02:32:30 · Speaker 2

Yeah okay so okay

### 02:32:32 · Speaker 1

You can combine them any way you want any way you want

### 02:32:35 · Speaker 2

Okay okay

### 02:32:43 · Speaker 1

Okay help me move on

### 02:32:44 · Speaker 2

Yes sir

### 02:32:47 · Speaker 1

So we'll go to like yeah one of the application of this the next thing that we will do is uh

### 02:33:20 · Speaker 1

So we already saw that we can do conditional generation. And one other advantage of doing conditional generation is that suppose you are solving a classification problem and you have less data. What you can do is you can build a GAN, a conditional GAN, and generate class-specific data using conditional GANs and use that for augmenting your classifiers.

### 02:33:46 · Speaker 1

Understand

### 02:33:48 · Speaker 1

If you can do a class conditional generation, then you can use that to like augment your classifier for your downstream task. Does that make sense?

### 02:34:02 · Speaker 4

Sir please repeat again

### 02:34:06 · Speaker 1

See, suppose you have a classifier, okay, and you want to try in a classifier and you don't have data from one of the classes. What you do is you build a GAN on that, on that data, okay, the conditional GAN and generate more data from that conditional GAN. So if you do it in an unconditional way, what happens is you will not know what the label of the generated data is. If you build a conditional GAN, you already know what label the data is coming from, right? And you can use the

### 02:34:36 · Speaker 1

to augment your classifier and retrain your classifier with more data

### 02:34:41 · Speaker 4

Yeah correct sir correct

### 02:34:43 · Speaker 1

Aditya

### 02:34:54 · Speaker 2

so the second half of the can anyway can so wouldn't it like my doubt was the data set the amount of information we have in the images we are just uh creating instances of that right so the classifier should be able to learn the same amount from the

### 02:35:10 · Speaker 1

No no no you will generate new data right it's like augmenting your data suppose you have more data in your data set you classifier would anyway become better

### 02:35:23 · Speaker 1

I mean, again, this is under the assumption that you have trained your GAN well so that the underlying distribution is correctly estimated. If it's not estimated, then what you're saying is true. I mean, the classifier will only see some noise. But if the underlying distribution has been correctly estimated via GAN training, good GAN training, not only GAN, you can use it for any kind of classifier, any kind of generative model, right? Take a generative model, train it well, and you can use that data. Of course, you need to do it in a conditional way.

### 02:35:53 · Speaker 1

data augment your classifier again always do that

### 02:35:56 · Speaker 2

Okay so my my my doubt was if we had sufficient images in order to actually

### 02:36:02 · Speaker 2

uh i mean generate the actual distribution required of that images then wouldn't that be sufficient to directly give a good classifier because we have enough to even estimate

### 02:36:14 · Speaker 1

No, not necessarily, not necessarily. But I mean, your question is valid. What you're saying is, if we can anyway estimate the end-to-end distribution, would classifier would anyway do that? No, not necessarily. Sometimes what you're saying is true in a sense. But sometimes, you know, what happens is, you know, let's say that your classifier is restrictive in the sense that you can't make your classifier large enough, right? In that case, even if you have a lot of data because of restrictions on the architecture of the classifier, unless you have like diverse

### 02:36:44 · Speaker 1

more diverse data you can't train the classifier well

### 02:36:48 · Speaker 4

Okay okay

### 02:36:49 · Speaker 1

So in those cases you can or the other thing now other thing that you can do is let's say that you have class imbalance right then to sample from the tail of the distribution you can use conditional GANs and then augment your classifier.

### 02:37:01 · Speaker 2

Understood okay

### 02:37:04 · Speaker 1

That's a good question by the way yeah

### 02:37:08 · Speaker 2

Hi sir, so the original data must have a must have some data from a class right the generator

### 02:37:14 · Speaker 1

Of course, of course, of course, of course. Otherwise you can't do a condition with generation, right? Yeah. It should have some data from all classes, yeah. Or rather the class that you would want to sample from.

### 02:37:28 · Speaker 1

Okay, so let's move on. So I'll talk about two applications of GANs and then we will like move to the next topic in the next class. The first thing that I want to talk about is what is called as image to image translation. Okay.

### 02:37:59 · Speaker 1

Image to image translation. Okay, what is the thing here is the objective here is let's say that we have two data sets

### 02:38:13 · Speaker 1

X one through X n given by let's say P X

### 02:38:20 · Speaker 1

Uh and there's the why is not

### 02:38:25 · Speaker 1

What do we call it

### 02:38:28 · Speaker 1

Set is also taken okay let me change the notation

### 02:38:37 · Speaker 1

Yes one, yes two

### 02:38:40 · Speaker 1

is send some data that is coming from some distribution peers and you have like

### 02:38:49 · Speaker 1

T1 T2 TN that is coming from ET

### 02:38:56 · Speaker 1

Okay, so the objective is that

### 02:39:05 · Speaker 1

Just a second

### 02:39:21 · Speaker 1

Show some examples so that you appreciate it better just opening that paper just a second

### 02:39:33 · Speaker 1

Now the objective

### 02:39:38 · Speaker 1

to okay translate

### 02:39:43 · Speaker 1

you what that means translate from translate from

### 02:39:51 · Speaker 1

PS to PT

### 02:39:54 · Speaker 1

Okay, what does that mean? Simply show you an example in development standard easily.

### 02:40:04 · Speaker 1

Have you seen my screen?

### 02:40:10 · Speaker 1

this is what it is right so i suppose i want to do a style transfer meaning that i have some style image and i want to convert it to some other style and i mean this is another example right if i have zebra images i want to convert them into horses if i have this you know these are different styles you know photograph to monet to vancouver paintings etc they have winter images you want to convert into summer there are more examples you have let's say that you have sketches you want to convert that into the full images

### 02:40:40 · Speaker 1

other examples that are given yeah this is like you have uh uh you have maps or rather satellite images you want to convert it into map and and yeah and the other way around you have the segmentation maps you want to convert that into full images and so on okay so this is what i mean by translation so basically in my notation you have been given data from two different distributions ps and pt the objective is to convert from one distribution to the other

### 02:41:09 · Speaker 1

Uh did you understand the objective is it clear

### 02:41:16 · Speaker 4

Yes that's good

### 02:41:18 · Speaker 1

Okay now how do we do that is that so recall

### 02:41:24 · Speaker 1

recall that again right so what does it do it will it will take an arbitrary random variable and project it to random variable of interest so this is arbitrary right

### 02:41:41 · Speaker 1

This is data of interest

### 02:41:47 · Speaker 1

So there is no other no reason why easy to be arbitrary right So what you can do is you can build a

### 02:41:55 · Speaker 1

Gang bang

### 02:41:57 · Speaker 1

to take data from the source distribution so s coming from ps and now this converts it into the t coming from pt so let's call that t cap coming from pt cap okay now have a distribution so what you are trying to do is you are trying to start from the the source distribution okay and generate it on the distribution does it make sense you can do that right so basically you can start from any

### 02:42:27 · Speaker 1

the variable and go to any random variable as long as so this f divergence okay that you minimize the divergence between the true target distribution and the generated target distribution why are this GANs this you can do of course there will be a discriminator here right because it's a GAN that we are talking about it is a discriminator okay

### 02:42:50 · Speaker 1

that will take the generated image, the cap, or the real image from the target distribution T and gives you a number between 0 and 1. Now, but this will, so this entire thing, right, this thing will...

### 02:43:05 · Speaker 1

We convert

### 02:43:11 · Speaker 1

PS, right to PD. Okay. So here, right, what is this doing? This is.

### 02:43:18 · Speaker 1

The mark

### 02:43:20 · Speaker 1

P Z two

### 02:43:24 · Speaker 1

PX Similar way this is converting PS to PT. Do you understand this?

### 02:43:33 · Speaker 2

Yes so in that case uh G theta of S will look like a autoencoder right

### 02:43:39 · Speaker 1

No no no bear is auto encoder here

### 02:43:41 · Speaker 2

I mean

### 02:43:41 · Speaker 1

simply there is nothing there is no no no no no no there is no auto inputting nothing is happening it's simply a gam instead of taking z it will take a s as input and it will give you t cap as output that's all

### 02:43:43 · Speaker 2

They're video

### 02:43:56 · Speaker 2

Okay

### 02:43:56 · Speaker 1

Why is there an auto encoder here

### 02:43:59 · Speaker 2

Uh so will there be a need to have a equal sized image uh I mean so initially we sampled z and we got g theta of z

### 02:44:09 · Speaker 1

That's a different question. That's a different question. So what should be the architecture of this? Architecturally changes of course you start with an equal sized input yeah.

### 02:44:09 · Speaker 2

That's the key feature

### 02:44:21 · Speaker 1

But there is no auto encoding only the size of this network changes that I agree

### 02:44:25 · Speaker 2

You can okay

### 02:44:29 · Speaker 2

Yes

### 02:44:32 · Speaker 1

Uh yeah any other questions on this

### 02:44:34 · Speaker 2

And sir, one more thing sir, how we can identify or calculate the performance of this gains like how per it

### 02:44:41 · Speaker 4

are performing well on the data

### 02:44:46 · Speaker 1

this question does not fit into what we are discussing right now it is a good question but it is not i'm talking about this image to image translation right like i've not talked about evaluating games yet so i request all of you to like ask questions that are relevant to what is being discussed right now okay but i'll answer that question how do we evaluate i actually hinted that in the previous session i told you that there are metrics called fid etc uh which i will describe but yeah any

### 02:45:16 · Speaker 1

question that is like relevant to what we are discussing right now please raise your hands before asking questions please yeah Harish

### 02:45:23 · Speaker 2

So while sampling this distribution uh the samples from BS uh from the distribution S here so we really don't know the distribution right underlying distribution in this case.

### 02:45:33 · Speaker 1

We don't know it's just like Z yeah we don't know we neither know PS nor we know PD we just have samples no matter

### 02:45:41 · Speaker 1

So what can we do with that

### 02:45:45 · Speaker 4

So how do we convert that to like for example that in the general one the Z is of the form of like 16 or 32 that I already told

### 02:45:54 · Speaker 1

I already told you right you start with a it's a it's a CNN so it's basically a CNN right of the same size if you want I can write it this way

### 02:46:04 · Speaker 1

It's of the same size

### 02:46:09 · Speaker 1

It's okay the input and the output I mean the intermediate layers can be anything but you can actually make it a unit if you want to get them just like that

### 02:46:22 · Speaker 1

It's an architectural choice what you can do is start from PS okay and reduce the dimensionality and just increase the dimensionality again

### 02:46:31 · Speaker 1

I want to then get your P this is from PS this is your J theta of S

### 02:46:38 · Speaker 1

It's it's an architectural choice you can do it anyway so you can reduce the dimension and increase the dimension again to get to t and the t and s has same dimensions is that correct

### 02:46:49 · Speaker 1

Okay that's so cool

### 02:46:51 · Speaker 4

to the discriminator you have T cap or T it should be and if there any specific reason you're inviting all

### 02:47:00 · Speaker 1

I I mean like by r I mean see when you are looking at the first term you need to give t when you're looking at the second term you need to give t t cap

### 02:47:10 · Speaker 4

Okay

### 02:47:11 · Speaker 1

Right that is how we have been doing that no discriminators either it T cap goes as input or T goes as input depending upon what term you are evaluating

### 02:47:24 · Speaker 1

Yeah service

### 02:47:28 · Speaker 4

Yes, sir, for this image to image translation, so shouldn't there be a need of a mapping from which S is mapped to which T or like good question.

### 02:47:36 · Speaker 1

Good question. Good question. Good question. Yeah. See, there was a paper called picks to picks that actually paired. I mean, this is called pairing. So now how do you, I mean, the question that you are asking basically is that how do you ensure that one corresponding S goes to that same T, right? I mean, the example that I showed, how does the semantic semantics preserve, get preserved? That's a very good question. That is why, you know, in the in the first paper called picks to picks,

### 02:48:06 · Speaker 1

Okay it's called picts to pics here there was pairing

### 02:48:11 · Speaker 1

So pairing was there and pairing was an issue because when you get the data you would do you wouldn't get pairing. There is another paper that came which was called cycle bound where there was no pairing. Okay what they do is

### 02:48:27 · Speaker 1

They do this trick called what they do now if you want to convert from S to T okay so they have a gun okay

### 02:48:36 · Speaker 1

From S to T

### 02:48:42 · Speaker 1

Then they also have another gam from T2S

### 02:48:50 · Speaker 1

Now what they do is in addition to

### 02:48:58 · Speaker 1

in addition to two GAN losses

### 02:49:06 · Speaker 1

Cycle Vian also has

### 02:49:12 · Speaker 2

Stain loss

### 02:49:13 · Speaker 1

No no no as what is called as a cycle consistency loss

### 02:49:24 · Speaker 1

Cycle consistency loss. Now, what do you mean by cycle consistency loss? What they do is, so for GAN from S to T, so you have this, no? You have expectation of log of DS that you get is from T, and you have T coming from PD, plus that expectation of log of

### 02:49:49 · Speaker 1

1 minus TS T cap T cap coming from that generator no PT cap theta okay in addition to this they will have another loss okay that would say that

### 02:50:07 · Speaker 1

Yeah

### 02:50:12 · Speaker 1

If you take the

### 02:50:18 · Speaker 1

Actually yeah so there is another

### 02:50:21 · Speaker 1

here right which is similar to this expectation of log of dt on s

### 02:50:29 · Speaker 1

S coming from PS so they do are the other direction they develop translation in other direction also they have this and S cap coming from PS cap let's call this P right so what they do is they'll say that if I take I will write that so there are two generators here so generator one is taking S and giving T let's call this G1 there is another generator

### 02:50:57 · Speaker 1

Of course there are two discriminators also this is taking T

### 02:51:01 · Speaker 1

and it is giving you yes now what they say is that if i take an image okay uh that has been

### 02:51:12 · Speaker 1

generated okay if I take g1 okay and pass it t

### 02:51:18 · Speaker 1

it sorry given takes S no if I take an S and pass through it

### 02:51:23 · Speaker 1

What should I get

### 02:51:25 · Speaker 1

I'll get an image in T, correct? Now I will take this image T and pass it through G2.

### 02:51:34 · Speaker 1

What should I get

### 02:51:38 · Speaker 2

Say against the same measure

### 02:51:38 · Speaker 1

Against the same image

### 02:51:40 · Speaker 2

That's brilliant

### 02:51:40 · Speaker 1

Right I get I get S right I should get S so I minimize this loss

### 02:51:45 · Speaker 1

is called cycle consistency law similarly they do this they take g1 okay and g2 pass it pass through a t you will get an s you pass it through t you will get another t to take that corresponding t and okay it is this so this is what is the cycle again

### 02:52:06 · Speaker 1

So I claim that if you do this in addition to try to do the variance then the pairing will happen. Let me just show you that.

### 02:52:26 · Speaker 1

Is my screen visible

### 02:52:31 · Speaker 1

Yeah, you see that, right? There are three objectives here, right? One is the two GAN objectives, of course, and there's the cycle consistency objective. What is cycle consistency objective here? So they call this T and S as X and Y, by the way. So and two generators as G and M. So when X goes through G, you get an image from Y, and then you have to go make it pass through the other generator and match that with X1, X, the input image. And you do this for the other generator and add that as another.

### 02:53:04 · Speaker 1

So this is what they get, no input, output of the generator and the reconstruction that is happening. So we have to ensure that this also happens. And they show that if you do this, then the, I mean, you can use this for image to image translation.

### 02:53:21 · Speaker 1

Okay so that's it for today then let me

### 02:53:26 · Speaker 1

Share that

### 02:53:32 · Speaker 1

See, as I said, no, there are so many applications that GANs are being used for. And I know I can teach a full course on GAN. But yeah, so you don't have that time, unfortunately. Yeah, questions are coming.

### 02:53:45 · Speaker 2

Uh so I'm sorry but I did not understand the pairing uh that uh

### 02:53:49 · Speaker 1

There is no

### 02:53:49 · Speaker 2

This is not the question that was asked

### 02:53:51 · Speaker 1

There is no pairing. See, the question was, while doing this, do you need the corresponding S and V? See, in the example that I showed, if you take a sketch and you want the corresponding field image, while training the scan, do you need the pairing? This is the question.

### 02:54:11 · Speaker 2

We we should right we need

### 02:54:11 · Speaker 1

Anyhow

### 02:54:14 · Speaker 1

No, we don't. That is what I'm saying. In pixel to pixel paper, pairing was needed. But in cycle GAN, pairing was taken. I mean, they gave up pairing. They said pairing is not needed. Then how do you ensure that the corresponding image gets generated is through having these two different generators? Even though you want S to be converted to T, you also have another GAN that is T from S and then you have the cycle consistency.

### 02:54:38 · Speaker 2

And then you have the cycle of the testicle convert it back and then the difference between them should be minimal okay yes oh okay okay

### 02:54:47 · Speaker 1

Okay okay uh centered

### 02:54:57 · Speaker 1

Minister

### 02:54:59 · Speaker 2

Translate from English

### 02:55:08 · Speaker 1

What's your question or just clarifying is it

### 02:55:12 · Speaker 1

Or third

### 02:55:12 · Speaker 2

The other GAN was just for you know learning of the first one

### 02:55:17 · Speaker 1

Uh you can say it that way right it is aiding the running of first one but it also gives you one additional advantage that you can have conversion back also no T2S as well

### 02:55:33 · Speaker 1

Yeah such a thing

### 02:55:36 · Speaker 2

So when pairing is given it's more like conditional GAN

### 02:55:41 · Speaker 1

Ah it becomes like a conditional yeah that's a good observation yes it becomes very conditional yeah correct

### 02:55:41 · Speaker 2

I'm sorry

### 02:55:47 · Speaker 1

That's a good observation instead of having uh

### 02:55:51 · Speaker 1

like a text as a one hot vector or as a conditioning variable you have this image as a conditional variable that's a good observation yes in fact you can see this right you can use GAN for inpainting now image inpainting because you can use the input image or the or the like mask image as input and you can train again to complete the image so you can imagine any any of the applications now because what is GAN doing at the end of the day that is why you need to have that abstraction that's taking starting from

### 02:56:21 · Speaker 1

arbitrary distribution it converts it into distribution of interest and it does that via minimizing the f-dimensions now you take your input to be anything that you want and output to be anything that you want and imagine whatever application you want there right

### 02:56:36 · Speaker 2

So, sir, in basically these mobile phones and everything, we see many photo editing tools which convert the image or enhances the image.

### 02:56:47 · Speaker 1

Yeah, they can be GANs. They can be GANs, but right now the state of the art is not GAN. They use diffusion models, charge generating models, but the fundamental idea is the same.

### 02:56:47 · Speaker 2

They're asking us

### 02:56:59 · Speaker 1

They use diffusion models because they are more easy to train and robust. We will come to diffusion models later in this course, okay?

### 02:57:07 · Speaker 1

Okay yeah I'll go

### 02:57:11 · Speaker 4

Uh so uh

### 02:57:28 · Speaker 4

Will it will be uh converted

### 02:57:29 · Speaker 1

What do you mean by quotient and what do you mean by that

### 02:57:35 · Speaker 4

Okay, so when you say that we can we find a loss function by passing it to g g1 s minus s right and that

### 02:57:48 · Speaker 1

will not loss function yeah g1 of s is simply an image

### 02:57:54 · Speaker 1

G2 of G2 of G1 of H is another image. We're just looking at the differences of the images. See, G1 is a generator, no?

### 02:58:00 · Speaker 4

You're welcome

### 02:58:02 · Speaker 4

Ha generator so the image is same which is passed like S is same and whatever we are getting

### 02:58:07 · Speaker 1

whatever we are getting hold on hold on hold on please hold on yeah i'll tell you what is happening take an image s pass it through g1 you get another image t right

### 02:58:09 · Speaker 4

Output

### 02:58:18 · Speaker 1

If you take that T and pass it through G2 you will get some other images

### 02:58:24 · Speaker 1

See that email maybe I should uh

### 02:58:27 · Speaker 2

Okay that's not though it is

### 02:58:28 · Speaker 4

The state the state

### 02:58:29 · Speaker 1

Why is it the original image? Why is it the original image? It is output of the generator it is something you you are matching that to the original image

### 02:58:38 · Speaker 4

Okay, that's what I was confused. I thought you were telling like we are reversing the process and finding out the loss function.

### 02:58:43 · Speaker 2

after that

### 02:58:45 · Speaker 1

It's impossible no you understood what I'm saying right so it's yeah

### 02:58:45 · Speaker 4

Sorry about that

### 02:58:50 · Speaker 1

Okay so it's a different image it's not the because the it is the generator right we have actually there will be another descrip one discriminator here

### 02:58:54 · Speaker 2

Yeah yeah

### 02:58:59 · Speaker 1

EWS will be another discriminator here

### 02:59:06 · Speaker 1

Is it T W T Yes go on okay

### 02:59:09 · Speaker 2

Ah sir when we are talking about the differences between the these two images

### 02:59:13 · Speaker 4

like G2T and G10

### 02:59:14 · Speaker 1

Pixel level differences pixel level differences

### 02:59:17 · Speaker 4

Oh it's a pixel level yes okay great thank you sir

### 02:59:23 · Speaker 1

Yeah

### 02:59:24 · Speaker 2

Okay

### 02:59:25 · Speaker 2

So one question so from this we can see that any arbitrary distribution can be converted by by training to one more other distribution right to make it closer to the one

### 02:59:34 · Speaker 1

So

### 02:59:35 · Speaker 2

Is there are there any cases where we cannot do that? For example, there are two distributions which we cannot train again to for them to convert to one more distribution.

### 02:59:47 · Speaker 1

Theoretically no you can convert anything to anything theoretically

### 02:59:52 · Speaker 1

Yeah, practically what happens is if you do not have like strong priors on data, for instance, if you have, let's say, data like tabular data or data like, you know, where you have compositional data and all that, now it's difficult to train GAN. But theoretically speaking, you can do it. Anything is possible.

### 03:00:12 · Speaker 2

Thank you.

### 03:00:16 · Speaker 1

Okay I think all these questions are

### 03:00:20 · Speaker 1

Yeah it's okay I'm not disgracing that but yes the time is 12 10 now

### 03:00:25 · Speaker 1

See there is one other thing that I wanted to do which is like domain

### 03:00:31 · Speaker 1

What does it mean?

### 03:00:38 · Speaker 1

It's um

### 03:00:43 · Speaker 1

Way to solve domain solving problem of domain adaptation

### 03:01:00 · Speaker 1

via GAMS so I wanted to do that it'll take 15 minutes people like complain if I extend shall I do that in the next class okay I wanted to finish this and go to video and online course in the next class but anyway so it'll take me 15 minutes I'll do it in the next class time okay

### 03:01:22 · Speaker 1

Okay, that's all for today. So we'll have the you will have with quiz next next class. Uh, starting at nine after the quiz, we will look at the domain adaptation with GANs and then we'll move to BAEs. Okay.

### 03:01:37 · Speaker 1

Please see, what I recommend you is that now that we have come to the thick of the things, please start reading the papers that we have discussed in the class in the original. And if I have questions, you can either contact me or TS and get your doubts cleared. Okay. See you then. See if I like, you know, while asking questions, you know, I'm just trying to moderate it a little so that there is relevance. So don't get me wrong. So yeah, questions.

### 03:02:07 · Speaker 1

are always encouraged okay I'll see you next week

### 03:02:12 · Speaker 4

Yeah tha thank you sir thank you sir

### 03:02:14 · Speaker 2

Thank you sir

### 03:02:14 · Speaker 4

Thank you sir

### 03:02:15 · Speaker 2

Kind of

### 03:02:17 · Speaker 4

And just so

### 03:02:17 · Speaker 1

Thank you so much

### 03:02:27 · Speaker 1

T right correct take that T and pass it through G2 you will get some other images

### 03:02:34 · Speaker 1

See that TMA or maybe I should uh

### 03:02:40 · Speaker 1

Why is it the original image? Why is it the original image? It is output of the generator. It is something you you are matching that to the original image. Yeah

### 03:02:47 · Speaker 3

Oh my god

### 03:02:55 · Speaker 1

thing it's very possible no you understood what i'm saying right so it's yeah it's more okay so it's a different image it's not the because it is the generator right we'll have actually there will be another one discriminator here

### 03:03:05 · Speaker 2

Yeah yeah

### 03:03:09 · Speaker 1

EWS will be another discriminator here

### 03:03:17 · Speaker 1

Is it DWT Yes go on okay

### 03:03:20 · Speaker 2

Ah sir when we are talking about the differences between the these two images like G2T and G16

### 03:03:25 · Speaker 1

Pixel level differences pixel level differences

### 03:03:28 · Speaker 4

Oh it's a pixel level yes okay great thank you sir

### 03:03:34 · Speaker 1

Yeah I got it

### 03:03:34 · Speaker 2

I'm not

### 03:03:36 · Speaker 2

one question so from this we can see that any arbitrary distribution can be converted by by training to one more other distribution right to make it closer to the other one

### 03:03:45 · Speaker 4

I don't know

### 03:03:45 · Speaker 2

Is there are there any cases where we cannot do that? For example, there are two distributions which we cannot train again to for them to convert to one more distribution

### 03:03:58 · Speaker 1

Theoretically no you can convert anything to anything theoretically

### 03:04:03 · Speaker 1

Yeah, practically what happens is if you do not have like strong priors on data, for instance, if you have, let's say, data like tabular data or data like, you know, where you have compositional data and all that, now it's difficult to train GAN. But theoretically speaking, you can do it. Anything is possible.

### 03:04:26 · Speaker 1

Okay I think all these questions are

### 03:04:30 · Speaker 1

It's okay I'm not discouraging that but yes the time is well 10 now

### 03:04:36 · Speaker 1

See there is one other thing that I wanted to do which is like domain

### 03:04:41 · Speaker 1

Adverse serial networks

### 03:04:49 · Speaker 1

Just um

### 03:04:54 · Speaker 1

to solve domain solve the problem of domain adaptation

### 03:05:11 · Speaker 1

Why are the ants

### 03:05:13 · Speaker 1

So I wanted to do that. It'll take 15 minutes. People like complain if I extend. Shall I do that in the next class? Okay. I wanted to finish this and go to the additional module and codes in the next class. But anyway, so it'll take me 15 minutes. I'll do it in the next class time. Okay.

### 03:05:33 · Speaker 1

Okay that's all for today so we'll have the you'll have a quiz next next class

### 03:05:34 · Speaker 4

I think so

### 03:05:37 · Speaker 1

Uh, starting at nine after the quiz we will look at the domain adaptation with grams and then we'll move to VAEs. Okay.

### 03:05:48 · Speaker 1

Please see what I recommend you is that now that we have come to the thick of the things, please start reading the papers that we have discussed in the class in the original. And if I have questions, you can either contact me or TS and get your doubts cleared. Okay.

### 03:06:07 · Speaker 1

you then see if i like you know uh while asking questions you know i'm just trying to moderate it a little so that there is relevance so don't get me wrong so yeah questions are always encouraged okay i'll see you next week

### 03:06:22 · Speaker 4

Yeah tha thank you sir

### 03:06:24 · Speaker 2

Thank you

### 03:06:25 · Speaker 4

Thank you sir

### 03:06:26 · Speaker 1

Mm-hmm

### 03:06:28 · Speaker 4

So it's a

### 03:06:28 · Speaker 1

Thank you
