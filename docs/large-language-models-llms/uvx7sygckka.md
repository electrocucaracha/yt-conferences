---
type: Video Note
title: "Stanford CS224N: NLP w/ DL | Spring 2024 | Lecture 12 - Efficient Training, Shikhar Murty"
description: "In this lecture, the instructor shifts focus from natural language processing to practical aspects of training large machine learning models on GPUs, covering topics essential for final projects. The lecture begins with an explanation of fl..."
resource: https://www.youtube.com/watch?v=UVX7SYGCKkA
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture, the instructor shifts focus from natural language processing to practical aspects of training large machine learning models on GPUs, covering topics essential for final projects.
The lecture begins with an explanation of floating point representations (fp32, fp16, and bfloat16), highlighting the trade-offs between memory usage, range, and precision, and introduces mixed precision training as a way to optimize GPU memory and computation.
The discussion then moves to multi-GPU training, detailing strategies like Distributed Data Parallel (DDP) and the Zero Redundancy Optimizer (ZeRO) in its various stages, which progressively shard optimizer state, gradients, and model parameters across GPUs to improve memory efficiency without significant communication overhead.
The instructor also addresses the limitations of these methods, especially when models are too large to fit even with advanced sharding, and introduces parameter-efficient fine-tuning techniques such as LoRA (Low-Rank Adaptation), which allow updating only a small subset of parameters to save resources while maintaining performance.
Throughout, the lecture emphasizes practical guidelines—such as always using mixed precision, leveraging ZeRO stages, and applying LoRA to specific weight matrices—and discusses the broader importance of efficiency in machine learning, including environmental and accessibility concerns.
The session concludes with a review of communication strategies in FSDP (Fully Sharded Data Parallel) and practical advice for implementing these techniques in student projects.
# Main Points

|   # | Main point                                                                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture focuses on training large models on GPUs, mixed precision training, multi-GPU training (DDP, FSDP), and parameter efficient fine-tuning.                                                                                               |
|   2 | Announcements: Proposal grades and project milestone details will be released soon; milestone is 5% of grade, due in 12 days, max 2 pages.                                                                                                     |
|   3 | Floating point representations: fp32 (4 bytes per parameter), fp16 (2 bytes, less range and precision), bfloat16 (same range as fp32, less precision).                                                                                         |
|   4 | Mixed precision training reduces memory usage and speeds up matrix multiplications.                                                                                                                                                            |
|   5 | Issues with fp16: small numbers round to zero, large numbers to NaN, less precision causes rounding errors.                                                                                                                                    |
|   6 | Solution: Maintain master weights in fp32, use fp16 for forward/backward passes, upcast gradients to fp32 for updates.                                                                                                                         |
|   7 | Gradient scaling (loss scaling) helps prevent small gradients from vanishing in fp16.                                                                                                                                                          |
|   8 | bfloat16 avoids need for gradient scaling but requires newer GPUs (Ampere architecture).                                                                                                                                                       |
|   9 | Multi-GPU training: DDP (Distributed Data Parallel) keeps full model, gradients, and optimizer state on each GPU; uses all-reduce for gradient synchronization.                                                                                |
|  10 | DDP has poor memory scaling; Zero Redundancy Optimizer (ZeRO) shards optimizer state (stage 1), gradients (stage 2), and model parameters (stage 3/FSDP) across GPUs to save memory.                                                           |
|  11 | ZeRO stage 1 and 2 save memory with no extra communication overhead; stage 3 (FSDP) shards model parameters but increases communication.                                                                                                       |
|  12 | Model activations also consume GPU memory, scaling with batch size.                                                                                                                                                                            |
|  13 | Recommended workflow: Always use mixed precision; use bfloat16 on supported GPUs; use ZeRO stage 2 for free memory savings; use ZeRO stage 3 or FSDP if batch size 1 doesn't fit; if still out of memory, use parameter efficient fine-tuning. |
|  14 | Parameter efficient fine-tuning (e.g., LoRA): Only updates a small subset of parameters, stores low-rank matrices, reduces compute and storage, maintains performance.                                                                         |
|  15 | LoRA applies low-rank updates to attention matrices; main hyperparameters are alpha, rank, and wh                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=UVX7SYGCKkA)