---
id: 1Xz9ijkMAT8
title: Lec 5a - Deep Generative Models GAN Training
url: https://www.youtube.com/watch?v=1Xz9ijkMAT8
date: '2024-11-23'
duration: 01:02:15
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 5a - Deep Generative Models GAN Training

## Transcript

### 00:00:01 · Speaker 1

of of f can okay which will get us to the the basic or the manila gann article of the gann model that generally people use so if your generator function or the f function in the f divergence happens to be of this particular form okay the corresponding divergence measure is called the f divergence sorry sorry sorry jensen channel divergence okay now in that case the

### 00:00:31 · Speaker 1

Okay

### 00:00:38 · Speaker 1

The loss function will take this particular form. Let me write that. So the cost

### 00:00:51 · Speaker 1

or the above case

### 00:01:04 · Speaker 1

The cost function

### 00:01:07 · Speaker 1

What was that recall that let us denote that with some

### 00:01:13 · Speaker 1

G of

### 00:01:15 · Speaker 1

theta comma w it's a function of theta and w what was that it was expectation of p of x right as x comes from bx minus expectation of

### 00:01:32 · Speaker 1

It's start off

### 00:01:34 · Speaker 1

It's good

### 00:01:36 · Speaker 1

as x cap comes from theta right this was our cost function in general now if you take this f right and plug it in here

### 00:01:47 · Speaker 1

See in the FGN paper right they have given the F and the corresponding F stars I will show you that so if you use that and do that for this particular case this will be equal to the expectation of

### 00:02:04 · Speaker 1

as coming from px log of

### 00:02:11 · Speaker 1

I think this is TW

### 00:02:17 · Speaker 1

Log of d w of x

### 00:02:22 · Speaker 1

I mean this

### 00:02:24 · Speaker 1

Expectation of X cap coming from P theta.

### 00:02:31 · Speaker 1

log of one minus

### 00:02:35 · Speaker 1

W of X

### 00:02:43 · Speaker 1

where dw dw x is simply the 1 by 1 plus e power minus dw of x

### 00:02:57 · Speaker 1

It is simply sigma of T w of h

### 00:03:03 · Speaker 1

So I mean if you uh maybe we will make this uh

### 00:03:09 · Speaker 1

item in the ta session and as i said please note take a note of what all to be done in the ta session and you should ask chandran to do that okay so what is to be done is that you take this f divergence and you take the corresponding f star and you plug in that f divergence here in this equation and if you simplify the algebra you will get this cost function this way

### 00:03:37 · Speaker 1

Okay, where instead of T W, you just represent another function T W, which is simply you take the T T W and put a sigmoid at the output of it, okay, which is I'll write that. So now what happens is that you have a network.

### 00:03:52 · Speaker 1

T theta of Z

### 00:03:57 · Speaker 1

that would take a VS input

### 00:04:00 · Speaker 1

Arma 0 1 and you'll get X cap

### 00:04:04 · Speaker 1

It is coming from P G D

### 00:04:08 · Speaker 1

And to have another network which would give us the lower bound lower bound

### 00:04:16 · Speaker 1

be called as the pw of x right x or x cap here sorry this should be x cap

### 00:04:24 · Speaker 1

dw of x cap so this network is simply

### 00:04:32 · Speaker 1

what we were writing as T network

### 00:04:39 · Speaker 1

small c one here

### 00:04:44 · Speaker 1

one so this is this entire thing is D and yeah

### 00:04:50 · Speaker 1

This was T and you have a sigmoid on top of it. And you get what? Because it is a sigmoid now, you get a number that is between 0 and 1. So this is only for the case where your F divergence has this particular form.

### 00:05:06 · Speaker 1

So this if you see if you if you if you can notice this is the the last function

### 00:05:22 · Speaker 1

Oh fuck

### 00:05:25 · Speaker 1

Naive GAN, isn't it? If your people have seen that, if you look at the blog post and all that, they would say that this is the loss function of a GAN. It actually comes from here that you, I mean, this is the usual M divergence, mean, minimizer, the loss function that we have. And for that, if you plug in that particular F star, I will show you that paper. If you have a paper, you will understand. I've done that in my notes also. Just have a look at it. I will share my screen.

### 00:05:55 · Speaker 1

You see my screen

### 00:06:00 · Speaker 2

Not in the house sir

### 00:06:05 · Speaker 1

You see it now

### 00:06:07 · Speaker 2

Yeah. Yes sir. Yes sir.

### 00:06:09 · Speaker 1

Okay, this is that FGN paper, right, which actually I taught so far. Now all this M divergence, et cetera. So look at this table. Now in this table, what they have done, no, they have given different divergences and the different F functions corresponding to those divergences and the corresponding T functions, optimal T functions. And for Gyan, right, which is the naive Gyan, this is what is the generator function. Okay, now they have skipped the algebra. I think I've done it in my notes or you can ask.

### 00:06:39 · Speaker 1

you can ask them to do it so now with this particular look at this now with particular divergence metric your output activation function which i just said now that on the output of the t function if you put an activation that would change it is simply expressing the t function in a different way

### 00:06:59 · Speaker 1

right so so finally this objective you know which is the objective function of a GAN that would happen under this particular f divergence so if you take a different f divergence let's say if you take the Pearson's chi squared distance uh or the different f function uh instead of GAN's f divergence a Jensen's channel divergence then you would have a different uh different loss function basically right all you have to do is just plug that in

### 00:07:29 · Speaker 1

I will show you the corresponding yeah f star also you see this no so these many divergence metrics are there no and you have the output activation function which is just the appending that you do on the t network because why should you do this output activation function it is because if you recall the t function is designed in such a way that its output comes from the domain of f star right for the corresponding active corresponding f divergence that you choose

