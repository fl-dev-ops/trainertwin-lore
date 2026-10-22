---
id: uQvtdAPjKqI
title: Lec 3 - Deep Generative Models Intro to Generative Modelling
url: https://www.youtube.com/watch?v=uQvtdAPjKqI
date: '2024-11-23'
duration: 03:10:10
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

# Lec 3 - Deep Generative Models Intro to Generative Modelling

## Transcript

speaker_1: putting here


Uh yeah so just a couple of logistics things um


We will start the tutorial from tomorrow I think you have should have got a calendar invite and then I should have sent you right


So if if you people have time so please join the tutorial otherwise you can access it later and we will we will start the quizzes from next to next week okay so which means like the second Saturday from today today is 31st of last week Wednesday


Next to next Saturday

speaker_2: Fourteen I will leave

speaker_1: Yeah


We will have our first quiz on 14th hmm


Okay

speaker_2: Uh sir can we have the tutorial either on Saturday evening or any of the weekday evenings Sunday is not the weekend thing

speaker_1: And this is


See that right that please talk to coordinate with the TA because I believe that he had a He had a poll or something did he

speaker_2: North

speaker_1: Didnt he

speaker_2: No I I think we didnt got it

speaker_1: Surprising let me just call him right away and just to little data just give me a minute

speaker_2: So there was a poll actually there was a poll in that channel yeah yeah theres a poll in the channel

speaker_1: And they supply


Then okay right I mean I think the how how how when it came actually or in the in the chat window or

speaker_2: No in the channels in the general of this channel there is a poll

speaker_1: Oh okay


Yeah so so then its fine right it was was uh decided based on the outcome of that poll I suppose right

speaker_3: There were only 30

speaker_1: Okay what can we do Okay so let me ask him to have another poll perhaps and then decide just a second let me call him

speaker_3: I will carry my little toy with you

speaker_1: Hes not picking it up let I hell call back once he calls back Ill tell him


Yeah I uh


I mean its very difficult to find the time that is convenient for like all hundred people in the class okay so I mean we have to do something um so yeah so whatever works for most of the people well have to stick to that so Ill ask him to have the poll again


And then we can decide okay where is this thing at here


You see my screen

speaker_2: Not yet

speaker_1: This says it is being shared


Oh it says it has been shared here how come


Really John


Uh


Yeah tell me


Please go on somebody go ahead

speaker_3: Yes

speaker_1: Dr Telli me

speaker_3: Yeah we are able to see it

speaker_1: Okay shall we start


Oh good Yeah So a little bit of recap before we continue with todays content


Yeah so we were looking at the relevant probability theory stuff right so we have the probability triplet which is the sample space the event space and probability measure and we define this function called random variable that would give you this push forward measure right yeah so then we said that once you have this function called random variable that will move the sample space to some d dimensional real numbers and


subsets of real numbers and then you have the


corresponding measure probability measure that gets translated into the real space which we call the distribution function


Right and we looked at some of the properties of what distribution functions are and looked at multiple random variables conditional random variables independence


and joint random variables and so on okay


Uh uh before I go to the supervised learning part machine learning part any questions on the


Probability theory part


second I have to open that yeah okay yeah go on searching

speaker_2: question from last lecture so


that boreal sigma algebra so we just last week studied that in recent process class

speaker_1: Im closing

speaker_2: Uh zero to one and


just asking for this


problem you mentioned this sig borel sigma algebra is defined on minus infinity to infinity or like it is always on

speaker_1: See sigma borel sigma algebra for the real numbers right they are defined on real sets


Oh I think Ive confused right why is it between zero and one I

speaker_2: No no he just gave an example

speaker_3: Thats all

speaker_1: So you can take any set and generate

speaker_3: So you can take any set and generate

speaker_1: Yeah you can you can take any set and generate a sigma algebra on top of that right


Uh but specifically Boolean Sigma algebras are defined on L numbers right

speaker_2: Yeah

speaker_1: Yeah small h sigma algebra on R that contains all the intervals that are possible that is the full sigma algebra yeah


See that is why I did not even take the I mean to define borel sigma algebra right I said like r rd and subsets of rd and then you have the distribution function on top of it right


Uh its more anything else uh


But in such thing who is teaching random process is Aditya teaching it

speaker_3: Yes sir I did take a balance

speaker_1: Yeah we are very good friends Yeah Okay So with that we will look at what supervised machine learning is I said that the data right is defined as some n samples okay that are drawn Yeah that is what I know The notation is that you have data sampled from a particular distribution or data drawn from a distribution Yeah


actually boils down to saying that every data point that we have is an element from the range space of a random variable that we have that is x okay i mean that we denote by x so we this implies that there exists an underlying probability measure and does the distribution function induced by x okay so this is clear right so whenever we say that we have n data points we actually mean that we are sampling i mean we have n uh


vectors from the range space of the random variable once we talk of the range space of the random variable uh we uh we we understand that uh there has been uh I mean there is an underlying measure space the underlying the sample space that is there and a probability measure and therefore a distribution function induced by x okay


Now for the so called supervised learning what happens is that you have data sampled from the joint distribution of a pair of random variables x and y


where x denotes a random variable whose range space is some rd i mean i gave the example of m n straight where it is r 784 dimensions because the images are in 28 cross 28 pixels and y which is the it is another random variable that we are talking of denotes the labels so called labels and there exists two sample spaces right uh or


Yeah so two sample spaces whose cross product is what we are talking about when we talk of joint distributions And when we say data this is what we mean right We have


Basically right in other words what we are saying is obtaining data is equivalent to conducting the underlying random experiment that generated your sample space multiple times Thats what it means right We have conducted the we have we are actually running the running the random experiment multiple times We are making multiple trials right And each of the trial gives rise to some sort of an outcome Okay And that outcome


gets mapped to some d dimensional real space via random variable and because we are looking at a random experiment there is a there is a probability measure that we have assigned and because we have since we have a random process sorry random variable im sorry excuse me because we have since we have a random variable um you have uh i mean the the outcomes of these experiments have been converted into something measurable that is a d dimensional real number


That is what is happening Is this world view clear See from now on right I will not tell you that these are actually vectors in the range space of a random variable which is a function and you have the underlying measure and you have the distribution etc I will simply say that we are given a data from an underlying distribution Thats all So you should understand what I mean when I say that Is this clear


Any questions on this


Okay so now let us start with the definitions


Asters


Whatever it is


Oh I dont know what this is okay

speaker_2: Sir you need to select a plus page


in the third column

speaker_1: Speech


Okay

speaker_2: Then you can mention the titles

speaker_1: We will also putting lecture numbers right L3


So we will mostly set up the problem today right What are what is the generative modeling problem and so on Okay So that is what the major focus of todays lecture is


Now let us start with


data so this is our input right means this is the say I always represent data with


set so it is either so let us first maybe


set up supervised machine learning actually right at a at a core level there isnt a lot of difference between supervised and unsupervised machine learning i will tell you why it is


Will it be comprehends


From a comprehensive standpoint will it be better to introduce


Can all of you mute please let me do that


So let me introduce uh


in general then we will talk of the differences of data so lets say that you have data data is of this form x1 x2


XM


Make it a little abstract from now on xn and these has been drawn from some


underlying distribution px and this is unknown so this is the setting right


No


This actually means that


This keeps happening


I keep my palm over the screen right it just gets distorted I dont know how to control it let me know if somebody knows how to do that anyway so the this is thing that we have data that is drawn from an unknown distribution it actually means that see this is the central problem of machine learning that data


on


Pump boost


unknown distribution okay


Okay so this actually means that the distribution is unknown but we have samples from it So this is the the central problem of machine learning in arm statistics that you have samples from a distribution but you dont know what the underlying distribution is Okay so now the question that we ask the for the question the central question that is asked in ML is the following that


Give one


Samples from a distribution


distribution okay


Estimate the distribution


estimate the underlying distribution


So this happens to be a central question in ML that if you have if you are given samples from a distribution can you estimate the underlying distribution


Okay now why is this important You understand the question right There are two different things Having samples from a distribution is different from knowing the distribution itself Can you see the difference


Can all of you see this difference This is very very important okay


So now so the question is if you if you are given some samples from the distributions you have to under estimate the underlying distribution So why is this of importance is the question Okay The the thing is


This is important because now let me write that down


Knowing the distribution


Rabbits


prediction


Section slash sampling


Okay this is the claim So if you know the distribution okay you can do prediction and you can do sampling So now what do you mean by prediction and sampling is that see in supervised machine learning the problem is that of prediction And in unsupervised machine learning mostly the problem is of sampling All right in generative models the problem is of sampling Now to do both


request all of you to kindly mute yourself okay uh so unmuting with some noise will just cause some disturbance thank you yeah so knowing the disturbance


knowing the distribution enables prediction and sampling okay now what do i mean by this is the question so now lets say that you have


Lets take some examples


example may be that so given


It pairs off


images and labels


Ill put it in quotes because Im not defined this yet learn to


predict


the so learn to predict the labels of unseen images


This is the classical classification problem Given pairs of images and labels in terms of data learn to predict labels of unseen images So now my claim is that you can model this in the language that we have just said So now we would say that the data that has been given us is following that you have


pairs of x and y So note that whenever I write this I mean that there is there are two random variables that are there and the data has been drawn from an unknown joint distribution between x and y Right So this is given pairs of images of given the pairs of images and labels Now how do you define this Learn to predict part of it Okay So now prediction is defined as the following


Prediction is defined to be evaluate


Evaluate


likelihood


of label


You want


image


This is the definition of prediction problem I will define what likelihood is okay Now well have to define likelihood right So likelihood


Okay likelihood of


This is a very important terminology likelihood of a of a point


is defined to be


Value


of the density function


This has x uh x cap okay density function evaluated


x square so this is the definition of the like the likelihood so note that i am not calling it a probability because i am evaluating the density function remember last class i told you that evaluating the density function of a continuous random variable will not give you the probability right so that is why


I am defining likelihood of a point as the value of the density function evaluated at x okay at some point x this means that


Suppose you have a point you know suppose there is some x cap that is in some rt okay and px is a density function


density function then


The likelihood of X cap is simply the density function evaluated at X cap


Is this clear


