---
id: 1Xz9ijkMAT8
title: Lec 5a - Deep Generative Models GAN Training
date: '2024-11-23'
url: https://www.youtube.com/watch?v=1Xz9ijkMAT8
description: ''
author: prathoshap5226
duration: 01:02:15
model: saaras:v3
transcript: true
---

# Lec 5a - Deep Generative Models GAN Training

## Transcript

### 00:00:02 · Speaker 8

of of FDM okay which will get us to the

### 00:00:09 · Speaker 8

the basic or the vanilla GAN article or GAN model that generally people use. So if your generator function or the F function in the F divergence happens to be of this particular form, okay? The corresponding divergence measure is called the F divergence. Sorry, sorry, sorry, Jensen-Chanon divergence, okay? Now in that case, the

### 00:00:33 · Speaker 8

Hmm

### 00:00:38 · Speaker 7

Loss Function

### 00:00:40 · Speaker 0

will take this particular form let me write that. So the cost

### 00:00:51 · Speaker 0

for the above case

### 00:01:04 · Speaker 0

the cos function

### 00:01:07 · Speaker 0

what was that recall that let us denote that with

### 00:01:10 · Speaker 8

some

### 00:01:13 · Speaker 8

JF

### 00:01:15 · Speaker 8

theta comma w which is a function of theta and w what was that? It was expectation of t of x right? As x comes from b x minus expectation of

### 00:01:32 · Speaker 8

star of P of

### 00:01:34 · Speaker 8

Skip

### 00:01:36 · Speaker 8

as x cap comes from theta right this was a cos function in general

### 00:01:42 · Speaker 8

Now if you take this F, right, and plug it in here, uh see in the FGyan paper, right, uh they have given the F and the corresponding F stars. I will show you that. So if you use that and do that, for this particular case, this will be equal to the expectation of

### 00:02:04 · Speaker 8

as coming from P X

### 00:02:07 · Speaker 8

Law

### 00:02:07 · Speaker 0

log

### 00:02:11 · Speaker 0

I think this is T W

### 00:02:17 · Speaker 7

log of d w of x okay minus

### 00:02:24 · Speaker 7

expectation of x cap coming from p theta

### 00:02:32 · Speaker 0

log

### 00:02:33 · Speaker 0

one minus

### 00:02:35 · Speaker 0

T W of X

### 00:02:43 · Speaker 0

D W, D W. So simply one by

### 00:02:49 · Speaker 7

1 plus

### 00:02:52 · Speaker 7

e power minus theta w of x.

### 00:02:57 · Speaker 7

which is simply sigma of T W of S

### 00:03:03 · Speaker 7

So

### 00:03:03 · Speaker 8

I mean if you uh maybe we will make this uh

### 00:03:09 · Speaker 8

an item in the T A session

### 00:03:12 · Speaker 8

And as I said, please note, take a note of what all to be done in the T S session and you should ask Chandan to do that, okay? So what is to be done is that you take this F divergence and you take the corresponding F star and you plug in that F divergence here in this equation and if you simplify the algebra, you will get this cos function this way.

### 00:03:37 · Speaker 8

Okay. Where instead of T W which is represent another function T W which is simply you take that T W and put a sigmoid at the output of it. Okay which is I'll write that. So now what happens is that you have a network.

### 00:03:53 · Speaker 7

g theta of z

### 00:03:57 · Speaker 7

to take G S input.

### 00:04:00 · Speaker 7

normal zero one and you get x cap

### 00:04:04 · Speaker 7

that is coming from P theta.

### 00:04:06 · Speaker 8

Okay. And you have another network which would give us the lower bound row, lower bound.

### 00:04:15 · Speaker 8

This we called as the

### 00:04:18 · Speaker 8

D W of X, right? X or X cap, sorry, it should be X cap. X cap. D W of X cap. So this network is simply

### 00:04:30 · Speaker 7

Oh

### 00:04:32 · Speaker 7

what we were writing as

### 00:04:33 · Speaker 0

T network

### 00:04:38 · Speaker 0

plus a small sigma here.

### 00:04:44 · Speaker 0

sigma one. So this is this entire

### 00:04:46 · Speaker 8

I think it's D and yeah

### 00:04:50 · Speaker 8

this was T and you have a sigmoid on top of it. And you get what because it is a sigmoid no you get a number that is between zero and one. See this is only for the case where your F F divergence has this particular form.

### 00:05:06 · Speaker 8

So this if you see, if you

### 00:05:10 · Speaker 0

if you if you can notice this is the the loss function

### 00:05:22 · Speaker 0

of

### 00:05:25 · Speaker 0

Knife can, isn't it?

### 00:05:26 · Speaker 8

If you people have seen that if you look at the blog post and all that. They would say that this is the last function of a GAN. It actually comes from here that you I mean this is the usual F divergence minimizer the the last function that we have. And for that if you plug in that particular F star I will show you that paper. F GAN paper you will understand. I have done that in my notes also just have a look at it. I will share my screen.

### 00:05:55 · Speaker 7

You see my screen?

### 00:06:00 · Speaker 0

Not yet sir

### 00:06:01 · Speaker 7

Okay

### 00:06:01 · Speaker 2

Okay

### 00:06:01 · Speaker 2

Sir

### 00:06:05 · Speaker 8

You see it now

### 00:06:07 · Speaker 7

Yeah. Yes sir.

### 00:06:08 · Speaker 2

Yes, yes.

### 00:06:09 · Speaker 8

ओके, दिस इज दैट एफ गियान पेपर, राइट, व्हिच एक्चुअली आई टॉट सो फार।

### 00:06:15 · Speaker 8

Now all these M divergences etcetera. So look at this table now in this table what they have done now they have given different divergences and different F functions corresponding to those divergences and the corresponding T functions optimal T functions and for Gyan right which is the naive Gyan this is what is the generator function. Okay. Now they have skipped the algebra I think I have done it in my notes or you can ask you can ask Chandan to do it. So now with this particular look at this now with particular

### 00:06:45 · Speaker 8

revergence metric, your output activation function which I just said no that at the output of the T function if you put an activation that would change. It is simply expressing the T function in a different way.

### 00:06:59 · Speaker 8

Right so so finally this objective you know which is the objective function of a Gyan that would happen under this particular F divergence

### 00:07:09 · Speaker 8

So if you take a different f divergence, let's say if you take the Pearson's chi squared distance, uh or the different f function, uh instead of uh Gann's uh f divergence, the Jensen channel divergence, then you would have different uh different loss function basically, right? All you have to do is just plug that in. I will show you the corresponding uh yeah, f star also. You see this, no? So there is many divergence metrics are there, both.

### 00:07:39 · Speaker 8

and you have the output activation function which is just the appending that you do on the T network. because why should you do this output activation function it is because if you recall the T function is designed in such a way that its output comes from the domain of F star.

### 00:07:55 · Speaker 8

