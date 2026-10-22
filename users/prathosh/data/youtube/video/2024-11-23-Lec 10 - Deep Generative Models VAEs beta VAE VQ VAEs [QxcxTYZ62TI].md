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
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: I think two voices it is it from


Okay yeah


Okay so last class we completed VAE straight


Hello

speaker_2: Yes sir yes sir

speaker_1: Yes sir


Its for computer okay


Okay so maybe quickly uh well take five 10 minutes to look at the inference I think training of EAE was done I suppose And uh


I hope that you people could revise everything that we had done in the wake of exam right So that you are up to the speed Okay So what Ill do today is like initial five ten minutes and just complete the inference part of VAE okay Just ten minutes and then well move on to the diffusion models okay So thats what the plan for today is


Before we continue I just want to see how many classes are we left with 19th is 19th we have one class 26th we have one class


Second also we can have a class right


So yeah

speaker_2: Im sorry

speaker_1: One two three four


Four


and 9th 5th and 16th also we can have a class So even though they have said that 14th is the last working day last class day we can also have a class on 16th


So that there will be one two three


Four


One two three four

speaker_2: Ive been shooting today

speaker_1: five including today Yeah I think thats good So what Ill do today we will start the DDPM diffusion models Maybe next one more class I will complete DDPM Okay So that will leave us with three classes three more classes


Yeah thats good enough So one class for autoregressive models and LLMs and


Think yeah thats what we can cover a lot more growth

speaker_2: Sir but we didnt do VQVA and

speaker_1: I will do that today So initially today before I complete Ill do inference on VAEs and Ill do VQVAEs and then well go to diffusion models


Okay thats it

speaker_3: encoded

speaker_1: You mean the training you are saying

speaker_3: Yes yes

speaker_1: Thats the process Ill do that


So this is there in your second assignment right So when you implement it it will become much more clearer anyway Ill do that


Okay


Okay so as you know right we have these two components the encoder and decoder Encoder is probabilistic


Okay I also told you why this would be a reconstruction cost right Ah yeah we have done that Okay Why would the log likelihood becomes a reconstruction cost Okay that also we have done Good Okay So here is how a VAE works So you take a sample xi and this is of course for training Take a sample xi which is the data sample Pass it through the encoder This is the forward pass So once you pass it through the encoder


get a mean and a variance typically how is it done is if k is the dimensionality of your latent space


the output of the encoder


The output of the encoder is


This is D dimensional


This is D dimensional okay And this will be


dimensional so typically what what will be done is this will also be a k dimensional vector see actually it should be a k square dimensional vector uh people take it as k dimensional vector by by assuming a diagonal covariance okay if you assume this to be a diagonal covariance then you only have k parameters right because its only a diagonal matrix so input is a d dimensional vector which is a which is an image or whatever right and the output of encoder will be two


k dimensional where first k dimensions will be corresponding to the mean and the next k dimensions correspond to the variance


Now once you get the mean and variance what you do is you sample a Gaussian distribution outside of the neural network epsilon j


You do this reparameterization which is you add this mean that the output of the encoder has given okay to epsilon which is scaled by sigma


That will give you a ZJ So take that ZJ okay and pass it through the decoder And the output of the decoder is taken to be XJ cap So this is one forward pass Any questions on this

speaker_2: Sir when we say variational inference sir like what do we mean by that

speaker_1: No no no hold on I still not come to that We are not talking about inference We are only talking about training now See one forward pass through encoder and decoder is this That much is clear So pass a sample through the encoder get your parameters reparameterize it Sample outside the neural network reparameterize And then again pass it through the decoder You get an X cap So that is one pass through the encoder decoder Okay Now to train the encoder what you do is encoder has two layers


right one is the uh the kl loss this is to train the decoder we saw how to train the encoder here yeah to train the encoder we had once you get the x cap right you compute this um


deconstruction term okay And then you back propagate it by keeping the decoder parameters fixed okay And there is also a once you come to the input of the decoder you have the KL term also Differentiate that KL term with respect to the encoder parameters and then differentiate through this reparameterization term and then back propagate all the way through the input of the encoder So that is one backward pass through the encoder


Is that okay Any questions on this


So to train the encoder you will have to do one forward pass through the encoder and decoder and then one backward pass through the decoder and the encoder again While you are doing backward pass through the encoder you also have to add the KL loss


And for the decoder training one forward pass through the encoder decoder get the output of the decoder compute the reconstruction loss and one backward pass through the output of the decoder


That completes the training we


Any questions on this


Okay so once this is trained what do we do with it


Is it not

speaker_3: You can just write anything and then it will score

speaker_1: Inference between


So post training VAE can be used for two tasks Okay The first task is


Posterior inference


As I said in the previous class what do you mean by posterior inferences given


Data point X


So lets call that as lakes


or something because this is not in the training data okay


Finding the


responding


Latent vector


also called as embedding


This is what is called as


is the test okay so this is what is called as posterior inference i told you right uh any latent variable model uh one of the advantages is that once you try in a latent variable model you can get an embedding corresponding to uh the given data point that is what we do in all these encoder decoder based llms also right the uh the encoder will give you an embedding corresponding to data now how do you do that take the encoder


Just trying okay


star so you pass x test to this and what you get here is


mu v star at x test


to get sigma c star at x test


This is what you get right now the


Embedding


of extra x tests


are multiple options right can be taken to be


mu phi star itself So this itself can be taken as an embedding corresponding to H star This is one possibility The other possibility is you sample an epsilon from


normal 0 1 okay lets call this embedding 1 normal 0 1 and then take z test to be equal to lets call this epsilon t epsilon t times


Basically you do the reparameterization


New v start test


This now becomes


embedding for its test


and B Z test also


this lets call this embedding too so you can get so for any data point right you can get an embedding this way just pass it through the encoder you either take the the mean of the encoder itself as the embedding or you do a sampling outside of neural network reparameterize and take that as an embedding so now how do you use this embedding is up to you you can use it for a class if you say use it in a classifier see what happens is


We know that the dimensionality of the test


know that this is much much less than dimensionality of x test so what can be done is you can try in a classifier


using z test right or do you can do arithmetic uh in the embedding space and all that right so


I can see it


Bangalore weather since last 15 days had made it has made everybody sick


Z test can be used


Classification


Okay or like compression


You can do contrastive learning on top of it etc


Well talk about this contrastive learning later in the class I mean later in the course So basically you can use this embedding to whatever effect that you want Thats the idea So this is called posterior inference Any latent variable model right You can


get this meaning post training you can use the encoder to get the embedding corresponding to unseen data points I mean of course you can get embeddings corresponding to the training data as well entire data you can get the embedding take the trained encoder pass the data through the trained encoder and you get the embedding and use it for whatever task downstream tag the downstream task that you would need so that is about the posterior inference using latent variable


models any questions on this


Yeah uh Shirisha

speaker_4: Yes sir Sir uh so when you said Z tests can be used for classification what kind of classification you mean

speaker_1: Lets say that you have built a VAE on MNIST right Now you want to train a classifier on MNIST Typically what you do is you take the images and train a classifier on MNIST right So instead of doing that you take the embeddings on the MNIST and you train a classifier using embeddings


Does that make sense

speaker_4: Okay so basically we are trying to classify the class of the images it

speaker_1: Anything So it doesnt matter right Your input can be image or it can be text or anything depending upon what sort of data you have But the idea is that you can instead of using X test you can use Z So whats I mean a more interesting question is what advantage do you get by using Z instead of X


Now the answer to that is actually if you have learned a good encoder decoder model right the hope is that the embeddings that you have gotten is well clustered and well behaved Because I mean as I told you in one of the earlier classes these naturally occurring data will be in very high dimensional spaces and they will all be scattered no because of curse of dimensionality They will not be well clustered


If you learn a representation in a lower dimensional space it will be much more clustered and classifiers would behave much better in the embedding space compared to the data spaces the HOOP


Tell me this in your assignment have I asked you to use these embeddings and build a classifier

speaker_2: Yes sir

speaker_1: This is exactly what I have asked you to do right Try in a VAE and then get the corresponding Zs and then use it in a classifier And I think I have asked you also to compare this with a classifier that is built only on the data space also right

speaker_2: Yes sir

speaker_1: Have I Let me just open the assignment and see


asked you right yeah yeah so thats what it is so first you have to use a cnn and classify that classify the data and then use these embeddings and reduce the network size and simply use an mlp and see what happens on top of it


Yeah service

speaker_3: So so for this uh parameter reparameterization so this is eps the sigma should be raised to half right because we need some standard deviation type component to be added

