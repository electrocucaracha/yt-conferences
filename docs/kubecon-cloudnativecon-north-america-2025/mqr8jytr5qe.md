---
layout: default
title:
  "AI Models Are Huge, but Your GPUs Aren’t: Mastering Multi-Node Distributed
  Infe... E. Wong & J. Shan"
nav_order: 6
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=MQR8jyTR5QE
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

Here is a summary of the video transcript in 3-5 sentences: Ernest, a software engineer at Microsoft, discusses the challenges of serving large language models (LLMs) on GPUs, particularly with regards to data privacy, model customization, and predictable costs.
He presents a four-step process for tackling this challenge: model selection, fitting, serving, and communication.
The key to efficient serving is prefill decode disagregation, which separates the initial processing of token generations from decoding, reducing interference and improving performance.
Ernest also discusses multi-node deployment strategies, including attention and FFN disagregation, and the importance of observability and topology-aware scheduling in optimizing performance.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Self-hosting AI models on Kubernetes provides full control over data and privacy, model customization, and predictable costs.                      |
|   2 | The four-step process for self-hosting AI models on Kubernetes includes:                                                                           |
|   3 | Model selections                                                                                                                                   |
|   4 | Model fitting (using tensor parallelism, pipeline parallelism, or a combination of both)                                                           |
|   5 | Serving (using prefill decode disagregation)                                                                                                       |
|   6 | Communications (between GPUs within a node and across multiple nodes)                                                                              |
|   7 | Hybrid approach of tensor parallelism and pipeline parallelism is used to fit huge models.                                                         |
|   8 | Prefill decode disagregation separates the initial processing of token generations from interfering with each other.                               |
|   9 | Benchmark shows that PD disagregation strategy when deployed on Kubernetes with independent scaling dramatically improved tail latency under load. |
|  10 | Multi-node system requires fall tolerant solutions to minimize service interruption.                                                               |
|  11 | Attention and FFN disagregation will push network performance further, requiring joint orchestration of performance and communication stages.      |
|  12 | Data transfer for attention and FFN disagregation is super large, but can be calculated given the model and data lens.                             |
|  13 | Observability is crucial for monitoring performance and optimizing setups.                                                                         |
|  14 | Topology aware scheduling within a node aligns nick and GPU for lowest latency.                                                                    |
|  15 | Inter-node topology scheduling is well-solved in the upstream Kubernetes community.                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MQR8jyTR5QE)
