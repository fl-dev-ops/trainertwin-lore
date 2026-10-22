---
id: c475SLygCK4
title: Lec 9 - Deep Generative Models Variational Auto Encoders
url: https://www.youtube.com/watch?v=c475SLygCK4
date: '2024-11-23'
duration: 02:57:32
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

# Lec 9 - Deep Generative Models Variational Auto Encoders

## Transcript

speaker_1: or something


So I 14th is when it is ending for the off line semester I think well have one on 16th I think that should be okay


And given that you have an exam next Sunday not having a class on Saturday is okay I suppose okay well do it that way

speaker_2: No one

speaker_1: Shall we start today


uh okay so as i said no todays um uh focus will be on the variational autoencoders or vaes okay so as a precursor uh we were looking at uh latent variable models last time correct now what are latent variable models uh these are uh models that are defined as uh okay so whenever i talk of a model


model yeah so p theta which is a distribution over the uh the data variable right is what is called as a model so whenever we talk of model it is p theta that we talk of okay now in a latent variable setting that p theta is given as a marginal over the joint distribution of two uh variables okay one is called the uh the data variable of course x uh which is given and one is the latent variable that is not observed


I mean thats why the name latent of the hidden variable


Okay so what happens in a latent variable model So what is a latent variable model where p theta the model is given as a marginal over the joint distribution of the latent and the data variable So that is what is called as the latent variable model Unfortunately this does not have a pointer Otherwise Ive been so nice that I pointed things out when I was recapping Anyway okay


As the name suggests the latent variable model latent variables are not observed right they are not observed they are to be estimated together with the model parameters so typically z is also estimated or learned along with the model parameters theta


Now the way it is defined is for every observed data point which is in the data set D there exists a corresponding latent variable that is not observed So several examples latent variable can be discrete or it can be continuous If latent variable is discrete the example that is given is that of the Gaussian mixture model or k means clustering where the latent variable denotes what cluster


or what group of Gaussian that it belongs to Okay that is one example The other example is a latent variable which is continuous Whenever you have this encoder decoder model it may not be autoencoder Any kind of encoder decoder model is a latent variable model with the output of the encoder seen as a feature or latent variable corresponding to xi Right So that is yeah So feel free to ask questions Im just recapping what we said


saw in the last class If you have any questions you can raise your hand and ask Okay Now this is about the definition of latent variable model Now the question is how do we model distributions using latent variable model So that is the question So now as I said the P3 topics in the case of latent variable model is given as a marginal over the joint distributions And in all latent variable models the optimization is


usually carried out by maximizing the log likelihood or minimizing the KL divergence So the objective is to maximize the log likelihood or minimize the KL divergence So for the rest of the lecture I will be using the term maximization of log likelihood not minimization of KL divergence because they are equivalent The reason I am using the term log likelihood is because that is what is usually used in the literature everywhere


Okay so now how do we model the how do we get the parameters of latent variable model as I told in latent variable models right the latent variable also has to be estimated jointly with the model parameters theta So now what do you mean by estimating the latent variable because we are talking about random variables here and latent variable is another random variable it amounts to estimating a distribution over the latent variable


That is what it means by estimating a latent variable How did we do that We wrote down the log likelihood as L theta And we multiplied and divided the log likelihood by some distribution that you would want to estimate on the latent space Call it as Q of Z given X And then with the Jensens inequality what we found out was that there exists a lower bound on the


log likelihood that you would want to optimize So yeah the storyline is the following right There is a model latent variable model with parameters theta and we want to estimate the parameters of that model theta along with the distribution over the latent variables right Now the distribution over the latent variable is what we called as a variational latent posterior denoted by Q of Z given X


Now when you introduce this unknown latent variable or distribution of the latent variable into the model you cannot directly optimize the log likelihood okay Because in most of the latent variable models computing this integral right to get your p theta okay p theta is an integral over the joint distribution of x and z That is not feasible because you dont know what the latent variable is What you can do is take a guess on the latent variable distribution


which is called as Q of Z given X Once you take a guess on the latent variable latent distribution on the latent variable there will be an inequality that arises which means that you will get see observe this what you would want to maximize which is the log likelihood L theta whenever you take a guess on the latent variable okay via the distribution Q there will be a lower bound that is created on the log likelihood


Now that lower bound is what is called as the evidence lower bound or elbow With our choice of q and theta you will get a particular elbow or the evidence lower bound Now the goal in all latent variable models is to find out model parameters theta and a distribution of the latent variables q such that the evidence lower bound is maximized


the log likelihood but because we cannot do it exactly what we do is we will optimize a lower bound on the log likelihood which is called the evidence lower bound so it takes this particular form that i have written in the box item okay um any questions so far because this is the param this is of paramount importance because this is what we are this is the idea that we are going to use uh multiple times uh when we optimize uh like when we when we you when we look at we


and diffusion models all these models right they work in this particular principle that there is we are looking at a latent variable model okay what is a latent variable model it is given by where the distribution over the data is given as a marginal over the joint distribution of the data variable and another unobserved variable denoted by z called the latent variable okay the goal is to minimize the k divergence and find out the parameters theta now we cannot


do it because exactly we cannot do it because uh we do not know what the latent variable is So we assume a distribution over the latent variable called I mean denoted by q of z given x Once we assume a distribution over the latent variable there will be a lower bound that will be constructed on the objective the log likelihood that we would want to maximize right and when we are maximizing it we would learn both the model parameters theta and the distribution of the latent variable by maximizing the lower bound


And that lower bound is given by this expression right Expectation of log of p theta x and z divided by q of z given x And the expectation is over q of z given x So this is what we optimize whenever we are looking at VAEs and diffusion models and so on


Any questions on this Please ensure that you understand this like right I mean then after that we will continue yeah

speaker_2: Yes so this Q of Z given X is also unknown right So how do we compute the X

speaker_1: I I Ill tell you Ill tell you that I still know we dont know what Q of C connect thats why I said no the look at the box item it is an optimization joint optimization over theta and Q


You have to compute both theta and the cube


Theyre jointly estimated

speaker_2: Well cover that right so

speaker_1: Absolutely thats exactly what well do


Any other questions


So this broad philosophy of what we are doing is clear I suppose Okay Now we took an example after that the last class which is a Gaussian mixture model Gaussian mixture model is a latent variable model Okay Its a proper latent variable model where p theta is given by again marginal of the joint distribution marginal over the joint distribution of x and z right and this is the definition of a gmm no this equation second equation period of x is given by a linear combination of multiple gaussian distributions


having different means and variances Now a set of parameters are the mixing coefficients which are alpha 1 through alpha m There are m number of mixtures m number of means and m number of variations Sorry variances Now what do we do We want to solve that optimization problem right with respect to theta and q right How do we do it We do it alternatively First we solve for theta assuming that q is known and then we will solve for q assuming that theta is known


Now what can be shown Raghavendra I said this last class maybe I have forgotten See this is in GMM the way to find this Q you said that Q is unknown no What can be shown is that at a given theta the optimal Q okay that would make the lower bound tight What do you mean by lower bound tight The lower bound that we have constructed on the log likelihood will be equal to the log likelihood That is the best value that it can assume no Lower bound


can assume the best value which is equal to the log likelihood Now that would happen if the q the choice of q that you have made for a given theta is p of z given x


So if Q is fixed to be P of z given X or P theta of z given X


That is the best estimate for Q


Its all right

speaker_2: I mean sir uh we we said that we would cover this in the TA session but I think last session we did not have it so maybe well cover this in the next session

speaker_1: I meant is no no what I meant is what will be covered in the session is that the proof of this that optimal Q for knowing a particular I mean for given a particular theta is P theta of z given x


This will be covered So this is an algebraic proof But what is important is that I mean see I didnt do it in the class and I dont want to do it in the class because in VAEs and diffusion models we will not use this because in neural models we will not know what p theta of z given x is


Thats the reason So the jump from mixture models to like autoencoders I mean VAEs is because of this fact See had we knew p theta of z k 1 x then the problem of latent variable models is solved because you have the EM algorithm and this can be done But since we do not will not know what p theta of z k 1 x is that is why we need to move to something else So please note this everyone


So again Im reiterating it its very very important So now the goal is to find model parameters theta and the variational distribution or the latent variable distribution Q together


Now there is a result that would show that the optimal Q or the optimal distribution over the latent variable is actually P theta of Z given X


Now if you know how to compute p theta of z given x then it is done Because we know what the optimal what we can do is we can do this alternative optimization where you start with a random theta right and set this q to be equal to p theta of z given x when we know how to compute p theta of z given x okay And then with that q you find the next best theta and keep alternating between them


Okay now how do we know p theta of z given x p theta of z given x is given by the Bayes rule okay which is written here And in the case of a GMM or other mixture models we know how to compute p theta of z given x given a particular theta And therefore we know how to compute Q optimal Q Understand So once we get that optimal Q what do we do that We plug in that optimal Q in this evidence lower bound f theta okay and optimize the


take a derivative of that with respect to theta and then find the new theta with that new theta you again compute p theta of z given x and keep alternating between them which is called the expectation maximization algorithm


Does it make sense So I have said this also right So yeah so the question is however what if p theta of z1x cannot be computed So if you have models and in a Gaussian mixture model or a simple other mixture model p theta of z1x can be computed If you cannot compute p theta of z1x you dont know what your optimal q star is And you do not know what the optimal q star is How do you compute how do you estimate the parameters of a latent variable model is the primary question that would be that would be