speaker_1: uh that depends on yeah that depends on what you are representing as sigma no im representing that root of that itself as sigma depends i mean thats just a scaling factor right

speaker_3: So were actually getting standard deviation type


But Ill be right back

speaker_1: That is what Im saying right So now if you represent the output of your encoder as standard deviation then you raise it to power of half If I say that its the variance then you dont have to Depends upon how do you see it thats all


Oh send it

speaker_2: Sir is this the right time to ask that about variational inference like

speaker_1: Ah see this is this is posterior inference Okay Posterior because what youre actually calculating here is youre calculating


P theta P phi star of Z given X right


I mean technically speaking not P its the


I was going to say that this is


Yeah

speaker_2: Yeah

speaker_1: Yeah Q star Q star Q phi star of Z given X correct


Now this is inference definitely because given an x you are giving a z okay and this is posterior I mean technically speaking you can actually call this variational posterior inference


Variational posterior inference variational because


We dont have


access to


p theta star z given x this is the true posterior distribution right


are using


Ah variation and distribution


distributive distribution which is Q phi of Z given X


approximate it so that is why its called the variational posterior okay uh in fact in your exam i had asked you to uh start from the kl divergence between these two distributions and derive the elbow


Do you remember that question

speaker_3: Yes yes

speaker_1: We had told you that you start from the KL divergence between the variational distribution


And this


And show that minimizing this


boiled down to the elbow objective that you optimize in VAE correct


So this is exactly what it is right I mean you can actually see see the entire analysis that we did in VAE was by saying that we want to maximize the log of


the data likelihood under the latent variable model right thats how we derive the elbow the entire story can be constructed via this route okay its only an algebra you can you should just write this scale divergence and write this posterior in terms of the joint distribution between x and z and marginal and then you get it in fact its pretty easy uh i hope that uh


Like a lot of you could get this crack this


Did you do that


So you just have to write down the KL divergence definition of KL divergence and use Bayes law and show it Its not at all difficult Okay Now yeah So basically the reason I asked you that question is to make you appreciate this that it is called a variational model because while we want the true posterior distribution of Z given X because we do not have it we approximate that using another distribution which is which we call the variational distribution which represented


by q phi of z given x so the objective is to make sure that the posterior of the true i mean yeah posterior under the true model is going close to the variational posterior and you minimize the k l divergence between them that is the objective okay so now thats why you call this i mean when you estimate q phi of z given x under a trained model you call that as variation of posterior inference


The posterior because


you are getting z given x this is because posterior uh inference because you do it under phi star post training


Is this all right Sanjit So its called variational posterior


uh influence


Okay so this is I mean we were talking about inference with VAE right One is to get the embeddings The other thing that you can do with this is obviously


data generation or sampling because its a generative model


To do data generation or sampling how do you do that is that take the decoder


See this is exactly what happens in a language model also okay Encoder decoder based LLMs exactly the same thing happens The encoder is used for inference okay And the decoder is used for generation Same thing with all encoder decoder models Now you sample Z from normal 0 1


and give it to the trained decoder


will take which will take z and give you an x


will give you x cap so this is the


Generated data point


See a true decoder I mean while training decoder is trying to take samples from Q phi of z given x


You get what Im saying See decoder is trying to see samples from Q phi of Z given X and give you sample from P theta of X given Z right But now you are sampling from normal 0 1 not from Q phi of Z given X Why would decoder help you


You see the question

speaker_2: you are reducing the KL divergence between exactly

speaker_1: Exactly right Exactly So now what happens is now post training


Q phi of Z given X okay would reduce to normal 0 1


Because of the


Here the


Elbow


Therefore therefore


Z coming from


Q will be of Z given X is


Equivalent to


Z coming from normal 01 In fact Ive asked you to do this also in your assignment okay That once you try in the decoder you sample Z from normal 01 and then give it to the decoder you get the generated data Now in an LLM right we will see that later We will do what is called as conditional generation Because all these GPT et cetera what they do is they take an input and then gives you an output right Its not unconditional generation unlike in a VAE


I mean you can also tweak the VAE to do conditional generation all you have to do is as I said we looked at conditional GAN right similarly you can do a conditional VAE just by appending another conditioning variable in terms of text embedding or one hot vectors right so but basically the idea is that once you train you take the trained decoder and then you can do sampling or data generation so now encoder becomes the inference model and decode


for data generation


See the idea is if you take lets say a naive autoencoder okay that has an encoder and a decoder


x and x cap okay now what happens is uh lets say that it will give you z and you simply have a reconstruction task here


Excuse me so you have a reconstruction task here


Now this if you train a a nice autoencoder like this okay now post training you can only use this autoencoder to do inference because you can take the encoder and given an x it will give you a z but you cant do generation using this thing because the distribution of the latent space is unknown


Na nay water encoder


Now what do we do in a variational autoencoder is if you see that we will say that look I dont only want my I not only want my decoder to reconstruct the data but I also want the distribution of the output of the encoder


To follow


some distribution of interest so that once I train this I can sample from a known distribution and then use the decoder as a generative model


Right so now BAE you can see BAE


Uh


Auto encoder


A regularization


On the latent space


Such that


The distribution of the latent space


Should follow a caution


our predefined distribution lets say in this in general case it will be predefined


Larger distribution


Is this all right So in an autoencoder what will happen is theres an encoder and a decoder You would say that okay the data has to get encoded into some latent space And from the latent space well have to get back to the data space right In a variational autoencoder well say that okay we just do not want the data to be reconstructed We also want the latent space to follow a particular distribution of interest okay So that why do we do this is because post


We can sample from this distribution of interest and give it to the decoder and use it as a generative model


Is this alright


So that way right VAE can be seen as a regularized autoencoder an autoencoder with a regularization on the latent space such that the latent space follow a particular distribution of interest


Yes and it

speaker_2: Sir but the normal distribution that is a very like a very wide space right So its not possible that for every sample within this normal distribution we will get like a proper image that is similar to the original data set So like thats where like we try to learn on the poles or the clusters

speaker_1: Oh see


While you can see this as a reconstruction plus a regularization you should always remember how did we get to this objective We got to this objective by minimizing the KL divergence between the model distribution and the true data distribution correct

speaker_2: distributing into distribution

speaker_1: We started how did we get this This was our elbow right Whatever I have written here is our elbow That is why I dont write the loss function of VAE as simply reconstruction plus KL simply because I want you to appreciate where did this come from This actually came from the elbow right Now what was that That was the KL distribution KL divergence between Px and P theta Thats what we started from


Now doing all this we are actually reducing the KL divergence between Px and P theta So now if we have done it right right then no matter what this distribution is you know it can be normal or anything the VAE has to sample from Px because we have technically reduced the KL divergence between Px and P theta


Does that make sense

speaker_2: Okay

speaker_1: because the entire model has reduced the KL divergence between Px and P theta If you have done it right then this objective should lead you to sample data points from Px

speaker_3: Yeah so in the assignment what we observe is the reconstruction loss is I mean decreasing pretty fast but we dont know We see that the KL divergence its hard to reduce I mean it keeps generally increasing So whats

speaker_1: little increasing so whats correct correct that happens see that is because uh something uh which is called a posterior collapse so ill talk about it uh okay so ill come to that so this is yeah this is how what what do you do in a knife vae right there are lots of improvisations that people have done over a knife vae ill not talk about all of them ill only talk about like one of them which is the vector contest vae which is


sort of state of the art VAEs that people use Okay Yeah That is precisely because the observation that you have made in your assignment Okay So there is something called posterior collapse in VAE Ill talk about it


Oh la


Then maybe


sort of related to the question that Sanjit asked Hell tell you what happens is See in the NIVE whats happening is


Recall


that in a VA


Now Q phi of Z given X


is force to


go to normal 0 1


Irrespective of okay


For all X


See now QP of Z given particular X this is what it means no X by conditioning it on X This means X is equal to a particular XI okay Now for all XI we want this to be equal to normal 01 in a VAE because we are minimizing the KL divergence between these two


Understand Now okay so is this clear to all of you that in a VAE this Q phi of Z given encoded distribution is supposed to go to normal zero one for all X


Okay now what is the consequence of it The consequence of this is that


Okay do you people know of this idea called bias variance decomposition bias variance trade off

speaker_2: No sir

speaker_1: Okay see whenever you regularize a model okay so if you take a learning model and you regularize the model what will happen is I mean you might be knowing it in a different name perhaps right See if you over regularize a model what will happen is why do you regularize a model You regularize a model because you want to avoid overfitting right Now if you over regularize it the model will go to the regime of underfitting Now if you do not regularize it


