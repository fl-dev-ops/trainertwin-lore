---
id: -PDQA3Q5w2E
title: JavaScript Pure Functions are not that easy (Pure Functions Ep - 1)
url: https://www.youtube.com/watch?v=-PDQA3Q5w2E
date: '2022-02-26'
duration: 00:07:54
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_1: null
  speaker_2: null
---


# JavaScript Pure Functions are not that easy (Pure Functions Ep - 1)


## Transcript

speaker_1: Hello all welcome to Uncommon Geeks myself Fasent I hope you all are doing well Todays topic is pure functions Pure function is considered to be one of the fundamental topic of all the programming language same as JavaScript Due to its simplicity many candidates tend to ignore this topic during the interview preparation Its a fact that pure functions are straightforward but there can be small variations of pure function that can be created that candidate tend to confuse during the interview and theyll not be able to answer it


this problem I pick the pure functions in my series and Ill be asking you all the possible questions that can be asked in the interview and how easily you can tackle it Ill guarantee you youll be thrilled to know the variation of pure functions that can be formed whether you are a beginner or a candidate who to take an interview and were unable to answer pure functions youll definitely enjoy this video series Thank you so much for watching lets get started

speaker_2: Let us understand what are pure functions with a simple example


So let me create a function function area of a rectangle it takes two arguments length and width


So what it returns is


length star width okay so basically quite straightforward whoever has read the geometry are fundamentally aware of this concept where area of a rectangle is length into width or breadth okay so now ill call this function from the outside so ill insert a log statement itself so area of rectangle im passing 10 into 20 okay so lets see what is the output there is nothing fancy here you will get 220 tensi is


200 20 into 10 is 200 so youre getting 200 okay so no matter how many time you invoke the function with passing the same set of arguments so youre getting same value as output okay if you change the value so 30 into 40 40 30 obviously the values are gonna change okay so but for the same given set of values the function will always return same value so no matter


many times you in call the area of rectangle with 10 and 20 youre always going to get the same same area okay so pure functions in very simple words we can tell this are those function


Those functions


that are deterministic in nature okay so these are the functions where you you can you can be so sure if i call this function this is the output that im gonna get so thats about the pure functions okay so the concept is same concept is straightforward you call a function and you anticipate an output and you always get the same output those are the pure functions in fact this is not specific to javascript in all the programming languages pure functions mean the same where


For those functions that are deterministic where if you pass the same set of values youre always gonna get the same set of values So always youre gonna return the same set of outputs Those are called as pure functions Okay So now there are obviously there is an opposite type to this And they are called impure functions And some places they are also called as not pure functions Okay Now both the terms exist in the industry People refer both Okay Lets see impure or the not pure functions


uh let us uh stick to some lets make it some test function ms test because we no longer calculate the area of our rectangle im making it test you pass the length and width okay what im doing here is const temp im creating a temporary variable what im doing here is im creating a mathematical mathrandom a random variable basically okay and im doing mathfloor ill explain why im doing that in a while


And let me know the same test again okay and what Im doing is along with the length and breadth Ill also start the temp


So let me call the same function again


Maybe lets call test where Ill pass 10 and 20


Let me execute this


So were getting zero okay Im executing this again


getting zero two times so what might be happening is uh temporary variable whatever is getting generated uh maybe lets multiply by 10 so that we get some higher number okay so basically whats happening here is uh before seeing the output let me explain the block of code whatever ive written so math dot random will generate a random number generally that number or by default that number will be in some decimals okay so 0 point 5 0 point 6 0 point 4 something like that so im just imagining


multiplying it into 10 so that it becomes a slightly a bigger number so 0 point 8 means it becomes 8 8 point 4 or something then Im doing a mathfloor here mathfloor and mathseal you might be already aware what it does is it will increase the value or decrease the value so for example if you have a value like 0 point 4 mathfloor okay lets make it 1 point 4 mathfloor if you pass this inside mathfloor it will become 1 if you if you pass it inside mathseal


as you notice to the top it will become 2 So this is what the mathfloor and mathceil functions do I am just using this because we get the whole number rather having the points in the decimals So you are invoking now and now we are invoking the same function twice here Same arguments are getting passed Let us see the output So once we got 1800 second time we are getting 1000 If I call third time again


So Im getting a different value 1000 1000 1000 400 So basically whats happening is 20 into 10 is same In all the cases length and length into width that 20 into 10 is happening same But the output that we are getting is different because of this temporary variable So now you yourself know impure functions impure functions those functions that are non deterministic in nature Okay So you will not be able to predict the output from a given function If youre invoking it youre not sure what value youre going to get It always varies


Okay so this this example looks vague Who is going to do like this This example is something that may not exist all the time Okay in industry we may not get such kind of example But think in in this way where you have some network call that you are making Okay so depending on what type of data youre getting sometimes you may not get a data Sometimes you may get a data and depending on the type of data youre getting youre gonna you are you will be rendering it So those are the actions that are non deterministic So youre not sure Lets say for example user X will get some set of data user Y will get some set of


data so whatever the data that you are getting may vary okay or user x may not get same set of data all the time so depending on his location he may get some offers and some location he may not get okay so what is the what will be returned from a function is non deterministic okay so this is a very important concept uh that is the reason im touching it here and there could be a lot of very interesting questions that can be asked in this simple concept this looks very straightforward and very simple but slightly tweaking it will make it a very complicated during the interview so those questions i


discussing in next video if you have liked my video please like it and if you if you if you want your friends also to learn from this video please share it with them also subscribe to our channel and in case you want me to make video on a particular topic please do mention that in the comment section ill make a video on that catch you in next video with very interesting questions on pure and impure functions thank you all
