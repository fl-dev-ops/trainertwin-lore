---
id: C83xmx80tMo
title: Lec 07 IID Assumption
url: https://www.youtube.com/watch?v=C83xmx80tMo
date: '2026-01-16'
duration: 30:41
model: youtube-captions (en-orig)
transcript: true
---

# Lec 07 IID Assumption

## Transcript


Welcome back What is this IID
So this means that this is
Okay
Again Ill have to um
tell you one other interpretation
Lets say uh
that we have
two random variables D dimensional
random variables okay
That are defined on the same sample
space
Okay
There will be two distributions
corresponding to each of them
What if
both the distributions are exactly the
same
So its like having Its like observing
the same random variable twice
You can see that as either observing the
same random variable twice
or you can see that as observing
two different random variables having
the exact same distribution correct
Okay So thats the when I when I say
that they are identically distributed
you see these all of these N points as
one realization of N random variables
having the exact same underlying
distribution PXY
That is what it is
Okay So it is that you have either you
have N realizations of
the random variable or
you say that
you have
one realization of N random variables
all of which which have the all of which
have the exact same distribution PXY
Okay So that is one thing You know
theyre all identically distributed So
whenever we do machine learning we make
this assumption that
all the N data points that we have are
coming from the exact same distribution
which is which says that the underlying
experimental conditions are not
changing
So thats why
non IID data you know dealing with
non IID data is a well known research
problem in ML community
So what happens when the IID assumption
breaks
Okay So thats why
if you
create a machine learning algorithm
build a machine learning algorithm on
one data set lets say that you do it
on lung X rays
So you cant use the same uh
same algorithm to work on lets say
brain MRI because theyre not
identically distributed The underlying
sample space or the random experiment
that we are doing is not the same
Okay Thats one thing
The other thing is you know youre
saying that theyre independent So
what do I mean by that I actually did
not define independence earlier Ill do
it See uh recall your probability
theory classes
If there are two events there is
something called statistical independent
that is defined between two events
right
When When are those two events called
statistically independent
Two events are called statistically
independent if
Yes the intersection uh the probability
of the intersection of those is equal to
the
Sum or product
Yeah So no no Im Im not asking
about about the distributions Im
asking about the probability measures
The measures So Im saying if two
events A and B are independent if A
intersection B is equal to
P of A
Yes This is the definition of
independence right Same thing happens
with the
the distribution If the joint
distribution
happened to be product of marginals
then they are called
then the then the random variables or
the underlying distributions are called
statistically independent
So this this is a technical term This
is not nothing to do with the English
independence or anything okay Even
though they are sort of related
Now what are we saying here is that
I told you that this can be seen
as one realization of N random
variables
This can be seen as
one realization of N random variables
each which have which all have the exact
same underlying distribution
What we are assuming or what we are
saying is that each of these random
variables
are statistically independent
Which means
that if I have to write the joint
distribution of all N data points I can
write that as product of
the individuals
Okay Please note
that Im not saying
that
Okay so hold on Let me come to that
You know this creates a little bit of
confusion See here
each of these random variables right
XI They are in D dimensions right
Initially I told you that even as even
a D dimensional random variable can be
seen as
combination of D scalar random
variables
Even amongst those random variables we
can define define statistical
independence Do you see
Am I saying that here
No
Very very important
Okay
Independence in the IID assumption does
not mean that
the vector valued random variable here
is independent across its dimensions
The independence here only means that
there is statistical independence
between the individual data points that
we have drawn
make that clear So if you if you want
to you know
Im saying
that image one is independent of image
two
Im not saying
that the first pixel in image one is
independent of the first second pixel in
image two Sorry image one
Do you see the difference
See we can make that assumption by the
way In some of one of some of the
algorithms we do make an assumption
that the
there is statistical independence across
the dimensions of data
But in general we dont make that
assumption In general
we dont make that assumption that there
is statistical independence among across
the dimensions of data We only make an
assumption that there is statistical
independence across
multiple observations of data
But in general different pixels might
have Not might they will almost always
have dependence So we dont model it
that way
See again very very important right
You know we have two variability here
you know two or two axes of
variability right One is that every
single random variable which is a data
point okay is a D dimensional random
variable which has which can be seen as
amalgamation of D scalar valued random
variables
Okay And we are not talking about
statistical independence amongst those
D scalar valued random variables that
constitutes a single data point
We are talking about statistical
independence between
different data points We also saw we we
we said that every data point can be
seen as
one element of the range space of one
random variable and there are N of them
which have exactly the same
distribution Okay So those N random
variables are statistically independent
Thats the IID assumption
Okay Let me write that So
independent
across
data points
and not data dimensions

 And theyre identically distributed
