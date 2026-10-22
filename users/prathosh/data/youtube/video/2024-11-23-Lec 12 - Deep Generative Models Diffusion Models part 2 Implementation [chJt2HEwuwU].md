---
id: chJt2HEwuwU
title: Lec 12 - Deep Generative Models Diffusion Models part 2 Implementation
url: https://www.youtube.com/watch?v=chJt2HEwuwU
date: '2024-11-23'
duration: 02:40:23
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: xt is given by root of alpha t xt minus 1 plus 1 minus alpha t times epsilon where epsilon is a sample drawn from normal 0 1 and this defines a first order Markov chain is what we saw so starting from a data point you keep projecting it onto the latent space according to this equation this particular equation


this particular equation and that will quote unquote add noise right that is adding noise and slowly because its a Markov chain stationary distribution will go to


Not Mozill and his work we saw


Now um this encoding uh in processor distribution


on the tth latent space conditioned on t minus first latent space which happens to be a Gaussian with certain parameters mean and variance that is written here and the corresponding decoded distribution is what we call as the model distribution it is learnable

speaker_2: Uh

speaker_1: What you learn is that you learn the decoding distribution the mean and the variance of the decoding distribution at all times thats t Now as we saw later in the lecture that the variance is actually often not learned that is also assumed to be fixed or known What is learned is the mean of the decoding distribution Now how do we do that We do that using the usual elbow optimization So for that we started from the log likelihood


the elbow and yeah they did some algebraic manipulations right


And finally uh what we got was that there was three terms in the elbow one we call it as the reconstructed term where you take the uh


first latent variable and try to reconstruct the data and the second term is prior matching term okay which was independent of model parameters theta okay and the third term is what we call as the


Consistency term or denoting matching term okay that is what we call it as the consistency term


that involved a KL divergence computing KL divergence between two distributions one was this Q XT minus one given XT and X part and the model D or D decoding term P theta XT minus one given XT so note that in the denoising matching term or consistency term right there are two distributions one is the decoding distribution the other is is a sort of reverse of the encoding distribution reverse in the sense that it is


its going in the backward direction of xt minus 1 given xt and x0 but yeah so that is known okay but has to be computed it is not trivially known we have to compute that distribution so what we did was we wanted to compute that consistency terms for that we need to compute the known reverse distribution that appears in the consistency term


and we use Bayes law right and the fact that all of the involved distributions are Gaussian distributions completed square and finally we yeah so two things one in the while we are computing the


known term okay known denoising term in the consistency loss component we encounter terms like q of xt given x naught right where uh where xt is the dth latent vector and x naught is the data so now we use recursion to find this q of xt given x naught right uh using this argument and finally q of xt uh given


x0 still happen to be a Gaussian with parameters denoted by alpha bar x0 and yeah parameterized by alpha bar x0 where alpha bar is the one that is defined here which is a product of multiple on all the alphas till the time t


So using that and the fact that all of them that are involved are Gaussian distributions completed the square and finally found out what this the known denoting matching term was right and we called we called that as a Gaussian distribution We found out that it was a Gaussian distribution 2 with a mean denoted by this mu cube and the variance denoted by sigma cube ok and


Sigma Q was simply a function of


t okay that had nothing to do with any parameters it was a function of t and we wrote that as small sigma q square t times identity and mu q uh was a function of uh x t and x naught okay which can be uh computed which which is known and can be computed okay now having


PK top


We have to we can now finally compute the um the learning learning term or consistency term which is a k divergence between two power field distributions okay


Now the KL divergence between two Gaussian distributions as a deterministic form we use that deterministic form which is KL divergence between two Gaussian distributions and finally found out that the D Noggin matching term will involve difference computing difference between two means one which is the mean of the


backward of the decoding distribution mu theta at xt and the other term was the mean of this known denoising term okay mu q computed at xt


Thats what we saw any questions on the so far


No hope Im audible

speaker_2: Yes

speaker_1: Okay so then what we did was while we can actually stop here okay and we can implement DDPM this way as I said you know in the literature people dont use this formulation to implement but they rather reparameterize this particular thing using


In terms of the epsilon of the noise that is added that is what is implemented So we saw that three parameterization as well So maybe I will do it again


it in the last class now let me do it again so well assume that we know that the elbow now has a difference between the means of mu q means means mu q and mu theta okay let us take it from there and do it


Oh

speaker_2: So are you waiting


So we have


It was a kill dev

speaker_1: Thank you


xt minus one given

speaker_2: 60 and 6 not


one distribution the other distribution was

speaker_1: Other distribution

speaker_2: Eat here


Its t minus one t one x t


This was what it was and we show that


Thats a cute one


State minus one we one


X two and its not


Gaussian distribution


mean we call this mu q


And the variance was sigma cubed


and mu q


was a function of xt and x0 so given an xt and x0 you had this mean to be equal to


Lotta


alpha t into 1 minus alpha t bar times xt


alpha t minus one bar


to one minus


will part t into x


rewritten by


One minus


for T bar see note that

speaker_1: The denominator is actually a constant its a scaling factor So basically its a linear

speaker_2: combination of XT and X naught that is what this new Q is right

speaker_1: So Ill

speaker_2: Now if you recall using a recursion we showed that the th latent variable x t okay can be represented in terms of


alpha t bar okay


presented in terms of x naught right alpha t bar into


Its not


root of 1 minus alpha t bar into epsilon


Do you remember this So we used recursion and showed that Xt can be showed in terms of X0 and the noise added epsilon correct


Put this in place


that now mu q

speaker_3: No its not stuck

speaker_1: Its lagging I guess

speaker_2: Hold on see let me do one thing let me just use my phone internet to connect huh that should be better give me a second


Do you see the screen now

speaker_1: Oh whats happening


Just change my internet to my phone internet

speaker_2: Yeah please tell me if you can see the screen


There we go


visible

speaker_4: Yes

speaker_2: Only it works


Yeah sorry about this as I said Ive come to my hometown and


Internet is not my standard one

speaker_4: Some issues oh so uh


what they were doing is that expressing this mu q okay in terms of


Its not an

speaker_2: This mu q now can be expressed in terms of x0 and epsilon So this is the recursion that we wrote Sorry xt is expressed in terms of x0 and epsilon Which means that I can write

speaker_4: root of alpha r t minus


into 1 minus alpha t

speaker_2: Okay now this implies that here I can write x naught


in terms of x t and epsilon right x t minus root of 1 minus alpha t bar times epsilon divided by alpha t root of alpha t bar right so which means that this x naught which is there in u q I can replace that with


thing now xt minus root of 1 minus alpha t bar into epsilon divided by root of alpha t bar right this entire thing divided by


1 minus alpha t bar


Right so I can I mean what did I just do Xt can be reparameterized in terms of X naught and epsilon which means that X naught can be written in terms of Xt and epsilon So mu Q now the X naught in mu Q now can be written in terms of Xt That is what was done So I will skip the algebra If you rearrange the terms and group them and modify what will happen is finally the mu Q


can be expressed


One way


to alpha t


into xt minus 1 minus alpha t divided by root of 1 minus alpha t bar


