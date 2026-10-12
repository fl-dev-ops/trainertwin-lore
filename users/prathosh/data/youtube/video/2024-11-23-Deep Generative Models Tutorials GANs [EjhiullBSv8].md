---
id: EjhiullBSv8
title: Deep Generative Models Tutorials GANs
url: https://www.youtube.com/watch?v=EjhiullBSv8
date: '2024-11-23'
duration: 00:57:26
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

We have to ask some more questions here we spoke about the triple of hundred

### Speaker 2

Okay thanks Somebody has recorded the recording Okay good So so okay I came to know from Shujaaz that you wanted some specific questions from the quiz to be resolved Is that the case or what what Im open for the whatever discussion you want to have we can have


Im actually open for the day


So we will go ahead with the quiz questions There were some questions from the quiz that Soha has told that you had some queries Let me go ahead with that


Which quiz we will start Well start quiz four


The latest one or you want quiz two


Which one you want


a leader


Option do you want to start with quiz four or you want to start with quiz two


Guys come on its a tutorial you should interact something

### Speaker 3

One additional thing Sohas had told is he would share the question papers of the quiz

### Speaker 2

Youre welcome

### Speaker 3

So right now its not accessible to us because that test we can only attempt it once Once you attempt it you cant open the link again So he said hed shared the PDF of the quiz at least if not the actual submission

### Speaker 2

Okay I was not knowing that


Yes we may and then so you want quiz twos questions

### Speaker 3

No we dont have the questions from any quiz so whichever possible are

### Speaker 2

So okay what Okay you dont tell me anything on that Okay now there were four quizzes What Ill do is Ill put all the quiz questions together into one single PDF and then Ill send it to you That would be comfortable

### Speaker 3

Yes yes uh thank you

### Speaker 2

Okay good okay so now


Let me take the what do you call thing and then let me go ahead with quiz two risk quiz two risk quiz


the GM quiz


Uh quiz two you had a question with the last one


Here is a question okay which is two questions I am doing


was true


The question is the generator


In a gun


receives a


people


Nice


around which distribution


Can somebody try to answer this question any any any guesses


I cannot leave


uh the answer directly


Not a question

### Speaker 3

Not a question

### Speaker 2

Okay how does how does okay let me ask this question uh in a simple way how does a GAN works

### Speaker 4

Chandan I think the question was in the original formulation which distribution was used And I think there was a confusion whether the original formulation refers to uniform distribution or Gaussian distribution

### Speaker 2

It was from Gaussian distribution right

### Speaker 4

I think thats where the confusion was because someone said that in the paper it mentions uniform

### Speaker 2

okay no its Gaussian on that day I clarified the specific doubt right no no it is Gaussian distribution


I explicitly remember classifying that doubt okay okay


So okay I I thought you have problem with the formulation okay I was not knowing that the problem was something else okay let me go ahead and


Up


this summer

### Speaker 1

And then I have one question


So for todays tutorial the agenda is the discussion of queries right

### Speaker 2

Okay see that is what people Suha said that people want So I just want to go ahead and discuss the questions So whatever you have

### Speaker 4

I think we did that already in the last time

### Speaker 2

Youre done with all the questions

### Speaker 4

Youre done with all the questions

### Speaker 3

Yeah almost all are done except for few outliers I think that can be posted in channel and we can just get the answers I think we can use this for solving any other thing

### Speaker 4

Almost all are done except


for solving any other things

### Speaker 2

See that that is that see that was my initial question okay my initial question was that


See these things can be exactly as you rightly pointed these things can be posted and you you can get it clarified in the chat and


And even what do you call it Let me put it like this The questions were pretty straightforward right You felt that it is did you okay let me ask this question like this Did you feel that the questions are tera meta something like that

### Speaker 4

I think that we already noted those three or four questions where there was a confusion


Yeah I think that was already noted by Sohas


Maybe specifically those questions we could clarify maybe either today or maybe offline in the chat as well So that that thats also fine

### Speaker 2

So now were


Okay


And then what would be the

### Speaker 4

I mean one topic that we had raised was uh due uh in the assignments right

### Speaker 2

Port Collins


Like we did not talk in detail I believe during the classes at least thats my perception

### Speaker 4

We did not

### Speaker 2

uh regarding the mode collapse and all those things

### Speaker 3

Ah is that uh if if it can be discussed

