---
id: ihkGbIdbbxc
title: Lec 12 Kullback-Leibler (KL) Divergence
url: https://www.youtube.com/watch?v=ihkGbIdbbxc
date: '2026-01-28'
duration: 16:49
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome back Now remember what our
objective was or our objective was to
quantify
the distance between a pair of
distributions Now this entropy sure
will give us the average information
contains contained in a particular
distribution Now how is this related to
what our objective is So let us define
one other term Okay Suppose
px and qx
are
two distributions
Actually theres a slight abuse of
notation here See here I this this P
was probability the probability measure
Here this P is the
 mass function mass function because we
are looking at a discrete random
variable
Okay And uh yeah so when I write P and
QR two distribution Im talking about
mass functions again So we have to be
careful about that I mean now we are
looking at uh discrete random variables
because uh for conditional random so for
continuous random variables theres
something called differential entropy
which looks similar mathematically but
interpretations are slightly different
but anyway suppose p and q are two
distributions
to compute
lets say that we compute let me just be
clear about the definition
Ill tell you why this thing what Im
writing is not symmetric so suppose I
look at the expectation of
two distributions on the same sample
space Again right on the same sample
space
It goes without saying
Let me go to the next page
Define
expectation of
negative of log of
qx This expectation is computed with
respect to px
Okay
What does this give you So negative of
log of Q of X will give you the
information or surprisal associated with
the events under the distribution Q
Correct
Right Now if you take expectation with
respect to PX then what am I saying Im
saying that my actual samples have come
from px
but Im estimating px to be qx Now if I
do that then what is the average
surprisal that I get If I take if I
consider that my true distribution is uh
is qx or rather if I if my true
distribution is px while I consider that
the samples are coming from qx
Does it make sense The other way to
interpret this is that what is the
average information that qx contains
with respect to px
or about px Suppose px and qx were the
same then what happens This will become
the entropy of px Now if px and qx are
not same they are two distribution two
distributions then this quantity is
telling you what is the average
information that one distribution
contains
about the other
See suppose I take my qx to be a gshian
distribution with mean three right and I
take and my px is a goshian distribution
with mean zero while the samples are
actually coming from a goshian
distribution with mean zero Im wrongly
thinking that my samples are coming from
distribution with mean three right I I
compute surpris results for all samples
and then take an average
what am I computing Im computing what
is the information that q contains means
with respect to P or rather what is the
mistake that I am incurring by wrongly
making an assumption that my reality is
Q while it was P
okay okay
so you can interpret it in multiple ways
and this has a name okay this is
actually written as H P comma Q what is
this called this is called the cross
entropy
Okay And by definition cross entropy is
not symmetric
You see this h of p comma q is not equal
to h of q comma p by definition
Okay You observe this Now
again going back to our original
objective Our objective was to define
distance between distributions Consider
 small
 uh again this is notation of misnome