into root of times


Yeah so this is simply by rearranging the terms above


That should be okay right I mean what we did was we uh


mu q was written in terms of


X t and epsilon Thats all right


Now recall that


p theta of xt minus one


P1 XT the one that we had


What was that we assumed it to be a Gaussian


a mean mu theta and variance was exactly equal to sigma q right we didnt want to change the variance the mean was mu theta


Right now this mu theta now


can be expressed as follows


minus divided by 1 minus


40 bar


into some epsilon theta


Okay so now this is something which is subtle If you understand this then we are done Okay so what did we do We express the mean okay of the decoding distribution


In terms of XT and some epsilon theta cap okay that is to be learned Well say that is epsilon theta cap


Not clear


So what did we do here We note that

speaker_1: Uh

speaker_2: Any Gaussian distribution right can be expressed in terms of any other Gaussian distribution just by scaling and shifting correct Do you do you agree with me on that


So that is reparameterization right So you if you are given a particular Gaussian distribution you can always scale and a sample from a particular Gaussian distribution you can always scale and shift the sample of that particular Gaussian distribution to make it into any other Gaussian distribution Do you agree


Hello am I audible

speaker_3: Yes yes so its audible yes yeah

speaker_2: So you agree with what the statement that I made right can be expressed in terms of any other Gaussian distribution

speaker_3: Yeah

speaker_2: Now this p theta of x3 minus 1 given xt is a Gaussian distribution with a certain mean mu theta Okay So what we did was we just represented that mean in terms of xt right which is a constant right and some sample from a Gaussian distribution epsilon theta cap with some scales and shifts


I can always find an epsilon theta


Mm


Which when scaled by this particular scaling factor and shifted by 1 by 1 by root of alpha t times x t will give back my mu theta Do you agree So what Im trying to say is if you scale and shift a particular Gaussian distribution right you can always learn the scale and shift factor so that you can get back to the original Gaussian distribution Is that is that all right


So why I mean then the next question is why did we even have to like introduce these random scale shapes This is just to make the loss function look nice Thats all Okay so there is in fact you know I can just write this as mu theta and mu q minus mu theta can be written as this this entire mu q that we have minus mu theta right It doesnt matter but people generally write it this way to ensure that the final loss function that you see has a nicer form to see


thats all there is no other sanctity to this and what i am simply doing is


I mean deliberating all the learnable things on a scale and shift into this epsilon theta Thats all Okay So with this what will happen is the loss that we had no the KL divergence between


2 of xt minus 1


You can XT and X not


Too dark


X t minus one will give an X t e


simply became let me just write proportional to because generally the constants are ignored they became proportional to this was initially uh we had a sum here from t equal to 2 to capital T


mu q which was a function of xt and x not and there was mu theta


which is a function of


60 and a T


p because there is an alpha t there okay this is what the last term was and this we saw was now equivalent to


All terms being equal lets call this as epsilon t Okay I think this is better to write this as epsilon t because the tth sample right I mean tth noise sample that was drawn to make x naught xt


Easier to understand okay This is around T and you have


Epsilon chi dot


just to make it look this elegant no this mu q im sorry mu theta was reparameterized in terms of xt and those constants finally this is what

speaker_1: Its done

speaker_2: this all right so when you are implementing a diffusion model right a DDPM all you have to do is implement this loss function so this becomes a regression problem right so this is a regression over epsilon t let me explain that more


Decrision over epsilon t


Any questions so far How did we get there Get here before I move to the implementation nuances


So am I audible any questions here


Are you there We are here with you

speaker_3: Yes sir we if youre audible yes we are hearing this

speaker_2: Oh no questions Okay Right Okay So this is what it becomes So now the next thing is how do we implement this in practice


Implementation


So its basically training of the DPM


So now what are we given So given I will show it for one data sample No you have to do it again in batch Given its not this is a sample from the data distribution


True theta distribution


What is to be done is that


So first what youll do is


ample


T okay uniformly between 2 and capital T so what is done in practice is the sum that you see here no from T equal to 2 to capital T people dont do it on like all Ts and take a sum of it they do a uniform sampling of some some subset of T between 2 and T and then do it okay so typically its not they dont take all Ts because of computational


complexity some t is taken okay sample t uniformly between 2 and capital T okay and you obtain


X T okay


And if you also have the alpha one


set alpha 1 alpha 2 up to alpha capital T okay so you fix this so typically it is fixed at


The schedule that


0 point 98 and so on 0 point 9 okay uh this is again this is an example but yeah so you could set alphas this way and you obtain xt uh using this equation right square root of alpha t bar times x naught plus 1 minus alpha t bar into some epsilon t where epsilon t is a sample from normal zero


with me so far so given an x naught so you have x naught is lets say that x naught is a particular image you take an x naught and you sample uh sorry you get some t okay lets say that we are doing it for one particular t okay uh you take a t


a bad code okay so you sample a t uh from uh 2 to capital t and you set alpha 1 to alpha uh capital t to be some constant okay and you obtain xt uh using this equation where epsilon t is some sample from normal zero is this all right so far


Okay so once you have this what you do is the following that you build construct


Structure neural network


parameterized by theta okay so this neural network typically will have this architecture which is called the


Okay so now it is called unit because note that finally what we need is a regression over epsilon theta


Right because our last function is this right We want an estimate of epsilon t Now we know that the dimensionality


The dimensionality of epsilon t is actually d which is the data dimensionality


Now when you have regression tasks okay where the output is same as that of the input and especially when you are using image kind of data the standard architecture that is used is this sort of an architecture which is called unit The name unit is given to this is because it looks like a U right U I


You start from the dimensions okay keep reducing the dimensions


then you come to some bottom like d dash and then you increase the dimensions and finally you get back to the d dimensions you know thats why the name unit okay so now what does this take as an input so you please note here that the mu theta that we had in fact this epsilon


theta cap now will also become a function of xt right and t obviously right because that is the scale and shift and uh thats what it a function of mu theta was a function of xt and t and when I just reparameterize that in terms of some epsilon theta cap that also becomes a function of xt and t right so now this unit will take xt which we have obtained and t as an input okay and it is supposed to


output epsilon theta cat which is an estimate of epsilon t that we have used to get xt What is the last function The last function is simply the difference between note that both of them are vectors of size


We can easily compute this


Thats all So this is the loss function You need to compute the gradient of this with respect to theta and then back up of it So this is all it is right I mean you do it for multiple ts


In fact I mean ideally you should do it for t equal to 2 to capital T Typically what is done is I mean t is fixed to some thousand right Thousand or two thousand is what is done So instead of taking thousand XTs people typically take some 50 XTs for a given X naught okay And then try it And again well you take another sample X naught input sample X naught and you sample some other subset of T and do this


Now how do you give T as an input to this unit is something that Ill talk about in a while But yeah so other than that is the training procedure for DDPM clear See one other thing that is to be noted is unlike in VAEs and GANs right where


The final inference happens to be just a forward pass through the network that you have trained here


The inference is not through this network We will see that in a while What Im saying is this network will not give you a new sample from the data distribution Do you see that


