---
id: PM1dQTlwHWY
title: Lec 8 - Deep Generative Models WGANS Intro Latent Variable Models
url: https://www.youtube.com/watch?v=PM1dQTlwHWY
date: '2024-11-23'
duration: 02:55:07
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

## Transcript

### Speaker 1

Yes sir we were able to see the first quiz also you got to see the marks right

### Speaker 2

suggesting this

### Speaker 1

Okay thanks And we have decided the midterm exam to be on 10 13th or something right I think Ive marked our calendars also

### Speaker 2

Yes its 13th August on

### Speaker 1

13th after noon okay great okay so lets get somebody has raised their hand Aditya yeah

### Speaker 4

Uh sir maybe a logistical request if feasible otherwise please reject because this code two to six is like a festive for us like Durga Puja and all the Shara So that assignment time can it be this by Matt report there Just a request if not for feasible please ignore

### Speaker 1

What can what uh I

### Speaker 4

the assignment date assignment deadline is nine i believe right and two to six is somewhere is a festive session for most of us like the theradurga etc so can it be increased by two three days i mean the timeline because we may not give the complete hour should be given to this project during that time its just a request i mean if not possible please ignore

### Speaker 1

I mean see what happens is if I move it then the other assign the entire schedule has to be re arranged


Kindly excuse me on that


Okay lets get started uh


You dont see my screen

### Speaker 3

Mm

### Speaker 1

So todays agenda is that uh as I said we will move on to the next class of models which are various autoencoders which also happens to be the


a baseline for the state of the art generative image generating models called diffusion models which we will see next okay so before we go there uh we just take uh some 10 15 minutes and quickly finish this domain at those serial networks right which was left out the last time


Palm is there


Still let us


So I highlight this


Somebody asked me to central line this so they can get cut


Doesnt even know how to do that


Yeah


Okay thanks we should be enough


Okay so um


We will start with this uh domain at our serial networks okay or so called DANS one of the


powerful applications of adversarial learning other than generative modeling and also right before we start I hope that you have started with the assignment


Uh and if there are any questions you can let me know or ask also

### Speaker 4

I pinged and TA but no one replied

### Speaker 1

Oh is it I Ill ask to do it So last tutorial was done on CNN and PyTorch right Was it useful


mean in the assignment you are saying see what i have observed is that uh that this animal data set right because there are multiple classes there about 90 classes uh unless you have a very uh deep architecture and you do a lot of hyperparameter tuning you dont get a very good generated images right but you know if you if you get images that are like

### Speaker 4

But it doesnt work

### Speaker 1

award looking like aha butterfly you will definitely get for that data set you will get good dream images not for the first one there are two data sets that we have given now


Yeah for the animal data set the images that are generated are like somewhat uh like looks looks like animalish but you need a lot of resources and deeper architectures to


get very good results okay in fact


Okay so uh have I uh


We talked about FID in this course


Oh no

### Speaker 4

Not exactly

### Speaker 1

It is planned for today Yeah Ill have to do that today as well


Ive not told you about the the bursa strains metric also no

### Speaker 4

knows that we havent


Uh if the data set is hard for question one and two then why are you asking for the other questions

### Speaker 1

And it is the code

### Speaker 4

Like if animal data set is hard to train given the compute resource we have then for other questions also like third fourth and waste all like well have to use the same data set right Animal then well have a poor result there also if we train this animal Okay

### Speaker 1

Nah


Thats okay Thats okay See the assignment grading will not be based on the quality of your generated data anyway Its not about results


So yeah but it has I mean I have deliberately chosen that data set because I want you to appreciate the fact that if there are too many classes and data has a lot of modes right


Building a generative model is difficult especially using adversarial training So we will use the same data sets for VAEs and diffusion models and you will see that it will improve It was deliberately done Yeah


So theres a

### Speaker 4

This is a confirmation what we were trying to ask the butterfly data set is for only the 192

### Speaker 1

the front

### Speaker 4

from the third onwards we need to use the animal data set the the the the first again we need to use the animal data set

### Speaker 2

and to see how the outcomes are coming even the FAD calculation everything

### Speaker 1

But

### Speaker 2

Okay okay that was a question

### Speaker 1

But for the first and second question you will have to use the animal data set as well both of them

### Speaker 2

So yeah we definitely we need to train it for the other

### Speaker 1

But its

### Speaker 2

Okay but the generation may not be so accurate

### Speaker 1

Yes yes yes


Okay so lets maybe continue quickly Here I go on lets go on Yes sorry sir one more thing I noticed sir in the original Jan paper the model was basically on a 64 by 64 image The moment I scale it up to 128 right I noticed the mode collab

### Speaker 2

Becomes a lot frequent than 64 by 64 like the performance is much better

### Speaker 1

Domain D C again youre D C again youre saying

### Speaker 2

Yeah yeah yeah

### Speaker 1

TCAN okay Yeah see you can tweak One thing that you can do is if you start from 128 128 just have another down sampling layer and then use TCAN on top of it

### Speaker 2

Sure sir um I tried that I think it requires a little hyperparameter tuning to get it right

### Speaker 1

Got it got it


Yeah biology


Its in the again the first question


Shatya

### Speaker 2

So there is the instance of GAN we discussed right where we used the GENSIN SHEN and DIVERGENT for being naive GAN So actually if you see that the GAN paper right sir that is the GAN is separately mentioned and GENSIN SHEN is also separately mentioned So its not that because of GENSIN SHEN and here we are talking about GAN

### Speaker 1

Okay okay Ill tell you Yeah see okay thats a good observation See the divergence that is used in the Naive GAN paper is Jensen Shannon divergence minus a constant I think its log 2 or something Okay thats the and its JL divergence plus a constant That is what the GAN objective is


Okay so lets maybe quickly go to too many things to discuss Okay lets get started Yeah its charged I said so this


there is another application of uh uh adversarial learning which is called domain adversarial networks okay so here is the problem so what you are given as you are given some data from a distribution called source distribution okay its one y one


Two way two


Up to


X and Y and note that this is a supervised problem this is drawn ID from a distribution PS which is called the source distribution this is source data


And there is another data that is given to you we call XCAP one


two and


Thanks


this is sampled iid from et okay and this is called the target data


You note that source data has both the features and labels target data only has the features and does not have label source data is a supervised


And this is unsupervised


Now the goal


what is called as unsupervised domain adaptation


called as Yuda okay is


Even


PS and DT


Learn features or representations


So thats that


Thats that they perform


Well on both source and target data


Oftentimes what happens is that suppose you want to let me just give you an example uh suppose you want to uh you are you want to build a classifier


Mm so what a waste


So some examples in the list


Give me a minute Im just looking for that image


Yeah this is good hold on let me share my screen


You see my screen

### Speaker 4

Marius

### Speaker 1

So you look at this So there are these data sets There is MNIST there is USPS something called MNIST M and there is the street view house numbers data set Now what you see is that all of these are semantically the same The class wise they all have the same right They have digits But if you build a classifier on lets say MNIST and try to test it on USPS


it will not give you good performance


Now the goal is that suppose you are given


data from MNIST with labels and data from USPS without labels That is the setting right Where you understood the setting that there is a source domain which has labels and theres a target domain which has data but does not have labels


Now the task is that you have to build representations such that


The classifier that is trained on the source data does well on the target data as well That is the problem setting


Is it clear any questions


So you have to ensure that the problem definition is clear then we will move on


Please ask if you have any questions I can see your sir Yes Shivan Yes sir When we say we want to learn this on the the the model should perform well on the target distribution as well eventually we will be passing target distribution back to the model

### Speaker 2

get the respective target labels right

### Speaker 1

The final evaluation will be done with target labels of course but while you are building the model you dont have target labels


Of course I mean you can evaluate the definitely it will be based on the target labels only but yeah


I dont see yeah uh Satya go on

### Speaker 2

So sir isnt it the cycle young the same right Richard only that we dont have the label for the first data set or the second set or something

### Speaker 1

No see in cycle again the objective is to convert the source data to target data right Generate samples from target data Here you know youre not the objective is not to generate the target data it is to build a classifier or representation such that it does well on target data as well