will be there Okay So these are uh
mass functions for no discrete random
variables and mass functions Okay
Consider
take entropy of P and subtract it with
the cross entropy between P and Q
This will be
let me just get the math right
uh px
log px
plus
uh px
log
qx
And the reason Im staring at it is its
asymmetric right Because it is
asymmetric If I write it the other way
if I write HQ and P youll have a
different expression altogether But
anyway it doesnt matter Okay Now
what is this expression telling you
Lets interpret this right So this
will tell you the average information
the entropy of P is the average
information in P Right Cross entropy
is the information that Q has about P
If I take the difference between those
two what am I looking at Im saying
what is the error that I have incurred
by wrongly choosing Q over P or wrongly
choosing Q while it it should have been
P or the extra bit of information that
is there in Q and not in P
Make sense What is the difference
between the entropy and the cross
entropy It is telling you that if I
look at the average information in P and
the cross entropy or the information
that is in Q with respect to P subtract
them both Ill get the extra
information that is there in Q which is
not in P Make sense Right So now that
is equal to
just use the definition of uh logarithms
just log uh
Correct
This is what it is
Now suppose P and Q are the same then
what would this quantity be It will be
zero Suppose P and Q are very far away
from each other What would this
quantity be It will be high So
take two things as homework Show that
this quantity is not symmetric
Okay So let me write this quantity as
by the way this is what is called as the
K divergence
equal divergence between two
distributions So this is this is you
know the what is to be shown is that to
show
that DKL
of between P and Q is not the same as KL
between Q and P
Okay and also show that this is non
negative
and show that this is
equal to zero if and only if P matches
with Q Its a two sided result
Okay So please take I mean this is use
the definitions and use the law of log
logarithms and uh the the definitions of
density functions youll get it That is
how you do it take it as a homework and
do it
Now we got our objective right We were
looking at a measure that would tell us
how far or close a pair of distributions
are and K divergence is one such
measure And also you can show that this
is uh not a metric in the sense that
this does not obey the law of
triangularity Why Its obvious right
If its not symmetric
if its not symmetric if a if a metric
is not symmetric then itll it cannot
satisfy the law of triangularity
Okay lets show that I mean its
pretty simple to show Oh anyway So
this is not a metric in the sense in the
strictest mathematical sense Okay but
it gives you a sense of the closeness
between pair of distributions Its
called a K divergence
Okay So a a similar uh definition
exists for the case of continuous random
variables and as I said uh we assume
that most of our uh data is continuous
right in most of the time So Ill also
give you a similar definition So this
is called this differential entropy and
differential cross entropy right so
which is x is the definition of
k divergence
for continuous random variable cases
looks very similar to the discrete case
The only thing is these are density
functions now okay and cannot be
interpreted as probabilities but yeah of
course they are density functions

right
P and Q the kale between P and Q here it
was between Q and P so its P log Q by P
here it is P log P by Q
uh did I make a mistake
No its the same thing See this will
stay the same See HP minus H Q minus
P
Sorry Q P See HP minus H Q P See
only the cross entropy term changes The
entropy term does not change
 So if its HQ P what will happen
P with respect to
 Q Right
Hold on Let me just uh confirm it once

P and Q is uh
my my bad I think the mistake is that
it is the difference Okay Ill just
change it this way The minimal changes
difference between the cross entropy and
entropy
Okay So in this case what happens it is
uh
because of this asymmetry theres always
a question hold on
hold on just give me a second Ill
correct

 See uh cross entropy this is P and Q
this is correct So HP and Q is
expectation
this Yeah
This is
this will become
So H P is uh P log PX This is uh the
cross entropy
minus entropy Ah okay Fine I think
theres a theres a minus here and a
plus here right And this will make it
P by Q Okay correct
Yeah
 Yes Yes Yes This is the KL between P
and Q Correct Thanks for that
Difference between the cross entropy and
entropy Its because of the asymmetry
right So this algebra does not work
out Okay Thanks for that So this is
not asymmetric and so on Yeah So now
the definition falls right So its P
log P by Q Correct Okay
Any any other questions here
No this is not this is not cross
entropy No this is the difference
between the cross entropy and entropy
HPQ is the cross entropy HP is the
entropy So were looking at the
difference between the cross entropy and
entropy
 No test it out Yeah it should be the
difference between cross entropy and
entropy
So now this Im also saying one other
thing Im also saying the cross entropy
is always higher than entropy No
more information
 Yeah So that that should be the case
because if if these two match match is
always upper bounded by or it is lower
bounded by entropy always
see thats why you need to take the
difference between see when I said
difference
HP minus HPQ or HPQ minus HP both of
them are differences but to ensure that
its non negative because by definition
cross entropy is uh bounded by entropy
youll have to ensure that you take the
higher and subtract the
Thats only definition Okay Fine So
for the continuous random variable case
the K divergence is defined this way
Okay Any other questions here
So you would have heard about this No
to erase human Its becoming more and
more prominent these days
The more the mistakes that you do the
more it is proven that you are a human
being and not an AI
anyway Okay Sh Yeah
 Huh So for uh distribution functions I
use capital for mass and mass functions
For density functions I use small P and
Okay Uh we will stop here and continue
in the next lecture