Please note the the notations here whenever I talk of distribution functions right I write this script P you know double line P whenever I write the density functions I write small p okay and in most of the rest of the part of this course we will work with density functions not the distribution functions okay because simply because they are easy to work with okay and remember the connection between the density function and distribution functions right distribution functions are valid


probability measures okay and the derivative of the distribution functions are what are called as the density functions density functions evaluated at a particular point will not give you probabilities but density functions integrated over a range will give you probabilities because that would be the distribution function evaluated at a particular point all this is clear right


Just repeating what we did in the last class Okay great So now likelihood whenever

speaker_4: Yeah

speaker_1: Yes go on

speaker_4: So you mean to say that the likelihood function is the same as the probability density function

speaker_1: I am defining the likelihood as the density function evaluated at the likelihood at a point is equal to the density function evaluated at that point


Actually definition of likelihood see whenever we talk of likelihoods right the definition is that it is the density function evaluated at that particular point Now if the underlying random variable happens to be a discrete random variable then evaluating density function becomes mass function and evaluating the mass function at a point will actually give you probability right But in general because we are looking at continuous random variables density functions are not probabilities thats why I dont want to call likelihood as probability of that particular point because it does not


mean anything I would just want to define likelihood as evaluating or likelihood of a point is simply the value of the density function evaluated at that point and as we saw in the previous class density function of a continuous random variable evaluated at a particular point can be more than 1 okay can can have values more than 1 and it does not correspond to a probability this much is clear right


Okay now with the definition of likelihood function well have to define what prediction is Now I said prediction is simply evaluating the likelihood of the labels given any way okay Which implies that this implies that prediction


is defined the following that


But evaluate


The conditional density


X cap well have to say prediction at X cap right


Prediction at XCAT


is evaluating the conditional density at x cap so what does that mean so suppose or assume


of


Y given X denote


The conditional density function


y given x See note that whenever there is a density function there is an underlying distribution function and I am talking of conditional probabilities here Let p y given x denote the conditional density function of y given x Then


Prediction


but x square is simply equal to evaluating this density function okay but


Okay I will explain my notation and I will okay


X is equal to x cap


okay uh i will explain okay let me explain the the notation first see when i write the rotational note


P of y given x


Then whats the following So y given x


the subscript here


Denotes


random variables okay whenever i write the density function or any distribution function anything right subscript always denotes the random variables


This which is


Whatever I write inside the parentheses right denotes


value


which the function is being evaluated


Okay is this clear This is the notation See whenever I write conditional distributions right I always mean that the conditioned random variable right is fixed at some particular value


See this is the definition of conditional distribution that when I write conditional distribution it always means that the conditioned random variable is fixed to a particular value So given that the conditioned random variable has taken a particular value what does this density evaluate at Is this clear


So now in this notation the prediction what does the prediction happen what is the prediction problem prediction problem is let us call that


prediction


of X cap is simply the likelihood


that likelihood is a density function likelihood okay


the conditional density


Why do you want X


Evaluated


the value of the conditioned random variable


Condition random variable


What is it In this case it is X Okay Fix that


This is the definition of prediction See whenever you talk of regression and classification problems right this is what you are doing What you are doing is


you are doing is evaluating the density function okay conditional density function of labels conditioned on data and you are evaluating that okay with the conditioned random variable which is the data random variable fixed at a particular x cap because by definition the conditional distribution always means that you have to fix the conditioned random variable at a particular value so now given that your condition


random variable is fixed at a particular value what does the density function evaluates to that is called a prediction at x cap


Do you understand Now tell me this


When we uh okay so maybe before we go that before we go there I will perhaps Ill tell you that okay see now suppose let me take an example suppose


Y okay is a discrete random variable that takes value 0 1 2 up to k


Okay if this happens then


Prediction


Text cap


is what what is this object can somebody tell me


And we will also fix x and x lets say x is some random variable that is in some thousand dimensions We are saying that there is an image okay Its a hundred by hundred image


10000 dimensions 100 by 100 image and we have k labels So if I have to set up the prediction problem here what does predicting give me


Can somebody tell me

speaker_4: argmax of P of like even

speaker_1: No no no I have not defined it that way right Ive d look at the definition


No it wont

speaker_4: Probability density of Y given X

speaker_1: That is what Ive yeah what do you mean by that How many values does this give you If you predict it on XCAP how many values will it give you

speaker_2: So it will give us the values

speaker_3: But wait a second

speaker_1: It will give you k plus 1 values right So now prediction here means that it will give you an entire density function in this case a mass function because y happens to be a discrete random variable So you have 0 1 2 up to k here and this will have some values like this


Do you understand So now this what is this This is the density function of


y given x right evaluated at x equal to x cap


Do you understand this So prediction will give you a distribution sorry it gives you a density function right or a mass function in this case because it happens to be a discrete random variable okay which is evaluated at x cap Is this clear


Any questions on this


Now what do you do with this is a different question See now you can relate to what we were talking in the first class right given some x you want to know what the corresponding y is In the deterministic case right or in the non probabilistic treatment of stuff what was happening is that for a particular x you give a particular y okay Now here for a particular x okay you are giving me


multiple ys with with certain likelihoods associated with each of them


Is this clear Now what do you do with this Do with this is something that is specific to the user Either I mean most of the times what do we do We take one y okay corresponding to the maximum value of this density function isnt it


If you look at machine learning what people do is we want one label So we dont want the density over labels we want one label Therefore we take the argmax of this density and assign that as label for x cap However the problem is set this way that given a particular label what youre actually doing is youre evaluating the density function p of the conditional density function and that x cap


Is this clear


Any questions so far

speaker_2: one question so this x cap means a particular point in the this x x random variable

speaker_1: Uh you should be careful in in in choosing your words yeah see what do you mean by that its actually one of the points in the range space of the random variable no

speaker_2: Yeah rain space

speaker_1: But yeah that is what it is see typically right X cap typically


X cap does not belong to the data set that you have because thats the test data right thats what is called as test data


Right when you are interested when you when you are talking about prediction you can predict on X cap that is that is that belongs to D as well But typically X cap does not belong to D because you know you want to predict on unseen data right


Okay uh yeah so Vivek


Sorry is there any way we can visualize PY given X I mean P or um uh what is that

speaker_2: Conditional random variable

speaker_1: What do you mean by visualize

speaker_2: Visualize means so

speaker_1: See again I have to go back to the previous lecture I have told you that but let me repeat see what is happening is that think of it like you know there are there are two random experiments that are being done one where the images are being taken okay the other where every image

speaker_2: Well go get it so its a joint

speaker_1: Yeah of course Im not talking about joint distribution There is a joint distribution Once you have a joint distribution you have a conditional distribution as well So we are saying that given that a particular outcome has occurred in one of the sample spaces in one of the trials what is the likelihood or like what is the probability that the other event happens right I mean the other trial takes these particular values That is what the conditional distribution talks about Yeah


Yeah yeah

speaker_4: Just uh uh I mean is there any particular reason why we take likelihood function to be a density function rather than the distribution function

speaker_1: Uh yeah I told you right it is easier to work with density functions Thats all Most of the time that is easier to work with density functions especially when you have continuous random variables it is easier to work with them Thats the only reason Everything that you do with density function can be done with distribution functions Okay Not vice versa not vice versa Everything that you can do with distribution functions cant be done with density functions because there can exist random variables for which the density functions do not even exist


But most of the in most of machine learning we assume that density functions are the you know well defined and they exist And then we work with density functions Typically in literature not typically right In almost everywhere in literature likelihood is defined as the density evaluating the density function at a point Yeah Because of ease of computation and analysis thats all Yeah You will see that more you know when we talk of the divergence matrix et cetera in a while you will see why


density function is easier to work with So also right there are lots of mathematical tools to deal with density functions You know when we talk of random variables we always talk of associate density function right So uniform random variable we give density functions distribution functions we dont remember do you remember the distribution function of uniform random variable no no and do you remember the distribution function of Gaussian random variable we dont but we remember the density functions


Thats the only reason But remember that when whenever we talk of likelihoods likelihoods are always density functions evaluated at a point Okay


Okay

speaker_4: So the dimension

speaker_1: Of course of course


X cap okay X cap is not in D right but


Its a sample from the same underlying distribution


Actually not

speaker_3: Uh so uh so I have a doubt so this is the conditional distribution of P of X given Y uh

speaker_1: Why do you want it Why do you want it Why do you want it

speaker_3: No sir I was just having a doubt if the other order is that of any importance like does that have any significance in the real world basically P of X

speaker_1: Its given a lot a lot of significance it has Okay that is called the class conditional density This is called the the conditional of labels given data That is the conditional of data given labels right


So it does have a significance I will see that We will see that So I am setting up the problem of supervised machine learning When we talk of unsupervised machine learning we will see that that has a significance


Any other questions


Card kick

speaker_3: Ah sorry Yeah I had a query I mean like here always we are talking about predicting one variable given the other So this label we should it be always

speaker_2: is something like discrete or can it be not necessarily

speaker_1: Not necessarily no not necessarily See if you have a y belonging to some y is another continuous random variable you can evaluate the density of that at a conditioned on another random variable as well In that case the problems name changes no then then it is called the regression problem thats all


The difference between the regression and classification is that that what sort of random variable your y is If your y is a discrete random variable then the problem is called the classification problem Then if y is a continuous random variable it is called the regression problem But the underlying task is the same The underlying task is still to evaluate the conditionals of y given x fixed at a particular point


Okay well write that maybe right If y is discrete


Its the classification problem


If y is continuous


The problem is called a regression problem


Okay now lets get back to what we were doing so now now given B


that


Its like this


Sampled from the underlying joint distribution Okay Now given this


This becomes


Okay good notes when I used to write put a box like that no that will become a nice box a rectangle here it doesnt okay


Okay so this is the central problem in this is this is what is called as supervised machine learning


Supervised machine learning are also called as the discriminative machine learning


discriminative modeling or machine learning whatever okay


Understand So now given data from the joint distribution I want to estimate the conditional


density function of y u and x


Is this okay


Be it classification be it regression this is the problem that we are solving


Questions on this


See note that we dont know the density function P of Y given X Okay we only have samples drawn from the joint distribution of X and Y So now given having samples from the joint distribution of X and Y how do you estimate the conditional distribution or conditional density function Its a question that is to be answered and that is the question that is answered in all of like discriminative machine learning Okay we will we will see that


