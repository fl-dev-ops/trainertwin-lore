---
id: nGwjqvLHguA
title: Tutorial 2 : Simple Problem solving in Probability Theory
url: https://www.youtube.com/watch?v=nGwjqvLHguA
date: '2026-01-21'
duration: 53:51
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Hello all welcome to this tutorial on
problems of probability

Till now you have successfully completed
two weeks of lecture sessions
By now it should be clear to you that
the basic ideas of probability
are needed
in understanding
the ideas of machine learning So to
reinforce that we have selected a few
problems which will indicate some of the
important aspects of probability
So we will go through each of those
problems
The main idea as I told you is to
reinforce that Okay Now these ideas of
probability can be used whenever
necessary in the coming discussions that
happens during the course So without
further delay so lets proceed
So Ill take a very first problem as a
very simple one
The problem goes something like this
You have four letters Okay Letter one
letter two letter three letter four
Okay You have letters and then you have
four envelopes on which the address have
been written Okay So now you have four
letters and then you have four
envelopes Now
you can randomly put a letter into an
envelope
Now when this is the case now what is
the probability that exactly three
letters are in correct envelopes Okay
So out of four three are in correct
envelope So you have four letters
exactly three of them should be on the
correct envelope
Now this is a very interesting question
The reason being see if I have four
envelopes and four letters
If three of them
are in correct envelopes then the fourth
one has to be there
Correct So the probability of this is
actually zero
Why Exactly three He is saying okay
exactly three No it is not possible
Okay exactly two I would have computed
exactly three If three of them is in
correct envelope then the fourth one
has to be in the correct envelope
properly Okay so now
therefore the probability of this
specific event is zero Okay now the
answer
is zero So Ill not be going into the
uh pro uh detailed writing of detailed
explanation but intuitively now it makes
sense to us Okay So now this is the
first simple problem that we have taken
So now lets go to the next problem
Now the problem is like this A bag
contains two coins Okay You have a
small bag It contains two coin Now one
coin is a fair coin Now what do I mean
by fair coin is uh that if you toss it
the probability of hedge and the
probability of tails those are the two
outcomes that are there they have equal
probabilities Now by now you should be
knowing the overall idea of this coin
tossing and what is the probability and
stuff which has been discussed also Now
on the other hand you have the second
coin now which has both the heads
Okay Now you have a fair coin Okay
And then you have a second coin which is
a biased coin Now when which both are
heads Okay
So now then what happens is you randomly
pick a coin from that bag and then you
toss it Okay You randomly pick a coin
and then toss it Now what is the
probability that its a fair coin
Is the first question The second
question is you draws the same coin
again it gives you tails then what is
the probability that its a fair coin
Okay Now to understand this
we should be going ahead and using a
very important base rule So now lets
uh
I have
coin one
lets call it a fair coin
Coin two lets call as a
biased coin
Okay And what are the outcomes that are
possible The outcomes that are possible
are either you can get a head
Okay lets indicate this head by H and
tail
Lets indicated by T Now what is that
we have now Already I have tossed a
coin and then head has come up I
already know something has happened Now
on that evidence what is the probability
that its a fair coin given head has
already occurred
Okay
So
now
now well be using B rule and then the
total of probability together it will be
probability of heads
given a
fair coin into probability of
choosing a fair coin
This is the numerator
divided by
in the denominator we have two terms
Now probability of h
head now given that its a fake coin
into probability of
fair
plus the second term is probability
that I have a head given
biased coin into
probability of getting
biased coin
Okay
this now probability of head when you
have a fair coin Now its a fair coin
Now therefore it has to be 0 point 5
Now then probability of you getting a
fair coin Now that means when you take
a coin from the bag what is the
probability of you getting a fair coin
There are two outcomes So one of them
being fair So it has to be 0 point 5
divided by this 0 point 5
into 0 point 5
plus
Now when you have a biased coin when you
know that you have a biased coin what is
the probability that you get head It is
1 into what is the probability that you
get a biased coin Okay that is 0 point 5
Now if you compute this this is 1 by 3
That means that when you know that you
have got a head the probability that
the coin that you have in hand is a fair
coin is 1 by 3
Okay Now this is for the first one
What is the probability that its a fair
coin The second one is you toss the
same coin Now whatever coin that you
have got okay it was the same coin and
then it shows a tail
okay
so in that case what is the probability
that it has to be a fair coin now
intuitively you know that it has to be
one
but the question is can you obtain it
in terms of equations I will leave it up
to you
that is probability that
the coin that I have is a fair coin
given a head and then a tail has
occurred
Can you substitute this
Now
this is the probability of
getting head and tail
given a fair coin
into probability of
getting a
fair coin
divided by
I have two terms again here
that is probability of head and tail
The coin is fair
into probability of
fair
plus
probability of getting head and tail by
knowing that its a biased
into probability of a
biased coin See now here this is the
denominator the sum of these two terms
Now probability of getting head and a
tail from a biased coin Now it is not
possible at all Why A biased coin has
two heads in our case So this will be
zero This zero into something So it is
zero This plus 0 So its the same
term So you this term and this term
will get cancelled So it has to be a
fair coin So its one Its a for sure
So once I get a head and then I toss it
again and get a tail Okay Now the one
that Im getting is a fair coin On the
other hand can you compute in addition
to this You take a coin randomly and
toss it you get a tail What is the
probability that its a fair coin Can
you compute it in a similar manner I
believe it Okay Now this is how you
try to understand
the calculation of probability
So now lets go further
The next question that we have in hand
is now you have a
random variable Now to be more specific
now this is a
continuous random variable I should
have mentioned that you have a
continuous random variable
Okay And then for a continuous random
variable you have a density This is the
density Okay and the density is uh
between 0 and 1 Okay thats the
range of this Okay so now the question
is find the value of K
So now lets try to understand this is a
very interesting question altogether
No it which will give us a very
interesting idea For example lets for
this random variable X I can have a
distribution function Now a
distribution function is from R to
01 Now you know that the distribution
function or of push forward function
which is there is actually a probability
measure Okay you know it So now and
then in the similar hand you know that
the distribution function
can be evaluated at a given point Now
how do you evaluate it minus infinity
to x
the density function at that point into
dx
correct
So now you can say that
function of infinity
now what it will be now it will be minus
infinity to infinity px of x
dx now this has to be one
1 equals and then what is the actual
thing now this is between 0 and 1
px of x
dx X
Okay So now lets substitute the value
Now this is same as 0 to 1
k
into
1 minus x into x dx
Now k is independent of x So we can
take it out integral of 0 to 1 x minus x²
dx
if you
integral can be applied uh to both of
this So you will get
x² by 2
this is 1 x cq by 3 0 to 1 we have to
evaluate this now this is
k
1x 2 minus 1x 3
this is
k into 1 by 6 is
implies
k equals 6 Now what is the main outcome of
this overall thing Now
if you integrate your density function
from minus infinity to infinity you
should get one
Okay
Now please remember Im not say saying
that for a specific value of x you will
get anything No Im saying that you
integrate it from minus infinity to
infinity you should get one
because of which I would be able to
calculate the value of this key
Okay that is the take home message from
this specific problem After that it is
just uh what do you call the algebra of
it Okay now then the overall
computation is boils down to the the
algebra
Okay Okay Good So now lets take the
next question
Now we have already been even in the
class introduced into the uniform
distribution
So lets say that I have a random
variable X now which is a uniform
distribution from minus1 to 2 Okay
And what is the density for uniform If
x is a uniform from a to b then the
density x is 1 by b minus a in this case
1 by 2 minus 1 which is 1 by 3
okay this is the density
fine now this density is
defined in this between these values now
I take y which is mod of x Now because
of which now tell me what is the
probability that x is
less than or equal to y and then what is
the probability that x is less than y
Now you might think that both of them
are same actually hold on Okay theres
a very nice catch here which we should
understand So now
lets try to understand this for any
number for any real number x okay we
dont we we we whenever I say number now
throughout the course unless specified
we are dealing with real numbers okay
for
any
real number
x
is always less than or equal to x for
sure right
okay now lets Say that x is minus1 1
is less than mod of 1 1 is less than
one This is true Even if it is a
negative value If x takes a negative
value If x takes a positive value
lets say that x is one Now one is less
than modulus of one Less than or equal
to yes It is trivially holds Good Now
that means that irrespective of the
value it holds
Okay Let it be positive or let it be
negative So now
this holds And
only
when
x is negative
x will be less than this
Now you see this this and this is
different Now this is valid This
relation is valid for all the values of
x But this relation is only valid when
x is negative So now
therefore probability that x is less
than or equal to y which is same as the
probability that x is less than or equal
to modulus of x
This is one because it is true for every
value But on the other hand
probability that X is less than Y
is same as probability that X is less
than modulus of oh sorry theres no
equal to here
Okay
So now X is less than modulus of X Now
the effective values that X can take in
negative is from 0 to minus 1 Correct
So therefore
now this has to be probability of X less
than 0
And the question is do we know how to
calculate this
Yes we actually know how to calculate
this Now this is nothing but integral
from minus infinity to 0
p x of x dx Now the effective value is
 1 to 0 1 by 3 dx which is 1 by 3
