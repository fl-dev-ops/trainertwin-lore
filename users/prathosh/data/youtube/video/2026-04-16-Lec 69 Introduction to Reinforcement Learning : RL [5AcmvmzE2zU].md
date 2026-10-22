---
id: 5AcmvmzE2zU
title: Lec 69 Introduction to Reinforcement Learning : RL
url: https://www.youtube.com/watch?v=5AcmvmzE2zU
date: '2026-04-16'
duration: 31:13
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 69 Introduction to Reinforcement Learning : RL

## Transcript

speaker_1: Welcome everyone
So the last topic that I wanted to touch
upon today was RL reinforcement learning
and as I said reinforcement learning is
a
topic by itself that requires
uh
at least a semester if not more of time
to teach But Ill just introduce that
okay
for the sake of completeness
Now
in this I mean now that we are talking
about language models and auto
regressive models right An auto
regressive uh AR language model it
basically learns a distribution over set
of tokens Thats what its doing
right
Now reinforcement learning okay so
Ill just introduce that to you See
what happens is
when you train these auto regressive
transformers on internet scale data
it has good bad ugly everything
Okay
Actually there was a
there was this nice picture Let me just
show if uh
This is the picture
So what they show is as follows right
So when you
when you train a large language model on
internet scale data using the techniques
that we just showed the showed what you
get is this ugly looking monstrous
model
Okay Thats thats what they have
mentioned as unsupervised learning here
which it is not at all usable because it
has all See if you train it on the
entire internet
so it will have everything right Good
bad ugly everything On top of it what
people do is what is called a supervised
fine tuning SFT
What is supervised fine tuning
You take some data So you have See
when you do unsupervised learning
you dont have any labels so to speak
Theres just data
Then for supervised fine tuning you
have the input and the
the desired response as the output
Okay Now use the input Lets say that
you know you have some data on how human
beings
or other what should be the output of a
chat response Some human beings have
have asked a question and you have
generated the response and curated that
And then you use the same model and do a
supervised fine tuning on top of it
Exact same procedure The only thing is
now instead of predicting it on the next
token okay you predict on the
response
So your input token now becomes the
entire question The output token
becomes the first token of the output
And then you take the take the
prediction append it and then do a
supervised fine tuning because now you
have the pairs of input and output That
is supervised fine tuning So thats
this pink face
Its still ugly
Yeah right So
it doesnt align with the human
uh
you know uh
intent Okay So if you remember right
The the the the head of one of these
large big companies told that to make
your LLM say thank you we spent a lot
of dollars
You remember that It just happened very
recently So that is alignment So this
the the smiley that you see at the
at the at the output of this entire
thing is what is called as RLHF
Reinforcement learning based out of
human feedback
So if you use if you have ever used
these LLMs right They generate two
responses and ask you to choose one of
them isnt it Thats exactly thats
thats actually collecting data
In fact there have been companies
that have made
thousands of hundreds and thousands of
human beings just
evaluate the response of LLM and use RL
on top of it
Okay They like the response So
basically you are given
for a question you are given two
responses two samples basically These
are stochastic models right Every time
you sample you get two
different responses Take two responses
and rank order them I mean which one
is better which one is good
Okay Then use RL reinforcement learning
framework to align it to whatever humans
prefer
See thats why LLMs are very polite
because they have been asked to be
polite using RL
Okay You can actually use RL to train a
rogue LLM right I mean Im not
suggesting that you do but what Im
saying is the technique is generic For
science research that might be
important You want to be know when you
are wrong Exactly right I mean it
depends So basically the idea is that
unsupervised learning is
like no data at all okay Uh
I mean in mathematical terms
model the marginal supervised learning
will model the conditional RL is model
the environment
Thats the paradigm shift
Okay In supervised In so far what we
have do what we are doing is we are
assuming that all we have are samples
drawn from a distribution and thats it
We dont have any way to actively
interact with the environment
But human learning right Doesnt
happen through one shot data and then uh
doing ERM It happens through
interactions
Now RL is a framework where
learning happens through interactions
Thats why the name reinforcement
reinforcement learning where the setup
is as follows Lets go to the math
See
aligning LLMs to human intent is one of
the multiple applications of RL
Okay
Initially RL was being used for
modeling games
Okay
Uh I mean have you played these Atari
games
I dont know Maybe youre youre all
Gen Z right We have played We have
grown up playing Atari games
 to be 10 back then Uh I mean Atari is
