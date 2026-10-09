---
id: '7432475691897470976'
date: '2026-02-25T17:24:53.669Z'
url: https://www.linkedin.com/posts/prathosh-a-p-50ab9511_fineiclr-activity-7432475691897470976-PnRY
likes: 314
comments: 13
document:
  title: fINE_ICLR
---

Hello All, 

 Have you ever wondered why AI "explainability" fails when you hit 'Retrain'?

If you’ve ever used Influence Functions or Data Attribution to debug a model, you’ve likely hit the wall of Instability. 

The same training sample might appear "critical" in one run and "irrelevant" in the next, simply due to a change in the random seed. If our debugging tools are volatile, how can we ever trust them for data curation or safety?

This is the exact question we take up in our latest work, "f-INE: A Hypothesis Testing Framework for Estimating Influence under Training Randomness," that has been accepted to  #ICLR2026 (A premier A* confrence in AI)

The Problem: Existing influence methods (TRAK, TraceIn, etc.) collapse under training randomness. They provide a deterministic answer to a non-deterministic process.

The Solution: We move away from point-estimates and ground influence estimation in Hypothesis Testing. Our framework, f-INE , explicitly accounts for training randomness to provide Reliable Influence Estimation.

Here are some salient points - 


🔹We’ve established a mathematically rigorous framework (f-influence) that is stable across seeds and requires only a single training run.

🔹 We scaled this to Llama-3.1-8B. We demonstrate that f-INE can reliably detect poisoned samples in instruction-tuning data, a critical step for Reliability in LLMs and AI Safety.

This work is a testament to the synergy between deep academic rigor and industrial scale, born out of a fantastic collaboration between IISc Indian Institute of Science (IISc) Institute of Science (IISc), LatentForce.ai LatentForce, University of Southern California University of Southern California, and Washington University Washington University in St. Louis. A group having interns, PhD students and faculty members. 

Congratulations to the team: Subhodip PandaSubhodip Panda Dhruv Tarsadiya Dhruv Tarsadiya, Shashwat Sourav and Sai Praneeth Karimireddy.

The paper attached for the interested readers. 

EECS @ IISc, Bengaluru Indian Institute of Science (IISc) Institute of Science - IISc Department of ECE, IISc. 

#MachineLearning #ICLR2026 #LLM #AISafety #Interpretability #DeepLearning #IISc #LatentForce #ReliabilityInAI

### Shared Document: [fINE_ICLR]()

