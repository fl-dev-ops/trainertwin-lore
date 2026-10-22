---
id: wjFSuXgeHrY
title: Deep Generative Models Tutorial Probability theory
url: https://www.youtube.com/watch?v=wjFSuXgeHrY
date: '2024-11-23'
duration: 00:50:45
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: You know


Only the weight of network two will be updated


Okay that is how you can make sense of it I have given you one Stanford course Okay now there go to the course notes And then there you can see some of the topics where in which he explains backpropagation So where he takes a sigmoid node explicitly


He takes a specific sigmoid node and then he explains how to do the back propagation


Yeah to that specific signal node

speaker_2: To that specific signal

speaker_1: Its in the course notes of the link that I have given

speaker_2: Okay well check that

speaker_1: Now this is yeah this is one of the very good resources on CNNs Okay Now they have really given a very good resource on CNNs Now to understand CNN this is one of the best resource that I have come across I am not saying that there might be some other good resources but this is one of the notes that I have come across And apart from that one other resource that I have come across is a three blue one brown channel


three blue and brown

speaker_2: Yeah at least I know that

speaker_1: Yeah three blue one brown channel now there you can look at the convolution and so he has a specific chapters on neural networks now there you can look at it now in which the queries will be resolved

speaker_2: Yeah sure sure Chandan I think maybe we can yeah continue with the

speaker_1: So any other questions you have any others


So things are going on comfortably no issues are there


So now with this lets try to continue with todays discussion Now todays discussion is basically around some of the topics that Sir would have left in between for TS to fill in the some of the proofs and some of the algebra Now in that manner we will take some of the ideas from wherever he has left I have listed some of the important points


Im not Im not going till the first session Im trying to finish off the things that he has recently done Now so that your VAE and other stuffs so after VAE he will go to the diffusion models Now once he goes to diffusion models so you should be comfortable with those topics So I what I thought is rather than going ahead with a lot of previous things that was there there were some ideas on probability which whenever time permits we will come back


we will be looking into some of the stuff that sir has left in BAE okay so now the some of the basic proofs that I thought we will be covering today is one is KL divergence is always positive and then the idea of law of the unconscious statistician now depending on that we will see whether well be well be able to go ahead with other ideas


Okay Ill just stop on that


So now first we will take this weird thing that was law of the unconscious distribution This is one of the very important ideas that you find in probability


Law of the


of the unconscious statistician also called as lotus not any party symbol but just the abbreviation


So now it is useful to calculate


Easy to calculate expectation of


a function of a random variable


Okay


Now g of x


Its a


is a function of a random variable x


And then the assumption is


Distribution of X is known


and g of xs are known


If g of x is known then you can directly get the density and then do the stuff but it is not meant


Lets say Px


Now let this be


PMF or


pdf of x depending on whether x is a discrete random variable or a continuous random variable now what ill be doing is ill be going ahead with the continuous case proof for the continuous case is much simpler


So Ill be going ahead with the


roof for them


Continuous case


Okay Now lets say y is g of x


Okay and then we assume some ideas on G So we say that G is


Differentiable


And its


Inverse inverse which and then

speaker_3: Shandun

speaker_1: Yes sir Yes sir

speaker_3: Uh sorry I interrupted you uh Professor

speaker_1: Yes sir yes sir I got it

speaker_3: Yeah I I I mean if you can maybe just solve the midterm exam questions no that would I think be useful

speaker_1: I I I myself did not prepare for it

speaker_2: So can we have a separate tutorial for it this week maybe for that

speaker_3: Yeah yeah no problem maybe next week yeah maybe next week

speaker_1: Yeah sure sure sure sir

speaker_2: Or even I think maybe that that that I mean going through the mid term is also something which we wanted to go through so

speaker_1: Yeah


Sure uh we we will surely do it uh uh in the next session yeah

speaker_3: And then one other thing here Im sorry I did that

speaker_1: Yes sir yeah no no no no no problems yes sir

speaker_3: This is Saturday I will take the class between 8 pm and 11 am

speaker_1: Yes Im 11 yeah yeah yeah I saw the message

speaker_3: Yeah so you have the quiz at 11 oclock okay Sure after 11

speaker_1: Sure after sure sure yeah your sons interview is there

speaker_3: Oh yeah I mean sh

speaker_1: So all the all the best with the interview


See the guy cannot talk they want to interview him I dont know

speaker_4: See the guy cannot talk they have want to interview him why dont


I mean these Bangalore schools right I dont know what theyre

