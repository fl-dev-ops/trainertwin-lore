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

### 00:00:00 · Speaker 1

Hello all, welcome back to Carroted with Wason YouTube channel. My name is Bhavna. I hope you all are doing well. So this is a series as you all know we will be doing a lot of mock interviews. Today with me I have Chandrasekhar. So Chandrasekhar is a two year experience of front end developer. Right now he is working for Decathlon. So this interview is going to be

### 00:00:15 · Speaker 2

on various topics we would be starting with a scenario driven question followed by basics of javascript then basics of react there's a lot of things to learn so please watch the video till the end in case if channel checker do not answer certain questions properly at the end i'm going to give answers to those others so please watch the video till the end channel checker if you can introduce yourself we can get started

### 00:00:33 · Speaker 1

Hi, my name is Chandresh Shilkar. I have the education side of it. I've done my engineering in computer science and the experience side of it, I've been working as front-end developer using tools like React, Next.js, HTML, CSS for past two years.

### 00:00:54 · Speaker 2

wonderful wonderful let's get started immediately let's say you have a scenario where you have to build a video calling application something like google meets okay what are all the challenges that comes to your mind in the sheet building a video calling application like that

### 00:01:09 · Speaker 1

So building a video calling application let's say the first thing would be um security as to how we're gonna maintain the security of an application so that anyone whoever wants to join the call wouldn't be allowed just authorized persons would be allowed to join the call yeah the other would be how we'll maintain the network maybe there is different bandwidth and there is switch between the networks as to how we'll handle that and

### 00:01:39 · Speaker 1

Other would be if it is uh browser based co video calling then uh there'll be things like cross border cross browser compatibility so the different browsers so how do we handle that and there are other edge cases uh something like if the user has exited or maybe then there is some network issue so how do we handle it so we should have some hard exit or something in that

### 00:02:04 · Speaker 2

Exactly

### 00:02:05 · Speaker 1

And that would be maybe providing access how to like integrate it with your application

### 00:02:14 · Speaker 2

So as you rightly told Chandrasekhar, along with that, there are multiple other problems whenever we're integrating with a video calling. So a lot of these problems are recently been solved by a tool called Zego Cloud. I've been using the Zego Cloud across multiple projects of mine. See the advantages of it is like first thing is a plug and play. If you are a developer who hasn't worked a lot about the video calling, all you have to do is just take their APIs using the help of their powerful UI kit. All you have to do is just take their UI kits. Just at a project, you will be able to introduce into the, you know, inculcate the video calling into your web mobile app with React Native React.

### 00:02:44 · Speaker 2

js angular react native and android ios everywhere you'll be able to integrate the video calling seamlessly and they also have not just the video calling they also have audio calling and other multimedia facilities so also they have like a beautiful thing is you don't even have to worry about the customization whether you want a group video call whether you want one-on-one video call full screen and as you can see like multiple templates like this all of them are readily available for you and all you have to do is just go and register in their portal as soon as you register you're even gonna get like 10 000 seconds of free duration

### 00:03:14 · Speaker 2

Like for first 10th and second you can experiment and learn about Zego Cloud and then you can start using it officially. So everything that somebody wants whenever they want to integrate with video calling, audio calling or any other multimedia things are readily available with Zego Cloud. I would suggest you and all the fellow developers to use Zego Cloud. Okay. So now getting back into the further questions of the video calling channel, Shaker. Okay. I'm sorry. Have you ever got a chance to work with a video call in the past, Shaker?

### 00:03:42 · Speaker 1

Yeah I've uh but I've had the opportunity to work with uh

### 00:03:45 · Speaker 2

So now my question is see do we have to transfer video from person X to person Y? Correct. So video end of a day there is nothing called a media that exists in reality. We have to convert that into some form that is transferable. Correct. So tell me which protocol we should use if we have to transfer the video between like video data between one user to another user. I must see network.

### 00:04:06 · Speaker 1

So we have network protocols we can use TCP or UDP so based on our preference we can work

### 00:04:15 · Speaker 2

If you go with TCP and UDP what do you think is the primary difference between the two

### 00:04:22 · Speaker 1

Uh TCP would be transmission I think the security and the two-way communication and the other parameters like let's say bandwidth the not very sure but

### 00:04:37 · Speaker 2

Not very sure

