---
id: 6eKnv52CTPM
title: Lec 14 - Deep Generative Models Knowledge distillation Transformers
url: https://www.youtube.com/watch?v=6eKnv52CTPM
date: '2024-11-23'
duration: 02:23:22
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 14 - Deep Generative Models Knowledge distillation Transformers

## Transcript


### Speaker 1

Not yet

### Speaker 2

So yeah so we will see that and well let us Ill tell you how people evolve to transformers and talk about transformers as well and then we can close Okay We have distillation also we plan on distillation

### Speaker 1

No legislation is pending

### Speaker 2

the dissipation is printing okay so lets uh okay lets start with dissipation and then move to sequence models okay


Its very handy


Okay so this was an idea that was proposed by Hinton and his group in the early late 2000s I think its a


The objective here


Its not the primary objective but still the context in which distillation is used today the objective is to reduce


Reduce the size of

### Speaker 1

Something

### Speaker 2

Are you laughing something


Want to see my screen

### Speaker 1

Not yet sir

### Speaker 2

I dont know


It is saying that it is showing the screen okay let me do it again

### Speaker 1

At least I am not able to see

### Speaker 3

No no it is not shared

### Speaker 2

Still not seen


Uh well come rejoin from here


Let me know when you see the screen we can see now so


Okay so the objective here is to reduce the size of very large neural networks without compromising the performance


This is the objective The idea is pretty simple when it was proposed


It was proposed without further understanding of what was actually happening I tell you what it is So in knowledge situation what happens is you have a very large neural network that has to be compressed


largest neural network to be compressed


This usually called the teacher network


Then the you have another neural network


D desirable size


It is called the student network

### Speaker 1

Sir I have a question

### Speaker 2

Uh lets let me complete this and then yeah tell me what is it

### Speaker 1

Sir this is related to like a bit related to the assignment So like in the animal data set we have around 5500 images We divided among 90 classes right And even when we were going for the classification tasks we saw that the training accuracy was very high but the testing accuracy is always very low So what my perception was since the data


the data size is very small like we have good number of classes but not sufficient images per classes that is the reason that the model is able to learn the features from like you know remember the features and not able to classify properly on a newer set of images is that the correct interpretation

### Speaker 2

Yeah why what is the relevance of that question to what we are doing now I think it would have been asked at the end of the class right anyway so now that you have asked

### Speaker 1

Anyway so now that you have asked


So the

### Speaker 2

So the reason why youre asking We were looking at distillation I think after this after I finished this part you could have asked anyway Yeah that can be one of the reasons So what happens is when your data has multiple short modes so you can think of each of the classes as one data mode And typically when the data set has too many modes okay with very less samples amongst each of the mode then getting a


A discriminator or classifier that would put decision boundaries across those classes would be difficult


Yeah so in that way your interpretation is correct

### Speaker 1

Okay

### Speaker 2

we continue with what we were doing so if you have any questions on assignments etc please note that down and ask at the like at the end of the class okay so that it does not break the flow of what is being done of course you can ask questions regarding what is being taught okay


Anyway wave was I yeah so this relation two neural networks one large neural network that needs to be compressed that is called that is typically called the teacher network And there is another neural network with the desirable size which is called the student network okay


No um


To teacher network


is trained


supervised objective whatever suppose you are solving the classification problem it is solved with


object with the cross entropy loss and whatever the supervision might be


supervisor objective independently of the student


What happens is is a network here


Whatever the task might be okay let us call this the teacher ritual


So some data some task and it is trained with minimizing lets call the parameters theta just


usual


minimizing the expected loss function okay which is uh


between uh


lets call this uh f theta maybe f theta of x comma y


Yeah so this is the usual empirical risk minimization okay or supervised training Now there is a smaller neural network which is called the student network


CM bas of externally


speed okay now this has two objectives for training


One is a


KL objective between


Lets call this CT and this as CS


objective between the distribution of ZT and the distribution of CS plus


A super wise loss


phi plus


Supervise last between


Something like


Okay so what is happening here is that


student network is being trained okay now the uh scale divergence between


The distributions of some


features in some uh some layers typically the pre softmax layer of the student and the teacher network is minimized okay and there is a supervised loss that is uh minimizing the uh loss between the


Real true predictions and predictions of the neural network Okay so now what is this doing is this


going to match


the features


learn or match actually learn or match the features of teacher


To the tough students students that is what it is doing


Right by ensuring that the KL divergence between the distributions of representations between the


about it so by making by ensuring that the the clear divergence between the features of the teacher and the students are are matching your i mean the idea is to ensure that the um


features that the teacher has learned is imbibed by the student you know if it does that then whatever the performance that the teacher is supposed to give with a larger network can be achieved or can be expected to be achieved using the student network okay so procedure wise this is what is done so in practice


the KL divergence term no between the teacher features and student features


is approximated


Oh yeah


So mean squared error loss so squared error loss average it is actually mean squared error loss


between


Uh GD and GS


Yeah this is also not a bad approximation right When we assume these two distributions PT and PG actually what this actually means that


have pt coming from a Gaussian okay and ps is also coming from a Gaussian if you make this assumption then we know that the scale divergence is equivalent to minimizing the mean squared error between the features taken when averaged over all possible


samples okay


Okay so


This is what this is how the finally what is done is instead of using the teacher network teacher network is discarded meaning it is I mean it is it is the goal is to not use the teacher network but to use the student network for further process So that is the idea


Okay so I will tell you so there is this was what was being done in distillation Now a very recent paper came that gave a very nice statistical perspective of why should this work okay What is actually happening under the hood Ill talk about that Before that if there are any questions on the procedure of what distillation is do ask And by the way in your assignment what Ive asked is Ive asked you to use a large


teacher network and


distill it out to a smaller student and compare it with just training a student network separately i mean meaning a network that is of the size of the student network separately and then compare the performance


okay questions now uh yeah we wake

### Speaker 4

So two small questions So should the sizes of the features of the Z and the I mean the both the ZT and ZS should they both be the same

### Speaker 2

By sizes you mean the dimensionality

### Speaker 4

Dimensions yes

### Speaker 2

Yeah they they have to be same otherwise how would you define KL divergence

### Speaker 4

Okay so the second question is how important is the KL divergence term in this so if we skip that and if we simply use a completely different network so is that still called distillation

### Speaker 2

What do you mean by that See if you do not use any features from the teacher while training the student network then there is no distillation right It is simply an independent training

### Speaker 4

