---
id: wQeMcnV_B-k
title: Lec 5 - Deep Generative Models Generative Adverarial NetowrksGANs
url: https://www.youtube.com/watch?v=wQeMcnV_B-k
date: '2024-11-23'
duration: 01:34:45
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

Okay what Im saying is what we will do is I will I will stop lets say after after 30 minutes or so once Ive gone through a major topic then we can have a question and session So if people have questions what I would recommend you is that just write them down Okay so whenever you have a question just write write them down on a sheet of paper


And whenever I talk and ask for questions I mean ask prompt you for questions ask me then Does that make sense So that there is a gap I mean there is a balance between the flow of the class and also the I mean I do encourage a lot of questions I mean Im happy that you people are asking good questions but let us not have multiple pot and pour interruptions So that the flow is there


thing and there was one there was a couple of other questions on uh


I mean some of you are asking whether this course is going to be a fully quote unquote mathematical or will there be some practical considerations issues that would be considered uh uh I mean see the a good answer that is that uh there is no practice without theory without math uh I mean having said that


Once we complete the mathematical nuances and other details you definitely go to go to the practical implementations because all your assignments will be coding assignments So there will all be practice based assignments only And also in the class and tutorials whenever needed we will also talk of the practical implementations and the other things


Okay uh thats about it I suppose anything else that you just take other issues that you want to discuss before we start the class

### Speaker 2

So I would like to share with you

### Speaker 1

Hello

### Speaker 3

Yes

### Speaker 1

Yeah anything you did did you have a comment

### Speaker 3

Are you able to hear me

### Speaker 1

Yes yes I can hear you go on

### Speaker 3

Yes just one suggestion if possible you cover theory and then you give a problem example right

### Speaker 1

Uh for theory and energy what

### Speaker 3

problems you explain a problem and give a solution to it right

### Speaker 1

Uh problem I I I didnt solve it yet

### Speaker 3

Well example example


Like you give cover cover a topic story of it and then you give example for that right

### Speaker 1

these are not like these are these topics are not like your lets say class 12 math where okay you learn you learn how to differentiate functions and then there are some example problems on differentiate functions its not that see now we are looking at adversarial optimizations or GANs right so by practice what I mean is for instance in todays class

### Speaker 3

Im playing

### Speaker 1

I will tell you how to try again practically right How does all the theory that we are looking at translate into practice practical implementation right So there are no numerics per se


Because its as I said no its not like a fundamental calculus or probability theory kind of course where you introduce a concept and solve many many problems to be solved It is not that way right By practical stuff I mean the implementation stuff That how would you how would you take these ideas and implement those in practice


Uh does it make sense

### Speaker 3

Yeah

### Speaker 1

Uh okay anything else

### Speaker 3

You have one more doubt right here This is about conjugate of a convex function


If we draw a graph of conjugate of a function convex function how will it look like Will it be inverse of it or

### Speaker 1

Yeah itll yeah itll look something like


Yeah


Should we continue with the class


Me


So Im throwing my iPad


Yeah also tell me whether this black background and the white font is okay with you or should we have to


Switch it to white background and black

### Speaker 4

I did it myself

### Speaker 1

It is fine okay


Okay

### Speaker 4

So so if possible just change the colour of pen whenever there is a highlighted topic


Like a note or anything

### Speaker 1

Uh that Im doing right Im looking uh doing that highlighted highlight thing

### Speaker 4

No no no I mean I mean when you are taking some new topic

### Speaker 1

No no no I mean I

### Speaker 4

something new then just change the color so that we can mark it properly if possible otherwise also fine

### Speaker 1

Uh but yeah so everything that I write is important that way Yeah So anyway so Ill Ill Ill take that into consideration Uh and also there was some uh discussions on KL divergence and and all that in the group No I will like I thought once we cover these topics it will be clear Uh or I Ill respond to that Okay Okay So lets start So just quick quick recap Uh before we go to the topic


for todays lecture so we were looking at adversarial optimization right or generative models uh via adversarial uh optimization so what is the context the context is that we want uh to build a generative model which is that it takes uh an arbitrary random variable as input in this case a gaussian random variable and it generates uh


or it samples from an underlying unknown distribution right so we represented that that function as g theta of z where z is an arbitrary random variable and its cap just highlight it


So this apple pencil is always with my laptop Whenever I want to write it it has 0 percent charge I dont know why Anyway so there is this function d theta that would map an arbitrary random variable z to another random variable x cap Okay Now what do we need We need a situation where this x cap has a distribution that follows the distribution of data


Okay which we have called px Why is that If this p theta becomes close to px then we have achieved what we want because then if you take an arbitrary variable z and pass it through this function g theta then you get samples from px which is the underlying distribution Okay


Now the question was how do you set the parameters of this neural network g theta such that p theta which is the distribution of the output of the neural network is close to px which is the input of I mean which is the input unknown distribution The solution for that is that what you do is estimate a distributional divergence measure between px and p theta that will become a function of theta and set the parameters of


this neural network theta such that this is minimized so if you do this then the resulting neural network g theta of neural network that you get will be such that it will take an arbitrary random variable z as input and it will output x cap whose distribution happens to be following px


Now if you recall the tutorial how do we solve this optimization problem of minimizing some sort of a divergence measure or a loss function with respect to the network All of you know how to do that correct Now this theta star equal to argmin d b theta px and p theta This optimization problem is solved using backpropagation


Is that okay


Any questions on problems problem setting the


how the problem is set up so in the

### Speaker 3

What is that


This accent is the complete image right

### Speaker 1

chart as the completing measure

### Speaker 3

Yeah and it doesnt depend upon the random inputs we are given

### Speaker 1

Very much depends on the random input right Because it is G T of Z Z is the input

### Speaker 3

Yeah but it depends on theta parameters right

### Speaker 1

It also depends on parameter parameters and it also depends on theta


See

### Speaker 3

Okay when I say input its z z which is a uniform sorry normal distribution on this diagram

### Speaker 1

It depends it depends on C it depends on theta both of it

### Speaker 3

But G is the random right

### Speaker 1

Z is random correct

### Speaker 3

Yeah then then it should not matter what we do right its random right

### Speaker 1

Oh that way youre going to see Okay so what when you said that it does it does not depend I thought what X cap that you get does not matter what Z that you get Thats not what it is So for a given Z you will get a given X cap But yeah but you can choose any input distribution on the arbitrary random variable Yeah that is correct

### Speaker 3

So whatever we give as Z because it is random well get the X cap right