### 00:04:39 · Speaker 2

Yeah, I mean, what you're saying is correctness is very secure. No data loss. All data is basically safely transferred. Whereas in case of the UDT, there is some packet loss is possible. Okay. For a video calling application, I would suggest it's always good to use UDT than DCT because we are finally some packets are lost. For example, when we are speaking, a couple of packets lost will not create a lot of problem. So it's always good to use the library.

### 00:05:00 · Speaker 1

Live streaming

### 00:05:02 · Speaker 2

Yes, exactly. Correct? So let me ask you one fundamental question around the same again video call it in the system. It's a video has to be transmitted from you to me in some same like zoom we are using right now or in Google which we are using. Just explain me the architecture how it's going to transfer from you and it will come to me. What are all the things that would happen behind the scenes in a high level?

### 00:05:24 · Speaker 1

okay so let's say there are like two people connected in a call so first there has to be a network connection a socket has to be created so both are connected and we have to use one form of let's say transmission protocol let's say if we're using udp to use udp to transfer data from one to another in a secure way and maybe if it's it's very secure and it has to be encrypted and decrypted or something

### 00:05:54 · Speaker 1

And the data has to be converted and processed

### 00:05:58 · Speaker 2

Got it yeah yeah okay present yeah anything else you want to add anything please

### 00:06:04 · Speaker 1

Uh so something like chat application we can use something like Socket.IO where we can

### 00:06:11 · Speaker 2

but some more interfaces can be added probably when you're building it and you some more things can be added can you please present your screen general let's follow through problem the problem is very simple general listen to music okay the problem is you have to have like four characters a b c d consider this a b c d as buttons a is a button b is a button c is a button d is a button every time whenever you click a character let's say click on a

### 00:06:41 · Speaker 2

In below you will be printing A and an arrow.

### 00:06:46 · Speaker 2

Can you put

### 00:06:47 · Speaker 1

The end

### 00:06:48 · Speaker 2

Arrow okay this arrow

### 00:06:50 · Speaker 1

I don't know

### 00:06:50 · Speaker 2

okay you click on b you're gonna put b and an arrow man you can click on c you're gonna put c and arrow you're gonna click on d you're gonna click on d and arrow okay so let's say you click the same character second time like for example a b c d then you click a again just add a to the end of the list i'm a clear jenny basically keep making that more like a train you're making a train of all of it let me start in the session yeah with like around 10 to 15 minutes you saw that is very straightforward

### 00:07:43 · Speaker 1

So I have it a little slow

### 00:07:48 · Speaker 1

Oh sorry

### 00:07:58 · Speaker 1

Book

### 00:08:02 · Speaker 1

But I'll we can see the difference in the next step because I'll put the console on in the same place

### 00:08:19 · Speaker 1

Mm is this good

### 00:08:21 · Speaker 2

Yeah instead of logging can you put it on the screen like I want to see the stack can you render it

### 00:08:27 · Speaker 1

Yeah okay

### 00:08:34 · Speaker 2

the check again it's working okay so let's slightly extend it now the ask is let's say it can be in the sports and books the ask is let's say you already have a character in the thing for example in um you have a b c d okay you click on a again okay let's say let's say click on c again c is already part of this train okay or what we have to do is we have to remove that c and it's aroma okay and

### 00:09:04 · Speaker 2

that C in the beginning of the list for example we had A B C D if you click on C again it will become C A B D

### 00:09:14 · Speaker 2

Sees it okay

### 00:09:16 · Speaker 1

Okay so if we have A B C D and if I click on C again it has to be C A B D

### 00:09:24 · Speaker 2

Correct. So whichever the position it is there currently, that position has to be sliced and it should be kept in the beginning. For somebody that is already in the beginning, okay. If it is already in the beginning, then you can you don't have to do anything. You can just skip it.

### 00:09:30 · Speaker 1

Holy

### 00:09:36 · Speaker 2

I'm not good please continue I have five to seven minutes to implement this channel code yeah

### 00:09:43 · Speaker 2

If you want to know about some syntax let me know

### 00:09:46 · Speaker 1

Yeah uh to check position of uh let's say a value

### 00:09:50 · Speaker 2

You want to know where that particular character present

### 00:09:55 · Speaker 2

Then you can use it index of right which one you're using

### 00:10:08 · Speaker 2