then the model will go to the regime of overfitting right it is this trade off between the underfitting and overfitting is what is called as the bias variance decomposition so that is a topic by itself


Thats exactly what happens here okay so Ill tell you the consequence of this is the following


U phi of z u and x okay


Apologies


Normal zero one


Or Olex Olex


Think about it Suppose your q phi of z given x approaches normal 0 1 for all x What is the consequence of it Then the decoder


Very


have a difficulty


will have difficulty


reconstructing


Why do you think so See you see what is happening Lets say that there are two x okay x1 and x2 okay Now q phi of


Z given X one okay is equal to Q phi of Z given X two


And both of them are lets say normal zero one


Suppose this happens If this happens then if you get a Z1 from


Q phi of z given x 1 okay and z 2 from


Q phi of Z given X two right so decoder


not be able to


Differentiate


between G1 and G2 because both of them are coming from the same distribution


See this


This is what is called as posterior collapse


Which means that for


all x okay q phi of z given x is collapsing


A particular distribution


By design


This is a consequence of elbow right We are not like we cant help This is what is happening So now since x1 and x2 rather since for all x q phi of z given x is going close to one particular distribution


Decoder will have difficulty in trying to reconstruct


rather see if it if it can differentiate between each sample input sample it can reconstruct easily isnt it if it cannot differentiate between the the latents corresponding to two different samples then itll have hard time reconstructing it do you see this point does all of you see this point any questions on this


Yes Norman

speaker_3: Uh so this happens only in naive uh VA or that

speaker_1: It happens only in NIV yeah we have well see how to circumvent this problem how do you solve this problem

speaker_3: But

speaker_1: Actually you should have seen this in your uh in your assignments if youve started implementing it


Yeah so Ill tell you what happens This is not what happens in the kind of architectures that we use right Reconstruction will not suffer The other way happens Theres only half of the story Ill tell you the other half Maybe I can ask you the I can take questions after this This is posterior collapse okay Now


Suppose suppose


So I suppose the weight on the care term is reduced


Now what do I mean by that The last function in in VAE looks like this right you have the deconstruction plus the KL term


Well this one was zero only


Okay now this is how it is I mean in the naive implementation both of these terms are equally weighted right So there is another version of VAE called a beta VAE okay which is simply adding this beta term to the KL where your beta is between 0 and 1


Okay now


So higher beta right corresponds to


More weight to kale


So this is this is


beta VA improvisation on VA called beta VA higher beta corresponds to more weight to KL and vice versa right


So now lets say that lets come to this Suppose I give more weight to KL What will happen This may lead to posterior collapse We already saw that


Okay now if you have suppose I give very low weight to beta what will happen This means that more weight to reconstruction


More emphasis on reconstruction


This means that the reconstruction happens very nicely okay because now the decoder can I mean see this implies okay lower beta implies implies QP of Z given X okay may not be equal to normal 0 1


For all X Okay so this implies that reconstruction is easier


construction is easier


Because because why is this


Z1 and Z2 okay


can be different


x1 and x2 See if you have two different latent codes for different input samples then the decoder it will be easier for the decoder to use that latent information and then reconstruct it back right


You see what Im saying


Now okay reconstruction is better if you reduce the weight on the KL divergence but it should come with a cost what is the cost can somebody think about it

speaker_2: So there will be inference collapse

speaker_1: Now meaning the the the generation will suffer however


Generation quality will suffer


with lesser beta why is this


This is because see remember that what we do what we do post training


We take p theta star okay we sample from normal 0 1


Okay now if


Q phi of z given x okay is not normal 0 1 for all x


during the


Generation


Sampling a Z from normal 0 1


and passing through the decoder


the decoder okay may not


Need to


Data samples


Because why is this because


Recorded


As seen


U phi of z given x during training


It is


not equal to normal


Understood Now for the decoder to work you need QP of Z given X to be normal 0 1 for all


Okay And if you make that then what happens is the reconstruction quality suffers while the generation becomes okay So now there is a trade off between these two In fact if you look at the beta VAE paper they will show you that with different values of beta you will see the trade off between reconstruction and generate quality What I suggest you is to implement this beta VAE in your assignments


It comes with no cost in the sense that you just have to have a weight factor on your KL divergence term and you experiment with different betas and you would see that if you have a large beta then the reconstruction will become difficult Okay Why the generation will be okay And if you reduce the beta reconstructions will be better Will the generation quality suffer In fact you might have seen right I mean people who have read the architecture on VAE


you you might have seen uh people saying that v a is uh results in blurry generation right blurry images so that what is that that is simply saying that if your q phi of z given x is not normal 0 1 for all x what will happen is if you if there is a deviation between what the decoder has seen during training and what it sees during inference then the images that you generate will not match that of v theta and thats why


code blurriness comes into generation quality now to avoid that if you make your reconstruction very strong okay by reducing the beta then the generation quality suppose that there is this trade off between these two


Okay so now we will take questions Uh yeah we wake

speaker_2: So will making beta zero convert this into an autoencoder

speaker_1: Thats a good observation If you make beta zero then itll simply become a non automated code


Lesser and lesser beta will always take it closer and closer to an I O autoencoder


Yes

speaker_2: Can you so can you hide this side panel

speaker_1: Can you hide this eye panel How do I do that This one


It opens something else

speaker_2: The full screen is there when the computer

speaker_3: A dog brain

speaker_1: Ah this is


Is it just not moving

speaker_2: If you write something it will start moving

speaker_1: Do you recognize anything at all


What happened to this


Something happened


I mean I am not able to see this can somebody tell me what happened with this

speaker_4: Sometimes it gets stuck sir

speaker_3: Was killing me

speaker_4: We can just close and open

speaker_1: age old solution uh restarting

speaker_4: that is a tall problem

speaker_1: Oh yeah it actually will


Okay uh lets take questions Vivek do you still have questions or is it done

speaker_2: Uh so yes I have a question Uh suppose we change it

speaker_1: Yeah hold on just one other side thing see I have been calling all of you by your first name I hope you dont mind I Mean for all we know all of us are of pretty much same age or you might be like seniors to me So please dont mind and also feel free to call me Pratosh I dont mind So you dont have to call me sir Thats too British Just just take my name right Yeah I mean I mean it I really mean it you can


can feel free to call me pratik and ill be happy and also right i mean dont uh dont feel uh earth because i i call your first names out okay because if i start calling you sirs so theres so many 85 people right sir and madam so you dont know who is who thats why thats where thats why the names are given anyway so anyway go on please

speaker_2: Yes so one question is suppose we have a generation for a given z and I change z a little bit So will the output look just a little bit modified or

speaker_1: Yeah yeah yeah That is how it should it should happen right I mean that is how it should ideally happen If you have trained it well with good architecture that is how it will happen See that is why in in GANs right I think did I include this in your assignment Did I ask you to sample two Zs and then do interpolation between

speaker_2: Interpolation between yeah

speaker_1: Yeah so did you see it changing smoothly

speaker_2: Yes so yeah that happens

speaker_1: Yeah that happens Yeah it happens if you have if you have latent space or the embeddings that you have learned are good In fact when we come to some of these language models right you would see that in in in this thing right What was that thing Was it


Bird it was not pitch


Which was that right I mean that famous example where they show that a man minus king embedding corresponding

speaker_2: Yeah work to it

speaker_1: word to work word to work word to work right that that should happen so it should semantically make sense if you have learned good embeddings


So it depends See that is why imposing this sort of a constraint or rather a distribution on your latent space makes sense

speaker_2: Okay

speaker_1: Yeah

speaker_2: Asser and one more question but yeah its not I think its not the maybe right time to ask but uh if we have a picture from uh somewhere else and if we want to find its Z


How can we do that

speaker_1: I told you right thats what you do thats what the inference is you take a pre trained encoder or a VAE pass it through the encoder in fact we will see that see you know the stable diffusion right all these the state of their diffusion models imagine or whatever the Googles and all these they dont do diffusion models on the on on the image space they do it on the latent space of a VAE in fact a VQVAE once I talk about VQVAE I will tell you that so basically


the trained encoder pass your data through the encoder get the embedding and then use it this posterior inference thats exactly what what youve seen on on your screen you train your encode vae on lets say image net and keep that right and given some new data pass your data through the encoder get the embedding and use it for whatever reason whatever downstream thing that you would want to do

speaker_2: Yes thank you

speaker_1: Thats it

