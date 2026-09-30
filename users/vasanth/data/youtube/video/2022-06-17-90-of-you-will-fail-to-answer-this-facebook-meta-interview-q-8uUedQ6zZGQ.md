---
id: 8uUedQ6zZGQ
title: 90% of you will fail to answer this Facebook/Meta Interview question Pt-2 (MAANG
  series - 2)
date: '2022-06-17'
url: https://www.youtube.com/watch?v=8uUedQ6zZGQ
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ At the time of this series recording, there was no video series which was discussing\
  \ MAANG (Meta, Apple, Amazon, Netflix, Google) interview questions for the frontend\
  \ developers in detail. So, I have decided to decode most of the interview questions\
  \ that were available on the internet. \nThe purpose of this series is not just\
  \ to help you to clear MAANG interview, but help you become a fundamentally strong\
  \ frontEnd Engineer. Stay tuned and watch this entire series.\n\nFollow me on LinkedIn\
  \ -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\nGithub Repository that\
  \ contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nMedium Blog: https://mevasanth.medium.com/  \n\nInterview Preparation series :\
  \ https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation Series:\nhttps://www.youtube.com/watch?v=eGzErMUfdpk&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I"
author: careerwithvasanth
duration: 00:19:22
model: saaras:v3
transcript: true
---

# 90% of you will fail to answer this Facebook/Meta Interview question Pt-2 (MAANG series - 2)

## Transcript

### 00:00:00 · Speaker 1

putting other way. So how your mind should think is, so you have to form a sum or the result. The result should be of a type string. Only string can hold a very large character length, correct? So result is of string. You compute the sum in integer, you concatenate that to a string.

### 00:00:23 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Hassan. I hope you all doing well. As you know, this is a video series where we are discussing about most recent MANG interview question, where MANG refers to Meta, Apple, Amazon, Netflix and Google. And here, this is a part two of the question, where in the part one we have discussed a very, very important question. If you don't know what is the question,

### 00:00:43 · Speaker 2

is the one

### 00:00:52 · Speaker 2

So, in part one,

### 00:00:54 · Speaker 1

I have already explained what is the question and what are the sub elements required to solve that question, okay? Now this is a part two where we actually read the solution. So if you are someone who have not seen my previous video and directly landed in this video, then I would highly advise please go ahead and watch the previous video and come to this. The reason being all the technicalities of the question or all the crux of the question already explained in the previous video. Here we'll write only the code. So if you landed directly in this video, it will be slightly difficult for you to understand everything.

### 00:01:24 · Speaker 1

Okay? So the link I'll put somewhere on the screen also in the description section. Okay? So you already know the problem. So given a function where you pass two strings and that string could be a potential number. So you convert that into a number, add it to a number and return the result. Okay? That's what you have to do. So we have already seen what are the problems that happens with a very large numbers. So how to tackle that? So I there are a lot of solutions that are available on the web. Okay? I have picked one of the most easiest approach I think and with a most efficient solution. Okay? Obviously you may come

### 00:01:54 · Speaker 1

with some other solution which is efficient than me. If you if if you come so please do mention that in comment section. So I will try to link that in the video description also so that somebody get more benefited. So but whatever I know for the best when the time of this recording I am adding that solution here. So my solution is very very primitive solution, okay, which we did in our KGs or in the very primary schools. So where whenever you have to add two numbers something like this if you what you would have done is you would have added first these two numbers nine plus three twelve. So you would have

### 00:02:24 · Speaker 1

written two which is in the unit digit and you would have given carry as one correct which is in the tens digit you would add these two nine plus one and you will write ten which stands for one not two okay now

### 00:02:37 · Speaker 1

Whenever I write this solution, something should strike in your mind, okay? So what is striking in your mind? If you would have explained this to me, I would have got one sense that the problem with this whatever the question that is given to us is, we cannot add two very large numbers.

### 00:02:52 · Speaker 1

in the in the max safe integer we cannot add two large numbers. So but we can add two numbers at some digits. Correct? Two numbers at at once which will never form a number which is greater than eighteen. So nine plus below could be nine. Nine plus nine is eighteen which easily a number can hold. Correct? So that is the number one thought that would come to mind mind. So second thought which will not come to our mind but we have to think in the direction. So I'm just preparing you. See whenever you are adding here this is all the addition.

### 00:03:20 · Speaker 1

What happens below is kind of a concatenation if you observe carefully. Nine plus three is twelve, given a carry as one. Nine plus one is ten. So ten and two are concatenated if you observe carefully, correct? So, putting other way. So how your mind should think is, so you have to form a sum or the result. The result should be of a type string. Only string can hold a very large character length, correct? So result is of string. You compute the sum in integer, you

