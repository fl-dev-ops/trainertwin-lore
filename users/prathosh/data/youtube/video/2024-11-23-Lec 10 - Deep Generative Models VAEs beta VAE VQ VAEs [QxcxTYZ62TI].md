---
id: QxcxTYZ62TI
title: Lec 10 - Deep Generative Models VAEs beta VAE VQ VAEs
url: https://www.youtube.com/watch?v=QxcxTYZ62TI
date: '2024-11-23'
duration: 02:44:13
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 10 - Deep Generative Models VAEs beta VAE VQ VAEs

## Transcript

### 00:00:09 · Speaker 1

I think two voices it is it from

### 00:00:13 · Speaker 1

Okay yeah

### 00:00:25 · Speaker 1

Okay, so last class we completed VAE straight

### 00:00:35 · Speaker 1

Hello

### 00:00:35 · Speaker 2

Yes sir yes sir

### 00:00:36 · Speaker 1

Yes sir

### 00:00:43 · Speaker 1

It's for computer okay

### 00:00:48 · Speaker 1

Okay, so maybe quickly, uh, we'll take five, 10 minutes to look at the inference. I think training of EAE was done, I suppose. And, uh,

### 00:00:58 · Speaker 1

I hope that you people could revise everything that we had done in the wake of exam, right? So that you are up to the speed. Okay. So what I'll do today is like initial five, ten minutes and just complete the inference part of VAE, okay? Just ten minutes and then we'll move on to the diffusion models, okay? So that's what the plan for today is.

### 00:01:28 · Speaker 1

Before we continue, I just want to see how many classes are we left with. 19th is 19th, we have one class. 26th, we have one class.

### 00:01:40 · Speaker 1

Second also we can have a class right

### 00:01:47 · Speaker 1

So yeah

### 00:01:47 · Speaker 2

I'm sorry

### 00:01:49 · Speaker 1

One two three four

### 00:01:56 · Speaker 1

Four

### 00:01:58 · Speaker 1

and 9th, 5th and 16th also we can have a class. So even though they have said that 14th is the last working day, last class day, we can also have a class on 16th.

### 00:02:09 · Speaker 1

So that there will be one two three

### 00:02:14 · Speaker 1

Four

### 00:02:17 · Speaker 1

One two three four

### 00:02:21 · Speaker 2

I've been shooting today

### 00:02:22 · Speaker 1

five including today. Yeah, I think that's good. So what I'll do today, we will start the DDPM diffusion models. Maybe next one more class, I will complete DDPM. Okay. So that will leave us with three classes, three more classes.

### 00:02:41 · Speaker 1

Yeah, that's good enough. So one class for autoregressive models and LLMs and

### 00:02:48 · Speaker 1

Think yeah that's what we can cover a lot more growth

### 00:02:51 · Speaker 2

Sir but we didn't do VQVA and

### 00:02:56 · Speaker 1

I will do that today. So initially, today before I complete, I'll do inference on VAEs and I'll do VQVAEs and then we'll go to diffusion models.

### 00:03:09 · Speaker 1

Okay that's it

### 00:03:15 · Speaker 3

encoded

### 00:03:17 · Speaker 1

You mean the training you are saying

### 00:03:18 · Speaker 3

Yes yes

### 00:03:19 · Speaker 1

That's the process I'll do that

### 00:03:25 · Speaker 1

So this is there in your second assignment right So when you implement it it will become much more clearer anyway I'll do that

### 00:03:33 · Speaker 1

Okay

### 00:03:35 · Speaker 1

Okay, so as you know, right, we have these two components, the encoder and decoder. Encoder is probabilistic.

### 00:03:46 · Speaker 1

Okay, I also told you why this would be a reconstruction cost, right? Ah, yeah, we have done that. Okay. Why would the log likelihood becomes a reconstruction cost? Okay, that also we have done. Good. Okay. So here is how a VAE works. So you take a sample xi, and this is, of course, for training. Take a sample xi, which is the data sample. Pass it through the encoder. This is the forward pass. So once you pass it through the encoder,

### 00:04:16 · Speaker 1

get a mean and a variance typically how is it done is if k is the dimensionality of your latent space

### 00:04:26 · Speaker 1

the output of the encoder

### 00:04:31 · Speaker 1

The output of the encoder is

### 00:04:35 · Speaker 1

This is D dimensional

### 00:04:43 · Speaker 1

This is D dimensional, okay? And this will be

### 00:04:51 · Speaker 1

dimensional so typically what what will be done is this will also be a k dimensional vector see actually it should be a k square dimensional vector uh people take it as k dimensional vector by by assuming a diagonal covariance okay if you assume this to be a diagonal covariance then you only have k parameters right because it's only a diagonal matrix so input is a d dimensional vector which is a which is an image or whatever right and the output of encoder will be two

### 00:05:21 · Speaker 1

k dimensional where first k dimensions will be corresponding to the mean and the next k dimensions correspond to the variance

### 00:05:30 · Speaker 1

Now once you get the mean and variance what you do is you sample a Gaussian distribution outside of the neural network epsilon j

### 00:05:40 · Speaker 1

You do this reparameterization which is you add this mean that the output of the encoder has given okay to epsilon which is scaled by sigma

### 00:05:53 · Speaker 1

That will give you a ZJ. So take that ZJ, okay, and pass it through the decoder. And the output of the decoder is taken to be XJ cap. So this is one forward pass. Any questions on this?

### 00:06:16 · Speaker 2

Sir, when we say variational inference, sir, like what do we mean by that?

### 00:06:24 · Speaker 1

No, no, no, hold on. I still not come to that. We are not talking about inference. We are only talking about training now. See, one forward pass through encoder and decoder is this. That much is clear. So pass a sample through the encoder, get your parameters, reparameterize it. Sample outside the neural network, reparameterize. And then again, pass it through the decoder. You get an X cap. So that is one pass through the encoder decoder. Okay. Now to train the encoder, what you do is encoder has two layers.

### 00:06:54 · Speaker 1

right one is the uh the kl loss this is to train the decoder we saw how to train the encoder here yeah to train the encoder we had once you get the x cap right you compute this um

### 00:07:10 · Speaker 1

deconstruction term, okay. And then you back propagate it by keeping the decoder parameters fixed, okay. And there is also a, once you come to the input of the decoder, you have the KL term also. Differentiate that KL term with respect to the encoder parameters and then differentiate through this reparameterization term and then back propagate all the way through the input of the encoder. So that is one backward pass through the encoder.

### 00:07:42 · Speaker 1

Is that okay Any questions on this

### 00:07:47 · Speaker 1

So to train the encoder, you will have to do one forward pass through the encoder and decoder and then one backward pass through the decoder and the encoder again. While you are doing backward pass through the encoder, you also have to add the KL loss.

### 00:08:03 · Speaker 1

And for the decoder training one forward pass through the encoder decoder get the output of the decoder compute the reconstruction loss and one backward pass through the output of the decoder

### 00:08:16 · Speaker 1

That completes the training we

### 00:08:21 · Speaker 1

Any questions on this?

### 00:08:29 · Speaker 1

Okay, so once this is trained, what do we do with it?

### 00:08:39 · Speaker 1

Is it not

### 00:08:44 · Speaker 3

You can just write anything and then it will score

### 00:08:58 · Speaker 1

Inference between

### 00:09:09 · Speaker 1

So post training VAE can be used for two tasks. Okay. The first task is

### 00:09:22 · Speaker 1

Posterior inference

### 00:09:30 · Speaker 1

As I said in the previous class, what do you mean by posterior inferences given?

### 00:09:37 · Speaker 1

Data point X

### 00:09:44 · Speaker 1

So let's call that as lakes

### 00:09:47 · Speaker 1

or something because this is not in the training data okay

### 00:09:52 · Speaker 1

Finding the

### 00:09:56 · Speaker 1

responding

### 00:10:03 · Speaker 1

Latent vector

### 00:10:08 · Speaker 1

also called as embedding

### 00:10:18 · Speaker 1

This is what is called as

### 00:10:20 · Speaker 1

is the test okay so this is what is called as posterior inference i told you right uh any latent variable model uh one of the advantages is that once you try in a latent variable model you can get an embedding corresponding to uh the given data point that is what we do in all these encoder decoder based llms also right the uh the encoder will give you an embedding corresponding to data now how do you do that take the encoder

### 00:10:54 · Speaker 1

Just trying okay

### 00:11:00 · Speaker 1

star so you pass x test to this and what you get here is

### 00:11:11 · Speaker 1

mu v star at x test

### 00:11:16 · Speaker 1

to get sigma c star at x test

### 00:11:23 · Speaker 1

This is what you get right now the

### 00:11:29 · Speaker 1

Embedding

### 00:11:35 · Speaker 1

of extra x tests

### 00:11:37 · Speaker 1

are multiple options right can be taken to be

### 00:11:44 · Speaker 1

mu phi star itself. So this itself can be taken as an embedding corresponding to H star. This is one possibility. The other possibility is you sample an epsilon from

### 00:11:58 · Speaker 1

normal 0 1 okay let's call this embedding 1 normal 0 1 and then take z test to be equal to let's call this epsilon t epsilon t times

### 00:12:16 · Speaker 1

Basically you do the reparameterization

### 00:12:21 · Speaker 1

New v start test

### 00:12:26 · Speaker 1

This now becomes

### 00:12:32 · Speaker 1

embedding for its test

### 00:12:36 · Speaker 1

and B Z test also

### 00:12:41 · Speaker 1

this let's call this embedding too so you can get so for any data point right you can get an embedding this way just pass it through the encoder you either take the the mean of the encoder itself as the embedding or you do a sampling outside of neural network reparameterize and take that as an embedding so now how do you use this embedding is up to you you can use it for a class if you say use it in a classifier see what happens is

### 00:13:11 · Speaker 1

We know that the dimensionality of the test

### 00:13:23 · Speaker 1

know that this is much much less than dimensionality of x test so what can be done is you can try in a classifier

### 00:13:38 · Speaker 1

using z test right or do you can do arithmetic uh in the embedding space and all that right so

### 00:13:51 · Speaker 1

I can see it

### 00:14:04 · Speaker 1

Bangalore weather since last 15 days had made it has made everybody sick

### 00:14:12 · Speaker 1

Z test can be used

### 00:14:20 · Speaker 1

Classification

### 00:14:28 · Speaker 1

Okay or like compression

### 00:14:35 · Speaker 1

You can do contrastive learning on top of it etc.

### 00:14:39 · Speaker 1

We'll talk about this contrastive learning later in the class, I mean later in the course. So basically you can use this embedding to whatever effect that you want. That's the idea. So this is called posterior inference. Any latent variable model, right? You can.

### 00:14:58 · Speaker 1

get this meaning post training you can use the encoder to get the embedding corresponding to unseen data points I mean of course you can get embeddings corresponding to the training data as well entire data you can get the embedding take the trained encoder pass the data through the trained encoder and you get the embedding and use it for whatever task downstream tag the downstream task that you would need so that is about the posterior inference using latent variable

### 00:15:28 · Speaker 1

models any questions on this

### 00:15:39 · Speaker 1

Yeah, uh, Shirisha

### 00:15:43 · Speaker 4

Yes sir. Sir uh so when you said Z tests can be used for classification what kind of classification you mean?

### 00:15:51 · Speaker 1

Let's say that you have built a VAE on MNIST, right? Now you want to train a classifier on MNIST. Typically what you do is you take the images and train a classifier on MNIST, right? So instead of doing that, you take the embeddings on the MNIST and you train a classifier using embeddings.

### 00:16:19 · Speaker 1

Does that make sense?

### 00:16:20 · Speaker 4

Okay so basically we are trying to classify the class of the images it

### 00:16:25 · Speaker 1

Anything. So it doesn't matter, right? Your input can be image or it can be text or anything, depending upon what sort of data you have. But the idea is that you can, instead of using X test, you can use Z. So what's, I mean, a more interesting question is what advantage do you get by using Z instead of X?

### 00:16:49 · Speaker 1

Now the answer to that is, actually, if you have learned a good encoder-decoder model, right, the hope is that the embeddings that you have gotten is well-clustered and well-behaved. Because, I mean, as I told you in one of the earlier classes, these naturally occurring data will be in very high-dimensional spaces and they will all be scattered, no, because of curse of dimensionality. They will not be well-clustered.

### 00:17:19 · Speaker 1

If you learn a representation in a lower dimensional space it will be much more clustered and classifiers would behave much better in the embedding space compared to the data spaces the HOOP

### 00:17:32 · Speaker 1

Tell me this in your assignment have I asked you to use these embeddings and build a classifier?

### 00:17:39 · Speaker 2

Yes sir

### 00:17:40 · Speaker 1

This is exactly what I have asked you to do, right? Try in a VAE and then get the corresponding Z's and then use it in a classifier. And I think I have asked you also to compare this with a classifier that is built only on the data space also, right?

### 00:18:00 · Speaker 2

Yes sir

### 00:18:03 · Speaker 1

Have I? Let me just open the assignment and see

### 00:18:09 · Speaker 1

asked you right yeah yeah so that's what it is so first you have to use a cnn and classify that classify the data and then use these embeddings and reduce the network size and simply use an mlp and see what happens on top of it