speaker_3: Sir in this example in this description for posterior collapse so sir it is high since the normal distribution is a very large space and we have a finite set of images like input images so isnt it possible that we get each z that is unique for a given x

speaker_1: Yeah if you recall our encoder is probabilistic


We are not asking the encoder to give the Z we are asking it to give the mean and variance


Thats precisely why we make it probabilistic Its not the z that you get You get the parameters of the distribution And by construction you are asking the output of this encoder or the mean of this encoder to go to zero for all x Even though the distribution the support of the distribution is broad what you are predicting is the mean invariance not the z itself

speaker_3: Okay and sir one more question I was a bit confused with the term variational Bayesian Is it same as the variational inference we talked about

speaker_1: Its based because see auto encoding variational base is what they call the VA people Its based because again this if you had done this exercise that I had given you in exam


You use Bayes theorem to get this elbow is it right Correct Yeah thats why its called variational Bayes


Okay variational because you use a distribution of variational approximation to p theta of z given x which is unknown


Okay yeah yeah is that it

speaker_2: Yeah what is the difference between reconstruction and generation

speaker_1: reconstruction and generation Okay See reconstruction is that you take an X pass it through the encoder and the and take that Z okay that the encoder gives you I mean when I say Z it is this reparameterized Z and pass it through the decoder right And you expect the output of the decoder to be exactly the same as that of the input That is reconstruction


Right Its the first term

speaker_2: Yeah but

speaker_1: No but I think this


See even after training you can take a data point that is there that you use for your training pass it through the encoder get it z and pass it through the decoder and expect the decoder to give you the exact same x isnt it


Post training nobody is stopping you from using the training data and passing through the encoder and giving it to the decoder isnt it


Yeah so that is a reconstruction thing isnt it


So generation is see generation is that you take a Z and pass it through the decoder you get a new point that is not there in your training data Thats sampling of course But you can do reconstruction on training data as well How do you do it Take it take the X okay and pass it through the training sorry the encoder get the Z take that Z pass it through the decoder and you expect the same X to come back


Uh

speaker_3: Yes sir In the parameterized model for decoder we are only considering the mu and we are saying that the sigma is identity Right Can we also take sigma I mean and what implications that

speaker_1: Yeah you can you can and then you have to again to generate you have to do another sampling right at the output of the decoder as well right Typically sigma is not taken but yeah theres nothing that stops you from doing it that way Typically it is not done


Okay Harish

speaker_2: our use case that is whether we are doing reconstruction or the generation so we can change the training objective to have this uh k l i just regularization term or not

speaker_1: Correct Thats a good point Yes That is why no its like a knob beta VAE This beta is a knob depending upon what you want right In your what you are training your VAE for you can tweak it the way you want Thats a good point Yes

speaker_2: So you can have two different models uh for exactly two different times

speaker_1: Yes yes yes yes So in fact in your assignment I encourage you to actually do that you know sweep over beta and see the effect of what happens on your VA


Yeah actually not

speaker_3: to the KL divergence we expect the mu and sigma outputted by the encoder to be close to zero and one but not exactly

speaker_1: Okay for OLEXP for OLEXP correct

speaker_3: but it should be exactly zero one then of the

speaker_1: I mean yeah if the training has happened properly yeah

speaker_3: Right and so is this somewhat of an adversary relation because if the KL divergence becomes zero then the reconstruction loss will explode and different

speaker_1: No no it should not it should no right why should it explode see as I think one of Sanchita was saying that uh I mean youre asking the asking it to make it Gaussian distribution zero mean unit variance for all x but even within zero mean unit variance you have infinite support you can place your z different places But practically what happens is because you have like limited capacity encoder decoder right All these zs would be placed on very close to each other and


and discerning the difference between those two will become difficult to the decoder theres no adversary here


So ideally if you have see if you have infinite capacity encoder and decoder both the objectives can be achieved

speaker_3: Because uh the encoder is technically not giving as you said right its not giving z it is giving the parameter z

speaker_1: Doesnt matter doesnt matter Lets say that it will do perfectly and it will go to zero mean and unit variance for all x And suppose your decoder has infinite capacity right As long as for two xs exactly the same z is not getting generated from the sampling the decoder can do it And also remember that the sample that the decoder sees as input okay is a sample that you get outside of the encoding


And also you do an averaging over it no see you dont take one sample of z and give it to the decoder you take multiple samples of z and give it to the decoder


So that way if you have infinite capacity of encoder and decoder ideally a VAE should do perfectly well But since we have like finite capacity architectures right if you make your encoder to have same distribution for all x decoder will have in fact that is one other experiment that you can see that keep everything constant including the beta but only increase the architectural size of encoder and decoder and you will see better performance


Yeah these are very good questions by the way In fact I received one comment from one of you I mean I dont want to know who it is but because thats the whole point of it being anonymous It said that you know you see you have spent so much time on quote unquote basics right Now we only have these many classes and you know youre not covering the syllabus and this happens with all courses in ISE et cetera and all that


sort of uh the the uh not so positive uh sentiment but see the thing is uh


good course right in in our opinion i mean uh good that the person said that this happens across the board in isc see what we feel uh as as faculty in isc is that we want to prepare you uh to you know to to read some of these literature independently so the idea is not to cover a lot of breadth a lot of papers you know a lot of ideas at a superficial level the idea is to go sufficiently deep and make you independent


so that you pick up any paper in the literature and then you can read it So even if we dont quote unquote cover the syllabus I dont know what syllabus is you know because none of the ISE courses will have any syllabus per se especially these advanced courses The idea is to you know make you think and enable you with a lot of tools and arsenals of tools such that you can start reading and appreciating and understanding things


So so I mean what I was coming with this I I was reminded of that particular comment because all the questions that you are asking are very very relevant And then I I hope when I suspect that that that you are you are able to ask some of these questions and appreciate these things in deep because we spend so much time on basics What are these divergence metrics You know how do you carve bounds on things and how do you build models et cetera I think that is what is valuable isnt it I think we can have this discussion maybe when we


When we have that hybrid class when you people meet me okay and I wanted to have that discussion as well right I mean we have to plan for that


post Diwali so now that Im talking about it maybe we should


some dates the second how about uh


Can we do it on 16th itself


The last class that we do shall we do it hybrid Can you people plan a visit to ISE on 16th of November


Lets do it that way so tentatively lets keep it on 16th


Okay again we will do the exact same thing I will do it at Teams call and I will write it on my iPad and project on screens But whoever wants to come to ISE right you are welcome Ill arrange for a physical class and well do it offline you know hybrid on 16th


So yeah I think 16th is the only date because


26th we can do but 26th is too short of a notice But second is that Diwali week I think a lot of you will be traveling


Ninth I dont know if you people come back on ninth I have a I have some other commitment but I cant travel to IAC I think 16th is the only day Lets keep it on 16th So tentatively 16th will be a hybrid class Okay


Plans for it okay if you want to come I mean theres absolutely no compulsion or anything only if you want to


Come and have a look at the campus and uh like meet me in person youre welcome to come there okay


right so this is about uh posterior collapse and this uh uh you know the the trade off between uh the reconstruction and uh generation now as i said people have addressed this problem in multiple ways and there have been a lot of efforts uh in improvising uh vae models so one of them is of course this beta vae right where you have an explicit uh scale term uh on uh


uh the KL divergence to control between the the reconstruction and KL divergence is one thing the other thing other class of methods okay uh are where


Which channels


I should be the latent prior


Hear some music that some guy on the streets right So yeah not me Why should be the latent power p theta of z okay Be the latent power p theta of b fixed


to be normal zero one see all the while if you


Notice the in elbow the KL divergence was between


u phi of z given x and p theta of z


Now what did we do in in a naive VAE


theta of z is fixed


Thats normal 01 right


which cause problems right which


was the issue of posterior collapse


So lot of people question this assumption that why should we fix p theta of z Now in fact like my first PhD student from IIT Delhi actually worked on this So his entire thesis was on optimal p theta of z So now the question that can be asked is


Rather not question because Ive posted the question already call it as solution


is to learn


deligent press


Learn the latent prior p theta of z


along with the model


along with the encoder decoder So this is one of the key ideas As I said no my first PhD student his entire work was on this So learning the latent prior for encoder decoder models Why should you fix it You learn the latent prior itself So what could be the best distribution that you have to impose on the latent space so that you get the optimality Lot of work has been around this So one notable thing is what is called as VAE


Its a variational


called vamp prior okay


Variation variational maximum a posteriori prior okay this is one thing where the idea is roughly


So make


make p theta of z okay a GMM a Gaussian mixture model and learn it


During training


