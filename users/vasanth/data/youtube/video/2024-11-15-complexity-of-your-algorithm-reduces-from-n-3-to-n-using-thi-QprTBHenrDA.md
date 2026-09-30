---
id: QprTBHenrDA
title: 'Complexity of your algorithm reduces from n^3 to n using this technique |
  Two pointer approach #dsa'
date: '2024-11-15'
url: https://www.youtube.com/watch?v=QprTBHenrDA
description: "#dsa #datastructures #algorithm #javascript #typescript \n\n@careerwithvasanth\
  \   is a Youtube channel dedicated to helping candidates clear their interview.\
  \ There are more than 150 videos and new videos will be uploaded every week. If\
  \ you're seriously preparing for interviews and looking for tips and tricks, please\
  \ subscribe to my channel and press the bell icon.\n\nIn this Video I have explained\
  \ and important DSA problem solving technique known as \"Two pointer approach\"\
  \ using #javascript.  Must watch video if you're looking for DSA as a frontend developer.\
  \ \n\nYou can get more mock interviews here : https://www.youtube.com/playlist?list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD\n\
  \nTo get a dedicated one on one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\
  \nJoin CareerwithVasanth community to discuss with other developers: t.me/uncommongeek.\
  \ \n\nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\n\
  Medium Blog https://mevasanth.medium.com/  \n\n\U0001F449 “Contact on WhatsApp:\
  \ 9731039408”\n\nJavaScript Interview preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:08:43
model: saaras:v3
transcript: true
---

# Complexity of your algorithm reduces from n^3 to n using this technique | Two pointer approach #dsa

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to the Career with Vasant YouTube channel. My name is Vasant. I hope you all doing well. I'm back with another new DSA topic. Without wasting further time, let's get started. The topic is two-pointed approach, okay? In that video also, I mentioned you there are two different ways to look at the DSA problems. One is like you keep solving the various different data structure problems. Like for example, you solve array problem, link list problem, trees problem and goes on. The another way to look at the DSA is there are few techniques in data structure algorithm problem solving. Like there are techniques like two-point

### 00:00:30 · Speaker 1

sliding window and multiple other techniques are there where you pick those techniques and solve problems from all the data structures within that. Okay, for example, you pick a sliding window and you solve sliding window related questions in arrays, strings, linked list, trees, etcetera. Okay. See, the second technique of solving problem is useful for those who already know very well about a data structure, like you should know how to traverse a tree first. Without that if you pick a problem just with the help of technique, it's not gonna work. Okay. Now let's understand

### 00:01:00 · Speaker 1

more about this technique by looking at a problem, okay? So in a sorted array, find a pair exist with a given sum, yes. So const array is two, six, five, eight, eleven. So this is an array and we have n as five, which is the length of the array and target is fourteen. Give a pair of numbers. See, in a sorted array, this is very important. In a sorted array, find a pair that exist with a given sum. Like for example, two plus six, will it make fourteen? No. eleven plus two, will it make fourteen? No. six plus five, will it make fourteen? No. eight plus six, will it

### 00:01:06 · Speaker 0

Silk

### 00:01:30 · Speaker 1

make fourteen yes. So eight and six will make the fourteen. So definitely similar questions you might have studied during your graduation. And the easiest solution to solve this problem is writing a function. Function pair exist array n and s so we use two for loops. The first for loop is where starting with the zeroth index second for loop is where starts with the zero plus one index. So where for two we add six and see will it produce some six we then we see two plus five two plus eight two plus one two plus eleven one iteration over and then for six again we are going to check six plus

### 00:02:00 · Speaker 1

six plus eight, six plus eleven. So, most of you who might have looked at this solution would know that complexity of this, that is the complexity of this approach is the n squared. Because there's an outer for loop, there's an inner for loop that is n squared. Correct? So just to tell whether the particular pair exists or not, we need to process the array two times. Okay?

### 00:02:17 · Speaker 0

Now, so this is

### 00:02:19 · Speaker 1

one way of solving the problem what we call a brute force way of solving. There is a better way of solving the problem as the array is sorted. Okay. So that particular technique that we are here we are using is a two pointer approach. Okay. So this is an example in sorted array find the pair with the given sum is where we are going to determine how two pointer approach is basically help us to save the time complexity. But before that let's understand what is a two pointer technique. Two pointer technique allows us to keep two pointers referencing two different location

### 00:02:49 · Speaker 1

you know, different data structures like array linked list, etcetera. Okay? So basically, instead of having one pointer pointing to one particular location in the array or different data structures,

### 00:02:59 · Speaker 1

We are using two pointers pointing to two distinct locations within the data structure for simplicity purpose let's assume array in two different locations so that the processing becomes much faster. By looking at the diagram only by now you might have understood. As the array is sorted here. Two six five eight eleven. Correct? How about I keep one pointer here and one pointer here.

### 00:03:20 · Speaker 1