### Speaker 2

Okay okay to produce a label over that argument

### Speaker 1

Send it

### Speaker 4

you answered my question so basically we are trying to

### Speaker 1

Basically we are going to move on Lets move on Then lets move on please because theres too many things to cover today If Ive answered your question lets move on Okay So thats the uh the um okay Ill have to share it again


What is the problem setting See there is also another class of problems right where you do not even have data from the target distribution Those set of problems are called domain generalizations


This is domain adaptation Suppose you dont have DT as well Then those class of problems are called domain generalization We are not looking at domain generalization Now we are looking at domain adaptation where target data is also present albeit without labels How do you solve this question solve this problem There are multiple methods that people have come up with One of them is what is called as domain adversarial networks


Way networks serial networks okay what is done is the following Ill show so there is a


Each are extractor let us call that as some phi of x


This will take excess which is the source data


think let us okay x and x cap right x is the source data and theyll also take


Is it target data as input Okay Itll give you the corresponding representations So lets call it as ZS


ZT it ended here


Okay so this is a simply a feature extractor So this P is a function that will take X and it will give you some features Z Okay then what we will do is there is a classifier there is a critique network here or a discriminator network here


EW this will take a Z so this will take either ZS okay sorry ZS


and Z T


Okay now I should say that uh


P of X is equal to ZS okay and P of X cap is is GT okay that is how I have represented it


Now what I do is I will


Find this thing


This will be trained adversarially okay


The gun


To ensure


distribution of Zs okay


close to the distribution of Zt


Correct That is what if I try this adversarially right then what happens is that the distribution of features PGS will be close to the distribution of PCT Do you agree


See this uh whatever I have uh uh okay


Marked with red colour this is again okay


Ow


It shows


ECS is the same as ECT


Does it make sense


Now phi of x will become the generator okay and there is another discriminator that is there and you are ensuring you are training it adversarially to ensure that PZS is equal to PZT So what is the loss function here The loss function would be that you learn your C star and W star okay such that minimize


in over phi and max over w you have an expectation of log of


GS as GS comes from PS


you have expectation of


Lot of


One minus uh


PW of Z


this uh ZT comes from


easy to


getting it so now if i train this as a gan now right what it will do is it will ensure that the features for the source data and target data follows the same distribution


Does it make sense


Any questions on this


Go on and read it


Can does it go on please


I dont know if you can uh any any can you hear me uh all of you

### Speaker 2

Yes sir

### Speaker 1

Okay Raghavendra Govind go on Oh yes in this case the phi network that you have shown is kind of compressing the features But I mean is it reducing the dimensions or Yeah it is Typically z is less than dimensionality of z is much less than that of x


It acts like a generator now yeah

### Speaker 2

But I mean it looks very similar to the discriminator right because uh its reducing the dimensions

### Speaker 1

Lets reduce the dimensions No just because it reduces the dimension its not a discriminator right It is simply a neural network that transforms X from Z X to one random variable to other It can increase the dimension reduce the dimension doesnt matter


Of course it is similar to discriminator in the sense that it reduces the dimensionality but yeah it is not a classifier right Which is trying to give a number between zero and one


Okay so this is uh uh Yamiwake

### Speaker 2

So what does it mean X and X cap So are we passing it in sequence or are we

### Speaker 1

In sequence or are we Yeah sequence sequence yeah So you X when X goes ZS comes out When X cap goes so ZT comes out

### Speaker 2

technical some

### Speaker 1

Here in additional to that theres also a classifier here okay


This classifier its called the task H theta it will take z


as input the s as input and it will give you y as output which are the which is trained on only the source domain Okay Now this


He does start


Theta star okay simply the minimizer


of the cross entropy loss which is


GES coming from PS simply the minimizer of the usual cross entropy loss we can train supervised in a supervised way


Now the gradients flow like this


So the gradients for the free network right one there is


backward pass from here to here


It is learned at OCLE and then there is another backward pass which is which is supervised training that goes from


Yeah two inches


But this is supervised classification


Youre supervised


And this


This is our new CD


So now what is happening is that this fee network is trying to learn features okay in such a way


One it will ensure that the distribution of the features on source data and target data are exactly the same This is done via adder serial optimization And the features are also learned in such a way that it does classification well on source domain


Okay now during inference what do you do Finally during inference


inference okay uh you take x cap coming from pt okay and then pass it through phi star which is will give you gt then take gt


and pass it through the


Classifier this will give you the labels which are the predicted labels on


T


Does it make sense So this this is how you are doing so what you are doing is you are trying a classifier on source data okay


using features that have the same distribution as that of the target data Now you basically are training a classifier that has exactly that is working on a feature space whose distribution follows exactly that of the features of the target and you are ensuring that it will happen you are enforcing that it will happen via adversarial training Okay so now once it is done the features that are extracted


for the source data is same as the features for the target data So now if you take the features for the target data and pass it through the classifier that is trained on source features


It is expected to do well on the the the features of the target data because you have ensured via R do serial training that the features the distribution of the features of the source data is same as the distribution of the features of the target data


This thing is called domain adversarial training and it is shown to be a very very effective method in reducing the problems with unsupervised domain adaptation


Okay uh any questions on this method


Yeah locations

### Speaker 2

Sir is it necessary to back propagate through phi from H of the theta as well

### Speaker 1

Yes because otherwise what will happen No the features that have been learned okay may not be such that they are conducive for classification


So youll have to ensure that the classification also happens The classification on the source data has to happen

### Speaker 2

Cant that be captured by H of theta itself

### Speaker 1

H of theta is strain no you have to strain H of theta

### Speaker 2

Yeah yeah so during that training on the

### Speaker 1

No no it wasnt it your question you are saying just use the zs and try in h of theta separately is what you are saying z

### Speaker 2

Right right

### Speaker 1

Why do you have to try and feed together with HF data is that your question

### Speaker 2

Right right

### Speaker 1

See if you if you take a ZS separately and try an H of theta what will happen is the features that have been learned to ensure that these two distributions are same may not be useful for the classification for instance what can happen is


Suppose both of them for all x right or both of I mean the PGS and PGT are such that they give you one vector for all data points Lets say that they all collapse


So if that happens even then the distribution matches PCS and PGT matches if for all x it will give you one vector but that that is not useful for classification


Understood So the features that have been learned have to be such that they are useful for classification and thats why you have the classification objective also together while you are training it

### Speaker 2

The future


Okay

### Speaker 1

Uh stands it

### Speaker 4

Sir can you please explain once again this process like how we are training and like how we are doing these like taking the supervised classification and the discriminative part back propagation together

### Speaker 1

Help diminish


See first you take the source data pass it through this V network you get a feature ZS right And then you have then you take XCAP pass it through that network I mean you initialize this V network randomly you get ZT okay Now ZS become your ZS becomes your true data and ZT becomes your generated data and use those with a discriminator to adversarially backpropagate VZ through the


phi x network and ensure that the distribution of zs and zt are the same this is the usual GAN training


The only difference between a usual GAN training and this is that in a usual GAN right the real data is not passed through the network right Generator network You assume that its already there with you But here GS becomes your real data and GT becomes your generated data I use that to ensure use that with a discriminator to ensure that the distributions are same that is GAN training


Okay then you have another classifier which is trained together with the GAN where this classifier takes data from the source features and predicts the source labels and train it in a supervised way


Now the the the this phi network which is the feature extractor will be trained both using the adversarial objective and the supervised objective together so that it has to ensure that the distributions of source and target data matches while the classification also happens properly

### Speaker 4

so sir these X and X cap these are from the available input

### Speaker 1

I have defined it already I mean you should not forget See this is ds and dt are given So x is the samples from ds and x cap are samples from dt Theyre given


That is what is given now


Uh


What do you mean there is only

### Speaker 2

Perfect

### Speaker 1

Credible data only from the source

### Speaker 2

A generative model here I mean adds to this supervised learning because we could also directly train the H network over

### Speaker 1

