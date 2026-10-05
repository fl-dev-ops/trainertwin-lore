---
id: QxcxTYZ62TI
title: Lec 10 - Deep Generative Models VAEs beta VAE VQ VAEs
date: '2024-11-23'
url: https://www.youtube.com/watch?v=QxcxTYZ62TI
description: ''
author: prathoshap5226
duration: 02:44:13
model: saaras:v3
transcript: true
---

# Lec 10 - Deep Generative Models VAEs beta VAE VQ VAEs

## Transcript

### 00:00:09 · Speaker 6

getting two voices. Where is it from?

### 00:00:12 · Speaker 6

Okay

### 00:00:25 · Speaker 3

Okay, so last class we completed V A E straight.

### 00:00:35 · Speaker 3

Hello

### 00:00:35 · Speaker 6

Yes sir, Yes sir.

### 00:00:37 · Speaker 3

Okay

### 00:00:43 · Speaker 3

for computer okay

### 00:00:47 · Speaker 3

Okay, so maybe quickly

### 00:00:49 · Speaker 4

take five ten minutes to look at the inference I think training of AI was done I suppose and

### 00:00:58 · Speaker 4

I hope that uh you people could uh revise everything that we had done in the uh in the wake of exam, right? So that you know you are up to the speed. Okay. So what I'll do today is uh like initial five ten minutes I'll just uh complete the inference part of V A E, okay? Uh just ten minutes. And then we'll move on to the diffusion models, okay? So that's what the uh

### 00:01:26 · Speaker 4

plan for today is

### 00:01:28 · Speaker 4

before we continue, we just want to see how many classes are we left with. nineteenth is nineteenth we have one class.

### 00:01:37 · Speaker 4

twenty sixth we have one class. Two. Second also we can have a class right?

### 00:01:47 · Speaker 3

Yes, I can have

### 00:01:47 · Speaker 6

Yes, that can happen.

### 00:01:48 · Speaker 4

Yes

### 00:01:48 · Speaker 3

Yes

### 00:01:49 · Speaker 4

one, two, three, four.

### 00:01:56 · Speaker 4

four uh and ninth five and sixteenth also we can have a class even though they have said that fourteenth is the last working day last class day we can also have a class on sixteenth.

### 00:02:09 · Speaker 4

so that there will be one two three

### 00:02:14 · Speaker 4

four

### 00:02:17 · Speaker 4

one, two, three, four

### 00:02:21 · Speaker 5

five including today.

### 00:02:22 · Speaker 4

five including today. Yeah, I think that's good. So, what I'll do now, today we will start the D D P M diffusion models. Maybe next one more class I will complete D D P M, okay? So that will leave us with three classes, three more classes. uh Yeah, that's good enough. So, one class for auto regressive models and L L M's and

### 00:02:48 · Speaker 4

I think yeah, that's good. We can cover a lot more growth.

### 00:02:51 · Speaker 5

Sir, but we didn't do VQVAE and

### 00:02:54 · Speaker 4

will lose

### 00:02:55 · Speaker 4

Yeah, I I will do that today. So initially, today before I complete, you know, I'll do inference on VAEs and I'll I'll do VQ VAEs and then we'll go to diffusion models. Okay.

### 00:03:09 · Speaker 4

started then

### 00:03:09 · Speaker 2

Sir, for two minutes can we just go through the passes once for the decoder encoder?

### 00:03:16 · Speaker 4

you mean the training you are saying

### 00:03:18 · Speaker 2

Yes. Yes.

### 00:03:19 · Speaker 4

I'll do that. I'll do that.

### 00:03:24 · Speaker 4

So this is there in your second assignment, right? So when you implement it, it will become much more clearer anyway. I'll do that.

### 00:03:33 · Speaker 4

ओके

### 00:03:35 · Speaker 4

Okay. So as you know right we have these two components the encoder and decoder. Encoder is probabilistic.

### 00:03:45 · Speaker 4

Okay, I also told you why this would be a reconstruction cost, right?

### 00:03:52 · Speaker 4

uh yeah we have done that okay. Why would the log likelihood becomes reconstruction cost okay that also we have done good. Okay so here is how uh VAE works. So you take a sample X I this is of course for training. Take a sample X I which is a data sample. Pass it through the encoder. This is the forward pass. So once you pass it through the encoder you will get a mean and a variance. Typically how is it done is uh if K is the dimensionality of your latent space

### 00:04:26 · Speaker 3

the output of the encoder

### 00:04:31 · Speaker 6

the output of the encoder is

### 00:04:35 · Speaker 6

This is D dimensional

### 00:04:43 · Speaker 6

This is D dimensional, okay? And, uh

### 00:04:47 · Speaker 4

this will be

### 00:04:51 · Speaker 4

k dimensional. So typically what what will be done is this will also be a k dimensional vector. See actually it should be a k square dimensional vector. uh people take it as k dimensional vector by by assuming a diagonal covariance, okay? If you assume this to be a diagonal covariance, then you only have k parameters, right? Because it's only a diagonal matrix. So input is a d dimensional vector which is a which is an image or whatever, right? And the output of encoder will be

### 00:05:21 · Speaker 4

two k dimensional where first k dimensions will be corresponding to the mean and the next k dimensions correspond to the variance

### 00:05:30 · Speaker 4

Okay. Now once you get the mean and variance, what you do is you sample a Gaussian distribution outside of the neural network epsilon j. And uh you do this reparameterization which is you uh add this mean that the output of the encoder has given. Okay. Uh to epsilon which is scaled by sigma.

### 00:05:53 · Speaker 4

that will give you a Z J. So take that Z J, okay, and pass it through the decoder and the output of the decoder is taken to be X J cap. So this is one forward pass. Any questions on this?

### 00:06:14 · Speaker 6

Hello

### 00:06:16 · Speaker 5

सर, व्हेन वी से वेरियेशनल इन्फरेंस

### 00:06:16 · Speaker 3

when we

### 00:06:17 · Speaker 4

Hmm

### 00:06:20 · Speaker 4

Hmm

### 00:06:21 · Speaker 5

Sir, like, what do we mean by that?

### 00:06:24 · Speaker 4

No no no hold on I I still not come to that we are not talking about inference we are only talking about training now see one forward pass through encoder and decoder is this that much is clear. So pass a sample through the encoder get your parameters reparameterize it sample outside the neural network reparameterize and then again pass it through the decoder you get an X cap so that is one pass through the encoder decoder okay. Now to train the encoder what you do is encoder has uh two

### 00:06:34 · Speaker 5

process

### 00:06:54 · Speaker 4

process, right? One is the the KL loss.

### 00:06:58 · Speaker 4

This is to train the decoder. We saw how to train the encoder here. Yeah. To train the encoder we had once you get the X cap, right? You compute this

### 00:07:09 · Speaker 4

reconstruction term, okay? And then, you back propagate it by keeping the decoder parameters fixed, okay? And there is also a once you come to the input of the the the decoder, you have the KL term also, differentiate that KL term with respect to the encoder parameters and then differentiate through this reparameterization term and then back propagate all the way through the input of the encoder. So that is backward pass through the encoder

### 00:07:42 · Speaker 4

Is that okay? Any questions on this?

### 00:07:47 · Speaker 4

So to train the encoder, you'll have to do one forward pass through the encoder and decoder, and then one backward pass through the decoder and the encoder again. While you are doing backward pass through the encoder, you also have to add the KL loss.

### 00:08:03 · Speaker 4

And for the decoder training, one forward pass through the encoder decoder, get the output of the decoder, compute the reconstruction loss, one backward pass through the output of the decoder.

### 00:08:16 · Speaker 4

that completes training we

### 00:08:20 · Speaker 6

Hmm

### 00:08:21 · Speaker 3

Any questions on this?

### 00:08:29 · Speaker 3

Okay. So once this is trained, what do we do with it?

### 00:08:33 · Speaker 6

Hmm

### 00:08:39 · Speaker 6

is it not?

### 00:08:44 · Speaker 3

You can just write anything sir then it will score

### 00:08:48 · Speaker 6

Oh

### 00:08:56 · Speaker 6

inference with V

### 00:09:09 · Speaker 6

Okay, so post training, V I E can be used for two tasks, okay? The first task is

### 00:09:22 · Speaker 6

posterior inference

### 00:09:29 · Speaker 6

as I said in the

### 00:09:31 · Speaker 3

previous class what do you mean by posterior inferences given

### 00:09:36 · Speaker 3

a data point X

### 00:09:43 · Speaker 3

Okay. So let's call that as lakes.

### 00:09:47 · Speaker 3

test or something because it is not in the training data, okay?

### 00:09:52 · Speaker 6

Find the

### 00:09:56 · Speaker 6

responding

### 00:10:03 · Speaker 6

Latent vector

### 00:10:07 · Speaker 6

also called as embedding

### 00:10:18 · Speaker 6

This is what is called

### 00:10:19 · Speaker 4

plus

### 00:10:20 · Speaker 4

that is a test, okay? So this is what is called as posterior inference. I told you, right? Any latent variable model, one of the advantages is that once you try in a latent variable model, you can get an embedding corresponding to the given data point. That is what we do in all these encoder decoder based LLMs also, right? The the encoder will give you an embedding corresponding to data. Now how do you do that?

### 00:10:48 · Speaker 6

Hello

### 00:10:49 · Speaker 4

take the encoder

### 00:10:54 · Speaker 6

which is trained, okay?

### 00:11:00 · Speaker 6

star. So you pass X test to this. And what you get here is

### 00:11:10 · Speaker 3

μv star at x test.

### 00:11:16 · Speaker 3

to get sigma phi star

### 00:11:18 · Speaker 6

at X dash

### 00:11:23 · Speaker 6

This is what you get, right?

### 00:11:25 · Speaker 3

Now

### 00:11:25 · Speaker 6

Hello

### 00:11:26 · Speaker 3

the

### 00:11:29 · Speaker 6

embedding

### 00:11:35 · Speaker 3

of extra X test.

### 00:11:37 · Speaker 3

there are multiple options, right?

### 00:11:39 · Speaker 4

can be taken to be

### 00:11:44 · Speaker 4

mu phi star itself. So this itself can be taken as an embedding corresponding to H dash. This is one possibility. The other possibility is to sample an epsilon from

### 00:11:58 · Speaker 4

normal zero one okay

### 00:12:01 · Speaker 4

let's call this embedding one. normal zero one. and then take z test to be equal to let's call this epsilon t. epsilon t times

### 00:12:16 · Speaker 4

basically you do the reparameterization test plus

### 00:12:21 · Speaker 6

Move V star X test.

### 00:12:26 · Speaker 6

this now becomes

### 00:12:32 · Speaker 6

embedding for its test.

### 00:12:36 · Speaker 6

can be Z test also.

### 00:12:41 · Speaker 4

uh this let's call this embedding too. So you can get so for any uh data point right uh you can get an embedding this way. Uh just pass it through the encoder. You either take the the mean of the encoder uh itself as the embedding or you do a sampling outside of the neural network reparameterize and take that as an embedding. So now how do you use this embedding is up to you. You can use it for a class use it in a classifier. See what happens is Hello

### 00:13:12 · Speaker 3

we know that the

### 00:13:13 · Speaker 3

dimensionality of the test

### 00:13:23 · Speaker 3

you know that this is much much less than dimensionality of X test. So what can be done is you can train a classifier.

### 00:13:38 · Speaker 3

using Z test

### 00:13:41 · Speaker 3

right or do you can do arithmetic in the embedding space and all

### 00:13:45 · Speaker 6

All that right so

### 00:13:51 · Speaker 6

can say

### 00:13:57 · Speaker 6

is

### 00:14:04 · Speaker 3

Bangalore weather since last fifteen days had made has made everybody sick.

### 00:14:12 · Speaker 3

Z test can be used.

### 00:14:18 · Speaker 6

or

### 00:14:20 · Speaker 6

classification.

### 00:14:28 · Speaker 6

okay? Or like compression.

### 00:14:35 · Speaker 4

you can do contrastive learning on top of it etcetera.

### 00:14:39 · Speaker 4

We'll talk about this contrast learning later in the class, later in the course. So basically, you can use this embedding to whatever uh effect that you want. Okay, that's the idea. So this is called posterior inference. Any latent variable model, right? uh You can

### 00:14:58 · Speaker 4

get this meaning post training you can use the encoder to get the embedding corresponding to unseen data points I mean of course you can get embeddings corresponding to the training data as well entire data you can get the embedding take the trained encoder

### 00:15:14 · Speaker 4

pass the data through the trained encoder and you get the embedding and use it for whatever task downstream task that you would need. So that is about posterior inference using latent variable models.

### 00:15:30 · Speaker 6

Any questions on this?

### 00:15:39 · Speaker 6

Yeah, Shirisha

### 00:15:43 · Speaker 1

Yes sir. Sir, so when you said Z test can be used for classification, what kind of classification mean?

### 00:15:51 · Speaker 4

let's say that, let's say that that you know you have built a VAE on MNIST, right? Now, you want to try you want to train a classifier on MNIST. Typically what you do is you take the images and train a classifier on MNIST, right? So instead of doing that, you take the embeddings on the MNIST and you train a classifier using embeddings.

### 00:15:51 · Speaker 1

say that

### 00:16:19 · Speaker 4

Does it make sense?

### 00:16:20 · Speaker 1

ओके, सो बेसिकली वी आर ट्राइंग टू क्लासिफाई द क्लास ऑफ द इमेज, इज इट?

### 00:16:25 · Speaker 4

anything. So it doesn't matter, right? It can your input can be image or it can be text or anything, depending upon uh what sort of data you have. But the idea is that you can instead of using X test, you can use Z. So what I mean, more interesting question is what advantage do you get by using Z instead of X, right? Now the the answer to that is uh actually if you have learned a good encoder

### 00:16:55 · Speaker 4

decoder model, right? The the hope is that the embeddings that you have gotten is well clustered, you know, well behaved. Because in I mean, as I told you, in one of the earlier classes, these naturally occurring data will be in very high dimensional spaces and they will all be scattered, no, because of curse of dimensionality. They will not be well clustered. If you learn representation in a lower dimensional space, it will be much more clustered and classifiers would behave much better in the embedding space compared to the data spaces they hope.

### 00:17:32 · Speaker 4

Tell me this, in your assignment have I asked you to use these embeddings and build a classifier?

### 00:17:39 · Speaker 5

Yes sir

### 00:17:40 · Speaker 4

This is exactly what I have asked you to do, right? Train a VAE and then get the corresponding Zs and then use it in a classifier. And I think I have asked you also to compare this with a classifier that is built only on the data space also, right?

### 00:18:00 · Speaker 3

Yes sir

### 00:18:03 · Speaker 4

let me just open the assignment and see.

### 00:18:05 · Speaker 3

Yes

### 00:18:06 · Speaker 5

CNN West

### 00:18:09 · Speaker 4

I have asked you, right? Yeah, yeah. So that's what it is. So first you have to use a CNN and classify that. Classify the data and then use these embeddings and reduce the network size and simply use an MLP and see what happens on top of it.

### 00:18:27 · Speaker 4

Okay. Yeah, Sarvesh.

### 00:18:31 · Speaker 2

so for this uh parameter reparameterization so this is the sigma should be raised to half right because we need some standard deviation type component to be added. See that depends

### 00:18:34 · Speaker 4

Hmm