Take a nap A


Does it make sense Any questions so far


This is exactly what we do in GMM right GMM is also a latent variable model okay We estimate f theta or we estimate theta and q alternatively and this algorithm is called the expectation maximization algorithm And for EM algorithm to work no we need to know what the optimal q is or we need to be able to compute p theta of z given x


It is


Please ask questions if you have any then Im waiting

speaker_3: So in this EM algorithm which we have mentioned we are trying to find p theta of z given x


using the Bayes theorem so but the p theta of x given z is also unknown right

speaker_1: theta of x k x given z x given z is known no because that is a single parameter Gaussian its actually a Gaussian distribution by assumption by construction by definition


and I go back to the next slide


I dont intend to like teach GMMs anyway so here now yeah that is what I have written here look at this

speaker_3: For a given z we have p theta of okay

speaker_1: Its a particular Gaussian See in a GMM the way you model the distribution you show that


This is how we model it now p theta of x is given by this linear combination of multiple Gaussians


Okay now this can be written this way right there so this is equal to


equal to one to n


e theta of z into e theta of x given z

speaker_3: Yes sir

speaker_1: So this it is alphas okay and this every one is a Gaussian


With a particular let me write this the beta dot z


is equal to some particular j the mu j and sigma j


Alright so we do know that


The conditional of X given a particular Z is a single component Gaussian

speaker_3: Understood sir

speaker_1: Any other question on this

speaker_2: So does it have to be a convex combination

speaker_1: in mixture model yeah yeah yeah in mixture density is always taken because the reason is uh if you look at it now alphas are distributions over discrete uh variable z isnt it


alpha will give you a discrete also p theta of z given j is given by alpha j right which means that if we take


over all j they should sum to one and all of these have to be non zero because they are probabilities no


So they have to be all that is why it has to be concurrent coordination


And by the way a mixture density right you dont add the mixture density need not be a Gaussian mixture model no it can be exponential mixtures or Bayesian I mean sorry Bernoulli mixtures or anything


To model uh data which which has infinite support and uh like the the vector value which lies in continuous space right usually GMMs are preferred


And did I also talk about the clustering See one other thing in a latent variable model is tell you post training


So training is what training is uh like estimation of theta thats what training is all about


After we estimate theta okay a latent variable model


The different variable model can be used


can be used for


policies


This can be any latent variable model including a GMM The first thing is


Uh sampling or generation because these are generating models right


Now example how do we do it in GMM is that in a GMM


Now first you sample a Z from


Im discrete


alpha 1 alpha 2 up to alpha m so note that all of these are estimated using the EM algorithm once you estimate them this what is this is actually a tossing an m phase die so first you do that and then


Sample X


X given Z okay by Gaussian so lets say that the outcome of this is


i is the outcome alpha i is the outcome


Uh okay so lets call i is the outcome


Once you do that what you should do is sample an X


By Agashen which is the which has the ayat mean


And I have the variants thats all


Yeah thats all it is So this is how you do a generation in a GML


Whatever x that you get now by doing the sampling this is z equal to i you do that sampling via a Gaussian in fact if you look at the Bishops book which is like


classical book by bishop pattern recognition so what you will see is that he has shown uh what will happen uh if we do sampling i mean if we fit a gmm to mns data and do a sampling it will look like some images right but it will not be like as good as it says some other generative models such as gans so what happens is no in very high dimensions uh these gm gmms they often tend to


have this curse of dimensionality and they will not uh model the data well so that is because of the saturation of the EM algorithm again NOI


Since I am not teaching GMM I am not going into details of it but yeah Okay This is how you sample from a GMM I will talk about how do you sample from a from a variational autoencoder But yeah So what is more important is that one can use a latent variable model to do sampling or generation The other thing that can be used that these models can be used is what is known as posterior inference


Posterior inference okay


also known as feature extraction feature or embedding extraction


becomes embedding extraction if


This is uh or its also called as clustering


f for Z discrete


Now what is this So given


Fine


A latent variable model


Um


And give one


Data point X


Oh you just compute compute


Few starters


the g on x thats all so this lets see what happens is uh if in in the case of uh uh q


Let us say it that way compute or sample from either both of them are possible Ill give you I mean there are different variants of it okay now let me tell you what it is compute


will start of G G1X


Or sample number


depending upon what the case is Okay so what do you mean by this


So given a data point x now post training given a data point x I am finding out a distribution over the the latent variable given the data point


So lets say that uh let that Z is uh discrete then what will happen you take Z is discrete


If Z C is discrete we have values one through M so C can take M values


z can take 1 through m values So if you are computing q star of z given x what will happen is there will be a discrete distribution over z


There will be an entire distribution over Z what is this


This is called clustering


So every x now is divided into one of m possibilities right that is that is clustering okay Now if z is continuous then what will happen is given a


given a given a given an x okay so youll find out a z given x okay which is a sample from q of z given x that particular z given x this will be a vector


turns on rk where that is where the z lies so this is typically referred to as the embedding so all these bird embeddings etc that you see no textual embeddings and image embeddings etc are nothing but samples from uh the posterior the latent posterior given data so this is one other usage of latent variable models


That is why now we say that we can do clustering using GMM right So GMM is a latent variable model with discrete latent space okay And thats why we can do clustering of it It is either GMM or K means K which is a special case of GMM right All these are clustering methods


Under the hood what is happening is that you are estimating Q star of Z given X So two things can be done right One you can do sampling or generation okay which is simply the generative task that we were looking at The other thing that you can do is what is called as posterior inference that is that given a particular point X you can find out Q star of Z given X Is this okay So these are two tasks

speaker_3: So do that


Sir in the embedding case the received vector will be a one hot vector right

speaker_1: No no no no no uh I mean you mean the X you are talking about is it

speaker_3: No sir um Z given A the the resulting vector

speaker_1: No no no it is not one one one one hot no see thats what Im saying think of an autoencoder right you have an encoder decoder model I cover all that detail in detail but Im just giving you an overview here so if you have uh like lets i mean if you know what bird embeddings mean there is a pre theres a trained model you pass it through a trained model right your x which can x can be one hot and you will you will get a particular vector at the output thats all it is


That vector is a sample from ZQ on X yeah thats your embedding

speaker_2: So why do you call it as a sample so that means uh for a given x you can get a different values of z

speaker_1: The reason Im calling it as a sample is because in in in whenever the the uh the


Latent variables are continuous no You wont get an entire distribution over z given a particular x


especially in in in in in cases like uh BERT and all that but as we will see uh in a VAE right uh Q is modeled I mean the you you you will get an entire distribution over the Z okay but typically when people call it as embedding extraction no its always a sample from Q not an entire distribution see I just wanted to make this distinction that if Q is discrete then given an X you get an entire distribution over Q sorry


Right but when Q is continuous typically typically what happens is you get a sample from Q star not an entire distribution I just wanted to make the distinction


Any other question So two I mean remember these two things no I mean this is how the VAE paper starts also that the goal is to do two things that given data you need to first learn a latent variable model which is by maximizing the likelihood or ELBO Second task is to after you have completed your training we need to do generation okay or sampling and then we do posterior inference So let me write it in the next thing itself

speaker_3: Sir which paper is it uh what Ive I forgot the name you mentioned

speaker_1: Are you looking at my handwritten notes


Because there I have like at the end of my every each notes I tell you the name of that paper but I encourage all of you to actually look at my handwritten notes its very lucidly written

speaker_4: Its very lucidly written


Its a Kingma and Willing

speaker_1: Yeah Velling and Kings paper I tell you the name see whats important is dont digress whats important is that you all of you look at my handwritten notes at the end of my handwritten notes key papers are listed and I expect and by the way for the exams I think this is the way to make you read right there is only one way for your exams right all the papers that I have listed in my handwritten notes at the end of them they are they are a part of syllabus


so you are supposed to read those papers there are only four five papers per topic so please read them yeah so the name of the paper is uh vaes paper is auto encoding variational ways


If you google for VAE original paper youll get that But the title is auto encoding variational base So please read my handwritten notes once and the citations that are given at the end of each chapter I urge all of you to do that Okay So now the problem here is that given D which is data


samples from


Examples drawn ID from an unknown distribution PX Okay the goal is threefold


Little now


Learn a latent variable model


Unknown


in posterior right I mean this is what it makes different from uh EM okay if you read the introduction of that paper no they will actually say that uh because P of P theta of Z given X is unknown we are assuming that it is not known we want an alternative method because otherwise in fact they explicitly say that EM cannot be used because we dont know what P theta of Z given X is okay thats the first goal the second goal is that you need to do


generation


Sampling post training


Third goal is to


Enable posterior inference


which is nothing but estimating the u star of the


Okay so these are the three goals that are cited in the VA paper or maybe let me just show you that Itll be nice to see that once


See a lot of times right we uh these uh BAE paper


These papers are sort of intimidating but one of the goals of this the one of the goals of designing this particular course was to ensure that you people start reading papers students start reading papers and you know you dont get intimidated looking at it okay so they will say the following here


