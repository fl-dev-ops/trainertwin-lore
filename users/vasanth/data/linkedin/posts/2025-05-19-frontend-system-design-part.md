---
id: '7330110315256274944'
date: '2025-05-19T06:01:26.021Z'
url: https://www.linkedin.com/posts/careerwithvasanth_bookmyshow-activity-7330110315256274944-i-SA
likes: 57
comments: 11
---

Frontend system design part - 16 

Question: When 2 people try to book the same seat in ticket booking applications like #bookmyshow how does it handle?

answer: 

Optimistic approch: Let all the users go till the last step and whoever pays first, they will get the booking confirmation.

Pessimistic approach: Lock the seat for pre-defined duration (ideally 10 minutes) for the first person who selects the seat and goes to the next screen. After 15 minutes if booking do not happen, that seat will be freed up. 

there is another approach, if you know that, mention it in the comments section.

follow me and I will help you to find your dream job: Vasanth Bhat