### 00:18:42 · Speaker 4

That depends on, yeah, that depends on what you are representing as sigma, no? I am representing that root of that itself as sigma. Depends, I mean that's just a scaling factor, right?

### 00:18:55 · Speaker 3

so we are actually getting standard deviation type thing

### 00:19:01 · Speaker 3

of the

### 00:19:01 · Speaker 4

That is what I'm saying, right? So now if you represent the output of your encoder as standard deviation, then you raise it to power of half. If I say that it's the variance, then you don't have to. Depends upon how do you see it, that's all.

### 00:19:13 · Speaker 5

Okay

### 00:19:14 · Speaker 4

Okay, Sanchit

### 00:19:17 · Speaker 5

Sir, is this the right time to ask that about variational inference? Like,

### 00:19:23 · Speaker 4

Ha, see this is this is posterior inference, okay? Posterior because what you are actually calculating here is you are calculating

### 00:19:34 · Speaker 4

p theta p p star of z given x right?

### 00:19:40 · Speaker 3

Yes

### 00:19:41 · Speaker 4

I mean technically speaking not P, it's the

### 00:19:46 · Speaker 4

I was going to say that this is

### 00:19:49 · Speaker 3

Q

### 00:19:50 · Speaker 5

Q B Star

### 00:19:50 · Speaker 4

Q star Q star Q phi star of Z given X correct? Right? Now this is inference definitely because given an X you are giving a Z okay? And this is posterior I mean technically speaking you can actually call this variational posterior

### 00:20:09 · Speaker 6

Insurance

### 00:20:23 · Speaker 6

variational posterior inference. Variational because

### 00:20:29 · Speaker 6

we don't have

### 00:20:36 · Speaker 6

access to

### 00:20:39 · Speaker 6

p theta star zee k one x. This is the true posterior distribution, right?

### 00:20:46 · Speaker 6

we are using

### 00:20:52 · Speaker 6

variation and distribution.

### 00:20:58 · Speaker 6

variational distribution which is

### 00:21:01 · Speaker 4

Q phi of Z given X

### 00:21:04 · Speaker 4

to approximate it. So that is why it's called the variational posterior. Okay. uh In fact, in your exam, I had asked you to uh start from the KL divergence between these two distributions and derive the elbow. Correct?

### 00:21:23 · Speaker 4

Do you remember that question?

### 00:21:25 · Speaker 3

Yes, yes sir.

### 00:21:26 · Speaker 4

I had told you that you start from the KL divergence between the variational distribution.

### 00:21:35 · Speaker 4

and this

### 00:21:39 · Speaker 3

right? And show that minimizing this will

### 00:21:45 · Speaker 3

boil down to the elbow objective that you optimize in VIE, correct?

### 00:21:48 · Speaker 4

Right

### 00:21:52 · Speaker 6

Yes sir

### 00:21:54 · Speaker 4

So this is exactly what it is, right? I mean you can actually see, see, the entire analysis that we did in V A E, uh was by saying that we want to maximize the log of

### 00:22:07 · Speaker 4

the data likelihood under the latent variable model, right? That's how we derived the ELBO. The entire story can be constructed via this route. Okay, it's only an algebra. You can you should just write this scale divergence and write this posterior in terms of the joint distribution between X and Z and marginal and then you get it. In fact, it's pretty easy. uh I hope that uh like a lot of you could get this, crack this.

### 00:22:35 · Speaker 4

Did you do that?

### 00:22:38 · Speaker 4

just have to write down the uh the KL definition of KL divergence and use Bayes' law and show it. It's not at all difficult, okay? Now yeah, so basically the reason I asked you that question is to make you appreciate this that it is called a variational model because while we want the true posterior distribution of Z given X because we do not have it, we approximate that using another distribution which is which we call the variational distribution which which represent

### 00:23:08 · Speaker 4

by Q phi of Z given X. So the objective is to make sure that the posterior of the true, I mean, yeah, posterior under the true model is going close to the variational posterior. And you minimize the KL divergence between them, that is the objective.

### 00:23:28 · Speaker 4

Okay. So now that's why you call this, I mean when you estimate Q phi of Z given X under a trained model, you call that as variation of posterior inference. Posterior because

### 00:23:42 · Speaker 4

because you are getting Z given X this is because posterior. uh inference because you do it under fee star post training.

### 00:23:54 · Speaker 4

Is this alright, Sanchit? So it's called variational posterior

### 00:23:58 · Speaker 4

inference.

### 00:24:01 · Speaker 5

ओके सर

### 00:24:03 · Speaker 4

Okay, so this is, I mean, we were talking about inference with V A E, right? One is to get the uh embeddings. The other thing that you can do with this is obviously...

### 00:24:17 · Speaker 4

data generation or sampling

### 00:24:19 · Speaker 6

because it's a generative model

### 00:24:32 · Speaker 6

data generation or sampling. How do you do that?

### 00:24:35 · Speaker 4

that take the decoder

### 00:24:38 · Speaker 4

See, this is exactly what happens in a language model also, okay? Encoder decoder based LLMs, exactly the same thing happens. The encoder is used for inference, okay? And the decoder is used for generation. Same thing with all encoder decoder models. Now you sample Z from normal zero one.

### 00:25:01 · Speaker 4

give it to the trained decoder.

### 00:25:05 · Speaker 3

which will take which will take Z and give your X

### 00:25:13 · Speaker 3

I'll give you X tab. So this is the

### 00:25:20 · Speaker 3

generated data point

### 00:25:26 · Speaker 3

Now, see, a true decoder, I mean, while training, decoder is trying to

### 00:25:32 · Speaker 4

take samples from Q phi of Z given X

### 00:25:36 · Speaker 4

Isn't it?

### 00:25:40 · Speaker 4

You get what I'm saying? See decoder is trying to see samples from Q phi of Z given X and give you give you sample from P theta of X given C. Right? But now you are sampling from normal zero one not from Q phi of Z given X.

### 00:25:55 · Speaker 4

Why would decoder help you?

### 00:26:01 · Speaker 4

Do you see the question?

### 00:26:03 · Speaker 5

because we are reducing the K L divergence between exactly

### 00:26:06 · Speaker 3

Exactly, right? Exactly. So now what happens is

### 00:26:10 · Speaker 3

post training

### 00:26:18 · Speaker 3

Q phi of Z given X, okay? would reduce

### 00:26:22 · Speaker 6

normal zero one

### 00:26:25 · Speaker 6

because of the

### 00:26:30 · Speaker 6

Kelt

### 00:26:33 · Speaker 6

In elbow

### 00:26:37 · Speaker 6

Therefore, therefore

### 00:26:41 · Speaker 6

Z coming from

### 00:26:46 · Speaker 6

Q phi of C given X is

### 00:26:54 · Speaker 6

equivalent to

### 00:26:57 · Speaker 4

C coming from normal zero one. In fact, I've asked you to do this also in your assignment. Okay? That once you train the decoder, you sample Z from normal zero one and then give it to the decoder. We get the generated data. Now, in a in an LLM, right, we will see that later. We will do what is called as conditional generation. Because all these uh GPT etcetera, what they do is they take an input and then gives you an output, right? It's it's not unconditional generation unlike in a VIA.

### 00:27:27 · Speaker 4

I mean you can also tweak the V A E to do conditional generation all you have to do is as I said we looked at conditional GAN right similarly you can do a conditional V A E just by appending another conditioning variable in terms of text embedding or one hot vectors right so but basically the idea is that once you train you take the trained decoder and then you can do sampling or data generation so now encoder becomes the inference model and decode for data generation

### 00:28:00 · Speaker 4

See, uh the idea is if you take uh let's say a naive auto encoder, okay? That has an encoder and a decoder.

### 00:28:14 · Speaker 4

X and X cap, okay? Now what happens is, uh let's say that it will give you Z. And you simply have a reconstruction task here.

### 00:28:28 · Speaker 4

Excuse me, so you have a reconstruction task here.

### 00:28:32 · Speaker 4

Now, this if you train a a nice auto encoder like this, okay? Now, post training, you can only use this auto encoder to do inference because you can take the encoder and given an X, it will give you a Z. But you can't do generation using this thing because the distribution of the latency

### 00:28:54 · Speaker 6

space is unknown

### 00:29:05 · Speaker 6

ಇನ್ನ ನೈವ್ ಆಟೋ ಎನ್ಕೋಡರ್

### 00:29:09 · Speaker 4

Okay. Now what do we do in a variational auto encoder is if you see that we will say that look I don't only want my I not only want my decoder to reconstruct data but I also want the distribution of the output of the encoder.

### 00:29:30 · Speaker 4

Okay, to follow

### 00:29:35 · Speaker 4

some distribution of interest so that once I train this I can sample from a known distribution and then use the decoder as a generative model.

### 00:29:46 · Speaker 4

Right? So now VAE, you can

### 00:29:48 · Speaker 6

C V A E

### 00:29:54 · Speaker 6

as

### 00:29:56 · Speaker 6

An auto encoder

### 00:30:02 · Speaker 6

which

### 00:30:05 · Speaker 6

regularization

### 00:30:11 · Speaker 6

on the latent space.

### 00:30:19 · Speaker 6

such that

### 00:30:25 · Speaker 6

the distribution of the latent space

### 00:30:38 · Speaker 6

should fall over caution

### 00:30:46 · Speaker 6

predefined distribution let's say. In this in general case it will be predefined.

### 00:30:57 · Speaker 6

cosine distribution.

### 00:31:03 · Speaker 6

is telling

### 00:31:03 · Speaker 4

Right? So, in an autoencoder what will happen is there's an encoder and a decoder you would say that okay the data has to be get encoded into some latent space and from the latent space you'll have to get back to the data space, right? In a variational autoencoder we'll say that okay we just do not want the data to be reconstructed we also want the latent space to follow a particular distribution of interest. Okay? So that why do we do this is because post training

### 00:31:33 · Speaker 4

we can sample from this distribution of interest and give it to the decoder and use it as a generative model.

### 00:31:41 · Speaker 4

Is this all right?

### 00:31:43 · Speaker 4

So that way, right, uh V A E can be seen as a regularized auto encoder, an auto encoder with a regularization on the latent space such that the latent space follow a particular distribution of interest. Okay. Yeah, Sanjit.

### 00:31:57 · Speaker 5

Sir, but the

### 00:32:01 · Speaker 5

the normal distribution that is a very like a very wide space right. So it's not possible that for every sample within this normal distribution we will get a like a proper image that is similar to the original data set. So like that that's where like we try to learn on the poles or the clusters.

### 00:32:19 · Speaker 4

clusters

### 00:32:21 · Speaker 4

See, uh

### 00:32:28 · Speaker 4

Why you can see this as a reconstruction plus a regularization. You should always remember how did we get to this objective. We got to this objective by minimizing the KL divergence between the model distribution and the true data distribution, correct?

### 00:32:42 · Speaker 5

model distribution into distribution. Correct.

### 00:32:44 · Speaker 4

we started how did we how did we get this get this was our elbow right? whatever I have written here is our elbow.

### 00:32:53 · Speaker 4

That is why I don't write the loss function of V A E as simply reconstruction plus K L, simply because I want you to appreciate where did this come from? This actually came from the elbow, right? Now what was that? That was the K L distribution, K L divergence between P X and P theta, that's what we started from.

### 00:33:14 · Speaker 4

Now doing all this, we are actually reducing the KL divergence between PX and P theta. So now if we have done it right, right? Then

### 00:33:25 · Speaker 4

No matter what this distribution is, you know, it can be normal or anything, the VAE has to sample from PX because we have technically reduced the KL divergence between PX and P theta.

### 00:33:40 · Speaker 4

Does that make sense?

### 00:33:43 · Speaker 6

ஓகே

### 00:33:44 · Speaker 4

because the entire model has reduced the KL divergence between P X and P theta. If you have done it right then this objective should lead you to sample data points.

### 00:33:55 · Speaker 3

PX

### 00:33:59 · Speaker 6

Okay

### 00:34:03 · Speaker 3

Ravindra

### 00:34:05 · Speaker 5

Yes, so in the assignment what we observe is the reconstruction loss is, I mean, decreasing pretty fast, but we we don't we see that the K L divergence, it's it's hard to reduce. I mean, it keeps generally increasing. So what's the...

### 00:34:12 · Speaker 4

That

### 00:34:17 · Speaker 4

correct. generally increasing. So what's correct? Correct. That happens. See that is because uh something uh which is called posterior collapse. So I'll talk about it. Uh okay so I'll come to that. So this is yeah this is what you what do you do in a knife VAE right? There are lots of improvisations that people have done over a knife VAE. I'll not talk about all of them. I'll only talk about like one of them which is the vector quantized VAE.

### 00:34:47 · Speaker 4

which is sort of state of the art VAE that people use, okay? Yeah, that is precisely because the observation that you have made in your assignment, okay? So there is something called posterior collapse in VAE, I'll talk about.

### 00:35:00 · Speaker 6

about it

### 00:35:10 · Speaker 6

collapse

### 00:35:13 · Speaker 6

in a naive AI

### 00:35:22 · Speaker 3

sort of related to the question that Sanjit asked. I'll tell you what happens is. See in a naive AI what's happening is.

### 00:35:31 · Speaker 3

Recall

### 00:35:35 · Speaker 6

that in a V A E

### 00:35:42 · Speaker 6

Now Q phi of Z given X, okay? Is

### 00:35:52 · Speaker 6

is forced to

### 00:35:56 · Speaker 6

go to normal zero one.

### 00:36:01 · Speaker 6

irrespective of okay

### 00:36:09 · Speaker 6

for all x

### 00:36:12 · Speaker 6

Isn't it?

### 00:36:12 · Speaker 4

See, now Q P of Z given particular X, this is what it means, no, X by conditioning it on X. This means X is equal to a particular X I, okay? Now for all X I, we want this to be equal to normal zero one in a V A E, because we are reducing the KL divergence between these two, right?

### 00:36:34 · Speaker 4

You understand? Now, okay, so is this clear to all of you that in a in a in a V A E, uh this Q P of Z given encoder distribution is forced to go to normal zero one for all X?

### 00:36:48 · Speaker 4

Okay, now what is the consequence of it? The consequence of this is that

### 00:36:54 · Speaker 4

Okay. um Do you people know of this this idea called bias variance decomposition? Bias variance trade-off?

### 00:37:05 · Speaker 5

No sir

### 00:37:08 · Speaker 4

Okay. See, uh whenever you regularize a model, okay? So if you take a learning model and you regularize the model, what will happen is, uh I mean you might be knowing it in a different name perhaps, right? See when you if you over regularize a model, what will happen is, it will why do you regularize a model? You'll regularize a model because you want to avoid overfitting, right? Now if you over regularize it, the model will go to the regime of underfitting. Now if you do not regularize it,

### 00:37:38 · Speaker 4

uh then the model will go to the regime of overfitting. It is this trade off between the underfitting and overfitting is what is called as the bias variance decomposition. So that is a topic by itself. That's exactly what happens here. Okay so I'll tell you the consequence of this is the following.

### 00:37:58 · Speaker 4

If

### 00:38:00 · Speaker 6

Q phi of Z given X, okay?

### 00:38:05 · Speaker 6

Approaches

### 00:38:11 · Speaker 6

normal zero one

### 00:38:14 · Speaker 4

