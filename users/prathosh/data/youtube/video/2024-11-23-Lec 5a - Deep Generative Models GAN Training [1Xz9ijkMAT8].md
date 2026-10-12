---
id: 1Xz9ijkMAT8
title: Lec 5a - Deep Generative Models GAN Training
url: https://www.youtube.com/watch?v=1Xz9ijkMAT8
date: '2024-11-23'
duration: 01:02:15
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

of of f can okay which will get us to the the basic or the manila gann article of the gann model that generally people use so if your generator function or the f function in the f divergence happens to be of this particular form okay the corresponding divergence measure is called the f divergence sorry sorry sorry jensen channel divergence okay now in that case the


Okay


The loss function will take this particular form Let me write that So the cost


or the above case


The cost function


What was that recall that let us denote that with some


G of


theta comma w its a function of theta and w what was that it was expectation of p of x right as x comes from bx minus expectation of


Its start off


Its good


as x cap comes from theta right this was our cost function in general now if you take this f right and plug it in here


See in the FGN paper right they have given the F and the corresponding F stars I will show you that so if you use that and do that for this particular case this will be equal to the expectation of


as coming from px log of


I think this is TW


Log of d w of x


I mean this


Expectation of X cap coming from P theta


log of one minus


W of X


where dw dw x is simply the 1 by 1 plus e power minus dw of x


It is simply sigma of T w of h


So I mean if you uh maybe we will make this uh


item in the ta session and as i said please note take a note of what all to be done in the ta session and you should ask chandran to do that okay so what is to be done is that you take this f divergence and you take the corresponding f star and you plug in that f divergence here in this equation and if you simplify the algebra you will get this cost function this way


Okay where instead of T W you just represent another function T W which is simply you take the T T W and put a sigmoid at the output of it okay which is Ill write that So now what happens is that you have a network


T theta of Z


that would take a VS input


Arma 0 1 and youll get X cap


It is coming from P G D


And to have another network which would give us the lower bound lower bound


be called as the pw of x right x or x cap here sorry this should be x cap


dw of x cap so this network is simply


what we were writing as T network


small c one here


one so this is this entire thing is D and yeah


This was T and you have a sigmoid on top of it And you get what Because it is a sigmoid now you get a number that is between 0 and 1 So this is only for the case where your F divergence has this particular form


So this if you see if you if you if you can notice this is the the last function


Oh fuck


Naive GAN isnt it If your people have seen that if you look at the blog post and all that they would say that this is the loss function of a GAN It actually comes from here that you I mean this is the usual M divergence mean minimizer the loss function that we have And for that if you plug in that particular F star I will show you that paper If you have a paper you will understand Ive done that in my notes also Just have a look at it I will share my screen


You see my screen

### Speaker 2

Not in the house sir

### Speaker 1

You see it now

### Speaker 2

Yeah Yes sir Yes sir

### Speaker 1

Okay this is that FGN paper right which actually I taught so far Now all this M divergence et cetera So look at this table Now in this table what they have done no they have given different divergences and the different F functions corresponding to those divergences and the corresponding T functions optimal T functions And for Gyan right which is the naive Gyan this is what is the generator function Okay now they have skipped the algebra I think Ive done it in my notes or you can ask


you can ask them to do it so now with this particular look at this now with particular divergence metric your output activation function which i just said now that on the output of the t function if you put an activation that would change it is simply expressing the t function in a different way


right so so finally this objective you know which is the objective function of a GAN that would happen under this particular f divergence so if you take a different f divergence lets say if you take the Pearsons chi squared distance uh or the different f function uh instead of GANs f divergence a Jensens channel divergence then you would have a different uh different loss function basically right all you have to do is just plug that in


I will show you the corresponding yeah f star also you see this no so these many divergence metrics are there no and you have the output activation function which is just the appending that you do on the t network because why should you do this output activation function it is because if you recall the t function is designed in such a way that its output comes from the domain of f star right for the corresponding active corresponding f divergence that you choose


You will have to choose your f function in such a way that it would respect domain of f star That is why you should have another activation at the output of the dL function That is why you have an activation You have the corresponding conjugate function also f star So what you should do is once you pick an f you get an f star you plug in that f star and you adjust for the output activation you get the new loss function for that f divergence