See now I just
please remember this
Okay Now the key takeaway from this
question should be okay So now
depending on the nature of the function
Okay Now please try to understand the
equalities
this can change For one
see what has happening just for the
other see what is happening
Okay please be vigilant
with these kinds of things
Okay I assume that the takeaway message
is clear from this question Okay so
now lets go to the next question
Now I have a discrete random variable
Okay now whenever I have a discrete
random variable this is a mass
function
Okay its not a density function only
when so but for both of them we use the
same notation but while using it now you
should be very much clear okay depending
on what is the random variable at hand
now if it is a continuous one then it is
a density else its a mass okay if it
discrete its a mass so now here uh so
we just need to look at the expectation
remember expectations
So remember moment generating functions
what is the relationship between moment
generating function and expectations
Have a nice recap Okay
So now
now always now we are trying to estimate
the distribution or the moments of it
Correct Thats what the first premise
was So now we are estimating it Now
the uh the expectation of x since x is a
discrete random variable for all over
all x it is x into px of x the values
that it is taking is lets say that k equals 1
to 20 this is k into 1 by 20
okay
now this is 1 by 20 into summation k equals 1
to 20 of k Now you should be knowing
this 1 by 20 into 20 into 21 by 2
Remember the formula sum of n numbers
Go back This is 21 by2
This is how you calculate the
expectation of a
discrete random variable
Okay
after that its a numericals Okay
these are algebra
Now lets go to the next question
Now
I have a
continuous uh random variable a uniform
distribution from 01 okay 01 uniform So
the density will be one So now Im
asking you if this is the y now y is a
function of x now now and then youre
trying to find the expectation of y and
y is a function of f function of x sorry
okay
so
do you recall a very interesting
proof
by the term
Lotus
law of the unconscious statistician
Now it says
if you have expectation
of a function of x
okay then uh how do you do it Now
integrate over it Now you apply the
function at a specific point and then
have it
thats
okay
Now go back to this and then please try
to look at it Law of the unconscious
statistic its so common you dont feel
the difference at all Okay We will use
it now Okay So now what is y y equals
x² plus 2x plus 1
Now expectation of y equals
expectation of this x² plus 2x plus 1
You remember the linearity of
expectations
Thats the catch with the linearity of
expectations
Expectation of x² plus 2 into
expectation of x plus expectation of
constant one Expectation of a constant
is a constant itself Okay So now this
expectation of x Now I have to
calculate Now this expectation of x² x²
is a function of x So now I will be
using this law of the unconscious
statistician So lets calculate each
one of them So expectation of x is
0 to 1 x into px of x density dx which
is integral of 0 to 1 x dx Why Because
the density is 1 This is x² by 2 at 01
This is half
Expectation of x is half Now you have
to compute expectation of x²
How do you compute
Now you take the integral and then you
evaluate fx that is integral 0 to 1 x²
into the density of it
See now it is so natural okay from here
so x is there you x square is there that
is why it is called as unconscious
statistician you dont even you dont
need even need to be conscious a
statistician whenever he is applying
this he dont even need to be conscious
unconsciously he can just apply this and
take it from me the proof is three pages
okay nice proof is there in Wikipedia a
very easy for uh showing it for a
discrete case please go ahead have a
look at it its interesting now this
integral
0 to 1 x² dxq
by 3 by 0 1 this is 1 by 3 now then you
have everything now lets put them
together expectation of y equals 1 by 3 plus 2
into half plus 1 this is 7 by3
okay The key takeaways from this is now
how do you apply this law of the
unconscious statistician and the
linearity of expectations
Okay Now this example is designed for
understanding the linearity of
expectations and expectation of a
constant and then law of the unconscious
statistician That was the aim of this
problem
Okay lets proceed
The next question that we have in hand
is let X be a random variable See Im
not specifying that know what it has to
be Okay Now this we are generically
using for continuous random variable or
discrete random variable
So if X is a
random variable and Y is a function of
X See expectation of X is a constant
Variance of X is also a constant
Therefore the square root of it is a
constant So this is X minus some
constant divide by some other constant
Now whatever it might be Okay Now
given Y which is a function of X Now
now compute mean and variance of it
Okay Thats the problem at hand Okay
So now lets
define lets make it easy lets say
expectation of X is lets say lets call
it by mu easy
So and then sigma square no I should
have written the other way the the
variance of x lets use sigma square
therefore
implies the square root of variance
now what my y will be now my y will be x
 minus mu by c now this is write for