for all x. all x. Okay? Think about it. Suppose your Q Q phi of Z given X approaches normal zero one for all x. What is the consequence of it? Then the decode

### 00:38:30 · Speaker 6

Hello

### 00:38:35 · Speaker 6

will

### 00:38:37 · Speaker 6

has a difficulty

### 00:38:41 · Speaker 6

will have difficulty

### 00:38:45 · Speaker 6

in reconstructing

### 00:38:51 · Speaker 4

Why do you think so? See, you see what is happening. Let's say that there are two x, okay, x one and x two, okay. Now, q phi of

### 00:39:03 · Speaker 4

Z given X one, okay? Is equal to Q phi of Z given X two.

### 00:39:11 · Speaker 4

and both of them are let's say normal zero one.

### 00:39:18 · Speaker 4

Right? Suppose this happens. If this happens, then if you get a Z one from

### 00:39:26 · Speaker 4

क्यू फी ऑफ जी गिवन एक्स

### 00:39:28 · Speaker 3

x one okay and z two from

### 00:39:37 · Speaker 3

Q P of Z given X two, right? So decoder

### 00:39:47 · Speaker 6

will not be able to

### 00:39:53 · Speaker 6

Differentiate

### 00:40:00 · Speaker 6

between G1 and G2. Because

### 00:40:04 · Speaker 3

both of them are coming from the same distribution.

### 00:40:10 · Speaker 6

You see this?

### 00:40:13 · Speaker 3

This is what is called as

### 00:40:14 · Speaker 3

Posterior collapse

### 00:40:16 · Speaker 6

Right?

### 00:40:23 · Speaker 3

which means that for

### 00:40:27 · Speaker 3

all x, okay? q phi of z given x is collapsing

### 00:40:38 · Speaker 6

to a particular distribution

### 00:40:46 · Speaker 6

by design

### 00:40:49 · Speaker 4

This is a consequence of elbow, right? We are not like we can't help. This is what is happening. So now since x one and x two or rather since for all x q phi of z given x is going close to one particular distribution. Right?

### 00:41:05 · Speaker 3

Okay

### 00:41:07 · Speaker 4

uh uh decoder will have difficulty in trying to reconstruct uh

### 00:41:15 · Speaker 4

or rather see if it if it can differentiate between each sample input sample it can reconstruct easily isn't it? If it cannot differentiate between the the latents corresponding to two different samples then it will have hard time reconstructing it.

### 00:41:31 · Speaker 4

Do you see this point?

### 00:41:32 · Speaker 3

Does all of you see this point? Any questions on this?

### 00:41:42 · Speaker 3

Yes, Nirmal

### 00:41:43 · Speaker 2

Sir, this happens only in naive VAE or

### 00:41:47 · Speaker 4

Correct. It happens only in IVI. Yeah. We have we'll see how to circumvent this problem. How do you solve this problem? Actually, you should have seen this in your in your assignments if you have started implementing it. Right? Yes. Yeah. So I'll tell you I'll tell you what happens. This is not what happens see in in in in the kind of architectures that we use, right? Reconstruction will not suffer. The other way happens. This is only half of the story. I'll tell you the other half. Maybe I can ask you the

### 00:41:48 · Speaker 2

pun zone

### 00:42:00 · Speaker 5

minus

### 00:42:17 · Speaker 4

I can I can take questions after this. This is the this is posterior collapse, okay? Now,

### 00:42:24 · Speaker 4

suppose, suppose

### 00:42:31 · Speaker 6

Okay? So I suppose the weight on the KL term is reduced.

### 00:42:49 · Speaker 3

what do I mean by that? the loss function in in V A E looks like this right? you have the reconstruction plus the K L term.

### 00:43:13 · Speaker 6

call this normal zero one only

### 00:43:24 · Speaker 6

Okay. Now,

### 00:43:26 · Speaker 4

This is how it is. I mean, in the naive implementation, both of these terms are equally weighted, right? So, there is another version of VIE called a beta VIE, okay, which is simply adding this beta term to the KL where your beta

### 00:43:40 · Speaker 3

is between zero and one.

### 00:43:45 · Speaker 3

Okay, now

### 00:43:51 · Speaker 3

So higher beta

### 00:43:51 · Speaker 6

right? corresponds to

### 00:43:55 · Speaker 6

More weight to KL

### 00:44:01 · Speaker 3

So this is this is

### 00:44:04 · Speaker 4

Beta V

### 00:44:06 · Speaker 3

Hello

### 00:44:07 · Speaker 4

improvisation on V A E called beta V A E. Higher beta corresponds to more weight to K L and vice versa, right?

### 00:44:15 · Speaker 4

So now let's say that let's come to this. Suppose I give more weight to KL, what will happen?

### 00:44:22 · Speaker 6

this may lead to posterior collapse. We already saw that.

### 00:44:35 · Speaker 3

Now if you have suppose I give very low weight to beta

### 00:44:40 · Speaker 3

What will happen? This means that more weight to reconstruction

### 00:44:50 · Speaker 3

more emphasis on reconstruction.

### 00:44:56 · Speaker 4

This means that the reconstruction happens very nicely, okay, because now the decoder can, uh I mean, see, this this implies, okay, lower beta implies, implies Q P of Z given X, okay, may not be equal to normal zero one.

### 00:45:15 · Speaker 4

for all x

### 00:45:17 · Speaker 4

Okay

### 00:45:18 · Speaker 6

This implies that reconstruction is easier.

### 00:45:28 · Speaker 6

reconstruction is easier

### 00:45:32 · Speaker 6

because, because, why is this?

### 00:45:38 · Speaker 6

Z1 and Z2, okay?

### 00:45:42 · Speaker 6

can be different

### 00:45:46 · Speaker 4

for

### 00:45:47 · Speaker 4

X one and X two. See if you have two different latent codes for different input samples then the decoder it will be easier for the decoder to use that latent information and then reconstruct it back right.

### 00:46:01 · Speaker 4

You see what I'm saying?

### 00:46:03 · Speaker 4

Now, okay, reconstruction is better if you reduce the weight on the KL divergence, but it should come with a cost. What is the cost? Can somebody think about it?

### 00:46:14 · Speaker 2

So there will be inference collapse.

### 00:46:17 · Speaker 4

meaning the the the generation will suffer however.

### 00:46:21 · Speaker 3

Yes

### 00:46:25 · Speaker 6

the generation quality will suffer.

### 00:46:38 · Speaker 6

with lesser beta. Why is this?

### 00:46:44 · Speaker 6

This is because

### 00:46:46 · Speaker 4

See, remember that what we do, what we do

### 00:46:49 · Speaker 3

Post Training

### 00:46:51 · Speaker 3

is that

### 00:46:54 · Speaker 4

we take p theta star, okay, we sample from

### 00:46:57 · Speaker 3

normal zero var

### 00:47:00 · Speaker 3

Now if

### 00:47:04 · Speaker 3

Q phi of Z given X, okay, is not

### 00:47:07 · Speaker 6

not normal zero one for all x

### 00:47:13 · Speaker 6

then

### 00:47:16 · Speaker 6

during

### 00:47:19 · Speaker 6

generation

### 00:47:23 · Speaker 6

Okay

### 00:47:23 · Speaker 3

sampling a Z from normal zero one

### 00:47:27 · Speaker 3

and passing through the decoder.

### 00:47:29 · Speaker 6

Sir

### 00:47:35 · Speaker 6

the decoder, okay? May not

### 00:47:40 · Speaker 6

Lead to

### 00:47:44 · Speaker 6

data samples

### 00:47:48 · Speaker 6

because why is this because

### 00:47:52 · Speaker 6

decoder

### 00:47:55 · Speaker 6

has seen

### 00:48:00 · Speaker 6

Q fee of G given X during training

### 00:48:08 · Speaker 6

which is

### 00:48:11 · Speaker 6

not equal to non-zero. That's fine.

### 00:48:16 · Speaker 4

understood? Now for the decoder to work you need Q P of Z given X to be normal zero one for all X. Okay? And if you make that then what happens is the reconstruction quality uh suffers while the generation becomes okay. So now there is a trade off between these two. In fact if you look at the beta V A E paper they will show you that with different values of beta you will see the trade off between

### 00:48:46 · Speaker 4

reconstruction and generate quality. uh what I suggest you is to implement this beta V A E in your assignments. When it's it's it it comes with no cost in the sense that you just have to have a weight factor on your KL divergence term and you experiment with different betas and you would see that if you have a large beta then reconstruction will become difficult. Okay? uh while the generation should will will be okay and if you uh reduce the beta

### 00:49:16 · Speaker 4

the reconstructions will be better, will the generation quality suffers. In fact, you might have seen, right? I mean, if people who have read the architecture on VAE, people you you might have seen people saying that VAE's results in blurry generation, right? blurry images. So that what is that? That is simply saying that if your Q phi of Z given X is not normal zero one for all X. What will happen is if you if there is a deviation between what

### 00:49:46 · Speaker 4

the decoder has seen during training and what it sees during inference, then the images that you generate will not match that of V theta and that's why quote unquote blurriness comes into generation quality. Now to avoid that if you make your reconstruction very strong, okay, by reducing the beta, then the generation quality suffers and there is this trade off between these two.

### 00:50:09 · Speaker 4

Okay

### 00:50:10 · Speaker 4

Okay, so now we will take questions. Uh, yeah, Vivek.

### 00:50:18 · Speaker 3

So will making beta zero convert this into auto encoder?

### 00:50:22 · Speaker 4

Exactly. It's a good observation. Yeah, if you make beta zero, then it will simply become a naive auto ID code.

### 00:50:29 · Speaker 4

lesser and lesser beta will always take it closer and closer to a naive auto encoder.

### 00:50:35 · Speaker 3

Okay

### 00:50:39 · Speaker 4

Yes, Miss Shirish

### 00:50:40 · Speaker 3

So can you, So can you hide this side panel?

### 00:50:44 · Speaker 4

Can you hide the side panel? How do I do that? This one? No.

### 00:50:48 · Speaker 3

Yeah

### 00:50:50 · Speaker 4

It opened up something else

### 00:50:50 · Speaker 3

Something else

### 00:50:51 · Speaker 6

So full screen is there on the top right

### 00:50:53 · Speaker 3

top right. This is

### 00:51:01 · Speaker 3

Why is this not moving?

### 00:51:10 · Speaker 3

So

### 00:51:13 · Speaker 6

write something it will start moving.

### 00:51:29 · Speaker 6

not recognizing at all.

### 00:51:37 · Speaker 6

What happened to this?

### 00:51:42 · Speaker 6

something happened

### 00:51:45 · Speaker 6

Mineral

### 00:51:45 · Speaker 4

I'm not able to see this. Can somebody tell me what happened with this?

### 00:51:51 · Speaker 1

sometimes it gets stuck sir

### 00:51:52 · Speaker 4

times

### 00:51:54 · Speaker 4

Oh

### 00:51:55 · Speaker 2

cos k l l

### 00:51:56 · Speaker 1

We can just

### 00:51:56 · Speaker 4

start

### 00:51:57 · Speaker 1

Close and open

### 00:52:00 · Speaker 4

age old solution. Restart.

### 00:52:03 · Speaker 3

solution to all problems.

### 00:52:05 · Speaker 4

Huh?

### 00:52:07 · Speaker 3

I said solution to all problems.

### 00:52:10 · Speaker 4

Oh yeah, it actually worked.

### 00:52:19 · Speaker 4

Okay, uh, let's take questions. Vivek, do you still have questions or is it done?

### 00:52:26 · Speaker 3

Uh, so,

### 00:52:27 · Speaker 5

Yes, I have a question. Suppose we change

### 00:52:29 · Speaker 4

change. Yeah, hold on. Just one other side thing. See, I have been calling all of you by your first name. I hope you don't mind.

### 00:52:39 · Speaker 4

I mean for all we know all of us are of pretty much same age or you might be like seniors to me so please don't mind and also feel free to call me Pratosh I don't mind so you don't have to call me sir. That's too British.

### 00:52:54 · Speaker 4

just just take my name right so. Yeah yeah. I mean I mean it I really mean it you can can feel free to call me Pratosh and I'll be happy. And also right I mean don't don't feel hurt because I I call your first names out okay. Because if I start calling you sir so many eighty five people right sir and madam so you don't know who is who. That's why that's where that's why the names are given anyway so. Anyway go on please.

### 00:52:55 · Speaker 5

name

### 00:53:22 · Speaker 5

Yes, so one question is, suppose we have a generation for a given Z and I change Z a little bit.

### 00:53:29 · Speaker 4

and

### 00:53:32 · Speaker 5

So will the output look just a little bit modified or

### 00:53:32 · Speaker 4

E

### 00:53:36 · Speaker 4

or yeah yeah yeah that is how it should it should happen right I mean that is how it should ideally happen. If you have trained it well with good architecture that is how it will happen see that is why in in Gyaans right I think did I include this in your assignment? Did I ask you to sample two Zs and then do interpolation between them? Interpolation. Yeah so did you see it changing smoothly?

### 00:53:42 · Speaker 5

Okay, fine.

### 00:53:54 · Speaker 5

population between them. Interpolation. Yeah.

### 00:54:00 · Speaker 5

Yes, yeah. That happens.

### 00:54:01 · Speaker 4

it happens. Yeah, it happens if you have if you have latent space or the embeddings that you have learned are good. In fact, when we come to some of these language models, right, you would see that, uh in in in this thing, right? uh what was that thing? Was it

### 00:54:17 · Speaker 4

was it but it was not which

### 00:54:20 · Speaker 4

Which was that, right? I mean that famous example where they show that man minus king embedding corresponding to word to vec. Word to vec, word to vec, yeah. So word to vec, right? That that should happen. So it should semantically make sense if you have learnt good embeddings.

### 00:54:27 · Speaker 3

Yeah, go to it

### 00:54:29 · Speaker 3

got to be

### 00:54:38 · Speaker 3

Okay

### 00:54:39 · Speaker 4

Right? So it depends. See that is why imposing this sort of constraint or rather a distribution on your latent space makes sense.

### 00:54:51 · Speaker 5

Okay

### 00:54:51 · Speaker 4

Yeah.

### 00:54:52 · Speaker 5

So and one more question but yeah it's I think it's not the maybe the right time to ask but if we have a picture from somewhere else and if we want to find its Z.

### 00:55:03 · Speaker 4

one

### 00:55:04 · Speaker 4

Hmm

### 00:55:05 · Speaker 5

How can we do that?

### 00:55:07 · Speaker 4

I told you, right? That's what you do. That's what the inference is. You take a pre-trained encoder or a VAE, pass it through the encoder. In fact, we will see that. See, you know this stable diffusion, right? All these the state of the art diffusion models, Imagine or whatever, the Googles and all these, they don't do diffusion models on the on on the image space. They do it on the latent space of a VAE, in fact, a VQVAE.

### 00:55:33 · Speaker 4

Once I talk about VQVAE I'll tell you that. So basically take the trained encoder, pass your data through the encoder, get the embedding and then use it. This posterior inference, that's exactly what what you've seen on on your screen.

### 00:55:49 · Speaker 4

You train your V A E on let's say image net and keep that, right? And given some new data, pass your data through the encoder, get the embedding and use it for whatever reason, whatever downstream thing that you would want to do.

### 00:56:06 · Speaker 3

Yes, thank you.

### 00:56:07 · Speaker 4