Unlike in a GAN and a VAE where you just take a Z right and pass it through the decoder or the generator you get a sample from the input distribution right and you sample from the input distribution that does not happen in IDDPM So I will also talk about how to do inference in IDDPM in a while but is the training procedure clear This is what you are supposed to implement in your assignment so let me know if this makes sense otherwise I can explain more

speaker_4: Sir when we are taking a x naught sorry I have a question so can I


Can I go ahead with the question

speaker_1: Yeah

speaker_4: So when we take a X naught the T for every X naught the T has to be a fixed length like the sample that we are taking

speaker_2: what do you mean by that see uh you take one x naught right one extra suppose you are doing this on some data set right some image data set x naught is one sample from the data set one image


You take one image for that one image you get all the noisy versions latent versions x1 x2 x3 x4 and so on


For each of them you do one one training through this unit

speaker_4: Is it one or more than one for for a given data point

speaker_2: See for a given data point x naught you get uh one uh sorry for one xp you do one forward pass one backward pass

speaker_3: Okay and t is we take multiple for a given x model

speaker_2: Now because the last function has the sum across all ts no

speaker_3: But here we we dont take all these but we take some samples from two to t

speaker_2: practice yeah in practice capital D is see capital D is fixed at thousand okay but while training you do a random sampling uniform sampling between two and thousand and do it that is how it is done this is for one X naught and you need to do it for all data sets all data points now that will that will be one epoch so typically what is done is you do it on batches you take a batch of X naught


Great and for


Excuse me so take a batch of X naught and for each of the samples in X naught you do a sampling of certain ts okay and find those X ts and do a forward pass and a backward pass for this entire batch and you do another batch of samples you take another batch of samples from the data set and iterating over the entire data set will give you one epoch and you do multiple epochs of training usually training


Yeah

speaker_3: And epsilon epsilon t is just a sample from a normal zero I

speaker_2: Yes epsilon t is always a sample from normal 0 Thats all So for you when you obtain xp you take one sample from normal 0 In the last class we saw that no it is simply one sample from normal 0 1 But the the the information about t is encoded in this alpha bar because alpha bar is product of all alphas from 1 to t isnt it You have to actually there is one other step here You have to compute alpha bar t right


the product of equal to one two three alpha i this is how we define alpha bar no for every t you have to define alpha bar this way and get an xt then pass it through the unit predict whatever is coming compute the loss back propagate


Any other questions on training


As I said this is what you are supposed to implement right so


Okay if its clear then there is one other question that is to be answered is

speaker_1: How do we uh give this time d right as an input to the unit


Yeah lets go home to


Now which is a scalar right


An input


neural network okay


Now what can be done is note that T E right is is one dimensional it is scalar right


one dimensional scalar so typically what happens is if you create an image at p and concatenate the speed which is a scalar


a one dimensional scalar with this p what happens is the neural network will offer none of the p because its a unidimensional scalar it will be simply ignored so for that what is done is one dimensional and


He usually ignores


If concatenated or when concatenated with a very high dimensional vector


Okay Ill connect it with a


Im not sure


So in this case this is XTE which is an image right


Some uh some data Okay so now for that what is done is


Why


able scenario


for the scaler


is converted into a vector


Okay P is converted into a vector and then concatenated


Okay theres a name for this do you know what this is called


Positional embedding


This positional embedding its a high sounding name Its nothing but converting this p which is a scalar right into some vector okay so what is done is p is converted into some p cap where


T is a scalar okay Now T cap is in some D dimension So that is what the idea of positional embedding is right P is a function that would take P and project it onto T cap So how is it done There are multiple ways One usual way that is used both in the transformers and

speaker_2: diffusion models is what is called as the sinusoidal embedding


I will just give you the idea of this you can go and look at the details on this is like lot of blocks etc its not not at all difficult what is done is construct sinusoids okay of multiple frequencies


Oh the entire thing okay


The next one is thats a higher frequency


And so on okay


Okay now this how many sinusoids are there There are


d number of sinusoids construct d number of sinusoids and what youll do is that at every t so this is the time axis


time axis so at every t so it is just t equal to 1 t equal to 2 t equal to 3 and t equal to capital T at every t you just sample the value of this sinusoid at this particular value that is all it is


This is a t equal to one let t equal to two let t equal to three and so on


Do you see what is happening now this p cap


Okay at a particular t so p cap at a particular t okay is a vector of dimensions d okay where every component is sine of some fixed frequency So you have a fixed frequency thats a function of t okay Let me just call this as two


pi times B


D is fixed no so let me call it as some


ie


divided by D


Oh


And then you have uh


The second component is cyn


2 pi times 2 divided by t you have like sine 2 pi


Uh one two three


T by D


Right So this is at okay there should be a dependence on D also here Yeah dependence on T okay


This is a tab particular d I can put a d here also yeah


this all right I mean do you get the idea whats happening so what is happening is for a given T okay so basically you want to convert a scalar into a vector like how do you do that is that you just take construct like these sinusoids if you want to convert that into a d dimensional space you construct these sinusoids okay of different frequencies and at every T you take a snapshot of all these sinusoids so youll get


a d dimensional vector at every t so now you converted a scalar t into a vector a t dimensional vector at all ts


Is this alright

speaker_3: So the sequences have to be

speaker_1: If you want to

speaker_2: Come again

speaker_3: The frequencies have to be harmonics or it can be any frequency

speaker_2: Yeah yeah generally they are taken to be harmonics In fact I think I mean thats why you know I dont remember the exact details I think in the typical sinusoidal embeddings what is done is for even ts I think they take a sinusoid and for odd ts they take cosines I suppose just to intersperse There is a sine and a cosine and you convert it into a data dimensional vector


You can go and look at the exact equations that are used no But this is the fundamental idea of what sinusoidal potential embedding does This is OK Any questions

speaker_3: So that we are defining that vector

speaker_4: Right it means like comma in between each sign just to

speaker_1: Uh sorry I missed it what did you say

speaker_4: Sir we are defining T cap as a vector right So its a sine 2 pi T by T comma I mean like those are terms of that vector right

speaker_1: Yeah yeah

speaker_4: Yeah yeah

speaker_1: These are different terms Yeah its a vector I just said space These are different


vector yeah see look at this one this t cap is in d dimensions right i mean t is a scalar t cap is in d dimensions


So in a transformer also right all these GPT etc kind of models when the tokens are given as input these things are also concatenated because a naive transformer does not have the idea of time right so to ensure that the sequential nature of that is preserved this is also given as an additional input same thing is done in this this thing also right when you implement I mean there are standard implementations of sinusoidal positional embeddings in PyTorch you just take that and


concatenate that in fact there is one other thing that is done these are additional improvisations over the architecture that depends on oh my god what happened


It comes to big things


So some of the improvisations are done over this where what is done with right Instead of concatenating this T here there are this unit typically will have this thing called skipped connections okay


what is done is uh there are connections of this sort where you take the the uh