But why would what yeah if you do that then what is the guarantee that the X if you suppose you train a classifier on X and pass X cap through it it will have a very bad performance

### Speaker 2

Like why would you

### Speaker 1

Because why is that

### Speaker 4

Why is that so

### Speaker 1

Because PS and PT are not the same no Distributions and PS and PS and PT are not the same Thats why I showed you that picture right Where you had the MNIST and the SVHN data


Right the distribution of PS and PT are not the same I should make maybe write it explicitly see here

### Speaker 4

They must be close enough right

### Speaker 1

will not be uh that is the problem with domain adaptation when the id assumption breaks right when the resource data is not equal to the target data the classifier trained on one will fail miserably on the other so you can you can

### Speaker 2

If you go back to the diagram right so does it mean


the fine the the fee network is actually uh extracting features which are common across distribution is that

### Speaker 1

yeah yeah it is ensure it is ensuring that the features are extracted in such a way that across both the distributions the features have uh features are same level see while pt right pt is or rather


And PS is not equal to PT right PGS is equal to PCT by construction that is the point

### Speaker 2

S thats what we are trying to identify which is the distribution which

### Speaker 4

overlapping between those two

### Speaker 1

We are not identifying that way So not that we should not say that there is there exists a distribution that overlaps We are trying to extract enforce features such a way that for both the distributions they match


Anything else


also called DAN okay Domain Network Serial Networks or DAN Powerful technique and it has See actually I wanted to include this as a part of assignment but I thought it will be too much So if anyone is interested you can try that out Take MNIST and the UPS dataset


samples also here this can be


This can be UPS data You train a classifier on MNIST and test it using UPS dataset you will see a drastic reduction in accuracy


Okay now and then you do this domain over serial networks and see the accuracy on the target data will increase considerably


Okay so thats about it yeah see the last thing


The Gansss


Time is too short and we have so many things to discuss


Its supposed to be uh


content for at least two courses if not more okay so the last thing that Ill talk about for GANS in GANs is this thing called the versus trains GANS okay


This is needed only for that FID thing otherwise we could have uh


that can we do it


Buses trains you know an optimal transport


W you guys


Okay so now you know that for the F divergence minimizers right


very unstable in practice so you have already seen that right the GAN training is its very difficult


Writing in Ghan is very difficult because


So this is something that you have seen right ganttiring is very difficult because of that saddle point problem that is there Okay that is one problem The question is question is


What makes turn training hard okay


So in in in this paper which is called was a strange again what they show is the following suppose


So you have uh what is the notation that we are using for that p x and p theta right suppose p x and p theta are such


Yes


supports okay


Dont overlap


Now I will explain what this means See px and p theta okay first of all px and p theta okay


are distributions


distributions over x right which is typically some d dimensional real space correct this is how it is now typically


Oh


distributions


Real data okay real data


Light is over


or a small subspace


So called as manifold


The ambient space Rd


explain what this means okay hold on


Here is what I mean Suppose you are generating or rather generating data like this Lets say that I toss a coin Okay And then if its head I will fill this pixel with one If its tail I will fill that pixel with zero


Do you understand what Im doing Im tossing a coin okay


Depending upon the outcome of that coin I will decide to fill this particular pixel Lets say that I have a grid of lets say 24 by 24 or 28 by 28 I think MNIST is 28 by 28 Now Ill fill these pixels 784 pixels like this I toss a coin If its head I will fill that pixel with 1 If its tail I will fill that pixel with 0


Okay the question is what is the probability or likelihood that this procedure will generate MNIST dataset


Do you see the question Do you understand the question


Okay so now can somebody tell me what is the probability of generating MNIST via this procedure


Yeah its really extremely low right Its actually called a typewriter monkey problem right Where say that you make a monkey sit on a typewriter and start typing randomly Now what is the likelihood that it will create a Hamlet right Or Shakespeares work What is the question Say that its very very low right I mean similarly getting a data set which is semantically meaningful like MNIST


doing this procedure random procedure is is very very low now this means that out of all possible images


binary images MNIST occupies a very very small space in 784 dimensional space


Do you see that


See this this example was to show that out of all possible points in 784 dimensional space MNIST occupies a tiny region That is what I have written here right distributions over real data lies on a very small subspace or manifold in the ambient space Rd


Does that make sense


So now what is the consequence of this the consequence of this is this implies


Does a high chance


supports supports meaning the points where the distributions are non zero okay that supports of


of px and p theta r


H and P theta are are not perfectly aligned


Right because we are talking about of two distributions right in RD And we know that distributions of images are actually supported on a very tiny space in RD So if I take two distributions that are in RD then their supports will not be perfectly aligned Okay theres a high chance of them being not perfectly aligned


Now again what is the consequence of this This is it can be shown that


We shall


one can always find


A perfect discriminator


screeminator


use that uh a DW network with 100 percent accuracy


Accuracy when


supports of


Theta and Px are not the same


So this is saying that okay now if the supports of px and p theta they do not align perfectly or are not exactly the same then you can always find a discriminator with 100 percent accuracy


Okay now if you find a discriminator with 100 percent accuracy what does this imply This implies that the GAN training


Thats it


The moment you you find the discriminator with 100 percent accuracy there is no signal to the generator to learn isnt it Because it is perfectly classifying thats all you are done right So GAN training simply saturates and this is the reason okay why GAN training becomes difficult So let me tell you what I said See the argument that is given is first thing is that the data that is lying I mean that that is that that


that occurs naturally like images and text and all that They occupy a tiny manifold or tiny little space in the ambient space Okay Now this means that the true data and the generated data okay they both lie on tiny manifolds and those tiny manifolds may not perfectly align


Now if they do not perfectly align even if there is a single point where there is misalignment then it can be shown that in such cases you can always find a discriminator that is perfect Now once you find a perfect discriminator then the gain training simply saturates So this can also be said in a different way saying that this means that for


P x and P theta


Misaligned supports


Misaligning supports


This align supports okay if you take any f divergence


This will this will be either infinity or some constant


Let me say its a constant


become a constant now it will what if it becomes constant does it become independent of theta it becomes independent of theta then thats all right i mean gant training simply saturates because the divergence youre calculating is independent of theta and there is no way that you can learn it learn more


This is why mode collapse also happens This happens all the time So the the respite or solution for this is solution for this is


Use a softer metric


Softer divergence metric


that


It quantifies


Close


Give me any full results


called support manuals are


supports of we are talking about p x and p theta okay instead


Instead of instead of


Measuring if they overlap or not


Theyre perfectly aligned or not okay


This is demotivation so what we are saying is


If the manifolds do not perfectly align then all the F divergences that we saw simply will max out or rather become a constant which will become independent of theta and thats why Ganttaring saturates Instead of that its better to have another metric a divergence metric that will tell you how close or far the manifolds on which distributions are supported are Instead of just making it a constant in fact whenever the manifold


do not align you want that metric that you are that you are thinking of


just measure how far or close the manifolds are without uh no just maxing out or becoming a constant so if this happens right what what we are saying is that you know you cant find a perfect discriminator and that is why the gan training does not saturate


Okay So we will see I mean this metric happens to be that metric is what is called as the versus stains metric


So called as the optimal transport


Ill define in a while Yeah before that before we go to the definitions Ill take questions on the discussion so far Any questions


Yes and it

### Speaker 4

Sir what what do we mean by the support here

### Speaker 1

If you take a distribution supports are the points on which distribution is non zero

### Speaker 4

Selling

### Speaker 1

Exactly


If you take a uniform distribution between lets say A and B support of distribution is set A B


on which the distribution is non zero


it all right so Gaussian distribution right will have infinite support for instance


Its a set okay its a set over which the data has been observed


Any other question


I got a window

### Speaker 4

Yeah so here we are only trying to say that if the supports match then they are close enough so we are not really looking at the divergence metric in addition

### Speaker 1

No in fact divergence


We we do compare distributions okay I mean we saw that right we actually compare distributions okay but the thing is


If the distributions the real I mean if the distribution that we are comparing will have a mismatch okay in terms of non alignment then what this paper says is that you can always find a perfect discriminator and thats why training becomes unstable