a part of it now but this is the problem setting of uh


discriminatory machine learning now you can now see the connect right now uh oh this went


Is there a way I can put a box nicer box

speaker_3: there seem to be circular and spire icon at the top left third one


Im from

speaker_2: Left from left third

speaker_3: The third one right my mistake

speaker_1: Cheers


This is open


Okay now yeah so now how do you estimate the conditional distribution a conditional density function given data from an unknown distribution is a question Okay so maybe write this also with px


are known here okay


question that well answer but this is what the machine learning problem is all about okay discriminative machine learning is all about that so now this xis can be uh okay so let me write so xi


in some RD right and


yi can be discrete 1 to k or it can be another rk okay if its this then it is classification


If it is this then it is regulation


Entire supervised machine learning is this this thats all right how do you estimate this p of y given x given d


Now what about the so called generative models and unsupervised machine learning is that you have given I mean in my mind both of them are very very similar given D


It are of this form so you dont have the notion of y there


Okay So you estimate


PX thats all


There is one other part to the uh the generative problem maybe Ill try to p estimate px and


Sample from it


I have to define what sampling is shall I do it now or later because it is a little digression


Let me define it perhaps


before i define the problem of generative modeling right i would like to ask you this question any questions on this definition of supervised machine learning see i still have not answered this question of how do you estimate the underlying density function i mean that is what we are going to do with this entire course but problem setting i want you people to understand what the problem setting is uh yeah so is is the problem setting clear for discriminative modeling and machine


uh supervised machine learning please let me know if you have questions Kartik

speaker_2: So one query I I know we we dont know the distribution function P of x y but how do we know that its all been sampled from that distribution function itself

speaker_1: And thats an assumption that we make

speaker_2: Okay so they got some

speaker_1: You make an assumption that the data is coming from one given distribution Have you heard of something called IID


in independent and identically distributed data IID data


Have you heard of that thing going in

speaker_2: Have you heard of that yes yes yes in Ramakrishna

speaker_1: Yeah that actually means yeah in fact I deliberately left that because I didnt want to confuse you with things But yeah let me tell you this So this is actually sampled IID from this distribution is what is said This means that they are independently and identically distributed Identically distributed means that all of these are actually coming from the same distribution Independence means that all of these data points are independently sampled which means that


one image is independent to observing the other image the next image


okay so now we make an a basically we are making an assumption that the that the entire data is coming from one distribution that is why you know all these methods that have been uh developed using the iid assumptions fail if there is a distributional shift


Right Thats because you know theres suddenly the IID assumption gets broken which means that the data that you have given was coming from one distribution and you modeled it you did everything Now the test data comes from some other distribution What do you do


So that is an assumption that we make that the underlying distribution stays stays the same okay yeah Aditya

speaker_2: Uh so I wanted to ask what about outliers in that scenario like we assume that there are no outliers then

speaker_1: No Ive not defined what an outlier is right See how Even if its an outlier it can still come from the same underlying distribution with less probabilities right


Can come from the tail of the distribution but it is still coming from the same distribution is it Is it right


Okay if there are no questions any more questions on this So well move on Ill define what generative modeling is See generative modeling again is that you are given data that is sampled IED from an unknown underlying distribution This is also unknown


Now again you still want to estimate the likelihood or the density function thats also same One additional thing that comes in the generative modeling thing is you need to sample from it Okay So now what do you mean by sampling First let us


Ill put a box around it


This is the


Problem of generative modeling


This is generative modeling So given data from an unknown drawn from an unknown distribution estimate the distribution or the density corresponding density function and sample from it Now sampling is defined as follows The process of sampling is that


We need to implicitly


conduct


So run


The random trial


corresponding to the sample space


This is the process of sampling


Now you understand what what Im meaning So lets say that you are your sample space is tossing a coin right And you are given some hundred coin tosses Now what do you mean by sampling You have to implicitly toss the coin again


See in practice we will not have the coin and wear it all right So but what we can do is once why am I saying implicitly is because if you run the underlying random trial again what do you get is an outcome But now because we are working in the space of random variables we will get one point So this implies that


Sampling


Leads


point


The range space


of the random variable


You see why Do you all see why Because see what we are doing is sampling is conducting the random trial that gave rise to the sample space right So once you conduct the random trial you have an outcome And once you have an outcome you know the entire story right You have the random variable and because you have the random variable you get a point in the range space of the random variable because random variable operates on outcomes and gives you a point in RD Is this clear


Now generative modeling is all about this Okay I will take questions I will take questions Generative modeling is all about this that you are given some data okay that is drawn from an unknown distribution okay You should of course estimate the underlying distribution that is a part of the process Not only estimate the underlying distribution unlike in the discriminative learning case you should also learn to sample from it Now what do you mean by learning to sample from it Learning to sample from it is simply


you are conducting the underlying random trial right again and again so that every time you conduct a random trial you have the random variable that is there which will give you a point in the range space of the random variable thats all that is generating one that is generating sampling or generating modeling


Okay all this tag GPT right all the everything that youve seen us on it Claude et cetera are actually doing this Theyre actually running the underlying random trial multiple times whenever you do an inference


Okay Now somebody asked me a question just now right They said that okay what is the significance of X given Y Okay So that is actually that distribution If you learn to sample estimate P of X given Y and learn to sample from it you are actually learning to


sample from the conditional distribution sampling from conditional distribution is nothing but conditional generation or prompt based generation so given an input prompt right which is represented as another random variable y now p of x given y is the distribution that you are sampling from given a particular prompt okay y is fixed at something you need to learn to sample from p x so it is p of x given y is what you sample from in


general conditional generative models this is unconditional generative modeling where given data drawn from an unknown distribution you estimate the distribution and learn to sample from it sampling is the process of running the underlying random trial okay so that you get an outcome from the sample space and because you have a random variable thats already in place instead of observing the outcome what you observe is the element in the range space of the random variable practically speaking if you are given some images all the images are points in the range space of the random


variable if you learn a generative model on it if you get a generative model on it and learn to sample from it when you sample what you get is another image okay which is nothing but a point in the range space of the underlying random variable and you will have to sample see also observe that is a very important uh point here in the definition that I say that you have to run the random trial that is corresponding to the underlying sample


space youll see


See it is not doing see if you are given a lets say that you are given a given a coin tosses from a biased coin Okay Its not enough if you just learn to toss a coin You have to learn to toss a coin toss that particular coin which generated this random trial Isnt it Do you understand what Im saying


So the sampling has to has to respect the underlying sample space which means that it has to respect the underlying underlying probability measure which also means that it has to sample in accordance to the underlying distribution


Okay so let me complete it perhaps Sampling leads to a point in the range of the random variable respecting


respecting the underlying distribution


This means that if I have given you data from MNIST dataset the sampling has to generate data from MNIST dataset only no It should not start generating data from some other human faces or something It has to generate data from MNIST dataset What is the mathematical way of saying it That you run the random the corresponding random trial right That would respect the underlying sample space which means that the underlying probability measure is intact which means that the underlying distribution function is also intact


So now now you understand right now you understand why there is a connect between estimating px and sampling from it If you estimate px you cant estimate you cant sample from an unknown distribution unless you estimate the underlying distribution because you need to sample such that the underlying distribution is preserved Do you see that


Now the entire problem of generating modeling is that you are given data that are drawn from an unknown underlying distribution learn to run the underlying


I mean random trials okay such that the distribution function is respected and intact itself So if I say that you will have to sample such that the you have to sample from the underlying sample space it is understood no because you cant sample from the same sample space unless the measure that is there is is preserved but yeah I am just making it explicit to say that youll have to learn to run the random trial such that the underlying distribution is intact


which means that you better estimate the underlying distribution and then you learn to sample from it So this is the difference between the discriminative modeling and generative modeling In discriminative modeling what you do is you stop at estimating the conditional distributions of the labels given data given x right Here you estimate the distribution and also learn to sample from it


Okay questions


I didnt get it

speaker_2: Not understand fully because


Well you need to we need to know how to sample from it right so

speaker_3: We do this

speaker_2: coin example we already sampled the coins right maybe there are hundred coins and out of that we are choosing

speaker_1: No no no no no no hold on hold on hold on no okay in the coin toss example we have one coin we dont have hundred coins

speaker_2: Okay okay we have

speaker_1: We have tossed one coin 100 times That is your data

speaker_2: Okay got it got it

speaker_1: But you dont know what the what is the likelihood with which the coin turns out to be head or tail You get it

speaker_2: Mm Yes yes

speaker_1: Okay learning to sample from it is to learn to toss the coin again without having access to the coin

speaker_2: Okay okay

speaker_1: Right So we have yeah we dont have we have not sampled yet We only have samples that somebody has already given us That is our data


So without having access to the coin we need to know how the coin would have turned out if we toss you know 10000 more times that is sampling

speaker_2: So it basically means uh uh we have to sample more from near the peaks of the PDF function

speaker_1: Basically


No Im not saying peak you just have to sample it such that the underlying distribution function is intact you can sample from the tail also

speaker_2: Yeah occasionally Im a bit more I mean

speaker_1: You simply say that you sample such that the underlying distribution function is respected Thats all See if you are sampling from so called tail the measure associated with that outcome has to be lesser Thats all it means

speaker_2: Okay of course

speaker_1: You get it see now that you know this language you know try to use this more so basically Im saying that the underlying measure is respected

speaker_2: I think the main issue is

speaker_1: Now if the measure has to be respected then the underlying probability measure or if the distribution has to be respected then when you sample when you sample hundred times right like more number of times if there is a if there is a if there is an outcome that has more probability then that has to appear more compared to other right obviously

speaker_2: Yes yes

speaker_1: But the the underlying measure has to be perfectly intact otherwise then you are not running the current random trial no you are learning to to sample from some other random trial or some other sample space which is undesirable

speaker_2: Okay perfect

speaker_1: See that is what hallucination is all about right See what is hallucination that the underlying distribution is not estimated properly If it is not estimated properly it will start sampling from some some other sample space that that does not correspond to the given data

speaker_2: Okay but sir there is a no guarantee to uh I mean entirely we can reduce this hallucination right

speaker_1: That is what I am saying no that is why the entire course is designed that you need to that depends on how good is your estimate on PXS


Isnt it So now the sampling process has to estimate the underlying distribution If you have not estimated the underlying distribution correctly then you have you mean you will obviously when you sample you will get things from outside of the sample space no


