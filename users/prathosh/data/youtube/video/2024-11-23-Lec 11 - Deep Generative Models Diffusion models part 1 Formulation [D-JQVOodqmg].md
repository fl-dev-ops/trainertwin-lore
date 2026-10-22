---
id: D-JQVOodqmg
title: Lec 11 - Deep Generative Models Diffusion models part 1 Formulation
url: https://www.youtube.com/watch?v=D-JQVOodqmg
date: '2024-11-23'
duration: 02:45:18
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: of us have marked in the quiz but the answer is saying increased disentanglement on increasing beta

speaker_2: One second

speaker_1: Yeah I have pasted it

speaker_2: And I have a question

speaker_1: Yeah Ive pasted the snippets

speaker_3: Seems like


there should be decreased disentanglement with reduced reconstruction quality

speaker_1: Ive been trying

speaker_2: Come again so has

speaker_3: It says it should actually the correct option should be decreased descent angle right But the option that is marked correct is increased descent angle

speaker_2: Yeah it should be decreased over time What is it saying If beta is increased what will happen is that the weight for the KL is increased If the weight for the KL is increased then


Should be


It should be both the construction quality and entanglement getting decreased okay


Okay so first let us I think if the correct answer is marked as this thing


What is the correct answer given now increase the entanglement reduce the construction quality is it


No that is not correct Okay so can we change this like and

speaker_3: Yeah Ill Ill change the

speaker_4: But sir is it uh like whenever we are increasing the beta it will be a stronger penalty on KL divergence which is promoting the disengagement and because its not private

speaker_2: No it is not right No see because thats what I told you right the word disentanglement refers to having different posteriors for all x and for each x


That is not happening no if you if you increase beta r


Posterior collapse would be more isnt it

speaker_4: the potential cost uh sir when we are giving a higher value of beta uh what we are saying is that in the overall loss minimization we have to minimize kl divergence

speaker_1: loss more than we have to minimize reconstruction loss

speaker_2: Correct correct

speaker_1: So if we are reducing if we are increasing beta eventually what we are doing is we are ensuring that KL divergence loss comes down further which means disentanglement is going to increase

speaker_2: We said it


disentanglement is going to decrease no if the KL is reduced further that is what I am saying if the KL is see first understand that reduction of KL is inverse I mean is inversely proportional to in in disentanglement

speaker_1: Right so dissing and entanglement should increase when KL divergence is reducing right

speaker_2: Yeah

speaker_1: So then the marked answer is right increase disentanglement will reduce the confusion

speaker_2: I think when multiple sources online say the same thing but uh no hold on I think Im getting confused lets see there is a double meaning

speaker_4: Ill bet


There is a double N and a centangle and a centangle

speaker_2: Let me let me let me make it clear for myself and then well discuss now beta is increasing beta is increasing meaning kl is reduced further if the kl is reduced further then the disentanglement


will decrease


Because disentanglement uh kale is reducing further the disentanglement has to reduce correct

speaker_1: The entanglement has to reduce

speaker_2: no no kale reduction is entang entang entang entanglement reduction see suppose kale is zero okay if if kale is zero then what happens if kale is zero the entanglement would be increased right because all of them are collapsing to z given sorry normal zero one isnt it


Is it dead

speaker_1: Maybe

speaker_4: Maybe so we will come back with the proper way of this

speaker_3: I think uh entanglement

speaker_4: Whenever we increase the beta it will increase the means at the cost of KL diversion it will reduce the quality of reconstruction and increase the t angle mid

speaker_1: And yeah I need to do your notes again

speaker_4: But yeah I need to do your notes again

speaker_1: If the disentanglement is reducing it means for any input the latent variable space is going to be almost similar which means the reconstruction quality should be reducing

speaker_2: Reconstruction quality reducing that is definite there is no question there

speaker_1: Right so basically we cannot have a scenario where disentanglement reduces and reconstruction quality increases

speaker_2: We cannot have it

speaker_4: I mean what what do we mean by entanglement So for example if the posterior becomes normal has the entanglement increased or decreased

speaker_1: So what my understanding is that entanglement being higher means that for any input image that we are giving the latent space is coming out to be almost similar That is why there is an entanglement in the latent space for any input image is coming out to be similar

speaker_2: That is correct that is correct

speaker_1: So if we are saying that we are giving more weightage to the KL divergence we are going to basically try to ensure that the entanglement reduces


So when posterior becomes normal

speaker_4: When posterior becomes normal

speaker_1: No and the angle point increases

speaker_4: and angle point increases more weightage to KL means angle point becomes close to normal

speaker_2: All of a sudden it will become

speaker_1: Uh but but but

speaker_4: KL is a loss KL is a loss


If we are multiplying with the

speaker_1: There is a minimization operation happening When we are giving more weightage to beta we are going to further reduce the value of KL divergence which means we are going to reduce the entanglement

speaker_2: We all agree that

speaker_1: You all agree with that

speaker_2: If the KL has decreased then the posterior becomes normal right We all agree on that

speaker_3: Yeah

speaker_2: So does this mean entanglement has increased or decreased

speaker_3: Its maximum entanglement right When your posterior has become a normal thats what people are trying to say

speaker_2: So antangleman has increased right

speaker_1: Thanks for having me on the show

speaker_4: Do you see my screen

speaker_1: Yes yes

speaker_4: Can you read whatever whatever I have uh highlighted

speaker_1: Is that any sea

speaker_2: Can you see what I have highlighted But what is good in this


Disentanglement is good


This is the this is an excerpt from the beta VA paper


Okay so higher the beta better disentanglement

speaker_4: Better means increasing surplus

speaker_2: higher the beta increase this entanglement

speaker_1: But here they put minus of beta d instead of plus beta

speaker_2: in the the beta VAE loss term theyre subtracting instead of adding the loss


appropriate even beta greater than one call um hold on lets see have they done that uh yeah the term above that image yeah there is a minus beta correct we we did plus when we were discussing so


Uh I think that might be the


Okay I got it So in our formulation it was plus z

speaker_1: Thanks for your

speaker_2: It was plus beta


Then it wont hit you

speaker_3: How would how would plus beta work here It it wouldnt work right you need

speaker_2: No no what I meant is see that then beta is taken to be negative right I think so has lets do one thing I think you know theres confusion So let us just ignore that question and just add one to everyone thats our easiest way to deal with it


But yeah so I think you got the point right At least in terms of what is happening If beta is taken to be a positive integer and the objective is written to be minus beta then increase in beta right implies


disentitlement right better discontentment i think that is what it is yeah i think im convinced just think about it lets move on because its already pretty late okay so so has taken note of it we just have to add one to everyone in this in this particular quiz

speaker_3: Sure okay yeah

speaker_2: Thank you Swoos I think you can leave now if you want I can start the class


Okay thank you

speaker_4: Sorry for interrupting uh can you please repeat what you said about the beta thing sorry

speaker_2: The beta is a positive integer and the cost is KL minus beta sorry the construction minus beta okay


So if beta is increased then disentanglement will become better because we are minimizing that KL thats all and beta is a positive number


So just read this uh uh this beta vae paper no its pretty well described I think that is correct The only confusion was because you know the in in our formulation we we took plus beta and beta in our case was between 0 and minus 1


Right so in that way this question can be interpreted as if you put plus there increasing beta means it is you are moving it away from minus one So


lets not get into that confusion I think this its its the problem is with writing that as plus thats all so let us like ignore that question for everyone okay so


How many quizzes are done now Four


Yes sir


order okay so we need two more


Uh we can do streak let me just look at the calendar


Second ninth and sixteenth


We have three weeks including today so today is done


Uh shall we do a quiz on 9th and 16th


You can skip on second uh because

speaker_4: So 16th I think were planning for an online uh hybrid class

speaker_2: Correct Well have a quiz then No problem Okay We dont want See otherwise we can do it on second and ninth also

speaker_4: Otherwise we can do it


So lets take a

speaker_1: Reckon many people will not only keep on second search

speaker_4: Yeah

speaker_2: Okay so then let us do it on 9th and 16th okay

