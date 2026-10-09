---
id: CL0wlAkLx6Y
title: Deep Generative Models Tutorials CNNs
url: https://www.youtube.com/watch?v=CL0wlAkLx6Y
date: '2024-11-23'
duration: 01:08:19
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Deep Generative Models Tutorials CNNs

## Transcript

### 00:00:02 · Speaker 1

Uh can we clarify some questions on the assignment or at the last week and discuss because regarding the implementation

### 00:00:13 · Speaker 2

See let me be very frank with you I haven't even read the

### 00:00:20 · Speaker 1

But uh we have some

### 00:00:20 · Speaker 2

But uh we have some

### 00:00:22 · Speaker 1

Yeah clarity or offline shall be sent in

### 00:00:26 · Speaker 2

Yeah, you can send me a request. I'll look into it and then rectify it. Sorry, it's like sometimes, no, we read things on need basis. So only I should be reading assignment during evaluation, right? So I thought of reading it. So I'm as lazy as you all. So, okay. Okay, then.

### 00:00:44 · Speaker 1

Okay then we then we will post all the questions to you just

### 00:00:46 · Speaker 2

post all the questions you just you just send me those questions on teams or else you do it that I reply okay yeah

### 00:00:52 · Speaker 1

Oh yeah

### 00:00:54 · Speaker 2

And so uh so what is today's date is 25th so 25 25th

### 00:01:01 · Speaker 2

September two zero two four

### 00:01:06 · Speaker 2

So I presume that at least my handwriting is

### 00:01:10 · Speaker 2

readable okay so now i'll assume that you know you know the basic ideas of why torch okay now what do i mean by that you know how do you create a simple

### 00:01:24 · Speaker 2

MLP network use

### 00:01:29 · Speaker 2

Some is GD or Adam

### 00:01:35 · Speaker 2

and then use CCE loss

### 00:01:40 · Speaker 2

And then you can back propagate

### 00:01:44 · Speaker 2

back prop and then

### 00:01:47 · Speaker 2

get accuracy

### 00:01:51 · Speaker 2

Same model

### 00:01:53 · Speaker 2

Can I assume that you know these things

### 00:02:00 · Speaker 1

Yeah the the o only questions and then here is the saying

### 00:02:03 · Speaker 3

PGD versus the atom so everywhere it is showing in the papers or everywhere we are saying it is like atom so is there any specific reasons nowadays everybody is going to atom or

### 00:02:17 · Speaker 3

Optimist

### 00:02:18 · Speaker 2

See uh see atom is SGD there is an idea called as momentum

### 00:02:25 · Speaker 2

Okay uh see if we go into that that is totally a different trajectory altogether but you can think of it like it's a next version of SGD

### 00:02:35 · Speaker 2

SGD you know right gradient descent the idea of gradient descent is here

### 00:02:38 · Speaker 1

Yes yes yes yes yes yes

### 00:02:41 · Speaker 2

So you can just think of it like the next version of SGD, which is the which you have used. That is Adam. There is something that has new that has come that is AdamW. People are very much skeptical about its working. I haven't seen anybody using it per se. SGD and Adam are the ones that people will use. Now, sometimes when the network is quite deep, what they will use, they use SGD.

### 00:03:11 · Speaker 2

there is okay now what do you mean by deep how do you quantify it it's like uh what do you call day-to-day terms so if it is quite deep for example it is 20 layers 25 layers something like that you use sgd or sometimes even the the some of the problems sgd gives better answers than better predictive accuracies or better performance on whatever tasks that you are doing compared to adam so these are all very heuristic there is

### 00:03:41 · Speaker 2

no one thing to say that okay this is the what do you call silver bullet or uh what do you call the magic wand you just wave it up things will work there is nothing like that

### 00:03:53 · Speaker 2

You should try it up with multiple things. So I assume that you are comfortable with these basic things.

### 00:04:03 · Speaker 1

Oh, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no,

### 00:04:08 · Speaker 2

Sure, sure. Okay. Now everybody's clear with these topics. Anybody has any queries on these topics specifically?

### 00:04:24 · Speaker 4

What is CC loss

### 00:04:24 · Speaker 2

DCL

### 00:04:26 · Speaker 2

Categorical cross entropy loss

### 00:04:34 · Speaker 2

So now let's take this data set which is MNIST. Now MNIST is the at least a very simple toy data set that everybody will take so to get anything. Okay. It's this those the simplest data set that you can have. Now what is this MNIST? Now it is the Y that you have. Okay. See sometimes now the notations that I write and

### 00:05:04 · Speaker 2

Sometimes the notations that sir writes may be different. Okay. If you don't understand any notation, please stop me then and there and let me know. Okay. Y that we have is from 0 to 9. Okay. These are the Y's that you take. And then the X that you have, no. X belongs to R 28 cross 28.

### 00:05:29 · Speaker 2

Okay, so it's a matrix, so it's a matrix, so all x that you have, it's a matrix of

### 00:05:37 · Speaker 2

28 cross 28. Okay, you have 28 here and then you have 28 here.

### 00:05:44 · Speaker 1

And then why can't I use my notations

### 00:05:50 · Speaker 2

Set it up the thingy. Oh okay.

### 00:05:52 · Speaker 3

Uh just just joking yeah continue

### 00:05:57 · Speaker 2

And the thing is

### 00:05:59 · Speaker 3

It's okay please continue

### 00:05:59 · Speaker 4

okay please continue no no please i understand please continue yes that's okay see i just came here because you know i just wanted to let you know see i have given them the assignment right so it would be good if you can quickly tell them how to implement cnn's i think this is what you have planned and also the up convolutions transpose convolution kind of layers and how do you do them that is what you say

### 00:06:17 · Speaker 2

I found a lot of

### 00:06:21 · Speaker 2

Yes yes yes sir that is the that is the plan for uh today sir yes sir okay I'm just giving them why MLP is not a good idea for images now the spatial

### 00:06:31 · Speaker 4

See, general one, yeah, one like, you know, piece of advice, if I may. See, try to refrain from, you know, covering some theory because, you know, most of it I would have covered in the class. And so because it's only one hour, no, and it's focus more on implement because previous times also what people told me is that one hour is too less and there's too much to cover. Strike, jump straight away into implementations and codes and show them things.

### 00:06:49 · Speaker 2

We need to take a

### 00:07:00 · Speaker 2

Sure sure sure sir yeah sure

### 00:07:03 · Speaker 4

Thanks for volunteering and yeah enjoy

### 00:07:05 · Speaker 2

It's a C yeah thank you thank you sir

### 00:07:08 · Speaker 4

I'll t yeah yeah

### 00:07:10 · Speaker 2

Yes yes I'm good

### 00:07:14 · Speaker 2