### 00:07:59 · Speaker 1

You will have to choose your f function in such a way that it would respect domain of f star. That is why you should have another activation at the output of the dL function. That is why you have an activation. You have the corresponding conjugate function also, f star. So what you should do is once you pick an f, you get an f star, you plug in that f star and you adjust for the output activation, you get the new loss function for that f divergence.

### 00:08:26 · Speaker 1

Is that clear? So that is how you get the you get the loss function for the naive GAN. So they choose in fact somebody was asking at the beginning of the session right did they start with this math and come back? No that is not how they did. In the original GAN paper they write this loss function in a different I mean from a different motivation. I will tell you that motivation also. It is not mathematically grounded but this paper at F divergence it creates that GAN class where in

### 00:08:56 · Speaker 1

also becomes a member okay so did all of you get how we got from the uh the loss function of the f gann or rather f divergences to this particular instantiation it's simply as i said no we have defined a class a gann class from the gann class uh we got one instantiation with this f of u becoming tension chain and divergence

### 00:09:21 · Speaker 1

Uh any questions on this Yeah okay

### 00:09:26 · Speaker 3

Section

### 00:09:28 · Speaker 3

zero like in this Janshan diversion

### 00:09:32 · Speaker 1

Yeah, it is no no f of no it's not I think we corrected that no it should be in f of let me just see that f of zero is one

### 00:09:41 · Speaker 4

I think the second term should be here in uh log of u plus 1 by 2

### 00:09:49 · Speaker 1

done let me just see that did I make a mistake here

### 00:09:55 · Speaker 1

Oh that's correct

### 00:09:58 · Speaker 1

It forth won this seedling

### 00:10:01 · Speaker 3

Yeah but uh FF1 doesn't evaluate to zero with this equation doesn't evaluate to zero here

### 00:10:08 · Speaker 1

It evaluates to what that is 0 this is log 2 which is evaluate to 2 log 2 right

### 00:10:13 · Speaker 3

Yeah

### 00:10:16 · Speaker 3

Yeah

### 00:10:16 · Speaker 2

It was u plus one half

### 00:10:17 · Speaker 1

u plus one by four two

### 00:10:20 · Speaker 2

it is u plus 1 by 2 in the uh original expression so if it is u plus 1 by 2 then it will evaluate to 0

### 00:10:29 · Speaker 1

No, but there is no u plus 1 by 2 in this generator function in place. Okay, so fine I can put it u plus 1 by 2 that's also convex that will evaluate to 1 more than that case.

### 00:10:40 · Speaker 3

Yeah

### 00:10:43 · Speaker 1

Let's see if I can write it

### 00:10:48 · Speaker 1

See okay so I I'll tell you where this thing is see the the GAN's loss function that they use no it's not a proper f divergence in the sense that it is off by f divergence by that you know 2 log 2 factor

### 00:11:05 · Speaker 1

Do you understand So that's why you are getting that term

### 00:11:10 · Speaker 1

Divide that by two it become proper Jensen's and a divergence that will become uh that Gann's objective

### 00:11:17 · Speaker 1

So it is off by that uh that factor uh 2 log 2

### 00:11:22 · Speaker 1

Yeah

### 00:11:25 · Speaker 4

Sir can you please repeat why you said that we need this final activation of sigmoid This is because

### 00:11:30 · Speaker 1

Huh this is because yeah this is this is because

### 00:11:36 · Speaker 1

this is because uh the t function that we the way we define now the t function we define that what was the d function it was from uh x right the domain of x to the domain of f star

### 00:11:57 · Speaker 1

Right? So now if you choose a particular f star and f function, you have to ensure that your t function has the output that obeys domain of f star.

### 00:12:14 · Speaker 4

Okay and a sigmoid is one or is this the only one

### 00:12:18 · Speaker 1

Sigma is one for this function

### 00:12:23 · Speaker 1

For this function sigmoid is the one that you take

### 00:12:28 · Speaker 1

That's that's big ticket

### 00:12:28 · Speaker 4

So that's a fixed that's a fixed mapping or for a given function

### 00:12:31 · Speaker 1

For a given function for a for a given f function it is fixed that is why I showed you in that f f g and paper they have listed the output activation for different f values

### 00:12:42 · Speaker 4

Okay yeah

### 00:12:44 · Speaker 1

Yeah in fact it's a good point that you made

### 00:12:49 · Speaker 1

Because the the output activation for this particular f function happens to be giving you a value between 0 and 1, no, the t function in this case can be interpreted as a classifier.

### 00:13:09 · Speaker 1

you understand that see now because the d function in this case will give you a value between 0 and 1 it can be interpreted as a classifier that is why it is called a discriminator in that case

### 00:13:26 · Speaker 1

I mean, in general, it is, it's called a critique, right? I mean, it can be anything, but in this particular case, because it gives you a value between zero and one, you can call that a classifier. You can interpret that as a classifier, another interpretation that I give you. Okay.

### 00:13:46 · Speaker 1

Great. Okay, so now what we will do is the following we have promised that I will write down the

### 00:13:54 · Speaker 1

Gladiators and all that no I mean do that now

### 00:13:57 · Speaker 1

Okay, let us write the optimization problem now. So we have

### 00:14:03 · Speaker 1

He does that

### 00:14:06 · Speaker 1

and W star

### 00:14:08 · Speaker 1

So you need to

### 00:14:12 · Speaker 1

it minimize with respect to theta and you have to maximize with respect to w right uh what is that in this case it will be log of

### 00:14:24 · Speaker 1

Oh normally I have an expectation there

### 00:14:29 · Speaker 1

Can all of you mute please

### 00:14:43 · Speaker 1