Okay. Uh, Sanchit?

### 00:56:12 · Speaker 5

Sir, in this exam, in this description for posterior collapse, uh so sir, it is since the normal distribution is a very large space and we we have a finite set of images like input images, so isn't it possible that we we get each Z that is unique for a given X?

### 00:56:36 · Speaker 4

if you recall our encoder is probabilistic.

### 00:56:42 · Speaker 4

We are not asking the encoder to give the Z, we are asking it to give the mean and variance.

### 00:56:48 · Speaker 3

Okay. Okay.

### 00:56:50 · Speaker 4

That's precisely why we make it probabilistic. It's not the Z that you get. You get the parameters of the distribution. And by construction, you are asking the output of this encoder, uh or the mean of this encoder to go to zero for all X. Even though the distribution, the support of the distribution is broad, what you are predicting is the mean and variance, not the Z itself.

### 00:57:15 · Speaker 5

Okay. And sir, one more question. I was a bit confused with the term variational Bayesian. Is it same as the variational inference we talked about?

### 00:57:16 · Speaker 4

one

### 00:57:18 · Speaker 4

um

### 00:57:25 · Speaker 4

Yeah, yeah, yeah. It's based because see auto encoding variational base is what they call the V I P people. It's it's based because again this if you had done this exercise that I had given you in exam. This one.

### 00:57:32 · Speaker 5

It's

### 00:57:40 · Speaker 6

Hmm

### 00:57:41 · Speaker 4

यू यूज़ बेस थ्योरम टू गेट दिस एल्बो, इज़ इट इट? करेक्ट। करेक्ट। दैट्स व्हाई इट्स कॉल्ड वेरिएशनल बेस।

### 00:57:44 · Speaker 6

Correct. Correct.

### 00:57:49 · Speaker 4

okay? Variational because you use a distribution a variational approximation to P theta of Z given X which is unknown.

### 00:57:59 · Speaker 4

Yeah

### 00:58:00 · Speaker 4

Okay, Indrajit

### 00:58:04 · Speaker 0

Yeah, what is the difference between reconstruction and generation?

### 00:58:10 · Speaker 4

reconstruction and generation. Okay. See reconstruction is that you take an x, pass it through the encoder and the and take that z, okay, that the encoder gives you. I mean when I say z it is this reparameterized z and pass it through the decoder, right? And you expect the output of the decoder to be exactly the same as that of the input, that is reconstruction.

### 00:58:35 · Speaker 3

Correct? It's the first term.

### 00:58:38 · Speaker 6

Yeah, but one thing is

### 00:58:38 · Speaker 3

Yeah, but one thing is

### 00:58:52 · Speaker 6

See, even after training,

### 00:58:54 · Speaker 4

you can take a data point that is there that you use for your training, pass it through the encoder, get its Z and pass it through the decoder and expect the decoder to give you the exact same X, isn't it?

### 00:59:08 · Speaker 4

See, post training, nobody is stopping you from using the training data and passing through the encoder and giving it through the decoder, isn't it?

### 00:59:17 · Speaker 0

Right

### 00:59:18 · Speaker 4

Yeah, so that is a reconstruction thing, isn't it?

### 00:59:22 · Speaker 0

Okay

### 00:59:24 · Speaker 4

So generation is see generation is that you take a Z and pass it through the decoder you get a new point that is not there in your training data. That's sampling of course. But you can do reconstruction on training data as well. How do you do it? Take it take the X. Okay? And pass it through the the training sorry the encoder get the Z. Take that Z pass it through the decoder and you expect the same X to come back.

### 00:59:50 · Speaker 0

Okay

### 00:59:51 · Speaker 4

Hello

### 00:59:52 · Speaker 0

Thanks

### 00:59:53 · Speaker 4

ओके. राघवेंद्र,

### 00:59:57 · Speaker 5

Yes sir, in the parameterized model for decoder we are

### 01:00:00 · Speaker 4

only considering the mu and we are saying that the sigma is identity

### 01:00:05 · Speaker 1

Correct

### 01:00:05 · Speaker 4

Can we also take sigma, I mean, and what implications that will have?

### 01:00:09 · Speaker 1

Yeah. You can, you can and then you have to again to generate you have to do another sampling, right, at the output of the decoder as well. Right? Typically sigma is not taken, but yeah, there's nothing that stops you from doing it that way. Typically it is not done.

### 01:00:27 · Speaker 3

Okay

### 01:00:29 · Speaker 1

Okay Harish

### 01:00:32 · Speaker 4

So depending on our use case, that is whether we are doing reconstruction or the generation. So we can change the training objective to have this KL divergence regularization term or not, right? That's that's that's

### 01:00:44 · Speaker 1

Correct. That's a that's a that's a good point. Yes. That is why you know it's it's like a knob. Beta V A E. This beta is a knob depending upon what do you want, right? uh in your what you are training your V A E for, you can tweak it the way you want. That's a good point. Yes.

### 01:00:59 · Speaker 4

So we can have two different models uh for two different types.

### 01:01:02 · Speaker 1

exactly. Yes, yes, yes, yes. Okay. So in fact, in your assignment, I encourage you to actually do that, you know, sweep over beta and see the effect of what happens on your VAE.

### 01:01:04 · Speaker 4

Okay

### 01:01:16 · Speaker 1

Yeah. Srinath.

### 01:01:19 · Speaker 3

Yeah, sir, my doubt is about this posterior collapse. So here, due to the KL divergence, we expect the mu and sigma outputted by the encoder to be close to zero and one, but not X. For all X. For all X.

### 01:01:33 · Speaker 1

for all x, for all x, correct.

### 01:01:35 · Speaker 3

but it should be exactly zeroed one.

### 01:01:38 · Speaker 1

I mean yeah if the training has happened properly yeah

### 01:01:41 · Speaker 3

Right? And so, is this somewhat of an adversary nature because if the KL divergence becomes zero, then the reconstruction laws will explode. And if it goes

### 01:01:52 · Speaker 1

So no it should not it should no right why should it explore? See as I think one of Sanchit was saying that uh I mean you are asking the asking it to make it Gaussian distribution zero mean unit variance for all x. But even within zero mean unit variance you have infinite support you can place your Z different places.

### 01:02:11 · Speaker 1

But practically what happens is because you have like limited capacity encoder decoder right all these E's would be placed on on on on on very close to each other and and discerning the difference between those two will become difficult to the decoder. There's no adversary here. See.

### 01:02:31 · Speaker 1

See, ideally if you have, see, if you have infinite capacity encoder and decoder, both the objectives can be achieved.

### 01:02:32 · Speaker 2

I

### 01:02:32 · Speaker 3

D

### 01:02:40 · Speaker 1

Isn't it?

### 01:02:42 · Speaker 3

because the encoder is technically not give as you said right it's not giving Z it is giving the parameters of. doesn't matter doesn't matter.

### 01:02:47 · Speaker 1

doesn't matter, doesn't matter. Let's say that it will do perfectly and it will go to zero mean and unit variance for all x. And suppose your decoder has infinite capacity.

### 01:02:57 · Speaker 1

Right? As long as for two X's exactly the same Z is not getting generated from the sampling, the decoder can do it. And also remember that the sample that the decoder sees as input, okay, is a sample that you get outside of the encoding.

### 01:03:19 · Speaker 1

Right? And also you do an averaging over it, no? See, you don't take one sample of Z and give it to the decoder, you take multiple samples of Z and give it to the decoder.

### 01:03:28 · Speaker 1

So that way if you have infinite capacity of encoder and decoder

### 01:03:32 · Speaker 1

Ideally, a VAE should do perfectly well. But since we have like finite capacity architectures, right? If you make your encoder to have same distribution for all X, decoder will have. In fact, that is one other experiment that you can see that keep everything constant including the beta, but only increase the architectural size of encoder and decoder and you will see better performance.

### 01:03:55 · Speaker 3

Okay

### 01:03:57 · Speaker 1

Huh?

### 01:03:58 · Speaker 1

Yeah, these are very good questions by the way. In fact, I received one comment from one of you. I mean, I don't want to know who it is, but because that's the whole point of it being anonymous. It said that, you know, you see you have spent so much time on on on on quote unquote basics, right? Now we only have these many classes and you know, you are you are not covering the syllabus and this happens with all courses in I I C etcetera and all that. sort of not so positive sentiment. But see the thing is

### 01:04:38 · Speaker 1

a good course, right, in in our opinion. I mean, good that the person said that this happens across the board in I I C. See, what we feel as as faculty in I I C is that we want to prepare you to you know, to to read some of these literature independently. So the idea is not to cover a lot of breadth. A lot of papers, you know, a lot of ideas at a surface level. The idea is to go sufficiently deep and make you

### 01:05:08 · Speaker 1

dependent so that you pick up any paper in the literature and then you can read it. So even if we don't quote unquote cover the syllabus, I don't know what syllabus is, you know, because none of the ISE courses will have any syllabus per se, especially these advanced courses. The idea is to, you know, make you think and and enable you with a lot of tools and arsenals of of tools such that such that you can you can start reading and appreciating and understanding things.

### 01:05:38 · Speaker 1

So, so I mean, what I was coming with this, I I I was reminded of that particular comment because all the questions that you are asking are very very relevant and and I I hope when I I suspect that that that you are you are able to ask some of these questions and appreciate these things in deep because we spent so much time on basics. What are these divergence metrics, you know, how do you carve bounds on things and how do you build models etcetera. I think that is what is valuable, isn't it? I think we can have this discussion maybe when we

### 01:06:08 · Speaker 1

when we have that hybrid class when you people meet me, okay? And I wanted to have that discussion as well, right? I mean, we have to plan for that. Post Diwali. So now that I'm talking about it, maybe we should

### 01:06:23 · Speaker 1

some dates. So second, how about

### 01:06:28 · Speaker 1

Can we do it on sixteenth itself?

### 01:06:32 · Speaker 1

The last class that we do, shall we do it hybrid? Can you people plan a visit to I I C on sixteenth of November?

### 01:06:44 · Speaker 1

Let's do it that way. So tentatively, let's keep it on sixteenth.

### 01:06:48 · Speaker 1

Okay. Again, we will do the exact same thing. I will do it at team's call and I will write it on my iPad and project on screens. But whoever wants to come to I I C, right, you are welcome. I'll arrange for a physical class and we will do it uh offline, you know, hybrid on sixteen.

### 01:07:09 · Speaker 1

So yeah, I think sixteenth is the only date because uh

### 01:07:17 · Speaker 1

nineteenth, twenty sixth we can do but twenty sixth is too short of a notice. uh but second is that Diwali week. I think lot of you will be traveling.

### 01:07:28 · Speaker 1

Yeah. Ninth, I don't know if you people come back. Ninth I have a have some other commitment that I can't travel to I C. I think sixteenth is the only day. Let's keep it on sixteenth. So tentatively sixteenth will be a hybrid class, okay?

### 01:07:44 · Speaker 1

plans for it. Okay, if you want to come, I mean there's absolutely no compulsion or anything, only if you want to

### 01:07:52 · Speaker 1

come and have a look at the campus and like meet me in person you are welcome to come there okay

### 01:07:59 · Speaker 1

Right. So this is about posterior collapse and this you know the the trade off between the reconstruction and generation. Now as I said people have addressed this problem in multiple ways and there have been a lot of efforts in improvising V A E models. So one of them is of course this beta V A E right where you have an explicit scale term on

### 01:08:29 · Speaker 1

uh the KL divergence to control between the the reconstruction and KL divergence is one thing. The other thing other class of methods okay. uh are

### 01:08:40 · Speaker 0

Where

### 01:08:48 · Speaker 0

Question is

### 01:08:55 · Speaker 0

Why

### 01:09:02 · Speaker 0

Why should we the latent prior

### 01:09:17 · Speaker 0

here some music that someone

### 01:09:18 · Speaker 1

guy on the street side so yeah not me. Why should we the latent prior P theta of Z okay? latent prior P theta of B fixed.

### 01:09:33 · Speaker 1

fixed to be normal zero one. See, all the while if you

### 01:09:38 · Speaker 1

Notice the in elbow the KL divergence was between

### 01:09:47 · Speaker 1

Q fee of Z

### 01:09:48 · Speaker 0

and P theta of Z. Right? Now what did we do in in in a naive VAE?

### 01:10:04 · Speaker 0

p theta of g is fixed.

### 01:10:08 · Speaker 0

at normal zero one, right?

### 01:10:12 · Speaker 0

which cause problems right which

### 01:10:17 · Speaker 0

cause the issue of posterior collapse.

### 01:10:28 · Speaker 0

So, a lot of people question

### 01:10:30 · Speaker 1

this assumption that why should we fix P theta of Z. Now, uh in fact, like my first PhD student from IIT Delhi actually worked on this. So his entire thesis was on uh optimal P theta of Z. So now the question that can be asked is

### 01:10:52 · Speaker 0

rather not question because I've posted question already call it as solution

### 01:10:59 · Speaker 0

is to learn

### 01:11:02 · Speaker 0

the latent prior.

### 01:11:09 · Speaker 0

learn the latent prior P theta of G

### 01:11:13 · Speaker 0

along with the model

### 01:11:18 · Speaker 1

along with the encoder decoder. So this is one of the key ideas. As I said, no, my first P.D. student, his entire work was on this. So learning the latent prior for encoder decoder models. Why should you fix it? You learn the latent prior itself. So what could be the best distribution that you have to impose on the latent space so that you get the optimality? Lot of work has been around this. So one notable thing is what is called as V.A.E.

### 01:11:48 · Speaker 1

which a variational

### 01:11:52 · Speaker 1

called Vamp prior okay

### 01:11:55 · Speaker 1

variational maximum a posteriori prior. Okay, this is one thing where the idea is roughly

### 01:12:04 · Speaker 1

to make

### 01:12:07 · Speaker 1

make P theta of Z, okay, a G M M. A Gaussian mixture model and learn it.

### 01:12:16 · Speaker 1

during training

### 01:12:20 · Speaker 1

is what they do. Okay, they make they make P theta of Z a Gaussian mixture model which is a flexible, more flexible distribution than a univariate Gaussian and learn it during training. Learn the parameters of the latent prior also, right? So what will happen is the elbow will have three parameters, right? So it was we had theta, phi and uh theta and phi, right? So there in all these methods you will have another parameter lambda. okay? where

### 01:12:54 · Speaker 1

P lambda of Z is the learnable latent prior.

### 01:13:01 · Speaker 1

So, now the optimization will be you you find theta star, you find phi star and you also find lambda star.

### 01:13:09 · Speaker 1

as the minimization you do a minimization over theta, do a minimization over phi, do a minimization over lambda and you have this elbow. So now this elbow will be a parameter of the encoder which is parameterized by phi, decoder parameterized by theta and you have the prior which is parameterized by lambda. So this is how it looks.

### 01:13:34 · Speaker 1

Okay? So not withstanding the details of Vamprior because that's not the state of the art, right? What uh people observed is that if you make P theta of Z a continuous distribution and make it a GMM, right? It's again you in in in problems like posterior collapse, I mean while it gives you some respite, that's not the best thing that you can do. You can do better than that which is the vector contest VEE which you will see. But the basic idea is that

### 01:14:02 · Speaker 1

along with learning the encoding decoding you also learn the parameters of the prior distribution on the latent space.