### 00:18:27 · Speaker 1

Yeah service

### 00:18:31 · Speaker 3

So so for this uh parameter reparameterization so this is eps the sigma should be raised to half right because we need some standard deviation type component to be added

### 00:18:42 · Speaker 1

uh that depends on yeah that depends on what you are representing as sigma no i'm representing that root of that itself as sigma depends i mean that's just a scaling factor right

### 00:18:55 · Speaker 3

So we're actually getting standard deviation type

### 00:19:01 · Speaker 3

But I'll be right back

### 00:19:02 · Speaker 1

That is what I'm saying, right? So now if you represent the output of your encoder as standard deviation, then you raise it to power of half. If I say that it's the variance, then you don't have to. Depends upon how do you see it, that's all.

### 00:19:14 · Speaker 1

Oh send it

### 00:19:17 · Speaker 2

Sir is this the right time to ask that about variational inference like

### 00:19:23 · Speaker 1

Ah, see this is this is posterior inference. Okay. Posterior because what you're actually calculating here is you're calculating

### 00:19:34 · Speaker 1

P theta P phi star of Z given X right

### 00:19:41 · Speaker 1

I mean technically speaking not P it's the

### 00:19:46 · Speaker 1

I was going to say that this is

### 00:19:50 · Speaker 1

Yeah

### 00:19:50 · Speaker 2

Yeah

### 00:19:51 · Speaker 1

Yeah Q star Q star Q phi star of Z given X correct

### 00:19:57 · Speaker 1

Now this is inference definitely because given an x you are giving a z okay and this is posterior I mean technically speaking you can actually call this variational posterior inference.

### 00:20:23 · Speaker 1

Variational posterior inference variational because

### 00:20:29 · Speaker 1

We don't have

### 00:20:36 · Speaker 1

access to

### 00:20:39 · Speaker 1

p theta star z given x this is the true posterior distribution right

### 00:20:47 · Speaker 1

are using

### 00:20:53 · Speaker 1

Ah variation and distribution

### 00:20:58 · Speaker 1

distributive distribution which is Q phi of Z given X

### 00:21:04 · Speaker 1

approximate it so that is why it's called the variational posterior okay uh in fact in your exam i had asked you to uh start from the kl divergence between these two distributions and derive the elbow

### 00:21:23 · Speaker 1

Do you remember that question

### 00:21:25 · Speaker 3

Yes yes

### 00:21:26 · Speaker 1

We had told you that you start from the KL divergence between the variational distribution

### 00:21:35 · Speaker 1

And this

### 00:21:40 · Speaker 1

And show that minimizing this

### 00:21:45 · Speaker 1

boiled down to the elbow objective that you optimize in VAE correct

### 00:21:54 · Speaker 1

So this is exactly what it is, right? I mean, you can actually see, see, the entire analysis that we did in VAE was by saying that we want to maximize the log of

### 00:22:07 · Speaker 1

the data likelihood under the latent variable model right that's how we derive the elbow the entire story can be constructed via this route okay it's only an algebra you can you should just write this scale divergence and write this posterior in terms of the joint distribution between x and z and marginal and then you get it in fact it's pretty easy uh i hope that uh

### 00:22:31 · Speaker 1

Like a lot of you could get this crack this

### 00:22:35 · Speaker 1

Did you do that?

### 00:22:38 · Speaker 1

So you just have to write down the KL divergence definition of KL divergence and use Bayes' law and show it. It's not at all difficult. Okay. Now, yeah. So basically, the reason I asked you that question is to make you appreciate this, that it is called a variational model because while we want the true posterior distribution of Z given X, because we do not have it, we approximate that using another distribution, which is which we call the variational distribution, which represented

### 00:23:08 · Speaker 1

by q phi of z given x so the objective is to make sure that the posterior of the true i mean yeah posterior under the true model is going close to the variational posterior and you minimize the k l divergence between them that is the objective okay so now that's why you call this i mean when you estimate q phi of z given x under a trained model you call that as variation of posterior inference

### 00:23:38 · Speaker 1

The posterior because

### 00:23:42 · Speaker 1

you are getting z given x this is because posterior uh inference because you do it under phi star post training

### 00:23:54 · Speaker 1

Is this all right Sanjit So it's called variational posterior

### 00:23:58 · Speaker 1

uh influence

### 00:24:04 · Speaker 1

Okay, so this is, I mean, we were talking about inference with VAE, right? One is to get the embeddings. The other thing that you can do with this is obviously

### 00:24:17 · Speaker 1

data generation or sampling because it's a generative model

### 00:24:32 · Speaker 1

To do data generation or sampling how do you do that is that take the decoder

### 00:24:38 · Speaker 1

See this is exactly what happens in a language model also, okay? Encoder-decoder based LLMs, exactly the same thing happens. The encoder is used for inference, okay? And the decoder is used for generation. Same thing with all encoder-decoder models. Now you sample Z from normal 0, 1.

### 00:25:01 · Speaker 1

and give it to the trained decoder

### 00:25:05 · Speaker 1

will take which will take z and give you an x

### 00:25:14 · Speaker 1

will give you x cap so this is the

### 00:25:20 · Speaker 1

Generated data point

### 00:25:27 · Speaker 1

See a true decoder I mean while training decoder is trying to take samples from Q phi of z given x.

### 00:25:40 · Speaker 1

You get what I'm saying? See, decoder is trying to see samples from Q phi of Z given X and give you sample from P theta of X given Z, right? But now you are sampling from normal 0, 1, not from Q phi of Z given X. Why would decoder help you?

### 00:26:01 · Speaker 1

You see the question

### 00:26:03 · Speaker 2

you are reducing the KL divergence between exactly

### 00:26:07 · Speaker 1

Exactly, right? Exactly. So now what happens is now post training.

### 00:26:18 · Speaker 1

Q phi of Z given X okay would reduce to normal 0 1

### 00:26:25 · Speaker 1

Because of the

### 00:26:30 · Speaker 1

Here the

### 00:26:33 · Speaker 1

Elbow

### 00:26:37 · Speaker 1

Therefore therefore

### 00:26:41 · Speaker 1

Z coming from

### 00:26:46 · Speaker 1

Q will be of Z given X is

### 00:26:54 · Speaker 1

Equivalent to

### 00:26:57 · Speaker 1

Z coming from normal 01. In fact, I've asked you to do this also in your assignment, okay? That once you try in the decoder, you sample Z from normal 01 and then give it to the decoder, you get the generated data. Now, in an LLM, right, we will see that later. We will do what is called as conditional generation. Because all these GPT, et cetera, what they do is they take an input and then gives you an output, right? It's not unconditional generation unlike in a VAE.

### 00:27:27 · Speaker 1

I mean you can also tweak the VAE to do conditional generation all you have to do is as I said we looked at conditional GAN right similarly you can do a conditional VAE just by appending another conditioning variable in terms of text embedding or one hot vectors right so but basically the idea is that once you train you take the trained decoder and then you can do sampling or data generation so now encoder becomes the inference model and decode

### 00:27:57 · Speaker 1

for data generation

### 00:28:00 · Speaker 1

See the idea is if you take let's say a naive autoencoder okay that has an encoder and a decoder

### 00:28:14 · Speaker 1

x and x cap okay now what happens is uh let's say that it will give you z and you simply have a reconstruction task here

### 00:28:28 · Speaker 1

Excuse me so you have a reconstruction task here

### 00:28:32 · Speaker 1

Now this if you train a a nice autoencoder like this okay now post training you can only use this autoencoder to do inference because you can take the encoder and given an x it will give you a z but you can't do generation using this thing because the distribution of the latent space is unknown.

### 00:29:05 · Speaker 1

Na nay water encoder

### 00:29:10 · Speaker 1

Now what do we do in a variational autoencoder is if you see that we will say that look I don't only want my I not only want my decoder to reconstruct the data but I also want the distribution of the output of the encoder

### 00:29:31 · Speaker 1

To follow

### 00:29:35 · Speaker 1

some distribution of interest so that once I train this I can sample from a known distribution and then use the decoder as a generative model.

### 00:29:46 · Speaker 1

Right so now BAE you can see BAE

### 00:29:54 · Speaker 1

Uh

### 00:29:57 · Speaker 1

Auto encoder

### 00:30:05 · Speaker 1

A regularization

### 00:30:11 · Speaker 1

On the latent space

### 00:30:20 · Speaker 1

Such that

### 00:30:25 · Speaker 1

The distribution of the latent space

### 00:30:38 · Speaker 1

Should follow a caution

### 00:30:46 · Speaker 1

our predefined distribution let's say in this in general case it will be predefined

### 00:30:57 · Speaker 1

Larger distribution

### 00:31:03 · Speaker 1

Is this all right? So in an autoencoder, what will happen is there's an encoder and a decoder. You would say that, okay, the data has to get encoded into some latent space. And from the latent space, we'll have to get back to the data space, right? In a variational autoencoder, we'll say that, okay, we just do not want the data to be reconstructed. We also want the latent space to follow a particular distribution of interest, okay? So that why do we do this is because post

### 00:31:33 · Speaker 1

We can sample from this distribution of interest and give it to the decoder and use it as a generative model

### 00:31:41 · Speaker 1

Is this alright

### 00:31:43 · Speaker 1

So that way right VAE can be seen as a regularized autoencoder, an autoencoder with a regularization on the latent space such that the latent space follow a particular distribution of interest.

### 00:31:55 · Speaker 1

Yes and it

### 00:31:57 · Speaker 2

Sir, but the normal distribution that is a very like a very wide space right. So it's not possible that for every sample within this normal distribution, we will get like a proper image that is similar to the original data set. So like that's where like we try to learn on the poles or the clusters.

### 00:32:21 · Speaker 1

Oh see

### 00:32:28 · Speaker 1

While you can see this as a reconstruction plus a regularization, you should always remember how did we get to this objective? We got to this objective by minimizing the KL divergence between the model distribution and the true data distribution, correct?

### 00:32:42 · Speaker 2

distributing into distribution

### 00:32:44 · Speaker 1

We started, how did we get this? This was our elbow, right? Whatever I have written here is our elbow. That is why I don't write the loss function of VAE as simply reconstruction plus KL, simply because I want you to appreciate where did this come from. This actually came from the elbow, right? Now, what was that? That was the KL distribution, KL divergence between Px and P theta. That's what we started from.

### 00:33:14 · Speaker 1

Now doing all this, we are actually reducing the KL divergence between Px and P theta. So now if we have done it right, right, then no matter what this distribution is, you know, it can be normal or anything, the VAE has to sample from Px because we have technically reduced the KL divergence between Px and P theta.

### 00:33:40 · Speaker 1

Does that make sense

### 00:33:43 · Speaker 2

Okay

### 00:33:44 · Speaker 1

because the entire model has reduced the KL divergence between Px and P theta. If you have done it right, then this objective should lead you to sample data points from Px.

### 00:34:05 · Speaker 3

Yeah, so in the assignment what we observe is the reconstruction loss is, I mean, decreasing pretty fast, but we don't know. We see that the KL divergence, it's hard to reduce. I mean, it keeps generally increasing. So what's...

### 00:34:17 · Speaker 1

little increasing so what's correct correct that happens see that is because uh something uh which is called a posterior collapse so i'll talk about it uh okay so i'll come to that so this is yeah this is how what what do you do in a knife vae right there are lots of improvisations that people have done over a knife vae i'll not talk about all of them i'll only talk about like one of them which is the vector contest vae which is

### 00:34:47 · Speaker 1

sort of state of the art VAEs that people use. Okay. Yeah. That is precisely because the observation that you have made in your assignment. Okay. So there is something called posterior collapse in VAE. I'll talk about it.

### 00:35:10 · Speaker 1

Oh la

### 00:35:13 · Speaker 1

Then maybe

### 00:35:22 · Speaker 1

sort of related to the question that Sanjit asked. He'll tell you what happens is. See in the NIVE what's happening is

### 00:35:31 · Speaker 1

Recall

### 00:35:36 · Speaker 1

that in a VA

### 00:35:42 · Speaker 1

Now Q phi of Z given X

### 00:35:52 · Speaker 1

is force to

### 00:35:56 · Speaker 1

go to normal 0 1

### 00:36:01 · Speaker 1

Irrespective of okay

### 00:36:09 · Speaker 1

For all X

### 00:36:13 · Speaker 1

See, now QP of Z given particular X, this is what it means, no, X by conditioning it on X. This means X is equal to a particular XI, okay? Now for all XI, we want this to be equal to normal 01 in a VAE because we are minimizing the KL divergence between these two.

### 00:36:35 · Speaker 1

Understand. Now, okay, so is this clear to all of you that in a VAE, this Q phi of Z given encoded distribution is supposed to go to normal zero one for all X?

### 00:36:48 · Speaker 1

Okay, now what is the consequence of it? The consequence of this is that

### 00:36:54 · Speaker 1

Okay, do you people know of this idea called bias-variance decomposition, bias-variance trade-off?

### 00:37:05 · Speaker 2

No sir

### 00:37:08 · Speaker 1

