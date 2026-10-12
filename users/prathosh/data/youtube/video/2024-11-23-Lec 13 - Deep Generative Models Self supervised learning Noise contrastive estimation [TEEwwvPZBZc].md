---
id: TEEwwvPZBZc
title: Lec 13 - Deep Generative Models Self supervised learning Noise contrastive
  estimation
url: https://www.youtube.com/watch?v=TEEwwvPZBZc
date: '2024-11-23'
duration: 02:37:56
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 13 - Deep Generative Models Self supervised learning Noise contrastive

## Transcript


### Speaker 1

See well its not opening calendar CCC exam and


Course grade entry 311 to 1812 IC


which means that we can do the assignment by us after your exam will that be okay for you


First week of December

### Speaker 2

Yes sir

### Speaker 1

Okay let us do it then then what we can do is after the final exam is done on 30th the first week of December we will do because 12th is when I need to submit the grade sorry 18th is the last date for me to submit the grades so Ill have enough time to consolidate and discuss and all that oh no no no this is 2023 Im sorry Im sorry I need to look at 2024 calendar


Just a second ah sorry sorry this is my mistake

### Speaker 3

I think it is twelfth sir

### Speaker 1

Twelfth of December ah how do you know

### Speaker 3

I think in reinforcement learning salaried nagars are told that 12th is the final date to put grades we have a project pending there in reinforcement learning also

### Speaker 1

Okay okay so there is this link its not opening yeah


Yeah I am just opening hold on yeah


Course grade entry 13 12 2024 is the last date Yes Yeah Okay 13th is the last date Even then I think


Its enough for me if I have one week So yeah let us do it on the week of 2nd December 2nd to 6th December is there no We will do it Well do the Vaibhavan Okay I think that is okay


Okay so then thats it yeah I think Ill continue with the class

### Speaker 4

So what is the format of the VIVA exam going to be I mean how much time is that going to take and what will be the schedule

### Speaker 1

I we will let you know all of that


See Im thinking of uh like uh about uh 20 minutes per group uh or rather half an hour per group


And we have 20 groups no We are like three of us four of us three TAs and myself We will make five groups per instructor and we will spend half an hour with each of the groups and then we will evaluate That is the scheme that Im thinking Schedule I will let you know okay Maybe late evenings or weekend something we will make so that it is beneficial for all


That that you can adjust no problem yeah whatever works for you

### Speaker 4

I just wanted to request for some flexibility as I will be traveling due to some official work so Ill be in a different time zone at that time

### Speaker 1

No no okay see those requests we can always accommodate no problem yeah

### Speaker 4

John thank you

### Speaker 1

Okay so shall we get back to the business Shall we start Sir one question

### Speaker 2

So one question I had


This is something related to the quiz five we just did So if you allow I wanted to ask a question

### Speaker 1

And tell me what is that

### Speaker 2

So sir there was a question It says in DDPM the variance schedule alpha t for each time step is carefully designed to satisfy which of the following criteria The answer marked is it should increase gradually to prevent complete information loss in early steps But as per my understanding like alpha t is the product of from alpha 1 till that particular time

### Speaker 1

No no no see that we call as alpha bar


This is the variant schedule alpha

### Speaker 4

But even alpha should reduce right because we want the variance to increase as we go forward in the steps

### Speaker 1

Variation should reduce no

### Speaker 4

Variance is one minus alpha t right

### Speaker 1

Now alpha is what we called as the variance isnt it in our in our treatment

### Speaker 4

I suppose it was one minus alpha was the

### Speaker 2

Select alpha we are drawing it from a zero from these samples from zero comma one space right

### Speaker 1

No no they are simply linearly varying let me just check it once hold on


So small alphas are


So beta 1 minus alpha would increase So which means alpha should decrease gradually right What was the option that was there


Electro

### Speaker 4

The selected option was alpha alpha increases


Uh the correct option was marked as alpha should in increase

### Speaker 1

No one minus alpha should increase

### Speaker 4

Yeah I mean for the last options that are very gradually decrease

### Speaker 1

That will gradually decrease Yeah that should be the correct one Because


Yeah because the variance was 1 minus alpha right The variance term in Xt that is 1 minus alpha the variance should gradually increase


Its correct

### Speaker 2

Our variance should increase eventually because we want the final x of t of normal distribution correct

### Speaker 1

Yeah yeah the thing is


Only when the variance slowly increases you can guarantee that the Markov chain converges to a normal 0 1 So variance should gradually increase


Bendon are you there

### Speaker 2

Yes sir Im there yes sir

### Speaker 1

variance schedule I mean of course variance schedule is 1 minus alpha but yeah you can the parameter is alpha so variance schedule alpha so if you are looking at alpha as the variance schedule then the alpha should gradually decrease

### Speaker 4

Yes sir Ill make the necessary change yes sir

### Speaker 1

Beta should increase basically yeah

### Speaker 4

Um just a thing sir in the option it says it should decrease exponentially the one that is being debated right now um so is is it supposed to really decrease exponentially or was that the case

### Speaker 1

Isnt there an option that would say it would linearly decrease

### Speaker 2

No sir

### Speaker 1

No

### Speaker 2

I have I I really have no access to the quiz I really dont know

### Speaker 4

What is the challenge of

### Speaker 2

Chandan I have pasted this screenshot in the chat if you could have a look

### Speaker 1

Thats okay if if if there is no linear decrease option

### Speaker 4

Thats okay


Uh decrease option well give it to

### Speaker 1

It should be see yesterday what happened as I looked at the quiz and there was beta there I told them that beta is not something that I have used so change it to alpha so I think they just change beta to alpha without changing the options


You guys you do What can I say See I told you to change beta to alpha in a meaningful way and just not replace alpha beta by alpha Right If alpha is 1 minus beta then the options have to like

### Speaker 4

Ill know it has to be flipped

### Speaker 1

Anyway so any other question you have about the add plus one feature okay

### Speaker 4

Oh yeah yeah yeah

### Speaker 1

Thanks for checking it out yeah

### Speaker 2

are one more question so we we said that we are choosing alpha alpha alpha as from zero to one but on what basis are we selecting like what is the predefined logic for that

### Speaker 1

I told you in the class already in the previous class it is designed in such a way that the forward macro chain that we do that we construct has to be


designed in such a way that the stationary distribution converges to normal 0 1


So that is why the variance has to slowly decrease


And also if you look at it its all huh huh

### Speaker 2

Variance has to slowly increase

### Speaker 1

What do you what do you call by variance

### Speaker 4

minus alpha

### Speaker 1

If you call one minus alpha as variable then it should increase yeah


Depends on what you call by variance so it is uh if its alpha then the alpha should gradually decrease which means that 1 minus alpha should increase okay


That is what you have to implement in your assignment also right and talking of assignment I have made assignment three of right last week itself I did it huh


I hope you have started working on it When is the deadline for assignment three Now Ive kept it


1870


Okay then you should have started it already


Anything else shall we get started in the class

### Speaker 4

Oh okay can I take this

### Speaker 1

I oh


It says working offline to me do you see my screen


know why it says you are working offline okay anyway okay lets start see todays agenda is that we will be discussing some self supervised learning techniques


So which are the


