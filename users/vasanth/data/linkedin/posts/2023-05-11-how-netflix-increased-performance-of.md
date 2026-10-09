---
id: '7062425772778524672'
date: '2023-05-11T13:58:37.756Z'
url: https://www.linkedin.com/posts/careerwithvasanth_netflix-netflix-loadbalancer-activity-7062425772778524672-rEnZ
likes: 121
comments: 4
---

How #netflix increased performance of the backend by client side load balancing ?? 
..
Building a load balancer is one of the common interview questions asked for both frontend and backend senior developer and architect roles. Lot of people still think load balancer means server side. Do you know there is a load balancer on the client side too and #netflix uses it ?

1. In simple words load balancer sits between the user and the server group and acts as an invisible facilitator, ensuring that all resource servers are used equally.

2. Problem is what if the load balancer itself is down ? then routing between different servers will be stopped. (Obviously there can be backup and other mechanisms to prevent it)

3. In client side load balancer Netflx uses its open source library Ribbon. With which client will know which all servers are available at that time and calls the right server. 

4. Client side load balancing offers reduced cost as the need for server-side load balancer goes away. Less network latency as the client can directly invoke the backend servers removing an extra hop for the load balancer.

Let me know what are the disadvantages of client side load balancing in the comments section. 

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview :Vasanth Bhat

#loadbalancer #loadbalancing #architecture #architect #server #clients #clientservice #frontend #developer #help