So that is why you have so many techniques you have that model this model every model is trying to do the same thing that every every generative model right you know be GPT autoregressive and GPT etc are come from this family of models called autoregressive models right and you know there is this adversarial networks and diffusion models and flow based models score based models all of these all of these are trying to solve this exact same problem that they are trying to estimate the underlying distribution and trying to


from it Why are there so many models is because each of them estimate the underlying distribution in a different way Since they dont estimate the distributions quote unquote perfectly you have so many models Same thing goes for the uh discriminative models also Why do you have linear regression logistic regression and SVMs and kernel machines and neural networks All of them are actually trying to solve this exact same problem which is estimating the underlying conditional distribution But one model is better than the


Other because you know different they estimate the underlying distribution in a different way


Now you might have heard this term no All models are wrong some are useful


Right So everything is a model Everything is trying to estimate some distribution given some data They are all models All of them are wrong Some of them are useful That is why you have metrics to estimate how good the performance of a given model is Okay So now I have to define what is a model Right See see I mean observe that we are solving an estimation problem We are trying to estimate a density function So every estimator is a model


that we are we are looking at generative models discriminative models What is a model Model is nothing but an estimator for the underlying density function that we want to estimate There can be thousands of estimators Each estimator comes with its own property Right Claude has its property Sonnet has its property Like gamma has its property This thing you know GPT has its property and so on Everything is a model But all of them are trying to do this exact same thing that given data from an unknown distribution trying to estimate the underlying distribution


and learn trying learning to sample from it


Yeah

speaker_4: Yes sir just to clarify my understanding on this prompt based generation so you mentioned that that problem is basically to sample from P of X given Y is that correct

speaker_1: It is it is it is it is estimating the conditional distribution of X given Y and learning to sample from it See we will see this in great detail In fact you know we will look at multiple estimators in this course Okay Yeah So this is Im just setting up the problem now Okay


Yeah

speaker_2: Uh hi sir so here just a second

speaker_1: Just a second uh just just a second Uh like Im Im Im Im both you know happy and a little disappointed Im happy that uh like you know more people are talking Im slightly disappointed that the same set of people are kind of asking questions I mean it is Im not discouraging you people but I want to encourage the entire class to participate Okay So feel free to ask questions Otherwise uh yeah I mean I dont want to go into the


philosophy of pedagogy but yeah I encourage all of you to ask questions dont hesitate do ask questions okay ask it go on

speaker_2: Yeah so as we discussed that we are estimating the distribution but we are estimating the distribution via the density function associated to it right

speaker_3: the density function

speaker_1: Yes yes

speaker_2: So earlier we discussed that the density function cant be like a proper like exactly 100 percent representation of the distribution function

speaker_3: Okay so what that would mean

speaker_1: No no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no

speaker_2: Okay so if we get a value of a density function at a particular point

speaker_1: Then we know everything about the distribution function because if you have the density function right you can integrate that and get the distribution function

speaker_2: Okay okay okay

speaker_1: See but somebody asked me that question no why do we work with density functions and not with distribution functions is because

speaker_3: Mm

speaker_1: Computationally easy thats all

speaker_2: By the way

speaker_1: Otherwise otherwise I can actually say this now the problem is


I can set the problem as estimating the disi underlying distribution function

speaker_2: Okay

speaker_1: But I set it up as density function because when I what happened


I set it up as density function because when I uh when I


Answer this question of estimators No I will use density functions for everything that is why

speaker_2: Mm hmm okay

speaker_1: uh yeah so but uh there is a one to one correspondence between density function and distribution function just that evaluating the density function at a point will not give you a probability thats all yeah

speaker_2: Mm hmm okay okay understand

speaker_4: Oh so just to continue the discussion so here we said that we will get the likelihood right and the likelihood may be low uh but still the probability may be high that is possible right

speaker_1: No no no no no right No see again see when you when you evaluate the density function at a point you get a likelihood So for continuous random variables there is nothing called probability at a point that itself is not defined


because probabilities are evaluating the distribution function Now if you evaluate the density function at a point right you get zero Which means that I mean so rather if you integrate the density function right at a particular point you get zero So the probability of obtaining a particular image is zero actually

speaker_4: Yes thats correct but what is the likelihood

speaker_1: What did you work on lately Huh

speaker_4: Yeah but what we are interested in is the probability right that I mean when the probability is high we want to take that particular label as yes

speaker_1: just say say no no for for you mean the discriminatory part youre saying is it not yes

speaker_4: Yes yes yes the what does that mean

speaker_1: Yeah see if y happens to be a discrete random variable then density functions are probabilities


Because they are mass functions

speaker_4: Oh but if it is a regression problem then

speaker_1: If its a regression problem then you should just say that its likelihood I want a point with higher likelihood dont call it probabilities thats all you see

speaker_4: Yeah but thats my point so higher likelihood may not mean the higher probability right

speaker_1: Probability of a point itself is not well defined it is not even defined so you take decision based on likelihood is all I am saying stop there

speaker_4: Stop this

speaker_1: See dont jump to the probabilities because probabilities of continuous random evaluating the density function at a point or likelihood of a point is not the probability of that point


Yeah so just just say that I want to pick a point with higher likelihood Thats all That is perfectly fine Dont say that you know higher likelihood corresponds to higher probability That is incorrect

speaker_4: Okay

speaker_1: Yeah I mean Im just making it you know pedantically correct There are nitty gritty is but that is what it is Yeah

speaker_4: Yeah thank you so much

speaker_1: See now you should see the connect between estimating the density function and sampling from it right I mean if you cant estimate the density function you cant sample from it because you have to sample in accordance with the underlying density function that will happen only if you know what the density function is right Yeah Okay Um Avirup

speaker_4: modeling very in discriminative modeling

speaker_3: So can do we have a corresponding definition for unsupervised learning also Im just asking for clarity yeah

speaker_1: Yes yes So you can also call generative modeling as unsupervised machine learning


Yeah so uh there is a um


For now let us let us call in in in unsupervised machine not all unsupervised machine learning models enable sampling Now for instance if you do k means clustering right it will not enable sampling strictly speaking But if you do if you if you if you do GMM clustering it does enable generative modeling OK and also you know k means happens to be a special case of GMM


You for now let us call this as unsupervised machine learning but when we come to this thing called latent variable models right which is a special case of special way of modeling the underlying density function then that also is called unsupervised machine learning OK But yeah so for now you can assume that that unsupervised modeling lets say that


Unsupervised models are sort of a subset of canned in modeling Okay for now


Maybe I will not write it but simply consume it yeah


Was this social No this was a virup I suppose

speaker_3: Yes thank you sir

speaker_1: Uh so we still have a question I think socially you have a question


Okay so maybe hes not there okay so let us move on shall we move on any other question


Okay so let us now answer ask this uh


Yamanish go on


also like for suppose text base we try to predict the next word right so while training we fed uh fed that next word what will be the next word try to predict that so its its a kind of uh supervised on you know in that case


Yeah it is not because your I mean the word is I mean the word is modeled as X here Okay In that case you are looking at autoregressive models Your words are also the random variable X So now you are actually sampling from the underlying distribution


That is why I define prediction in this case particularly as evaluating the the likelihood at a point


no supervision per se there see that is why no i dont want to use this terminology of supervised and unsupervised learning precisely because of this you know there the line is very very blurred uh you simply say that in both the cases you are estimating the uh estimating some distribution okay given some data that is all


Okay but typically in supervised models or discriminative models you will not have an explicit sampling process but in generative model you will have explicit generative sampling process Thats all Okay so maybe let us call this as discriminative machine learning if you are


comfortable with this


Okay discriminative modeling and generative modeling Discriminative modeling does not have sampling generative modeling has sampling So lets have that as the difference Yeah so shell progress


Now the important question is

speaker_2: Answer one question

speaker_1: Yeah cool

speaker_2: What if like in both the cases we get the density function d y given like in one like for a the discriminative model we get the dist


density function so why cant we get the distribution function from that

speaker_1: We can Im not saying we cant we can but I mean most of the applications right it is enough if you have the density function


We can get the discriminant uh we can get the distribution function from it

speaker_2: Okay and then like if we want to sample it from like do sampling from that like for an example we have a set of images of 10 classes basically 10 different animals and we get the underlying probability distribution And then we sample and say okay we want to generate an like image of an animal in a different scenario Lets say we had the sample of animals in jungle


But we want that to want the model to generate the images for those animals in a city context So wont that be considered as generative model

speaker_1: That is a generative model but the is changed no See that is all I mean that is definitely generative model but then see if you only have images of animals that are from like jungle in your data then there is no way that your model is generating images of animals in cities

speaker_2: No no no sir my my point was so in in the discriminative model we have the uh like basically the k classes from which the data belongs the data can be classified into now using this available data we develop uh like we get the distribution and we develop a model to uh you know generate some fresh data fresh fresh data out of it

speaker_1: No no no my


when we say that see that is what im saying let me i dont know maybe i didnt convey the point properly see when i say that you need to sample from the corresponding underlying distribution it means that you have to sample from you have to get a quote unquote fresh sample only you know sampling is always fresh sampling


Suppose you are given 100 images of these animals let them belong to 10 different categories When you generate you have to generate it from those 10 different categories only You cant generate from an unseen category is what I am trying to say

speaker_2: Yes sir agreed

speaker_1: You cant generate it by construction because you have only estimated the underlying distribution

speaker_2: Correct correct correct

speaker_1: Thats all When your model is as good as your data unless your model has seen that see it will it can generate the images from I mean which are not there in your data set

speaker_2: Big

speaker_1: You understand but it cant generate data from the distribution that does not correspond to your to your data set

speaker_2: Button center

speaker_1: You understand that See for example if you have lets say the images of like you know human beings as your data when you construct a generative model and sample from it it will generate


the face of a non existent human being Okay But it cant generate the face of a monkey or a dog or a cat

speaker_2: Correct sir agree agree

speaker_1: Next up next one

speaker_2: That is one of them

speaker_1: That is what is meant by uh uh respecting the underlying distribution

speaker_2: got it sir so like my point of making this statement here was whether we have the classification uh or not it it it wont make a difference right