Right? For the corresponding active corresponding F divergence that you choose, you'll have to choose your F function in such a way that it would respect domain of F star. Okay? That is why you should have another you should have another activation at the output of the D function. That is why you have an activation. You have the corresponding conjugate function also, no? F star. So what you should do is once you pick an F, you you get an F star, you plug in that F star and you adjust for the output activation, you get the new loss function for that F divergence.

### 00:08:26 · Speaker 8

Is that clear? So that is how you get the you get the loss function for the naive Gyan. So they chose in fact somebody was asking in the beginning of the session right? Did they start with this math and come back? No that is not how they did. In the original Gyan paper they write this loss function in a different I mean from a different motivation. I will tell you that motivation also. It is not mathematically grounded. But this paper right F divergence it creates that Gyan class where the naive

### 00:08:56 · Speaker 8

Gyan also becomes a member. Okay. So, did all of you get how we got from the uh the loss function of the F Gyan or rather F divergences to this particular instantiation. It's simply as I said no we have defined a class. A Gyan class. From the Gyan class uh we got one instantiation with this F of U becoming Jensen Shannon divergence.

### 00:09:21 · Speaker 8

any questions on this? Yeah, Mukesh.

### 00:09:25 · Speaker 5

सर शुडंट एफ ऑफ वन बी इक्वल टू ज़ीरो लाइक इन दिस जंसन डाइवर्शन

### 00:09:32 · Speaker 8

Yeah, it is, you know. No, no, f of, no, it's not. I think we corrected that, no? It should be f of, let me just see that. f of zero is one.

### 00:09:40 · Speaker 9

touch

### 00:09:41 · Speaker 9

f of zero is one

### 00:09:42 · Speaker 9

I think the second term should be here log of u plus one by two.

### 00:09:49 · Speaker 8

let me just see that. I make a mistake here.

### 00:09:55 · Speaker 8

No, that's correct.

### 00:09:58 · Speaker 8

f of 1 is 0

### 00:10:01 · Speaker 5

Yeah, but f of one doesn't evaluate to zero with this equation.

### 00:10:05 · Speaker 8

evaluate to zero here. It evaluates to what? That is zero. This is log two. It evaluate to two log two, right?

### 00:10:16 · Speaker 12

Yeah

### 00:10:16 · Speaker 5

it was u plus one by two

### 00:10:16 · Speaker 8

it was u plus one by two.

### 00:10:20 · Speaker 5

So it is u plus one by two in the original expression. So if it is u plus one by two then it will evaluate to zero.

### 00:10:28 · Speaker 8

I know but there is no u plus one by two in this generative function in face. Okay. So fine I can put it u plus one by two that's also convex that will evaluate to one node in that case.

### 00:10:40 · Speaker 5

Yeah

### 00:10:43 · Speaker 8

Syllable Eight Two One. Okay.

### 00:10:48 · Speaker 8

See, okay, so I I'll tell you where this thing is. See the the GaNs loss function that they use, no, it's not a proper f divergence in the sense that it is half by f divergence by that, you know, two log two factor.

### 00:11:05 · Speaker 8

Do you understand? So that's why you are getting that term.

### 00:11:10 · Speaker 8

divide that by two it will become proper Jensen standard divergence it will become that Gyan's objective.

### 00:11:17 · Speaker 8

So it is half by that that factor two log two.

### 00:11:22 · Speaker 8

Anyway, yeah, Raghavendra

### 00:11:24 · Speaker 4

Uh sir, can you please repeat why you said that we need this final activation of sigmoid? Uh this is because

### 00:11:30 · Speaker 8

this is because, yeah, this is, this is because

### 00:11:35 · Speaker 8

uh this is because uh the T function that we the way we defined no? The T function we defined that what was the T function? It was from uh X right? The domain of X to the domain of F star.

### 00:11:56 · Speaker 4

Yeah

### 00:11:57 · Speaker 8

Right? So now if you choose a particular f star f function, you'll have to ensure that your t function has the output that obeys domain of f star.

### 00:12:14 · Speaker 4

Okay and sigmoid is one. Or is the only one?

### 00:12:18 · Speaker 8

Sigmoid is one for this f function.

### 00:12:21 · Speaker 4

Okay

### 00:12:23 · Speaker 8

for this function sigmoid is the one that you take.

### 00:12:28 · Speaker 8

So that's fixed

### 00:12:28 · Speaker 4

So that's a fixed mapping or for a given function

### 00:12:31 · Speaker 8

for a given function it is fixed that is why I showed you in that fgan paper they have listed the output activation for different fgn lenses.

### 00:12:42 · Speaker 4

Okay, yeah. Thank you.

### 00:12:44 · Speaker 8

in fact, it's a good point that you made. See,

### 00:12:49 · Speaker 8

because the the output activation for this particular f function happens to be giving you a value between zero and one no. The t function in this case can be interpreted as a classifier.

### 00:13:09 · Speaker 8

Do you understand that? See now because the T function in this case will give you a value between zero and one, it can be interpreted as a classifier. That is why it is called a discriminator in that case.

### 00:13:25 · Speaker 8

Alright

### 00:13:26 · Speaker 8

I mean, it's in general it is it's called a critique, right? I mean, it can be anything. But in this particular case because it it gives you a value between zero and one, you can call that a classifier. You can interpret that as a classifier. That is another interpretation that I'll give you. Okay.

### 00:13:26 · Speaker 7

Yeah

### 00:13:46 · Speaker 8

Great. Okay, so now what we will do is the following. We have I promise that I will write down the gradients and all that. No, I will do that now.

### 00:13:57 · Speaker 8

Okay, let us write the optimization problem now. So we have

### 00:14:03 · Speaker 8

Theta Stars

### 00:14:06 · Speaker 8

and W star

### 00:14:08 · Speaker 8

So you need to

### 00:14:12 · Speaker 8

minimize with respect to theta and you have to maximize with respect to W, right? uh what is that? In this case it will be log of

### 00:14:24 · Speaker 8

you have an expectation there

### 00:14:29 · Speaker 0

All of you mute please.

### 00:14:42 · Speaker 0

from P X minus

### 00:14:46 · Speaker 0

expectation of

### 00:14:49 · Speaker 0

What was that? log of one minus T W

### 00:15:03 · Speaker 0

X cap, X cap is coming from

### 00:15:06 · Speaker 8

की जेटा राइट

### 00:15:08 · Speaker 8

this is the loss function. Now we know that we can approximate these using expectations using law of large numbers, right? So approximating

### 00:15:22 · Speaker 0

the expectations

### 00:15:30 · Speaker 0

law of large numbers.

### 00:15:40 · Speaker 0

simply resample estimates.

### 00:15:49 · Speaker 0

How do we do that?

### 00:15:51 · Speaker 0

We have

### 00:15:51 · Speaker 7

let me write that cos function on j theta comma w this is what I am

### 00:15:58 · Speaker 7

representing as J.

