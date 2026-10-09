---
id: '7250130197998415872'
date: '2024-10-10T13:09:00.108Z'
url: https://www.linkedin.com/posts/careerwithvasanth_yingyang-html-css-activity-7250130197998415872-ERM2
likes: 43
comments: 0
images_count: 1
---

How to build #yingyang using #html and #css ? this question was recently asked on #meesho frontend developer interview. 

HTML:
<div class="yinyang"></div>

CSS:
body {
  display: flex;
  justify-content: center;
}

.yinyang {
  position: relative;
  background: #fff;
  height: 100px;
  border-color: #000;
  border-style: solid;
  width: 50px; 
  border-width: 2px 50px 2px 2px;
  border-radius: 50%;
  animation: roll 40000s infinite;
} 

.yinyang:before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  background: #fff;
  border: 18px solid #000;
  border-radius: 50%;
  width: 14px;
  height: 14px;
  }


.yinyang:after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  background: #000;
  border: 18px solid #fff;
  border-radius: 50%;
  width: 14px;
  height: 14px;
}


@keyframes roll {
  from {
    transform:rotate(0deg);
  }
  to {
    transform:rotate(3600000deg);
  }
}

let me know what is the significance of Ying Yong in the comments section.

follow me and I will help you to find your dream job: Vasanth Bhat
