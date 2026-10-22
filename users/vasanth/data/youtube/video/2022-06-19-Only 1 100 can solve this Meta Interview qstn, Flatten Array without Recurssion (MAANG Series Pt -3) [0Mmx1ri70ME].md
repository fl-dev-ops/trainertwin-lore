---
id: 0Mmx1ri70ME
title: Only 1/100 can solve this Meta Interview qstn, Flatten Array without Recurssion
  (MAANG Series Pt -3)
url: https://www.youtube.com/watch?v=0Mmx1ri70ME
date: '2022-06-19'
duration: 00:10:18
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_1: null
  speaker_2: null
---

speaker_1: So today I have picked up a question which is asked in Facebook or Facebook or Meta Amazon Apple Google also in Microsoft Okay five companies have asked this Dont think it is very old Even in last April 2022 April also they have asked this question

speaker_2: Hi all welcome back to uncommon geeks myself Vasanth I hope you all doing well

speaker_1: So as you already know this is a video series where we are discussing about the most common interview questions that are asked in MANG MANG stands for Meta or Facebook Apple Amazon Netflix and Google Okay So today I have picked up a question which is asked in Facebook or Facebook or Meta Amazon Apple Google also in Microsoft Okay Five companies have asked this Dont think it is very old Even in last April 2022 April also they have asked this question Okay So its not I have already discussed


solution to this question in different ways in my articles and also in one of my video but in this particular video I am gonna give a all altogether different approach towards that problem this is very very important video if you are preparing for man interviews please watch this video till the end okay without wasting further time lets get started


This video is mainly on flattening the array in JavaScript Okay so in my medium blog Ive already written a beautiful article to explain how to flatten a given array in JavaScript Okay so to be very precise if given this as an input 1 2 3 4 5 6 7 which is a nested array or array of array so you should flatten it Thats the requirement Okay Ive written a recursive solution here In my previous video where I have explained a custom implementation of arrayflat even there I have written a recursive approach itself


In Facebook interviews they have asked both solutions like an iterative solution also a recursive solution Okay So in this video Ill be discussing the iterative approach So in same interview for the same candidate theyll ask both approaches to it The reason being how many different solutions that you can come up for a single problem Okay Thats very very important when youre applying for companies like this Okay Let me start by explaining you the flat first So it is here as you can see So if you run so this three comma four


away if you dont pass anything inside the flat it is considered as zero hierarchy okay so one level of hierarchy it will remove not zero hierarchy one hierarchy one array inside of this array will be removed one level of hierarchy if you pass infinity then it will remove all the hierarchy no matter how many array inside an array it will remove all the arrays and it will just make sure the entire array is flattened okay so this is about the array dot flat


And what recursive approach for this Ive already shown you here how we can write a recursive approach So there is also iterative approach which Ive taken from here Okay I have not written this logic Ive taken this logic from here itself I assume if it is documented here this could have gone through a lot of iterations and best minds of the world might have approved this So I am also picking the same and Ill be explaining you how to do that Okay Ill link this also in the description so that you can go ahead and read by yourself as well Okay Also my blog where Ive explained the


approach very clearly also ill link my youtube video where ive explained the recursive approach now without wasting further time lets get started but before i start writing the any code for the flattening if you are someone who is seriously preparing for javascript related interviews like vue angular node react etc so i would highly advise you to go ahead and watch my basic interview questions so ive linked that on the screen also in the description so 20 plus videos which are most commonly asked across all the companies okay and how to


approach that problem what mistakes can they do how to avoid that all of that ive explained the series if you dont watch that and directly landed here the problem is this is advanced level questions so companies like manga are asking it correct so if you are not watching that and directly landed in this video problem is you may not go to to this level only in the interview because every interview starts the basic question if you are answering the basic he would go for the advanced if you are not answering basic question itself then there is no point correct so watch that series and come to this video okay also i have created another video series from the


Custom implementation