### 00:16:05 · Speaker 0

then

### 00:16:06 · Speaker 7

equal to

### 00:16:08 · Speaker 7

uh

### 00:16:11 · Speaker 7

n samples of data, it is one by n.

### 00:16:17 · Speaker 7

I equal to one through N

### 00:16:20 · Speaker 7

Log off

### 00:16:22 · Speaker 7

T W X I

### 00:16:27 · Speaker 7

Money

### 00:16:27 · Speaker 0

minus

### 00:16:29 · Speaker 0

like there's much spectation over this all

### 00:16:36 · Speaker 0

1/m

### 00:16:39 · Speaker 0

J is one through M

### 00:16:44 · Speaker 0

log of one minus T W

### 00:16:48 · Speaker 0

X cap J

### 00:16:53 · Speaker 0

where

### 00:16:57 · Speaker 7

x one x two up to x capital n

### 00:17:03 · Speaker 7

are coming from P X which is the data

### 00:17:08 · Speaker 7

right? And you have

### 00:17:11 · Speaker 7

X one cap. X two cap.

### 00:17:17 · Speaker 7

up to x m cap are coming from b theta which are the

### 00:17:25 · Speaker 7

आउटपुट ऑफ जी थीटा नेटवर्क

### 00:17:28 · Speaker 7

How do you get this sample?

### 00:17:34 · Speaker 7

Z one through Z M, okay? From normal distribution.

### 00:17:40 · Speaker 7

and

### 00:17:43 · Speaker 7

past and

### 00:17:46 · Speaker 0

through

### 00:17:49 · Speaker 0

G theta

### 00:17:52 · Speaker 0

See, two of ten

### 00:18:07 · Speaker 0

Is that okay? So this, right? Now,

### 00:18:09 · Speaker 7

Let me call this as J cap because I'm taking a sample estimate, okay? Now this J cap, J cap.

### 00:18:18 · Speaker 0

theta can be computed, right?

### 00:18:28 · Speaker 0

Any questions on this?

### 00:18:31 · Speaker 0

This is pretty important

### 00:18:33 · Speaker 8

This is what you are going to implement. So this J cap can be implemented, no?

### 00:18:39 · Speaker 8

Yeah, uh

### 00:18:41 · Speaker 8

Sarvesh

### 00:18:43 · Speaker 10

Yes, so is there a specific reason of choosing NNM different or like, ah, okay, or can be something

### 00:18:48 · Speaker 8

Ah okay. It can be something. It's just batch processing no that's batch size. Of training your discriminator and generator you can use any batch size.

### 00:18:58 · Speaker 10

Okay

### 00:18:58 · Speaker 8

typically you don't take the entire data set, no? You do uh stochastic gradient descent where all of you know what stochastic gradient descent is, right? It can then talk about it. When you do gradient descent, you don't take all data points, you just take a subset of data points and you iterate over it, no? That's what one epoch means. All of you know this, no?

### 00:19:21 · Speaker 0

Okay. No questions on this. So now the cap can be computed. So now how do you train this? Training again.

### 00:19:35 · Speaker 0

Practically

### 00:19:45 · Speaker 0

Hello

### 00:19:46 · Speaker 0

True

### 00:19:47 · Speaker 8

don't take me wrong but I'm just take this in a lighter note. for the person who who said that I'm paying this much not to learn maths. I hope I'm doing some justice now by telling you how to try and guess practically also. okay. that was

### 00:20:06 · Speaker 8

right, please don't take it negatively, it's simply a clean a line or not. Okay, so now let's see finally how see how to train again practically, right? So now what happens is we do it using gradient designs. Let me write the

### 00:20:22 · Speaker 0

architecture here

### 00:20:32 · Speaker 0

World has become too sensitive these days.

### 00:20:35 · Speaker 8

You can't crack jokes.

### 00:20:38 · Speaker 8

but take it too seriously

### 00:20:40 · Speaker 8

I'm not talking about you in general, right? So, if you crack jokes with your friends and spouses or children or students, everybody takes it too seriously.

### 00:20:53 · Speaker 4

we are the samples of the same population.

### 00:20:55 · Speaker 8

No. See, when I was a student, I don't know. Most of you might be younger than me, right? I'm thirty-five. So most of you will be maybe, you know, late twenties or early thirties. Every five years is a new generation now. My teachers used to do all kinds of things for us, you know, they used to harass us, embarrass us, beat us, all kinds of things and we never took it seriously, but this generation, my God.

### 00:21:30 · Speaker 8

somebody again in one of those feedbacks somebody wrote not your course. somebody wrote that you are just doing your job you are getting paid for what you are doing so there's nothing great about you teaching.

### 00:21:44 · Speaker 8

I I think I realized that okay that is one way to look at this entire thing I'm doing my job which is true. Okay so let's not even do this let's say that he

### 00:21:58 · Speaker 0

So this is the

### 00:22:13 · Speaker 0

See our parents

### 00:22:14 · Speaker 8

always tell us right that aapko paida kiya, bada kiya and all that. imagine if children tell them that you just did your job. which is also true. we never say that right so.

### 00:22:29 · Speaker 8

Yeah

### 00:22:30 · Speaker 8

That's how people do it in the West, right? I mean, this happened by the way. A child went to court against their parents and the and the case was that that that he he put a case on their parents for having given birth to him.

### 00:22:53 · Speaker 8

without his consent

### 00:22:56 · Speaker 6

Wow

### 00:23:02 · Speaker 6

If I say something like this my parents will slap me first

### 00:23:07 · Speaker 8

No, I said, and if you don't mind, I'll just take two minutes on something that one of my senior colleagues from IIT Delhi told me. It's a story which he told.

### 00:23:18 · Speaker 3

please share sir, please share

### 00:23:20 · Speaker 8

so he said that it have see I have so many stories to say outside of this class the problem is that you know I I it's not my job to tell you stories it's my job to teach you to gyans unfortunately. Anyway so here is I was having a conversation with one of my very senior colleagues from IIT Delhi he also got a you know some highest national award for science Professor Bhim Singh very prolific senior man he was already sixty five then when I was there I was a twenty five years old kid.

### 00:23:50 · Speaker 8

when I joined as a faculty then twenty six twenty seven years. I was talking to him and he narrated a nice incident very funny incident to me. He said he has a collaborator from some university in Canada. He's an Indian guy Punjabi guy okay. Now what had happened is this professor in Canada he had gone to university for work. And like that professor's son who was ten twelve years old.

### 00:24:21 · Speaker 8

he was left in home with his grandfather, grandchildren, sorry, grandparents, who is this professor's father and mother, okay? Parents. Now, this grandfather scolded that pota, okay? did something. And this grandchild who was born and brought up in Canada, he lodged a complaint against his own grandfather. And in those countries, you know, my own sister stays in Sweden and it is it is a true thing that

### 00:24:51 · Speaker 8