special cases of these broad learning tech no methodologies called representation learning okay So what is representation learning I had given some introduction in the previous class So given some data that is on iid for my distribution what you want to learn is a function f theta from the data space to some latent space z okay where the dimensionality of z is much less than the dimensionality of x


So now we seek some special properties on Z so the properties that we seek is in such a R R that


the representations are win by representation I mean z okay the projection that you learn on data and we need that to have some desirable properties such as


If you use z instead of x then the amount of supervision that you need is much lesser and the


Z becomes much robust than X and all that Now learning representations can be done in two ways One is the generative way where you learn a latent variable model and use the latent space as representations We have seen this all throughout the course


And Ive asked you to do this in your assignments as well where any latent variable model that you learn


implicitly have this capability of learning representations because when you do posterior inference which is get samples from p of z given x then you are automatically doing


representation learning because z the latent variables that you get from a latent variable generative model can be seen as representations ok that is one way to do it The other way to do it is what we will see which is a non generative way also called self supervised learning or contrastive learning way ok where the fundamental idea is that you define a pre text task


Okay uh what is the pretext task you solve


Some other task using data Note that in all the representation learning literature you dont have labels This is label free learning So now we should when you dont have the labels you define some pseudo tasks where you define some pseudo labels and you ask a neural network to solve some pseudo tasks And the intermediate representations of the


pseudo task solver is what you take as representations for data The examples for pseudo tasks are if you are looking at like learning representations for images then you take an image rotate it with some angle by some angle and ask a neural network to predict the angle of rotation So that can be one pseudo task The other pseudo task can be that you have an image you add some noise to it and try to


Classify between the noise and the data and you take the intermediate representations of that classifier as your representation and so on The other thing can be that you take data and you mask it and try to reconstruct the data back That is one other way to define it So these class of methods are called self supervised learning techniques Now we will go deeper into it and see why should these methods even help in learning good


representations and also some famous examples of how to do it In fact the language models like BERT etc also uses the same kind of technique to learn representations on data


Uh any questions on this so far


Nope my audio is off


Any questions

### Speaker 2

Maybe well cover it later Just a query here The pretext tasks are defined I mean like based on how it should perform in the end right I mean

### Speaker 1

Well not necessarily um not necessarily see


I will tell you what the fundamental idea behind this thing and in fact how to define a pretext task is a question that people have been asking right and different ways have been looked at okay I will talk about it we will talk about it yeah

### Speaker 2

Good thank you

### Speaker 4

Worry like is there any methodology like if we define this pretext then the embedding well get well have you know some kind of structures which will be helpful for other features like what I mean is if suppose I use the pretext as in painting then it will be helpful in classification or segmentation but if I use some other pretext then it wont be much helpful for classification or any other segmentation task


Theyre any such kind of thing

### Speaker 1

Um


Not theoretically but there are some empirical ideas on what sort of predicate tasks would help We will discuss all that just lets see give some time


Okay its not there yet


Did I do and see


Just turn it down its looking pretty


Just wanna see if I did it the last year and if there is


Ah okay Ive done it


Just a second


Two minutes I have to


Okay the fundamental idea for all


Self supervised learning techniques come from this very nice paper very nice methodology that came up which was called noise contrastive estimation


as contrastive estimation also we write it as MCE So the basis for self supervised learning lies here The question that is asked is the following Suppose


The theta


Drawn from a


from an unknown distribution P x


So what we have is we have D that is given by X1


to up to X M


These are drawn IED from PX


Objective


Easy to estimate


estimate the underlying distribution


Underlying distribution P x


given D right So it has been a question that we have been asking So now how do we estimate the underlying distribution given a particular given samples from distribution right This is a question that we have been asking How did we do that I mean so far we have looked at the maximum likelihood estimate


the minimum KL estimate right so both of them are equivalent


How did we do that


Start with


A parametric form for the PX


Call it p theta


Get theta


that would simply minimize some divergence metric which we call the F divergence between P x and P theta This is what we have been doing the entire course right all the ah generative modeling frameworks that we saw uh were actually


fitting into this framework right where uh


uh minimized uh a divergence metric between started with uh an assumption on the uh the parametric assumption on the underlying density called it P theta right


And minimize the divergence metric F uh F divergence metric between these two so now how do we define uh P theta


is where we change different models you know in Gyan the speed theta is taken to be the samples that are coming from a transformed


Gaussian random variable transformation is through neural network in a VAE we use a latent variable model for this and we


find a lower bound on this and then optimize this and so on right then we know the entire story this is how we do it in a


generative framework right So where we assume a parameter form p theta and define the parameters by minimizing error parameters So now NCE provides an alternative for this


alternative for ML estimation


Now uh self supervised learning for today get uploaded hold on a minute


I just wanted this to get uploaded to my drive so that I can access it simply


Okay so in noise contr in in self supervised learning see you what do we need We need a representation for data right So when do you think data would be represented optimally The data would be represented optimally only if you learn the underlying distribution correctly isnt it


See what we need is that we need to learn the underlying distribution correctly because if we do not learn the distribution then we are not representing the data See that is why the generative modeling framework right will give in will implicitly give you representations because by by definition when we have a latent variable model the latent variables actually aid minimizing the KL divergence between or rather F divergence between the the true distribution and the model distribution right


Therefore the representations that we get by solving a KL minimization problem under related variable model implicitly gives us a representation Now we are explicitly trying to find the representation This is not getting uploaded


Do you know some other way to do this Uh


Sorry about this


Has anybody used this airdrop thing between two Mac devices Do you know how that works


Am I audible

### Speaker 4

So you can also also share it between two teams instances if you have it on both the instances


Share it to yourself

### Speaker 1

you can just right click on the file and share and then youll see airdrop there


Oh this is very good okay I just came from a math


Apple devices are what they are for a reason no they are extremely good okay I just got what I wanted thanks


Okay so you see my screen now


You see my screen

### Speaker 2

So theres a file transfer pop up

### Speaker 1

No no no Im writing on my official stamps no


Let me know when you can see my screen


Can you see my screen

### Speaker 2

Not yet

### Speaker 1

Its a computer

### Speaker 2

Mm yes it is visible now

### Speaker 1

Im writing do you see that no

### Speaker 4

No no it is stuck at the NC provides an alternative for ML estimation I think its stuck there

### Speaker 1

Can you please let me know if its coming

### Speaker 4

Yes sir we can see suppose that youre not

### Speaker 1

Okay so hopefully


not misbehavior Now we have noise contrastive estimation provides an alternative for ML estimation where the goal is to estimate the underlying distribution Now how does NCE does this Now we have data


We have data that is x1 x2


Up tall


Lets call it X


Let us draw it from bx this is what we need to estimate ok


I think we deflame


Nice


find a noise distribution


Noise distribution P


Yeah


and draw samples from it


Lets call this as DN


This


uh maybe we will change the notation the too many ns that Im using t number of samples and you have n1 n2


Yen


These are drawn from P N IAD from P N


So you know what we you understand what we are doing we have the data distribution that we have been given ok We define a noise distribution Pn and draw samples from it which we are denoted by n1 to n t ok Now define an estimator


Define an estimator JT parameterized by theta as follows