So uh let's take a very simple case let's not go into this 28 cross 28 now let's take a very simple matrix you know which is of shape 4 cross 4

### 00:07:27 · Speaker 2

Now one advantage of okay I have taken four cross four I have taken five cross four let me erase this

### 00:07:35 · Speaker 2

So now I'll write some numbers here

### 00:07:41 · Speaker 2

One one

### 00:07:49 · Speaker 2

Okay, this is a very crude way I'm telling you that this is, if you consider these pixels are ones, now this is how the nine is. Okay, now similarly, you can think of in a 24, 28 cross 28 case, how this nine will be. So those pixels, so which are there, so the values of the pixels will be between 0 and 255, but the roughly the idea is this. Okay, so now if you want to classify this, what you will do is you convert this,

### 00:08:19 · Speaker 2

Now this is a 4 cross 4 thing is there no? Now the MLP takes a vector as an input. MLP always takes vector as an input.

### 00:08:29 · Speaker 2

So what do you do? You convert this into a vector. Now, when you convert this into a vector, now you take a row by row. That is, you take 0, 1, 1, 0, 0, 1, 1, 0.

### 00:08:42 · Speaker 2

0 0 1 0 0 0 0 0. No, this will be the vector. So that you will pass it through some MLP block and then that will give you the label.

### 00:08:57 · Speaker 2

This is how good will be

### 00:09:00 · Speaker 2

See the problem that happen is once you flatten things up the spatial information is lost

### 00:09:09 · Speaker 2

So you lose spatial information

### 00:09:15 · Speaker 2

Okay, spatial information is lost. Now you somehow want to work with the structure itself, the existing structure itself. Okay. I assume now the problem is clear why MLP is not a good idea for images.

### 00:09:31 · Speaker 2

Okay, now it's like if you convert my face into an image, the pixels, if you take like this, now why the eyes is here, why the nose is here, there's a specific reason. If you flatten things up, things are gone.

### 00:09:44 · Speaker 2

Now you don't get to know that that spatial information. Now that is the reason why we don't want to do this thing. Now to resolve this problem, they came up with this idea of CNNs, okay, which is

### 00:10:01 · Speaker 2

Convolutional

### 00:10:07 · Speaker 2

neural networks

### 00:10:12 · Speaker 2

So now

### 00:10:14 · Speaker 2

So let's take any image

### 00:10:22 · Speaker 2

Now you have seen lots of images right? So what do you mean by this HD? When you say HD now you mean something like 1 8 sorry you mean basically 1 0 8 0 into 7 20 right? And then you have three channels RGB channels now this is what it is a matrix okay this is one second channel and then the third channel okay now this is R channel G channel B channel and each channel

### 00:10:52 · Speaker 2

is having uh 1080 now this is you can think of this as 1080 and this is 720 okay each channel is like this is how the image is so now now you want to work on this now how do you apply the convolutions i'll directly step into that

### 00:11:13 · Speaker 2

Okay, so now let's take, let me take a very straightforward and a simple example.

### 00:11:38 · Speaker 2

Uh yeah

### 00:11:42 · Speaker 2

If someone is interested, how did they come up with these ideas? Now you can look into the Linnett paper. That's where things are pretty much clear. Now how did the idea of what do you call local receptive fields and the idea of convolutions, everything put into together and then how did they came up with the Linnett architecture? Now that was the first CNN architecture that came up. So now let me directly dive into this.

### 00:12:12 · Speaker 2

that are there here is

### 00:12:15 · Speaker 2

the idea of

### 00:12:18 · Speaker 2

Local receptive fields

### 00:12:22 · Speaker 2

Local receptive fields

### 00:12:26 · Speaker 2

and weight sharing

### 00:12:29 · Speaker 2

Okay that is the idea in which we work

### 00:12:33 · Speaker 2

Okay, I presume that the image is quite big that you can see the numbers clearly.

### 00:12:44 · Speaker 2

No

### 00:12:47 · Speaker 2

I want to show you one specific let me stop sharing this for a slight moment and then let me share you one thing from

### 00:13:00 · Speaker 2

Stanford

### 00:13:03 · Speaker 2

C and N

### 00:13:18 · Speaker 2

Let me share my laptop screen

### 00:13:29 · Speaker 2

We're able to see the see my screen

### 00:13:35 · Speaker 2

Yes

### 00:13:38 · Speaker 2

Yes okay right now this is the so this is a wonderful course

### 00:13:46 · Speaker 2

Now you just go to this, they have a very nice GIF. Now I have taken the example basically from that GIF. Now you see how the convolutions are.

### 00:13:57 · Speaker 2

You this is the image that you have three channels of the image now this filter this is for this this portion of filter is for this this is this portion of filter is for this now this is filter one and filter two now these are some of the ideas that are there now see how the movement is happening.

### 00:14:14 · Speaker 2

Shift it like this

### 00:14:18 · Speaker 2

You see you are moving like this I'll explain all these movements in a while

### 00:14:26 · Speaker 2

Now this is the idea of convolutions. Now see, you're not flattening this image up. No, this is the image. No, image is nothing but a matrix for all practical purposes for us. Okay. So now you're not flattening things up. And then the outcome that you're getting is also a matrix. This is your output. Now this is your matrix. This is also a matrix. Okay. Now why is this 2 and all those things? Why is it 3 by 3? Why is it such big? Why am I getting only 3 by 3? Now all these things I'll explain. But I just want you to look at this animation.

### 00:14:56 · Speaker 2

showing this convolution process

### 00:15:00 · Speaker 2

Let me stop sharing this and let me share my iPad now

### 00:15:26 · Speaker 2

So now

### 00:15:28 · Speaker 2

Let us take this

### 00:15:33 · Speaker 2

So you can see here, now this is one filter, so this is another filter. So this is your input, your input has three channels as of now, okay. Your input has three channels and then you have taken two filters.

### 00:15:49 · Speaker 2

Okay, so now when you have two filters, now there are three components of these two filters. What are these three components? Now these three components refers to this. Now if you had four blocks here, you would have had the fourth block here.

### 00:16:06 · Speaker 2

Okay, and the output now you can see that now this is for first filter, this is for second filter. Now how is it obtaining all those things? I'll come to. Okay, now but remember why is this three? This is this this. Okay, this is for this, this is for this and this is for this.

### 00:16:23 · Speaker 2

Okay so normally so this is

### 00:16:26 · Speaker 1

channel correct one filter for each

### 00:16:30 · Speaker 2

See okay no need to restrict for RGB now if you have four more

### 00:16:36 · Speaker 2

How much ever you have, consider that you have fourth one, you will have fourth one here, that's all. And this is for this and this will be for this, okay?

### 00:16:46 · Speaker 2