speaker_3: Anyway

speaker_1: Will you interview your son or you like you also I mean I dont know

speaker_4: Otherwise why would I go no I mean my wife could have gone so they have asked to specifically ask both the parents to be present with the child so

speaker_3: Yeah

speaker_4: Yeah go ahead and do that and then you have the

speaker_3: Its called

speaker_4: of these schools in the south bank but yeah so

speaker_1: So it has uh the sixth the sixth crosser DBJ road

speaker_4: Or Tatas will be at me

speaker_1: That is the link for him yeah yeah

speaker_4: Yeah so have that quiz on 11 oclock okay 11 oclock

speaker_1: Im loving it yeah

speaker_4: And one other thing somebody asked me to not have the quiz on 2nd of November right Because thats like a series of holidays and yeah sort of Diwali right So what we can do no 19th we will have a quiz 26th we will have another quiz okay

speaker_1: Just a

speaker_4: Then maybe I discuss that in today I mean the Saturdays lecture I just wanted to let you know that that one of these tutorials no you can see

speaker_3: Maybe or you can do another thing why dont you just solve the midterm

speaker_4: questions and just upload it in the group you dont have to spend time

speaker_1: That Ill do yeah

speaker_3: I think that would be easier

speaker_1: be easier sure sure sure that and we can we can ask doubts if any i mean

speaker_3: Oh yeah you can ask them to do it for you too

speaker_1: Itll be easier later

speaker_3: Sorry gentlemen I disturbed you please continue

speaker_1: No no no no yeah no problems no problem yeah


Sorry to interrupt you

speaker_4: Sorry Chandra before going into mathematics detail can you just suggest what is the intuition why we are doing this law of unconscious guidance

speaker_1: Ill Ill Ill come to that and Ill exactly come to that okay see uh for example Ill give you a very simple idea to calculate it comes up in

speaker_4: It comes up in reparameterization it came up in reparameterization

speaker_1: reparameterization so even a simple idea is to calculate the variance you want expectation of x square


x square is a function of x We know how to calculate the expectation of x How to calculate the expectation of x square We need the idea of lotus Thats the simplest example that we can think of


In addition to reparametrization thats what Sir said but the simplest idea that we can think of is

speaker_4: Ooh


Good example I like it yeah

speaker_1: Thank you


So my my internet got disconnected just just give me one minute


Im not a good


are in between what will be the syllabus for the next quiz will it be the last two classes


whatever has been covered till the pre previous quiz and then see you we cannot compartmentalize things like that for example if i ask you a simple question on probability now you cannot say that this is the quiz ones topics and this is not limited right

speaker_4: But Chandra dont ask things that Im going to know no no no

speaker_1: No no no no no no no no no no

speaker_4: You can be Markovian you should be ergodic

speaker_1: No no no no no no that Ill not do sir


So now the idea is see the first of all lets try to understand the name itself So now it is called as law of the unconscious statistician Okay Now you will be able to understand why it is called such in some time Okay So it is not like simply they just use that name Okay It has a very deeper meaning to it So the idea is you apply it in a totally in an unconscious way


What is this what happened screen


Are you able to see my iPad screen


So now we know how to we know how to calculate the expectation of x Now but now what we have is expectation So we have a function of a random variable now for which we want to know how to calculate the expectation


So now let us try to understand how to put Okay So now the conditions that we are imposing on g is now the function g that we have should be differentiable and the inverse should be monotonic Okay So under these assumptions once we have these assumptions now the current code will work I will tell you how each of the conditions make sense Okay So now


If y is z of x


exists


The inverse of


So now what is


by dy of g inverse of y


What do you say about this Can you compute this


Inductively can you think of the formula for this


So now this is


So just go ahead and refresh your uh our calculus uh stuff this is


the inverse of y


Now this is now this is


This is by the


inverse function rule


No


is nothing but this is D


The coins


One over


the inverse of y


Now all these things are fine Now where is this coming into picture Okay lets write what is expectation of g of x


How do you write it Now this is continuous uh thing is what my assumption is this is integral of


y into fy of y


This is how I write it right

speaker_4: sorry its g dash of g inverse of y right one y i mean we should take the differential of g


I am wrong sorry

speaker_1: No no no just just go ahead and on this is correct


Now what is the


distribution function of y Now this is probability that


Y is less than or equal to y


So this is nothing but probability that


y is less than or equal to g of x


This will be


This will be probability that


less than or equal to C inverse of


Agree with me so far


So this is effects of


Effects off


g inverse of y