So we are interested in and propose a solution to three problems in the above scenario right Efficient approximate maximum likelihood estimation for parameter parameters of theta Thats not very good map estimation Its the efficient approximate maximum likelihood estimation of parameters of theta Number one The second thing is efficient approximate posterior inference of the latent variable given an observed value x for a choice of parameters theta For a choice of parameters theta meaning post training And this is useful for


For coding or data representation tasks that is what is meant by embedding extraction or representation learning Second thing is you need to efficient approximate marginal inference of the variable x This allows us to perform all kinds of inference tasks where a prior over x is required Common application in computer vision include image denoising inpainting and super resolution All these are generative tasks


So these are the three questions that is asked So this is that paper which is VAEs paper We will go into all these details and math in a very that is what we do in this lecture But yeah so these are the three questions that are of interest which is learn a latent variable model with unknown p theta of z on x Oh I should also show you that now that they say that EM is not feasible


interactability look at this no the first point here in one two interactability the case where the integral of the marginal is intractable


Where the true posterior density p theta of z given x is intractable So the EM algorithm cannot be used


That okay

speaker_2: So it is intractable because we need to do it over all values of Z or

speaker_1: Well not necessarily right I mean for instance if you assume z to be continuous variable with unknown distribution its you cannot find that integral one thing The other thing is see observe that p theta of z given x involves a division by p theta of x which is again an integral over the joint distribution and this integral is over z So if you assume z to be of very high dimensions that integral cannot also be computed

speaker_2: Okay yeah got it

speaker_1: Yeah so because that is why EM cannot be used here and we need something else other than using EM Thats the prelude So please read See these are sort of seminal papers okay which are very good to read and youll gain a lot of insights I have gained a lot of insight by reading those papers as a student So please do read them I recommend all of you to read that Similarly that FGN paper


I dont know if I showed you that so we covered that no this if GAN


its variational divergence minimization lets see yeah this one training generative neural samplers using variational divergence minimization so this is what we actually covered in class


So this was the paper that I covered in class in all these lower bounds that we constructed etc So with the background that you have right now please read the paper Its short and extremely insightful


I urge you to read all these at least these fundamental seminal papers okay


Right so we have these three objects


To to learn given the data we will start doing it okay So now


Recall


latent variable model


each other


k1 by the integral of p theta


given z times


the shift of the whole DC right so is also equal to the joint distribution of


Now the goal is to learn


Longita star


That would


Maximize the log of the likelihood


So we saw that this is uh


Approximately


MS


finding out the


theta such that the lower bound on the evidence is maximized which is the evidence lower bound where


Okay now f theta


Q is given by the expectation of log of


Eat it up


X and Z divided by


You off


Cythonics


respect to Q1 C1X right


A few with me so far


Now we need to find the theta such that it is maximized Now let us simplify this


You to see you on next


Slow down


beat here doc


Given Z times P theta of Z divided by


It off


See you guys next


is equal to expectation log of


E to the top x given z


Thank you all see you guys next


Minus


Expectation see you next


Mm


Two or three given X divided by


into the c


All right I just used two things here one linearity of expectations and law of logarithms Any questions on this stuff


did I do there is log of a b divided by c I wrote it as log a minus log c by log b so minus came here because I I inverted the numerator and denominator


Is it alright


Hello are you there

speaker_2: Yes sir

speaker_1: Is that alright any questions on this


respond how do I know uh maybe Im not uh this is all right no yeah okay uh okay lets move on so this is


Expectation of law of


theta of x given c and this is with respect to z given x minus whats the second term can can you recognize the second term

speaker_2: real divergence of QZ given

speaker_1: Yeah and the

speaker_2: And the end

speaker_1: The decay and divergence


between u and z given x


Be careful


So this is


Actually the last function of a VA okay this is thing but elbow right we are writing the evidence like like evidence lower bound expressing this this way so this if you want to remember something this is something that you would want to remember this is D


Conditional


Ill let you hear


Okay let me interpret it later Okay so this is the equation So you have LBO can be decomposed into two terms one which is an expectation of log of p theta of z given x given z and there is a clear divergence between Q of z given x and p theta of z Okay


Now what is done in a VAE is that the first thing that you do is


Approximate

speaker_3: So one question


For this to be KL divergence there should be a p theta of z term also right before log

speaker_1: should be a q of z given x term

speaker_3: Yes q q of z given x

speaker_1: Theres expectation is there no expectation is integral QZP is Linux log of QYP isnt it

speaker_3: Okay okay

speaker_1: It is


is integral using the on X


log of plus e one x divided by


That scale no


Okay so whats important now is that you approximate p theta of z sorry p theta of x given z


And


U or Z here next


Giral networks


So lets call that as q phi because there are two neural networks neural networks theta neural networks with parameters theta and phi


Okay so what we do is you look at this elbow right There are two distributions that we are talking about here which is Q of Z given X which is the unknown posterior Okay the other thing is P theta another thing is P theta of X given Z We represent both of them using neural networks Now observe the difference here from the EM algorithm right In EM algorithm Q of Z given X the optimal Q of Z given X was known to be P theta of Z given X


because because we dont know what p theta of j given x is we approximate that using a neural network now the question is what do you mean by approximating okay let me write that


Its important as question


Waters


What is meant by


Approximating distributions using neural network neural networks


Approximating distributions


using your own devices


very important there are two ways here right see one way is that there is a there is a probabilistic way okay


And there is a deterministic way


Now what do you mean by a probabilistic way Lets say that there is a neural network here


Now this


This is the QV


or Z given X


Now this takes


sample of G as input okay so G


Neural networks are deterministic functions which is that you know you give a fixed input it will give you a fixed output always right So now a sample of z sample of x sorry a sample of x it takes as an input and what it gives out are


Atomizers


a distribution


of z given x So this is typically called as the probabilistic neural network where a neural network will give you the parameters of a distribution Now typically lets say as an example


If Q of Z Q on X


is assumed to be lets say a Gaussian of some mean and variance


Okay this neural network will give you mean and variance as output


So this is called the probabilistic way of representing a distribution using a neural network A neural network will give you the parameters of a distribution So note that in most of the probabilistic ways of representation you assume the underlying distributional form for the distribution that you are assuming What you make your neural network output the parameters of the distribution


Probabilistic way Okay Theres a deterministic way which we have already seen right which is


because typically in latent variable models at least x will have a larger dimension compared to


Doesnt matter but yeah so just to ensure that it is consistent so if you are doing it in deterministic way lets say that you are modeling some


p theta of x given z right now itll take a sample of


you a sample of Z okay it will give you what what will you give you what will a determination network give it will give you a sample


simply give you a sample okay x cap from p theta of x given z this is the deterministic curve so here the neural network is not giving you parameters of the distribution but it is giving the samples from the distributions example


Is a is a is a GAN generator no


A GAN generator is a deterministic neural network I mean all neural networks are deterministic that way but a GAN generator is modeling the conditional data distribution in a deterministic sense So what do I mean by that I mean to say that it will give you a sample from the distribution that it is modeling but not the parameters of it

speaker_3: Sir but for a given z also lets uh this uh the sample x will be different right

speaker_1: No no no not in a in a in a in a GAN in a GAN right if you fix z it youll always get the same x no because neural networks are deterministic functions


Thats the whole point that Im trying to make See the variability in the generated data comes because Z has randomness into it right Because we know that Z typically trampled from a content distribution Thats why different Z will give you different Xs But post training a GANs generator or for that matter any neural network is a fixed function right


Given fixed input it will give you a fixed output there is no stochasticity in a neural network by design


Does it make sense

speaker_2: So one question so in the probabilistic way so we estimate only the parameters for only one distribution or a family of or a group of distributions

speaker_1: Yeah see it is one distribution in the sense that if we are looking at Q phi of z given x right Q phi of z given x is actually Q phi of z given one particular x always isnt it


This this mu and sigma will be a function of x

speaker_4: Okay

speaker_1: for a particular x But if you are saying that you know the same neural network neural network is being used to estimate the Q phi of g given x for different values of x then you are estimating it for a family and thats what is happening


Because once you try given one particular x it will give you the parameters of q phi of z given that particular x


Okay okay

speaker_2: It gener it generates a family itself right and

speaker_1: uh right i mean see uh for a given x it does not generate a family yes correct to be clear about it right when you say see there is no stochasticity associated with the neural network so for a fixed x it will give you a fixed output


In the probabilistic way what will happen is that there will be that that will be seen as parameters of impact How do you do it practically is that suppose mu x is lets say that z is in some k dimensions right then what we will do is this output this neural network will have k plus k squared dimensional output now because sigma will have k squared parameters mu will have k parameters it will be k plus k squared


stacked into a long vector that is the output So now for one x it will give you one output and that can be interpreted as the parameters of a distribution So it is modeling a family in the sense that for every x it will give you parameters corresponding to that

speaker_2: Got it

speaker_1: So Ill ask you a question now What do you think what way do you think these are the only two ways that you model that use neural networks in any task okay Here is a question What do you think a classifier a KA class classifier is doing Is it a probabilistic model or a deterministic model

speaker_2: Probably will distinct

speaker_1: Why do you think its a probabilistic model


So what is the classifier model by the way what distribution is a classifier modeling take a classifier what distribution does it model you take an x as an input what is what distribution is it modeling

speaker_3: The line

speaker_2: giving the probability of the classes

speaker_1: This is what it models right


All classifiers model PT top by Gionx


