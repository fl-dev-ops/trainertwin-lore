---
id: '6970032077337436161'
date: '2022-08-29T14:59:04.171Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontenddeveloper-reactjs-interview-activity-6970032077337436161-zYXy
likes: 41
comments: 3
---

Writing custom implementation for Flattening an array is one of the overrated frontEnd developer interview question. It is most commonly asked in ReactJS/JS interview rounds. Not sure, why people still think it is difficult. For those of you, who don't know what is flattening an array and how to flatten it, here is the basic information. 

Question 1. 
What is Array.flat method ??

Answer : 
The flat() method creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.

Question 2:
Can you write custom implementation for the same. 

Answer: 
It's very simple recursive code to write custom Array.flat method for completely flattening the nested array.  

Below is the code: 

let output = []
function flattenArray(arr){
        for (let i = 0; i < arr.length; i++) {
            if(Array.isArray(arr[i])){
                flattenArray(arr[i]);
            }else{
                output.push(arr[i]);
            }
        }
        return output;
 }

Question 3: 
Can you write non-recursive solution for the same ? 
Answer: 
Many get confused here as recursive solution is very popular. I tried explaining all the above concepts along with recursive and non-recursive approach in my Youtube video (Uncommon Geeks channel). Link to video is in the description. Please watch the video and share your feedback. 

In case if you have not followed me, you can do it here, I will help you to clear your frontEnd developer interview : Vasanth Bhat

#frontenddeveloper #reactjs #interview #javascript #uncommonGeeks