If a child goes to police and complains against their parents, the children is just taken away, okay? Parents are penalized under law and children are taken away and put into some government looked facility, okay? So now this professor comes back home and there is police there interrogating his parents. So what had happened and all that. So then he somehow managed and this kid has complained basically, you know, he said that my grandfather abuses me and all that. So then

### 00:25:21 · Speaker 8

this professor somehow managed. So a few months later, the entire family visits India, okay, for for vacation. Maybe my my colleague Professor Bheem Singh exaggerated this, but the way he told me is, the moment they touched down India, right? This this this professor starting hitting that kid in the airport itself. like jor se maar raha tha. So a few

### 00:25:51 · Speaker 8

when came to came to came to this professor and asked him kya hota hai right why are you beating your child. So this professor narrated that entire incident. That policeman said that hum bhi maarenge unko. It is more possible sir.

### 00:26:07 · Speaker 6

is possible sir. This is definitely possible.

### 00:26:11 · Speaker 6

I mean so

### 00:26:11 · Speaker 8

So, yeah, so I mean that's the cultural difference, no? I think, you know, that is slowly weeping into our culture as well. We should be very careful with our students, very careful with our children these days. uh And by the way, Indian law also has that and you cannot, I mean, you cannot quote unquote abuse your children.

### 00:26:31 · Speaker 8

See my mother I still remember she used to she used to take these you know I don't know what it is called in English

### 00:26:43 · Speaker 8

I don't know. See the thing that you that you use to place hot utensils on top of your stove, no? What is it called? There's I don't know what is it called. It's a heavy throng kind of a thing that is made in in steel. Iron actually, not even steel. So she used to take that and hit me on my knuckles. So and that was that was a usual thing, you know, I never took it offensively. If I do it to my child now maybe she will go and complain to police.

### 00:27:18 · Speaker 11

Maybe you are unaware of the rights

### 00:27:19 · Speaker 6

Right

### 00:27:21 · Speaker 8

Perhaps

### 00:27:22 · Speaker 6

I had a I had a geography teacher in my school days and he used to tell me that like all the students that pad chhuo. So he used to tell us to like touch your own feet. And the moment we used to touch our own feet, he used to smack us on our back with a wooden stick. So I mean this is very common in our generation but this Gen Z it's very difficult to even scold them.

### 00:27:27 · Speaker 8

and

### 00:27:32 · Speaker 8

Hello

### 00:27:36 · Speaker 8

woman we used to

### 00:27:50 · Speaker 8

exactly, exactly. Anyway, so that's for a different day's discussion. Let's get back to what we were doing. Okay, so what will happen is, so there is this j cap theta, w, okay? Which is one over n.

### 00:28:08 · Speaker 8

you have some

### 00:28:11 · Speaker 8

Overall

### 00:28:12 · Speaker 12

property and you have drawn for the G data etcetera right it is changed usually for the different

### 00:28:20 · Speaker 8

come again? I I'm not following.

### 00:28:21 · Speaker 12

Okay

### 00:28:22 · Speaker 12

the diagram you decide that you know drawn for the G theta of Z usually draw a different property right not this one. Should be expanding.

### 00:28:27 · Speaker 8

Yeah

### 00:28:30 · Speaker 4

should be expanding not narrow.

### 00:28:32 · Speaker 8

Oh sorry sorry sorry sorry correct. So because the dimensionality of Z is much lesser than that of X. Thank you.

### 00:28:41 · Speaker 8

It's my mistake

### 00:28:46 · Speaker 8

So typically right Z comes from some eight sixteen or thirty two dimensional space okay when you implement. So it is it comes from thirty two dimensional Gaussian okay. So X is of course X cap is in R D where D is the data dimensionality if it's an image it is ten thousand dimensional whatever your data dimension is. So this is it and then minus you have one over M.

### 00:29:19 · Speaker 8

we have one minus z log, we always forget that it is log of one minus that, okay.

### 00:29:32 · Speaker 8

See I could have actually written this down and started discussing Gyan with this. I don't like that narrative at all because I don't understand where this last function came suddenly right it just appeared out of blue and why should this work and so on I I would I was never convinced. I think this is a more principle way of doing it okay. Now how do we train that. So now we need theta T plus one so let us look at the

### 00:29:57 · Speaker 8

different colors

### 00:30:00 · Speaker 8

This is for the

### 00:30:01 · Speaker 7

Let's train generator training

### 00:30:11 · Speaker 7

Okay. For generator training what you should do

### 00:30:14 · Speaker 8

is that you should write theta t plus one is equal to theta t minus the gradient of j cap

### 00:30:26 · Speaker 0

evaluated at theta T

### 00:30:36 · Speaker 0

comma W T

### 00:30:40 · Speaker 0

with respect to theta

### 00:30:49 · Speaker 0

So there is this

### 00:30:54 · Speaker 8

You can use your favorite optimizer by the way. I mean I am simply writing a uh this thing uh stochastic gradient descent. You can use Adam or RMS prop like back prop I mean this thing uh gradient descent with momentum whatever doesn't matter. So so now you get this. Now how do you do that? That's you look at the gradient.

### 00:31:19 · Speaker 8

of J cap

### 00:31:21 · Speaker 8

with respect to theta

### 00:31:24 · Speaker 8

simply look when observe that the first

### 00:31:28 · Speaker 7

term right here. This term is

### 00:31:32 · Speaker 7

scratch it out.

### 00:31:38 · Speaker 7

this term is

### 00:31:39 · Speaker 8

independent of theta, right? It's so the gradient becomes zero. So the gradient is simply the gradient of

### 00:31:49 · Speaker 8

Negative

### 00:31:51 · Speaker 8

1 minus L

### 00:31:53 · Speaker 8

j equal to one through m log of one minus d w

### 00:32:01 · Speaker 8

scab

### 00:32:03 · Speaker 8

J. Now, uh the way I have written, no, the dependence of theta is not accurate, but observe that X cap J, okay, maybe I'll write it explicitly so that it will become easier for you. This is

### 00:32:18 · Speaker 8

E W of what is this? This is G theta Z I no.

### 00:32:25 · Speaker 8

the dependence on theta is uh is apparent so this is

### 00:32:30 · Speaker 8

is okay. So now how do you do that? So, uh first you do a

### 00:32:38 · Speaker 8

let's write down the forward pass using green. So you take this two one forward pass through G theta. So you get

### 00:32:47 · Speaker 8

x j or g theta of c j, okay?

### 00:32:54 · Speaker 8

Okay, then X J cap. And pass this

### 00:32:59 · Speaker 8

X J cap through D W X. I will not write X here because it can take both X or X cap. Then what do you get? The output what you get here is D W of X J cap. Okay? Once you get this,

### 00:33:18 · Speaker 0

which is

### 00:33:19 · Speaker 8

Okay, I will write that down.

### 00:33:19 · Speaker 0

bus

### 00:33:30 · Speaker 0

is also d w of