And I keep adding like eleven plus two, is it producing the sum? No. Then I'll move the position to I position to here and probably the J position to here and then I'll add. So the second iteration itself, I got the value. So instead of n square, it become n. Let me show you. You got a code as well, okay? So what we are doing, if while I is less than J, so here I is pointing to the starting location. The J is pointing to the ending location, okay? n minus one as you can see. While I less

### 00:03:24 · Speaker 0

No

### 00:03:50 · Speaker 1

less than j. Current sum is array of i plus array of j. That is nothing but let's say I copy this for paste here. So first it is two plus eleven which is eleven plus two which is thirteen. Okay? So we have a check. If it is sum then we are going to return true. If it is lesser than sum then we are incrementing i. That means sum is less. So then we are incrementing the i-th indicator from two we are going here. If sum is like sum is

### 00:04:20 · Speaker 1

more than the given sum like for example, uh array of I plus array of J if it is greater than the current sum, then we have to reduce this pointer. The reason being if I increase this pointer as it is already sorted array, if I move further towards the right, then basically I'm gonna increase the value which is not expected, correct? So whenever the value is increasing or give whenever the sum of two numbers is greater than the target, then we are gonna reduce this. Whenever it is lesser, then we are gonna increment this, okay? That's how it's gonna work. work

### 00:04:52 · Speaker 1

as you can see, when the current sum is equal to sum written true, when current sum is lesser than S, then you are going to increment I plus plus. When current sum is greater than the S, then you are going to do the J minus minus. So whenever the value is higher, like whatever the sum is higher than the target sum, so reduce this. Whenever the target sum is lesser, then basically increment this, so that you are going to produce get a higher sum. Okay? So as simple as that, it's not about primarily understanding the code here, it's about understanding the technique. Instead of like one pointer, you are having two pointers.

### 00:05:22 · Speaker 1

two different locations in the array and you would be incrementing this pointer and you would be decrementing this pointer to get the given sum. So this is two pointer approach how we can how we can save the time complexity. Okay from n square this approach is just n. Let's look at another example of space complexity quickly. So given an array reverse it. Very simple. So how you are gonna reverse so basically you are gonna take the another array and you are gonna iterate i is equal to zero i less than n i plus plus. So n minus i minus one this is one approach or you can iterate the array

### 00:05:28 · Speaker 0

So

### 00:05:52 · Speaker 1

like I is equal to n minus one I greater than zero I minus minus and you're going to put the like reversed value into the reversed array. Like instead of like you take the same array keep the Ith index here and keep adding the values into the reversed array. Okay? The only problem here is you are having another space like another array correct? So space complexity of this algorithm is n. Like imagine a case where this array has one million items. So for reversing one million item if you have to create another array of one million item then you're going to taking a massive

### 00:06:22 · Speaker 1

space. Okay? So which should be ideally avoided. Now we'll come here. Two pointer approach, what we are doing? You can also think actually. We have two pointers. One pointer I keep here, another pointer I keep here. Swap the values of the two pointer. Increment decrement this, increment this. And again swap these two values. Whenever we hit the middle, stop it. As simple as that. Okay? So where same is done here. I is equal to zero, J is equal to n minus one, I less than J, array of I, array of J, array of J, array of I. You do they like we no longer need to

### 00:06:52 · Speaker 1

the way of using a temp variable to swap the values with the help of this sort of an expression we can swap the elements at one go okay I plus plus J minus minus when I is less than J I is less than J so no matter whether it's a even array or R array or even array or odd number of elements in the array whenever the I crosses the J it is assumed to be like we crossed all the elements okay so instead of like using the n square instead of using the n space we just able to do within the one space that is within the given array

### 00:07:22 · Speaker 1

only we are able to reverse the array, okay? So this is about the two pointer approach. So again one last time if I have to iterate, instead of using one pointer or one direction of iteration, use two diff multi whenever there is a possibility of using a distinct location to start and end and we can start the processing, that's when we are gonna use the two pointer approach. And especially keep in mind whenever there is array sorted or where the string sort of an example where string is with the sorted, whenever the sorted comes, think of this

### 00:07:52 · Speaker 1

kind of an approach. There are slightly advanced version of this called one. So the fast pointer and slow pointer also approach that we use in the link list. I'm going to explain that in the upcoming videos. That's all for this video. If you like the video, please like. Whatever you felt honestly, please comment. Share the video with your friends so that they also get benefited. My intention is to bring as much more content as possible with in DSA for front end developers for free. That's the whole intent. So I'm making more and more videos. If you want any specific videos, please do mention that in the comment section. My last two videos regarding a strategy and how to

### 00:08:22 · Speaker 1

Google DSA has got quite good viewership. Please do watch the videos. So link to that in this that particular videos are in this playlist only. And I write very actively on LinkedIn about front end interview preparation. Please do follow me. I have a Telegram group of 3200 plus members where a community of developers sharing knowledge and sharing job related information. Please do join. Thank you so much for watching. Catch you in the next video.
