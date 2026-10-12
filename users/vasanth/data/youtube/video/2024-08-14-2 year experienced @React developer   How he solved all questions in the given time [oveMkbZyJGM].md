---
id: oveMkbZyJGM
title: 2 year experienced @React developer | How he solved all questions in the given
  time
url: https://www.youtube.com/watch?v=oveMkbZyJGM
date: '2024-08-14'
duration: 00:19:10
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---


# 2 year experienced @React developer | How he solved all questions in the given time


## Transcript

### Speaker 1

Hello all welcome back to Carroted with Wason YouTube channel My name is Bhavna I hope you all are doing well So this is a series as you all know we will be doing a lot of mock interviews Today with me I have Chandrasekhar So Chandrasekhar is a two year experience of front end developer Right now he is working for Decathlon So this interview is going to be

### Speaker 2

on various topics we would be starting with a scenario driven question followed by basics of javascript then basics of react theres a lot of things to learn so please watch the video till the end in case if channel checker do not answer certain questions properly at the end im going to give answers to those others so please watch the video till the end channel checker if you can introduce yourself we can get started

### Speaker 1

Hi my name is Chandresh Shilkar I have the education side of it Ive done my engineering in computer science and the experience side of it Ive been working as front end developer using tools like React Nextjs HTML CSS for past two years

### Speaker 2

wonderful wonderful lets get started immediately lets say you have a scenario where you have to build a video calling application something like google meets okay what are all the challenges that comes to your mind in the sheet building a video calling application like that

### Speaker 1

So building a video calling application lets say the first thing would be um security as to how were gonna maintain the security of an application so that anyone whoever wants to join the call wouldnt be allowed just authorized persons would be allowed to join the call yeah the other would be how well maintain the network maybe there is different bandwidth and there is switch between the networks as to how well handle that and


Other would be if it is uh browser based co video calling then uh therell be things like cross border cross browser compatibility so the different browsers so how do we handle that and there are other edge cases uh something like if the user has exited or maybe then there is some network issue so how do we handle it so we should have some hard exit or something in that

### Speaker 2

Exactly

### Speaker 1

And that would be maybe providing access how to like integrate it with your application

### Speaker 2

So as you rightly told Chandrasekhar along with that there are multiple other problems whenever were integrating with a video calling So a lot of these problems are recently been solved by a tool called Zego Cloud Ive been using the Zego Cloud across multiple projects of mine See the advantages of it is like first thing is a plug and play If you are a developer who hasnt worked a lot about the video calling all you have to do is just take their APIs using the help of their powerful UI kit All you have to do is just take their UI kits Just at a project you will be able to introduce into the you know inculcate the video calling into your web mobile app with React Native React


js angular react native and android ios everywhere youll be able to integrate the video calling seamlessly and they also have not just the video calling they also have audio calling and other multimedia facilities so also they have like a beautiful thing is you dont even have to worry about the customization whether you want a group video call whether you want one on one video call full screen and as you can see like multiple templates like this all of them are readily available for you and all you have to do is just go and register in their portal as soon as you register youre even gonna get like 10 000 seconds of free duration


Like for first 10th and second you can experiment and learn about Zego Cloud and then you can start using it officially So everything that somebody wants whenever they want to integrate with video calling audio calling or any other multimedia things are readily available with Zego Cloud I would suggest you and all the fellow developers to use Zego Cloud Okay So now getting back into the further questions of the video calling channel Shaker Okay Im sorry Have you ever got a chance to work with a video call in the past Shaker

### Speaker 1

Yeah Ive uh but Ive had the opportunity to work with uh

### Speaker 2

So now my question is see do we have to transfer video from person X to person Y Correct So video end of a day there is nothing called a media that exists in reality We have to convert that into some form that is transferable Correct So tell me which protocol we should use if we have to transfer the video between like video data between one user to another user I must see network

### Speaker 1

So we have network protocols we can use TCP or UDP so based on our preference we can work

### Speaker 2

If you go with TCP and UDP what do you think is the primary difference between the two

### Speaker 1

Uh TCP would be transmission I think the security and the two way communication and the other parameters like lets say bandwidth the not very sure but

### Speaker 2

Not very sure


Yeah I mean what youre saying is correctness is very secure No data loss All data is basically safely transferred Whereas in case of the UDT there is some packet loss is possible Okay For a video calling application I would suggest its always good to use UDT than DCT because we are finally some packets are lost For example when we are speaking a couple of packets lost will not create a lot of problem So its always good to use the library

### Speaker 1

Live streaming

### Speaker 2