the so called cross entropy loss that you use is actually minimization of KL divergence no actually its minimization of KL divergence between the true posterior label posterior okay and the neural network model posterior this is exactly what you do right when you minimize this is cross entropy because the other term which is the entropy term will be independent of theta the first term right which is expectation of log of


p theta of y given x with respect to p of y given x this is what you minimize negative of this is what you minimize which is the cross entropy term which is nothing but the k divergence right so even a classifier is doing the same thing that they are doing right it is doing a maximum likelihood estimation or minimizing the k divergence but now the output what do you get do you get a sample from this distribution or do you get the parameters of this distribution so lets say that y is


is a discrete distribution that will take one out of k values


Uh with


probabilities P y 1 to P y 2 up to P y k So post training when you do an inference for a particular x what do you get at the output Do you get a sample from the P theta y given x or do you get parameters of P theta y given x

speaker_2: Get a sample

speaker_1: you say so do you get one of the case that depends okay okay so here is the answer right the way to look at it is so if you look at the entire classifier suppose you take the final layer to be the argmax of logs


Okay then it is a sample


But if you stop at logits


Then its actually a distribution probabilistic way


You see that if you take the logits right then its it sums to one right and its all all non negative Okay which is the softmax if you take the output of the softmax and which is the Logits no even before the softmax you take the logits then its an entire distribution Okay you can see that as you can interpret that as parameters if you take the argmax Okay take the softmax and then take the argmax of all possible values then it becomes


a sample of this discrete distribution


Anyway so


Not something that I intended to say But anyway so these are two ways to model distribution right One is the probabilistic way where the neural network gives you samples from the distribution that it is modeling and the deterministic way where the neural network will give you samples from the distribution that it is modeling Okay Now what do we do in a VAE


few


Distribution Q phi of Z given X is modeled


There are multiple instantiations of it okay


modeled probabilistically


about realistic


And P chi top x given z


is modeled


using either probabilistic or deterministic you know as the case may be yeah I I tell you there are these are different instantiations of same idea right probabilistic or


So basically both of them are modeled Q phi of z given x is always modeled probabilistically Okay P theta of z given x can be modeled probabilistically or in a deterministic way Okay Let us see one instantiation where you have


Okay so now data is a set of X is


We have end of them


have sampled from BXU have right now typically X is in some RD


In all latent variable models Z is assumed to be in some R K okay where K is much less than D


is how it is done in the variable models now what will happen is there is a net neural network


This neural network takes xi as input one of the xis as input and this is modeling q phi of z given xi


Now this is as I said it will model it probabilistically So in one of the instantiations of I mean one of the naive implementations of VAE now Q


P of Z given X


It is assumed to be a Gaussian


Its a distribution in Z the mean of this is mu


of x because its a function of x the variance is a function of x


Typically it is assumed to be uh you can model it to be a diagonal matrix okay


diagonal matrix of uh


My one true secret


Let us call this as sigma of x sigma x vector okay


Now what will happen is that in a in a in a in a VAE this will get mu


of xi as the output


sigma of xi as the output okay now note that both


x and sigma x lie in k dimensional spaces right because i have assumed sigma x to be a diagonal matrix they both lie in k dimensional spaces that means that the the output of this you know this will be a


dimensions this will be


Two K dimensions


This is uh this is also called the the encoder network


simply modeling through P of G given X using neural networks but there is another neural network we said that we also model P theta


So this will take zi which is a sample from q phi of z given xi


input and then this is model p theta of x given z so now lets say that this gives you a sample


In this case Im assuming that this is a model deterministical okay this network is also hold on


This will take zi the sample from qv of


given xi as an input okay and this this this network is also called the decoder network


This is a VAE Okay Now one thing that is to be noted here is


Of course this is k dimensional this will be d dimensional


Now see one thing that has to be noted here as I tell you


There is no


Connection


Between the


Incorporate decoder networks


they are not connected at all right so what is happening is given an xi


So you first get the uh the parameters of the distribution Q phi of z on x


Having those parameters you sample a gi from qp of z given x okay and give that gi as an input to the decoder to get a sample from p theta of x given z


Here the output of the encoder right does not go as an input to the decoder


You see that


The output of the encoder does not go as an input to the decoder I should write that So this means that the output


be encoded


Who has


Input


decoder


Uh is this setup clear now what is happening


Well have to now see how to train this or rather how to get the parameters by optimizing the elbow and also we have to see how to do generation and inference later post I mean because you remember no we had these three goals that you learn a latent variable model enable generation and enable posterior inference well see all that to be done but in terms of like architecture is all of you clear on what is happening

speaker_2: So the input to the decoder is a sample from Q of


Uh give an example

speaker_1: of ZG on extract

speaker_2: So we indirectly use it right because uh

speaker_1: Oh we go

speaker_2: The distribution

speaker_1: Im not saying we dont use the encoder network Im saying that the output of the encoder does not go as an input to the decoder


I didnt say that we are not using the encoder encoder is very much used

speaker_2: but its used to only determine the parameters of the distribution and then we sample

speaker_1: It is using the parameters of the distribution and using those parameters you sample okay and once you sample use that sample as an input to the decoder

speaker_3: So I have one question

speaker_1: Yeah go on

speaker_3: for q p z of x we say that is a normal distribution on the variable z with mean mu x and sigma variance sigma x so while this mu mean and variance are on the or on x they should be on z right

speaker_1: Ah no no no they are see they are okay I mean that they are functions of x see look at this now I have said that both of them lie in Rk which means that they are in these space but they are functions of x


See when I write off something it means that there are functions

speaker_3: The pot

speaker_1: Im talking about them being function subjects

speaker_3: Okay but they are uh but they are over the Z since yeah

speaker_1: Ill look at that

speaker_3: The damage

speaker_1: Absolutely absolutely


See a neural network is taking an xi as an input no that theyre thats why its a function of x

speaker_3: part itself

speaker_1: So I mean I want all of you to like strictly understand this and clearly understand whats happening otherwise everything that we do next will not make sense So please ask me questions if you have on how this thing works I mean architecture

speaker_2: K is again a hyperparameter here or

speaker_1: Page I have a parameter yes

speaker_4: Sorry one query here the decoder network we have found out deterministically

speaker_1: Uh see we are just yeah yeah we have at least in this uh exam instantiation I have made this uh deterministic because I say that it gives you a sample from p data of x m c yeah

speaker_4: Does it maybe you might cover it later you can say that I mean like whether it changes when you

speaker_2: it probabilistically

speaker_1: Yeah you simply get the parameters of p theta of x given z No thats all Instead of getting a sample from p theta of x given z you get parameters of p theta of x given z Then it becomes a probabilistic thing

speaker_4: Got it then again from that parameter we again uh use that

speaker_1: Yeah you do sampling but typically right in a in a naive implementation of VAE the output of the decoder itself is taken as a sample from p theta of x given z


But yeah so later like in the class no I will also give you one example where it is taken deterministically as well But for now let us think that it is I mean sorry the probabilistic but for now let us think that it is deterministic

speaker_2: Sure thanks

speaker_1: Okay

speaker_2: Yeah sir so for a given xi the xi cap which we get from p theta might be different right Because we have a sampling step in between and that might lead to a different z i

speaker_1: I am not even saying that you get uh like xi at the output of the decoder right decoder will just give you a sample from p theta which you know I have not established any relationship between xi and xi cap yet


Okay if your question is you know why where is that so called quote unquote auto encoding happening here right We will see that We will see how to how does it come out okay

speaker_4: So this sampling process of lid uh from q of e right so is it like generally uh having a random sample using like like a random function

speaker_3: Yes

speaker_1: Yeah yeah you use the standard samplers so you can suppose if you model your q to be a Gaussian distribution then you can use that like standard random sampler for this


Okay so is the setup clear to all of you now what we should do is like with this


this now the elbow will become a function of


Yeah theta and phi which is given by the expectation of log of e theta of x given z and this is with respect to q phi of z given x minus the k l divergence between


View view view next


okay this is what it is what we should do is that


You should solve this I dont theta star and V star


simply the


what we need right we need to train both of these neural networks so how do we do that we do it using gradient descent right so we need


the gradient of


Elbow


respect to phi and unit gradient of


the elbow with respect to theta this is what we need right because finally what we do is this is how we train the neural networks


assuming that we are simply doing a SGD rate first order gradient descent


Heres how we do it so we need the gradients of the elbow with respect to both phi and theta under this


I think somehow the pages are sizes are going heavier


I should not zoom out and zoom in arbitrarily I think Yeah Let us keep it this way Okay So now with this modeling choice that we have made no we have to ensure that we get the gradients of the lower bound with respect to phi and with respect to theta Okay And then we can of course use gradient design tool to train both of these networks Is this all right Now what we will do in the rest of the classes So getting this gradient right with respect to gradient of the elbow with respect to


is a non trivial thing and you might have heard this term reparameterization right it is used in VAE like so called reparameterization that comes into picture to calculate this gradient itself so calculating this gradient with respect to calculating the gradient of LBO with respect to the encoder parameters needs this idea called reparameterization because of a simple fact look at this no


the there is a sampling step that is involved okay which cannot be differentiated so i i will show all that you know very rigorously but the basic idea is that there is a sampling step and the encoders encoder and decoder are connected via the sampling step but sampling is a non differentiable operation and you back propagate no through chain rule you have to back propagate lets say that you start from the output of the decoder back propagate all the way through the input of the decoder from there