Now I know the distribution function of y in terms of x I know see what is my assumption Now lets go back to my assumption Now I know I am saying that distribution function of x is known Now because of this trick that I have used I know the distribution function of y also now


Once I know the distribution once I know the distribution yeah Ive got it

speaker_4: I have a question So when you invert the g right to the other side x would be greater than g inverse of y right

speaker_1: A is less than B


1 over A is greater than 1 over B


1 over B is less than 1 over A


answers your question

speaker_4: Uh I think Ill have to Ill Ill take a look

speaker_1: Hey no no no no no no there is nothing there yes okay

speaker_4: Yes a chain of supplies one

speaker_1: See what is this is A okay let us come back here No this is A this is B cut


Apply this idea you will get this exactly the same steps


Now in inversion in terms of scalar is 1 by A right


Exactly the same thing See the inversion that is happening No B is coming here


And A is coming here You can see that


Now its clear exactly the same idea


Now okay whatever questions you have you can stop me anytime Okay See what is what will be happening is so from most of the times these will be like more of a mathematical work rather than what do you call any intuition or any stuff working Okay Now this is basically most of the times our discussions will be more on a mathematical proof kind of ideas Okay So sometimes it is known that we will lose path


that time we should take simple ideas like this to understand intuitively what is the steps that we are doing okay so now now now finally now i know the distribution function now if i know the distribution function can i get the density function

speaker_4: Yes differentiate

speaker_1: Differentiated thats all effects of


Green versus whitey


One by


See you off


Okay so now lets go back to expectation of


The office


What is expectation of g of x This is integral of y into fy of y dy correct


Now this is nothing but


What is y is g of x


Why use the office


What is f y of y that is f x of


g inverse of y


into


One by


g into g inverse of y


What is G inverse of Y


The inverse of y is x


Is it DX


This will be


Integral law


of x


fx of x


This is expectation of


This is the proof


See what is this fellow saying See if you have a function dont worry apply this g of x on everything and then use the density of x only which is mathematically crazy to us right


No but as it turns out with these proof it is very much clear to us yeah this is working


Does it make sense


Now that is why it is called as unconscious decision You dont even have to be conscious So just apply the function and take the density of x only or density or mass of x only It will work immediately You dont need to worry about at all


That is why this fellow is called as law of the unconscious statistician


Make sense Why it is called as law of the unconscious statistician


I have done it in steps now to get this


I did this this


Thats all very simple


Any questions with this proof Im done it only for the continuous case


to on a very restricted continuous case where g is differentiable and inverse is monotonic


Only for this specific case have considered it


Not for any other case

speaker_4: And then one question

speaker_1: Go ahead

speaker_4: How are we getting uh the derivative of g inverse of phi


Can you please elaborate a bit on this

speaker_1: You okay Uh you you you remember inverse function rule You know inverse function rule

speaker_3: Maybe Im missing out on that

speaker_1: Okay


So now to do so we should go on some more ideas

speaker_2: Is it the same as Janes rule gentlemen or

speaker_1: Now it is basically the derivative of inverse


Okay now how do you okay uh uh yes yes it is chain rule It is basically chain rule only Now how do you how do you calculate uh so


See okay uh


1 by x square


How do you do it

speaker_2: x square inverse and then

speaker_1: In the same way you proceed


So it is basically d by dx of x to the power of minus 2


And how do you proceed Tell me the full equation How do you do it

speaker_2: Find the one that fits

speaker_4: So this is minus 2x minus 3

speaker_3: Still extra

speaker_1: Yeah so fine So always confusions will be there You would have left all this differentiation integration some time ago because of which so well be rusty about the formulas but that is fine But the intuition is clear Now now does that answer your question Whoever asked this

speaker_4: not completely so if we are trying to relate inverse in terms of a reciprocal then maybe i am not able to understand that

speaker_2: I think Sanchit you can just check for this chain rule then you will get to know that how it works

speaker_1: How do you how do you do it Okay No okay This rather than that my previous example was much more simpler D by DX of 1 over X square How do you solve this

speaker_4: So this is x to the power of minus 2 The rule will be d by dx of x to the power n which is n x n minus 1 So in our case n is minus 2 It will be minus

speaker_1: 10 is minus 2 it will be minus If you dont if you dont want to use that is there any other way of doing it

speaker_2: It is uh I think f of g of x right I mean how do you evaluate

speaker_4: Do you want to edit your file for me

speaker_2: Yeah

speaker_4: F P of P of P by Q