### Speaker 1

post training post training if you train it such that this divergence is minimized then it is true you will get an x cap from the distribution different z will give you different x caps so you remember i told you to look at that this person does not exist dot com last time right yeah so every time you get a different you you give a different z as an input you get a different image generated

### Speaker 3

Yeah

### Speaker 1

Okay but you have to like you should not change the distribution of Z For instance suppose while training you have sampled Z from uniform random variable you should not start sampling from normal random variable when you are doing inference or generation That is not what should do what you should do

### Speaker 3

Okay so yeah does it mean that if X hat is a human face different Z will give different human faces

### Speaker 1

Of course driving different Gs will give you different outcomes correct

### Speaker 3

Oh

### Speaker 1

Okay


All right so now any other question on this

### Speaker 2

one quick question the output is gonna be human faces and human faces only but the mixtures of human faces or it can be like


You can have human faces with different features lets say three eyes or four eyes

### Speaker 1

Okay that depends on how good your training has been It that can happen See how does that translate to mathematical is that if you have made this divergence metric between px and p theta really low then you will only get images from human faces because px the data that you have been given only have like images from the distribution of human faces


Thats why you should train it well See if you have not trained it well in such a way that this divergence measure has not gone to arbitrary low values then you will have all these kinds of artifacts So you will see that in your assignment So in your assignment I will actually ask you to train these neural networks If you have not trained them well then the output will not be good

### Speaker 2

Got it so

### Speaker 1

Just one


one other question uh third question

### Speaker 4

Lesser of the two


Uh so uh just something I was wondering sir um like uh I was

### Speaker 3

looking at the talk as well that the Afghan authors gave on YouTube So it was not very clear to me like did they think of this adversarial approach first and then justified it or proved it with maths or the maths

### Speaker 4

to the discovery like what came first like the the intuitive understanding or the mathematical foundation behind it

### Speaker 1

Yeah


Yeah so thats a general question See Ive been in this business of research for a decade now I can tell you for sure that all of my papers the work that I have done its always that we do some empirical experiment based on some hunch It works Whenever it works we backfit the math


My firm belief is that if there is something that is working then there should always be good math behind it or good


systematic understanding behind it but the way this is how i do it i dont know how others do it in fact uh chronologically speaking no as our home minister said to chronologically so if you look at if you look at the chronology gan paper came in 2014 okay uh which only has em empirical experiments okay but this f gan which is a much more uh uh foundational uh


Understanding of what was happening came two years afterwards So that way uh empirical stuff came first and then math came later But


My I mean this is how


things happen right mostly in engineering research however while you understand so to me always principled understanding is something that i would like right i mean if you just tell me and give me an algorithm and say that oh there is a discriminator there is a generator okay there is these two networks competing with each other etc i will not be convinced because i dont know why it is working what is actually happening and so on so that is why when i teach i always teach math first from a math first approach because that is


more grounded and principled Now once we once I put down that mathematical foundation I would connect it to the empirical stuff which I will do in this todays class Okay Yeah But I mean its too long I mean its too long story short


In engineering mostly the empirical science precedes math but there have been a lot of cases where you come up with mathematical ideas and then translate it to empirical structure as well Both happens

### Speaker 4

Got it

### Speaker 1

okay so uh now the thing is given data and and samples from p theta so now again okay so now what is the core question here that uh you again im emphasizing this multiple times because it has to just look into the


your mind so basically the question that we have is we have this setup and we want to minimize this distribution and divergence measure between px and p theta okay now what do we have what we have as in at our hand are samples from px which we call as uh data okay that is what data is and we also have samples from p theta what are samples from p theta they are simply the outputs of neural networks how do we get multiple samples from p theta as somebody


saying you sample or you get you get multiple uh samples from the gaussian random variable how do you get the samples from gaussian random variable you have this rand in function right in in all pseudo random random number generators right you get uh the random numbers generated from random function and give it as an input to g theta okay that is so you get multiple samples from p theta so now you have samples from d you have samples from p theta


The question now is how do you compute the distributional divergence d theta so that we can use that as a loss function and back propagate through this neural network to minimize that That is what we need to do right If we take p theta and px and compute the distributional divergence and minimize the distributional divergence and train the neural network using that this neural network g theta will start generating samples from px That is the idea correct Yeah


So what is the big deal about it is that remember that the biggest problem in all of generative modeling or all of machine learning is that you


Do not know the distributions okay between which you are computing the divergence you only have samples from it So you dont know what the form of p x and p theta is but you only have samples from p x and p theta


Yes I have written that already right So how do we have samples from P x It is the given data How do we have samples from P theta It is simply choose different gs and pass them through g theta of c That will give you samples of P theta Now having samples of P x and P theta how do you compute the distributional divergence is the question Okay


Now before going to compute distributional divergence I defined a large family of divergence matrix which we called as the F divergence of which the KL divergence is also a member KL divergence the forward KL reverse KL gents and Shannon divergence all of them are members of this family we defined F divergence as this particular integral and this F


is a convex function okay so you plug in a convex function you get a different divergence metric okay that is what we saw


okay now coming back to our goal our goal was to compute the f divergence between px and p theta using their samples without knowing the underlying distributions okay so we saw that there is a way to do it uh the way to do it is that if you have uh an integral okay with respect to a density function to be computed you can approximate that using uh what is called a sample means okay now this result which we call


Love lies in numbers one


Simply say that


Integrals can be computed


out okay or rather with only the samples


So that is law of large numbers if you simply have samples from distribution and if you are looking at integrals of functions with respect to density functions without having so please look at this equation this is a pretty important so this one


Okay so this is actually one of the key equations that we will be using multiple times in this course that if you want to compute an integral of a function h of x with respect to some density function p of x I mean it is also called the expectation of h of x with respect to p of x you simply take the sample averages of the delta of x h of x computed all xis where xis are coming from px So in this case it is data right


You can compute these sorts of integrals using sample estimates This is a known result Now how do we use that If the divergence metric that we are trying to minimize if we can express that in terms of expectations over px and p theta then this divergence metric can be computed using sample estimates from px and p theta via log log logs Because we know that we can compute expectations using samples


this result called of last numbers then if we can represent our df in somehow via expectations over px and p theta then we can compute the m divergence you simply using the samples correct so now with that goal we now wanted to express df in terms of expectations over px and p theta okay now uh with this goal we saw that we cannot represent this m divergence exactly