Is that clear So that is how you get the you get the loss function for the naive GAN So they choose in fact somebody was asking at the beginning of the session right did they start with this math and come back No that is not how they did In the original GAN paper they write this loss function in a different I mean from a different motivation I will tell you that motivation also It is not mathematically grounded but this paper at F divergence it creates that GAN class where in


also becomes a member okay so did all of you get how we got from the uh the loss function of the f gann or rather f divergences to this particular instantiation its simply as i said no we have defined a class a gann class from the gann class uh we got one instantiation with this f of u becoming tension chain and divergence


Uh any questions on this Yeah okay

### Speaker 3

Section


zero like in this Janshan diversion

### Speaker 1

Yeah it is no no f of no its not I think we corrected that no it should be in f of let me just see that f of zero is one

### Speaker 4

I think the second term should be here in uh log of u plus 1 by 2

### Speaker 1

done let me just see that did I make a mistake here


Oh thats correct


It forth won this seedling

### Speaker 3

Yeah but uh FF1 doesnt evaluate to zero with this equation doesnt evaluate to zero here

### Speaker 1

It evaluates to what that is 0 this is log 2 which is evaluate to 2 log 2 right

### Speaker 3

Yeah


Yeah

### Speaker 2

It was u plus one half

### Speaker 1

u plus one by four two

### Speaker 2

it is u plus 1 by 2 in the uh original expression so if it is u plus 1 by 2 then it will evaluate to 0

### Speaker 1

No but there is no u plus 1 by 2 in this generator function in place Okay so fine I can put it u plus 1 by 2 thats also convex that will evaluate to 1 more than that case

### Speaker 3

Yeah

### Speaker 1

Lets see if I can write it


See okay so I Ill tell you where this thing is see the the GANs loss function that they use no its not a proper f divergence in the sense that it is off by f divergence by that you know 2 log 2 factor


Do you understand So thats why you are getting that term


Divide that by two it become proper Jensens and a divergence that will become uh that Ganns objective


So it is off by that uh that factor uh 2 log 2


Yeah

### Speaker 4

Sir can you please repeat why you said that we need this final activation of sigmoid This is because

### Speaker 1

Huh this is because yeah this is this is because


this is because uh the t function that we the way we define now the t function we define that what was the d function it was from uh x right the domain of x to the domain of f star


Right So now if you choose a particular f star and f function you have to ensure that your t function has the output that obeys domain of f star

### Speaker 4

Okay and a sigmoid is one or is this the only one

### Speaker 1

Sigma is one for this function


For this function sigmoid is the one that you take


Thats thats big ticket

### Speaker 4

So thats a fixed thats a fixed mapping or for a given function

### Speaker 1

For a given function for a for a given f function it is fixed that is why I showed you in that f f g and paper they have listed the output activation for different f values

### Speaker 4

Okay yeah

### Speaker 1

Yeah in fact its a good point that you made


Because the the output activation for this particular f function happens to be giving you a value between 0 and 1 no the t function in this case can be interpreted as a classifier


you understand that see now because the d function in this case will give you a value between 0 and 1 it can be interpreted as a classifier that is why it is called a discriminator in that case


I mean in general it is its called a critique right I mean it can be anything but in this particular case because it gives you a value between zero and one you can call that a classifier You can interpret that as a classifier another interpretation that I give you Okay


Great Okay so now what we will do is the following we have promised that I will write down the


Gladiators and all that no I mean do that now


Okay let us write the optimization problem now So we have


He does that


and W star


So you need to


it minimize with respect to theta and you have to maximize with respect to w right uh what is that in this case it will be log of


Oh normally I have an expectation there


Can all of you mute please


from px minus


But thank you


was that log of one minus state of due


x cap as x cap is coming from e theta right this is the loss function now we know that we can approximate these using expectations using law of large numbers right so approximating


expectations


Large large numbers


are simply sample estimates


although we do that we have let me write that cost function j theta comma w this is what im


representing as J


the record to uh


I have n samples of data it is one by n


equal to one through n


Long


E W X I


Linus


Its like uh theres much expectation on this one


One by young


J is one through M


log of one minus d w x cap j


X one X two up to X capital N


are coming from PX which is the data


And you have


X one cap X two cap


of to x m cap are coming from p theta which are the


Output of G theta network