### 00:33:33 · Speaker 8

x j cap. Okay? Then you have this d w of x j cap, right, which is this this term. So you can compute the log of it.

### 00:33:43 · Speaker 8

Right? Once you compute the log of it, you compute, I will write the gradients in in blue. So you compute the gradient of this.

### 00:33:52 · Speaker 8

log of

### 00:33:54 · Speaker 8

one minus d w of x j cap

### 00:33:59 · Speaker 8

Okay? And then back propagate that all the way through this. It comes like this, the gradients and goes all the way

### 00:34:06 · Speaker 7

through the input. So this is with

### 00:34:11 · Speaker 7

W fixed

### 00:34:16 · Speaker 8

This okay? So now to do one backward pass through the generator, what you have to do is first do a forward pass through the generator, get X J cap. Take that X J cap. So this is

### 00:34:34 · Speaker 0

So

### 00:34:54 · Speaker 0

I think the timing of the tutorial

### 00:34:55 · Speaker 8

was perfect, no? So the backdrop was taught precisely before I wanted to do this. That was the intention. Okay, I hope this is clear. Any self-explanatory

### 00:35:08 · Speaker 0

any questions on this?

### 00:35:25 · Speaker 0

Does anyone have any questions?

### 00:35:34 · Speaker 0

Hello, am I audible?

### 00:35:39 · Speaker 7

Yes sir. Yes sir.

### 00:35:40 · Speaker 12

Yes

### 00:35:40 · Speaker 3

Yes sir

### 00:35:40 · Speaker 8

Yeah, okay. Is this clear? It should be pretty clear, no?

### 00:35:45 · Speaker 3

Yes sir

### 00:35:46 · Speaker 8

Okay. Now let us do the this is generator training okay. Let us do the same thing for similar thing for discriminator training. I don't want to clutter it with this. I will write another.

### 00:35:59 · Speaker 8

So can we extend the class by ten minutes? Like because I want to finish this today.

### 00:36:02 · Speaker 7

Yes

### 00:36:06 · Speaker 7

Sure sir

### 00:36:07 · Speaker 0

Let's write the discriminator training.

### 00:36:13 · Speaker 0

critic discreminated training

### 00:36:30 · Speaker 0

then we will do the same thing here.

### 00:36:33 · Speaker 0

Srishti

### 00:36:39 · Speaker 0

record pass. I'll use some other color.

### 00:36:44 · Speaker 0

Which colors?

### 00:36:48 · Speaker 0

Hello

### 00:36:54 · Speaker 0

See, someone's suggestions on using different color was really good.

### 00:36:59 · Speaker 8

I never thought about this.

### 00:37:02 · Speaker 8

it will add one or a dimension to

### 00:37:05 · Speaker 8

remotes okay forward pass.

### 00:37:09 · Speaker 8

who are suggested

### 00:37:10 · Speaker 0

Thank you. So this is how the network is.

### 00:37:26 · Speaker 0

A bar B sign in A

### 00:37:31 · Speaker 0

of

### 00:37:43 · Speaker 0

Okay, that's not matter

### 00:37:47 · Speaker 0

sorry

### 00:37:47 · Speaker 8

you have this C1

### 00:37:50 · Speaker 8

up to C M sample from N zero one and we have this G theta of C

### 00:37:58 · Speaker 7

the network and the output is X

### 00:38:05 · Speaker 7

fix

### 00:38:08 · Speaker 7

app, let us

### 00:38:12 · Speaker 0

What did I write here? I wrote this. X one cap through X one X I cap, okay.

### 00:38:27 · Speaker 0

okay? So okay. And then you have the critique or the discriminant of network.

### 00:38:36 · Speaker 8

you know that this network can take x or x cap both as input, okay? So in this case what did we do? uh we only took x cap through the d w network, no? Because we only wanted to compute the second term, correct? Here we will see that we have to take uh okay, so maybe I will make it concrete. y y x here, we only take x cap here as input, correct? In the discriminator training, sorry, in the generator training,

### 00:39:06 · Speaker 8

only x cap goes with the discriminator so that is perfect. okay here both of both will go. this will be a number between zero and one.

### 00:39:18 · Speaker 8

point one because it has a sigmoid at the output. Fine. Now J

### 00:39:25 · Speaker 8

θ, W is equal to 1 over N

### 00:39:31 · Speaker 8

is one through n you have log of d w of x i minus one over m

### 00:39:40 · Speaker 7

from one throw M

### 00:39:43 · Speaker 7

log of

### 00:39:46 · Speaker 7

one minus

### 00:39:50 · Speaker 7

P W of G theta of C theta

### 00:39:56 · Speaker 7

Okay. Right. Now we will look at the

### 00:40:01 · Speaker 0

Okay

### 00:40:04 · Speaker 0

Training

### 00:40:08 · Speaker 0

or

### 00:40:12 · Speaker 0

District

### 00:40:17 · Speaker 8

or the discriminator in the case of this particular if tag origins. So it will be, so you have to write W T plus one.

### 00:40:28 · Speaker 8

this is W T minus some beta times the gradient of same loss function with respect to theta that you have taken at the Tth instant and W that you have taken at the Tth instant. That's all. So this is how you try it. Now to find the gradient what you do is

### 00:40:52 · Speaker 8

take

### 00:40:54 · Speaker 8

So note that the output of the discriminator, right, you need to compute

### 00:41:01 · Speaker 8

T, okay, gradient we are writing like this. Now we have to compute T.

### 00:41:07 · Speaker 8

gradients of the first term which is log of d w of x i. Now how do you do that?

### 00:41:17 · Speaker 8

simply take some x i's, okay? So this is x one through x n, okay? Pass it through the discriminator.

### 00:41:27 · Speaker 8

you will get T W of

### 00:41:31 · Speaker 0

Exide

### 00:41:32 · Speaker 0

Okay, then you compute this.

### 00:41:40 · Speaker 0

Okay, and then

### 00:41:47 · Speaker 0

back propagate this all the way to the input

### 00:41:51 · Speaker 0

Is this okay? As for the first term.

### 00:41:56 · Speaker 0

Alright

### 00:42:02 · Speaker 0

Okay. So what about second term?

### 00:42:08 · Speaker 0

for the second

### 00:42:09 · Speaker 7

term we need to do the following. So we need to

### 00:42:14 · Speaker 0

to one forward pass through the generator.

### 00:42:23 · Speaker 0

Okay. uh This way we'll get

### 00:42:33 · Speaker 0

Okay? Now, take all these.

### 00:42:40 · Speaker 0

and pass it through

### 00:42:41 · Speaker 0

the discriminator

### 00:42:42 · Speaker 7

Hello

### 00:42:43 · Speaker 0

Oh, there is no

### 00:42:44 · Speaker 0

Special

### 00:42:48 · Speaker 0

What do I do?

### 00:43:01 · Speaker 0

take all this and

### 00:43:04 · Speaker 0

