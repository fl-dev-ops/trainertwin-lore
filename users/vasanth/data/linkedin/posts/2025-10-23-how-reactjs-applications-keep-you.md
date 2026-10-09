---
id: '7386995133507956736'
date: '2025-10-23T05:21:23.561Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-myntra-facebook-activity-7386995133507956736-PqvP
likes: 26
comments: 2
---

How #reactjs applications keep you always login ? 

1. You logged into websites like #myntra / #facebook and you will never logout right ?
2. There are usually 2 token approch. One short lived and other long lived. When short lived token expires, long lived token refeshes it. 

But, what happens when a long lived token also expires? 

Most common strategy is, with some periodicity you refresh that also to ensure it is not expiring. 

now answer what if the app is not opened for a long time ? where both tokens will expire ? how will system handle that ?