What does that mean That you have one
observation of N N random variables
Each of them have exactly the same
underlying distribution Or you can say
that
See if you if you have the viewpoint
that you have N observations of the same
random variable this identically
distributed
becomes redundant you know you dont
have to say that they are identically
distributed because there is only one
random variable that youre dealing with
anyway There are N observations from of
that random variable
Do you see this
You know two viewpoints Basically
there are two different ways of looking
at the exact same thing When you see a
textbook or when you read a paper they
will say that you have data set
and this tilde corresponds to sample
from The symbol tilde corresponds to
sample from So it is saying that
the random experiment What do you mean
by sampling by the way
Sampling is conducting
multiple trials of the underlying random
experiment that gives rise to the sample
space That is sampling
So this means that we have
got tossed the coin or rolled the die
capital N number of times
Okay And that has given rise to an
underlying sample space And that sample
on that sample space we have defined a
random variable And we have N
observations of that Okay And the
underlying probability measure that we
have defined on the sample space have
given rise to a distribution
that we wish to uh estimate later
Ill take questions in a while
Is this viewpoint clear
See Ill From now on Ill just write
that we start with a data set which has
N tuples sampled from an underlying
distribution You should know what it
is
Okay You can see this as one
realization of N random variables that
have the exact same distribution
Or
N realization of one random variable
which has a distribution
Same way to look at it
The
independence is across different
realization of or rather different
random variables
Right And uh not across the data
dimension These are the points that I
want you to understand and know Okay
Okay lets let me take questions now
No independence is not interpret
Identity is interpret Sorry implicit
Not independence
See independence only makes sense if
you have multiple random variables If
you have one random variable
then there is no need to actually even
either even Okay I think I I should
correct myself If there is If you see
that as multiple realization of a single
random variable then you neither have
to talk about independence nor you have
to talk about identity because theres
only one random variable and n
realizations of it
In the other interpretation you need
IID because you have n random variables
defined on the same sample space All of
them are identically distributed and
statistically independent
Make sense
One realization each of multiple random
variables all of which have exact same
distribution and which are all
statistically independent Yes
The other one was n realization of one
random variable
IID at all
Yeah
Yes
Anything else
Of course Of course So basically
saying you know all of your patients
are going to the same hospital or using
the same machines See again this is
for This is up for interpretation Okay
this is a good question that you made
See
uh typically what happens is lets say
that you are you have two data sets
Okay One which is which contains images
of human faces The one that contains
the uh images of buildings lets say
Now
do you want to see them as uh same
underlying sample space or same random
experiment or not is a design choice
Suppose typically what happens is you
know suppose you take a data set that
has uh the human faces
and build an algorithm
Okay And try to test it on the building
images it wont work because by
assumption youre youre youre uh
youre uh by construction youre
assuming that
the random variables are identically
distributed So when you get when you
get the building image
your assumption breaks
However
suppose you know you combine both the
data sets and build an algorithm
together You can see both of them as
the outcome of the same uh random
experiment So thats design choice
So thats why
if you include all data in the world and
create a data set
theres no non IID Thats exactly what
the current LLMs are doing you know
So I joke always
that if you can
learn a I mean or construct a lookup
table for the entire universe and come
up with a good hashing function then
machine learning is a solved problem
All you need to do is learn a huge
lookup table for the entire universe
So if you look at you know petabyte
scales of data and combine all internet
you know for all you know
you might be learning a you know
creating a big lookup table
Anyway so point is
what do you want to call as your data
set is your design choice
Okay But most you know uh
often than not what happens is you
start with a data set
But mathematically speaking when we
design algorithms as you will see
later we will use these uh these
properties that we have uh imposed Now
well use the property that these are
statistically independent and well use
the property that they are identically
distributed
But it is up for interpretation
Or rather rather it is up for uh the
construction Now you construct it the
way you want But
ensure Make sure that you know uh the
the so called test data Ill define
what test data is
Uh assuming that you know what test data
is You know basically you know this
is this is data that you build your
algorithm on You have new data that you
want to predict upon right Youll have
to ensure that that also comes from the
same distribution
Because you have made this assumption
implicit Because you will be estimating
the underlying distribution anyway
And if you if you
start you know uh giving your
algorithm points that have not come from
this distribution the algorithm is
deemed to fail
Now uh one one request that I have is
use
the precise terms that we have defined
you know So what is similarity All we
are saying is that
by construction or by assumption you
know whenever you make an assumption
that your training and test data comes
from the same distribution Thats the
way you construct the algorithms Thats
it
Yeah
Anything else
Yeah
Good question Very good question Uh
the question is what is the intuition
behind you know combining uh or rather
taking
interpret interpreting the data and
label as two random variables you know
Why not see that as one single random
variable and deal with it
Mathematically you can
Right But
actually you know I I I was going to
say that later but now that you asked
me Ill tell you See people
typically design or not give
nomenclatures to problems So when you
Suppose you have a problem where you
have data and some labels
people call that as supervised learning
Okay And suppose you have only data and
no labels Honestly I dont understand
what that is Precisely because of the
point that you asked
To me
it is some random experiment thats
happening and some random variable
sitting and you want to
estimate the underlying distribution
Now how does it matter if its a label
or data or anything But
historically there has been a a
nomenclature that people have made You
know for instance okay there is an
image and somebody says that So what
happens is the following right I mean
to be fair to people who did it
see
an image or typically data points are
uh humanless measurements
In the sense that uh some machines make
an assumption You take an image and
there is no human that is involved But
when you apply a label there is some
human judgment that comes in you know
Thats why you want to see that as a
different random variable
But
Ill tell you there is a uh there is a
uh
a field of subfield of machine learning
called self supervised learning
All they do is they take a few
dimensions of data
and call that as a separate random
variable and estimate the conditionals
there
Its only an interpretation issue
Thats why I told you I dont like to
call algorithms as supervised learning
unsupervised learning and all that
Okay But
but people do take that nomenclature
They call this Y as label
Now why So Ill tell you one other
interesting thing Now that you asked
that question suppose there is an
image okay
Okay And my problem is you know we
know that some some of the pixels of
this image is bad for some reason Its
some old picture and some
And the task is to
uh find out what these what these miss
miss missing pixels are
Okay This problem is called inpainting
by the way
Inpainting So you have an image and
you inpaint it right I mean now
nowadays some of these you know
state of the art models right Uh they
can do they can erase a a background and
they can add things These are all same
problems
So now what is the label here
The missing pixels So when you take
data how do you train such kind of
models You take an image randomly mask
some of these things
and ask it to reconstruct it back In
that case you know there are
the the data some of the dimensions of
data itself can be seen as the label
That is precisely why I did not start
this course by saying that machine
learning is divided into three parts
called uh supervised learning
unsupervised learning and all that
Thats not what it is To me a sample
space a random variable
you want to see that as two different
random variables call one data call
one labels That is why you know if
you look at my writing
see typically a label is taken to be
another random variable defined on the
same sample space You dont want to
call it label you dont call it label
And by the way now that he has asked
the question
uh problems or algorithms where label
exists are called supervised learning
Really Okay Problems where the label
does not exist are called unsupervised
learning
And problems where some of the
dimensions of data itself is made as
label is called self supervised
learning
Very pseudo
distinction right Now you see why
generalization helps
Okay So typically that is how it is
written Okay Yeah Good that you asked
that question I would have anyway told
you that
No it does not See Ive still not
defined what ML is
Okay Maybe some of you have the lot of
curiosity right now Ill tell you See
finally it comes down to what is the
distribution that you would expect Ill
tell you what happens is all machine
learning is this Given D estimate P
Thats it
All machine learning is given that you
have sampled from an unknown underlying
distribution estimate the underlying
distribution Thats the problem
And the end rest of the course is simply
to estimate that In fact this is
discriminative machine learning
Generative machine learning is you not
only estimate the underlying
distribution but also learn how to
sample
Thats it
The problem is given D estimate P
Now
you can estimate multiple Ps You know
for instance you can estimate the
conditional P of Y given X Then this is
a classifier
Okay And if Y belongs to RK its
called a regressor
If Y is discrete its called a
classification problem
And if you estimate P of X given Y it
is called
conditional data estimation problems
Okay If you estimate PXY its called
generative problem
But basically given this you estimate
marginals conditionals joints and
learn to sample Thats all machine
learning Guys Im Im formally
defining that in a while
But that is why I I want you to
understand this
Hello
Random experiment sample space random
variable distributions Thats it And
we have samples from these
distributions And you do 100 things on
top of those distributions
Makes sense Yeah
Any questions Any more questions Yeah
So can we now also define notion of
something as good label space and
Good label space
Uh
no you cant No What do you mean How
do you define a good label space Like
label can be anything
So
how can we say that
some label is a good
descriptor of
See that becomes you know too
philosophical a question to answer
Now the question that youre asking is
what is the good way to
divide
labels I dont divide images divide
society divide people
Divide anything So do you think men
and women is a good label
Or do you think that you know
whatever right You know people have
divided things into based on any random
Thats why you know I keep saying
that this notion of label is very very
very
Good that you asked that question You
know its extremely synthetic in most
of the good times
Thats why I keep telling this
See
to even fly an aircraft you know which
is an engineering marvel
all you need is a four five parameter
model
Newtonian mechanics will take care of
your aircraft And its only three four
parameters is all you need to estimate
Kalman filters and particle filters
Thats it
But to identify whether a picture is
that of a man or a woman you need a 100
million parameter model Why
Because the idea of
semantics is very very
pseudo
See nature is simple
You can fly an aircraft only by using
four five parameter models
But to identify whether somebody is you
know something is a spam or not you
need a 100 billion 100 million parameter
model Because the idea of spam keeps
changing
Thats why one of your assignments will
be the following Ill give you some
random data set and ask you to randomly
label it
And train a neural network to solve
that It will solve with 100 percent accuracy
That only shows
how fragile and meaningless human
divisions are
I actually made this experiment I have
a 3 year old son right
So
whatever whatever image that we identify
as two three or something you know
jumble them and give them give some
random label to them They will learn
it
Right So thats all I mean see
as engineers we are not concerned with
philosophy
Our job is that you are given something
somebody has labeled it asked to ask me
to give an algorithm that would do this
We will do this Thats it
Okay
Just a question Like you said about the
jumbling of the of the numbers and
giving it any random label So like
that randomness is across every time if
three is coming we are giving the
random label or every time that label
becomes constant like if three we are
Too philosophical So what do you mean
by three Like three is one of the
numbers I dont know When Im
labeling I dont know if that is one
number Like this particular shape you
are giving it label
Very good Every time No two
images are same Yeah thats it
 So I decide to label them So you give