### Speaker 4

Can we can we discuss

### Speaker 2

Sorry Ragavendra you were saying something I interrupted

### Speaker 4

Oh yeah that was the same thing So I mean from the experiences we had with our assignments right we observed different things So we wanted to I mean one of the most important things

### Speaker 2

Okay go ahead

### Speaker 4

And maybe we can pro probably start with the motor collapse itself

### Speaker 2

Maybe we can prov

### Speaker 4

like what is it and how do we really see the symptoms of it in the in the training

### Speaker 1

Uh okay let me discuss with more collabs then


Ill not uh so Ill give you briefly a a small idea of what is mode collapse


or mode collapse lets go ahead with that


So now


Did you see in your output that the generation of images that is happening is very limited


Will you observe that specific phenomena

### Speaker 4

Yes we did

### Speaker 1

So now why is that did you did you try to do anything because of that

### Speaker 4

No I mean one thing that at least I was not very sure of was in which scenario it was actually leading to a mode collapse so if you look at the generator and the discriminator losses right

### Speaker 1

I that

### Speaker 4

If you can figure it out

### Speaker 1

that that how you come but my point is did you observe more collapse in your experiments is the first question

### Speaker 4

Yes we did So for example the samples that we generated right many of them look very similar

### Speaker 1

So its in


issue in training GANs


So where

### Speaker 2

where generator learns


produce


Only limited variety of outputs

### Speaker 1

Limited da


the radio outputs


as observed him as uh


observed in your assignment


Okay now how does it happens now basically uh


It will it will it in this sense is generator it will ignore


ignore certain regions


regions or to be more specific certain modes


So it can modes


of that


data distribution


This is the first idea of the thing


So now now let me

### Speaker 4

And by modes you mean the modes of the data distribution or

### Speaker 1

Yes yes yes

### Speaker 4

Okay so i

### Speaker 1

Right right

### Speaker 4

So it it tries to only uh learn those modes or certain modes are ignored I mean


Okay so for instance if the data say just to take an example if the data has like 20 modes it will only pick something like five or six

### Speaker 1

will only five or six that is the reason why youre not hitting some varieties

### Speaker 2

So ten then one question

### Speaker 1

What a kid Yes go ahead

### Speaker 2

we shouldnt be correlating modes and the classes right like the like lets say in animal data set we had some good number of classes of animals like different different varieties of animals so we should not be considering a mode as a particular class of animals right

### Speaker 1

We dont know the data distribution like that right We cannot say that it might be or it might not be Even see okay let me take this Now take a standard GMM okay the mixture of Gaussians So what is happening is you are just learning one particular mode You are not looking into the variety of the modes Okay now we dont know so whether what do you call one animal for example lets take animal A Okay so how is its distribution


Is the animal A learned fully because of which BC are not able are being ignored or A is partially ignored or B is also partially ignored we dont know that as we as we know that the training is pretty complex process we dont know where it will lead to right okay with me till now


Okay good


So now let me write some notations again so


Now what is this


Sorry wrong notation again


g of z and this is the generator


Maps


Sample Z


Latent distribution


E z of z


Generated data distribution


So now this the generated data distribution should match


Should match them


Through data distribution correct


Oh I should use X here


So this this makes sense This you are able to get the first point


Is this point clear Okay this is the standard idea okay


See okay okay okay again I dont know whether sorry is there or not again every time I tell you the same thing sometimes I use different notation so I always first write to put my notations and then go ahead okay now then you have discriminator D of X


is


a strain to


Distinguish between


real data


Real data samples to be more specific real data samples from which distribution


From which distribution


examples one


In this case can you tell me what will be the objective

### Speaker 4

Classify real as real and fake as fake

### Speaker 1

Correct no no no what will be the objective function


How does uh it works What will be the objective function of this GAN

### Speaker 4

Reduce the cable divergence between


Data and PSR

### Speaker 1

Okay


Okay that is true How do you put it through How do you write it as a min max game


How do you write it

### Speaker 3

Maximize with respect to theta minimize with respect to

### Speaker 1

Okay you can now So minimize with respect to which which thing Do you want to minimize with respect to generator or you want to minimize with respect to discriminator weights

### Speaker 2

It is with respect to the generator

### Speaker 4

with respect to the generator

### Speaker 1

Yes minimize with respect to the generator Okay then maximize with respect to

