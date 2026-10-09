---
id: '7449874472528134145'
date: '2026-04-14T17:41:26.225Z'
url: https://www.linkedin.com/posts/prathosh-a-p-50ab9511_deeplearning-generativeai-diffusionmodels-activity-7449874472528134145-lnJe
likes: 378
comments: 8
images_count: 2
---

Fine-tuning Diffusion Models to fix their output biases is computationally expensive. What if we could fix the math directly at inference time, with zero additional training?

I am happy to announce that our new paper solving this exact problem has just been accepted at Transactions on Machine Learning Research (TMLR).

But on a much more personal note, this marks a massive milestone: This is the 5th top-tier paper acceptance for my first PhD student, Piyush Tiwary Piyush Tiwary at the Indian Institute of Science (IISc) Indian Institute of Science (IISc). With this acceptance, every single chapter of his doctoral thesis has now been published in top-tier venues. Watching his growth as a researcher has been an absolute privilege.

Here is a breakdown of what we built:

As Diffusion Models scale, they inherit and amplify societal biases (gender, race, community). The industry standard for debiasing requires auxiliary classifiers, new reference data, or expensive fine-tuning. We proved you don't need any of that.

We introduced a training-free, inference-time method for debiasing DMs:
The Root Cause: We theoretically show that the unconditional score predicted by the denoiser acts as a convex combination of conditional scores. 

Underrepresented attributes simply get mathematically starved of weight, allowing other attributes to dominate the overall score function.

The Fix: We built a score-guidance method that forces the generation to adhere to a user-provided reference distribution strictly at inference time.

Multimodal Execution: To our knowledge, this is the first debiasing framework that can utilize different modalities. You can steer the distribution using either text prompts or just 'exemplar images'.

It works out-of-the-box across various attributes on both unconditional and conditional models, including Stable Diffusion.

Massive congratulations again to Piyush on a stellar PhD journey.  

My Masters student Prabhav, Prabhav Verma contributed significantly to this work. Congratulations to both. 

Stop burning GPU hours to debias models, and fix the math at inference instead.

📄 Read the full paper here: https://lnkd.in/gfBpSyqc
 Code available here: https://lnkd.in/giCJhym4
#DeepLearning #GenerativeAI #DiffusionModels #MachineLearning #IISc #Research #PhD

EECS @ IISc, Bengaluru
