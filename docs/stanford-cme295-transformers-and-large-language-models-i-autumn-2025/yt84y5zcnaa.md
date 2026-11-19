---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 2 - Transformer-Based Models & Tricks"
nav_order: 2
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "This lecture from CME295 reviews the self-attention mechanism and transformer architecture before detailing key architectural variations that have evolved since the original 2017 paper."
resource: "https://www.youtube.com/watch?v=yT84Y5zCnaA"
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

This lecture from CME295 reviews the self-attention mechanism and transformer architecture before detailing key architectural variations that have evolved since the original 2017 paper.
The instructor explains the transition from learned position embeddings to sinusoidal functions and, more recently, Rotary Position Embeddings (RoPE), which encode relative position information directly into the attention computation to improve long-range dependency modeling.
The discussion also covers the shift from post-norm to pre-norm layer normalization and the adoption of RMSNorm for computational efficiency, alongside attention optimizations like sliding window attention and Grouped Query Attention (GQA) to reduce memory usage and computational complexity.
The second half of the lecture, led by Shervin, categorizes modern transformer models into encoder-decoder (e.g., T5), encoder-only (e.g., BERT), and decoder-only architectures, noting that decoder-only models have become dominant for large language models due to their scalability and alignment with next-token prediction tasks.
Finally, the lecture provides a deep dive into BERT, explaining its bidirectional nature, the use of special tokens like [CLS] and [SEP], and its two-stage training process involving Masked Language Modeling (MLM) and Next Sentence Prediction (NSP), while also introducing variants like DistilBERT and RoBERTa that address limitations in size, latency, and pre-training objectives.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture 2 of CME295 covers the evolution of the Transformer architecture, focusing on position embeddings, normalization, attention mechanisms, and specific model variants like BERT.          |
|   2 | The original Transformer uses self-attention where queries, keys, and values allow tokens to attend to all other tokens in a sequence.                                                          |
|   3 | Multi-head attention allows the model to learn different projection matrices for queries, keys, and values in parallel, capturing various relationships between tokens.                         |
|   4 | Position embeddings are necessary because self-attention lacks inherent sequential order, requiring explicit injection of positional information.                                               |
|   5 | The original paper used learned position embeddings, which are limited by the maximum sequence length seen during training and prone to overfitting specific positions.                         |
|   6 | Sinusoidal position embeddings use fixed sine and cosine functions to encode positions, allowing the model to generalize to longer sequences and ensuring closer tokens have higher similarity. |
|   7 | Modern models often use Rotary Position Embeddings (RoPE), which rotate query and key vectors based on position to make attention scores depend on relative distance.                           |
|   8 | Layer normalization stabilizes training by normalizing activations; modern architectures prefer Pre-LN over Post-LN and often use RMSNorm for efficiency.                                       |
|   9 | Sliding window attention restricts each token to attend only to a local neighborhood, reducing computational complexity from O(N^2) to O(N*W).                                                  |
|  10 | Grouped Query Attention (GQA) and Multi-Query Attention (MQA) share key and value projection matrices across multiple heads to reduce memory usage in the KV cache.                             |
|  11 | The T5 family uses an encoder-decoder architecture with a span corruption objective, where the model reconstructs masked spans of text.                                                         |
|  12 | Encoder-only models like BERT focus on bidirectional representations for classification tasks, using a CLS token to aggregate sequence information.                                             |
|  13 | BERT pre-training involves two objectives: Masked Language Modeling (MLM) to predict masked tokens and Next Sentence Prediction (NSP) to determine if two sentences are consecutive.            |
|  14 | BERT uses WordPiece tokenization and adds segment embeddings to distinguish between two input sentences, aiding the NSP task.                                                                   |
|  15 | Fine-tuning BERT involves adding a task-specific head, such as a linear layer for classification, on top of the pre-trained encoder weights.                                                    |
|  16 | Distillation techniques, such as those used in DistilBERT, reduce model size by training a smaller student model to mimic the output distribution of a larger teacher model.                    |
|  17 | RoBERTa improved upon BERT by removing the NSP objective, using dynamic masking, and training on larger, more diverse datasets to enhance performance.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/yT84Y5zCnaA/hqdefault.jpg)](https://www.youtube.com/watch?v=yT84Y5zCnaA)

[Watch on YouTube](https://www.youtube.com/watch?v=yT84Y5zCnaA)