Oh how do you get this sample


Z1 through ZM okay from normal distribution


Boston


So


GT tough


So okay


Is it okay So this right now let me call this as J cap because Im taking a sample estimate Okay Now this J cap J cap


Theta can be computed right


Any questions on this


This is pretty important this is what you are going to implement so this J cap can be implemented no


Yeah uh service

### Speaker 4

So so is there a specific reason of choosing NNM different or what like

### Speaker 1

Oh okay

### Speaker 4

Or it can be something

### Speaker 1

Its just batch processing no you thats bad size of training your discriminator and generator you can use any batch size


Okay typically you dont take the entire data set no You do stochastic gradient descent where all of you know what stochastic gradient descent is and then you can then talk about it When you do gradient descent you dont take all data points you just take a subset of data points and you iterate over it So thats what one VPOC means All of you know this no


Okay I have no questions on this and now JCAP can be computed and now how do you train this or training again


Practically


Dont take me wrong but Im just take this in a lighter note


For the person who said that Im paying this much not to learn math I hope Im doing some justice now by telling you how to train GANs practically also That was Please dont take it negatively Its simply a


cleaner light or not okay so now lets see finally how see how to try and again practically right so now what happens is we do it using gradient descent let me write the architecture here


The world has become too sensitive these days so you cant crack jokes


take it too seriously


Im not talking about you in general right so if you crack jokes with your friends and spouses or children or students everybody takes it too seriously

### Speaker 4

Here are the samples of the same population

### Speaker 1

See when I was a student I told you most of you might be younger than me right Im 35 So most of you will be maybe late 20s or early 30s Every five years is a new generation now My teachers used to do all kinds of things for us They used to harass us embarrass us beat us all kinds of things that we never took it seriously But this generation my God


again in one of those feedback somebody wrote not your course somebody wrote that youre just doing your job youre getting paid for what you are doing so theres nothing great about you teaching


I think I realized that okay that is one way to look at this entire thing Im doing my job which is true okay so lets not even do this lets say that he


So this is the


Yeah parents always tell us right that uh and all that imagine if children tell them that uh you just did your job which is also true we never say that quite so


thats how people do it in the west right i mean this happened by the way a a child went to court uh against their parents and the and the case was that uh that uh that he uh he put a case on their parents for having given birth to him


Without his consent


Wow


If I say

### Speaker 2

something like this my parents will slap me first

### Speaker 1

No I think if you dont mind Ill just take two minutes on something that one of my senior colleagues from IIT Delhi told me its a story which which he told

### Speaker 2

Simply share sir simply share

### Speaker 1

So he said that it have see I have so many stories and to say outside of this class the problem is that you know I Its not my job to tell you stories Its my job to teach you to gas Unfortunately anyway so here is how I was having a conversation with one of my very senior colleagues from IIT Delhi He also got a you know some highest national award for sciences professor Bream Singh very prolific senior man is already 65 then when I was there I was a 25 years old kid


when I joined as a faculty then 26 27 years I was talking to him and he narrated a nice incident very funny incident to me he said he has a collaborator uh from some university in Canada hes an Indian guy Punjabi guy okay now what had happened is this professor in Canada he had gone to university for work and like that professors son who was 10 12 years old


He was left in home with his grandfather grandchildren sorry grandparents who is this professors father and mother okay parents now this grandfather scolded that Buddha okay did something and this grandchild who was born and brought up in Canada he lodged a complaint against his own grandfather and in those countries you know my own sister stays in Sweden and it is it is a true thing


that if a child goes to police and complains against their parents the children is just taken away Okay Parents are penalized under law and children are taken away put into some government looked facility Okay So now this professor comes back home and there is police there interrogating his parents So what had happened and all that So then he somehow managed and this kid has complained basically you know he said that my grandfather abuses me and all that So then


uh he this professor somehow managed so a few months later the entire family visits india okay uh for for vacation maybe my my colleague professor bhimsingh exaggerated this but the way he told me is the moment that they touched down uh india right uh this uh this professor starting uh hitting that kid in the airport itself so a few


policeman came to came to came to this professor and asked him why are you beating your child so this professor narrated that entire incident that policeman said that

### Speaker 2

It is possible sir it is definitely possible

### Speaker 1