No, it is not dependent on RGB. For easiness sake, I have taken three channels, that's all. Okay. If you have 100 channels, okay, as an input, and then you are having four filters, okay. Now you'll have filter one, filter two, filter three, filter four. There'll be 100 components in each of the filters. Okay. That is the idea.

### 00:17:09 · Speaker 2

Is that clear everybody? Yes. Okay. So now what are you doing this? Now we have something called as a receptive field. Now see this is a 3 cross 3 block. The receptive field for this also will be 3 cross 3.

### 00:17:23 · Speaker 2

Okay, now this is this and this. Now this is this.

### 00:17:32 · Speaker 2

It is

### 00:17:34 · Speaker 2

Okay, now what do you do? First you apply it on the leftmost thing.

### 00:17:39 · Speaker 2

First you apply it here some operation then you move okay then you should move how much should I move do I need to move one or do what do I mean by move one

### 00:17:52 · Speaker 2

Now I start with this then I move one in the sense I move here okay

### 00:17:59 · Speaker 2

If I move two means I start with this and then I'll move two here. Okay. Now this moment is there now. This moment that I have is called as the

### 00:18:11 · Speaker 2

Spider

### 00:18:16 · Speaker 2

And you can say that how much to move

### 00:18:22 · Speaker 2

Okay how much to move

### 00:18:26 · Speaker 2

Now as of now we are taking stride equals to two that is our current assumption here

### 00:18:34 · Speaker 2

So now currently you're here let me mark the boundaries here this is the one

### 00:18:42 · Speaker 2

This is the second channel. This is in the third channel. Now, you have a 3 cross 3 block here. You have a 3 cross 3 block here. You have a 3 cross 3 block here. So, what you can do? You can perform an element wise multiplication, element wise addition or matrix multiplication is what you are supposed to do. These are the possible options that are there.

### 00:19:08 · Speaker 2

This what we will do is we will perform an element wise multiplication and add things up. Now what do I mean by that? Let me explain you that. So you see 1 here right and you see 0, 1 into 0, 0. So now let's not worry about wherever 0s are there either in this or here. Now only let me look at the non-zero values. Now there is a non-zero value here.

### 00:19:41 · Speaker 2

These are the only non-zero values correct

### 00:19:46 · Speaker 2

These values are zeros so I don't need to worry about it. This and this are zeros so I don't need to worry. So these numbers are gone.

### 00:19:57 · Speaker 2

I should only worry about this this and this

### 00:20:00 · Speaker 2

Similarly, let's come here. I'm just showing you the operation. These zeros, you don't need to worry about this. These two are gone. These two are gone. So you're only worried about the remaining three numbers. Okay, you're worried about this, this, and this.

### 00:20:16 · Speaker 2

If you want zoom in I can zoom in more come to the third filter third block this 0 this is gone this is gone you're only remaining with this so basically only with 2 basically this is the only number

### 00:20:33 · Speaker 2

So it will be easy for us to look into the operations now. So now what I'll do, I'll multiply. Now what am I supposed to do? Now this is, now this is 2 into minus 1.

### 00:20:49 · Speaker 2

1 into 1

### 00:20:53 · Speaker 2

2 into minus 1

### 00:20:59 · Speaker 2

Is it clear the operation? No this is a non-zero value non-zero value non-zero value this this this you multiply and add

### 00:21:07 · Speaker 2

2 into minus 1

### 00:21:11 · Speaker 2

2 into minus 1

### 00:21:14 · Speaker 2

1 into 1

### 00:21:18 · Speaker 2

Okay, now similarly let's do it for remaining thing. Now this is 2 into 1 plus 1 into minus 1 plus 2 into minus 1, oh sorry, 2 into minus 1.

### 00:21:34 · Speaker 2

for the next one this is 2 into minus 1 now what is this totaling to this is minus 2 plus 1 minus 2 this is minus 3

### 00:21:50 · Speaker 2

This is minus 1. Now this is minus 2. Now you have got 3 numbers. Now what are you supposed to do with these 3 numbers? Add them. Now that is minus 3, minus 1, minus 2. This will give you minus 6. Now where is that minus 6 here? Now this is the number that you get.

### 00:22:11 · Speaker 2

Okay when you did

### 00:22:15 · Speaker 2

This operation in all the three channels, you got this number.

### 00:22:22 · Speaker 2

Then you did this

### 00:22:24 · Speaker 2

On these numbers, you got minus six. Then you did went two more.

### 00:22:32 · Speaker 2

got this then you come down stride is two again you are here you started with here you should come two down

### 00:22:40 · Speaker 2

You start with this similarly you take three here and then you take three here you get this

### 00:22:49 · Speaker 2

So on you can get into. So you can look into the toggle thing that I showed you earlier. Now this is what do we call as the convolution operation.

### 00:23:02 · Speaker 2

any questions with the operation now if there is a bias term we should add it now here bias is zero so you don't need to add it if the bias term is one

### 00:23:12 · Speaker 2

You should do plus one finally okay yeah go ahead Satya yeah

### 00:23:17 · Speaker 4

on current is like how are you designing the filter size and number of filters

### 00:23:23 · Speaker 2

Keep that question. Filter size, this is what filter size is. Why am I deciding this? And how am I deciding number of filters is your question. Very good question. I'll answer that in some time.

### 00:23:40 · Speaker 2

Sanchez

### 00:23:41 · Speaker 1

You mentioned one property, right? Like when we started discussing about this, this topic, yeah, local receptive fields. So I could not understand this, like this aspect completely here. So what we are trying to say.

### 00:23:56 · Speaker 2

See is this local now as of now for this the receptive field is this.

### 00:24:01 · Speaker 1

Okay

### 00:24:03 · Speaker 2

Okay, and what, why do I say weight sharing? Now, the same set of weights is shared across the whole thing.

### 00:24:15 · Speaker 2

Now look into that LeNet paper

### 00:24:18 · Speaker 2

Linet paper

### 00:24:20 · Speaker 2

So yeah, there are many biological aspects which might not be of interest because they will say that how convolution networks are inspired by brains structure. Okay, brains. So there is image processing that initially happens, no, that V1, VGN, something, something is there. I don't remember them. Okay, but there are six layers that are there from which it got inspired. No, they will tell that. Okay, so now, now.

### 00:24:51 · Speaker 2

And you have here, this is, this I am showing in a different color, right? This is what do we call as padding. Okay. Now, why is this padding needed is, now sometimes you want your output to be of specific size. Okay. Now, in that case, you need to add some extra things. I will show you with a formula. Now, we decide, we described what is a stride now. And then the next thing that we have is,

### 00:25:24 · Speaker 2

kernel size okay or it is called as the

### 00:25:30 · Speaker 2

Filter size

### 00:25:32 · Speaker 2

Now this is 3 cross 3 in our case

### 00:25:37 · Speaker 2