the exactly where expectations over these two but what we can do is we can express the lower bounds on df in terms of expectations now instead of minimizing the m divergence we minimize the lower bound of it that is the idea one can ask no okay and we set our goal as finding out the g theta such that the uh the m divergence


sorry f divergence is minimized now instead of minimizing f divergence you are minimizing the lower bound on it i mean is it is it correct now thats not thats not exactly correct because if you can minimize the divergence itself then it is great but the problem is f divergence cannot be minimized exactly uh without having the distributions px and p theta now because we dont have distributions px and p theta but only have samples from it what


do is we instead solve an approximate problem which is minimizing the lower bound on f divergence okay right so now what we should do is in an issue we should bound f divergence and express in terms of expectations over px and p theta for that we did some uh some algebra we took the convex conjugate of uh of the f function in the f divergence and we did some manipulations and finally what happened is that we got


got this result where we expressed uh uh f theta okay df the f divergence uh as the uh as i mean we carved a lower bound on the f divergence uh via this expectation so what is this there is uh the lower bound that we obtain will become a function of this another class of functions called dx right now what we what we are saying is that there is some terminology here which is expectation of some function


of some other function f star of tx as x cap is coming from p theta right so we know how to compute both of these expectations why if we know what t function is then this expectation can be computed using log large numbers right where you can approximate this using sample errors i will write down all that and show you how to do it in practice okay so now basically what we did was yeah we have expressed the lower bound on the f divergence in terms of expectations over unknown distributions


Now the lower bound that we computed on f divergence okay is itself involves an optimization that itself involves an optimization problem over a class of functions Tx Now what I mean to say is that if you give one particular Tx you will get one lower bound on f divergence


And it is something that you should note


that as a note here


Okay so it is two


once it aired this was a little bit


Now lower bound


Or if theyre interested


No ones


following


an optimization problem


over some function classes denoted by t of x


Okay yeah this is the uh model of the story uh


See that Okay Is that now we constructed the lower bound on the M divergence or the loss function that you would want to minimize and we express that in terms of expectations over P x and expectations over P theta


And the lower bound itself contains an optimization problem that is to be solved over another set of functions class of functions that we denoted as Tx


Okay so let me stop here for a couple of minutes and ask questions Please ensure that all of you are totally with me on this okay Because whatever I do now will be building upon this So make sure that you understand this perfectly and then we will move on We will spend some five minutes on this And this is actually a key equation for GANs Once we do this then actually its all done Okay


questions

### Speaker 4

Sir I think theres a typo on the line just before this if you could scroll just a little higher


The close bracket I think should come just before dx in that line

### Speaker 2

and then the close bracket because p of p theta of x should be multiplied

### Speaker 1

Oh yeah right yeah thank you for noticing that


this here


More business


Some fancy thing okay


And this is for school girls and kids okay theyre eight something


Okay thanks Luke Sh Sir can you please explain how this greater than sign came once again


Like DTF is greater than


thats the content of last class but anyway so if you have to trace back the entire derivation


But

### Speaker 4

Thats the last step uh after TX

### Speaker 1

I mean we have been we have been after

### Speaker 4

30 star of science you want

### Speaker 1

You understood you understood why there is this why instead of having small t y capital T K M right because you are solving an optimization problem internally correct


Im fine

### Speaker 4

Oh yeah

### Speaker 1

If I pull that maximal maximization out okay So would this capital T or rather this Tx that we have right should be such that it will give you the solution for that optimization problem internal optimization problem at all x correct

### Speaker 2

Yeah

### Speaker 1

Now suppose there is some T x with capital T of x which is a function that would not give you the solution for optimization problem for all x

### Speaker 2

Okay

### Speaker 1

In that case what happens This entire integral that we compute right or the maximum value that we compute under that Tx will not be will always be less than the case where you would have gotten the maximum at all x isnt it

### Speaker 2

Okay

### Speaker 1

get it see sup i mean instead of t star of x which would give you the maximum value at all t if you had another function t that would not give you maximum at all points if it does not give you maximum at all points what does that mean it is always less than the maximum right it can at most is equal to the maximum or it is less than the maximum

### Speaker 2

Yeah okay yeah so

### Speaker 1

So basically what you are doing is you are searching for that function okay T of X which would give you the maximum value for that optimization problem at all Ts sorry at all X


Now if you get that function then this inequality will be the weak quality


If you get that function


Okay now what is the script T Script T you can see the visualize script T as a bucket of large classes of functions So you are choosing from a bucket of family of functions


Okay now if you in that bucket of function that you are searching over if you can get a function small I mean t of x such that it is equal to t star of x for all x then this becomes equality

### Speaker 2

Yeah good observation

### Speaker 1

But if you cannot get that function if you get another function t of x which is not equal to t star of x at even at 1x then it becomes inequality because at that x your t of x is less than t star of x


Call it no

### Speaker 2

Yes I can record

### Speaker 1

I can write it maybe


Ill write that here


inequality


Bites


Because


DRP


less than or equal to t star of x


for every x lets up


Okay if


T of x is equal to T of x star oh sorry T star of x star


Paratolics


Then you correct


Yeah I think thats worth writing


And see one other thing Im almost ensuring that whatever I say you know whatever the storyline that I build Im writing all of it right one after the other right I mean I write this as goal questions and all that So this notes right please go through it before you come to the next class Every class go through this line by line step by step Also you have the recordings watch the video and come to the next class That will help you a lot And of course


We are available for questions for WhatsApp and Teams Okay

### Speaker 4

Yes sir in this case this T of X do we choose any function and then try to optimize it or we d we try to

### Speaker 1

Good try too Good good question uh see if you know how GANs work in other than this network there is another network now which is called the discriminator network


That is your t of x The need for another network comes up because you have to choose from a bucket of functions and you optimize when you pick those bucket of functions you approximate those functions using another neural network We will see that

### Speaker 4

Okay okay yeah thank you so much

### Speaker 1

Okay any other question


Yeah

### Speaker 4

function

### Speaker 1

No no no no no no no See this T has nothing to do with that F See F divergence in the F function in F divergence know that our definition only that is convex Nothing else is convex This F function is convex thats all


Should have been one


Skuttle


See on a lighter note the person who put this feedback no please dont take it badly I mean theres no anyway its anonymous but it was pretty funny So I received a feedback where somebody said that you know Im paying this much fees to ISD for this particular course So I expect this this is right So I mean one thing was its very very revealing for me that this course


cost this much money I didnt know that apparently every credit here is worth twenty thousand rupees no I mean I was thinking that all this is reimbursed for you from your respective companies


