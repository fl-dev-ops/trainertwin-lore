---
id: '7445347791532457984'
date: '2026-04-02T05:54:01.374Z'
url: https://www.linkedin.com/posts/prathosh-a-p-50ab9511_machinelearning-speechrecognition-sanskrit-activity-7445347791532457984-mpui
likes: 924
comments: 88
images_count: 2
---

Namaste to All,


What happens when an IISc Professor rolls up his sleeves and becomes a full-stack developer?

You get a machine-learning solution to a 3,000-year-old oral tradition.

I spend my days teaching and researching Machine Learning at the Indian Institute of Science. But recently, I found myself diving deep into mobile UI states and gesture handlers to build VedaVaaNi - an ad-free educational tool for practicing the Krishna Yajur Veda. 

The goal was simple: build a smart, hands-free teleprompter that perfectly syncs ancient Sanskrit text to the audio during repetition. 

The engineering reality, however, was incredibly complex. When you feed a 5-minute continuous Vedic chant into standard acoustic models like Wav2Vec, standard CTC decoding completely breaks down:

1. The Drift: Conversational ASR expects natural pauses. Vedic chanting utilizes extreme temporal stretching (Pluta) and unbroken phonetic junctions (Sandhi). By the second minute, the alignment matrix loses its anchor.
2. The Tokenizer: Neural networks cannot comprehend Vedic 
Swaras (the precise mathematical tonal markers). Feeding rich, swara-annotated Devanagari into a tokenizer instantly shatters the alignment path.

The Full-Stack Pivot:

To fix this, I couldn't just theorize; I had to build the whole stack. 

On the backend, we dropped standard decoding. We stripped the complex text down to pure acoustics, extracted the raw emission probabilities, and used Dynamic Time Warping (DTW) to force a strictly monotonic path through the audio frames. 

On the frontend, I had to engineer a custom fluid-velocity scrolling algorithm. The UI calculates the exact time difference (Delta T) and physical pixel distance (Delta Y) between lines, continuously auto-scrolling the text anchored to the center of the screen—and gracefully pausing the math the exact millisecond a user touches the screen to scroll manually. 

The Result:

Today, I am thrilled to officially launch 

VedaVaaNi (v1.1) on the Play Store. It features the complete Krishna Yajur Veda and Rig Veda, synced with millisecond precision. 

This is rendered in 5 different scripts - Devanagari, Kannada, Telagu, Tamil and Roman. 

It is 100% free and ad-free. If you are interested in Indic linguistics, speech-to-text ML challenges, or just want to see what happens when a professor writes production code, I would love for you to try it out. 

🔗 Play Store Link: https://lnkd.in/gz-7qw7A


#MachineLearning #SpeechRecognition #Sanskrit #IndicTech #FullStack #IISc #VedaVaaNi #AppDevelopment