a company basically Its a Japanese
company that used to make games So we
used to play video games you know this
is pre Xbox and PlayStation era
We used to I mean when we were kids we
were used to play Atari games Theyre
simply board games right And the
scenario based games
which which can be modeled I mean if
you want to
train a model in RL they are called
agents Agent to play an Atari game
then you can People were using RL And
then people solved the problem of chess
right And then also go
See AlphaGo is RL
Okay Now one of the the striking
applications of RL is to align LLMs to
human feedbacks
Thats why I told you RL is an entire
topic by itself Its a very interesting
way of looking at things So this is how
you model
the problem of ML in RL So in RL we
assume that there is an agent
So I will connect these terminologies to
whatever we have seen so far right I
mean agent uh
is is something that interacts with the
environment Okay So it can be somebody
who is playing a game or
in this case it is it is the LLM and so
on So I I Ill connect that So there
is an agent there is an environment
And there is an interaction that is
happening So what what do you what do
you mean by interaction Agent
stays
in one out of n possible discrete
states Okay
And at every time so there is a sense
of time here okay Because you know
discrete time So every time there is an
interaction thats happening Being at
one of the states the agent performs an
action
This is dependent on the state
We Yeah depending upon well map well
well well
well put math around it So there is a
state Being at a state agent performs
an action Okay When the agent performs
an action environment
gives a reward back to the agent
Depending upon what action the agent
display Let me take the example of
playing the game Okay The game player
is an agent So you press some key in
your joystick Thats the action
Based on that action the game the game
gaming environment gives you a reward
So its Or a punishment
Reward Reward can be negative reward as
well So in RL right Reward can be
negative So we only use reward So
there is negative reward is punishment
The the environment gives a reward So
this is the setting
There is an agent Its in a state
performs an action
The environment gives back a reward And
this keeps happening
The agent keeps performing an action
the environment keeps giving a reward
Okay That is the uh thing And theres
also something called a policy
Okay
Which decides what action the agent has
to take being at a particular state
Okay Its a probability distribution
over the set of actions conditioned on
states Its a conditional distribution
Thats called a policy
Policy is the distribution on the set of
actions conditioned on states So that
will tell you given that Im in a
particular state I meaning the agent is
in a particular state what are the set
of actions that that I should perform
what distribution governs that
particular action
Okay
And agent also See it performs an
action and it moves to a different
state
So it transits from one state to the
other So the the
There is also a probability distribution
that would decide how the agent transi
transitions from one one state to the
other
So being at state st at time t and
having performed an action at at time t
the next time
step in the next time step it
transitions to transitions to state t
plus one
So there is a distribution okay That
governs
what state it transitions to at a given
time
It is called the transition kernel
Understood right So whats happening
Theres an agent It goes from one state
to the other which is governed by the
transition kernel And being at every
state it performs an action
that is which is governed by the policy
Okay And
depending upon what action it takes
environments
gives it a reward and this keeps
happening
No it does not No
The kernels transition kernel does not
depend depend on the reward
Only policy depends on reward Well
Well get to that Okay And an RL
right Is is uh
quantified by what this thing called
Markov decision process which whatever
I just described is is called a Markov
decision process Very Where is a
five tuple right There is a set S
which is a set of which is set of
states which is also called state space
of the agent
the possible states And there is set of
actions which is also called action
space There are
typically the number of states and
actions need not be the same right
When you can take them to be different
And there is transition kernel which is
the probability that an action
that an action AT being in ST at time T
will lead to the state ST plus 1 at time T
 plus 1
