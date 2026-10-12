---
id: joL7g6DSxPU
title: Lec 36 Max-Margin Classifier and SVM
url: https://www.youtube.com/watch?v=joL7g6DSxPU
date: '2026-02-25'
duration: 43:45
model: youtube-captions (en-orig)
transcript: true
---

# Lec 36 Max-Margin Classifier and SVM

## Transcript

Okay. So, welcome everyone uh to this
lecture.
So far we have seen empirical risk
minimization and the framework of
regularization.
The summary of the discussions that we
have had so far is that by changing the
loss function and the regularizer
one can
impose certain type of behavior in the
hypothesis that we are looking at. So
that is the uh moral of the story so
far. You change the loss function and
you impose a particular type of
regularizer on top of it. The kind of uh
classifier or the hypothesis that erm
outputs will be different. So this is
the the general philosophy of how ML
algorithms are designed. Regularizers
can come in multiple forms, right? One,
you know, you change the architecture or
you know you what do you mean by
architecture? the class of functions
that you choose from to build the
hypothesis is your architecture. You can
change that or you can add an explicit
regularizer in in in terms of a
constraint in the optimization problem
or you can per up the data uh with some
noise and so on. There are multiple ways
to add regularizer but the fundamental
idea is that if you want to observe a
particular type of behavior in your
hypothesis function
you change the loss function and or
regularize right when I say regularize
it also means that you change the
architecture changing the choice have
making a different choice for the
hypothesis is also a regularization as
we saw right so pick a classifier uh
class pick a class of functions uh which
come which
which will form the hypothesis space.
Within that space, you solve an
optimization problem with a a loss
function by adding regularizer and you
had add different regularizers. You
choose different hypothesis, different
kinds of behaviors are seen. That is
what we have seen so far. So we'll
continue this thesis okay and uh look at
many other choices for the hypothesis
function. one significant choice that is
made is these class of functions called
neuronet networks which we will see
later.
Now for the sake of completeness and uh
the elegance that this particular
algorithm brings in we will look at
these uh classes of hypothesis which are
called max margin classifiers. Okay,
of which support vector machine is a
member.
So support vector machine uh is an
extremely elegant way of formulating
hypothesis function. In fact remember uh
in the beginning uh initial lectures I
told you that one of the central
problems in machine learning is to
relate the minimizer of the true risk
with the minimizer of the empirical
risk. Right? Support vector machine
gives an elegant mathematical
formulation of actually bounding the
empirical risk in terms of bounding the
true risk in terms of the empirical
risk. So this will these classes of
classes of results are called sample
complexity results where the true risk
okay is bounded as a function of the
empirical risk and the number of samples
that are used for the training. Now that
that was a very strong result because
one question that often gets asked is
that how many samples do you need in
your data data set to achieve a
particular accuracy.
Right? So this question is a question on
true risk
because if the question were of
empirical risk then we already know the
answer because you know we can overfitit
on data on the data that we are given
but the actual question is what can you
say about the empirical sorry the true
risk having performed an erm on uh the
data that you have been given. So if
there is a result that relates the true
risk with the empirical risk that is a
very strong result right and support
vector machines is one class of
algorithms that actually gives a bound
on true risk in terms of the empirical
risk and the number of data samples.
However um I mean that is why it is so
powerful right I mean in the sense that
you can theoretically guarantee that
your algorithm is going to have this
performance on unseen data as well. But
unfortunately what happened you know
historically is that uh these algorithms
did not perform very well on very large
scale of large scale data in high
dimensions that that was an empirical
observation that was made and for the
kinds kinds of algorithms or the
hypothesis functions that are used today
in modern ML which are neural networks
you cannot come up with sample
complexity bounds such as SVMs. So
that's why the question of what is the
uh the number of samples that are needed
and what are can you give a theoretical
guarantee on what would be your
performance what would be the
performance of the classifier based on
neural network on unseen data cannot be
theoretically answered today because of
lack of such sample complexity bounds
for these kinds of transformer based
models. However SVMs do give such a kind
of nice formulation. So I mean in
today's scenario max margin classifiers
or support vector machines are are
seldom used in practice right but this
philosophy that by changing the loss
function and having placing a very nice
regularizer you can impose a good
behavior on the classifier is what the
take-home message is when we look at max
margin classifier and for that sake we
will look at the max margin classifier
in its entirety uh for a couple of
classes now right and then before we
move on to the neural networks. Okay. So
let us look at uh max margin classifiers
or support vector machines.
>> [snorts]
>> Okay. So let us consider a binary
classification problem to start with.
I will start with the simplest of the
formulations and then we will keep on
increasing the complexity. Consider a
binary classification problem.
So we have uh uh x
data that is in RD and uh
y
we have been using symbols 0 and one to
denote classes so far. Uh here I've used
minus1 and one for a particular purpose.
You know algebra will become easier if I
use minus1 and one. Doesn't matter as
you know right? I mean these are just
two symbols. So let's say that the the
output classes are minus1 and one. Okay.
Now let me introduce uh you to a concept
called uh discriminant functions.
See the recall that
[snorts]
that for some cases
of class conditional densities
densities the classifier
will take this particular form. Right?
Right. So there will be it will be one
if
I had asked this as one of your
questions right in your exam that for a
particular case of class conditional
density a binary classifier or the
optimal classifier will take this
particular form okay where
g of x is
function of x right
so it's actually uh you have this to be
a function from rd which is x to
r
okay
and in the okay actually it's not for
some cases of class conditional
densities, right? In fact, uh um
can actually say that uh
a binary classifier
any binary classifier
can be represented
as follows. Actually this is in general
any binary classifier can be represented
this way right uh we used classes as one
and minus one right so we can take it as
1 and minus one here one if g of x is
greater than zero and minus one
otherwise so this function g of x is
what is called as the discriminant
function
okay [snorts]
now for the case where uh the class
condition densities are gausian this
discriminant function will become linear
there's no need why this discriminant
function has to be linear in general any
any function but for some cases this
discriminant function will be linear
correct
so let's let me take an example okay let
me write that for
some specific cases
specific cases of
class conditional densities
g of x will be linear.
The reason I'm talking about linear
decision boundaries is that uh we will
start the max margin classifier the
formulation by assuming that we have a
linear discriminant function and then we
will uh generalize that to nonlinear
discriminant functions. Okay. So what do
you mean by having a linear discriminant
function? Let me show you an example.
Suppose uh x is in r2
uh y r2 this is what I can write
-1 and 1. So
let's say that I have uh two classes
like this.
This is uh all x such that y = minus1
and this is all x
such that y is equal to 1. So what are
these axis by the way? These are axis of
the data dimensionality. Uh what was the
symbol that we were using
supererscript right? This is x1 axis and
this is x2 axis. So every x is
of the form x1 comma x2 right
[clears throat]
you have to access and this is how the
data is distributed okay now in this
case uh
there is a discriminant function g of x
let us write that
it's a linear discriminant function this
is g of x that's equal to some wranspose
x
I can also add a bias term here plus b.
So this is an example of a linear
discriminant function. So finally the
classifier says that if my x is on the
the upper side of g of x then it belongs
to one class and it's lower side of g of
x it's one other class. What do you mean
by that? There is a line and if [snorts]
the data point uh falls above the line
it belongs to one class below the line
one other class and you understand what
above and below. So mathematically
speaking all we are saying is that if
when we compute this h of x right it if
if uh if for that particular x if g of x
is greater than zero then I I classify
it as one point and the other you saw an
example for this in your exam. And so
this is exactly what I'd asked for
for uh in that first question, right?
You have to show that under a specific
condition, you will have your classifier
with this particular form where you have
a linear discriminant function. Make
sense? Right? So this g of x is called
discriminant function. And if this
discriminant function, you understand
what a discriminant function is, right?
So there is hypothesis classifier. If
the classifier decides based on a
function of data that particular
function is called the discriminant
function and uh in a specific case where
this discriminant function happens to be
a linear function of data it's called
the linear discriminant functions. Okay,
we will start our treatment by assuming
that uh the the classifiers that we have
uh have linear discriminant functions
with it. So that's the easiest way to
look at it. Okay. Right. Now with this
let me define uh another idea which is
called linear separability.
A data set D
is linearly separable
if and only if there exists a W and B
such that
Wrpose X + B is greater than zero for
all X such that
for all X I such that yi is equal to 1
and wrpose x i + b is less than zero for
all x i that yi is equal to minus1.
You understood what is it right? So if
there exists a linear discriminant
function which would end up giving 100%
accuracy on some data set then that set
data set is called as a linearly
separable data set. That's called linear
separability
that you can always find a line okay
that would uh give 100% accuracy on the
training data or whatever data that we
have. If such a data set exists then
that data set is called linearly
separable data. Is that okay?
So for for instance whatever I have
drawn here is linearly separable because
you can find a line uh that that can
separate this.
Okay. So here is the question. Suppose
data is linearly separable. How many
discriminant functions can exist?
>> Infinite. Right? Yeah. So that is
something that you should keep in mind
because uh we will talk of uh uh uh an
optimal
uh discriminant function. So that is
what we are going towards right. So how
do we come up with an opt given that
there can exist infinite discriminant
function is there a way of defining
optimality?
Okay, that is where we go. But yeah but
you understand this right? If data is
linearly separable then then there there
can exist infinite discriminant
functions. Okay. Okay. So let us now ask
that question. [snorts]
Scroller is linearly separable data.
We'll have
infinitely many
discriminant functions.
question.
Is there a
an optimal
discriminant function
among all possible
[cough]
discriminant functions is the question.
One can define optimality in multiple
ways, right? I mean maxin classifier or
support vector machine is one way to
define optimality. So that is what we
will look at. So given that data is so
now please note that in practice data
will neither be linearly separable
right nor be even uh separable that way
right uh so now the question is even if
you have a nonlinear discriminant
function uh can you guarantee that it is
separable under some any function is a
question which need not be the case.
The most general generalized version of
a max margin classifier does not put
these constraints. No, it it it it it
assumes that data is neither linearly
separable nor separable under any other
constraint. Right? But for the ease of
uh formulation, we will start with the
case by assuming that the data is
linearly separable. Okay? And then we
will increase the complexity of that.
Okay? Now
right,
let's consider optimality
via
maximizing the margin.
Okay, let us look at this
now since Okay, so consider linearly
separable data.
Now since it is linearly separable.
So there exists an epsilon
that is greater than zero
such that
wranspose x i + b is greater than
epsilon
for all x i such that yi = 1 and wrpose
x i + b is less than epsilon
for all x i such that yi is equal to
minus
What do I mean by this? Now, initially
uh the way we defined our discriminant
function is that if the uh the data
point is above the line, then we have uh
uh then we assign one class and if it's
below we assign one other class. So we
are saying this there always exists a
small epsilon okay within which you can
push the decision boundary. Okay, by the
way, discriminant function is also
referred to as the decision boundary for
obvious reasons, right? Yeah, you can
push the discriminant function
geometrically or decision boundary
by an epsilon
if the data is linearly separable. So
what do I mean by that? So look at this.
We'll take a different color.
Choosing a color is an issue. Okay.
Do you see that uh margin? Should I use
a different color or something? This is
okay. Right. Yeah. So this right is
what is this width mathematically?
2 epsilon. This is 2 epsilon. This width
is 2 epsilon. I can always push this
decision boundary within a within a
margin of two epsilon epsilon either
sides and why have I taken it
symmetrically this is just for alge
algebraic convenience I use one epsilon
all I'm saying is that if the data is
linearly separable I can always find
epsilon such that the decision boundary
can be moved along in fact think about
it in other words I'm saying that there
always exists a case within any decision
boundary that you take within which
there exists no data points
right this is true for any uh linearly
linearly separable data set do you all
agree with this okay because this is a
key idea you convince yourself that this
is true okay so what what what does it
translate to mathematically is
[clears throat] that instead of uh
writing my discriminant function as
greater than zero I can write it as
greater than epsilon less than epsilon
for two different classes Okay. [snorts]
Now,
so now W and B
can be rescaled.
>> Correct.
Thanks for that. Yeah, should be uh less
than minus epsilon. [snorts]
W and B can be rescaled. Okay. such that
now WCAP
transpose XI
plus B is greater than epsilon.
Sorry, greater than not epsilon. No, it
is 1.
and wcap transpose x i plus pcap is less
than or equal to minus 1.
Now once we have this epsilon right I
can rescale w by dividing the entire
thing by epsilon.
Okay uh and rewrite the discriminant
function in this particular fashion.
Is that all right?
Does this change the line? Does this
change the discriminant function? Why?
What is this W, by the way?
I mean, geometrically speaking, it's the
normal the direction of W is the normal
to the decision boundary, right? So,
rescaling it will not change the
direction of that. Therefore, this W
does not change. This line does not
change. Okay, I can always rescale it. I
will not write as wcap going forward. I
will still write it as w because
notationally it's easier. But you should
know that you know we started from a
discriminant function being greater than
uh greater than zero and then we uh put
that margin and then we rescaled it to
make it plus or minus one. Okay, I'll
I'll continue writing it as w. Okay,
don't confused. Okay. Um now this why
did I do all this is to ensure that
these discriminant function can be
written in an elegant algebraic form
right? So now the above can be
so this is all for all x i such that yi
is equal to 1 and for all x i such that
yi is equal to minus1 okay I just want
to combine this so above can be combined
as
just write it as wi *
wrpose x i + B
is greater than or equal to 1
for all I.
That's it. [cough]
[clears throat] We did all this to
ensure that I can write uh the the
discriminant function in this particular
way. So why is this correct? Look at
this. Right? Uh if my wi is 1, then it
is wrpose x i + b is greater than 1. If
it's minus one, then it is wrpose x i +
b is less than
one or less than minus one right so I
can combine both these conditions this
way that's it uh does that make sense we
did all this see I told you that I
assume my classes to be plus one and
minus one for this particular reason 0
and one will not make me write it this
way so started with +1 minus one and
rescaled it so that I can write the
classifier this way finally discriminant
function this way finally
okay
see what is the difference between the
final hypothesis our classifier and the
discriminant function. It's that you put
a threshold on the discriminant function
to get the final classifier. That's it.
Remember h of x is equal to 1 if g of x
is greater than zero. That that's what
it is. Yeah, that's it. Okay.
Okay.
[snorts] So finally for the linear
separable case
there exists a W and B such that
Yi * Wrpose X I
+ SB is greater than or equal to 1 for
all I right that is what
it boils down to if the data is linearly
separable. There always exists a W and B
such that this product is greater than
or equal to 1.
Correct?
Also
there exists
no data point
between
the lines or the hyperplanes.
See in two dimensions the discriminant
function is a line. In higher dimensions
it's a hyper plane. Remember that. No
between the hyperplanes
wranspose x + b = 1 and wrpose x + b =
minus 1. Isn't it?
If the data is linearly separable,
I can draw two hyperplanes wrpose x + b
equal to 1 and wrpose x + b equal to
minus1 such that there exists no data
points between them. Let's go back to
our figure.
So these are the lines that I'm talking
about. I think this is too dull a color
to do this. Let us use some other color.
So this line is
wrpose x + b = 1
and this is wrpose x + b = -1.
And you see that there does not exist
any data points between these two.
point on the line.
>> Let's get to that in a while. So the
question is can there be a line on the
point? They are called support vectors
as we will see later. So we'll get to
that right there can be because you know
the way we have defined it there can
exist but between them there is no data
point right. So I mean the take-h home
message is as follows that if the data
is linearly separable then you can
always find the w and b such that for
all data points the product of y *
wrpose x + b is always greater than or
equal to 1 and there exists no data
points between wrpose x + b equal to 1
and minus1 lines.
Is this all right? Okay. See remember
why are we doing all this? We still want
to formulate this optimality of a
discriminant function. That is why we
are doing all this. Let us uh see how
this thing is uh useful. Now,
and by the way, okay, there there is
exist no data points data point between
these two lines. And both of these are
parallel to okay they are parallel to
they're parallel to what
the discriminant function which is
wrppose x + b equal to0 the discriminant
function they are parall to this correct
[snorts]
okay
consider
the
distance perpendicular distance
between
the lines. And by the way, these
parallel lines are what are called as
margins.
Okay, I I'll I'll actually define
margins in a in a more rigorous fashion
in a while. Yeah, just use the
these these are called margins.
Consider
perpendicular distance between the
margin. What is it?
>> Huh?
>> The what? If you if you have two of
hyperplanes, what is the uh distance
between them in terms of its uh slope?
It is 2 by nom w. No,
they're parallel lines and the distance
perpendicular distance between them is 2
by nom nom of that. Okay.
Now one criteria
for optimality
of a discriminant function G of X
is
that this distance know
to be maximized.
This is one way one can define
optimality. So amongst infinitely
possible discriminant functions, give me
the one that maximizes the distance
between margins.
Why is this a good uh criteria to define
optimality?
There are multiple ways to answer this
questions. You know there is a very nice
uh learning theory way to answer this.
only if you do this then the true risk
can be upper bounded in terms of
empirical risk. Okay, that is the best
way to answer this question. So remember
finally our goal in ML is to learn uh is
to ensure that uh minimizing empirical
risk right leads to a good minimization
on true risk. So if you do this then you
can show that the true risk can be
bounded in terms of the empirical risk
and the margin actually.
Okay. uh so the higher the uh the uh the
distance between these two margins the
better is the bound on the true risk is
is one way to see it and there's also a
geometrical or an intuitive way to look
at it right why do you want the distance
between these two lines to be maximum so
let us look at that
so why do you think amongst all possible
classifiers or discriminant functions uh
the one that has the maximum margin is a
better classifier
Come again.
>> Why? That's that's correct. I mean I I
already told you that right? I mean
it'll have a better bound on the true
risk. The answer that he gave is that on
unseen data the one that has maximum
margin will perform better. My question
is why
then it somehow separates them the most
like
>> no no okay so see I'm not saying that
the discriminant function should be
between the lines between the classes
that the notion of between the classes
is not even well defined see when you
okay so this is one general advice piece
of advice that I that I would give all
my students right
to me uh personally uh intuition doesn't
mean anything as long as it is supported
with evidence and math because otherwise
it's all fragile language. So language
is too fragile and you can't explain
anything with language. Okay. But even
when you are drawing uh intuitions and
inspiration, right? Ensure that you use
math to do that. For instance, you know,
I mean there's nothing against what you
said but because you made that
statement, right? What do you mean by
between the classes?
See, classes are the values that my
other random variable Y can take. It's
only plus one and minus one. So now what
what do you mean by between the classes?
I can understand what do you mean by
between classes. There's some cluster
and there is some cluster center and all
that which we have not defined. Okay.
All that we have defined so far is these
two lines. You know we know what a
discriminant function is and we know
what margins are.
Okay. Margins are these two lines which
are parallel to discriminant function
such that there exists no data point
between the margins. That's a well
definfined concept. Now the claim that
I'm making is amongst all possible every
discriminant function will have a
margin.
Isn't it? I draw any discriminant
function or decision boundary that is
going to have a margin. The claim is
amongst all discriminant function the
one that has the maximum margin will
lead to a better generalization.
Algebraically the easiest way to show
that is that my true risk right is is
bounded by the empirical risk that is
scaled by inverse of the margin length.
So the larger is the margin okay the
tighter is the bound and the true risk
in terms of empirical risk. That's the
easiest way to say it. Okay. And that
convinces me completely because that's
what my goal is. Now if you want
intuition, I just want uh you to give me
the intuition that why do you think the
larger this this distance is, the better
its performance will be on unseen data.
uh does it make sense? So what he's
saying is um
in fact uh the discriminant function
that I have written in this example is
not the max margin classifier.
The max margin classifier is uh maybe
somewhere here like this
something like this. No okay let me
write that down so that you can compare
both the
classifiers.
I'm spoiled for choices. No. If you see
alphabets, colors run out of everything.
Okay. Huh? [clears throat] Red is
already taken. No,
yellow does not. Yellow does not.
Okay. Blue is not taken. Yeah, blue is
not taken. Okay. So, let us write
another uh classifier.
Okay, let's say that this is another
classifier at margin. I've written the
margin of the other classifier. Which
classifier uh do you think is better or
which discriminant function is better?
Is the blue one or the pink one? Uh it's
obvious, right? Why? It's obvious. See,
it's it's it's it's obvious
algebraically also. I can show you that
the true risk is upper bounded by this
particular thing. But now why do you
think this is better? Whatever
explanation that he gave. So what
happens is if you have margin and the
classifier is always here right in
between these two lines. Now during test
phase test data points actually have
this much of space to fall without
giving up the without making an error on
the actual classifier. Now if this is
small
what happens is if your data point falls
uh outside the margin. All right. Within
the margin it it has the chances of uh
wrongly
crossing the decision boundary.
You understand?
Did do you get the intuition? So
algebraically what's happening is if you
have a larger margin okay then you have
this much of space you know the space
within which uh a a data point can fall
without making a mistake is the margin
isn't it during test test phase I mean
if it's if it's uh suppose it is uh it
is above the as long as it is above the
discriminant function it'll the class is
correct okay however
during the I mean we have constructed at
the classifier so that anyway it is
linearly separable and when we do
empirical minimization we will ensure
that we have 100% accuracy on the
training data. Now during test phase
as long as it is above the uh the
discriminant function it does well.
However
if the margin is higher okay it can fall
within the margin without
making an error or a mistake in
classification. So the larger the margin
is the better the chances of
generalization.
Is this intuition enough?
>> Because the decision is taken the
question is if something a point falls
within the margin right why isn't uh why
isn't it it is mclassified because the
decision is taken based on the
discriminant function not on the margin.
as long as it is above the discriminant
function. It is taken as one class.
Remember final decision is based on g of
x not on margin. And by the way there's
a the textbooks uh different textbooks
use this word margin in different
context. There are two ways that people
use this width is referred to as margin.
Okay. Some books call these lines
themselves as margins.
Okay. Yeah. So it depends on what book
you're looking at. Either the distance
between these two separating hyperplanes
are called uh is called the margin or
the lines themselves are called the
lines that are parallel to discriminant
functions are also called margins. Okay.
>> We are not sure if
>> agreed. So as I said this is just
formulation. So we will generalize this
for the case where the data is not
linearly separable.
In the next class what we will do is we
will assume that the data is not
linearly separable and then we will look
at what the treatment is
the true
data is corresponding to a
boundary which is which has a smaller
then how do we know that
>> there is no true data here right once
the once the uh data is linearly
separable you can come up with infinite
decision boundaries. The question that
I'm asking is amongst all these possible
decision boundaries, which is the one
that g gives me the best generalization.
What do you mean by best generalization
in terms of reducing the true risk?
See, all we can do as practitioners is
to minimize the empirical risk. Right?
The question that I'm asking is which
classifier amongst infinite possible
choices for the classifier is the one
that minimizes the true risk the most.
The answer turns out to be the one that
maximizes the margin. That's it.
Okay. [snorts]
>> H.
>> So can we connect between?
>> Oh yeah. If the class conditional
density happens to be that gian with
same means same variance it will turn
out to be a linear discriminant
function.
But will that okay so the question that
you asked is uh I mean I understand your
question as suppose uh the data is uh
let's say coming from a class a true
class I mean a gian class conditional
density and we estimate the class
conditional density perfectly
and uh the discriminant function happens
to be linear in that case will it
corresponds to the max margin classifier
is the question that you're asking isn't
it
>> it should be
It is optimal. It is optimal in that
sense. Uh that's a good question. Uh the
question that is asking is will
the optimal classifier that we the base
classifier that we get in terms of
linear decision boundary uh if it
happens to be a linear discriminant
function will it correspond to the max
margin classifier? Uh not sure. That's a
good question. Let me think about it
because optimality
uh
in terms of minimizing the true risk,
right? Will it always corresponds to
maximum margin uh classification is the
question. In other words, let me think
about it. This is a good question. I'll
come back to this next class. I'll try
to answer this. Okay, you got the
question, right? It's a nice question.
Does maximizing the margin okay finding
the discriminant function such that the
maxim margin is maximized always leads
to the best classifier?
I'll I'll think about it. I mean
intuitively it's it looks like it should
but let me confirm it and then tell you.
Okay. Shall we move on? So now yeah one
criteria that's why I wrote one criteria
for optimality. It's not the criteria. I
mean it would have been the criteria for
optimality had it been the best
classifier.
So one criteria for optimality is that
you find a discriminant function such
that the max margin is maximized. Okay.
So let us uh formulate this now.
Uh we will stop here and continue in the
next lecture.