### 01:14:11 · Speaker 0

Idea clear?

### 01:14:23 · Speaker 0

Yeah, Raghavendra, we'll see one instance.

### 01:14:25 · Speaker 1

instillation of this just a second. We'll see one instillation of this which is the which is actually as I said no the state of the art VAE which is the vector quantized VAE. Even there the idea is to learn the latent space distribution of the latent space along with inputted decoder called the vector quantized VAE. Yeah go on Raghavendra.

### 01:14:44 · Speaker 4

Yeah so I mean uh what this uh this lambda distribution right what what it would try to come close to? Is it P theta P theta of Z given X or?

### 01:14:58 · Speaker 1

Exactly, exactly. So theoretically what what can be shown is the ideal prior right is it's actually the ideal prior is

### 01:15:11 · Speaker 1

can be shown to

### 01:15:12 · Speaker 0

equal to what is called as the aggregated posterior which is the integral of

### 01:15:24 · Speaker 0

This can be shown.

### 01:15:26 · Speaker 0

the ideal prayer that one would need to get the

### 01:15:29 · Speaker 1

the optimal elbow is what is called as this is called the

### 01:15:35 · Speaker 1

aggregated posterior. It can this can be shown. This is shown in the Vamprior paper.

### 01:15:42 · Speaker 0

Okay

### 01:15:44 · Speaker 1

Yeah. So what is this? You take all the encoding distribution, sorry. Take the encoding distribution, marginalize it with respect to the data distribution, okay? And that is what the ideal prior has to be. That is what is shown. Okay?

### 01:16:00 · Speaker 1

Again, you don't have to worry about it here.

### 01:16:09 · Speaker 1

Okay, so we will see one uh instantiation of uh this this idea which is as I said, no, state of the art VAE which is called the vector quantized VAE. Go on, Sanjit.

### 01:16:22 · Speaker 1

vector quant S B A E here.

### 01:16:22 · Speaker 2

Sir, but where we are learning the distribution on X, like it is it is the in maximum likelihood estimate format, right? P X given Z.

### 01:16:35 · Speaker 2

सो, हाउ विल वी बी एबल टू कैलकुलेट पी एक्स देन?

### 01:16:40 · Speaker 1

So we can't. See that's only a theoretical result.

### 01:16:44 · Speaker 1

whatever I wrote is only theoretical in the sense that the ideal prior on the latent space is the aggregated posterior is a theoretical result. That is what you try to approximate using G M M.

### 01:16:44 · Speaker 2

Okay

### 01:16:57 · Speaker 1

Okay

### 01:16:57 · Speaker 0

Okay

### 01:16:59 · Speaker 1

is discrete

### 01:17:01 · Speaker 1

and it is vector quantized.

### 01:17:05 · Speaker 1

in VQVAE

### 01:17:09 · Speaker 1

What I mean in fact the VQAE paper right the title of the paper is not vector quant as VAE they call it neural discrete representation learning that is the title of the VQAE paper. Neural discrete representation learning.

### 01:17:25 · Speaker 1

Okay. That's what the paper is. So basically what they do is the following. The motivation comes from the fact that they say that you see, uh all the uh naturally occurring data, right, can be compactly represented using some discrete amount of codes is what they call, what they say. Here is what what they mean by that, okay. So let's say that you want to represent speech signals using some latent space.

### 01:17:56 · Speaker 1

Now, human speech can be represented using a finite set of phonemes.

### 01:18:03 · Speaker 1

Okay, so what do you mean by phonemes? See, let's say that I, I say A and you people say A. So if you plot that speech signal of A of what I say and what you say, all of them look very differently. Okay, even the different instantiations of the same sound that I, one speaker say, will look differently, right?

### 01:18:28 · Speaker 1

In spite of that, no matter who says that sound, we perceive one particular idea called a, right, or a. That's a phoneme. So phoneme is an abstract idea that you perceive when you hear speech.

### 01:18:42 · Speaker 1

ओके। नाउ इन इंग्लिश लैंग्वेज, देयर आर ओनली अ फ्यू फाइनैट सेट ऑफ पोनीम्स दैट वुड रिप्रेजेंट द एंटायर लैंग्वेज।

### 01:18:51 · Speaker 1

Okay, so that is let's say I mean they have identified some fifty odd phonemes. And in Indian languages also you have about fifty, sixty sort around sixty phonemes. Okay. So now to represent language all you need are sixty codes, right, which correspond to each of the phonemes.

### 01:19:09 · Speaker 1

same thing can be said in in terms for for images also right? I mean if you want to represent a image any scene can be represented by saying things like okay there are how many regular

### 01:19:24 · Speaker 1

regular figures like rectangle or circles are present here and you know, uh like how many slant lines are here etcetera. So basically you can have a finite number of discrete discrete discrete descriptors which are latent codes that can be used to represent uh any kind of naturally occurring data. So that is the motivation.

### 01:19:48 · Speaker 1

Okay. So that's why they use a discrete latent space in a VQVAE. They they vector quantized and learnable. When we know why we should learn the latent space also, right? So it is learned.

### 01:20:03 · Speaker 1

learnable during training. So if you incorporate all these ideas in a V A E, right, you will get what is called as a vector quant as V A E. We will see what it is. Is the motivation sort of clear? Okay, let's let me write down the architecture and also the way it is done and then we can discuss.

### 01:20:25 · Speaker 1

So they make the encoder deterministic, not probabilistic. So it takes X I

### 01:20:33 · Speaker 1

Okay, it will give ZI.

### 01:20:35 · Speaker 1

Okay, so they call it

### 01:20:38 · Speaker 1

Z E of X I E corresponds to encoding

### 01:20:43 · Speaker 0

you get ZEEI, okay? Then

### 01:20:46 · Speaker 0

Suppose

### 01:20:50 · Speaker 0

there exists

### 01:20:54 · Speaker 0

सर योर स्क्रीन इज नॉट मूविंग फॉर मी एटलीस्ट।

### 01:20:59 · Speaker 3

Yes, it's not visible when you are writing.

### 01:21:03 · Speaker 3

leg is

### 01:21:04 · Speaker 3

that I guess.

### 01:21:06 · Speaker 0

that's all

### 01:21:10 · Speaker 3

how it's refreshed I suppose

### 01:21:14 · Speaker 0

let's see sometimes networks network gives issues

### 01:21:21 · Speaker 0

Suppose there there are

### 01:21:30 · Speaker 0

M

### 01:21:39 · Speaker 0

M latent vectors

### 01:21:43 · Speaker 0

of

### 01:21:47 · Speaker 0

हे डायमेंशन ईच

### 01:21:52 · Speaker 0

call them Z one, Z two, Z three up to ZM.

### 01:22:00 · Speaker 0

All the die

### 01:22:02 · Speaker 0

is in

### 01:22:03 · Speaker 0

R

### 01:22:04 · Speaker 0

mention

### 01:22:06 · Speaker 0

So now this

### 01:22:09 · Speaker 0

these form, right, a dictionary. Let's call this, this is a latent dictionary.

### 01:22:22 · Speaker 0

the latent dictionary, okay? What is done in VQVA is that you find

### 01:22:30 · Speaker 0

P

### 01:22:32 · Speaker 0

quantized version of the X I to be

### 01:22:39 · Speaker 0

V K

### 01:22:42 · Speaker 0

that we call the Z

### 01:22:45 · Speaker 0

J Star Okay

### 01:22:49 · Speaker 0

where J star is the one that is

### 01:22:54 · Speaker 0

the closest

### 01:23:00 · Speaker 0

between Z E of X I

### 01:23:05 · Speaker 0

and Z J you have

### 01:23:18 · Speaker 0

j to be equal to one to m

### 01:23:23 · Speaker 1

Does it make sense? See what we are doing is the following okay it's a two norm.

### 01:23:29 · Speaker 1

Now X I is a is an image or some data point that goes as an input to the encoder and it will give you some vector Z E. What I will do is

### 01:23:40 · Speaker 1

I will look

### 01:23:43 · Speaker 1

I will search for uh that ZM, okay, that ZK which is closest to the this output of this encoder.

### 01:23:55 · Speaker 1

okay? And replace that ZE with the with that particular vector in the dictionary.

### 01:24:03 · Speaker 1

you, you

### 01:24:04 · Speaker 0

to see what is happening

### 01:24:07 · Speaker 0

And that

### 01:24:10 · Speaker 0

goes as an input to the decoder.

### 01:24:24 · Speaker 0

So the quantized version of input goes as

### 01:24:33 · Speaker 0

the input to the T-code

### 01:24:36 · Speaker 1

is this clear what is happening? to all of you questions on this. So this is vector quantization so this operation right this operation is what is called as

### 01:24:47 · Speaker 1

vector quantization

### 01:24:54 · Speaker 0

Quickly, Nirmich

### 01:24:57 · Speaker 3

Sir, this latent dictionary is fixed, right? We have to pre-decide.

### 01:25:00 · Speaker 1

No, no, no, no, no, no, no, no, no, no, no, no, learnable. We'll, we'll see how to learn that. This is exactly what we learn.

### 01:25:03 · Speaker 3

see how

### 01:25:06 · Speaker 1

I mean, I told you that the latent space is also learnable, no?

### 01:25:11 · Speaker 0

Yes

### 01:25:12 · Speaker 1

So we will learn this.

### 01:25:14 · Speaker 0

Okay

### 01:25:16 · Speaker 1

Raghav

### 01:25:17 · Speaker 4

So going back to the the motivation right so you mentioned that we want to discretize it here. uh but if you see even in the V A E's right the um the number of Z that we fix can't we uh I mean look at it like some basis

### 01:25:32 · Speaker 1

there's no there's no discrete no there's no discrete no it has a distribution they don't have a fixed amount of Z

### 01:25:41 · Speaker 1

Okay, so these are

### 01:25:42 · Speaker 4

Okay, so these are these are these are very much fixed in the sense if you are choosing K dimensions then we know exactly what they are. No, no, no. Nothing beyond that.

### 01:25:46 · Speaker 1

They're fixed

### 01:25:49 · Speaker 1

No no no and nothing beyond that. It's it's not about dimensionality. It is about M. M latent vectors are fixed. M is a hyperparameter. You fix the number of vectors in your in your latent dictionary.

### 01:26:03 · Speaker 4

Okay, and once we have learnt them, we use them as the as the dictionary too. Correct. So we we don't really look at the entire spectrum.

### 01:26:07 · Speaker 1

Correct. So we

### 01:26:10 · Speaker 1

No. See, in fact, the, uh I mean, one question that might come to, come to the mind is, suppose you take an image and pass it through an encoder, right? So, uh if suppose there are, if I make M to be hundred, so there are, let's say that there are hundred vectors. Now,

### 01:26:31 · Speaker 1

Are hundred vectors good enough to represent a space that is as versatile as imagine it? Might be a question.

### 01:26:39 · Speaker 1

Right? Actually the way they do it is that they take a they make the latent space latent vector a two dimensional grid okay? Where each of these columns okay are k dimensional so you have

### 01:26:56 · Speaker 1

one to k. So what they do is they quantize each of these columns. So each column is quantized.

### 01:27:06 · Speaker 1

of the latent vector. You understood?

### 01:27:10 · Speaker 1

So that's how they represent. So basically what they do is the latent space will be a two dimensional thing. It's a K cross

### 01:27:20 · Speaker 1

P dimensional latent space.

### 01:27:25 · Speaker 1

okay? where each of the P vectors in the latent space is quantized using the dictionary.

### 01:27:34 · Speaker 1

You understood? So that way every image now will be represented using P vectors, okay, from the dictionary. That way it becomes versatile.

### 01:27:44 · Speaker 4

And are there any weights to each of these dictionaries?

### 01:27:47 · Speaker 1

No no no no no no no no no no no. So decoder now will see a k cross p dimensional uh I mean grid. See. When I said that it is q I mean z q of x i it is not one vector right it is the quantized version of this entire grid that's what the decoder sees as an input. That's what they do in the uh in the v q a paper. Is this clear? So that's how no it is not a single vector that is going as an input to the decoder. It is p number of vectors.

### 01:28:17 · Speaker 1

right? Where all these P vectors come from this predefined dictionary. And how do you find which of the vector from the P dictionary that you should take is you pass the XI to the encoder and encoder gives you a map, right? A grid of P vectors and each of the columns of this P dimensional grid you quantize using the dictionary and you give that as an input to the decoder.

### 01:28:45 · Speaker 4

But where is the variation variation coming from? I mean randomness coming here because if you have chosen a fixed set of P K vectors, right? I mean K size vectors, the output would always be the same or?

### 01:28:45 · Speaker 1

but

### 01:28:57 · Speaker 1

No no, during training of course, right? You take those P vectors and then you try to reconstruct it.

### 01:29:03 · Speaker 4

Correct, Okay.

### 01:29:04 · Speaker 1

Okay

### 01:29:04 · Speaker 1

Now the question is how do you use this for generation, right?

### 01:29:08 · Speaker 4

Okay, okay.

### 01:29:09 · Speaker 1

Uh that is a question that I'll answer later. Okay yeah sure. Right now see we are see the way uh the template is define the architecture right and train it and then you do the inference. I'm defining the architecture and we'll we have still not trained it. Let us train this and then we'll do the inference. But it's a valid question. How do you generate from a VQVI is a valid question. But did all of you understand what's happening right in terms of architecture and training? Any questions on that?

### 01:29:10 · Speaker 4

Okay, yeah, sure. Right now,

### 01:29:22 · Speaker 4

Yeah

### 01:29:41 · Speaker 2

सर, हियर फॉर अ गिवेन एक्स आई, वी विल रिसीव ओनली वन वेक्टर ज़ेड ई ऑफ एक्स आई, राइट?

### 01:29:48 · Speaker 1

That is what I'm saying. So for images what they do is, say this is a

### 01:29:54 · Speaker 1

working offline an error occurred.

### 01:29:57 · Speaker 1

I don't know what error occurred.

### 01:30:00 · Speaker 1

See input will be a let's say a four hundred cross six hundred image okay. Okay. Output will be a let's say thirty two cross

### 01:30:12 · Speaker 1

fifty dimensional vector. Okay, where thirty two is your K and fifty is your P. What will be done is all of these V I's, okay, will be in thirty two dimensional space.

### 01:30:28 · Speaker 1

What will be done is that each of these thirty two dimensional vector fifty vectors will be quantized using the dictionary. And the input of this will also be a thirty two cross fifty dimensional grid. Do you see that? It's not one vector it is a grid.

### 01:30:48 · Speaker 1

And each vector in that grid is quantized using the dictionary. That's how they do it.

### 01:30:58 · Speaker 1

Is this all right?

### 01:31:00 · Speaker 2

Sir, in in the name, uh, V A E, we used to get the mu and sigma vectors. See, I told

### 01:31:06 · Speaker 1

See, I told you, you look at this, right? I said that it's a latent space that is discrete and vector quantized and learnable. You should also say that the encoder is deterministic. It is not a probabilistic encoder.

### 01:31:22 · Speaker 2

No no sir I am talking about the dimension. So in in the naive V A E the mu E we we used to get one mu per dimension right like for six hundred four hundred cross six hundred image we will be getting the mu vector of size four hundred cross six hundred right.

### 01:31:25 · Speaker 4

So

### 01:31:41 · Speaker 1