intermediate hidden layer and connect it to the corresponding layer at the reflection I mean it actually looks like a reflection right along this So so you connect the corresponding dimensions using a script connection just as you do in do with ResNet Okay Now what is done is that at every of these different dimensions


P is concatenated P the vector P is concatenated all of these


So this is how I think in one of the improvised architectures this is how this unit is implemented


in your assignment uh you dont have to do this all you can do is just take a t okay uh take the corresponding uh sinusoidal embedding concatenate that with xt and just appropriately give it as an input but if you can right this would be a better way to do it when you have skip connections in fact doing skip connections in pytorch is is not difficult uh you can ask tes to help you out with that and with every skip connection that you do right from uh


to a pair of layers you concatenate T with that that is how it is typically done


Any questions on this

speaker_3: Is that a one

speaker_4: uh yes ill go ahead so when you concatenate t to the other layer so the dimension is uh less than d or uh how do you

speaker_1: It is less than d you have to appropriately take care of the dimensions

speaker_4: Okay so so the Ts will be generated differently for each uh at each layer or so

speaker_1: No no no you take the same T but the dimensionality have to be appropriately taken care of thats all


Thats okay no

speaker_4: So we just

speaker_1: We just have to reshape each layer


You have to appropriately reshape at every layer

speaker_3: I had the similar question so because uh unit the input layer would be some convolution layers right

speaker_1: Oh

speaker_3: How do we append the key to the data where because thats not really part of the image right

speaker_1: Thats not part of image that is why what is done is XT is not concatenated at the input layer So what is done is after the first convolutional layer okay you take the output of the first convolutional layer concatenate T okay appropriately reshape and then use the next layer That is how it is done


Okay

speaker_3: And any particular reason why we are using unit here I mean why do we have to create this bottleneck

speaker_1: otherwise no uh like xt and epsilon theta have the same dimensions right what sort of neural network do you use

speaker_3: So so at at uh at the bottom it has to be um

speaker_1: at the bottom it has to be coming x you have to do it like this right now what will happen is x t has the same dimensions and you can you have to maintain the exact same dimension here and then get the epsilon theta right see that would the you will run into the problem of uh not learning it well because you might get into identity


Then you have to reduce the dimension start from xt and reduce the dimension If you reduce the dimension you will not get epsilon theta Youll have to get to epsilon theta Then you have to again increase the dimension right


So that will make the architecture a naturally unit kind of architecture


Any other questions See I today I dont as I said no I dont have my multiple screens So uh you mean you I dont I cant call call out name So please unmute yourself and ask questions Huh Ill just answer them

speaker_3: So just to correlate in conditional can we use like one hot vector that embedding so is that very similar to this one

speaker_1: Yeah but see Ive still not talked about conditional generation I will talk about conditional generation in a while it is done very differently in a diffusion model

speaker_3: I know Im talking about glands


Against in gain conditional gains

speaker_1: Understand but see dont confuse this uh this concatenating this P with uh I mean as concatenating a class information that is not what it is We are still doing unconditional generation Okay Okay We will do conditional generation in a while I will talk about that Uh like we will discuss that in a while But yeah so it is similar in spirit to concatenating that one hot vector but please be uh like uh aware of the fact that this P is not


T is not having any class information here okay it is having the time information because there is a temporal evaluation of the encoding process here right this T is having that time information it does not have any class information

speaker_3: So one more point so with this time information what we are I mean what we want the model to learn is at any given time step how to do the denoising is that understanding correct

speaker_1: So yeah of course see this look at it no what this unit is actually doing is given a noisy input okay at time t it is trying to tell you what was the amount of noise that was added to make x naught noisy


So epsilon theta is an estimate of that no the amount of noise because that is what you are regressing over


Any other questions So now I think you can implement it right


Yeah Okay So let us move on quickly then So this is about training Let me talk about inference in DDPM Suppose you have after you have trained this how do you generate images Okay Let us look at that


we will talk about conditional generation and then well go to DDIMs Okay so this is inference with DDPMs


Okay so what are we given so we are given


So this is what we should do We have a trine network epsilon theta I mean say theta star okay that would take xt and give you epsilon theta So now what we need to do is we need to sample from xt p theta of xt minus 1 given xt okay So let us do that We have to do it iteratively now


This is where one uh


One of the drawbacks of DDPM comes you know the sampling is very very slow because we have to start from t equal to capital T and go all the way till


Uh t equal to one let me write that


thats it so its its pretty simple see what is happening is the following right what do we need to do is we need to sample from this distribution p theta of x t minus 1 given x t right so what is p theta of x t minus 1 given x t its a normal distribution with mean equal to mu theta and variance equal to sigma t right so what is what is mu theta mu theta is simply this x t divided by root of alpha t minus 1 minus alpha t this thing into epsilon


theta okay is that okay so now how do we get a sample from a Gaussian distribution with a particular mean and variance we know reparameterization sample from a zero mean unit variance Gaussian right and


shift it right with whatever mean you want and scale it with whatever variance you want that is exactly what we are doing here


So sample from a zero mean unit variance covariance okay and this is the shift that you do to get that mu theta so this entire thing


entire thing right is mu theta thats all just shift it with mu theta and this is again you have the sigma q right which is the variance that we are using and you get xt minus 1 and where are we using the unit here so the trend unit


So this will take xt at every time okay And this will give you epsilon theta star which is used for sampling You start from x capital T past this you get x capital T minus one


So then you take x capital T minus one pass through this network get an epsilon theta star at that T right And then keep doing it till you get x naught This will give you a generated sample


Is this all right This is how you do sampling See as I said unlike in a GAN right or a VAE where doing one forward pass through the network that is trained will give you a sample which is needed this is not the case So here to generate one data sample okay you need to do capital T number of forward passes That makes this DDPM very slow


very slow if you have seen these things like you know stable diffusion and all that right when you give a prompt you will have to wait for a while you generate the sample that is because it is doing these t number of forward passes through this network


Any questions on this


In maybe


for this let me know if you have any questions on this

speaker_3: So I have one question regarding the training of the network itself in the first place So I mean what kind of issues can we anticipate while training Just some practical

speaker_1: ddbm training is not that hard uh i mean that is why these are state of the art generative models right visual visual models these days because they are pretty stable okay uh one thing that can happen is that if you dont sample your t properly then the underlying distribution might not be learned but if you do a good enough sampling ive seen that in our experience these networks actually work pretty well


Unlike in a GAN right where you have this saddle point problem and you have the mode collapse etc Those sorts of issues do not generally arise with DDPMs

speaker_3: Okay and after how many epochs we can expect uh to get a

speaker_1: Generation

speaker_3: One generation quality

speaker_1: That depends on data sets


So you can track the loss right I mean this is a regression loss So whenever the loss is converging and reducing that is the point where you can perhaps stop


Depends on the data set it completely depends on the data set and the architecture how deep your architecture is and theres no answer for that


Okay so any questions on inference generation


No questions


Shall we move on then


Am I audible Did I


up down or something hello

speaker_4: Yes we can

speaker_1: Let me hope


So next what we will do is um


Well look at how to do conditional generation okay uh guided diffusion

speaker_4: So before that sir can you give an example where this unconditional DDPM is used

