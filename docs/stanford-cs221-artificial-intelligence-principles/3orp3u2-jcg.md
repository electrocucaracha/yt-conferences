---
type: Video Note
title: "Stanford CS221 | Autumn 2025 | Lecture 17: Language Models"
description: "The lecture provides an overview of language models, emphasizing their ubiquity in modern technology, from chatbots and autocomplete features to robotics and code completion. It explains that contemporary large language models are trained o..."
resource: https://www.youtube.com/watch?v=3orP3u2-jcg
tags: ["stanford-cs221-artificial-intelligence-principles", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The lecture provides an overview of language models, emphasizing their ubiquity in modern technology, from chatbots and autocomplete features to robotics and code completion.
It explains that contemporary large language models are trained on massive datasets—sometimes tens of trillions of words—requiring enormous computational resources and financial investment.
The core of language modeling is predicting the next word in a sequence, which enables multitask learning and allows a single model to perform a wide range of tasks, such as translation, summarization, and reasoning, simply by scaling up data and model size.
The lecture discusses the evolution from simple counting methods to neural network-based models, particularly transformers, and highlights key innovations like pre-training on vast internet text, post-training for instruction following and safety, and the importance of tokenization and efficient system design.
Finally, it addresses the current landscape, where both closed and open-source large language models are rapidly advancing, raising new questions about safety, accessibility, and the societal impact of increasingly powerful AI systems.
# Main Points

|   # | Main point                                                                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Language models are widely used in applications like chatbots, autocomplete, code completion, robotics, and voice/video processing.                                                                                                         |
|   2 | Modern large language models (LLMs) are trained on massive datasets (e.g., Qwen 3: 36 trillion tokens ≈ 27 trillion words ≈ 144TB raw text).                                                                                                |
|   3 | Training LLMs requires significant compute resources, time, and money (e.g., $42 million for a single pre-training run).                                                                                                                    |
|   4 | LLMs are built and maintained by large teams and organizations, often requiring hundreds of contributors.                                                                                                                                   |
|   5 | Language models are models of structured sequences (language), defined by vocabulary and grammar.                                                                                                                                           |
|   6 | The core task is predicting the next word/token in a sequence (auto-regressive modeling).                                                                                                                                                   |
|   7 | Language modeling can be viewed as a multiclass classification problem over vocabulary.                                                                                                                                                     |
|   8 | Probabilistically, language models learn a distribution over sequences, using the chain rule to factor probabilities.                                                                                                                       |
|   9 | Early approaches included counting sequences or n-grams; modern models use neural networks (especially transformers).                                                                                                                       |
|  10 | Many real-world tasks (writing, coding, responding to messages) can be framed as language modeling.                                                                                                                                         |
|  11 | Language modeling enables multitask learning: training on diverse data with a single objective teaches many tasks.                                                                                                                          |
|  12 | Scaling up data, model size, and compute leads to improved performance; unified models can handle multiple tasks.                                                                                                                           |
|  13 | Key innovations: transformer architecture, pre-training on large datasets, post-training (instruction following, safety tuning), tokenization (subword units, byte pair encoding), and efficient system design (quantization, parallelism). |
|  14 | Pre-training uses massive, curated internet text; post-training aligns models with human preferences and safety.                                                                                                                            |
|  15 | Tokenization breaks text into subword units to handle rare/misspelled words efficiently.                                                                                                                                                    |
|  16 | System-level optimizations (quantization, sharding, kernel fusion) are crucial for training and inference at scale.                                                                                                                         |
|  17 | LLMs are now primarily developed by organizations; open and closed mode                                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=3orP3u2-jcg)