How do you define J theta J t of theta t because it depends on t number of samples its given by 1 over 2 t


Sigma 40 log of


H theta of


xt plus log of


1 minus h theta of n t


What


HTDP


H theta you can take both H t and N t so H theta is a function


adametloid


You are in neural network


Four


H theta is a function that takes data from d dimensional space and maps it to the 0 1

### Speaker 2

So the submission

### Speaker 4

is common right for both

### Speaker 1

Assessment is common for both of them yes


Okay so this J T theta okay is called the noise contrastive estimator


Okay this is the noise contrasive estimator okay


Okay Now


are multiple okay so now there are multiple claims that we should make okay now the first claim that we do and show is the following claim one is that


J t of theta


But we do it the other way now just a second ah let me just think how to best present this


Okay so maybe Ill tell you this and then okay client one is J theta of theta okay J t of theta the noise contrastive objective Before we move on let me just tell you this See this J theta can be computed right Suppose you have H theta as a neural network J theta can be computed and you can actually backpropagate through that neural network to find theta So basically what we will do is


Represent J theta using the neural network okay and find your theta star as the minimizer


Off


objective function over theta


We can do this we can solve this optimization problem So this theta star we get is the NCE estimate for data Now the question that we should ask now is why should this theta star or rather why solving this object optimization problem lead us to okay so let me write it down So question


Why is J T D


Estimator


Stimulator


for px okay so now you remember that what we actually need is an estimate for px is it good what we are trying to do is learn the underlying distribution px that is our goal now i somehow define some objective function right that uh that that we would like to solve the question is why would solving this objective function lead to a good estimate for px are we good so far let me repeat what we did so we are given


some data okay uh yeah we should mind here we are we are given some data and we define another uh distribution called the noise distribution from which we know how to draw samples we draw some we draw equal amount also you should observe that the dimensionality of of x okay is the same as the dimensionality of n so noise and the data both have the same dimensions here so we draw n


noise samples okay and we define an estimator or an objective function that would involve the data samples xt and the noise samples nt okay and there is another function h theta and h theta is is approximated using the neural network and once we use this objective function so now what is happening actually is that there is a neural network okay and this neural network will either take x or n as


input


and give you 1 or 0 as the output correct


will give 1 or 0 as input right I mean this is our h theta function right Now the and what is the objective objective that we are using this j theta here


Now the question is why should solving the claim that we are making here is that if we do this then we would implicitly learn in PX


Is the story clear so far Now we should see why doing solving this sort of an objective using this technique should give us should implicitly estimate px that is what we are going to answer now But is the is the is the story clear so far what we are trying to do

### Speaker 4

Yes only DN were not sure how it is

### Speaker 1

Only what

### Speaker 4

DN DN

### Speaker 1

It is it is yeah it is some distribution yeah it is totally random it is some distribution that is not px so we will

### Speaker 4

Code to this action

### Speaker 1

It does not


So Pn is just a distribution that is not the same as Px

### Speaker 2

So if the noise is input

### Speaker 1

Are there any noises in

### Speaker 2

Theyre not

### Speaker 4

Theta will return a zero

### Speaker 1

Lets see lets lets see what it returns okay

### Speaker 4

Look at the seat

### Speaker 1

But yeah its in for now its simply a function from uh the data or noise space to 0 1


Alright is that okay


Okay so let us see some properties of this estimator now What is this estimator actually is doing and why should it get the why should it estimate the underlying distribution Okay now let us look at the


properties of the


NC estimator so this is called the NC estimator okay


The first one which is


You will see just


What end is that


J theta


is equivalent to


Solving the


binary classification problem


Were green


The sample so


and this is the first property what we are saying is that this complicated looking or rather this estimator that we have is nothing but solving the binary classification problem between the samples of P and P So let us look at why this is the case Now


Creator


Supervised data set


supervised data set combining


Combining D and DN okay


As follows


Lets call it some S the new data set supervised data set Now that has samples like this you have u comma


Lets call that u1 comma p1


one comma t one


U2 over T2


u 2 t comma t 2 t because there are t samples of noise and t samples of data we are combining them both okay Now how are we defining this Now t i is equal to 1 if u i comes from x i


And T i is equal to zero


UI is from Y and I


Do you understand what we did


What did we do We just created so that we had the t samples of noise and t samples of data We combined them both and created a data set such that whenever we have data samples we gave it one label and whenever we have noise samples we gave that another label Is that alright


Are you dead


Now what we do is the following first step


From the above


We have


What is the posterior of u given t equal to 1 what is this equal to

### Speaker 2

Data

### Speaker 1

This is Px correct Yeah good So now the distribution P


of u given t equal to 0 is p n


E of


equal to one is equal to


What about the priors t equal to 0 both of them are equal to half because we have t samples of data and t samples of noise Correct Now with this let us find


The posterior


Procedure of labels


So what are labels here labels are t correct given data u


What is this which is probability of p equal to 1 given u


What does this equal to is equal to p of u given t equal to 1 divided by


P of u given t equal to 0 times P of t equal to 0 plus


P of u given t equal to one plus P of sorry into


equal to one here you have p


Just open it

### Speaker 2

Word one

### Speaker 1

E of t equal to one no


This is Bayes law right Now because all the priors are equal we can just cancel the priors All of these are half Just cancel them This is equal to P of U given T equal to 1 which is


Beads


divided by


Pn plus Px o what is this is the posterior of


e equal to one given u is given by this


So itll be right


Are we good so far


Now its actually called the optimal base classifier between the samples of these two


which decides upon the ratios of posteriors ok ratios of class conditional densities ok Now suppose


We model see in all classifiers what do we do we model the posterior of the label given data right using a neural network parametric function


parametric function h theta of u


Right So what is happening We are modeling P of t equal to 1 given u using some parametric function See this is exactly what we do in all supervised learning isnt it


We model that using some parameterized function at state of u which can be a neural network


Okay now


given you


Can somebody tell me what sort of a random variable T given U is What is the the what is the form of T given U

### Speaker 2

Indicator random variable

### Speaker 1

Yeah its yeah indicator random variable all binary classification I mean all binary random variables right they are


is a Bernoulli random variable also indicate random variable


What is a Bernoulli random variable Bernoulli random variable is a random variable that takes one of two values with probability p and 1 minus p Coin toss is one example okay It is a Bernoulli random variable with


the parameter


h theta h theta of u isnt it I mean h theta of u is the success probability of this Bernoulli random variable t given u okay That is what it is Now


Suppose we want to find the set theta of u by finding out the I mean by maximizing the likelihood So now lets write the maximum likelihood estimate

### Speaker 2

So how is this parameter h theta of u

### Speaker 1

See that is what we have done no this h we have modeled p of t t equal to 1 given u using a parametric function So this h theta of u is giving you that probability of t being equal to 1 given u


In fact right all binary classifiers does the same thing All binary classifiers what do they do The output of it is actually the estimate for the success probability of a Bernoulli random variable which is the conditional random variable of label given data correct


Okay so let us look at the ML estimate maximum likelihood estimate for this Bernoulli random variable t given u


How does that look like


Likelihood


likelihood function L theta for a Bernoulli random variable in fact the log likelihood


for T given U