So yeah so I mean thats the cultural difference no I think no that is slowly peeping into our culture as well We should be very careful with our students very careful with our children these days And by the way Indian law also has that and you cannot I mean if you cannot quote unquote abuse your children


See my mother I still remember she used to she used to take these you know I dont know what it is called in English


I dont know see the thing that you that you used to uh uh place hot utensils on top of your stove no what is it called that is I dont know what is it called its a heavy throng kind of a thing that is made in in steel uh I dont actually not even steel so she used to take that and hit me on my knuckles so and that was that was a usual thing you know I never took it offensively if I do it to my chest


I dont know maybe shell go and complain to police

### Speaker 2

Maybe you were unaware of the

### Speaker 3

Thats right

### Speaker 1

What happens

### Speaker 2

I had a geography teacher in my school days and he used to tell me that like all the students that perch who so he used to tell us to like touch your own feet and the moment we used to touch our own feet he used to smack us on our back with a wooden stick so

### Speaker 1

Oh

### Speaker 2

I mean this is very common in our generation but this G and Z its very difficult to unscroll them

### Speaker 1

Exactly Anyway so thats for a different days discussion Lets get back to what we were doing Okay so what will happen is so there is this J cap theta comma W

### Speaker 2

Just one over n


You have a some


Oh no

### Speaker 3

So on total thats uh proper CMR dye drawn for the G data right it is changed usually drawn at

### Speaker 1

Okay

### Speaker 2

Okay I I am NOT following the diagram you you say that they are drawn for the G data of is that usually draw a different required GM right

### Speaker 4

It should be expanding not narrowing

### Speaker 1

Oh sorry sorry sorry


So because the dimensionality of z is much lesser than that of x thank you thats my mistake


So typically right Z comes from

### Speaker 2

some 8 60 32 dimensional space okay when you implement So it is it comes from 32 dimensional Gaussian okay So X is of course X cap is in R D where D is the

### Speaker 1

dimensionality but its an image it is 10 so 10 000 dimensional whatever your data dimension is so this is it and then minus you have 1 over m

### Speaker 2

of one minus is it log always forget that it is log of one minus that okay


See I could have actually written this down and started

### Speaker 1

a GAN discussing GAN with this I dont like that narrative at all because I dont understand where this last function came suddenly right it just appeared out of blue and why should this work and so on I I would I was never convinced I think this is a more principal way of doing it okay now how do we try in that so now we we need theta t plus one so let us look at the


Ill use different colors this is for the lets try in generator training


Okay for generator training what you should do is that you should write theta t plus 1 is equal to theta t minus the gradient of J cap


Okay evaluated at theta p


W T


This with respect to theta


So that is just uh


You can use your favorite optimizer by the way I mean I am simply writing a this thing stochastic gradient descent you can use Adam or RMS prop like is backprop I mean this thing gradient descent with momentum whatever it doesnt matter So so now you get this now how do you do that thats you look at the gradient of JCAP


It is put to T da


is simply look when observe that the first term right here this term is scratch it out


term is independent of theta right its so the gradient becomes zero so the gradient is simply the gradient of


So negative one minus seven


j equal to one through m log of one minus dw


Scuba


j now uh the way i have written no the dependence of theta is not accurate but observe that x cap j okay maybe ill write it explicitly so that it will become easier for you this is


EWF what is this This is T theta Z


So the dependence on theta is uh is apparent so this is


XJ cup its okay so now how do you do that so uh first you do a


Lets write down the forward pass using green So you take this do one forward pass through g theta so you get


xj or g theta of zj okay okay then xi xj cap and pass this


xj cap through dw x i will not write x here because it can take both x or x cap then what do you get the output what you get here is dw of xj cap okay once you get this uh which is okay i will write that as


is also DW of


check app okay then you have this dw of exact app right which is this this term so you can compute the log of it right once you compute the log of it you compute i will write the gradients in in blue so you compute the gradient of this


Logger


One minus DW of XJ cap


and then back propagate that all the way through this it comes like this the gradient and goes all the way through the input so this is which


W fixed


okay so now to do one backward pass through the generator what you have to do is first do a forward pass through the generator get xj cap take that xj cap so this is


Says


I think the timing of the tutorial was perfect So the backdrop was had taught precisely before I wanted to do this That was the intention Okay I hope this is clear Any self explanatory Any questions on this


