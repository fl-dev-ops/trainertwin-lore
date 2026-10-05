---
id: CL0wlAkLx6Y
title: Deep Generative Models Tutorials CNNs
date: '2024-11-23'
url: https://www.youtube.com/watch?v=CL0wlAkLx6Y
description: ''
author: prathoshap5226
duration: 01:08:19
model: saaras:v3
transcript: true
---

# Deep Generative Models Tutorials CNNs

## Transcript

### 00:00:02 · Speaker 2

Chandan Chandan two things. uh Can we clarify some questions on the assignment or at the last we can discuss because regarding the implement

### 00:00:02 · Speaker 5

E

### 00:00:13 · Speaker 5

see assignments. See, let me be very frank with you, I haven't even read the assignments.

### 00:00:20 · Speaker 2

but we have some yeah clarify or offline shall we send a note or

### 00:00:20 · Speaker 5

But we have some

### 00:00:26 · Speaker 5

Yeah, yeah, you can send me a request. I'll look into it and then rectify it. Sorry, it's like sometimes, no, we we read things on need basis. So only I should be reading assignment during evaluation, right? So I thought of reading at that time. So I'm as lazy as you all. So. Okay. Okay, then then we will post all the questions to you. You just you just send me those questions on Teams. I'll see to it that I reply. Okay. Yeah. So, so what is

### 00:00:43 · Speaker 2

Okay. Okay, then then we will post all the questions to you. You just

### 00:00:51 · Speaker 2

Okay, Thank you

### 00:00:56 · Speaker 5

today's date is twenty fifth. So twenty five, twenty fifth.

### 00:01:01 · Speaker 5

September 2024. Okay.

### 00:01:06 · Speaker 5

So I presume that at least my handwriting is

### 00:01:10 · Speaker 5

readable. Okay. So now I'll assume that you know, you know the basic ideas of by torch, okay? What do I mean by that? You know how do you create a simple

### 00:01:24 · Speaker 5

MLP network use

### 00:01:29 · Speaker 5

some

### 00:01:29 · Speaker 6

is GD or Adam

### 00:01:33 · Speaker 6

Okay

### 00:01:35 · Speaker 6

and then use C C E loss.

### 00:01:40 · Speaker 6

and then you can back propagate.

### 00:01:44 · Speaker 6

back prop and then get accuracy and save model

### 00:01:53 · Speaker 6

Can I assume that you know these things?

### 00:02:00 · Speaker 2

The only question Chandan here is this G D versus the Adam. So everywhere it is showing in the papers or everywhere we are seeing it is like Adam. So is there any specific reasons nowadays everybody is going to Adam or...

### 00:02:17 · Speaker 2

Optimizer

### 00:02:18 · Speaker 5

See, uh, see, Adam is SGD, there is an idea called as momentum.

### 00:02:25 · Speaker 5

Okay. See, if we go into that, that is totally a different trajectory altogether, but you can think of it like it's a next version of SGD.

### 00:02:35 · Speaker 5

SGD you know right? gradient descent. The idea of gradient descent is clear. Yes yes yes yes.

### 00:02:38 · Speaker 2

Yes, yes, yes, yes, yes.

### 00:02:41 · Speaker 5

Okay. So you can just think of it like the next version of SGD which is the which you have used. That is Adam. There is something that has new that has come that is Adam W. People are very much skeptical about its working. I haven't seen anybody using it per se.

### 00:03:00 · Speaker 5

SGD and Adam are the ones that people will use. Now, sometimes when the network is quite deep, okay, what they will use, they use SGD when the when there is, okay, now what do you mean by deep? How do you quantify it? It's like, what do you call, day-to-day terms. So if it is quite deep, for example, it has twenty layers, twenty-five layers, something like that, you use SGD or sometimes even they use some of the problems SGD gives

### 00:03:30 · Speaker 5

better answers than better predictive accuracies or better performance on whatever task that you are doing compared to Adam. So these are all very heuristic. There is no one thing to say that okay this is the what do you call silver bullet or what do you call the magic wand. You just wave it up things will work there is nothing like that. Okay. Okay. You should try it up with multiple things. So I assume that you are comfortable with these basics.

### 00:03:53 · Speaker 2

Okay, Thank you

### 00:04:00 · Speaker 5

things

### 00:04:01 · Speaker 2

Yeah, yeah. Okay. May not be everybody. Yeah, you can go ahead. I just had a question since you asked. Sure, sure. Yeah.

### 00:04:02 · Speaker 5

Okay. May not be

### 00:04:08 · Speaker 5

Sure, sure. Okay. Now everybody's clear with these topics? Anybody has any queries on these topics?

### 00:04:14 · Speaker 6

specifically

### 00:04:24 · Speaker 7

What is CC loss?

### 00:04:24 · Speaker 6

C loss

### 00:04:26 · Speaker 6

categorical cross entropy loss

### 00:04:28 · Speaker 7

Okay

### 00:04:30 · Speaker 6

Okay

### 00:04:34 · Speaker 6

So now

### 00:04:35 · Speaker 5

Uh

### 00:04:37 · Speaker 5

Let's take this data set which is

### 00:04:41 · Speaker 5

amnest. Now amnest is the at least a very simple toy data set that everybody will take so to get anything, okay? It's this those the simplest data set that you can have. Now what is this amnest? Now it is the why that you have. Okay, see, sometimes no the notations that I write and sometimes the notations that sir writes may be different. Okay, if you don't understand any notation, please stop me then and there and let me know.

### 00:05:11 · Speaker 5

okay, the y that we have is from zero to nine. okay, these are the y's that you take and then the x that you have, no? x belongs to our twenty eight cross twenty eight.

### 00:05:28 · Speaker 5

Okay, so it's a matrix, so it's a matrix, so all x that you have, it's a matrix of

### 00:05:37 · Speaker 5

twenty eight cross twenty eight. Okay, you have twenty eight here and then you have

### 00:05:42 · Speaker 5

Twenty Eight

### 00:05:44 · Speaker 1

And then why can't you use my notations?

### 00:05:47 · Speaker 5

Sorry

### 00:05:50 · Speaker 5

ಸರಿ ಓಕೆ

### 00:05:52 · Speaker 1

just just joking yeah continue.

### 00:05:54 · Speaker 5

Sir, the thing is, Sir, no, no, it's okay, please continue.

### 00:05:58 · Speaker 1

Yeah, no, no, it's okay. Please continue. No, no, please, I understand. Please continue. It's just okay.

### 00:06:02 · Speaker 5

Yes, S.H.O.

### 00:06:03 · Speaker 5

Okay

### 00:06:04 · Speaker 1

See, I just came here because, you know, I just wanted to let you know. See, I have given them the assignment, right? So it would be good if you can quickly tell them how to implement CNNs. I think this is what you have planned and also the up convolution, transpose convolution kind of layers and how do you do them. That is what you should do.

### 00:06:15 · Speaker 3

Hello

### 00:06:17 · Speaker 5

Opconvulsion

### 00:06:21 · Speaker 5

Yes, yes, yes. That is the, that is the plan for today, sir. Yes, sir. Okay. And just giving them why MLP is not a good idea for images. Now the spatial, how it moves. See, Chandan,

### 00:06:26 · Speaker 1

Okay. And just giving them

### 00:06:31 · Speaker 1

See Chandan one yeah one like you know piece of advice if I may. See try to refrain from you know covering some theory because you know most of it I would have covered in the class.

### 00:06:38 · Speaker 5

mine

### 00:06:43 · Speaker 0

Okay so

### 00:06:43 · Speaker 1

So because it's only one hour no and it's focus more on implement because previous times also what people told me is that one hour is too less and you know there's too much to cover. Straight jump straight away into implementations and codes and show them things.

### 00:06:47 · Speaker 0

Yes sir

### 00:06:49 · Speaker 0

previous times also

### 00:06:56 · Speaker 5

Yes

### 00:06:58 · Speaker 5

Sure, sure.

### 00:07:00 · Speaker 5

Sure, sure, sure, sir. Yeah. Sure.

### 00:07:03 · Speaker 1

Thanks for volunteering and yeah, enjoy.

### 00:07:05 · Speaker 5

Thank you, Thank you, Sir.

### 00:07:08 · Speaker 1

Okay, yeah, bye.

### 00:07:10 · Speaker 5

Yes, yes sir. Thank you sir.

### 00:07:13 · Speaker 5