speaker_4: Yes picture

speaker_2: And uh assignments we said three assignments right

speaker_4: I think you mentioned that you will give the third one in the November first week

speaker_2: Uh coding assignments are three into fifteen so two is done when is the deadline for your second assignment


Repeat it

speaker_4: Repeat

speaker_2: 28th So then Sunday I will release the third so that we can finish by mid mid November Okay good So one exam is done quiz for two more quizzes and one more assignment Okay great We are on track Okay so let us get back to classes So you can see my screen Can you see my screen


Okay so todays agenda is diffusion models TDPM Yeah so Ill tell you rest of the course the way Im planning is we have three more classes right So Id hopefully complete diffusion models today Lets see So today well do diffusion models and well have three more classes And one class I will do noise contrastive estimation self supervised learning all these ideas and well have two more classes


We can use it for autoregressive models and LLMs Okay Thats how Im planning Okay Lets get back to stuff So we were looking at denoising diffusion models Just a quick recall These are hierarchical VAEs right which have multiple latent spaces capital T number of latent spaces All the latent spaces have the same dimension as the data space So you start from the data and


keep projecting onto the latent space till it becomes um


the stage and still it becomes until it becomes a Gaussian distribution and from the latent space you get back to the latent space by


traversing the path in the reverse direction So the thing is the dimensionality of all the latent spaces is same as that of the data space is something that we saw right And the


It is not moving does somebody know why


Not able to move this

speaker_4: Both can restart

speaker_2: Oskar and Ester


Uh what did you say


You could just restart the application close it and restart


Still not moving


I can have a virtual money


Okay yeah so the dimensionality of the latent space is same as that of the data space something that we saw right The encoding process in a DDPM is not learnable its a fixed encoding process and its a Markov chain okay that is one other thing that we saw okay Yeah so we made the notation consistent with the literature the data is represented using x naught and the latent space is represented using x1 through x capital T okay


um yeah so you start from x naught and go to x capital t and the dimensionality of x naught is equal to xt for all t and this is how the encoding process is defined okay uh you have fixed alphas alpha 1 to alpha t and uh every xt is given by uh the previous uh x previous latent scaled previous latent plus some scaled noise where you sample from normal 0 1 and add it okay this is the so called


called a forward process or the encoding process in a DDPM Its a first order Markov process with Gaussian transitions which means that you take one random variable add Gaussian noise you get the second random variable and you traverse that Markov chain Okay And the stationary distribution of this Markov chain is normal 0 1 And I hope that I also showed you that picture Did I where you start from an image and get a renoise I showed you that picture


Last class


Okay great Yes Okay so this is where we are so let us move on from here


Okay so Ill give you the high level idea of what we will do today and then I will run through the math


The algebra is a little involved but its not difficult


Yeah okay


So the idea is see we have uh


encoding process


is a fixed encoding process


given by the following so we have xt to be equal to root of alpha t times xt minus 1


root of 1 minus alpha t times epsilon where epsilon comes from normal 0 right this is the encoding process correct this implies that the conditional distribution of any xt given xt minus 1


What is this Can somebody guess We know that from reparameterization that if you start from a normal distribution scale it and shift it with a certain mean and variance you will still get a normal distribution right So these are normally distributed So please note that my notation normally distributed the random variable is Xt


The mean is


Root of


alpha t into xt minus 1


variance is 1 minus alpha t times identity so theres a very slight abuse of notation here ill tell you what it means see when you


When youre writing a conditional distribution like this right the conditioned random variable xt minus one is fixed in the sense that it has already taken some value


but the the random variable that is to be conditioned xt is not fixed we have a distribution over it that is what we have written that its a normal distribution over xt okay where the mean is square root of alpha t times xt minus 1 so this xt minus 1 which i have marked right in lo it is a fixed value because you are already in xt minus 1 and xt minus 1 has assumed a particular value okay and given that xt minus


one already has a particular value you have an entire distribution over xt which is given by that equation does it make sense why do you have a distribution over xt is because of this epsilon that is there so fix you you are given an xt minus one you get an entire distribution over xt is that all right to all of you


Okay now what do we do is as I said we have an encoding distribution that is fixed Now please ask me questions if you have any because I


make it a little faster today because I want to complete DDPMs Lets see So we have this is the encoding distribution We have the decoding distribution


which is to be learned


Okay what is the decoding distribution we write that as p theta


So decoding has to happen in the reverse direction XT minus 1 given XT So please note the commonalities between this and the VAE right In VAE the encoding distribution is Q of G given X which is the posterior of latent given data The sorry the encoding distribution is posterior of latent given data Decoding distribution is posterior of data given latent Okay Similar thing is happening here I mean here there is no one latent you know there are directions of latent So you start


from uh x naught which is the which is the data and you go to x capital t in one direction that is the encoding distribution the decoding distribution is in the reverse direction correct now this has to be learned


Okay so this is at first of all this is assumed to be a Gaussian distribution again okay at xt minus 1 with a certain mean mu theta and a certain variance sigma theta


Okay so this mu theta and sigma theta


Are the learn are the learnable model parameters So this is what we will learn


are the learnable model parameters so given the fixed encoding distribution okay we will make a distributional assumption on the decoding distribution and we learn the parameters of it that is what we are going to do now how do we do it so we learn that through


Yeah same thing elbow optimization well do the exact same elbow optimization and well learn this


Thats all So rest is algebra Okay Now you understood right So we have an encoding fixed encoding distribution and we have a learnable decoding distribution Given the encoding distribution okay we optimize the LBO and learn the decoding distribution parameters of the decoding distribution That is what the idea is Okay Any questions so far quickly Surveillant

speaker_4: Previously it was written alpha t xt minus one plus one minus alpha t epsilon

speaker_2: Oh sorry my bad my mistake Or its either here or there Let me just see what the doesnt matter right I mean depends on what your alpha is but lets see what the literature does


I keep appointing that


Yes yes


A second now give me a second


I think the problem here I made a mistake so this has to be


Generally we write it as root of alpha okay


Noted correctly today but yeah


Is that okay I should clear it Okay Yeah Avatosh lets make it quick guys yeah

speaker_4: Now why is the encoding process fixed here

speaker_2: Told you all that in the last class okay


because that that is see that is how the uh the ddpm is described okay the encoding process is fixed because its a what do we want we want a projection from the data space to the uh the latent space okay or rather gaussian 0 1 now we do it in the hierarchical manner now in a ddpm it is a marco chain right so you are doing a random walk through a marco chain now unlike in a


where projection from the data distribution to the normal 0 1 okay cannot be guaranteed and has to be learned via that phi encoder network in a markov chain okay if you have gaussian transition it can be guaranteed that the stationary distribution of a fixed markov chain after sufficient number of steps converges to normal 0 1 so since you want your data to go to normal 0 1 and you construct a markov chain where there are slow transitions


You dont have to learn anything

speaker_4: So

speaker_2: the idea okay i think i mentioned this in the last class but anyway okay is this clear so what we will do then next is that under these model assumptions we will write down the elbow as usual and optimize it thats all so thats all the entire processes now okay now just like with the case as in the case of uh vae the final generation is via decoding because in vae also you do the same thing right we will do the same thing here uh the only thing


Yes we have these kinds of model assumptions and we will have to optimize the L value Okay let us do that


uh let us start okay elbow optimization for ddpm


Recall you should recall that uh what was our elbow so log


p theta of x okay we will start from the definition of the uh latent variable model that was integral so log of


Integral p theta


X and Z


DC correct this is what it was so finally what was our elbow uh the


Function of theta and phi


Represented that as F theta of QV What was that


That was an expectation of log of p theta


x and z divided by


U oxygynics


This was with respect to Q of Z geonics


Do you recall this one of you


Okay we just have to write this down for a DTPM okay thats all it is let us do that


Oh this is um


LBO for DDPM or diffusion models is only a function of theta because theres no dependence on phi is equal to expectation of


log of p theta so what is x and z here that is x naught x one


Oh why is this This is because


X naught is the data variable and X one through XT are the latent variables