Right okay

### Speaker 2

Isnt it

### Speaker 4

Yeah win you

### Speaker 2

I mean see it is called estimation only because you have a teacher network and you are using those features too


But youre actually imposing those features on the features of the student thats all right

### Speaker 4

Right yes so

### Speaker 2

Its like whatever teacher network has learned the transformation that the teacher teacher network has learned are trying to ensure that the features of the student network matches those features at a distributional level

### Speaker 4

Yeah but if the student network is struggling too hard to simply match with the teacher network more than increasing the accuracy of the classification task then should we reduce the weightage on the KL division task

### Speaker 2

Of course of course of course I mean thats thats always there right I mean when you have for two loss terms you can you always rate them accordingly

### Speaker 4

Yeah so thats all thank you

### Speaker 2

Okay uh yeah salvage

### Speaker 3

So if Z are just the pre softmax terms so why to include this expected loss in student network Because anyways they will be same right If they are same then

### Speaker 2

Good question See what happens this is a practical thing What happens is when you do not have the supervised loss because I mean teacher network may itself have not learned to solve the task properly right The performance of the student network will not be great if you dont include that

### Speaker 3

So just to be sure that it is learning the main correct

### Speaker 2

Correct whatever is needed no The main uh


Learning should happen that is why the supervised loss is also included

### Speaker 3

Thank

### Speaker 2

Unkitted

### Speaker 1

Sir if the teacher network is like as we are asking it is very large and lets say the data size is not sufficient enough for the learning to happen correctly and at the same time then we are trying to use that loss for training the student network


uh how can we expect the student network to be learned properly

### Speaker 2

Yeah youre saying if the teacher network is bad how do how what does what happens to distillation

### Speaker 1

No no like my like I asked a previous question right If the uh the data set is not sufficiently large So we cannot expect the teacher network itself to learn the uh the classification properly And then we are trying to train the student network

### Speaker 2

That is what no what happens if the teacher network itself is not good


That is what you are asking Yeah Yes Yeah So yeah So what happens is if there is like some level of uncertainty in the teacher network is OK right As we will see in the theory but if teacher network is not even doing like


supervised learning right then obviously the student network will perform badly


So we have to ensure that the teacher network has to have some level of good accuracy for this to work


Anything else


Shall we continue

### Speaker 4

Yeah just one small query what is the benefit is it going to use less resources

### Speaker 2

Training definitely not


But the inference of course right because the student network is by design smaller in terms of sizes it is going to use less number of less resources during inference Because finally what you end up storing is the student network not the teacher network

### Speaker 1

Sir one more question the training has to happen simultaneously


First we have to train the teacher network and then the student network

### Speaker 2

So thats a design choice typically what is done is uh uh


Feature network is trained up to some level okay where you have decent accuracy and then uh both of them were trained simultaneously


But you can completely train the teacher network once and then reuse it and then do a distillation that is also possible


I tried design choice


Okay so yeah so this is what is done procedurally Now as I said no there is a very nice interpretation so as to why this works Lets try to look at that


Statistical perspective on knowledge distillation


Okay so what happens is um


In typical


Supervised learning


Mm


labels


are deterministic


in the sense that


Every data point so okay let us design the problem that way


Opposed


the class labels right they belong to uh


one out of K categories


in a in a k class classification problem then typically


for each x


for each x okay y


Why is only


One of the


You can use one label


This is what happens


However


It is always uncertainty in labeling


eternity enabling


So between place


for each x


there exists


There exists a distribution over y


p of y given x


What Im trying to say is lets say that there is uh you have you have an image that you want to label


Now okay so Ill take an example that is sort of ambiguous


Okay Ill try to check it


I like this


Okay which digit do you think it is I mean lets say that Im


annotating MNIST


Yeah thats right


So people write it this way now so this means that this has uh


likelihood of being in three and some likelihood of being in five


So now there exists so what is this Along y axis what I have written is this is p of y given x


Okay now what is done in typical supervised learning is okay in


Supervised learning


of y given x


Approximated


With a delta function


Isnt it so the uncertainty that is associated with the labeling is completely ignored when I mean in typical supervised learning right now what this this this nice paper does is the following


They consider okay so any questions so far What Im trying to say is there are there is an uncertainty that exists with the labeling inherently because every data point can


can probabilistically belong into one of k possible classes But labeling is always done in such a way that the uncertainty that that is there in the labeling is ignored and labels are marked labels are given in a deterministic way Is this clear

### Speaker 4

Yes sir

### Speaker 2

Okay now what is the consequence of it is the following define


Two types of risks or losses


One is the typical supervised loss


Supervise loss


Deterministic labeling


Call it R


And there is uh okay lets call it R cap and there is something called base distill loss okay


dystrophic loss call it RV cap


Now this is what can actually be shown is that this is we know what R cap is right this is simply the expectation of the loss F is the classifier that we are looking at this is F theta of X comma Y this is what it is this is with respect to PXY and this can be shown as KL divergence


between the


Distribution of uh


F theta


effects


of y given x lets say is a classifier imposes a distribution on labels right that is what it does and the


true label distribution that is what you can show okay uh i mean if you use a cross entropy kind of loss then the scale divergence is equivalent to that cross entropy i mean that is easy to show okay


The interesting result that which is shown us Now suppose


R star represents the generalization risk


Its also called the true risk


It is nothing but the error average error on unseen data


on unseen data


What can be shown is that r star


will be lower


RB cap okay compared to


So this is a this is actually the main result


which is there in that paper which uses Jensens inequality okay to bound the variance of these two risks


Yeah but this is the crux of the result that would say that the generalization error that we get


generalization error that is achieved using base distill risk is lesser compared to that of the risk that is obtained using the direct delta approximation


Okay which means so what does this imply a summary is


It is better


It was


base distill risk or the distribution the actual distribution over the labels given data okay instead of


instead of


Delta approximated labels


So this is the idea Okay So now uh this paper says that now see if you incorporate the I mean that is why this thing P of Y given X is also called dark knowledge That is the term that is used in the distillation literature Okay If you incorporate the dark knowledge that is there uh in the labeling or uncertainty that is there in the labeling you achieve a better generalization performance is the idea Now uh this is not directly related to connected


To distillation yet Okay Now this now the question is


Given a labeling a deterministic labeling scheme


a scheme there is no access


access to p of y given x isnt it I mean we are only given deterministic labels How do we know what is the distribution of the labels conditioned on data We dont know that Therefore the idea is