indication that there is I just rewrote
this so that you dont see X and then
again do some kind of other blunders of
uh calculations So now I have to find
the mean that is expectation of Y is
expectation of this whole thing X minus mu
divided by sigma
So now
expectation of
ax is a into expectation of x Now 1 by z
sigma is a constant I can take it out
Okay This is 1 by zigma into expectation
of x minus mu Now by the linearity of
expectations I can this is expectation
of x minus expectation of mu
Now we know that expectation of a
constant is constant itself Therefore
this will be 1 by sigma into mu minus mu
this will be zero
Okay expectation of x I have said that
it is mu and here mu is a constant
expectation of a constant is the
constant itself So mu minus mu is 0 So 0
into anything is 0 So I got zero over
here
Okay So now
then I need to compute the variance
Okay Now variance of
y now which is variance of x minus mu
sigma
Now
variance of something into constant
Okay Now if variance of ax is equal to
a² into variance of x Okay Now I can
use it 1 by sigma square into variance of
x minus mu
Okay
So now okay maybe I should write it
somewhere Okay Ill write these
formulas used somewhere Expectation
Okay
Let me use some other color some which
formula Im using expectation of
x plus y if you have these are the formulas
not related to this is expectation of x
plus expectation of y okay linearity of
expectations and again you have this is
the first one uh expectation of a
constant
is constant
then you have expectation of ax is a
into
expect see expectation of x is a
constant its a scalar okay please
remember that similarly what I have used
here okay the same thing now this is
I have used
variance of ax
equals a² into variance of X
and the other one that Im using is
variance of
X plus A
equals
variance of X
Now this is variance of X plus some
constant minus mu Now therefore this
will be 1 by sigma square into variance
of X Now this is 1 by sigma square Now
what is variance of X How did I define
it
I used sigma square
Therefore this will be square
Therefore it is one So y is a random
variable which is function of x with
mean zero and variance one
Okay
So now now what are the key takeaways
from this Now trying to understand
applying expectations and trying to
understand how do you get how do you
apply the equations of variance that is
the key take key takeaway from this
specific question okay I think that has
been
uh pinned properly
okay so now lets go to the next
question which is a fairly simple one
now in question now what is that Im
having Im having XY are IID binary
random variable now
IIID you know what is independent and
identically distributed
uh we discussed it in quite a length
remember that very important assumption
now to understand that assumption itself
we are trying to handle this question
okay now X and Y are IID binary random
variables taking only two values
0 and one That means that this random
variable takes only two values Okay
Now the probability of taking one value
that is zero is 1 1 minus p and the
probability of taking uh 1 is p
Now if zed that you have is x plus y what
is the mass function of z
Now mass function is at each point Now
what is the values what is the uh
probability that it is having So now
these are discrete random variables X X
X and Y are discrete random variable
Therefore X plus Y will be a discrete
random variable Okay Now what are the
values that zed can take Lets go ahead
with this Zed can take value
0 1 2 These are the values that zed can
actually take
Okay So now we have to find the mask
Now that means that what are the things
that you should do now PZ of zero you
should calculate PZ of 1 you should
calculate
mass at two you should calculate Okay
So now
PZ of zero Now what do you mean by
this This is probability that Z takes
the value zero Now what is Z This is
probability that X plus Y takes the value
zero
Now when will x plus y takes the value
zero When x plus y individually can take
only 0 and 1 Now this is possible only
when probability that x is zero and y is
zero Correct These are the this is the
only case
Now you see this this x and y are iid
independent is a I Im just using the
independent
uh feature here Now
this I can write it as probability that
x equals to0 and probability that y
equals to z
Okay Now what is probability that x
equals to 0 The probability that X
equals to 0 is 1 minus P
Now what is the probability that Y is
equal to 0 Now since X and Y are
identically distributed
Y taking the value zero is also 1 minus
P Now this is where Im using the
identical part of it Okay Previously
from here to here I used the independent
part of it Now Im using the identical
part of it This is 1 minus p square Okay
Now I presume that these minute
differences are clear for you Okay So
now the next value that okay now
the next is the mass at value 1 Now
this is probability that
z equals 1 Now this is
probability that x plus y takes the value
one See x plus y can takes the value in
two different things Okay And
those two events are disjoint that is x
is equal So what are the values that it
can Okay Now the two options is x equals 0
y equals 1 x equals 1 y equals 0 See these two events are
disjoint Now whenever recall the exams
now whenever you have disjoint events
now you can add them This is
probability that x equals 0
comma y equals 1
plus probability that x equals 1 y equals 0
Now I think from here you are capable
enough to take it Similarly
PZ of 2
This is probability that zed takes the
value two Now which is probability
that X plus Y equals 2 It is only possible in
the case when X equals 1 and Y is equal to 1
Okay Now I have partially solved the
problem for you From here use the
independent and get them into products
and then use the identical get the
numbers and find the
final values Okay Now this is for you
to understand Now how do you apply the
iid assumption that you have Okay Now
please remember Im reiterating See
dont Yeah Okay Dont put uh
calculation emphasis is needed but
understanding
which property has been used in which
step is very critical in going ahead
Okay I presume that that is pretty much
clear
Okay
So now lets go to the next question
Interesting question in itself
Okay So now
we have a random number generator
that generates random numbers uniformly
distributed over 01
Okay Now you ask it give me a random
number it will give you a random number
Now you ask it for 10 times Okay Now
you ask it for 10 times and then it gave
you 10 numbers Okay Lets say that
this is
X Okay If I got 10 instances of them
x1 x2 so on till you got till x10
all of them are sampled iid okay all of
them are sampled iids
from a uniform 01
again this question is also to reiterate
the idea of iid now what is that I want
now I want the probability that the
maximum number is less than 0 point 8 8 Now
the maximum of these things is less than
0 point 8 Now that means that each and
everyone is less than 0 point 8 Correct
Now if lets say that m is the maximum
m
of
x1 x2 so on till x10
Now if my maximum value is less than 0 point 8
8 Now which means that individually
x1 is less than 0 point 8
x2 is less than 0 point 8 so on
x10 is less than 0 point 8
Okay So now you need the probability of
this
m less than or equal to 0 point 8
Now this is this the probability of this
is union of these individual things and
these are disjoint
Okay
Oh no no no no sorry these are sorry
sorry sorry for that No no no not not
that No these are iid assumptions
Sorry Okay These are iid Now
therefore what happens is this is
probability that x i less than 0 point 8
Now you multiply each one of them So
therefore Ill get 10 here
Now x i taking a value less than 0 point 8
Now this is you know this already from
uniform 01 this value will be 0 point 8 to
the of 10 Now why is this 0 point 8 Now
what is this This is integral
0 to 0 point 8 8
x into px of x dx
Okay
Oh sorry Integral Sorry Sorry Sorry
for that Okay This is integral
0 to 0 point 8
This is px of x dx I confused with
expectation
Okay
This is one Therefore you get 0 point 8
This is your distribution calculation
Okay Sorry I wrote expectations Yeah
Uh no see this is as s reiterates No
this is a straightforward indication
that we are not AI which means that we
make mistake and immediately we get a
feedback and then we correct it Okay
Good So now here again the idea is to
understanding the IID assumption
Okay Now ID is a very important
assumption during our discussion Okay
So lets go to the next question
Let XY be random variables with mean and
variance one both of them Okay Now
whenever you get like this always write
it expectation of X equals expectation
of Y equals Z and then variance is one
Now that is variance of x equals
variance of y equals 1 and then the
covariance between x and y
is row
Okay Now find
expectation of x plus y whole square Okay
Now again this combines all our uh uh
ideas on expectations Expectation of
x plus y
square This is expectation of
x² plus y² plus 2 x y
This is expectation of x² plus expectation
of y² plus 2 into expectation of xy Now I
dont know see if if you want to
calculate the expectation of x² okay I
know the law of the unconscious decision
now I can integrate and say x into px of
x dx but what is this px of x I havent
been given I even dont know what is the
the effective uh uh support of this
random variable
okay so now with these I should go ahead
okay so now the idea is quite simple
Simple
Lets use the variance of X formula Now
what is variance of X Now variance of X
is expectation of X² minus expectation
of X square
Okay Now we know variance of X is how
much It is given 1 equals expectation
of X² minus Do I know expectation of X
Yes it is 0 square It is 0 which
implies expectation of x² equ equals 1
Similarly
expectation of y square is also 1
See now by using this variance formula
which is a new learning in our case we
understood these two things
Okay Now I just need to know
expectation of xy Now how do I know
expectation of xy
Now we know that the covariance of XY is
given by expectation of XY
minus expectation of X minus oh sorry
uh expectation of X into expectation of
Y Now expectation of X and expectation
of Y are zero Now therefore this term
is zero Therefore this is this I know
row is expectation of XY Done I got
all the values internally Now I can
substitute them Expectation of X² is 1
 plus Y square is 1 plus 2 into row This is 2
