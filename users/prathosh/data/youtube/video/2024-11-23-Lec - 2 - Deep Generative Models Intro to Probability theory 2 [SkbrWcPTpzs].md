---
id: SkbrWcPTpzs
title: Lec - 2 - Deep Generative Models Intro to Probability theory 2
url: https://www.youtube.com/watch?v=SkbrWcPTpzs
date: '2024-11-23'
duration: 03:16:30
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: Shall we begin


okay so good morning all of you um start uh i hope you had a chance to brush up some of the fundamentals uh of what we discussed the last time i will just quickly recap and then take it from there so what we did the last time was uh said that uh most problems in sense engineering happens to be approximating functions right


Um


So we we cast the problem of function approximation as that when you are given pair stuff elements which are of the form x i comma y i


where xi comes from the domain of the function and yi comes from the range of the function uh the task is to find the uh underlying function that is there okay so some examples also right uh where the underlying function happens to be simple functions like linear and quadratic functions so why do we need to do function approximation that is because uh one of the major reasons is that function approximation enables prediction


right so if you know what the relationship between the uh the domain basically elements of two sets called the domain and range if you are given a new uh element in the from the domain set you can predict or estimate what is the corresponding element in the range set right so that is why uh function approximation is uh important and necessary okay so the problem was that what is the mapping between


the sets cannot be found using the known mathematical tools mostly the solution is that you come up with new mathematical tools so given this pretext context probability theory was introduced so basically we need that because the relationship between the given sets are rather complex do not adhere to the existing mathematical frameworks saw some examples of it right where


where the elements of the domain happen to be coming from like rp comma q where it corresponds to every element in the rp cross q space corresponds to a picture okay and what you need is the range space comes from one of the two values like these are called genders so relationship between the picture values and the idea of genders cannot be modelled using existing


mathematical tools and that was one example and we saw some textual example where you have a document and document gets mapped to an abstract idea called emotion and similarly speech signal to phoneme or words and all that right so first the idea means it is non measurable in the sense that they are abstract okay and you cant measure emotion you cant measure gender you can only give labels associated with it but


domain can be measured okay uh as i said even to solve these problems historically people attempted to solve these problems using classical mathematical tools and give you examples of


yeah speech and images where speech signal was being modeled from a linear system or nonlinear system perspective where you have the signal and you model the uh the signal the output as uh concatenation of several linear systems or wave guides and you estimate the parameters of it similarly with image processing where you uh and you wanted to analyze an image and uh that analyzing an image was uh


conceived in a in a hierarchical manner where you detect edges and you know you compose objects from edges and


primitive shapes and then you try to make sense of what it is okay but these methods mostly did not yield human level performance okay because this constructing the functions that would map speech signal to phonemes or pixel values to complex object relations are not trivial


So then came probability theory I mean it was actually not that you know historically speaking statistics and probability theory was around Okay But the the application of probability theory as a mathematical tool to solve these kinds of problems was not that popular uh before lets say 19 late 1980s okay the probability theory probabilities probabilistic tools were not the go to tools to solve these kinds of problems but yeah so people realized that


Using classical function approximations may not be the best thing to do while you want to solve these kinds of block graphs


so with this context right we were looking at what probability theory was so uh okay so maybe i i pause for a while here any questions so far which is all some historical context any questions here


Okay lets continue So we introduced standard introducing problem theory So what is it basically Its it allows uncertainty by construction Okay


uh what is what does that mean that the functions that we are talking about which are mappings from the domain and range can possess quote unquote uncertainty we want to quantify what uncertainty is uncertainties are so uncertainties what do what does it allow uh the the user to is that it makes function learning feasible okay because we saw that uh function learning was in in feasible in so in in so many cases and uh it sort of helps creativity because


Theres uncertainty If there is uncertainty Ill give you an example of an artist right The artist does not know a priori what sort of art is being created and thats why creative or a new stuff gets generated out of it Okay


we could try to concretize some of these ideas that uh yeah uh probability theory starts from this this this fundamental concept called a random experiment or a random trial so as i said in the whole of probability theory this is one thing that has not been mathematically defined right what is a random experiment or a trial just said that it is it is a process that gives rise to a set of outcomes thats


Okay so anything that that gives rise to certain outcomes is called a random experiment or a trial So collection of all the outcomes of all outcomes are the observations or outputs of a random experiment are enumerated in a discrete set and that set is called a sample space Okay need not be discrete set can be a real space as well Lets not do that


just say that the set of all outcomes are enumerated in a in a in a in a set and thats called a sample space so examples of random experiment is that you toss a coin and the sample space comprises of a red tile and you roll an interface die then the sample space comprises of n phases of the die and we also saw some practical examples right where taking a picture of a person can be looked into as a random experiment where the sample space happened to be


different people right every time we get different people recording the speech signal happens to be a sample space and so on


okay so uh this was the uh sample space and we are not i mean its not enough if we only have sample space right because remember that finally our intent is to mark a picture to agenda of these kinds of ideas for that what we needed was something called a measure okay it defined a measure so what is what what is the measure so given a particular set take a subset of a set and for each subset you associate


a scalar right or a non negative number such that it has some properties and the properties are the following that you take any subset of any one set the measure has to be non negative non zero and if you take the null set the measure has to be zero and if you take the measure of union of two sets such that the intersection of them is null then the sets have to add up so we also saw an example of a famous measure that all of us know


of which is the level measure which is the length and the area measure in length area and volume measure in r1 r2 r3 etc similarly uh one can define a measure on sample space right you have collection of all possible outcomes of a random experiment is what is called an sample space like if f denotes the set of subsets of all possible subsets of omega then a measure uh which is also called the probability measure is defined on the subset of the the


sample space okay probability measure is a measure that is bounded upper and lower bounded between 0 and 1 okay it can be interpreted as the uncertainty associated with a subset of the sample space the subset of sample space is also called an event okay so probability measure is just like the Lebesgue measure gives you the sense of length okay of a subset of a real number sorry Im sorry


So it gives the notion of a length of a subset of a real of the real the set of reals Probability measure can be interpreted right as some measure that is that is giving you the sense of uncertainty associated with certainty or certainty like uncertainty associated with a particular subset of the sample space Yeah this is what Ive said No length or areas on RR2 is similar to probability on


Okay so this was okay now we have the the probability triplet


Which is this generally called the


the probability triplet that is a sample space


the subset which is the event space and the probability measure okay this is typically the probability triplet


i mean again you can compare this with the when every time you define a measure you get something like this a triplet like this in r now you have r you have subsets of r which are also called the borel sigma algebra and you have the length or the lebague measure right similarly you have a probability triplet that is omega and the subsets of omega and probability measure okay now okay uh there is another problem wait remember that our goal is always to


uh learn that association between the pictures and uh abstract concepts like gender or whatever okay uh to do that we need something more okay there is a measure no okay we can measure uh we associated a measure with the outcomes of


random experiment but thats not enough because elements of sample space are not observed in practice okay what do I mean by that what do I mean by that is that if the random experiment is taken as observing a particular person okay and taking a picture we dont get to see that person or rather we dont yeah we dont get to see that person which are the elements of sample space


But what do we get What we get to see is


an observation rather some measurement okay that we do on the elements of sample space so this has to be appreciated because otherwise right i mean this this notion of random variables will will not be uh appreciated better let me repeat what im saying see while uh the elements of random experiments are are enlisted in a sample space in practice


we dont get to observe the elements of sample space now why is that in the example of the pictures that i said okay uh when the random experiment is that you are you know you you pick a person take a picture right and a picture an abstract object picture is something which is an element of sample space you dont get to observe that what do you get to observe is a surrogate to that particular picture


Okay so now we need to somehow define one other concept okay that would map the elements of sample space to something that we observe so that we can work with them


is this idea clear i mean this is a this is a central idea right because we never go to sample space while we are working in in machine learning we only work on uh the observations or rather the instantiations of what are called as random variables okay uh why is that why is that is because when we when we do a measurement right using some sensors or something what we observe are some surrogates of the elements of sample space but not the elements of sample space at all okay now


do you model that mathematically is the question uh we model that using a function uh that is mapped from the elements of sample space to rd okay d is an arbitrary number uh depending upon what sort of uh application or data that we have uh d gets fixed the example the in the example that we saw if the sample sample space happens to be uh people or pictures of a person


then this function okay this function will take every picture or every person and maps it to a real number okay in pq dimensional space what is this pq uh we envisage this as a picture grid of pq pixels right where every element in p p q uh grid happens to be a real number so every picture happens to be


real number uh in a p q dimensional space so now this function takes a picture right or takes and takes a person and maps it to a real number in our p q dimensional space and which is what we observe okay uh yeah i will take the questions in a while uh please keep that hand raised of course virtually otherwise the time will start paining um okay uh in the second example uh this


space has a head tail okay and the function maps the head tail to lets say zero one two numbers


Okay so this is here is a function the function takes elements of sample space and maps it to some d dimensional real numbers Okay and this function is what is famously called as a random variable and as I said its a misnomer in the sense that this it is actually a deterministic function that takes elements of sample space and maps it back to Maps it to some real numbers a d dimensional real numbers


Okay now the data that we are given the data that we are given okay what is that They are actually the members or elements from the range space of a random variable What do I mean by that When we lets say that you know we have we are working with MS data set or some imagined data set What we get are elements from this RPQ dimensional space right We get multiple vectors of dimension RPQ


you what are those they should be conceived or seen as elements okay coming from the range space of this function called random variable


Okay because the elements from the sample space are not observed Okay what is happening is you should imagine that okay there was a sample space some random experiment was happening and there is this function which is called a random variable that has mapped the elements of sample space to the set of real numbers What I am seeing are the set of these real numbers which are nothing but the elements from the range


space of the random variable which is a function and you should imagine that there exists an underlying sample space uh which would tell you what was the random experiment that that was being conducted okay so this is uh till that till this we had seen the last class so now we will continue from here yeah so any questions here uh please raise your hands ill call out names


Right


Yeah somebody tell me ha this is the one I want


I want a new page how do I get a new page here

speaker_2: Sir you can unselect this and on the bottom there is a new page button page plus page in that column only


Can you open that once again

speaker_1: Yes

speaker_2: On the bottom there is a

speaker_1: Here we are got it got it so here


Next one


What was the naming convention this was L2


Okay so


just to distinguish it from


Where was that thing which uh


We had the sample space


the set of subsets and a probabilistic measure


Not this


For that yeah


Suppose this function called the random variable that took elements of sample space mapped into some t dimensional real numbers Okay this is where we are Okay questions Yeah Prasad Gupta

speaker_3: Hi Sir good morning

speaker_1: One yeah

speaker_3: So sir I just want to analyze a little bit more on the concept of random variable in the context of our problem of taking a picture and understanding whether its what gender it is So in that concept as you said the picture that we clicked is a set is a member of the right hand side of the random variable definition that is the RD side

speaker_1: I encourage you to use mathematically correct terms dont call it the right hand side of random variable call it the range space of range space of random variables

speaker_3: Ill be right there


Yeah train space all right yeah

speaker_1: So every picture every piece every point in data that you get is an element of the rate space of random variable

speaker_3: um now um i i want to imagine a scenario so like its possible right that we take multiple pictures of the same person where he is standing in different poses so how does the idea of random variable handle that like so there is one element of sample space that is being mapped to different ranges uh different elements in the range set correct

speaker_1: No see yeah a function cannot map one element to multiple elements no one to many mapping is not a valid function at all

speaker_3: That makes sense