should go to the output of the encoder and those two are connected via sampling But sampling is a non differentiable operation So what do you do to find the the gradient of the ELBO with respect to the encoder parameters is what we should look at next That is done through this trick called reparameterization trick that I will discuss


Okay so I think shall we take a break 15 minutes break


10 40 10 48 now


A good time to stop yeah


Oh my mistake okay yeah shall we take a break


Uh Satya go ahead

speaker_4: Uh yes I can they can take a break I own question on the assignment

speaker_1: maybe later after the class yeah please do ask me after the class okay so now uh yeah it is 10 49 in my clock we started uh late today no 20 minutes late so lets cut down the break lets get back at 11 5 okay in 15 minutes lets come back lets come back at 11 5 and uh finish the report from my parameters so dont miss the next part of the class no its pretty important okay see you in 15 minutes then bye


Shall we continue


Okay


So uh Sylvia Minnow right


Can you hear me


Okay nice Okay so we were looking at now computing the gradients of the encoder and the decoder parameters with respect to sorry computing the gradients of elbow with respect to the encoder and decoder parameters Okay now okay so what do we so lets take one term at a time you know there are two terms in elbow So consider


um computing


computing the


Radiance


Ill go


Respect to P and Q


You consider the first term in the elbow consider


If first turn available


which is the expectation of


Log


Each top x given z


with respect to


The obvious hit and its okay


Now


does it look like suppose um look something like this no this table


you have an expectation of


some function


Please note that this z you know what is this z here x given z what is this z the z


Z is being sampled from Q phi of z given x right


Right So this entire thing whatever the log of p theta of x given z is log that is also a function of p


understand that please let me know if you dont understand so this is of some random variable v okay and the expectation is with respect to a distribution


a PV and this is also a function of P


So just giving you a simpler example


with us


Let me use a different parameter maybe lets call this as some psi and we have some distribution


This random variable do you agree that it looks like this Any questions on this


okay let me write it on me itll be easier that way


The up side of V is actually


Naga


theta of x given z okay and then p psi of v is simply


You know next


V Z okay and Psi is


Is this okay


Hello Im Audible


Fine so now what do we need is that we need the gradients of this expectation


This gradient has to be with respect to the parameter size correct


is what we are seeking now let us write this down so this is equal to

speaker_3: Sir sorry to interrupt Instead of going for psi cant we straight away use the like like phi Otherwise it will be it will be a bit confusion

speaker_1: A the reason I didnt use phi was you know phi has been taken as encoder parameters I can do that


Let us keep it that way no I have written it down so let us have it that way


This is equal to


Mm


RTN


of integral


respect to v we have p psi of v times


psi of v dv right this is definition of expectation and we can move the gradient inside because expectation is a linear operator right we can move the gradient inside this will be p psi of v times


So youll be correct


Now what do we do now next Can somebody tell me


use staying rule this is


The idea go


uh the gradient of


one function


James


psi of v dv


Plus


The gradient of


the other function


what it is right now what is the first


Look at the first term right you have


some function here and the probability distribution here what is that and theres an integral what is that this is an expectation of


gradient


respect to psi of v


This is not an expectation


This the first term now can be approximated using one over n


one through n and you have


of vi where vi is coming from p psi of v right this is again lot of last numbers we know how to estimate expectations approximate expectations but this


return


as an expectation


And therefore therefore


and we compute it


You see this See this is the problem See when I said that you cannot differentiate through sampling so look at what is happening See there is an expectation of a certain function and that function is parameterized by some set of parameters right Now the expectation is with respect to a density okay And that density is also parameterized by same set of parameters


So now if you want to do that if you want to now take the gradient of such an expectation of a function that is see typically what happens now in most of a neural network training you need to take the derivative of an expectation of a function with respect to set of parameters and these will be neural network parameters But this expectation will be typically over lets say px where px are simply the distribution of data which has nothing to do with


model parameters and then we approximate this expectation with respect to I mean using the samples that we are given which are the true data Now here is a case okay where you need to take the gradient of an expectation okay with respect to our density function and that density function


is also parameterized by the same set of parameters with respect to which we need the gradients


see that and why is that happening if you look at it that is happening because our encoder network is made probabilistic you know when we make our encoder network probabilistic okay then the the parameters that we are getting know of the expectation of of the distribution with respect to which we are taking the expectation uh is uh that the distribution also is parameterized by same set of parameters with respect to which we need the uh


the the derivatives


Algebraically speaking what happens is that if you take the gradient you cannot express the second term that comes up in the gradient of the expectation in terms of sample averages And therefore that cannot be computed Is this point clear to all of you


This implies so if you want to generalize this implies


the gradient of the first term in elbow which is the expectation of log of heat heat of x given z with respect to


Q V of Z Unix okay


This cant be


Muted


Cant be computed directly is what it means


Can you all appreciate this fact


Any questions on this See this is the key part okay this is what this is where we need uh what is what what we call as the reparameterization that we will see but is this clear


Any questions on this


Am I already


questions great now what do we how do we solve this solution


as the reparameterization trick


Okay now what does this mean Recall that we had


We wanted the gradient of


expectation of some function of some function that is parameterized by some parameters and the distribution was also parameterized by the same set of parameters right we wanted this now all we need to do is


It wouldnt be computed


Correct So what you do what you do is


or express express


Dumps up


Another distribution


distribution which is


Independent of


Exactly what is called as the reparameterization okay Ill tell you the parameterize


So what does this mean This means that lets say that


Suppose


there exists


A random variable


epsilon okay its some distribution p epsilon okay so note that this is independent of


ID parameters


Such that such that your v which is the random variable of interest


some function of this epsilon


Then then


the expectation of


respect to


E psi of V can be shown to be equal to the expectation of


F psi of what is V now V is equal to G times epsilon


And this expectation now will become the expectation with respect to PFSR It is either you take it as a homework or it can be taken in the DS session just to show that these two are equivalent Okay It is also called the law of the unconscious statistician Okay Abbreviated as LOTUS I mean this is a standard probability proof You can just do it Two steps you can show that So now what did we show That


There is this random variable V right with respect to which we are taking an expectation Now we represented that random variable okay in terms of another random variable epsilon


a function of another random variable epsilon that is independent of these parameters uh psi


And if you do that then the expectation of the function with respect to this random variable p psi now will become an expectation with respect to another random variable p epsilon that is independent of the parameter psi


So this is what is called as reparametrization right I mean this g function is called the reparametrization function

speaker_2: How do you find this epsilon

speaker_1: good question now that depends upon uh like in the vae paper no they give multiple ways to find this epsilon and g its not enough if you only find epsilon you need to find g also you need to find an epsilon and a g such that this happens ill give you examples of how to do this okay at least in the in the case of uh like the naive implementation of vae ill tell you how this is done okay so now this if you do this now its easy right so now um


If we solve the problem the problem was to find the gradient of this


expectation


respect to psi now this is equal to the gradient of the expectation of


This can be done You just now push the expectation inside the gradient inside the expectation and that can be computed using sample averages So now this is approximately equal to take some m samples of epsilon and this are equal to 1 to m and you have the gradient of


F psi of G of epsilon i


your epsilon i you know is sample from p epsilon so now you will not have that uh have this uh in uncomputable integral problem now because the dependency the expectation is not now with respect to uh p psi but it is with respect to p epsilon


Now let us look at the let us look at an example of reparameterization somebody asked me how to do that so example of


Mm


is spelling correct T bar I mean the reservation right here


You know what about me


right okay in v a in particularly in v a e okay i mean this reparameterization is independent of v a or nothing its a general probability uh probabilistic technique okay but yeah ill show you an example of v a e okay let us take the same example where my q phi


of zero on X


u p of z d on x okay is a Gaussian distribution


and it has parameters lets say mu of x and sigma of x okay


is what it is now let us now reparameterization okay so now uh what is phi by the way ill tell you


Mistake in the writing as well


that this mu is a function of phi because this is the output of the neural network sigma is also a function of parameterized by phi a function of x okay now that is why this becomes a function of p now let us reparameterize now let let epsilon be a gaussian distribution with zero mean and unit variance


Okay if you do that then then


Let Z is equal to


mu phi of x plus


times epsilon if I do this


do this then Z will now have


distribution equal to z given x


Now this function right is the g function that Im talking about this is g of epsilon


If you take a a a normally distributed random variable with zero mean and unit variance


Excuse me So you add it with a constant and scale it with a constant If you do that then the output random variable will again be Gaussian okay with the mean and variance given by the scale and the shift


This is a reparameterization


You see that


Is this alright


We have this g function


is simply mu


Uh


This is one way There is another way to reparameterize which is not often used in VAE literature but there is one other way to reparameterize which is called as this is one example


The other example that is given in that paper is what is called as the inverse CDF method We will not use inverse CDF method but I am simply


engineered it for the sake of completeness See suppose


Oh X is a random variable


F x of x


notes its CDF


Well we know that


If x of x is simply


The integral of the


function right over this Now let us call that represent that by some random variable z


No this is a function of the question is question is


What does this mean


distribution


You understand the question Now given a random variable you compute its CDF


Now CDF itself becomes another random variable