is what they do They make P theta of Z a Gaussian mixture model which is a flexible more flexible distribution than a univariate Gaussian and learn it during training Learn the parameters of the latent prior also So what will happen is the elbow will have three parameters So it was we had theta phi and theta and phi So there in all these methods you will have another parameter lambda


Okay well


P lambda of Z is the learnable latent prior


So now the optimization will be you you find theta star you find phi star and you also find lambda star


As the minimization you do a minimization over theta do a minimization over phi do a minimization over lambda and you have this elbow Now this elbow will be a parameter of the encoder which is parameterized by phi decoder parameterized by theta and you have the prior which is parameterized by lambda So this is how it looks


Okay so not with studying the details of vampire because thats not the state of the art right What people observed is that if you make P theta of Z a continuous distribution and make it a GMM right Its again you


in in in problems like posterior collapse i mean while it gives you some respite thats not the best thing that you can do you can do better than that which is the vector contest ve which you will see but the basic idea is


Along with learning the encoding decoding you also learn the parameters of the prior distribution on the latent space Is this idea clear


Yeah Raghavendra well see one instantiation of this just a second Well see one instantiation of this which is the which is actually as I said no the state of the art VAE which is the vector quantize VAE Even there the idea is to learn the latent space distribution of the latent space along with input decoder called the vector quantize VAE Yeah go on Raghavendra

speaker_3: Yeah so I mean uh um what this


this lambda distribution right what what did you try to come close to is it uh p theta or p theta of z q and x

speaker_1: Exactly exactly So theoretically what can be shown is the ideal prior right is its actually the ideal prior is


Can be shown to be equal to what is called as the aggregated posterior which is the integral of


This can be shown


The ideal prior that one would need to get the optimal elbow is what is called as this is called the


uh aggregated posterior it can this can be shown this is shown in the vampire paper


So what is this You take all the encoding distribution sorry take the encoding distribution marginalize it with respect to the data distribution okay And that is what the ideal prior has to be That is what is shown


Again theres no you dont have to worry about it here


Okay so we will see one instantiation of this idea which is as I said the state of the art VAE which is called the vector contest VAE Go on Sanjit


Electro contacts be here

speaker_2: somewhere where we are learning the distribution on x like it is it is the in maximum likelihood estimate format right px given z so how will we be able to calculate px then

speaker_1: So we cant see thats only a theoretical result


Whatever I wrote is only theoretical in the sense that the ideal prior on the latent space is the aggregated posterior is a theoretical result That is what you try to approximate using GMM


is discrete


And it is vector quantized


Can we kill the AA


what I mean in fact the VQA paper right the title of the paper is not better contest VAE they call it neural discrete representation learning that is the title of the VQA paper neural discrete representation learning


Again thats what the paper is so basically what they do is the following the motivation comes from the fact that they say that you see


all the naturally occurring data right can be compactly represented using some discrete amount of codes is what they call what they say here is what what they mean by that okay so lets say that you want to represent speech signals using some latent space


Now human speech can be represented using a finite set of phonemes So what do you mean by phonemes Lets say that I say A and you people say A So if you plot that speech signal of A of what I say and what you say all of them look very differently Even the different instantiations of the same sound that I one speaker say will look differently


In spite of that no matter who says that sound we perceive one particular idea called R or A Thats a phoneme So phoneme is an abstract idea that you perceive when you hear speech


Okay now in English language there are only a few finite set of phonemes that would represent the entire language


Okay so that is lets say I mean they have identified some 50 odd phonemes And in Indian languages also you have about 50 60 sort of around 60 phonemes Okay so now to represent language all you need are 60 codes right which correspond to each of the phonemes The same thing can be said in for images also right I mean if you want to represent an image any scene can be represented by saying things like okay there are how many regular


Uh


Regular figures like rectangle or circles are present here and you know like how many slant lines are here etc So basically you can have a finite number of discrete discrete discrete descriptors which are latent codes that can be used to represent any kind of naturally occurring data So that is the motivation


Okay so thats why they use a discrete latent space in a VQVAE They vector quantized and learnable And we know why we should learn the latent space also right So it has learned


during training so if you incorporate all these ideas in a vae right you will get what is called as a vector quantized vae we will see uh what it is is the motivation sort of clear okay lets let me uh write down the


architecture and also the way it is done and then we can discuss


So they make the encoder deterministic not probabilistic So it takes Xi


Okay it will give Zi okay so they call it


z e of x i e corresponds to encoding you get z e i okay then suppose


It exists

speaker_2: Sir your screen is not moving for me at least

speaker_3: Yes its not visible when youre writing it


Flag is the rightest

speaker_1: Thats all


Lets see sometimes networks network gives issues Suppose there there are


M latent vectors


It does


Here dimension each


Call them Z1 Z2 Z3 up to ZM


Alls a die


R a dimension


So now this


These form right a dictionary lets call this this is a latent dictionary


The latent dictionary Okay What is done in VQVA is that you find


Okay


quantized version of the excite to be


Z A


We call this Z


J star okay


where J star is the one that is


the closest


between Z E of XI


And Z J you have


j to be equal to one to m


Does it make sense See what we are doing is the following okay its a two norm


Now xi is a is an image or some data point that goes as an input to the encoder and it will give you some vector ze Now what I will do is


I will look


I will search for uh dot zm okay dot zj which is closest to that this output of this encoder


Okay and replace that ZE with the that with that particular vector in the dictionary


Do you do you see what is happening


And that


goes as an input to the decoder


So the quantized version of the input goes as


the input to the decoder


Is this clear what is happening to all of you questions on this So this is vector quantization So this operation right this operation is what is called as


recorded session


Literally no much

speaker_3: I said this earlier

speaker_2: The written dictionary is fixed right we have to pre decide

speaker_1: no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no


So we will learn this


Yeah I dont know

speaker_3: So going back to the the motivation right so you mentioned that we want to discretize it here but if you see even in the VAs right the the number of Z that we

speaker_2: I mean look at it like some business

speaker_1: Theres no discrete no there is no discrete no it has a distribution the they dont have a fixed amount of z


Mm C is not good

speaker_2: Okay C is not fixed these are these are these are very much fixed in the sense if you are choosing

speaker_1: Theyre fixed time

speaker_2: a k dimensions then we know exactly what they are

speaker_1: No no no and nothing beyond that Its its not about dimensionality it is about m m latent vectors are fixed m is a hyper parameter you fix the number of vectors in your in your latent dictionary

speaker_2: And nothing beyond that


Okay and once we have learnt them we use them as the as the dictionary tool Correct So we we dont really look at the entire spectrum

speaker_1: See in fact the I mean one question that might come to you come to the mind is suppose you take an image and pass it through an encoder right So if suppose there are if I make M to be 100 So there are lets say that there are 100 vectors now


Are 100 vectors good enough to represent a space that is as versatile as ImageNet Might be a question Actually the way they do it is that they make the latent space latent vector a two dimensional grid where each of these columns are k dimensional So you have


1 to k so what they do is they quantize each of these columns so each column is quantized of the latent vector you understood


So thats what they represent So basically what they do is the latent space will be a two dimensional thing Its a K cross


P dimensional latent space


Okay where each of the p vectors in the latent space is quantized using the dictionary


You understood So that way every image now will be represented using p vectors okay from the dictionary That way it becomes versatile

speaker_2: And uh are there any weights to each of these dictionaries No no no no no

speaker_1: No no no no no no no no no So decoder now will see a k cross p dimensional uh uh I mean grid


When I said that it is Q I mean ZQ of Xi it is not one vector right It is the quantized version of this entire grid Thats what the decoder sees as an input Thats what they do in the VQA paper Is this clear So thats how it is not a single vector that is going as an input to the decoder It is P number of vectors right Where all these P vectors come from this predefined dictionary And how do you find which of the vectors


the p dictionary that you should take is you pass the xi to the encoder and encoder gives you a map right a grid of p vectors and each of the columns of this p dimensional grid you quantize using the dictionary and you give that as an input to the decoder

speaker_2: But where is the variation variational coming from I mean a randomness coming here because if you have chosen a fixed set of p k vectors right I mean k size vectors the output would always be the same or

speaker_1: So during the training of course right uh you take those p vectors and then you try to reconstruct it

speaker_2: Correct okay

speaker_1: Now the question is how do you use this for generation right

speaker_2: Okay okay

speaker_1: Uh that is a question that Ill answer later

speaker_2: Okay sure