speaker_1: Well if you want to build a generative model right where you dont condition it on a particular text or like any prompt or anything you can use I mean you can take any data set and


generate I mean I didnt get you a question are you asking me for a

speaker_4: Uh yeah specifically like uh if we give a prompt uh and say like create this uh using a diffusion model that that is a conditional uh diffusion right


And if its random then its unconditional Is that correct

speaker_1: uh see dont call it as random okay i mean theres nothing random about it i mean the point is if youre sampling from some distribution px then it is unconditional generation if youre sampling from px given y where y is another random variable then it becomes conditional generation

speaker_4: About it yeah

speaker_1: Yeah so uh


Just thinking if I have to like


that now or just take a break and do it what do you want should we do you need a break or should we complete does it will take me about 20 minutes to complete the guided diffusion shall i complete that and then take a break


Can lets finish this huh


Okay see


While the diffusion models were being developed there was another parallel formulation right for the generative models that came out that was that those were called


Score based models okay


So there are multiple variants of score based models but all of them converge to DDPM So let Ill not describe more I mean score based models in detail because they are not a different class of generative models They are also diffusion models But yeah so let me talk about quickly mention score based formulation We need this for guided diffusion meaning conditional diffusion Thats why Im doing this score based reformulation


Okay now um


There is a statistical result okay


That would say that


Called okay let me write that now There is something called result


not prove this ill just state it this is also called the 3ds formula


It would say that this is a very well known classical historical result that would say that if Z is a Gaussian


And a variable


Its mean mu c and variance sigma c okay


in sigma z then the


Expectation of


mu z given z okay expectation of the mean given z is given by z plus


SIGMA Z times


Gradient of


Log off


E z with respect to z okay so please take this uh a defaced value right this is something that can be proved assume that this is true okay this is called the tweedy formula


Okay so now here the


variant of the log likelihood of a particular distribution with respect to the random variable of interest is defined as core


Theres this called function


Okay this is a known result Okay so now we lets use this result So what do we do is we have in the context of DDPM


context of DDPM we had this queue of


60 given x naught remember this right using the recursion we showed that this was a Gaussian okay with mean being equal to root of alpha t bar into x naught the variance was 1 minus alpha t bar times i


the quality and distribution suppose i apply this 3d formula to this okay what i can write is that i can write the expectation of


mu xt okay which is the expectation of this distribution given xt is written as xt


1 minus alpha RT


Fines


X P


Lagga


p x t because it is simply applying the 3ds formula as above right i mean sigma the variance of this is 1 minus alpha t bar into i therefore uh the identity matrix may go away this will simply be this particular thing okay so what is the mean of this distribution we know that the mean of this distribution is the root of


alpha t bar into x naught is equal to xt plus 1 minus alpha t bar times


the square function


your mixed D


Okay so now rearranging the terms this implies my x naught can be reparameterized in terms of


XT


plus one minus alpha t bar


into the square function


Divided by


So put up alpha T bar


Okay now why is this of any consequence is because we also know that this X naught


uh was reparameterized in terms of


1 minus alpha t bar into epsilon right if you remember this


Okay this is what it was We showed this So we if we compare the terms okay we see that the score of


log of p of x t is simply equal to some scaled version of


minus alpha t bar times epsilon okay this is the result that we need okay which is


the ground truth I mean the noise that we are adding to xt okay is actually the score which is the derivative of log of p of xt with respect to xt with a scale


Is this all right This implies that this implies that the last function that we had which was epsilon minus epsilon theta cap


is equivalent to


Regressing over the score of the model


particular t so this is the result right i mean that thats why the name ddpms are also called score based model so basically what is being done is core matching isnt it so the true score the true score is the noise and whatever the model is giving can be looked into as uh uh the estimated score to using the neural network and that is what we are matching is that all right see actually we dont need this result what we need


is that a simple thing that why when we are constructing DDPMs we are implicitly okay matching these scores


of the I mean the true score and the estimated score is that is that all right


And this is the result that we actually need right which is the


Original noise that we add to make X naught XT okay is actually a scaled version of what is called as the score function Is this is all right So we will use this result to to build a conditional diffusion model


Any questions so far


We dont we all we did was you know we just introduced a concept called score which is the derivative of the log likelihood of a random variable with respect to the random variable itself Okay And we showed that in the case of DDPMs the ground truth noise that we add to X naught to get to Xt is simply a scaled version of what is called as the score function at Xt Is this all right Any questions here


Uh yeah I dont if you dont speak up I dont know I I dont I cant see my screen right So if you are interacting I dont know if you are interacting So I think its better if you speak up Shall we move on This is all right


Now we will do what is called as conditional generation


Using this idea is also called the graded diffusion


typically called classifier guided diffusion


okay so now note that okay so note


Alright


a DDBM


Estimates


Estimates these four up


That is what it is doing We know that This is where we will use the fact Now for conditional generation


One needs to estimate


Its good up


P of X P given Y okay where Y is a conditional random variable which can be a class or a text embedding or anything right conditional


can be a class label


Or it can be a text embedding or anything depending upon what your classes


your conditioning is right so yeah so what we are doing is instead of estimating the score of p x t we need to we need to estimate the score of p x t given y correct that is what is to be done now how do we do that is that we simply use bayes rule to do that we have the score of log of we need p of x t given y


with respect to HD


the derivative of log of


And we use Bayes law


P of x t times


of y i given x t divided by p y this base law okay then ive used the law of logarithms so this is log of p of x t


Yes


Derivative of log


f y given x t


Minus


log of derivative of log of


of y note that these derivatives are with respect to xt because these are scores right


Of this term is zero because it is independent of y So now the conditional score that we would want to estimate


be equal to derivative of log of


p x t with respect to x this is the unconditional score right plus some term okay this is log of


P y given x t with respect to x t


Yeah so this is the result This is the result that we need is that what we showed is that the if you want to train a diffusion model on P of XT given Y all you need to do is train a model on unconditional data and have an additional term okay estimate this score


estimate this core okay of p of y given x t so what do you mean by that see how do we do this in practices


Beep


Y given XT what is this is actually a classifier right


You agree see y is a class that you are conditioning your generation on p of y given x t is a classifier on x t isnt it


So what is done is that first train


Fine a classifier


On XD


Just keep it you know try and classifier on XT and then guide guide


The diffusion


Oh yeah this classifier okay what do you mean by that


So now there is a theres a unit that is to be trained


And note that this is actually estimating the score right so this will take xt


Now because this is a network


that is a conditional diffusion model it will also take a y as an input this is where you have the the class label right that is coming as an input so let us make it a little more


easier to understand so this will take x t and y as an input and here you have the


P going as an input okay right so now what you get here is the epsilon theta star which is


the unconditional score right we want this to be the conditional score what do we do is that train another classifier


classifier is p y given x t so this will take x t as an input and it will give you a class okay this is pre trained okay we could declassify the pre trained now what you do is there is a score matching that is happening here which is the usual


loss that is back propagated