So, let let's take a very simple case. Let's not go into this twenty eight cross twenty eight. No, let's take a very simple matrix, you know, which is of shape four cross four.

### 00:07:26 · Speaker 5

Now one advantage of okay I have taken four cross four I have taken five cross four. erase this.

### 00:07:35 · Speaker 5

So now

### 00:07:36 · Speaker 6

I'll write some numbers here

### 00:07:41 · Speaker 6

one one

### 00:07:49 · Speaker 6

Okay, this is a very crude way

### 00:07:51 · Speaker 5

telling you that this is if you consider these pixels are ones. Now this is how the nine is, okay? Now similarly you can think of in a twenty four twenty eight cross twenty eight case how this nine will be. So those pixels so which are there so the values of the pixels will be between zero and two fifty five. But the roughly the idea is this. Okay? So now if you want to classify this what you will do is you convert this now this is a four cross four thing is there, no? Now, the MLP takes a vector as an input. Okay, MLP always takes vector as an input.

### 00:08:29 · Speaker 5

सो व्हाट डू यू डू? यू कन्वर्ट दिस इंटू अ वेक्टर। नो व्हेन यू कन्वर्ट दिस इंटू अ वेक्टर, नो यू टेक अ रो बाय रो।

### 00:08:36 · Speaker 5

that is you take 0 1 1 0 0 1 1 0

### 00:08:42 · Speaker 5

zero zero one zero

### 00:08:45 · Speaker 5

zero zero zero zero. No, this will be the vector. That you will pass it through some MLP block. And then that will give you the label.

### 00:08:57 · Speaker 5

This is how it will be.

### 00:09:00 · Speaker 5

See, the problem that happened is

### 00:09:02 · Speaker 6

once you flatten things up, the spatial information is lost.

### 00:09:09 · Speaker 6

So you lose spatial information.

### 00:09:15 · Speaker 6

Okay, spatial information.

### 00:09:16 · Speaker 5

is lost. Now you somehow want to work with the structure itself, the existing structure itself.

### 00:09:24 · Speaker 5

Okay. I assume now the problem is clear why MLP is not a good idea for images.

### 00:09:31 · Speaker 5

Okay. Now it's like if you convert my face into an image, the pixels if you take like this, now why the eyes is here, why the nose is here, there is a specific reason. If you flatten things up, things are gone.

### 00:09:44 · Speaker 5

you don't get to know that that spatial information. Now that is the reason why we don't want to do this thing. Now to resolve this problem, uh they came up with this

### 00:09:55 · Speaker 5

Idea of

### 00:09:56 · Speaker 6

CNNs, okay? Which is

### 00:10:01 · Speaker 6

convolutional

### 00:10:07 · Speaker 6

Neural Networks

### 00:10:10 · Speaker 6

Okay

### 00:10:12 · Speaker 6

So now

### 00:10:14 · Speaker 6

Let's take any image

### 00:10:19 · Speaker 6

One minute

### 00:10:22 · Speaker 5

Now you have seen lots of images, right? So what do you mean by this HD? When you say HD, you mean something like one eight, sorry. You mean basically

### 00:10:33 · Speaker 5

1080 into 720, right? And then you have three channels, RGB channels. No, this is what. It is a matrix, okay? This is one second channel and then the third channel, okay? Now this is R channel, G channel, B channel. And each channel is having 1080. This is you can think of this as 1080 and this is 720. Okay?

### 00:11:03 · Speaker 5

each channel is like this is how the image is. So now. Now you want to work on this. Now how do you apply the convolutions? I'll directly step into that.

### 00:11:13 · Speaker 5

Okay. So now

### 00:11:15 · Speaker 6

Let's take, let me take a very straightforward and a simple example.

### 00:11:37 · Speaker 6

Uh, yeah.

### 00:11:42 · Speaker 6

If

### 00:11:42 · Speaker 5

someone is interested how did they come up with these ideas. Now you can look into the Linette paper. Okay. That's where things are pretty much clear. Now how did how did the idea of what do you call local receptive fields. Okay. And the idea of convolutions everything put into together and then how did they came up with the Linette architecture. Now that was the first CNN architecture. Now that came up. So now let's let me directly dive into this. Okay. So now the ideas that are there here is

### 00:12:15 · Speaker 5

idea

### 00:12:16 · Speaker 6

of

### 00:12:18 · Speaker 6

local receptive fields

### 00:12:22 · Speaker 6

local receptive fields.

### 00:12:26 · Speaker 6

and weight sharing

### 00:12:29 · Speaker 6

Okay, that is the

### 00:12:30 · Speaker 6

idea in which we work

### 00:12:33 · Speaker 5

I presume that the image is quite big that you can see the numbers clearly.

### 00:12:40 · Speaker 6

ओके

### 00:12:42 · Speaker 6

Fine. So now

### 00:12:47 · Speaker 6

I want to show you

### 00:12:47 · Speaker 5

one specific let me stop

### 00:12:49 · Speaker 6

sharing this for us.

### 00:12:51 · Speaker 6

slight moment and

### 00:12:52 · Speaker 6

then

### 00:12:54 · Speaker 6

late

### 00:12:54 · Speaker 6

Let me share you one thing from

### 00:13:00 · Speaker 6

Stanford

### 00:13:03 · Speaker 6

See and then

### 00:13:06 · Speaker 6

course

### 00:13:18 · Speaker 6

Let me share my laptop screen.

### 00:13:29 · Speaker 6

able to see the see my screen.

### 00:13:34 · Speaker 7

Hmm

### 00:13:35 · Speaker 6

Yes

### 00:13:37 · Speaker 7

Yes

### 00:13:38 · Speaker 6

Yes, okay.

### 00:13:40 · Speaker 5

Now this is the so this is a wonderful course okay

### 00:13:46 · Speaker 5

Now you just go to this. They have a very nice GIF. Now I have taken the example basically from that GIF. Now you see how the convolutions are happening. You this is the image that you have, three channels of the image. Now this filter, this is for this. This portion of filter is for this, this is this portion of filter is for this. Now this is filter one and filter two. Now these are some of the ideas that are there. Now see how the movement is happening.

### 00:14:14 · Speaker 5

shift it like this. Okay?

### 00:14:18 · Speaker 5

You see you are moving like this

### 00:14:20 · Speaker 5

I'll explain all these movements in a while.

### 00:14:25 · Speaker 5

Okay. Now this is the idea of convolutions. Now see, you're not flattening this image up. No, this is the image. No, image is nothing but a matrix for all practical purposes for us. Okay. So now you're not flattening things up until the outcome that you are getting is also a matrix. This is your output. This is your matrix. This is also a matrix. Okay. Now why is this two and all those things? Why is it three by three? Why is it such big? Why am I getting only three by three? Now all these things I'll explain, but I just want you to look at this animation. where in which they are showing this convolution process

### 00:14:58 · Speaker 6

Okay

### 00:15:00 · Speaker 4

Let me stop

### 00:15:00 · Speaker 6

sharing this. And let me share my iPad now.

### 00:15:26 · Speaker 6

So now

### 00:15:28 · Speaker 6

Let us take this.

### 00:15:33 · Speaker 6

you can see

### 00:15:34 · Speaker 5

here

### 00:15:35 · Speaker 5

Now this is one filter. So this is another filter. Now this is your input. Your input has three channels as of now. Okay? Your input has three channels and then you have taken two filters.

### 00:15:49 · Speaker 5

Okay. So now, when you have two filters, Now, there are three components of these two filters. What are these three components? Now, these three components refers to this. Now, if you had four blocks here, you would have had the fourth block here.

### 00:16:05 · Speaker 5

Okay. And the output, you can see that now this is for first filter, this is for second filter. Now how is it obtaining all those things? I'll come to. Okay. Now but remember why is this three? Now this is this this. Okay. This is for this, this is for this and this is for this.

### 00:16:23 · Speaker 5

Okay, so now what is that?

### 00:16:24 · Speaker 4

सो दिस इज, सो दिस इज फॉर आरजीबी चैनल, करेक्ट? वन फिल्टर फॉर ईच आरजीबी।

### 00:16:30 · Speaker 5

See, okay, no need to restrict for RGB. Now if you have four more,

### 00:16:35 · Speaker 5

how much ever you have. Consider that you have fourth one, you will have fourth one here, that's all. And this is for this and this will be for this, okay?