And when I say three cross three this

### 00:25:44 · Speaker 2

So now then we have

### 00:25:47 · Speaker 2

number of filters

### 00:25:51 · Speaker 2

number of filters we had two filters okay in this case this is filter one this is filter two

### 00:25:59 · Speaker 2

Filter one filter two

### 00:26:02 · Speaker 2

And then number of input channels

### 00:26:07 · Speaker 2

number of input channels

### 00:26:12 · Speaker 2

I had three

### 00:26:15 · Speaker 2

number of output channels

### 00:26:20 · Speaker 2

I have it two. Why did I get it two? I'll give you the answer.

### 00:26:36 · Speaker 2

They will be saying

### 00:26:40 · Speaker 2

So now I'll give you a very important formula. You should remember this formula. Now this is where most of you will do mistakes when coding CNNs.

### 00:26:52 · Speaker 2

Select the

### 00:26:55 · Speaker 2

Input B HI into WI into DI

### 00:27:03 · Speaker 2

Now this consider before padding

### 00:27:07 · Speaker 2

Considered

### 00:27:09 · Speaker 2

before padding

### 00:27:12 · Speaker 2

Okay now what is that we have five into five into three in our current example

### 00:27:19 · Speaker 2

Okay, so now

### 00:27:22 · Speaker 2

number of filters

### 00:27:25 · Speaker 2

given by K

### 00:27:29 · Speaker 2

Seven

### 00:27:31 · Speaker 2

In our case, number of filters we have is 2. Filter size is given by F. In our case, it is 3, 3 cross 3. It will always be of square shape, so it will just write 3.

### 00:27:46 · Speaker 2

Stride

### 00:27:49 · Speaker 2

Represent by S currently we have two

### 00:27:53 · Speaker 2

Padding

### 00:27:55 · Speaker 2

is p is 1. Now, why am I saying 1? Now, because in all the direction you are adding 1 1 element. If you have 2, you will get 1 more here. If you have 3, you will get 1 more here. Okay. How many layers of things you are adding? Okay. That is padding. We have 1. Now, then, then, if this is what you have,

### 00:28:19 · Speaker 2

Then

### 00:28:21 · Speaker 2

Output will be

### 00:28:25 · Speaker 2

HO into WO into DO. Now what is this HO? HO will be HI minus F plus 2P

### 00:28:39 · Speaker 2

By s plus one

### 00:28:44 · Speaker 2

Okay, now what is WO? WO will be WI minus F plus 2P divided by S plus 1.

### 00:28:57 · Speaker 2

Now what is this DO? DO equals to K. Now let's substitute this value. What is HI? HI is 5.

### 00:29:07 · Speaker 2

minus f is three plus two into one is two

### 00:29:15 · Speaker 2

divided by s that is 2 plus 1 what is this

### 00:29:24 · Speaker 2

What is this value?

### 00:29:28 · Speaker 2

Well this is

### 00:29:33 · Speaker 2

Similarly, W will be 3 and D naught will be 2. Is that what we got?

### 00:29:43 · Speaker 2

3 cross 3

### 00:29:49 · Speaker 2

So now I will tell you some of the intricacies of this which you should remember. Okay. Now why is this padding needed will be your first question. See sometimes we want the image to be of some specific size. At that time, okay. So you can obtain either by varying F. Sometimes varying F or S you will not be able to get it. For that you should be adding 2K.

### 00:30:14 · Speaker 2

You should be adding a padding

### 00:30:17 · Speaker 2

Okay, otherwise you cannot get the image of that size. Now what will happen is when you create an image, no, you use, Sir said something called as transposed convolutions, right? Now there also the same thing will pitch in. You want image to be of some specific size. For that you should give some specific numbers. Now if you want to understand those numbers, this is the formula.

### 00:30:40 · Speaker 2

You apply that convolution operation if this is the input and these are the parameters this will be the size of the output. This is determined.

### 00:30:50 · Speaker 2

Now this is where most of the people do mistake they will get confused here

### 00:30:57 · Speaker 2

Okay now they will not be able to get what is what

### 00:31:03 · Speaker 2

Is this clear

### 00:31:06 · Speaker 2

Is the idea of convolution operations and the parameters of that is it clear

### 00:31:13 · Speaker 2

Okay, one question now just yeah, go ahead, go ahead. So this filter size you have chosen three, right?

### 00:31:22 · Speaker 4

Is there any specific reason for that like could I have chosen no like any other size

### 00:31:26 · Speaker 2

All of these are variable you can do whatever you want

### 00:31:30 · Speaker 4

That would be

### 00:31:32 · Speaker 2

Okay, now that will raise your question. So why on earth is this? Then I can have any number of networks, right? I can, so this is one layer. Similarly, I can have any number of layers of CNNs and any of these things. You go on varying things and you go on getting different different networks, right? And then I will say that Chanda net and you will say that Sachin net, okay? And then Satya will say the Satya net. And so on and so forth. Everybody let's go on giving each one network one and a name.

### 00:32:02 · Speaker 2

and let's let's uh uh destroy the whole of the thing we go on with so many names okay then what happened was there is something called as an image net computation

### 00:32:16 · Speaker 2

Okay, now there is one data set called as ImageNet. Now where know is there are thousand classes. From each of these classes there will be thousand two hundred training images and hundred testing images.

### 00:32:28 · Speaker 2

okay now every year this competition will have happen okay so now the winners of these competitions now they are the what do you call the famous networks okay now that is how the famous networks like vgg resnet everything came they were the winners at different years and then you would have heard that there is something called as se resnet okay resnet uh some you would have heard something called as resnet and all those things no no they came up because of that winning okay otherwise every person will

### 00:32:58 · Speaker 2

go on creating his own networks no it is not that there is there is some inherent meaning to all these things from which somehow we are not able to get it okay we in the sense all of us the whole community put together okay

### 00:33:11 · Speaker 2

Actually uh when you did this convolution so this stride size and the output of this filter size looks like related something right

### 00:33:22 · Speaker 2

No no no

### 00:33:28 · Speaker 2

Okay, okay, in the sense, okay, I got your point. What you are saying is, if the number of filter sizes is three cross three, I cannot have stride more than three.

### 00:33:37 · Speaker 1

Yeah yeah like something there should be some common

### 00:33:39 · Speaker 2

Okay. Yeah, yeah, yeah. So you cannot see if I am starting here, I cannot have stride four, which I'll get into here. Because in middle, one row will be left. Okay. So those are some inbuilt ideas that you should immediately get it. That's a valid point, correct? Now you can have either one, zero. So sorry, it should be either one, which is default, two or zero. Okay. Now what should be the movement in each of the cases?

### 00:34:07 · Speaker 2

And then you cannot put any random numbers here and things will not work out. I'll just give you one example. Okay. Now, now tell me this. I have a convolutional layer here.