Yeah


The idea is to


Approximate


We have ionics okay as


using using a neural network


So this neural network is the teacher neural network


Right So now what happens is in fact this theory right it does not talk about the size reduction at all So it suggests what is called as self distillation Ill talk about it So there is this network F theta where you get X and Y It is trained in a supervised way with deterministic label Okay


What do you think


deterministic labels However the free softmax activations that you get the logits that you get these


can be interpreted


as


An approximation


P of y given x So this is an approximation to P of y given x So then what you do is you take the you take another network


We dont talk about sizes here right I mean it can be the same size or different size If its of the same size then it is typically called the self desolation okay


take that and use RB star here to try this So RB is the base distance discussed simply the scale divergence between the true or rather the


models


estimate of y given x okay and the true y given x so now we dont have access to true y given x so you we use the features f thetas logits as an approximation to this now when somebody asks the question right we can why why do we have a supervised loss so if we


If we have a perfect uh uh


estimation of P of Y given X then we do not need supervised loss Now since we are approximating the true uncertainty using another neural network that is trained using deterministic labels so it can only do so much right So that is why you also have a supervised loss here okay To ensure that the network the distilled network also does well on the supervised training


As I said no in this treatment there is no reference to making this SP a smaller network Now that becomes a byproduct right Or a happy consequence of this that okay theres no restriction on how big or large this SP network should be Because as long as you are matching the true labor uncertainty you should get better risk irrespective of the network size And that is why people tried okay lets try to


to make this SP a smaller network and then


uh try to ensure so this is there is a scale here and try to use this technique for network compression in fact as uh as it stands you can do what is called as self distillation which is that you try the neural network using supervised fashion and then take that same neural network and use the logits of the previous one and retrain it by minimizing the kL between the logits and the supervised loss


If you have gotten P of Y given X to a fair extent from the teacher network then doing self distillation should improve the generalization according to this theory


Okay thats about it uh questions yeah Vivek

### Speaker 4

So the so we uh you told about the base uh distill distill laws uh but instead of using that so if we just use the entropy of the uh pre decision layer output I mean if we uh try to


Minimize the entropy will that lead to any benefit

### Speaker 2

Its that same as this isnt it

### Speaker 4

Thats what it should be less indecisive uh that in that that way the entropy will uh reduce


I yeah so okay

### Speaker 2

very uh in fact its not the absolute entropy it becomes i mean what we are suggesting is to minimize the cross entropy here

### Speaker 4

Cross entropy okay between the teacher and the student

### Speaker 2

Correct correct


I mean its actually not the teacher It should be the true distribution the post true posterior of labels given data That is what it should be Now because we dont have access to that given hard labels we will try another neural network and use its logits as an approximate for that That is the idea

### Speaker 4

Okay

### Speaker 2

Any other question

### Speaker 1

If the student network or the size of the student network is not so small its almost same same to the teacher network then what is the benefit of doing this because we can directly do the

### Speaker 2

I told you no it is improve improve improve generalization you know it will do much better on test data unseen data


Because now you are not training this neural network just using hard labels but you are trying to get using I mean you are incorporating the uncertainty also that is there in the labeling


Got it


And do it

### Speaker 1

Sir for the supervised loss we will be taking up the true labels y and the approximated labels from the S S phi network right

### Speaker 2

Of course yeah


Youre saying why why you are doing supervised training for the student network youre saying yeah

### Speaker 1

No no no Im um


Im trying to understand like


what are we comparing are we comparing it from the uh labels generated from f theta network or from the sv network

### Speaker 2

labels here the supervised losses losses with these true labels the output of the SVE network and the true labels thats what the losses between

### Speaker 1

And this F theta network so this can be any network right It need not be trained just that we need a representation for well if it

### Speaker 2

Well if its not if its not trained then how do you expect it to give uh the actual P of I units


Should be trained should be trained in a supervised way yeah


Okay so thats about it And yeah this is how you implement it in your assignment right I have not asked you to do self distillation I have asked you to reduce the network size and do a distillation on reduced network size itself So yeah please do that And also read this paper okay This is called a statistical perspective on knowledge distillation I will tell you the authors also stress a grain


Uh


Or this destination


to


Share the link no let me do it


You see my screen


see my screen right so this is that paper so here what they do is the following right yeah so they call this as what this pt of x is what they call as what they called as the teacher class probability estimates or the


label posterior okay so where pt of y given x estimates how likely x is to be classified as y


Now these are used by a student model which replaces empirical risk which is the standard empirical risk with the distill risk This is what they call R tilde is what they call as the distill risk Then the question is why does distillation help So they compute this thing called base distill risk and this is the main result which I just said that if you take any bounded loss then the generalization error that we get with the base distill risk is much less


compared to the tough non distilled risks that is the result okay so I suggest that you read this paper its a nice paper and this the proof that they use to show that is also not very difficult it is simply using the definitions of variance and using the Jensens inequality thats all it is have a look please


Okay uh


about distillation do you need a five minutes break ten minutes break before we go to sequence modeling


Hello am I audible

### Speaker 1

Yes it is

### Speaker 2

Shall we shall we get back after the break


So


Okay so lets come back at 11 am Maybe just take some 15 minutes break


Okay yeah see you in the way


Will we continue


Let me just share my screen


Yeah we wait you have a question

### Speaker 4

Yes sir so I was just seeing the paper so what is temperature scaling

### Speaker 2

Oh yeah yeah So that is like I think it was you or somebody else who talked about the weighting of those two losses no

### Speaker 4

Okay yes

### Speaker 2

uh the supervised and the uh clear losses


That is what is referred to as temperature scale how much weight do you have to give for each of them

### Speaker 4

Okay


Okay sir said uh okay so what is a well calibrated models so what can we do to what how should the temperature be scaled

### Speaker 2

Thats a hyperbolic effect

### Speaker 4

Okay so should we should we learn that hyperparameter or should we

### Speaker 2

Yeah see just like with any other loss function right I mean where you have two or more components and you need to decide the weight either you can do it using hyperparameter tuning or you can learn it In fact I have a paper sometime back one year two years back where we cast it as a meta learning problem and learn both the weights loss weights and the losses together All that is again


level up but yeah so typically it is trained as a hyperparameter either you learn it or keep it I mean fix it based on validation data

### Speaker 4

So can we can we have can we have a link to the paper

### Speaker 2

I mean actually shared it no I actually shared it

### Speaker 4

I mean


Okay its the same paper okay