into 1 plus
the expectation of X plus Y square See
here I was not knowing the support of
the random variables I was not even
knowing
uh their densities or mass for that
matter Okay Now here Im not even
assuming that they are continuous or
discrete in any way And I even dont
have the
uh information that theyre IID Now if
you had IID okay you would have said
something else would have got something
but none of that was happening
Okay By using these given values we
were able to compute this
Now here the idea is to introduce to the
idea of covariance
and then the calculation of variance was
the main idea the additional thing and
this from here to here we already knew
this This is from the linearity of
sorry from here to here we already knew
knew this This is from the linearity of
expectations How do you get this
independent value Okay that was the
main idea in this case
Okay
so good So now lets go to the next
question
Next question is an interesting question
which is on conditional expectations
Now here I have X and Y are independent
See Im not again Im not saying theyre
ID Theyre independent independent
random variable with
expectation of x is mu1 and expectation
of y is mu2 Now give me okay if zed is
x plus y then what is the expectation z
given y okay now lets try to do it now
this is what is that I have to find I
have to find expectation of
conditional expectation of z given y now
this is expectation of
x plus y
given y
Okay
Now again from the linearity of
conditional expectations this I can
write it as expectation of X given Y
plus expectation of Y given Y
Okay Now this is from the linearity of
conditional expectations
Now
we need to calculate each one of them
here expectation of X given Y
See now X and Y are independent
Now therefore conditioning on Y has no
impact It is expectation of X which I
know as mu1
Okay When independent So when X and Y
are
independent We know this
And the next thing is I need
expectation of y given y
We know this this is y
Okay Now substituting these back Now
this is mu1 plus 1
Now here now we are understanding now
how do you calculate the conditional
expectations under the nature that x and
y are independent
Okay
Now
the last problem for our discussion is
if X and Y are IID standard Gaussian
Okay standard normal distribution
Whenever I say standard normal mean is
zero and variance is one Okay that is
what when I mean by standard normal that
is X and Y are
normal 01
Okay and I have my zed
 equals 3x plus 4 y Now what is expectation of