### 00:16:45 · Speaker 4

Saturday

### 00:16:46 · Speaker 5

No, it it is not dependent on RGB. For easiness sake I have taken three channels that's all.

### 00:16:52 · Speaker 5

Okay, if you have hundred channels, Okay, as an input and then you are having four filters, Okay, now you will have filter one, filter two, filter three, filter four. There will be hundred components in each of the filters. Okay, that is the idea.

### 00:17:09 · Speaker 5

Is that clear everybody? Yes. Okay. So now what are you doing is, now we have something called as the receptive field. Now see this is a three cross three block. The receptive field for this also will be three cross three.

### 00:17:09 · Speaker 4

clear?

### 00:17:10 · Speaker 4

Yes

### 00:17:23 · Speaker 5

Okay. Now this is this and this. Now this is this.

### 00:17:32 · Speaker 5

this

### 00:17:33 · Speaker 5

Okay, now what do you do? First you apply it on the leftmost thing.

### 00:17:39 · Speaker 5

First you apply it here some operation. Then you move. Okay? Then you should move. How much should I move? Do I need to move one or what do I mean by move one? Okay?

### 00:17:52 · Speaker 5

Now I start with this. Then I move one in the sense I move here. Okay.

### 00:17:59 · Speaker 5

If I move two means I start with this and then I'll move two here.

### 00:18:04 · Speaker 5

Okay, now this movement is there, no? This movement that I have is called as the

### 00:18:11 · Speaker 5

Stride

### 00:18:14 · Speaker 6

Okay

### 00:18:15 · Speaker 6

you can say that how much to move

### 00:18:22 · Speaker 7

Okay

### 00:18:23 · Speaker 6

How much to move?

### 00:18:26 · Speaker 5

Now as of now we are taking stride equals to two. That is our current assumption here. Okay? So now currently you are here let me mark the boundaries here. This is the one.

### 00:18:42 · Speaker 5

this is

### 00:18:44 · Speaker 5

the second channel. This is in the third channel. Now, you have a three cross three block here. You have a three cross three block here, you have a three cross three block here. So what you can do, you can perform an element wise multiplication, element wise addition or matrix multiplication is what you are supposed to do. These are the possible options that are there. Now but

### 00:19:08 · Speaker 5

this what we will do is we will perform an element wise multiplication and add things up. Now what do I mean by that? Let me explain you that.

### 00:19:18 · Speaker 5

So you see one here, right? And you see zero. One into zero. Zero. So now let's not worry about wherever zeros are there, either in this or here. Now only let me look at the non-zero values. Now there is a non-zero value here.

### 00:19:39 · Speaker 5

your

### 00:19:41 · Speaker 5

Deepak, these are the only non-zero values, correct?

### 00:19:46 · Speaker 5

These values are zeros. So I don't need to worry about it. This and this are zero so I don't need to worry. So these numbers are gone. Correct?

### 00:19:57 · Speaker 5

I should only worry about this, this and this.

### 00:20:00 · Speaker 5

Similarly let's come here. I'm just showing you the operation. These zeros. You don't need to worry about this. This two are gone. This two are gone. So you're only worried about the remaining three numbers. Okay you are worried about this. This and this.

### 00:20:16 · Speaker 5

If you want to zoom in, I can zoom in more.

### 00:20:19 · Speaker 5

come to the third filter. third block. this zero, this is gone. this is gone. you're only remaining with this. so basically only with two basically. this is the only number.

### 00:20:33 · Speaker 5

So it will be easy for us to look into the operations now. So now what I'll do, I'll multiply. Now what am I supposed to do? Now this is, now this is two into minus one.

### 00:20:46 · Speaker 6

Plus

### 00:20:49 · Speaker 6

one into one plus

### 00:20:52 · Speaker 6

2 into minus 1

### 00:20:57 · Speaker 6

Okay

### 00:20:58 · Speaker 6

Is it

### 00:20:59 · Speaker 5

clear the operation. Now this is a non-zero value, non-zero value, non-zero value. This, this, this, you multiply and add.

### 00:21:07 · Speaker 5

2 into minus 1

### 00:21:11 · Speaker 6

two into minus one

### 00:21:14 · Speaker 6

one into one

### 00:21:18 · Speaker 6

ओके? सिमिलरली लेट्स डू इट फॉर

### 00:21:19 · Speaker 5

meaning thing

### 00:21:21 · Speaker 5

this is two into one plus one into minus one plus two into minus one oh sorry two into minus one

### 00:21:34 · Speaker 5

for the next one. This is two into minus one. Now what is this totaling two? This is minus two plus one minus two. This is minus three.

### 00:21:50 · Speaker 5

This is minus one. Now this is minus two. Now you have got three numbers. Now what are you supposed to do with these three numbers? Add them. Now that is minus three, minus one, minus two. This will give you minus six. Now where is that minus six here? Now this is the number that you get.

### 00:22:11 · Speaker 5

Okay? When you did

### 00:22:15 · Speaker 5

this operation

### 00:22:17 · Speaker 5

in all the three channels, you got this number.

### 00:22:22 · Speaker 5

Then you did this.

### 00:22:24 · Speaker 5

on these numbers you got minus six. Then you did went two more.

### 00:22:32 · Speaker 5

you got this. Then you come down stride is to again you are here you started with here you should come two down. Okay? You start with this. Similarly you take three here and then you take three here. You get this.

### 00:22:49 · Speaker 5

so on, you can get into. So, you can look into the toggle thing that I showed you earlier. Now this is what do we call as the convolution operation.

### 00:23:00 · Speaker 5

Okay

### 00:23:02 · Speaker 5

any questions with the operation? Now if there is a bias term, you should add it. Now here bias is zero so you don't need to add it. If the bias term is one,

### 00:23:12 · Speaker 5

should do plus one finally. Okay. Yeah go ahead Satya. Yeah.

### 00:23:17 · Speaker 3

on queries like how are you deciding the filter size and number of filters?

### 00:23:22 · Speaker 5

Keep that question. Filter size, this is what filter size is. Why am I deciding this and how am I deciding number of filters is your question. Very good question. I'll answer that in some time.

### 00:23:29 · Speaker 3

MI

### 00:23:33 · Speaker 6

Right

### 00:23:37 · Speaker 6

Okay

### 00:23:37 · Speaker 5

Yeah

### 00:23:40 · Speaker 5

Sanchit

### 00:23:41 · Speaker 2

you mentioned one property, right? Like when we started discussing about this this topic.

### 00:23:47 · Speaker 4

या लोकल रिसेप्टिव फील्ड

### 00:23:48 · Speaker 4

So I could not understand this like this aspect completely here so what we are trying to say

### 00:23:56 · Speaker 5

See, is this local? As of now, for this, the receptive field is this.

### 00:24:01 · Speaker 4

Okay

### 00:24:03 · Speaker 5

okay? And what why do I say weight sharing? Now the same set of weights is shared across the whole thing.

### 00:24:10 · Speaker 4

Got it. Got it.

### 00:24:12 · Speaker 5

Okay?

### 00:24:13 · Speaker 4

Got it

### 00:24:15 · Speaker 5

Now look into that Linnet paper, okay? Linnet paper.

### 00:24:20 · Speaker 5

So, yeah, there are many biological aspects which might not be of interest. Now because they will say that how convolution networks are inspired by brain's structure. Okay, brain's so there is image processing that initially happens, you know, that V one, V G and something something is there. I don't remember them. Okay, but there are six layers that are there from which it got inspired. Now they will tell that.

### 00:24:46 · Speaker 5

Okay, so now, now

### 00:24:46 · Speaker 6

Okay

### 00:24:51 · Speaker 5

And you have here, you this is this you are I'm showing in a different color, right? This is what do we call as padding.

### 00:24:59 · Speaker 5

Okay. Why is this padding needed is, now sometimes you want your output to be of specific size. Okay. Now in that case you need to add some extra things. I'll show you with a formula. Now, now we decide this we described what is a stride now. And then the next thing that we have is

### 00:25:23 · Speaker 5

Colonel Sai

### 00:25:24 · Speaker 6

is

### 00:25:26 · Speaker 6

Okay, or it is called as the

### 00:25:30 · Speaker 6

filter size

### 00:25:32 · Speaker 6

Now this is three cross three in our case.

### 00:25:37 · Speaker 6

When I say three cross three, this

### 00:25:42 · Speaker 6

Okay