### Speaker 2

In the respect to respect to discriminator

### Speaker 4

Discriminator

### Speaker 1

Discriminator okay and then


expectation of


Sampled from which distribution


data what do you what is the thing

### Speaker 4

Log of D of X


Logarithmic

### Speaker 1

Or speculation

### Speaker 4

N minus D of G of Z

### Speaker 1

Correct This is from which distribution See always remember okay dont always always remember this is a this is small trick that I have learnt No always no write which distribution


Okay otherwise you will really get confused which distribution youll get


And then here what I should write


Logo

### Speaker 4

Log of and minus

### Speaker 1

Be off

### Speaker 4

Youll see

### Speaker 1

video


So now


Ew


Now what do you think will happen


Oh fine let me go ahead with the next step


The one thing that happens is


Now the generator so let me use G the generator learns


distribution

### Speaker 2

Through data distribution

### Speaker 1

Which distribution generator should learn

### Speaker 2

True data distribution

### Speaker 1

No generator should run PG


And that should match with the true distribution


Okay are you with me


With me on that is it clear

### Speaker 2

Yes

### Speaker 1

Generator should learn pg of x


Now what will happen is


support on


Very limited


Very limited


subset of


Moods of


data of X now is it clear what is happening


And what it what what will be the outcome of this


Now if this case happens if the generator learns with the support of limited nodes of p data now what will happen


Now it has only learned okay so okay you know the idea of support right

### Speaker 2

No please elaborate on that as well a bit

### Speaker 1

Please elaborate


Okay what is the support for Gaussian

### Speaker 2

Standard deviation

### Speaker 3

Minus infinity to infinity

### Speaker 1

Infinity to infinity correct now support in the sense what is the values that it takes


Okay so now what has happened with me So is the idea of support clear

### Speaker 3

is basically range is support range

### Speaker 1

Yes


Okay so now what happens is that the

### Speaker 2

No sorry the Gaussian distribution the domain is minus infinity to infinity but the range is 0 to 1

### Speaker 1

Or should it be


Oh yeah yeah sorry sorry sorry yeah


Correct correct sorry sorry my bad my bad

### Speaker 2

So when you when we say support do we mean the range here or the domain

### Speaker 1

Okay uh support basically means


Let me write that


Support basically means


set up all possible


values


Back up


Random variable can you feel it there are many things

### Speaker 2

Antique

### Speaker 1

So now now what has now does this statement make sense Now the generator has learned the distribution PG with support on very limited subset of modes See if you have modes like this it has only learned the support of this


If your mode is like this it has only learned like this Now because of which what happens What will be the outcome of this


This is what I should do what will be the outcome of this limited support learning


Therefore G produces what


What is the input for G


G produces


Similar output


different values of z


Make sense Is this clear


Okay any any questions here No questions on this

### Speaker 2

So what do we mean by the modes here like limited subset of modes of p data

### Speaker 1

Okay well sir did not do GMMs I think he hasnt done GMMs correct okay uh this is the one question

### Speaker 3

one question so c is the set of all possible values that random variable can take um then you mentioned uh produce it produces similar output for different values so that when c is large and c is small or is there any

### Speaker 1

No what okay okay sorry that is not C that is I have just put it in a bracket

### Speaker 3

Oh oh okay okay

### Speaker 1

Sorry my bad


Okay I just wanted to write what is supported


Okay again dont think this I have put colon and then it is a function


So now in this case okay now now can you understand what will be the role of discriminator in this case If this happens now what will happen in discriminator


What will what will be the role of what even if this is the case if this is the way in which the learning has happened now what will happen in the case of a discriminator

### Speaker 2

For a given output discriminator was classifying either as a real or as a fake for different values of Z the response will be same like since the output is similar

### Speaker 1

So now now because of this what will happen is the discriminator


Then


Easily


Distinguish between


These modes


And


and regions where


Does this make sense


This is a direct outcome of this


Does this make sense in uh


The discriminator case


Okay what does discriminator should do

### Speaker 2

It should be able to accurately classify between a real and a fake

### Speaker 1

So now if it has learned very well the distribution on selected modes then what will happen to the discriminator in that case

### Speaker 2

It wont be able to distinguish between the true and the false

### Speaker 1

No because of which what will happen


Just one

### Speaker 2

Just one


Discriminator will fail

### Speaker 1