speaker_1: It it should not but as I said there is this thing called conditional generation that Im not talked of right where you where you some learn to sample from P of Y given X sorry P of X given Y now suppose you have 10 categories and you know you want to lets say that you have cat images dog images whatever images and you have you have learned to the question is what is the underlying distribution that you are modeling if you are modeling remember that when I said that there is a conditional distribution it means that you are modeling


y equal to a particular value right Now lets say that y equal to 1 corresponds to cats If you are modeling this distribution learning to sample from it you are only learning to sample from the cat images

speaker_2: Yes

speaker_1: You understand However if I just take this and multiply this with P by and just take a sum of all this what am I doing This is equal to P X isnt it Yes sir Now if I combine all the images from different categories and learn to estimate this distribution P X then Im sampling from all possible animal faces Thats all So it depends on what the what distribution are you modeling You get it

speaker_2: Yes sir

speaker_1: that those categories or those labels are are are random or I mean I should not be using this word random they are they are synthetic or they are pseudo in the sense that


See if you can you can group all the cat images into one and call that as one distribution and estimate it so that you when you sample you only get cat images


If you take say images from 10 categories combine them all and call them Px and if you if you mod estimate that then you get images from all categories thats all


So that categorization is a sort of you know its a its a synthetic thing right depends on like what are you calling as general end distribution and data thats all right

speaker_2: Okay sir

speaker_1: Okay uh yeah Manisha

speaker_3: So as an extension to this discussion and we have answered that but so basically what we are saying is we are finding the as I mean as a part one of the problem its finding the distribution the underlying distribution which will tell us which class is linked to which label in a way

speaker_1: No no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no no

speaker_3: No no no no no

speaker_1: See estimating the underlying distribution simply tells you that what is the likelihood of this particular image under the given distribution thats all


So there is no idea of class here at all in generative modeling

speaker_2: But we still I mean the first step is to find the underlying distribution

speaker_1: Right

speaker_2: all you know are the like for the exa for example what was being discussed for all the animals you know we are kind of cate its kind of

speaker_1: no no no its a its a its its a strict no i tell you so you have to understand what is meant by estimating the distribution in the generative modeling case and we will see examples and we will actually go deep into it but anyway at this step you need to understand it see if you are given lets say 100 images of animals okay estimating the underlying distribution means that you are trying to find out how likely or what is the likelihood of a particular


image under the distribution thats all how likely is that Im obtaining this image suppose Im conducting that random trial how likely it is to obtain this particular image is what Im finding by estimating the distribution it has nothing to do with classes here there is not even an idea of classes because there is no y here


The way I have set up the problem there is no why here at all

speaker_3: Okay get that Okay so its just the likelihood of getting

speaker_2: a particular point in that distribution

speaker_1: Thats all thats all so if you have thousand images Im just calculating what is the likelihood of obtaining this particular image thats all


See if you if you if you imagine obtaining an image as a roll of a die


So Im what Im asking is when I conduct that random experiment okay what is the what is the likelihood that Im obtaining this particular image That is what estimating PX is all about


So what is the likelihood that I get this particular face Thats all I mean face of the die I mean if you take the die example there is no notion of labels in this setting

speaker_2: And then the sampling part that we are talking about is basically from

speaker_1: is that you are obtaining a new non existent human face thats all


You are actually obtaining an image that is sampling

speaker_4: Getting that yeah I think I get the notion of that yeah right

speaker_1: There are two things here One see once you estimate the underlying distribution you can plug in any of the data points that are within your D or outside of your D as long as it is coming from PX and estimate the likelihood of that particular point using this PX

speaker_4: Absolutely yeah

speaker_1: Sampling is that you are obtaining or you are running the random underlying random trial so that you get a point a fresh or a new point that is not a part of your D but still comes from the underlying sample space that is sampling

speaker_4: Get that sir yeah

speaker_1: So there is no notion of labels here at all

speaker_4: Got it got it right sir

speaker_1: Right So now I still have not defined this conditional this conditional sampling Right I mean sampling from P of X given Y See as I said yeah see as I said this has a notion of you know prompting

speaker_4: Kiss

speaker_1: Exactly So that I have not brought that notion yet I mean see now in the because that is simply confused stuff you know once you like like assimilate this idea of generating modeling and sampling no putting a conditioning here and saying that Im modeling the conditional distribution is not difficult

speaker_2: Right so that that was my point also so that is that doesnt seem difficult but now I think I get the actual problem there yep

speaker_1: See yeah so it is not estimating y given x You want us to understand that The problem with generative modeling is not estimating y given x So that is the problem of discriminative modeling that you are estimating p of y given x

speaker_2: Im not

speaker_1: And there is no sampling here


Okay but in generative modeling the the two things one there is no notion of labels here


and two you need to learn to sample from it I mean thats a huge thing because see suppose you have you are given MNIST dataset and you create a CNN to predict the classes right that will not give you samples from MNIST dataset does it


But that is simply estimating p of y given x


Right But if you build a GAN or a diffusion model on MNIST dataset it will give you new samples from the MNIST dataset that are unseen because you are not only estimating the underlying distribution but you are also learning to sample from it That is generating model


What is common in both the cases is that there is some distribution that has I mean there is some sample space and some random trial that has happened and you have generated the data already And that is the input to both the I mean all of machine learning that you have some data given from an unknown distribution Now what do you do when it is the question Having that data if you estimate I mean if your data is of this sort if you rather model your data coming from a pair of random variables having the joint


distribution and you interpret one random variable as data or rather the features and the other random variable as labels then if the problem is set up as estimating the conditional of the label random variable conditioned on the feature random variable that is discriminative modeling without bothering about sampling but now okay Ill make things a little involved because you asked this question please see if you can understand this see I can actually construct a generative modeling


Having the data


that that is given in discriminative modeling as well Do you see


What I am trying to say is suppose I have that data set of animals with the corresponding classes also given


Now if I estimate P of X Y the joint distribution P of X Y and learn to sample from P of X given Y then that is another generative modeling that is conditional generation

speaker_3: get it so thats uh the joint uh uh distribution here and yeah we also get it from a single uh you know distribution of a random variable

speaker_1: distribution of a single data variable It depends on how do you want to view your data See if you are given thousand animal images now do you want to categorize them into subcategories and say that hey look my data is such that I have the image and the corresponding label with it or do you want to see that as simply thousand images without having labels

speaker_3: Yes and then draw sample uh

speaker_1: Thats all see yeah thats all its a modeling choice you know what are you drawing samples from are you drawing samples from px or are you drawing samples from px given y


Right Now if you are drawing samples from P of X given Y it simply means that given these animal images and the fact that you know I want to generate from dog images or rather I want to generate the image of a dog then I know how to do it But now if I give if I I mean that needs the corresponding labels as well


Right because you are you have you want to estimate P of X given Y But I mean estimating P of X given Y and learning to sample from it also is a generative model right So suppose you estimate P of X given Y and sample from X given Y thats also generative modeling That is actually conditional generation which is which is what ChatGPT does So given Y which is a particular prompt you want to generate

speaker_3: Im like

speaker_1: And for that the kind of data that you need is pairs of x y Do you see that Because you need the underlying joint distribution

speaker_4: Absolutely yeah yeah

speaker_1: So depends on like what sort of data you have and what sort of density are you modeling and sampling from Thats all


But the major difference between these two models is that in discriminative modeling see in both of the cases you have data drawn from an unknown distribution you are estimating some distribution But what is not there in discriminative modeling is that you dont learn to sample But in generative modeling you learn to sample from it Thats the only difference


I hope that you know this notion is clear because you know I mean this this is what differentiates lets say a ResNet based CNN or VGGNet from a diffusion model or a GAN Both of them are actually estimating the underlying distribution given data Both of them are given same kind of data What is different is that the generative models learn to sample from the underlying distribution Discriminative models dont learn to sample Thats the difference


Okay great Any other question on this I mean this is important because this is I mean you you if you understand what the actual problem is you know then rest of the math and algebra becomes easier Any other questions So now you see that right I mean now one of the central problems in both uh in discriminative and generative learning modeling is that given data from an unknown distribution how do you estimate the underlying density function is the question right


This is an important question right Given data drawn from an unknown distribution how to estimate the underlying density function is the question that has to be answered Okay For that there are multiple techniques One technique that we will be seeing I mean that is common across multiple models that we will see in this course is what is called as divergence minimization


all these models right GANs VAEs diffusion models autoregressive models etc all of them employ this technique called divergence minimization to answer the MBO question and by the way every generative model that you can think of right that the people are coming up with are actually solving this problem that given D you estimate the underlying density and sample from it


Right Minor modifications here and there I mean depends on what sort of D that people have If you have like like text and the corresponding next word or label or something image and label you learn to sample estimate the conditional distribution and sample from it That does not matter because thats simply a model like a design choice But they are all solving this particular problem Now to solve this problem you need to estimate the underlying density Right Otherwise how do you learn to sample according to that particular


density So you have to estimate the underlying density So all of the generative models in fact even discriminative models have to solve this problem of divergence minimization or rather given data drawn from an unknown distribution how to estimate the underlying density function is a problem that all ML models have to solve And one technique to do that is what is called as divergence minimization that is employed by all the existing generative models


So we will see that next you know how to and what is this divergence minimization and how to use that to solve this problem is something that we will see next Shall we take a break now


I think its 90 minutes lets take a break for 15 minutes now


Okay so in my clock it is 11 am Let us reconvene by 11 point 15 ish Okay Yeah see you in 15 minutes


The resume

speaker_2: Yes sir

speaker_1: See Kendan has just put a poll for tutorial timings so please respond to that It is I think both on WhatsApp and Teams WhatsApp I definitely saw it now I dont know if its on Teams Is it on Teams already or

speaker_3: Thats exactly what Im saying

speaker_1: Okay please respond depending upon your response whatever works for most of us most of you will take that time okay


Okay uh let us continue


See one small request is that from now on the content will become a little dense and intense So please spend some time after the class in sort of just looking at what is happening so that the storyline is not lost Okay So please do that before coming to every class And also you can look at my reference look at my notes that I have given to you that also has some references


Okay so now what is the the question that we are looking at that we are given data drawn from an unknown distribution and we want to estimate the underlying density function that is the question that we are looking at How do we do that One of the methods to do it is via this thing called divergence minimization So what is the idea there Okay the idea is the basic idea is the following that first


assume