### 00:25:43 · Speaker 6

So now then we have

### 00:25:47 · Speaker 6

number of filters

### 00:25:51 · Speaker 5

number of filters, we had two filters. Okay, in this case, this is filter one, this is filter two.

### 00:25:59 · Speaker 5

filter one, filter two.

### 00:26:02 · Speaker 6

and then number of input channels

### 00:26:07 · Speaker 6

number of input channels.

### 00:26:12 · Speaker 6

I had three

### 00:26:15 · Speaker 6

number of output channels

### 00:26:20 · Speaker 6

I have it two. Why did I get it two? I'll give you the answer.

### 00:26:26 · Speaker 6

Okay?

### 00:26:35 · Speaker 6

they will be same.

### 00:26:40 · Speaker 6

So now

### 00:26:41 · Speaker 5

give you a very important formula. You should remember this formula. Now this is where most of you will do mistakes when coding CNNs. Okay?

### 00:26:52 · Speaker 5

Let the

### 00:26:55 · Speaker 5

input B H I into W I into D I. Okay? Now this consider before padding.

### 00:27:07 · Speaker 5

consider

### 00:27:09 · Speaker 5

Before padding

### 00:27:12 · Speaker 5

ओके। व्हाट इज दैट वी हैव फाइव इंटू फाइव इंटू थ्री इन आवर करंट एग्जांपल।

### 00:27:19 · Speaker 5

Okay. So now

### 00:27:22 · Speaker 5

number of filters

### 00:27:25 · Speaker 5

given by K

### 00:27:29 · Speaker 5

then

### 00:27:31 · Speaker 5

in our case number of filters we have is two.

### 00:27:35 · Speaker 5

filter size is given by F. In our case it is three, three cross three. It will always be of square shape, so it will we will just write three.

### 00:27:46 · Speaker 5

Stride

### 00:27:49 · Speaker 5

represent by S. Currently we have two.

### 00:27:53 · Speaker 5

padding

### 00:27:55 · Speaker 5

is P is one. Now why am I saying one? Now because in all the direction you are adding one one element. If you have two, you will get one more here. If you have three, you will get one more here. Okay? How many layers of things you are adding?

### 00:28:11 · Speaker 5

that is padding, we have one.

### 00:28:14 · Speaker 5

Now then, then, if this is what you have,

### 00:28:19 · Speaker 5

then

### 00:28:21 · Speaker 5

output will be

### 00:28:25 · Speaker 5

H O into W O into D O. Now what is this H O? H O will be H I minus F plus two P.

### 00:28:39 · Speaker 5

by S plus one

### 00:28:43 · Speaker 5

Okay. Now what is W O? W O will be W I minus F plus two P divide by S plus one.

### 00:28:57 · Speaker 5

Now what is this d o? d o equals to k. Now let's substitute this value. What is h i? h i is five.

### 00:29:07 · Speaker 5

minus F is three plus two into one is two

### 00:29:15 · Speaker 6

divided by S that is two plus one what is this

### 00:29:24 · Speaker 6

What is this value?

### 00:29:26 · Speaker 7

Ree

### 00:29:28 · Speaker 6

this is

### 00:29:30 · Speaker 6

Three

### 00:29:32 · Speaker 6

Similarly W will be three and D naught will be two. Is that what we got?

### 00:29:43 · Speaker 6

3 cross 3 into 2

### 00:29:48 · Speaker 6

Okay

### 00:29:49 · Speaker 5

So now I will tell you some of the intricacies of this which you should remember. Okay? Now why is this padding needed will be your first question. See sometimes we want the image to be of some specific size. At that time, okay?

### 00:30:06 · Speaker 5

सो यू कैन ऑब्टेन आइदर बाय वेरिइंग एफ, समटाइम्स वेरिइंग एफ ऑन एस यू विल नॉट बी एबल टू गेट इट। फॉर दैट यू शुड बी ऐडिंग टू पी।

### 00:30:14 · Speaker 5

should be adding a padding

### 00:30:17 · Speaker 5

Okay, otherwise you cannot get the image of that size. Now what will happen is when you create an image, no, you use, okay, sir said something called as transposed combinations, right? Now there also the same thing will pitch in. You want image to be of some specific size. For that you should give some specific numbers. Now if you want to understand those numbers, this is the formula.

### 00:30:40 · Speaker 5

You apply that convolution operation. If this is the input and these are the parameters, this will be the size of the output. So this is determined.

### 00:30:50 · Speaker 5

Now this is where most of the people do mistake. They will get confused here.

### 00:30:57 · Speaker 5

Okay, now they will not be able to get what is what.

### 00:31:03 · Speaker 5

Is this clear?

### 00:31:06 · Speaker 5

is the idea of convolution operations and the parameters of that, is it clear?

### 00:31:11 · Speaker 6

Yeah

### 00:31:13 · Speaker 5

one question. So now just yeah yeah go ahead go ahead.

### 00:31:13 · Speaker 4

वन क्वेश्चन

### 00:31:17 · Speaker 4

So this uh filter size you have chosen three right?

### 00:31:21 · Speaker 5

Yeah

### 00:31:21 · Speaker 4

Is there any specific reason for that like could I have chosen like any other size?

### 00:31:24 · Speaker 5

No, like any other

### 00:31:26 · Speaker 5

All of these are variable. You can do whatever you want to choose.

### 00:31:29 · Speaker 4

October

### 00:31:30 · Speaker 4

Okay

### 00:31:31 · Speaker 7

Okay

### 00:31:31 · Speaker 4

Okay

### 00:31:32 · Speaker 5

Okay, now, now that will raise you a question. So why on earth is this? Then I can have any number of networks, right? I can, so this is one layer. Similarly, I can have any number of layers of CNNs and any of these things. You go on varying things and you go on getting different different networks, right? And then I will say that Chandan net and you will say that Sachin net. Okay? And then Satya will say the Satya net. So on and so forth. Everybody lets go on giving each one network one name.

### 00:31:47 · Speaker 4

any of

### 00:31:52 · Speaker 4

said that

### 00:32:02 · Speaker 5

and let's let's destroy the whole of the thing. We go on with so many names. Okay, then what happened was there is something called as an imaginate competition.

### 00:32:16 · Speaker 5

Okay, now there is one data set called as ImageNet. Now wherein which there are thousand classes. From each of these classes, there will be thousand two hundred training images and hundred testing images.

### 00:32:22 · Speaker 7

from each

### 00:32:28 · Speaker 7

ஓகே

### 00:32:28 · Speaker 5

Okay. Now every year this competition will happen. Okay. So now the winners of these competitions, no, they are the what do you call the famous networks. Okay. Now that is how the famous networks like VGG, ResNet, everything came. They were the winners at different years.

### 00:32:45 · Speaker 7

and then

### 00:32:45 · Speaker 5

And then you would have heard that there is something called as S E Resnet. Okay Resnet. uh some you would have heard something called as Resnet and all those things no. No they came up because of that winning. Okay otherwise every person will go on creating his own networks no it is not that. There is there is some inherent meaning to all these things from which somehow we are not able to get it. Okay. We in the sense all of us the whole community put together.

### 00:32:51 · Speaker 7

Okay

### 00:33:06 · Speaker 4

Hmm

### 00:33:11 · Speaker 4

actually, uh, when you did this convolution, so this stride size and the output of this filter size looks like related something, right? The

### 00:33:12 · Speaker 5

Hello

### 00:33:15 · Speaker 5

try

### 00:33:22 · Speaker 4

Stride by which he will move

### 00:33:22 · Speaker 5

stride by which he has moved. No, no, no. No.

### 00:33:28 · Speaker 5

ओके, ओके, इन द सेंस, ओके, आई गॉट योर पॉइंट. व्हाट यू आर सेइंग इस, इफ द नंबर ऑफ फिल्टर साइज़ इस थ्री क्रॉस थ्री, आई कैन नॉट हैव स्ट्राइड मोर दैन थ्री.

### 00:33:35 · Speaker 4

and

### 00:33:37 · Speaker 4

Yeah, yeah, like something, there should be some combination.

### 00:33:39 · Speaker 5

Okay. Yeah yeah yeah. So you cannot see if I am starting here, I cannot have stride four which I'll get into here. Because in middle one row will be left. Okay. So those are some inbuilt ideas that you should immediately get it. That's that's a valid point, correct? Now you can have either one, zero, so sorry, it should be either one which is default, two or three.