So you basically the motivation is that you need another alternative metric Okay That is not over dependent on alignment of the supports of these distributions

### Speaker 4

So I mean its in in in addition to uh the divergence minimization or this is a separate way to optimize

### Speaker 1

Uh see you minimize the divergence only Basically you minimize the divergence but the divergence metric that you are coming up with is not sensitive to a misalignment between supports Thats all


Okay so Wassersteins metric is also a divergence minimization metric only so so given two distributions


P x and P theta the bosons strain metric between them is defined as follows


keeping some details here because you know you wont have a lot of time so this is metric is given as the minimum


expectation of


They have the two norm and this expectation is over


X and X square they come from


new and this minimization is over all new okay which belongs to a joint distribution between px and p that I will explain all this


Give me a minute write that down and then explain


This is the definition of the Wassersteins distance Okay Okay Ill tell you what this means Now suppose there are two discrete distributions Okay


Ill do it in one dimensions to ensure that the idea is clear So lets say that this is X There is another distribution which is a histogram


x squared lets say that this is this is p x and this is p x cap or p theta


Okay now


The mass


in px px can be


redistributed


Whats that


It transforms


p theta do you agree


the mass in px can be redistributed okay such that it will transform to morph into p theta do you agree how do we do that


So its like this How do we do that We take lets say that this is this is x1 and this is some xk You take some mass from x x1 and


reduce it and put it to x2 and so on right i mean you can redistribute the mass in px so that it will get transformed to p theta isnt it do you agree

### Speaker 2

But usually we are not supposed to touch X right so its like a source distribution

### Speaker 1

No no no See forget about source and target and all that now Im just simply saying given two distributions you can always change the distribute mass in one distribution to get it marshed into some other distribution correct


Now the fingers


Now this redistribution


redistribution can be expressed


Can be expressed


as a table


Lets say that this has this has uh k and this is


X cap one two X cap


Okay now I will write a


Okay in this direction this is excel sorry x cap


in this direction it is


This is X one through XK and this is


Uh its one cap rule


Right So what Im saying is how much mass should I take from X1 and should I put it in lets say here So lets say that I put the 0 point 3 percent of X1 here and I put 0 point 2 percent of it and Ill write 0 point 01 percent of X1 here and then redistribute amongst all X1 cap through XL Same thing with X2 also right I take 0 point 1 percent and 0 point 4 percent and 0 point 02 percent and so on


Do you see that So what Im saying is every row here is telling me how much mass how should I redistribute 1x k okay amongst all possible x caps such that it will get transformed to


I mean p theta do you agree


And every row should sum to one right Because you can I mean the total mass on x1 should sum to one correct So now this right What is this If you closely look at it is actually a joint distribution


distribution between


P x n P theta


Shall I call it as PX cap


Its okay you understand now X cap is coming from uh P theta


Is this okay Px is sampled from P x is sampled from Px here and scap is sampled from P theta So this table okay which will tell you how to redistribute


to and px to get morphed into p theta is actually a joint distribution between px and p theta


Any questions so far


Yeah Amitosh write this down

### Speaker 2

Shouldnt it


just p theta so that it becomes equivalent to px or is it because

### Speaker 1

No no no its uh no no no See again Im saying telling forget about it for a while You you you forget what is p theta what is p h Theres two distributions Of course you can write it that way right I mean you say that p theta is being adjusted in GAN framework That is what youre trying to say right Yeah yeah In general doesnt matter No in general Im defining divergence metric between two distributions Can mean anything


That is why if its confusing for you let me


Change it


Theres more


find and replace here so you have to do it manually


Any other questions on this


So a joint distribution between


between px and p theta px cap now px cap okay specifies


Specifies a transport plan its called a transport plan


Transport plan okay


B X N B X Capp


Now if you give me a joint distribution between Px and P Px and Pxcap Im simply saying every joint distribution is telling me how to convert or redistribute masses in Px such that it gets mapped to Pxcap Do you agree


No


Suppose


Suppose now I move suppose a mass


X cap okay is or rather X is more


X is more to X cap


move to x gamma right then


Norm between x and x cap gives you the distance


movement


I am evaluate


The joint distribution at these points x current x gap you the mass


That wasnt work


Right This much of mass was moved this much of distance So now P xx graph which is the joint distribution between these two If you multiply this with this thing So what is distance times mass


Work done right


moving


You lost


y a distance of x minus x cap


Mass into distance is the work done right By definition Now if I take


integrate this okay over the entire joint distribution


What will this be for me


This is by definition the expectation of


Over the joint distribution of PXX cap What is this This is the


Average work done


in a transport plan


So fire by


You will agree


Now every joint distribution between x and x cap will give me a transport plan right which would tell me how to transform one distribution to the other correct


If I I mean uh if I multiply that if I take the expected value of uh the distance between uh the supports okay over the joint distribution it will tell me the average work done in a transport plan that is specified by the joint distribution


Everybody agree on this


Are you audible


Yes yes yes

### Speaker 2

Yes it will

### Speaker 1

Okay is this clear Okay Now the question that Im asking is


Give one


Multiple transport plans that are possible


Every transport plan is a joint distribution mind you right


and distributions okay possible


between two random variables X and X cap okay


Which one


has the least work done


In other words


In other words what is


What is the least work done


Who transform


PX2 PX cap


you specify this so now what you do is that if you take a joint distribution new okay


is a joint distribution between x and x cap okay this will give you the work done


via that joint distribution Now amongst all possible transport plans or the joint distribution that will take PX to PCAT give me the one


Y okay represents represents


set of all possible joint distributions between X and X cap


All possible


joint distributions or transport plans right


So every joint distribution is a transport plan


between x and x caps


So this is seeking what is this seeking this is seeking the least


I dont know


Transport plan


Least average work


You see this So Im saying amongst all possible joint distributions or amongst all possible ways that I can transform my PX to PX cap give me the one


That corresponds to the least work done


Do you agree do you see this


Oh


This is what is called as the versus trains distance


What is this distance between


distributions Px and Px cap


The minimum okay and please note the minimization is over minimization is over all possible transport plans okay that would transform PX to PX cap Now the question that Im asking is amongst the new is


joint distribution between


You belong to


Set pi okay is a joint distribution


Excellent


Now amongst all possible joint distributions that would transform Px to Px cap give me the one that has the least work done So that is the Vortzestrauns distance Now you can see that


lesser the versus strains distance okay


Closer R PX and PCAP isnt it


Because if PX and PX cap are close then the amount of work that you should do to bring PX to PX cap will be least Now there can be other transport plans that would I mean even if PX and PX cap are close there can exist transport plans that would have a that would that would involve a lot of work But since we are seeking the minimum work done to transform PX to PX cap if they are close enough


then you dont have to do a lot of work to transform Px to Px cap


Thats why its a distance metric between two distributions


So this is also called thats why its also called no optimal transport Wassersteins metric is also called as optimal transport


Any questions on the definition


Is there any question

### Speaker 4

Not those

### Speaker 1

My art is good


Okay great Okay so now this is shown to be a softer metric right So versus change distance is a softer metric okay compared to


Compared to F divergence


in the sense that


It will not


to max out right or saturate


Accurate


But misaligning okay what does D


alignment of the supports this is the greatest thing right i mean that you can use the versus strength metric uh to i mean it will become much stabler if you use versus strength metric now how is this related to adversarial learning is that so the next question is


Continue the class till 11 15 right and then we will take a 10 minutes break okay lets finish this the question is


how to build a generative model


optimizes the versus change metric okay this is a good metric fine now how do we build a generative model that would


optimizes the versus strength metric


So thankfully there exists this duality okay which is called the Kontrovich Rubinsteins duality


That says that versus strains distance between two distributions Px and P theta okay can be expressed as a maximum okay


set of functions lets call them STW


are like this Ill tell you what this is so this is


expectation


X coming from BX


Simply dw of x


expectation of


Its cap coming from b theta


have again dw of x


So now you know right I mean this so now if you want to minimize


in theta just simply you have a min


Over the tea table