Call it L theta


can be expressed as follows


So p theta


is equal to


We have a log of products What is the log like to do we know that no log of


We too dog


Excuse me


Mm hold on that test


Oligotrophic function it is sum of log of


Each heat of it say this is the definition of log likelihood no or i


The bit that has t here i is the sampling index


In the case of Bernoulli random variable what is p theta


P theta of the variable that we are looking at is P given U


So what is the distribution of a Bernoulli random variable


If you write that as an indicator random variable then it is


the power off


or rather write that as uh


when t equal to zero


product of these two

### Speaker 2

it is p to the power t plus 1 minus p to the power 1 minus t

### Speaker 1

Its theta right there that is what it is so you have


The distribution of Bernoulli random variable is given by


The success probability is h theta no which is h theta of u to the power d


1 minus h theta to the power 1 minus t This is the definition of a likelihood of a Bernoulli random variable So just substitute this here So log likelihood will be equal to sum of


What I we have


P times log of


H theta of u


Less


1 minus t times log of


1 minus h theta of u


Now if I split this i into indices where t equal whenever t equal to 1 this will become log of


theta of xi right because whenever t equal to 1 we have xi as the data point whenever t equal to 0 we have it to be n so this is log of 1 minus h theta of ni


etc So now what did we what is this equal to this is actually equal to 2 times 2 p times


J3 of the J Jt of theta which is our NCE estimate


Right so what did we show so far notwithstanding the math is that we showed that J theta is equivalent to solving a binary classification problem between the samples of P x and P theta That is what we showed so far How did we do that


We first created a supervised data set where two classes were created one for the noise and one for the data And we looked at the optimal base classifier as the estimator of the posterior of the labels given data


And we model that as a binary Bernoulli random variable using a parametric function h theta and we just simply obtained the maximum likelihood estimate for the posterior which turned out to be simply the NC estimate


Then what are we saying the summary is that


NCE is a binary classifier


What do you mean


These samples of


X and P theta


Is this i is it alright


Any questions on this


Okay


So this is good So what we are actually doing by in noise contrastive estimation is that given data we just define some noise distribution We take samples from some noise distribution that is not the data distribution and trying to learn to classify between them

### Speaker 2

So so but somehow it seems the

### Speaker 4

This depends on how well we give it the noise


So how do we ensure that the entire I mean like uh


So how big is non data distribution Like it is the entire universe right What can we do

### Speaker 1

Yes that is good that is a good question that is a good question we will answer that we will answer that eventually in this class In fact I mean to


Not to make you wait see the point is its very difficult to come up with that noise distribution and that is why you might have heard this term called hard negative mining right In contrastive learning or self supervised learning techniques There is this term called hard negative mining


Yeah so that is actually this How do you sample P and is a question that people have asked We will discuss that briefly later Yeah but what I wanted to convey was this NCE is a binary classifier between these two samples So not P C T sorry this is P and


Yeah okay


That is what it is Okay So now okay fine You just let us classify between the samples of the data distribution and some random distribution Now what Right Now comes the most interesting part What we would show is that solving this you know J theta attains its optimal okay only when this H theta implicitly estimates the underlying distribution is what we will show


Uh that is something that we will uh uh show


I was thinking should I have to do it now or just take a break and come back and do it


Shall we take a break some fifteen twenty minutes break and come back


Okay I think weve been uh getting quizzed and all that Lets take some break So this is 1050 1053 Lets uh get back at 1115


And continue from here see you in fifteen twenty minutes


Ill get a zoom

### Speaker 4

Yes so we can hear you

### Speaker 1

Shall we continue


I was just reading some news Do you know the name of this Elon Musks son


People dont create

### Speaker 2

Im a glorzzer

### Speaker 1

No its not code I mean its


Some X A A 12 or something like that


No liquid


Imagine the plight of that kid when he goes to school


actually not very a big fan of these complicated I mean even its today you know young parents in India they are also doing these weird things you know they name see because naming happens only once in lifetime and they want it to be exotic they name children with all kinds of random things you know I I keep thinking especially when these kids grow to be like older adults how do you call them with such weird names

### Speaker 4

Theyll be traumatized thats what I am

### Speaker 1

So


And so many you know names that mean nothing simply theyll see somewhere and theyll say that its a Sanskrit name I mean studied you know Sanskrit to identify that most of these names are not Sanskrit so what

### Speaker 4

Usually in India people base the names on like movies and all those places but this pyramid kind of name is A A 12 some 1 to 14 I dont know what it is

### Speaker 1

for business okay lets get back uh yeah so we were looking at the noise contrastive estimation and we saw that its a binary classifier between samples of two distributions


Okay now we will continue So now okay finally the question is finally do a binary classification between these two distributions Whats great about it right There is this very nice result that would say the following So property two of in noise contrastive estimation is


You have j theta


be equal to


1 by 2t


Lets uh


Log off


H theta on X


Yes


Logos


1 minus is theta evaluated at n t right this is what the loss function was


Now large large numbers


Im not sure


J theta is approximately equal to some J tilde of theta


J tilde of J tilde of theta is given by the following it is half


expectation of


Log off


Its theta evaluated at x


Lago


1 minus h theta evaluated at n


And this expectation is over the joint distribution of P X and N


This is what the law of large number says


Okay this we know right I mean if you have samples from distributions then expectation can be approximated using sample averages We inverted that meaning we said that this was a this I mean this was


A sample average right whatever we had in J theta was a sample average we just converted that into t equal to 1 to 2t converted that into


Expectation


Suppose


given by


Log off


Let P theta of X denote


each distribution


being estimated


We are NCE We solve this optimization problem We are implicitly imposing a distribution on the model Lets call that as P theta


Let f be equal to log of


ETI topics


Okay now what can be shown us that I will just give the proof for the want of time J theta can be shown to be equal to half


of expected value of log of


Odd


Perfect


Minus


Logos


P and of X


expected half times the expected value of log of


1 minus r times


f of n minus log of


The n evaluated at n


So this equivalence I will not show I mean this is only an algebraic manipulation What can be shown is that this j theta can be written equivalently this way where r something that we dont know where r is simply the logistic function r of k is 1 by 1 plus e power minus k r is the logistic function When it involves just rewriting the equation


Rewriting the equation of J in terms of what we know So why is this important So again I will state a theorem without proof which again can be solved easily I will tell you how to do it proved easily So theorem is that


So with this what happens is your J theta now can be written as a function of F no


Because we yeah question

### Speaker 2

So in the first term this r for this function r the argument is just fx or fx minus log pn of x

### Speaker 1

So it is R of f of x here So R is a logistic sigmoid right So it is R of f of x right And R of f of n minus log p n n into n correct Yeah the bracket was missing


So now you represent this entire see what did we do I mean we represented the ah ah the log likelihood of the underlying distribution using some function f So I mean strictly speaking this is f theta right and we present we represented the noise contrast f estimator in terms of f theta


Now this theorem which is the most powerful theorem that would say that the


Optimal value


of f theta


That would


Optimize


j tilde of theta


is such


Next star


is equal to log of p x of x


This is the most important result Now the question that we are asking is the following I will tell you how we would get it that way The question that we are asking is that what would be the F star That would