### 00:34:18 · Speaker 2

So I will not give you the details. What should be the convolution layer? You should give me F, K, P and S value. Now my input is 28 cross 28 cross 3.

### 00:34:34 · Speaker 2

And then my output is 24 cross 24 cross 16. Now tell me what are the values of this FKPS?

### 00:34:45 · Speaker 2

Reduce the size you can look into it

### 00:34:49 · Speaker 2

Now tell me what are the values that I should be giving for this FKPS

### 00:34:56 · Speaker 2

Put it in the chat box is there a chat

### 00:34:56 · Speaker 4

Excellent

### 00:35:08 · Speaker 4

A five cross five is the filter

### 00:35:11 · Speaker 2

No no just put it just just put it there just put put all the four values there put it in the chat do a calculation and put it in the chat

### 00:35:32 · Speaker 2

I want everybody to do this calculation now because these kinds of calculations where you surely get stuck because you'll be applying lot of convolutions and then you should be knowing what will be the outcome of that convolution okay

### 00:35:57 · Speaker 2

So now how do we calculate? The idea is very simple.

### 00:36:03 · Speaker 2

Now K is fixed.

### 00:36:07 · Speaker 2

k is 16. Any questions on that? d naught equals to k. k is fixed. Now d output is this. So k is fixed. Okay. So then the remaining things is that what we want. So what do we know? We know ho equals hi minus f plus 2p by s plus 1. Now what is ho is 24 equals 28 minus

### 00:36:37 · Speaker 2

f plus 2p by s plus 1. Now just take a simple thing. Let's first take s is equal to 1, p is equal to 0. If you take this, you will get f equals 5. Works? We just keep this. Now if the input image is this and the output size you want is this. Now this should be the combination of features, this should be the combination of parameters that you should be

### 00:37:07 · Speaker 2

having to get it

### 00:37:09 · Speaker 2

Is that clear

### 00:37:12 · Speaker 4

I know the creepback

### 00:37:15 · Speaker 2

See, you have, you can get two equations, three unknowns are there. Okay. No, even God cannot solve it. Okay. No, I don't know. There is a statement. Okay. One equation, one unknown. Any fools can solve it. Okay. One equation, two unknowns. Not even God can solve it. Okay. So, so you have two equations, three unknowns. So, not even God can solve it.

### 00:37:44 · Speaker 2

So now

### 00:37:47 · Speaker 2

Screen is not visible. Yes, screen is visible. Screen is visible. Yeah, yeah, I got it, got it, got it. Somehow it got.

### 00:37:56 · Speaker 2

No God got offended by my statement oh you see this I cannot do it I can do something better

### 00:38:08 · Speaker 2

Just give me a moment what happened was my internet was

### 00:38:24 · Speaker 2

So so now everybody is clear with these ideas

### 00:38:29 · Speaker 2

Now what you are supposed to do now

### 00:38:34 · Speaker 4

Can you tell that equation solving again this k is fixed after that

### 00:38:40 · Speaker 2

K is fixed, okay. K is fixed, okay. So now you cannot have what do you call weird kind of things, okay. You cannot do it. You cannot basically solve it, right? Now because you have three equations, sorry, three unknowns and two equations, you cannot solve them. So now you should fix some of the things. So now let's fix S is equal to one and P is equal to zero is my proposition. And let's see whether we can get something out of it. Yes, we got something out of it. Let's use it.

### 00:39:10 · Speaker 2

Okay, I'm not saying that that is the only unique solution. There can be multiple other solutions that are possible. This is the one solution that I have got. I'll just fix to it.

### 00:39:23 · Speaker 2

Now my screen is back

### 00:39:28 · Speaker 2

Oh 912R this is the reason sir told me don't do theory and start coding directly okay

### 00:39:42 · Speaker 2

So now always know when you have things fixed, okay, now input size is fixed. So you want this to be the output size. These are how you can manipulate. Okay, so this manipulation is clear, I guess.

### 00:40:01 · Speaker 2

Any questions on these manipulations

### 00:40:07 · Speaker 2

Fine. So now let's not waste any more time. Let's go into the coding part of this. Okay.

### 00:40:14 · Speaker 2

Let me stop sharing my screen let me go to the

### 00:40:21 · Speaker 2

aspects

### 00:40:48 · Speaker 2

You can see my screen

### 00:40:51 · Speaker 2

Google, yes.

### 00:40:54 · Speaker 2

uh just go to Collab

### 00:41:09 · Speaker 2

Let's go to Google Collab

### 00:41:12 · Speaker 2

create a new notebook

### 00:41:17 · Speaker 2

I presume everybody's comfortable with Google Collab right

### 00:41:22 · Speaker 2

Exactly similar to Jupyter Notebook

### 00:41:25 · Speaker 2

And I don't need to worry about many of the things. Now here I'll have

### 00:41:32 · Speaker 2

PGM 24

### 00:41:36 · Speaker 2

Tutorials okay

### 00:41:39 · Speaker 2

So now

### 00:41:41 · Speaker 2

Let me directly start doing things

### 00:42:08 · Speaker 2

I will be explaining you this code directly

### 00:42:14 · Speaker 2

like on par

### 00:42:25 · Speaker 2

Now I presume that these libraries are very much clear for you by now

### 00:42:34 · Speaker 2

Transforms are done right now you know what is transforms

### 00:42:39 · Speaker 2

And other things normalization to tensor all those things are clear, right? Can I assume them?

### 00:42:49 · Speaker 2

So can I assume that transforms are clear

### 00:42:55 · Speaker 2

So now you are getting the train loader under the test loader train set and test set. Now let's try to understand this thing.

### 00:43:02 · Speaker 2

Okay, now here you're creating a simple CNN. Now first you are having a convolutional layer. Now what is this convolutional layer? Convolutional layer, now first you should say that how many input channels are you having? This is input channels. How many output channels you want? You want 32. Input channels, now it depends on your input. How many output channels? I want 32. Now that means that how many filters will be there?

### 00:43:33 · Speaker 4

I can see

### 00:43:33 · Speaker 2

If we say that the output 32 filters will be there okay and then how many components will be there in each of the filter

### 00:43:46 · Speaker 2

How many components should be there each of the filter

### 00:43:49 · Speaker 4

One one channel is

### 00:43:51 · Speaker 2

one component correct your input has only one channel so there will be one component in each of these 32 filters and then each filter size you are saying that it is 3 that means that it is 3 cross 3

### 00:44:09 · Speaker 2

Is that clear the first thing

### 00:44:13 · Speaker 2

kernel size it is saying that 3 that means that it is 3 cross 3 kernel so now and then you are saying that padding is 1 so now you take this uh image so which is one channel and then you are having 32 filters and then each filter has one component the size of that component is 3 cross 3 and then for the image you are had even padding is 1