speaker_1: Okay so that does not become a valid function So it cannot map the picture of one person to multiple coronal numbers But why I mean thats a good question right I mean thats actually a good question Let me answer that See in that case the way you should imagine is that the sample space itself has pictures of that person standing in multiple angles


While while I conceived I mean the example that I gave why I I understand why that question is uh question right in the the way I I I I gave you the example of sample spaces I I said that uh uh every person corresponds to one object in the sample space right it may not be the case right I mean if you are taking I mean that is in the case where you take one picture of a person if you are taking multiple pictures of a person then all those pictures becomes elements of the sample space


And that variable will map it to different real numbers for different angles


A function by definition cannot have one to many mapping

speaker_3: Got it So we are still not at the place So sample space has all the possible poses everything related to every person on this planet but we are still a little away from our final goal where we then analyze the sample space and all the possible poses and find out okay these are all actually the same person

speaker_1: Yeah


Thats what we need to do


See that way we will do See we have I I I have not set up the the next problem yet Im just telling you what the sample space is and what random variable does right

speaker_3: Thats the new


Now

speaker_1: Now thats why I mean actually you brought up a nice point See I hope that all of you got the question The question was that in the example that you gave there was one person and like taking the picture of one person was one element in the sample space


Then if you take multiple pictures of that same person how do you handle it Now the answer to that is that see you conceive what is there in the sample space Meaning the user would define what the sample space is because the random experiment is something that is a user defined idea you see But what I wanted to tell you is that when you have like lets say multiple elements from R D R P Q R O S Q which are which are


are images right or the set of pixels you have to imagine that this is the result of this process where there was a sample space and there is a function which is a random variable that has mapped the elements of the sample space to this rd


Okay there exists some sample space some underlying sample space and you constructed sample space accordingly right I mean it doesnt matter how you construct it And the good thing is that you dont have to even worry about the sample space once you get the outcomes of I mean once you look at the range space of random variables thats enough That is why you define the random variable in the first place okay

speaker_3: Ah okay So the way I understand this what you said triggered another thought that ultimately what we want to understand is the gender right Even if the same person repeats again and again the gender stays the same So its irrelevant for the problem Is that how I should know

speaker_1: No no I say dont worry about thats what I said Dont worry about the gender part yet Okay Just just think just think about having a few data points Yeah Which are pictures Now how do you see those data points is something that we are looking at right now How do you look at the labels is something that well come to in a while Okay For now just imagine that you have a set of data points


Okay these data points are seen as the elements of the range space of a random variable And the moment you talk of a random variable there exists an underlying sample space which is giving you some elements That is how you should look at it Okay

speaker_3: Sure sir so were only talking about representatives right now got it

speaker_1: No no the data data I mean data yeah sorry

speaker_3: Data yeah sorry like uh not

speaker_1: uh not labels i will i come to the labels in a way see for instance right in in generative modeling you dont have labels right you only have data lets look at the representation of data now uh from a random variable perspective then we will come to the the labels in a way okay any other questions on this this is very important right i mean this understanding is very important because from this is the last class when ill be talking about the sample space from like next class on onwards well only talk about


variables and distribution functions so you have to understand like thoroughly what is going on so if you have questions so this is the opportunity for you to ask them

speaker_3: You will be happy


I need it

speaker_1: Any other questions


But we may

speaker_4: Some so maybe the uh the trick is in designing the I mean coming up with the correct probability measure

speaker_1: Yeah yeah yeah see um probability measure is I mean I didnt get your question I mean that that was a sort of assertion right what is the question

speaker_4: Oh yeah


Okay so in one sense I understand that this is still only talking about understanding the basic data points but when we move on to the next step when we start try to assign labels then probably we have to worry about a probability measure We have to model that part

speaker_1: Um hold on I was like as I said no please try to if you have questions on things that Ive said already do ask and lets not jump Ill Ill come to that Ill come to all that in a while yeah


Any questions on things that we did so far

speaker_3: Hello sir can I ask one question

speaker_1: Just a second uh and yes I think all

speaker_3: So sir I was asking like this random variable function is like very important We are converting this sample space into some range space So as per our problem like different

speaker_1: No no converting no no hold on hold on converting sample space into real numbers

speaker_3: Yes

speaker_1: Dont call it range space real numbers See what is range When you have a function you have a domain and the range So random variable is a function that takes sample space and maps it to real numbers

speaker_3: So for a given sample space there we can define multiple ways or we can define multiple functions this random variable function right based on the work

speaker_1: over very good very good observation yes you can and that is why no that is a model thats basically what a model is so ultimately we will see that entire machine learning is about uh finding this underlying probability measure okay why does the probability measure change the probability measure changes because uh i mean when the probability measures changes the random variable changes right you can actually you can yeah so you can there may not be one random variable cross


responding to a random uh sorry uh a particular sample space there can exist multiple random variables yeah


But what is important is that the the moment you have some data you should imagine that there has already been a random variable that has been applied to it You understand

speaker_4: No

speaker_3: Like data is in its raw form like like images or speech

speaker_1: Now you have data the moment you have data the moment you have data you should all you should know that there has been some random variable that has been operated on the sample space


In practice yeah

speaker_4: But it will be expensive

speaker_1: Youre right


Okay


Okay uh yeah I think Bridge Cooper has a question I think yeah

speaker_3: Uh yeah sorry so just a small one its a little different uh so uh the way you said right uh for a for a simple experiment like tossing a coin um we usually immediately associate a rand a random variable with the uh possible outcomes like zero and one we assign to head and tails right


Why uh like uh so Im assuming the reason we choose zero and one is that something to do with the probability measure and uh like uh like why did we choose zero and one is my question why cant we have one far better

speaker_1: Thats arbitrary thats arbitrary you can choose anything you can choose anything

speaker_3: It thats it


Okay okay okay So that is not affected by our pro uh probability uh measure and our us wanting to keep it between zero and one

speaker_1: It has nothing to do no no no oh that has nothing to do with the measure its the the range of the random variable is arbitrary you can choose it to be anything in fact it becomes a function of your sensor and all that no your quantizer your sensor when you take a picture what values do you see in the picture becomes a function of what does the what does the bit representation of your machine what is the machine precision what is the quantization that you are doing and so on isnt it

speaker_3: Okay so maybe Im merging two concepts okay thank you

speaker_1: So it has nothing to do with measure okay


Okay next one Now the question is


Once you have okay we understood what happens to the elements of omega under the random variable Okay So now we understand why it is such a misnomer right Keep calling it random variable but you should imagine a function thats there Right Yeah its the biggest misnomer that Ive ever seen Its not a random variable its a function Okay Now yeah so we saw what happens to the elements of sample space under


random variable they get converted into real numbers right the next question that we should ask is what happens to probability measure there is this probability measure right once you operate a a random variable data function on the sample space what happens to probability measure is the question you can always imagine this right so now


Once


omega that belongs to omega i mean the w or w belongs to omega right and if you take that w and that is mapped to some real number lets say


Okay now what is x of omega x of omega right is a real number Im assuming that you have a one dimensional random variable in a while okay Well define that notion for n dimensional random variables after a while Lets say that you have a one dimensional random variable If you take an element a w belonging to omega belonging to omega you will get a real number Okay thats what this random variable does


No


Its a push


Opposed


What do we call that


often run out of uh alphabet


Suppose a small r is a subset of real numbers


Okay examples can be


So minus 2 and 3 right and like minus infinity to 2 and so on right all these are subsets of real numbers


X inverse of R


What can you say about this


Let me repeat the question We have a random variable which is a function that would take elements of sample space and maps it back maps it to real numbers Now what I do is I take a subset of real numbers


You understand I take a subset of real numbers Okay And look at the inverse image So this is the


In love with image


under the function x


So the inverse image of a subset of R under the function X what do you get from doing this

speaker_4: Subset of omega

speaker_1: Exactly

speaker_3: Exactly

speaker_1: Yeah you get a subset of omega from here can all of you see this there


will be some set okay which belongs to F which is a subset of omega


all of you see this is very important please let me know if you see this


questions on this Im saying suppose you take a subset from the real numbers real real numbers a subset of real numbers and look at its inverse image under this function then you will get a subset of


Is it clear


See when I ask you a question if its clear to respond otherwise

speaker_4: Here a is x inverse i is that the result

speaker_1: come again

speaker_4: Ill be using a to represent x inverse of the range subset

speaker_1: Correct correct correct correct A is the X But what is that A I mean whats more important is that that A is an element of F F is the subset of omega


Now this implies that this implies that we can talk of probability measures on


inverse of any subset of the real numbers okay this is well defined now


It is because it is equal to the probability measure defined on A which is a subset of F so this is very different Do you see this


So we can define probabilities on the inverse images of the subsets of real numbers taken under random variable Let me write that


Probability


Hold up


Inverse image


a subset of R


Im done


function f


Very fine


See note that probability measure was a measure that was defined on the subsets of omega sample spaces Now random variable maps the elements of that to real numbers Now we come backwards We take a subset of real numbers Okay And we look at the inverse image of that subset of real numbers that subset of real numbers under this function called the random variable that will give you an element from the sample space or a subset from the sample space


space and on that we have already defined a probability measure therefore the probability of the inverse image of a subset of a real numbers under the function called random variable is well defined


Did all of you get this Ill take questions in a while but yeah


Okay one by one Harish

speaker_4: So is it correct to say that uh these elements of A are the samples which are just sampled from this whole sample space or are the ones which were just observed

speaker_1: Element of which is a subset A is a subset A is a subset See you remember this no There was an omega f and p What was this f f was set of subsets of omega right


And on the elements of F is where we defined probability model which I will write that also here is that So P is a function that is defined on A okay that would take an element A okay which is a subset of F and maps it to the number between 0 and 1


This is the measure that we defined no


So F is set up


Thats your total we got


Right So we define the probability measure on the elements of f which are the subsets of omega Okay Now we are saying that the inverse image of the of any subset of r under the random variable will take us back to a and on a probability measure certain Therefore we can talk of the probability of inverse image of some subset of real number under the inverse of random variable that is well defined


Tarmish

speaker_4: Yes so since f is a set of subsets of omega so a should be a member of f right not a subset of f because anyways all the subsets are there in f

speaker_1: Thank you for that


Some mistakes


My mistake that was a that was a good point thank you for telling that


Yeah I actually meant that but I wrote subset Yeah so thats my mistake Sorry Thanks Avirup Did all you get the mistake that I had done I mean thats A is not a subset of F A is an element of F Yeah because okay yeah Avirup

speaker_4: Yeah so when you say the inverse image so are you referring to some notion called inverse function

speaker_1: Of course right absolutely absolutely

speaker_4: No

speaker_1: Because x is a function right x is a function uh when the a function always always have an inverse right that would take an element from the range of the function and maps it back to the domain

speaker_4: Okay now in that case inverse function is also a function A function by definition should always have many to one or one to one mappings But in this case we are having multiple elements from the domain and we are mapping them to a set which is a

speaker_1: No no no see when you take when you define the random variable right you can make it a bijective function so that the inverse exists


Yeah so you take every element from the sample space and map it to a unique real number


So then it becomes invertible right its a bijective function that can be inverted

speaker_4: Is it always possible to come up with a random variable which we

speaker_1: Of course why not because a random variable is something that we are defining no you always make it by definition


So thats why the inverse exists


So basically what Im saying is this function random variable always maps a unique element from the sample space to a unique element in real numbers thats all

speaker_4: Okay okay

speaker_1: Yeah see in fact even if its not a bijective right only surjection is enough for inversion but you can make it bijective nobody stops you yeah