divided by q of what is the latent variable here x1 x2 up to xt conditioned on x0 okay and we have that same q here that entire thing cant write it is this is this all right this is this is only a function of theta as you can see because encoding is fixed


This is alright


Okay so now well just shorten this down and write it as So please pay a little more attention today because its notationally heavy Its not difficult but if you miss one notation it will all be gone Ill write this as x0 to t because I cant write 1 to t all the time divided by q of


one through t which are the random variables conditioned on x naught and this is is this okay


So every step you either react or interrupt me if you dont understand Otherwise it will be difficult for me So this is all right right This is our elbow So well have to optimize this with respect to theta correct This is what we need to do


So let us do that


Excuse me just a second um


Okay great So now this can be written as will not write this equal to every time So let us write this expectation of log p theta x 0 to t divided by q x 1 to t given x naught Okay this is what we want Okay so now this is


Okay so first of all what we should do is well have to write this as


Expectation of log of


Please observe here So now p theta of x 0 to t I will write it as p x t times the product of


p equal to one two p


E theta


xt minus one given xt


divided by


You


Product of


t equal to one to t q xt given xt minus one okay okay why did I write this


B theta of


x naught x 1 up to x t okay it is what we wrote as p theta of x naught to t this is equal to


P theta of xt


ET off


Im not sure


the other way round


So that is p equal to one right p theta of


X not


Given


X one given X naught


No no no we are going in the reverse direction yeah Im just Im just writing the checking rule hold on so this is um


should come on the other end no hold on should be so ive written it from the power i mean ive written it from t equal to 1 to t should be the other one so xt minus 1 given xt okay so this is uh xt minus 2 given xt minus 1 and so on up to p theta of xt


This is what it is How is this this is chain rule of uh


probability right so now since the forward process is first order Markovian right reverse process is also a first order Markovian process which means that given xt okay uh xt minus 1 is independent of all the other states that is why we have written it this way okay now this can be represented as p of xt p of xt into product of p equal to 1 2 capital t


p theta of xt minus 1 given xt Now observe what did we do We took we took off the dependency of theta on x capital T y is thus we have designed our xt


was XT by construction


normal 0 1 isnt it while transiting the forward chain we have ensured that the capital T at x random variable is normal 0 1 therefore it is independent of p of x t is independent of theta so this is p of x t


Is it alright


So that is the numerator in that equation So let us write down the denominator So now what is q of So what do we have in the denominator We have q of


1 2 t given x naught This is what we have What is this equal to


This is equal to


You off


X1 given X naught


rho of x2 given x0


And so on the product of all this q of xt given xt minus one Sorry this is


three minus s one x two minus x one and so on


Okay uh why is this this why is this the case


Is there independent of each other like the X one X two are

speaker_1: distributions

speaker_2: X1 X2 are not independent

speaker_1: Okay thats the Markov process

speaker_2: Exactly this is the Markov process right this is the first order Markov process this is because


See this can actually be written as you can write this as q of x1 use the chain rule of probability right so you can write this as q of x1 given x0 and you have q of x1 given sorry q of x2 given x1 and x0 into q of x3 given x1 that x2 x1 x0 and so on correct


This is by chain rule of probability correct So now Q of X2 first order Markov and chain rule


Now all these terms no Q of x2 given x1 and x0 Q of x3 given so up to Q of should have written this and then written that Okay so Q this is Q of x capital T given everything behind that xt minus 1 up to x0 Now and since it is


First order Marco


So it will happen you I think you got it right but this is this is what it is


Is that alright No I will perhaps take this and put it there


Lowish yeah


Set in the above equation like p theta is it going to x t or x 0 Shouldnt it be going to x 0 here and x 1


like we had mentioned p theta of xt minus 1 given xt times p theta of xt minus 2 given xt minus 1 so on till p theta of x0 given x1 right

speaker_4: So here right you do you have a pp theta of xt term also at the outside okay so what im what what you said is correct hold on cdb

speaker_2: Let us make it a little precise So now here you have a


This is equal to you have a P of XT term here Okay And the last term here would be obviously


E t dot X naught Y naught


Yeah okay thank you thats what I meant yeah okay


Okay so now please have a look at it now in the elbow right we now have the numerator

speaker_4: okay so now the reason i did this is how did we come from this step to this step okay now there was the joint distribution of x z x x 0 to x t okay under the model we wrote that as this product and in the denominator there was the conditional distribution of latents given data and we represented that using this product is that okay


I will continue from there take this equation so now we have the elbow


equal to this


Dog off


expectation of log of


P x t please note that I have taken the dependence on theta for the final random variable t equal to 1 to t we have p theta of x t minus 1 given x t divided by


Product off


product of t equal to one to capital T f q of xt given xt minus one


I hope that all of you know how this equation came right this is what we showed okay now its a lot of algebra lets keep doing this see I will omit the expectation term here okay and only write the whatever is inside okay so that it is easier otherwise Ill have to write that bracket every time


We will write back the expectation term later okay right thats a omit


outer expectation


This is not any mathematical thing this is simply to ease of writing thats all So dont think that this is some step or something Ill write back the expectation later So consider log of f whatever is inside I will write that as log of pxt times


Well take back


B theta of the first


rather the last transition okay from the decoder I will tell you why this was taken out this will algebraically this will turn out to be easier t equal to t 2 to capital T you have p theta of xt minus 1 given xt


Uh divided by


do the same thing with the encoder also the q of x1 given x0 take that out okay and what is remaining is t equal to 2 to capital T


Q of


XT given XT minus one


Right now uh this log I mean this log is for everything


Okay


Now this is I use the law of logarithms and pull these things outside P of XT times P theta of X naught given X1


Invited by


X1 given X naught


Uh the second term is plus log of this one product T equal to two to capital T


B theta XT minus one given XT


divided by


You will


xt q1 xt minus 1


Okay they should be all right this is simply log logarithms


Now you consider what is important as the second term okay so consider


The denominator in the second term


So which is Q of x t minus x t minus this is the forward distribution that we know of right So now this can be written as Q of x t given


x t minus 1 and x naught Can I write it this way Now why do I do that This is because of algebraic convenience So as we will see later no if we write this then the elbow optimizing the elbow will become easier There is one like vague interpretation that people have given in the original paper I will also mention that but this is mostly because of algebraic convenience Okay Please observe this carefully This is one non trivial step Can we do


this can we write q of xt given xt minus 1 as q of xt given xt minus 1 and x naught are these the same

speaker_1: Markov process is independent of the

speaker_4: Yeah it is because of the first order Markov property If you condition it with anything else than the previous state it is exactly the same


Now what we will do is we will use Bayes law


And the height this has


View of


Its t minus one


given xt and x0


You off


xt given x naught


divided by


u of xt minus 1 given x naught


What is this This is simply the Bayes law right I mean you have probability of A given B and C can be written as probability of B given A and C times probability of B given C divided by probability of A given B That is Bayes law with three variables Is that okay So this is Bayes law


Please uh with which


three random variables you can please check that out in Wikipedia okay is that okay this is simply Bayes law so now note that the first distribution that you have right in the numerator okay what is this


Well write that down The skew of


60 minus 1


Given Xt and X naught


What is this distribution can somebody guess


Which is D


Distribution of


xt minus 1 given given


the encoding process


encoding process has started


Started from x naught okay


Landed at


60


t equal to t okay see please note that this is not the forward distribution


forward distribution what is forward distribution Forward distribution is Q of XT given XT minus 1 Okay So this distribution is that while you are constructing the forward process okay what is the distribution of XT minus 1 How does the distribution of XT minus 1 looks given that you have started from X0 and landed at XT at T equal to T


Does it make sense Do you understand what this distribution is


Basically if you start from x naught okay depending upon what kind of noise that you add at like or what kind of samples that you get for epsilon


XT can be very different correct


Do you agree


Starting from x naught you keep adding noise Please focus on this and like respond to me okay if you understand and not understand because this is the key you have to understand this What Im saying is you start from x naught okay and keep adding noise Now depending upon what sort of noise do you add you end up at one particular xt