### Speaker 2

Hes the same


So you mean my paper youre saying huh

### Speaker 4

Yeah yeah yeah

### Speaker 2

Hold on


ALMKD


the paper or the link

### Speaker 4

Maybe you can share the name and the title

### Speaker 2

Your title is there but I myself should find my paper now where is it


Its published in AAA but where is the link for that


I think so


Surprising that I cant spot the link


I found it I got it


I just put it in the chat window So what we do is that wherever you have these kinds of settings right where you have like two losses and you need to in fact one of the applications is knowledge distillation If you look at section four of the paper


We actually learn that temperature

### Speaker 4

Okay okay okay knowledge distillation yeah so two applications okay

### Speaker 2

If you look at equation nine ten and all that we actually learn that and show that uh like that its just an optimal value we do it using uh


this thing uh


Metal only yeah it is what the report is about But generally that is not done you know it is taken as a hyperparameter and used to validate fixed based on validation data

### Speaker 4

Okay okay just through some sample values and uh what is giving the right data okay


Okay

### Speaker 2

Lets move on The final piece that we will talk about is the


Quince modelling


Beta in this case


Well


Every data point okay is


Its a sequence


Okay data point in a sequence So what do you what do you mean by a sequence Lets say that x is one data point So one data point itself will have


Uh superscript perhaps huh


2 x t okay


every xj is in some d dimensional space This is what is called as a sequence where every data point has a


is a is a is a series of d dimensional vectors t of them okay so examples of this you know that this is you have


Second place


Right is a sequence of


Linguistic tokens these tokens can be characters or words or something right so the other example is the speech signal


This is a sequence of uh


Frequency domain vectors


Called the MFCC and so on Okay so this is one thing and you have


some industrial time series and you can also look at video as


sequence of


Sequence of images


or frames


Okay so this is a sequence I mean this is what is called as sequence data Now sequence modeling is a set of all those methods where the objective in sequence modeling the objective is to solve


The objective


to solve either


discriminative or generative preminative


generative problems on sequences


on sequences


Okay so now there you have examples of these problems So examples can be of course we have machine translation


where you have a sequence in right or a sequence in one language


sequence in English and what comes out is a sequence in in in Hindi lets say right so this is one example the other example can be


Ex summarization


Right you have video classification


spam detection and so on right i mean you can think of any number of problems that uh uh we have uh uh that that you can encounter


between sequences Okay so now how do you deal with this kind of sequential data is a question that people have been asking for a long time now


Now Ill just give you a broad history of how things were happening and then then well move on to what the current state of the art is


History of


sequence models


Very early days right people were using models such as autoregressive models or AR models


where the idea was the following so you have to model xt right so xt was modeled as simply a linear combination of


to or rather lets say t minus k to


Okay so this is an autoregressive model where you take you model or rather you express the tth sample Okay so we used a superscript for t you know the tth vector that we have is given as a linear combination of


see i dont want to confuse you by using superscript and subscript okay let us use uh


Script only


Dont confuse it with like one two three up to t data points okay in one data point itself you have t uh


Length sequence it is okay that is what the convention is XT is equal to


Okay so now what we are doing is every


Yet


token


in the data


is a linear combination of


Kelvin


window


before it This is an autoregressive model You can imagine why the name it is regressing on self That is why it is autoregressive So it is not using anything else It is only saying that I will express rather the tth token is expressed as a linear combination of previous t minus k tokens It is also called linear prediction model


Linear predictive coding


LPC in fact even today this is used in telecommunications to compress speech and all that so now the question here is how do you find these coefficients a and it is found out in a statistical way where you have a lot of data and try to reconstruct the data back using the k previous samples and find out these coefficients and use them in fact what is done in speech compression is that you need to transmit


uh speech data from one point to the other lets say right the raw data is not at all transmitted what is transmitted are these coefficients aj so that uh you can i mean that is a compressed version of it okay and then you use that and uh reconstruct the data back at the decoder that is in fact as i said now as we are speaking a lot of voip protocols and all this even today uses some variant of this linear predictive coding okay


The thing is these kinds of models work with speech kind of data where there is a lot of predictability but they dont generalize for tasks like machine translation and so on Okay People then move to statistical models


Such as one example was one famous example was what is called as a hidden Markovian model or HMM


Its MM was the the go to model right to model sequences go to choice for modeling sequences for a long time What is the model here is that you assume that there is a theres a Markov chain


Amongst what are called as states Ill tell you what states are


transition from here to here okay okay so and every state emits symbols


And these symbols are XJs X1 X2 up to X I mean its simply XJ okay So now these are states Z So its actually HMM right Is a latent variable model Its a latent variable model


where the latent variable is discrete Markovian


Okay and the model is the following right There is a Markovian transition between the latent variable states and at every transition right after every transition the model emits an observable symbol xt okay This is continuous


and model using neural net uh uh GMLs


So the HMM the famous HMM GMM model where see basically what is happening is the following right I mean imagine the speech signal example So the motivation behind this is


this assumption that when somebody is speaking okay what is actually happening is that before you speak you think of what is the phoneme that you have to emit given the uh semantic meaning that you want to convey okay depending upon what uh uh uh phoneme that you need to emit okay uh phoneme you need to convey uh you create some constrictions in your vocal fold and what is uh produced is a pressure difference


When we speak what happens is there is a certain pressure difference that occurs in the environment which is what is recorded using a microphone a condenser microphone So this is the observable speech signal These are the observations


which happens to be at the speech signal itself which we measure


Okay so what is Markovian R the unobservable


Unobservable abstract


What names


So now there is a Markovian transition between them because given that you need to convey something and given that you have already said the particular type of phoneme you can only choose from a I mean there is a probability from which you can choose what phoneme to be uttered next


So that is why there is a Markovian assumption between the hidden states and what is observed are the measured quantity Now this is a model and the distribution So now basically what happens is there will be a distribution amongst the states


which is Markovian


And that will be a distribution over the


observations given uh a particular state this is modeled as a Gaussian mixture model this was the this was actually the standard uh this used to be the standard modeling choice for any sequences where you say that okay so you can extend this for lets say handwriting recognition right where the observations are modeled as uh the pen strokes or the coordinates of the pen strokes and the latent variable or the z models what was the uh the what is the


Uh


letters or rather the symbol that is to be conveyed okay


And if you want to model speech as I said there are phonemes and every phoneme emits a symbol which is a speech signal and so on Okay so now what as to what are to be learned This is parameterized by some theta this is parameterized by some phi Theta and phi are learned


