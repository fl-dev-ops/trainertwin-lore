---
id: jQ-3gT8Mytw
title: Lec 39 SVM for Non-Linear Seperable Case
url: https://www.youtube.com/watch?v=jQ-3gT8Mytw
date: '2026-03-04'
duration: 34:08
model: youtube-captions (en-orig)
transcript: true
---

# Lec 39 SVM for Non-Linear Seperable Case

## Transcript


Welcome to this class So let us look at
the case where the data is not linearly
separable SVM for
right nonlinear separability it doesnt
mean that it is separable with a
nonlinear decision boundary Okay
nonlinear separable case if I write it
that way it means that there is a
nonlinear separating hyper plane its
not that well consider that case later
so well look at the case where the
decision boundary is still linear but
the data is not separable so which means
that there does not exist a war
such that you get 100 percent accuracy on data
right so what do we do uh in that
particular case is the question let us
look at that
so so this implies that there does not
exist a w star such that
yi times wrpose x i plus b
is
greater than one for all i So remember
how we got to this greater than one from
zero right from greater than zero we
went to this greater than one by scaling
it and all that right so that so this
there does not exist a w not w star
well say does not exist a w such that
this happens now what do we how do we
formulate svm in this case is the
question okay
any
ideas on how to do this how do you tweak
the SVM to accommodate this is
 if you already know it then then fine
you know if you dont know it youll
have to think yeah not kernel yet right
well go to the kernel case where the
decision boundary itself is not linear
think about it first I mean for people
who does not know what we are doing it
right think from first principles you
know what we are saying is that
there can exist uh cases or there there
does not exist a separating hyper plane
that give you 100 percent accuracy so what do
you do is the
Okay the way to do it is introduce
another additional variable into
optimization
That quantifies
the extent of mclassification
See if the data is not linearly
separable
and remember that we are still looking
at the case of linear discriminant
functions The discriminant function is
still linear but the data is not not
linearly separable This means that we
are going to make mistakes Right Now
what should we do is that well have to
find a decision boundary that would
minimize the mistake in a sense Right
That is what we should do So to
quantify the mistake that uh that this
decision boundary is incurring well
have to introduce another variable into
the optimization Okay Now how do we do
that So we have the original problem
was as follows
Original problem was that we minimize
half wrpose w maximize the margin
uh subject to
wrpose x i plus b was greater than one
Right This is what the original problem
was
Now on a data point x i this decision
boundary can make a mistake Now because
I know that for all x I cannot for all x
i cannot find a w such that this
happens Now suppose it makes some
mistake So what Ill do is
I will add or subtract that mistake from
this
Okay Now suppose for a data point x i
for a data point x i the product of yi times
wrpose x i plus b is some value Okay
which is less than one
then what I do is I will subtract that
value from this thats it thats what I
incorporate in this variable zi
you understand what Im saying so now
think about it for all data points for
which zi is
uh greater than one the the discriminant
function is making a mistake
Yeah
Okay So here what am I doing is let me
write it geometrically maybe then youll
uh appreciate it much better
Case where
Okay now this is not linearly
separable right So lets say that I
have a decision boundary here
Okay this is the decision boundary So
now this is making mistakes on these
data points right on these data points
the ones that are its making a mistake
So for every mistake that it does these
are the data points for which
yi times wrpose x i plus b is not greater than
one for these data points do you agree
correct but I mean it is some value
right its not greater than one it is
some value so what is that difference
Im encoding that difference in this new
variable called zi
does it make sense
Right So Ive still not completely
defined the optimization problem You
know its its not complete yet But did
you understand what this variable is
Whatever decision So remember that Im
constraining my uh uh my choice of
functions to linear discriminant
functions We have not gone to the case
where the discriminant function itself
can be nonlinear We are still looking
at the case where the the discriminant
function is still linear Now because
the data is not linearly separable No
matter what line I draw Im going to
make mistakes Correct And I am
incorporating I am Im codifying those
mistakes by an additional variable
called I mean which which Ive denoted
by this zi Okay Now the optimization
problem should have something to do with
zi also right I need this to be minimum
or maximum We will see how to codify
that But you understand what this zi is
for
any line that I write that I draw is
going to
make some mistakes and those mistakes
have been uh uh accounted for with this
new variable Z that this is called the
slack variable
 We well put all the constraints Well