Okay so every time you take the same X naught and add different kinds of noises you get two different XTs do you agree with this


The question that we are asking is given that you have started from x naught and landed at a particular xt what is the distribution over xt minus one

speaker_1: Question

speaker_4: Does it make sense See note that this is not Q of XT minus 1 given XT because we are talking about independence between XT given XT minus 1 and the other thing right we are not talking about independence of so XT minus 1 is not independent of XT or X naught given XT correct


Markovian process says that xt is independent of everything else given xt minus 1 It is not saying that xt minus 1 is independent of xt Im just saying that it is in the reverse direction and therefore this x0 cannot be removed What did we do Please note again we had a q of xt given xt minus 1 term in the in one of the terms in the in the elbow wrote that q of xt given xt minus 1 in terms of I mean just conditioned that x


minus 1 x uh with x naught that is okay because its markovian once we did that we use bayes law to invert that okay and wrote this distribution in terms of q of x t minus 1 given x t and x naught q of x t given x naught q of x t minus 1 given x naught and this distribution q of x t minus 1 given x t and x naught is simply the distribution of x t minus 1 given that the encoding process has started from x naught and landed at x t at t equal to t


Any questions yes


One question that might come up here is that why did we even write this as write this in terms of this q of this this weird distribution right is because see if you keep it q of xt given xt minus 1


What you see is the numerator okay is going in one direction okay theta is decoding distribution is going in the reverse direction and the denominator is going in the forward direction correct as it is


Okay so if you want to optimize for the elbow you cant simultaneously do it from both the directions


So the idea is to represent the forward direction also somehow in terms of I mean introduce the reverse direction transition in the forward direction also and that is why we use the Bayes law to invert it Now once you do this what happens you see you know this q of xt minus 1 given xt and x0 is actually going in the reverse direction


So that is the algebraic convenience that we wanted and thats why we wrote it this way okay


okay so let us get back to elbow now so now uh getting back to elbow sir one question yeah if we do not

speaker_1: Like if we do not have x naught then also we could have come up with this base rule right Like were just based on xt minus one and xt

speaker_4: Your voice completely broke off Was it only for me


I cant hear you at all

speaker_1: Okay let me repeat sorry am I audible

speaker_4: Yes yes

speaker_2: This is clear for us uh budget

speaker_1: Sir am I audible to you

speaker_4: I cant hear you uh any anybody else can hear me yeah we can hear him uh yes sir

speaker_1: Sir am I audible now

speaker_4: Can you hear me


The cord is disconnected just a second


Oh can you hear me

speaker_1: Yes sir

speaker_4: Okay so you were saying something I mean I completely missed it because I think some connection issues Can you repeat what were you saying

speaker_1: Yes sir Im audible

speaker_4: Do you know Yes yes

speaker_1: Okay Im saying if we did not include the x naught term then also we could have come up with this like a backward distribution q xt minus 1 given xt

speaker_4: No you cant know because how how do you do that


then you will have marginals over so you can use the Bayes law and simply write it as q of xt minus 1 times q of xt divided by q of xt minus 1 right uh but you will have to find the marginals of q of you have to you will get terms like q of xt q of xt minus 1 and so on right these marginals are not computable


Okay so however what we will see now we can compute to both q of x t given x naught and q of x t minus 1 given x naught We will see that in a while okay


Okay great so let us get back to elbow so what we were doing was


Albors we had log of log of p x t times p theta of


x naught given x one divided by


x1 given x0 this was the first term second term was plus log of


of product T equal to 2 2 capital T numerator was P heat of XT minus 1 given X


Divided by


You off


xt it was given xt minus 1 right xt minus 1 and x0 we just conditioned it on that okay and lets use the Bayes law if we use the Bayes law then whatever we had written there


Step two


What would this entire thing


But I better to write it down again okay fine log of thought Ive saved on time


does not give give x1 divided by


u of x1 given x naught plus


Log off


uh product equal to 2 to capital T we have P theta of XT minus 1 given XT


divided by okay we will use that Bayes theorem that we had written this was q of xt minus 1 given xt and x0 times q of xt given x0 divided by q of xt minus 1 given x0 okay so I will just show this to you have a look and let me know if it works


How did we do We went from here to


And that jump was done using the intermediate steps Is that clear


Just have a look and let me know if it if its clear


Okay let us continue then


Again copy this let me read this


Log off


to capital D


heat of xt minus 1 given xt


x t minus 1 given x t times the denominator of the denominator comes up q of x t minus 1 given x naught


Divided by


of xt minus 1 given xt and x naught times q of xt given x naught correct hmm now observe what happens to this product now so this product


a speed heat of xt minus 1 given xt times what is this product

speaker_1: of xt minus one given x1

speaker_4: divided by hold on so this is q of x t minus 1 given x t and x naught okay t equal to 2 to capital T so this term into we have terms like q of x 2 right so this is a x 1 given x naught into q of x 2 given x naught and so on in the


In the denominator we have Q of x2 given x naught


x3 given x naught and so on right


So these terms will cancel out Only two of the terms will survive Can you see that


So what terms will survive We will write this down now log of p xt into p theta of x naught given x1 divided by


u of x1 given x naught


plus log of only two terms would survive what are those terms well have q of


x1 given x0 that is the first term that would survive in the numerator in the denominator we will have q of


p given x naught okay everything else will cancel down the other term that we have is plus log of product of t equal to 2 to capital T


P theta of x t minus one given xt divided by


u xt minus 1 given xt and x naught


All right


Is it okay


Everyone with me so far


Okay so now look at this no there is q of x1 given x0 log of you have log of ab by c okay so this is log of ab minus log of c and there is this this term and this term gets cancelled away right Thats why we took that x1 and x0 outside in the beginning


Now this will become log of a plus log of b I can combine them and write that as log of p of xt okay times


I will just trying to skip one step thats why I was looking at it okay let me skip it anyway so log of log of p theta x naught given x1 okay plus


Log of log of PXT divided by


2 xt given x naught


Come on


equal to 2 to capital T


Log off


E theta xt minus 1 given xt divided by u of xt minus 1 given xt and x naught


All right can you see that


We are almost done with three more steps


So note that there was an outer expectation right So bringing


bringing in the outer expectation


Okay so what did we have We had the expectation of it was Q of Z given X right What is Z 1 to T given X naught So this is our Q of Z given X okay And this entire thing just this elbow which is whatever were out no log of P theta of X naught given X one


plus plus two three terms i will not write it again okay now what is to be noted is this will be equal to expectation of okay log of p theta of x naught given x1 okay this outer expectation now will be with respect to q of x1 given x naught why is this


while the outer expectation was with respect to q of x1 to t given x0 since whatever the function that we have are only uh uh the functions of x0 and x1 the outer expectation will become function of x0 and x1 is that okay


Now uh similarly to the second term welcome to the second term

speaker_2: sorry I missed to understand that part expectation of Q of X 1 to T X 0

speaker_4: given x naught will become an expectation with respect to q of x 1 given x naught because the term that you have inside the log now it is independent of all other random variables other than x naught and x 1


That is like uh like law of expectations okay hold on um


We have


we have this conditional expectation argument which can be done okay so hold on okay so this is the first term so the second term would be


We have the same thing expectation of


of log of what was that term P x t divided by Q of x t given x naught and this expectation is with respect to Q similar argument take x t and x t minus 1 given x naught


Everything else will be going away correct

speaker_1: So y ht minus one here

speaker_4: I think yeah I think I made a mistake here while writing


Uh see here


Oh this was my mistake sorry so here


Uh a q of x naught


hold on hold on uh x12


Yeah that should only be XT


Its only Q of x t given its not correct


This is this is what it is


Now the third term


What dependencies do we have Let us write it that way


take the expectation inside the sum because it is linear to to t expectation of we had log of

speaker_1: From X1 to XT minus 1

speaker_4: P theta xt minus 1 given xt divided by


Q phi of no there is no Q phi sorry it is Q of


x t minus 1 given x t and x naught okay dependency is on q


XT XT minus one given XT given X naught correct


is fine now


Should be alright


One last step C represents us