And worst case in the sense is simply a max over this T w Ill tell you what this norm of T w less than this means And you have this usual


Classroom


We know how to approximate using sample estimates


Its got so its got


from BT


Right so now this what is this again this becomes this became a a dosedial optimization


How do you optimize this same thing you have


Generator network


Take get take a Z


and gives you X cap coming from P theta the usual story and you have this critique network here


W of X


your real number in this case and this is


Either X or you have X cap that goes as input because you can you have to compute the expectation over both of that


And then the only constraint is that the T network right have to be one lipshitz


So what is meant by that I will just tell you


implies that if you take T w of x 1 minus T w of x 2


divided by x1 minus x2 this is upper bounded by 1 this is the definition of 1 lipschitz so i mean if you look at it it is exactly a gann right optimizing the versus trains distance is exactly a gann thats why its called a w gann the only thing is the discriminator network right or the critique network have to be 1 lipschitz


Of course the the uh the


form of the uh the uh loss function changes a little because there you have the expectation of f star of tw here you dont have that f function right otherwise it is simply a an adversarial optimization problem that you are solving right but with only one additional constraint that the discriminator network have to have bounded derivatives right or it should be one lipschitz now how do you make a neural network one lipschitz is a question that ill answer in a while


But yeah so but for that it is simply again with


uh with with the objective function taking expectations over two distributions and then you optimize the advantages in a jan right what happens is or an f divergence minimizer this maximization that you are constructing no is actually a lower bound on the divergence but here there is an equality you see the versus strength metric is exactly equal to this maximization problem which is again no thats what makes it a softer metric


Now the practical implication of this is whenever you are implementing a GAN right always implement a WGAN because it is much more stable in terms of training Okay Even for your assignment no question one and two I would recommend that you implement a WGAN So now how does it change The only thing that will change is this will not be between zero and one now It will simply you will have a linear activation at the output


Linear activation okay


The loss function will not have a log of D of G or something It will simply have the output of this It will be expectation of the output of this So this will be a this is the output of this network Okay Thats one thing The other thing is youll have to ensure that the discriminator network is lipshitz So now to practically


What you do is that you


Normalize


Wait


of TW


Such that their norm is always


If you do this then it will become one lipstick So what you should do is after every gradient step right


after every ingredient


every gradient update So after every gradient update what you do is take the weights update take the weights of the discriminator network and normalize them so that they will have


unit norm if you do that you become one likelihood thats all that is the only thing that you should do while you are training the bus a strain scan and this is shown to be much more stabler for training and it it will give you much better uh uh like outcomes compared to f divergence minimization even though this also happens to be a saddle point on adversarial optimization okay with the only constraint that you should have the discriminator to be one likelihood


Thats about WGANs Any questions on this


Yes go on

### Speaker 4

So the norm that we are talking about here is the

### Speaker 2

I dont know or

### Speaker 1

Here yeah yeah this is L2 this is L2 this is L2 yeah


good that you asked that question right here when we define the versus stains metric its always uh two that we talk about here right the two norm between x and x cap okay and the the this duality you know the control which rubinsteins duality is for versus stains two in general you can use a pth norm here if you do one norm here that will become versus stains one if you if you use two norm it will become versus stains two if you use p norm it will become p versus stains distance in general but generally


Wassersteins two is what is used everywhere and the duality rate or the GAN formulation comes up for Wassersteins two


Tall drinks


The water stains too


Yeah service


for calculating the norm of the network we just have to take put all the weights in a vector in any order and then just calculate the norm yeah yeah yeah yeah simply vectorize it compute the norm and divide it by the norm of it you dont have to compute it no just divide the weights every individual weight which with its norm

### Speaker 2

It works for every network and convolution also same

### Speaker 1

Yeah yeah same thing same thing yeah yeah


Okay nothing else right I mean this see whenever you implement a GAN always implement a WGAN much more stable


Okay the final piece before we close Gyanus like how do you evaluate


generate generate if or evaluate GANs right typically


This is uh I should not be calling it as GANs you can do it for any generative model


Now given


X1 through XN


For example from some distribution px typically the real data


And you have


On cap true


Excellent


Its a sample from p theta star this like the generated data post training of course right


Now the goal


Compare the closeness


Its called this as uh


T real and T generated okay compare DR and DG Now how do you compare these two You need a metric to compare these two Of course now you need to resort to some distributional divergence metric only to compare DR and DG What is done is typically there are multiple metrics to do it One of the famous metrics is what is called as the threshold inception distance


Squared


Abbreviated as FID


have seen no fid is the metric that is used to evaluate the quality of generated data so what is this at the heart of it fid


is simply versus strains metric okay


simply was a distance metric between uh uh like px cap and p theta cap but it is done in a convoluted way ill tell you what what is done what is done in f fids


Positive this


Um pull this off


DR and DG


Ill pass them through


them to an inception network a pre trained infection infection inception


Through an inception net thats why the name inception distance okay inception network


Retrained


Can you imagine it


then take


features


from some nth layer some different people take it uh different layers I think you know example is 64th layer


Now what was done so far is that you have a pre trained inception network


Now you pass your x and x cap both through this and take the features at some 64th layer right This is you call this as z real and you know z generated


Okay then now you will have two data sets right Lets call that as D


cap real which is


zero real one zero real two up to zero real n and you have d


generated cap which is C generated 1 C generated 2 and C generated the n so here Z R


Lets call this as some fee okay so now fee at 64th layer of


Z I


And ZGI is fee at 64


x cap i okay where phi is d


Is the pre trained inception net okay


So far so good Any questions on this


Given data real data and generated data take a pre trained inception network okay Pass both of them through that and take the 64th layer features of both of them and collect them as vectors You get two sets Is this okay so far


Okay now what you do is this is the third step the fourth step is that


Compute


mean and variance okay for


DR cap and DD cap


Lets call this as mu real


and sigma real


Compute mu real on z real You compute sigma real on z real You compute mu generated on z generated Compute sigma generated on mu generated Is that okay


The first step was


Assume assume


Z real and Z generated both to be coming from Gaussian distributions


Now Z real comes from Gaussian with mu real and sigma real and Zg comes from a Gaussian from mu g and sigma g


Then finally you compute the Versus Training metric


Between the normal distribution at mu rian sigma rian


This is FID


is clear how to do it


Now Ill tell you this is this actually is given by a formula


Wassersteins distance between two Gaussian distributions is given by the simple formula L minus mu g


2 squared plus the trace of


Sigma real plus sigma generated dash minus 2 sigma real sigma generated dash to the power of half


See this is a scalar because its a norm


And this is a trace no trace of a matrix is also a scalar Okay And therefore this is the FID which will be a scalar


So this was a strength two metric no scalar uh so this is lower the better


distributions match then it will be zero because it is was a strange distance between two Gaussian distribution better not between


Let me show you the entire procedure


a look at it okay and let me know if you have questions on fid so this is the metric that is used to one of the metrics that is used to uh quantify the goodness of generated data and beat from gans or vaes or anything you can compute fid so what is fid let me take quickly go through the steps now


Now you have samples from the generated and the real data pass it through a pre trained inception network to get the features I mean Im not sure if its 64th layer or something Ill some people different people use different layers anyway Okay So now once you get those features assume that those features follow Gaussian distribution and compute the mean and variances of them and use those mean and variances to compute the versus


two metric between these two features of real data and generated data using this formula that is your FID


Any questions on the computation of FID


asked you to compute FID right on the the data that you generate using GANS so this is the formula that you should implement there are standard implementations of FID as well yeah but this is what they do okay survey


So what is sigma g prime


Oh sorry this thing wont be on here yeah


Have a look

### Speaker 4

So I have two questions one is why why did you place so much of importance on one particular inception architecture

### Speaker 1

I didnt I mean somebody did because if you read the FID paper what they say is inception architecture correlates well with human perception is what they have done by doing some perception studies

### Speaker 2

Okay okay Okay Second question is

### Speaker 4

Suppose I I am modifying the problem a little bit and I ask uh like I want to see the inception I mean the uh the distance between uh generated images uh of a given style like if Im not going to