maximize this objective or minimize this minimize the negative of this objective is the question right because the only variable here is f no we are searching for an f okay that would maximize this objective Now what can be shown is that irrespective of what n you are using


that f which is maximizing the objective j theta non scorer estimator j theta theta is the one for which the f happens to be the log of log likelihood of the true underlying data distribution Now how do we get that So we get that by writing this entire thing in terms of double integral right this expectation will be written in terms of the double integral of this thing times p x into n assuming that noise and data are independent you write these as


channels over BX and BN okay


V x V n and then you differentiate this integral with respect to f and put it to 0 what you will get is that the optimal f is going to be log of P x that is what it is I mean you need a bit of variational calculus to show that which is beyond scope of this particular course and that is why I am skipping the proof But yeah but the result is that


The optimal value for the noise contrastive estimator is when the log of the distribution that it is that it is implicitly imposing on the model is equal to the log of the likelihood of the underlying data distribution


There is a very powerful result So now the summary or the take home message from this what is the consequence of this is summary yes


One can use or rather


Solving


The classification problem in DNC estimate


Between Px and Pn


Yeah


Well implicitly


Non


The underlying distribution P theta


distribution P x This is the most important result So you understood right So what we are doing is suppose we have


A classifier that is built


Let us say that we take x power n to this This is your h theta and this will finally give you 1 or 0 Okay Trying this What we are saying is if you take the intermediate representations of this Okay So let us call this as


F theta of x because as you saw what the h theta


was the logistic sigmoid of f theta of x So whatever you get before the final layer is the logistic sigmoid So whatever you get before the the final layer penultimate layer of the logics is what you call as f theta And we know that f theta the optimal f theta is log of f of x


right and what we can use that we can write Z


be equal to f theta of x


The features are embeddings or representations


So this is the result So what we are saying is that you do not have to do anything all you need to do is that if you are given some data ok define some noise sample from it and learn to classify between the data and the noise So now if you do that then you are implicitly learning the underlying distribution take the logics of that classifier and use that use those as features See this is the this is what is called as the contrastive learning


of self supervised learning So what is the self supervision part here Remember that we defined a pseudo task now the pseudo task the pretext task that we defined here is that of classification right


This is the fundamental bedrock of contrastive versus supervised learning okay where it comes from noise contrastive estimation that would say that solving an optimization problem which turns out to be classification between the data distribution and some noise test distribution will implicitly learn the underlying data distribution up to a constant


Any questions here See this is the idea I mean everything else that came after this no its only as improvisation over


this idea but this is the fundamental idea actually


Any questions here


Hello are you


Is it there Am I audible

### Speaker 4

Yes it is you would

### Speaker 1

This is a very powerful result right I mean it is saying that I mean all you need is to simply classify between the data distribution and some noise distribution And if you do it please note that these results are asymptotic in the sense that this will give you an estimate for the log likelihood of the underlying data distribution only if you have enough samples Now as Vivek was asking before the break now how do you know what noise distribution would help it


what can be shown while doing this proof is that the larger is the divergence between px and pn the better it is to estimate the underlying data distribution okay now getting those noise samples is is very important now that is why we have so many methods on how do you define the hard negatives how do you how do you come up with the negative samples okay but yeah so this is the fundamental idea of why should solving a pretext task okay or a


pseudo label task


could help you in learning the data distribution Please note that this is this entire thing is non generative in the sense that you cant sample points from PX from this right Is this clear This is not generative right


not able to sample from PX


Its a non generative

### Speaker 2

if we are not able to generate some samples then how can we say that we have learnt the original data distribution

### Speaker 1

And thats what we saw so far right


See what we showed was that see we are not able to sample from this thing but


Solving this classification task what we are getting is at the penultimate layer of this classifier we are learning the log of the underlying distribution is what we just showed isnt it The entire todays class was on that

### Speaker 2

So

### Speaker 1

So we can learn the underlying data distribution even without sampling from a distribution is what we should

### Speaker 4

So from this if we connect it to a sampler it can ideally sample it right I mean we got the distribution right data

### Speaker 1

So we didnt know not explicitly right See given an x it will see what is this penultimate layer giving you given an x as an input it is giving you log of px of x thats all right It is not telling you what px of x is

### Speaker 4

So there is no way to

### Speaker 1

There is no way absolutely no way no But what is what is important is that if you know log of px of x for all samples then you know everything about the data That is why these features are powerful


See why do you think bird embeddings are so in fact bird also does exactly this thing we will come to that in a while Why do you think those are so powerful is because if you do this well ok with a large number of samples so that the log large number is is is respected then the the representations or the embeddings that you are getting from this classifier are actually estimating the log likelihood of the data right that is all So you know everything about the data so you can use it for anything that you want that is the idea but you are not able to sample


From here yeah


Anything else


See compare this with lets say VAE or a diffusion model or a DDIM where you will get embeddings as well as ability to sample


So this uh


generative pre training GPT So that is an example where you have the embeddings and also the generative ability We will look at GPT probably in the next class right


where you generate the embeddings right or rather find an embedding space representation and also learn to sample implicitly from I mean together just like a diffusion model or a VAE in a GAN right for instance in a naive GAN


Can somebody tell me what abilities does it have


It can generate it can generate it cant find out D it cant do posterior inference

### Speaker 4

Yeah

### Speaker 1

But we did see some examples right In your assignment I had asked you to did I ask you to do that or not Like build a classifier or an inverter over the generator and solve a reconstruction task over the latent space Did I ask you to do that


So you have done that right So now you can you can improvise GAN to to to do an inversion or a embedding extraction as well ok


All right service

### Speaker 4

So so in this case so this f theta for this discriminant will it be a scalar single number

### Speaker 1

Youre supposed to get that

### Speaker 2

getting only one output one or zero so

### Speaker 1

Yeah thats a very good question Yeah it will be scalar and thats why people said okay lets move away from this Why only do a binary classification problem Let us solve an n class classification problem which is what is called as info NC


Okay where the idea is to extend and see


Whoa


Multi class classification study

### Speaker 2

so that we can get a vector of embeddings

### Speaker 1

So what InfoNCD does is that it is simply a multi class classification problem so given a data point


data point x i ok defined


Okay


ICE examples or IC examples


from PN and


solve a k class classification problem


between XI in fact its actually K plus 1 class classification problem and K negative samples noisy samples


Okay this is what noise sorry InfoNCE does The papers name is Representation Learning with Contrastive Predicting Coding Okay I mean its nothing but extension of noise contrastive estimation


for uh


key class classification problem so let me


I thought just show you show you the paper give me a second


Let me share my screen and show you


Heres Green


Did you see my screen


But anyway this is the


This is the paper on noise contrast estimation Its a very very nice paper Okay Very old but this is the one that noise contrast estimation a new estimation principle for unnormalized statistical models Please look at this paper Its very good Okay Like 2010 it appeared Okay But it was just sort of buried because this could not be scaled to higher dimensions because then the neural networks were not very powerful Its a very nice paper Okay Have a look at it Then came the


Info NC paper 2019 which is called representation learning with contrastive predicting coding So where what they do is just extend NC for a K class classification setting