No, no, no, no, no, definitely not. See, I've been telling that multiple times, right? This is a K dimensional thing.

### 01:31:49 · Speaker 1

if if you are uh

### 01:31:52 · Speaker 2

Okay, okay, like

### 01:31:54 · Speaker 1

Haven't you implemented V I E yet? See this is a K dimensional thing.

### 01:31:57 · Speaker 2

No sir I got confused I got confused

### 01:32:00 · Speaker 1

This is k dimensional, this is also k dimensional assuming that it is a diagonal matrix. Told this multiple times.

### 01:32:07 · Speaker 1

Got it?

### 01:32:08 · Speaker 0

Okay

### 01:32:09 · Speaker 1

it is one mu with a k dimensional thing because see this lies in k dimensional space right it is z z is in k and therefore mu is also in k dimensions

### 01:32:21 · Speaker 0

ओके

### 01:32:22 · Speaker 1

Okay, any other questions on the architecture of V V I?

### 01:32:27 · Speaker 1

Okay, so now we will have to train this.

### 01:32:28 · Speaker 0

Right, training with UAE.

### 01:32:41 · Speaker 0

Now the objective

### 01:32:44 · Speaker 1

is again the elbow, right? It will have two parameters. It will have the encoder decoder parameters and also this lambda parameters. Note that lambda parameters are Z one to Z M themselves.

### 01:32:57 · Speaker 1

Isn't it? Now, the lambda parameters are Z one to Z M themselves, right? Now the objective here

### 01:33:05 · Speaker 0

is

### 01:33:10 · Speaker 0

you simply do a reconstruction task.

### 01:33:18 · Speaker 0

Hello

### 01:33:18 · Speaker 1

And there is this other thing which is reduce the KL divergence between the output of the sorry reduce the the not the KL divergence the norm between the

### 01:33:31 · Speaker 0

output of the encoder

### 01:33:37 · Speaker 0

and the quantized version of it.

### 01:33:41 · Speaker 0

That's all. This is all the objective, it's very very simple.

### 01:33:48 · Speaker 0

right? This you optimize this with respect to so what is happening here is that

### 01:33:55 · Speaker 0

the gradients

### 01:34:02 · Speaker 0

X I. Look at Z E of X I.

### 01:34:15 · Speaker 0

decoder. This will be ZQ of

### 01:34:19 · Speaker 1

of X I. This will be X I cap. So now you have here Z one through Z M, right? Now, once to learn the encoder, of course, the there is a forward pass like this.

### 01:34:33 · Speaker 1

and

### 01:34:33 · Speaker 0

there is a simple reverse pass, right?

### 01:34:36 · Speaker 0

with the reconstruction term.

### 01:34:43 · Speaker 0

with respect to fee. This is what you do.

### 01:34:47 · Speaker 0

Okay

### 01:34:50 · Speaker 0

to learn the

### 01:34:51 · Speaker 0

of course for the decoder

### 01:34:52 · Speaker 0

also you do the same thing

### 01:34:54 · Speaker 0

to learn the latent space what

### 01:34:56 · Speaker 0

what you should do is

### 01:34:57 · Speaker 0

you should take the gradients of

### 01:35:18 · Speaker 0

at an dictionary

### 01:35:20 · Speaker 0

Okay

### 01:35:22 · Speaker 0

have to take the gradient of

### 01:35:27 · Speaker 0

this particular term

### 01:35:36 · Speaker 0

with respect to G itself and then back propagate.

### 01:35:39 · Speaker 1

See, Z you can take here

### 01:35:43 · Speaker 1

We know how to take gradients with respect to parameters, right? We can also take gradients with respect to vectors themselves. You see Z one to Z M, okay? Actually, you have to take it with respect to all Z I's here, you know, Z J's. Where Z J belongs to dictionary.

### 01:36:03 · Speaker 1

take the gradient with respect to uh the dictionary vectors themselves and then back propagate.

### 01:36:10 · Speaker 1

from the output. from the output, okay? till the uh till this space, till the uh see you see this as another layer sort of, right? in the neural network, this is a dictionary.

### 01:36:26 · Speaker 1

the gradients will flow from the output of the decoder till here. This is how it and this is how you update the gradients. So now what will happen is your

### 01:36:39 · Speaker 1

Z J you have to do it like vector by vector wise. G J T plus one will be Z J T randomly initialize that minus some alpha times

### 01:36:52 · Speaker 0

the gradient of the elbow which is this term

### 01:37:02 · Speaker 0

with respect to

### 01:37:04 · Speaker 0

C G

### 01:37:09 · Speaker 0

This is all right. This is how you do it. This is how the latent vectors are learnt.

### 01:37:21 · Speaker 0

an

### 01:37:21 · Speaker 1

questions on this. Otherwise it is simply a an auto encoder training. You have the encoder decoder, you train both the encoder decoders through back propagation. The one extra thing is you learn the latent dictionary vectors themselves by doing a back propagation through the latent dictionaries.

### 01:37:40 · Speaker 1

Is this all right? Any questions on this?

### 01:37:43 · Speaker 1

Reserve you try na VQVI. Go on.

### 01:37:47 · Speaker 4

Yeah, so I mean, is it, can we see it like we are trying to find some basis vector of the data during the training?

### 01:37:52 · Speaker 1

there's no during the training. It's not basis for data, no. It's a it's a you can say that it's the basis for the representation space of data.

### 01:38:04 · Speaker 4

Okay

### 01:38:04 · Speaker 1

data is being represented in the space

### 01:38:08 · Speaker 1

for that you are trying to learn the basis.

### 01:38:11 · Speaker 4

and the number of vector that we choose would be a hyperparameter.

### 01:38:15 · Speaker 1

M is a hyperparameter.

### 01:38:17 · Speaker 4

thank you

### 01:38:18 · Speaker 1

Okay, so now this is how you train it. So now

### 01:38:22 · Speaker 0

once you try this you will have to do inference

### 01:38:40 · Speaker 0

first thing that we'll do is

### 01:38:43 · Speaker 0

posterior inference.

### 01:38:48 · Speaker 0

or embedding extraction, right? This is what we call as embedding.

### 01:38:59 · Speaker 0

just straightforward, right? You have the encoder always

### 01:39:02 · Speaker 1

for the posterior inference. You take the encoder. Its test goes as an input to the tri-and encoder. You will get a Z E X test.

### 01:39:16 · Speaker 0

the embedding

### 01:39:22 · Speaker 0

for X test

### 01:39:25 · Speaker 0

is simply

### 01:39:28 · Speaker 0

vector quantized version of Z that's all. J equal to

### 01:39:35 · Speaker 0

through M you search for

### 01:39:42 · Speaker 0

closest

### 01:39:44 · Speaker 1

version in the quantize space. I have written it as a star because learned it already.

### 01:39:50 · Speaker 1

This is the embedding. Is it all right?

### 01:39:54 · Speaker 1

So as I said typically what happens is right you take a a grid of

### 01:40:00 · Speaker 1

A cross P, right? And quanta is

### 01:40:07 · Speaker 1

Each column

### 01:40:10 · Speaker 1

that is what is done. Now this embedding right is the state of the art that is used in all the text to image generating models.

### 01:40:22 · Speaker 1

they use they take a VQVAE that is pre-trained on ImageNet. They take this embedding and use it for and and train a diffusion model on top of these embeddings. Nobody starts I mean like the state of the art right people don't build diffusion models on data or rather in the image space. They do it on the the embeddings that are gotten by a VQVAE trained on ImageNet.

### 01:40:50 · Speaker 1

Is this all right?

### 01:40:54 · Speaker 1

questions on this? How do you do posterior inference?

### 01:41:00 · Speaker 0

Great. Sir, what is, what is P here? I mean, what should it be?

### 01:41:00 · Speaker 1

Great Sir

### 01:41:01 · Speaker 1

Yeah

### 01:41:05 · Speaker 1

hyperparameter, that's a hyperparameter that is typically used. uh I mean if you look at the VQVI paper, right? The first there is VQVI one and VQVI two. I think in VQVI one they take P to be lesser and then they show that P should be, in fact you can actually make it a three dimensional thing also, no? Where you make each of it uh a map. Depends, so that that depends upon uh the kind of

### 01:41:33 · Speaker 1

network hyperparameter choice that you make.

### 01:41:37 · Speaker 0

is. Thank you.

### 01:41:39 · Speaker 1

and you replace each of those columns by the I mean you vector quantize each of those columns that's the point. Okay. Two we have to do generation. See uh

### 01:41:51 · Speaker 1

VQVIs are not typically used for generation. As I said, right? They are only they are mostly used for embedding extraction, okay, or inference. But you can also do generation from it, generation or sampling from VQVI.

### 01:42:12 · Speaker 0

See, one thing that is to be noted is that because

### 01:42:16 · Speaker 0

since the latent space is vector quantized.

### 01:42:21 · Speaker 0

space is discrete

### 01:42:29 · Speaker 0

write it as quantized

### 01:42:36 · Speaker 0

Monetized, Okay.

### 01:42:39 · Speaker 0

one does not know the distribution of it. You see that?

### 01:42:47 · Speaker 0

doesn't know the distribution of it.

### 01:42:59 · Speaker 0

Right? See,

### 01:43:00 · Speaker 1

Now V I E, we know that the latent space follows normal zero one. That's why post training we can take sample from normal zero one and give it to the decoder and we will get the output right. Here, we don't know what the distribution of latent space is. So that's why what is done typically is that you the way it is done is

### 01:43:21 · Speaker 0

first

### 01:43:25 · Speaker 0

extract

### 01:43:29 · Speaker 0

embeddings

### 01:43:35 · Speaker 0

of training data

### 01:43:44 · Speaker 0

You understood? So what is done is given

### 01:43:48 · Speaker 0

x one through x n from the training data, okay? Get

### 01:44:00 · Speaker 0

Z one through Z. We're using different notation.

### 01:44:04 · Speaker 1

for that no? what shall we use? it's called the Z cap one through Z cap n where

### 01:44:18 · Speaker 0

C cap I is the

### 01:44:22 · Speaker 0

embedding

### 01:44:26 · Speaker 0

for

### 01:44:26 · Speaker 1

X I, okay? Get this via encoding, encoders. So once by posterior inference, you get the embeddings. Then what is done is, fit a

### 01:44:42 · Speaker 1

GMM

### 01:44:45 · Speaker 1

actually what you can do is fit a generative model or train a generative model on top of these embeddings.

### 01:44:54 · Speaker 1

is the first step. is the second step. You try na

### 01:45:00 · Speaker 1

generative model

### 01:45:02 · Speaker 1

on

### 01:45:04 · Speaker 1

C one cap through C N cap. Now this generative model can be a G M M. Okay? Or in the in the V Q A paper they train what is called as a pixel C N N.

### 01:45:18 · Speaker 1

which is an auto regressive model. Auto regressive generative model we will see the auto regressive model later next in the course. So basically you try to you try in a generative model on top of the latent embeddings that you got from the encoder okay then

### 01:45:37 · Speaker 0

Now sample

### 01:45:41 · Speaker 0

Zee New, Zee Cap New from

### 01:45:46 · Speaker 0

the

### 01:45:48 · Speaker 0

generating model on Z one cap to Z n cap, okay?

### 01:45:56 · Speaker 0

then pass

### 01:45:58 · Speaker 0

C cap new through the decoder.

### 01:46:02 · Speaker 0

to get

### 01:46:07 · Speaker 0

Did you understand this?

### 01:46:14 · Speaker 0

the problem is unlike in a

### 01:46:15 · Speaker 1

यू डोंट नो व्हाट द डिस्ट्रीब्यूशन ऑफ द लेटेंट स्पेस इज, करेक्ट?

### 01:46:22 · Speaker 1

because it is discrete. Therefore, what they do, what is done is that once you learn the encoder decoder, you take all the training data and pass it through the encoder and get the corresponding embeddings. Now that becomes a new data set. Okay? On the embedding data set, you learn a generative model.

### 01:46:42 · Speaker 1

Now you know how to sample from the latent space of the VQVAE, right? And therefore what you can do is, once you learn a generative model on the latent space, then you sample from it and give it to the decoder and decoder should give you a new data point.

### 01:46:59 · Speaker 1

This is all right. In fact, people say that, I mean, there's also our experience that training a generative model on the latent space of a VQVAE is very difficult, and that's why VQVAE is typically not used as a generative model itself. What is done is, VQVAE is used for posterior inference. You get the embeddings and use train a diffusion model on top of those embeddings. Right? uh Yeah, in fact, this is exactly, in fact, this is what is done in a stable diffusion. and all that. What they do is

### 01:47:33 · Speaker 1

actually this is what is written no you try

### 01:47:36 · Speaker 0

Uh, uh

### 01:47:41 · Speaker 0

it can be a G M M or it can

### 01:47:43 · Speaker 1

and we have PixelCNN

### 01:47:48 · Speaker 1

or it can be a diffusion model. That's exactly what is done in stable diffusion.

### 01:47:55 · Speaker 1

So basically, you take a VQVAE, get its embeddings, learn a generative model on the latent space, okay? And generate a new sample in the latent space of the VQVAE and give that new generated latent sample through the decoder and get the X new. That is exactly what is done in in stable diffusion.

### 01:48:19 · Speaker 1

and all this imagine that you have Google's this thing right? All the I think it's J E N

### 01:48:29 · Speaker 1

it's that Google's engine, right? All of these commercially available things, that's exactly what they do. They take a VQVAE

### 01:48:39 · Speaker 1

try in a generative model on the latent space of the VQVAE and generate a new sample from the latent latent distribution of VQVAE and give it to the decoder to generate the image. And what you see is the image. But the generation is happening in the the latent space.

### 01:48:56 · Speaker 1

ओके संजीत

### 01:49:00 · Speaker 2

So if you are training a G M M on these embedding Z one to Z Z one hat to Z one Z N hat. So what shall be the mean and variances for a like a like individual Gaussian model?

### 01:49:17 · Speaker 1

That is what is learned in a G M M. In a G M M you don't fix the mean and variance of of of the individual Gaussians. That's what you learn.

### 01:49:26 · Speaker 1

You learn the mean and variance of individual components in a G M M. You're using E M.

### 01:49:34 · Speaker 0

Okay

### 01:49:35 · Speaker 1

Okay, so yeah, forget about GMM right now, right? You can, I mean, as I said, no, in stable diffusion, etcetera, the model that is the generative model that is used on the latent space is actually a diffusion model, which we will see right now.

### 01:49:52 · Speaker 1

Okay, so if you understood good, so this is the

### 01:49:57 · Speaker 1

end of V A E's in one form because the diffusion models are also V A E's but yeah so in the naive form this is the end of V A E's

### 01:50:07 · Speaker 1

See, I have not asked you to implement a VQVI in your assignment because I thought it would be too much. But yeah, if anyone of you have some bandwidth and time, I'd be happy to see you implementing VQVI, that would be nice if you can do that.

### 01:50:19 · Speaker 3

V2V

### 01:50:20 · Speaker 3

You have asked

### 01:50:22 · Speaker 1

How I

### 01:50:24 · Speaker 3

Yes, yes, we have VQV with discrete latent space.

### 01:50:30 · Speaker 1

so cruel of me. Then do it. Okay, I think then you should do it. Yeah, you can you should do it.

### 01:50:41 · Speaker 1

Okay, so great

### 01:50:44 · Speaker 1