A parametric form


Unknown dead city


the density function that is to be estimated okay


for the density function


It will be a steel on a trip


Okay so I mean this Ill give you step by step So this is the first step Now what does this mean This means that so now you are given some data d right You assume that the density function that I have to estimate


can be represented using a neural network with some parameters


understand okay so typically denoted by


denoted with p theta okay


Theta are the set of parameters


Do you understand what this means So an example can be multiple examples Assume your p theta lets say that I assume it to be a Gaussian density and note that this density function is still on the same sample space or the random variable as the underlying data right I mean obviously it has to be defined on that only So this can be lets say a Gaussian distribution okay with some mean okay mu and some variance


Now theta in this case happens to be the mean vector


and the variance matrix


understand Now what we do is we assume a parametric form for the density function that is to be estimated ok denoted by p theta You you can assume that to be anything You assume it to be a Gaussian density assume it to be exponential density and those parameters happens to be that This is one example The other example can be that I


assume it to be a neural network right so p theta of x right is this is output of some


some neural network right where


G theta


is a neural network


a neural network and this z is simply some some gaussian distribution so basically the way im modeling this is there is a sample of the gaussian distribution that is going through a neural network g theta well go to the details of all this but these are examples so z is going as output and what is what am i getting at the output are actually p theta of x


I can model it I mean this is again a design choice I mean this is where different models are different This d theta can be a transformer right It can be a CNN or RNN or whatever depending upon what your choice is But basically the idea is that you assume parametric form for the underlying density function that is to be estimated Do not expect p theta Is this clear Like what do I mean by parametric assumption


So this is the first thing that you do So once you make that assumption what is the second step The second step is that


Define and compute


compute okay a distance or a divergence metric


divergence metric between okay the true density function


Exactly true


density function


Which is PX right and


as parameter


parameter function p theta okay so basically d okay that will take the true density and the parameter density this is the notation okay px double slash p theta so this measures


So this is the divergence metric that would compare the true density function to the parametric density function You might ask me here right I mean we dont know the true density function How do we compute this Hold on to that question that that actually turns out to be the central question of all generative models When you dont have the true density function how do you estimate the distance metric is a question that well answer later However what we need to do is we need to define and compute some sort of a divergence or a distance


metric between density pair of density functions in this case the density functions happens to be the true density and the parametric density that we have assumed okay okay once we do that what do we do so


Theyre just


compute


the parameters


of pre theta


Such that


D of px slash p theta is minimized


procedure right this is the this is what is called as training agent say training a model or learning a model and so on this is the learning part of it understand mathematically speaking what you do is you set the parameters theta star okay as the ones that would minimize what do you mean by argument the set of parameters that would minimize a function okay now that would minimize the distance metric that you have defined between


density functions We have two density functions This entire thing now will become a function of theta because p theta is a function of theta and you want to solve for this of theta such that this distance between track is minimized


Now the final estimate


This is the learning problem this is the training of learning of generative model right training


So training basically is solving an optimization problem You all know that right That is why we use gradient descent and backpropagation algorithm to train Okay Basically you are solving an optimization problem The final estimate for px right is simply p theta star obtained by solving the following


You need to get us stuff


Obpained


is solving


the EMO optimization problem


Optimization as you know in this case that is the minimization problem


This is the general recipe right of how to solve any machine learning problem It can be generated discriminative or generative modeling What are we doing We are simply we are given data from a known distribution We assume a parametric form for the density function to be estimated typically denoted with parameters theta See that is why now you can I think relate Now in the discriminative case the underlying density function that we need to estimate is p of y given x isnt it We either model this as a logistic


Or we model the sub


is our model p theta what is the model this is for the underlying density to be estimated right


This actually P theta


what is called as a model


be it in a generative model or a discriminative model the parametric assumption that we are making on the underlying density function is what is called as a model It can be a neural network it can be anything any kind of parametric function Then the problem of estimating the underlying distribution translates to estimating the parameters of the underlying model that we are assuming That is also a density function Now how do you estimate the parameters


of this density function is the question For that we need to first measure Lets say that we fix one value for this mu and sigma Lets say that our model is a Gaussian model okay And the only parameters that we need to estimate are mu and sigma We initialize that with some value Now you get one p theta with that What we should do is we should compare that p theta with the actual density Now for that we need a way to compare density functions If you take pairs of density functions


need a way to compare the density functions right now you compare that and you see if its large if the if the distance between the true density and the density function with a particular set of parameters is large then you change your parameters in such a way that that distance become lesser right so for that you need to first compute a or rather compute a distance or a divergence metric between the true density and the assumed parametric density or the model okay and then i


or compute the parameters of the model such that this divergence or the distance metric between the pairs of density is minimized that is what the training is mathematically speaking you are solving this optimization problem that you find your theta such that this distance metric between this distance metric itself becomes a function of theta right now you need to find this theta such that the distance between the px and that particular p theta is minimized so we should solve this problem


which is which is training the model the final estimate for px will be that p theta star is the set of parameters that you have gotten from solving this optimization problem that would minimize the distance metric between the true density and the model density


Is this clear Now again the open questions are I have not told you two things I have not told you how to compute the systems budget when you dont have PX We still dont have PX right That is our whole problem We will I have not told you that I will tell you that The second thing that I have not told you is how to solve this optimization problem and what sort of model choices that we need to make That will be the subject matter of this course entire course We will take different see for Gans makes for instance you know adversarial


networks make some assumption on p theta v as made some other assumption on p theta diffusion models make some other assumption on p theta they would change this underlying distance metric they would change the way the optimization is being done that is what the the you know the levers with which we can play what sort of distance metric can we use what sort of optimization can we do what sort of model choices we can do are the questions answering in different models but this recipe would is going to stay that


You make an assumption on the unknown density function define a presence matrix between two density and fix the parameters of the density such that the distance between the density and is minimized


That is all the recipes for making the density I am not still telling you how to sample I will tell you how different models sample in different ways We will talk about it later But this is how you estimate the unknown underlying density and this is the recipe This is called the divergence minimization right Because you are assuming a model minimizing the divergence This D is called the divergence and minimizing the divergence between the pair of densities


Okay any questions about uh

speaker_2: Sir I wanted to understand uh what is this g of theta when like when you have written g of theta g theta

speaker_1: Its a neural network no I told you no its a neural network simply a neural network

speaker_2: Okay and Z Z

speaker_1: There is some random variable some some arbitrary random variable that will go as an input to this neural network and whatever output this neural network is giving I model it as which you know


Whatever output that neural network is giving no I take that as P theta of x

speaker_2: Okay okay

speaker_1: There is one way to modernize that I said no as I said there are multiple uh models that one can think of but this is one of the uh models that you can that you can design

speaker_2: Okay see

speaker_1: Is that okay


Yeah so many questions Kartik

speaker_3: Yes sir uh I have a little um

speaker_2: I didnt understand it fully about the parametric form that we were referring can we get it based on another example maybe a little more simpler one


Uh why why do we think this will happen

speaker_1: is that simply a number right yeah yeah you assume if you assume that its a gaussian distribution thats a parametric form okay that how do you how do you differentiate one gaussian distribution from the other


is through the parameters no mean and variance thats all so you are assuming that ah you are assuming that its a Gaussian density but you dont know what the mean and sigma are correct now how good is my assumption is a different question it can be a totally crappy assumption that you have made but that is that is I mean thats why I said all models are wrong no you have made some model assumption

speaker_2: Youre thinking

speaker_1: Now these are simplistic models but in places like you know GANs and GPTs etc these models are made express enough they are made huge neural networks so that they can express a large family of functions


Basically youre expressing the density function Now you choose a parametric model such that it is expressive enough so that it can express a large family of functions And transformers and neural networks are such functions So now what differentiates one transformer from the other transformer is the weights that they have


Now that is that relates hold on that relates suppose you have like you know two transformers okay of the same architecture but you have two underlying distributions you want to estimate right using the same architecture you can fix the weights of these two transformers in it in different ways so that uh you know they represent two different distributions thats all that


In most of this course right our parametric models are zero networks only because they are expressive enough


Since neural networks are I mean we will see that neural networks are said to be universal function approximators That means that you can use a neural network to approximate any function Thats a known result Okay That is why you know entire machine learning has moved towards neural networks because they are very good parametric models that you can have a neural network and set its parameter to represent any function Same thing goes for discriminative model also right Why did people move away from C Initially people thought that okay this can be modeled using the same


logistic regressor it was not expressive enough what if the final density function that you that you need okay for the given data that happens to be something that a logistic regressor cannot model then you need to go to more models that are more flexible thats why you know the todays data of the art is that p of p of y given x these the parameter family that you assume on the underlying density are neural networks or transformers or anything those models are


expressive enough that means that see no matter what you do a Gaussian density can only represent this density you know I mean it can represent this this this and all that but it is a unimodal density with different you only have two degrees of freedom to play with


What is your under


has something like this a Gaussian density can never


No matter what mean and variance you play with that is why you choose this

speaker_2: Im not saying it should be done

speaker_1: GML can express this of course but right I mean you need more complex models to represent this And thats why people use neural networks Okay So thats what is meant by parametric model that you just assume that my my my my real density is one member of this family large family that my parameter parametric model can express So basically if I model that as a neural network or a transformer Im saying that my true density can be


represented by one set of weights of this neural network there exists one set of weights of this neural network that would represent my underlying density and Im interested in finding that one set of weights


Now how do I find that one set of weight is simply I fix a particular weight and I compute I see how far my density that I have gotten from this particular weight is from my true density And then I adjust my weight such that you know that measure becomes lesser and lesser That is training no

speaker_2: So yeah a query here is when the when then we like try to optimize the minimize that particular variable that I understood so if it is not

speaker_1: Divergence not variables call it call it divergence

speaker_3: divergence so if Im minimizing that divergence say it is not minimizing up to my mark will we need to go back and change the model again I mean like is it what the new trend is a good question

speaker_1: Thats a good question Of course of course you need to change And that is why you know you have like you know ResNet 30 ResNet 50 ResNet 100 Why did people make it deeper and different kinds of architectures Is because my divergence is not getting minimized


How do I know my divergence is not getting minimized Is it through some metrics evaluation metrics like you know whatever the accuracy precision et cetera They are all surrogates to measure how bad is your divergence right If its bad then go back and change your model Thats all It means that okay maybe the model assumption the parametric model assumption that you have made is not good enough If you are using neural networks as your parametric families the architecture is not good enough Change the architecture make it deeper have more neurons