### 00:33:44 · Speaker 4

cannot

### 00:33:47 · Speaker 4

because in

### 00:33:50 · Speaker 4

Okay

### 00:33:56 · Speaker 4

you can have

### 00:34:01 · Speaker 4

Okay

### 00:34:03 · Speaker 5

Okay. Now what should be the movement in each of the cases? Okay. And then you cannot put any random numbers here and things will not work out. I'll just give you one example. Okay. Now, Now tell me this, I have a convolutional layer here.

### 00:34:12 · Speaker 7

Hmm

### 00:34:18 · Speaker 5

So I'll not give you the details what should be the convolution layer you should give me F K P and S value. Now my input is twenty eight cross twenty eight cross three.

### 00:34:31 · Speaker 5

Okay

### 00:34:34 · Speaker 5

And then my output is twenty four cross twenty four cross sixteen. Now tell me what are the values of this F K P S?

### 00:34:45 · Speaker 5

reduce the size, you can look into it.

### 00:34:49 · Speaker 5

Now tell me what are the values that I should be giving for this

### 00:34:53 · Speaker 6

FKPS

### 00:34:56 · Speaker 6

Put it in the chat. Is there a chat?

### 00:34:56 · Speaker 7

Students

### 00:35:00 · Speaker 6

Pune

### 00:35:08 · Speaker 7

five cross five is the filter. sixteen no no just put it

### 00:35:11 · Speaker 6

No, no, just put it, just just put it there, just put put all the four values there, put it in the chat. Do a calculation and put it in the chat.

### 00:35:32 · Speaker 6

want everybody to do this calculation. Now because these kinds of calculation

### 00:35:36 · Speaker 6

where

### 00:35:37 · Speaker 6

you surely get

### 00:35:39 · Speaker 6

stuck

### 00:35:40 · Speaker 6

because you will be applying lot of

### 00:35:42 · Speaker 6

convolutions and then you should be knowing what will be the outcome of that convolution, okay?

### 00:35:54 · Speaker 6

Okay

### 00:35:57 · Speaker 6

So now how do we calculate? The idea is very simple.

### 00:36:03 · Speaker 6

Now

### 00:36:03 · Speaker 6

Hello

### 00:36:04 · Speaker 5

K is fixed

### 00:36:07 · Speaker 5

K is sixteen. Any questions on that? D not equals to K. K is fixed. Now D output is this. So K is fixed.

### 00:36:17 · Speaker 5

Okay. So then the remaining things is that what we want. So what do we know? We know H O equals H I minus F plus two P.

### 00:36:30 · Speaker 5

by S plus one. Now what is H O is twenty four equals twenty eight minus F plus two P by S plus one. Now just take a simple thing. Let's first take S is equal to one P is equal to zero. If you take this you will get F equals five. Works?

### 00:36:53 · Speaker 3

you just keep this

### 00:36:53 · Speaker 5

Now, the input image is this and the output size you want is this. Now this should be the combination of

### 00:37:02 · Speaker 5

features, this should be the combination of parameters that you should be having to get it.

### 00:37:09 · Speaker 5

Is that clear?

### 00:37:12 · Speaker 4

Can you repeat that last question?

### 00:37:15 · Speaker 5

See, uh you have you can get two equations, three unknowns are there. Okay. Now even God cannot solve it. Okay. Now I don't know, there is a there is a statement. Okay. One equation, one unknown. Any fools can solve it. Okay. One equation, two unknowns, not even God can solve it. Okay. So, so you have two equations, three unknowns, so not even God can solve it.

### 00:37:29 · Speaker 2

pools

### 00:37:44 · Speaker 5

So now

### 00:37:46 · Speaker 4

the screen is not visible.

### 00:37:47 · Speaker 5

Yes, screen is, screen is visible. Yeah, yeah, yeah, got it, got it, got it. Somehow it got

### 00:37:48 · Speaker 7

screen is

### 00:37:56 · Speaker 5

God got offended by my statement. Oh, you're saying this, I cannot do it. I can do something better.

### 00:38:04 · Speaker 6

hmm

### 00:38:04 · Speaker 6

Yeah

### 00:38:08 · Speaker 6

just give me a moment.

### 00:38:10 · Speaker 6

what happened was my internet was

### 00:38:14 · Speaker 6

Gone

### 00:38:24 · Speaker 6

So now everybody is clear with these ideas?

### 00:38:29 · Speaker 6

what you are supposed to

### 00:38:30 · Speaker 5

supposed to do now

### 00:38:34 · Speaker 4

Can you tell that equation solving again? K is fixed after that

### 00:38:39 · Speaker 5

K is fixed, okay. K is fixed. Okay. So now you cannot have what do you call weird kind of things, okay. You cannot do it, you cannot basically solve it, right? Now because you have three equations, sorry, three unknowns and two equations, you cannot solve them. So now you should fix some of the things. So now let's fix S is equal to one and P is equal to zero is my proposition and let's see whether we can get something out of it. Yes, we got something out of it, let's use it.

### 00:39:07 · Speaker 4

Yes

### 00:39:09 · Speaker 5

Okay, I'm not saying that that is the only unique solution. There can be multiple other solutions that are possible. This is the one solution that I have got. I'll just fix to it. Okay.

### 00:39:13 · Speaker 4

October

### 00:39:19 · Speaker 6

Okay

### 00:39:23 · Speaker 6

No, my

### 00:39:24 · Speaker 6

Screen is back

### 00:39:28 · Speaker 6

Oh 9 12

### 00:39:30 · Speaker 6

This is the reason sir told me don't do theory and start coding directly, okay.

### 00:39:40 · Speaker 6

Okay

### 00:39:42 · Speaker 5

So now always no when you have things fixed okay now input size is fixed so you want this to be the output size these are you can manipulate. Okay. This manipulation is clear I guess.

### 00:40:01 · Speaker 6

Any questions on these manipulations?

### 00:40:06 · Speaker 6

ओके फाइन

### 00:40:07 · Speaker 5

Now let's not waste any more time. Let's go into the coding part of this, okay? Let me stop sharing my screen. Let me go to the

### 00:40:21 · Speaker 6

coding aspects

### 00:40:48 · Speaker 6

You can see my screen.

### 00:40:51 · Speaker 6

Google

### 00:40:52 · Speaker 7

Yes. Yes.

### 00:40:53 · Speaker 6

Okay. uh Just go to collab.

### 00:41:09 · Speaker 6

Go to Google Colab

### 00:41:11 · Speaker 6

create one new notebook

### 00:41:17 · Speaker 6

I presume everybody's comfortable with Google Colab, right?

### 00:41:22 · Speaker 5

exactly similar to Jupiter notebook

### 00:41:25 · Speaker 5

and I don't need to worry about many of the things.

### 00:41:28 · Speaker 5

Now here I'll have

### 00:41:31 · Speaker 5

Hmm

### 00:41:32 · Speaker 5

DGM 24

### 00:41:36 · Speaker 6

tutorials, okay?

### 00:41:39 · Speaker 6

So now

### 00:41:41 · Speaker 6

Let me directly start doing things.

### 00:42:08 · Speaker 6

we will be explaining you this code directly.

### 00:42:14 · Speaker 6

Hey, Kumba

### 00:42:25 · Speaker 6

Now, I presume that these libraries are very much clear for you by now.

### 00:42:33 · Speaker 6

transforms are done right? Now you know what is transforms

### 00:42:39 · Speaker 6

another things normalization to tensor all those things are clear right

### 00:42:44 · Speaker 5

Can I assume them?

### 00:42:49 · Speaker 5

So can I assume the transforms are clear?

### 00:42:52 · Speaker 6

Yes

### 00:42:54 · Speaker 5

Okay. So now you are getting the train loader and the test loader, train set and test set. Now let's try to understand this thing.

### 00:43:02 · Speaker 5

Okay. Now here you're creating a simple CNN. Now first you are having a convolutional layer. Now what is this convolutional layer? Convolutional layer, now first you should say that how many input channels are you having? This is input channels. How many output channels you want? You want thirty two. Input channels, now it depends on your input, how many output channels I want thirty two. Now that means that how many filters will be there?

### 00:43:33 · Speaker 6

thirty two

### 00:43:33 · Speaker 5

I say that

### 00:43:34 · Speaker 7

output thirty two filters will be there. Correct? And then how many components will be there in each of the filter?