### 00:03:50 · Speaker 1

statinate that to a string. So this is a thought process. Correct? Hope you got the thought process. The reason I explain this is this is something that should come to your mind whenever you have been interviewed. Okay? Now, the second part.

### 00:04:04 · Speaker 1

is a is a basic division process. So this is not related to the concept, but I want you to know the difference between what the division operator does and what the modular operator does. Okay? Many of you would know, just quick revision. Sorry for my drawing, I'm not that expert, just I try to do something on the sketch. Okay? So if you divide eighteen by ten, so eighteen is on the top, ten is in the bottom. Okay? Then ten into one is ten and we get eight. So quotient is one, remainder is eight. So whenever you want the quotient,

### 00:04:34 · Speaker 1

you divide the number. Okay? So ten divided by eighteen will give you one. Whenever you want the remainder, which is eight. So ten modulus eighteen, or sorry, eighteen modulus ten will give you the eight as a remainder. I'm sorry. Yeah, ten modulus eighteen only will give you eight as a remainder. Okay, these are the two things that I wanted to tell you. In case if I missed here explaining something, I'll definitely explain that in the code again. So this is very essential for solving the problem. Okay? Now without wasting

### 00:05:04 · Speaker 1

for that time let's get started and coding. Okay? So same example I'm extending. Okay? So if some of you might noticed in the last example whenever I've written right? So there was something called nine nine nine nine nine nine I added one, correct? So it was the output was something like this. It followed by n. Some of you might have noticed Vasanth you did not explain that you were skipping something no. n basically refers to begin is created by appending n to the end of an integer literally ten n or by calling a functional begin. Basically here appending n at the

### 00:05:34 · Speaker 1

end refers to it has been a big int. That's it. Okay, nothing much. The number was not truncated or nothing happened, just n got added at the end. Okay. So, now without wasting further time, let's get started with the coding. Okay.

### 00:05:48 · Speaker 1

See, before I start the coding, I just have one call up. If you are someone who is seriously preparing for front end developer interview, I said this in my all videos. I know some of you might get annoyed, but my whole purpose of making this making this YouTube video series is to help someone to clear the interview, okay? So, I have created two beautiful series, one on most common JavaScript question and how to solve them, another on the custom implementation that are generally asked in the interview. So, both of them, I'll link that on the description also in the screen, okay? So, please go ahead and watch those videos and

### 00:06:18 · Speaker 1

come to this video. Unless you have seen those videos, technically you may not come to level this much of a difficulty in the interview because nobody will ask you to write this solution if you don't know what are the basics itself. So watch the series also and then this series, okay? Please do that so that it will be helpful for your interview, not just for the mag, any other interviews as well, okay? Now.

### 00:06:38 · Speaker 1

So, we have two numbers, number one and number two. Next, what I'll do is I have to get the length of the both the numbers. So number one length, okay? Is equal to number one dot length, okay? Then I will also do number two dot length, okay?

### 00:06:56 · Speaker 1

Why I'm doing this is I should be calculating the sum till the length of the biggest number. So in this case ninety nine, I should be calculate I should run the loop twice, correct? So whichever the number is maximum till that length I'll be running the loop, okay? Max length is equal to number one dot length. If it is greater than number two dot length, then we'll consider number one dot length as the maximum number, correct? If not, we'll consider number two dot length as the maximum. See I've come prepared

### 00:07:26 · Speaker 1

for this video, means I have written this solution couple of times to make sure I explain the things properly. But still there is a possibility I make a mistake. If I make a mistake, I'll try to correct that in the video itself so that you get benefited from the mistakes I do and do not repeat that in the interview. Okay? Now.

### 00:07:42 · Speaker 1

like you know there could be a carry carry is required correct? So where we will be we need to add the carry whenever there is a possibility of carry correct? And we can also create another variable called sum.

### 00:07:56 · Speaker 1

Okay, this is something that we will be concatenating. Remember the concatenation I said. Okay? Now I'll run the loop till the length of the uh max length, whatever the number that is big, I'll run the loop. There are solutions which convert a number in order where a top will be a bigger number and the bottom will be a smaller number. I have picked a generic approach. So whether you pass three comma ninety nine or ninety nine comma three, the solution works the same way. Okay? Now, here, I need to extract the last numbers, correct? So we can name it like last number one is equals to what I'll do is number one

### 00:08:32 · Speaker 1

dot care at

### 00:08:36 · Speaker 1

number one dot length minus i. Okay, don't worry, I'll explain this once again, okay? And last number two is equals to number two dot length, okay? I'll also explain why I'm putting a plus here, okay?

### 00:08:52 · Speaker 1