Dont they I think they would know I mean there is some learning program thats always there You dont pay these fees from your pocket do you Just curious Im not asking Im not asking that that person who wrote okay I dont want to I dont wish to know But yeah in general Im asking out of curiosity So not all of you like your companies dont pay that huh

### Speaker 4

Im not ready

### Speaker 2

Partially

### Speaker 4

Absolutely

### Speaker 1

I see

### Speaker 3

But I think its different

### Speaker 4

But I say its difficult

### Speaker 2

That is fully sponsored

### Speaker 4

for response

### Speaker 3

This conference

### Speaker 1

See that makes me feel a little little less guiltier you see okay so

### Speaker 4

too for all

### Speaker 1

Then Ill be speeding

### Speaker 4

No you are not guilty

### Speaker 3

What was the question

### Speaker 1

i have some demand right i mean they have to teach more practical stuff you know i didnt pay the fees to look at math and whatever it doesnt matter thats thats fair also the demand was fair i mean im not im just joking right i mean this the weight of putting it that okay i this is the amount of fees that i pay i mean its sort of exorbitant uh thats a lot i didnt know that this course cost that much money okay so but they said that okay


paying this much money not to look at math or whatever but then I thought okay yeah its a lot of money I hope see if its your company that is paying I dont mind no they paid for all kinds of stuff thats not big money for your company but if youre paying it from your pocket then its its it is I mean its all relative but still yeah


So one credit apparently cost 20000 rupees right interesting okay which is considerable

### Speaker 4

But this is one of the prime courses in the program so maybe he felt like that

### Speaker 1

Hop hop how do you know that its a he I dont know I might be here

### Speaker 4

I dont know thats

### Speaker 1

Uh uh here so so this is the

### Speaker 4

So simple so this is the course Im doing the M Tech for

### Speaker 1

People are acting

### Speaker 4

People are acting yeah

### Speaker 1

I mean I understand you know you uh to I mean dont get me wrong again that customers always have their right to question whatever the product that is being see everybody now talks of customer obsession and all that right so customer is looking that is the reason I put that feedback form out and it is totally anonymous and whoever wrote that please dont get uh offended Im just taking it lightly so whatever you think


is a fair demand put it out there and ill be happy to incorporate as long as i can incorporate okay yeah okay

### Speaker 4

Sir how about the offline classes student also register for this course and elective subjects or lets say generic one like three four classes for them

### Speaker 1

again uh what is what is the question

### Speaker 4

I mean how offline classes goes uh they need to register for this core courses or its a scheduled for them like first year these classes next year

### Speaker 1

no no no no no very similar to you i mean there are core courses just like you have three four core courses right they would i think have some six core courses rest of all are all uh like this thing um electives and by the way i also teach this course right offline and im doing it in isc right now that class also has 100 plus people in isc and uh trust me uh thats i mean thats at least two three times more mathematical than


this okay i would i mean i i know that most of you people are not most all of you are professionals and might have been a little out of touch of from maths but there i do like much more maths than this so this is not the upper bound of your maths that one can do in this course so please be rest assured on that but anyway if you have any any anything that that you would like to see as a change in this course let us know that is why we have that feedback thing and we are happy to listen


Okay

### Speaker 3

Modes are in a regular product development like this type of maths we are rarely using right

### Speaker 1

I mean Im did I become judgmental I mean Im not complaining at all I completely agree with you that you dont use that but that is why no I kind of


Yeah so make it accessible I try to make it as much accessible as possible But we see there is another way to teach this Ill tell you honestly I can completely get rid of math and only teach it like what is done in Coursera right Or this Android kind of stuff where Ill just give you algorithms and tell you put some block diagrams and tell you how to do it But honestly right as an instructor I dont see value in doing that See whoever has done this course before again this is not self bragging have told


that uh you know doing it this way uh while difficult uh while while it is difficult during the course time right but if you put in enough effort to understand and do assignments and uh tutorials and all that uh they have been benefited from this you know this is what will actually differentiate uh you people from everybody uh and their grandmother who does machine learning so everybody is a data scientist these days right what differentiates uh


somebody who knows well and somebody who does not is that you know some of the fundamentals and you can go more deeper into it So I there is value in doing math Its not that its totally valueless but I understand that it takes a little bit of more effort but yeah that is what I expect from you people to do Having said that let me know if all of you think that math is completely valueless Its much easier for me to teach the algorithms and course around we can do it


but again thats not my recommendation though okay so lets continue so what we had was that we had this


call the word bound on DFTI budgets lets start from date given so we are given data


Thats it


This is


ID from PX on from PX


so we have constructed an f divergence between okay before that well write what our p theta is so we have this setup where


That is a neural network


And the AI represent neural networks right they


represent the dimensionality of the data so this is a neural network whose


Dimensionality keep increa increasing as you go deeper and deeper


By the way did Chidan do backpropagation for CNNs or was it only for material MLPs

### Speaker 3

Mail piece mail piece

### Speaker 1

For the M and N piece okay


Okay then you should look at backprop for CNNs okay just as an exercise When its not completely needed but its a good exercise to do Okay g theta and whatever we get at the output is what we call as x theta And this has distribution p theta right This z was coming from normal distribution Now with this setup we constructed a lower bound on the distributional divergence between px and p


theta okay this v set was greater than equal to this maximization over a class of function so what does this mean this actually means that you are searching over a class of functions script d and the thing that you have is you have an expectation here with respect to d of x as x comes from px you have another expectation here


respect to F startup


effects as


X graph here as X graphs comes from P theta


That is what we have seen so far Now the question is um so recall that we are interested in recall


interested in finding out a theta star okay that is the minimizer


The m divergence right This is what we wanted


We could not do it because we didnt have access to PX and P theta So we approximated that by the minimizers


And this minimization is over theta okay minimize this minimize the lower bound


Okay now which is


And by the way all of you understand this notation argument right Have I explained notation argument


it right i mean it is that set of theta which would minimize whatever is there within the function okay mean is the minimum value argument is the minimizer okay the argument which minimizes fine so you have to minimize over theta which is the lower bound


No that it door bound


Its a further maximization of P


This differences of this expectation I will not write it expectation over the px minus you have expectation of something with respect to e theta this is what it is right


Oh thats will become will become


Okay maybe before that let us do this


Now this minimization right this the outer minimization is


Mean with respect to


is pay attention here this is mean with respect to


I dont know what this


Often you dont know what correct


Theta are parameters of a neural network and you need to minimize a function or a value with respect to parameters of a neural network Do we know how to do that