put the constraints Yeah
Okay Now we will talk about as he said
no well have to talk about constraint
So suppose I now solve the optimization
problem Okay Uh okay So first of all
my optimization problem now will have
another variable Z also right well
have to
control this variable as well cuz if we
dont do it then the the optimization or
the algorithm will take any arbitrary
line and account all the mistakes in
this zi
so well have to constrain
to put a constraint on that right
without constraining every data point
can be mclassified and all the
mclassifications can be just designated
onto this slack so well have to ensure
this the slack back is constrained So
how do we do that is the question So
let us write that down
So unconstrained
unconstrained slack
may lead to
trivial solution
What is a trivial solution
Mathematically speaking it can make W
to be zero Make your W to be a zero
vector So everything is miscl
mclassified right Okay fine Ill
Ill Ill choose my zi to be minus x i
or something right minus
adjust it that way in accordingly so
that uh all mistakes are accounted for
right the trivial solution for instance
so w equal to0 okay therefore solve a
constrained version
can you tell me what the constraints has
to
H uh
so well have to do some we have to
place some constraint on this zi what
can be a constraint so I mean what do we
want slacks to be
as yeah minimum right and we need as
many uh lesser slack variables as
possible right so first of all we assume
that all these are non negative because
thats a choice that we are making okay
so well Well constrain that these have
to be non negative And well also say
that the kind of uh the number of slacks
that we need has to be as small as
possible because every slack is a
is is a correction for the
mclassification and we want the
mclassification to be minimal and
therefore well say that the the slacks
have to be minimized Okay So how do we
do that Well do it this way So you
minimize
minimize wrpose w plus
so add some yeah lets
wrppose w plus some c times
sum of slack
and we want this to be minimized So we
are minimizing Wrpose W right which is
maximizing the margin We want to find
this discriminant function in such a way
that the sum of slacks have to be
minimized So
thats a non ifferiable thing No So
you want something that can be
differentiated So and we are assuming
that these slacks are non negative
Therefore we can its minimizing the one
norm that way you know Yeah So
minimize U over W and Z What do we have
to do is that well have to find this in
such a way that the sum of slacks is
minimized And we also put this
constraint that the two constraints such
that
yi times wrpose x i plus b
is greater than 1
ci for all i We also want all these
lags to be non negative
This is the problem that we solve Hold
on
a couple of observations before I take
questions The first observation is that
those slacks okay which are between 0
and one
slack variables for those data points
for which slacks are between 0 and one
will be those points which are correctly
classified but within the margin
The one for which the slack is greater
than one are the one that are
mclassified
This is just geometrically this this is
how it looks like Okay So now we
instead of solving the uh the standard
SVM problem uh well solve this
particular problem and this is called
this formulation is called SVM with
slacks slack variables where we are
accounting for mistakes So here we are
not assuming that the data is linearly
separable
Okay questions on this
distance from the margin No this way
Thats the slack Now the way we have
done it geometrically it is distance
from the margin Yeah And thats why
thats why the statement that I just
made makes sense Now if its between 0
and one then it puts the data point
between the decision boundary and
margin If its greater than one then
it is mclassified Okay
Shall we move on Well have to write
the KKT for this problem
Lets do that
Okay Ill tell you what we are going to
get now Okay Yeah
Even if something is classified
correctly
will have a value
What are what
variable that inhibits it from giving a
value that are
just the distance from the
 this one
we want it to be minimized No So the
only way the sum of the slack can be
minimized is by making it zero for the
points which are correctly classified
So we have incentivized the the
optimization problem to choose zeros for
slacks as much as possible and that can
only be done if its correctly
classified
Yeah
So Ill tell you where we get get into
right We will see that the optimal
decision boundary does not change The
equation for the optimal decision
boundary does not change Okay Even the
dual problem does not change with the
slack formulation There is only one
additional constraint that comes on the
dual problem Thats all Everything
else remains the same So now if you put
a
additional constraint on the final QP
problem that we solve then you are
implicitly solving the slack formulation
is what we will show now mathematically
Thats why thats why this is so
elegant
So even when we change the know we make
such a big assumption that the data is
not linearly separable the final problem
that well be solving will will stay
exactly the same but for an additional
constraint
that is what we are going to show now
okay Ill do the algebra quickly
um
now uh yeah before we write the KKT
well have to write the lranian for the
above problem right
so now legangen
will be a function of WB
leg multipliers mu There will be
another leg multipliers lambda
for this particular constraint
Right So there are two constraints here
is equal to half Wrpose W plus
close the door
C times
1 through N uh Z I
plus
M UI times 1 minus Z Okay