Okay, see, whenever you regularize a model, okay, so if you take a learning model and you regularize the model, what will happen is, I mean, you might be knowing it in a different name perhaps, right? See, if you over-regularize a model, what will happen is, why do you regularize a model? You regularize a model because you want to avoid overfitting, right? Now, if you over-regularize it, the model will go to the regime of underfitting. Now, if you do not regularize it,

### 00:37:38 · Speaker 1

then the model will go to the regime of overfitting right it is this trade-off between the underfitting and overfitting is what is called as the bias-variance decomposition so that is a topic by itself

### 00:37:50 · Speaker 1

That's exactly what happens here okay so I'll tell you the consequence of this is the following

### 00:38:00 · Speaker 1

U phi of z u and x okay

### 00:38:05 · Speaker 1

Apologies

### 00:38:11 · Speaker 1

Normal zero one

### 00:38:14 · Speaker 1

Or Olex Olex

### 00:38:18 · Speaker 1

Think about it. Suppose your q phi of z given x approaches normal 0, 1 for all x. What is the consequence of it? Then the decoder

### 00:38:35 · Speaker 1

Very

### 00:38:37 · Speaker 1

have a difficulty

### 00:38:41 · Speaker 1

will have difficulty

### 00:38:45 · Speaker 1

reconstructing

### 00:38:51 · Speaker 1

Why do you think so? See, you see what is happening. Let's say that there are two x, okay, x1 and x2, okay. Now, q phi of

### 00:39:03 · Speaker 1

Z given X one okay is equal to Q phi of Z given X two

### 00:39:11 · Speaker 1

And both of them are let's say normal zero one

### 00:39:18 · Speaker 1

Suppose this happens. If this happens, then if you get a Z1 from

### 00:39:26 · Speaker 1

Q phi of z given x 1 okay and z 2 from

### 00:39:37 · Speaker 1

Q phi of Z given X two right so decoder

### 00:39:48 · Speaker 1

not be able to

### 00:39:53 · Speaker 1

Differentiate

### 00:40:00 · Speaker 1

between G1 and G2 because both of them are coming from the same distribution

### 00:40:10 · Speaker 1

See this

### 00:40:13 · Speaker 1

This is what is called as posterior collapse

### 00:40:23 · Speaker 1

Which means that for

### 00:40:27 · Speaker 1

all x okay q phi of z given x is collapsing

### 00:40:39 · Speaker 1

A particular distribution

### 00:40:46 · Speaker 1

By design

### 00:40:49 · Speaker 1

This is a consequence of elbow, right? We are not like, we can't help. This is what is happening. So now since x1 and x2, rather since for all x, q phi of z given x is going close to one particular distribution.

### 00:41:09 · Speaker 1

Decoder will have difficulty in trying to reconstruct

### 00:41:16 · Speaker 1

rather see if it if it can differentiate between each sample input sample it can reconstruct easily isn't it if it cannot differentiate between the the latents corresponding to two different samples then it'll have hard time reconstructing it do you see this point does all of you see this point any questions on this

### 00:41:42 · Speaker 1

Yes Norman

### 00:41:43 · Speaker 3

Uh so this happens only in naive uh VA or that

### 00:41:47 · Speaker 1

It happens only in NIV yeah we have we'll see how to circumvent this problem how do you solve this problem

### 00:41:48 · Speaker 3

But

### 00:41:54 · Speaker 1

Actually you should have seen this in your uh in your assignments if you've started implementing it

### 00:42:01 · Speaker 1

Yeah, so I'll tell you what happens. This is not what happens in the kind of architectures that we use, right? Reconstruction will not suffer. The other way happens. There's only half of the story. I'll tell you the other half. Maybe I can ask you the... I can take questions after this. This is posterior collapse, okay? Now...

### 00:42:25 · Speaker 1

Suppose suppose

### 00:42:31 · Speaker 1

So I suppose the weight on the care term is reduced

### 00:42:49 · Speaker 1

Now what do I mean by that? The last function in in VAE looks like this right you have the deconstruction plus the KL term.

### 00:43:13 · Speaker 1

Well this one was zero only

### 00:43:25 · Speaker 1

Okay, now this is how it is. I mean, in the naive implementation, both of these terms are equally weighted, right? So there is another version of VAE called a beta VAE, okay, which is simply adding this beta term to the KL where your beta is between 0 and 1.

### 00:43:45 · Speaker 1

Okay now

### 00:43:51 · Speaker 1

So higher beta right corresponds to

### 00:43:55 · Speaker 1

More weight to kale

### 00:44:02 · Speaker 1

So this is this is

### 00:44:04 · Speaker 1

beta VA improvisation on VA called beta VA higher beta corresponds to more weight to KL and vice versa right

### 00:44:15 · Speaker 1

So now let's say that let's come to this. Suppose I give more weight to KL. What will happen? This may lead to posterior collapse. We already saw that.

### 00:44:35 · Speaker 1

Okay, now if you have, suppose I give very low weight to beta, what will happen? This means that more weight to reconstruction.

### 00:44:50 · Speaker 1

More emphasis on reconstruction

### 00:44:56 · Speaker 1

This means that the reconstruction happens very nicely, okay, because now the decoder can, I mean, see, this implies, okay, lower beta implies implies QP of Z given X, okay, may not be equal to normal 0, 1.

### 00:45:16 · Speaker 1

For all X. Okay, so this implies that reconstruction is easier.

### 00:45:28 · Speaker 1

construction is easier

### 00:45:32 · Speaker 1

Because because why is this

### 00:45:38 · Speaker 1

Z1 and Z2 okay

### 00:45:42 · Speaker 1

can be different

### 00:45:48 · Speaker 1

x1 and x2. See, if you have two different latent codes for different input samples, then the decoder, it will be easier for the decoder to use that latent information and then reconstruct it back, right?

### 00:46:01 · Speaker 1

You see what I'm saying

### 00:46:03 · Speaker 1

Now okay reconstruction is better if you reduce the weight on the KL divergence but it should come with a cost what is the cost can somebody think about it

### 00:46:14 · Speaker 2

So there will be inference collapse

### 00:46:17 · Speaker 1

Now meaning the the the generation will suffer however

### 00:46:25 · Speaker 1

Generation quality will suffer

### 00:46:38 · Speaker 1

with lesser beta why is this

### 00:46:44 · Speaker 1

This is because see remember that what we do what we do post-training

### 00:46:54 · Speaker 1

We take p theta star okay we sample from normal 0 1

### 00:47:00 · Speaker 1

Okay now if

### 00:47:04 · Speaker 1

Q phi of z given x okay is not normal 0 1 for all x

### 00:47:16 · Speaker 1

during the

### 00:47:19 · Speaker 1

Generation

### 00:47:23 · Speaker 1

Sampling a Z from normal 0 1

### 00:47:27 · Speaker 1

and passing through the decoder

### 00:47:35 · Speaker 1

the decoder okay may not

### 00:47:40 · Speaker 1

Need to

### 00:47:44 · Speaker 1

Data samples

### 00:47:48 · Speaker 1

Because why is this because

### 00:47:52 · Speaker 1

Recorded

### 00:47:55 · Speaker 1

As seen

### 00:48:00 · Speaker 1

U phi of z given x during training

### 00:48:09 · Speaker 1

It is

### 00:48:11 · Speaker 1

not equal to normal

### 00:48:16 · Speaker 1

Understood. Now for the decoder to work, you need QP of Z given X to be normal 0 1 for all.

### 00:48:25 · Speaker 1

Okay. And if you make that, then what happens is the reconstruction quality suffers while the generation becomes okay. So now there is a trade-off between these two. In fact, if you look at the beta VAE paper, they will show you that with different values of beta, you will see the trade-off between reconstruction and generate quality. What I suggest you is to implement this beta VAE in your assignments.

### 00:48:55 · Speaker 1

It comes with no cost in the sense that you just have to have a weight factor on your KL divergence term and you experiment with different betas and you would see that if you have a large beta then the reconstruction will become difficult. Okay. Why the generation will be okay. And if you reduce the beta reconstructions will be better. Will the generation quality suffer? In fact, you might have seen, right? I mean, people who have read the architecture on VAE,

### 00:49:25 · Speaker 1

you you might have seen uh people saying that v a is uh results in blurry generation right blurry images so that what is that that is simply saying that if your q phi of z given x is not normal 0 1 for all x what will happen is if you if there is a deviation between what the decoder has seen during training and what it sees during inference then the images that you generate will not match that of v theta and that's why

### 00:49:55 · Speaker 1

code blurriness comes into generation quality now to avoid that if you make your reconstruction very strong okay by reducing the beta then the generation quality suppose that there is this trade-off between these two

### 00:50:10 · Speaker 1

Okay, so now we will take questions. Uh, yeah, we wake.

### 00:50:18 · Speaker 2

So will making beta zero convert this into an autoencoder

### 00:50:23 · Speaker 1

That's a good observation. If you make beta zero then it'll simply become a non-automated code.

### 00:50:29 · Speaker 1

Lesser and lesser beta will always take it closer and closer to an I-O autoencoder

### 00:50:39 · Speaker 1

Yes

### 00:50:41 · Speaker 2

Can you so can you hide this side panel

### 00:50:44 · Speaker 1

Can you hide this eye panel? How do I do that? This one?

### 00:50:50 · Speaker 1

It opens something else

### 00:50:51 · Speaker 2

The full screen is there when the computer

### 00:50:53 · Speaker 3

A dog brain

### 00:50:54 · Speaker 1

Ah this is

### 00:51:01 · Speaker 1

Is it just not moving

### 00:51:13 · Speaker 2

If you write something it will start moving

### 00:51:30 · Speaker 1

Do you recognize anything at all?

### 00:51:37 · Speaker 1

What happened to this

### 00:51:42 · Speaker 1

Something happened

### 00:51:45 · Speaker 1

I mean I am not able to see this can somebody tell me what happened with this

### 00:51:52 · Speaker 4

Sometimes it gets stuck sir

### 00:51:55 · Speaker 3

Was killing me

### 00:51:56 · Speaker 4

We can just close and open

### 00:52:01 · Speaker 1

age old solution uh restarting

### 00:52:03 · Speaker 4

that is a tall problem

### 00:52:12 · Speaker 1

Oh yeah it actually will

### 00:52:19 · Speaker 1

Okay, uh, let's take questions Vivek, do you still have questions or is it done?

### 00:52:26 · Speaker 2

Uh so yes, I have a question. Uh suppose we change it

### 00:52:29 · Speaker 1

Yeah, hold on just one other side thing see I have been calling all of you by your first name I hope you don't mind I Mean for all we know all of us are of pretty much same age or you might be like seniors to me So please don't mind and also feel free to call me Pratosh. I don't mind. So you don't have to call me sir. That's too British Just just take my name, right? Yeah, I mean I mean it I really mean it you can

### 00:52:59 · Speaker 1

can feel free to call me pratik and i'll be happy and also right i mean don't uh don't feel uh earth because i i call your first names out okay because if i start calling you sirs so there's so many 85 people right sir and madam so you don't know who is who that's why that's where that's why the names are given anyway so anyway go on please

### 00:53:22 · Speaker 2

Yes, so one question is suppose we have a generation for a given z and I change z a little bit. So will the output look just a little bit modified or

### 00:53:36 · Speaker 1

Yeah, yeah, yeah. That is how it should, it should happen, right? I mean, that is how it should ideally happen. If you have trained it well with good architecture, that is how it will happen. See, that is why in, in GANs, right? I think, did I include this in your assignment? Did I ask you to sample two Zs and then do interpolation between?

### 00:53:54 · Speaker 2

Interpolation between yeah

### 00:53:56 · Speaker 1

Yeah so did you see it changing smoothly

### 00:54:00 · Speaker 2

Yes so yeah that happens

### 00:54:01 · Speaker 1

Yeah, that happens. Yeah, it happens if you have if you have latent space or the embeddings that you have learned are good. In fact, when we come to some of these language models, right, you would see that in in in this thing, right? What was that thing? Was it?

### 00:54:18 · Speaker 1

Bird it was not pitch

### 00:54:21 · Speaker 1

Which was that right I mean that famous example where they show that a man minus king embedding corresponding

### 00:54:27 · Speaker 2

Yeah work to it

### 00:54:28 · Speaker 1

word to work word to work word to work right that that should happen so it should semantically make sense if you have learned good embeddings

### 00:54:39 · Speaker 1

So it depends. See that is why imposing this sort of a constraint or rather a distribution on your latent space makes sense.

### 00:54:51 · Speaker 2

Okay

### 00:54:51 · Speaker 1

Yeah

### 00:54:52 · Speaker 2

Asser and one more question but yeah it's not I think it's not the maybe right time to ask but uh if we have a picture from uh somewhere else and if we want to find it's Z

### 00:55:05 · Speaker 2

How can we do that

### 00:55:07 · Speaker 1

I told you right that's what you do that's what the inference is you take a pre-trained encoder or a VAE pass it through the encoder in fact we will see that see you know the stable diffusion right all these the state of their diffusion models imagine or whatever the Google's and all these they don't do diffusion models on the on on the image space they do it on the latent space of a VAE in fact a VQVAE once I talk about VQVAE I will tell you that so basically

### 00:55:37 · Speaker 1