In addition to this you also calculate here okay this is the output of P of y given xt okay Take the log of it compute the derivative of this gradient of this with respect to xt How do you do this See we can do a backpropagation with respect to parameters Just like we do that we can do a backpropagation with respect to the input of the network also in PyTorch right So you take the gradient of this the output of this


Network with respect to XT here Okay you back propagate add those gradients


with respect to XT to this and then back up again here


Thats all youre trying to do


Is this all right So finally during the inference what do you do You give an x and a y as an input to this t data star network If the sampling is exactly the same sampling procedure here is the same thing right You do the exact same thing here but you give y also as an input here while you are estimating this loss

speaker_4: So one question

speaker_1: Uh hold on huh Okay

speaker_4: Oh okay sorry

speaker_1: Yeah so this is called classifier guided diffusion models conditional diffusion classifier guided conditional diffusion There is another version called classifier free guidance I will not talk about it I mean you can just do see that as a homework Its a variant of this


read that as a self study thing yeah this is called classifier guided conditional diffusion where uh you first uh realize that the diffusion model that you are training is implicitly doing the score matching and use bayes law to estimate i mean represent the conditional score in terms of unconditional score and the classifier okay pre trained classifier on xt on different noise levels okay and then use that pre trained classifier along


with the unit to estimate the conditional score okay then you have trained a conditional diffusion model where you have classifier guidance so now one question that might come up is uh see y need not be a class label no it can be a text embedding also if it happens to be a text embedding this p of y given x uh y given xt will become a regression mod regression network that would take an xt and produce the


uh corresponding text embedded


Right So I have asked you to implement this So what you should do is while you collect multiple XTs no while you are training this theta you also train a classifier to get the corresponding class for the XT OK Use that classifier Get the gradient of every XT with respect to the output of this classifier and add that to the gradient of this unit and backpropagate That is what you need to do


Yeah so now any questions on this

speaker_3: Uh yes sir so the classifier is not trained as part of the process right

speaker_1: So classifier is already pre trained so you pre train the classifier and keep it yes

speaker_3: Okay but if the but if it has no effect if this process does not have an effect on our if we are not getting the desired results what could be wrong actually

speaker_1: uh whats the see typically what happens in classifier guided diffusion this see if you look at it this classifier has to discern the class uh by taking a noisy sample as input correct

speaker_3: Okay

speaker_1: Now if if P is very high the sample becomes too noisy

speaker_3: Okay

speaker_1: See it has to design the class at all noise levels that will become too much for a classifier to do isnt it

speaker_3: Okay okay

speaker_1: And typically this classifier fails that is because at high higher noise levels and thats why classifier guided diffusion does not work too nicely

speaker_3: I need this

speaker_1: So thats why people went from classifier guided diffusion to classifier free diffusion okay classifier free guidance okay so which I said just read it as a homework I mean I need


uh i mean i i leave some questions i mean some concepts uh to you as homework so thats why people move to classifier free guidance where there is no classifier by having a good guidance just read that huh it is there in the tutorial that i had given uh as a reference read that once but yeah but what ive asked you to implement in assignments as a classifier guided equation the problem might be that you are overburdening this classifier to get the classes at multiple noise levels thats why thats where the problem can come


In fact all the the state of the art models right like this this stable diffusion imagine etc all all use classifier free guidance not classifier guided diffusion for conditioning


Yeah okay so any other question see there is uh one other last piece right I mean you see this uh

speaker_3: Okay so any of the

speaker_1: stable diffusion thing ive asked you to do that in your assignment as well the stable diffusion stabilityai company you know what they are doing is the diffusion ddpms are not built on the image space what they do is they first train


they take x naught and get x naught cap so this is a they first try in a vqva okay


is the encoder and decoder of a VQ VIE okay so you get the Z corresponding to the data they first try a VQ VIE okay then what they do is TDPM


Or that prime G D P M


On the latent space of VQVA


They train a DDPM on the latent space of the QAE and generation right So now what happens is generation


First


Get a new latent sample right Because the entire generative model is


built on the the latent space of VQVAE and then pass it


So the decoder


of VQVA to finally get the image


I asked you to do this as well right I mean its pretty simple The point is that building a diffusion model on the image space is very difficult because its of very high dimensions right Instead of doing that you first train a encoder decoder model or a VQVAE get the latent vectors and you train a DDPM on the latent vectors of the VQVAE and then when you sample you first sample the latent vector


latent vector pass it to the decoder of eqvae and get the generated sample thats what all i mean thats what is done in this table diffusion right where uh i mean they step they call it stable stable because you are not doing it on the image space but you are doing it on the latent space of a pre trained eqvae


Okay so thats about it Thats all I wanted to cover in DDPMs So one other piece to be covered today is DDIMs right Diffusion implicit models where you have the inversion possible possibility of inversion and also they address this drawback of the inference time of DTPM being too slow right Because you need to hop capital T number of steps which is typically of order of thousands So


DDIMs which are denoising diffusion implicit models will take care of that particular issue We will look at DDIMs and then Ill go to noise contrastive estimation and self supervised learning


Shall we take a break now for about 10 15 minutes

speaker_3: Okay

speaker_1: the plan is the following right i will uh uh we will we will do ddpms ddims this class possible at the end of this class uh i will just give you an introduction to self supervised learning next class i will do noise contrastive estimation self supervised learning and if possible ill also sneak in some distillation ideas knowledge distillation and in the final class on 16 we will look at the autoregressive models transformers and some introduction to llms


that would conclude the course see we had to have 14 classes right uh how how much do we have do we have how many classes have we done so far does anyone have a count

speaker_4: So as per your lecture label it is 10th

speaker_1: Uh thats I also noticed that but did I start writing from the very first class

speaker_4: I think uh theres also lecture zero so it is its like

speaker_1: Like eleven


Is that zero Yeah there is a logistic

speaker_4: Logistics one yeah

speaker_1: so yeah this is 11 so well have 13 classes uh okay yeah typically thats what a semester is you know its between 13 and 14 14 classes of three years but its okay i think we have covered uh like a sufficient growth so well have two more classes right and well do self supervised learning distillation and some introduction to llms i think that would that would conclude it okay so lets take a break its 11 10 uh lets take a short break of about 10 minutes


Come back at 1120


That okay

speaker_4: Yeah so just one question so in the assignment uh you mentioned IJPG so would you be talking about that

speaker_1: Of course definitely


Maybe in the next class yeah thats a self supervised learning method called IJPA Ill do it in the next class perhaps

speaker_4: Shirts

speaker_1: Yeah see you in a minute please come back in ten minutes uh where we have things to cover yeah


So shall we resume

speaker_4: Yes sir I have a question regarding stable diffusion


So the latent space used in the generation is it just after the encoder or the after mapping to the dictionary of embeddings

speaker_1: Oh yeah yeah so it is the quantized latent space only

speaker_4: Okay okay

speaker_3: So but how do we sample from that because its a its a quantized set of vectors right

speaker_1: So what See you take the encodings as the quantized vectors right And then build a generative model on top of it


Then the all the all

speaker_3: All the all the quantized vectors

speaker_1: for bank corresponding to the entire data set