from px minus

### 00:14:46 · Speaker 1

But thank you

### 00:14:49 · Speaker 1

was that log of one minus state of due

### 00:15:03 · Speaker 1

x cap as x cap is coming from e theta right this is the loss function now we know that we can approximate these using expectations using law of large numbers right so approximating

### 00:15:22 · Speaker 1

expectations

### 00:15:31 · Speaker 1

Large large numbers

### 00:15:40 · Speaker 1

are simply sample estimates

### 00:15:49 · Speaker 1

although we do that we have let me write that cost function j theta comma w this is what i'm

### 00:15:58 · Speaker 1

representing as J

### 00:16:06 · Speaker 1

the record to uh

### 00:16:11 · Speaker 1

I have n samples of data it is one by n

### 00:16:17 · Speaker 1

equal to one through n

### 00:16:20 · Speaker 1

Long

### 00:16:22 · Speaker 1

E W X I

### 00:16:26 · Speaker 1

Linus

### 00:16:29 · Speaker 1

It's like uh there's much expectation on this one

### 00:16:36 · Speaker 1

One by young

### 00:16:39 · Speaker 1

J is one through M

### 00:16:44 · Speaker 1

log of one minus d w x cap j

### 00:16:57 · Speaker 1

X one X two up to X capital N

### 00:17:03 · Speaker 1

are coming from PX which is the data

### 00:17:09 · Speaker 1

And you have

### 00:17:12 · Speaker 1

X one cap X two cap

### 00:17:17 · Speaker 1

of to x m cap are coming from p theta which are the

### 00:17:25 · Speaker 1

Output of G theta network

### 00:17:28 · Speaker 1

Oh how do you get this sample

### 00:17:34 · Speaker 1

Z1 through ZM okay from normal distribution

### 00:17:43 · Speaker 1

Boston

### 00:17:46 · Speaker 1

So

### 00:17:49 · Speaker 1

GT tough

### 00:17:53 · Speaker 1

So okay

### 00:18:07 · Speaker 1

Is it okay? So this right now, let me call this as J cap because I'm taking a sample estimate. Okay. Now this J cap, J cap.

### 00:18:18 · Speaker 1

Theta can be computed right

### 00:18:28 · Speaker 1

Any questions on this

### 00:18:31 · Speaker 1

This is pretty important this is what you are going to implement so this J cap can be implemented no

### 00:18:39 · Speaker 1

Yeah uh service

### 00:18:43 · Speaker 4

So so is there a specific reason of choosing NNM different or what like

### 00:18:48 · Speaker 1

Oh okay

### 00:18:49 · Speaker 4

Or it can be something

### 00:18:50 · Speaker 1

It's just batch processing no you that's bad size of training your discriminator and generator you can use any batch size

### 00:18:58 · Speaker 1

Okay, typically you don't take the entire data set, no? You do stochastic gradient descent where all of you know what stochastic gradient descent is and then you can then talk about it. When you do gradient descent, you don't take all data points, you just take a subset of data points and you iterate over it. So that's what one VPOC means. All of you know this, no?

### 00:19:21 · Speaker 1

Okay I have no questions on this and now JCAP can be computed and now how do you train this or training again

### 00:19:35 · Speaker 1

Practically

### 00:19:46 · Speaker 1

Don't take me wrong but I'm just take this in a lighter note

### 00:19:54 · Speaker 1

For the person who said that I'm paying this much not to learn math, I hope I'm doing some justice now by telling you how to train GANs practically also. That was... Please don't take it negatively. It's simply a...

### 00:20:11 · Speaker 1

cleaner light or not okay so now let's see finally how see how to try and again practically right so now what happens is we do it using gradient descent let me write the architecture here

### 00:20:32 · Speaker 1

The world has become too sensitive these days so you can't crack jokes

### 00:20:38 · Speaker 1

take it too seriously

### 00:20:40 · Speaker 1

I'm not talking about you in general right so if you crack jokes with your friends and spouses or children or students everybody takes it too seriously

### 00:20:53 · Speaker 4

Here are the samples of the same population

### 00:20:58 · Speaker 1

See, when I was a student, I told you most of you might be younger than me, right? I'm 35. So most of you will be maybe late 20s or early 30s. Every five years is a new generation now. My teachers used to do all kinds of things for us. They used to harass us, embarrass us, beat us, all kinds of things that we never took it seriously. But this generation, my God.

### 00:21:30 · Speaker 1

again in one of those feedback somebody wrote not your course somebody wrote that you're just doing your job you're getting paid for what you are doing so there's nothing great about you teaching

### 00:21:44 · Speaker 1

I think I realized that okay that is one way to look at this entire thing I'm doing my job which is true okay so let's not even do this let's say that he

### 00:21:58 · Speaker 1

So this is the

### 00:22:13 · Speaker 1

Yeah parents always tell us right that uh and all that imagine if children tell them that uh you just did your job which is also true we never say that quite so

### 00:22:31 · Speaker 1

that's how people do it in the west right i mean this happened by the way a a child went to court uh against their parents and the and the case was that uh that uh that he uh he put a case on their parents for having given birth to him

### 00:22:53 · Speaker 1

Without his consent

### 00:22:56 · Speaker 1

Wow

### 00:23:02 · Speaker 1

If I say

### 00:23:03 · Speaker 2

something like this my parents will slap me first

### 00:23:07 · Speaker 1

No I think if you don't mind I'll just take two minutes on something that one of my senior colleagues from IIT Delhi told me it's a story which which he told

### 00:23:18 · Speaker 2

Simply share sir, simply share

### 00:23:20 · Speaker 1