zed This is expectation of
oh sorry uh what is the density of zed
Uh for density understanding you should
know the expectation and variance So
expectation of
3x plus 4 y the linearity 3 into
expectation of x plus 4 into expectation of
y this is zero Expectation of x is zero
and expectation of y is zero Okay And
then
variance of Z
is
variance of
3X plus 4 Y
Now what is this This is
variance of 3X plus variance of 4 Y plus
covariance of 3X 4 Y See since
X and Y are independent the coariance
term will go to zero It will not So
therefore this is variance of 3X plus
variance of 4 Y
This I know this is 3² into variance of
X plus 4²
into variance of Y What is variance of
X and variance of Y It is 1 And
therefore it is 3 squar plus 4 squar which
is 25 Therefore z is a random variable
Its a stand its a gaussian
distribution with mean zero and variance
as 25 I think from here now you should
be able to write the density Now that
is P Z of Z equ equals 1
2i
sigma square root of this
exp of
Z minus mu
square there is a minus here divide by 2
zigma square okay now this is 1 by 5 into
square roo of 2i
exp of minus Z²
50
This is your density function
Okay Now with this I
conclude todays tutorial on the
problems on probability theory Now the
main aim of this tutorial was to give
you some of the interesting ideas
and how do we use them and when do we
use them Okay throughout the course in
each of the problem we have looked at
some of the important ideas and as we go
along now whenever these ideas are
needed well be recalling them back and
then using the same good old ideas
Okay these are quite important I
assume that
you enjoyed this tutorial on
simple problems on probability theory
These were not numerically heavy
problems These were simple calculations
for us to indicate the key concepts that
are needed during our discussion of this
course I hope you are enjoying the
learning Thank you Well meet in the
next tutorial Thank you
Bye bye