yi times wrpose x i plus b
minus
uh lambda i z i
 oh sorry yeah this will be a function of
z also Yeah
So is a function of WB Z
uh mu and lambda Thats what its going
to be Lambda are the new lean
multipliers Okay That we are getting
for the newer constraint that we have
Is that okay
This one right
here theres no one minus because its
greater than zero is what we are writing
the way the constraints are written are
some a I mean some some function of the
optimization variable less than or equal
to zero and thats why theres a minus
here and thats why you have a minus
here
hold on Ill tell you thats a good
question what is the role of D right um
it plays the same role as that of uh the
regularization constraint
Well see that at the end of this class
Okay
So well have to write the KKT for this
problem
So the first one is the derivative of
the engine with respect to W is zero
which will lead to the exact same uh
solution I mean
solution that we had before
and if you take the derivative of this
with respect to B and put it to zero
then
theres
Well have to know take the derivative
of this with respect to Z as well
Right So this will
give rise to this one constraint that
mui star plus lambda IAR
is equal to C
Okay for all I
and we have the complimentary slackness
conditions which would be constraints
time langian multiplier is
1 minus z i minus y i times wrpose
x i plus b
is equal to zero and lambda i times z i
is equal to zero for all i So this is
these these two are complimentary
slackness conditions Okay These these
are the kks that we have
Okay So please note that this as I said
w doesnt change it just still remains
exactly the same we have this
additional constraint that the optimal
grand multipliers for both the
constraints both the uh both the
objectives have to sum to C So you can
do this right take the lrangian and
differentiate this with respect to z and
see that itll end up giving mui star
plus lambda star to be equal to c Okay
so this is one additional constraint
that we got got what we will use now
well have to formulate the dual problem
formulating the dual
So to find the dual now which is a
function of both the lean multipliers mu
and lambda well have to consider the
infyum of the lean leanian
which is a function of wb b z mu and
lambda This infyum is with respect to
the optimization variables in the primal
problem which are
W B and Z
Okay Now we already know what the
optimal WB are which we can just plug in
there Okay Now observe just like we
put the constraints in the previous case
on while constructing the dual right So
observe
that
that L has a term
L has this particular term uh sum
C minus MUI minus lambda times S I
So where do we have this term It comes
from here So theres a Z c time sum of
zi here right And uh theres a lambda times
zi here The sum is over same i Okay
And there is a mu times i term here The sum
is over i Again do you see that So if
you combine all these terms youll have
a sum okay
of z i multiplied by c minus mui minus
lambda i Correct So this term is
there Now if again just like the
previous case if you do not draw this to
zero then this infyum can go to minus
infinity So well have to constrain it
to go to zero So well have to ensure
that this is put to zero as a term that
needs to be
made zero
to avoid
the trivial solution
Which implies we have
mui plus lambda i This to be equal to
c
Correct
Right So with this now the dual problem
will be as follows
We have we need to maximize over
actually uh you know uh with this
constraint and making WB B Z to be the
optimal values youll have to plug that
into the lrangian and show that this Q
mu okay will now become
a function of mu only mean which is very
similar to the dual problem that we had
previously okay again complete that
algebra am I clear so what Im saying is
that
put this constraint into the lrangian
and put substitute W star and B star the
optimal W star and B star to the lean
engine and expand it out Okay if you
do that then you will end up getting
this particular dual problem which Ill
write now which is minus
some i some j
yi yj
mui muj
x i transpose xj
such that
mui is negative and f lambda i also to
be non negative see so this dual problem
had to be a maximization over lambda as
well okay but the objective function
itself becomes independent of lambda so
it comes up in constraint you can just
ignore that okay and fine Im using the
same symbol for z and let let me not do
that
And we have that C is equal to UI plus
lambda I Correct
Right
now the problem uh the objective
function is independent of lambda
Right So now if I mean theres no need
why we should have a lambda here we can
subsume this lambda to be uh non
negative here in this constraint itself
How do we do that Uh so to
take out lambda
modify the constraint as
so make your force mui
to be with less than c
Just a second If I make mui to be less
than c right then I can give away this
lambda to be greater than zero
Right Now the final problem now will be
exact same maximization
such that Mu is greater than zero and
and it is bounded between
zero and C
come again lambda here correct yeah
well not have a lambda here so now this
is the elegance when I told you right
finally
we are still still solving this problem
this problem is still quadratic in mu
okay with linear constraints on mu
theres only one additional constraint
that comes up that this mu has to be
bounded
within c thats
If we do that then we are implicitly
saying that there is a slack
and the sum of that slack is
controlled by the C The question that
you ask right where is the effect of C
This is where it is So now how do we
choose the C in practice Its a
hyperparameter
Okay In fact livium will give you an
option to grid search over the C
Choose different values of C How do we
I mean how do you select
hyperparameters You already know that
you know look at the performance on the
validation data and then do it So C is
a hyperparameter
and it isnt it so elegant So for all
that we did introduce a slack and all
that Finally the optimization problem
that well be solving will exactly be
the same but with one constraint on the
variable or or the optimization variable
that we have We are simply saying that
find my C such that it is less than find
my mu such that it is less than a
particular fixed value and that fixed
value appears as a scaling factor Okay
In the sum of the slack variables in the
primar
yeah thats also there thats there
which is which which came in the
previous case right thats there Yeah
So it is here
youre saying youre talking about this
term right this term had to be made to
zero correct I assume that it is similar
to the previous one yeah thats correct
fine so finally what happens is when you
solve this using kind of optim and QP
solvers put a constraint on your mu and
youre already assuming that theres a
slack
okay yeah this uh
and then
we have to make some terms that
every function
 Well yeah Yeah So thats a standard