### 00:44:39 · Speaker 2

Is that clear? Any queries with how is this defined?

### 00:44:46 · Speaker 2

its components and uh

### 00:44:49 · Speaker 2

Each of these terms is it clear stride if you don't specify by default stride will be one

### 00:44:56 · Speaker 2

Is this much clear

### 00:45:02 · Speaker 2

Okay, so now after this

### 00:45:05 · Speaker 4

So sorry to interrupt and then I have one question we can have non square filters also right

### 00:45:08 · Speaker 2

That's what we learned

### 00:45:15 · Speaker 2

Uh no madam secretary

### 00:45:16 · Speaker 4

We are considering uh three cross three we can have three cross three also right

### 00:45:21 · Speaker 2

No no no no then the whole convolutional operation will just have issues

### 00:45:28 · Speaker 2

explicitly define okay you cannot have it i guess

### 00:45:33 · Speaker 2

Okay, I haven't seen non-square kernels as of now, but I presume that it is not possible. The reason is because of the formula. I haven't seen that. Let me look into it and if there is anything, I'll put it in the group. But as of now, my hands...

### 00:46:00 · Speaker 2

See, okay, let's not, okay, I, as of now, I don't know. If there is anything, I'll put the resource in the group, okay? Let's not take the deviation towards non-square channels, non-square filters, okay? So now, this is the convolutional layer, and then there are layers called as pooling layers.

### 00:46:21 · Speaker 4

Oh what does

### 00:46:22 · Speaker 2

This pooling layer does

### 00:46:43 · Speaker 2

Zoom is far better this Microsoft Teams is there now it doesn't allow to annotate it doesn't allow many of the operations

### 00:46:58 · Speaker 2

you see this four cross four entity now

### 00:47:02 · Speaker 2

You see a 4 cross 4 thing. If I say that, perform a max pooling with 2 cross 2 block with stride 2. Max pooling with 2 cross 2 filter with size with stride 2. Now, first you apply for this.

### 00:47:21 · Speaker 2

What do you mean by max pooling now out of this find the maximum value six is the maximum value you get six

### 00:47:28 · Speaker 2

Now then you should move two because you are saying that stride is two. Now max is eight. Then you started with here. Now you should move by two. You'll get it here. Max is three. Then you move by two. You get max is four. Now this is max pooling. Now if you want average pooling, you can say the same thing. Average pooling with two cross two filter and stride two. Now then you take the average of it. This is 11. 11 plus two is 13. 13 by four is three.

### 00:47:58 · Speaker 2

point two five so on and so forth you get like this now either you can have a max pooling or you can have an average pooling

### 00:48:08 · Speaker 2

This is the pooling layers

### 00:48:11 · Speaker 2

Now here I am saying that pooling layer you have a kernel size of 2 cross 2 and stride 2.

### 00:48:18 · Speaker 2

Now now tell me

### 00:48:22 · Speaker 2

If the input size is 28, okay, now tell me if the input size is 28 cross 28 cross 1, what will be the output size in this case?

### 00:48:38 · Speaker 2

If the input size is 28 cross 28 cross 1, what will be the output size? Go ahead, take a pen and paper and calculate. I'll also do it. Even I don't know.

### 00:48:51 · Speaker 2

Now H o equals H i minus F plus 2 p by S plus 1. Now H input is 28 minus 3 plus 2.

### 00:49:08 · Speaker 2

by 1 plus 1 now this is

### 00:49:16 · Speaker 2

25

### 00:49:19 · Speaker 2

25 plus 27

### 00:49:23 · Speaker 2

This will be 28 cross 28 cross 32 correct

### 00:49:30 · Speaker 2

The output will be 28 cross 28 cross 32 cut. I also got the same thing. Now, then you apply a max pooling. Now, when you apply a max pooling of size 2 cross 2, so then it will be converted to 14 cross 14 cross 32.

### 00:49:47 · Speaker 2

Now that means that after you have applied this pooling layer you get 14 cross 14 cross 32.

### 00:49:53 · Speaker 2

Is that correct So for four you should

### 00:50:01 · Speaker 2

fighting this battle

### 00:50:03 · Speaker 2

The reason why you're adding max pooling is now sometimes you want to reduce the dimension

### 00:50:11 · Speaker 2

Okay now in that case you should you will be adding max coolings

### 00:50:16 · Speaker 2

Okay, and it doesn't change the number of channels, right? It can only change the dimension of each feature.

### 00:50:30 · Speaker 4

I understand

### 00:50:30 · Speaker 2

understood okay now then you are applying

### 00:50:36 · Speaker 2

you are applying one more convolutional layer where in which input you have is 32 output features you are having is 64 kernel size you are having is 3 and padding you are having is 1 therefore stride will be 1. now can you tell me

### 00:50:55 · Speaker 2

Now what will be the

### 00:50:59 · Speaker 2

Size of the output now your size of the input is

### 00:51:03 · Speaker 2

14 cross 14 cross

### 00:51:06 · Speaker 2

32 now what will be the size of the output

### 00:51:13 · Speaker 2

14

### 00:51:16 · Speaker 2

Minus three

### 00:51:19 · Speaker 2

plus two

### 00:51:21 · Speaker 2

divided by 1 plus 1

### 00:51:28 · Speaker 2

Across

### 00:51:32 · Speaker 2

Okay, now the output of this will be 14 cross 14 cross 64, correct?

### 00:51:40 · Speaker 2

The output of convolutional two will be 14 cross 14 cross 64. Everybody's clear with that?

### 00:51:50 · Speaker 2

So now, uh, now you are done with what do you call understanding the features.

### 00:51:58 · Speaker 2

Okay, so now what happens is, now always in any convolutional layer, there are two parts. One is called as the feature extractor. The other is called as the classification head. Okay, now one is called as a feature extractor. Other is called as a classification head. Now feature extractor is where in which you will try to understand, okay, is there any corners? Is there any edges? Okay, how is the combination of them working? Now because of which you get all these filters.

### 00:52:28 · Speaker 2

And finally what should be the output your output should be a probability vector right

### 00:52:33 · Speaker 2

Everybody appreciates that the final output will be a probability vector for sure. You cannot have anything else.

### 00:52:39 · Speaker 2

If it is a 10 class problem the final output should be a vector with 10 components

### 00:52:47 · Speaker 2

So now you have a 14 cross 14 cross 64 block so that you should convert it into a vector

### 00:52:57 · Speaker 2

With me so far

### 00:53:00 · Speaker 2

Any questions? Now your final output has to be a vector. Now you have a 14 cross 14 cross 64 block. That you should convert into a vector. Everybody agree with me on that?

### 00:53:14 · Speaker 2

Chandran you mean that we should flatten it or