the trained encoder pass your data through the encoder get the embedding and then use it this posterior inference that's exactly what what you've seen on on your screen you train your encode vae on let's say image net and keep that right and given some new data pass your data through the encoder get the embedding and use it for whatever reason whatever downstream thing that you would want to do

### 00:56:06 · Speaker 2

Yes thank you

### 00:56:10 · Speaker 1

That's it

### 00:56:12 · Speaker 3

Sir, in this example, in this description for posterior collapse, so sir, it is high, since the normal distribution is a very large space and we have a finite set of images, like input images, so isn't it possible that we get each z that is unique for a given x?

### 00:56:36 · Speaker 1

Yeah if you recall our encoder is probabilistic

### 00:56:42 · Speaker 1

We are not asking the encoder to give the Z we are asking it to give the mean and variance

### 00:56:50 · Speaker 1

That's precisely why we make it probabilistic. It's not the z that you get. You get the parameters of the distribution. And by construction, you are asking the output of this encoder or the mean of this encoder to go to zero for all x. Even though the distribution, the support of the distribution is broad, what you are predicting is the mean invariance, not the z itself.

### 00:57:16 · Speaker 3

Okay, and sir, one more question. I was a bit confused with the term variational Bayesian. Is it same as the variational inference we talked about?

### 00:57:26 · Speaker 1

It's based because see auto encoding variational base is what they call the VA people. It's based because again this if you had done this exercise that I had given you in exam.

### 00:57:41 · Speaker 1

You use Bayes' theorem to get this elbow is it right Correct Yeah that's why it's called variational Bayes

### 00:57:49 · Speaker 1

Okay, variational because you use a distribution of variational approximation to p theta of z given x which is unknown.

### 00:58:00 · Speaker 1

Okay yeah yeah is that it

### 00:58:04 · Speaker 2

Yeah, what is the difference between reconstruction and generation?

### 00:58:10 · Speaker 1

reconstruction and generation. Okay. See, reconstruction is that you take an X, pass it through the encoder and the and take that Z, okay, that the encoder gives you. I mean, when I say Z, it is this reparameterized Z and pass it through the decoder, right? And you expect the output of the decoder to be exactly the same as that of the input. That is reconstruction.

### 00:58:35 · Speaker 1

Right? It's the first term.

### 00:58:38 · Speaker 2

Yeah but

### 00:58:38 · Speaker 1

No but I think this

### 00:58:52 · Speaker 1

See even after training you can take a data point that is there that you use for your training pass it through the encoder get it z and pass it through the decoder and expect the decoder to give you the exact same x isn't it

### 00:59:09 · Speaker 1

Post training nobody is stopping you from using the training data and passing through the encoder and giving it to the decoder isn't it

### 00:59:18 · Speaker 1

Yeah so that is a reconstruction thing isn't it

### 00:59:24 · Speaker 1

So generation is, see, generation is that you take a Z and pass it through the decoder, you get a new point that is not there in your training data. That's sampling, of course. But you can do reconstruction on training data as well. How do you do it? Take it, take the X, okay, and pass it through the training, sorry, the encoder, get the Z, take that Z, pass it through the decoder, and you expect the same X to come back.

### 00:59:54 · Speaker 1

Uh

### 00:59:57 · Speaker 3

Yes, sir. In the parameterized model for decoder, we are only considering the mu and we are saying that the sigma is identity. Right. Can we also take sigma, I mean, and what implications that...

### 01:00:09 · Speaker 1

Yeah, you can you can and then you have to again to generate you have to do another sampling right at the output of the decoder as well right. Typically sigma is not taken but yeah there's nothing that stops you from doing it that way. Typically it is not done.

### 01:00:29 · Speaker 1

Okay Harish

### 01:00:32 · Speaker 2

our use case that is whether we are doing reconstruction or the generation so we can change the training objective to have this uh k l i just regularization term or not

### 01:00:44 · Speaker 1

Correct. That's a good point. Yes. That is why, no, it's like a knob, beta VAE. This beta is a knob, depending upon what you want, right? In your, what you are training your VAE for, you can tweak it the way you want. That's a good point. Yes.

### 01:00:59 · Speaker 2

So you can have two different models uh for exactly two different times

### 01:01:02 · Speaker 1

Yes, yes, yes, yes. So in fact, in your assignment, I encourage you to actually do that, you know, sweep over beta and see the effect of what happens on your VA.

### 01:01:16 · Speaker 1

Yeah actually not

### 01:01:25 · Speaker 3

to the KL divergence we expect the mu and sigma outputted by the encoder to be close to zero and one but not exactly

### 01:01:33 · Speaker 1

Okay for OLEXP for OLEXP correct

### 01:01:35 · Speaker 3

but it should be exactly zero one then of the

### 01:01:38 · Speaker 1

I mean yeah if the training has happened properly yeah

### 01:01:42 · Speaker 3

Right and so is this somewhat of an adversary relation because if the KL divergence becomes zero then the reconstruction loss will explode and different

### 01:01:52 · Speaker 1

No, no, it should not it should no right why should it explode see as I think one of Sanchita was saying that uh I mean you're asking the asking it to make it Gaussian distribution zero mean unit variance for all x but even within zero mean unit variance you have infinite support you can place your z different places. But practically what happens is because you have like limited capacity encoder decoder, right? All these z's would be placed on very close to each other and

### 01:02:22 · Speaker 1

and discerning the difference between those two will become difficult to the decoder there's no adversary here

### 01:02:32 · Speaker 1

So ideally if you have see if you have infinite capacity encoder and decoder both the objectives can be achieved.

### 01:02:42 · Speaker 3

Because uh the encoder is technically not giving as you said right it's not giving z it is giving the parameter z

### 01:02:47 · Speaker 1

Doesn't matter, doesn't matter. Let's say that it will do perfectly and it will go to zero mean and unit variance for all x. And suppose your decoder has infinite capacity, right? As long as for two x's exactly the same z is not getting generated from the sampling, the decoder can do it. And also remember that the sample that the decoder sees as input, okay, is a sample that you get outside of the encoding.

### 01:03:19 · Speaker 1

And also you do an averaging over it no see you don't take one sample of z and give it to the decoder you take multiple samples of z and give it to the decoder

### 01:03:28 · Speaker 1

So that way if you have infinite capacity of encoder and decoder ideally a VAE should do perfectly well. But since we have like finite capacity architectures right if you make your encoder to have same distribution for all x decoder will have in fact that is one other experiment that you can see that keep everything constant including the beta but only increase the architectural size of encoder and decoder and you will see better performance.

### 01:03:58 · Speaker 1

Yeah, these are very good questions, by the way. In fact, I received one comment from one of you. I mean, I don't want to know who it is, but because that's the whole point of it being anonymous. It said that, you know, you see, you have spent so much time on quote unquote basics, right? Now, we only have these many classes and, you know, you're not covering the syllabus and this happens with all courses in ISE, et cetera, and all that.

### 01:04:28 · Speaker 1

sort of uh the the uh not so positive uh sentiment but see the thing is uh

### 01:04:38 · Speaker 1

good course right in in our opinion i mean uh good that the person said that this happens across the board in isc see what we feel uh as as faculty in isc is that we want to prepare you uh to you know to to read some of these literature independently so the idea is not to cover a lot of breadth a lot of papers you know a lot of ideas at a superficial level the idea is to go sufficiently deep and make you independent

### 01:05:08 · Speaker 1

so that you pick up any paper in the literature and then you can read it. So even if we don't quote unquote cover the syllabus, I don't know what syllabus is, you know, because none of the ISE courses will have any syllabus per se, especially these advanced courses. The idea is to, you know, make you think and enable you with a lot of tools and arsenals of tools such that you can start reading and appreciating and understanding things.

### 01:05:38 · Speaker 1

So, so I mean, what I was coming with this, I, I was reminded of that particular comment because all the questions that you are asking are very, very relevant. And then I, I hope when I suspect that, that, that you are, you are able to ask some of these questions and appreciate these things in deep because we spend so much time on basics. What are these divergence metrics? You know, how do you carve bounds on things and how do you build models, et cetera? I think that is what is valuable, isn't it? I think we can have this discussion maybe when we

### 01:06:08 · Speaker 1

When we have that hybrid class when you people meet me okay and I wanted to have that discussion as well right I mean we have to plan for that

### 01:06:18 · Speaker 1

post Diwali so now that I'm talking about it maybe we should

### 01:06:23 · Speaker 1

some dates the second how about uh

### 01:06:28 · Speaker 1

Can we do it on 16th itself

### 01:06:32 · Speaker 1

The last class that we do shall we do it hybrid Can you people plan a visit to ISE on 16th of November?

### 01:06:44 · Speaker 1

Let's do it that way so tentatively let's keep it on 16th

### 01:06:48 · Speaker 1

Okay, again, we will do the exact same thing. I will do it at Teams call and I will write it on my iPad and project on screens. But whoever wants to come to ISE, right, you are welcome. I'll arrange for a physical class and we'll do it offline, you know, hybrid on 16th.

### 01:07:09 · Speaker 1

So yeah I think 16th is the only date because

### 01:07:17 · Speaker 1

26th we can do but 26th is too short of a notice. But second is that Diwali week. I think a lot of you will be traveling.

### 01:07:29 · Speaker 1

Ninth, I don't know if you people come back on ninth, I have a, I have some other commitment, but I can't travel to IAC. I think 16th is the only day. Let's keep it on 16th. So tentatively 16th will be a hybrid class. Okay.

### 01:07:44 · Speaker 1

Plans for it okay if you want to come I mean there's absolutely no compulsion or anything only if you want to

### 01:07:52 · Speaker 1

Come and have a look at the campus and uh like meet me in person you're welcome to come there okay

### 01:07:59 · Speaker 1

right so this is about uh posterior collapse and this uh uh you know the the trade-off between uh the reconstruction and uh generation now as i said people have addressed this problem in multiple ways and there have been a lot of efforts uh in improvising uh vae models so one of them is of course this beta vae right where you have an explicit uh scale term uh on uh

### 01:08:29 · Speaker 1

uh the KL divergence to control between the the reconstruction and KL divergence is one thing the other thing other class of methods okay uh are where

### 01:08:48 · Speaker 1

Which channels?

### 01:09:02 · Speaker 1

I should be the latent prior

### 01:09:17 · Speaker 1

Hear some music that some guy on the streets, right? So yeah, not me. Why should be the latent power p theta of z, okay? Be the latent power p theta of b fixed.

### 01:09:33 · Speaker 1

to be normal zero one see all the while if you

### 01:09:38 · Speaker 1

Notice the in elbow the KL divergence was between

### 01:09:48 · Speaker 1

u phi of z given x and p theta of z

### 01:09:53 · Speaker 1

Now what did we do in in a naive VAE

### 01:10:04 · Speaker 1

theta of z is fixed

### 01:10:08 · Speaker 1

That's normal 01 right

### 01:10:12 · Speaker 1

which cause problems right which

### 01:10:17 · Speaker 1

was the issue of posterior collapse

### 01:10:28 · Speaker 1

So lot of people question this assumption that why should we fix p theta of z? Now, in fact, like my first PhD student from IIT Delhi actually worked on this. So his entire thesis was on optimal p theta of z. So now the question that can be asked is,

### 01:10:52 · Speaker 1

Rather not question because I've posted the question already, call it as solution.

### 01:10:59 · Speaker 1

is to learn

### 01:11:02 · Speaker 1

deligent press

### 01:11:09 · Speaker 1

Learn the latent prior p theta of z

### 01:11:13 · Speaker 1

along with the model

### 01:11:18 · Speaker 1

along with the encoder-decoder. So this is one of the key ideas. As I said, no, my first PhD student, his entire work was on this. So learning the latent prior for encoder-decoder models. Why should you fix it? You learn the latent prior itself. So what could be the best distribution that you have to impose on the latent space so that you get the optimality? Lot of work has been around this. So one notable thing is what is called as VAE.

### 01:11:48 · Speaker 1

It's a variational

### 01:11:52 · Speaker 1

called vamp prior okay

### 01:11:55 · Speaker 1

Variation variational maximum a posteriori prior okay, this is one thing where the idea is roughly

### 01:12:04 · Speaker 1

So make

### 01:12:07 · Speaker 1

make p theta of z okay a GMM a Gaussian mixture model and learn it

### 01:12:16 · Speaker 1

During training

### 01:12:20 · Speaker 1

is what they do. They make P theta of Z a Gaussian mixture model, which is a flexible, more flexible distribution than a univariate Gaussian and learn it during training. Learn the parameters of the latent prior also. So what will happen is the elbow will have three parameters. So it was, we had theta, phi and theta and phi. So there in all these methods, you will have another parameter lambda.

### 01:12:50 · Speaker 1

Okay well

### 01:12:54 · Speaker 1

P lambda of Z is the learnable latent prior

### 01:13:02 · Speaker 1

So now the optimization will be you you find theta star, you find phi star, and you also find lambda star.

### 01:13:09 · Speaker 1

As the minimization, you do a minimization over theta, do a minimization over phi, do a minimization over lambda, and you have this elbow. Now this elbow will be a parameter of the encoder, which is parameterized by phi, decoder parameterized by theta, and you have the prior, which is parameterized by lambda. So this is how it looks.