speaker_2: So how to write your

speaker_1: own array dot map method array dot flat method array dot concat all of this okay so please watch that series also that has become very very trendy question across all the high paying jobs now implement your own functions watch that series also and come to this as a next level of further preparations okay now without wasting further time now lets get started so crux of the logic ill explain first so you have an array a nested array


1 2 3 comma 4 okay so 3 comma 4 is a nested array


the entire array what you would do is you will get the last element of this okay by just array dot


Okay arraypop would give you the last element correct So you can log last Then what you would do is you will push that value push that array back into the source array but without using the array brackets So how you do that is arraypush you will just spread the last


What this does is three comma four will turn into three comma four


the array bracket will be eliminated due to which the output will be if you log it now array it will be 1 comma 2 comma 3 comma 4


that array bracket will be gone So this is the crux of the logic So what you would do is you will take the last element and insert it back to the array if it is an array If it is not an array in the case of 1 and 2 it is not an array then just push this values into a result Okay Let me run this So you are seeing 3 4 was the last correct this was the last


one two three four is the array that is the final output so this is the crux okay first you should always try to find out the crux or a repeating pattern in the question with which you can form a solution so now you know the crux with this logic you will be implementing the actual implementation okay so I dont need these so Im removing I would need this the two statements Ill Ill keep them okay function now Ill create flatten array flatten array is


my function okay which will take input as the input array so I would call flatten array from this log okay what I would do is Im using a variable called stack actually its a stack based approach only stack I think most of you know first in last out okay arranging of plates you pick the last plate in the first


reason a spread operator okay so here usage of spread operator is because not because of anything any significant reason it is mainly because this input is used uh not to use the same reference of this array okay they want to use a different array reference here so youre using dot dot dot input here okay as array passed always arrays passed as a reference and not by value okay now now its very simple what you would do is you also need an a variable to hold the output cons response is this okay then


Then you have a while loop inside which you will check and you will run this till stack is not empty


Then what you do is very simple same like you will get the last element from the stack by using the stack dot pop


two two things are possible one array is one one the last value is an array second last value is not an array correct so if


And else see I have practiced this solution before giving explaining you guys But otherwise also I will have a solid bifurcation of the problem correct So first I know the crux Then I know what are the major two conditions If this condition what I do this condition what Ill do An algorithm should think algorithm should run in your mind Then only you will be able to write an efficient code okay So please do follow in this direction whenever you are thinking in the interview Now if first you need to check whether last element is an array


So you know arrayezarray method is available which will help you to identify that So Im passing last here


So if it is not an array in this case 1 and 2 are not an array you can directly push it into the result correct result dot push you are pushing the array of sorry you are pushing the last value correct if it is an array then also you know by the crux what you need to do correct you will push the value back into the stack only thing is you will extract it only thing is you will use a dot operator just to get the remove that array brackets spread operator you will use to get the values out of the array okay


Then you have to return the result Only thing that you have to make a change here is you have to reverse the return The reason being you are popping the values putting other way you are iterating the array from the last So you have to reverse it and you have to send it as a response Okay First let us run then well see what is happening So 3 4 is happening Lets say I put 5 here


So it is flattening Okay So thats about the crux of the logic and how to flatten the array in a iterative approach Okay So so was and why you pop Can we now do this by using the first like rather using the last element Cant we use from the first element Obviously you can do that also Like you would start iterating from this keep pushing the values Then whenever an array is encountered then you can you can follow the similar approach Even that is also possible Okay Im just sticking to the Mozilla approach considering that could be the best


approach possible okay so if you like the content that i have made in this video please do like this video on youtube channel do not forget to share the videos with your friends and please do subscribe to my channel uncommon geeks that will help me to make more such good content i also link my medium blog this in this video link in the description please do subscribe to please do follow me on the medium as well okay ill be putting the solution in my github repository you can copy that and practice on your own okay thank you again for watching this video catch you in the next one