speaker_1: So now in a similar manner you can obtain it for the previous case also


Makes sense


Any other questions

speaker_2: Watch out for the next question

speaker_1: You look next

speaker_2: Why that monotonically not increasing I mean where does that come into picture

speaker_1: So


that comes into picture in these steps


Okay now that is something that I have put it under rug I have put it under rug So now first you should understand what is monotonic sequence for that Now since we havent discussed monotonic sequence and other stuff so lets not go there Okay I mean is it coming from

speaker_2: I mean is it coming from the definition of CDF that it should always be increasing monotonically non decreasing

speaker_1: decrease yes yes yeah it is non decreasing it is not increasing okay cdf is monotonically non increasing monotonically uh non decreasing


Okay Yeah So its its like you have multiple layers of stuff Okay How much ever you peel no there will be something that is below it Okay Now we should somewhere put a stop So now Ill always give this example Now this example may be like So there is something called as real analysis


What is one plus one


It is straightforward answer But do you know the proof for one plus one is equal to two runs for three pages


There is a proper proof to say that one plus one is two which run for three pages


Okay now at some point or the other now we should stop it Now my point of discussion is like at least at the top level we should be able to understand the stuff and the derivations that well be looking in class and the tutorials


So now the next idea that we will be looking into is dKL is non negative


So now to do this now lets try to fix up some things


Lets start


P and Q


Be there


the distribution function


Okay let P and Q be the distribution function


And then they have density or mass now lets PQ


density function


respectively


Now when I say these are two distribution functions now the basic assumption is the what is okay what is a random variable can you recall


But now in these assumptions P and Q they have the same omega is the assumption


The underlying omega is same as the


So let small p and q be the


density function


So how do you define BKL between two distributions lets say P and Q


to define this


This is integral of


X by


So now if


If we are considering the discrete random variable now then


KL between ah these two distributions P and Q


This will be summation over all x


logo


X by


So now lets try to do it for uh


the discrete case


Lets lets prove it


Lets prove it


discrete case


So when I mean discrete now what do I mean by discrete


in this case

speaker_4: The random variable is discrete

speaker_1: Random variable is discrete Okay Now please remember that both of them share the same sample space


So it is not like they have different sample space


If they have different sample space you cannot even think of doing anything


So now what do we want to prove We want to prove dL is always greater than or equal to zero Okay So now


to prove


decay and off


E cube is always greater than or equal to zero


No because of which I can write that


Minus decay law


PQ less than or equal to 0


Now minus the gale of


By definition this is


minus summation of x


Beef fix


log px


QX


So this is same as


summation over x


Log


U x y


So far so good


So now


We know that


Logies are


Log is a concave function What is a concave function


How does the log x graph look like


Is this a concave function

speaker_3: Yeah

speaker_1: Okay what is a convex function then


How to how to get the convex function from log x now do you know any ways of doing getting it

speaker_2: Minus

speaker_1: Okay this is some good idea Let me put that minus


Logics


Is this a convex function


How do you know that it is a convex function

speaker_2: I think if you take any two points then they are always above the curve


I mean the line segment joining the two points is always above the

speaker_1: The idea is called as epigraph Okay That is the next idea that we will be discussing in the next tutorials Okay The idea is called as epigraph We will come to that specific point in the next session that thats rightly correct Okay Now log is a concave function


And then I invoke something that I havent proved yet will be proving it explicitly


By there is something called as Jensens inequality


And there are so many of these inequalities no no theyre very much what do you call


Always there is something called Jensens inequality


Have you heard of any other inequality


No not the inequality in the society


In mathematics have you heard of any other inequality

speaker_2: Triangular inequality

speaker_1: triangle inequality apart from that in probability do you hear anything


there is something called as Chernoff bounds okay uh that is idea called as Markov inequalities these things will come they are very wonderful inequality to get the bounds okay now we will be discussing them in time now the Jensens inequality basically says log of expectation of x is always less than expectation of log x


What is this


Is this expectation of log x


Does that look like this form


This is


Maybe I did a some some mistakes somewhere


So there is a negative symbol so I should be okay okay got it yeah


Why did I take this symbol


Okay there is a negative symbol here now because of which I have taken the other other inequality now because of which I can cancel of this and this

speaker_2: Then I have a query here

speaker_1: Morning

speaker_2: We said e log x


Less than or equal to log EX right So in the previous example it is not E

speaker_3: log x right i mean expectation is px if it was px no this is this is

speaker_1: No this is this is eLogix


Okay now this is expectation of log x