using the EM algorithm So we have seen the EM algorithm right in the beginning classes So EM algorithm is used to learn this So this is how initially the sequence models were being learned So if anybody wants to learn more about HMMs right there is one very nice tutorial by Lawrence Rabiner


have a look at it where he formulates the problem and write downs the likelihood log likelihood for an hmm and works out the em so basically it is working out the em okay hmm tutorial


Any questions so far on this

### Speaker 4

So but in this MARCO model ah are we actually passing the is it dependent on the past I mean

### Speaker 2

It is no it is because it is Markovian yeah

### Speaker 3

So just to know I mean you said when we say a sentence right we say one word and the next word is basically we can predict whatever is the next word kind of right

### Speaker 2

Not predict there is a probability over what the next word is going to be that is reasonable because if you are con yeah because in a given language given that you have uttered one word theres a certain probability of what the next word is going to be

### Speaker 3

So it just depends on the previous word alone right

### Speaker 2

I mean it depends on what order of the Markovian assumption that you are making you can make it a first order Markov second order Markov third order Markov anything


Its called an n gram model right You can make it a unigram bigram trigram anything right So it is not one word always In diffusion models we assumed it to be a first order Markov process but it need not be first order Typically it is taken to be a third or fourth order Markov process when it comes to the sweet signals


Okay so as I said right I mean HMM is sort of obsolete now Like its not the go to choice So then came the revolution of neural networks right This was in this was 19 early 90s and so on This AR models right autoregressive models they date back to like early 19th 20th century And then 1980s and 90s people started looking at hidden Markovian models and other statistical models similar statistical models


the when neural networks started taking off right so came the recurrent neural networks


known as oddimans


I think if there is one more tutorial right you can ask Chendran to talk more about RNNs and BPTT I will just give you an overview So the idea in recurrent neural networks is that what you have is that you build a


Okay so let me before that see what happens in a in a sequence kind of data is every data point


have


Different length


Right because imagine that we are looking at


If you are looking at natural language sentences then each of the sentence will have a different length you know obviously So now if you take a fully connected neural network or an MLP it is difficult to handle data with different lengths So now how do you handle this is the question So now the one answer is to use what is called as recurrent neural networks The idea is the following that


to handle


Equal equal uh


Not equal


Input lens


So what you do is share the parameters across time


What is meant by this but this is the architecture of a bare bone


Recurrent neural network


say that you have x p here that is the tth length and you have the corresponding y t because its a sequence in sequence out model now you have the t minus first hidden state you have the tth hidden state going out okay this is one r and then


RN block or RN and RN cell


So you have parameters that are lets say U P and W


Okay now the relationship between the parameters are given by this that you have yt is equal to sigma of w times ht minus 1


Less


Uh is there


xt is coming into u times of v times xt and the next state or next hidden state is given by


Its right what Im writing no we times that is this yeah u times x t x yeah yeah

### Speaker 3

Oh

### Speaker 2

u times xt


Less


W times 15 minus 1 yeah


Yeah so this is one R and N cell So now what do you do is that you get


Have you seen an RNN picture right where people write this kind of a thing


Okay so and then they write something called unrolling of RNN So what that means is that you repeat this So now if you have a sequence of lets say length T


uh its its zero


There is x1 here x2 here and x3 here And you have h1 h2 and h


t and y1 to yt observe that everywhere so you have the same u w and v exact same parameters everywhere


So this is what is called as parameter sharing across time

### Speaker 1

So in the equation for yt


Shouldnt XT be multiplied with U

### Speaker 2

x t b multiplied with u see the the way i have written is uh that you take x t here multiplied with v and then get y t and you take x t but i can write u here perhaps this is better no write it this way


I think this is better


What I meant


here there is W here there is E and here there is U


Is it alright now


See what is important is that you see that the parameters are shared across time in the sense that for all times okay x1 to xt the UVW matrices do not change okay they are actually shared across time and that is how an RNN is trained okay now how do we how do we get these UVW matrices theres an algorithm called back propagation


back propagation through time okay its not at all difficult ill tell you what it is so we know back propagation its abbreviated as bptt we know back propagation but here what happens is the loss is calculated between yt and xt here right you calculate loss between xt and yt or rather at all points and you have a loss here at


uh x x5 and y5 and so on so what you should do is uh all these losses right have to be back propagated this way and they should also be back propagated this way


So there are two directions in which it back propagates and that is why this algorithm is called back propagation through time because there is a back propagation through time also time direction also So you have to basically add those two losses one across the space one across the time Thats all an RMI is trying As I said no if you are interested in a nice articles or you can also ask TAs to run through back propagation through time but now with all the things that you have learned in this course if you just look at


standard uh descriptions on ppt you will understand what it is okay


So this was being used then what happened is um uh


It was this uh


This is okay if you want to solve a supervised learning problem where you have input and output lengths equal You can have different input lengths different sequence lengths at the input but the output lengths have to be different But a problem like machine translation


Whereas both the input and output lengths are different


You cant use one standard standalone RNN okay What is done is the following so you have an RNN


And by the way what I just showed you is a naive RNN okay And there are improvisations over it by using things like LSTMs long short term memory networks which are different ways of writing these two equations okay So to avoid this problem called vanishing gradient So what happens is when you do backpropagation through time because there is parameter sharing across time you will multiply the same WUV matrices multiple times with each other


And if the length of the sequence is too large then the eigenvalues of that will reduce over time and the gradients will have very less values That is in a nutshell what is called as the vanishing gradient problem And you modify these equations so that there is a skip connection sort of thing that is used in resonance so that the gradients will not vanish And also what is done is there is no like this is only one layer RNN that I


showed you what can be done is you can have multiple hidden states like this okay and you have multiple matrices uh across the space also okay those are all improvisation that i dont talk about here what is done in in in cases where the input and output both of them have different lengths is the following that you use a typical encoder decoder sort of model where you have x0 to xt okay


We have HT here You take another


and then or a sequence where you take h t and output y 1 okay and you take y 1 and give it as an input to the next uh unit and give get you on y 2 and take y 2 and give it as an input to this and get y 3 and keep doing this till you get the last symbol emitted which is y m so typically how it is uh


And in the in okay lets not call it YM so that is XT and this is


Typically how it is done is that there is a special symbol called end of sequence symbol which is one of the tokens that is used Now you keep emitting or you keep generating till you get the end of sequence symbol And once you see the end of sequence symbol just stop it there That is how the translation or decoding is done So this is the decoding network