### Speaker 4

Back up

### Speaker 3

Thats okay

### Speaker 1

That is back propagation so you can do this using back propagation


back prop over what


over the G theta network


Okay thats what it is Now there is


is maximization with respect to class of functions


Do we know how to solve that We dont


we dont know how to optimize we know how to optimize over parameters of a neural network we dont know how to optimize with respect to a class of function so what do you mean by optimization over parameters is that i mean we can we can do a gradient descent in the parameter space in space of parameters of a neural network but we cant do gradient descent in the space of a function right we dont know how to search over functions we know how to search over parameters how do we get rid of this problem is that so you translate


the second door


Do that represent


script T which are the family of functions that we are optimizing over via neural networks


Lets call them T W of X where


WR the set of parameters the set of


Means


I use the word weights and parameters interchangeably weights are parameters of a neural network


Now with different w values okay you will get a different functions Tx do you agree


Because it is represented using a neural network


Can I ask a question at this moment


Okay go on Sir we are trying to represent the set functions using neural networks Im just trying to understand lets say we want to represent a cubic polynomial or a

### Speaker 3

a polynomial of nth order then in that case how will we represent it using neural networks

### Speaker 1

easy right so now this function uh cubic polynomial right i mean are you talking about a polynomial a vector valued polynomial or a scalar valued polynomial

### Speaker 3

Anything sir

### Speaker 1

Yeah if its a scalar value polynomial then what do you need So lets say that f of x is equal to ax cubed plus bx squared plus cx plus d right Right Yes So you build a neural network that will take x as input and give you f of x as output See thats what you do in all classification and everything right


Or something

### Speaker 3

So like there like if we consider a multi layer perceptron so we have the weights we have the bias okay

### Speaker 1

Yeah

### Speaker 3

And then eventually for each layer we have a non linear activation

### Speaker 4

Okay so Im trying to understand there like how lets say I want to do x cubed


So that case how will I do that

### Speaker 1

You can right see that is the regression problem what you are saying is the classical regression problem okay so


Lets say that your f of x is equal to


Okay so what you have is for different values of x you have f of x So what you have is lets say its an x1 f of x1


x2 comma fx2


And so on you have XN comma of XN this is your data


Heres what you have you should have this to represent this as a neural network


So what I do is I will have an MLP


you take xi as input so it will take xi as input and it will predict f of xi as output


This is a T predictor


Now how do I train this neural network this lets call this cap X of theta thats all theta star is equal to


Really wrong


We have n samples here one by n one through n Ill take f of f theta of f xi minus f of xi


Thats all now this is classical neural network training this is solving a regression problem

### Speaker 3

got itself

### Speaker 1

This is how we are representing this polynomial function in a neural network program


See thats hard

### Speaker 4

So so the presence of non linearity allows us to also model this non linear functions right

### Speaker 1

Well yeah see okay that is some other dual networks


The deep neural networks are universal function approximators That is why they are powerful


Okay now what does this mean That means that by choosing the weights and the biases and the non linearity of an MLP which is deep enough you can represent any function to arbitrary closeness That is a known result That is why the go to architectures for all machine learning these days are neural networks


Theyre fine


Okay so I think we should move this

### Speaker 4

So Im not sure if you


But here we like already know that function should be like T x right like T of x so can you put some restriction on that so that it will no

### Speaker 1

No I mean T where is what do we we dont know I dont I understand we dont know anything about T what do we know about T

### Speaker 4

Not in one day

### Speaker 1

We know nothing about tea


See in the F Bergens case T is simply a class of functions What we know is that this T has to be such that it is a solution for the inner optimization problem for all x But we dont know anything beyond that no


See we want the T to be such that it maximizes whatever is there in the internal bracket thats all


See just like we had that regression problem that I had written So here you are only solving an optimization problem with respect to this T So T is a neural network Okay So I write that

### Speaker 4

But I think we know here like it should be the maximum value right So at least that conditional things can be

### Speaker 1

No no hold on you want


we want see this is an optimization problem that we are solving just okay i erased it it is no different from the problem that i had just written so you had to minimize you had to find a theta such that it minimizes uh the


Differences between norm of these two functions right That is what we had for the regression problem isnt it

### Speaker 4

Yeah

### Speaker 1

it this is exactly the same instead of having the differences between the predictions it has some other expectation thats all


You are trying to maximize see maximization minimization not both I can write this minimization as maximization with a minus here correct


same thing that is we dont know anything we only know that this neural network has to maximize whatever is there inside okay now i will write that so now i mean i hope that all of you understood what i mean when i say that i will represent this t function via neural network okay now what happens is we will write down so with this


Oh no we have


a G theta of C network okay that will take the C and give you X cap


from P theta okay so maybe we okay a complete as we can write we have another network now neural network


which is T W of


x will take x and it will give you the output tw of x


Instead now there is a particular loss function which is okay let us write that as loss


Its like not loss but it does cost functions


equal to


expectation of


T of x as x is coming from p theta minus the expectation of f star of t of x


Next cap is coming from


If x graph is coming from d theta now what happens is we need to find the optimal w for this d network such that


to maximise this cost


We agree


of you agree let me just see what what is happening here look at this right we have to find the t network or the t function such that this cost is maximized correct


All of you with me on this


Now we want to find theta such that it would minimize the same cost


Im sorry I should not write it as argument and argument right Because w star is not the minimum value of the function It is the minimizer of the function So it is the argument with respect to all possible ws And theta has to minimize the exact same cost

### Speaker 3

Sir is the first one is P of Px right instead of P theta the cost

### Speaker 1

All right good good thanks


This is okay So there is a cost function Okay And there are two neural networks here So one neural network has to maximize that cost And the other neural network has to minimize that same cost Now where is this coming from You look at this right Let me write that down So basically what is happening is so we have represented the T function So first what happens is that you construct a lower bound on your F divergence


Bye man see you my Ziggy


Expectation over PX


minus expectation over p theta so you maximize this with respect to w you get a lower bound on on what on a divergence


I completely like it so that it is


an expectation over t of x okay t w of x now right because uh it is parameterized using another neural network now minus is another expectation with respect to p theta of f star of


of x gram t w of x gram now you optimize this with respect to w you get a t function which is actually a neural network now that would create a lower bound on this thing right solving this


38


I dont know about


On DF


recall what was happening right so this lower bound is is created by maximizing this now if you choose one t it will create one lower bound do you agree


One particular p function will create one particular lower bound correct