So he said that it have see I have so many stories and to say outside of this class the problem is that you know I It's not my job to tell you stories. It's my job to teach you to gas Unfortunately, anyway, so here is how I was having a conversation with one of my very senior colleagues from IIT Delhi He also got a you know some highest national award for sciences professor Bream Singh very prolific senior man is already 65 then when I was there I was a 25 years old kid

### 00:23:50 · Speaker 1

when I joined as a faculty then 26 27 years I was talking to him and he narrated a nice incident very funny incident to me he said he has a collaborator uh from some university in Canada he's an Indian guy Punjabi guy okay now what had happened is this professor in Canada he had gone to university for work and like that professor's son who was 10 12 years old

### 00:24:20 · Speaker 1

He was left in home with his grandfather grandchildren sorry grandparents who is this professor's father and mother okay parents now this grandfather scolded that Buddha okay did something and this grandchild who was born and brought up in Canada he lodged a complaint against his own grandfather and in those countries you know my own sister stays in Sweden and it is it is a true thing

### 00:24:50 · Speaker 1

that if a child goes to police and complains against their parents, the children is just taken away. Okay. Parents are penalized under law and children are taken away, put into some government looked facility. Okay. So now this professor comes back home and there is police there interrogating his parents. So what had happened and all that. So then he somehow managed and this kid has complained basically, you know, he said that my grandfather abuses me and all that. So then,

### 00:25:20 · Speaker 1

uh he this professor somehow managed so a few months later the entire family visits india okay uh for for vacation maybe my my colleague professor bhimsingh exaggerated this but the way he told me is the moment that they touched down uh india right uh this uh this professor starting uh hitting that kid in the airport itself so a few

### 00:25:50 · Speaker 1

policeman came to came to came to this professor and asked him why are you beating your child so this professor narrated that entire incident that policeman said that

### 00:26:07 · Speaker 2

It is possible sir, it is definitely possible

### 00:26:11 · Speaker 1

So, yeah, so, I mean, that's the cultural difference, no? I think, no, that is slowly peeping into our culture as well. We should be very careful with our students, very careful with our children these days. And by the way, Indian law also has that, and you cannot, I mean, if you cannot quote unquote abuse your children.

### 00:26:31 · Speaker 1

See my mother I still remember she used to she used to take these you know I don't know what it is called in English

### 00:26:43 · Speaker 1

I don't know see the thing that you that you used to uh uh place hot utensils on top of your stove no what is it called that is I don't know what is it called it's a heavy throng kind of a thing that is made in in steel uh I don't actually not even steel so she used to take that and hit me on my knuckles so and that was that was a usual thing you know I never took it offensively if I do it to my chest

### 00:27:13 · Speaker 1

I don't know maybe she'll go and complain to police

### 00:27:18 · Speaker 2

Maybe you were unaware of the

### 00:27:19 · Speaker 3

That's right

### 00:27:22 · Speaker 1

What happens

### 00:27:22 · Speaker 2

I had a geography teacher in my school days and he used to tell me that like all the students that perch who so he used to tell us to like touch your own feet and the moment we used to touch our own feet he used to smack us on our back with a wooden stick so

### 00:27:36 · Speaker 1

Oh

### 00:27:43 · Speaker 2

I mean this is very common in our generation but this G and Z it's very difficult to unscroll them

### 00:27:50 · Speaker 1

Exactly. Anyway, so that's for a different day's discussion. Let's get back to what we were doing. Okay, so what will happen is, so there is this J cap theta comma W.

### 00:28:04 · Speaker 2

Just one over n

### 00:28:08 · Speaker 2

You have a some

### 00:28:11 · Speaker 2

Oh no

### 00:28:12 · Speaker 3

So on total that's uh proper CMR dye drawn for the G data right it is changed usually drawn at

### 00:28:20 · Speaker 1

Okay

### 00:28:20 · Speaker 2

Okay I I am NOT following the diagram you you say that they are drawn for the G data of is that usually draw a different required GM right

### 00:28:30 · Speaker 4

It should be expanding not narrowing

### 00:28:32 · Speaker 1

Oh sorry sorry sorry

### 00:28:34 · Speaker 1

So because the dimensionality of z is much lesser than that of x, thank you, that's my mistake.

### 00:28:46 · Speaker 1

So typically right Z comes from

### 00:28:50 · Speaker 2

some 8, 60, 32 dimensional space, okay, when you implement. So it is, it comes from 32 dimensional Gaussian, okay. So X is, of course, X cap is in R D, where D is the

### 00:29:04 · Speaker 1

dimensionality but it's an image it is 10 so 10 000 dimensional whatever your data dimension is so this is it and then minus you have 1 over m

### 00:29:19 · Speaker 2

of one minus is it log always forget that it is log of one minus that okay

### 00:29:32 · Speaker 2

See I could have actually written this down and started

### 00:29:34 · Speaker 1

a GAN discussing GAN with this I don't like that narrative at all because I don't understand where this last function came suddenly right it just appeared out of blue and why should this work and so on I I would I was never convinced I think this is a more principal way of doing it okay now how do we try in that so now we we need theta t plus one so let us look at the

### 00:29:57 · Speaker 1

I'll use different colors this is for the let's try in generator training

### 00:30:11 · Speaker 1

Okay, for generator training what you should do is that you should write theta t plus 1 is equal to theta t minus the gradient of J cap

### 00:30:26 · Speaker 1

Okay evaluated at theta p

### 00:30:37 · Speaker 1

W T

### 00:30:40 · Speaker 1

This with respect to theta

### 00:30:49 · Speaker 1

So that is just uh

### 00:30:54 · Speaker 1

You can use your favorite optimizer by the way. I mean I am simply writing a this thing stochastic gradient descent you can use Adam or RMS prop like is backprop I mean this thing gradient descent with momentum whatever it doesn't matter. So so now you get this now how do you do that that's you look at the gradient of JCAP