### 00:43:46 · Speaker 7

How many components should be there in each of the filter?

### 00:43:49 · Speaker 6

one one channel is one component

### 00:43:51 · Speaker 5

one component. Correct. Your input has only one channel, so there will be one component in each of these thirty two filters. And then each filter size you are saying that it is three. That means that it is three cross three.

### 00:44:07 · Speaker 5

ಓಕೆ

### 00:44:08 · Speaker 5

Is that clear? The first thing?

### 00:44:13 · Speaker 5

kernel size it is saying that three that means it is three cross three kernel. So now and then you are saying that padding is one. So now you take this uh image so which is one channel and then you are having thirty two filters and then each filter has one component the size of that component is three cross three. And then for the image you are had even padding is one.

### 00:44:39 · Speaker 5

Is that clear? Any queries with how is this defined?

### 00:44:45 · Speaker 5

its components and

### 00:44:49 · Speaker 5

each of these terms, is it clear? stride if you don't specify, by default stride will be one.

### 00:44:56 · Speaker 6

Is this much clear?

### 00:45:02 · Speaker 5

ಓಕೆ. ಸೊ ನಾವ್

### 00:45:04 · Speaker 0

after sir. So I have sorry to interrupt and then I have one question. We can have non square filters also right?

### 00:45:04 · Speaker 6

So I

### 00:45:08 · Speaker 5

Go ahead, Go ahead, Go ahead

### 00:45:10 · Speaker 5

We can

### 00:45:14 · Speaker 0

No madam. Here we are considering three cross three, we can have two cross three also, right?

### 00:45:15 · Speaker 5

No Madam

### 00:45:21 · Speaker 5

No no no no then the whole convolution operation will just have issues.

### 00:45:27 · Speaker 5

should explicitly define. Okay, you cannot have it I guess.

### 00:45:33 · Speaker 5

Okay. I haven't seen non-square kernels as of now. But I presume that it is not possible. The reason is because of the formula. I haven't seen that. Let me look into it and if there is anything I'll put it in the group. But as of now my

### 00:45:50 · Speaker 1

As of now my

### 00:45:52 · Speaker 1

I think we can have like non-square kernel also because for each channel the filter will apply.

### 00:46:00 · Speaker 5

See, okay, uh let's not, okay, I I as of now I don't know. If there is anything I'll put the resource in the group, okay? Let's not take the deviation towards non-square channels, non-square filters, okay?

### 00:46:07 · Speaker 2

root

### 00:46:11 · Speaker 2

field

### 00:46:13 · Speaker 5

So now this is the convolutional layer and then there are layers called as spooling layers. What does this spooling layer does?

### 00:46:13 · Speaker 2

Sure

### 00:46:25 · Speaker 6

Okay. This is

### 00:46:31 · Speaker 6

Okay

### 00:46:43 · Speaker 6

Zoom is far better. This Microsoft Teams is there, no? It doesn't allow to annotate. It doesn't allow many of the operations. Okay.

### 00:46:57 · Speaker 6

Okay. Now you see this four cross four entity, no?

### 00:47:02 · Speaker 6

You see a four cross four thing.

### 00:47:03 · Speaker 5

If I say that, perform a max pooling with two cross two block with stride two. Max pooling with two cross two filter with size with stride two. Now first you apply for this.

### 00:47:21 · Speaker 5

What do you mean by max pooling? Now out of this, find the maximum value. Six is the maximum value, you get six.

### 00:47:28 · Speaker 5

Now then you should move to because you are saying that stride is two.

### 00:47:33 · Speaker 5

Now max is eight. Then you started with here, now you should move by two, you will get it here. Max is three, then you move by two, you get max is four. Now this is max pooling. Now if you want average pooling, you can say the same thing, average pooling with two cross two filter and strike two. Now then you take the average of it. This is eleven, eleven plus two is thirteen, thirteen by four is three point two five. So on and so forth you get like this. Now either you can have a max pooling or you can have an average pooling. Okay? This is the pooling layers.

### 00:48:10 · Speaker 5

Now here I am saying that pooling layer you have a kernel size of two cross two and stride two.

### 00:48:18 · Speaker 5

Now, now tell me

### 00:48:22 · Speaker 5

if the input size is twenty eight

### 00:48:26 · Speaker 5

ओके। नाउ, टेल मी इफ द इनपुट साइज़ इज़ ट्वेंटी एट क्रॉस ट्वेंटी एट क्रॉस वन, व्हाट विल बी द आउटपुट साइज़ इन दिस केस?

### 00:48:37 · Speaker 5

If the input size is twenty eight cross twenty eight cross one, what will be the output size? Go ahead take a pen and paper and calculate, I'll also do it. Even I don't know.

### 00:48:51 · Speaker 5

now H O equals H I minus F plus two P

### 00:48:58 · Speaker 5

by S plus one. H input is twenty eight minus three plus two.

### 00:49:08 · Speaker 6

by one plus one. Now this is

### 00:49:16 · Speaker 6

Twenty Five

### 00:49:19 · Speaker 6

twenty five plus two twenty seven

### 00:49:23 · Speaker 6

will be twenty eight

### 00:49:24 · Speaker 5

cross 28 cross 32, correct?

### 00:49:30 · Speaker 5

the output will be twenty eight cross twenty eight cross thirty two correct. I also got the same thing. Now then you apply a max spooling. Now when you apply a max spooling of size two cross two so then it will be converted to fourteen cross fourteen cross thirty two.

### 00:49:45 · Speaker 5

Hello

### 00:49:47 · Speaker 5

Now that means that after you have applied this pooling layer, you get fourteen cross fourteen cross thirty two.

### 00:49:53 · Speaker 5

Is that correct? So for four you should

### 00:49:56 · Speaker 7

Chandan just one

### 00:49:59 · Speaker 7

So I have one question. So what is the purpose of adding this maximum in Q? Why do we add it?

### 00:49:59 · Speaker 5

S

### 00:50:03 · Speaker 5

The reason why you are adding max pooling is now sometimes you want to reduce the dimension

### 00:50:11 · Speaker 5

ओके? नो इन दैट केस यू शुड यू विल बी ऐडिंग मैक्स कूलिंग्स। ओके?

### 00:50:16 · Speaker 7

Okay, and it doesn't change the number of channels, right? It's only change, it doesn't change the number of

### 00:50:20 · Speaker 5

It doesn't change the number of channels, it will change the dimension of each feature.

### 00:50:30 · Speaker 7

Yeah, I understand. Thanks.

### 00:50:31 · Speaker 5

Okay

### 00:50:32 · Speaker 5

Okay. Now then you are applying

### 00:50:35 · Speaker 5

then you are applying one more convolutional layer when which input

### 00:50:41 · Speaker 5

you have is thirty two. Output features you are having is sixty four. Kernel size you are having is three. And padding you are having is one. Therefore stride will be one. Now can you tell me

### 00:50:55 · Speaker 5

Now what will be the

### 00:50:59 · Speaker 5

size of the output. Now your size of the input is

### 00:51:03 · Speaker 5

fourteen cross fourteen cross

### 00:51:06 · Speaker 6

thirty two. Now what will be the size of the output?

### 00:51:13 · Speaker 6

14

### 00:51:16 · Speaker 6

minus three

### 00:51:19 · Speaker 6

plus two

### 00:51:21 · Speaker 6

डिवाइडेड बाय वन प्लस वन

### 00:51:27 · Speaker 6

cross

### 00:51:32 · Speaker 6

Okay? Now the output of this will be fourteen

### 00:51:35 · Speaker 5

cross 14 cross 64, correct?

### 00:51:40 · Speaker 5

The output of convolutional two will be fourteen cross fourteen cross sixty four. Everybody is clear with that?

### 00:51:49 · Speaker 5

So now, now you are done with what do you call understanding the features.

### 00:51:58 · Speaker 5

Okay. So now what happens is, now always

### 00:52:03 · Speaker 5

in any convolutional layer, there are two parts. One is called as the feature extractor, the other is called as the classification head. Okay? Now one is called as a feature extractor, other is called as a classification head. Now feature extractor is where in which you will try to understand, okay, is there any corners, is there any edges, okay, how is the combination of them working. Now because of which you get all these filters. Now finally what should be the output? Your output should be a probability vector, right?

### 00:52:33 · Speaker 5

everybody appreciates that the final output will be a probability vector for sure. You cannot have anything else.

