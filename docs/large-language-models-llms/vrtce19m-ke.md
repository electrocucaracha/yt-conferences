---
layout: default
title:
  Stanford Webinar - Large Language Models Get the Hype, but Compound Systems
  Are the Future of AI
nav_order: 17
parent: Large Language Models Llms
type: Video Note
description:
  The speaker emphasizes that while large language models (LLMs) receive
  most of the attention in AI, real progress and practical deployment rely on viewing
  AI as compound systems—integrations of models, prompts, sampling methods, and externa...
resource: https://www.youtube.com/watch?v=vRTcE19M-KE
tags:
  - large-language-models-llms
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker emphasizes that while large language models (LLMs) receive most of the attention in AI, real progress and practical deployment rely on viewing AI as compound systems—integrations of models, prompts, sampling methods, and external tools.
The talk traces the evolution from focusing solely on model size and capabilities (as seen in GPT-3, PaLM, and Gemini) to recognizing that the true power and behavior of AI emerge from how these models are embedded within broader systems.
Key system components, such as prompting strategies and sampling methods, are shown to have significant, sometimes surprising, effects on performance, often outweighing the impact of model size alone.
The speaker advocates for a shift in both research and regulation from evaluating and governing models in isolation to considering entire systems, arguing that small models in well-designed systems can outperform large models in simplistic setups, and that risks and benefits are determined by system-level interactions.
The talk introduces the DSPy library as a tool for principled, modular AI system design and optimization, and concludes by urging the community to adopt a systems-thinking mindset for future AI development, deployment, and governance.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Large language models (LLMs) receive most of the attention, but real-world AI involves compound systems.                                                |
|   2 | The trend of focusing on models began with the GPT-3 paper, which highlighted scaling as a driver of new capabilities.                                  |
|   3 | Announcements from Google (PaLM, Gemini) and OpenAI (ChatGPT, GPT-4o) center on models, but these are actually systems.                                 |
|   4 | Headlines and social media reinforce model-centric thinking, but in practice, we interact with systems.                                                 |
|   5 | A model alone is inert; to function, it requires at least a prompt and a sampling method—together forming a minimal system.                             |
|   6 | Modern systems often integrate LLMs with tools like calculators, databases, and web APIs, making the model just one component.                          |
|   7 | Investing in AI should focus on system design, not just model size—analogous to building a race car with more than just an engine.                      |
|   8 | A small model in a smart system can outperform a large model in a simplistic system, especially considering cost, latency, safety, and privacy.         |
|   9 | Regulation should target systems, not just models, as small models in complex systems can be more dangerous than large, isolated models.                |
|  10 | Sampling methods (e.g., greedy decoding, top-p, beam search, majority completion) significantly affect system behavior; there is no single best method. |
|  11 | Prompting is central to system performance; small changes in prompt formatting can cause large swings in output quality.                                |
|  12 | Model and prompt are inextricably linked; evaluation must consider their combination, not the model alone.                                              |
|  13 | Prompt engineering is fragile and model-dependent; system-level programming libraries like DSPy aim to abstract and optimize this process.              |
|  14 | Data-driven optimization of prompts and demonstrations can outperform hand-crafted strategies.                                                          |
|  15 | Most enterprise AI usage relies on smaller models due to cost and latency constraints; system design is key to maximizing their value.                  |
|  16 | Tool access (e.g., web search, APIs) further emphasizes the need for system-level thinking.                                                             |
|  17 | Future progres                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vRTcE19M-KE)