x minus 1 and x not right this should be


Just thinking if I have to do it or uh


Boom


Give it as an exercise


Okay see what we should do is after this okay let me write that down This is equal to lets write the first term The first term is expectation of log of p tilt of x naught given x1 Expectation is with respect to q of x1 given x naught Okay what is the second term The second term is simply the KL divergence no KL divergence between


You also


T given X naught


TXT this is by definition


And if you look at the third term the third term is also can be written as t equal to 2 to capital T There is an expectation with respect to Q of XT given X naught times


a KL divergence between


Q of xt minus one given xt and x naught


and p theta of x t minus 1 given x t okay so here is where the tricky part is ill tell you that okay the first term and second term are okay no so the second term here


This thing is simply recall divergence right by definition that should be all right correct

speaker_1: Minus scale like

speaker_4: Yes of course of course negative of kL divergence So now what happened to the third term Thats tricky right So what we actually did is here we express this expectation right You have an expectation with respect to q of xt and xt minus 1 given x naught correct Okay You can write this as product of two expectations okay 1 over an expectation of q of x


T given X naught times the expectation over


You up


Okay I dont have space here


I just want to form a


create some space and write it now we have


Expectations


something right with respect to we have q of xt given sorry xt and xt minus 1 given x naught okay now this can be written as product of two expectations first expectation is q of xt given x naught okay and the second expectation is with respect to q of


x t minus 1 given x t and x naught This is similar to Bayes rule okay This is called the property of conditional expectation


You either please take it as a homework or can ask PS to do this


is a like known result okay this is a simple you can actually write this down you can write this expectation uh with you use the bayes law and use the law of conditional expectations this is called the law of conditional expectation


Here property of conditional expectations please have a look at it Now if I do this and write this expectation in terms of product of two expectations


then what will happen The outer expectation is still around Whatever is the inner expectation now which is you will have an expectation of Q XT minus 1 given XT and X naught log of P theta of XT minus 1 given XT divided by Q of XT minus 1 given XT X naught That is the negative of KL isnt it between these two distributions


Is that alright


Do you see how we got the third term


Any questions on this


Okay so thats it I mean we have to now interpret this and compute this so now what did we do so far is that


elbow for TDPM


So we just


only a function of theta


We wrote that as


Expectation of log of p theta x naught given x1 with respect to q of x1 given x naught


Minus


BKL


Q of XT given X naught and XT


Minus


This is a tiny town


Oh I paste this

speaker_2: Think if you long press on the screen and

speaker_4: Uh huh what what should I do


Select P


You seem seem to be an expert in this


How do I move it now No I cant move it


Painful yes yes


This is what we saw So now its this is all it is and we are done


at the interesting structure no if you look at the structure what is the first term


The first term is very similar to the reconstruction term


BAE right


x0 is your data x1 is your uh first latent variable you are records reconstructing the data values in the first latent variable that is the first term okay and what is the second term the second term is


Same as the prior matching term that we had in BA


Very similar to prior matching because x t so look at this now this is like your q of z given x right


P of Z thats exactly how it is


two terms are very similar to the vae but the other thing other thing to that is to be noted is see this second term is completely independent of theta there is no dependence on theta at all so you can completely ignore that while while training okay whats interesting is the third term this third term right


I dont want to change it this is called the consistency term


Or they call it the denoising


denoising matching term


So look at what is happening okay so what is happening is that


at every step t okay p theta of xt minus xt minus 1 given xt is telling you how should the model move to xt minus 1 given xt that is what you need to learn so this is the one that you should learn okay so what is this term saying this term is saying starting from x0 okay and given the fact that you have reached xt tell me what is the distribution of xt minus 1 this is saying given xt


tell me what should be the distribution of x t minus 1 So now if you minimize the KL divergence between these two terms intuitively what it will lead to is that if you traverse through p theta of x t minus 1 given x t you would eventually get to distribution of x naught isnt it


Because what you are saying is this distribution Q is telling you that this is known okay This is known This is telling you that given that I have started from X naught and reached XT what is the distribution on XT minus one This is telling me that given XT how should I go to XT minus one So now if I match these two terms it is actually matching denoising right


This I can call it does it match the denoising


And this is


Learnable denoising


where we are whatever we know how to we are we know how to denoise and we are matching that denoising with uh with the learnable denoising so that we can generate data and of course from a hold on i i know this from a mathematical standpoint this works because finally what we are doing is minimizing the kl divergence between the model distribution and the data distribution via elbow optimization that is what we are doing okay now what we will do next is we will take this consistency or denoising


machine term and we will see how to compute it in practice that is what we will do next but I hope that you understood what these three terms are in GDPMs elbow okay any questions here

speaker_1: So it will help

speaker_4: Yeah yeah

speaker_1: So here how are we evaluating the known denoising term


Thats the next thing

speaker_4: Thats the next thing that we thats the next thing that we will do I dont know


derived now we will see how to compute it known denoising term has to be evaluated now we will do it


That is what Ill do next


Yeah let me go on quickly


Can you make it quick please


Uh I mean how are the the third sum


That is because similar argument no dependency is only on xt minus xt xt minus 1 and x0 here the expectation was q of x 1 through t q and x0 okay see dependence of whatever is inside is only on xt xt minus 1 and x0 isnt it thats all

speaker_1: But the log term that

speaker_4: But the random variable see that see expectation outer expectation is with respect to x 1 2 3 2 1 2 t given x naught correct


Right now what are terms we can drop in X1 to T is the question


You can only drop everything other than xt and xt minus 1 thats all

speaker_2: Okay so that given XT is also included when we compute expectation

speaker_4: Isnt it See the distribution does not change What changes is the dependency of whatever random variables are not there You can just omit them from the distribution joint distribution Its actually writing this joint distribution right in terms of so okay So what actually is happening is you see that we wrote it this way no Where was that


So we wrote this was the expect this was the distribution with respect to which we need the expectation isnt it Okay hold on it is still coming up Correct This is the distribution with respect to which we need the expectation and we wrote it as a product of so many things right Now when you write it as a product of so many things whatever distributions that are independent you can just remove them and they are constants Thats all will happen Okay What will remove what will remain are the ones where the dependencies


So there will be q of xt given x0 and q of xt minus 1 given x0 I have written that as q of xt comma xt minus 1 given x0 thats all


Makes sense now Yeah


Okay anything else


So now what we will do next is that we will see how to compute this denoising like known denoising term and learnable denoising term and we will build a model that is what we will we are going to do Why is my screen stuck Yeah that is what we are going to do next and that is how you try in our DDPM and we will see how to sample from it


Okay uh shall we take a break then this is a good time to take a break


Okay shall we make it a shorter break Because people might have a hard stop at 12 15 12 20 Well make it a short break So this is 11 7 in my clock Let us get back at 11 15 huh 11 20 or 11 15 What do you want


1120 lets get back at 1120 okay


So please be exactly at 1120 well continue from here okay see


Hello all shall we continue shall we resume


Let us uh look at the


What have to do is


Compute the consistency term now So it is simply the KL divergence


Between


You off


X three minus one given next year and next month


Each it off


T minus one given


is what the term is okay first we need to consider


Somebody was asking know how to compute this so let us see how to compute this


Lets consider this


how to do this so this lets use base log


Q of XT


Given xt minus 1 and x0


u of xt minus 1 given x naught


divided by Q of


X t given x naught this is base log


What is this equal to this is equal to you are


Is this alright

speaker_1: Because of macro processors

speaker_4: Yeah it because of the Marco process


xt given xt minus 1 and x0 is simply xt correct give me q of xt given xt minus 1


Should be alright yeah okay now


So we know how to compute this no this we have this we know what distribution it is and we have to consider


the distribution of


You up


XT given X naught is what we should do


We need this okay how do we get this is the question


Actually we can get this


we obtained


using recursion


you how you have


Okay so what does this distribution by beta win This is


Distribution of


yet


latent variable


Given data


Yeah how do we get this is the question so we have


