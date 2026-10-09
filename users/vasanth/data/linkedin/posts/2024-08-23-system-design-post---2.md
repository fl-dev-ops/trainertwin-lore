---
id: '7232622275743604736'
date: '2024-08-23T05:38:46.161Z'
url: https://www.linkedin.com/posts/careerwithvasanth_system-design-post-2-lets-learn-the-intricacies-activity-7232622275743604736-ee1U
likes: 32
comments: 2
---

System design post - 2 Let's learn the intricacies of Type a head system (showing suggestion when you're typing).

**** How to efficiently make a API call:
-> Minimum 3 characters needs to be typed before making a call.
-> Limit unwanted calls with the help of Debouncing.

**** How to cache the search results ?
-> Store the result in the form of map (key as search string and value as array of results)
-> But, this will still consume more memory, what is the efficient approach instead of using maps? mention in comments section. 

**** How to kill the previous request
-> Let's say request 1 is made and the client hasn't received the result with the string "me". Meanwhile the user typed "men" and a second API call was made.
-> Now the result of the first API call will come first followed by a second request, in such a scenario we cannot show the result of the first API call for the current string.
-> We can solve the problem by passing the latest timestamp to the request and the server returns it and we will compare it with the local timestamp and if it is latest we will show the result on screen otherwise no.
-> There is a better approach than this, if you know it, mention it in the comments section.

Let me know, what other system design topics, you want me to write about ?

Follow me and I will help you to find your dream job: Vasanth Bhat
