---
layout: default
title: "Talks - Jodie Burchell: Lies, damned lies and large language models"
nav_order: 151
parent: PyCon US 2024
type: Video Note
description: 'In a presentation titled "Lies, Damn Lies, and Large Language Models," data scientist Jod Burchell explores the phenomenon of hallucinations in autoregressive LLMs, explaining that these errors ste...'
resource: "https://www.youtube.com/watch?v=innz9iBIAdU"
youtube_stats:
  view_count: 702
  like_count: 21
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

In a presentation titled "Lies, Damn Lies, and Large Language Models," data scientist Jod Burchell explores the phenomenon of hallucinations in autoregressive LLMs, explaining that these errors stem from the models' reliance on lossy compression of vast, often imperfect training data.
Burchell distinguishes between faithfulness hallucinations, where models deviate from provided source text, and factuality hallucinations, which arise from incorrect or outdated knowledge encoded in the model's parameters.
To quantify these issues, the talk introduces the TruthfulQA dataset, a benchmark designed to test models against common misconceptions and conspiracy theories, and demonstrates a Python-based workflow using LangChain to evaluate GPT-3.5 Turbo’s performance on this metric.
The presentation further examines mitigation strategies, including prompt engineering, fine-tuning, and Retrieval-Augmented Generation (RAG), while highlighting the complexities and potential pitfalls of RAG pipelines, such as retrieval errors that can inadvertently worsen hallucination rates.
Finally, Burchell presents the "Retrieve Only When It Needs" (ROWAN) method as an advanced RAG technique that significantly improves factual accuracy, concluding with resources for further exploration and an invitation to discuss implementation details with colleagues at the JetBrains booth.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The talk addresses hallucinations in large language models, covering their causes, classification, measurement, and mitigation strategies.                                     |
|   2 | Autoregressive LLMs generate coherent text but can produce incorrect outputs, known as hallucinations, which remain a significant challenge for real-world applications.       |
|   3 | Transformer architectures, specifically decoder-based models, enable LLMs to scale effectively by processing longer inputs and larger datasets.                                |
|   4 | Training involves predicting the next word, allowing for easy data scaling, while model growth from GPT-1 to GPT-4 reflects increased capacity to encode parametric knowledge. |
|   5 | Smaller models conserve only syntactic rules due to lossy compression, whereas larger models like GPT-3 encode broader semantic knowledge and meaning.                         |
|   6 | Training data primarily comes from web sources like Common Crawl, which requires automated cleaning to remove low-quality, duplicate, or offensive content.                    |
|   7 | Inadequately filtered datasets, such as C4, have introduced misinformation and conspiracy theories into models, contributing to factuality hallucinations.                     |
|   8 | Faithfulness hallucinations occur when a model deviates from provided source text, while factuality hallucinations involve incorrect knowledge learned during training.        |
|   9 | Measurement datasets include SQuAD v2 and Extreme Summarization for faithfulness, and HalluEval QA and TruthfulQA for factuality.                                              |
|  10 | TruthfulQA contains 817 questions across 38 categories of falsehoods, including health, legal, conspiracy theories, and fiction.                                               |
|  11 | A Python demo using Hugging Face datasets and LangChain showed that GPT-3.5 Turbo answered only 36% of TruthfulQA multiple-choice questions correctly.                         |
|  12 | Hallucination leaderboards exist, but understanding specific metrics helps in making better trade-offs when selecting models for particular use cases.                         |
|  13 | Mitigation strategies include prompt engineering to reduce ambiguity, fine-tuning on domain-specific data, and self-refinement of outputs.                                     |
|  14 | Retrieval-Augmented Generation (RAG) integrates external context into prompts to improve accuracy, particularly for outdated or specific information.                          |
|  15 | RAG pipelines involve chunking documents, creating embeddings, storing them in vector databases, and retrieving relevant chunks based on prompt similarity.                    |
|  16 | Poor RAG implementation can worsen hallucinations if irrelevant documents are retrieved or if the model fails to accurately summarize the provided context.                    |
|  17 | Advanced methods like Retrieve-Only-When-Needed (ROWAN) improved GPT-3.5 Turbo's accuracy on TruthfulQA from 70% to 84% by selectively retrieving information.                 |
|  18 | Combining multiple mitigation techniques is often necessary to effectively reduce hallucination rates in LLM applications.                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/innz9iBIAdU/hqdefault.jpg)](https://www.youtube.com/watch?v=innz9iBIAdU)

[Watch on YouTube](https://www.youtube.com/watch?v=innz9iBIAdU)
