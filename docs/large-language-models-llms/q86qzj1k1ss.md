---
type: Video Note
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 9 - Recap & Current Trends"
description: "In the final lecture of CM295, the instructors provided a comprehensive recap of the course, tracing the evolution of language models from early tokenization and word embeddings through RNNs to the transformer architecture, highlighting key..."
resource: https://www.youtube.com/watch?v=Q86qzJ1K1Ss
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In the final lecture of CM295, the instructors provided a comprehensive recap of the course, tracing the evolution of language models from early tokenization and word embeddings through RNNs to the transformer architecture, highlighting key concepts such as self-attention, positional embeddings, and the development of encoder, decoder, and encoder-decoder models.
They discussed the scaling of large language models (LLMs), efficient training techniques like mixture of experts and flash attention, and the multi-stage training process involving pre-training, supervised fine-tuning, and preference tuning using reinforcement learning methods such as PPO and GRPO.
The lecture also covered advanced topics including reasoning chains, retrieval-augmented generation (RAG), tool use, and evaluation methods leveraging LLMs as judges, while addressing biases and benchmarks.
In the second part, they explored trending topics like the adaptation of transformers to non-text domains (e.g., vision transformers), the emergence of diffusion-based LLMs for faster and more flexible text generation, and the cross-pollination of techniques between vision and language models.
The session concluded with reflections on ongoing research challenges—such as data quality, architectural choices, hardware optimization, and future directions in cost-effective, smaller models and democratized agentic workflows—while encouraging students to stay engaged with the rapidly evolving field.
# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture 9 is the final lecture of CM295, divided into three parts: course recap, trending topics, and concluding thoughts.                            |
|   2 | Recap of course content:                                                                                                                              |
|   3 | Started with understanding transformers, tokenization (subword tokenizers), and embeddings (word2vec).                                                |
|   4 | Discussed limitations of early embeddings (lack of context), introduction of RNNs, and their limitations (long-range dependencies).                   |
|   5 | Introduced self-attention and transformer architecture (encoder, decoder), and key concepts (query, key, value, softmax).                             |
|   6 | Improvements to transformers: rotary position embeddings (RoPE), group query attention, normalization (postnorm vs prenorm).                          |
|   7 | Derived models: encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5); differences in text generation and embeddings.                         |
|   8 | Large Language Models (LLMs): scaling, mixture of experts, efficient computation (flash attention), data/model parallelism.                           |
|   9 | LLM training: pre-training, supervised fine-tuning (SFT), preference tuning (RLHF), reward models, and regularization.                                |
|  10 | Advanced reasoning: chain-of-thought prompting, RL algorithms (PPO, G-RPO), verifiable rewards, and extensions (G-RPO-done-right, DAPO).              |
|  11 | Retrieval Augmented Generation (RAG): candidate retrieval (bi-encoder), reranking (cross-encoder), prompt augmentation.                               |
|  12 | Tool calling: LLMs leveraging APIs, agentic workflows combining RAG and tool use.                                                                     |
|  13 | LLM evaluation: LLM-as-a-judge, rationale + score, biases (position, verbosity, self-enhancement), benchmarks (knowledge, reasoning, coding, safety). |
|  14 | Final exam covers lectures 5-8.                                                                                                                       |
|  15 | Trending topics:                                                                                                                                      |
|  16 | Transformers applied beyond text: Vision Transformer (ViT) for images, patch embeddings, CLS token for classification.                                |
|  17 | Multimodal models: combining image and text tokens, methods for input integration.                                                                    |
|  18 | Diffusion-based LLMs: diffusion models for text (masking as noise), masked diffusion models (MDM), advantages (speed, fill-in-the-middle tasks).      |
|  19 | Concluding thoughts:                                                                                                                                  |
|  20 | Cross-pollination betwe                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Q86qzJ1K1Ss)