Okay think of it in terms of gradient signal what will happen in terms of gradient signal


What will be the gradient signal in that case


What will happen to the gradient signal

### Speaker 4

The gradient will reduce

### Speaker 1

No no no no gradient will reduce in which regions


Correct gradient correct clear correct gradient will be reduced in which regions


Reducing the sense it takes very small values

### Speaker 4

are not so common I mean the ones which in the

### Speaker 1

In the modes which


in the modes which it hasnt learnt


So therefore the gradient signal

### Speaker 2

So how comes this like gradient signal uh gradient signals are reducing for those modes which are not learned


If it is if the discriminator is not is failing for the learned modes then


It is not

### Speaker 1

Go on go on

### Speaker 2

then it is not able to uh you know like the the loss function will be less right

### Speaker 1

The loss function will be less


So if loss function is less what will be the outcome

### Speaker 2

So that if loss function is less that means uh so it is telling the generator that no you have what you have learned is correct Like you dont need to you know

### Speaker 1

You know what will be the outcome if if okay if loss function value takes a lesser value what will be the outcome in terms of gradient

### Speaker 2

It will be lesser

### Speaker 1

Answers your question

### Speaker 2

But why for those modes which are not learnt it will be for those modes which are learnt


Like Im not sure if it is the correct interpretation but

### Speaker 1

Okay so now tell me there are two kinds of modes now


Okay so now for okay lets take that there are two modes okay mode a


mode B So this is learnt


not learned


Now tell me out of these two which will have the stronger value of gradient and which will have the weaker value of gradient

### Speaker 2

Mode A should have a weaker value

### Speaker 1

One


vector value


Stronger value makes total sense right


So now what is the solution for this


You know the you already know the solution for this This is the problem Okay So now because of which the learning is not happening properly because of which the outcome is what you are getting Now why is this happening It is pretty much clear for us now Now tell me what will be the solution for this


You already know the solution I know that


What will be the solution

### Speaker 4

Dont learn the discriminator uh with each


or learn the uh generator more often than the disc

### Speaker 1

Which divergence you use in WGAN

### Speaker 2

Distance metric

### Speaker 1

Which divergence you used here

### Speaker 2

divergent

### Speaker 4

It is J S

### Speaker 1

Which is this

### Speaker 4

um for the new game

### Speaker 1

So now you use the Versus time Gantt so the problem is solved


Okay and that is the reason why people dont go ahead with the regular GAN Make sense now

### Speaker 4

But Chidan one question I mean in which scenarios do we get into mode I mean is this is it like see okay okay this is not in our hands

### Speaker 1

See okay okay no that is not in our hand no no that is not in our hand


Okay it is not like okay you do this you go into mode collapse you do this well not go into mode collapse It is the problem with the learning We dont know how it will go right How can we know that

### Speaker 3

Uh yeah

### Speaker 4

And the discriminators too weak


Yeah yeah correct I mean that was also one of the question in the quiz I suppose that if the discriminator becomes too strong early enough then what happens

### Speaker 1

okay what happens if discriminators too strong okay go ahead what will happen


You have the equation in front of you go ahead if discriminators is very strong what will be the outcome


Which okay which quiz was this question okay Let me look at let me go back to the quiz so that I

### Speaker 4

Like can only I suppose

### Speaker 1

Something done


Yes


This druma


In that the question was in the context of grand uh GAN training when does the mode collapse refers to Now the generator produces identical samples uh regardless of input noise is the answer


What else was there

### Speaker 4

I think somewhere there was one mention that discriminator is too strong early then what happens or this was one of the option where it says that the discriminator is too strong in the early in the training

### Speaker 1

Okay okay okay okay

### Speaker 2

And then maybe uh

### Speaker 1

Okay in case of GAN which of the following condition leads to unstable training That is the question Yeah there was someone was saying something Yeah

### Speaker 2

Yeah


Yeah maybe before the next quiz if you can you know open the quiz for review for all of us so we can have we can you know pick up the questions and then ask Otherwise its been a long time when we dont remember the exact questions

### Speaker 1

Makes sense makes sense Yeah sure See the thing is you know what will happen is okay we should have given you the PDF That is not done Ill look into it myself Okay We cannot open the quiz once it is closed Then we will have all possible problems in our end backend So thats the reason why we close the quiz Okay It is not like we want to do it Okay So now

### Speaker 3