### 01:13:34 · Speaker 1

Okay, so not with studying the details of vampire because that's not the state of the art, right? What people observed is that if you make P theta of Z a continuous distribution and make it a GMM, right? It's again, you...

### 01:13:48 · Speaker 1

in in in problems like posterior collapse i mean while it gives you some respite that's not the best thing that you can do you can do better than that which is the vector contest ve which you will see but the basic idea is

### 01:14:03 · Speaker 1

Along with learning the encoding decoding, you also learn the parameters of the prior distribution on the latent space. Is this idea clear?

### 01:14:23 · Speaker 1

Yeah, Raghavendra, we'll see one instantiation of this, just a second. We'll see one instantiation of this, which is the, which is actually, as I said, no, the state of the art VAE, which is the vector quantize VAE. Even there, the idea is to learn the latent space, distribution of the latent space along with input decoder, called the vector quantize VAE. Yeah, go on, Raghavendra.

### 01:14:44 · Speaker 3

Yeah so I mean uh um what this

### 01:14:48 · Speaker 3

this lambda distribution right what what did you try to come close to is it uh p theta or p theta of z q and x

### 01:14:58 · Speaker 1

Exactly, exactly. So theoretically what can be shown is the ideal prior, right, is it's actually the ideal prior is

### 01:15:11 · Speaker 1

Can be shown to be equal to what is called as the aggregated posterior, which is the integral of.

### 01:15:24 · Speaker 1

This can be shown

### 01:15:27 · Speaker 1

The ideal prior that one would need to get the optimal elbow is what is called as this is called the

### 01:15:35 · Speaker 1

uh aggregated posterior it can this can be shown this is shown in the vampire paper

### 01:15:44 · Speaker 1

So what is this? You take all the encoding distribution, sorry, take the encoding distribution, marginalize it with respect to the data distribution, okay? And that is what the ideal prior has to be. That is what is shown.

### 01:16:01 · Speaker 1

Again there's no you don't have to worry about it here

### 01:16:09 · Speaker 1

Okay, so we will see one instantiation of this idea, which is, as I said, the state of the art VAE, which is called the vector contest VAE. Go on, Sanjit.

### 01:16:22 · Speaker 1

Electro-contacts be here

### 01:16:23 · Speaker 2

somewhere where we are learning the distribution on x like it is it is the in maximum likelihood estimate format right px given z so how will we be able to calculate px then

### 01:16:40 · Speaker 1

So we can't see that's only a theoretical result

### 01:16:44 · Speaker 1

Whatever I wrote is only theoretical in the sense that the ideal prior on the latent space is the aggregated posterior is a theoretical result. That is what you try to approximate using GMM.

### 01:16:59 · Speaker 1

is discrete

### 01:17:01 · Speaker 1

And it is vector quantized

### 01:17:05 · Speaker 1

Can we kill the AA?

### 01:17:09 · Speaker 1

what I mean in fact the VQA paper right the title of the paper is not better contest VAE they call it neural discrete representation learning that is the title of the VQA paper neural discrete representation learning

### 01:17:25 · Speaker 1

Again that's what the paper is so basically what they do is the following the motivation comes from the fact that they say that you see

### 01:17:34 · Speaker 1

all the naturally occurring data right can be compactly represented using some discrete amount of codes is what they call what they say here is what what they mean by that okay so let's say that you want to represent speech signals using some latent space

### 01:17:56 · Speaker 1

Now human speech can be represented using a finite set of phonemes. So what do you mean by phonemes? Let's say that I say A and you people say A. So if you plot that speech signal of A of what I say and what you say, all of them look very differently. Even the different instantiations of the same sound that I, one speaker say, will look differently.

### 01:18:26 · Speaker 1

In spite of that, no matter who says that sound, we perceive one particular idea called R or A. That's a phoneme. So phoneme is an abstract idea that you perceive when you hear speech.

### 01:18:42 · Speaker 1

Okay, now in English language, there are only a few finite set of phonemes that would represent the entire language.

### 01:18:51 · Speaker 1

Okay, so that is, let's say, I mean, they have identified some 50 odd phonemes. And in Indian languages also, you have about 50, 60, sort of around 60 phonemes. Okay, so now to represent language, all you need are 60 codes, right, which correspond to each of the phonemes. The same thing can be said in, for images also, right? I mean, if you want to represent an image, any scene can be represented by saying things like, okay, there are how many regular

### 01:19:21 · Speaker 1

Uh

### 01:19:24 · Speaker 1

Regular figures like rectangle or circles are present here and you know like how many slant lines are here etc. So basically you can have a finite number of discrete discrete discrete descriptors which are latent codes that can be used to represent any kind of naturally occurring data. So that is the motivation.

### 01:19:48 · Speaker 1

Okay, so that's why they use a discrete latent space in a VQVAE. They vector quantized and learnable. And we know why we should learn the latent space also, right? So it has learned.

### 01:20:03 · Speaker 1

during training so if you incorporate all these ideas in a vae right you will get what is called as a vector quantized vae we will see uh what it is is the motivation sort of clear okay let's let me uh write down the

### 01:20:17 · Speaker 1

architecture and also the way it is done and then we can discuss

### 01:20:25 · Speaker 1

So they make the encoder deterministic not probabilistic. So it takes Xi

### 01:20:33 · Speaker 1

Okay it will give Zi okay so they call it

### 01:20:38 · Speaker 1

z e of x i e corresponds to encoding you get z e i okay then suppose

### 01:20:50 · Speaker 1

It exists.

### 01:20:55 · Speaker 2

Sir your screen is not moving for me at least

### 01:20:59 · Speaker 3

Yes it's not visible when you're writing it

### 01:21:03 · Speaker 3

Flag is the rightest

### 01:21:06 · Speaker 1

That's all

### 01:21:15 · Speaker 1

Let's see sometimes networks network gives issues. Suppose there there are

### 01:21:39 · Speaker 1

M latent vectors

### 01:21:44 · Speaker 1

It does

### 01:21:47 · Speaker 1

Here dimension each

### 01:21:52 · Speaker 1

Call them Z1 Z2 Z3 up to ZM

### 01:22:00 · Speaker 1

All's a die

### 01:22:03 · Speaker 1

R a dimension

### 01:22:06 · Speaker 1

So now this

### 01:22:09 · Speaker 1

These form right a dictionary let's call this this is a latent dictionary

### 01:22:22 · Speaker 1

The latent dictionary. Okay. What is done in VQVA is that you find.

### 01:22:30 · Speaker 1

Okay

### 01:22:32 · Speaker 1

quantized version of the excite to be

### 01:22:39 · Speaker 1

Z A

### 01:22:42 · Speaker 1

We call this Z

### 01:22:46 · Speaker 1

J star okay

### 01:22:49 · Speaker 1

where J star is the one that is

### 01:22:55 · Speaker 1

the closest

### 01:23:01 · Speaker 1

between Z E of XI

### 01:23:05 · Speaker 1

And Z J, you have.

### 01:23:19 · Speaker 1

j to be equal to one to m

### 01:23:24 · Speaker 1

Does it make sense? See what we are doing is the following okay it's a two norm

### 01:23:29 · Speaker 1

Now, xi is a is an image or some data point that goes as an input to the encoder and it will give you some vector ze. Now, what I will do is

### 01:23:40 · Speaker 1

I will look

### 01:23:43 · Speaker 1

I will search for uh dot zm okay dot zj which is closest to that this output of this encoder

### 01:23:55 · Speaker 1

Okay and replace that ZE with the that with that particular vector in the dictionary.

### 01:24:03 · Speaker 1

Do you do you see what is happening?

### 01:24:07 · Speaker 1

And that

### 01:24:10 · Speaker 1

goes as an input to the decoder

### 01:24:24 · Speaker 1

So the quantized version of the input goes as

### 01:24:34 · Speaker 1

the input to the decoder

### 01:24:37 · Speaker 1

Is this clear what is happening to all of you questions on this? So this is vector quantization. So this operation right this operation is what is called as

### 01:24:47 · Speaker 1

recorded session

### 01:24:55 · Speaker 1

Literally no much

### 01:24:57 · Speaker 3

I said this earlier

### 01:24:58 · Speaker 2

The written dictionary is fixed right we have to pre decide

### 01:25:00 · Speaker 1

no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no

### 01:25:12 · Speaker 1

So we will learn this

### 01:25:16 · Speaker 1

Yeah I don't know

### 01:25:17 · Speaker 3

So going back to the the motivation right so you mentioned that we want to discretize it here but if you see even in the VAs right the the number of Z that we

### 01:25:30 · Speaker 2

I mean look at it like some business

### 01:25:32 · Speaker 1

There's no discrete no there is no discrete no it has a distribution the they don't have a fixed amount of z

### 01:25:42 · Speaker 1

Mm C is not good

### 01:25:42 · Speaker 2

Okay C is not fixed these are these are these are very much fixed in the sense if you are choosing

### 01:25:46 · Speaker 1

They're fixed time

### 01:25:47 · Speaker 2

a k dimensions then we know exactly what they are

### 01:25:50 · Speaker 1

No no no and nothing beyond that. It's it's not about dimensionality it is about m m latent vectors are fixed m is a hyper parameter you fix the number of vectors in your in your latent dictionary

### 01:25:50 · Speaker 2

And nothing beyond that

### 01:26:03 · Speaker 2

Okay, and once we have learnt them, we use them as the as the dictionary tool. Correct. So we we don't really look at the entire spectrum.

### 01:26:11 · Speaker 1

See, in fact, the I mean, one question that might come to you come to the mind is suppose you take an image and pass it through an encoder, right? So if suppose there are if I make M to be 100. So there are let's say that there are 100 vectors now.

### 01:26:31 · Speaker 1

Are 100 vectors good enough to represent a space that is as versatile as ImageNet? Might be a question. Actually, the way they do it is that they make the latent space, latent vector, a two-dimensional grid, where each of these columns are k-dimensional. So you have

### 01:26:56 · Speaker 1

1 to k so what they do is they quantize each of these columns so each column is quantized of the latent vector you understood

### 01:27:10 · Speaker 1

So that's what they represent. So basically what they do is the latent space will be a two-dimensional thing. It's a K cross

### 01:27:20 · Speaker 1

P dimensional latent space

### 01:27:25 · Speaker 1

Okay, where each of the p vectors in the latent space is quantized using the dictionary.

### 01:27:34 · Speaker 1

You understood? So that way every image now will be represented using p vectors okay from the dictionary. That way it becomes versatile.

### 01:27:45 · Speaker 2

And uh are there any weights to each of these dictionaries No no no no no

### 01:27:47 · Speaker 1

No, no, no, no, no, no, no, no, no. So decoder now will see a k cross p dimensional uh, uh, I mean grid.

### 01:27:56 · Speaker 1

When I said that it is Q, I mean ZQ of Xi, it is not one vector, right? It is the quantized version of this entire grid. That's what the decoder sees as an input. That's what they do in the VQA paper. Is this clear? So that's how it is not a single vector that is going as an input to the decoder. It is P number of vectors, right? Where all these P vectors come from this predefined dictionary. And how do you find which of the vectors

### 01:28:26 · Speaker 1

the p dictionary that you should take is you pass the xi to the encoder and encoder gives you a map right a grid of p vectors and each of the columns of this p dimensional grid you quantize using the dictionary and you give that as an input to the decoder

### 01:28:45 · Speaker 2

But where is the variation variational coming from? I mean a randomness coming here because if you have chosen a fixed set of p k vectors right I mean k size vectors the output would always be the same or

### 01:28:58 · Speaker 1

So during the training of course right uh you take those p vectors and then you try to reconstruct it

### 01:29:04 · Speaker 2

Correct okay

### 01:29:04 · Speaker 1

Now the question is how do you use this for generation right

### 01:29:08 · Speaker 2

Okay okay

### 01:29:09 · Speaker 1

Uh that is a question that I'll answer later

### 01:29:10 · Speaker 2

Okay sure

### 01:29:11 · Speaker 1

So right now, see, we are see the way the template is define the architecture, right? And train it. And then you do the inference. I'm defining the architecture and we have still not trained it. Let us try this and then we'll do the inference. But it's a valid question. How do you generate from a VQVA is a valid question. But did all of you understand what's happening, right? In terms of architecture and training? Any questions on that?

### 01:29:41 · Speaker 3

Sir here for a given xi we will receive only one vector z e of xi right

### 01:29:48 · Speaker 1

That is what I'm saying. So, for images, what they do is say this is a

### 01:29:54 · Speaker 1

Working offline error occurred

### 01:29:57 · Speaker 1

I don't know what error occurred

### 01:30:00 · Speaker 1

See input will be a let's say a 400 cross 600 image okay okay output will be a let's say 32 cross

### 01:30:12 · Speaker 1

50 dimensional vector okay where 32 is your k and 50 is your p what will be done is all of these v i's okay will be in 32 dimensional space what will be done is that each of these 32 dimensional vector 50 vectors will be quantized using the dictionary and the input of this will also be a 32 cross 50 dimensional grid

### 01:30:42 · Speaker 1