We have last two to three minutes and a second okay

### 00:10:11 · Speaker 1

Yeah

### 00:10:22 · Speaker 1

Yeah this works

### 00:10:23 · Speaker 2

It could be

### 00:10:26 · Speaker 1

Sorry B

### 00:10:27 · Speaker 2

What frequency

### 00:10:30 · Speaker 2

or not be the

### 00:10:32 · Speaker 1

You do it.

### 00:10:34 · Speaker 2

Okay

### 00:10:42 · Speaker 2

Yeah B

### 00:10:45 · Speaker 2

yeah yeah dd we prefer dog

### 00:10:48 · Speaker 1

Okay

### 00:10:51 · Speaker 2

okay sounds good yeah we'll discuss the first time from this challenge second okay if audience has been watching the video if you feel like there is a better approach to solve this please do put it and put your repository or just in the comment section me or challenge secretary can be behind tell whether the right answer or not okay so i'm sharing a secret with you in the chat section okay please copy this

### 00:11:15 · Speaker 1

So uh

### 00:11:20 · Speaker 1

So every second uh the value changes so initialize zero for one two three four five six

### 00:11:27 · Speaker 1

So it'll print uh

### 00:11:30 · Speaker 1

uh like increase the value of it

### 00:11:34 · Speaker 1

No it will print but no no it will print wait just a second

### 00:11:34 · Speaker 2

Okay

### 00:11:39 · Speaker 2

Please please correct

### 00:11:40 · Speaker 1

Yeah, so it'll start from zero and for every second it will add a number and we'll look zero one two three four five six

### 00:11:50 · Speaker 2

Now, can you try running the code? Will it run? Have you exported? Please export it.

### 00:11:55 · Speaker 1

Yeah

### 00:12:16 · Speaker 2

Okay, so every time basically it is incrementing the value of count. Initially the value of count was zero and we have an interval that is running it every one second. So because of which the value of the count it is keep incrementing, correct? But if you observe, do you feel like the value of count is changing every time or the count value is always one, what it is?

### 00:12:40 · Speaker 1

So the value of count

### 00:12:42 · Speaker 2

always changing right or it is always

### 00:12:44 · Speaker 1

Yeah it's strange

### 00:12:46 · Speaker 2

In line number 12 uh line number 12 if you remove the account what will happen

### 00:12:52 · Speaker 1

So if we remove the okay if we remove the count and we refresh the then it will be zero it will not change

### 00:13:01 · Speaker 2

Okay please do that

### 00:13:10 · Speaker 1

Okay one sorry

### 00:13:12 · Speaker 1

So first time it decreases the value and it remains there

### 00:13:16 · Speaker 2

Correct, correct. So I'm sharing another snippet in the checker now. Okay. So please take the snippet. Okay. And try to tell me how many times the console.log will be printed in this exception is simple. How many times the console.log will be printed? Okay. Let that error be there on the line number 19 so that you can guess it.

### 00:13:52 · Speaker 1

This should have a different name right my component okay

### 00:13:52 · Speaker 2

Actually that should be my computer

### 00:13:56 · Speaker 2

don't give that there for a while let's imagine the code would run okay let's imagine line number three is a different name okay the ask could be how many times the control.log will be printed let's assume line let's assume like line number three is my component actually okay or else we get another thing you could like uh like in the export default right instead of app you make something else so that any of you will get error yeah yeah and line number three you make it as my component

### 00:14:30 · Speaker 2

Mm no

### 00:14:33 · Speaker 1

Saw

### 00:14:34 · Speaker 2

And output basically I want to know how many times the console log is printed that's my question

### 00:14:37 · Speaker 1

So is it like the first time when it renders Or is it and every time we click on increment how many times uh

### 00:14:44 · Speaker 1

Last time and the component renders

### 00:14:44 · Speaker 2

Last time

### 00:14:47 · Speaker 1

First time in the competent

### 00:14:47 · Speaker 2

So let's try one

### 00:14:49 · Speaker 2

okay let's see run the code okay and then you keep clicking on the button let's imagine you can tell that way like let's say for example first it'll be shown once then every time when you click on a button and we keep implementing like that you can tell

### 00:15:04 · Speaker 1

So I didn't

### 00:15:04 · Speaker 2

So you need

### 00:15:05 · Speaker 2

Yeah yes