In some of the other subjects at least we were able to see what we had marked and what like which questions we got wrong after the quiz


So maybe theres some option

### Speaker 1

Maybe theres some option


That you are not able to see Okay let me look into it

### Speaker 2

Thats what I meant by review

### Speaker 1

At least we can see

### Speaker 2

At least we can see

### Speaker 1

Just leave me a minute Im just looking into it


And one thing that I feel we can do is you just before in the student group you just put what are the questions that you have okay so that these kinds of logistic issues we dont want to all the logistic issue just put it in the chat somewhere somewhere in some place so that we dont need to look at these issues when having the tutorial okay


Now you are able to see quiz two at least


Go ahead and check in your uh this thing


Yeah and then we are able to see Whos poo you are able to see now right

### Speaker 3

Quiz three

### Speaker 1

Yeah it will come now it will it will come now

### Speaker 3

It will come now it will it will come now

### Speaker 1

is two you are not able to see okay just refresh it you should be able to do it okay Im just doing the same thing


And uh one more thing okay Ill put it in the channel so you will have uh next two weeks continuous quiz or both the weeks you will have quiz


Okay quiz five and quiz six so we will do it in a continuous manner okay


Now youre able to see all the clues

### Speaker 2

Yes

### Speaker 1

Problem solved Okay Yes go ahead So now we are looking into the quiz 2 question In the case of GANS which of the following conditions can lead to unstable training


Okay lets look at the options


So lets use the idea of elimination Thats the best idea to use in quiz Lets take one So when proper balance is there between generator and discriminator what do you mean by proper balance between generator and discriminator What does that option even mean


What will happen in in the training process in that case


Forgotten Gans already Since youre in diffusions you have already forgotten Gans


Using VersaScience distance instead of JS divergence will it have any problem in training


With this current discussion are you convinced that if you use okay at least Jensens channel divergence will not work

### Speaker 3

Chandan I have a basic question so what do we mean by stability of train

### Speaker 1

Yeah


What do you mean


Stability of training is that your uh what do you call your gap okay okay in lets take in terms of classification what do you mean by stability of training


If if training is done properly what do you mean by that in terms of classification and see in in any any in any model or in regression for that matter

### Speaker 3

I mean the loss the way I understand this may is could be like that the loss is continuously decreasing its not uh

### Speaker 1

Creating

### Speaker 4

or its not increasing

### Speaker 1

or decreasing because what what what will be the outcome of loss decreasing

### Speaker 3

That means your accuracy is increasing at least in the classification

### Speaker 1

What do you mean by that


Your model has learned product

### Speaker 4

Thats right

### Speaker 1

But our accuracy is it has learnt what it needs to learn that is what we mean by stable training

### Speaker 4

But accuracy is

### Speaker 1

Okay now tell me what do you mean by stable training in terms of GANs Extend the same idea

### Speaker 3

the generator is learning or learning the data distribution

### Speaker 1

And is that the only thing

### Speaker 3

to distinguish between real stuff

### Speaker 1

So now then both of them does this mean that both of them are in balance now

### Speaker 3

I mean its its so its its a min max uh game right so

### Speaker 1

Correct correct when did when did you okay okay good point good point when do you say that so also have a check on that

### Speaker 3

Do you want to go first


So so also one question I have is one question I have is in the GAN training right in

### Speaker 4

Initially should the generator be strong or the discriminator be strong

### Speaker 1

What do you mean by initially the generator should be strong

### Speaker 4

the beginning because if the discriminator is too strong the generator doesnt get good feedback right

### Speaker 1

Oh both of them are okay both the losses initialized with random weights its a min max game they will come to an optimal point there is nothing like see youre not like first generate first you are learning the generator then youre learning the discriminator its not like that right

### Speaker 4

But doesnt it make both of them okay both the losses could be lost

### Speaker 1

The lights not like that are they

### Speaker 4

Its not like that right But but but if the discriminator is strong initially itself right That means it would not send back a good gradient for the generator to improve upon correct

### Speaker 1

Does that answer the question that you have in the quiz

### Speaker 4

Yes kind of but the the point is

### Speaker 1

Correct you are correct sir So is it a stable training then No no one minute Is it a stable training then

### Speaker 3

No I mean

### Speaker 1

Yeah the

### Speaker 3

get a chance to really

### Speaker 1

Is it stable training in that case