practice in optimization theory So why
are we doing that is as follows right
See if your optimization over some
variable without putting some
constraints leads to leads the problem
to a trivial solution right You dont
want that it will it will definitely
take you to that trivial solution
Whats the point
You put a constraint to just to avoid
that trivial solution Thats it Its a
standard practice in optimization So if
you have if if your optimization problem
leads to a trivial solution avoid it by
putting constraints
 You also get mu lambda
 sum of mu star and lambda star
 No we get it actually in the dual
problem two that constraint exists It
it comes up like this
 No no this one See youre talking
about it it being it appearing in the
See okay youre talking about this
one right This one is because Zi can
be choosed in such a way that it goes to
trivial solution We want to avoid that
See please note that the dual function
is an optimization over your primal
optim the variables in the primal
problem It is not our le multipliers
You understand So any constraint that
you are putting while you are
constructing the dual function has to be
a constraint on the optimization
variables of the primal problem either w
or b
or in this case z
Okay Now this z can be made to take the
value of minus infinity and this q mu
can take minus infinity We dont want
that We dont want that Therefore you
drive this term to zero And now because
you drive that term to zero that this
entire lean engine will become
independent of Z That is how this dual
function still be the exact same form as
that of the dual function in the
non slack case because you are
completely removing the dependence on Z
here Got it So my question is that
different
but start that already
 correct
 is is there a relation between like
setting this to the condition that we
 uh is there a relationship between them
 because
 I understand yeah there is right I mean
if see if I say that mui plus lambda is
equal to c choose a mui star lambda i
star such that it is equal to See then
this term is anyway going to zero Yeah
correct
 Correct But this is while constructing
the dual
not while optimizing but that is while
optimizing
H
right So this is the see formulation
wise you got the exact same problem with
an additional constraint on mu Okay
Okay So this is about uh uh x margin
classifier with a slack formulation In
fact uh its very interesting that given
a problem
we will not even know how many slacks
were chosen and what values slacks I
mean slacks have for every data point
We we will not get to know that at all
because finally when you solve this what
you will get is a is a mu okay a mu and
then a w and a b with a w and a b there
is no access to z at all you can control
z only through the c we will not know
what slacks are you know when we solve
the problem its very elegant that way
okay so let now let lets finally
theres one final case that we have to
look at SVM with the kernel function Uh
we will stop here and continue in the
next lecture