Now how do you get expectation of log x

speaker_3: a a summation of x into log x right thats what expectation of log x is right

speaker_1: Whom did you leave the density function for me


Okay happens dont worry all these things we all of us will do these kinds of mistakes


Yeah


Okay so now what is this now


What is Q


Or to be even more specific we are considering a discrete case in discrete case what is Q

speaker_4: Yeah

speaker_1: Now this is summation over all the x what will be this


this is

speaker_4: This should be one


Log one is zero

speaker_1: The log one is zero correct


See okay let me let this not confuse you when I say again and again here Im just carry forwarding this Im not saying this this quantity is less than this quantity that is not what I mean So if you are confusing with that You can always write this


And Im reusing the same in the quality


So because of which what I can say


KL off


is always greater than zero hence the proof


Uh I have seen one mistake


Now if px is a density function can you define it clearly for me


So so see when you say fx of x now you say that this is from r to 0 1 right


What is


This is R two R


If on the other term


If x is a discrete random variable so then it is from


R two zero one


the difference that is the reason why your density is not a probability measure


Now this is not something that is coming out of because of this if something has to be a probability measure the outcome has to be between 0 and 1 right and everything has to be positive Now it takes real values


Make sense now


Yeah so


I thought Ill be con starting with Jensens inequality today


yeah we dont have much time yeah any questions we will stop for the day

speaker_2: Chandan in the mid term there was one question that whether DKL is symmetric or not and if it is not symmetric what are the consequences of it so shall we cover this now or in the mid term review

speaker_1: Ill what Ill do is Ill write the answers for everything see to be very frank I havent seen the mid sem questions at all let me be very frank okay now Im a very what do you call this that that this will be there no so I I havent seen I should start even so we should come up with answer script now what Ill do is Ill come up with an key solutions and then Ill put it out and then in the next tutorials that is next Wednesday if you have got any questions well surely take it


Okay

speaker_2: Yeah thats fine

speaker_1: Okay sorry I I so if Sarah has told me I would have looked into it even it did not come to me also sorry for that


We will look it up in the next session

speaker_3: And one more question

speaker_1: Black guys

speaker_4: So this probability density function right So thats a function from R to R you mentioned Its basically the if you differentiate the CDF you get the probability density function right

speaker_1: Yeah if if X is a continuous random variable

speaker_4: if x is a continuous random variable so that can be looked at as a likelihood of the value taking x right x taking the value x

speaker_1: Why are you looking lightly here Okay fine then

speaker_4: Uh would it go beyond zero and one in in so basically my question is like yeah would that uh value of px the density function go beyond zero and one Yes yes yes that is what I said r2r

speaker_1: Yes yes yes that is what you said yes yes yes

speaker_4: Yes please can you give an example

speaker_1: It takes Gaussian distribution


Take take any Gaussian how is the density of the Gaussian distribution is

speaker_4: Yeah this is the density of the hose

speaker_1: This is the density of the Gaussian distribution


Okay now so if you make it sharper or larger no it will exceed the zero one You can do it easily

speaker_4: Yeah yeah yeah I yeah so for example even if you take a uniform distribution between zero and half

speaker_1: Im not sure

speaker_4: And that can have a value two right and any point between zero and okay

speaker_1: can have a value two right at any point between zero and

speaker_4: Okay got it

speaker_2: But it is not defined for a particular point right it has to be always I mean the density function is it defined for any given point


We have to always take an interval right


So we can we cannot evaluate PDF at a particular point right

speaker_1: We cannot evaluate


no no no no what his question is correct your point is correct what his question basically is at any given point what will be the value you are correct it will be zero at at a single point correct but at any given interval also it can take more than uh uh zero one is my point

speaker_2: I think the question is like uh I mean how does it relate to the likelihood

speaker_1: No see okay dont dont bring in likelihood at all


Okay so now it is much more simpler now without looking into likelihood and then see it as an R2R function


Okay now that will be even simpler

speaker_2: Yeah

speaker_1: Okay and it is much more simpler and say that this is not a probability function It is not probability Your mass is a probability your distribution function is a probability but your density is not probability


No questions no further questions


So meanwhile maybe today or tomorrow at tomorrow or day after at max Ill be putting the solutions for your quiz sorry for your test one online So you can look at it and then we will discuss any queries So in the next tutorial session Okay And then we will continue with


proving of this uh uh what do you call Jensens uh inequality and then we will continue with the discussions that are remaining


Make sense


So thank you


Lets meet next week