### Speaker 4

Uh is it always stable training then


Yeah but its also not its also not a stable training if say for example generator is too strong initially and the discriminator is not right

### Speaker 1

Im taking all that off


No no okay okay what do you mean by generator being strong

### Speaker 4

Its able to generate real quite good images in the beginning itself and at that same point of time the discriminator is not able to identify I mean is

### Speaker 1

So whats the outcome of that

### Speaker 4

Its a banana

### Speaker 1

The generator okay I understand what do you mean by generator is strong

### Speaker 4

The generator Okay I understand what do you mean by generator

### Speaker 1

What will be the outcome of generator being strong

### Speaker 4

And working with the open source community


Yeah the discriminator gives wrong feedback

### Speaker 1

Okay

### Speaker 4

because discriminator is not strong enough yet

### Speaker 1

Okay

### Speaker 4

Even this is a uh uh I mean not a balanced training right


I mean would you would you call this unstable

### Speaker 1

I got your point I got your point l let me let me think through it


How to say that okay


See that is what we want right in a way Okay now okay at a stable training what do we want the discriminator to do


Post training if your training has happened properly what do we want the discriminator to do

### Speaker 3

It has to tell you what is real and what is fake

### Speaker 1

Im sorry


So what should be the probability What should be the probability of real example Correct

### Speaker 4

Probably

### Speaker 1

So so it should be in an equilibrium state So you should get 0 point 5 as the outcome of the discriminator correct Is that the first point clear Okay So now if if the generator is strong that means that it is generating good images what will be the outcome of that on the discriminator

### Speaker 4

But at that point of time the discriminator hasnt learned good enough So it may be giving you saying that okay uh


is not able to distinguish correctly right So it may it may tell you whether it is real or it may tell you it is fake But it has not learnt good enough at that point of time

### Speaker 1

Oh


Okay your point is that there are two answers for this question

### Speaker 4

No what I dont understand is what is really the problem in this case

### Speaker 1

I got that one


Oh their balance is

### Speaker 4

balance which is who should who should who should be learning faster or who should be

### Speaker 1

Oh dear

### Speaker 4

Dancing still over there

### Speaker 1

There is nothing there is nothing like that who should be learning faster and who should be learning slower now both of them will reach an equilibrium that is what we want okay we dont want one to become stronger than the other

### Speaker 4

And since we are training both of them simultaneously


We dont I mean we are not training both of them uh separately we are training them simultaneously

### Speaker 1

Yeah so both of them are learning

### Speaker 4

So both of them are learning at at a particular rate

### Speaker 1

Which rate is it

### Speaker 4

Well and which rate is ideal

### Speaker 1

Oh there is nothing like that is my point


you can really see that is the reason okay why do you think that people went to diffusions

### Speaker 4

No we we understand the problem we generated okay its very hard to believe

### Speaker 1

Okay its very hard to believe Yes these are the problems Yes as you rightly pointed yes Ill look into these answers because even if generator is strong so you will okay generator is strong so okay Im not able to convince myself that if generator is strong that makes it discriminated to be weak That argument I somehow Im not able to get it Let me mull over it okay And then so somehow somehow I personally feel that generator is strong

### Speaker 3

Yeah and even in the in the questions right I mean so so when when we are get such a question its it was at least very very difficult for me to understand

### Speaker 4

What do we mean by stable

### Speaker 1

What is totally fine Okay okay stable okay stable now you understood what is stable

### Speaker 4

Uh not fully because I dont know uh see

### Speaker 1

See stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training is stable training

### Speaker 4

Is it unsaveable or is it saveable


But then that can all be at the beginning right that that can all be

### Speaker 1

No no no no no no no no no no stable training is once youre done with the training


When you have when you have achieved that okay did he tell about Nash equilibrium right when you have achieved that Nash equilibrium or equilibrium for that matter


Okay now that is when you say that training is done Okay so now the question here is no we want discriminator to give me 0 point 5 because of the generated even if I generate an image that should give me 0 point 5 is what we should learn there Now that is what I mean by stable training in terms of discriminator In terms of generator what do I mean by stable training is it is able to generate samples in as per all the modes Okay so that at least it


its generation is proper that is that is what i i mean by stable training now that means that it has learned proper weight now overall that is a uh uh view that ill tell you okay so now okay uh here as per your uh you have rightly pointed so generator also becomes strong uh because i havent given a counter example that so and uh discriminator about any discriminator i havent told okay thats something that we need to which which ill look into it no problem