Does anyone have any questions


Hello am I audible

### Speaker 4

Yes yes yes

### Speaker 2

Is that your name again

### Speaker 1

Yeah okay uh is this clear it should be pretty clear no


Okay now let us do the this is generator training okay Let us do the same thing for similar thing for discriminator training I dont want to clutter it with this I will write another


So can we extend the class by 10 minutes Like because I want to finish this today


Society discriminator training


Pretty discreet about it I reckon


And well do the same thing here


Sister


code pass and use some other colors


Which colours


See some someones suggestions on using different color was really good I never thought about this


It will add one other dimension to


notes okay power up


Whoever suggested thank you so this uh is how the network is


I Barbizonia


Okay thats in my category


We have this C1 up to CM sample from N01 and we have this G theta of Z network and the output is X


have let us


What did I write here I wrote this X1 cap to X1 XI cap


Okay sub gaps and then you have the critique of the discriminant of network


We know that this network can take x or x cap both as input Okay So in this case what did we do We only took x cap through the DW network because we only wanted to compute the second term correct Here we will see that we have to take okay So maybe I will make it concrete Why x here We only take x cap here as input correct In the discriminator training sorry in the generator training


uh only x cap goes for the discriminator so that is perfect okay here both of both will go and this will be a number between zero and


Point one because it has a sigma and a d output fine now j


theta comma w is equal to one over n


is one through n you have log of dw of xi minus one over m j from one through m


Log off


Like this


E w of g theta of c theta


Right now we will look at


signing


des critic


or the discriminator in the case of this particular F divergence So it will be so you dont have to write W O T plus one


This is w t minus some beta times the gradient of same loss function with respect to the theta that you have taken at the tth instant and w that you have taken at the tth instant Thats all So this is how youve tied it Now to find the gradient what you do is


take so note that the output of the discriminator right you need to compute


T okay gradient we are writing like this now we have to compute T


gradients of the first term which is log of T w of x i now how do you do that


Simply take some x is okay so this is x 1 through x n okay pass it through the discriminator


You will get T W of


Okay then you compute this


And then


Back propagate this all the way to the input


Is this okay That is for the first term


Okay so what about second term


For the second term we need to do the following so we need to


Do one forward pass through the generator


Uh this way well get


Now take all these


And passing through the discriminator Oh there is no space here


What do I do


Quickly call this and


Shall I write a copy of discriminator here again

### Speaker 3

But I guess you can create a space

### Speaker 1

I guess you can create a space

### Speaker 3

Like that

### Speaker 1

Help

### Speaker 3

So in top I guess there is double sided arrow right somewhere

### Speaker 2

Perfect

### Speaker 4

Im not going to

### Speaker 1

Yeah left of D

### Speaker 3

Out of rubber yes

### Speaker 1

Here are now here

### Speaker 4

Left left yeah you can go to space

### Speaker 1

Okay I see

### Speaker 4

Click on the hamburger icon

### Speaker 1

Pick this up

### Speaker 3

Its just expensive

### Speaker 4

Its just a pencil

### Speaker 2

Click on where you want to add space and pull it down

### Speaker 1

Oh oh nice


I didnt know this at all


I dont want that to happen


Looks like I cant do it

### Speaker 2

It yeah it will get cuts on entire page gets down

### Speaker 1

Okay so maybe let me do one thing


This I can rewrite no problem

### Speaker 4

So there are different pencils as well


Pencils


So if you are changing same colour colour of same pencil you can use different one

### Speaker 1

How is that

### Speaker 4

So there are already there

### Speaker 1

So here that


Oh you change them to different colors I see and you can add more pencils also yeah okay great thank you very useful tips


Okay yeah this is okay This is one form and pass So now once you get this what you can do is that you take this


and pass through the discriminator I have to write another copy of discriminator here


Its not that big


Please dont Okay if I write it what if you think that there are two discriminators That is what Im worried about


There arent two discriminators theres only one discriminator here


You get this X1 through XM and you take them and okay pass them through the discriminator


Obtain what do you get you get


It will compute


log of one minus dw of g theta zi zj


it compute this and then


Ill propagate


So now in this entire thing like uh I have to write that here See the entire thing here


W is kept


Okay so here


Theta is fixed