### 00:31:21 · Speaker 1

It is put to T da

### 00:31:24 · Speaker 1

is simply look when observe that the first term right here this term is scratch it out

### 00:31:38 · Speaker 1

term is independent of theta right it's so the gradient becomes zero so the gradient is simply the gradient of

### 00:31:49 · Speaker 1

So negative one minus seven

### 00:31:53 · Speaker 1

j equal to one through m log of one minus dw

### 00:32:01 · Speaker 1

Scuba

### 00:32:02 · Speaker 1

j now uh the way i have written no the dependence of theta is not accurate but observe that x cap j okay maybe i'll write it explicitly so that it will become easier for you this is

### 00:32:18 · Speaker 1

EWF what is this? This is T theta Z

### 00:32:25 · Speaker 1

So the dependence on theta is uh is apparent so this is

### 00:32:30 · Speaker 1

XJ cup it's okay so now how do you do that so uh first you do a

### 00:32:38 · Speaker 1

Let's write down the forward pass using green. So you take this do one forward pass through g theta so you get

### 00:32:48 · Speaker 1

xj or g theta of zj okay okay then xi xj cap and pass this

### 00:33:00 · Speaker 1

xj cap through dw x i will not write x here because it can take both x or x cap then what do you get the output what you get here is dw of xj cap okay once you get this uh which is okay i will write that as

### 00:33:30 · Speaker 1

is also DW of

### 00:33:33 · Speaker 1

check app okay then you have this dw of exact app right which is this this term so you can compute the log of it right once you compute the log of it you compute i will write the gradients in in blue so you compute the gradient of this

### 00:33:52 · Speaker 1

Logger

### 00:33:54 · Speaker 1

One minus DW of XJ cap.

### 00:33:59 · Speaker 1

and then back propagate that all the way through this it comes like this the gradient and goes all the way through the input so this is which

### 00:34:11 · Speaker 1

W fixed

### 00:34:16 · Speaker 1

okay so now to do one backward pass through the generator what you have to do is first do a forward pass through the generator get xj cap take that xj cap so this is

### 00:34:34 · Speaker 1

Says

### 00:34:54 · Speaker 1

I think the timing of the tutorial was perfect. So the backdrop was had taught precisely before I wanted to do this. That was the intention. Okay. I hope this is clear. Any self-explanatory? Any questions on this?

### 00:35:25 · Speaker 1

Does anyone have any questions?

### 00:35:34 · Speaker 1

Hello am I audible

### 00:35:39 · Speaker 4

Yes yes yes

### 00:35:39 · Speaker 2

Is that your name again

### 00:35:40 · Speaker 1

Yeah okay uh is this clear it should be pretty clear no

### 00:35:46 · Speaker 1

Okay, now let us do the, this is generator training, okay? Let us do the same thing for similar thing for discriminator training. I don't want to clutter it with this. I will write another.

### 00:35:59 · Speaker 1

So can we extend the class by 10 minutes? Like because I want to finish this today.

### 00:36:07 · Speaker 1

Society discriminator training

### 00:36:13 · Speaker 1

Pretty discreet about it I reckon

### 00:36:30 · Speaker 1

And we'll do the same thing here

### 00:36:33 · Speaker 1

Sister

### 00:36:39 · Speaker 1

code pass and use some other colors

### 00:36:44 · Speaker 1

Which colours

### 00:36:54 · Speaker 1

See some someone's suggestions on using different color was really good I never thought about this

### 00:37:02 · Speaker 1

It will add one other dimension to

### 00:37:06 · Speaker 1

notes okay power up

### 00:37:09 · Speaker 1

Whoever suggested thank you so this uh is how the network is

### 00:37:26 · Speaker 1

I Barbizonia

### 00:37:43 · Speaker 1

Okay that's in my category

### 00:37:47 · Speaker 1

We have this C1 up to CM sample from N01 and we have this G theta of Z network and the output is X.

### 00:38:08 · Speaker 1

have let us

### 00:38:12 · Speaker 1

What did I write here? I wrote this X1 cap to X1 XI cap.

### 00:38:27 · Speaker 1

Okay sub-gaps and then you have the critique of the discriminant of network

### 00:38:36 · Speaker 1

We know that this network can take x or x cap both as input. Okay. So in this case, what did we do? We only took x cap through the DW network because we only wanted to compute the second term, correct? Here we will see that we have to take, okay. So maybe I will make it concrete. Why x here? We only take x cap here as input, correct? In the discriminator training, sorry, in the generator training,

### 00:39:06 · Speaker 1

uh only x cap goes for the discriminator so that is perfect okay here both of both will go and this will be a number between zero and

### 00:39:18 · Speaker 1

Point one because it has a sigma and a d output, fine now j.

### 00:39:25 · Speaker 1

theta comma w is equal to one over n

### 00:39:31 · Speaker 1

is one through n you have log of dw of xi minus one over m j from one through m

### 00:39:43 · Speaker 1

Log off

### 00:39:46 · Speaker 1

Like this

### 00:39:50 · Speaker 1

E w of g theta of c theta

### 00:39:57 · Speaker 1

Right now we will look at

### 00:40:04 · Speaker 1

signing

### 00:40:12 · Speaker 1

des critic

### 00:40:17 · Speaker 1

or the discriminator in the case of this particular F divergence. So it will be so you don't have to write W O T plus one

### 00:40:28 · Speaker 1

This is w t minus some beta times the gradient of same loss function with respect to the theta that you have taken at the tth instant and w that you have taken at the tth instant. That's all. So this is how you've tied it. Now to find the gradient what you do is

