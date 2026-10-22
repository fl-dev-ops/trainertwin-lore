---
id: DaBw9qBpt2s
title: Lec 03 Recap of Probability Theory - 1, Part 2
url: https://www.youtube.com/watch?v=DaBw9qBpt2s
date: '2026-01-13'
duration: 14:30
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 03 Recap of Probability Theory - 1, Part 2

## Transcript

speaker_1: So now you have the probability measure
So what do you do with this Uh youll
have to finally solve that problem of as
I say as as he asked where does it fit
in the entire the machine learning
framework that we are looking at
Proist realized that you just cannot
stop at this So finally what we have is
we have this famous triplet which is
the sample space
the events F and the
probability measure P
This is called
trip probability triplet Right The
probability triplet
In fact the analogy is you can start
from real real numbers
take a subset of real numbers and assign
a measure to it Thats another triplet
R subset of R and length measure Thats
another triplet
Make sense Okay Now we cant stop here
and you know we need more uh tools to
deal with what we are uh what we are up
to because remember that I told you that
the sample space its is pretty abstract
it need not have numbers
correct however
we as engineers need numbers
because we can crunch numbers we can add
them we can subtract them you know we
can do algebra on top of it and all
Unless we have numbers we cannot deal
with things You know we we cannot
again its I mean its its sort of uh
Im contradicting myself when I say that
you need to look at abstraction and then
I say that no you cant stop at
abstraction You need to measure
something and need something concrete to
make something work
So think abstract
as they say no think analog act digital
think abstract
act concrete So your thinking has to be
at an abstract level right So just
thinking that the hunger in the world
has to go away will not make anything
Youll have to act for it So now this
this transition from the the abstract
space of sample space event space and
probability measure to something that
can be measured No that can be measured
not in the in the see okay so Im
overloading the term measure See
measure is a mathematical construct when
I say probability P is a measure Its a
function basically right
now when I I Im also using the word
measure in the sense of you know the
colloquial English word measure If you
want something to be lets not call it
measured you know some lets call it u
uh
what do you do with a sensor actually
measure
 detect or observe
 detect or observe or something right
yeah so if you want to do that on top of
abstraction you need something else Ill
tell you Ill tell you uh the if you go
back to our analogy of uh the x ray okay
somebody got a disease right somebodys
lungs developed a nodule and you know
they went to I mean that itself is a
part of our sample space Remember
somebody developing a lung nodule itself
is a part of our sample space and they
coming and standing in front of the
machine and all that happened and some
and something came in the sample space
We dont know what the elements are
However if you want to work we need
something that is concrete or observed
at detected Now how do we do that
Typically we use sensors
to connect the the abstract world to the
real world We use devices or sensors
and we make measurements
Okay in this case we get an image we
get an X ray and we store that on a
computer and what we get is a vector at
the end of the day Now you work with
vectors
practically you work with vectors
but you started everything from an
abstract sample space What is the
connect between these two
You understand What you work with are
numbers vectors but what you have as
an abstraction is something that is it
is only a that may only be a a mental
construct So you need something that
bridges the gap between these two And
thats exactly what a random variable
does
A random variable converts
the abstraction of sample space to
something that is concrete which is
real numbers
Okay See when we hear this term random
variable for the first time we rather
underestimate it and say think of it
like something some esoteric thing
right Oh theyre talking about some
variable and all that Its its its
needed I mean Im saying that its not
that somebody just came up with this
idea It it is it it was defined because
you need it Lets define it formally
So there is the sample space
omega But what we operate on are real
numbers right Thats the motivation
So what we do is we define a function
X
Okay So this is called the random
variable
Random variable is a mathematically its
a function So what function is it We
know what functions are right
Functions are mapping between two sets
Now what are the two sets that we are
considering here Okay define a
function X from
the sample space omega to real numbers
R So X is a function that starts from
take elements of the sample space and
maps it to real numbers Why do we need
this I hope that all of you can really
appreciate this fact that we need
another function on top of sample space
to work with We cannot stop at sample
space
Do you see that Why Because sample
space is very abstract You know we
cannot do anything with head head or
tails We need numbers
and we need something another function
that would map the abstraction of sample
space onto something that we can deal
with which are real numbers and thats
the function that we call as random
variable
Hold on I Ill take questions Now
random variable is neither random nor a
variable
Its a deterministic function
I dont know who named it a random
variable Its the you know biggest
misnomer of the world
At least one of them should have been
meaningful No So call it random
function or or deterministic variable or
something They called it random
variable Right So I dont know where
this name came from anyway It came from
somewhere
 Why cant the name
 Yeah Huh
 Why cant the name
 too small to do it