Is this clear How do you try and discriminate The discriminator has two terms right I mean both the terms in the loss depends on discriminator because you have dw both here So for the second term its simple You just take samples from x1 through xn pass it through that You get this then compute log of dwxi take the gradient backpropagate thats all To get the second term you start from z1 to zm pass it through the fixed generator you get x1


cap through xm cap take those samples pass them to the discriminator and compute this log of 1 minus dw g theta z j and then back propagate that loss


And see note that backpropagation stops at the input of discriminator because theres a discriminator training The loss do not pass through the generator Here


While the losses pass through the discriminator the weights of the discriminator is not changed


He said okay


So is the now you can code this up right


Tell me this do you need a tutorial on PyTorch like thats what he did in the previous class or did he only do a theory of backdrop

### Speaker 3

The next class is what he said

### Speaker 1

Ah so do you need a tutorial on PyTorch how to do this backpropagation

### Speaker 4

Yes sir

### Speaker 1

Okay so you know thats Ill just put it right away


Yes


If you have any questions on this feel free to ask me

### Speaker 2

You guys are just playing games I dont know


just trying to capture this effectively or digest this

### Speaker 1

You can ask me in the next class no problem


Okay uh sorry maybe I will uh make this

### Speaker 4

Yeah this is Hello

### Speaker 1

Yeah please go through this carefully maybe before coming to the next panel you can ask me questions no problem yeah

### Speaker 4

Yes sir So this Z1 to Zn that we are using which are the first random variable So are these fixed or they could change between the iterations

### Speaker 1

And they can they can they can they can they can change In fact you do batch gradient descent here You dont take m samples You take you dont take all n samples in data You take a subset of it and do it on all possible subsets That is one epoch of gradient descent

### Speaker 3

Okay so for every batch we could generate a new M samples and then run it through

### Speaker 1

That is how you do it yes


13

### Speaker 3

Sir can you explain this discriminator training or the generator training in like intuitive way like not in the mathematical formula what exactly is happening

### Speaker 1

Um


What exactly is happening is that this generator this discriminator is


What do you want to hear Do you want to hear me saying that okay there is this basically whats happening is discriminant is creating that lower bound and generator is trying to minimize it


Okay however for this particular case of Jensen channel divergence rate because this discriminator happens to be a classifier there is one other interpretation that you can give which I will give you next class


But I want to like I deliberately avoided that simply because see I mean this is see this is not restrictive to this particular F divergence Now you take any F divergence the exact same procedure holds Do you see that

### Speaker 3

Correct

### Speaker 1

For this particular where your denominator or the critic that happens to be a classifier there is a there is another interpretation that one can give for this loss function You can actually see this as classification losses These things as classification losses And there is a there is another classification interpretation that one can give Ill do that in the next class Ill start the next class with that Okay


So after next class I will again the end of next week is when I will release the bus assignment I can do it the mid of next week itself I will be asking you to implement the plans basically okay


this is clear please go through this uh todays content


Hey and uh like one of the other comments was that somebody said that uh uh that you know we would choose uh a quality over quantity right uh do you think im covering too much


And it goes

### Speaker 2

Its good sir too much of those

### Speaker 1

No but Im not doing too much in my see I dont like the the in my opinion the what I do in the offline course I do 30 percent of it in the online course

### Speaker 2

Yeah

### Speaker 1

8000

### Speaker 2

every every other quarter there is a new LLM coming so I think covering more is good sir because otherwise even if


This is good to know

### Speaker 1

Are you asking them

### Speaker 2

I can cover more but we cannot thats everything

### Speaker 1

Right but like and also am I compromising on quality and thats the question

### Speaker 4

No sir no sir

### Speaker 2

Definitely not

### Speaker 1

definitely if you feel it that way just let me know okay see im covering too little im going a little slow actually just to ensure that everybody is in the same page anyway so shell

### Speaker 2

So in this network X is the image the input


Or X can be any kind of data like text or numbers

### Speaker 1

X can be any kind of data like yeah X can be any kind of data

### Speaker 2

And so then do we use this again for text generation also

### Speaker 1

uh generally people dont use cans for text generation okay there is another reason for it you asked this question next class to me i will cans is not over it okay i will spend the half of the next class on this i will i will give you more interpretations on this okay i will tell you why people typically dont use cans for text generation


