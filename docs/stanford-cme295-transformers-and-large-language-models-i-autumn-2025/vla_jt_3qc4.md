---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 4 - LLM Training"
nav_order: 4
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "Lecture 4 of CME 295 focuses on the training of Large Language Models (LLMs), beginning with an overview of exam logistics and a recap of previous topics such as Mixture of Experts and decoding str..."
resource: "https://www.youtube.com/watch?v=VlA_jt_3Qc4"
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

Lecture 4 of CME 295 focuses on the training of Large Language Models (LLMs), beginning with an overview of exam logistics and a recap of previous topics such as Mixture of Experts and decoding strategies.
The lecture introduces the concept of transfer learning, explaining that LLMs are first pre-trained on vast datasets to predict the next token, a process that requires significant computational resources measured in FLOPs and is optimized according to scaling laws like the Chinchilla hypothesis.
To manage the high memory demands of training, the instructor details various parallelism techniques, including data parallelism, model parallelism, and Zero Redundancy Optimizer (ZeRO), as well as Flash Attention, which improves efficiency by leveraging GPU memory hierarchies and recomputing activations.
The second half of the lecture, led by Shervin, covers supervised fine-tuning (SFT) and instruction tuning, which adapt pre-trained models to be helpful assistants by training them on high-quality, instruction-response pairs.
Finally, the lecture addresses the challenges of evaluating LLM performance through benchmarks and user preference platforms like LMSYS Chatbot Arena, and introduces parameter-efficient fine-tuning methods such as LoRA and quantized LoRA, which allow for efficient adaptation of models by updating only a small subset of weights.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The midterm for CME 295 is scheduled for the following week, covering lectures 1 through 4 with multiple-choice and free-form questions.                                                   |
|   2 | The final exam is set for December 10th from 7:00 p.m. to 8:30 p.m., covering lectures 5 through 9 in a closed-book format.                                                                |
|   3 | Transfer learning allows models to reuse knowledge from pre-training to adapt to specific tasks rather than training from scratch.                                                         |
|   4 | Pre-training involves training large language models on vast datasets to predict the next token, requiring hundreds of billions to trillions of tokens.                                    |
|   5 | The Chinchilla scaling laws suggest that optimal compute usage occurs when the training dataset size is approximately 20 times the number of model parameters.                             |
|   6 | Training large models requires significant compute resources, measured in FLOPs, and is constrained by limited GPU memory.                                                                 |
|   7 | Data parallelism distributes data across GPUs to reduce memory load, while Zero Redundancy Optimizer (ZeRO) partitions optimizer states, gradients, and parameters to further save memory. |
|   8 | Model parallelism techniques, including tensor, pipeline, and expert parallelism, distribute model components across multiple devices to handle large architectures.                       |
|   9 | Flash Attention optimizes attention computation by using tiling to minimize data transfer between high-bandwidth memory and fast on-chip SRAM.                                             |
|  10 | Flash Attention also enables activation recomputation during the backward pass, reducing memory usage and improving runtime efficiency.                                                    |
|  11 | Quantization reduces the precision of model weights to save memory and increase compute speed, with mixed precision training maintaining high-precision weights for updates.               |
|  12 | Supervised Fine-Tuning (SFT) refines pre-trained models using labeled input-output pairs to make them helpful assistants for specific tasks.                                               |
|  13 | Instruction tuning is a subset of SFT that trains models to follow user instructions, using high-quality data for tasks like story writing and code generation.                            |
|  14 | SFT datasets are significantly smaller than pre-training corpora, focusing on high-quality, task-specific examples to align model behavior.                                                |
|  15 | Evaluation of LLMs involves benchmarks like MMLU and GSM8K, though these can be influenced by training on similar tasks and may not fully reflect user preference.                         |
|  16 | LLM Leaderboards, such as LMSYS Chatbot Arena, use pairwise user comparisons to rank models but suffer from biases and potential manipulation.                                             |
|  17 | Alignment is the process of combining fine-tuning and preference tuning to ensure models are helpful, harmless, and honest.                                                                |
|  18 | Mid-training is an emerging step between pre-training and fine-tuning that aligns data distribution with target tasks before final tuning.                                                 |
|  19 | LoRA (Low-Rank Adaptation) efficiently fine-tunes models by freezing pre-trained weights and training small, low-rank matrices, significantly reducing trainable parameters.               |
|  20 | LoRA is most effective when applied to feed-forward blocks and typically requires higher learning rates compared to full fine-tuning.                                                      |
|  21 | Quantized LoRA combines LoRA with weight quantization, such as NF4 format, to achieve substantial VRAM savings while maintaining performance.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VlA_jt_3Qc4/hqdefault.jpg)](https://www.youtube.com/watch?v=VlA_jt_3Qc4)

[Watch on YouTube](https://www.youtube.com/watch?v=VlA_jt_3Qc4)