Suppose there are 100 images You give
them 100 different labels You can You
can make a machine learning model to
learn it
Understood
See thats the whole point that I am
trying to make So the idea of
similarity is very very
Its a pseudo idea
You can see every image as different
So somehow we have learned to uh
Okay So Ill tell you now that youre
asking
Hold on
What is this number

 Five or eight
It looks like six You got the point
Thats it
Just like what youre predicting like
when youre See the
learning The algorithm will do
something Yeah thats what The
question is you can make the algorithm
learn anything
That is That is the point
 Accuracy part you said like Uh you
define See
you Again we have to define accuracy
metrics right So now we have That we
will define So thats why we need a
test data We will say Okay is this
matching with them All that we can do
Right But the idea is that okay
Any other question We are actually
running out of time
Yeah
Uh so uh can you distinguish between
like the first D dimension within the
same lets say the pixel
and then this like two different set of
random variables
The D dimensions and then Okay By the
way uh this is only an interpretation
The way you interpret is the way I mean
you can see that See if you want this
pixel thingy right I mean image
youre looking at
The dimensions of data are different
pixels in the same image
In the constant Im saying how it was
different Lets say we defined IID Uh
in in IID we are never saying that the
independence is across data dimensions
We are saying that the independence is
across data points
Rather you know we have N data in in
the interpretation So okay See this
IID thing only applies if you look into
your data set as one realization of N
random variables right Because there
are N random variables we can talk of
statistical independence among those N
random variables So we have N cross D
random variables
If we view this Yeah Yeah Yeah I
mean if you if you want to see all
random variables as scalar random
variables then you have N cross D
random variables Correct
Amongst which
there is statistical independence
amongst set of DD random variables or
rather Yeah D dimensional random
variables not across the scalar
dimensions Thats the way to look at
it Yeah
Sir sir this idea that the test data
should come from the same distribution
its sampled Sir isnt it
self defeating Because this can lead to
overfitting anyway For example the
tumor problem that you said We dont
want to learn the tumor classification
from a particular hospital or particular
experimental conditions Hold on to that
question We have the entire course to
answer that
Good question Hold on to that question
Yeah
Anything else
Earlier when you described the joint
distribution function you said youre
using small lower case X1 X2 Was it
because you took a particular case of
small A and small B
No Yeah Good that you reminded me of
that Uh see I said that each of this
is a D dimensional random variable
right
So each of the dimensions I represent
by lower case later in the course
Each of these XIs are X1
X2 X3 X4 up to D So thats why I
wrote the scalar random variable as
lower case See I will soon run out of
happen So lower cases are for scalar
alphabets I told you So that will
valued random variables and
upper cases are for vector valued random
variables And in general my random
variables are always vector valued
Okay So I think lets stop here Uh
just a couple of minutes
Uh I mean I wanted to actually define
the problem okay Uh which I will
Maybe Ill just do it right now
Give me 2 minutes See all
problems
in machine learning
can be seen
as
given D sampled from an unknown
underlying distribution PX
See note that Im writing PX here not
XY because you can combine that Y also
in this X Doesnt matter PX
Estimate PX
And sample from it So
estimate PX
or
conditions conditionals over it
This is it
So given that you have
in realizations of uh
random variable with an unknown
underlying distribution estimate the
underlying distribution
and learn to sample from it I mean you
dont have to learn to sample from it
all every way every time So sampling
is the generative modeling problem You
dont have to learn to sample either
estimate the underlying distribution or
some conditional or marginals on top of
it
and learn to sample With this we
conclude this particular session on
basics of probability theory Now that
we have defined everything that we need
uh to go to the actual definitions of uh
the machine learning problems From the
next class we will start with
defining rigorously what the problem of
machine learning is and look at
the algorithms for machine learning one
after the other Thank you for
attending