Do you see that? It is not one vector, it is a grid.

### 01:30:48 · Speaker 1

And each vector in that grid is quantized using the dictionary. That's how they do it.

### 01:30:58 · Speaker 1

This is alright

### 01:31:00 · Speaker 3

So in in the nave VAE we used to get the mu and sigma vectors

### 01:31:07 · Speaker 1

See, I told you, you look at this, right? I said that it's a latent space that is discrete and vector quantized and learnable. You could also say that the encoder is deterministic. It is not a probabilistic encoder.

### 01:31:22 · Speaker 3

No no sir I'm talking about the dimension

### 01:31:25 · Speaker 3

in in the naive vae the mu e we we used to get one mu per dimension right like for six and four hundred cross six hundred image we will be getting the mu vector of size four hundred cross six hundred right

### 01:31:41 · Speaker 1

No, no, no, no, no, definitely not. See, I've been telling that multiple times, right? This is a k-dimensional thing. If, if you're uh...

### 01:31:52 · Speaker 3

Okay okay like

### 01:31:54 · Speaker 1

Haven't you implemented VAE yet? See this is a k-dimensional thing.

### 01:31:58 · Speaker 3

Too sir I got confused here I got confused

### 01:32:00 · Speaker 1

This is k-dimensional, this is also k-dimensional, assuming that it is a diagonal matrix. Told this multiple times.

### 01:32:09 · Speaker 1

is one mu with a k dimensional thing because see this lies in a k dimensional space right it is z z is in k and therefore mu is also in k dimensions

### 01:32:22 · Speaker 1

Okay, any other questions on the architecture of V2V?

### 01:32:27 · Speaker 1

Okay so now we will have to train this right training VQVAE

### 01:32:41 · Speaker 1

the objective

### 01:32:44 · Speaker 1

is again the elbow rate will have two parameters it will have the encoder decoder parameters and also this lambda parameters note that lambda parameters are z1 to zm themselves

### 01:32:58 · Speaker 1

Now the lambda parameters are Z1 to ZM themselves right. Now the objective here is

### 01:33:10 · Speaker 1

You simply do a reconstruction task

### 01:33:19 · Speaker 1

And there is this other thing which is reduce the KL divergence between the output of the sorry reduce the the not the KL divergence the norm between the output of the encoder

### 01:33:38 · Speaker 1

and the quantized version of it

### 01:33:43 · Speaker 1

This is all the objective and it's very very simple

### 01:33:48 · Speaker 1

Right? This you optimize this with respect to. So, what is happening here is that.

### 01:33:55 · Speaker 1

gradients

### 01:34:02 · Speaker 1

xi look it as z e of xi

### 01:34:15 · Speaker 1

decoder this will be zq of xi this will be xi cap so now you have here z1 through zm right now once to learn the encoder of course the grade there is a forward pass like this

### 01:34:33 · Speaker 1

And there is a simple reverse pass right

### 01:34:37 · Speaker 1

In the reconstruction term

### 01:34:43 · Speaker 1

with respect to feet this is what you do

### 01:34:50 · Speaker 1

To learn the of course for the decoder also you do the same thing to learn the latent space what you should do is you should take the gradients of

### 01:35:18 · Speaker 1

written dictionary

### 01:35:22 · Speaker 1

to take the gradient of

### 01:35:27 · Speaker 1

particular term

### 01:35:36 · Speaker 1

respect to z itself and then back propagate see z you can take a here we know how to take gradients with respect to parameters right we can also take gradients with respect to vectors themselves and you see z1 to zm okay actually you have to take it with respect to uh all z i's here z j's where z j belongs to dictionary

### 01:36:03 · Speaker 1

the gradient with respect to the dictionary vectors themselves and then back propagate from the output from the output okay till the uh till this space so till the uh see you see this as another layer sort of right in the neural network this is a dictionary

### 01:36:26 · Speaker 1

the gradients will flow from the output of the decoder till here this is how it and this is how you update the gradients so now what will happen is your

### 01:36:39 · Speaker 1

g j you have to do it like vector by vector wise g j t plus 1 will be g j t randomly initialize that minus some alpha times the gradient of the elbow which is this term

### 01:37:02 · Speaker 1

respect to

### 01:37:09 · Speaker 1

Is this all right? This is how you do it. This is how the latent vectors are learned.

### 01:37:21 · Speaker 1

any questions on this? Otherwise, it is simply an autoencoder training. You have the encoder-decoder, you train both the encoder-decoders through backpropagation. The one extra thing is you learn the latent dictionary vectors themselves by doing a backpropagation through the latent dictionaries.

### 01:37:40 · Speaker 1

Is this all right Any questions on this

### 01:37:43 · Speaker 1

Deserve you try now we could be

### 01:37:47 · Speaker 2

Yeah so I mean is it can we see it like we are trying to find some basis vector of the data during the training

### 01:37:53 · Speaker 1

is known during the training it's not basis for data no it's uh it's uh you can say that it's the basis for the representation space of data okay data is being represented in the space

### 01:38:08 · Speaker 1

For that you are trying to learn the uh basis

### 01:38:11 · Speaker 2

And the number of vector that we choose would be a hyperparameter

### 01:38:15 · Speaker 1

M is a hyperparameter

### 01:38:20 · Speaker 1

Okay so now this is how you try in it so now once you try in this you'll have to do inference

### 01:38:40 · Speaker 1

First thing that we'll do is

### 01:38:43 · Speaker 1

a posterior inference

### 01:38:48 · Speaker 1

or embedding extraction right this is what we call as embedding

### 01:38:59 · Speaker 1

just straight forward right you have the encoder always for the posterior inference you take the encoder its test goes as an input to the trained encoder you will get a z e x test

### 01:39:17 · Speaker 1

The embedding

### 01:39:22 · Speaker 1

or X test

### 01:39:25 · Speaker 1

is simply

### 01:39:29 · Speaker 1

vector quantized version of Z that's all you have J equal to one through M you search for

### 01:39:42 · Speaker 1

Closest

### 01:39:44 · Speaker 1

In the quantized space I have written as a star because we learned it already.

### 01:39:50 · Speaker 1

This is the embedding is it all right

### 01:39:54 · Speaker 1

So as I said typically what happens is right you take a a grid of

### 01:40:00 · Speaker 1

across p right and quantize

### 01:40:07 · Speaker 1

column

### 01:40:10 · Speaker 1

That is what is done. Now this embedding, right, is the state of the art that is used in all the text to image generating models. They use, they take a VQVAE that is pre-trained on ImageNet. They take this embedding and use it for the and and try a diffusion model on top of these embeddings. Nobody starts, I mean, like the state of the art, right? People don't build diffusion models on data or rather in the

### 01:40:40 · Speaker 1

image space they do it on the the embeddings that are gotten by a VQVE trained on ImageNet

### 01:40:50 · Speaker 1

This is alright

### 01:40:54 · Speaker 1

questions on this how do you do posterior inference

### 01:41:05 · Speaker 1

hyperparameter that's a hyperparameter that is typically used uh i mean if you look at the vqve paper right the first there is vqvei one and vqvei two i think in vqvei one they take p to be lesser and then they show that p should be in fact you can actually make it a three-dimensional thing also no where you make each of it a a a map depends so that that depends upon uh the kind of network hyperparameter choice that you make

### 01:41:39 · Speaker 1

And you replace each of those columns by the, I mean, you vector quantize each of those columns. That's the point. Okay. Two, we have to do generation. See, um,

### 01:41:51 · Speaker 1

VQA's are not typically used for generation. As I said, right, they are only, they are mostly used for embedding extraction, okay, or inference. But you can also do generation from it, generation or sampling from VQA.

### 01:42:12 · Speaker 1

See one thing that is to be noted is that because since the latent space is vector quantized

### 01:42:21 · Speaker 1

Space is a discrete

### 01:42:29 · Speaker 1

write it as quantized

### 01:42:36 · Speaker 1

Quantized okay

### 01:42:39 · Speaker 1

One does not know the distribution of it. You see that?

### 01:42:47 · Speaker 1

doesn't know the distribution of it

### 01:42:59 · Speaker 1

See in a VAE we know that the latent space follows normal 0 1. That's why post training we can take sample from normal 0 1 and give it to the decoder and we will get the output right. Here we don't know what the distribution of latent space is. So that's why what is done typically is that you the way it is done is

### 01:43:21 · Speaker 1

Uh first

### 01:43:25 · Speaker 1

Extract

### 01:43:29 · Speaker 1

embeddings

### 01:43:35 · Speaker 1

of training data

### 01:43:44 · Speaker 1

Understood so what is done is given

### 01:43:49 · Speaker 1

X1 through Xn from the training data okay

### 01:44:00 · Speaker 1

Z1 through Z, we're using different notation for that, no? What shall we use? It's called the Z cap 1 through Z cap N where

### 01:44:18 · Speaker 1

The cap I is D

### 01:44:22 · Speaker 1

embedding

### 01:44:27 · Speaker 1

xi okay get this uh via uh encoding encoders so once by posterior inference now you get the embeddings then what is done as spitter

### 01:44:42 · Speaker 1

GMO

### 01:44:45 · Speaker 1

Actually what you can do is fit a generative model or train a generative model on top of these embeddings.

### 01:44:54 · Speaker 1

is the first step this is the second step you try na

### 01:45:00 · Speaker 1

Kinetic model

### 01:45:02 · Speaker 1

On

### 01:45:04 · Speaker 1

G1 cap through GNCAP. Now this generative model can be a GMM or in the in the VQA paper they try in what is called as a pixel CNN.

### 01:45:18 · Speaker 1

which is an autoregressive model, autoregressive generator model. We will see the autoregressive model later next in the course. So basically you try in a generative model on top of the latent embeddings that you got from the encoder.

### 01:45:37 · Speaker 1

No sample

### 01:45:41 · Speaker 1

Z nu Z cap mu from

### 01:45:46 · Speaker 1

Yeah

### 01:45:48 · Speaker 1

Generating model on Z1 cap to Zn cap okay

### 01:45:56 · Speaker 1

Then pass

### 01:45:58 · Speaker 1

C cap new through the decoder

### 01:46:08 · Speaker 1

Do you understand this

### 01:46:14 · Speaker 1

The problem is, unlike in a VAE, you don't know what the distribution of the latent space is, correct? Because it is discrete. Therefore, what they do, what is done is that once you learn the encoder-decoder, you take all the training data and pass it through the encoder and get the corresponding embeddings. Now that becomes a new data set, okay? On the embedding data set, you learn a generative model. Now you know how to sample from the latent space.

### 01:46:44 · Speaker 1

the VQVA right and therefore what you can do is once you learn a generative model on the legend space then you sample from it and give it to the decoder and decoder should give you a new data point

### 01:46:59 · Speaker 1

This is all right. In fact, people say that, I mean, this is also our experience, that training a generative model on the latent space of a VQVA is very difficult. And that's why VQVA is typically not used as a generative model itself. What is done is, PQVA is used for posterior inference. You get the embeddings and use a train a diffusion model on top of those embeddings.

### 01:47:24 · Speaker 1

Uh yeah in fact this is exactly in fact this is what is done in a stable diffusion and all that what they do is

### 01:47:33 · Speaker 1

Actually this is what is it done no you train uh

### 01:47:41 · Speaker 1

It can be a GMM or it can be a pixel CNN

### 01:47:48 · Speaker 1

Or it can be a diffusion model. That's exactly what is done in stable diffusion.

### 01:47:55 · Speaker 1

So basically you take a VQVAE get its embeddings learn a generative model on the latent space okay and generate a new sample in the latent space of the VQVAE and give that new generated latent sample through the decoder and get the X new. That is exactly what is done in in stable diffusion.

### 01:48:20 · Speaker 1

And all this imagine that you have Google's this thing, right? All the, I think it's J-E-N.

### 01:48:29 · Speaker 1

It's that Google's engine, right? All of these commercially available things, that's exactly what they do. They take a VQVAE.

### 01:48:39 · Speaker 1

Find a generative model on the latent space of the VQVAE and generate a new sample from the latent latent distribution of VQVAE and give it to the decoder to generate the image and what you see is the image but the generation is happening in the the latent space okay Sanjit

### 01:49:00 · Speaker 3

So if you are training a GMM on these embedding Z1 to Z, Z1 hat to Z1, Z and hat, so what shall be the mean and variances for a like a like individual Gaussian model?

### 01:49:17 · Speaker 1

That is what is learned in a GMM. In a GMM you don't fix the mean and variance of the individual Gaussians. That's what you learn. You learn the mean and variance of individual components in a GMM using EM.

### 01:49:35 · Speaker 1

Okay, so yeah, forget about GMM right now, right? You can, I mean, as I said, no, in stable diffusion, et cetera, the model that is, the generative model that is used on the latent space is actually a diffusion model, which we will see right now.

### 01:49:52 · Speaker 1

Okay so if you understood good so this is the

### 01:49:58 · Speaker 1

of VAEs in one form because the diffusion models are also VAEs but yeah so in the naive form this is the end of VAEs see I have not asked you to implement a VQVA in your assignment because I thought it would be too much but yeah if any one of you have some bandwidth and time I'd be happy to see you implementing VQVA that would be great if you can do that