### Speaker 1

Sorry youre not audible at least to me

### Speaker 2

Is that so Hello

### Speaker 3

And also

### Speaker 4

Youre audible for us homie

### Speaker 2

Okay so this is the uh the input language


Sentence in input language and this is the translated output


Yeah so this is the typical encoding decoding model using RNN kind of architectures And this was actually in the state of the art till lets say 2014 2015 times okay In some form or the other of it which is an improvisation over this is what was being done Any questions so far

### Speaker 3

Yes just one question


Uh you said we dont send the speech initially we send the symbols right and then this is

### Speaker 2

No no this is this is this is a text translation no this is a machine translation task

### Speaker 3

No no no but before this


Uh you said symbols are transmitted not speech and speech is regenerated right

### Speaker 2

Uh the you mean for the telephony right Long distance telephony and all that Yes that is true

### Speaker 3

And how voice can be transmitted actually or how it will recognize like if I speak how the generated signal will match my voice

### Speaker 2

Okay Yeah thats a good question See what is done is the LPC model right One there is content There is another thing which is your signature which is that no matter what you speak there is a particular source signal that that mimics your voice that is your signature Okay Even that is transmitted And that does not require a lot more bits I mean that will go to speech signal speech processing theory So two things are transmitted One the


part of it the other is your voice signature think of it like that so its like given your voice i can overlay any of the symbol any of the phoneme that i want on your particular voice thats the idea

### Speaker 3

And for this text thing the words can be in different sequence when transmitted into or translated into different language

### Speaker 2

No no no words no words will be of different length I said

### Speaker 3

No length is fine but one language may have a different order of words If their literal meaning is taken then it will not make sense Like in different language it will be a different sequence of words

### Speaker 2

Now the words themselves will be very different right

### Speaker 3

Yeah and their sequence will also be different right

### Speaker 2

When words themselves change how would the sequence matter of course statements will be different so

### Speaker 3

how that is learned while predicting

### Speaker 2

Yeah see that is why what you predict is given the previous word that you have out I mean you have given as output the next word is predicted That is conditioned on the previous word Now you can see here that the output right y2 depends on the previous word y1 So if you have enough data the hope is that the model would see all those combinations implicitly

### Speaker 3

Okay but first well be in the tradition

### Speaker 2

condition done condition ah see now the question is I mean how would the first word be uh predicted right the first word would be predicted based on the input sequence and what the input sequence information goes to the the output rnn through this last hidden state ht so its like you encode the input sequence in this hidden state ht and that goes as an input to the decoder okay and


encoder gives you the first word right based on the first word and the hidden represent there is also one other hidden representation here no for the


or the decoder also based on that the next words are predicted one by one

### Speaker 3

Okay and is it trained on some kind of literature or trend

### Speaker 2

Pairs pairs pairs they are trained on pairs of sentences from languages So you have to have a lot of pairs of English and Hindi sentences and given a pair of English and Hindi sentence it will be trained that way Its always trained on pairs

### Speaker 3

Here you are saying

### Speaker 2

Yes be I have this


Let me write that down


Does it make sense

### Speaker 3

Yeah so even if its trained on pairs of sentences it will not kind of do we do couple right It will just try to generate each word separately

### Speaker 2

One word after one word after the other give conditioned on the previous word


Yeah thanks Vivek

### Speaker 4

So after the encoding process is over we just have a single uh vector right

### Speaker 2

Exactly thats an issue

### Speaker 4

Yeah so thats exactly what I want to know its hard to believe that one small vector can

### Speaker 2

Yeah its a you point exactly that was actually an issue and that is when Ill just hold on to that question that would be my next narrative

### Speaker 4

Its a you


Okay

### Speaker 2

Im actually building up to transformers so that Ill tell you why that is an issue and how people solved it okay Santosh

### Speaker 3

Yes sir So the number of RNN cells will be equivalent to the input sequence in the first layer

### Speaker 2

Correct correct correct See that is because it is it is the parameters are shared across time We are just repeating the same RNN cell one after the other with a different input and hidden layer thats all But the weights remain the same across time

### Speaker 3

Okay Also my second question is that right now we have only two layers If we have multiple RNN layers so the final hidden state of first layer will be passed to the second layer and then like that So the output will be passed to next layer There will be two

### Speaker 2

There will be two things right if you have like a two layer thing there will be one that goes like this one that goes like this

### Speaker 3

Um

### Speaker 2

Yeah you can have any number of NN layers one after the other Any number of hidden layers one after the other You can make it deep

### Speaker 3

Okay okay yeah

### Speaker 2

As I said in the beginning of the course right I like this is not a course where I teach NLP fundamentals and architectures right So I mean one can actually teach a full course on sequence modeling and how RNNs work and a lot of nuances there But as I said this course is more on like you now you know what this course are Im almost coming at the end of it But yeah so an overview of RNNs are like this Any other question on this


if not lets move so as uh this was as i said no this was the the state of the art till


or machine translation okay like till lets say uh like 20 tens okay 20 tens this is what was being done and since uh this is not as as you can imagine right as Vivek was said was saying theres only one hidden state that has to compress all the information regarding the input sentence it was not doing great and thats why machine translation was not available commercially at large scale beyond the academic labs right so then came this nice idea which


I will tell you


is X1 this is XT and you have


one white two


to y uh what did we call s okay


Somebody thought that okay why only have one


hidden representation compress all the information that is regarding that that that that I mean regarding the entire input sentence so can we do something else so this is like the hierarchical VAE idea so somebody said okay well do this that we will take the


This is the first hidden representation This is the second hidden representation hidden representation corresponding to x3 and all that Now what is done is that you take you have take all of these


Take a linear combination of all of these so let me write it neatly


abut


AJ


HJ okay


if h1 h2 h3 and ht and compute this and give this lets call this uh h8 cap okay a


Cap okay and give this as an input to


and have as many uh a t so there is a one and there is a two you have another string which is lets call this as a one


This is uh AJ to HJ


have a three cap and so on okay and give all of these as inputs to


the corresponding output sequences


Does it make sense So what we are actually saying is take a linear combination okay and here the as are also learnt okay


Do you understand what is happening


Now instead of making one hidden layer have all the information and compress and then decode saying I will take I will tab the hidden representations from each of the time steps from the encoder side take a learnable have a learnable linear combination of that and then give it as an input while decoding


Do you understand this