Question that we are asking is what will be the distribution of CDF of a random variable Do you know that


Does anyone know that


It would be a uniform distribution


between zero and one


you so please take it as a small homework and show this that you take any random variable okay and show that the distribution of its cdf of any random variable is uniform between 0 and 1 can you already intuitively see why that should be the case if you take the cdf now cdf is a non decreasing function right and it is upper bounded by 1 so which mean i upper it is bounded between 0 and 1 right


the CDF so that should be a uniform distribution between 0 and 1 just I mean this is a standard proof okay so so please find it out in the internet or just do it as a homework okay now the thing is this implies this implies that if I take a u that is uniform between 0 and 1 okay and compute x to be equal to the inverse okay of the CDF that is evaluated at u


Ten ten


Maybe


Distribution of X


Let us call this as x cap x cap is inverse cdf of a random variable x then the distribution of x cap


Its same


And the dog


is the idea Makes sense right See now we know that the distribution of the CDF of any random variable is uniform


Now that means that if you take a uniform random variable between 0 and 1 okay and make a transformation okay using the inverse of the CDF of any random variable then the then the the uh the outcome will be another random variable which would have a distribution that is same as that random variable whose CDF you have inverted


Now in this case in this case


g functions for now epsilon


Epson is uniform zero one


And the g function okay says the inverse


the CDF So this is another reparametrization technique which is called the inverse CDF method


is all right see but the thing is in this case no the only requirement is that the cdf of the func of the distribution that you are modeling using your encoder has to be invertible


which is not always the case and thats why you know more in most of the cases uh in VAs the distribution of Q is taken to be Gaussian and this sort of reparameterization is used you know which is the affine reparameterization is used not the inverse ADF method But I hope that you got the idea behind reparameterization right Let me repeat what is happening here So we wanted to find the gradient of the encoder parameter uh with respect to


elbow right sorry we wanted to find the gradient of the elbow with respect to the encoder parameters that cannot be found out because the the elbow has an expectation of some function with respect to a distribution and that distribution itself happens to be a function of these parameters


So we cannot compute the gradients So what do we do about it The way to do it is represent that distribution with respect to which you are taking the expectation in terms of another arbitrary random variable which is independent of the parameters So that representation through a function is what is called as reparameterization If you do that then this expectation can be written in terms of an expectation over that arbitrary random variable and therefore the gradients of


this function with respect to the encoder parameters can be found out so that is the idea and we saw two ways to do reparameterization which is that if you assume your qp to be normally distributed theres a certain mean and variance the way to reparameterize that is start with a Gaussian random variable which has zero mean and unit variance and scale it with the the sigma and shift it with the mu you will get another random variable whose mean and variance


This is what the Wiener variance of Q pi Q pi is


Any questions so far


Now we will use this to compute the gradients and then back propagate But yeah if you have any questions here please ask me This is actually one of the


idea of VAEs because otherwise its simple right you are like maximizing the likelihood representing the distributions using neural network and back propagating but whats important is once you represent a distribution using a neural network in a probabilistic sense you have to get to reparameterization otherwise you cannot compute the gradients that is the idea


Uh once I dont think

speaker_2: So are we saying that we are transforming the distribution that we get to either a standard normal or a uniform in this case Is that the way to see it or

speaker_1: other way around no we are representing the output the distribution of the encoder okay our distribution that is being modeled by the encoder in terms of standards normal zero

speaker_2: Okay and and the transformation I mean is the g function basically right

speaker_1: Transformation is a g function and thats it thats that that is a user defined function no it is nothing to do with it youre not learning it or anything it is just a user defined thing

speaker_2: And is that also the way we say that okay uh that random sampling process we eliminate and then we introduce some kind of uh a determinism here

speaker_1: No there is still sampling is happening in epsilon mc we are just re representing that in terms of some other random variable

speaker_2: Okay

speaker_1: which is which is which is not a function of the see it is only to do a simple thing all we need to do is express this expectation that is there in elbow with respect to a distribution of a random variable which is independent of the parameters thats all thats all we want to do

speaker_2: Okay so so uh sampling this way uh still allows us the to flow the gradient backwards

speaker_1: I will show you how to do that See now I mean algebraically you are convinced that now we can express this expectation now right


Typically the the the distribution which is uh which you are sampling from is not now dependent on uh phi it is you you got it no


Yeah that is the basic idea any other question


So now let us write what is happening So now what happens is that you have the encoder network


the encoder network okay this is not


to take it as


Yeah Karthik go on you had a question


goes as an input and this is modeling q by of z un x okay now what happens here is this neural network gives you uh mu and sigma so what you do is sample epsilon from normal 0 1


lets call this as psi so given a particular sample you take an epsilon from normal zero one and then do z get your zi


pretty much the same


Uh sigma p sigma p of x


We got this Zi correct now take that Zi


Pass it through the decoder


Did I say yeah


This is what is happening You understood now So do you see the difference between these two Here yeah just zoom it here So here what we are doing is that we started from xi got a mu and sigma sampled from sample gi using that mu and sigma directly from qf and then gave that gi Here when we reparameterize what did we do We got mu and sigma okay Sampled an epsilon from an arbitrary design from


standard normal 0 1 and then got gi by reparameterizing


Is it alright


You know the difference now after re before and after reparameterization


I hope that you got it so now what do we have to do is we need to compute the gradient of


the expectation of


Nah but


Meet you at the


Q and Z with respect to Q V of Z given X correct


Now this is equal to the gradient of


Application of log of


readed off


X okay given what is Z now


Z is given by this particular z of yeah this particular formula let me call this as uh


Do you have a question


It is a bit of a spectacle


Is that alright


Strictly speaking now this g function is a function of phi now because look at this right I mean it has mu phi and sigma phi here its parameterized by phi


The question is we got rid of the dependency on p right this expectation now can be is equal to 1 over


the sample m samples of epsilon right then this is equal to j to m and we have


log of p theta of xp one


D C O


Epsilon G


Please note that for a particular xi for a given xi we can get m number of z is see that


Or


One x sorry okay


ZIs can be obtained


Do you understand that


Because we are doing sampling right like outside of the encoder since we are doing sampling we can sample for one xi we can sample multiple gis but typically I mean what is done in implementing vi is that they keep capital M to be 1 that means that they only do one sampling and send it across okay which means that the sum will only be on one particular sample Hope that it is okay Now the next question is that how to compute


to compute log of

speaker_3: So here we are doing it in a probabilistic approach right for the encoder

speaker_1: Encoder is always probabilistic


xi will give you mu and sigma once you get your mu and sigma you sample epsilon from lets call this yeah epsilon from epsilon j lets call it you sample epsilon from normal 0 1 and then they reparameterize and get m uh z js


But there is

speaker_3: So there is some like so if we write it like this so there is some linear translation happening between the output of encoder and the input of decoder

speaker_1: yeah input of the yeah that is the reparameterization no in this particular case that is what i am saying if you assume your q to be normal mu sigma then this reparameterization is adaptable


There is no rule why this is the only way to reparameterize no Thats what Im saying Suppose you assume your to be some other distribution You just have to find an epsilon and g such that it transforms See what is important is that now this gradient right The gradient that we are computing here this will become this expectation will become independent of phi Thats all we need


And for that we do reparameterization Now what sort of reparameterization you do is a design choice That depends upon what form do you assume on QP and what what epsilon will just transform what epsilon and G combination will transform that into this is the question Thats all That depends upon whatever you use

speaker_3: Okay sir

speaker_1: Is that all right


Okay Uh yeah Sarvesh do you have a question

speaker_2: So in the last step one by m so there should be a gradient inside right

speaker_1: as a gradient here so this will be


Go on

speaker_2: So can you just repeat why that m can be taken as just one here

speaker_1: its that its like youre approximating this expectation by a single sample estimate thats all it can be anything uh people take it as one and also experiment i mean in your assignment ill ask you to experiment with different values of m okay but yeah so generally i mean like in the naive most naive implementation you just take one sample of z or one sample of x but it is not uh i mean its not a hard and fast right i mean you can make your m to be hyper


Ill put it on and play with it yeah

speaker_2: Because I think in this equation we say that it is an expectation so we we are free to choose the value of m here right and because

speaker_1: And also single sample estimate is not a good way to do it yeah always


Yeah

speaker_3: Sir I didnt follow on this part sir can you please explain once again

speaker_1: But see here you sample for one xi goes as an input to the encoder right you get a mu and sigma Now with that mu and sigma you can sample any number of zis no for a particular xi


Huh

speaker_3: So that is what the choice of them

speaker_1: that is what I have represented as capital M so you sample like multiple samples from so its like for lets say X i is an image you know for a given image for one particular image you will have m different embeddings


Right So that is the I mean that is the sort of advantage with a probabilistic encoder right That unlike in a BERT et cetera where for a given text sequence of tokens you only have exactly one embedding Here you can have a plethora of embeddings for a given particular input because you are modeling it probabilistically correct


And once you do that if you have M of them to compute the first term right you need to take an average I mean meaning you take a sample average of all those M uh M M MCI basically right CJs


But what I said is that some people when they implement VA you know they make this capital M to be 1 You can do it 1 also because its a hyperparameter but you know M M being equal to 1 is not a great choice because you are approximating an expectation using one sample which is not a good thing to do no


Yeah yeah