### 00:53:18 · Speaker 2

should happen from 14 by 14. okay yeah yeah i'm coming there i'm coming there so now finally i should get a vector i have a matrix or a block now okay now i should flatten it now

### 00:53:31 · Speaker 2

So now you will ask a question, oh what is the difference between flattening it earlier and flattening it now? Now you have extracted the features. Now if you flatten it up at the initial thing itself, you will lose the spatial information but as you come further after performing lot of feature extractions that will not happen is the hypothesis there. Okay. So now that is what you are doing. Now you have an FC1 that is fully connected layers which is MLP now which takes 64 into 67 into 7. Now I have

### 00:54:01 · Speaker 2

64 14 into 14 into 64 now then if you flatten it up I should how many elements will be there 64 into 14 into 14 elements will be there but somehow here 7 into 7 is coming now that means that I'm applying this pooling again

### 00:54:18 · Speaker 2

Okay, and that you are converting into 128 and 128 to 10. Now, because your output should be a finally a 10 length vector, you did all these feature extraction. And then finally, you converted that feature block that you had into a vector. That vector you converted into 128 from 128 to 10. So 10 will be your output.

### 00:54:43 · Speaker 2

me so far

### 00:54:46 · Speaker 2

Is the network structure clear? Sir, so this convolution layer one is connected to pooling layer then this pooling layer is connected to another convolutional layer? No, no, no, no. Wait, wait, wait, wait. That I'll come. Okay, for that you should be looking at here. Now this is the forward method that you have seen earlier also in MLP. Now see the input x you get, first you apply convolution one. When you apply convolution one, what will be the output of this? The output of this will be 28 cross 28 cross 32.

### 00:55:16 · Speaker 2

So then you apply a ReLU

### 00:55:20 · Speaker 2

What will happen when you apply a reload

### 00:55:22 · Speaker 2

All the non-zero entities entities will become zero that's all

### 00:55:27 · Speaker 2

Then you apply pooling. Now 28 cross 28 cross 32 will become 14 cross 14 cross 32.

### 00:55:36 · Speaker 2

Now then this is X. Now X is 14 cross 14 cross 32. Now then you get here, you apply this convolutional layer. Now because of which your output will be 14 cross 14 cross 64. Then you apply the ReLU. Again any zeros that will go off. Then you will apply this pooling. Now this pooling doesn't have any weights. All these things will have weights. Convolutions and fully connected layers will have weights. But pooling layers will not have weights.

### 00:56:06 · Speaker 2

Okay, now then you apply it. Now you will get 64 into 7 into 7. That is the block size that you have. And you convert it, you flatten it up here. Okay, using this x.view minus 1, 64 into 7 into 7. And then you apply FC1 for which you apply ReLU. Then you apply FC2, now which is equivalent to your things. This x you will pass it on. Now to this x you should apply softmax and then

### 00:56:36 · Speaker 2

get the posterior probabilities

### 00:56:40 · Speaker 2

This is the idea of convolutional networks. Now let us run this by the time, no, the remaining things should be clear. It is exactly the same what you have seen earlier.

### 00:56:51 · Speaker 2

Okay, this is exactly the same, the remaining things. So there will be no difference in that. Now, now here you have applied two convolutional layers. There is nothing stopping us from using more convolutional layers. You use any number of convolutional layers you want.

### 00:57:07 · Speaker 2

Okay, now VGG 19, you know that network, right? VGG 19. Now why, what is that 19? Now you have almost 16 convolutional layers. After that, you have some fully connected layers as your classification center.

### 00:57:21 · Speaker 2

Okay, now whenever I say classification head, what do I mean by that is the feature block that I have, I'll flatten it up and then I'll use it to get my posterior vector. That is the idea. There is nothing stopping us from increasing number of layers and other things. Okay, now I have a very nice set of material on different networks that is there. I'll pass it on to you in the chat.

### 00:57:47 · Speaker 2

can make use of them okay now the data is getting loaded and the same remaining things will just happen it like that exactly similar to MLP we don't need to worry about that the whole idea that should be conveyed from this discussion is now what is a convolutional layer how does the convolutional layer works what are the components of the convolutional layers if the given input is this how do you get some specific output by manipulating the parameters that are manipulating the values the numbers that you have so

### 00:58:17 · Speaker 2

Those are the things that you should get

### 00:58:21 · Speaker 2

I presume that that is clear any questions there

### 00:58:29 · Speaker 4

this feature extraction is like same right the convolutional we are doing right

### 00:58:35 · Speaker 2

Yes, yes. Convolution layers are called as feature extractors. You listen to this word lot of times. Convolution layers are called as feature extractors. And that last block of fully counted layers are there now. Now, they are called as the classification header. Now, because see, there are multiple tasks, right? Once one you have is classification task. You can have segmentation task. Or you can have what do you call computing task. Okay. Sometimes you count number of people in the image. That is called as crowd

### 00:59:05 · Speaker 2

computing now depending on the task the head changes but the feature extractor which is there no they remain

### 00:59:14 · Speaker 2

And uh this cooling layer is cooling cooling layer is just

### 00:59:14 · Speaker 4

Oh this is

### 00:59:18 · Speaker 2

to like decrease or increase or reduce the dimension reduce it

### 00:59:23 · Speaker 2

And this will always be between two two layers of convolution

### 00:59:30 · Speaker 2

Yes, it will be like so don't think of it like between two layers of convolutions. Now think of it like this is one what do you call operation that is happening. Okay. Which you can which I am highlighting here. Now which is one operation that is happening. Think of it like that.

### 00:59:48 · Speaker 2

which is applied next to each other

### 00:59:51 · Speaker 2

Now, okay, uh, let me show you this

### 00:59:57 · Speaker 2

You see this network here. Now you have a convolution layer. After that you have a ReLU. After that you have convolution, ReLU. Then you have max pooling, convolutions, ReLU, convolutions, ReLU, pooling. Convolution, ReLU, convolution, ReLU, pooling. After that you have fully connected layers. So this is one more network.

### 01:00:23 · Speaker 2

I think this network is basically this network is limit I guess

### 01:00:29 · Speaker 2

This is the LINET network is what I feel

### 01:00:32 · Speaker 2

I'm telling it from my memory, I really don't know. And this will be the output. Now, what see the output here? It is saying that car with this much of probability. Okay. Now, let me go to the home page. This home page has a very nice. See here, your image will change. And then similarly, the predictions you can see that's changing, right? And this is happening live.

### 01:00:56 · Speaker 2

This is convolutional layers

### 01:01:04 · Speaker 2

Now you can see that loss is decreasing. So similarly you will get the accuracy finally. Now this is how it will work.

### 01:01:13 · Speaker 2

This is the idea of convolutions

### 01:01:17 · Speaker 2