### Speaker 3

So what is the A here

### Speaker 2

A is a learnable constant

### Speaker 1

Professor how is AJ1 different from AJ2

### Speaker 2

Sort of hose


They are learned differently no

### Speaker 1

But though they are tapped from the same motor right

### Speaker 2

But they are mapped from the same mode Thats right But these indices are taken to be different So here what you do is here you only take j from like 1 to 2 and you make 1 to 3 and you take like just cumulatively do that


Okay


there are different improvisations over it but the idea is clear right what you do is you take a linear combination of hidden layer representations and take a i mean learn the weights with which they have to be linearly combined and then give it as an input while you are decoding it is this idea clear

### Speaker 3

So sir here number of linear combinations equal to number of ys right I mean sequence number of

### Speaker 2

Number of voices number of voices correct


Okay now do you know what these things are This is actually what is called as attention


This is what is called an attention okay uh like say like R and Ns with attentions


is RNN with attention okay what you are doing is that you take the linear combination of hidden layers and then uh take uh give that as an input to the while decoding so this uh received a lot of attention okay uh and this gave a significant boost in terms of uh uh what the uh the what we could achieve using machine translation okay so then came this this this thing no which is the


transformer architecture where they said okay see any way youre using attentions here okay why even have an RNN cell because you end up with the problems of vanishing gradient and all that if you have very long sequence lengths so why not create an architecture right so come this transformer


Which is


An attention only architecture without a recurrent nature structure


Without recurrence


Yeah that is what a transformer is all about okay it is an attention only architecture without recurrence


Ill briefly talk about what attention is I mean this transformer is okay Now you have like input sequence X that is equal to


x1 x2 up to xt right


Okay now a transformer is some function f theta that will take each xj and gives you a corresponding zj


Okay so now what does it do is given


A sequence X


of data X okay a transformer


outputs


A sequence of


representations or hidden layers or hidden representations I mean you dont have to call them hidden representations


z okay for corresponding to each of the input token so for every input token xi there is a uh corresponding uh representation z okay that is how you do it so now the question is how do you get the zg right now zg is given as


a linear combination of


alpha j what is called as t


value vectors okay now i will tell you what these value vectors are so now given


Given a


Data token


xj xj okay multiply that with


Three matrices call one as the query matrix So this is


Transpose X J okay then you have


value


matrix


the key matrix


What are we doing We are getting three particular vectors Okay So here do all


Obtain three vectors


Okay as does here the W Q W V and W uh


wk are learnable and learned through backpropagation these are the learnable matrices do you understand so what is happening given a particular data point you take each of the token corresponding to it which is a vector okay uh pre multiply that with three matrices okay and you get three other vectors call them query value and key is that okay


Lets call any query but any questions so far

### Speaker 1

XJ should be the entire sequence right not one of the

### Speaker 2

One of the no no no its one of the components its not the sequence because for every vector in the sequence okay you compute the query value and key

### Speaker 1

where x in itself is a vector

### Speaker 2

X is a sequence


X is a sequence that has p number of vectors


Is it okay


See how did we define a sequence we have defined a sequence this way right


A sequence every vector right a sequence is a t length


where every each component of it is a d dimensional vector


So every x j is a vector here


You get these three vectors right So now then what you do is


You define the


representation corresponding to the jth token as a linear combination of


all the value vectors corresponding to all the other tokens in the sequence okay so the question is how do you get this alpha j


This is alpha J cotton so what you do is that


Multiply the


jth query get the inner product of the jth query which actually I should call it alpha uh okay hold on


So uh


I need one more symbol here


This is what J oh now what the


Okay let me just write it So now you take the jth query and multiply that with the ith key


declare that with the ith key okay then what you get is you get the attention score or the weight score corresponding to the jth query and the kth key okay so this will give you alpha ji


Is a scalar fine now uh


You need to multiply this


Thats why Im thinking how can I simplify this just give me a second quick think


Theres one value


I need to look at


Dude


Yeah this is


So fix this K


This is what it is


Uh do you understand whats happening


Okay so Ill tell you see now what is happening is that we are given Ill write it here it will be easier


I thought this class would end early these are these are


These are sequences right FT sequences What is first done is that you multiply these with the W matrices and get the corresponding queries So this is Q1 Q2 up to Qt We have these queries and we have these multiply that with the K matrix and get the


Okay and then you have the multiply that with the


value matrices to get the values


Okay now what we are doing is uh we get


to get z j okay z 1 to get z 1 what you do is you take the uh inner product okay between the query corresponding to the first token okay with the query keys corresponding to all of the tokens so this is a you take an inner product like this between this these two


East two east two


these two and these this will give you what will this give you this will give you uh the way i have written it this will give you alpha 1 1 alpha 1 2 alpha 1 t


Is this okay


Are you getting it


questions on how are we getting alphas


This is important so please tell me if you dont understand this


Hello am I there Am I audible

### Speaker 4

Yes sir you already will yes

### Speaker 2

Okay Yeah Total radio silence So I dont know how to interpret it Is it okay Did all of you get how to get these alphas


Yes hello


Now how are these Vs obtained Sorry Zs obtained They are obtained by taking a linear combination of all these values okay and they are weighted


by the corresponding alphas In fact its actually a convex combination So what is done is you dont use alphas but you use betas


And so


beta j is okay where betas


Or you take alphas okay


And divide that by some constant d which is the dimensionality of data And then you do a


See that


Alphas are soft max


Over alpha divided by t thats all So now why do you do this This you do because


all beta js right they are bounded between 0 and 1 and they are simply sum to 1 that is why you do this soft mat so that the linear combination of the values that you are taking okay uh is bounded between 0 and 1 so now let me repeat what is done here is that


You given a token given a sequence of tokens Okay which is an input data point one input data point you define three matrices Call them as and multiply those data points with the with these three matrices Okay they can call them as the query value and key Vectors so corresponding to each of the token you will get three vectors Okay then the representation corresponding to each


of the input uh token is a linear combination of all the value vectors corresponding to each of the tokens okay thats all now how do you define uh which of the mean how do you get uh what is the weight factor for the linear combination to get the weight factor for the linear combination you use the query and key vectors how uh you take the query vector corresponding


to the token of interest You take an inner product of that vector with all the key vectors corresponding to all the tokens and normalize it so that it lies between 0 and 1 That would give you what is the weight or scale which with with which you have to scale each of the value vectors to obtain the representation corresponding to the I mean the token of interest So this is one