### 00:40:52 · Speaker 1

take so note that the output of the discriminator right you need to compute

### 00:41:01 · Speaker 1

T okay gradient we are writing like this now we have to compute T

### 00:41:07 · Speaker 1

gradients of the first term which is log of T w of x i now how do you do that

### 00:41:17 · Speaker 1

Simply take some x i's okay so this is x 1 through x n okay pass it through the discriminator

### 00:41:27 · Speaker 1

You will get T W of

### 00:41:31 · Speaker 1

Okay then you compute this

### 00:41:40 · Speaker 1

And then

### 00:41:47 · Speaker 1

Back propagate this all the way to the input

### 00:41:51 · Speaker 1

Is this okay? That is for the first term

### 00:42:02 · Speaker 1

Okay, so what about second term?

### 00:42:09 · Speaker 1

For the second term we need to do the following so we need to

### 00:42:14 · Speaker 1

Do one forward pass through the generator

### 00:42:24 · Speaker 1

Uh this way we'll get

### 00:42:34 · Speaker 1

Now take all these

### 00:42:40 · Speaker 1

And passing through the discriminator. Oh there is no space here.

### 00:42:48 · Speaker 1

What do I do

### 00:43:00 · Speaker 1

Quickly call this and

### 00:43:04 · Speaker 1

Shall I write a copy of discriminator here again?

### 00:43:11 · Speaker 3

But I guess you can create a space

### 00:43:11 · Speaker 1

I guess you can create a space

### 00:43:12 · Speaker 3

Like that

### 00:43:13 · Speaker 1

Help

### 00:43:15 · Speaker 3

So in top I guess there is double sided arrow right somewhere

### 00:43:23 · Speaker 2

Perfect

### 00:43:23 · Speaker 4

I'm not going to

### 00:43:24 · Speaker 1

Yeah left of D

### 00:43:27 · Speaker 3

Out of rubber yes

### 00:43:29 · Speaker 1

Here are now here

### 00:43:32 · Speaker 4

Left left yeah you can go to space

### 00:43:38 · Speaker 1

Okay I see

### 00:43:39 · Speaker 4

Click on the hamburger icon

### 00:43:44 · Speaker 1

Pick this up

### 00:43:46 · Speaker 3

It's just expensive

### 00:43:46 · Speaker 4

It's just a pencil

### 00:43:48 · Speaker 2

Click on where you want to add space and pull it down.

### 00:43:54 · Speaker 1

Oh oh nice

### 00:43:57 · Speaker 1

I didn't know this at all

### 00:44:03 · Speaker 1

I don't want that to happen

### 00:44:19 · Speaker 1

Looks like I can't do it

### 00:44:21 · Speaker 2

It yeah it will get cuts on entire page gets down

### 00:44:30 · Speaker 1

Okay so maybe let me do one thing

### 00:44:34 · Speaker 1

This I can rewrite no problem

### 00:44:49 · Speaker 4

So there are different pencils as well

### 00:44:54 · Speaker 4

Pencils

### 00:44:56 · Speaker 4

So if you are changing same colour colour of same pencil you can use different one

### 00:45:04 · Speaker 1

How is that

### 00:45:05 · Speaker 4

So there are already there

### 00:45:07 · Speaker 1

So here that

### 00:45:09 · Speaker 1

Oh you change them to different colors I see and you can add more pencils also yeah okay great thank you very useful tips

### 00:45:21 · Speaker 1

Okay, yeah, this is okay. This is one form and pass. So now once you get this, what you can do is that you take this.

### 00:45:29 · Speaker 1

and pass through the discriminator I have to write another copy of discriminator here

### 00:45:38 · Speaker 1

It's not that big

### 00:45:42 · Speaker 1

Please don't. Okay, if I write it, what if you think that there are two discriminators? That is what I'm worried about.

### 00:45:49 · Speaker 1

There aren't two discriminators there's only one discriminator here

### 00:45:54 · Speaker 1

You get this X1 through XM and you take them and okay pass them through the discriminator

### 00:46:06 · Speaker 1

Obtain what do you get you get

### 00:46:14 · Speaker 1

It will compute

### 00:46:20 · Speaker 1

log of one minus dw of g theta zi zj

### 00:46:29 · Speaker 1

it compute this and then

### 00:46:34 · Speaker 1

I'll propagate

### 00:46:53 · Speaker 1

So now in this entire thing like, uh, I have to write that here. See, the entire thing here.

### 00:47:05 · Speaker 1

W is kept

### 00:47:13 · Speaker 1

Okay so here

### 00:47:17 · Speaker 1

Theta is fixed

### 00:47:24 · Speaker 1

Is this clear? How do you try and discriminate? The discriminator has two terms, right? I mean, both the terms in the loss depends on discriminator because you have dw both here. So for the second term, it's simple. You just take samples from x1 through xn, pass it through that. You get this, then compute log of dwxi, take the gradient, backpropagate, that's all. To get the second term, you start from z1 to zm, pass it through the fixed generator, you get x1,

### 00:47:54 · Speaker 1

cap through xm cap take those samples pass them to the discriminator and compute this log of 1 minus dw g theta z j and then back propagate that loss

### 00:48:07 · Speaker 1

And see note that backpropagation stops at the input of discriminator because there's a discriminator training. The loss do not pass through the generator. Here.

### 00:48:18 · Speaker 1

While the losses pass through the discriminator, the weights of the discriminator is not changed.

### 00:48:27 · Speaker 1

He said okay

### 00:48:35 · Speaker 1

So is the now you can code this up right

### 00:48:44 · Speaker 1

Tell me this do you need a tutorial on PyTorch like that's what he did in the previous class or did he only do a theory of backdrop?