speaker_1: So right now see we are see the way the template is define the architecture right And train it And then you do the inference Im defining the architecture and we have still not trained it Let us try this and then well do the inference But its a valid question How do you generate from a VQVA is a valid question But did all of you understand whats happening right In terms of architecture and training Any questions on that

speaker_3: Sir here for a given xi we will receive only one vector z e of xi right

speaker_1: That is what Im saying So for images what they do is say this is a


Working offline error occurred


I dont know what error occurred


See input will be a lets say a 400 cross 600 image okay okay output will be a lets say 32 cross


50 dimensional vector okay where 32 is your k and 50 is your p what will be done is all of these v is okay will be in 32 dimensional space what will be done is that each of these 32 dimensional vector 50 vectors will be quantized using the dictionary and the input of this will also be a 32 cross 50 dimensional grid


Do you see that It is not one vector it is a grid


And each vector in that grid is quantized using the dictionary Thats how they do it


This is alright

speaker_3: So in in the nave VAE we used to get the mu and sigma vectors

speaker_1: See I told you you look at this right I said that its a latent space that is discrete and vector quantized and learnable You could also say that the encoder is deterministic It is not a probabilistic encoder

speaker_3: No no sir Im talking about the dimension


in in the naive vae the mu e we we used to get one mu per dimension right like for six and four hundred cross six hundred image we will be getting the mu vector of size four hundred cross six hundred right

speaker_1: No no no no no definitely not See Ive been telling that multiple times right This is a k dimensional thing If if youre uh

speaker_3: Okay okay like

speaker_1: Havent you implemented VAE yet See this is a k dimensional thing

speaker_3: Too sir I got confused here I got confused

speaker_1: This is k dimensional this is also k dimensional assuming that it is a diagonal matrix Told this multiple times


is one mu with a k dimensional thing because see this lies in a k dimensional space right it is z z is in k and therefore mu is also in k dimensions


Okay any other questions on the architecture of V2V


Okay so now we will have to train this right training VQVAE


the objective


is again the elbow rate will have two parameters it will have the encoder decoder parameters and also this lambda parameters note that lambda parameters are z1 to zm themselves


Now the lambda parameters are Z1 to ZM themselves right Now the objective here is


You simply do a reconstruction task


And there is this other thing which is reduce the KL divergence between the output of the sorry reduce the the not the KL divergence the norm between the output of the encoder


and the quantized version of it


This is all the objective and its very very simple


Right This you optimize this with respect to So what is happening here is that


gradients


xi look it as z e of xi


decoder this will be zq of xi this will be xi cap so now you have here z1 through zm right now once to learn the encoder of course the grade there is a forward pass like this


And there is a simple reverse pass right


In the reconstruction term


with respect to feet this is what you do


To learn the of course for the decoder also you do the same thing to learn the latent space what you should do is you should take the gradients of


written dictionary


to take the gradient of


particular term


respect to z itself and then back propagate see z you can take a here we know how to take gradients with respect to parameters right we can also take gradients with respect to vectors themselves and you see z1 to zm okay actually you have to take it with respect to uh all z is here z js where z j belongs to dictionary


the gradient with respect to the dictionary vectors themselves and then back propagate from the output from the output okay till the uh till this space so till the uh see you see this as another layer sort of right in the neural network this is a dictionary


the gradients will flow from the output of the decoder till here this is how it and this is how you update the gradients so now what will happen is your


g j you have to do it like vector by vector wise g j t plus 1 will be g j t randomly initialize that minus some alpha times the gradient of the elbow which is this term


respect to


Is this all right This is how you do it This is how the latent vectors are learned


any questions on this Otherwise it is simply an autoencoder training You have the encoder decoder you train both the encoder decoders through backpropagation The one extra thing is you learn the latent dictionary vectors themselves by doing a backpropagation through the latent dictionaries


Is this all right Any questions on this


Deserve you try now we could be

speaker_2: Yeah so I mean is it can we see it like we are trying to find some basis vector of the data during the training

speaker_1: is known during the training its not basis for data no its uh its uh you can say that its the basis for the representation space of data okay data is being represented in the space


For that you are trying to learn the uh basis

speaker_2: And the number of vector that we choose would be a hyperparameter

speaker_1: M is a hyperparameter


Okay so now this is how you try in it so now once you try in this youll have to do inference


First thing that well do is


a posterior inference


or embedding extraction right this is what we call as embedding


just straight forward right you have the encoder always for the posterior inference you take the encoder its test goes as an input to the trained encoder you will get a z e x test


The embedding


or X test


is simply


vector quantized version of Z thats all you have J equal to one through M you search for


Closest


In the quantized space I have written as a star because we learned it already


This is the embedding is it all right


So as I said typically what happens is right you take a a grid of


across p right and quantize


column


That is what is done Now this embedding right is the state of the art that is used in all the text to image generating models They use they take a VQVAE that is pre trained on ImageNet They take this embedding and use it for the and and try a diffusion model on top of these embeddings Nobody starts I mean like the state of the art right People dont build diffusion models on data or rather in the


image space they do it on the the embeddings that are gotten by a VQVE trained on ImageNet


This is alright


questions on this how do you do posterior inference


hyperparameter thats a hyperparameter that is typically used uh i mean if you look at the vqve paper right the first there is vqvei one and vqvei two i think in vqvei one they take p to be lesser and then they show that p should be in fact you can actually make it a three dimensional thing also no where you make each of it a a a map depends so that that depends upon uh the kind of network hyperparameter choice that you make


And you replace each of those columns by the I mean you vector quantize each of those columns Thats the point Okay Two we have to do generation See um


VQAs are not typically used for generation As I said right they are only they are mostly used for embedding extraction okay or inference But you can also do generation from it generation or sampling from VQA


See one thing that is to be noted is that because since the latent space is vector quantized


Space is a discrete


write it as quantized


Quantized okay


One does not know the distribution of it You see that


doesnt know the distribution of it


See in a VAE we know that the latent space follows normal 0 1 Thats why post training we can take sample from normal 0 1 and give it to the decoder and we will get the output right Here we dont know what the distribution of latent space is So thats why what is done typically is that you the way it is done is


Uh first


Extract


embeddings


of training data


Understood so what is done is given


X1 through Xn from the training data okay


Z1 through Z were using different notation for that no What shall we use Its called the Z cap 1 through Z cap N where


The cap I is D


embedding


xi okay get this uh via uh encoding encoders so once by posterior inference now you get the embeddings then what is done as spitter


GMO


Actually what you can do is fit a generative model or train a generative model on top of these embeddings


is the first step this is the second step you try na


Kinetic model


On


G1 cap through GNCAP Now this generative model can be a GMM or in the in the VQA paper they try in what is called as a pixel CNN


which is an autoregressive model autoregressive generator model We will see the autoregressive model later next in the course So basically you try in a generative model on top of the latent embeddings that you got from the encoder


No sample


Z nu Z cap mu from


Yeah


Generating model on Z1 cap to Zn cap okay


Then pass


C cap new through the decoder


Do you understand this


The problem is unlike in a VAE you dont know what the distribution of the latent space is correct Because it is discrete Therefore what they do what is done is that once you learn the encoder decoder you take all the training data and pass it through the encoder and get the corresponding embeddings Now that becomes a new data set okay On the embedding data set you learn a generative model Now you know how to sample from the latent space


the VQVA right and therefore what you can do is once you learn a generative model on the legend space then you sample from it and give it to the decoder and decoder should give you a new data point


This is all right In fact people say that I mean this is also our experience that training a generative model on the latent space of a VQVA is very difficult And thats why VQVA is typically not used as a generative model itself What is done is PQVA is used for posterior inference You get the embeddings and use a train a diffusion model on top of those embeddings


Uh yeah in fact this is exactly in fact this is what is done in a stable diffusion and all that what they do is


Actually this is what is it done no you train uh


It can be a GMM or it can be a pixel CNN


Or it can be a diffusion model Thats exactly what is done in stable diffusion


So basically you take a VQVAE get its embeddings learn a generative model on the latent space okay and generate a new sample in the latent space of the VQVAE and give that new generated latent sample through the decoder and get the X new That is exactly what is done in in stable diffusion


And all this imagine that you have Googles this thing right All the I think its J E N


Its that Googles engine right All of these commercially available things thats exactly what they do They take a VQVAE


Find a generative model on the latent space of the VQVAE and generate a new sample from the latent latent distribution of VQVAE and give it to the decoder to generate the image and what you see is the image but the generation is happening in the the latent space okay Sanjit

speaker_3: So if you are training a GMM on these embedding Z1 to Z Z1 hat to Z1 Z and hat so what shall be the mean and variances for a like a like individual Gaussian model