Given a set X of n random samples containing one positive samples from the distribution that you want to estimate and n minus one negative samples from the proposal distribution right So yeah So if you take a set of n samples okay one of them is the so called positive sample or the data sample from the data distribution and there are n minus one negative examples You define the NCE loss as the negative of the expected loss of expected value


the log of this thing So what is this if you look at it this is nothing but the softmax okay where fk will give you the the kth output of the softmax in the neural network okay and it is summed over all possible other samples


This is all right This is the infoency loss Now what


can be shown just like the NCE counterpart is that optimizing the optimal value of this fk is the one that gives you the log of this underlying data distribution Its just simple extension of NCE ok for a k class classification problem


Is this okay


Now this came in 2019 and this was extended to the contrastive learning This was Hintons paper right This was well celebrated This is called SIMCLR okay It stands for Simple Framework for Contrastive Learning of Visual Representations Now look at this graph What they show is the following that if you take the ImageNet top one accuracy you take the representations that are


given by the SIMCLR and do a fine tuning So now what do you do with the representations You take those representations and if you want to solve a classification task just fine tune another classifier using those representations that is how you use it It was shown that it just beats all the existing state of the art Okay On yeah The fully supervised is of course the best that you can get Right But even with like very less number of parameters on


the fine tuning of the fine tuning network you can get a pretty comparable result is what was shown Now what does this do This is nothing but infoency look at this expression So this loss function that is used in SimSLR is nothing but the infoency loss write it as the dot product between So what they have done is look at the


Info and sheet paper they write this FK right as a dot product


between the representations for the positive sample and the negative sample and this is just the normalization constant


So what is done is the following that given an image


image they create multiple augmentations of the image by doing these kinds of things crop and resize and then you have color distortions and you do you add some Gaussian noise and make blur it out and you do Sobel filtering and extract the edge and all that okay now what they do is given this particular image all of these counterparts are taken to be the positive


positive counterparts of this particular image okay and then what they do is whenever the network sees these augmentations they want the network to output one see think of it like


solving a k class classification problem where the original image and all of these augmentations are taken to be of the same class okay and all the other images that does not correspond to this original image is taken to be the


from the other classes and you solve the K class classification problem


Does it make sense

### Speaker 3

Yes sure

### Speaker 1

Any questions on this

### Speaker 4

So this one will result in a k plus 1 vector outright


I mean the the the the the dimension of the

### Speaker 1

Not not necessarily the representative see the way no no the way they have done it

### Speaker 4

that our presentation

### Speaker 1

they have taken the the penultimate layer to be of some d dimensions Now the loss function will take those d dimensional vectors and compute the dot product between those representations here That is how they implement this f k


So you can you can actually customize it


because the the I mean they dont implement it as cross entropy they implement it as the dot product between the representations that have been gotten between these two


Any other question on this


At C the fundamental idea is that of the NCE Now improvisations have been done where instead of solving a


binary classification problem you solve a k class classification problem Now you represent the objective of the k class classification problem in terms of


in terms of dot products right or inner products between the pre logit layers okay that is proportional to of course the binary cross I mean categorical cross entropy right I mean that is what SIMCLR does


Is this alright

### Speaker 4

Oh yes sir but uh there is no noise in

### Speaker 3

Hold here now right

### Speaker 1

Well you can see all the negative samples that you get here right I mean is actually the noise See if you look at the algorithm what they do is they take one sample okay one data data example okay and create all the augmentations of it and call it the positive example


And then what they do is they sample randomly Ill just show you that


See here they say that we do not sample negative examples explicitly Instead given a positive pair we treat the other 2 n minus 1 augmented examples with a mini batch as negative examples This is the way they define the noise here

### Speaker 4

Okay okay

### Speaker 1

But again as I said there are lots of improvisations over it I mean then people came up with something called MOCO right momentum update contrastive encoding yeah

### Speaker 4

So what effect does this re actually have this just tries to push away the vectors from each other like if youre going to say the dot product

### Speaker 1

So what is what this what does it do is whenever you have the positive pairs it will try to cluster them together whenever they are they are they are negative pairs they will try to push them apart that is what a classifier also does isnt it

### Speaker 3

Right yeah so

### Speaker 1

That is exactly what a classifier does It is trying to cluster the points that are from one category It is trying to push the points from the other categories away Thats all Now what is the intuition See I did the math because I mean you might have probably known from the course so far is that I I mean I get convinced better if I am shown some mathematical guarantees of whats actually happening But I can give you some intuition also So what is actually happening


with all these methodologies is that suppose you know how to uh like


group all these uh all these examples as close to this dog image and the cat image you know how to push the cat image away from this you cant do it as long i mean you cant do it or rather you can do it only if you know understand the semantics of this object called dog isnt it okay see if somebody wants to put this dog image and this cutout dog image into one same category they should know that okay this is actually a cutout


of this dog isnt it


Right So thats the whole point So now as means you do you recall these uh uh these these question types that we we we were having we were having when we were going to school right One of the question types was this thing called fill in the blanks Isnt it Yes They used to give a give a sentence and used to ask us to fill in the gaps randomly match some of the words and ask them to ask us to fill the gaps Now you can do it only if you know perfect


what the semantics are isnt it

### Speaker 4

Yes yes

### Speaker 1

Thats the whole point In fact the all these language LLMs today are learned using that technique or this technique only which is that yeah which is the mass reconstruction So you have data you mass some parts of it and try to reconstruct it back So which is nothing but classifying between the data sample and the noise sample


Okay so any other question on this

### Speaker 4

So there is a two into n minus one images right So what is that two indicates here Is that two augmentations only we do or images

### Speaker 1

No no no no given a an image you take n augmentations


And you sample another random point


Okay so that will make it 2 n minus 1 isnt it I mean they count from 0 thats why there are like 2 times n minus 1


Basically its 2n So you take an image or a data point you take n augmentations of it and call all of them as positive right And then you sample n negative samples from the data set So that will make it 2n no 2 capital N thats all it is

### Speaker 2

Sir and negative samples here means can you clarify

### Speaker 1

You need samples from the noise distribution right

### Speaker 2

Yes

### Speaker 1

Now what is done is that you take a dog image and you take n augmentation that will give you the positive ones


You need samples from the noise distribution as well So what is done is people just sample n random points from the data set itself and call them the samples from the noise

### Speaker 2

from this dog data set itself

### Speaker 1

Not dog this data set has all kinds of objects


This data set has all kinds of objects So now if you randomly do a sampling from all objects the other n samples that you have gotten hopefully are not from the dog category Thats a good point that you made See what happens is these methods especially SimCLR has been shown to work well only if you have a very very large batch size


Okay now why is that the case is because suppose you have like a you have very small batch size when you take when you do a like sampling for something negative sample with n samples with n being very small there is no guarantee that these so called negative examples that you get are not from the doc category isnt it You do not have control because we have no labels


But if you make our batch size to be very very large then


What happens is if you take if you sample a very large number of samples then most of them will not be from the class that you are considering for this particular example Thats why the SimCLR is known to work only with very large number of examples like very large batch sizes


Okay uh questions on this yeah we wait

### Speaker 4

So uh one question so is the noise contrastive estimation the same as out of data distribution detection

### Speaker 1