### Speaker 1

focus on content at all and I just want to focus on style so can I modify the uh just I mean picking up the 64th layer feature vectors and instead replace them with


maybe the gram matrix or the add in layer activations I mean and continue with the same procedure will I get a meaningful result

### Speaker 2

It is not FID but yeah so it is something right I mean you might get some meaningful result but its not FID by definition thats why You cant say that its the standard FID metric

### Speaker 1

It does that for me

### Speaker 2

It does make sense

### Speaker 1

Okay fine I mean the actual problem is I want to recommend images to

### Speaker 2

Uh yeah I I so shall we take it offline because this may not be relevant to the class

### Speaker 1

I


Yes yes yes

### Speaker 2

Please swing me know we can discuss all that Okay Any other question on FID Okay So this is the


End of GANs for this course I mean there are too many things that are there Yeah this is the end of generative adversarial networks Its more on to VAEs Yeah so


Okay so we come to the end of GANs then so lets move on to the next topic which is variational autoencoders Shall we take a break


Uh okay so how long uh 11 18 shall we come back at uh yes and deep


I think yeah so well come back at 11 35


And go up to 1220 perhaps and then well stop 1135 okay 15 minutes


Okay see you in a while bye


Hello should we resume

### Speaker 1

Yes sir

### Speaker 2

The next class of generative models that we would consider are these variational autoencoders or VAEs Now these come under a broad family of models called


Latent variable models


latent variable models so what do you mean by latent variable model is that you have theta


what our starting point is right


on as usual IED from an unknown distribution px okay


Suppose p theta of x denotes a model What is a model Model is basically a distribution over theta right Suppose p theta


Denotes


A morden


Latent variable model is the following


defined as follows p theta of x


given as a marginal


or the joint distribution of the data and another variable Z where Z is another


Is it this


is a hidden so Id name latent variable okay hidden or unobserved


An object


random variable


Or this is integral


If its continuous okay if z is discrete


Where to move that anyway


Um I actually wanted lets do that


Okay so this if


Z is discrete


C is continuous


Now where Z is hidden


or unobserved random variable


So this is the definition of a latent variable model where you express your data in terms of


marginal okay over the joint distribution of


Joint distribution between the data and one other unobserved random variable


So typically give you examples of what this is typically


Typically Z


C is also estimated


or learned


along with the model parameters theta


Okay so basically what we are saying is for


each xi in data can there exists a zi okay correspond corresponding to xi


So that is unobserved


Now this ZI examples what is


Z is discrete okay


Lets say that z


is discrete and it is


take lets say one two


0 to like m values lets say 1 to m values


values


Given an X I


belonging to D okay Zi given this X Xi


may indicate


Indicate


Indicates


Ill see that I didnt see


zi comma xi plus test plus test


xi into


M categories


You understand so in this sense right a Gaussian mixture model


of which the K means clustering is a


special case okay are both latent variable models


Any questions on this


So basically what we are saying is the following right Given data what we do is that we model our data this way which is a marginal over the joint distribution of the data and another random variable called Z Okay Now what is this Z This Z is a latent variable or an unobserved random variable that is not with data that is not actually measured or seen with the data but it is there with the data


Okay now what is the advantage of having this sort of a modeling is there are multiple reasons One having a latent variable model will like will enable will enable model learning Okay easy easier make it easier In the case of Gaussian mixture model it will make it easier algebraically easier That is one reason The other reason is if you have a latent variable model you can actually get information like this which is given a particular


X i after training right if you estimate the corresponding latent variable it will tell you if its discrete it will tell you what cluster every X i belongs to so that is the that is the classical example of k means clustering and Gaussian GMM clustering where they are both latent variable models which will tell you for every X i it will tell you what cluster X i belongs to the second example can be okay the first example second example is Z is continuous


It is actually an autoencoder or a VAE also


But


Zi given an xi okay can be seen as


your z then some rk its a continuous vector can be seen as seen as


Teacher


Corresponding to it so latent variable models right will enable feature extraction


You can use zi rather than xi for downstream tasks and all that So these are called I mean these are feature extractors So thats why you want to model the data xi by introducing one other random variable zi which is called the latent variable Any questions on this motivation

### Speaker 4

for the continuous case we are saying that zi by xi can be seen as a feature for

### Speaker 2

Or not by not by z i given x i its a conditional random variable conditional distribution


ZI Z1XI

### Speaker 4

Sorry sorry for that zi given xi can be seen as a feature corresponding to zi

### Speaker 2

Corresponding to sorry corresponding to Xi

### Speaker 1

So the feature should be useful in some way right

### Speaker 2

Correct correct they it will be useful in some way thats the point


Latent variable models are imposed because features are useful in some way


Thats what Im saying so now the


In the literature these latent variable models are designed in such a way that you learn the latent variable and the model parameters together


Alright


In auto see in GANs right what did we learn we basically learn the model okay but in in in latent variable models learn the model okay but you will also learn the the latent variable together


Its on right


Okay shall we do one


Now lets look at


Cant I draw straight lines here in this thing Is there a way to do it


long press in good notes right a long press would make it a straight line here i dont know how i have to go insert line and all that thats too much

### Speaker 1

No sir that is in the draw itself


End of words off

### Speaker 2

In the woods are

### Speaker 1

These symbols are there octopencils there are one round and one square that is giving you yes

### Speaker 2

Great I will have to do this huh Okay fine

### Speaker 1

It will disturb you

### Speaker 2

Okay so this will convert into regular figures huh


Okay lets not complicate stuff maybe I will use a line and do it okay fine so now uh


Modeling


Yeah different variable models


Okay so recall so suppose


Boss


Ethiopia


Yes Ill for now use assume that the latent variables are continuous and this is my model


Different variable model


Now again the same thing right so goal


Do you want


D


The car samples


I did samples from VX I need to


estimate


theta okay such that some divergence metric


For for VA right the divergence metric that is taken as the KL okay


Min waste


That those are good


So we need theta star


Thats the minimum you can set off


E e tail between


X and E theta


Recall that this is equal to


The maximum is a rough


expected long life


Do you remember this


We had done this right


Thats all of you remember this

### Speaker 4

Minimizing KL divergence is same as maximizing log likelihood

### Speaker 2

Yeah expected log likelihood right


Maximize G law like you know okay this is what it is So lets


right that we are interested in in maximizing the


likelihood function so ill remove the expectation because uh if you maximize the likelihood for all x the expectation will also be maximized right so thats because just to make the algebra easier i mean the final loss function and everything will have an outer expectation with respect to px which will have a sum over all samples in px okay let us uh remove that to make life a little easier so our objective is to maximize the log of the likelihood under


Model p theta Okay so denote


log p theta of x


theta lets call that l theta now our objective is to maximize l theta okay now how do we do that under related variable model we have l theta is now equal to log


ETI topics


Now under the latent variable model


Integral


E theta X


Please let me know if uh uh if if any one of these steps are not uh clear to you okay


Okay this is because


latent variable models my p theta is the marginal over these two right that is why it is


equal to this


No


This is equal to log of


E theta X and C times


given x


divided by Q for C D one X


So that I can continue


E or Z given X is some distribution


over z so q of z given x is q of z given x is some distribution over the latent variable right you take any distribution over latent variable right you can just multiply and divide


Divide by that okay and the integral doesnt change Is this all right


use some distribution over the latent variable is is this okay


It can be any arbitrary distribution doesnt matter Okay Now this is


Logo


expectation of


You do the sensei


divided by Q J given X with respect to Q


Is that is that alright


definition


And what have I done just grouped this together


and taken this as a function and written that integral as the expectation over z is that okay


Now theres something called Jensens inequality


It says


Log of expectation


As always


less than or equal to expectation of


Log off


function


Does everybody has everybody heard of instance inequality or not

### Speaker 4

Yes sir

### Speaker 2

If not right maybe we can take it in the TA session Okay just look into it now So using that what we can do is so we have now L theta which is our log likelihood that we would want to maximize is equal to log of expectation of this entire thing with respect to Q Now I can write that as something that is less than or equal to