Now then comes the idea of transposed convolution. See the idea of transposed convolution is very simple. In convolutions normally what will happen is this the dimension will decrease.

### 01:01:29 · Speaker 2

Okay, see when you are doing the task of image generation, no, initially you will decrease, after that you should increase. The idea is called as unit. Maybe the next tutorial that we will take will be on unit. It will decrease and finally it will increase, no? For that increasing, no, we have something called as transposed convolutions. Okay, the idea is called as transposed convolutions in which the size will increase, but the way in which the operations are happening is exactly similar and the number of features that are there is also similar. Now what do I mean by features in the

### 01:01:59 · Speaker 2

sense that k p s and other values are there no they are similar the only thing that you should look into is how the formula is the formula calculation is changing okay uh i think i have an uh note on that i'll share that with you

### 01:02:15 · Speaker 2

So this is the idea of convolutions and transposed convolutions is this clear any questions

### 01:02:23 · Speaker 2

So what is the application of this transpose convolution? See, you decrease the image, right? See, now you have 28 cross 28 cross 1, no? That you have decreased it to 7 cross 7 cross 64. Now you should take it back to 28 cross 28, 1.

### 01:02:40 · Speaker 2

that is what inner means right you reduce it to something and then you increase it no now finally that increasing has to happen and to do that we have something called as transposed convolution now in that case you take the mse loss between those two the generated image and the original image to compare them and you back propagate the errors okay uh that is a bit of a tricky one there tricky in the sense to understand not to code okay coding everything

### 01:03:10 · Speaker 2

I don't know how many of you are using copilot github copilot

### 01:03:16 · Speaker 2

Oh my God, it resolves most of our problems. I don't know, are you allowed to use GPT? How do I know whether you are using or not? I don't have any...

### 01:03:27 · Speaker 4

I mean GPT is not an animal

### 01:03:29 · Speaker 2

DGPT is not allowed ah okay I don't know we still haven't discussed the evaluation mechanisms I don't know

### 01:03:39 · Speaker 2

So good. So yeah, we will stop at this point today. We will take up the remaining discussion in the next week. Now finally, you will have any questions, you can feel free to ping me or Suhas in the teams. We will surely help you out. Yes, Satyajit. Satya, yeah.

### 01:03:58 · Speaker 4

Uh yeah I'll send a question you can ask if you want me to answer

### 01:04:01 · Speaker 2

Then you can watch me this time

### 01:04:04 · Speaker 2

If you can call me Chanzy okay

### 01:04:06 · Speaker 4

Yeah yeah no the first question initially asked right that how are we deciding the number of filter and the filter size because the tutorial it is just because you have to understand

### 01:04:15 · Speaker 2

Yeah, see, I think I somehow explained you, but maybe you missed it. The idea is very simple. What should be the output you want is the question. The example, the numerical example I gave, no, this is the input, this is the output, so you fix the remaining things.

### 01:04:35 · Speaker 2

Okay this is the output size you want so then you want to manipulate the remaining things right

### 01:04:41 · Speaker 4

So in between whatever the layer we can uh we can take out whichever the filters we need is it because we need only the output uh

### 01:04:49 · Speaker 2

You cannot take how much ever filters you want no because the output size is fixed now the number of filters and the number of dimensions they are same if you remember

### 01:04:59 · Speaker 4

That is output layer only right In median we can and median a lot of convolutional layers

### 01:05:01 · Speaker 2

Every layer every layer has an output right every layer has an output every layer's output see okay

### 01:05:08 · Speaker 4

No no I what I ask is the output channel which you mentioned that we can decide by our own right

### 01:05:13 · Speaker 2

One minute one minute see the output of this is given to input as this

### 01:05:19 · Speaker 2

The output of convolution one is given as input to convolution two. So they are not different. It's a chain that you have. Okay. Now you should decide what is the output that you want. Depending on that, you decide on the values like how many kernels you what should be the size of the kernel and what should be the padding that you are using. And because of this, everything changes. Because if you decide to go ahead with five kernel, five cross five kernel.

### 01:05:46 · Speaker 2

So the value of here will be changing right now finally the value here will be changing you'll not get seven cross seven you'll be getting at least four less I guess you'll get 64 into three into three.

### 01:05:57 · Speaker 4

I I'm not saying that I tell where but I'm thinking about the channel uh okay so I can't really tell because how we are deciding what we have to see if you change number of

### 01:05:58 · Speaker 2

I'm not saying that

### 01:06:06 · Speaker 2

See if you change number of channels here now consider that you take 16 channels here then you should take 16 channels here you cannot have 32.

### 01:06:15 · Speaker 4

I know my question is obviously the same as your 32 and 64

### 01:06:16 · Speaker 2

Questions all being said

### 01:06:20 · Speaker 4

Okay

### 01:06:20 · Speaker 2

Yeah, they are yours, sir. Your, your, your whims. Now, that is the reason why I told you there can be so many networks. And then they standardized all these things. And then they got some specific networks like ResNet, VGG, where these sizes that are there now, everything is fixed. Okay. They fixed all those things. How many channels should be there in each of the layers? What should be the kernel size? What should be the padding? What should be the stride? Everything they fixed.

### 01:06:48 · Speaker 2

in these standard networks

### 01:06:51 · Speaker 2

Okay, otherwise you can do whatever you want to just you should match the things. So now what do I mean by match the things 32 here? If you want the changes to 20, okay, change this also to 20. If you want this to be 40, change this also to be 40. That's all. If you want this to be 120, okay, change this also to be 120.

### 01:07:08 · Speaker 2

I think it's

### 01:07:08 · Speaker 4

We can only use our own right only because it's our own we can keep it any anything

### 01:07:14 · Speaker 2

whatever you want you can put no problem but standard networks they have some things okay and so this final classification is coming from this fully connected layer

### 01:07:25 · Speaker 2

Yes that is the classification header

### 01:07:31 · Speaker 2

Chandan, will you also cover this transpose convolution layer or maybe in the next two two days? Yes, yes. In a sense, I don't specifically say that I cover it, but I'll give you an intuitive idea. We will not be going in depth like this because the idea is exactly similar. There is something called a fractional stride that we want to look into. Yeah, yeah, that's exactly what I wanted you to clarify. That's where I could stop.

### 01:07:51 · Speaker 4

Yeah that's exactly what I wanted you to clarify that's where I got stuck

### 01:07:56 · Speaker 2

Yeah, yeah, yeah. I'll be explaining what do you mean by fractional stride and then how it work there. Okay, that I'll explain.

### 01:08:04 · Speaker 2

Yeah thank you

### 01:08:08 · Speaker 2

Okay, so we will stop at this point. Let me stop sharing. Sorry, let me stop recording.

### 01:08:18 · Speaker 2

Good