have more hidden layers etc

speaker_3: So just to add on that point just to maybe a little bit philosophical question I mean like what if it doesnt like we cant model it using a parametric model at all Maybe its pure chaos kind of where we cant find a one which satisfies our divergence values

speaker_1: And we are doomed


But it seems like all these transformers and billion parameter models are able to estimate general line divergence to a good level Thats why you have the boom of AI right I mean they are working which means that the divergence is minimizing

speaker_3: Okay yeah but I was thinking as you said initial class maybe change the math just

speaker_1: again no no but i mean if the nature the mod see this we all this probabilistic uh way of thinking has taken us this far you see weve actually reached pretty far we have very very strong models these days models that can crack international mathematics olympiad and get a silver medal thats a very very strong model no


In model that can crack JE I mean we have such models good things are happening right


Thats how the people did research right I mean what was all this research all about is that changing the speed theta looking at different forms changing divergence metrics different divergence metrics and changing the way this optimization problem is solved Thats only the three things that you can do though Either you can change the model assumption or you change the divergence or you change the way you optimize That is all people have been doing so far

speaker_2: Oh so yeah I was thinking

speaker_3: whether we like the more uh the parametric form itself we can define a new one kind of I mean like based on the inputs

speaker_1: People have done that no I mean like from MLPs from logistic regressors they went to MLPs from MLPs they went to CNNs and then RNNs and transformers whatnot and all these kinds of different model assumptions right


But the recipe itself has to be changed I mean this is by the way this is also called divergence minimization or empirical risk minimization People have tried to look at other ways of doing stuff as well But the thing that has worked the most and one which is there in practice today is this


Thanks Yeah Low gauge


Low key Kumar cant hear you


Yes I can hear you now

speaker_2: Uh will we be always be able to come up with a divergence metric

speaker_1: that we define no yeah see if your question is will we always be able to evaluate the divergence metric the answer is no thats why you need a lot of trick all this GAN etc are actually kinds of tricks to evaluate this divergence metric will we be able to define a divergence metric of course I will just right now I will define a few metrics

speaker_3: I mean Im waiting

speaker_1: Evaluation No not necessary No we cant know because there is one apparent problem with this The apparent problem is that this divergence metric seems to ask for a px We dont have px Thats our whole problem

speaker_3: Oh

speaker_1: Right Now how do we evaluate these reversion metrics when you dont have PX is the question that we are going to answer in this course There are different tricks to do that Many people generally compute a bound on this You cant find this exactly So you compute an approximation to this which is computing a bound That is what this evidence lower bound and all this expectation maximization VAE etc do We will see all that in detail You can always define it but can you compute it always


Perhaps not depending upon what divergence method you are looking at


Thats the I mean see in this in the rest of this course we will only do this we will pick up e theta we will pick up d and we will see how to solve that optimization problem thats all thats all well do in this course next


Uh okay yeah

speaker_4: Yes uh the first question is um uh the choice of the original distribution right is also a model parameter

speaker_1: So but in this case

speaker_4: So for instance in this case choice of the distribution the original distribution that you try to fit so so here you try to fit the normal distribution

speaker_1: No no no please See one again a kind request is please dont try to use the terms that I have not defined I have never told what do you mean by fitting


So I have defined learning training models etc Please try to use my terms anyway So that that apart see there is we are not making an assumption on P x We are only saying that my P x I mean we are making an assumption on parametric form We are just saying there exists a P theta a family of P theta of which my P x is a member


You get it When I make an assumption lets say that P theta is a normal distribution Im saying that my Px is also a normal distribution with certain mean and variance That is the assumption that we are making Understand So you see its a method of

speaker_4: That is something that we need to choose appropriate right

speaker_1: to choose other than right let me compete

speaker_4: There is a lot of noise

speaker_1: Yeah somebody are muted


Okay so let me complete Im saying suppose you may assume P theta to be a neural network What Im trying to say is that there exists a set of weights for this neural network which corresponds to my underlying PFs


Now what is your question

speaker_4: No but again here we have chosen normal right And then the parameters are only mu and sigma right But I could have chosen a different distribution also

speaker_1: I told you right I mean that is your model choice You choose anything that you want You are going to choose

speaker_4: Yeah but yeah in general do we uh say that I mean the normal fits I mean or the normal is a better candidate

speaker_1: We cant care at all definitely not

speaker_4: It kind of was good I thought

speaker_1: Because you know if you take M nest and if you want to model it by normal distribution you are doomed There is absolutely no way that there exists a mu and sigma that would make I mean that that that will give you the distribution of M nest data

speaker_4: So that is something that we need to decide based on the data

speaker_1: I mean today people are like you have to have a family P theta that is expressive enough that would express a large class of density functions No normal density does not express a large class of density functions at all

speaker_4: Okay

speaker_1: Isnt it Because it cant even express a binom I mean like bimodal distribution It can only express monom uni modal distributions and most data will be by multimodal distribution right

speaker_4: Okay and in case of neural network can we just go a little down


So so basically at the end you get a distribution but uh what youve shown here as the input is is the z the the normal standard

speaker_1: Yeah so what does that mean So you have a neural network that will take a normal distribution as an input and gives you a distribution as output

speaker_4: So so what does that mean

speaker_1: modeling it that way no i can choose see p theta is our p is in our hand we can choose our p theta to be anything


we we can choose it to be anything now if i choose it to be a neural network then there are large sets of the distributions that my neural network can express

speaker_4: Okay so so its its kind of showing that you are transforming the normal distribution to a some complex distribution using neural network

speaker_1: Oh yeah theres neural network okay yes

speaker_4: Yeah okay understood

speaker_1: See even in the discriminative models you do the same thing no you have to estimate P of Y given X so you take a neural network


you take a neural network right that would take x as an input and gives you p of y given x this is exactly what a resident etc does know


Now you can either make this p of y given x 1 by 1 plus e power minus x e power w transpose x or something in which case it becomes a logistic regressor That is your p theta right The choice that you make on the model is what you call a model


You can make any choice for it You can make it you can say that okay its a logistic regressor You can take any parametric form for that and estimate the parameters thats all yeah

speaker_4: Yeah got it

speaker_1: Okay uh Rajat

speaker_3: Sir my question is if we have some ways to identify the real PX


using some tricks or methods that and you told well discuss later in this course then I didnt what we will achieve by by a mini divergence because knowing the real px is something that we all interested in right

speaker_1: No we cant I mean the whole problem is there is no way to know real pHs Every whole present

speaker_3: how we will um


Diverge how we can create divergence

speaker_1: I have not told you that no I said yeah yeah that is one problem that is one question that I will answer in a while

speaker_3: I told you dont know I said

speaker_4: Well directly sample from the try to sample

speaker_1: Please dont jump There is a method to do There is something called law of unconscious statistician and law of large number that we will use and we will use construct some bounds Those are the things that we will do in this course I have told you that that is some question that we will answer Now how do you evaluate the divergence metric if you dont know Px is a question that I will answer I have not answered that Okay But I want you to understand the philosophy right I mean like what is happening You given data assume some parametric form on underlying Px


the divergence metric and then adjust your parameters of your p theta such that this divergence metric is minimized thats all i mean is this point clear i mean this is what i wanted to uh drive home if this is clear then the next question is of course what divergence metric what form how do you compute the divergence metric etc is what we teach in this course okay


Is that okay Yeah okay any other question on this


Okay now well take up the so now the next question is given


a pair of density functions


functions how to measure


The distance or divergence between them


It this is a question that we should answer now okay because


One of the I mean there are three questions right how do you choose the model is the first question then the second one is how do you compute the divergence metric the third thing is like how do you optimize right I will take up the second question first we will take all questions one by one but this is more important right I mean this is the first step so given a pair of density functions how do you measure the distance or divergence between them is the question see there are enormous I mean like of many many ways to do this


So there are things called F divergences that we will be seeing


And there are things called you know Wassersteins distance


optimal transport


And there are things called maximum mean discrepancy MMD We will look at all of these one by one But yeah so how do you estimate So you understand right Suppose Ive given you two points in Cartesian plane How do I know how close and far off they are Is that just compute the Euclidean distance right If this is x1 y1 and this is x2 y2 then you know how to compute the distance between them right x1 minus x2 squared whatever the usual Euclidean distance


Now if you are given two density functions how do you define uh how do you measure divergences or distance between them is the question okay


What we will do is


I will start with one famous divergence metric Okay so here is a question that I want to ask you

speaker_3: We should start that

speaker_1: asked you that but see um as i said in this course we will be looking at uh uh models like vaes and gans and diffusion models and and so on right um which one do you want to start with you want to start with gans and then go to vaes or


VAEs and then go to GANs So typically

speaker_2: No hes been good

speaker_1: Typically I used to do that I used to start with VAEs and then goes to GANs But this time Im just thinking I should do the other way around Ill tell you the reason The reason is these diffusion models right Diffusion models are special cases of VAEs Theyre actually hierarchical VAEs with a fixed encoding process So now if I do VAEs and then do diffusion models right I mean it will be fresh in your memory and I dont have to repeat things that Ive done for VAEs So now what


uh perhaps we will do is you know GANs are a very different class of models and they are sort of like out of trend now people are not looking at GANs because of the problems that it comes with so let us start with adversarial learning okay and perhaps then we will go to VAEs


So having said that I will simply give you an example of how to look at the divergence metric and how to compute that etc And then from next class we will go to adversarial learning So now lets take up this question Given a pair of density functions how to measure distance between them is the question Now to do that let us look at this Suppose


Theres an event


A okay that is in the set of events F okay and Im interested in


Nah no my sorry


That quantifies


Amount of information


want of information


associated with it


Okay do you understand So what are we trying to do now We are actually trying to derive a famous divergence metric between two distributions which is called the Kullback Lieber divergence or KL divergence Okay and to do that you know we need some concepts of like basics of information theory Okay Im just trying to derive that so that you understand where this actually came from Okay now suppose theres an event that is there in the in the in the in these event event space and what you are


interested in is you are interested in in a measure that would quantify the amount of information associated with it


Okay now that measure lets call that as some I of A What properties do you seek in such a measure I would say that the should be high