Yes exactly Correct So let me ask you one fundamental question around the same again video call it in the system Its a video has to be transmitted from you to me in some same like zoom we are using right now or in Google which we are using Just explain me the architecture how its going to transfer from you and it will come to me What are all the things that would happen behind the scenes in a high level

### Speaker 1

okay so lets say there are like two people connected in a call so first there has to be a network connection a socket has to be created so both are connected and we have to use one form of lets say transmission protocol lets say if were using udp to use udp to transfer data from one to another in a secure way and maybe if its its very secure and it has to be encrypted and decrypted or something


And the data has to be converted and processed

### Speaker 2

Got it yeah yeah okay present yeah anything else you want to add anything please

### Speaker 1

Uh so something like chat application we can use something like SocketIO where we can

### Speaker 2

but some more interfaces can be added probably when youre building it and you some more things can be added can you please present your screen general lets follow through problem the problem is very simple general listen to music okay the problem is you have to have like four characters a b c d consider this a b c d as buttons a is a button b is a button c is a button d is a button every time whenever you click a character lets say click on a


In below you will be printing A and an arrow


Can you put

### Speaker 1

The end

### Speaker 2

Arrow okay this arrow

### Speaker 1

I dont know

### Speaker 2

okay you click on b youre gonna put b and an arrow man you can click on c youre gonna put c and arrow youre gonna click on d youre gonna click on d and arrow okay so lets say you click the same character second time like for example a b c d then you click a again just add a to the end of the list im a clear jenny basically keep making that more like a train youre making a train of all of it let me start in the session yeah with like around 10 to 15 minutes you saw that is very straightforward

### Speaker 1

So I have it a little slow


Oh sorry


Book


But Ill we can see the difference in the next step because Ill put the console on in the same place


Mm is this good

### Speaker 2

Yeah instead of logging can you put it on the screen like I want to see the stack can you render it

### Speaker 1

Yeah okay

### Speaker 2

the check again its working okay so lets slightly extend it now the ask is lets say it can be in the sports and books the ask is lets say you already have a character in the thing for example in um you have a b c d okay you click on a again okay lets say lets say click on c again c is already part of this train okay or what we have to do is we have to remove that c and its aroma okay and


that C in the beginning of the list for example we had A B C D if you click on C again it will become C A B D


Sees it okay

### Speaker 1

Okay so if we have A B C D and if I click on C again it has to be C A B D

### Speaker 2

Correct So whichever the position it is there currently that position has to be sliced and it should be kept in the beginning For somebody that is already in the beginning okay If it is already in the beginning then you can you dont have to do anything You can just skip it

### Speaker 1

Holy

### Speaker 2

Im not good please continue I have five to seven minutes to implement this channel code yeah


If you want to know about some syntax let me know

### Speaker 1

Yeah uh to check position of uh lets say a value

### Speaker 2

You want to know where that particular character present


Then you can use it index of right which one youre using


We have last two to three minutes and a second okay

### Speaker 1

Yeah


Yeah this works

### Speaker 2

It could be

### Speaker 1

Sorry B

### Speaker 2

What frequency


or not be the

### Speaker 1

You do it

### Speaker 2

Okay


Yeah B


yeah yeah dd we prefer dog

### Speaker 1

Okay

### Speaker 2

okay sounds good yeah well discuss the first time from this challenge second okay if audience has been watching the video if you feel like there is a better approach to solve this please do put it and put your repository or just in the comment section me or challenge secretary can be behind tell whether the right answer or not okay so im sharing a secret with you in the chat section okay please copy this

### Speaker 1

So uh


So every second uh the value changes so initialize zero for one two three four five six


So itll print uh


uh like increase the value of it


No it will print but no no it will print wait just a second

### Speaker 2

Okay


Please please correct

### Speaker 1

Yeah so itll start from zero and for every second it will add a number and well look zero one two three four five six

### Speaker 2

Now can you try running the code Will it run Have you exported Please export it

### Speaker 1

Yeah

### Speaker 2

Okay so every time basically it is incrementing the value of count Initially the value of count was zero and we have an interval that is running it every one second So because of which the value of the count it is keep incrementing correct But if you observe do you feel like the value of count is changing every time or the count value is always one what it is

### Speaker 1

So the value of count

### Speaker 2

always changing right or it is always

### Speaker 1

Yeah its strange

### Speaker 2

In line number 12 uh line number 12 if you remove the account what will happen

### Speaker 1

So if we remove the okay if we remove the count and we refresh the then it will be zero it will not change

### Speaker 2

Okay please do that

### Speaker 1