Yeah


Any other questions


Yeah its a sample tag


Okay so let us uh look at this another class of models now called


You know


Fusion implicit models theyre called


Okay so now the the motivation for these class of models are the following right So they first ask this question right DDPMs


R Marco VM right


Actually first order mark will be in


Because of this what happens is so the sampling or the inference


Sampling is slow Uh what do you mean by that It is slow because


Wee


Im Clive


us to hop through


Three steps


Because I did recall that right in the sampling procedure


inference here you need to hop to capital T to one okay which is very slow so why is this happening this is happening because the uh the model that we have constructed is Markovian right the question that they asked in DDIMS so is there a


The question is so this is yeah Ill


I can give you the other motivation also and then we will answer both of them using one model construction


DDPMs cannot perform posterior inference or also called inversion Okay So what do we mean by that We know that right I mean given X we need P of Z given X We need a latent vector And DDPMs cannot do that Okay Why Why is that Because the encoding process will converge to normal 0 1 And for every input sample you will get some sample from normal 0 1 Now suppose you take that sample from normal


zero one okay and uh run through the uh the


generate generation process or the denoising process okay theres no guarantee that you get the exact same image that you started with let me repeat what i said suppose you take an image okay or a data point and encode it using the ddpms encoder you get a particular x capital t right now if you take the same image and do encoding another time uh you will get another sample corresponding to that right if you take both those uh outputs


of both both of those forward processes and run through the backward process there is no guarantee that you will get the exact same input sample that you started within a DDPM model right


thats what i mean by ldpms cannot perform posterior inference or inversion so now the question is can both of these uh props the ddims uh solve both of these issues actually okay


I am


Non non Marquisean


What is


Dot dot


That enable fast sampling


Because of the non Markovian assumption right Okay Non Markov enable fast sampling plus inversion Both of these are possible


Now the I mean this is not the most interesting part The most interesting part is


If you train a DDPM okay then you are also training DDIM which is which means that requires more additional training


No additional timing


So this is the beautiful part of it right DAN DDPM


If you train a DD3M then you are implicitly training DDIM is what the idea is Okay So let us concretize these ideas You know what do I mean by all this We will put math to it and understand Okay See the first observation that is made is


Its an observation


The DDPM


DDPM loss


Last function


depends


only on Q of


XT given X naught


Okay this is the first observation that they do is that the DDPM loss function only depends on Q of XT even X naught


Okay


So now the the


Based on this observation


Right based on this observation they say that


on and not on


You are


X


1 2 t given x not


Okay so please pay attention here See Q of XT given X naught is the posterior of the Tth latent variable conditioned on X naught okay And Q of X1 to T given X naught is the joint distribution of okay all the latents given the data variable Now the observation that is made is that the DTPM loss function okay or the elbow


does not depend on the joint the the joint distribution of all the latents given data but only on the dth latent variable given data okay so this means


in place


Thats long the ass


You lost


is same


as that of DDPM


The elbow does not alter this is the key observation okay


So which means that as long as Q of XT given X naught remains the constant the elbow doesnt alter Which means that see there is one other known thing in the probability theory which would say that there can exist multiple joint distribution that has the same conditional


you that does that make sense suppose there are uh like there is a particular conditional distribution okay we can construct multiple joint distribution that would have exactly the same conditional distribution


Now what I do is so define


A family of non Markovian


Encoding distribution


including distributions okay dark


Exact


Conditional


as in DDP So what we are seeking is that I will give you now a family of non Markovian


conditional encoding distribution such that the conditional is same that of the uh ddpm okay so what they do is suppose


Sigma is a positive real number


Is a positive real number They define Q sigma of


x 1 2 3 given x naught so this is the joint distribution non Markovian joint distribution that we are defining okay its given by


Q of Q sigma


Steve give a next mark


Lines


This is by the chain rule of probability Q sigma


xt minus one given xt and x0


This is a non Markovian distribution okay


glo Sigma


T minus 1 given XT and X naught


Given its a normal distribution


Which


mean equal to root


alpha t minus one bar the same notation that we have with d d p of x naught plus root of


1 minus alpha t minus 1 bar minus sigma t squared


Long very distant


Just a second here this is


exploit art this is


Theres something wrong with this


One minus


Uh 1 minus alpha t into sigma t squared okay and yeah


It looks a little complicated but Ill tell you why this was done


x to the minus


T bar into X naught


divided by root of one minus alpha t power


the mean and the variances yeah sigma squared into i yes


Okay so this is the distribution So now why is this how did they get into this complicated form Its simply they wrote this down such that such that sigma Q sigma of XT given X naught okay will match that of the DDPM which is simply


This term that we knew right alpha t bar into i


So this distribution okay Q sigma is constructed in such a way that


The conditional distribution matches that of a DDPM


Is this is this clear


See there is that the DDPM DDIMs paper right gives a proof that y would I mean they did do the algebra and show that Q sigma of xp given x naught is normal this has this particular form that matches with that of DDPM But yeah so the point is


What we have done now is defined a family of non Markovian forward processes okay such that all of them have the same conditional as that of DDPM Is this clear Any questions so far


Hello am I there


uh questions here did you understand this


Okay fine so oh this is uh how you define the uh the


non Markovian process Okay now you define the corresponding I mean as you see all of these are known right I mean theres nothing to learn The model similar to the previous case define the define


reverse process


Reverse or the denoising process


correspondingly


follows so what do we need we simply need a p theta of


xt minus one given xt


Define that to be for t equal to 1 it is a normal distribution Similarly at mean mu theta and variance sigma i okay at different other ts it is equal to q phi of


xt minus one okay given xt


And instead of x not what we have is


Yeah you can call that us


Lets not call it call it as mu theta only


This is the estimated mu theta let us call the estimated x naught as


F t dot


function of x t okay this is how we define it where


We know that our x naught is given by x t minus root of 1 minus alpha t into epsilon divided by root of alpha t bar it is what we have


So in the this is in the forward process


In the reverse corresponding reverse process we call the


g eta of x over is an estimate of x naught to be equal to


60 my best


Just like we did with DD PMs we have a similar thing with DD IMs Instead of epsilon we have epsilon theta cap right Which is the estimated epsilon divided by alpha t bar Thats all This is in the reverse process


Okay so now with this what can be shown is see I am skipping the proof because its sort of


slight forward in the sense that if you look at the DDIM paper you will get that and also its not like very relevant to what we are doing what can be shown us with the above models


The elbow okay


will come out to me


the same as that of the DPM


This is what the the take home message is that when you are training a DDPM okay you are also implicitly training a large class of non Markovian models with these particular distributional forms


Does that make sense


So is that clear So what Im saying is when you train one DGPM with the procedure that we just saw youre actually training a grammar model of infinite models non mathematical models with this particular distribution that we just learned Thats why we named them denoising distribution implicit models because youre implicitly training so many models while


also in one digital


So this implies what does this imply this implies that


The training procedure


Im the boss


the same


EDPM and EDIMES


Then you might ask right what is the whole point I mean like what are we achieving by doing all this Right However by returning procedures their information are different no


