---
layout: default
title:
  Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 3 - Tranformers
  & Large Language Models
nav_order: 3
parent: Large Language Models Llms
type: Video Note
description:
  The lecture begins with announcements about slide availability and a
  recap of previous sessions on self-attention and transformer models, categorizing
  them into encoder-decoder (e.g., T5), encoder-only (e.g., BERT), and decoder-only
  (e.g...
resource: https://www.youtube.com/watch?v=Q5baLehv5So
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

The lecture begins with announcements about slide availability and a recap of previous sessions on self-attention and transformer models, categorizing them into encoder-decoder (e.g., T5), encoder-only (e.g., BERT), and decoder-only (e.g., GPT) architectures.
The focus then shifts to large language models (LLMs), defined as decoder-only models trained on massive datasets with billions of parameters, requiring significant computational resources.
The concept of Mixture of Experts (MoE) is introduced as a way to activate only a subset of model parameters during inference, improving efficiency, with sparse MoE selecting top experts per input and techniques like routing and noisy gating used to ensure balanced expert utilization.
The lecture then covers response generation strategies, including greedy decoding, beam search, and sampling methods such as top-K and top-P, and explains the role of temperature in controlling output diversity.
Prompting strategies are discussed, including context length, zero-shot and few-shot in-context learning, chain-of-thought prompting, and self-consistency via majority voting.
Finally, the lecture explores efficiency techniques for inference, such as KV caching, group query attention, memory management (e.g., page attention), multi-latent attention for compact representations, and advanced decoding methods like speculative decoding and multi-token prediction, all aimed at making LLMs more scalable and practical.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Announcements: Slides are available on the site before class; will be posted every Thursday evening.                                                                                 |
|   2 | Recap: Previous lectures covered self-attention, transformers, and three main model categories: encoder-decoder (e.g., T5), encoder-only (e.g., BERT), and decoder-only (e.g., GPT). |
|   3 | LLMs (Large Language Models):                                                                                                                                                        |
|   4 | Assign probability to sequences of tokens (next token prediction).                                                                                                                   |
|   5 | Large in model size (billions to hundreds of billions of parameters), data (hundreds of billions to trillions of tokens), and compute requirements.                                  |
|   6 | Modern LLMs are typically decoder-only models (e.g., GPT, Llama, Gemma, Deepseek, Mistral).                                                                                          |
|   7 | Mixture of Experts (MoE):                                                                                                                                                            |
|   8 | Not all parameters are activated for each prediction; only a subset ("experts") are used.                                                                                            |
|   9 | Gating network (router) selects which experts to activate per input.                                                                                                                 |
|  10 | Dense MoE: All experts weighted; Sparse MoE: Only top-K experts activated.                                                                                                           |
|  11 | MoE typically placed in the feed-forward neural network (FFN) layer.                                                                                                                 |
|  12 | Routing collapse is a challenge; mitigated by modifying the loss to encourage uniform expert usage.                                                                                  |
|  13 | Techniques like noisy gating and dropout are used to improve training.                                                                                                               |
|  14 | Response Generation:                                                                                                                                                                 |
|  15 | Greedy decoding: Always pick highest probability token (deterministic, lacks diversity).                                                                                             |
|  16 | Beam search: Tracks top-K most probable sequences (more globally optimal, less diverse).                                                                                             |
|  17 | Sampling: Draw next token from probability distribution (more creative/diverse).                                                                                                     |
|  18 | Top-K and Top-P sampling restrict sampling to most probable tokens.                                                                                                                  |
|  19 | Probabilities are computed via softmax; temperature parameter controls output diversity (low T = deterministic, high T = diverse).                                                   |
|  20 | Guided Decoding: Restricts next token choices to enforce output formats (e.g., JSON).                                                                                                |
|  21 | Prompting Strategies:                                                                                                                                                                |
|  22 | Context length/window size: Modern LLMs handle tens of thousands to millions of tokens, but retrieval degrades with longer contexts ("context rot").                                 |
|  23 | Prompts typically include context, instructions, input, and con                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Q5baLehv5So)