Theres nothing in the name anyway
right So it doesnt matter Call it
anything So all of you I want you
people to understand two things one
appreciate why you need another function
on top of sample space Why cant you
just stop at sample space Thats very
very important Its the key And also
appreciate the fact that the function
that we that we uh that we define and
use it in practice is what is known as
random variable which maps the elements
of sample space to the real numbers
Okay any questions on definition
Is this a common way to say that measure
any measure on a given sample space
 No I Im still not talking about
measure here This is simply there
exists a function from sample space to
real numbers
 Hold on hold on We we what happens the
question that you should be asking is
now that there is a function that we
have defined from sample space to real
numbers what happens to the measure that
we have defined on the sample space the
subsets of sample space in this in this
new formulation right and well come to
that its called a push forward measure
well come to that in a while it gets
transformed and thats exactly what we
call as a distribution function
well come to that
 whyange needs to be R
 need not be R in general it can be
anything it can be
integers as well but generally you take
you consider real numbers in fact thats
a very good question that you ask the
question is why should it be R
in most practical cases it
dont it wont be R it would be RD it
would be a D dimensional real space
right so because its like you know you
can see uh other sets are subsets of R
right You generally define that as R
The range space of random variables is
typically taken to be R
 Yeah well trace that trace that back
Yeah it will be the its our data
basically right Well come to that in
a while
Any other question
Okay
Now yeah So lets start with R No I
dont want to overload the I dont want
to create cognitive overloads now So
lets say that we are looking at R for
now So sample spaces to R
Um
perhaps I should so because we are
looking at that image example right So
in the image example what would this
this function be So I told you in the
last the last time that every image can
be seen as a point in a dimensional real
space Right Right So in that case so
Ill generalize this notion Right So a
random variable is a function from
sample space to the d dimensional real
space Its better to generalize it
Okay So now what what is what is an
image now So you can see the image as
the element from the range space of the
random variable
which has been defined on an underlying
sample space
Do you see this
What is a data point Now what is an
image that we have An image is an
element in RD
that we know that Y is an image is an
element in RD that we just did that
scanning and its its a point in RD
right now what is that RD this RD or the
Dimensional real space that we are
talking about is actually the range
space of a function
what function are we talking about its
the random variable
okay what is this function defined on
what is the domain of this uh of this
function
 the sample space and what this sample
space is uh is is is is talking about or
rather denoting its the underlying
experiment So whenever I say that you
have an image with you this entire story
has to come in your head
You got it right So every data point
that we see which is a dimensional
vector Now in the in the deterministic
viewpoint it was a vector in RD In the
probabistic viewpoint it is an element
from the range space of the random
variable that has been defined on an
underlying sample space that we dont
have access to Only images that are
stored in a folder which set is that
 every image is this Every image is one
element in RD
You missed the last class
Dont miss classes
 So I know that an image can be in RD
But
 image is in RD not can be An image is
always in RD
We I want you all of you to see an image
as a point in RD always
Okay Now what is this in in in the last
class in the deterministic treatment
its an element in RD In the
probabilistic treatment it is still an
element in RD but this RD is the range
space of an underlying function and that
function is a random variable and that
random variable operates on a sample
space and that sample space is generated
from a random experiment This is the
story
All of you are clear so far
Okay
 Is the random function because every
point from the sample space has a
 I leave this as an exercise Good
question The question is is random
variable a bjective function Its an
exercise
This is not a course on probability
theory right But its okay Yeah
Good Its actually a good question
Think about it Yeah
Anything else
Okay Now now that we have defined
Okay See uh this should this is the
difference between
knowing something precisely and knowing
you know handwaving stuff See when I
say that oh I have an image X I right I
have 10 images and all each image is a
is a point in is a vector in RD which is
true but know to truth has multiple
layers The moment I talk of
distribution functions and probability
I should know that there exists an
underlying sample space and the
measurements that Im doing are actually
elements of the range space of the
underlying function that is called
random variables
Got it Yeah Okay So now that we have
uh uh uh we have defined a function on
the sample space uh omega what happens
to f
So we have RD
What happens to the subsets of sample
space under this function
What are those called
 They are called boron sigma algebra
As I said no it sounds very
complicated
Its not See what happens is the moment
so under the x under x what happens is
sigma gets mapped to rd
and f
gets transformed to the sigma algebra
which can be roughly again you know uh
a mathematician would would scold me for
this but you know a sigma algebra is not
perfectly a subset but lets say that
its Its roughly corresponding to the
subsets of RD Okay Now what happens
to the probability measure So we had a
probability measure P
What happens to this