xt be equal to root of alpha t times xt minus 1 into sorry plus root of 1 minus alpha t times some epsilon where epsilon comes from normal 0 1 okay let me call this as some epsilon t minus 1 okay i mean this is simply a sample from normal 0 1 there is nothing sacrosanct about t minus 1 but let me write it that


way just to differentiate it algebra so this now i can recurse over this now this is square root of alpha t okay into what is xt minus 1 root of alpha t minus 1


XT minus 2


root of one minus alpha t minus one


We call this as an epsilon t minus 2


root of one minus alpha t times epsilon t minus


This is all right


Okay now this


You can keep recursing the still you get x x naught but well have to see uh how to how how one step of recursion happens and then we can generalize it okay So this is equal to a lot of space to write this this is equal to


a square root of alpha t


Endo


alpha t minus one


xt minus 2 xt minus 2


That is the first term the second term is


root of alpha t minus


alpha t times alpha t minus 1 into epsilon t minus 2 plus root of 1 minus alpha t times epsilon t minus 0 correct


Okay now um


It should be done as


Okay so consider these two terms


these two terms okay which is root of


alpha t minus alpha t into alpha t minus 1 into epsilon t minus 2 So this this we know


is sampled from a Gaussian


That has zero mean


And


variance to be equal to alpha t minus alpha t into alpha t minus 1


I use I


Do you agree


Why is this the case This is because


again reparameterization right so you have a Gaussian uh you have a scaled Gaussian so epsilon t minus 2 is I have to write this one epsilon t minus 2


is again normal 0 1 okay if its normal 0 1 then something scaled with that will become another Gaussian with a different mean and variance agreed okay so this is one random variable and we have another random variable here which is


a root of


One minus alpha t times epsilon t minus one This is again Gaussian


Zero mean


Variances 1 minus alpha t times


Is this okay


Okay now what we have under that


Different colours


Even uh it is not a good colour


of this gown


Where did that colour go


B


corresponds to


And therefore


is another random another Gaussian random variable because sum of two Gaussians are Gaussians you know that right Gaussian random variable with the following properties so now T is the Gaussian okay


zero mean okay and the variance to be equal to one minus alpha t alpha t minus one


I so you can please verify this


take some of two Gaussian random variables with these particular mean and variance and add them and see what happens to the variance


Okay so this implies that I can write


60 the as


Root off


alpha t into alpha t minus one


So x minus 2


another random variable which is one minus alpha t alpha t minus one


Some epsilon


T minus 2 where epsilon T minus 2


I already use epsilon t minus two lets call this as epsilon star t minus two which is Gaussian 0 1 okay


You can simply see what I just did and take a take a minute and let me know if it works


So what did we do Xt was given by the forward equation okay Just recursed over that When you recurse over it you will get a sum of two Gaussian random variables with different means and variances sorry different variances means are both zero And we combine those two and reparameterize it into another Gaussian random variable and we got that final equation


Is it all right questions on this


be fine now its easy yeah so now I can do this again go recursively I can keep doing this this implies that my xt assume it now


implies that my x t e x t can be written as root of


alpha t alpha t minus one up to


Uh alpha


one right alpha one yeah alpha one times x naught


root of one minus product of


No I cant


the product later so one minus uh alpha t same thing alpha t alpha t minus one of two up to alpha one uh times epsilon


ch is equal to root of sum


i equal to one to t alpha i


Fix not


root of one minus


equal to one to t


alpha i times some epsilon this is equal to


root of alpha t bar times x naught plus root of 1 minus alpha t bar


Times have saluted


Gosh


Root of alpha or rather alpha t bar is the product of all that


for t bar is the product of all the alphas up to up to t


So now this is an equation So now what does this actually mean Okay let me write it


distribution and also then interpret that alpha is 0 normal 0 1 So this implies that we have Q of X T given X naught What is this


is this this is equal to this is a normal distribution again because this you know reparameterization the distribution at xt a mean is root of alpha t bar times x naught


And the variance is one minus alpha t bar


note what where did we come from uh we wanted to compute the consistency term and uh we we had this uh known denoising term and we used Bayes law to do that so for that we wanted q of x t given x naught and x t given x naught is computed recursively see this actually means that


yet


Latent


sample the latent sample


The th latent sample is also th noisy sample no


in the forward the encoding or the forward process


process can be obtained


In one step


Retort


Adding the noise


Eight times


So this is actually because of recursion thats all right Use the above recursion and found out that the tth latent variable in the forward diffusion process can be obtained in one step starting from x0 without having to hop the Markov chain for t steps All right is this okay


This is another consequence of uh of uh having this first order Markov chain with recursion right You can we can do it that way


Kara gunda

speaker_1: So judges are did

speaker_2: We just prove that a Gaussian of Gaussian is also a Gaussian

speaker_4: What do you mean by caution of caution

speaker_2: Uh because I mean we are taking so if you s if you look at the steps right


So X two is obtained by taking a sample from a Gaussian and then X three is

speaker_4: Where is X2 no no X2 is not from epsilon is from Gaussian no X2 is not from Gaussian

speaker_2: But if you see the the forward Markov chain I mean thats what we do right we take a Gaussian of the result and then again sample from another Gaussian

speaker_4: Im not getting what youre saying See X XT is obtained by this equation no where is another question here

speaker_2: But then it it depends on uh ultimately depends on X naught right

speaker_4: Of course it does so

speaker_2: One thing I can say

speaker_4: One question

speaker_1: In between we are applying multiple Gaussians

speaker_4: not applying any Gaussians no you take x naught and sample from a Gaussian distribution and add it to x naught thats what we are doing

speaker_1: Yeah and and we keep doing that

speaker_4: There is no application of Gaussian We are sampling from Gaussian adding the Gaussian yeah that we are doing

speaker_1: I mean does it mean that ultimately say the last result that we get is again a Gaussian right with the different parameters

speaker_4: Team will be the last result

speaker_2: And also

speaker_1: So yeah this

speaker_4: Distribution of

speaker_2: Distribution of

speaker_1: Its

speaker_4: B correct that is a Gaussian so

speaker_2: And the intermediate steps were also Gaussian Correct So with the different parameters So my question is did we just say that if we keep taking Gaussian and then sample and then again take again keep sampling from a different Gaussians the end result is the again sampling from a single Gaussian

speaker_4: Ah that is reparameterization no

speaker_2: So that was my yes I mean that was my point

speaker_4: Hi to okay so it you it is not a question I was expecting

speaker_2: No it was not it was not a question

speaker_4: You are making an observation yes yes yes correct yeah so now you can reparameterize any you know any amount of Gaussian addition in terms of Gaussians thats all it means yeah


Okay anything else Okay so now what did we do is we now know lets get back to this Our goal was to get the


consistency term estimated no so now we had a


This is the distribution that we had in the KL right So this is equal to


by Bayes law okay and then we use the


One Cohen property here is Q of xt given xt minus one


times u of xt minus one given x not


divided by


xt you know x naught okay this is what it was okay now uh


So we know the first term we do what is that that is the definition of the forward process So its Gaussian at xt and we have root of alpha t times xt as the mean


The variance was 1 minus alpha t


minus alpha t times i so the variance correct that was the first term what about the second term we just found that out right here we found out what q of xt given x naught was that was another Gaussian with a certain mean and variance let us write that down


So this is Q of XT minus 1 given X naught No that is another Gaussian Gaussian is at XT minus 1 Thats the random variable T mean is root of alpha T minus 1 bar times X naught


And the variance is one minus alpha t minus one bar


I


from here okay


comes from whatever we just derived through uh recursion and in the denominator we have another Gaussian

speaker_1: Sir sorry to interrupt the first term it should be a root of alpha t into xt minus 1

speaker_4: of alpha t into x t minus correct times for the correction so this is x t root of alpha t bar times x naught thats the mean and the variance is 1 minus alpha t bar times i


Is what uh what is the LHS LHS is Q of


xt minus 1 given xt and x0 is what we called as the known denoising term right thats what it is okay now look at this see this is if all the terms have things like this now you have e power minus some quadratic term now you have xt minus some mean time bar or rather its all identity so it will be like this it will be


xt minus