I thought I didn't expect this to take so much time but it's worth it. It's fine.

### 01:50:49 · Speaker 1

Okay, so shall we take a break? We're talking for one and a half hours, one hour forty five minutes now.

### 01:50:58 · Speaker 1

Uh as I said I need to leave like five minutes to eleven. Uh so let's not take a long break let's take a short break ten minutes. Ten twenty we'll be back.

### 01:51:11 · Speaker 1

Is it okay?

### 01:51:13 · Speaker 0

Yes

### 01:51:13 · Speaker 1

Do you need fifteen minutes? Ten minutes is enough I suppose.

### 01:51:20 · Speaker 1

Yeah, let's, yeah, so please come back at ten twenty because we'll start diffusion models. Don't miss the introduction. That's very important. Yeah,

### 01:51:21 · Speaker 0

That's a nice sign

### 01:51:29 · Speaker 0

reconvene in about ten minutes. See you.

### 02:07:46 · Speaker 1

सर यू आर ऑन म्यूट इफ यू हैव सांगे समथिंग। सर यू आर ऑन म्यूट।

### 02:07:47 · Speaker 2

Sir you are on mute

### 02:07:49 · Speaker 2

Yeah, so you are on mute.

### 02:07:52 · Speaker 0

Oh my

### 02:07:52 · Speaker 3

I got I got scared. Okay, I'm sorry, yeah. So I was just speaking on mute.

### 02:08:04 · Speaker 3

Okay. So the next topic that we will see in this course is about DDPMs also called as expanded as denosing diffusion probabilistic models.

### 02:08:22 · Speaker 3

I'm audible now, right?

### 02:08:24 · Speaker 2

Yes sir you are audible

### 02:08:26 · Speaker 3

Okay

### 02:08:28 · Speaker 3

Okay. So now the uh uh state of state of the art generative models uh in all the vision language models that you see today, right, are based on D D P M's. Uh they are

### 02:08:44 · Speaker 3

uh neither B A E's nor uh GaNs, right? I mean the people have uh moved on uh on to these these new class of models uh on called D D P M's, denosion diffusion diffusion probabilistic models. Uh we'll study that. Uh so basically right it it's um

### 02:09:11 · Speaker 3

DDPMs

### 02:09:14 · Speaker 3

So the plan is that I will set up the problem today in this class. Okay? uh and then we will look at the the rigorous math and all that in the next coming classes.

### 02:09:27 · Speaker 3

there is one tutorial by

### 02:09:32 · Speaker 3

you what that is. It's a very nice tutorial. I'll put it on the chat now.

### 02:09:44 · Speaker 3

actually very very good, okay? I encourage all of you to follow that and go through it. It will cover everything uh that I'll be doing in this class, okay? I found it very it's a it's a hundred page tutorial, it's almost like a short book but it is extremely good. Let me just put it here.

### 02:10:10 · Speaker 0

You want me to put it on teams also that also I can do.

### 02:10:32 · Speaker 0

teams

### 02:10:40 · Speaker 0

think it's already there.

### 02:10:44 · Speaker 0

Oakham

### 02:10:49 · Speaker 3

So whatever I put in here in the meeting chat it will appear on the teams is it? Yes.

### 02:10:54 · Speaker 0

Yes, yes sir. Yes sir.

### 02:10:55 · Speaker 2

Yes

### 02:10:57 · Speaker 3

Okay. That's good. Tutorial on diffusion models.

### 02:11:07 · Speaker 2

Please have a look at it. This is pretty much what I cover, okay?

### 02:11:14 · Speaker 0

Sure sir

### 02:11:15 · Speaker 2

So, it's a good tutorial, have a look at it. Okay.

### 02:11:19 · Speaker 2

So, um

### 02:11:22 · Speaker 2

Basic

### 02:11:23 · Speaker 3

basically the idea is the following right D D P M is is actually

### 02:11:26 · Speaker 0

actually is a special case of V A E.

### 02:11:39 · Speaker 0

Okay. Now, you can actually see DDPM as a special case of VAE with the following properties.

### 02:12:03 · Speaker 0

So if

### 02:12:03 · Speaker 2

If you look at this tutorial, right? He has actually derived the elbow, also done reparameterization, everything. Maybe I will just show you that once.

### 02:12:11 · Speaker 0

Hold on

### 02:12:29 · Speaker 2

Do you see my screen?

### 02:12:32 · Speaker 0

Yes sir

### 02:12:34 · Speaker 3

You see it's very very recent, no it has come out on tenth of September. It's pretty good. So they start with V A E's, okay? So there is this encoder decoder definition of latent variable, uh and uh yeah, he also talks of G M M. See it's this thing very much uh aligns with my narrative as well. I mean you should trust me when I say that I did not build my narrative looking at this because I've been teaching this course since three years. This this man has

### 02:13:04 · Speaker 3

use that very similar narrative as what I do, okay? So then he goes to the evidence lower bound constructing the evidence lower bound. And decomposition of the log likelihood as elbow using the variational distribution. Interpretation of elbow.

### 02:13:22 · Speaker 3

reconstruction and prior matching terms.

### 02:13:30 · Speaker 0

Okay, so optimize

### 02:13:31 · Speaker 2

in VAE

### 02:13:36 · Speaker 2

reparameterization. Right?

### 02:13:42 · Speaker 3

These are exactly the things that I did. I I don't know, right? Maybe somebody who looked at my notes, but that was not public at all. I don't know how. But anyway, exactly the thing that I did, okay? So V A E encoders.

### 02:13:56 · Speaker 3

and deparametrization tricks in high dimensions.

### 02:14:00 · Speaker 3

scale divergence between two Gaussians.

### 02:14:04 · Speaker 3

and this V A E training and then they completed this concluding remark. Then they come to uh D D P M's. This is a very good tutorial okay so please have a look at it. It will actually give you uh a lot of insights about V A E and also the D D P M's that I'll be covering. Okay? So and also as I said right uh thankfully it is very very similar to the kind of story that I have told you the narrative that I have built. So that very nicely aligns with what we have done. So please have a look at it.

### 02:14:40 · Speaker 3

a minute.

### 02:14:43 · Speaker 0

bring my charges now

### 02:15:21 · Speaker 3

Okay. So DDPM is actually a special case of VAE with the following properties. Okay, so we will see all those properties one by one.

### 02:15:32 · Speaker 3

Hope you can hear me and see my screen. Correct?

### 02:15:37 · Speaker 0

Yes sir. Yes sir.

### 02:15:38 · Speaker 3

Okay

### 02:15:41 · Speaker 3

Okay. See, one thing is

### 02:15:42 · Speaker 2

that

### 02:15:45 · Speaker 0

the

### 02:15:51 · Speaker 0

The first thing is that there are

### 02:15:57 · Speaker 0

multiple latent spaces.

### 02:16:08 · Speaker 0

Okay, unlike

### 02:16:15 · Speaker 0

one latent space in a VAE

### 02:16:24 · Speaker 0

there are um yeah so this is hierarchical

### 02:16:34 · Speaker 3

graphical, okay? So there are multiple latent spaces here unlike in a V A E where there is one latent space. So basically what happens in a V A E is that start from the data space, okay? Project to the latent space and from the latent space you get back to the data space, right? In a this is a V A E.

### 02:16:54 · Speaker 3

Okay. In a D D P M diffusion model what happens is start from X. Get to the first latent space Z one and from the first latent space you get to Z two. Get to Z three. And some

### 02:17:10 · Speaker 3

ZN let's call it, right? And from ZN

### 02:17:18 · Speaker 0

get back to Z n minus one retrace it back

### 02:17:36 · Speaker 0

Do you understand this?

### 02:17:37 · Speaker 3

Hello

### 02:17:38 · Speaker 3

Right, instead of having one latent space, you have multiple latent spaces in a hierarchical fashion.

### 02:17:45 · Speaker 3

Is it all right?

### 02:17:47 · Speaker 3

So now why do we do that is that because see

### 02:17:53 · Speaker 3

encofit like this. Start from data, let's say that you have a very high dimensional data. Projecting, the motivation is that projecting it on to a latent space in one step and trying to compress it, making it compact in one step might be very difficult for the encoder. Right? So typically, projection from the data space to the latent space is the encoding process and from the latent space back to the data space is the decoding process, right? Similarly, you have hierarchical encoding.

### 02:18:24 · Speaker 3

and you have a hierarchical decoding in a D D P M. Is this idea clear? So as I said no we will write rigorous math and we will concretize everything that we do eventually but yeah so high level is this clear?

### 02:18:40 · Speaker 2

सर, कैन यू कमेंट ऑन द डायमेंशन ऑफ जी वन, जी टू, जी थ्री?

### 02:18:44 · Speaker 3

we'll do that. we'll do that. we'll do that. one thing at a time.

### 02:18:48 · Speaker 3

hierarchical thing. The second thing that you do is that the

### 02:18:57 · Speaker 0

dimensionality

### 02:19:01 · Speaker 0

of the latent space.

### 02:19:05 · Speaker 0

of all the latent spaces

### 02:19:18 · Speaker 0

same as that of the data space.

### 02:19:32 · Speaker 0

So

### 02:19:43 · Speaker 0

Again

### 02:19:43 · Speaker 3

typically what happens in a V A E is that dimensionality of the latent space is much less compared to that of the data space, right? But in a D D P M, the dimensionality of the latent space is exactly same as that of the data space.

### 02:19:59 · Speaker 3

Okay? That is the second property. The third property

### 02:20:03 · Speaker 0

that is used is

### 02:20:09 · Speaker 0

encoding

### 02:20:14 · Speaker 0

encoding process.

### 02:20:17 · Speaker 0

Yes

### 02:20:20 · Speaker 0

Not learnable

### 02:20:25 · Speaker 0

but fixed

### 02:20:30 · Speaker 0

Right?

### 02:20:35 · Speaker 0

the Markov process

### 02:20:42 · Speaker 0

See

### 02:20:43 · Speaker 2

In a VAE what do we do? So VAE

### 02:20:47 · Speaker 2

what we do is q of q phi of z given x, okay?

### 02:20:53 · Speaker 2

is learned, right?

### 02:20:57 · Speaker 0

via elbow

### 02:21:01 · Speaker 0

Here

### 02:21:06 · Speaker 0

q of g given x

### 02:21:09 · Speaker 0

is non-learnable

### 02:21:10 · Speaker 0

is fixed. So you

### 02:21:12 · Speaker 0

see that fee

### 02:21:13 · Speaker 0

is there's no fee here

### 02:21:25 · Speaker 0

Do you understand?

### 02:21:27 · Speaker 0

is not learnable.

### 02:21:32 · Speaker 2

The encoding process is defined using a Markov process.

### 02:21:36 · Speaker 3

there is nothing to learn here.

### 02:21:40 · Speaker 3

is all right. So that implies that only decoding

### 02:21:45 · Speaker 3

only the decoding decoder

### 02:21:47 · Speaker 2

is learned.

### 02:21:49 · Speaker 2

There's no one decoder. Decoding process is learned.

### 02:21:58 · Speaker 3

So now if you incorporate all three of these properties, right, which is that there are you take hierarchical latent spaces and you match the dimensionality of the latent space to that of the data space and you make the encoding process a fixed one but not learnable, then the resulting V I E is called D D P M, that's all it is.

### 02:22:19 · Speaker 3

The rest is only algebra and mathematical details. So what we will do is we will incorporate these properties into a V A E and we will write down the uh

### 02:22:32 · Speaker 3

elbow for this sort of a VAE and when we optimize that and we do the algebra we will end up having the loss functions for a DDPF.

### 02:22:44 · Speaker 3

Okay? So that's why you know I taught Gyaans first and then came to VAEs and then we are going to DDPM because DDPM is a special case of VAE with these properties. Any questions on this?

### 02:22:56 · Speaker 1

Sir, what does Markov process mean? Just a random process or

### 02:23:01 · Speaker 3

Yeah, I'll tell you. See, for now, think of it like a like I mean I'll write all the equations and it will be clear. Right? So basically what what what do I mean by Markov process is that start from the data space, right? You go to the first latent space, from first latent space you go to the second latent space, from the second latent space you go to the third latent space and so on, right? By Markov process I mean that if you take the t-th latent space, okay? It only depends on T minus first latent space. And it does not depend on anything else.

### 02:23:37 · Speaker 1

Okay, understood. Time based.

### 02:23:40 · Speaker 3

हा, दिस नो टाइम पर से हियर बिकॉज़ इटरेशन। हा, इट्स नॉट इवन इटरेशन, राइट? यू कैन कॉल इट एस डिलेटेड स्पेस इंडक्स।

### 02:23:42 · Speaker 1

Iteration

### 02:23:48 · Speaker 1

understood. Yes.

### 02:23:49 · Speaker 3

When you can call it time if you want, I mean you can if you want to see that as start from the data, you go the first time instant, you go to the first latent space, second time instant, you go to the second latent space and so on.

### 02:24:01 · Speaker 3

Okay. Any questions on this? On on on the high level formulation?

### 02:24:08 · Speaker 3

या संजित

### 02:24:10 · Speaker 1

सर, सो हेयर आर वी सेइंग दैट वी आर नॉट टेकिंग द डेटा बैचेस बट वन डेटा पॉइंट एट अ टाइम?

### 02:24:18 · Speaker 3

See, it still do everything on a batch level. See, every every analysis that we do is for one data point, right? Because doing it on a batch is only one other summation at the outside. Correct. All the V I E analysis, we did it for one data point. So now this is for one data point. Everything that I'm doing is for one data point, okay?

### 02:24:23 · Speaker 1

every

### 02:24:32 · Speaker 1

Correct

### 02:24:41 · Speaker 1

Okay, no sir, like

### 02:24:42 · Speaker 3

Even for VI

### 02:24:43 · Speaker 1

Like we are saying at time like at one time we we reached the first latent very latent variable and at the next time we reached the the another latent variable. So...

### 02:24:43 · Speaker 3

like

### 02:24:57 · Speaker 1

that that part like I was not clear.

### 02:25:00 · Speaker 3

one there's no I I said there's no one time. See in a V A I wrote it here right? What do you do in a V A E? Start from the data point, get to the latent space using encoding and get back to the data space. Now in a D D P M you start from one data point, go to the first latent space, from first latent space you go to second latent space, from second latent space go to third latent space and so on. That's all.

### 02:25:25 · Speaker 3

We are doing it for one data point. I mean, of course, everything that we do, we'll do it over batches. uh But yeah, so but analysis we do for one data point, right? All the elbow etcetera, we do it for one data point. Assuming that we only have one data point and you just put a summation outside data.

### 02:25:28 · Speaker 2

Hmm

### 02:25:30 · Speaker 2

Hello

### 02:25:42 · Speaker 1

And sir, this encoding, is it probabilistic still?

### 02:25:46 · Speaker 3

It is probabilistic but fixed.

### 02:25:49 · Speaker 1

probabilistic but fixed.

### 02:25:50 · Speaker 3

not learnable. By fixed I mean learnable. We'll write the equations that will become more clear. Yeah.

### 02:25:56 · Speaker 3

Okay, so let us get to the math now.

### 02:26:03 · Speaker 0

Any other questions on this?

### 02:26:07 · Speaker 0

questions, let's

### 02:26:13 · Speaker 0

one

### 02:26:25 · Speaker 0

unfortunately