So now, before I go to the next step, let me quickly explain this. So this video is going to be slightly longer. It may take more seven or eight minutes where I'll be explaining all the things. So please stay tuned with me till the end. Do not skip any section because each and every point I explain is very, very important. Not from the Facebook point of view, point of view of you learning a concept very clearly, okay? So here, number one dot caret number one dot length minus I, okay? So let's say just take an example of ninety nine where you have to extract the last element, correct? So actually you shouldn't start the loop with I.

### 00:09:22 · Speaker 1

should start the loop with one. Okay, I'll explain why that as well and less than or equal to. So where number one dot length minus I, number one dot length is two in this case. Correct? So two minus I which is one. Two minus one is one. So if you see ninety nine, okay? So zero and one. Zero is the index and one is the index. So you want to extract the last index first. So number one dot length which is two. So two minus one is

### 00:09:49 · Speaker 1

one. Okay? So you get the last number. So next time it will become again I plus plus will become two. So two minus two which is zero. So that points to this nine. Okay? So we are starting with one and not with the zero. Okay? So now you got how to access the last numbers. So but we are trying to add three to here, correct? So we are trying to add three.

### 00:10:09 · Speaker 1

So three has a zero index. But three don't have the one index or the next index, correct? Which this number has. In that case, what will happen is if you try to extract the next index which doesn't exist. In that case, the caret, caret I guess most of you would know, we'll give a caret at a particular index that you're passing. In fact, we have also written a custom implementation for caret. I'll try to link that on the screen, also in the description. Please watch that video also which is very very useful, okay? So we have

### 00:10:39 · Speaker 1

So carrot will give in whenever we pass an index some empty string, just the empty string. So empty string with a unary plus will give you zero. Okay? So if there is no value in an index, adding zero doesn't hurt. So that is the purpose. So if you remember I showed you unary operator with a empty string in the first video. That is because of this. Okay? So now we got the last number one and last number two, okay? So then what I'll do, I'll calculate a temporary sum, okay? Let temporary sum is equal to

### 00:11:09 · Speaker 1

last num one, last num two plus the carry in case if carry exists, okay? Next, I'll write then I'll explain, don't worry, okay? So carry will be temp sum divided by ten, okay? If not it is gonna be a zero. Now temp sum is equals to temp sum mod ten, okay? Let me complete the code then I'll explain each and every step why I'm writing, okay? So if

### 00:11:38 · Speaker 1

I is equals to max length and there is a carry, okay?

### 00:11:44 · Speaker 1

will do some things. If it is not, then sum is equals to temp plus sum, okay? Otherwise, only thing that you do extra would be carry

### 00:11:57 · Speaker 1

star ten plus ten. See this is very very important code. Even a small misplacement will ruin your code. You will not get the expected output. Okay? So, finally you would return the sum. I'll explain the things step by step. Let's see whether at least it is working fine or not. Okay?

### 00:12:16 · Speaker 2

Hmm

### 00:12:19 · Speaker 1

Let's sum

### 00:12:21 · Speaker 1

sum is equals to ten plus sum what was the error? sum plus m. It's a good that there is some error first let me solve that then I'll explain this to you guys okay. There is no point explaining a wrong solution.

### 00:12:36 · Speaker 1

temp is not defined, I'm sorry. Most of you might have noticed and

### 00:12:41 · Speaker 1

wanting me to correct it. So I'm correcting it, okay?

### 00:12:45 · Speaker 1

So ten ninety nine plus three one hundred eight which is wrong. So I'm sorry here number two dot length. Okay. So if I run this one hundred two ninety nine plus three one hundred two which is correct. So maybe nine ninety nine plus one.

### 00:13:01 · Speaker 1

thousand

### 00:13:03 · Speaker 1

Let me just try all the combinations then we'll explain. Good. So it's working. Let's let's start with extreme basic numbers only, okay? Ninety nine plus one, then probably we'll go to the bigger numbers. So you know how till here, let me explain what is happening starting from here to here first. So we are calculating a temporary sum, that is temporary sum here refers to the sum of these two numbers, okay? The whatever the sum that you are currently calculating. So where in this case, the ninety nine, nine plus one, which was ten, correct? carry in the first place is zero, correct? So which which refers to temporary sum as

### 00:13:39 · Speaker 1

temporary sum as ten. Okay? Now, you already know what division returns and what modular returns, correct? So carry basically needs the tens digit, correct? So ten divided by ten which is one, correct? So which will be one, carry will be one in this case. What temp this one or whatever the sum we want to show here, like what we show here is the basically the remainder, correct? If you do the modulus operation, you would get this remainder. So what we have

### 00:14:09 · Speaker 1