Because you know functions like f of x squared sorry f of x equal to x squared even those have inverses So but now for I mean for ease of understanding let us assume that our random variables are all objective functions okay


Yes uh signed

speaker_2: Sir as per my understanding we have random variables map the individual outcomes in the sample space to a real number right

speaker_1: Correct correct

speaker_2: Now in the example we have taken we are saying that we have taken a range minus 2 comma 3 or minus infinity comma 2 and that we are mapping to a subset


So I agree that this subset A this can be individual elements but Im not able to digest that this subset can have multiple elements of the sample space

speaker_1: It can no because uh it depends on the way your function is defined isnt it


See its like this I tell you

speaker_2: You

speaker_1: Uh suppose theres a function right lets say f of x is equal to


of x is equal to say x plus 3 then what is the mapping 0 to 3 and then you have 1 to 4 2 to 5 and so on isnt it


Okay now suppose I take a set which is lets say four to eight


Cant I define this

speaker_2: Okay so it this will give us a range of x

speaker_1: Isnt it exactly no its a new subset of the domain

speaker_2: Okay Okay sir makes sense

speaker_1: Yeah that is why the inverse image of a subset of R will give you an element from F not an element from omega

speaker_2: no that that thats what the confusion like thats what i said

speaker_1: Its a matter of


But do you understand no no what Im actually talking about

speaker_2: Huh

speaker_1: Use an element from F because we are talking about subsets in the range space of the random variable that gets mapped to subsets in omega thats all yeah

speaker_2: Okay if if our domain is only the subset then anyways it will give give us

speaker_1: No no no uh what do you mean by domain is subset I didnt mean domain is a set

speaker_2: It might be

speaker_1: Domain is a set but what you are saying is if I consider subsets in R and take the inverse image I get subsets in omega


But if I take a singleton here I mean if this set has one element I perhaps I get back one element there right I note that a set here right A subset of R here might map back to null set also Thats also possible Yeah but thats also a subset of R See F also contains null no

speaker_2: Its also possible

speaker_1: All the possible subsets of omega and null is also a member of f therefore the inverse image thats why in fact probability measure is defined on null set also the probability of a null set is 0

speaker_2: All the possible subsets of all the possible

speaker_1: Yeah so thats why its well defined You can take a subset in the range So basically what Im saying is that you can take a subset in the range space of random variable and the inverse image of that will map back to an element in F Thats all no

speaker_2: Okay okay and that element it can be a singleton or uh it can be null

speaker_1: It doesnt matter it can be null yeah it can be that is why Im saying its simply a member of F thats all

speaker_2: It can be an easy

speaker_4: have to be an element in F but not uh say a subset of sample space

speaker_1: Same thing no subset of subset space is what we have denoted as uh f all possible subsets

speaker_4: It has to be an element in F right

speaker_1: Of course also for instance if I

speaker_4: So but

speaker_2: F is a set of subsets

speaker_1: If I increase the

speaker_4: I increase the range so now you have put minus 2 to 3 and now I change it to say minus 2 to 5 so now does it have to belong to only one element in F

speaker_1: Itll itll get to a different it will map back to a different element in F no

speaker_4: an element in F not a subset of subspace

speaker_1: Okay subset of subset of subset of subsets of sample spaces is what we have called as F F is nothing but set of subsets of sample space


What is there Okay

speaker_4: Okay so it cannot map to multiple elements in uh F is is my question

speaker_1: It cannot mat of course right


Of course right if you take a unique set in the unique subset in the rate space of any function the inverse image will map to a unique subset in the domain of the function right if the function is bijective


Simple I mean see this is like I mean your uh uh you know high school function I dont know when did you study functions was it in high school I studied it in class 11


Whatever you people I dont know yeah are we different generations perhaps no


you mean most of you may be like like between 20 and 30 I suppose right most of you yeah I have crossed 30 so maybe Im of Im often every every decade is a different generation you see so every decade they change the syllabus and all that so I studied functions in when did I study functions it was in class 11 when do the teacher teach teach them these days high school


Did did anybody study functions in high school

speaker_3: Yes at 11 oclock

speaker_4: Yes sir

speaker_1: lemon yeah leavened is not high school no yeah it depends i mean you know what what curriculum are you a part of i was i was in the state board right where this leavened was called college for some reason it was called pre university college anyway okay so im saying its just fundamental stuff right you have you have two sets we are talking about inverse images the one thing that we introduce new perhaps is that this is the idea of measure okay okay so clear so far


Okay now


Consider


consider


subsets of R


Of D


Following form


Lets say R1 is a subset of R that is equal to minus infinity to


Odd one


Again overloading locations here lets do this lets call this as s1 and this we will call as


you can call it Arman no problem and theres S2


Basically speaking it is not in close of this


So understand this notation right this set includes minus infinity does not include r1 its upper bounded by r1 here this set includes minus infinity but

speaker_2: Or how can we include minus infinity

speaker_1: Why not its an element in R no

speaker_2: It is but it is not defined right what like

speaker_1: No very much defined why not define its an element in our


You can definitely include minus infinity no problem with that Okay So let us consider these sorts of subsets of R Now


Uh yeah now X inverse of


one


is what is some element in our note lets lets call it as a1 which belongs to f okay right now the probability measure that is computed on the inverse of sets subsets


This particular type


ball


uh no this is for this this is for this we need one more bracket this okay this is building point right you understand what is this this is the probability measure that is computed on that is assigned to the element of f which is gotten by the inverse image of this set minus infinity to x under the random variable x


Okay maybe not use X here again itll make life difficult Lets call this as A


Is this clear to all of you This is a well defined measure no The probability assigned to an element of by the way have I already said this This is also called the event space okay F has a name Its called the event space So this is the probability measure assigned to the element of the event space that gets mapped to


gets mapped that that that gets mapped to a set minus infinity to a under x or rather it is a probability of the event or probability of the member of the event space obtained by taking the inverse image of this subset minus infinity to a under the random variable x do you understand the statement if you understand the statement that you have understood everything that ive said so far shall i repeat the statement okay let me write that term maybe its better to write it this is


is the probability of


D


element


in the event space


The art is obtained


pain


By taking


the inverse image


of T set


minus infinity to a


Under


the random variable X Is this clear Any questions on this


All of you please ensure that every one of you understands this

speaker_2: Uh Sir can you explain what is under the

speaker_1: Im not familiar with it

speaker_2: And thats a good one

speaker_1: X is a function no see when we talk of inverse images we have to test we have to we have to specify what function are we looking inverse images under


See when you take a subset and you talk of inverse images what is the function under which you are taking the inverse image It is a random variable which is a function correct

speaker_4: Is it does it mean that lets say if we take S of some sample space well reach out to a particular range If you take inverse of that whatever the sample space or the event space that we end up in probability of that is what we are defining here

speaker_1: Exactly exactly But we are looking at particular subset of real numbers No this particular subset The kind of subset that we are looking at is like close minus infinity to open a


Carter Kumar

speaker_4: Oh yes sir so thats it

speaker_3: Have I made a relation with

speaker_4: The

speaker_1: But why not make it bigger

speaker_4: So

speaker_1: Particular water is breaking

speaker_3: Sorry am I audible

speaker_1: I need to know

speaker_3: I need to know

speaker_1: Is it only for me

speaker_3: Uh

speaker_1: His voice is breaking

speaker_2: Im not sure

speaker_4: Youre just kidding

speaker_1: Is it still

speaker_4: Uh is it still breaking so

speaker_1: Yeah not now try try now

speaker_4: Yeah I just wanted to ask is A anyway related with R1 and R1 which we defined S1 with Minus infinity to R1

speaker_1: But well it takes in the sense that uh like uh this particular r1 is the is I mean this particular set is the one that maps back to a1 thats all other than that there is no relation per per set

speaker_4: Okay so yeah I mean like uh

speaker_1: If you take this particular subset and take the inverse image of this it will go back to EMIL thats all

speaker_4: Okay yeah sure thanks

speaker_1: Okay great so this we lets give a symbol for this let us


E this call this as px evaluated at a


This is a symbol Okay What is it saying is I mean I just represent this complicated looking thing using a simple symbol right I mean this symbol actually means that I am looking at the inverse images the probability of the inverse image of this particular type of subset minus infinity to a under the random variable This is the symbol Is this okay Im just using the symbol for this complicated thing Is that okay


Okay It turns out that this has a name This particular thing has a name which all of you know Do you know what the name of this is

speaker_3: Really is

speaker_1: No no not PDF This is the cumulative distribution function Yeah this is the distribution function

speaker_2: People have to test it before

speaker_1: This is the distribution function of a random variable


Some people also call it the cumulative distribution function I mean I dont know why it is called cumulative You dont have to call it cumulative okay But this is called the distribution function of a random variable Is this clear So what is it

speaker_4: since it accumulates the distribution

speaker_1: from minus infinity to no no no no no no no no pre space there is there is no accumulation thats happening up see

speaker_3: No no no no no

speaker_1: The reason perhaps why people call it cumulative is because you define a density function and then you like you can represent the this this function as a running interval of that other function and thats why its called cumulative but I Im not a fan of this term cumulative I mean standard textbooks call it a distribution function and yeah this is a distribution function okay now what is a distribution function its its the probability of the element of event space that is obtained by taking


the inverse image of the set minus infinity to a under the random variable x so if you evaluate this distribution function at a value x or a it will remember that you are actually looking at the probability of an event probability of an element from the event space what is that element that element is the one that you have gotten by taking the inverse image of this set minus infinity to a under the random variable x


Is this clear


This is the single most important definition that well be looking at because the entire machine learning is estimating this particular function given elements from the range space of random variables That is all the B generative models discriminative models classifiers regressors anything The entire machine learning is about estimating these functions the probability density functions sorry distribution functions


Okay so in fact instead of calling it cumulative distribution functions now let us call them the probability distribution functions you know that is


Its put on me


probability of the BLT distribution functions probability distribution function of A


Is this clear


Please remember that if you evaluate the distribution function at a particular point


Okay if you evaluate the distribution function at a particular point what are you actually doing


you evaluate the distribution function at a particular point youre actually getting a probability probability by definition is defined on the elements of f now evaluating distribution function at a particular point should give you right the probability of a particular element in f what is the element in f whose probability this function is giving you it is that element in f okay or rather that subset of the sample space which


Ease


getting map to minus infinity comma a under the random variable x


Is this clear


Please remember this because as I said this is the single most important demonition that we need for this course So yeah Questions on this Sanket H

speaker_4: The probability distribution function is usually the probability at a single point right

speaker_1: Definitely no no no definitely not I mean that is that is precise three and a half hours to define this it is not that


See point number one I am I am not talking about probability density functions here I am talking about the probability distribution functions

speaker_4: Point them


Okay okay

speaker_1: Okay and even probability density functions are not probabilities Please remember that probability is a measure that is defined on elements of F period You cannot talk of probability of X being equal to something It just does not make sense You understand


Because by definition by definition probabilities are defined on elements of F Thats all See its like can you talk of length of length of okay what do I say


If I say length of water length of water right or length of length of speech or something its just not defined right Length is defined only on elements of subsets of R isnt it Similarly probability is a measure that is defined only only on subsets of omega So whenever you talk of probability you should always make sure that you are talking about the probability of an element of F


That is why this distribution function while it is denoted as P x a okay this actually means this entire thing


Whenever I write PHCA in this course you should always remember that Im talking about this


Okay you should remember that there exists a function called random variable Okay and this random variable has an inverse image The inverse image of we are considering the inverse image of this particular set minus infinity to a Now that gives you an element in the event space that has a probability associated with it and that is what this function is giving me Always okay