greater than or equal to


This is equal greater than or equal to


the expectation of


Log off


functions

### Speaker 4

are less than equal to based on the previous expression

### Speaker 2

a log is less than or equal to that expectation of log

### Speaker 4

Yes sir

### Speaker 2

So uh this is this is log so this is less than that is less than expectation of log correct no log is less than expectation of log should be correct no

### Speaker 4

Ill send it

### Speaker 2

That should be other way around

### Speaker 4

That should be another way around

### Speaker 2

Okay so this is


I think that its correct now right

### Speaker 4

No sir I am I dont remember the inequality sign correctly but

### Speaker 2

No no no thats okay But with this inequality whatever I have written is correct No see I know for a fact that this is right So we have to change the Jensens inequality accordingly Okay so See Jensens inequality becomes an upper bound or a lower bound depending upon this function If this function is concave then it is one it is convex it is something else So sometimes I get confused about it This is correct right So just tell me that if its greater than or equal to here this will become greater than or equal to here correct


So then then change in equality is correct Okay Right So now this is greater than or equal to what what do we have here Its an integral


for C we have Q of C given X


times log of


E three TOS


So can you see do I need to


Youll see you get an XD set okay


Of this


lit


the entire thing right


Note that this is a function of two things right its a function of


theta obviously its also a function of q distribution that we have chosen isnt it Depending upon what q we choose here when we started right with some distribution over z so you will get a different uh lower bound on the likelihood correct


Now this implies what did we do so far is that by introducing a latent variable model and a distribution over it we showed that the function which is the log likelihood that we would want to maximize is


lower bounded by


some function which is a function of the model parameters and a distribution over latent variable So now this Q which is a distribution conditional distribution over Z is referred to as the variational posterior


Variational latent posterior thats why the name VAE okay


What is that Its a distribution over Z okay and this F theta is also called as the evidence


A lot of bones


Its a lower bound okay on log likelihood okay Log likelihood is also called as


evidence I mean its another name for that no So you want to in all models you want to maximize the evidence under the model p theta So now you have constructed a lower bound on the evidence okay based on a variational latent posterior and this is abbreviated as ELBO


Is this clear


Now what we need is we need to remember that we wanted to find a theta that would maximize the evidence or the log likelihood okay now this is equivalently


maximizing the lower bound on the evidence you know because in latent variable models no maximizing the evidence will become difficult just like we did it with the f divergence right minimizing f divergence directly was not feasible we constructed a lower bound on it similarly on the evidence we are constructing a lower bound okay now this maximization now is not only with respect to theta it is also with respect to q right so as i said you need to find two things one you need to find the q that would construct a


a lower bound on the log likelihood that you would want to maximize and you also want to find the theta that are model parameters


Is that all right So you need to find a theta star and the q star okay that would maximize the lower bound that we have constructed on the


So what is that lower bound lower bound is the expectation of log of


ETE


given by you have to give one x with respect to


This


This is a very important result okay that is used in all latent variable models I mean this is the framework for latent variable models So basically you find out the model parameters theta and also the latent variable parameters q okay such that the lower bound that you have constructed on the likelihood function is maximized


questions on this See note that there are two optimization problems here right one optimization problem is over theta okay which are the model parameters the other optimization problem is over q which is a functional approximation problem right


Its not a its not over parameters it is over class of functions


Is this alright


An example for this is


Ill come to use it Example for this is what is called a Gaussian mixture model or a GMM


Ill not go into the details of GMM okay But just tell you what p theta of x is as usual a latent variable model which is


where p theta of x and z is given by


Maybe I can try it uh


Well then write it this way only


See okay you have alpha Zs the normal distribution


So this is a GLMM right its a p theta is a linear combination of multiple Gaussian distributions


Okay so there are okay let me write it z equal to 1 through m so its a discrete model right Yeah so there are m Gaussian distributions and your model is a combination of m Gaussian distributions Now theta okay will be set of m alphas alpha 1 through alpha m okay And for every Gaussian you have one mean vector so you have m such mean vectors and you have m sigma vectors


that is your parameters that you would want to estimate in a GMM How is it done It is exactly done by solving this optimization problem no which is theta star and q star Okay So the way it is done is


Alternatively


Sulfur


theta star and q star Here you need to solve an optimization problem with respect to both theta star and q star right In a GMM you alternatively get q and theta star Now what can be shown as the optimal q star okay


which would maximize the


The elbow


Can be shown to be equal to simply the posterior


distribution thats all


So now maybe you can take this as a homework or make it in a T session So the optimal Q distribution right that would


For this right here


we constructed the lower bound right the optimal q that would maximize this lower bound by the way can somebody tell me this what would be the value of the lower bound with an optimal q


With the optimal Q what would be the value of the lower bound width


star okay


f theta of q star will be what See what is the maximum value of f theta cube


Am I audible

### Speaker 1

Yes

### Speaker 2

Didnt you understand my question


question is Ive created a lower bound on the likelihood function no L theta okay Ive denoted that as f theta cube what would be the maximum value of this


What is the maximum value that this lower bound can achieve

### Speaker 1

Love you too

### Speaker 2

L theta right


Because its a lower bound on L theta the maximum value that it can achieve is L theta isnt it


Do you see that or not

### Speaker 1

Yes so the maximum lower bound will equal L three times

### Speaker 2

Exactly right so the maximum load bound at that point will be simply equal to L theta


Okay so what Im saying is it can be theoretically shown that the optimal Q distribution is equal to P theta of G given X and for that Q theta okay with that Q star the lower bound that we have constructed is equal to the likelihood value


Okay now once you have gotten an optimal lower bound what you do is which


That Q star okay


Find the next


Next to best


theta so now lets call this alternatively solve for theta star and q star rate so lets say that we have taken that as theta t okay now q star at t plus 1


iteration t plus 1 is simply equal to the posterior at theta So f theta that we have gotten is equal to L theta at that stage So with that q star at t plus 1 okay you find the next best theta t plus 1 How do you do that Theta t plus 1 is simply the arg max of


that you have computed with q t plus one


as a function of theta thats all and you keep alternating between these two so you find that theta okay with q being equal to p theta of z given x at the previous time and you use that


to find your next cue and keep alternating between them


Is this all right Did you understand this The only thing that I have not done is I have not told you that y is the optimal q equal to p theta of z given x right So that is something that you can take it as a homework or just show that okay But yeah so it is there in my notes also I mean its given in the first lecture of my handwritten notes Have a look at it okay Lets see This is like


of note


have a look at it but yeah so now basically what we are doing is we are we are so remember this right what we want to do is we wanted to maximize the likelihood instead of that we constructed a lower bound and that and then we would we we started maximizing the lower bound and that lower bound depends on two things theta and q right and we would alternatively optimize between this theta and q one example is a gmm where you first fix a theta


and find this q to be this posterior okay and for a gmm how do you find this posterior this can be found out analytically now ill tell you so p theta of z given x in the case of a gmm is given by p theta of x given z times p z okay divided by p theta z sum of this thing right


z this is the definition now what is this equal to p theta of x given z for a gmm this actually means


g is equal to one particular j okay lets say p theta of g equal to j and this is z equal to j to m okay now what is this equal to the numerator for a given j gmm is simply that particular gaussian


And this is equal to alpha j


yeah alpha j and this is simply the sum of c equal to


No sorry j equal to one two m


g a equal to 1 to m


We have a Gaussian here


mu j sigma j times alpha j This can be found out Once you find this out what you do is simply plug that into the lower bound and then maximize that with respect to theta You get the new theta use that new theta to evaluate this again and keep alternating between those two steps


Theres a name for this algorithm do you know


Does anybody know

### Speaker 1

Expectation expectation maximization

### Speaker 3

Expectation expectation

### Speaker 2

This is the EM algorithm right This is the expectation maximization algorithm This is how you fit a GMM to some data no


EM algorithm See I wont go to showing why EM algorithm is correct and all that Okay that I will skip But basically this is I gave this as an example Im running through it quickly because we are interested in looking at VAEs not GMMs But yeah so basically the idea is that this will be common across GMMs and VAEs all latent variable models right where construct a lower bound on the likelihood and then find the variational distance