Inference is very different right so how do we infer for DD


P ms okay sampling is from you get xt minus 1 recurring recurring simply from p theta of xt minus 1 given xt


Okay which is caution


What was the distribution of DDPM


Recall it is


Can somebody tell me what it is E Gita


mu theta right which is xt minus one


Let me not write that its always 16 minus 1 and this one was uh


Alright the entire thing is what Im thinking its a


Huge thing


Hold on let me try to write it


Give me a second Ill write it I had written it before


So what was the mean mean was


XT by


This minus


1 minus alpha t divided by


root of one minus alpha t bar times


Epsilon theta star


So this was the mean and the variance was uh


t squared times i okay this was in ddpm while in dd ims


the inference procedure changes which is still sampled from p theta of xt minus 1 given xt but since it is a non Markovian process okay the mean and the variance changes thats all


may write it down the


Mean is given by


The water


for t minus 1


So power p r t minus one times


the output of the neural network


Yes


root of one minus


power bar t minus one minus sigma t squared


times epsilon theta star


It must clear the mind


Thats all right So this is what changes So what changes is that the way the denoising is done okay changes the


Fining procedure remains exactly the same as the DDPM Okay Now if you make sigma to be zero here right with sigma equal to zero the class of model that you get is such that the encoding process


Comes


Deterministic


The encoding process becomes deterministic because there is no noise component to it So now this what does this enable This enables inversion Okay Deterministic enable in inversion


So what do you mean by that Given a particular x naught which is a data sample okay what you could do is you could run the forward process okay that is a deterministic forward process for DDIM and get the corresponding latent vector the noise latent vector which when used in the sampling okay or denoising process will generate this exact same


For example its not


Does that make sense


All you should do is the following right What is to be done is given an x naught you run the forward process okay of the DDIM and you note that the forward process of DDIM is similar to that of the forward process of DDPM because the conditionals are the same But because with sigma equal to zero if you make sigma t equal to zero here and then run the sampling of DDIM okay


you will get the exact same sample okay corresponding to the input sample So you start with suppose you start with an image okay Running the forward process of DDIM will give you a noise sample which when used in the reverse process of DDIM will give you the input sample which means that you have encoded or inverted or youve gotten the exact same


latent variable corresponding to the input image


Is that making sense


Hello am I there


Any questions on this


See the difference between DDPM and DDIM is in the fact that in the sense that what you have right as the forward and reverse processes they would change They would become non Markovian processes okay But because of the way these non Markovian processes are constructed theyre constructed in such a way that the conditional distributions happen to be exactly the same has the same


form as that of RDD


which implies that training a DDPM is implicitly training multiple DDIMs that are there


What is the advantage of that The advantage is that because one of the at one of the the values of sigma the the class of models that we have generated becomes deterministic you can use that for inversion


Is that clear


I will also share our nice


blog post on this


You may ask any questions if you have on the meantime

speaker_3: So one question so uh the reason why DDPMs are non invertible is it because the the Markovian processes are non reversible

speaker_1: It is uh not because of that in particular it is because of the fact that the encoding process involves noise addition no


Its because

speaker_3: And in case of DDIMs

speaker_1: Yeah in in the case of DDIMs where sigma equal to zero the encoding process does not involve noise addition


It is simply a function of alpha

speaker_3: Okay and thats why it is reversible

speaker_1: That is why it is reversible correct But the thing is the alphas are designed in such a way that you know if you


keep moving in the forward direction they would still approach a a a normal 0 1 okay in the stationary distribution case however that the its the the the forward process is not that you take an image and add noise


the way they are constructed

speaker_4: So the forward process is non mock

speaker_1: Both the forward and the reverse processes are normal in DDIS yeah


okay so yeah see actually what ive asked you is that uh see you are you will be training one model okay which is the ddpm model but what changes is the inference right inference and the inversion uh in the case of ddim simply take a pre trained ddpm okay and use it for inversion as the nice uh blog on ddim inversion i will


uh share that with you hold on looking for it


Ive asked you to invert get the noise samples and do an interpolation between those noise samples corresponding to two different images and then do a reverse direction is what Ive asked for Its a nice experiment to do Let me just share that Hold on In our group I will put it in our group


mm not in the call chat how do I put it


Oh beams

speaker_3: They can put it in the culture itself

speaker_1: No but that will just go away no I dont want that to happen in general

speaker_3: Golf ball

speaker_1: No it will not

speaker_3: No it will not go away it will stay there

speaker_4: Whatever you put here is it will come in tunes uh yeah tunes

speaker_1: So anyway I just put it in the chat window have a look at it


Okay so thats it In fact thats the end of what I wanted to do with diffusion models


See all these uh these uh text to image uh generators right theyre all diffusion models okay uh


they use the classifier free guided diffusion and theyre all dd imms they are not ddpms because uh i mean yeah in fact the training is the same but because the inference has uh multiple advantages over the ddpms right what they do is they infer using dd imms processes not ddpms processes but all of the state of the art models are

speaker_4: All of them

speaker_1: diffusion models okay right so its better if I start a new


page


Should I start self supervised learning in the next class


What do you reckon


give you the introduction and go get over the math in the next class or like we can start in the next class


I go with what you say what should we do

speaker_3: Uh so i we can have introduction and then the maths in next class maybe

speaker_1: Sure then I have to start a new uh notebook


So this is uh L eleven I will continue in the same notes next time


Well supervised


Presentation learning


So these diffusion models right because of their elegance in a sense that all their

speaker_4: On the phone


Got the endergetic

speaker_1: Theyre gone

speaker_2: uh for the DBI and everything else

speaker_3: I mean like how we for the conditional generation and all those things

speaker_1: Yeah yeah yeah conditional generation its everything remains the same all that we changes is the forward and the reverse process even the training procedure does not change right the forward and the reverse process changes


uh the two xt uh the relationship between xt and x0 does not change the relationship between xt and x0 that you need for training the model does not change it remains exactly the same as that of ddpm but the forward and the reverse processes changes which means that the the sampling has a different equation which i wrote which is different from ddpm okay and the uh the uh the


Encoding process has a different equation Okay Encoding we dont use explicitly I mean we use it only if we need this inversion thing right If you want the corresponding X corresponding latent latent corresponding to a given image we have to run through the forward process of DDIM non Markovian DDIM Otherwise we only need that XT you know and the relationship between XT and X naught are exactly the same as that of DDPM in DDIM And the conditioning etc


All of them remain exactly the same

speaker_2: So lets now switch gears and we will look at the self supervised learning these are not generative models

speaker_1: say okay uh the problem is uh of that of what is called as representation learning we have actually done it in a slightly different way to representation learning


Okay so what is the problem the problem is given


data I will switch back to our older notation okay x1 through xn these are not the intermediate states states in diffusion models okay iid drawn from some unknown distribution px okay there are no labels here learn a function


learn a function f theta okay f theta from space of x to some space z okay where z the dimensionality of z is typically much lesser than that of dimensionality of


Learn a function such that such that


Downstream tasks tasks as they call them


On on Z


Yeah so this is the uh uh


Object