This is clear because I want to make this damn clear to all of you because people very wrongly say that the probability of a random variable its there is nothing called probability of a random variable


Okay it does not make sense You mean its like you know saying round circle or something There is no probability of random variable There is probability of elements of f So if you evaluate the distribution function of a random variable at a particular point what you are actually doing is this entire thing


Okay please be clear about it Rajan

speaker_3: So sir my question is when we are taking the inverse of a subset of R then it might not be having any element in F right for example

speaker_1: It will always be it will always be it will always be He cant

speaker_3: Most of the time

speaker_1: How come

speaker_3: Yes example tossing a coin will have outcome of head and tail And suppose head is translated to 0 under random variable and tail to 1 Then if I take if I try to take the inverse of for example 3 which

speaker_1: Then it then it maps back to null thats all and null is also an element of it

speaker_3: I got it in that case probability will be

speaker_1: Zero

speaker_3: Project Thanks

speaker_1: Actually mentioned this maybe you missed it no problem have a look


Whats up


a little down we might come to that see please again im reiterating dont jump we will not leave anything in this course okay we will address all those questions okay but uh see when i when i ask people questions right do ask please ask me questions on things that we have discussed so far because otherwise right if you jump ahead uh then you know it will sort of break the flow please dont take it in a negative sense uh just to ensure that you know we are going systematically


we may mean thats a good question by the way how do we estimate px uh is the question that we ask in machine learning all machine learning is about estimating this distribution function okay so dont worry well come to that in the next next part of this class in the genes

speaker_4: Yeah when you say you are taking probability of inverse random variable minus infinity to a

speaker_1: Uh just a second please please please uh use correct terms theres no inverse random variable


So can you can you say it correctly


probability of


So uh just just I dont c say correctly

speaker_4: So inverse probability of a real number

speaker_1: No no no not the inverse probability see inverse is defined for a function

speaker_3: Yeah okay

speaker_1: The universe is defined for a function


inverse of the function called random variable


That is how we should say it

speaker_4: So when you are taking that set as minus infinity to a

speaker_3: Can I see any

speaker_4: Any other set say

speaker_3: They wont do it

speaker_1: Im glad that you asked that question I wanted somebody to ask this Its a very good question So why are we considering this particular set What is the whats so whats so nice about this particular set is the question that youre asking correct


Yeah Ill answer that next Thats the next thing that Ill do but Im glad that you asked that question Ill answer that I was expecting someone to answer that question Ask me that question right Why it is so satisfactory about this particular set that we are assigning a function to it right I mean rather like we are calling we are giving it a particular name What is so important about this Ill answer that in a while Okay Okay


Now see its related to the other question that Indrajit asked Okay why what is so I mean what why why is this particular set right That is the next question Okay well answer that question perhaps Now it turns out Ill just state that without the proof maybe yeah I okay By the way there is one other convention


I can tell you that why


I think this question has to be answered


So the answer to this is it turns out


any substance in R


and being represented


Set operations


Thats a form


So does okay so here is the convention okay


So from now on whenever I state something okay without proof or without giving you a lot more details I will mark them as tutorial items Okay Now I ask one of you like or maybe


All of you two take a note of it okay and just put it in the teams as tutorial items and this has to be covered in the tutorial by TS I will keep doing this from now on


Okay anyway so the thing is any subset in R can be represented by our set operations over these kinds of sets That is the reason we are interested in this kind of set


What does that mean That means that suppose


if you take a set subset a b okay that is in r


This A B


Cant be done as well


Yeah this is a sub sentence


is good


Sorry

speaker_2: We need to have square braces for a comma b set a comma b

speaker_1: Because that is uh those are included no Yeah I think what I had written earlier was correct


Heres one example I think TS will do a proof for this So basically what Im saying is that if you can take any subset in R and that can be represented using the set operations on these kinds of things


Okay and we know that that you know probabilities measures probability measures will add up So therefore if you want to take prop if you want to look at the probabilities of lets say that you are interested in the probability of


um the inverse image


of this particular set


particular set this can be right obtained in terms of


The probability the distribution function that is evaluated at B subtract that with the distribution function that is evaluated at A So again the proof of that shall be done in the tutorials

speaker_4: included in that interval right

speaker_1: B is not included in the interval is that so


Yeah because its not included in the interval A is included B is included So yeah A is included B is not included I think this should be correct Correct This is what youre saying B is not included in the interval

speaker_3: Yeah because its not included in the minus and minus

speaker_1: Yeah so this is why we are interested in this particular set that if we want to look at the probability of the inverse image of any subset of R okay we can obtain that in terms of the probabilities of events that are associated with the inverse images of


this kind of subjects okay that is why we are interested in this particular type of subjects


Okay does that answer your question I think it does not ask this question And why are you interested in this particular subset Its because of this that we can obtain the probabilities of inverse images of any of subset of R and B subsets


Now what is this has a very big implication this implies this implies


the probability distribution function


Function completely


complete COOM PLATE ELOY completely specifies


underlying probability measure


So what I was saying is that if you know the distribution function then you know everything about the underlying probability interval


Can I make that statement So basically what happens now that you start from this is what you have this is the probability triplet You have the sample space the event space and the probability measure Now this when I operate a function called random variable on top of this


Then what happens is this will induce another measured space that is called an also pointy push forward measure This will map omega to R and it will map F2


subsets of F okay which are subsets of R which are also called the Borel sigma algebras Dont worry about it its just a name given to specific subsets of R and the probability measure gets pushed forward into distribution function


This is a big story


Okay now the thing is in practice no access to this you know we dont have access to this


Okay but this is accessible


The data that we get are actually the members of


This is odd


Okay so now when we have like thousands of images theyre all members of this R Okay now because we have this we always operate with R B and PX We dont even look at BR and PX So now if we get PX then we know everything about the underlying probability space Okay this is by the way this is also called the


the probability space or probability interpret


And this is called the


Push forward or induce space


Its actually a space that is induced by a function on the sample space which is called the random variable


forward are the induced space


So we simply work with this accessible and work with this


The work with distribution functions right and the elements of the range the elements of the range space of random variable thats our data Okay that is our data


But you should always remember that whenever we talk of a random variable and a distribution function you should always remember that this random variable is a function that has an underlying underlying probability space OK and the probabilities that we are talking about are on the elements of that f event space OK this is the clarity that you should have So in other words if we know what the distribution function is then we know everything about the underlying probability measure And that is why entire machine learning is


as estimating the problem of estimating the probability distribution function given data i will write down on this right yeah so i just wanted to tell you that that uh that why is uh why are you working with random variables and what are random variables and what are distribution functions hope that you people are clear about this okay uh questions no sanchit

speaker_2: why are we taking the concept of Borel sigma algebra here

speaker_1: Because uh the when you have this random variable right that would take omega to r f right get pushed forward into Borel sigma algebra

speaker_2: So like for Borel sigma sigma algebra what understanding I have is it will have all possible subsets of the form A comma B

speaker_1: Correct correct true That is why no f gets because you know those are the those are the elements those sets those subsets of r gets the map back to elements in f no thats why the push forward uh um push forwarding that happens from f


Why I write random variable is Boolean algebra


Im not Im not telling you that because as I said no you can mostly ignore this B because we are basically what Im saying is when omega gets mapped to R what happens to F F gets mapped to Borel sigma algebra thats all

speaker_2: Then sir by default the probability measure should be a length measure right

speaker_1: No no no yeah not necessarily because probability measure is defined on the probability triplet no But but I mean thats a good question that you ask See we can integrate distribution functions right

speaker_2: We can what

speaker_1: Integrate distribution functions we can differentiate distribution functions right

speaker_2: Correct correct

speaker_1: Operations of integration and differentiation are defined on Lebesgue measures


That is one of the reason yeah length measures no operations of integrations and differentiations are defined on the length measures Lebesgue measures


Now since that is one other reason why we need a random variable See you cannot integrate in the the probability space because integration is in probability space is not defined at all


Right So once you get to the uh the the the uh the push forward or reduce space you can do integration Thats why you can differentiate the distribution function and you get another function called the density function Right You can integrate the distribution function You can do all those things The the the default measure is not the length measure The length measure is defined only on Borel sigma algebra Okay Under the random variable right Once you do the push forwarding you get the the Lebesgue measure Before that


Its the probability measure only

speaker_2: So once we have an induced probability space we have a Borel sigma algebra and correspondingly the Lebesgue or length measure

speaker_1: Correct but we are not interested in the length measure on the Borel sets gotten from the push forward induced space We are interested in the probability measure that is obtained by the inverse images on the subsets of R Because we are interested in finding out the underlying probability measure not the length measure of this Borel space

speaker_2: Okay okay

speaker_1: Because the whole purpose is to model that picture and and map it to a gender or something right


We are not interested in the Lebesgue measure of this push forward space We are interested in these kinds of induced measures right which are called the probability distribution functions Yeah


Okay so rest of the people can ignore this discussion if it didnt make sense Okay so dont worry I mean that was like slightly off topic Okay the pian

speaker_4: So this is in the space we have data so this probability PX that is calculated based on the data or its available exclusive uh otherwise also

speaker_1: No it is not available no the whole problem of machine learning is to estimate the speeds we dont have the speeds with us


I will need to say that see what we have are the elements from the range space of random variable thats all that is our data


The X will be

speaker_3: The X will be

speaker_1: Whole problem going to be to estimate it


Entire machine learning is estimating PX okay

speaker_3: Got it sir

speaker_1: Well I will define that I will define that in a while uh yes Raghuvendra

speaker_3: Yes uh in general do we also know X always or

speaker_1: we will not know x we will only know we will only have elements from the range space of x we will not know x see when you have images right or do you have you have a lot of real numbers right each each image is a set of real numbers correct yes what is that thats actually the elements from the range space of random variable you dont know what the random variable is


Im telling you again random variable is not a variable its a function so please remember that


Okay um is this clear uh sentence has one more question yeah sentence

speaker_2: So basically we have a probability triplet and in order to have an ease of operations we are you know inducing the concept of random variables and not only

speaker_1: Not only not only that not only that right ease of operation is of course one because we can integrate and all that there is one other reason no the way i motivate it is you dont have access to omega fp


In in in real world what do you have access to you have access to real numbers you know how do you see real numbers as elements of omega no you cant there is something that is there is something that is

speaker_2: We just have the outcomes that are not

speaker_1: We dont even have yeah we dont even have the access to outcome we have access to some measurement of the outcome

speaker_2: Correct

speaker_1: And how do you quantify that using math that is quantified using a random variable no

speaker_2: Correct correct correct

speaker_1: So basically there is a function that is sitting on top of the outcomes which is giving you the real numbers That is what we have access to


And now since we have measure defined the probability measure on the subsets of outcomes we need an equivalence in the induced measure That is your distribution function That is your distribution function

speaker_2: I mean thats a good question


Sort it sir


Got it sir

speaker_1: Yeah but always remember this definition is very very sacrosanct I mean this is you should remember this Whenever I talk I mean I will be talking of distribution functions all along the course Okay Whenever I talk of distribution function you should remember this You know I suggest all of you go back today after todays class sit down maybe rewatch the lecture and try to get this idea solid into your mind Okay Very very important


lot of people hand wave on this and wrongly represent distribution function as probability of random variable that does not make sense at all so please get this get these ideas


Nicely into your mind okay uh in the teens

speaker_4: Here does it really matter whether we include A or B endpoints or exclude them

speaker_1: Here that


