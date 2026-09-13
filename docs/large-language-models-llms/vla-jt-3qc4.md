---
layout: default
title: Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 4 - LLM Training
nav_order: 4
parent: Large Language Models Llms
type: Video Note
description:
  The lecture begins with logistics about the upcoming midterm and final
  exams, including their formats, covered topics, and policies on materials. The main
  content reviews large language model (LLM) architectures, focusing on the mixture
  of...
resource: https://www.youtube.com/watch?v=VlA_jt_3Qc4
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

The lecture begins with logistics about the upcoming midterm and final exams, including their formats, covered topics, and policies on materials.
The main content reviews large language model (LLM) architectures, focusing on the mixture of experts (MOE) and methods for next-token prediction such as greedy decoding, beam search, and sampling.
The lecture then details the LLM training process, emphasizing the pre-training stage on massive datasets, the computational and memory challenges involved, and optimization techniques like data and model parallelism, zero redundancy optimization, and flash attention to improve efficiency.
Quantization and mixed-precision training are introduced as methods to reduce memory usage and speed up computation.
The session transitions to fine-tuning, specifically supervised fine-tuning (SFT) and instruction tuning, which adapt pre-trained models to be helpful assistants or to specific tasks using high-quality, labeled datasets.
Challenges in fine-tuning, such as data quality, distribution alignment, and evaluation difficulties, are discussed, along with evaluation benchmarks and user preference-based assessments.
The lecture concludes with efficient fine-tuning techniques like LoRA and quantized LoRA, which reduce computational costs by updating only a small subset of parameters or using lower-precision representations, enabling practical adaptation of large models to new tasks.

# Main Points

|   # | Main point                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Midterm is next week, Friday, October 24, 3:30–5:00 pm, in the same classroom; duration is 1.5 hours.                                                                                                    |
|   2 | Midterm covers lectures 1–4; includes multiple choice and free-form questions; closed book, no calculator, no cheat sheet allowed in the exam.                                                           |
|   3 | Final exam is Wednesday, December 10, 7:00–8:30 pm, in a different room; covers lectures 5–9.                                                                                                            |
|   4 | Office hours available after lecture and via Ed for questions.                                                                                                                                           |
|   5 | Auditors wanting to take the midterm should notify instructors by the weekend.                                                                                                                           |
|   6 | Previous lecture covered mixture of experts (MOE) architectures, LLM next-token prediction, decoding methods (greedy, beam search, sampling), temperature, and inference optimizations (e.g., KV cache). |
|   7 | LLMs are trained using transfer learning: pre-training on large datasets, then fine-tuning for specific tasks.                                                                                           |
|   8 | Pre-training involves predicting the next token on massive datasets (Common Crawl, Wikipedia, Reddit, GitHub, Stack Overflow); datasets can be hundreds of billions to trillions of tokens.              |
|   9 | Compute for training measured in FLOPs (floating point operations); training LLMs requires ~10^25 FLOPs.                                                                                                 |
|  10 | Scaling laws: model performance improves with more compute, data, and parameters; optimal compute use is when training set size is ~20x model size (Chinchilla scaling).                                 |
|  11 | Pre-training is expensive (millions to hundreds of millions of dollars), time-consuming, and has environmental impact; knowledge cutoff date limits model knowledge.                                     |
|  12 | Training uses GPUs/TPUs; memory constraints require distributing computation across multiple GPUs.                                                                                                       |
|  13 | Data parallelism splits data across GPUs; model parallelism splits model across GPUs; Zero Redundancy Optimization (ZeRO) reduces memory duplication.                                                    |
|  14 | Flash Attention optimizes attention computation by tiling matrices to use fast on-chip memory (SRAM), reducing memory reads/writes and enabling recomputation for memory savings.                        |
|  15 | Quantization and mixed precision training reduce memory and speed up training by lowering numerical precision.                                                                                           |
|  16 | Fine-tunin                                                                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=VlA_jt_3Qc4)