Uh sort of yeah you can you can you can view it as uh like outlier detection actually yeah


See if you if you are solving the binary classification problem yes it is outlier detection If you are solving the k class classification problem then like detecting outliers from multiple distributions Okay what is it

### Speaker 4

No so outlier is a very specific case what I mean is something like out of distribution detection which means

### Speaker 1

Agreed Agreed You want to you you are classifying between the the set of samples samples of the data distribution and everything that is not data Yes

### Speaker 4

I agree I agree


Yes yes yes yeah

### Speaker 1

See that thats how human beings also learn no if you know how to classify between you know what is important what is not important then

### Speaker 4

So

### Speaker 1

Then you have learned the tricks of the life thats what they say


Okay so let me come back get back to this So as I said there are multiple improvisations over it So now one question that people ask is now how do you reduce the batch size in SimCIRR So one way to do it is that whenever you are sampling from the noise distribution as Vivek was asking


You sample the noise points in such a way


that they are very very I mean they are they are pretty away in the representation space from the data samples ok So this is called hard negative


Sampling let me just write it down


Question is like


How to


Sample


Better negative examples or better


noisy or negative samples


So now there are this is called hard negative mining


negative meaning where given a particular sample okay


How do you make it hard in the sense that how do you ensure that that this negative sample is actually contributing to learning There are multiple ways One way to do it is that given a sample you take all the augmentations of it and call it positive For the negative samples you do for every sample that is that you get from the data set Okay And please note that for the case of


for methods like CMCLR the noisy samples are actually the samples from the data set itself that does not correspond to the the argumentations of the given input sample I hope that that is clear Is that clear


Let me write that down what I mean is in methods like SIMCLR


the noisy or the negative samples


the points from the data distribution


dot r


not the


Augmentations


of the given input sample


So that way it slightly differs from the NOS contrasted estimation in the sense that the in distribution samples are taken to be the one that that one the taken to be a sample and its augmentations The outer distribution samples are taken to be a few randomly sampled points from the data set itself


So example is right I mean suppose you have a have an image of a of of a digit 1 then the positive examples are its rotation and the masked version of it and you have the noisy version of it all of these are taken to be the in


These are positive examples or indistribution samples


And you take the images of let us say 2 3 5 etcetera all these are taken to be negative examples


And then you learn to classify between these two in a K class classification setting So this is also called as the anchor point


anchor point or the data point at over interest okay of interest so all the contrastive learning or self supervised learning techniques we would learn to classify between the samples of positive and negative examples


Its a funny

### Speaker 4

So but in this uh current context we do not have the labels right so thats why we dont

### Speaker 1

We dont we dont we dont Exactly exactly So now see what might happen no Like one particular sample from the same class might creep up here right Thats why you need a large batch size Thats what Im saying So these examples have to be negative enough for this to work because they have to actually come from PN Now thats why if you have very large batch size then the likelihood of having samples not from the same class or semantic


Label as that of the anchor point is less the idea

### Speaker 4

You need some kind of balanced data set here right as well

### Speaker 1

Uh not balance you need a l yeah I mean you can say balance or you need a lot of negative samples thats all


Okay now uh


Any questions so far


This is shown to be very powerful as I said no SIMCLR etc would reduce the the dependence on the supervised I mean labels by a drastic amount of reduction is there So examples of this approach contrastive learning approaches in the image space you have some methods like SIMCLR or you have MOCO and theres this thing called JAPA I will talk about it okay


the space of NLP all these models such as BERT and


What is the other thing called it is a world toek


All these are variants of this NCE and info NCE okay

### Speaker 4

So how do we click

### Speaker 1

Clip is also there but clip is for uh like its for multi its for multi uh multi modal data but the idea idea is exactly the same I can add it yeah

### Speaker 4

Im sorry

### Speaker 1

I will write it so for speech you have the wave to like for image plus


Next you have


What does this clip stand for I keep forgetting that


Contrastive pre training for images and languages it thats what it


Just opening the clip paper

### Speaker 2

Contrastive language image pre training

### Speaker 1

Yeah contrastive language image pretraining okay


That we spoke of clip no Maybe I can also talk about it So you know how it is done


Now that is up


The objective is to learn


on the representations or encodings


jointly


Between B


image and text modalities see this can be extended to any multimodal thing okay text modalities


How is it done you have you take two networks one we call as F theta the other you call as


G theta


this is the text encoder and we have the image encoder so this will take text as input this will take images as input


Okay what they do is they take so for this you need to have pairs of images and text okay the data that you have is you have images


You have an image comma text that is the kind of data that you have Okay Now uh


Do you need the pair I dont think you need the pair

### Speaker 4

We need the persons

### Speaker 1

Do we

### Speaker 4

Yes very much and in very large numbers

### Speaker 1

Let me just think about that


Contrastive pre training you have the


done let me just see

### Speaker 4

In a given batch there is a set of images and their captions

### Speaker 1

You need the corresponding captions also no

### Speaker 4

Yes


And the only thing is in that uh

### Speaker 1

Yeah you do need uh pairs

### Speaker 4

I mean it has to be a set and in that set whatever belongs to that image that only those dot products should be maximized and all the others should be minimized

### Speaker 1

So what is good is I will tell you yeah You do the same thing no for every text you get you get and I just yeah what will happen is for text let us say that you get some t1 t2 corresponding to some tn there are embeddings for n possible text and similarly for images suppose there are n images right you get image 1 image 2 up to image n okay So you take n embeddings from the


Uh


n embeddings from the image encoder n embeddings from the text encoder ok Then you have a n by n matrix


embeddings right so this is lets say that this is the text dimension and you have this is as the image dimension


So what does this tell you this will give you along the diagonal


This will tell you the the inner product between the image embedding with the corresponding


Externality isnt it Now what you need is to maximize the


Inner product


Rather this itself no is the inner product matrix so lets call this matrix let me write it down hold on


call this as IP now IP at I comma J is the


dot product between the ith text embedding and the ith image embedding and the jth text embedding The objective is to find theta and phi such that


Maximizes


diagonal of IP right


The maximizes this divided by


and take the sum of all the


So more all I you have diag of IP divided by


of diagonal elements of IP thats all So whenever you get the pair of you get embeddings in such a way that the inner product between the image and the corresponding text is maximized and everything else is minimized You need zeros here you need maximum values here that is how we are trying it


Now finally after you train this what you can do is you take the image okay and what do you get What do we need We we we need a an embedding right corresponding to


pair of text and image this is how we have done it isnt it now when we want to do uh


Prediction what do we do


We take an image and give it to the image encoder we get the image embedding Okay Then what you do is you take


gen possible candidate text pass it through the text encoder and get the text embedding And you take the inner product of all those text embeddings with the image embedding and see which one fires and that is the caption corresponding to that particular image And thats how you do zero shot prediction


But you as you can see all this is actually noise contrast estimation isnt it different ways of doing noise contrast estimation So I encourage you to look at all of these ok I mean SIMCLR we looked at JEPHA I will just talk about it in a while because I have asked you to implement this But we will cover it in the next class Wave2Vec for speech is again what they do is they take the speech signal