also note that the lower bound that we have constructed right on df for a particular theta


What does that mean See look at that this last function that we are calculating no is a function of theta Why X cap is a function of theta here


Do you see that


x cap that we get right depends on theta so its a function of theta the last function is a function of theta do you agree


So for a particular theta okay maximizing this thing will create one particular lower bound on df


Now once you create a lower bound on the F divergence for a particular theta you want to minimize that lower bound with respect to theta I dont have space to write it here


I bet it


So this minimisation


Many measures


Reminders


Anyways I still want to vote


In my cell that lower bound


that lower bound okay created


YTW in the previous step


Do you understand what is happening So first you you have a d function okay that would create a lower bound at a particular theta So you start with some random initialization for this d theta okay and then you train this d w network okay you create a lower bound Now with that lower bound you have to minimize that lower bound right because ultimately the goal is to find a theta that would that is that makes p theta close to p x Now we are not minimizing the exact


we are minimizing a lower bound Once you create a lower bound with a particular tw we note that after you train this network once okay one t function is fixed created actually So once you create a particular t function then there is one lower bound that you have created Okay and once you create a lower bound you train this neural network to find a theta that would minimize that particular lower bound


Okay now once you have minimized that lower bound you can again come back to this t function and change the t function again which would create a new lower bound for that new theta that you have learned


Do you see what Im saying


See the lower bound is created for a particular theta


you understand now given a theta t will create one particular lower bound now once a lower bound is created you can make it you can tweak your theta in such a way that your p theta gets close to a ps okay now with that p theta changing your t function again will create another lower bound maybe its tighter this time okay then with that lower bound you go back to theta and you keep alternating


between these two optimizations


Do you see do you see the pictures what is happening


So I mean again right you know that there are two networks right and by the way this network is is what is famously referred to as


the generator network


And this network is referred to as the discriminator or the critique network


See in the next part of the class I will give you concrete examples for one F divergence which is the original CAM formulation and actually show the loss equations and back propagate and all that Okay But here I want you to understand the abstract picture that there are basically two functions You know why do you have this discriminator network This discriminator network is simply creating the lower bound on the F divergence And lower bound itself has a optimization problem that is to be solved right Once you solve this


either optimization problem with respect to W okay you get a lower bound and for a particular theta and you minimize that lower bound with respect to theta okay so you have gotten a theta that has minimized the lower bound now what is the guarantee that the lower bound that you have constructed is tight or good lower bound so with a theta that is closer to the uh the


Here you create another title log or mode that you keep alternating between these two


See these kinds of problems uh I will take questions in a while so suppose you have a loss okay a cost


So it depends on lets say that this cost depends on


Two set of parameters


theta and w okay now what you are doing is you are maximizing the same cost function with respect to w and you are minimizing the same cost function with respect to theta so basically you are seeking the theta star and w star which would simultaneously maximize this loss function and minimize this loss function right so what is actually happening is that imagine that you have a you i mean i cant write it in uh two dimensions


that is the problem so basically imagine this cost okay lets say that both your theta and w okay theta is one axis here okay and w is another axis and your cost function is


Something like this okay


difficult to write that sad anyway so if its like this now what am i seeking is i am seeking a point right in the theta comma


W axis okay in such a way that if I move


In in in either of the directions at the theta star the function increases


If I move in the either directions of w okay at that w star the function decreases


you see what is happening there is one function okay uh one cost function which is a function of two set of parameters theta and w now i am seeking the point theta star and w star in the in the parameter space such that if i move on the function around that theta theta star the function value decreases at increases at both the both the directions and if i move uh along the w direction


At that particular point the function value decreases


Do you see that


Okay so these kinds of points right these kinds of points are called saddle points


because theyre like sorts of saddle right i mean you know what saddle is now saddle if you move along one direction at that mean the the function increases if you move along the other direction the function in decreases right thats why its called saddle points now this sort of an optimization problem right where you are seeking saddle point of a function they are called adverse real optimization thats why the name adverse real


Yeah adversarial networks


or those serial problems so because of obvious uh reasons right so this uh uh inner optimization problem right okay is trying to uh maximize whatever you are trying to uh rather the outer optimization problem is trying to minimize the same cost function that you are trying to maximize in the inner optimization problem so in that sense the inner optimization problem


is quote unquote adversary to the outer optimization problem and vice versa see in mathematical sense you are simply seeking a saddle point so GAN mean the optimal value for the GAN right the optimal parameters for the GAN the optimization problem that you are solving in a GAN is simply a saddle point problem which is that you have the same cost function we know why now right we have the same cost function and we have to maximize that cost function with respect to one set of parameters w and we have to


We will use the same cost function with another set of parameters theta


Right But where did this come from It came from the fact that we started see this network the another T network came because you remember the entire story please So you have a divergence metric between P theta and P x which you would want to minimize Okay You could not minimize that So we constructed a lower bound The lower bound that we constructed becomes I mean is dependent on another class of functions T of x And we represented those class of functions using another neural network


This is why another neural network came into picture


Okay see as you can imagine I will I will explain I mean dont worry I will like tie all the loose ends in this class But yeah see I mean just as a side note you can imagine that once we solve this optimization problem this discriminative network is of no use Well discard it right Because our ultimate goal is to give a Z as an input and get an X cap that behaves like PX right So this is of no use This T T W network is only to construct the lower bound on the F


divergence so that is why it is used during training but during inference or prediction or generation tw network is not at all used we will come to that in a while but anyway so we represented this t function using another class another set of neural networks so every time you get a t fix a tw function you will uh get a lower bound of the other things but to find this tw network there is a maximization problem that you will need to solve okay so this maximization


probability of solving creates a lower bound on the divergence for a particular theta once you create that you minimize that with respect to theta which is minimize that lower bound which is created by tw in the previous step and you keep alternating between these two so create a lower bound minimize it make that lower bound tighter again come back and minimize it make a create another lower bound try to minimize it and you keep alternating between these two so till a point where do you stop this you stop at a point where i mean


you stop gan optimization is a question that is uh thats not well answered i will answer that in the next half of the class but yeah so this is how you you uh you do an optimization in that i mean that is why its called an oz real problem because you have the same cost function that is being maximized with respect to one set of parameters and you are minimizing the same with respect to another set of parameters


Okay so I will stop here and take some questions and then we will break for a short break and then well come back and Ill make it much more implementation friendly and Ill take an example for the M5 versions and we will go to that basic GAN paper right which happens to be a special case of this Okay I have questions here Im sure there will be many