and the model parameters but through alternative optimizations that would be same across GMM and this thing


Now uh in a in in fact in fact uh does all of you know about k means algorithm k means clustering


K means clustering is exactly EM So what do you do in K means clustering Given data you randomly assign K clusters right and you assign each of those each of the data points to a particular cluster right That is the step evaluating this that is this particular step


evaluating your making your posterior equal to p theta of z given x is actually the assignment step okay once you assign you recalculate the means right recalculating the means is this step this uh finding out that theta in fact what can be shown is that k means clustering is a special case of gmm where the where the variance of those component gaussians are infinitesimally small that can be theoretically proved anyway uh thats a different matter but basically uh


the take home message is that for latent variable models to optimize what you do is that you construct a lower bound on the likelihood function that you would want to maximize okay and then you alternate you estimate both the model parameters and the uh the variational distribution q together okay that is the take home message now for models like gmm right you know that the optimal


Q is P theta of G given X okay and for GMM that can be computed because there is an analytical form The question is we have theta star and Q star to be the maximizers


We want maximizes with respect to both theta and q and we want to maximize the lower bound that we have constructed correct Now q star is known to be p theta of z given x correct However however


What if what if


E theta of z given x cannot be computed


See if P theta of z gamma x cannot be computed how do you solve the elbow optimization problem is the question


Does that make sense


For GMMs P theta of Z gamma X can be computed Thats why you can do EM If you cannot compute P theta of Z gamma X how do you solve elbow optimization is the question that is asked in the VAE paper


That is our preface Now we want so now the goal goal is to


is to estimate


the parameters of a latent variable variable model


Offer


10 variable model


For which For which


the posterior p theta of g given x okay


And we compute it


This is our starting point In fact the state of the art generative models which are diffusion models are also special cases of


of uh uh v i s okay so its very important that we understand what v i s are okay so this is the prelude or preface of why uh do we need another model okay when there were latent variable models like gmm it is because while all latent variable models seek to uh maximize the lower bound on the likelihood uh with respect to model parameters and distribution over z uh simpler models


like GMMs have this advantage that the optimal Q which is the p theta of z given x can be computed analytically but if there are models for which p theta of z given x cannot be computed analytically how do you solve for how do you estimate the model parameters for latent variable models is the question


Is this is the story clear so far


So with this right I ask I mean I request all of you to read the first and the second chapter of my handwritten notes before coming to the next class Okay So with this preface and if this preface and prelude is strong we can quickly go to like how VAE solves I mean VAE actually solves this problem by approximating the variational posterior using a neural network and all that which we will see in the next class So please read my


entered on notes first lecture and second lecture and come prepared for next class okay


Stop here and take questions if there are any Vivek

### Speaker 1

So initially felt like I understood but there are many things like so why we used Jensens inequality like why didnt why do we settle for a lower bound actually

### Speaker 2

Now because the log likelihood cannot be computed for latent variable models like GMMs right what happens is see how do we do maximization So if you start with the log likelihood lets say right


Let me show that


So now log of p theta of x in the case of GMM will be log of sigma


alpha j okay and you have x here and this is mu j and sigma j correct is over js

### Speaker 1

You are guess

### Speaker 2

Now this is sum of alpha j into e power x squared minus mu j squared so on right


See yes there was sum of C on differentiate this with respect to mu and sigma and put it to 0 to maximize this right

### Speaker 1

Yes

### Speaker 2

Now if there were a sum of log term then this log and e power exponentiation would cancel each other and you can differentiate But because you have a log of sum terms


because you have a log of sum terms here If you differentiate this you will not get mu js in one side and you will not get a tractable equation in terms of mu So you cannot maximize this

### Speaker 1

Okay the summation of uh I mean the log of the summation of

### Speaker 2

Multiple exponentiation a multiple Gaussian distributions if you differentiate that with respect to one mu it will not get separated out

### Speaker 1

Yes

### Speaker 2

Right so now you need to do something to ensure that this is maximized So now to maximize that one way to do it is construct a lower bound And if you construct the lower bound EM becomes easier It is one of the motivations of why do you need to construct lower bounds on log likelihood


The other thing is again similar thing you know log of integral of p theta of x and z right for z This is the model Now if you do not know how to integrate this with respect to z because you dont know this distribution how do you differentiate this with respect to theta You cant do that You need another method to optimize for the log likelihood no Thats why you construct a lower bound and then you optimize for it See just you remember why we constructed lower bound on it divergences right


Because we could not compute the F divergence step because it involved integrals What we did was we expressed that in terms of expectations that we could compute and then simply used sample estimates to optimize for it right

### Speaker 1

Yes exactly same

### Speaker 2

Exactly same thing here exactly same thing And you remember that maximizing this is again minimizing the KL divergence Ultimately we are minimizing the KL divergence And to minimize this this involves integrals with respect to px and p theta which we cannot compute And thats why we are computing lower bounds and expressing it in terms of expectations that can be estimated using the sample averages


Thats the fundamental idea okay


Uh have a look

### Speaker 1

Yeah sir My question is related to the midterm exam So the syllabus for it is till the next class or todays class or any any specification regarding

### Speaker 2

Till the next class yeah there will be one more class before the exam it will be till that

### Speaker 1

Okay and uh I mean just to get some idea on the question so shall we be expecting coding questions or mostly no there will not

### Speaker 2

No no there will not be any coding questions it will all be theoretical So just follow whatever has been said in the class and also the TA session works

### Speaker 1

So yes sir I got I got my answers

### Speaker 4

So yes sir


Yes Im going to share So I have a quick question sir we read about this model now we understood also exactly how it works internally So uh

### Speaker 1

For practical uses like where all we can use like image generations or data

### Speaker 2

Hold on I really youve just started VAEs right Theres two full lectures that will be that will be kept for this where I can talk about all kinds of applications how it is used for generative models everything will be covered

### Speaker 1

Okay sir okay that is planned okay I was just asking that thanks

### Speaker 2

Of course right I mean just like we did for Gans we are just starting it theres a lot that we need to do

### Speaker 4

Sure sure

### Speaker 2

Completely preface okay anything else


Yeah uh go on if you were told

### Speaker 1

So in the

### Speaker 4

Im just curious to ask like since you said there is no report to be submitted what all things we have tried we can simply add it in the markdown right because in order to get any valid result too many things are being tried out from my end so just want to know

### Speaker 2

Come again what is the question

### Speaker 4

like uh so far I was trying assignment questions so its not coming directly in the first step itself like a lot of things are being tried out here and there so we cant just put everything in the notebook

### Speaker 2

No no you can you can yeah mark those statements and every experiment that you you know try you know just comment it out and put your observations that will be appreciated

### Speaker 3

The problem is sir if you are looking for the outputs of those experiments right

### Speaker 2

No no no I dont I dont whatever experiments that you uh that you uh tried no just uh document them okay

### Speaker 3

Thank you

### Speaker 4

For assignment like you said we should use Google Colab for compute but uh theres no free GPU available so Im using my companys GPU and Ill put that

### Speaker 2

And thats okay thats okay it doesnt matter


collab if only if uh like you know people dont happen go on you can speak you dont have to raise your hands classes are done yeah

### Speaker 1

Yeah also one question regarding the background reading material So is it okay to read that the Machine Learning Advanced Topics by Murphy

### Speaker 2

Murphy nope its one of the best books yeah its its not an its actually a very good book yeah you can use Murphy

### Speaker 1

Is it putting


Okay only the portions related to generative

### Speaker 2

Whatever we have see

### Speaker 1

Yeah its a video Ive never seen a video like that

### Speaker 2

Whatever Ive taught in class is what your syllabus is nothing less nothing more


Anything that is related to things that I have taught in class is all that I am going to ask I dont assume you to know anything that is beyond whatever I have taught in class and also in TA sessions


Thats all Okay uh if thats all it is lets uh meet next week okay

### Speaker 1

Thank you

### Speaker 2

Thank you