Four


Less probable events


should be low for


High probable events


Do you agree See if I have to quantify the amount of information associated with a particular event that measure has to be very high for less probable events right I mean what Im trying to say is if I tell you that the sun rises in the west tomorrow then it has a lot of information in it isnt it But if I tell you that the sun rises in east tomorrow then it does not have any information Do you see what I mean


So now this information measure that I associated with associate with a particular metric has to be such that it should be high for less probable events and low for high probable events Now if you take the asymptotic cases of it right So the information that is associated with the entire sample space should be 1


Or lets say okay it can be that also No it can be infinity right It should be very high because the probability of sample space is one right


the probability of sample space is 1 because something when you when you when you when you conduct the random experiment some outcome will come that is what this is saying so the information that is associated with the sample space has to be infinity and the information that is associated with the null should be 0


Because I mean if I uh are the other way around no sorry I think Ive switched it sorry


The information associated with the sample space has to be 0 The information associated with the null should be infinity Correct Thats the asymptotic case of what I have just mentioned You know if I say that something from the sample space always happens of course Im not telling you anything If I say that you know something from the null space happens then the null set happens and Im giving you infinite information The other property has to be that the amount of information right


that is associated with


union with the intersection that two events happen should be equal to the individual


Use me for this


The information associated with two events in union of two events happening have to be equal to the individual sum of individual informations if they are mutually


Independent


This makes sense right I mean they have to add up basically I am saying that if there are two events happening together and if they are mutually exclusive then the total information that is conveyed by both of them have to be the sum of information conveyed by individuals of them Does it make sense

speaker_3: So should it be I of A intersection B equal to null set or just A intersection B equal to null set

speaker_1: Ah yeah yeah yeah Yes Thanks This is what it is Yeah Thanks for that The typo Okay This is okay right Now in fact I mean these measures were proposed by Shannon okay great information theorist who is responsible for all the communication that we have today that he defined this thing right to be the surprisal of a particular event as the negative of logarithm of the probability okay


associated with that particular event A You should not be writing this as script P because we have taken the script P for


distrib the distribution functions right its the probability


This event A


Can you just take a minute and uh convince yourself that it it will uh


Satisfy all three properties that we saw


Ill just take a minute and verify this


Is it clear to all of you


Okay so this is for one event right So now suppose


need to quantify


information


distribution right


What do we do This is for one event right If we want to do it for the entire distribution how do we do that

speaker_2: integrate all the values

speaker_1: Just take an average right over all events


So lets say that this is a discrete disbl Ill do it in a discrete distribution in a


In a discrete lets say that its a discrete distribution for the ease of understanding discrete distribution


So now PMFs are probabilities right So I will say that I will have to look at the negative of log of the PMF function associated with particular value xi ok I look at this and I take an average of this with all possible values that is


which is


P x of xi and just simply take the sum


the values that it can take so this will quantify the average information


information associated


distribution


PX


Do you agree


This should give you so because a negative log of pxi will give you the information associated with one event one outcome if you take the average of it over all the possible outcomes then you will get the average information that is associated with


the entire distribution


Okay yeah some people have questions here Let me take a question


Yes uh go on with questions

speaker_2: Sir I didnt get why the information associated with null set is infinity and also why information associated with event A is minus log of probability A

speaker_1: Okay Im muted just give me a second Ill answer that

speaker_2: You can hear you sir

speaker_1: Hello can you hear me

speaker_2: Yes sir we can hear you

speaker_1: You never


Can you hear me now

speaker_2: Yes sir we can hear you

speaker_1: Okay see the thing is this is our definition See what I want is I want a measure that would take very high value for less probable events It will take very low values for high probable events Okay that is the measure that I want Now


The asymptotic case asymptotic case which is the extreme case is the following that if you take the entire sample space


take the entire sample space then that is the most probable event isnt it

speaker_2: Yes that will be

speaker_1: That should have zero information


Okay similarly the least probable event which is the null should have infinite information

speaker_2: I understand that probability part but how come that gets reversed when we associate with the information

speaker_1: That is how we want right See now what are we desiring See okay So Ill tell you some historical thing right The question that was asked is if you say that an event has happened you tell me how much information is conveyed in that is the question


Now intuitively dont you think that an event that has very high probability or which is very high which is very highly probable conveys very less information


Historically what happened is the question Shannon was asking is if I have to compress the I suppose I want to you know I want to pass a message from point A to point B and I want to understand it now

speaker_2: And its good to know

speaker_1: Got it now

speaker_2: Its easy to understand

speaker_1: Yeah so I mean we defined the information this way information content associated with an event this way that it is the negative of log of probability associated with it Thats all


Okay uh artistic


I just look at it no the probabilities get multiplied if the events are independent and there is a log right so log will get summed


Probability of A and B a pro log of A B is log A plus log B isnt it

speaker_2: Okay okay if theyre distinct okay okay yeah I understand

speaker_1: Lets lets I give you a minute to just plug that yeah yeah I forgot that

speaker_2: Yeah yeah I forgot that they are disjoint also so yeah okay

speaker_1: Okay so

speaker_2: Yeah thank you

speaker_4: are in this average function will it be like capital P right this small p was for probability density

speaker_1: Im saying its a discrete distribution right so this is PMF probability mass function which is a probability by itself

speaker_4: Sorry uh can you tell me

speaker_1: See I said that it is a discrete distribution therefore this p is a PMF function probability mass function which is an it is actually a valid probability


Great thinking Paul


Okay some it

speaker_2: So this union property that is there basically I a union B is I a plus I b but if we consider a union of a with null set means this the intersection will also be a null but then this property will not hold no because a union null will be a itself but then if we add them up it will be infinity

speaker_1: No A union null is no A union null is A okay You can still represent that as I of A plus I of null right

speaker_2: But I of null is infinity no So I of a plus I of null will be infinity

speaker_1: Yeah I know


are saying um I mean maybe I should just add that or


Yeah that will solve it thats the next case


Other tier

speaker_3: Also similar just an add on to that question if B was for example an A complement over here so I of A plus I of A complement that

speaker_4: equal to i of omega the leg the


That should be zero

speaker_1: Yeah of course


Post per definition


Okay so now theres a name for this Do you know what this list is called


Sorry its quite


So this is called the entropy yeah this is called the

speaker_4: Its quite cool

speaker_1: This is the entropy associated with the distribution that is its simply the average information that is associated with the distribution is called the entropy of that distribution


Makes sense now Makes a lot of sense So basically you define the information content for an event and just take an average over all possible events that are there and that will give you the entropy which is the average information that is conveyed by a distribution Is that fine


Okay so now I actually have to now define the cross entropy and


on its 12 20 already we started 15 minutes late do you mind if i continue for 10 more minutes or should i stop shall we take it the next class


See if there is even one person who wants me to stop no I will stop


because I should not be continuing


Is there anybody who wants me to stop now


Let me know if you


to go somewhere and you have stop Ill stop it here


So let me take 10 more minutes now suppose


Old entity functions


B and Q now if I compute


So looks like my screen has frozen


Wording thing this will give you


And somebody tell me what does this give me


Can I interpret this as


Can I interpret this it this way Can I say that its the average information in Q about P


In all of these cities


This also has a name do you know

speaker_3: So central piece

speaker_1: This is the cross entropy


brain BLANK


If I take this


and subtract virus


How do I interpret this


Can I say that this is the information


that this is the extra information


In B


not in cube can i call it this way

speaker_2: Sir the first term tells us about like gives us the information about Q right

speaker_1: information about uh p like if us you know here here cross entropy is a cross entropy tells you that how much information does q has about p

speaker_2: So about means uh

speaker_1: Oh dear


Right and it of p tells you the information in p which will take the difference between them


Do you tell me how much extra information is there with P that


The Q does not have

speaker_2: And it should be subtracted by HQ right

speaker_4: Its the terms should be reversed right

speaker_1: You mean hp minus hq z

speaker_2: HP minus HPQ


Otherwise like this inter like this is giving a sense that the term will be negative wont it sir

speaker_1: See that is a minus log there no


minute la minus law also it will be


Like this one how does this look like This is uh


This is correct because there is a negative there no


So in the definition of entropy there is a minus So when you subtract it the minus will just go away and it will become plus


Understand so basically the difference between these two will tell you the extra information in P that is not in Q


Is it okay


Now this is equal to


is correct no so theres a minus here theres a minus of minus will become plus so it will be p of px log px and this term has a negative here so log a minus log b is log of a by b is this okay


Do you know the name for this This is the name this is the

speaker_4: Need it to be

speaker_1: This is one divergence metric that we will study in this course that the clear divergence between these two distributions px and qx


Play Doh and buy


its log


In fact this is the last function that is used in most of the supervised discriminative machine learning to minimize the KL divergence between Px and P theta


Okay see the reason I did all this is to make you appreciate why this is a good metric So Ill leave it for tutorials okay to show that AL is 0 if and only if PX matches QX Only if the underlying distributions matches then the divergence will become 0 Obviously right because the amount of information that is there in Q about P


should not be more than what P has itself So only if P and Q are exactly the same distributions then the cross entropy matches with the entropy And that is when the KL divergence becomes zero So now this becomes a metric to measure how far a given distribution is


So now we will trace back to what we did So we wanted to define or compute a divergence metric between the true density and the assumed parametric density you know


Quantify how far it goes KL is one way to do it


Does it make sense


So in the next class what we will do is that given a particular model how do you compute the KL and how do you optimize for it etc is something that we will see in the next class okay so


When you come to the next class please come prepared Just read whatever we have done in the previous classes and also read about entropy cross entropy KL et cetera so that you have idea about what we are talking


Okay then we are done for today See you in the next class And again reminding right if you want to express something you know have some opinion the feedback form is there It is completely anonymous You can just go and put in whatever your comments are if you want You go to my webpage There is this ADRL course webpage and there is that feedback form and you can just simply put in your comments if you have any


Okay well thats all for today see you next week


Have a nice week and bye bye

speaker_4: Okay

speaker_1: Okay just a second Next week next Saturday is this Ganesha Tirthi Thats okay right We can still have a class


Yeah thats it


Okay anyway we are recording if people want to take off they can take off and see that later


Ill have to ask my mother if that is possible but yeah Ill convince her okay see bye

speaker_4: Yes thank you sir
