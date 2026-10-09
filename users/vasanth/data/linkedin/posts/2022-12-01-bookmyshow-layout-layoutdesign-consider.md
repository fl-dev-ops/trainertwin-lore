---
id: '7003955428808146945'
date: '2022-12-01T05:38:21.427Z'
url: https://www.linkedin.com/posts/careerwithvasanth_bookmyshow-layout-layoutdesign-activity-7003955428808146945-Apme
likes: 20
comments: 1
images_count: 1
---

#bookmyshow #layout #layoutdesign consider the example below which shows layouts of 3 different theatres. How do you think applications like #bookmyshow render such dynamic layouts ?

Approach 1 (Not recommended):
Backend will send the rows and columns information and the client will populate the layouts. But this approach is not scalable, considering the diversity of layouts.

Approach 2 (Recommended):
Backend sends details of each seat with rows and column information. With details of each seat being booked or not. It also sends some value that corresponds to gaps in between the seats.

Ex: A1, A2, A3, A00, A00, A00 - when client encounters A00 it will not draw seats for those rows, for the remaining, seats are added on client.

I have tried explaining it very much in detail in #youtubechannel #uncommonGeeks. Link to the video is in the comment section. Please watch it and share your feedback.

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview : Vasanth Bhat

#systemdesign #interview #softwaredeveloper #frontenddevelopment #frontend #frontenddeveloper #frontenddev
