---
id: '7228995891846639617'
date: '2024-08-13T05:28:48.865Z'
url: https://www.linkedin.com/posts/careerwithvasanth_let-me-discuss-an-important-react-re-rendering-activity-7228995891846639617-GmoD
likes: 47
comments: 8
---

Let me discuss an important React re-rendering process today. Let's take an example of simple react snippet. 

#######################################################
...
function test() {
     try{
          setIsLoading(true);
          setIsError(false);
          const response = await makeAPICall();
          setResponse(response.data)
   } catch(error){
        setIsError(true);
        setIsLoading(false);
    }
}
...
#######################################################

Now in this simple block of code when will React start setting states ?  Common answer is at the end of the function. If setting state happens at end of the function 

1. Then how is the loading state presented first before making an API call ?
2. If setState is asynchronous why does it never happens where loading becomes true after making the call ? or any other task ? Why does setState always execute in the sequential order ?

Put your answer and explanation in the comments section. 

follow me and I will help you to find your dream job: Vasanth Bhat