It depends no you can take any set here and as I said any set can be represented using these kinds of sets thats all you can take any set you can take the inclusive inclusive sets exclusive sets doesnt matter you can represent any set like this using these kinds of sets operations on these kinds of sets okay


Okay great um okay bridge move one

speaker_3: Hi sir So lets say using machine learning we have successfully approximated PX which gives us basically the ability to tell how probable it is that well see a subset of event space A in real life correct Up to this point am I understanding So how does this understanding translate into us knowing about the actual underlying P of


So the the probability

speaker_1: So that is your p no that is p what is p p is the probability of a particular subset in f if you know that you know that thats all


See maybe you should ask a different question right why how will that be important or relevant in telling what is the gender of this particular person is right obtained from that image


That question I have not answered yet I will answer that question But if you estimate the probability distribution function then you know everything about the underlying probability measure

speaker_3: Okay so just Ill say a statement Please help me understand where Im going wrong in this So once we approximate Px so Im thinking of Px as a function that takes an input and generates an output So the output that is generated is P is a part of P

speaker_1: do you mean by output i didnt get that see the probability distribution function is a function i agree right yeah whose uh like uh whose uh range is zero to one


Ah now what is the question

speaker_3: So uh from the definition of Px what we get is the likelihood of observing A

speaker_1: No I have like have I have I defined the term likelihood

speaker_3: Uh oh okay

speaker_1: Please dont use the term because all those are mathematically precisely well defined dont use the terms that are not defined

speaker_3: Okay so

speaker_1: If you evaluate the distribution function at a particular point itll give you the probability of the inverse image thats all it is


No yeah that is the question yeah

speaker_3: So the probability of inverse image or to go with the notations probability of the output correct

speaker_1: So again there is nothing called probability of A This is again this is a notation When I evaluate the distribution function at A what am I doing is I am looking at the probability of inverse image of this particular subset That is all it is There is nothing called probability of A Please


That is the you know misrepresentation that I want to take out of your minds When you evaluate the distribution function at a point okay you are not getting the probability of that point That does not even make sense

speaker_3: Oh sorry I was not talking about small a I was talking about capital A the set

speaker_1: Oh sorry my bad Yeah it is the probability of A correct A1 I have said it as A1 no Yeah

speaker_3: Yeah okay A1 So now the probability of A1 is actually that underlying P correct that we were talking in that first triplet

speaker_1: Yeah of course no P is a function P is a function that will take an element of F and gives you a number between 0 and 1

speaker_3: Got it so I might have to

speaker_1: I have my turn

speaker_3: Yeah so am I underst uh am I correct in my understanding that the output of px on small a is actually something in the the p on the left hand side of this uh uh

speaker_1: Thats correct Thats precisely correct Yeah if you evaluate the probability distribution function right at a particular point A it will give you the same output that the probability measure right would have given on the subset A1 Correct That is correct

speaker_3: Okay yeah thank you so thats it

speaker_1: See that is why that is why that is why


That is why capital P right is a function that would take elements of F and map it to 0 1 correct


And probability distribution function okay will take an element of R and still maps it to 0 1


You notice that the range space of both of these are same


My definition my definition

speaker_3: Interesting yeah that clears it up thank you

speaker_1: Okay thanks


Okay anything else


So take home message is the following right When you take the distribution function and evaluate at a point what does it give probability of the inverse image right of the event that is obtained by taking the inverse image of this particular set minus infinity to a under the random variable x This is the take home message Remember this How do I


I think this is something


Does it stay Ah it stays hold on


It is the end


Its super duper important okay


Oh does red means that this is wrong or something when its not used red or yellow is okay


We are

speaker_4: So if you change the if you change the paper colour then it will be more visible

speaker_1: From black to white

speaker_4: White or yellow

speaker_1: is fine yeah please remember this this is the this is the message that im supposed to give today okay


Im mm


Okay uh shall we break for 15 minutes


There is one other nice question that I was expecting nobody is asking me anticipated an answer


It is 10 45 in my clock lets get back at 11 pm okay lets solve 11 am okay see you in 15 minutes


So begin continue


Tell me this show of hands please Is there anybody who has not studied a probability theory course in your undergrad


Like no probability theory course at all Is there anybody of anybody like that in the class


When you raise your hands there is somebody like that

speaker_4: So can you repeat

speaker_1: So is there anybody who has not taken a probability theory course like ever in your life undergrad or something


Okay nobody good See the reason I asked is that like see all of you know these things maybe in different forms right Maybe not this rigorously or in different forms I just am trying to give you a different perspective Thats all right So yeah So you people are aware of these things know that cumulative distribution functions you have heard these terms and like you have worked with these correct Gaussian distributions and all this Have you Most of you have worked with these things


with these things right i mean you are aware of these things earlier its good so as i said no the first two three classes initial two three classes i think i i develop the language and give you perspectives of how i would like to see things and then from then onwards you can take off very quickly okay uh lets get back so now we are we have uh the probability triplet and we have a reduced space uh uh a distribution function associated with it now um


the Pandora box of probability theory now theres too many things that come up Ill just define a few things that are kind of


obviously needed for our our cost and then well move on see the first thing that i want to define talk about is


Vectors valued random variables


Again another misnomer okay So vector valued random variables This is these are random variables right That such that the range space of these this function that we are talking about is R and D and not R the vectors okay


Do you understand


So what is happening is the elements of sample space now gets mapped to d dimensional real numbers not one real number All these while we were looking at like real numbers here right The mapping was to real numbers okay Now in a vector valued case which is our general case right When we have images or like embeddings of text and speech et cetera they are all some d dimensional vectors So these are like vector they are called vector valued non dimensional variables because


The range space of the random variable that we have will be vectors d dimensional vectors in general Any questions on this


great so in this case right when we


evaluate the distribution function right the distribution functions gets evaluated at a vector


a right now the argument for the distribution function will be a vector a i will not be using this uh like head bar after that but this is just for once okay so how do you define this now this is the probability


Probability okay so let us take an example and do it perhaps easier that way to show


So example suppose


Suppose the random variable is


dimensional okay maps the sample space to two dimensional real numbers okay now what happens to


the distribution function of this by the way any notation that I know this is the notation that I will be using when I write this subscript okay uh that that denotes the random variable okay and whatever is within the brackets is the value at which we are evaluating this so now how do how should I evaluate this x


What should I write inside the bracket now

speaker_2: x inverse and within brackets the vector

speaker_1: No no no Im evaluating it at a point The notation is that probability density distribution function is evaluated at a point And what is this point This point is now some vector A1 into correct


All of you with me on this


Because the random variable is a two dimensional random variable distribution function is evaluated at a vector Now again well interpret this Now what does this mean This is the probability of what


Again our own notation right it is the probability of the inverse image under x of what set are we considering here Can somebody tell me what is this set


Do you understand

speaker_3: You understand infinity to A one minus infinity to A two

speaker_1: Minus infinity two

speaker_3: A1 and minus infinity to A2

speaker_1: So what should I This is one set What should I write I should write a bracket here


Im trying to write

speaker_3: In fact this is an area sir like uh uh uh

speaker_4: This is also a question

speaker_1: So what should I write here tell me how should I write that

speaker_2: Ross

speaker_1: Okay so does all of you understand this What is this cross This is what is this cross


Or the cartilage product yeah


Well just tell you what that means See in one dimension if you have a line there is an A right The set that we are talking about is minus infinity That would end at A correct So this is the set that we are talking about Minus infinity to A is this particular set correct Now in two dimensions


If you take a point like this is a1 comma a2 right what is the set that we are talking about now we are not talking about this as the subsets of R2 they are not lines what are they

speaker_3: Yeah

speaker_1: uh what to call them areas

speaker_3: Playing

speaker_1: planes yeah they are planes okay first of all subsets of r2 are planes okay so what sort of uh plane are we talking about so lets say that we have a1 comma a2 here this is where we are evaluating the distribution function what is the set that i just wrote what does that correspond to

speaker_2: Or anything to the left of

speaker_1: This is uh this is A two

speaker_2: Yeah

speaker_1: And this is A1 Now tell me what else is that Im talking about

speaker_2: towards the left of line A1 and below the line A2

speaker_1: Okay so this is line


space this entire space which extends uh infinitely infinite to to infinity to in the left direction and to infinity in the bottom direction is this clear so this set


Cartesian product of


Is all of you clear


Now we will not be working in two dimensions we will be working in like 10000 dimensional space because our image is in 10000 dimensions So when I evaluate the distribution function at 10000 dimensional point a vector at 10000 dimension you should remember what is the inverse image that it maps to Its a Cartesian product of like all those things Do you see that It will be a hyper volume in that dimension


Is it okay


See when I evaluate the distribution function at a particular point in some 10000 dimensional space Ill be looking at the inverse images under that random variable of a certain hyper volume What is that hyper volume That hyper volume is given by this sort of a Cartesian product minus infinity to the first element cross minus infinity to the second element cross minus infinity to the third element and so on That becomes a hyper volume In three dimensions I can tell you what that is No its a huge three dimensional volume right In four dimensions


I dont know what it is just call it hyper volume


Is that okay So well be working with such distributions Well be working with random variables whose range space happens to be in some d dimensional real space And if its an image then it is some 10000 dimensional If its say what is the size of the embedding in bird kind of models Its a few hundreds right A few thousands I suppose


Can somebody tell me in bird kind of models what is the size of embedding vectors that you get for each bird This Google that


BERT embedding size

speaker_3: 8 12

speaker_1: Huh its poison fly for me


Thank you


768 length vectors word base and word tiny gives you 128 dimensional vectors yeah of order of 100 so that is that is your uh like that is the dimensionality of the range space of the random variable that you will be that ill be working with is this idea clear to all of you


questions on this so from now on well be working on working with vector value random variables okay not this which means that the elements of sample space gets mapped to a d dimensional real number okay


products Cartesian products okay fine now the next thing that I want to talk about is that


Why doesnt it come to a middle


thing


B


talk of multiple random variables


Okay now suppose there are two


random experiments that are happening


Let me give you an example what I do is first


In the


Its its


We are saying we are in the example


Theres a coin that is being tossed


And there is a die that is being loaded


D I E or D I E what is it D I E is it no D I E


EYE is colour I suppose no

speaker_2: Yes sir it should be D I E S

speaker_1: We are eating

speaker_2: If it is singular it should be D I C E

speaker_1: Times correct


So dice being rolled okay thanks yeah so now what happens is see both of these will have their own sample spaces and underlying probability measures right lets call this p1 and there is another sample space another


Event space does not probability measure correct


Right Now what I can do is can take an element A belonging to F1


and an element B that is belonging to F2


Okay and do this


Hmm


Im just thinking is this the best way to take over this point Im just going to do it


Which is not the best example


Yeah this may not be the best example because


You can send uh


Intersections no the art would create some lack in understanding


To talk that there are two random experiments okay so it is like uh


I said holding


Ooh


different configuration I think this would be a better example


So this can be a good example that here what we are doing is that we are we are throwing two dice of different configuration which means that there are two sample spaces again and two different probability measures


to okay now again if there is an element


that is in F1 and an element that is in F2 right Because these are sets we can talk about unions and intersections of these right


Can you see what Im talking about


We have two random variables We can talk about unions and intersections of these events right These subsets or these yeah these subsets of different sample spaces Now because we can do that there are a few things that are being defined which are like something called you can define a probability measure


In fact see the unions and intersections may not be on two different sets right I mean unions and intersections may be on


like one random variable as well unions and intersection maybe on a single random variable as well but yeah lets say that we are defining unions and intersections of the uh the


