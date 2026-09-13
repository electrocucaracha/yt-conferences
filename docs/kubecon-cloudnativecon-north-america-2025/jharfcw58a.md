---
layout: default
title:
  Benchmarking GenAI Foundation Model Inference Optimizations on Kubernetes -
  S.M. Varghese & B. Slabe
nav_order: 22
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The talk "Benchmarking Foundation Models on Kubernetes" discusses the
  optimization of generative AI models, specifically focusing on model inference and
  latency reduction techniques. The presenters, Sachin Vargas and Brendan Slave, introduc...
resource: https://www.youtube.com/watch?v=_JhARfcw58A
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The talk "Benchmarking Foundation Models on Kubernetes" discusses the optimization of generative AI models, specifically focusing on model inference and latency reduction techniques.
The presenters, Sachin Vargas and Brendan Slave, introduce a benchmarking tool called Inference Perf, which allows for the evaluation of performance gains from various techniques such as prefix caching, chunking, quantization, and speculative decoding.
They demonstrate the effectiveness of these techniques using a controlled experiment setup on a GKE cluster, showcasing improvements in latency and throughput.
The talk highlights the importance of benchmarking and standardizing performance evaluation methods for generative AI models, particularly in the context of Kubernetes deployments.

# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Foundation models are trained on large data and learn complex patterns to generate content.                                                 |
|   2 | Text-based auto-regressive models generate one token at a time, with two stages: prefill and decode.                                        |
|   3 | The prefill stage generates a single output token, while the decode stage generates subsequent tokens in an auto-regressive manner.         |
|   4 | KV cache stores results from previous computations for faster token generation.                                                             |
|   5 | Key metrics for measuring efficiency are time to first token and time per output token.                                                     |
|   6 | Static batching combines prefill and decode stages for concurrent requests, but increases queueing time.                                    |
|   7 | Continuous batching prioritizes new prefilled batches without queueing, improving GPU utilization and reducing latency.                     |
|   8 | Chunk prefill distributes the prefill process over multiple chunks, allowing for more efficient batching and improved hardware utilization. |
|   9 | Quantization reduces model memory footprint and computation, but may impact accuracy.                                                       |
|  10 | Speculative decoding pairs a larger model with a smaller draft model to propose tokens, cutting latency and boosting throughput.            |
|  11 | Inference Perf is a tool for performance benchmarking, not qualitative benchmarking.                                                        |
|  12 | The project aims to be the source of truth for inference benchmarking, welcoming new contributors.                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_JhARfcw58A)