speaker_2: uh this x p theta of x given z so this x is all all xs right x1 x2 xn because of we have to maximize the likelihood of all x1 to xn

speaker_1: Not exactly but yeah but we are doing the entire treatment for one particular data point now see whatever we are doing now there is an outer sum on all data points you take a batch size and do it over batches

speaker_2: Yes yes

speaker_1: But Im doing it for only one x right now for now Im only doing it for one x so this is actually x re


And I should not be writing it as xi because its a distribution over a random variable right but what I mean to say is that only one sample is what we are doing it for which should be extended to the entire data set on a batch level

speaker_4: So like its

speaker_1: Yeah yeah yeah or stochastic when you do it at the batch level because usual training no Im Im telling you how to train for one sample you can train it sample by sample or take a batch and do it doesnt matter but well see that Im I was going to say that at the end of the end of the lecture but this is only I mean all that we are doing it is for only one data point okay


Now the next question is any other questions on this If not well move on Now we have to compute this log of p theta of x k 1 z How do we compute log of p theta of x k 1 z is the question So again there are multiple ways to do it So now one way to do it is that express


using some parametric distribution


For example this is not the only way to do it again for example uh like assume


assume p theta of x given z to be coming from a Gaussian distribution okay what is the distribution on x of course


And you assume the mean okay to be equal to

speaker_4: Mm

speaker_1: output of the decoder


Variance to be equal to 100


note that in this case I am representing the neural network right the decoder network probabilistically


Now were t theta


e theta of z


is the


Let us call that as X cap weve been calling it as X cap X cap


T theta of z is the output of the neural network


decoded okay now in this case what happens is that this xi cap that we get now which is


of Z J right


Now now this we in we are interpreting this as the mean of a Gaussian distribution right of p theta of x given z So in this case in this case lets see what happens to log of


p theta of x given z what is this equal to this equal to


proposed that term one by two by


e by 2 sigma inverse that is identity that will go away this will be a e power


This is probably point x i know x okay lets call it as x x minus what is the mean the mean is given by d d t theta of z


the identity matrix is the identity is the uh the variance so this is equal to this okay now uh ignoring the constant lets just say some


I okay thats proportional because the other terms are independent


proportional to log and equal will go away this will be


Xmas


Now you see where the auto encoding thing is coming from it will become a


where there are loss okay between the input data point xi and the output of the decoder if you assume your p theta of x given z to be Gaussian so which implies


Now the expectation of what do we have expectation of log of p theta of x given z this with respect to q phi of z on x this is what we wanted right this we saw to be equal to the expectation of


But taking it with respect to P epsilon we have laws of


e theta of x given g of epsilon


Now sample in terms of sample averages how do we divide a approximate is approximately equal to 1 by m so if you sample


This is this under the assumption of Poisson entity it is theres a minus here that is equal to


psi minus


eat it off


You want to go to JK


Recorded


like I said zj is equal to


mu phi of xi plus epsilon j times sigma phi of


or j equal to one


Now you dont see the dependence on phi here so maybe I should write it that way Can you see that there is a dependence on z here It is entire thing this thing is a function of phi Do you see the dependence on phi It depends on phi through z correct Because z is dependent on phi correct


is what it is so now what we should do is that now how do we do like one uh training of encoder


One iteration of encoder is as follows Ill write that now


you have xi as an input the qf network


This will give you mu


new feel


and sigma phi of


So take these two sample epsilon j


Im normal Z one


And find out


Z J


mu phi of xi plus epsilon j times sigma phi of xi


and then take this ZJ and pass it through the decoder


holding P theta of X K M Z and this will give you


beat heat up


x cap i or rather x cap j which is d theta of z j


Now what do you do like there is a forward pass this is the forward pass right take this get this done and take the


Uh okay so


get your z okay from your z get it through this this is one forward pass okay now how do we do reverse pass you know reverse pass is compute


Ill build it


So one for one particular xi you need to compute 1 by m


Note that for a particular input xi you have multiple possible outputs because you have multiple embeddings right with different ms You compute this okay and then take the


It is


compute the gradient of this with respect to p


And then simply back propagate this


will relate to the input of this What happens here by the way once it comes to the input of the decoder


will happen so you have to backprop take this gradients


that propagate through this operation or ZJ operation


This operation

speaker_4: I mean well also have to remember this EJ that was used here right

speaker_1: Of course of course of course you have to save that


all Ms you know you have to remember that is EJ so okay maybe I will write it this way to make it easier


From here


like this


Okay first it will come like this


From here you travel like this


is called the reverse pass so now forward pass also it comes like this and


through this okay and then from here you go like this


Oh sorry I think I changed the colour


This is the color we come like this


And from here


like this


So once you click this and you pass like this this is the forward pattern and the previous pattern


all propagation and stability

speaker_4: All this while

speaker_2: Well we dont change theta right

speaker_4: We keep the tea topic

speaker_1: we keep the theta constant to hold on i think so ill have to do it this way to ensure that what im writing is more fit you will hold on this is only for training the encoder not decoder this thing that is this epsilon


Okay we know what that Ill Ill Ill write it you know what


Radiance


Do not flow


True sampling


see that so maybe Ill write it in a different color easier that way


This is something


Thats it so this is


one iteration of trimming the encoder with the first term and we have not looked at the second term yet this is only for the first term the first term for the encoder by keeping the theta constant


Any questions on this


I see a hand raised Harish so uh we get m gradients by back propagating uh


Sorry I didnt follow can you repeat it was yeah

speaker_3: Yeah sorry So we get M gradients right While we since we have

speaker_1: No no one one one gradient No no one gradient See what happens is you take M of Zs right You pass all those through the decoder and you get M X J caps correct

speaker_3: One one one

speaker_1: So you compute this this entire thing or this thing right you take the difference with all each of them individually and sum them off So that will be one scalar that will be one scalar

speaker_3: So we are summing up it at the end

speaker_1: not one M so it is like M different outputs you take the difference between them and you sum and then it will be one scalar that you backpropagate


Any other question See your second assignment will have this to be implemented So yeah I think this should be clear So let me know if you have any other questions on this

speaker_3: So why do we need to get a scalar sum at the decoder output like we have m different xjs and we can you know like compute the loss

speaker_1: See look at what is doing so we should not deviate from math so what is happening is we need to compute the expectation of q p of z given x for a particular x for 1 x


We represented that in terms of an expectation over another random variable So expectation has to be computed and back propagated You understand So you have to compute the expectation of sample averages and the output of the decoder and you get one scalar that would be back propagated

speaker_3: expectation of the sample average is and

speaker_1: Isnt it So this is look at this equation this equation is what we are trying to back propagate isnt it Thats the first term in elbow


So this is for a given x So for a given x you need to compute the expectation of that log likelihood with respect to q p of z given x for a particular x And that will be represented as an expectation over epsilon okay which is a sum over all m samples So we have to pass all those to the decoder compute this and then take a scalar and then backprop


Youre gonna have to make him

speaker_2: There was a second term for elbow right

speaker_4: Does not contribute

speaker_1: I see this one thing at a time that Im only doing lets see look at what we are doing but forget what we are doing


Look at this


All this is for the first term the gradient of the encoder parameters with respect to the first term Theres a story for the second term and both of the terms for the decoder We have to still come one thing at a time

speaker_2: This is not the complete gradient

speaker_4: Can we fall back

speaker_1: are not no we are not completely its only the first term that to the encoded parameters right so if you have questions on see this is the most complicated thing the rest are actually easy its just simply training a neural network this is the most thats why i took the most complicated thing the first and then we will go one thing at a time okay um any any other questions on this lets move on so now this second now we have to compute the


To compute the gradients


Encoder


Only second


So what is the second term the second term is the scale divergence between


u p of z union x and p theta of z okay now what is done is


P t dot z


is assumed to be


normal zero one okay note that this is assumed to be independent of theta


This is a model assumption that is made and there are other lots of other improvisations over VAE that would question this and make it dependent on theta also Okay So for the the nine implementation this is made independent assumed to be Gaussian 0 1 and it is made assumed to be independent of theta So in that case what happens is we have


u phi of z q on x okay to be a Gaussian


mu and sigma right


Now this implies that the second term which is the K between


will be equal to KL between


Gaussians okay one is a Gaussian


Another is a Gaussian


So this is


So what is this the deterministic form for this okay


Even by let me just tell you what


equal to


Hmm


Log


determinant of this minus D plus


Trace of uh


mine most of x


or I can write it as minus half log of this end


So this plus plus


We all


Mufi


mu phi of x squared this is this is what it is you know you can show this Gaussian between two sorry KL between two Gaussian distributions can be deterministically found out and simply take it as a small homework and do this okay yeah this is what it is okay so KL now is a simply a function of sigma v x right mu x so this means


It is encoder decoder thing write it again


X I Q P of

speaker_3: Is it square of norm or just the norm

speaker_1: I think it should be square square yeah


you have


Leave them off your website


All you need to do is just one forward pass to get your mu p and sigma p right and lets write this as some


which is a function of mu phi of xi and sigma phi of xi


So now you have to compute one forward pass and then the reverse pass just you just have to compute


Dont even have to go to decoder at all just compute this


Yeah I love you too


sigma v of xi okay and then simply


gradient of course not


and simply back propagate it