Some mean


Square okay


times e polar minus


x t minus 1 minus some other mean squared divided by same thing e power minus


so on right now um see observe that the distribution that we have in the left side is a distribution on x t minus 1 okay what should we do now can somebody suggest what should we do now


And we know all these means right We know all these means and variances Uh what should we do now


So what to be done is e power


I am this


60 minus 1


minus one


minus sum mean


Express it this way Okay Now how do we do that This we do by what is called as completing the square


Does all of you know how to complete this square or what do you mean by completing this square


This means that suppose you have a term a quadratic term like this no x squared plus bx plus c okay you can always add some lets say some


d times x minus d times x you can add and subtract things and write this in terms of say x minus some p squared plus some constant you know this no this is called completing the square right so whatever expressions do we have inside the exponentiations we need to complete the square in terms of xt minus 1 okay well get some mean and some variance


Is that all right Can all of you see that


Let me show you the calculations I will skip the calculations you can simply go through that I will just show you that


Do it later

speaker_1: Sir what about the XT term

speaker_4: xt term will become a constant right because the lhs is conditioned on xt so xt is xt is given a particular xt it is a constant as far as xt minus 1 is concerned


Can you see my screen


Hello can you scheme see my screen Do you see my screen

speaker_1: Yes sir yes sir

speaker_4: this is what im talking about see uh we have these three gaussians right there is one gaussian uh for q xt given xt minus an x naught there is one gaussian for the second distribution and one for the third you have to write down all these gaussian distributions and use the appropriate means and variances and you should you should simply complete the square this is the uh the calculation that im skipping see its only algebra okay its like high school level algebra please follow this and i have given


paper to you okay so please say this algebra finally what will happen is this will become a Gaussian distribution okay with a certain mean and a certain variance because you have completed the square and you can look at this now that all you have to do is rearrange the terms add and subtract the terms such that it will become it will assume a Gaussian distribution form and you should read out the mean and variance thats all we should do


Is that okay So please follow that I will skip this and only write the final mean and variance because its simply an algebra Did you understand all of you


Its not complicated huh You have you just have to run through the algebra


Alright is it okay


You can go through it and if you dont get it you can always come back to me and I will tell you its not at all difficult youll easily understand that


Your screen


Now this term will become so Q of


xt minus one given


X t and x naught now became a Gaussian distribution right


is a Gaussian distribution okay distribution is at xt minus 1 the mean is lets call that as mu q okay and that will be that will be a function of xt and x0 because these are conditioned on xt and x0 and there will be some variance call it as sigma q this will only be a function of t or alpha t it will be independent of Ill write down what these are the mean of this distribution mu q


The function of xt and x0 is given by


root of alpha t


One minus


minus one


Lexus


into x naught


divided by 1 minus alpha t bar


Now note that the both of these terms right both of these terms are known


And computable no


So now this means that this known denoising term can be computed So we know alphas we know xt we know x0 we know all of this So that can be computed So this is typically written as some sigma q squared times


Identity awareness


this entire thing is written as sigma q squared to the constant okay that is what is done


questions so far I think this is fine no now what did we do so we wanted that the third term in the elbow was scale between


xt minus 1 given xt and x naught and we had p theta of


XT minus one given XT okay


is what we had okay now in a DDPM


The decoding distribution


Its called decoding distribution or


Denoising distribution


Its also called the reverse process


This process is assumed to be a Gaussian


is in place


Each heat off


xt minus one given xt


This is a Gaussian


minus 1 with a mean mu theta this mu theta and the variance the variance of this is assumed to be equal to a equal to constant constant which is assumed to be equal to what the true thing is so only the mean is estimated variance is assumed to be constant in the in the normal course okay in the literature variance is assumed to be a constant okay


Okay now what happened is that because its Gaussian so we have


Greater divergence


The main Q


t minus 1 given


X t and X not


Eat it off


XT minus one given XT


is now


A clear divergence between


Gaussian


parameterized at mu q and sigma q


And this is a Gaussian that is parameterized


mu theta and sigma cube


Is this all right


Now KL between two Gaussian distributions


Known to be I mean it can be analytically computed is given by half log


determinant of sigma Q


minus d where d is the data dimensionality


The years of


Im not sure


It was


It mark you


mu theta minus mu q transpose


quadratic form sigma q inverse mu theta minus mu q


just take this as a homework and do it show that the gaussian distribution between two uh sorry kl divergence between two gaussian distributions can be computed this way this is equal to


half this is log one which is zero so like okay let me write it log one minus d trace of uh uh inverse of uh sigma q inverse times sigma is also equal to d that can be shown because its just constant times identity no d dimension it will just add up to be d trace is the sum of the diagonal elements if its a diagonal matrix plus so this log one will go away these two d will go


away sigma q inverses a so you have mu theta minus mu q transpose


Now this is small sigma q squared i this is what we have written that as this is mu theta minus mu q


its all so this will be equal to half


an inverse here okay so it will be uh 2 sigma q squared times


Normal


You take down when this includes question


is actually the elegance and beauty of DDPM


After doing all that the final denoising matching term will simply be a mean squared error between two means


Thats all actually we are done There is the other the rest of the things that we do is only some reparameterizations and well see how to implement this using a neural network Any questions here Yeah Sanchit

speaker_1: why are we assuming that the decoding distribution is Gaussian and like in a general case

speaker_4: I cant imagine thats


Ill take that is because see we are not assuming the distribution of data to be Gaussian We are only assuming the conditional of the latent given another latent to be Gaussian Okay That is one thing Why are we doing that assumption is that what can be shown is if you have a forward Markov chain okay with Gaussian transitions there exists a real reverse Markov chain that also has Gaussian transitions is something that can be shown


Okay but what changes is the parameters


changes as the parameters so one is mu theta the other is some other parameter no so but what can be shown is that if the if you have a markov chain whose forward distribution is uh gaussian transitions are gaussian okay then the backward distribution uh is also gaussian with a different parameters

speaker_1: So like in VAE also we try to assume like what Im trying to understand

speaker_4: And reporting distribution

speaker_1: Sorry that please continue


So like for VAE also like we were trying to you know mod like assume that the latent space will be a Gaussian distribution like a normal distribution And you know so like why are we so much biased towards a Gaussian distribution in almost all of the models

speaker_4: No no see that is a design choice you can see while in a naive VAE we assumed it to be Gaussian but in all VQVAE and the other Vampire etc it can be modeled as something else right Similarly see but here what you should see is that the stationary distribution here which is the distribution of the tth latent is assuming is assumed to be Gaussian We are not assuming the intermediate distribution to be Gaussian but only the conditionals are assumed to be Gaussian


Which is okay


and i mean yeah why are we assuming it to be gaussian is because like its an isotopic distribution right i mean uh it has it is a distribution that has infinite support so it is easy to work with there are diffusion models where they have used another uh i mean other exponential family of distributions but they lead to a similar thing because see note that nowhere we are assuming that p of x naught is gaussian this is not gaussian at all right so p


theta of x0 which is our data distribution is actually given by the product of all those distributions right we know that um we can use the chain rule and do it so the conditionals are assumed to be Gaussian which is okay you can have conditional to be Gaussian and you can use the Gaussian conditionals to model any distribution of interest


So that way I mean if your question is that isnt Gaussian as Gaussianity assumption restrictive here it is not restrictive at all it can model any distribution only the conditionals are assumed to be Gaussian Now why are we doing that choice in in in in the reverse process of DDPM is because what can be shown is that if you if you construct a Markov chain with Gaussian transitions in the forward direction the reverse transition also happens to be Gaussian okay with different set of parameters is a known result


Thats all right


It is not no we are finding out mu theta here It is parameterized by mu theta we will find that out no


See now finally what we are finding out is this mu theta mu theta is something that we find out

speaker_3: But that cannot be arrived

speaker_4: no no no that is our model right that is that is the whole point if you start look at the forward model that we

speaker_2: One problem that we start

speaker_4: fixed is known of course it is fixed you see this you see this p theta mu theta and sigma theta are learnable but in practice what they do is they they make sigma theta a fixed thing only mu theta is learned