### 00:52:39 · Speaker 5

If it is a ten class problem, the final output should be a vector with ten components.

### 00:52:46 · Speaker 5

Yes

### 00:52:47 · Speaker 5

सो नाउ, यू हैव अ फोर्टीन क्रॉस फोर्टीन क्रॉस सिक्सटी फोर ब्लॉक, दैट यू शुड कन्वर्ट इट इनटू अ वेक्टर।

### 00:52:57 · Speaker 5

with me so far?

### 00:53:00 · Speaker 5

Any questions? Now your final output has to be a vector. Now you have a fourteen cross fourteen cross sixty four block. That you should convert into a vector. Everybody agree with me on that?

### 00:53:13 · Speaker 5

Hello

### 00:53:14 · Speaker 6

Chandan

### 00:53:14 · Speaker 5

you mean that we

### 00:53:15 · Speaker 7

mean that we should flatten it or

### 00:53:18 · Speaker 6

we should flatten from fourteen by fourteen, okay.

### 00:53:18 · Speaker 5

platen from food

### 00:53:20 · Speaker 5

Yeah, yeah, I'm coming there, I'm coming there.

### 00:53:23 · Speaker 5

So now finally I should get a vector. I have a matrix or a block now. Okay? Now I should flatten it now.

### 00:53:32 · Speaker 5

So now you'll ask a question, oh what is the difference between flattening it earlier and flattening it now? Now you have extracted the features. Now if you flatten it up at the initial thing itself, you will lose the spatial information, but

### 00:53:45 · Speaker 5

As you come further after performing lot of feature extractions that will not happen is the hypothesis there. Okay. So now that is what you are doing. Now you have an FC1 that is fully connected layers which is MLP now which takes 64 into 67 into 7. Now I have 64 14 into 14 into 64. Now then if you flatten it up I should how many elements will be there? 64 into 14 into 14 elements will be there. Now but somehow here 7 into 7 is coming now that means that I'm playing this cooling again

### 00:54:17 · Speaker 5

somewhere. Okay? And that you are converting into one hundred twenty eight and one hundred twenty eight to ten. Now because your output should be a finally a ten length vector. You did all these

### 00:54:30 · Speaker 5

feature extraction and then finally you converted that feature block that you had into a vector. That vector you converted into one twenty eight from one twenty eight to ten. So ten will be your output.

### 00:54:43 · Speaker 5

with me so far?

### 00:54:46 · Speaker 5

Is the network structure clear?

### 00:54:48 · Speaker 4

Sir, so this convolution layer one is connected to pooling layer. Then this pooling layer is connected to another convolutional layer.

### 00:54:54 · Speaker 5

connect

### 00:54:57 · Speaker 5

No no no no wait wait wait wait that I'll come okay for that you should be looking it here no this is the forward method that you have seen earlier also in M L P. Now see the input X you get first you apply convolution one. When you apply convolution one what will be the output of this the output of this will be twenty eight cross twenty eight cross thirty two.

### 00:55:15 · Speaker 7

hmm

### 00:55:16 · Speaker 5

Then you apply a relo

### 00:55:19 · Speaker 5

What will happen when you apply a reno?

### 00:55:22 · Speaker 5

all the non-zero entities will become zero. That's all.

### 00:55:27 · Speaker 5

Then you apply pooling. Now, twenty-eight cross twenty-eight cross thirty-two will become fourteen cross fourteen cross thirty-two.

### 00:55:36 · Speaker 5

Now then this is X. Now X is 14 cross 14 cross 32.

### 00:55:42 · Speaker 5

then you get here. You apply this convolutional layer. Now because of which your output will be fourteen cross fourteen cross sixty four. Then you apply relu. Again any zeros that will go off. Then you will apply this spooling. Now this spooling doesn't have any weights. Okay? All these things will have weights, convolutions and fully connected layers will have weights. But spooling layers will not have weights. Okay? Now then you apply it. Now you will get sixty four into seven into seven. That is the block size.

### 00:56:12 · Speaker 5

that you have. And you convert it, you flatten it up here. Okay? Using this x.vu minus one sixty four into seven into seven. And then you apply FC one for which you apply relu, then you apply FC two, now which is equivalent to your things. This x you will pass it on. Now to this x you should apply softmax and then you will get the posterior probabilities.

### 00:56:39 · Speaker 5

This is the idea of convolutional networks. Now let us run this by the time, no, the remaining things should be clear. It is exactly the same what you have seen earlier.

### 00:56:51 · Speaker 5

Okay. This is exactly the same the remaining things. So there will be no difference in that. Now, now, here you have applied two convolutional layers. There is nothing stopping us from using more convolutional layers. You use any number of convolutional layers you want.

### 00:57:07 · Speaker 5

Okay, now VGG nineteen, you know that network, right? VGG nineteen. Now why what is that nineteen? Now you have almost sixteen convolutional layers, after that you have some fully connected layers as your classification filter.

### 00:57:21 · Speaker 5

Okay. Now whenever I say classification head, what do I mean by that is the feature block that I have, I'll flatten it up and then I'll use it to get my posterior vector.

### 00:57:31 · Speaker 5

That is the idea. There is nothing stopping us from increasing number of layers and other things, okay? Now I have a very nice set of material on different networks that is there. I'll pass it on to you in the chat.

### 00:57:47 · Speaker 5

you can make use of them. Okay, now the data is getting loaded and the remaining things will just happen it like that. Exactly similar to MLP. We don't need to worry about that. The whole idea that should be conveyed from this discussion is, now what is a convolutional layer? How does the convolutional layer works? What are the components of the convolutional layers? If the given input is this, how do you get some specific output by manipulating the parameters that are manipulating the values, the numbers that you have. those are the things that you should get done. Okay? I presume that that is clear. Any questions there?

### 00:58:29 · Speaker 4

Sir, this feature extraction is like same, right? The convolutional we are doing, right?

### 00:58:35 · Speaker 5

Yes, yes, convolutional layers are called as feature extractors. You you you listen to this word lot of times. Convolutional layers are called as feature extractors and that last block of fully connected layers are there, no? No, they are called as the classification head. Now because, see, there are multiple tasks, right? Once one you have is classification task. You can have segmentation task. Or you can have uh what do you call uh computing task. Okay, sometimes you count number of people in the image. That is called as crowd

### 00:58:55 · Speaker 4

Are

### 00:59:05 · Speaker 5

computing. Now depending on the task the head changes but the feature extractor which is there no they remain same.

### 00:59:06 · Speaker 4

depending

### 00:59:12 · Speaker 4

Okay. And this cooling layer is cooling cooling layer is just to like decrease or increase the

### 00:59:14 · Speaker 5

And this cooling layer

### 00:59:20 · Speaker 5

reduce the dimension

### 00:59:21 · Speaker 4

reduce the pressure. And this will always be between two two layers of convolution.

### 00:59:24 · Speaker 5

will always be

### 00:59:30 · Speaker 5

Yes, it will be like so don't think of it like between two layers of convolutions. Now think of it like this is one what do you call operation that is happening, okay? Which you can which I'm highlighting here. Now which is one operation that is happening, think of it like that.

### 00:59:47 · Speaker 5

which is applied next to each other. Now, okay, uh let me show you this.

### 00:59:55 · Speaker 5

okay

### 00:59:57 · Speaker 5

You see this network here. Now you have a convolution layer. After that you have a relu. After that you have convolution, relu. Then you have max pooling, convolutions, relu, convolutions, relu, pooling. Convolution, relu, convolution, relu, pooling. After that you have fully connected layers. So this is one more network.

### 01:00:22 · Speaker 6

Okay. I think this network is basically, this network is Linnet I guess.

### 01:00:29 · Speaker 5

This is the lineate network is what I feel.

### 01:00:32 · Speaker 5

I'm telling it from my memory, I really don't know.

### 01:00:35 · Speaker 5

And this will be the output. Now what see the output here. Now it is saying that car with this much of probability. Okay. Now let me go to the home page. This home page has a very nice see here. You'll image will change and then similarly the predictions you can see that's changing right. This is happening.

### 01:00:52 · Speaker 6

Live

### 01:00:55 · Speaker 6

Okay

### 01:00:56 · Speaker 6

This is convolutional layers.

### 01:01:03 · Speaker 6

Now you can see that loss is decreasing

### 01:01:07 · Speaker 5