So the elements of outcomes from two different random variables you can always talk of probability of unions and probability of intersections and so on There is also this conditional probability that is defined which is defined as a conditioned on b and you know the definition right it is the probability of the intersection divided by the probability of


condition in event this is how the conditional probability is defined all of you know this right thats why i asked you whether you people know probability theory this is known right all of you know this okay great now what i wanted to tell you because we can define uh like conditional probabilities and unions of probabilities on on on on uh outcomes coming from two different uh experiments now now what happens is


There are two uh probability spaces


There are two probability spaces which means that there are two reduced spaces Lets call them X


gives a rise to


point distribution function okay theres another


sample space and the corresponding probability measure its called that y this gives rise to another


induced measure


Now since we can talk of the unions and intersections of the elements from the sample space we can talk of what are called as joint distributions


See I will kind of hand wave now and not talk I mean not go to details of the definitions So this is represented like this which is a joint distribution of pair of random variables Now this is evaluated at two points no x y k b lets call it


Okay what does this mean Well go to our own definition This is the probability Okay so now this is like you take the X inverse of this particular event for the yeah the event that gets mapped to this particular thing under X Okay you take the Cartesian product of this under the random variable Y take this event that gets mapped to


maps under this inverse image and that probability right so this will be the probability of some event a that belongs to f1


intersection from event B that belongs to F


Is this clear Oh what happened to this


Is this clear


So we can talk of joint distributions right I mean joint distributions are again we are talking of probability of intersections of events Now these are intersections of events that are belonging to two different sample spaces Now these are how do you get it You take first random variable take its inverse image get one event take another random variable take that take its inverse image you get another event take the intersection of those two and that is the and look at the probability of that


And that will give you the value of the joint distribution function evaluated those two values Okay so similarly you can also talk of conditional distributions


definition of conditional distribution is slightly involved okay let me not give you the the definition of it okay denoted by this okay this is evaluated at one point this is


is like X


equal to vertex


given y equal to some p okay


I mean I dont want to


in continuous random variables no this step this has a very this has an involved definition but roughly you can see that as the we are looking at the probabilities of


these kinds of events right conditional events so we are looking this corresponds to some conditional uh the probability of some conditional distribution its the probability probability of some conditional event okay that the definition of condition the conditional event is this which is that you take the probability of intersection and divide it by the probability of the uh the uh the conditioned event so it has a similar definition but yeah its yeah you need a little bit of measure theory to know this at least for


the case of uh uh


continuous random variables and by the way all the definitions that i have given so far are for continuous random variables if its a discrete random variable now what happens is the mapping that the random variable does is element by element so you are talking about the inverse images of singletons okay this is a conditional distribution so basically what i want the the two points that i wanted to drive home is that there can be random variables which would take this


sample space and maps it to vectors and there can be pairs of random variables where you should envision you should you should you should imagine two uh random experiments that are happening okay so there is an association between those two uh random variables that happens through intersections and unions of events okay and and you can define joint distributions and conditional distributions now definition wise this is defined as


Okay


The joint distribution divided by


of entropy so it is defined mathematically uh but yeah so it always has a a corresponding uh probabilistic interpretation as we were looking at okay okay uh questions uh abirup

speaker_4: Yeah so I could not understand a couple of things can you scroll up a little bit

speaker_1: In which party Dr

speaker_4: Yeah after after after the vector valued when you were actually

speaker_3: saying that uh


Then uh


A and B they

speaker_4: I I cannot understand the notion how you can do it

speaker_1: You can know see its like you take a set uh lets say that we have two subsets of R you can define a union of both of them right why cant you do that

speaker_4: Yeah so

speaker_3: That is because in


So for

speaker_1: Same thing Im saying youre only two types of different configuration the universal center same thing right

speaker_3: So in in case of age

speaker_1: That is why you you remember I said toss a coin roll a die


Then I erase that example precisely because of this It will create confusion In the example that I have given the universal set is the comprising of roles of dice for both the cases

speaker_4: Okay so if we are considering one event space as rolling a die and another event space as tossing a coin

speaker_1: Then the universe will be one two six and those two things head and tail thats all

speaker_3: Oh

speaker_4: Uh okay so it is going to be F one union F two

speaker_1: Of course of course sigma omega 1 cross omega 2 omega 1 cross omega 2 that would be your universal sample space


I didnt want to do that because of this precise reason so if you roll a die and toss a coin then how can you define unions is a question that I anticipated thats why I said roll two dice

speaker_4: Okay okay okay And also as the second question when a little bit down if you dont mind a little bit scroll down


Yeah so x inverse of minus infinity to a cross of y inverse of this one


How are you replacing the cross sign with an intersection sign in the next line I have a difficulty in understanding that

speaker_1: Ah see the cross products here right in the condition this matches to one event that matches to another event right Okay So that is the intersection only


Okay so the point is that here when you talk of intersection you talk of cross products of two sets is it correct


This is cross product of two sets so the intersection is nothing but cross product of two sets no

speaker_4: Yes


Yeah yeah

speaker_1: Thats it


Okay service

speaker_4: is the same thing like x inverse of minus infinity a gives a

speaker_1: That gives you P

speaker_4: gives B and same thing like it doesnt A cross B right

speaker_1: It is defined that way you know joint distribution is defined that way by definition

speaker_4: So its a cross product right so uh

speaker_1: Correct it is by definition

speaker_4: Below it should also should be a cross be right so there will be pairs ordered pair

speaker_1: No no no A is no no no so there are two sets not talking about two sets here so probability is defined that is why you have

speaker_2: And B

speaker_1: The the proper idea intersections are defined


Okay so here the joint distributions are defined that way that if you evaluate it they are actually the intersections of see in fact I should I dont know where the definition is coming from Lets just say that these are intersections by definition And so then that will create that will clear the thing no


And thats thats the definition of job distribution by the yeah


Okay uh Sanjay

speaker_2: if we try to understand joint distributions with an example so okay let me just uh explain what i perceived by this statement is we have we want to find the joint distribution for events where there is a three on the first die and a four on the second die okay so getting a three becomes event a and on getting a four on dice two becomes event b so we want to


So both

speaker_1: So those two those two gets mapped those two gets mapped to different uh points at the by two different random variables and you get the inverse bits thats all yeah its correct

speaker_2: Correct correct So now when we want to find the probability that event A belongs to F1 and event B belongs to F2 so it will only be both are happening So that means we will obtain the Cartesian product of F1 and F2 and in that only point 3 comma 4 where 3 is obtained on die 1 and 4 is obtained on die 2

speaker_1: Oh stop packing


Agreed Thats thats the that thats the intersection that you have yeah

speaker_2: Yeah that is the only intersection right because otherwise since both

speaker_1: Is the only


Got it


I understand what you see yeah okay yeah uh

speaker_3: So in this case the x and y have to be independent right

speaker_1: need not be if they are independent then they I mean I have not defined independence right random variables are called independent if the joint distribution happens to be product of marginals


If they are independent then intersection is null


They are not independent right This is the general definition General definition is one experiment

speaker_3: So there can be one experiment can be dependent on the other dep

speaker_1: They are they are actually I mean the moment I talk of joint distributions they are dependent now


If they are independent then the joint distribution will become the product of marginals centered

speaker_3: And no no what I meant is say for example in this case of uh rolling two die the outcome of uh the second experiment shouldnt depend on the outcome of the first

speaker_1: And the way we have conceived it they are independent


Independence is if P of XY is given by PX into PY then it is independent

speaker_3: Okay but this not a necessary condition

speaker_1: No why I mean the way we have conceived the pair of random variables is that in general they are not independent right

speaker_3: Okay okay

speaker_1: Uh she wont

speaker_3: Just sir I dont have any question just one uh thing that I am getting confused with small y capital Ys I last time also

speaker_1: So where is small by Im not in small by its all capital right now

speaker_3: Those are yeah on the conditional distribution so its all random variable right so capital Y

speaker_1: Im sorry my my bag sorry

speaker_3: No so in your previous lectures also

speaker_4: The small y and capital Y we tend to use it

speaker_1: Yeah thanks for thanks for bringing that up if I make that mistake again just allow it to me okay

speaker_4: Thank you

speaker_1: so so that i can i can correct myself yeah see yeah this is i think uh how what is the how many times ive taught no um 2017 is when i started this is 2024 seven years so on an average i mean not on average every time ive taught every semester theres 14 times and this online some three four times but theres 17 18 times ive taught so what


you are seeing now is actually uh ive done gradient descent on my teaching based on feedback every time and it has come to some optimum and that is what you are seeing so imagine what my students have the plight of my students so many years back i didnt know how to do board work right i was like in spite of doing it for 15 times 18 times sometimes the notations gets uh here and there and all that but yeah i think ive improved right


of my students tell me that Ive improved over time Thats why I have that feedback form you see Please use that if you have any concern that you cannot When Seon was bold enough to tell me that I do this I appreciate that I dont mind You can tell me that this is youre going fast Whatever you know I dont mind Okay You can express it But if you think that expressing that will embarrass you for whatever reason


You have that anonymous feedback form Do put in your comments right Constructive destructive I told you right A lot of times students use it to vent out their frustration Its okay at times you can do that but dont use it for just venting out your frustration That will be too much negativity


Great Okay So Shivan thank you for that If you if you if you notice such a such kind of a thing just let me know Ill try to be consistent as much as possible in notations I understand how important it is to be consistent


Okay maybe Ill take this B out Ill tell you why this why I wrote this in a while Okay so these are Im kind of hand waving now because like this is not a probability theory course right This is just to build some basics on it


Now let us come to uh yeah independence conditional distributions joint distributions multiple tandem variables yeah one other thing that is to be defined is what is called as a probability density function

speaker_3: I dont know

speaker_2: Im finally getting it

speaker_1: Was that some gali in some some language If you speak in your language that I dont understand right what can I do


See gales make sense only if you make the other person understand what you are saying no so


See I have again off topic but I this is a professional Im married for 10 years so if Im too angry right on my children or like on my wife and I dont want to escalate the war what I do is Ill start scolding them in Sanskrit or some other language that they dont understand so that you know my anger is vented out but they dont understand and respond back so that no escalation happens


So maybe somebody is doing that that way who knows Okay So probability density functions So now probability density functions Okay Notation wise note that for distribution functions Im using the script p right I mean two lines p So for probability density functions I use like small p So this probability density function is a function right That is equal to the derivative of the distribution function


Right evaluated at that point thats all okay Ill maybe not use A lets use some other thing here


Yeah this is the definition of the probability density function its just a derivative

speaker_2: Thats the


or maybe I am moving ahead but just for clarification for a continuous function random variables we have CDF and PDF like cumulative distribution and probability density functions correct

speaker_1: Mm mm

speaker_2: And for

speaker_1: For discrete random variables I will tell you so that will become probability mass functions Distribution functions are the same as will become probability mass functions


Okay so good that you mentioned that See mostly in this course well be dealing with continuous random variables


that you mentioned that probability mass functions so this is for this is for continuous random variable okay for discrete random variable the probability density function is nothing but the


Cost difference


Distribution function evaluate for that and distribution function evaluate for that


A plus one and A you know yeah


the density function this is for the discrete and variable okay so please note


This right is this is not a probability That is why you know if you take an example right if you take a random variable this notation is normally distributed with 0 1 okay This means that the density function of this is equal to that thing 1 by 2 by sigma squared e power minus x minus mu


whole square divided by 2 sigma squared right