Please raise your hands if you have questions


A lot of people raised their raised their hands when I was explaining did I explain it in such a way that your questions are all answered


Its good to know Okay uh yeah

### Speaker 4

So what are what would be the dimension of this T w of x You have shown it as a narrowing right

### Speaker 1

Yeah yeah yeah Yeah thats a good question Depends on the f function that you have chosen For the knife when your f function happens to be such that it is the underlying divergence is Jensen Chandler divergence no That happens to be a scalar which could be interpreted as a classifier I will show that in the next half of the class That depends on f function no Because if you recall the definition of our t function from the previous class


What was t function t function takes x and gives out values from the domain of f star So whatever f star you choose f function that you choose this t depends on the choice of f divergence that you have made See that is why now that you asked that question it is very relevant See if you choose your f2b Jensen channel divergence this discriminator network will take x and give you values between 0 and 1


If you choose your f divergence to be what is called as chi square distance I mean choose your f in such a way then your T W network will become a regressor which means that the output of your T W network will be a real number And that is why you know different f functions will give you different instantiations of GAN So there is this L S GAN least square GAN which is just using an f function which corresponds to the chi square distance The ninth GAN is when you choose your f function such that your f double


is Jensen Shannon divergence so if you choose it to be total variation distance then it becomes TV Garam


So see what I have done I mean for you if you if you people can appreciate see when you write a class in object oriented setting write the constructor of a class now that is what I have done now


Okay so all these GANs are simply instantiations of this class


if you can if you can see the analogy so what we have done is just constructed the family of giants so each of the thing would be an instantiation of it okay


Yeah uh thank you and yeah and Rajit

### Speaker 4

Uh thank you

### Speaker 3

Yes the difference or the cost we are maximizing is the difference between random or okay X and X hat right

### Speaker 1

a difference between two expectations

### Speaker 3

No but X hat is the

### Speaker 1

The output of the out out X hat is the output of the G theta network X is the data

### Speaker 3

Yes so we are taking the difference between these two the difference by us no

### Speaker 1

We are taking no hold on hold p precise we are not taking difference between the data points we are taking the difference between expectations of t functions and f star of t functions where these x star and x comes from the corresponding distributions that is what it is we are not taking x minus x cap here we are taking the difference between the expectations of tx and f star of tx cap as x and x cap are coming from px and p theta


You see that the cost function is difference in expectations not difference in data points

### Speaker 3

Yeah thats correct so thats the difference between averages right

### Speaker 1

Difference between averages of not x and x cap again Difference between the averages of Tx as x is coming from Px and F star of Tx as x cap is coming from Px


It is again not the average of x it is average of p x


It is not average of x cap it is the average of s f star of t of x cap


Is that okay

### Speaker 3

Yeah and then this cost or the maximum maximization should not be equal to minimization which we are doing over theta

### Speaker 1

I didnt follow the question

### Speaker 3

First we are maximizing the this difference right


And then we are minimizing the same

### Speaker 1

So you should realize that maximization is with respect to different set of parameters and minimization is with respect to another set of parameters


The cost function is the same but maximization is with respect to w minimization is with respect to theta

### Speaker 3

So when we minimize maximize with respect to w are we not changing theta in any way

### Speaker 1

No no


That is why I said no its for a fixed data So you alternate between those two


So I will also show the you know the way the gradients flow in both of these in the next half of the class that is what I will do I will put out a particular f function and I will write down the gradients and also write the gradient descent equations which you would have to implement in your in your assignments okay By the way you will all be implementing all this that is the that is what you will do in this in your assignment so that there is absolutely no gap between the maths that we have done and the implementation that you do okay


Okay uh okay uh astic

### Speaker 4

Yeah so so you mentioned that we are maximizing and minimizing the same cost function

### Speaker 1

But but but but with respect to t two different set of parameters yeah

### Speaker 4

Thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats thats


Yeah yeah yeah so uh it is uh sequentially or at the same time it should be sequentially

### Speaker 1

It is sequence you know alternate

### Speaker 4

Okay okay okay and first we are maximizing

### Speaker 2

Then for that fixed value then

### Speaker 1

And its

### Speaker 4

Fixed value then we are again minimizing it for

### Speaker 1

Yes the order does not matter because you start from something and then you alternate between them no Okay yeah that makes sense

### Speaker 4

The order


Okay yeah that makes sense

### Speaker 1

Or order does not matter

### Speaker 4

Mm yeah

### Speaker 1

13


Its a two set of weights and weights correct


There are two neural networks one ones one neural network Ive called as W the other parameters Ive represented as theta


Ah correct both of them are like backpropagations only Both the maximise of course no both the optimizations are sort of using backpropagation only

### Speaker 4

for one given w that you maximize the cost and then for theta you minimize so like do we compare for all different ws

### Speaker 1

no different w now you are doing just gradient descent see one one iteration through uh tw and you get a w you get a lower bound now you get another you do one iteration through g network you get theta right then you come back with that fixed theta the cost function changes now see once you change theta the cost function changes

### Speaker 2

Um yeah okay

### Speaker 1

Now you come back to your W network tweak your W again And now the cost function has again changed Go back to your theta network change your theta and keep alternating between those two


See mathematically what is happening is that the moment you have a particular T that is fixed no there is a lower bound that gets fixed but that lower bound need not be tight


The door door door need not be typed okay so maybe if you want I thought I would do it at the end okay let me let me save that for the end okay because thats there is one picture that I write

### Speaker 3

Oh

### Speaker 1

please mute that okay see uh there is one picture that i write okay of what is happening uh alternatively uh that would give you i mean that would actually tell you a lot of story but that can that i can write only when your t function happens to be a classifier in the case where your f is jets and and divergence i will do that i will do that in this class at the end of the class it will youll get much more clarity as we move on okay


Okay


Any any other questions

### Speaker 3

Yeah sorry

### Speaker 1

Yeah yeah so she

### Speaker 3

Yeah so she maximized yeah so I

### Speaker 1

X cap no X cap is coming from d theta


scan


Next cap is coming from G theta no


Okay uh another question okay yeah

### Speaker 3

Another question okay yeah When do we stop Because I told you

### Speaker 1

The I I told you no I I told you I I I will tell you this topic criteria next in the next half of the class


So okay well take a break I think Ive been here since nine So take a 15 minutes break It is 11 point 10 in my clock Shall we come back at 11 point 20 11 point 25


11 30 we come back at 11 30 well only have 45 minutes okay 11 30 is also fine okay 11 30 well come back as theres another yeah people can leave but interesting now there is uh abhishek are you there