### 00:48:54 · Speaker 3

The next class is what he said

### 00:48:58 · Speaker 1

Ah so do you need a tutorial on PyTorch how to do this backpropagation

### 00:49:04 · Speaker 4

Yes sir

### 00:49:06 · Speaker 1

Okay so you know that's I'll just put it right away

### 00:49:17 · Speaker 1

Yes

### 00:49:21 · Speaker 1

If you have any questions on this feel free to ask me

### 00:49:26 · Speaker 2

You guys are just playing games I don't know

### 00:49:31 · Speaker 2

just trying to capture this effectively or digest this

### 00:49:36 · Speaker 1

You can ask me in the next class no problem

### 00:49:52 · Speaker 1

Okay uh sorry maybe I will uh make this

### 00:50:00 · Speaker 4

Yeah this is Hello

### 00:50:02 · Speaker 1

Yeah, please go through this carefully maybe before coming to the next panel you can ask me questions no problem yeah

### 00:50:12 · Speaker 4

Yes, sir. So this Z1 to Zn that we are using, which are the first random variable. So are these fixed or they could change between the iterations?

### 00:50:24 · Speaker 1

And they can they can they can they can they can change. In fact, you do batch gradient descent here. You don't take m samples. You take you don't take all n samples in data. You take a subset of it and do it on all possible subsets. That is one epoch of gradient descent.

### 00:50:43 · Speaker 3

Okay so for every batch we could generate a new M samples and then run it through.

### 00:50:47 · Speaker 1

That is how you do it yes

### 00:50:53 · Speaker 1

13

### 00:50:55 · Speaker 3

Sir can you explain this discriminator training or the generator training in like intuitive way like not in the mathematical formula what exactly is happening

### 00:51:09 · Speaker 1

Um

### 00:51:11 · Speaker 1

What exactly is happening is that this generator this discriminator is

### 00:51:19 · Speaker 1

What do you want to hear? Do you want to hear me saying that okay there is this basically what's happening is discriminant is creating that lower bound and generator is trying to minimize it

### 00:51:33 · Speaker 1

Okay, however, for this particular case of Jensen channel divergence rate, because this discriminator happens to be a classifier, there is one other interpretation that you can give, which I will give you next class.

### 00:51:51 · Speaker 1

But I want to like, I deliberately avoided that simply because see, I mean, this is, see, this is not restrictive to this particular F divergence. Now you take any F divergence, the exact same procedure holds. Do you see that?

### 00:52:11 · Speaker 3

Correct

### 00:52:12 · Speaker 1

For this particular where your denominator or the critic that happens to be a classifier, there is a there is another interpretation that one can give for this loss function. You can actually see this as classification losses. These things as classification losses. And there is a there is another classification interpretation that one can give. I'll do that in the next class. I'll start the next class with that. Okay.

### 00:52:36 · Speaker 1

So after next class I will again the end of next week is when I will release the bus assignment I can do it the mid of next week itself I will be asking you to implement the plans basically okay

### 00:52:49 · Speaker 1

this is clear please go through this uh today's content

### 00:52:56 · Speaker 1

Hey and uh like one of the other comments was that somebody said that uh uh that you know we would choose uh a quality over quantity right uh do you think i'm covering too much

### 00:53:12 · Speaker 1

And it goes

### 00:53:12 · Speaker 2

It's good sir too much of those

### 00:53:13 · Speaker 1

No but I'm not doing too much in my see I don't like the the in my opinion the what I do in the offline course I do 30 percent of it in the online course

### 00:53:17 · Speaker 2

Yeah

### 00:53:28 · Speaker 1

8000

### 00:53:29 · Speaker 2

every every other quarter there is a new LLM coming so I think covering more is good sir because otherwise even if

### 00:53:42 · Speaker 2

This is good to know

### 00:53:44 · Speaker 1

Are you asking them

### 00:53:44 · Speaker 2

I can cover more but we cannot that's everything

### 00:53:50 · Speaker 1

Right but like and also am I compromising on quality and that's the question

### 00:53:56 · Speaker 4

No sir no sir

### 00:53:57 · Speaker 2

Definitely not

### 00:53:57 · Speaker 1

definitely if you feel it that way just let me know okay see i'm covering too little i'm going a little slow actually just to ensure that everybody is in the same page anyway so she'll

### 00:54:09 · Speaker 2

So in this network X is the image the input

### 00:54:14 · Speaker 2

Or X can be any kind of data like text or numbers

### 00:54:14 · Speaker 1

X can be any kind of data like yeah X can be any kind of data

### 00:54:21 · Speaker 2

And so then do we use this again for text generation also?

### 00:54:26 · Speaker 1

uh generally people don't use cans for text generation okay there is another reason for it you asked this question next class to me i will cans is not over it okay i will spend the half of the next class on this i will i will give you more interpretations on this okay i will tell you why people typically don't use cans for text generation

### 00:54:55 · Speaker 1

A lot of noise in the background huh Okay I think

### 00:54:59 · Speaker 4

Sir you said you are covering a little less here so is there some reference material if we want to go a bit deeper

### 00:55:09 · Speaker 1

uh see my notes my handwritten notes all of that has uh reading material at the end of it

### 00:55:18 · Speaker 4

Okay so your handwritten notes the on your website right

### 00:55:22 · Speaker 1

I shared it with you did I or have I put it on the website

### 00:55:27 · Speaker 4

Uh I think there are some lecture uh videos uh but notes I'm not sure

### 00:55:32 · Speaker 1

pictures videos no

### 00:55:33 · Speaker 4

Yeah

### 00:55:35 · Speaker 1

The Google Drive

### 00:55:35 · Speaker 4

The Google Drive link