is temp sum mod ten which will be zero. Correct? Remainder is nothing. Ten mod ten. Ten ones are ten. So remainder is zero. So temporary sum is zero here. Correct? So then what we'll do, technically if you look at this example, so not here, if you just look at here, ninety nine plus one, in the tens digit we'll have zero only. Correct? Nine plus one is ten and you will have a plus one here which will make it again ten. Correct? So which is as per the requirement how we are doing. Okay? So now we got the carry, carry

### 00:14:39 · Speaker 1

this case is one. temporary sum is again truncated into a value of zero. So sum is equal to temporary sum plus sum. Sum is an empty string here, correct? So temporary sum is zero. So zero plus an empty string is actually a zero in the form of a string, okay? So if you see zero plus, I don't know whether it will work here. uh here it is not working. So in the Chrome inspect somewhere if you see zero plus an empty string is going to be a uh empty zero in the string format. So you concatenated that value. So in the next

### 00:15:09 · Speaker 1

iteration, okay? You have ninety nine plus one, okay? Here it is one. Now you come to the next iteration where the element number one dot caret will point to this nine. Second number doesn't have a character at that length, so it will be a zero, okay? So here it is a zero.

### 00:15:29 · Speaker 1

Now

### 00:15:30 · Speaker 1

nine plus zero plus the carry carry was one if you remember correct so nine plus zero plus one which points to ten correct so carry is equal to ten divided by ten which is actually one again correct and temporary sum is temporary sum mod ten so ten mod ten again it is zero correct so right now the whatever the output we have is we have read the here if you come in the condition we are at the last correct so right now the sum is equals to before starting this

### 00:16:00 · Speaker 1

this one, zero and only zero is there. Okay? So temporary sum is also zero. So since we have read the last length and we do also have a carry, correct? So what is carry? Carry is one. So one star ten is ten, okay? Temporary sum is zero, correct? So temporary sum is zero. Sum is also zero, which are both this is in a string format of zero. So which will result in the value of hundred, okay? If in the last index there is no carry, then you would just add it. So there are

### 00:16:30 · Speaker 1

cases like probably twenty two plus forty four. Okay, four plus two is eight and four plus two is eighty eight. Okay, in that case there is no carry. Correct in the last step. So you don't have to multiply ten and form a number and add it. So we would right away get the sum itself which is sixty six. Okay, so this was the solution which I have picked somewhere on the web. I did not write the solution on my own. But I analyzed it and I break down it to multiple steps and I figured out an easiest approach for you to solve. Okay,

### 00:17:00 · Speaker 1

among the multiple solutions that I read in the internet. Okay? So, let me quickly reiterate and end this video. So, add two numbers, okay? In fact, before I reiterate quickly, if you like the content that I'm making on the YouTube, please do like my videos on the YouTube and follow me on Medium and do not forget to share these videos with your friends. Like the videos, okay? That all give me boost to make some more good content like this, okay? Yeah. Now add two numbers, we are passing two numbers. I will I will keep it very short.

### 00:17:30 · Speaker 1

we get the length. We pick the maximum length of the number because loop has to run till the length, okay? Then what we do we we always try to get the last numbers in the sequence, okay? And last number means keep incrementing. So first it will be four and two, next you will increment to the next numbers, okay? Then you add the numbers, see if there is a carry, if there is a carry you use it for the next elements to add, if there is no carry then by default carry will points to zero. And you will be concatenating the number

### 00:17:57 · Speaker 1

will be concatenating the number and the sum, whatever you have got, okay? So in this concatenation, so first is actually a number, temporary sum, correct? So temporary sum in this case is actually a will be a numerical value and this is string value. So whenever you add a numerical and a string value, it is a string concatenation, not a numerical concatenation, okay? So for example now one plus one in the double quotes will give you eleven, not two, okay? So that happens here, so that as per our explanation also here if you see, it should be a string concatenation and

### 00:18:27 · Speaker 1

the numerical concatenation. Numerical addition happens here. This is a string concatenation. So same is being performed here as well. Okay? Finally you are returning the sum. So this can take any number, any length number because at the end of the day you are just calculating two numbers whose maximum sum could be of eighteen, correct? So that's all about this video, okay? I'll copy this code and put in my GitHub repository. You can copy take the code from there and practice on your own. Try other solutions also on the web and try to come up with the solution that is most feasible for you, okay? And the this one.

### 00:18:57 · Speaker 1

Whatever the complexity of this algorithm is very straightforward. This is the length of the bigger number. It is N. Okay? So this could be according to me could this could be the easiest or the efficient approach that can be written. Okay? Now, if you like this video, please do like it on YouTube channel. Do not forget to subscribe to Uncommon Geeks. Share the videos with your friends so that they get motivated to learn these things because whenever it is asked in the big companies, they will also tend to learn it. Okay? So thank you again. Catch you in the next video.