Okay I think hes not there yeah this uh his name in his name in his name and my name mean the same by the way okay


In Sanskrit right the word tosh represents happiness And any prefix that you add to it is just qualifying that So sum is a prefix that would qualify that It says you know exalted happiness So santosh is of course you know what that means right So pra is another suffix in Sanskrit that would have the same meaning Thats my name And avitosh is one other thing So yeah I was looking at his name and then


got this thought and thought to share you but share with you the person is not around anyway doesnt matter

### Speaker 3

Or opposite or same

### Speaker 1

No no same thing all these convey like magnification of whatever you are saying


So Tosh is happiness Tosh Avritosh Pratosh all these they mean the same You might have also heard this name of Ashutosh no Yeah Ashu means quick So thats why the Shiva is called Ashutosh somebody who gets happy very quickly So that is just a little different But Avritosh Santosh Pratosh all these mean the Paritosh I am not Paritosh by the way My name is Pratosh


It seems

### Speaker 4

Seems like too many happy people in the team

### Speaker 1

I always tell my parents that its a Mishnah and my name is


So I dont know how happy I am in my life but yeah they named me happiness And whats more interesting is when my parents named me they didnt know what my name means Somebody suggested and it looked unique and they just chose that name So then you know I dont know if how many of you know that I also happen to be interested in Sanskrit and Indian history philosophy


So studying Sanskrit for a long time then I realized what the meaning of my name is


Anyways

### Speaker 4

On a different note I think uh

### Speaker 1

Hey hold on hold on hold on see we are we are we are in the break people can leave this is all not in an unrelated stuff but yeah so go on whoever wants to say

### Speaker 4

Yeah uh so actually I think uh you remembered in the Sangaskrit club as well right So I thought uh there will be some way of teaching from the scratch Uh that was my interest point to join that

### Speaker 1

Its actually

### Speaker 4

So is that a

### Speaker 1

I am not an active member there I mean it is mostly it is mostly like headed by Sankirtan and Shankarama and these people I dont have a lot of say see when I was in IIT Delhi I used to teach Sanskrit to people like like undergrads there that was my here I have too much then I didnt have a family no I have two children and you know

### Speaker 4

Sir sir sir what is the thing like you resigned from IIT Delhi and came to IAC


I mean why you reside from IIT Delhi

### Speaker 1

Because Bangalore is my home Im a South Indian guy and Uttna Garmi or Tantakom I say I am


In fact thats actually yeah thats I mean come on right I mean say here anything more than 30 is hot for us and anything less than 20 is cold for us and uh it was too much

### Speaker 2

Yeah correct

### Speaker 1

Thats thats the only reason otherwise I was very happy at Delhi Professionally there was there was absolutely no problem and I like see when I went to Delhi I I thought that I would you know I would want to come back as soon as possible in fact because you asked when I was applying for faculty positions I applied to Bombay Madras Delhi okay uh i i could not apply to isc because i did my phd from isc only no they will not take their own students


Unless they go out some for some years and come back


Now that option was not there I applied to Bombay Madras Delhi and my preference was of course first preference was Madras and then its Bombay then you move up the map right But the first offer was made from IIT Delhi

### Speaker 4

But you for your PSD youve done PSD right sir

### Speaker 1

Otherwise you cant become faculty in any of these places

### Speaker 4

So from where you did this business

### Speaker 1

So only I see only

### Speaker 4

Oh I yes it said

### Speaker 1

Yeah so like 10 years back 15 years back I was a student at IIT So Silya forcefully I went to Delhi but what I was saying is when I went to Delhi I started liking it I mean some of my colleagues at Delhi told me that Delhi will grow on you you will start missing Delhi and all that I never thought I would miss Delhi but Agni I miss Delhi because there are lots of good things about Delhi which is not there in Bangalore Bangalore is its a doomed


place and infrastructure is so bad and even though I come from technically Im not from Bangalore Im from a place called Mysore which is 150 kilometers away from my Bangalore which is heaven yeah but this Bangalore is hell

### Speaker 4

Just so I know

### Speaker 1

I mean all broken infrastructure rude people right you know what I felt people in Delhi more more softer compared to people in Bangalore everybody says that North Indians are harsh or nothing but I mean after Hindi we were talking about that thats all the moment you start speaking in Hindi and people are people are more cosmopolitan and more softer there my God


Dreadful when I see auto drivers and all the other people here okay this is getting recorded dont put it on some social media right I mean I see professors make some comments on

### Speaker 4

I think so

### Speaker 1

So these days you can you cannot have a casual conversation with people right they will record and put it on social media it will become a national news


See

### Speaker 4

should not go on fly side definitely

### Speaker 1

I tell you I mean I just some two three months back I gave a talk somewhere okay Something on philosophy somebody called me and I gave a talk I mean when I was giving a talk I never knew that okay they were recording this and all that These people have recorded and put it on YouTube I mean this thing has become a big thing right People are tweeting it right left and center There are views for it against it and all that Then I had to contact these organizers of the talk and ask


to put a disclaimer saying that the expressions all the expressions are opinions are of the author and has nothing to do with isc these people have put it online no they have they have used my affiliation they have called it oh isc professor says this i mean which is true because i am a professor from isc but my that those are my views not my universitys views some of them can some of them may be politically correct some of them are not politically correct and yeah that might cause


my job also so its very should be very very careful when you talk

### Speaker 4

I think that when you start the classes you should put the same disclaimer

### Speaker 1

No no no this is okay no this is all technical content This is all like you know this is all standard stuff you can quote me saying oh YAC professor said that GAN solves a hadden point problem no problem right


I have no problem with it No IISc professor said that you train a neural network using back propagation Nobody cares It is true Now now if I start making statements like okay you know statements regarding some history philosophy language some sensitive issues If you quote me on that and if you tag IIScs name there its not correct no Its all my opinion and I am entitled to have my having my opinion but I should not be as a government employee I should not be having opinions that


But I should rather not make my opinions public See you saw what happened no recently our Prime Minister went to CGIs home for a festival and it became a big national news

### Speaker 3

Thats the


So there is a video of you sir where youre explaining Ahambra Masmi from sacred games

### Speaker 1

Yeah thats what Im saying

### Speaker 4

So so on the same same lines I saw your video on the video

### Speaker 1

No no thats a thats a thats a rabbit hole please dont start that okay so let me stop

### Speaker 4

So I I want to like ask you like how like how