### 00:55:37 · Speaker 1

they're not they're not videos they're notes only you never have had a look at it please have a look at it

### 00:55:43 · Speaker 4

Okay okay okay thank you

### 00:55:46 · Speaker 2

But I think when you say handwritten notes you mean these class notes

### 00:55:52 · Speaker 2

Or it it is different

### 00:55:54 · Speaker 1

Okay let me show you what I mean

### 00:56:07 · Speaker 1

Please mute yourselves

### 00:56:14 · Speaker 1

I'll put it in my web page

### 00:56:25 · Speaker 1

Interesting

### 00:56:33 · Speaker 4

Okay okay yeah fine

### 00:56:36 · Speaker 1

to the end of this and there are more content in in this which i'm not covering and also these things you know all of these this is where you can go and see get all information okay

### 00:56:47 · Speaker 4

Okay so these notes are from offline course or they're

### 00:56:51 · Speaker 1

Hey R, I wrote it three four years back I mean just for my reference

### 00:56:54 · Speaker 4

Okay

### 00:56:56 · Speaker 1

You want my offline course notes I think something you should ask some offline students I'm not making any notes for the offline class yeah

### 00:57:06 · Speaker 4

Okay so do you also have

### 00:57:08 · Speaker 2

Do you also have notes for ML or deep learning course

### 00:57:12 · Speaker 1

That haven't I shared the shared it with you hold on I think I have it somewhere in one of my students when I called

### 00:57:19 · Speaker 4

I really can't say oh yeah

### 00:57:20 · Speaker 2

or email

### 00:57:21 · Speaker 1

Hold on hold on I will put it in the chat group right now hold on photos teams

### 00:57:30 · Speaker 1

Isn't this

### 00:57:33 · Speaker 1

Somebody asked this in the offline version and I shared this yeah this is I mean this guy Prashant

### 00:57:41 · Speaker 1

My student in the offline class, his notes were so good. I mean, I generally don't do like slide based teaching. I do board work. So somebody wrote it very nicely and post.

### 00:57:59 · Speaker 1

Uh ML notes

### 00:58:01 · Speaker 1

This is the course that I teach in the other semester. I mean, it is not, I don't offer this for the online students, only for the offline students. Are you seeing my screen?

### 00:58:14 · Speaker 2

No

### 00:58:16 · Speaker 1

Yeah that I put it in the teams okay

### 00:58:21 · Speaker 1

yeah i put it in the teams just have a look at it yeah so this is the this is this notes

### 00:58:32 · Speaker 1

So you can have a look at it

### 00:58:42 · Speaker 1

I have done that

### 00:58:47 · Speaker 1

I don't know if it will be of any use to you, but anyway, because this is all my board work, whatever I did in the previous board work. See, what I suggest is if you want a good ML course, right, there are many of them. One of them is of my advisor, Professor Shastri. It is there in NPTEL. It's called Pattern Recognition and Neural Networks, PRNN, in NPTEL. Okay, you can have a look at it. That's a good foundational course on ML. Okay.

### 00:59:16 · Speaker 1

Okay I think we have to uh

### 00:59:20 · Speaker 1

Well past the time

### 00:59:22 · Speaker 4

Okay sir, last thing I'm very sorry regarding your deep genetic model old notes you just showed now if you please share that link as well please

### 00:59:22 · Speaker 1

Okay centre

### 00:59:33 · Speaker 4

Uh you showed that uh you took some of the notes on handwritten notes DGM

### 00:59:41 · Speaker 1

Uh what did I show you

### 00:59:42 · Speaker 4

I mean I mean just before before the email I mean same uh Google Drive I think you have

### 00:59:46 · Speaker 2

It is already shared actually if you search on the Google

### 00:59:52 · Speaker 4

Yeah

### 00:59:52 · Speaker 1

I think last year's board work I think I have it. Have I shared that with you? ADRL classwork.

### 01:00:01 · Speaker 2

So the one that is on your website

### 01:00:03 · Speaker 1

No no no not that there's one called ADRL class for kings let me see if that's the one

### 01:00:12 · Speaker 1

I think one year back was yeah this is some 130 MB

### 01:00:20 · Speaker 1

Let me share that

### 01:00:26 · Speaker 1

Here copy link manage access

### 01:00:33 · Speaker 1

Uh anyone with link

### 01:00:40 · Speaker 1

Here

### 01:00:44 · Speaker 1

Where should I go here

### 01:00:47 · Speaker 1

I'm not a good like hacker post

### 01:00:51 · Speaker 1

previous

### 01:00:53 · Speaker 1

Here's class workings

### 01:00:58 · Speaker 1

See I don't see these when I'm teaching because I want novelty every time. But this is the previous year's working if you are interested. Do you still see my screen? No.

### 01:01:11 · Speaker 2

Not sure about it

### 01:01:13 · Speaker 1

Okay let me show you

### 01:01:26 · Speaker 1

You see it now?

### 01:01:30 · Speaker 1

Yeah this is what I've shared with you this is my

### 01:01:34 · Speaker 1

last year's thing so I did very differently last time now I started from Gaussian mixture models VAEs and then I went to GANs

### 01:01:47 · Speaker 1

then to diffusion models and so on okay

### 01:01:50 · Speaker 1

If you want you can have a look at it okay

### 01:01:55 · Speaker 4

Cheers

### 01:01:58 · Speaker 1

Okay, I'll see you next week then bye bye have a nice weekend

### 01:02:02 · Speaker 4

Thank you

### 01:02:03 · Speaker 3

Yeah thank you sir

### 01:02:04 · Speaker 4

Thank you

### 01:02:05 · Speaker 2

I guess so

### 01:02:08 · Speaker 4

Thank you sir