shall I write a copy of

### 00:43:05 · Speaker 8

discriminator here again

### 00:43:06 · Speaker 0

Trip

### 00:43:07 · Speaker 0

Hello

### 00:43:11 · Speaker 13

But I guess you can create a space like that

### 00:43:11 · Speaker 5

Baggage

### 00:43:12 · Speaker 5

Base

### 00:43:14 · Speaker 8

How

### 00:43:15 · Speaker 13

Sir, in top, I guess there is double-sided arrow, right? Somewhere.

### 00:43:20 · Speaker 7

last

### 00:43:20 · Speaker 13

will also select

### 00:43:23 · Speaker 7

Left hand Left hand

### 00:43:23 · Speaker 2

Fifth Icon

### 00:43:25 · Speaker 8

left of the

### 00:43:27 · Speaker 13

rubber.

### 00:43:27 · Speaker 7

rubber

### 00:43:29 · Speaker 8

Here, uh, no, here.

### 00:43:32 · Speaker 2

Left left of it

### 00:43:33 · Speaker 13

Yeah. You can go to space.

### 00:43:35 · Speaker 8

Court

### 00:43:37 · Speaker 8

How? Okay, I got it.

### 00:43:39 · Speaker 2

click on it somewhere and track

### 00:43:40 · Speaker 13

Okay

### 00:43:41 · Speaker 2

Drag down

### 00:43:41 · Speaker 8

Done

### 00:43:41 · Speaker 13

down

### 00:43:44 · Speaker 8

Factors

### 00:43:45 · Speaker 10

No sir. Sir, it's with pencil.

### 00:43:46 · Speaker 8

Sir, pencil

### 00:43:48 · Speaker 10

click on where you want to add space and pull it down. It's like pulling that block down.

### 00:43:54 · Speaker 8

Oh. Oh, nice.

### 00:43:57 · Speaker 8

I didn't know this at all. Okay.

### 00:44:03 · Speaker 0

is not getting cut. I don't want that to happen.

### 00:44:19 · Speaker 0

looks like I can't do it.

### 00:44:21 · Speaker 5

it it will get cut sir entire page gets down

### 00:44:25 · Speaker 7

you will have to do from blank space.

### 00:44:25 · Speaker 12

Union

### 00:44:25 · Speaker 12

from black

### 00:44:30 · Speaker 8

Okay, so maybe let me

### 00:44:32 · Speaker 0

do one thing

### 00:44:34 · Speaker 0

this I can rewrite no problem

### 00:44:49 · Speaker 2

So there are different pencils as well.

### 00:44:53 · Speaker 7

different

### 00:44:54 · Speaker 2

Pencils

### 00:44:55 · Speaker 7

Hmm

### 00:44:56 · Speaker 8

Yes

### 00:44:56 · Speaker 2

सो इफ यू आर चेंजिंग सेम कलर ऑफ सेम पेंसिल, यू कैन यूज डिफरेंट वन।

### 00:45:04 · Speaker 8

How is that?

### 00:45:05 · Speaker 2

So there are already there.

### 00:45:07 · Speaker 8

So here's a

### 00:45:08 · Speaker 2

Yeah

### 00:45:09 · Speaker 8

Oh, you change them to different colors, I see. And you can add more pencils also.

### 00:45:14 · Speaker 2

Yep

### 00:45:15 · Speaker 8

ಓಕೆ ಗ್ರೇಟ್ ಥ್ಯಾಂಕ್ ಯು. ಯೂಸ್ಫುಲ್ ಟಿಪ್ಸ್.

### 00:45:21 · Speaker 8

Okay, yeah, this is okay. This is one forward pass. So now once you get this, what you can do is that you take this.

### 00:45:29 · Speaker 8

and pass through the discriminator. I have to write another copy of discriminator here.

### 00:45:38 · Speaker 8

Snow through

### 00:45:42 · Speaker 8

Please don't, okay, if I write it, what if you think that there are two discriminators? That is what I'm worried about.

### 00:45:49 · Speaker 8

There aren't two discriminators, there's only one discriminator here.

### 00:45:54 · Speaker 8

you get this x one through x m and you take them and okay

### 00:45:58 · Speaker 7

pass them through the discriminator.

### 00:46:06 · Speaker 0

to obtain, what do you get? You get

### 00:46:14 · Speaker 0

complete

### 00:46:20 · Speaker 0

log of

### 00:46:20 · Speaker 7

Hello

### 00:46:21 · Speaker 0

1 minus

### 00:46:22 · Speaker 7

T W of

### 00:46:24 · Speaker 7

जी थीटा जेड आई जे

### 00:46:29 · Speaker 7

Right

### 00:46:30 · Speaker 0

compute this and then

### 00:46:33 · Speaker 0

propagate

### 00:46:53 · Speaker 0

to the discriminator. So now in

### 00:46:56 · Speaker 7

this entire thing right? uh I I have to write that here. See the entire thing here.

### 00:47:03 · Speaker 7

W

### 00:47:05 · Speaker 0

is kept fixed.

### 00:47:13 · Speaker 0

Okay, so here

### 00:47:17 · Speaker 0

Theta is fixed

### 00:47:24 · Speaker 8

Is this clear? How do you try and discriminate? So discriminator has two terms, right? uh I mean, both the terms and the laws depends on discriminator because you have D W both here. So for the second term, it's simple. You just take uh samples from uh X one through X M, pass it through that. You get this, then compute log of D W X I, take the gradient, back propagate, that's all. To get the second term, start from Z one to Z M, pass it through the fixed generator, you get X one

### 00:47:54 · Speaker 8

cap two x m cap. Take those samples, pass them to the discriminator and compute this log of one minus d w g theta z j and then back propagate that loss.

### 00:48:07 · Speaker 8

And see, note that back propagation stops at the input of discriminator because there is a discriminator training. The loss do not pass through the generator. Here,

### 00:48:18 · Speaker 8

While the losses passes through discriminator, the weights of discriminator is not changed.

### 00:48:27 · Speaker 0

Is that okay?

### 00:48:35 · Speaker 0

So is the now you can quote this up right?

### 00:48:44 · Speaker 8

And tell me this, do you need a tutorial on PyTorch? Like that's what he did in the previous class or did he only do uh theory of back drop?

### 00:48:54 · Speaker 9

Pythagoras next class is what he said

### 00:48:58 · Speaker 8

So do you need a tutorial on Python? How to do this back propagation?

### 00:49:04 · Speaker 9

Yes sir

### 00:49:04 · Speaker 7

Hello

### 00:49:04 · Speaker 2

Yes sir

### 00:49:06 · Speaker 8

Okay so you just I'll just put it right away.

### 00:49:17 · Speaker 8

Yes

### 00:49:21 · Speaker 8

So if you have any questions on this, feel free to ask me.

### 00:49:26 · Speaker 12

years of just sitting around.

### 00:49:29 · Speaker 8