there is a square root here yeah i dont remember this and i dont expect you to remember as well this is for a scalar value case for a vector value case that is 1 by 2 pi to the power of d by 2 where t is the dimensionality and you have the determinant of this matrix so e power minus x minus mu transpose so this is a vector of d dimensions sigma is a matrix d by d this is x minus mu


Uh this is what it is so now note that this entire thing is a scalar no


this is p cross 1 times p cross d times no 1 cross d so my x and mu are p cross 1 and I tell you settle this for once for all 1 cross d times d cross d times p cross 1 so this would be 1 cross d times


d cross 1 this will be 1 cross 1 because x is in R d the range space of random variable is 3 dimensional which means that mu is also in R d okay this is the probability whenever we see in most of ml right we we work with density functions not distribution functions because of ease of computation thats what i mean lot of standard metrics exist lot of standard forms exist for density functions okay what is the what is density function


Density function is nothing but the derivative of the distribution function So if you evaluate the density function at a point right what you are getting is the derivative of the distribution function at that point Thats all Please note that if you evaluate the density function at a particular point A you are not getting the probability of that point


Okay so this is one take home message Evaluating the density function at a particular point will not give you the probability of that point Okay because probability of a point does not make sense Probability remember is a measure that is defined on the elements of sample space always Okay evaluating the density function at a point will simply give you the derivative the value of the derivative of the distribution function at that point Thats all However


If you take the density function right and integrate it


a laying over a set what do you get this is equal to the distribution function evaluated at a see this is equal to the probability of that entire story


Do you understand this What Im saying is


Evaluating


the density function


a point


Is not equal to the probability is not equal to probability of anything


How about that


integrating


density function


Oh a sec


is equal to the probability So for instance right if you take the density function and integrate it between a and b what do you get You will get the distribution function evaluated at b minus the distribution function evaluated at d So this is a valid probability You know this right So always remember that evaluating the distribution function will give you a valid probability Evaluating the density function will not give you


valid probability but integrating the density function over a range will give you a valid probability because that is equal to the distribution function


Is this clear to all of you


Okay okay so now I think we have like enough background to any questions so far Now lets come back to that problem of estimating genders from an image

speaker_2: Answer one question

speaker_1: Uh before you ask the question uh I have a request uh with this background right you know please go back to that uh uh that you know that Goodfellows book on machine learning and read the chapter on distribution and and probability theory please so while you come to the next class I expect you I expect all of you to know all this because this actually kind of uh uh brings us to the end of uh the basic probability theory treatment


okay i i dont intend to teach you probability theory because i assume that you people know it but just to give this perspective i spent some time please go back and uh brush up your probability theory fundamentals before you come to the next class please do that okay questions

speaker_2: Sir so when we have the probability density function and we have px of a so there a like it does not evaluate to minus infinity comma minus a right

speaker_1: So again if you ta if you evaluate the probability density function at a point

speaker_2: So it it does not mean that it is a range from minus infinity comma a it is strictly an

speaker_1: No no no no it is simply no no it is simply means that you are taking the derivative of the distribution function and evaluating that at a thats all

speaker_2: Okay

speaker_1: evaluating the see if you suppose you plug in some value a into the Gaussian distribution and evaluate it it only means that


There is an underlying random variable okay with a distribution function and that distribution function


you take the derivative or the differential of that distribution function and evaluating that derivative at a thats all it means


But if you take the distribution function if you take this Gaussian distribution Gaussian density function okay


integrated within a range then what you are doing is evaluating the distribution function at two different points no


That is what I wrote if you take it and take the running integral of this part you get the distribution function evaluated at this point this point A


If you take the range if you take the distribution density function and integrate it between the range it is equivalent to evaluating distribution functions at those two endpoints and taking the difference which is the probability Because distribution function evaluated at point will give you a probability


So remember this book

speaker_2: And sub distribution

speaker_1: answer distribution okay let me let me tell you so suppose there is a random variable that is uniform uh ask the class ill take your question that is uniform between zero and half okay what is the density function of this


Do people know what the density function of this is Uniform random variable between 0 and A and B What is the density function of a uniform random variable between A and B

speaker_3: Zero if less than zero


And half minus zero is the left minus the left minus zero

speaker_4: One thing

speaker_3: One by V minus there

speaker_1: 1 by b minus a 1 by b minus a row it is equal to 0 right if


Excess


Yeah maybe its easier to write it that way its equal to two


X is between this right and zero otherwise


The density function of a uniform random variable looks like this no zero and half This is zero this is half the height is equal to two This is how the density function looks right All of you agree Anyone has a question on this


Now I mean if we were to say that evaluating the density function at a point will give you a probability how can that happen its contradictory no


The probability is upper bounded by one Density function evaluated at a particular point here will not give you a probability Do you see that Do you appreciate that This is an example that I have constructed to show you that evaluating the density function at a point will not give you a probability


This is clear


However if you take if you integrate this and if you take a small area


This is the probability because you know that will evaluate to something less than one between zero and one


Evaluating the density function at a point will not give you probability but integrating that will give you probabilities Is that okay Because integrating the density function is equivalent to evaluating the distribution function at a particular point


Okay uh astic

speaker_3: Yeah hi sir so uh in the above integral uh where you are integrating it from a to b

speaker_1: Stay

speaker_3: Mistake Yeah while you define the derivative there also it should be a small x right where you take the derivative

speaker_1: It depends It depends I mean if its a if its a if its a scalar valued random variable then its small x right If its a vector valued random variable what happens Its the gradient that we define Thats all right because the you understand


Okay uh so this is clear


So when does our class end it is it at 12 or at 12 15


I think so

speaker_4: Thats 1215 1215

speaker_1: Can I continue for 10 15 more minutes


Okay because now this actually is a nice time to stop Yeah no we have topic wise and say we have come to the end of this


So lets come to machine learning


And for now lets do supervised machine learning


Okay so what do we have suppose


we have


thousand images


with labels


this can be like lets say research and done labels this can be any labels or identity labels anything okay now this is what we have this we understand now everything that we do from now on has to be seen in the uh seen from the perspective of uh the distribution functions and random variables and all that what how do we see this let us let us represent this as a set d okay


I will I will come I will reduce the levels


afterwards so let this is pics one


X two


and explosive


Oh easy image lets write it down here


Each image I am the image is


is uh what do you want two thousand two hundred into three hundred dimensional


how many 60 to 4060 to all the pixels okay this means that every xi is in


Any confusion on this any question on this


Any question on this This notation is clear We have 1000 images all of them are in 60000 dimension How do we see that So now from our language each X sign is


an element


Um


a range space


of a random variable x


You understand whats happening


So what is happening is the underlying random experiment right the random trial has been conducted thousand times okay And there is an underlying random variable that has taken those outcomes and mapped it to some 60000 dimensional space using this random variable


Is this clear


This implies that there exists


And then the


Probability measure


And thus


and distribution function


Do you agree


There exists an underlying probability measure and therefore a distribution function induced by X correct


So that is represented as this right I mean you say that this is a data that is sampled from this notation mean this tilde says sampled from


Okay what do you mean by sampled from There is a there is an underlying random trial that is happening and there exists a random variable and that random variable gives rise to some induced measure These are elements from the range space of random variable That is what this notation means being sampled from sampled from a distribution This is what this is how we write


You get the notation So this is a starting point for machine learning when we have data We say that data has been sampled from


Distribution


Okay sampled from our distribution not our distribution because we have specified that sampled from


E distribution


index this is like data


data sampled from the distribution px Okay What does that mean That means that you understand the entire story right now that there exists an underlying probability measure and there was a sample space there is a random experiment happening there is a random variable that mapped that those outcomes to some real numbers which is 60000 dimensional real numbers And what we see are the elements from the range space of it And because there was a probability measure there exists a distribution function Yeah thats what we are


Thats not we we have now


Is this clear


I just wanted to give you this world view right I mean had you knew this then I would have not spent those three hours so this is the world view that I want you to have please ask me questions if if you need clarifications at this point yeah in the genes

speaker_4: Yeah just trying to get how did you get sixty thousand on R

speaker_1: See every image right you have image is a 67 dimensional vector no right I mean 200 pixels horizontally 300 pixels vertically so this is the one real number second real number third real number fourth I have just tagged them as columns and made it a long vector of 67 dimensional

speaker_4: I read that as 30 C


I didnt read 300 it was looking like 30 C yeah


Yes whatever confusing yeah its clear

speaker_1: Yeah


If its word embedding no then it is some 786 7 703 dimensional vector it doesnt matter depends on what your data is uh I mean

speaker_3: Yeah so I have a question So regarding the you said that the these x1 x2 x3 these are the these belong to the range space of the random variable function And there is a probability

speaker_1: Yeah but I I I I I like your random variable function


thats thats what it is okay yeah but nobody calls it unfortunately a random variable function but thats what it is yes move on please

speaker_3: yeah so uh so the probability distribution

speaker_1: No no no no no hold on again now what do you mean by probability distribution function of outcomes thats not a well defined term


Probability measures are defined on over outcomes


not distribution functions


Are you asking how will they will probably measure relative distribution function

speaker_3: Yeah yeah

speaker_1: That is by definition now we have defined that here


That green thing this is how they are related

speaker_3: Okay okay then uh my question is

speaker_1: This is all related no Yeah

speaker_3: Yeah then my question is that how are these two probability measures they are related I mean how are they related they are

speaker_1: There are no two probability measures there is only one probability measure there is a distribution function


Where are two probability measures here There is only one probability measure no

speaker_3: Oh

speaker_1: But thats

speaker_3: No any

speaker_1: Any questions

speaker_3: somewhere in the in the top you mentioned like you know that we have a uh outcomes and we have a set of events and we have a random variable which maps them to certain real numbers and we have a borel sigma algebra and a probability measure

speaker_1: Not probability its not probability measure it is an induced measure induced measure induced measure is called distribution function

speaker_4: Okay okay

speaker_1: The induced measure itself is called distribution function

speaker_4: Okay okay

speaker_3: So P one

speaker_1: There are no two measures there is only one measure two measures will come into picture only if you have two random variables if you have a single random variable you only have one


Measure state and one distribution function

speaker_3: So I Im not even sure whether my question is correct or not if it is wrong then please correct me then how are P1 and Px they are related


And this and this

speaker_1: This is when you have two random variables okay are you talking about multiple random variables or a single random variable

speaker_3: People are not very well so as to


single random variable or the equations which we are just clashing

speaker_1: Which ones this ones

speaker_4: The place where you have written the induced thing like the X the X over the arrow


You just run past

speaker_3: This one this one


Not exactly you just went past it okay maybe I can just uh

speaker_1: Yeah thats right

speaker_3: Yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah

speaker_1: Here here there are two writing variables

speaker_3: Yeah but on the left hand side you have written omega one f one p one and there is an arrow where x is a random variable and this


real numbers our set of real numbers v is the vector signal and px

speaker_1: is the induced measure under that random variable f it is one there is one distribution function the induced measure itself is a distribution function

speaker_3: Okay okay

speaker_1: And another random variable introduces another distribution function and there is another standard link measure

speaker_3: So people want

speaker_1: Every random variable has a measure

speaker_3: Okay okay

speaker_1: Measure P1 get induced to distribution function Px measure P2 gets induced to distribution function Py

speaker_4: Okay okay okay

speaker_1: Send okay

speaker_4: Okay yeah yeah

speaker_1: But here right when we are talking about data there is only one measure that we are talking about and there is only one distribution function


He said okay

speaker_3: Yeah so

speaker_1: Any other question on this

speaker_4: Yeah answer you are considering black and white picture because otherwise it would be

speaker_1: No way

