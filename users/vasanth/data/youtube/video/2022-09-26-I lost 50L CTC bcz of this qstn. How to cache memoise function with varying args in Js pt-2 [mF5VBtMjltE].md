---
id: mF5VBtMjltE
title: I lost 50L CTC bcz of this qstn. How to cache/memoise function with varying
  args in Js pt-2
url: https://www.youtube.com/watch?v=mF5VBtMjltE
date: '2022-09-26'
duration: 00:00:56
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 1
speakers:
  speaker_0: Speaker 1
---

# I lost 50L CTC bcz of this qstn. How to cache/memoise function with varying args in Js pt-2


## Transcript

So first time you calculated 10 comma 20, what is the output? There was no necessary to compute the remaining three values, correct? You could have just stored the result of the previous computation and returned it, correct? So let's say you have another function called, I'm sorry, let's say you have another function called multiply. mult multiply that takes let's say three arguments number three number three and it will return multiplication of three arguments So now let's say you want to catch this as well, rather calling multiply with three arguments, let's say same function multiply with triggered with same set of arguments, 10, 20, and 30. You don't have to compute the value again. Earlier in my last video I had shown how you will cache the result of this add function and return the result if the arguments are matching but there is a argument so the results are matching you will return the same