So now there is and then the remaining things are clear So proper balance between generator and discriminator is what we mean by stable training And then using versus and distance instead of J as distance yes it will give us this balance So those two have to be eliminated Now these two I have so I have given the answer as discriminator taking discriminator becoming too strong Okay I havent given the answer of generator becoming too strong Let me mull over


and Ill Ill let you know no problem okay


Does that answer your question At least partially

### Speaker 3

Chandan we also had a question on like so what are the ideal curves we should expect for loss when we are training some kind of a

### Speaker 1

Oh ideal some kind of a review no not ideal

### Speaker 4

The loss curves and the curves of the loss so that we know whether the training is going good or not

### Speaker 1

No where did I get this question No where did we have this question

### Speaker 4

No not the question its not a question

### Speaker 1

Okay okay okay fine fine

### Speaker 3

from our assignments right I mean whatever we tried whether that was as expected or not I mean we also dont get that feedback thats why

### Speaker 1

Hey go and check in internet café


Its a its a very straightforward question Ill leave it Okay You dont Okay Uh what Okay


So now when you say ideal curve now tell me what is there in x axis and what is there in y axis at the first point


I just want okay uh okay the reason why I ask so many questions is I want to know the point was

### Speaker 4

The point was what we saw was the loss was reducing but there was the generation was never good

### Speaker 3

Right so

### Speaker 1

What do you what did the generation was not good

### Speaker 4

One of the

### Speaker 3

With the transition

### Speaker 1

The generation not good in the sense you are generating from the same modes or the cl the generation quality was not good

### Speaker 4

In the sense you are generating

### Speaker 3

Generation quality

### Speaker 1

So thats a good thing

### Speaker 4

So so when you look at the generated images

### Speaker 1

See it is reducing the loss is reducing but it should reduce even further that is what it means

### Speaker 4

Yeah it is a reducing


Yeah it was planned yes I mean it was

### Speaker 1

Which data set


No that we are stuck in local minima thats all

### Speaker 4

That we are stuck in local minimum

### Speaker 1

That means we have stuck with local unit


Use something like simulated annealing and other things to come out of it That would be a nice idea

### Speaker 2

Come again what what can we use

### Speaker 1

Simulate run the link


Theres an idea called a simulated tunneling that will help you if you are stuck in local minimum that will help you out Have you okay are you using okay what are the hyperparameters Okay in the sense okay what are the things that you are using


So okay what are the things that you are using in your code


Okay okay let me let me put it like this How do you okay which


How do you uh what do you call optimize

### Speaker 4

I mean the learning rate you are asking about and which optimizer we are using

### Speaker 1

And are you doing anything else apart from that

### Speaker 4

I mean at least we did not try anything more different


The standard Adam optimizer and we played around with learning rates but we couldnt get much improvement

### Speaker 1

Have you done standard CNN videos

### Speaker 4

And I also tried


As part of this DGM course itself yes but not before

### Speaker 1

Do you know something called as learning rateschedulers


just okay just okay Ill be back in a minute just just give me two minutes Ill be back just just give me two minutes


Have you okay my question was have you used the schedulers and learning that schedulers in your codes


Use it it will help you


We discussed about learning that scheduler right I I remember me I only telling you


Use learning rate schedulers will really


Data See this is like see


Uh let me be uh see the neural network training no even smart small things like this will give you a lot of uh boom in your uh results


So use a learning rate scheduler that will really help you Youre using all those DKs and other things in Adam


Or what is optimizer that youre using

### Speaker 4

So Adam was the one which we used

### Speaker 1

Are you using all those BKs and other things


beta and other things


You just give learning rate thats all what is the learning rate that you are using

### Speaker 4

I have one e to the power of minus minus five

### Speaker 1

okay dont start with so much okay so this is the problem we always know start with 10 to the power of minus 3 or 10 to the power of minus 4 and use schedulers so that it and use uh proper weight decays and other things so that the learning rate will gradually reduce okay dont use as a small learning rate in any any of the training that uses any images okay see i can understand if you had enough resources you would have tried and tested all these things okay so


some of the tricks of the trade you just go through any of the you youre okay while okay so okay any other okay uh can i stop uh the recording

### Speaker 4

Yeah sure