speaker_4: Uh I recall they said

speaker_1: No every pixel is a real number no

speaker_4: So yeah you are multiplying 200 by 100 so what you are saying

speaker_1: Now what you are saying is uh what you are saying is there should be another three channel image here not 200 plus 300 plus 3

speaker_4: Yeah right

speaker_1: If its three then you multiply this with three no thats all it is like one lakh eighteen thousand dimensional thats all yeah

speaker_4: Oh oh

speaker_1: For now Im for the sake of ease no it doesnt matter I mean you should understand that the data dimension doesnt matter because it can be anything it can be a picture it can be some 30 dimensional speech vector it can be some bird embedding it doesnt matter what it is


This will be an example So in general right in general I want to generalize this idea I have to just say that all data is in some d dimensional space thats all


Right So if its an image then it has 16000 dimensional If its a bird if its bird embedding its 7000 dimensional or whatever

speaker_4: Yeah thanks

speaker_1: Okay any other questions


Okay now suppose that take another example another scenario where suppose we have images same thing we have thousand images


With labels we take MNIST itself you know sixty thousand examples with


50 000 examples MNIST has 50 training data has 50 000 examples in it


10 to 100 devices with labels these labels are


10 labels 0 to 9


0 to 9 you have 10 labels Now how does the data represented Data is represented like this Every point is a tuple like this x1 comma y1


x to the power of 2


X fifty thousand


Im buying fifteen thousand


Okay now how do we use our worldview on this Is that you say that this is sampled from an underlying joint distribution between two random variables x y Because x represents the random variable So basically we are saying there are two sample spaces right There is a


x that takes the image space and maps it to 50000 no what is the dimensionality of image well lets say that each image each image is in 784 dimensional because MNIST is a 28 by 28 image okay so now this maps it to 784 dimensions this is one random variable there is another random variable so yi is a discrete random variable that can take values it is like


Rolling a die okay now this is theres another random variable y that takes another sample space omega 2 and maps it to


discrete center and note that a random variable need not


range space of the random variable need not be continuous no it can be discrete as well now there are two random variables here and the data is now modeled as coming from the cross products of these two right i mean you take a picture and you associate your sample one one i mean you you take a random trial from this sample space you get a picture and you make a a a random trial from this and then you take a pair of them that is your data point and because


Was that exist


Probability is on the intersections and unions of these two sets you can define joint distributions on it


You get it


Now in this is this is supervised this is typically called supervised machine learning okay


You have two random variables


two sample spaces and two probability measures basically right it is called supervised machine learning because you have one random variable corresponding to data the other other random variable is typically called as the label okay now the data has been sampled from joint distribution of x and y


Is this clear


And whatever I defined here no this is unsupervised machine learning where you have one only one probability measure In supervised machine learning you will have two probability measures One is called the data the other measure for the labels


So this we will write maybe


Uh this is


is heading for unsupervised learning


This is I think


So what changes You see that we have so we are sampling from px here right Theres one quality distribution function And here we are sampling from the joint distribution of those two because there are two random variables See now we actually think about it If you think about it what was our problem Our problem was that we dont know how pixels are related to these notion of digits right So the way we model it is that okay two random experiments are happening


somebody is writing that digit on like paper and take being the picture is being taken and all that okay theres one random variable that is basically converting all that into a real number so once this is done this is being now associated with one of these nine digits emotion of digits that is another random experiment so both of them have uncertainty right now but you have joint distribution which means that now every image right has a certain uncertainty or a probability


of belonging to one of these nine classes You see that now See initially I said that this probability theory will give you a tool to handle uncertainty that incorporates uncertainty in construction itself Now you see y Okay Now we dont talk about functions from y to x See in deterministic case we were talking about functions that deterministically map elements of y to elements of x Now we are not talking about it We are talking about distributions Okay


joint distributions between these two sets which means that given every element in y or rather every element in x there is a certain probability associated with that belonging to one of these nine classes nine labels do you nine elements from other set do you see that when i will concretize these ideas in next class okay but i want you to appreciate right i mean the whole branch of this probability theory was was was conceived because you start with a random expression


right and you have this notion of probability associated with events now you deal with everything you model everything in terms of those random events and the and distribution functions right and you have that notion of uncertainty by construction


Is this clear Ill continue from this in the next class while I take questions Ill continue from this in the next class Ill concretize these ideas But yeah you should understand how to represent data Now data is represented as samples drawn from this is actually called you know samples drawn from a distribution People also call this as data sampled from a distribution or samples data drawn from an underlying distribution Okay These are common words that are used


Whenever you see that they are drawn from a distribution you will you should know the entire story Whats happening is that there is a random experiment you get sample space you get event spaces there is a random variable that is mapping this to real numbers and there is a probability measure assigned to the elements of sample space or rather elements of event space and therefore a distribution function gets induced


Right So when you say that the data is sampled from a distribution this is what it means


Uh yeah prosanna


person but one


Yes I can hear you

speaker_3: Yeah so in the last slide I think you explained about x and y random variable function So what is the relation

speaker_4: between omega 1 and omega 2 here


Theyre on it

speaker_1: Yeah there are two sets basically right I mean theres no relation per se

speaker_4: But whatever the

speaker_1: But you can you can conceive you can talk of intersections and unions between those two elements thats all


Right Those two are the two sample spaces I mean those are samples Those two are sample spaces that would that would encompass the outcomes of these two random experiments But these two random experiments are not independent right Quote unquote independent in the sense that they are connected

speaker_4: Yeah only for the images that you have taken like you will assign the number

speaker_1: A true monumental

speaker_4: So basically like

speaker_1: Remember you sample an image yeah you sample an image you sample a number and do associate them using unions and intersections


Uh yeah

speaker_3: Sir do we know this PX or PXY in this case No

speaker_1: No we dont Thats the whole problem in machine learning The machine learning is if I have to summarize machine learning in one sentence it is this given the estimate px thats all That is machine learning ChatGPT is that only

speaker_3: But be honest

speaker_1: We will use multiple techniques to estimate p x given d yes

speaker_3: This is a good time to start this game


EX or PXY

speaker_1: It depends no in in unsupervised learning you could estimate p x y p x in supervised machine learning you estimate p x in fact in supervised machine learning you estimate p y given x Ill tell you next time you estimate the conditional distribution

speaker_3: Given given X

speaker_1: Ill tell you in the next class that gender given image

speaker_3: And okay because


Okay because these are sampled from those distributions we say that uh these they are kind of representative of the


Uh the the actual distribution

speaker_1: So they are actually sampled from the underlying distribution no they are they are completely sampled from the underlying distribution okay

speaker_3: Okay okay

speaker_1: Ah but the problem is the one big problem with the statistics is right if when you are given samples from a distribution how do you estimate the underlying distribution is the biggest problem in statistics Giving samples from a distribution is not enough to estimate the com estimate completely the underlying distribution


That is why no it is machine learning is heavily depend on the number of data points The more the number of data points that we have from the distribution the better our estimation will be We will see all that in the next class That is what I will do in the next class


Okay thats because

speaker_3: Thats because of either noise or maybe some something that we have not observed

speaker_1: something that we have not observed no no no no i dont call it noise or anything okay theres something called last last numbers i will describe all that in the next class

speaker_3: Okay yeah I think its a

speaker_1: Yeah so basically from take home takeaway from this class is that when you have data you should start representing data right as


uh samples from the in space of uh elements from the in space of the random variable and when you when we say that there is a distribution associated with it you should know that it is the induced probability measure that is coming from coming through the random variable that is the biggest take home


Is that clear


Okay lets stop here but you know I have a a couple of questions for you people lets maybe stop the recording


Yeah people can leave any element in Y or rather every element in X There is a certain probability associated with that belonging to one of these nine classes Nine labels Do you nine elements from other set Do you see that I mean I will concretize these ideas in next class Okay But I want you to appreciate right I mean the whole branch of this probability theory was was was conceived because you start with a random experiment right And you have this notion of probability


associated with events now you deal with everything you model everything in terms of those random events and the and distribution functions right and you have that notion of uncertainty by construction


Is this clear Ill continue from this in the next class while I take questions Ill continue from this in the next class Ill concretize these ideas But yeah you should understand how to represent data Now data is represented as samples drawn from this is actually called you know samples drawn from a distribution People also call this as data sampled from a distribution or samples data drawn from an underlying distribution Okay These are common words that are used


Whenever you see that they are drawn from a distribution you will you should know the entire story Whats happening is that there is a random experiment you get sample space you get event spaces there is a random variable that is mapping this to real numbers and there is a probability measure assigned to the elements of sample space or rather elements of event space and therefore a distribution function gets induced


Right So when you say that the data is sampled from a distribution this is what it means


Uh yeah Prasanna


person but one

speaker_4: Can you hear me sir

speaker_1: Yes I can hear you

speaker_4: Yeah so in the last slide I think you explained about x and y random variable function So what is the relation between omega 1 and omega 2 here


So dont mess with it

speaker_1: Yeah there are two sets basically right I mean theres no relation per se

speaker_4: But whatever the

speaker_1: You can you can conceive you can talk of intersections and unions between those two elements thats all


Those two are the two sample spaces I mean those two are samples those two are sample spaces that would that would encompass the outcomes of these two random experiments But these two random experiments are not independent right Quote unquote independent in the sense that they are connected

speaker_4: Yeah images that you have taken like you will assign the number

speaker_1: Thats true

speaker_4: So basically like

speaker_1: So you sample an image yeah you sample an image you sample a number as to associate them using unions and intersections


Uh yeah

speaker_3: Sir do we know this PX or PXY in this case

speaker_1: No we dont Thats the whole problem in machine learning The machine learning is if I have to summarize machine learning in one sentence it is this given D estimate P X Thats all That is machine learning Chat GPT is that only

speaker_3: To be honest

speaker_1: We will see what the depth needs to estimate PF given D yes

speaker_3: It was a good time to speak


EX or PXY

speaker_1: Depends no in unsupervised learning you estimate Pxy Px In supervised machine learning you estimate Px In fact in supervised machine learning you estimate Py given X Ill tell you next time you estimate the conditional distribution

speaker_3: Hey Mike

speaker_1: Give me a minute

speaker_3: Given X given Y okay

speaker_1: Ill tell you in the next class that gender given image

speaker_3: And uh okay because


Okay because these are sampled from those distributions we say that uh these they are kind of representative of the


Uh the the actual distribution

speaker_1: So they are actually separate from the underlying distribution no they are they are completely separate from the underlying distribution okay

speaker_3: Okay okay

speaker_1: Ah but the problem is the one big problem with the statistics is right if when you are given samples from a distribution how do you estimate the underlying distribution is the biggest problem in statistics Giving samples from a distribution is not enough to estimate the com estimate completely the underlying distribution


That is why you know it is machine learning is heavily depend on the number of data points The more the number of data points that we have from the distribution the better our estimation will be We will see all that in the next class That is what I will do in the next class


Okay thats because

speaker_3: Okay thats because of either noise or maybe some something that we have not observed

speaker_1: something that we have not observed no no no no dont call it noise or anything okay theres something called last last numbers i will describe all that in the next class

speaker_3: Okay yeah I think its a

speaker_1: yeah so basically the take out take away from this class is that when you have data you should start representing data right as as uh samples from the range space of uh elements from the range space of the random variable and when you when we say that there is a distribution associated with it you should know that it is the induced probability measure that is coming from coming through the random variable that is the biggest take home


Is that clear


Okay lets stop here but you know I have a a couple of questions for you people let us maybe stop the recording


Yeah people can leave right