### 02:26:25 · Speaker 3

Unfortunately, the community has used a different set of notations than VAE. So I will use the same notation as there as as it is there in the papers and the other tutorials. So it's a weird notation. Please bear with me on that. So data

### 02:26:45 · Speaker 2

is represented

### 02:26:51 · Speaker 2

using x not

### 02:26:52 · Speaker 3

Okay

### 02:26:55 · Speaker 3

So what used to be I'll just write the things that we were doing earlier also earlier using some other color. This was our X. Okay?

### 02:27:07 · Speaker 2

and

### 02:27:12 · Speaker 2

Latent space

### 02:27:14 · Speaker 2

is represented using

### 02:27:17 · Speaker 3

x one x two to xn

### 02:27:23 · Speaker 3

X capital T. Please note that this has this is not the data points that we had. As I said it is unfortunate because this is a very very non-standard notation. Okay so let's call this T.

### 02:27:39 · Speaker 3

Latent space is typically represented using Z, okay? But DDPM community, they represent that using X one two.

### 02:27:49 · Speaker 3

x capital T and data is represented as x naught. So this is what we used to call

### 02:27:57 · Speaker 3

Z one, Z two

### 02:28:00 · Speaker 0

to C T. Okay? I'll write this not to be confused.

### 02:28:11 · Speaker 0

with previous notations.

### 02:28:20 · Speaker 0

where

### 02:28:24 · Speaker 0

X one through X N were data points.

### 02:28:33 · Speaker 3

Okay, is that okay? Because see now from from now to the end of DDPMs, we'll be using this new notation. So now let me clarify. X not is the data point. And also note that all that we are doing is for one data point, so we'll do it for a single data point. X one.

### 02:28:53 · Speaker 3

x two

### 02:28:56 · Speaker 0

till X T R

### 02:29:02 · Speaker 0

latent vectors.

### 02:29:09 · Speaker 0

latent vectors, corresponding

### 02:29:12 · Speaker 2

into x not

### 02:29:14 · Speaker 2

Is this okay? So now the the encoding process is that you start from X not, go to X one and then from there

### 02:29:23 · Speaker 0

X2

### 02:29:30 · Speaker 0

This is the encoding process.

### 02:29:37 · Speaker 0

This is

### 02:30:02 · Speaker 0

latent vectors of same dimensions

### 02:30:15 · Speaker 0

Is this all right? Notation wise.

### 02:30:27 · Speaker 2

Yeah.

### 02:30:28 · Speaker 0

Yeah

### 02:30:28 · Speaker 3

yeah. please get used to this notation because as I said no very very non standard notation but that's what the community uses. I am not changing it. So just to ensure that that that notationally it is correct consistent across

### 02:30:50 · Speaker 3

don't know, no, this guy uses exactly the same

### 02:30:54 · Speaker 2

terminology as I do I will show you this

### 02:30:57 · Speaker 2

such a serendipity

### 02:31:07 · Speaker 0

Is my screen visible?

### 02:31:12 · Speaker 2

Yes sir

### 02:31:13 · Speaker 3

Look at this, no?

### 02:31:15 · Speaker 3

x not it is the original image which is the same as x in v a e. x t is the latent variable which is same in z in v a e.

### 02:31:24 · Speaker 3

ओके, एक्स वन एंड एक्स टी माइनस वन दे आर इंटरमीडिएट स्टेट्स और इंटरमीडिएट, दे आर आल्सो लेटेंट वेरिएबल्स बट दे आर नॉट

### 02:31:32 · Speaker 3

white Gaussian, yeah, that is okay. Yeah. So I strongly recommend all of you to go through this, okay? So I mean, of course,

### 02:31:42 · Speaker 3

in parallel to what what we have been doing but yeah so it's very consistent with what my narrative is and also the notations. Is the notation clear now? Please note that the dimensionality of all of these latent vectors are exactly same as that of the data space. I'll write that maybe.

### 02:32:04 · Speaker 3

prime of x not

### 02:32:07 · Speaker 3

Same

### 02:32:07 · Speaker 2

I am of I am of

### 02:32:11 · Speaker 2

T for T in

### 02:32:15 · Speaker 2

one through capital T. So note that X naught is your data vector.

### 02:32:22 · Speaker 0

Is this clear?

### 02:32:24 · Speaker 0

Is the notation clear?

### 02:32:31 · Speaker 0

Okay. Now, we will define the

### 02:32:41 · Speaker 0

encoding process

### 02:32:46 · Speaker 3

in DDPM

### 02:32:48 · Speaker 3

also I'll tell you why is it called a denosing diffusion probabilistic model. We'll we'll not leave anything out, okay? So but yeah, we'll I'll give you the easiest narrative first and then I'll connect every dots, don't worry, okay? Let us define the encoding process in DDPM. So now what is encoding? That projection from X to Z is the encoding process, right? This is the encoding process. How is it done in in a in a DDPM is that it is done in a Markovian way. What does that mean? मीन्स दैट यू मेक योर एक्स वन व्हिच इज द फर्स्ट लेटेंट वेरिएबल टू बी इक्वल टू

### 02:33:29 · Speaker 2

alpha not times x not.

### 02:33:33 · Speaker 2

plus one minus alpha not times

### 02:33:39 · Speaker 2

Epsilon

### 02:33:44 · Speaker 3

where epsilon is coming from normal zero one. This is the definition of encoding in a D D P M. Okay? So similarly X two is alpha one times X one plus one minus alpha one times

### 02:34:05 · Speaker 3

So let's call this as epsilon one or epsilon not and this as epsilon one.

### 02:34:11 · Speaker 3

So actually they are all samples from the same normal distribution you are doing different samplings that's all. So on. In general you have X Tth latent vector is given by alpha T times it's T minus one plus one minus alpha T times

### 02:34:33 · Speaker 3

some epsilon t where epsilon t is coming from normal zero one.

### 02:34:40 · Speaker 3

This is the encoding process. This is the fixed encoding process. You see that there is nothing learnable here. This is probabilistic, but there is nothing learnable.

### 02:34:51 · Speaker 3

Is this clear?

### 02:34:51 · Speaker 1

t minus one right alpha t minus one and

### 02:34:56 · Speaker 1

as per the general X to V capital

### 02:34:59 · Speaker 3

Yeah, yeah, yeah, yeah, yeah, yeah, yeah, I'll do that. I'll write that.

### 02:34:59 · Speaker 0

Yeah yeah yeah

### 02:35:08 · Speaker 3

um

### 02:35:11 · Speaker 2

Is this still Marco process?

### 02:35:12 · Speaker 3

Right

### 02:35:13 · Speaker 3

It is a marker process. Just a second, I just want to be consistent with the notation. Just a second, I'm just looking at that. P one forty.

### 02:35:25 · Speaker 3

This is alpha T

### 02:35:27 · Speaker 2

Okay

### 02:35:29 · Speaker 2

people generally write this as alpha t.

### 02:35:38 · Speaker 2

This is alpha one

### 02:35:41 · Speaker 2

is alpha two

### 02:35:42 · Speaker 3

again doesn't matter but just want to be consistent so where

### 02:35:47 · Speaker 3

where alpha one through alpha

### 02:35:53 · Speaker 2

R, right? R fixed scalars.

### 02:36:02 · Speaker 2

between zero and one, okay?

### 02:36:05 · Speaker 0

epsilon index as well sir

### 02:36:08 · Speaker 3

epsilon index. Epsilon index is okay, I mean, yeah. So, see, epsilon, I can write it as epsilon every time. It's just samples from a normal distribution, right? There is nothing, uh, like sacrosanct about this one, two, etcetera. But okay, fine, you can call it epsilon T.

### 02:36:27 · Speaker 3

So is this is this clear? Is this all right? Do you understand what's happening? What is happening is that you take the data point, okay? uh See this can be seen as some noise, right? When you take some noise, scale it, add it to the data point. So that will give you the first latent vector. Okay? Then you take that first latent vector, okay? uh take some noise, scale it, add it, and then you get the second latent vector and so on.

### 02:36:57 · Speaker 3

So this is whatever I have written here, right? This

### 02:37:01 · Speaker 3

actually a first order

### 02:37:06 · Speaker 2

Markov

### 02:37:08 · Speaker 2

process

### 02:37:12 · Speaker 0

its Gaussian transitions. Because the noise that we are adding is Gaussian.

### 02:37:23 · Speaker 0

and what is the spelling of

### 02:37:26 · Speaker 2

Transition Trans

### 02:37:28 · Speaker 2

Hello

### 02:37:31 · Speaker 2

T.I.T.I.O.N. is a

### 02:37:35 · Speaker 2

or S I O N

### 02:37:37 · Speaker 0

SIT SIT

### 02:37:38 · Speaker 2

SITI

### 02:37:40 · Speaker 3

ITI O

### 02:37:44 · Speaker 3

with Gaussian transitions. Okay. So basically what is happening is right you can see this as like this suppose we start with an image.

### 02:37:53 · Speaker 3

Okay. So this is x naught. What are we doing? We are just taking some

### 02:37:59 · Speaker 3

coefficient noise with the same dimensions, okay? Adding it to this, of course you scale it with alpha and add it with that. So you get

### 02:38:12 · Speaker 2

so-called noisy version, this will give you the first latent space, right? And then you add

### 02:38:21 · Speaker 2

another noise and this is alpha two and you get

### 02:38:25 · Speaker 3

image which

### 02:38:28 · Speaker 3

more noise and so on, right? So keep doing it. And there's a result that would say that if you keep doing this at X T with sufficiently large T, this X T, right? X T will follow a normal distribution zero one. So this is called the stationary distribution of a

### 02:38:46 · Speaker 2

Marco Chain

### 02:38:54 · Speaker 2

Right so if you create a marko chain like this it will go to a

### 02:39:03 · Speaker 2

normal

### 02:39:04 · Speaker 3

is what is known. Okay, so hold on, let me just show you a picture.

### 02:39:11 · Speaker 3

this is how you create the encoding process. This is the encoding process of a Marco chain. Let me of a of a DDPM. Okay, let me just show you this.

### 02:39:20 · Speaker 3

I mean of course your assignment will be one of your third assignment will be on this so you will implement all this and appreciate it.

### 02:39:29 · Speaker 3

Do you see my screen?

### 02:39:32 · Speaker 2

Yes sir

### 02:39:33 · Speaker 3

This is what I'm talking about. Starting from X not, you create a sequence of latent variables by adding noise.

### 02:39:45 · Speaker 3

Okay. So the picture is not

### 02:39:45 · Speaker 1

Sir, the picture is not zoomed in yet. Come again? That screen was not, it was not going to.

### 02:39:48 · Speaker 3

Come again?

### 02:39:51 · Speaker 3

you see this here?

### 02:39:53 · Speaker 1

Yeah, now we can see.

### 02:39:54 · Speaker 3

this is the process, right? You start from X naught, yes, keep adding that noise and you get a

### 02:40:03 · Speaker 2

the encoding process. Is this all right?

### 02:40:05 · Speaker 0

Hmm

### 02:40:10 · Speaker 0

Yes sir

### 02:40:15 · Speaker 2

Okay

### 02:40:15 · Speaker 3

Okay

### 02:40:17 · Speaker 3

Okay, so I think this is a good time to stop. So please again look at this and read my look at my notes, huh? So we will continue from here from the next class. So I'll have to leave now.

### 02:40:30 · Speaker 3

Uh okay, so the summary is that a DDPM is a VAE, a hierarchical VAE with multiple latent spaces with the property that the dimensionality of the latent space is exactly equal to that of the data space and the encoding is a fixed process. It's there's nothing learnable. What you do is you take the

### 02:40:50 · Speaker 3

data and create a Markov chain by adding Gaussian noises and that will give you the latent embeddings. So what do you do with it and how does this become a this thing a generative model and all that we'll see in the next class. So basically what we do is we will create a decoding model and we will write the elbow that we were writing for VAEs and then derive a loss function for it. That is what we'll do in the next class. Please have a read at that that that tutorial.

### 02:41:20 · Speaker 3

that I have shared. And also my handwritten notes is also there. There also I have done it. And yeah, and look at my notes and come prepared for the elbow and look at V A E's, okay? Next class we will do the maths for the diffusion models. Is that alright?

### 02:41:35 · Speaker 3

Again, you know, thank you for being accommodative. Okay, so and sorry about moving everything one hour before. So you have a quiz now, please wait, let me just call Chandan.

### 02:41:45 · Speaker 0

and then

### 02:42:06 · Speaker 0

can you not pick up

### 02:42:09 · Speaker 0

Chandan

### 02:42:10 · Speaker 3

I am done with the class

### 02:42:14 · Speaker 3

Yeah, so can you please join that link? Students are here and then conduct the quiz.

### 02:42:20 · Speaker 3

So, so I will ask the students to wait, just join there and you can conduct the quiz.

### 02:42:21 · Speaker 2

um

### 02:42:24 · Speaker 2

request

### 02:42:28 · Speaker 3

No no no I just completed because I have to leave now. Yeah. uh So the thing is see one other thing right if after the quiz if students have some time they can spare you can maybe just take a tutorial or rather just do some I mean uh do that exam thing.

### 02:42:31 · Speaker 2

Yeah

### 02:42:48 · Speaker 3

I see. Okay, no problem. You can conduct the quiz and then leave, okay? Okay, okay. Okay, so students are waiting, so you can please come online and

### 02:42:59 · Speaker 3

Oh, thank you.

### 02:43:01 · Speaker 3

Yeah, okay, so I just spoke with him. Chandan will be here in about two-three minutes and please take that quiz and then you can leave. We will meet next week.

### 02:43:10 · Speaker 1

सर, द नेक्स्ट क्विज इज़ सपोज़्ड टू बी द वीक आफ्टर द नेक्स्ट क्विज।

### 02:43:14 · Speaker 3

No, no, no. See, we have to do six quizzes, right? We will, I'll talk, I'll talk to Chandan. So we have, this is, this will be the third quiz, right?

### 02:43:23 · Speaker 1

Yes sir

### 02:43:24 · Speaker 3

will be third quiz we have three more. uh so we will I and Chandan will discuss about it and let you know. because we have what four more weeks and we need to do three quizzes.

### 02:43:34 · Speaker 3

Right? So what we can do is we can skip on that Diwali week and rest of the weeks we can have quiz every week. Yes sir. We'll do it that way.

### 02:43:35 · Speaker 1

What we can do is

### 02:43:41 · Speaker 2

Yes sir

### 02:43:45 · Speaker 2

Sure. Yes sir.

### 02:43:45 · Speaker 3

will do it that way. I will I will I will discuss about it and keep you notified on the WhatsApp group and teams, okay?

### 02:43:54 · Speaker 3

Okay, I really have to leave now. So please take the quiz. I'll leave next week.

### 02:43:57 · Speaker 2

Next week I will take you

### 02:43:58 · Speaker 1

Thank you Sir

### 02:43:59 · Speaker 3

ओके, थैंक यू, थैंक यू, थैंक यू

### 02:44:00 · Speaker 2

Thank you. Thank you.

### 02:44:01 · Speaker 1

All the best sir for your interview

### 02:44:03 · Speaker 3

for my interview exactly. Thanks. Okay, see you. Bye.

### 02:44:03 · Speaker 2

my interview exactly thanks

### 02:44:09 · Speaker 1

ओके सर बाय