So that is our model see if you make the reverse process also fixed then what is what are you learning

speaker_2: Yeah understood


Yeah I understood sir

speaker_4: Is this okay so finally it all boils down to I think Im doing a multi scale thing here right one thing is at some scale the other is another scale you just look at this


The day


zoom it inadvertently somewhere and itll become that should not be an issue for you know when you go back and look into it I think you can you can also zoom out and zoom in and look into that in different scales I suppose right

speaker_1: Is this a big guy

speaker_2: Printouts

speaker_4: Because of the scale issue because of the scale issue

speaker_2: Because of the scale issue because of the scale issue

speaker_4: I see okay

speaker_2: So how do you


We dont print that much but if sometimes we like to take a printout then

speaker_4: Uh

speaker_2: Taking a com petitive stance

speaker_4: The positive side of it is you know Im helping the environment so its fine


Okay so is this all right So what happened is that finally this elbow thing


Why dont you


There is this term this


solve right youll have to minimize this so of course there is that another term no this was minus k l there was this term of expectation of log of e theta of


x uh one given x naught this was also one term so thats all right so these are the uh two last terms that are that is there in the elbow so well have to now implement these two things using neural networks okay and then when uh like uh


Estimate these two terms minimize them and then learn how to sample from it See those two things have to be done I need at least half an hour to do that Shall we stop here Because it will be nice if I do it in one stretch Ill do it in the next class


Well the only problem is I wanted to do that today because I was planning to give your assignments out on like like Sunday at least tomorrow


Okay maybe Ill quickly tell you how to do that so that you can like start looking at your data building these things Okay shall I take 10 more minutes


Okay so that at least you know how to train this


Now lets do this reparameterization We can actually implement it this way but people generally implement it in a different reparameterization Let us do that We have reparameterizing

speaker_1: So there will be the KL divergence term also right

speaker_4: No that is the third one is what we showed as this uh difference between the mix second one

speaker_1: No no no essential

speaker_4: That is independent of theta no we can ignore that

speaker_1: So sir what will be its use for like which term which component will it be used for updating in the TDPN

speaker_4: What I didnt get the question which term what will be used for

speaker_1: Sir the KL divergence term that was independent of theta are we saying that we wont be using it anywhere for updating the

speaker_4: Yeah because model training of course no it is independent we dont there is no model at all there is no dependence on model it is a constant as far as the model is concerned


This comes because of the fixed forward process right And also yeah this primarily comes from fixed forward process okay So I will maybe quickly tell you what this is and handwave and do the math the next time okay So that you can start implementing See whats the idea is you have this term no You have mu theta minus mu q as your loss okay Now what is done is we have this mu q as what is mu q Some constant c1 times


x t I had written that some other constant times x naught divided by some constant right or rather I can write it as a some linear combination of x x1 and x naught this is how mu q was correct now we have


xt to be equal to we use that recursion and showed that xt was equal to root of alpha t times x naught okay uh x naught


Please pay attention here because this is what Ill ask you to implement okay is X naught


root of 1 minus alpha t bar times epsilon this is how it was correct now if I rearrange these terms I can write x naught in terms of xt minus root of 1 minus alpha t bar times epsilon divided by 2 root of alpha t bar okay this implies that my mu q now can be written okay in terms of


I can get rid of x naught right I can write this as some other constant k1 times xt okay minus or plus some other constant times epsilon Do you agree


All of you agree on this


Am I there audible Yeah Okay So this is all it is So this implies that I have my mu theta right Mu theta which is a function of xt I can also write this as okay some constant k1 times xt plus okay k2 times some epsilon theta okay which is a function of xt and t So what am I saying is the following Now see mu theta


or mu theta was the mean of a Gaussian random variable correct


Right I can always reparameterize that in terms of some other constant xt isnt it


Do you see what that means this is reparameterization


You get the idea


Media is


that mu theta was the mean of a Gaussian random variable okay I can always reparameterize that in terms of some other constant xt isnt it


I just have to arrange these k1 and k2 terms so Im just simply reading and meterizing them


Okay okay


that would get designated into this epsilon theta


Basically what Ive done is Ive written this mu theta in terms of some epsilon theta


Constant times XT is that okay


So now this implies that my loss that I had no mu theta minus mu q now becomes proportional to


epsilon minus


data


Didnt get it


because those constants will get cancelled away no We have like reparameterized mu theta also in terms of the same constant as that of mu q So those constants xt gets cancelled away So it will only be in terms of epsilon and epsilon theta cap


Is this clear to all of you


So now how do you implement this in practice is that you have a


please note that the dimensionality of and I will do it like more thoroughly in the next classes just to ensure that you will get started with your assignment okay you will have a neural network okay theta neural network this will have this kind of architecture is called the unit architecture where the dimensions will keep on decreasing hit a bottleneck and the dimensions will again keep increasing okay this is because the size of noise here epsilon is same as that of the input okay


So now what does it take as input Itll take input x t and t okay and this will predict


epsilon eta that is all that is all the training of GDDPM is the last function is epsilon minus


epsilon theta cap x t comma t okay now what is x t x t is as we know root of alpha t bar x naught


1 minus alpha t bar times epsilon Thats all How the result you try How do you do it


taken x naught okay and


Compute


So take x naught sample epsilon from normal 0 1


Compute XT using this equation


Okay so give that give that XT as an input to the neural network


And whatever the output is match that output with the epsilon noise that you have added Thats all the DDP Im training is Then you back propagate And you do it for multiple Ds


You are minimizing the is this clear See I mean OK I will not take any questions now because its 1220 We will start from this the next class OK I will tell you like precisely what the architecture is and how do you do this what the loss function is and all that But this is all it is Right So basically whats happening is given a data point you add some noise to it OK and you get the Tth latent variable pass that through a neural network and try to predict what was the amount of noise that was added to get


It is XT from XMARC thats all it is

speaker_2: So we pass it only once or repeatedly for the same data point

speaker_4: it in batch no do it for different ts you take all data points so we did all analysis for one data point you do it for all data points basically so for one data point you will have to sample multiple ts because you have a sum over all ts here no t equal to 2 to capital T


Take multiple Ts for a given data point try the neural network and do it for all data points that would be one epoch try it for multiple epochs thats all


Yeah theres a few trying at ADPM

speaker_1: So sorry multiple Ts per data point and we have to take batches of such data points

speaker_4: Course no because you need to train it through the entire data set


Yeah well do this well do this more thoroughly in the next class Now half of the next class will be on like training diffusion models and Ill tell you how these are related to what are called as core based models and then Ill talk about the conditional diffusion models you know where all these stable diffusion imagine dolly etc they will take a text and generate the corresponding image right how do you condition these models on text is something that Ill tell you that would end the diffusion models right uh half of the


class perhaps and the next the the other half we will do autoregressive models well start with these language models okay in the next class okay then thats it see i i i rushed through this implementation because i will give the assignment uh tomorrow so that you can if anyone wants to start doing it you can start doing it you know get your data loaders and write the equation for this noisy one get the network and start training at least so by the time next week we will thoroughly complete


it so that you can implement it completely yeah

speaker_1: So by the way I have to look for the papers

speaker_2: My name is

speaker_4: in my handwritten notes okay handwritten notes


Its always that I mean like my handwritten notes is pretty comprehensive it will have everything


Okay okay well thats it for today yeah

speaker_1: one question like not uh what this related so why cant we


9 20

speaker_4: Sure okay no problem well do it after we do

speaker_1: I am taking the quiz post 9 20 so thats why I just I am taking the quiz first and then joining the meeting like the class

speaker_4: Ah

speaker_2: Okay okay

speaker_4: Okay okay okay Two more classes two more quizzes well do it after the class no problem Okay

speaker_2: Okay cool

speaker_1: Sure sir thank you so much

speaker_4: Okay then huh So have a nice weekend Happy Diwali to all of you We will meet on second no next week next Saturday well continue with this okay

speaker_1: Certainly

speaker_2: Thank you sir and happy new year

speaker_4: Bye bye yeah