Okay one sorry


So first time it decreases the value and it remains there

### Speaker 2

Correct correct So Im sharing another snippet in the checker now Okay So please take the snippet Okay And try to tell me how many times the consolelog will be printed in this exception is simple How many times the consolelog will be printed Okay Let that error be there on the line number 19 so that you can guess it

### Speaker 1

This should have a different name right my component okay

### Speaker 2

Actually that should be my computer


dont give that there for a while lets imagine the code would run okay lets imagine line number three is a different name okay the ask could be how many times the controllog will be printed lets assume line lets assume like line number three is my component actually okay or else we get another thing you could like uh like in the export default right instead of app you make something else so that any of you will get error yeah yeah and line number three you make it as my component


Mm no

### Speaker 1

Saw

### Speaker 2

And output basically I want to know how many times the console log is printed thats my question

### Speaker 1

So is it like the first time when it renders Or is it and every time we click on increment how many times uh


Last time and the component renders

### Speaker 2

Last time

### Speaker 1

First time in the competent

### Speaker 2

So lets try one


okay lets see run the code okay and then you keep clicking on the button lets imagine you can tell that way like lets say for example first itll be shown once then every time when you click on a button and we keep implementing like that you can tell

### Speaker 1

So I didnt

### Speaker 2

So you need


Yeah yes

### Speaker 1

So that we can clear the

### Speaker 2

Yeah yeah very very one second audience members if you know the answers to this please mention that in the comment section like what is the answer question number three I think and your answer please go ahead

### Speaker 1

Yeah so every time we click on increment we will have a console log

### Speaker 2

Mm

### Speaker 1

Because we use memo here and we are changing the props value

### Speaker 2

Mm hmm

### Speaker 1

So it does get rendered every time we change the value


So

### Speaker 2

So yeah lets see you run the code the first time the component rendered will be printed


uh correct no no dont run you run it your component and it will be printed once then follow every time whenever you click on the increment button its going to be printed im a red check it

### Speaker 1

Yeah um yes

### Speaker 2

Okay please lets rent the pod now


Okay component rendered Im able to see once okay now click on the button


That could be it

### Speaker 1

Complementary

### Speaker 2

yes please yeah then we go back to the code now to check once again


Yeah so we have memoized its a memoized component that can dynamically can you talk briefly what is memoized component

### Speaker 1

Ah sorry what is memoise component

### Speaker 2

Yes yes

### Speaker 1

uh so uh memory memoise components are the one which we can avoid re rendering if the prop that we have passed to it has not changed

### Speaker 2

Okay

### Speaker 1

So we can

### Speaker 2

So because of this reason what is happening every time whenever you click increment as the value of count is changing the child company is also changing correct for example it would have count you would have passed another prop to the child company it would have not rendered correct

### Speaker 1

depend on

### Speaker 2

Okay you can stop sharing Jenis record Okay we are at the last like I think we have left with just two more minutes Im Dan from Mai and Jenis record I have noted on my feedback Before I share my feedback do you have any questions for me Jenis record

### Speaker 1

Um no I have no questions

### Speaker 2

So the way you are you are able to solve a problem that ABCD problem right so you are able to think through a problem very quickly and solve it which is good okay and even the guessing the output type of questions as well I know they are not very hard they are more like easy to medium sort of questions but still you are able to guess the whatever they have the program is good and guess the output almost accurately which is good couple of suggestion that I wanted to include


especially in the machine coding problem right uh lets take the first variation very click on a b c d and we have keep forming that chain correct you did not ask me like how long the chain would be continuing correct so always make sure whenever such questions come you ask the extremities the reason why im saying this is you cannot keep doing that right somewhere they should end whether it is the end of taking all the memory correct ask those questions one point number two do not start debugging all of a sudden


whenever such problems come right even if you have to debug take interviewers permission point number two point number three uh uh like before running the code always ask the interviewers you dont run by yourself also point here i would want to suggest is that get buy in on the approach like are you comfortable is the interview a friendly approach because you start summary should help correct this is at a very high level general rest all the things whatever it includes with me if i were interviewing you with the question that i asked i would definitely select it


Okay any closing thoughts

### Speaker 1

The interview was really good so the questions and all of it


So we look forward to maybe take another interview maybe if its possible something will level up

### Speaker 2

Okay so


Yeah sure just a couple of thank you so much yeah thank you so much for your feedback

### Speaker 1

Thank you so much


Thank you

### Speaker 2

Yeah all the audience who have watched the video if you like the video please like the video uh comment whatever you felt on it please share the video with your friends thank you so much for watching