Transformer block


with a single head they call it and there is also a counterpart uh called the multi head uh attention ill talk about that in a while but yeah any questions so far

### Speaker 4

So so if we shuffle the X1 to Xt then the Zs will also be shuffled


In the sense like the if the sequence changes

### Speaker 2

Yes it is true

### Speaker 4

Okay so please go ahead yeah so


So so does it when it changes does it still remain the do the individual values still remain the same or will they also change

### Speaker 2

No no they do change you know they do change depending upon what the sequence what the what the correspond what the relative positions of each of the tokens are in the sequence They do change


Yeah case fixed Yeah So you you keep hearing about this context lens of all these LLMs right


They say that they are coming up with like larger and larger context length This t is what is called as context length Now it is like 2500 is what the context length of GPT is and so on That is the context length So now you might ask this question


We started by saying that each of the input data point will have different sequence length How does transformer handle it They handle it by just zero padding Thats all So they keep a fixed context length And then if that length is equal to the highest possible length of the highest possible sequence And for all the other sequences that have length less than the highest possible length sequence theres a zero pad them and make them equal length And now how does that how is that handled


The hope is that that is handled by the appropriate representation


Okay the attention for or rather these alphas and betas for that corresponding


zero tokens will be zero and it has been observed that they will actually ignore them

### Speaker 3

One more point here so I mean here that position information is not present

### Speaker 4

Full of the

### Speaker 2

Yeah yeah hold on Thats correct That is correct And do you recall that during our DDPM discussions I talked about positional embeddings where we have to do give T the time information also as an input right In transformer also what is given is in addition to this T is also given as an input using the positional encoding


for the precise reason that you said


positional embeddings and we talked about positional embeddings during the


L M lectures sorry the diffusion lectures okay fine now how do we finally solve the uh the


Sequence to sequence problem is that we have here a transformer block


There is one other like normalization layer that they use and also a skip connection like ResNet and so on right Im skipping that The major focus is on attention okay So can yeah there are enormous amount of literature on this Youll understand And the difficult part is how the attentions are actually


computed so you get z1 through zt okay and there is this this is the encoder


And similarly there is a decoder block


It uh what does it do is itll take these uh


embeddings are the representations given by the encoder as the input okay and then do one autoregressive uh uh generation so now you get one y1 and you take y1 as an input and give it just like you do it in rnn right so you take that and you get y2 and you take that as give it as an input and so on okay so in fact this is exactly what a large language model does i mean in the okay


So this is bald kind of language model this is how the training happens in addition to this theres also


like attention blocks between the encoder and decoder okay


These are called uh


cross attention or details so this is whatever we saw right which is attention between the input tokens that is called self attention and there is also attention between the


queries keys of the the encoder and the query keys of the decoder that is called cross attention and this is actually the bare bone of what the modern day LLMs do okay so now you know that right I mean you are given a particular prompt when you give a GPT a prompt what you are actually doing is giving a prompt to the encoder and depending upon your prompt this decoder generates and how is the training done surprisingly enough training is completely supervised


Supervised training


using KL minimization I mean like uh the


Usual cross entropy loss is what is used


Its all the bare bare minimum try bare bone training of an L M happens in a completely supervised way Okay Using K L minimization So you have pairs of these tokens input and output tokens In fact actually what happens is that you first try in an embedding extractor using the self supervised learning techniques that we just saw no masked reconstruction Last class we looked at masked reconstruction So what is done is let me just talk about it perhaps


So first thing that is done is okay this is the broad level LLM training typically happens this way


So there is first a self supervised pre training


Well thats


And by the way architecture wise right everything that is used in an LLM today are transformers you take a transformer


Uh take an input sequence


And uh


You get the embeddings and the task is to simply reconstruct the data back


using the encoding so I technically speaking theres also an encoder decoder model here another transformer


the decoder


g1 to z3 and what is given as an input is uh a a version of x okay where it is uh where x cap is


masked masked version of X


usual self supervised learning task that we do right and this these zs will go as input to the decoder and what is given back is the true data so this is exactly what is done in BERT okay so you have an encoder and a decoder and encoder takes a masked version of x with random mask and it reconstructed data so this is what is called as the self supervised pre training


Okay this is done Once this is done you get embeddings of data So then you use a usual encoding decode encoder decoder model in the second stage using supervised fine tuning


Supervised fine tuning okay on the embeddings obtained in the


obtained using self supervised learning


See surprisingly uh


The inner workings of LLM is very very simple I mean from an ML complexity perspective all you do is take a lot of data and do a self supervised pre training using master conception kind of tasks and then you do a supervised fine tuning on whatever data that you want to fine tune it on Thats all it is Using transformer as the backbone


Now I mean there are nuances here where when you are doing fine tuning right you may not have a lot of data How do you do it without fine tuning There is this retrieval augmented generation or RAG kind of frameworks And also this low rank reconstruction low rank approximation for fine tuning where the problem is that if this pre training the model is like billions of parameters you cant you cant fine tune on all billions of parameters You just take a subset of them and then fine tune And all those are other


supervisions and nuances but at a broad level this is exactly what happens so we theres a transformer which is which is the big backbone architecture you take data typically from the entire internet and do a self supervised pre training using uh uh mass reconstruction task which we have seen and then whatever take that model which generates embedding and do a supervised fine tuning on whatever data that you want and thats and if you do that


But then you already have a like GPT two or GPT three that is there


thats thats what it is uh any questions on this yeah as i said no this is not a full course on llm so i dont go to the nuances of it just wanted to introduce and put it in the perspective of what the the so called modern llms are doing so this is exactly what it is in the as i said no in terms of ml complexity its very very simple there is a self supervised pre training using transformers and there is a supervised fine tuning that is happening using uh ugr


cross entropy kind of losses right and the underlying architecture that is used is a transformer please also remember the word generative AI right it is used in a very very loose sense today in in outside of expert community where it is used for like image generation language generation and all that whenever there are there is a sequence task that is done no it a transformer is used and this kind of recipes follow


So wherever there is an image generation task no typically transformer is not used a diffusion model is used


Okay so thats about it Thats all I wanted to cover in this course


Yeah so lets maybe just stop recording


Yeah see the thing is even when you fine tune right sometimes you know it will not it may not suit your purpose You know its think of it like using an additional data that you have okay without doing a fine tuning I mean supervised fine tuning on it You use that additional data to guide your transformer or generator in some way I mean or the decoder See in all our generative


first modeling right we know