A lot of noise in the background huh Okay I think

### Speaker 4

Sir you said you are covering a little less here so is there some reference material if we want to go a bit deeper

### Speaker 1

uh see my notes my handwritten notes all of that has uh reading material at the end of it

### Speaker 4

Okay so your handwritten notes the on your website right

### Speaker 1

I shared it with you did I or have I put it on the website

### Speaker 4

Uh I think there are some lecture uh videos uh but notes Im not sure

### Speaker 1

pictures videos no

### Speaker 4

Yeah

### Speaker 1

The Google Drive

### Speaker 4

The Google Drive link

### Speaker 1

theyre not theyre not videos theyre notes only you never have had a look at it please have a look at it

### Speaker 4

Okay okay okay thank you

### Speaker 2

But I think when you say handwritten notes you mean these class notes


Or it it is different

### Speaker 1

Okay let me show you what I mean


Please mute yourselves


Ill put it in my web page


Interesting

### Speaker 4

Okay okay yeah fine

### Speaker 1

to the end of this and there are more content in in this which im not covering and also these things you know all of these this is where you can go and see get all information okay

### Speaker 4

Okay so these notes are from offline course or theyre

### Speaker 1

Hey R I wrote it three four years back I mean just for my reference

### Speaker 4

Okay

### Speaker 1

You want my offline course notes I think something you should ask some offline students Im not making any notes for the offline class yeah

### Speaker 4

Okay so do you also have

### Speaker 2

Do you also have notes for ML or deep learning course

### Speaker 1

That havent I shared the shared it with you hold on I think I have it somewhere in one of my students when I called

### Speaker 4

I really cant say oh yeah

### Speaker 2

or email

### Speaker 1

Hold on hold on I will put it in the chat group right now hold on photos teams


Isnt this


Somebody asked this in the offline version and I shared this yeah this is I mean this guy Prashant


My student in the offline class his notes were so good I mean I generally dont do like slide based teaching I do board work So somebody wrote it very nicely and post


Uh ML notes


This is the course that I teach in the other semester I mean it is not I dont offer this for the online students only for the offline students Are you seeing my screen

### Speaker 2

No

### Speaker 1

Yeah that I put it in the teams okay


yeah i put it in the teams just have a look at it yeah so this is the this is this notes


So you can have a look at it


I have done that


I dont know if it will be of any use to you but anyway because this is all my board work whatever I did in the previous board work See what I suggest is if you want a good ML course right there are many of them One of them is of my advisor Professor Shastri It is there in NPTEL Its called Pattern Recognition and Neural Networks PRNN in NPTEL Okay you can have a look at it Thats a good foundational course on ML Okay


Okay I think we have to uh


Well past the time

### Speaker 4

Okay sir last thing Im very sorry regarding your deep genetic model old notes you just showed now if you please share that link as well please

### Speaker 1

Okay centre

### Speaker 4

Uh you showed that uh you took some of the notes on handwritten notes DGM

### Speaker 1

Uh what did I show you

### Speaker 4

I mean I mean just before before the email I mean same uh Google Drive I think you have

### Speaker 2

It is already shared actually if you search on the Google

### Speaker 4

Yeah

### Speaker 1

I think last years board work I think I have it Have I shared that with you ADRL classwork

### Speaker 2

So the one that is on your website

### Speaker 1

No no no not that theres one called ADRL class for kings let me see if thats the one


I think one year back was yeah this is some 130 MB


Let me share that


Here copy link manage access


Uh anyone with link


Here


Where should I go here


Im not a good like hacker post


previous


Heres class workings


See I dont see these when Im teaching because I want novelty every time But this is the previous years working if you are interested Do you still see my screen No

### Speaker 2

Not sure about it

### Speaker 1

Okay let me show you


You see it now


Yeah this is what Ive shared with you this is my


last years thing so I did very differently last time now I started from Gaussian mixture models VAEs and then I went to GANs


then to diffusion models and so on okay


If you want you can have a look at it okay

### Speaker 4

Cheers

### Speaker 1

Okay Ill see you next week then bye bye have a nice weekend

### Speaker 4

Thank you

### Speaker 3

Yeah thank you sir

### Speaker 4

Thank you

### Speaker 2

I guess so

### Speaker 4

Thank you sir