mask it and create the positive and negative examples and and solve a contrastive learning task and get the representations See in fact I was working with like one of these like insurance brokers I mean there is this company called Policy Bazaar right I was solving a research problem for them So they were building automatic speech recognition systems for their customer care customer centers call centers


So they had built a supervised ASR so when we tried wave to wave kind of approaches okay what happened was their dependence on supervised data came down by 85 percent


They could achieve the same performance on ASR by using only 20 percent of the supervised data So these are very very powerful methods e contrast learning methods okay


Now the last thing that I wanted to talk about is this joint extraction of


This is one thing that this guy uh Jan Likon keeps talking about everywhere no


Its quite hard


Joint embedding predictive architecture


What they do here is they


Avoid


We need for negative samples


What they do is the following they take an image okay and by the way they use what is called as a


Vision transformer as the backbone model


I will teach transformers in the next class then I will talk about vision transformers Now the idea is suppose you have an image like this okay what they do is they take random patches


You cut out some random patches from this image and call those patches as target patches


And all the other patches which are here


They create some other patches from the region that is outside of the target patches and call them as context patches


Okay the task


is to predict


the target batches


given the context patches as input


Thats all this JPAR does And they claim that if you do this then the performance that we get is much much better than most of the existing contrastive learning methods Let me just show you that


This is what I have asked you to implement okay So when you dont have to do it using vision transformer you can actually do it using the CNN Do you see this figure now my screen and figure three


Can you confirm if you see my screen

### Speaker 4

Those are not visible

### Speaker 1

Thats cool


Yeah I will take questions in a while


Now do you see the screen

### Speaker 4

This

### Speaker 1

This is what they do right They taken a given image given an image they divide the image into non overlapping patches or yeah non overlapping patches and they randomly take some patches as target patches okay And then take some other patches as context patches Now the task is that if you are given context patches they have two encoders one they call as context encoder and target encoder which share the weights Now given the context


patches the task is to predict the target patches


That is why they call it as the predictive architecture So what is to be done Yeah So the image based joint embedding predictive architecture uses a single context block to predict representations of various target blocks originating from the same image Of course they do not predict the target


patch image at the image level they do it at the represent I mean the embedding level


Whats interesting is that all they use is a square error loss between D


true target and the predicted target thats all Its extremely easy to implement Look at this figure So the original image you have this context and multiple targets What they do is they give the context image as an input to a VIT for the context encoder and they want to predict the embeddings corresponding to the target patches and they simply use an MFC between the predicted target embedding and the true


target everybody


Is it alright See it actually makes lot of sense intuitively you know See its like suppose I give you this image okay and ask you to predict this You are implicitly learning how to complete this dark phase isnt it


Do you get what Im trying to say


So that is why they say that this thing will learn implicitly the representations that correspond to the underlying data set Of course as I said the base for all this


lies in Nash Kantor estimation


Okay questions Its a survey

### Speaker 4

The assignment we are implementing IJPEGG so it is a typo right

### Speaker 1

I J E

### Speaker 4

PG in the 70s

### Speaker 1

The second one should be yeah yeah of course yeah


the other

### Speaker 4

So when choosing the patches they are completely random or there is some yeah

### Speaker 1

Theyre random theyre random


They are random but what they do know they will ensure that the patches for the context and the target are non overlapping

### Speaker 4

Answer the


Youre talking about

### Speaker 1

Oh

### Speaker 4

Choosing that

### Speaker 1

So that they have that that that is a hyper that is actually a hyper parameter okay and they have experimented with multiple of them

### Speaker 4

So in the IJPA uh net I mean method uh what how does the decoder and encoder look like uh like what is no decoder

### Speaker 1

There is no decoder


There is no decoder there there are two encoders one is the context encoder the other is called the target encoder

### Speaker 4

Then what are we learning there I mean what is learned is it a network

### Speaker 1

the network no the encoder that is MF theta network that would take a pair of I mean that would take a a a patch as an input and gives you some vector as an output

### Speaker 4

okay okay okay fine fine fine only okay so its not generating anything it is not generating anything no no

### Speaker 1

Hes not generating anything

### Speaker 4

Okay

### Speaker 2

Is that an assignment or a question

### Speaker 1

you can you can say that there is also a a a predictor right what which will do is that will take the see what they use for f theta is a is a vision transformer so this transformer would give you the embeddings okay they also have a predictor network that would take these embeddings right from the true target patch and predict the yeah

### Speaker 4

Okay predict the I mean the entire image with the with the field in

### Speaker 1

Not the image not the image it will predict the uh it will take as input the the embedding corresponding to the context yeah embeddings of the context is taken as input and it will predict the embeddings of the target

### Speaker 4

Youre building a


Okay without ever having to generate anything it can There is no generation there is no generation Okay okay okay

### Speaker 1

There is no generation there is no generation okay okay okay so there are two encoders basically let me just show you the figure again hold on


Is my screen visible

### Speaker 4

Yes yes

### Speaker 1

See there are two encoders one is called the context encoder and the target encoder okay So what will give is this con context encoder will give you a vector target encoder will give you another vector right

### Speaker 4

Yes

### Speaker 1

Now what would this there is another network called the predictor network What would this predictor network do It will take the embedding corresponding to the context encoder


Right


and predict the the target the embeddings of the target encoder

### Speaker 4

Yeah embeddings of the target yeah okay

### Speaker 1

embeddings of the target encoder and the loss for this G right So basically how does the loss go So there are two networks like this F theta and F theta cat Both of these are vision transformers The context network will take some patches from the context It will take context patches Target encoder will take target patches So you get two embeddings right Corresponding to target and the context Now you take a predictor network that would take as input the encoding embedding


correspond I mean output of the context encoder okay and predicts the output of the target encoder


It clear

### Speaker 4

Yes thank you

### Speaker 1

there is an L2 loss between them thats what you need to implement as I said no for for your implementation purposes uh you can either use a uh a vision transformer here if you if you can otherwise you can use a simple CNN also here no problem

### Speaker 4

Do we need two networks here to be trained separately

### Speaker 1

I mean what is done in practice is that they take you actually need two networks but you can share the weights between them You need one network for target encoding the other for the context encoding


Okay so great I think we have to took lot more time than usual Okay so thats it for today Uh we will reconvene again next week

### Speaker 2

Answer one question In question number nine it says distilled the above resonate on a small sized MLP


What do we mean by distilling it

### Speaker 1

Not taught you distillation right

### Speaker 4

So take a smaller network and show it a lot of uh

### Speaker 1

No no no I have to I have to teach distillation

### Speaker 4

Little rat

### Speaker 1

Let me do it next week if I do it next week then I have to extend the assignment deadline for one more week


This is a small topic that I wanted to said that should be

### Speaker 2

So that should be helpful sir


That should be helpful

### Speaker 1

I will do that too much

### Speaker 4

Its our equal ending our

### Speaker 1

Meaning the uh assignment deadline you are saying huh


Its okay no I mean Ill just give you maybe one more week till 30th

### Speaker 2

Yes sir yes sir its okay

### Speaker 1

38 should be okay no Let me do it right away So thats it


Signments


Because anyway Im grading it on uh like the first week right So time went to edit


Please remind me our next class I need to teach installation I complete it completely off went off my head First week of December


Yeah