Come again

### 00:49:30 · Speaker 12

Yeah, just trying to capture this actually or digest this.

### 00:49:36 · Speaker 0

You can ask me in the next class, no problem.

### 00:49:52 · Speaker 0

Okay, Sarvesh, maybe I will

### 00:49:55 · Speaker 7

this.

### 00:50:00 · Speaker 10

Yes, yes, hello.

### 00:50:02 · Speaker 8

Yeah, please go through this carefully maybe, uh, before coming to the next class and you can ask me questions. No problem. Yeah.

### 00:50:12 · Speaker 10

So so this uh Z one to Z M that we are using which are the first random variable. So are these fixed or they could change between the iterations like

### 00:50:15 · Speaker 8

initial

### 00:50:23 · Speaker 10

um

### 00:50:24 · Speaker 8

they can they can they can they can they can change. In fact you do batch gradient descent here no you don't take m samples you take you don't take all n samples in data you take a subset of it no and do it on all possible subsets. That is one epoch of training.

### 00:50:41 · Speaker 10

Price

### 00:50:43 · Speaker 10

ओके, सो फॉर एवरी बैच वी कुड जनरेट न्यू एम एम सैंपल्स एंड देन रन इट थ्रू। दैट इज हाउ यू डू इट।

### 00:50:46 · Speaker 8

Right through

### 00:50:47 · Speaker 7

you do it. Yes.

### 00:50:48 · Speaker 8

Yes

### 00:50:49 · Speaker 10

ओके. थैंक यू.

### 00:50:53 · Speaker 7

Sachin

### 00:50:55 · Speaker 9

Sir, can you explain this discriminator training or the generator training in like intuitive way like not in the mathematical formula? What exactly is happening?

### 00:51:09 · Speaker 8

Hmm

### 00:51:11 · Speaker 8

What exactly is happening is that this generator is discriminator is What do you want to hear? Do you want to hear me saying that okay there is this Basically what's happening is discriminator is creating that lower bound and generator is trying to minimize it.

### 00:51:33 · Speaker 8

Okay. However, for this particular case of Jensen-Chanell divergence, right, because this discriminator happens to be a classifier, there is there is one other interpretation that you can give, which I will give you next class.

### 00:51:50 · Speaker 11

Okay

### 00:51:51 · Speaker 8

But I I I I I want to like I deliberately avoided that. uh simply because uh see I mean this is see this is not restrictive to this particular F divergence. Now you take any F divergence the exact same procedure holds. Do you see that?

### 00:52:11 · Speaker 9

Correct

### 00:52:12 · Speaker 8

for this particular where your denominator or the critic network happens to be a classifier, there is a there is another interpretation that one can give for this loss function. You can actually see this as classification losses. These things as classification losses. And there is a there is another classification interpretation that one can give. I'll do that in the next class. I'll start the next class with that. Okay?

### 00:52:36 · Speaker 8

So after next class I will I think the end of next week is when I will release the first assignment I can do it. The mid of next week itself I will be asking you to implement cans basically okay.

### 00:52:49 · Speaker 8

Hope this is clear. Please go through this today's content.

### 00:52:56 · Speaker 8

Hey and like one of the other comments was that somebody said that that you know we would choose quality over quantity. Right? Do you think I'm covering too much?

### 00:53:12 · Speaker 6

It's good sir. Too much is too good.

### 00:53:12 · Speaker 8

good

### 00:53:13 · Speaker 12

it's fine

### 00:53:15 · Speaker 8

No, but I'm not doing too much in my see I told you that the in my opinion, the what I do in the offline course, I do thirty percent of it in the online course.

### 00:53:16 · Speaker 12

Smart

### 00:53:17 · Speaker 6

Oil

### 00:53:28 · Speaker 8

Right and

### 00:53:29 · Speaker 6

that is the

### 00:53:30 · Speaker 6

Every other quarter there is a new L L M coming so I think covering more is good sir because otherwise even if someone feels that we are covering more but I think this is good to know sir all this.

### 00:53:31 · Speaker 8

the

### 00:53:42 · Speaker 11

Good to know

### 00:53:44 · Speaker 8

Are you are you

### 00:53:44 · Speaker 11

we can cover more but we cannot

### 00:53:48 · Speaker 9

everything.

### 00:53:50 · Speaker 8

Right, but like and also am I compromising on quality? That's the question.

### 00:53:56 · Speaker 11

No sir. No sir.

### 00:53:57 · Speaker 9

Sir

### 00:53:57 · Speaker 8

definitely not. If you feel it that way just let me know, okay? See I'm covering too little, I'm going a little slow actually, just to ensure that everybody is in the same page, no? Anyway, so she'll

### 00:53:57 · Speaker 9

डेफिनेटली नॉट. इफ यू

### 00:54:09 · Speaker 3

in this network X is the image, the input

### 00:54:14 · Speaker 3

X can be any kind of data like text, audio

### 00:54:14 · Speaker 8

can be

### 00:54:16 · Speaker 8

uh, it's it's can be any, yeah, it's can be any kind of data.

### 00:54:21 · Speaker 3

And so then do we use this again for text generation also?

### 00:54:21 · Speaker 8

certainly

### 00:54:27 · Speaker 8

generally people don't use GaNs for text generation. Okay, there is another reason for it. You ask this question next class to me, I will GaNs is not over it, okay? I will spend the half of the next class on this. I will I will give you more interpretations on this, okay? I will tell you why people typically don't use GaNs for text generation.

### 00:54:34 · Speaker 7

Okay

### 00:54:50 · Speaker 3

ओके सर

### 00:54:55 · Speaker 8

sort of noise in the background. Okay, asking

### 00:54:59 · Speaker 9

Uh sir you said you are covering a little less here. So is there some reference material if we want to go a bit deeper?

### 00:55:08 · Speaker 8

Uh see my notes, my handwritten notes, all of that has uh reading material at the end of it.

### 00:55:18 · Speaker 9

Okay, so your handwritten notes on your website, right?

### 00:55:22 · Speaker 8

I shared it with you. Did I or have I put it on the website?

### 00:55:27 · Speaker 9

I think there are some lecture videos but notes I'm not sure

### 00:55:32 · Speaker 8

lecture videos, no?

### 00:55:33 · Speaker 9

Yeah, the Google Drive Lite.

### 00:55:35 · Speaker 8

Google

### 00:55:37 · Speaker 8

They are not they are not videos they are notes only. You never have had a look at it. Please have a look at it.

### 00:55:43 · Speaker 9

ओके ओके ओके थैंक यू

### 00:55:46 · Speaker 11

But I think when you say handwritten notes, you should say class notes.

### 00:55:52 · Speaker 11

it is different.

### 00:55:54 · Speaker 8

ஓகே லெட் மீ ஷோ யூ வாட் ஐ மீன்

### 00:56:07 · Speaker 8

Please mute yourselves.

### 00:56:14 · Speaker 0