### 01:50:20 · Speaker 4

Yeah

### 01:50:24 · Speaker 2

you know which we can we can we can with discrete letter to space

### 01:50:30 · Speaker 1

And so cruel of me

### 01:50:37 · Speaker 1

Okay I think then you should do it yeah you can you should do it

### 01:50:41 · Speaker 1

Okay so great

### 01:50:45 · Speaker 1

I thought I didn't expect this to take so much time but it's worth it it's fine

### 01:50:49 · Speaker 1

Okay, so shall we take a break? Been talking for one and a half hours, one hour 45 minutes now.

### 01:50:58 · Speaker 1

Uh as I said I need to leave like five minutes to eleven uh so let's not take a long break let's take a short break ten minutes ten twenty we'll be back

### 01:51:11 · Speaker 1

Is that okay

### 01:51:13 · Speaker 1

Do you do you need fifteen minutes? Ten minutes is enough I suppose.

### 01:51:20 · Speaker 1

Yeah let me try

### 01:51:21 · Speaker 2

What are you doing

### 01:51:22 · Speaker 1

Yeah, so please come back at 1020 because we'll start diffusion models. Don't miss the introduction. That's very important. Yeah, let's reconvene in about 10 minutes. See you.

### 02:07:47 · Speaker 3

You are on mute

### 02:07:48 · Speaker 4

So you are

### 02:07:50 · Speaker 2

So you're on mute

### 02:07:52 · Speaker 1

Oh my god I got scared

### 02:07:56 · Speaker 1

okay i'm sorry yeah so it's just speaking one mute

### 02:08:05 · Speaker 1

So the next topic that we will see in this course is about DDPMs also called as expanded as denoising diffusion probabilistic models.

### 02:08:22 · Speaker 1

I'm audible now right

### 02:08:24 · Speaker 3

Yes sir you are audible

### 02:08:28 · Speaker 1

Okay, so now the state of the art generative models in all the vision language models that you see today, right, are based on DDPMs. They are

### 02:08:45 · Speaker 1

Neither VAEs nor GANs right I mean people have moved on onto these these new class of models

### 02:08:57 · Speaker 1

on called DDPMs denoising diffusion diffusion probabilistic models uh we'll study that um so basically right it's um

### 02:09:11 · Speaker 1

So DDPMs

### 02:09:14 · Speaker 1

The plan is that I will set up the problem today in this class

### 02:09:19 · Speaker 1

Uh and then we will uh look at the rigorous math and all that in the next uh coming classes

### 02:09:27 · Speaker 1

Um there is one tutorial by

### 02:09:32 · Speaker 1

you what that is it's a very nice tutorial I'll put it on the chat now

### 02:09:44 · Speaker 1

very very good okay i encourage all of you to follow that and go through it it will cover everything uh that i'll be doing in this class okay i found it very it's a it's a 100 page tutorial it's almost like a short book but it is extremely good let me just put it here

### 02:10:10 · Speaker 1

You want me to put it on teams also that also I can do hold on

### 02:10:32 · Speaker 1

Names

### 02:10:42 · Speaker 1

I think it's already there

### 02:10:49 · Speaker 1

So whatever I put in here in the meeting chat it will appear on the Teams chat

### 02:10:54 · Speaker 2

It's it's

### 02:10:54 · Speaker 1

Yeah

### 02:10:54 · Speaker 3

S

### 02:11:00 · Speaker 1

tutorial on diffusion models

### 02:11:08 · Speaker 1

Please have a look at it this is pretty much what I cover okay

### 02:11:14 · Speaker 1

Sure sir so it's a good tutorial have a look at it okay

### 02:11:19 · Speaker 1

So um

### 02:11:23 · Speaker 1

Basically the idea is the following that DDPM is is actually is a special case of VAE

### 02:11:40 · Speaker 1

Now you can actually see DDPM as a special case of VAE with the following properties

### 02:12:03 · Speaker 1

So if you look at this tutorial right he has actually derived the elbow also done reparameterization everything maybe I'll just show you that once hold on

### 02:12:29 · Speaker 1

Did you see my screen

### 02:12:34 · Speaker 1

You see it's very very recent now it has come out on 10th of September it's pretty good so they start with VAEs okay so there is this encoder decoder or definition of latent variable

### 02:12:47 · Speaker 1

And yeah, he also talks of GMM. See, this thing very much aligns with my narrative as well. I mean, you should trust me when I say that I did not build my narrative looking at this because I've been teaching this course since three years. This man has used a very similar narrative as what I do. Okay. So then he goes to the evidence lower bound, constructing the evidence lower bound and decomposition of the log likelihood as elbow.

### 02:13:17 · Speaker 1

using the variational distribution interpretation of elbow

### 02:13:23 · Speaker 1

Right reconstruction and prior matching terms

### 02:13:30 · Speaker 1

Okay so optimization in BAE

### 02:13:36 · Speaker 1

The parameterization

### 02:13:42 · Speaker 1

These are exactly the things that I did. I don't know, right? Maybe somebody who looked at my notes, but that was not public at all. I don't know how. But anyway, exactly the thing that I did, okay? So VAE encoders.

### 02:13:56 · Speaker 1

and parameterization tricks in high dimensions scale divergence between two Gaussians

### 02:14:05 · Speaker 1

this vae training and then they completed this concluding remark then they come to uh ddpms this is a very good tutorial okay so please have a look at it it'll actually give you uh a lot of insights about vae and also the ddpms that i'll be covering okay so and also as i said right uh thankfully it is very very similar to the kind of story that i have told you the narrative that i have built so that very nicely

### 02:14:35 · Speaker 1

aligns with what we have done so please have a look at it

### 02:14:40 · Speaker 1

a minute there is cleaning let me bring my charges now a minute

### 02:15:21 · Speaker 1

Okay, so DDPM is actually a special case of VAE with the following properties. Okay, so we will see all those properties one by one.

### 02:15:32 · Speaker 1

you can hear me and see my screen correct

### 02:15:37 · Speaker 2

It's a

### 02:15:41 · Speaker 1

Okay, see one thing is that

### 02:15:45 · Speaker 1

Yeah

### 02:15:51 · Speaker 1

The first thing is that there are

### 02:15:58 · Speaker 1

Latent spaces

### 02:16:08 · Speaker 1

Okay uh unlike

### 02:16:15 · Speaker 1

One latent space in a VAE

### 02:16:24 · Speaker 1

There are uh yeah so this is a hierarchical

### 02:16:34 · Speaker 1

So there are multiple latent spaces here unlike in a VAE where there is one latent space. So basically what happens in a VAE is that start from the data space, project to the latent space and from the latent space you get back to the data space. This is a VAE.

### 02:16:55 · Speaker 1

In a DDPM diffusion model what happens is start from X get to the first latent space Z1 and from the first latent space you get to Z2 get to Z3

### 02:17:09 · Speaker 1

some z n let's call it right and from zn

### 02:17:18 · Speaker 1

back to Zn minus one retrace it back

### 02:17:36 · Speaker 1

Do you understand this? Instead of having one latent space, you have multiple latent spaces in a hierarchical fashion.

### 02:17:45 · Speaker 1

It's all right

### 02:17:47 · Speaker 1

So now why do we do that is that because see uh

### 02:17:53 · Speaker 1

Think of it like this. Start from data. Let's say that you have a very high dimensional data. Projecting, the motivation is that projecting it onto a latent space in one step and trying to compress it, making it compact in one step might be very difficult for the encoder, right? So typically, projection from the data space to the latent space is the encoding process and from the latent space back to the data space is the decoding process, right? Similarly, you have hierarchical encoding.

### 02:18:24 · Speaker 1

And you have a hierarchical decoding in a DDPM. Is this idea clear? So as I said, no, we will write rigorous math and we will concretize everything that we do eventually. But yeah, so high level, is this clear?

### 02:18:41 · Speaker 3

Sir can you c comment on the dimension of G1 G2 G3 and G4

### 02:18:44 · Speaker 1

We'll do that we'll do that we'll do that one thing at a time This hierarchical thing the second thing that you do is that the

### 02:18:57 · Speaker 1

Dimensionality

### 02:19:01 · Speaker 1

of the latent space

### 02:19:05 · Speaker 1

of all the latent spaces

### 02:19:19 · Speaker 1

is same as that of the data space

### 02:19:43 · Speaker 1

Again, typically what happens in a VAE is that dimensionality of the latent space is much less compared to that of the data space, right? But in a DDPM, the dimensionality of the latent space is exactly same as that of the data space.

### 02:20:00 · Speaker 1

That is the second property. The third property that is used is

### 02:20:10 · Speaker 1

Encoding

### 02:20:14 · Speaker 1

Encoding process

### 02:20:20 · Speaker 1

Not learnable

### 02:20:26 · Speaker 1

Part fixed

### 02:20:35 · Speaker 1

Markov process

### 02:20:42 · Speaker 1

See in a VAE what do we do so VAE

### 02:20:48 · Speaker 1

we do is q of q phi of z given x okay

### 02:20:53 · Speaker 1

is learned right

### 02:20:57 · Speaker 1

Elbow

### 02:21:01 · Speaker 1

Here

### 02:21:06 · Speaker 1

Q of g given x

### 02:21:09 · Speaker 1

non-runnable it's fixed so you see that fee is there's no fee here

### 02:21:25 · Speaker 1

Do you understand?

### 02:21:28 · Speaker 1

Not learnable

### 02:21:32 · Speaker 1

The encoding process is defined using a Markov process there is nothing to learn here

### 02:21:40 · Speaker 1

is all right so that implies that only decoding

### 02:21:45 · Speaker 1

Only the decoding decoder is learnt

### 02:21:49 · Speaker 1

There's no one decoder decoding process is learned

### 02:21:58 · Speaker 1

So now if you incorporate all three of these properties, right, which is that there are, you take hierarchical latent spaces and you match the dimensionality of the latent space to that of the data space, and you make the encoding process a fixed one, but not learnable, then the resulting VAE is called DDPM. That's all it is.

### 02:22:19 · Speaker 1

The rest is only algebra and mathematical details. So what we will do is we will incorporate these properties into a VAE and we will write down the elbow for this sort of a VAE. And when we optimize that and we do the algebra, we will end up having the loss functions for a DDP.

### 02:22:44 · Speaker 1

Okay, so that's why I taught Gyan's first and then came to VAEs. And then we are going to DDPM because DDPM is a special case of VAE with these properties. Any questions on this?

### 02:22:56 · Speaker 2

Um s sir uh what does Markov process mean just a random process or

### 02:23:01 · Speaker 1

Yeah, I'll tell you. See, for now, think of it like a, like, I mean, I'll write all the equations and it'll be clear, right? So basically, what do I mean by Markov process is that start from the data space, right? You go to the first latent space, from first latent space, you go to the second latent space, from the second latent space, you go to the third latent space and so on, right? By Markov process, I mean that if you take the tth latent space, okay, it only depends,

### 02:23:31 · Speaker 1

on T minus first related space and it does not depend on anything else.

### 02:23:37 · Speaker 2

Okay understood time based

### 02:23:40 · Speaker 1

There's no time per se here because

### 02:23:42 · Speaker 2

Iteration

### 02:23:44 · Speaker 1

Uh it's not even iteration right you can call it as the latent space index

### 02:23:49 · Speaker 2

Understood yes

### 02:23:49 · Speaker 1

And you can call it time if you want. I mean, if you want to see that as start from the data, you go the first time instant, you go to the first latent space, second time instant, you go to the second latent space, and so on.

### 02:24:02 · Speaker 1

Any questions on this on on on the high level formulation

### 02:24:08 · Speaker 1

Yeah isn't it

### 02:24:10 · Speaker 3

Sir so here are we saying that we are not taking the data batches but one data point at a time

### 02:24:18 · Speaker 1

No, no. See, it still do everything on a batch level. See, every every analysis that we do is for one data point, right? Because doing it on a batch is only one another summation at the outside. All the VA analysis, we did it for one data point. So now this is for one data point. Everything that I'm doing is for one data point. Okay.

### 02:24:42 · Speaker 3

Okay

### 02:24:42 · Speaker 1

You look so wee

### 02:24:44 · Speaker 3

Like we are saying at time, like at one time we reached the first latent variable and at the next time we reached the another latent variable. So

### 02:24:57 · Speaker 3

Had that part like I was not clear

### 02:25:00 · Speaker 1

one there's no i i said there's no one time see in a va i wrote it here right what do you do in a vae start from the data point get to the latent space using encoding and get back to the data space now in a ddpm you start from one data point go to the first latent space from first latent space you go to second latent space from second latent space go to third latent space and so on that's all

### 02:25:25 · Speaker 1

We are doing it for one data point. I mean, of course, everything that we do, we'll do it over batches. But yeah, so, but analysis we do for one data point, right? All the elbow, et cetera, we do it for one data point, assuming that we only have one data point and you just put a summation outside data.

### 02:25:42 · Speaker 3

Answer this encoding is it probabilistic still

### 02:25:46 · Speaker 1

It is probabilistic but fixed

### 02:25:49 · Speaker 3

Probabilistic but fixed

### 02:25:50 · Speaker 1

