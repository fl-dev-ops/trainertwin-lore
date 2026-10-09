---
id: '7440636950589612032'
date: '2026-03-20T05:54:49.370Z'
url: https://www.linkedin.com/posts/prathosh-a-p-50ab9511_buildinpublic-ai-ios-activity-7440636950589612032-2Kfo
likes: 448
comments: 24
images_count: 1
---

I have been teaching the math of building models for quite some time now.

It was time to make my hands dirty seeing them in action - I started vibe building :) 

I spent last evening building DinoBuddy - an interactive T-Rex companion app for young children that listens, thinks, and talks back in real time. No buttons. No typing. Just a kid having a conversation with a dinosaur.    This is for my 4-year-old son. 

Here is the tech stack that went in: 
          
Platform: Swift + SwiftUI with an MVVM architecture. 
Custom Animations: Procedural T-Rex built natively in SwiftUI Canvas (state-driven, zero external animation libraries). 
Audio Input: AVAudioEngine natively capturing audio, with AVAudioConverter resampling to 16kHz on the fly. 
Local Edge AI: A Python subprocess daemon running Silero VAD (PyTorch) to process 32ms chunks and trigger Apple SpeechKit (on-device ASR) when the user stops speaking. 
LLM: Anthropic Claude Haiku 4.5 (via raw REST/URLSession) for fast, child-friendly conversational logic. 
 TTS: ElevenLabs for lightning-fast voice generation.    

Could do this entire thing in less than an hour, and my son started enjoying it.

Agentic AI just turned a Mathy IISc Prof who is rusty in programming into a full-stack AI-rockstar in just 30 minutes - what a time to be alive 

  #BuildInPublic #AI #iOS #Swift #SwiftUI #Anthropic #Claude #ElevenLabs #VoiceAI #ChildTech #IndieHacker