that I'll put it in my web page.

### 00:56:25 · Speaker 0

System

### 00:56:33 · Speaker 7

Okay okay yeah fine

### 00:56:36 · Speaker 8

end of this. And there are more content in in this which I'm not covering and also these things you know all of these. This is where you can go and see get more information okay.

### 00:56:44 · Speaker 9

Okay

### 00:56:47 · Speaker 9

ओके, सो दीज़ नोट्स आर फ्रॉम ऑफलाइन कोर्स और दे आर

### 00:56:51 · Speaker 8

अरे यार, आई रोट इट थ्री फोर इयर्स बैक, आई मीन जस्ट फॉर माय रेफरेंस। यू वांट माय ऑफलाइन कोर्स नोट्स? आई थिंक सो, आई मीन यू शुड आस्क सम ऑफलाइन स्टूडेंट्स। आई एम नॉट मेकिंग एनी नोट्स फॉर द ऑफलाइन क्लास, या।

### 00:56:54 · Speaker 9

my referral

### 00:57:06 · Speaker 0

Okay

### 00:57:06 · Speaker 3

Okay. So do you also have notes for ML or deep learning course?

### 00:57:08 · Speaker 0

Hello

### 00:57:12 · Speaker 8

That haven't I shared it with you? Hold on. I think I have it somewhere here. One of my students when I taught him...

### 00:57:19 · Speaker 3

Maybe you can share your email

### 00:57:21 · Speaker 8

Hold on, hold on. I will put it in the chat group right now. Hold on. Teams.

### 00:57:30 · Speaker 8

not this

### 00:57:33 · Speaker 8

somebody asked this in the offline version and I shared this. Yeah, this is, I mean this guy Prashant.

### 00:57:41 · Speaker 8

my student in the offline class. His notes were so good. I mean I generally don't do like slide based teaching. I do board work. So somebody wrote it very nicely and uh hold on post.

### 00:57:58 · Speaker 8

ML notes

### 00:58:01 · Speaker 8

This is the course that I teach in the other semester. I mean it is not I don't offer this for the online students. Only for the offline students. Are you seeing my screen?

### 00:58:13 · Speaker 4

No sir. No, you are not saying.

### 00:58:14 · Speaker 8

you know

### 00:58:16 · Speaker 8

Yeah that I put it in the teams okay. uh Yeah I put it in the teams just have a look at it. Yeah so this is the this is his notes.

### 00:58:32 · Speaker 8

Yeah, so you can have a look at it.

### 00:58:40 · Speaker 4

Can you please share this link?

### 00:58:42 · Speaker 8

I have done that.

### 00:58:43 · Speaker 4

Okay

### 00:58:47 · Speaker 8

I don't know if it will be of any use to you but because this is all my board work whatever I did in the previous board work. See what I suggest is if you want a good M L course right there are many of them. One of them is of my advisor Professor Shastri. It is there in NPTEL. It's called pattern recognition and neural networks. P R N N in NPTEL.

### 00:59:09 · Speaker 8

Okay, you can have a look at it. That's a good foundational course on ML. Okay.

### 00:59:16 · Speaker 8

Okay, I think we have

### 00:59:20 · Speaker 8

well past the time.

### 00:59:22 · Speaker 1

ओके। सर, लास्ट थिंग आई एम वेरी सॉरी। रिगार्डिंग योर डीप जेनेटिक मॉडल, ओल्ड नोट्स यू जस्ट शोड ना। इफ यू प्लीज शेयर दैट लिंक एस वेल प्लीज।

### 00:59:22 · Speaker 8

ओके सर

### 00:59:32 · Speaker 8

Which one?

### 00:59:33 · Speaker 1

you showed that you took some notes on handwritten notes DGM

### 00:59:35 · Speaker 9

some good songs

### 00:59:41 · Speaker 8

what did I show?

### 00:59:42 · Speaker 3

I mean, I mean

### 00:59:42 · Speaker 1

I mean I mean just before before the ML I mean same Google Drive I think you have

### 00:59:46 · Speaker 3

It is already shared actually if you search on the Google.

### 00:59:48 · Speaker 1

Google

### 00:59:50 · Speaker 1

Okay

### 00:59:52 · Speaker 1

Okay

### 00:59:52 · Speaker 8

last year's board work I think I have it. Have I shared that with you?

### 00:59:58 · Speaker 8

ஏடிஆர்எல் கிளாஸ் வொர்க்கிங்ஸ்.

### 00:59:59 · Speaker 7

Yeah, I think

### 01:00:01 · Speaker 9

the one that is on your website

### 01:00:03 · Speaker 8

No no no not that. There's one called ADRL class for kings.

### 01:00:04 · Speaker 7

No, not that

### 01:00:08 · Speaker 8

Let me see if that's the one.

### 01:00:12 · Speaker 8

I think one year back or

### 01:00:14 · Speaker 7

It is some 130 MB

### 01:00:20 · Speaker 7

So let me share that.

### 01:00:26 · Speaker 0

Here, copy link. Manage access.

### 01:00:33 · Speaker 0

anyone with link

### 01:00:37 · Speaker 0

Done

### 01:00:40 · Speaker 7

here

### 01:00:43 · Speaker 7

Hello

### 01:00:44 · Speaker 7

Where should I go here?

### 01:00:47 · Speaker 7

triple I stack a post. Previous

### 01:00:53 · Speaker 7

Yes

### 01:00:54 · Speaker 8

Transfer Kings

### 01:00:58 · Speaker 8

See I don't see these when I'm teaching because you know I want novelty every time. But this is the previous years working if you are interested. Do you still see my screen? No.

### 01:01:10 · Speaker 3

No sir. No sir, we don't.

### 01:01:13 · Speaker 8

Okay, let me show you.

### 01:01:26 · Speaker 8

You see it now

### 01:01:29 · Speaker 2

Yes sir

### 01:01:30 · Speaker 0

Yes

### 01:01:30 · Speaker 8

this is what I've shared with you. This is my

### 01:01:34 · Speaker 8

last year's thing. So I did very differently last time, no? I started from Gaussian mixture models, V A E's and then I went to GaNs.

### 01:01:47 · Speaker 8

then to diffusion models and so on.

### 01:01:50 · Speaker 8

If you want you can have a look at it, okay?

### 01:01:55 · Speaker 7

yourself. Thanks.

### 01:01:58 · Speaker 8

Okay, see you next week then. Bye bye. Have a nice weekend.

### 01:02:02 · Speaker 12

Thank you sir

### 01:02:03 · Speaker 10

Thank you sir

### 01:02:04 · Speaker 12

Thank you

### 01:02:05 · Speaker 3

Thank you sir

### 01:02:06 · Speaker 12

Thank you sir

### 01:02:07 · Speaker 3

Okay

### 01:02:08 · Speaker 12

Thank you sir

### 01:02:08 · Speaker 7

Thank you sir