So take an action AT at state ST
what is the probability that you go to
ST plus 1 right At T Thats the
transition kernel Okay And there is a
reward This is a function from S cross
A to R
Okay S is the state space A is the
action state So given that the agent
is at state T and performs an action AT
what is the reward that the environment
gives
So note that reward can be negative
Its not our place unlike our loss
function right Reward can be negative
as well
Yeah
Reward is given by the environment
Okay
See when
when
when you are asked to choose
one of the two responses right
Theyre modeling the reward
Every time you are giving your They use
that data to
get a get the reward function
Okay And theres also this thing called
discount factor which will Its simply
a number between zero and one And there
is this distribution called
initial state distribution because the
Markov chain has to start from the
initial state right Before it gets
onto the transition So an MDP has this
five tuple right S is the state space
action space transition kernel
reward function
uh the discount factor and the
initial state distribution
What is the second last
Discount factor Its a number between
zero and one Ill tell you what that
is Okay
Okay
And also there is a policy
Okay What is a policy Its a
distribution over actions given state
Now note that you you assumed So what
is the modeling problem here Just like
we we modeled the underlying
distribution what is the modeling
problem here We assume that there is an
an underlying MDP that is governing this
process Example is playing an Atari
game
Theres an agent environment reward is
being given You have to you you you
want to
design an agent that would play the
Atari game Okay Theres an underlying
MDP What is that you you want to
estimate now You want to estimate the
policy
Right This also becomes a distribution
estimation problem now
Because policy is a conditional
distribution
Given all this I want to estimate the
policy the underlying policy that is
governing it So how do you do that
Assume that its a parameter In fact
in RL right In in the in deep RL this
policy is this
policy is modeled using neural networks
again
We know how to model distributions using
neural network right Use it for all
applications So
Okay So Ill formulate that problem in
a while So theres also this thing
called trajectory
Okay What is data here
We need some data right What is You
need trajectories of interaction So
what is a trajectory A trajectory
is
set of actions and states
Okay When you
walk through this MDP So you start
from S0 see what action
the agent takes and then go to the next
state and see what action the agent
takes and so on So that becomes one
trajectory Collect multiple
trajectories of this sort
So what do you mean by that You keep
playing the game
And see collect the states and actions
Thats it
S1 and S2 they are sort of not in user
control also right Because they will
change as per
the reward
No no See when you are collect See
of course start from initial reward and
But there is a reward See
youre not We are assuming that See for
RL you need to have a fixed reward
function
We assume that there is a reward
function We cant do anything about the
environment But given that we know what
the reward function is we can generate
a trajectory by interacting with the
environment right That Thats what the
trajectory is Data for RL is a
trajectory
Right So in an in an when you are
fine tuning an LLM right Using RL
what could be the trajectory
Responses
Prompts responses prompt responses
Thats what the trajectory is in the
case of an LLM
What is the policy The policy is the
transformer the the model that you have
trained itself is the policy
What is the reward
Reward is the choice that the human
beings have made
Given two responses if this is a better
response that is a better response
thats your reward
That is RLHF So now you cast the
entire problem of aligning
a pre trained LLM
to human preferences as an RL policy
estimation problem
Thats what RLHF is all about Okay
Okay so lets lets
formulate the problem So
since the trajectory Any question Yeah
See reward reward is something that the
environment is giving you right
You can only tweak the agent not the
environment
Yeah So we assume that the environment
is giving us reward and we know what the
reward function is In fact see in the
case of LLMs one needs to
estimate the reward function as well
Okay There are these these models
called Brad Bradley Terry model and so
on where
given preferential data like you know
this is the response that I like this
is something that I dont like there
are ways to estimate the reward model as
well But we will assume See your RL
methods are all as good as the
underlying reward function
Okay Thats That is something thats
there So we assume that the reward
function is known
Okay But there are methods to estimate
the reward function as well For at
least for the formulation lets assume
that we know what the reward function
is Okay
See its not supervised in the sense
that uh the the trajectory can be
obtained No see in in in supervised
what happens is
uh you dont continuously interact with
the environment so to speak So you
get the one sample from the distribution
and you use that
But here you can keep going back and
forth
Yeah but you keep going back and forth
Thats it So the environment interacts
with you actively Thats Thats the
difference
Okay So now we define what is called
as a trajectory distribution under the
policy
So what do you mean by that What is a
trajectory A trajectory is a
is a set that contains
uh the states and actions Okay When
the agent is interacting with the
environment Now the
trajectory depends upon policy Do you
see why
Uh because action depends on policy
Exactly So
actually trajectory depends on two
things It depends on the state
transition probabilities and also
policy
It should depend on both
Isnt it Both the state transition
probability and because you you What
state it goes to given it is at a
particular action depends upon the state
transition probability Right What
action it takes depends on the policy
So it depends on both of them
Okay Thats why we can write a
distribution over the trajectory
How do we write that Use chain rule
Okay What is it Start from the state
S0 Thats That is governed by your
initial state transition distribution
Okay Then from T equal to zero to
infinity
being at state ST perform an action AT
which is governed by your policy
Multiply that with the probability of
transitioning into state T plus 1 given
that you are at ST and AT at time T
Thats it This is chain rule of
probability right
If you have a sequence of random
variables okay That is That is
governed by the underlying distribution
you just write the distribution over the
entire sequence as the product of the
conditional Thats it This is the
product rule
Okay Now this is the distribution over
trajectory
Now what is the goal of RL
Just like we formulated the goal in in
in supervised learning the goal in
reinforcement learning is to learn a
good policy
What is a good policy
You need reward to define what a good
policy is Just like we had the
empirical risk right The loss
function
Similar idea here is that of the reward
Okay
Define what is called as a discounted
return or discounted reward for a given
trajectory What is that
Collect the reward for at each state
each time time step T and multiply it
with what is called as a discount
factor
This is a number that we have chosen
This is a hyperparameter actually So
why do you have to multiply it with
discount factor
The idea is the
farther you go
in the sequence right
The lesser less important the rewards
are because the system has
transition for very long So you dont
want the reward at each time to be
equally weighted Thats it So this is
a waiting factor
Okay That is what is called as
discounted reward I mean its simply
scaled reward Okay The most recent
reward should be given more weight
Correct Thats the idea
Okay Now define the goal of RL as
this
Take the expect expected expectation of
the discounted return R the scaled
reward Expectation is over all positive
possible trajectories
Lets say that you can interact with the
environment infinite amount of times
You get a distribution over
trajectories
Okay For every trajectory you have a
discounted reward
Take an average of discounted reward
over all trajectories
And get a policy that minimizes that
Thats it Optimizes the reward
You understood
Just like we had the expected loss
function as the risk function no
The same idea
Now the expectation there was over the
entire distribution of data Here the
expectation is over
all trajectories all possible
trajectories because data now is a
trajectory that you environment I mean
when you get while you interact with the
environment
Make sense So the goal of all RL is to
find a policy by theta star
that would maximize the expected reward
Is it okay
Now you can solve this problem in 100
different ways
Okay there is Q learning you know
there are Bellman equations and so on
Thats why I told you right RL is an
entire
entire course by itself But Ill only
show you one
way to do it which is called the policy
gradient theorem
Which is the
method that is used for RLHF in LLMs
Okay Policy gradient theorem is
assume that so you want to optimize
this particular task right
You want to find a policy that would
maximize this expected reward
How do you do it Just use gradient
descent to do it That is policy
updating using gradient descent
Now to do this we need to find the
gradient of the
expected reward isnt it
How do we get that is the question
And for that
we need this
you know beautiful theorem called
policy gradient theorem
Maybe skip the proof Its its very
nice Okay So
uh what happens is you can write the
gradient of the expected reward okay
In terms of this particular thing
Okay what is this Look at this
Theres a gradient here of the policy
The log of the policy multiplied by the
reward
The beauty of this entire theorem is
that every term inside this is
computable now
We know how to compute the reward
We know how to evaluate the policy Why
Because policy is a neural network
Right This is the outcome of a neural
network right And its a probability
distribution that the neural network is
imposing So we know what the
distribution is So log of pi theta AT
given ST can be found out
Okay And R2 is something that we know
Therefore this entire gradient becomes
computable
And this gradient how do we get this
the gradient Gradient of log pi theta
AT given ST how do we get this
Huh
Backpropagation no If this is a neural
network autograd is PyTorch we are
doing it but it is the normal error
backpropagation Thats it Because this
is a neural network and you want we can
compute the log of the outcome of a
neural network and the gradient with
respect to the parameters of neural
network is
something that we know how to do it
using how to do using gradient descent
Make sense
Yeah This is the famous policy gradient
theorem In fact its taken to be one
of the most
elegant theorems that have come in
recent times
in ML
Right Because this changed the way RL
is being done So the uh classical RL
does not did not look at policy gradient
theorem It looked at the other ways of
Q learning or different ways of doing
it But yeah So this is a very
elegant way of doing it So now how is
it done in the context of LLMs That you
assume you you assume that your language
model is a policy
And reward is what human beings tell
you whether they like this response or
does not like this response
Okay Using that to use your RL
uh to align the language models into the
preferences that human beings have
given
Okay so there are other details right
Where you have this uh
yeah so this is what Ill show you
Yeah before going there there are some
other where you reduce the the variance
of this estimate okay
What happens is
uh this estimate that we have gotten for
the gradient is is is shown to be
uh noisy in the sense that it has very
high variance
People came up with a lot of uh uh
ways to reduce the variance of this
estimate by using what is called as a
baseline function
Which would introduce to this concept of
Q function and advantage function and so
on Thats why you have this these
methods called GRPO and all that right
Which are the state of the art methods
Which See all these methods that you
have you might have heard about right
PPO preference policy preference
optimization DPO direct preference
optimization GRPO TRPO all of these
are variants of policy gradient theorem
Okay That uses different ways to reduce
the
the the variance of this particular
estimator Thats it Okay
Uh
yeah so the last piece is how do you
express an autoregressive language model
as an RL policy You already know that
right To apply to apply RL we need a
trajectory
In the language model initial input
token which is your prompt
is S0
The first state
The first output token A0 the first
output token that you get by giving this
prompt is taken to be the first action
Okay The second state is prompt plus
first output token
Thats your S1
And then the it it just goes on that
way right So A2 is
the output that you get for the appended
prompt and so on Thats how you
represent that as a policy
Yeah then we have proximal policy
optimization and so on which is
out of the scope of this particular
course okay So yeah this is about
RL right So the the striking
difference is that instead of assuming
that uh
that you have data from an underlying
distribution and you dont have any
other way in any way to interact with
the environment you model
the problem See this RL can only work
in those cases where
you can interact with the environment
that you are trying to model
Right Suppose you have these kinds of
problems where you have images and you
want to solve a regression problem or
some bounding box regression problem
there is no way that you can model that
as an RL problem because
youre not interacting with the
environment There is no nobody whos
giving you a reward
Right Only if you can formulate the
problem as an MDP a Markov decision
process that I talked about state
action transitions and reward then
you can formulate the entire problem in
the RL framework And RL is known to
do do well if you can formulate
an ML problem in that particular
framework
Okay
Okay so thats it then Thats thats
all I wanted to convey in this course
So
a quick summary of what we looked at
right I mean started from
probability theory Spent a lot of time
on that
So
saw how to cast the problem of machine
learning as a distribution estimation
problem So all that we are doing is
estimating the underlying distribution
okay And we looked at multiple ways of
doing it maximum likelihood estimation
Basically the idea is to parameterize
and then
use a divergence metric and find the
parameters by minimizing the divergence
And we looked at non parametric ways of
doing it as well
which are the Parzen window and the
K nearest
neighbor estimation and so on
Then we looked at multiple ways of
parameterizing this underlying
distribution using different models so
to speak right
In the in the empirical risk
minimization framework
Where we looked at linear models
the kernel machines and neural
networks and different kinds of neural
networks and so on
Then the then we also looked at some
unsupervised learning techniques You
know before that we looked at uh the
other non parametric techniques such as
decision trees and the ensemble methods
Then we came to the unsupervised
learning methods where the idea is to
model the marginal distribution
rather than the conditional Theres no
notion of a label here And a special
case of that was what was called as
the self supervised learning We also
looked at NCE and so on The last part
was uh
the generative modeling where you still
model the marginal distribution but the
additional component there is that you
also learn how to sample from the
underlying distribution And today we
looked at
RL just an introduction to RL So this
is sort of
broad taxonomy of what machine learning
is
Right That block diagram right
Machine learning deep learning and RL
self supervised learning and so on So
all that can be seen under one broad
umbrella of distribution estimation
right Given the samples We also looked
at ideas such as regularization
bias variance decomposition and so on
Okay
As I said theres another course that
is coming on coming up
which is which will start from where we
stopped here
So I assume that the
audience know everything that we did in
this course and we look at
the generative models in in in much
more depth We look at
adversarial learning the variational
learning flow based models diffusion
models
and the score based models energy based
models
auto regressive models and RL and also
some some parts of
uh
state space models as well So thats
thats what the content of the next
course would be
Okay so hope to see some of hope to see
some of you in that next course and
thats about it And for the online
audience right Thanks for
attending this NPTEL course on uh
mathematical foundations of machine
learning So as I said this is a course
that would take a different approach for
ML altogether in the sense that instead
of looking at algorithms themselves if
you have seen if you have sat through
the entire course you would have now
understood that ML is

 uh more about knowing what the
foundations are right From the
probability probabilistic standpoint
than understanding what the algorithm
is
So the algorithm is a byproduct right
Its its the core uh
ML probabilistic viewpoint that is that
is what is of importance So hope that
you enjoyed the course Thank you