speaker_1: That is what is learned in a GMM In a GMM you dont fix the mean and variance of the individual Gaussians Thats what you learn You learn the mean and variance of individual components in a GMM using EM


Okay so yeah forget about GMM right now right You can I mean as I said no in stable diffusion et cetera the model that is the generative model that is used on the latent space is actually a diffusion model which we will see right now


Okay so if you understood good so this is the


of VAEs in one form because the diffusion models are also VAEs but yeah so in the naive form this is the end of VAEs see I have not asked you to implement a VQVA in your assignment because I thought it would be too much but yeah if any one of you have some bandwidth and time Id be happy to see you implementing VQVA that would be great if you can do that

speaker_4: Yeah

speaker_2: you know which we can we can we can with discrete letter to space

speaker_1: And so cruel of me


Okay I think then you should do it yeah you can you should do it


Okay so great


I thought I didnt expect this to take so much time but its worth it its fine


Okay so shall we take a break Been talking for one and a half hours one hour 45 minutes now


Uh as I said I need to leave like five minutes to eleven uh so lets not take a long break lets take a short break ten minutes ten twenty well be back


Is that okay


Do you do you need fifteen minutes Ten minutes is enough I suppose


Yeah let me try

speaker_2: What are you doing

speaker_1: Yeah so please come back at 1020 because well start diffusion models Dont miss the introduction Thats very important Yeah lets reconvene in about 10 minutes See you

speaker_3: You are on mute

speaker_4: So you are

speaker_2: So youre on mute

speaker_1: Oh my god I got scared


okay im sorry yeah so its just speaking one mute


So the next topic that we will see in this course is about DDPMs also called as expanded as denoising diffusion probabilistic models


Im audible now right

speaker_3: Yes sir you are audible

speaker_1: Okay so now the state of the art generative models in all the vision language models that you see today right are based on DDPMs They are


Neither VAEs nor GANs right I mean people have moved on onto these these new class of models


on called DDPMs denoising diffusion diffusion probabilistic models uh well study that um so basically right its um


So DDPMs


The plan is that I will set up the problem today in this class


Uh and then we will uh look at the rigorous math and all that in the next uh coming classes


Um there is one tutorial by


you what that is its a very nice tutorial Ill put it on the chat now


very very good okay i encourage all of you to follow that and go through it it will cover everything uh that ill be doing in this class okay i found it very its a its a 100 page tutorial its almost like a short book but it is extremely good let me just put it here


You want me to put it on teams also that also I can do hold on


Names


I think its already there


So whatever I put in here in the meeting chat it will appear on the Teams chat

speaker_2: Its its

speaker_1: Yeah

speaker_3: S

speaker_1: tutorial on diffusion models


Please have a look at it this is pretty much what I cover okay


Sure sir so its a good tutorial have a look at it okay


So um


Basically the idea is the following that DDPM is is actually is a special case of VAE


Now you can actually see DDPM as a special case of VAE with the following properties


So if you look at this tutorial right he has actually derived the elbow also done reparameterization everything maybe Ill just show you that once hold on


Did you see my screen


You see its very very recent now it has come out on 10th of September its pretty good so they start with VAEs okay so there is this encoder decoder or definition of latent variable


And yeah he also talks of GMM See this thing very much aligns with my narrative as well I mean you should trust me when I say that I did not build my narrative looking at this because Ive been teaching this course since three years This man has used a very similar narrative as what I do Okay So then he goes to the evidence lower bound constructing the evidence lower bound and decomposition of the log likelihood as elbow


using the variational distribution interpretation of elbow


Right reconstruction and prior matching terms


Okay so optimization in BAE


The parameterization


These are exactly the things that I did I dont know right Maybe somebody who looked at my notes but that was not public at all I dont know how But anyway exactly the thing that I did okay So VAE encoders


and parameterization tricks in high dimensions scale divergence between two Gaussians


this vae training and then they completed this concluding remark then they come to uh ddpms this is a very good tutorial okay so please have a look at it itll actually give you uh a lot of insights about vae and also the ddpms that ill be covering okay so and also as i said right uh thankfully it is very very similar to the kind of story that i have told you the narrative that i have built so that very nicely


aligns with what we have done so please have a look at it


a minute there is cleaning let me bring my charges now a minute


Okay so DDPM is actually a special case of VAE with the following properties Okay so we will see all those properties one by one


you can hear me and see my screen correct

speaker_2: Its a

speaker_1: Okay see one thing is that


Yeah


The first thing is that there are


Latent spaces


Okay uh unlike


One latent space in a VAE


There are uh yeah so this is a hierarchical


So there are multiple latent spaces here unlike in a VAE where there is one latent space So basically what happens in a VAE is that start from the data space project to the latent space and from the latent space you get back to the data space This is a VAE


In a DDPM diffusion model what happens is start from X get to the first latent space Z1 and from the first latent space you get to Z2 get to Z3


some z n lets call it right and from zn


back to Zn minus one retrace it back


Do you understand this Instead of having one latent space you have multiple latent spaces in a hierarchical fashion


Its all right


So now why do we do that is that because see uh


Think of it like this Start from data Lets say that you have a very high dimensional data Projecting the motivation is that projecting it onto a latent space in one step and trying to compress it making it compact in one step might be very difficult for the encoder right So typically projection from the data space to the latent space is the encoding process and from the latent space back to the data space is the decoding process right Similarly you have hierarchical encoding


And you have a hierarchical decoding in a DDPM Is this idea clear So as I said no we will write rigorous math and we will concretize everything that we do eventually But yeah so high level is this clear

speaker_3: Sir can you c comment on the dimension of G1 G2 G3 and G4

speaker_1: Well do that well do that well do that one thing at a time This hierarchical thing the second thing that you do is that the


Dimensionality


of the latent space


of all the latent spaces


is same as that of the data space


Again typically what happens in a VAE is that dimensionality of the latent space is much less compared to that of the data space right But in a DDPM the dimensionality of the latent space is exactly same as that of the data space


That is the second property The third property that is used is


Encoding


Encoding process


Not learnable


Part fixed


Markov process


See in a VAE what do we do so VAE


we do is q of q phi of z given x okay


is learned right


Elbow


Here


Q of g given x


non runnable its fixed so you see that fee is theres no fee here


Do you understand


Not learnable


The encoding process is defined using a Markov process there is nothing to learn here


is all right so that implies that only decoding


Only the decoding decoder is learnt


Theres no one decoder decoding process is learned


So now if you incorporate all three of these properties right which is that there are you take hierarchical latent spaces and you match the dimensionality of the latent space to that of the data space and you make the encoding process a fixed one but not learnable then the resulting VAE is called DDPM Thats all it is


The rest is only algebra and mathematical details So what we will do is we will incorporate these properties into a VAE and we will write down the elbow for this sort of a VAE And when we optimize that and we do the algebra we will end up having the loss functions for a DDP


Okay so thats why I taught Gyans first and then came to VAEs And then we are going to DDPM because DDPM is a special case of VAE with these properties Any questions on this

speaker_2: Um s sir uh what does Markov process mean just a random process or

speaker_1: Yeah Ill tell you See for now think of it like a like I mean Ill write all the equations and itll be clear right So basically what do I mean by Markov process is that start from the data space right You go to the first latent space from first latent space you go to the second latent space from the second latent space you go to the third latent space and so on right By Markov process I mean that if you take the tth latent space okay it only depends


on T minus first related space and it does not depend on anything else

speaker_2: Okay understood time based

speaker_1: Theres no time per se here because

speaker_2: Iteration

speaker_1: Uh its not even iteration right you can call it as the latent space index

speaker_2: Understood yes

speaker_1: And you can call it time if you want I mean if you want to see that as start from the data you go the first time instant you go to the first latent space second time instant you go to the second latent space and so on


Any questions on this on on on the high level formulation


Yeah isnt it

speaker_3: Sir so here are we saying that we are not taking the data batches but one data point at a time

speaker_1: No no See it still do everything on a batch level See every every analysis that we do is for one data point right Because doing it on a batch is only one another summation at the outside All the VA analysis we did it for one data point So now this is for one data point Everything that Im doing is for one data point Okay

speaker_3: Okay

speaker_1: You look so wee

speaker_3: Like we are saying at time like at one time we reached the first latent variable and at the next time we reached the another latent variable So


Had that part like I was not clear

speaker_1: one theres no i i said theres no one time see in a va i wrote it here right what do you do in a vae start from the data point get to the latent space using encoding and get back to the data space now in a ddpm you start from one data point go to the first latent space from first latent space you go to second latent space from second latent space go to third latent space and so on thats all


