---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 3 - Tranformers & Large Language Models"
nav_order: 3
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "In Lecture 3 of CME 295, the instructors introduce Large Language Models (LLMs) as decoder-only architectures that are large in parameter count, training data, and computational requirements."
resource: "https://www.youtube.com/watch?v=Q5baLehv5So"
tags:
  - stanford-cme295-transformers-and-large-language-models-i-autumn-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T20:43:47+00:00
---

# Summary

In Lecture 3 of CME 295, the instructors introduce Large Language Models (LLMs) as decoder-only architectures that are large in parameter count, training data, and computational requirements.
The lecture details the Mixture of Experts (MoE) mechanism, which enhances model capacity by routing tokens to specific expert sub-networks, thereby reducing active compute per inference while mitigating issues like routing collapse through specialized loss functions and noisy gating.
The discussion then shifts to response generation strategies, contrasting greedy decoding and beam search with sampling methods, and explains how temperature, top-k, and top-p parameters control the diversity and determinism of the output.
Additionally, the session covers prompting techniques such as in-context learning, chain-of-thought reasoning, and self-consistency to improve model performance without weight updates.
Finally, the lecture explores inference efficiency optimizations, including KV caching, Grouped Query Attention, PagedAttention for memory management, Multi-Latent Attention for compact representations, and speculative decoding to accelerate token generation using smaller draft models.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Large language models are defined as large, decoder-only architectures that predict the probability of the next token.                                                                        |
|   2 | LLMs are characterized by having billions of parameters, training on trillions of tokens, and requiring significant computational resources.                                                  |
|   3 | Mixture of Experts (MoE) architectures use a router to select a subset of experts for each token to reduce inference compute.                                                                 |
|   4 | Sparse MoE activates only the top K experts, whereas dense MoE weights all experts, with sparse MoE offering lower FLOPs.                                                                     |
|   5 | In MoE models, experts are typically feedforward neural networks placed where the standard FFN would be in a transformer block.                                                               |
|   6 | Routing collapse occurs when the router consistently selects only a few experts, mitigated by adding a load-balancing loss term.                                                              |
|   7 | Greedy decoding selects the highest probability token, which is deterministic but lacks diversity and may not be globally optimal.                                                            |
|   8 | Beam search tracks the K most probable paths to improve global optimality but can favor shorter sequences and lacks creativity.                                                               |
|   9 | Sampling methods like top-k and top-p restrict the candidate tokens to the most probable ones to balance quality and diversity.                                                               |
|  10 | Temperature controls the probability distribution; low temperatures create spiky distributions for deterministic outputs, while high temperatures flatten distributions for creative outputs. |
|  11 | Guided decoding filters invalid next tokens during generation to ensure outputs conform to specific formats like JSON.                                                                        |
|  12 | Context length refers to the maximum number of input tokens a model can process, with modern LLMs supporting hundreds of thousands to millions of tokens.                                     |
|  13 | Context rot describes the degradation of a model's ability to retrieve specific information as context length increases.                                                                      |
|  14 | Prompts are structured with context, instructions, inputs, and constraints to guide the model's response effectively.                                                                         |
|  15 | In-context learning allows models to perform tasks without weight updates, using zero-shot or few-shot examples.                                                                              |
|  16 | Few-shot learning generally improves performance by providing examples, though recent models may perform well with better instructions alone.                                                 |
|  17 | Chain of thought prompting forces the model to generate reasoning steps before the final answer, improving accuracy and debuggability.                                                        |
|  18 | Self-consistency involves sampling multiple responses and selecting the most frequent answer via majority voting to enhance robustness.                                                       |
|  19 | KV caching stores key and value matrices from previous tokens to avoid redundant computations during autoregressive generation.                                                               |
|  20 | Group Query Attention (GQA) reduces the number of key and value heads to lower memory usage and improve efficiency.                                                                           |
|  21 | PagedAttention manages memory fragmentation by allocating KV cache in fixed-size blocks, improving throughput in inference servers.                                                           |
|  22 | Multi-Latent Attention compresses key and value representations into a lower-dimensional shared space to reduce cache size.                                                                   |
|  23 | Speculative decoding uses a smaller draft model to propose tokens, which are then verified by the larger target model to speed up generation.                                                 |
|  24 | Multi-token prediction integrates the draft model into the main architecture by training multiple heads to predict future tokens simultaneously.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Q5baLehv5So/hqdefault.jpg)](https://www.youtube.com/watch?v=Q5baLehv5So)

[Watch on YouTube](https://www.youtube.com/watch?v=Q5baLehv5So)