similarly you will get the accuracy finally. Now this is how it will work.

### 01:01:13 · Speaker 5

This is the idea of convolutions.

### 01:01:16 · Speaker 5

Okay. Now then comes the idea of transposed convolution. See the idea of transposed convolution is very simple. In convolutions normally what will happen is the dimension will decrease.

### 01:01:29 · Speaker 5

Okay. See, when you are doing the task of image generation, no, initially you will decrease, after that you should increase. The idea is called as unit. Maybe in the next tutorial that we will take, you will be on unit. It will decrease and finally it will increase, no? For that increasing, no, we have something called as transposed convolutions. Okay. The idea is called as transposed convolutions in which the size will increase, but the way in which the operations are happening is exactly similar and the number of features that are there is also similar. What do I mean by features?

### 01:01:59 · Speaker 5

in the sense that K P S and other values are there no they are similar. The only thing that you should look into is how the formula is the formula calculation is changing. Okay. I think I have a note on that I'll share that with you. Okay.

### 01:02:15 · Speaker 5

Now this is the idea of convolutions and transposed convolutions.

### 01:02:19 · Speaker 5

Is this clear? Any questions?

### 01:02:23 · Speaker 4

What is the application of this transpose convolution?

### 01:02:26 · Speaker 5

See, you you decrease the image, right? See, now you have twenty-eight cross twenty-eight cross one, no? That you have decreased it to seven cross seven cross sixty-four. Now you should take it back to twenty-eight twenty-eight one.

### 01:02:36 · Speaker 4

Okay

### 01:02:40 · Speaker 5

That is what image generation means, right? You reduce it to something and then you increase it, no? Now finally that increasing has to happen. Now to do that, we have something called as transposed convolution. Now in that case, you take the M S C laws between those two, the generated image and the original image to compare them and you back propagate the errors. Okay? Uh that is a bit of a tricky one there. Tricky in the sense to understand, not to code. Coding everything

### 01:02:41 · Speaker 4

in a

### 01:02:43 · Speaker 4

something

### 01:03:10 · Speaker 5

I don't know how many of you are using Copilot, GitHub Copilot.

### 01:03:16 · Speaker 5

Oh my god. It resolves most of our problems. I don't know, are you, are you allowed to use GPT? How, how do I know whether you are using or not? I don't have any GPT is not

### 01:03:27 · Speaker 4

I mean, GPT is not enough.

### 01:03:29 · Speaker 5

डी जी पी टी इज नॉट अलोड ओके। आई डोंट नो। वी स्टिल हैवंट डिस्कस द इवैल्यूएशन मैकेनिज्म्स, आई डोंट नो। ओके।

### 01:03:38 · Speaker 5

So good. So yeah. We will stop at this point today. uh We will take up the remaining discussion in the next week. Now finally you will have any questions you can feel free to ping me or Suhas uh in the teams we will surely help you out. Yes Satyan. Satya yeah.

### 01:03:58 · Speaker 3

Uh yeah. Sir, I have a question which I asked in that. You can call me Chandra. You can call me Chandra. Okay. Yeah, okay. Yeah. No, the first question initially I asked, right, that how are we deciding the number of filter and the filter size? Because the tutorial, it is first question that we asked.

### 01:04:01 · Speaker 5

You can call me to send

### 01:04:03 · Speaker 5

If you can call me Chandan, okay? Yeah, tell me. Yes.

### 01:04:09 · Speaker 5

how are we deciding the

### 01:04:15 · Speaker 5

Yeah. See, I think I somehow explained to you, but maybe you missed it. The idea is very simple. What should be the output you want is the question.

### 01:04:26 · Speaker 5

The example, the numerical example I gave, no? This is the input, this is the output, so you fix the remaining things.

### 01:04:29 · Speaker 7

business

### 01:04:34 · Speaker 6

Sakshi sir

### 01:04:35 · Speaker 3

Okay

### 01:04:35 · Speaker 5

This is the output size you want, so then you want to manipulate the remaining things, right?

### 01:04:41 · Speaker 3

So in between whatever the layer we can we can take how much ever the filters we need is it because we need only the output

### 01:04:49 · Speaker 5

See, you cannot take how much ever filters you want, no, because the output size is fixed. The number of filters and the number of dimensions, they are same. If you remember.

### 01:04:58 · Speaker 3

That is output layer only, right? In middle we can middle lot of convolution. Every layer, every layer

### 01:05:01 · Speaker 5

every layer every layer has an output right? every layer has an output. every layer's output. see okay. see here.

### 01:05:04 · Speaker 3

has an output

### 01:05:08 · Speaker 3

No no, what I ask is the output channel which you mentioned, that we can decide by our own, right?

### 01:05:12 · Speaker 5

ever own, right? One minute, one minute. See, the output of this is given to input as this.

### 01:05:18 · Speaker 3

Correct

### 01:05:19 · Speaker 5

The output of convolution one is given as input to convolution two. So they are not different. It's a chain that you have. Okay? Now you should decide what is the output that you want. Depending on that, you decide on the uh the values like how many kernels you what should be the size of the kernel and what should be the padding that you are using. And because of which everything changes. Because if you decide to go ahead with five kernel, five cross five kernel,

### 01:05:23 · Speaker 3

not

### 01:05:46 · Speaker 5

Now the value of here will be changing, right? Now finally the value here will be changing. You'll not get seven cross seven. You'll be getting at least four less I guess. You'll get sixty four into three into three.

### 01:05:57 · Speaker 3

I am okay with right and left but I am thinking about the channel. Okay right and left also I have to worry because how we are deciding which we have to go. See if you change number of

### 01:05:58 · Speaker 5

Okay

### 01:06:06 · Speaker 5

See if you change number of channels here. Now consider that you take sixteen channels here. Then you should take sixteen channels here you cannot have thirty two.

### 01:06:08 · Speaker 3

you

### 01:06:15 · Speaker 3

No, my question is how do you decide here thirty two and sixty four itself?

### 01:06:16 · Speaker 5

questions or we decide

### 01:06:20 · Speaker 5

they are yours your your your VIMS. No that is the reason why I told you there can be so many networks and then they standardized all these things and then they got some specific networks like ResNet, VGG wherein which these sizes that are there no everything is fixed. Okay? They fixed all those things. How many channels should be there in each of the layers, what should be the kernel size, what should be the padding, what should be the stride, everything they fixed.

### 01:06:47 · Speaker 3

Okay

### 01:06:48 · Speaker 5

in these standard networks.

### 01:06:51 · Speaker 3

Okay

### 01:06:51 · Speaker 5

Otherwise you can do whatever you want. Just you should match the things. So now what do I mean by match the things? Thirty two here, if you want to change this to twenty, okay, change this also to twenty. If you want this to be forty, change this also to be forty, that's all. If you want this to be one twenty, okay, change this also to be one twenty.

### 01:07:08 · Speaker 5

take care of those matches.

### 01:07:08 · Speaker 3

So this is a hypercarometer, right? Only we can, it's our own. We can't keep it any anything.

### 01:07:14 · Speaker 5

whatever you want you can put, no problem. But standard networks they have some things. Okay?

### 01:07:20 · Speaker 3

And sir this

### 01:07:20 · Speaker 4

And sir this final classification is coming from this fully connected layer right?

### 01:07:25 · Speaker 5

Yes, that is the classification head.

### 01:07:28 · Speaker 6

Okay

### 01:07:31 · Speaker 7

Chandan will you also cover this transpose convolution layer maybe in the next tutorial?

### 01:07:36 · Speaker 5

Yes yes. I'll uh in the sense uh I don't specifically say that I cover it but I'll give you an intuitive idea. We will not be going in depth like this because the idea is exactly similar. There is something called as fractional stride that we want to look into. Yeah yeah that's correct.

### 01:07:51 · Speaker 7

Yeah yeah that's exactly what I wanted you to clarify. That's where I could see.

### 01:07:52 · Speaker 4

what I wanted you to

### 01:07:53 · Speaker 5

Yes, yes. That's where I put. Yeah. Yeah, yeah, yeah. I'll be explaining what do you mean by fractional stride and then how it work there. Okay, that I'll explain. Okay.

### 01:08:04 · Speaker 6

Yeah, thank you.

### 01:08:08 · Speaker 5

Yeah. Okay, so we will stop at this point. Let me stop sharing. Sorry, let me stop recording.

### 01:08:18 · Speaker 5

Good
