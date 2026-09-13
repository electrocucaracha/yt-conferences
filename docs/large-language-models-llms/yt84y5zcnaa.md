---
type: Video Note
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 2 - Transformer-Based Models & Tricks"
description: "In this lecture, the instructors addressed logistical updates regarding audio quality and the final exam date before reviewing key concepts from the previous session on self-attention and the transformer architecture. They recapped how self..."
resource: https://www.youtube.com/watch?v=yT84Y5zCnaA
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture, the instructors addressed logistical updates regarding audio quality and the final exam date before reviewing key concepts from the previous session on self-attention and the transformer architecture.
They recapped how self-attention enables each token to attend to all others using queries, keys, and values, and explained the structure of transformers, including the encoder and decoder components, with a focus on multi-head attention.
The lecture then delved into position embeddings, contrasting learned and sinusoidal (static) methods, and discussed modern alternatives like rotary position embeddings (RoPE) that encode relative positional information directly in the attention mechanism.
Changes in normalization techniques were covered, highlighting the shift from post-norm to pre-norm and the adoption of RMS normalization for efficiency.
The instructors also explored attention mechanism variations, such as local (sliding window) attention and sharing projection matrices across heads (MQA, GQA), to improve scalability and efficiency.
The second part of the lecture introduced major transformer model families—encoder-decoder (e.g., T5), encoder-only (e.g., BERT), and decoder-only architectures—detailing their training objectives and use cases.
A deep dive into BERT explained its bi-directional encoder structure, pre-training tasks (masked language modeling and next sentence prediction), input embeddings (including segment embeddings), and fine-tuning for classification tasks.
The session concluded with discussions on model efficiency improvements through distillation (DistilBERT) and simplification of pre-training objectives (RoBERTa), emphasizing the evolution and practical considerations in transformer-based NLP models.
# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Audio setup improved for lecture; final exam date may change, updates to follow.                                                                                      |
|   2 | Lecture 1 recap: Introduced self-attention, where each token attends to all others using queries, keys, and values; formula: softmax(QKᵗ/√dₖ)V.                       |
|   3 | Transformer architecture: Encoder (processes input) and decoder (generates output); originally for machine translation.                                               |
|   4 | Multi-head attention: Multiple heads allow the model to learn different projections; attention maps visualize which tokens are attended.                              |
|   5 | Position embeddings: Two main types—learned (one embedding per position, limited by training data) and fixed (sinusoidal, allows generalization to longer sequences). |
|   6 | Sinusoidal embeddings use sine and cosine functions to encode position, enabling similarity based on relative distance.                                               |
|   7 | Modern models often inject position information directly into the attention layer (e.g., T5’s relative position bias, Alibi, RoPE/rotary embeddings).                 |
|   8 | RoPE (rotary position embeddings): Rotates queries and keys by position-dependent angles, encoding relative distance; widely used in current models.                  |
|   9 | Layer normalization: Originally post-norm (after sublayer), now often pre-norm (before sublayer); RMSNorm is a parameter-efficient alternative.                       |
|  10 | Attention complexity: Full attention is O(N²); local/sliding window attention restricts interactions to neighbors, reducing computation.                              |
|  11 | Multi-query/grouped-query attention: Sharing key/value projections across heads (MQA, GQA) saves memory and improves efficiency; common in modern LLMs.               |
|  12 | Transformer variants: Encoder-decoder (T5), encoder-only (BERT, DistilBERT, RoBERTa), decoder-only (modern LLMs).                                                     |
|  13 | T5 uses span corruption (masking spans) instead of next-token prediction; BERT uses masked language modeling (MLM) and next sentence prediction (NSP).                |
|  14 | BERT: Encoder-only, bi-directional self-attention, uses CLS and SEP tokens, segment embeddings, and multi-stage training (pre-training + fine-tuning).                |
|  15 | DistilBERT: Uses knowledge distillation to reduce mode                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yT84Y5zCnaA)