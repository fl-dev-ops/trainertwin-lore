---
id: '7236376407495360512'
date: '2024-09-02T14:16:20.919Z'
url: https://www.linkedin.com/posts/careerwithvasanth_gmail-activity-7236376407495360512-vrMC
likes: 41
comments: 2
---

System design part -4 #gmail has millions of emails, how does it verifies an email id is valid I'd or not ? I spent an hour reading this and here are my findings.

1. Blooom filter: When and email is added to system, a hash is formed and stored in a set.  Next time this will be used to tell whether an email id is present in the system or not without extracting actual information. 

2. Trie based approach: Where email id is stored character by character and each node represents a character. Searching an email is achieved by traversing the tree until a mismatch happens.

3. Hashmap: Special hashing techniques like consistent hashing can be implemented to store the email id. Where data can be accessed with lowest time complexity. 

4. Cuckoo filters: An extension to bloom filters helps to identify the valid email id very quickly and works better in case of false negatives.

which technique does Gmail uses ? it is a combination of above and optimisation techniques like sharading, indexing etc. Let me know, if your aware of any better techniques. 

Follow me and I will help you to find your dream job: Vasanth Bhat