We are doing it for one data point I mean of course everything that we do well do it over batches But yeah so but analysis we do for one data point right All the elbow et cetera we do it for one data point assuming that we only have one data point and you just put a summation outside data

speaker_3: Answer this encoding is it probabilistic still

speaker_1: It is probabilistic but fixed

speaker_3: Probabilistic but fixed

speaker_1: Not learnable by by fixed I mean learnable well write the equations it will become more clear yeah


Okay so let us uh go to the math now um


Any other questions on this


Lets


Unfortunately the community has used a different set of notations than VAE So I will use the same notation as there as as it is there in the papers and the other tutorials So its a weird notation Please bear with me on that So data


He is represented


Using X not okay


So what used to be Ill just write the things that we were doing earlier also earlier using some other color this was our X okay


And


latent space


is represented using


X one X two


2 XN


X capital T please note that this has this is not the data points that we had as I said it is unfortunate because this is a very very non standard notation okay so lets call this T


Latent space is typically represented using Z okay But the DDPM community they represent that using X1 2


X capital T and data is represented as X naught So this is what we used to call


Z1 Z2


ZT okay Ill write this not to be confused


Thats the usual notations


Well


One through XN were data points


Okay is that okay Because see now from now to the end of DDPMs well be using this new notation So now let me clarify x0 is the data point And also note that all that we are doing is for one data point So well do it for a single data point x1 x2


LXTR


latent vectors


latent vectors corresponding to x naught


this okay so now the the encoding process is that you start from x naught go to x1 and then from there to x2


This is the encoding process


Is this


Vectors of same dimensions


Is this alright notation wise


Yeah yeah Please get used to this notation because as I said no very very non standard notation but thats what the community uses and I am not changing it So just to ensure that that


Notationally it is correct uh consistent across


no no this guy uses uh exactly the same terminology as i do ill show you this thats a serendipity


Is my screen visible

speaker_3: Yes certainly

speaker_1: Look at this note


X naught it is the original image which is the same as X in VAE XT is the latent variable which is same in Z in VAE


Okay x1 and x t minus 1 they are intermediate states or intermediate they are also latent variables but they are not


White Goshen yeah that is okay yeah so I strongly recommend all of you to go through this okay so I mean of course


in parallel to what we have been doing But yeah so its very consistent with what my narrative is and also the notations Is the notation clear now Please note that the dimensionality of all of these latent vectors are exactly same as that of the data space Ill write that maybe


prime of x naught


Same of dime off


E or T in


So note that x naught is your uh data vector


Is this clear


Is the notation clear


Okay now we will define the


encoding process


Dippy


also i tell you why is it called a denoising diffusion probabilistic model we will not leave anything out okay so but yeah well ill give you the easiest narrative first and then ill connect every dots dont worry okay let us define the encoding process in dtpm so now what is encoding that projection from x to z is the encoding process right this is the encoding process how is it done in uh in a in a dtpm is that it is done in a markovian way what does that mean


Mean that you make your x1 which is the first latent variable to be equal to


alpha naught times x naught


1 minus alpha naught times


Epsilon


where epsilon is coming from normal 0 1 this is the definition of encoding in a DPU okay so now similarly x2


alpha one times x one


one minus alpha one times


So lets call this as epsilon 1 or epsilon naught and this is as epsilon 1 So actually they are all samples from the same normal distribution You are doing different samplings thats all So and so on In general you have x the tth latent vector is given by alpha t times x t minus 1 plus 1 minus alpha t times some epsilon t


If I learn D is going from not once itll look


This is the encoding process This is the fixed encoding process You see that there is nothing learnable here This is probabilistic but there is nothing learnable


Is this clear

speaker_2: t minus one right alpha t minus one

speaker_1: Yeah yeah yeah I can do that Ill write that

speaker_2: Is this a type of microphone process

speaker_1: It is a macro process Just a second I just want to be consistent with the notation Just a second Im just looking at that P14T


This is alpha T okay


People generally like write this as alpha t


This is alpha one


This is alpha two Again it doesnt matter but just want to be consistent So where


Alpha one through alpha


T E right are fixed scalars


between zero and one okay

speaker_2: epsilon index as well so

speaker_1: epsilon index epsilon index is okay i mean yeah so see epsilon i can write it as epsilon every time its just samples from a normal distribution right there is nothing uh like sacrosanct about this one two etc but okay fine can call it epsilon t


is this is this clear is this all right do you understand whats happening see what is happening is that you take the data point okay uh see this can be seen as some noise right when you take some noise scale it add it to the data point so that will give you the first latent vector okay then you take that first latent vector okay uh take some noise scale it add it and then you get the second latent vector and so on so this


This is whatever I have written here right this


is actually a first order


Markov


process


Its Gaussian transitions because the noise that we are adding is Gaussian


And


What is the spelling of transition trend


E I T A O N is it


Oh I say win

speaker_3: Its a dog

speaker_1: SITI SITI one SITI one

speaker_2: I say its a

speaker_1: gaussian transitions okay so basically what is happening is right you can see this as like this suppose we start with an image


Okay so this is X naught what are we doing we are just taking some


Gaussian noise with the same dimensions okay adding it to this of course you scale it with alpha and add it with that so you get


So called noisy version this will give you the first latent space right And then you add


Another noise and this is alpha two and you get


made with


noise and so on right we keep doing it and as a result that would say that if you keep doing this at xt with sufficiently large t this xt right xt will follow a normal distribution 0 1 so this is called the stationary distribution of a Markov chain


So if you create a Markov chain like this it will go to a


Normal 0 1 is what is known Okay so hold on let me just show you a picture


This is how you create the encoding process This is the encoding process of a Markov chain Let me offer of a DDP Okay let me just show you this


I mean of course your assignment will be one of your third assignment will be on this so you will implement all this and appreciate it


You see my screen


This is what Im talking about and starting from makes not you create a sequence of latent variables by adding noise


Okay so the fiction is

speaker_4: Thats prediction

speaker_1: Come again


You see this here


this is the process right you start from X naught just keep adding that noise and you get a


encoding process is this all right


Okay so I think this is a good time to stop So please again look at this and read my look at my notes So we will continue from here from the next class So well have to leave now


Okay so the summary is that a DDPM is a VAE a hierarchical VAE with multiple latent spaces with the property that the dimensionality of the latent space is exactly equal to that of the data space and the encoding is a fixed process Its theres nothing learnable What you do is you take the


uh and create a markov chain by adding gaussian noises and that will give you the latent embeddings so what do you do with it and how does this become a uh this thing a generative model and all that well see in the next class so basically what we do is we will create a decoding model and we will write the elbow that we were writing for vies and then derive a loss function for it that is what well do in the next class please have a read at that uh uh that that tutorial that ive shared


So my handwritten notes is also there Theyre also have done it and yeah and look at my notes and come prepared for the LBO and look at VAEs Okay The next class we will do the math for the diffusion models Is that all right


Again you know thank you for being accommodating Okay so Im sorry about moving everything one hour before So you have a quiz now please wait Let me just call Chandan


Can he not pick up


Now Chandan I am done with the class


Yeah so can you please join that link students are here and then conduct the quiz


So so I ask the students to wait just join there and you can conduct the quiz


No no I just completed because I have to leave now Yeah So the thing is see one other thing right If after the quiz if students have some time they can spare you can maybe just take a tutorial or rather just do some I mean do that exam thing


see okay no problem you can conduct the curriculum then leave okay okay okay okay so students are waiting so you can please come online and go okay thank you


Okay so I just spoke with him Chendan will be here in about two three minutes and please take that quiz and then you can leave we will meet next week

speaker_3: Sir the next quiz is supposed to be a week after the next one

speaker_1: No no no no no uh see we have to do six quizzes right we will ill ill talk ill talk to chandran so we have this is the this will be the third quiz right


be third quiz we have three more uh so we will uh i and chandan will discuss about it and let you know because we have what four more weeks and we need to do three quizzes right so what we can do is we can skip on that diwali week and rest of the weeks we can have quiz every week

speaker_3: Im not getting

speaker_1: Well do it that way

speaker_2: Yes

speaker_1: Well do it that way I will I will I will discuss about it and uh keep you notified on the whatsapp group and teams okay


Okay I really have to leave now so please stay do this uh Ill leave next week

speaker_2: Ill take it

speaker_1: Okay thank you

speaker_3: All the best sir for your interview

speaker_1: Oh my god you know exactly


Okay see you guys

speaker_3: Okay so anyway