You know what happens is no for one trust one uh uh one uh iteration of encoder training you will have like one gradient coming through the decoder okay and like there will be just this plus the KL gradient also gets added here


Well have to add both the gradients here So this what we are adding here this will get added with the gradient that is coming from the decoder and this completes the encoder training


Its all right


they should be straightforward no nothing complicated here now to train the decoder


How do we try and get the decoder So first thing to be seen is the second term


Here the term


Independent of


Equator parameters theta right


dont have to use that at all now what should we do is that just


Take an X ray


You will be of z given x


Just finish this and then close the class So sigma phi of xi


Then you have like epsilon j coming from normal 0 1


they compute cj to b


and then you pass it through the decoder


What do you get as XT cap


Now how do we train this So what we have to do one complete forward pass


as usual


Then you do sampling and once you do from here it goes like this and then it goes like this goes like this and you have to simply compute


gradient theta which which term you have to compute the term this xi minus d theta zj


So you do the radiant opacity


This term with respect to j right And then simply back propagate this all the way to the input


It is one decoded right


One I think I know decoder try


easy right thats all so now we are done with the training of VAE


In the next class know when we begin we will look at how to do inference which is the we have to do sampling and also posterior inference know I think its obvious right I mean you can once the training is done you just


discard the encoder and pass it through the depasser z through the decoder you will simply get uh uh the generation and you take an xi pass it through the encoder you get the uh the embeddings right thats all it is always remember right whenever we are doing sampling in an encoder decoder model generation is always done through the decoder model okay uh and the embeddings are extracted through the encoder model so we will continue from here so what ill do in the next class


that we will look at like complete the VAE discussions and also look at one two improvisations over it you know especially I want to talk about one state of the art VAE model called vector quantized VAE or VQ VAE which is what is used in stable diffusion and all that okay that would be like


like 30 percent of the net class and next we will go to diffusion models which are the state of the art for like image generation these days okay uh which is actually one particular form of the vae but i urge all of you to kindly go through my notes and also todays discussion on vaes and how to train them i think im sorry i actually did it this way right i mean i inadvertently zoomed it at this point but yeah i think you can also zoom it right because it was convenient


So please go through the class notes and also my handwritten notes and read the VAE paper and be thorough with all this before coming to the next class so that it will be easier for studying diffusion models and so on

speaker_3: Sir one question

speaker_1: Yes

speaker_3: So the first the first KL term that will be used to update both the encoder as well as decoder right like in the same path

speaker_1: So hold on there is no first term is not the KL term the second term is the KL term


So you just said path care term there is no sorry sorry I mean I mean

speaker_3: Sorry sorry I mean I mean I mean in in the overall equation the first

speaker_1: Oh shit you got em


reconstruction term it is called okay the reconstruction term is used to uh update both encoder and decoder but when you are training the encoder you keep the decoder parameters fixed and vice versa

speaker_3: So cant we like so does that mean in in in one pass we cannot update encoder and decoder simultaneously

speaker_1: How do you do it No see you have to do take two gradient passes I wrote the equation also right here here yeah this is how you do it first you have an encoder update and then a decoder update


Right So when you train the encoder you keep the decoder parameters fixed and vice versa

speaker_4: I I had a question on the assignment is this the

speaker_1: Yeah let me just any any questions on the class before we go to the assignments

speaker_2: Yeah so I had one question so for example in tr during this training right I mean we start with the decoder training first or the encoder training first I mean in fact

speaker_1: All right it doesnt matter doesnt matter doesnt matter you just train one one one pass of encoder one pass of decoder that finishes one training yeah

speaker_2: And any thoughts on the uh uh the convergence I mean how well this converges compared to say

speaker_1: Yeah this will very nicely convert there is no adversarial training that is happening here no


Unlike in a GAN there is no there is no min max there is no I mean encoder is not adversary to the decoder right they are both working towards the same objective


VAEs are known to converge much much better than VAEs because there is no adversary saddle point problem there is no saddle point problem

speaker_4: I understood thank you

speaker_1: Okay uh yeah Questions on assignment you said yeah go on

speaker_2: Yeah so sir uh as uh I understood it maybe Im wrong

speaker_1: One ago we are doing with

speaker_2: We are doing with uh

speaker_1: Sorry can you make it quick I have another class at twelve thirty so yeah yeah

speaker_2: Yeah yeah good question sure So one and two anyway we are doing with butterfly and rest all the animal data set right So anyway we have to retrain the model with animal So for the butterfly one can we go with our independence of freedom like choosing our laws and

speaker_3: etc

speaker_2: right because or anyway we have to we are doing all this condition like usual loss double gel loss

speaker_1: Arijit hold on What is your precise question Please ask me your precise question I can understand the question

speaker_2: Okay uh then let me do one thing let me watch

speaker_3: Okay that would be better I think you have a class

speaker_1: Right okay you can ask me the question I still have five minutes ask me the

speaker_2: So I I

speaker_1: I want to say

speaker_2: Yeah so the butterfly dataset one which we are doing one and two I can use any loss of my choice right I mean for example WGAN or all there is no foundation there Only the conditions are applied for the animal dataset which again anyway we have to retrain the model

speaker_1: Again what is your question here I I I so no

speaker_4: No I mean as a butterfly one we have the freedom to use any loss function or anything

speaker_1: Gan you always use one loss function right which is that saddle point problem what is the other loss function that you would use

speaker_2: Because uh no because uh there is a I mean we can use DC loss etc right also

speaker_1: For a DCGAN loss does not change only the architecture changes no

speaker_3: Yes yes right

speaker_1: Are you asking whether you can use an MLP for butterfly Is that what the question is

speaker_3: Yes kind of

speaker_1: So yeah you can use anything See but again thats why Im asking you that please if you if you make your question precise the answer can be given precisely

speaker_2: Uh okay I think uh I will ask you separately then uh I mean

speaker_1: So think about it and lets keep on yeah

speaker_3: Yeah

speaker_1: Ah yes yes

speaker_3: Yes yes sure

speaker_4: Thanks buddy

speaker_3: Sir just to confirm next week we are not having a class and also we wont be having a quiz right like every alternate week

speaker_1: You are

speaker_3: We were supposed to have a voice

speaker_1: it correct correct so the schedule will change so the quiz will be the week next afterwards correct


see on that note no like happy to serve out all of you yeah

speaker_3: So

speaker_4: So I have two questions in the assignment One is that we had mentioned is the decoder network for the eighth and ninth question right So we discussed the decoder network only in the VAE so is it similar to something that you are to use something like beyond

speaker_1: Yeah yes correct So Ive precisely told you what to do right You train another network See when you are training the GAN just have another network which will take the generated image and just gives back the input noise And you can take an MSE between them and train it together


Along with D along with

speaker_4: Oh indeed

speaker_1: along with the adversarial objective

speaker_4: Okay I think thats the same follow up question on Tolteque So yeah we mentioned that use the augmented images

speaker_2: the training right so is it only augmented image we got to use or we got existing original and augmented together and we got to pass it together

speaker_1: Whenever you are taking augmented images you should always take the original plus augmented You should not give away the original thing Original images rotated with two three angles right And that would be your data set will increase by three four times Yeah

speaker_4: I mean I dont know


Uh sorry sorry one more thing so this you mentioned the two inputs to be used right in this uh later stage so it is a say uh

speaker_2: same distribution or the different distribution with the two inputs in the machine

speaker_1: What do you mean to protect

speaker_4: We input our test

speaker_2: As a vector questing randomly sampling two input vectors

speaker_1: Yeah thats yeah thats

speaker_4: Yeah thats cool

speaker_1: same distribution right i mean in a gann like a sample you will only sample from the same distribution at the input otherwise sample from different distributions will yeah

speaker_4: I like the sound


Uh sample from okay


Okay okay so its a Z only we are using we have to do the two tool times we have to take the two input

speaker_1: Yeah take two zs pass it through the input generator and then interpolate between them and observe what happens at the output okay

speaker_2: Okay

speaker_1: Got it

speaker_2: Sorry about the exam so portions till this time uh including the references that you have mixed in your handwritten notes and all the glasses thats what we should be expecting right

speaker_1: You can be expecting

speaker_2: And like it would be a theory only and mostly derivations would be involved Just want to know the type of queries that we should be preparing

speaker_1: I have not I have not said the question please forget so it will be it will involve some math okay it will I will not be asking the questions like differentiate between GANs and VAEs thats not how it will be it will be like some thought provoking and you have to do you have to practice math okay


Itll not be descriptive Ill not be asking you to like describe how GAN works and all that no definitely not okay


Okay so see feel free to like ping on that WhatsApp group or teams and get in touch with TAS you know they are helpful as well both Suhas and Chandan you can get in touch with them


And you can always ask me questions as well Yeah And all the best for your exam I will give you details the instructions on how the exam would be and all that Once I complete the question paper which is like Ill do it the mid next week And once I do that Ill tell you like what the instructions are and so on Okay

speaker_2: Okay

speaker_1: But yeah anytime you think

speaker_2: sorry should we be like looking into the previous year model paper if you have any like whatever the paper you had

speaker_1: dont know where it is it should be there somewhere i dont know where its it where is it dont worry i dont worry too much its fine yeah


Okay see you then all the best

speaker_2: Yes sir

speaker_1: Thanks


Have a nice week