### 00:15:07 · Speaker 1

So that we can clear the

### 00:15:09 · Speaker 2

Yeah yeah very very one second audience members if you know the answers to this please mention that in the comment section like what is the answer question number three I think and your answer please go ahead

### 00:15:19 · Speaker 1

Yeah so every time we click on increment we will have a console log

### 00:15:24 · Speaker 2

Mm

### 00:15:25 · Speaker 1

Because we use memo here and we are changing the props value

### 00:15:29 · Speaker 2

Mm-hmm

### 00:15:30 · Speaker 1

So it does get rendered every time we change the value

### 00:15:33 · Speaker 1

So

### 00:15:33 · Speaker 2

So yeah let's see you run the code the first time the component rendered will be printed

### 00:15:39 · Speaker 2

uh correct no no don't run you run it your component and it will be printed once then follow every time whenever you click on the increment button it's going to be printed i'm a red check it

### 00:15:49 · Speaker 1

Yeah um yes

### 00:15:51 · Speaker 2

Okay please let's rent the pod now

### 00:15:55 · Speaker 2

Okay component rendered I'm able to see once okay now click on the button

### 00:16:03 · Speaker 2

That could be it

### 00:16:04 · Speaker 1

Complementary

### 00:16:08 · Speaker 2

yes please yeah then we go back to the code now to check once again

### 00:16:15 · Speaker 2

Yeah so we have memoized it's a memoized component that can dynamically can you talk briefly what is memoized component

### 00:16:25 · Speaker 1

Ah sorry what is memoise component

### 00:16:26 · Speaker 2

Yes yes

### 00:16:28 · Speaker 1

uh so uh memory memoise components are the one which we can avoid re-rendering if the prop that we have passed to it has not changed

### 00:16:38 · Speaker 2

Okay

### 00:16:39 · Speaker 1

So we can

### 00:16:40 · Speaker 2

So because of this reason what is happening every time whenever you click increment as the value of count is changing the child company is also changing correct for example it would have count you would have passed another prop to the child company it would have not rendered correct

### 00:16:53 · Speaker 1

depend on

### 00:16:54 · Speaker 2

Okay, you can stop sharing Jeni's record. Okay, we are at the last like I think we have left with just two more minutes. I'm Dan from Mai and Jeni's record. I have noted on my feedback. Before I share my feedback, do you have any questions for me, Jeni's record?

### 00:17:10 · Speaker 1

Um no I have no questions

### 00:17:12 · Speaker 2

So the way you are you are able to solve a problem that ABCD problem right so you are able to think through a problem very quickly and solve it which is good okay and even the guessing the output type of questions as well I know they are not very hard they are more like easy to medium sort of questions but still you are able to guess the whatever they have the program is good and guess the output almost accurately which is good couple of suggestion that I wanted to include

### 00:17:42 · Speaker 2

especially in the machine coding problem right uh let's take the first variation very click on a b c d and we have keep forming that chain correct you did not ask me like how long the chain would be continuing correct so always make sure whenever such questions come you ask the extremities the reason why i'm saying this is you cannot keep doing that right somewhere they should end whether it is the end of taking all the memory correct ask those questions one point number two do not start debugging all of a sudden

### 00:18:11 · Speaker 2

whenever such problems come right even if you have to debug take interviewers permission point number two point number three uh uh like before running the code always ask the interviewers you don't run by yourself also point here i would want to suggest is that get buy-in on the approach like are you comfortable is the interview a friendly approach because you start summary should help correct this is at a very high level general rest all the things whatever it includes with me if i were interviewing you with the question that i asked i would definitely select it

### 00:18:41 · Speaker 2

Okay any closing thoughts

### 00:18:45 · Speaker 1

The interview was really good so the questions and all of it

### 00:18:51 · Speaker 1

So we look forward to maybe take another interview maybe if it's possible something will level up

### 00:18:51 · Speaker 2

Okay so

### 00:18:58 · Speaker 2

Yeah sure just a couple of thank you so much yeah thank you so much for your feedback

### 00:19:00 · Speaker 1

Thank you so much

### 00:19:02 · Speaker 1

Thank you

### 00:19:03 · Speaker 2

Yeah all the audience who have watched the video if you like the video please like the video uh comment whatever you felt on it please share the video with your friends thank you so much for watching