Not learnable by by fixed I mean learnable we'll write the equations it will become more clear yeah

### 02:25:56 · Speaker 1

Okay so let us uh go to the math now um

### 02:26:03 · Speaker 1

Any other questions on this?

### 02:26:08 · Speaker 1

Let's

### 02:26:25 · Speaker 1

Unfortunately, the community has used a different set of notations than VAE. So I will use the same notation as there as as it is there in the papers and the other tutorials. So it's a weird notation. Please bear with me on that. So data

### 02:26:45 · Speaker 1

He is represented

### 02:26:51 · Speaker 1

Using X not okay

### 02:26:55 · Speaker 1

So what used to be I'll just write the things that we were doing earlier also earlier using some other color this was our X okay

### 02:27:07 · Speaker 1

And

### 02:27:12 · Speaker 1

latent space

### 02:27:15 · Speaker 1

is represented using

### 02:27:18 · Speaker 1

X one X two

### 02:27:21 · Speaker 1

2 XN

### 02:27:23 · Speaker 1

X capital T please note that this has this is not the data points that we had as I said it is unfortunate because this is a very very non-standard notation okay so let's call this T

### 02:27:39 · Speaker 1

Latent space is typically represented using Z, okay? But the DDPM community, they represent that using X1, 2.

### 02:27:49 · Speaker 1

X capital T and data is represented as X naught. So this is what we used to call

### 02:27:57 · Speaker 1

Z1 Z2

### 02:28:00 · Speaker 1

ZT okay I'll write this not to be confused

### 02:28:11 · Speaker 1

That's the usual notations

### 02:28:20 · Speaker 1

Well

### 02:28:25 · Speaker 1

One through XN were data points.

### 02:28:33 · Speaker 1

Okay, is that okay? Because see now from now to the end of DDPMs, we'll be using this new notation. So now let me clarify x0 is the data point. And also note that all that we are doing is for one data point. So we'll do it for a single data point. x1, x2.

### 02:28:56 · Speaker 1

LXTR

### 02:29:02 · Speaker 1

latent vectors

### 02:29:10 · Speaker 1

latent vectors corresponding to x naught

### 02:29:14 · Speaker 1

this okay so now the the encoding process is that you start from x naught go to x1 and then from there to x2

### 02:29:30 · Speaker 1

This is the encoding process

### 02:29:37 · Speaker 1

Is this

### 02:30:02 · Speaker 1

Vectors of same dimensions

### 02:30:16 · Speaker 1

Is this alright notation wise

### 02:30:28 · Speaker 1

Yeah, yeah. Please get used to this notation because as I said, no, very, very non-standard notation, but that's what the community uses and I am not changing it. So just to ensure that that.

### 02:30:43 · Speaker 1

Notationally it is correct uh consistent across

### 02:30:50 · Speaker 1

no no this guy uses uh exactly the same terminology as i do i'll show you this that's a serendipity

### 02:31:07 · Speaker 1

Is my screen visible

### 02:31:12 · Speaker 3

Yes certainly

### 02:31:13 · Speaker 1

Look at this note

### 02:31:16 · Speaker 1

X naught it is the original image which is the same as X in VAE. XT is the latent variable which is same in Z in VAE.

### 02:31:24 · Speaker 1

Okay x1 and x t minus 1 they are intermediate states or intermediate they are also latent variables but they are not

### 02:31:33 · Speaker 1

White Goshen yeah that is okay yeah so I strongly recommend all of you to go through this okay so I mean of course

### 02:31:42 · Speaker 1

in parallel to what we have been doing. But yeah, so it's very consistent with what my narrative is and also the notations. Is the notation clear now? Please note that the dimensionality of all of these latent vectors are exactly same as that of the data space. I'll write that maybe.

### 02:32:04 · Speaker 1

prime of x naught

### 02:32:07 · Speaker 1

Same of dime off

### 02:32:11 · Speaker 1

E or T in

### 02:32:15 · Speaker 1

So note that x naught is your uh data vector

### 02:32:22 · Speaker 1

Is this clear

### 02:32:24 · Speaker 1

Is the notation clear

### 02:32:31 · Speaker 1

Okay now we will define the

### 02:32:41 · Speaker 1

encoding process

### 02:32:46 · Speaker 1

Dippy

### 02:32:48 · Speaker 1

also i tell you why is it called a denoising diffusion probabilistic model we will not leave anything out okay so but yeah we'll i'll give you the easiest narrative first and then i'll connect every dots don't worry okay let us define the encoding process in dtpm so now what is encoding that projection from x to z is the encoding process right this is the encoding process how is it done in uh in a in a dtpm is that it is done in a markovian way what does that mean

### 02:33:18 · Speaker 1

Mean that you make your x1, which is the first latent variable, to be equal to

### 02:33:29 · Speaker 1

alpha naught times x naught

### 02:33:35 · Speaker 1

1 minus alpha naught times

### 02:33:40 · Speaker 1

Epsilon

### 02:33:45 · Speaker 1

where epsilon is coming from normal 0 1 this is the definition of encoding in a DPU okay so now similarly x2

### 02:33:57 · Speaker 1

alpha one times x one

### 02:34:02 · Speaker 1

one minus alpha one times

### 02:34:05 · Speaker 1

So let's call this as epsilon 1 or epsilon naught and this is as epsilon 1. So actually they are all samples from the same normal distribution. You are doing different samplings that's all. So and so on. In general you have x the tth latent vector is given by alpha t times x t minus 1 plus 1 minus alpha t times some epsilon t.

### 02:34:35 · Speaker 1

If I learn D is going from not once it'll look

### 02:34:40 · Speaker 1

This is the encoding process. This is the fixed encoding process. You see that there is nothing learnable here. This is probabilistic, but there is nothing learnable.

### 02:34:51 · Speaker 1

Is this clear

### 02:34:52 · Speaker 2

t minus one right alpha t minus one

### 02:34:59 · Speaker 1

Yeah yeah yeah I can do that I'll write that

### 02:35:11 · Speaker 2

Is this a type of microphone process

### 02:35:13 · Speaker 1

It is a macro process. Just a second, I just want to be consistent with the notation. Just a second, I'm just looking at that P14T.

### 02:35:26 · Speaker 1

This is alpha T okay

### 02:35:29 · Speaker 1

People generally like write this as alpha t

### 02:35:38 · Speaker 1

This is alpha one

### 02:35:41 · Speaker 1

This is alpha two. Again, it doesn't matter, but just want to be consistent. So where?

### 02:35:49 · Speaker 1

Alpha one through alpha

### 02:35:53 · Speaker 1

T E right are fixed scalars

### 02:36:02 · Speaker 1

between zero and one okay

### 02:36:05 · Speaker 2

epsilon index as well so

### 02:36:08 · Speaker 1

epsilon index epsilon index is okay i mean yeah so see epsilon i can write it as epsilon every time it's just samples from a normal distribution right there is nothing uh like sacrosanct about this one two etc but okay fine can call it epsilon t

### 02:36:27 · Speaker 1

is this is this clear is this all right do you understand what's happening see what is happening is that you take the data point okay uh see this can be seen as some noise right when you take some noise scale it add it to the data point so that will give you the first latent vector okay then you take that first latent vector okay uh take some noise scale it add it and then you get the second latent vector and so on so this

### 02:36:57 · Speaker 1

This is whatever I have written here right this

### 02:37:02 · Speaker 1

is actually a first order

### 02:37:06 · Speaker 1

Markov

### 02:37:09 · Speaker 1

process

### 02:37:12 · Speaker 1

It's Gaussian transitions because the noise that we are adding is Gaussian

### 02:37:23 · Speaker 1

And

### 02:37:25 · Speaker 1

What is the spelling of transition trend

### 02:37:32 · Speaker 1

E I T A O N is it

### 02:37:35 · Speaker 1

Oh I say win

### 02:37:38 · Speaker 3

It's a dog

### 02:37:38 · Speaker 1

SITI SITI one SITI one

### 02:37:38 · Speaker 2

I say it's a

### 02:37:44 · Speaker 1

gaussian transitions okay so basically what is happening is right you can see this as like this suppose we start with an image

### 02:37:53 · Speaker 1

Okay so this is X naught what are we doing we are just taking some

### 02:38:00 · Speaker 1

Gaussian noise with the same dimensions okay adding it to this of course you scale it with alpha and add it with that so you get

### 02:38:13 · Speaker 1

So called noisy version, this will give you the first latent space, right? And then you add.

### 02:38:21 · Speaker 1

Another noise and this is alpha two and you get

### 02:38:25 · Speaker 1

made with

### 02:38:28 · Speaker 1

noise and so on right we keep doing it and as a result that would say that if you keep doing this at xt with sufficiently large t this xt right xt will follow a normal distribution 0 1 so this is called the stationary distribution of a Markov chain

### 02:38:54 · Speaker 1

So if you create a Markov chain like this it will go to a

### 02:39:03 · Speaker 1

Normal 0 1 is what is known. Okay, so hold on, let me just show you a picture.

### 02:39:11 · Speaker 1

This is how you create the encoding process. This is the encoding process of a Markov chain. Let me offer of a DDP. Okay, let me just show you this.

### 02:39:21 · Speaker 1

I mean of course your assignment will be one of your third assignment will be on this so you will implement all this and appreciate it

### 02:39:30 · Speaker 1

You see my screen

### 02:39:33 · Speaker 1

This is what I'm talking about and starting from makes not you create a sequence of latent variables by adding noise

### 02:39:45 · Speaker 1

Okay so the fiction is

### 02:39:46 · Speaker 4

That's prediction

### 02:39:48 · Speaker 1

Come again

### 02:39:51 · Speaker 1

You see this here

### 02:39:54 · Speaker 1

this is the process right you start from X naught just keep adding that noise and you get a

### 02:40:03 · Speaker 1

encoding process is this all right

### 02:40:17 · Speaker 1

Okay, so I think this is a good time to stop. So please again look at this and read my look at my notes. So we will continue from here from the next class. So we'll have to leave now.

### 02:40:30 · Speaker 1

Okay, so the summary is that a DDPM is a VAE, a hierarchical VAE with multiple latent spaces with the property that the dimensionality of the latent space is exactly equal to that of the data space and the encoding is a fixed process. It's there's nothing learnable. What you do is you take the

### 02:40:51 · Speaker 1

uh and create a markov chain by adding gaussian noises and that will give you the latent embeddings so what do you do with it and how does this become a uh this thing a generative model and all that we'll see in the next class so basically what we do is we will create a decoding model and we will write the elbow that we were writing for vies and then derive a loss function for it that is what we'll do in the next class please have a read at that uh uh that that tutorial that i've shared

### 02:41:21 · Speaker 1

So my handwritten notes is also there. They're also have done it and yeah and look at my notes and come prepared for the LBO and look at VAEs. Okay. The next class we will do the math for the diffusion models. Is that all right?

### 02:41:35 · Speaker 1

Again, you know, thank you for being accommodating. Okay, so I'm sorry about moving everything one hour before. So you have a quiz now, please wait. Let me just call Chandan.

### 02:42:06 · Speaker 1

Can he not pick up

### 02:42:09 · Speaker 1

Now Chandan I am done with the class

### 02:42:14 · Speaker 1

Yeah so can you please join that link students are here and then conduct the quiz

### 02:42:20 · Speaker 1

So so I ask the students to wait just join there and you can conduct the quiz

### 02:42:29 · Speaker 1

No, no, I just completed because I have to leave now. Yeah. So the thing is, see, one other thing, right? If after the quiz, if students have some time they can spare, you can maybe just take a tutorial or rather just do some, I mean, do that exam thing.

### 02:42:48 · Speaker 1

see okay no problem you can conduct the curriculum then leave okay okay okay okay so students are waiting so you can please come online and go okay thank you

### 02:43:01 · Speaker 1

Okay so I just spoke with him Chendan will be here in about two three minutes and please take that quiz and then you can leave we will meet next week

### 02:43:10 · Speaker 3

Sir the next quiz is supposed to be a week after the next one

### 02:43:14 · Speaker 1

No no no no no uh see we have to do six quizzes right we will i'll i'll talk i'll talk to chandran so we have this is the this will be the third quiz right

### 02:43:24 · Speaker 1

be third quiz we have three more uh so we will uh i and chandan will discuss about it and let you know because we have what four more weeks and we need to do three quizzes right so what we can do is we can skip on that diwali week and rest of the weeks we can have quiz every week

### 02:43:35 · Speaker 3

I'm not getting

### 02:43:42 · Speaker 1

We'll do it that way

### 02:43:45 · Speaker 2

Yes

### 02:43:45 · Speaker 1

We'll do it that way. I will I will I will discuss about it and uh keep you notified on the whatsapp group and teams okay

### 02:43:54 · Speaker 1

Okay I really have to leave now so please stay do this uh I'll leave next week

### 02:43:58 · Speaker 2

I'll take it

### 02:44:00 · Speaker 1

Okay thank you

### 02:44:01 · Speaker 3

All the best sir for your interview

### 02:44:03 · Speaker 1

Oh my god you know exactly

### 02:44:08 · Speaker 1

Okay, see you guys

### 02:44:10 · Speaker 3

Okay so anyway
