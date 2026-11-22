---
layout: default
title: "Lightning Talk: Scalable and Observable RAG for Question-Answering in a Box - Selvi Kadirvel, Elotl"
nav_order: 3
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "Selvi Kaderville, an engineering lead at the startup Elottle, presented an open-source GenAI infrastructure project designed to manage AI inference workloads on Kubernetes."
resource: "https://www.youtube.com/watch?v=BkY5J-epi4U"
youtube_stats:
  view_count: 209
  like_count: 1
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

Selvi Kaderville, an engineering lead at the startup Elottle, presented an open-source GenAI infrastructure project designed to manage AI inference workloads on Kubernetes.
The solution utilizes Kubernetes for scalable infrastructure, employing tools like Luna for cluster autoscaling and VLLM with Ray for efficient, distributed inference of self-hosted large language models such as Microsoft’s Phi-3 and Mamba.
To handle diverse user queries on private data, the system integrates Retrieval-Augmented Generation (RAG) for unstructured data and Text-to-SQL agents for structured data, with a random forest classifier serving as a question router to direct inputs to the appropriate pipeline.
Kaderville emphasized that while AI frameworks provide a structural foundation, achieving high accuracy requires significant investment in real data preparation, field cleanup, and extensive parameter tuning of the inference engine and RAG components.
She concluded by noting that synthetic data was effectively used for generating training questions for the router, and the entire stack is available on GitHub for developers seeking to build self-hosted LLM question-answering systems.

# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Selvi Kaderville is the engineering lead at Elottle, a seed-stage startup building open-source GenAI infrastructure for Kubernetes.      |
|   2 | The company develops Luna, an intelligent cluster autoscaler, and Nova, a multicluster fleet manager for AI and generic workloads.       |
|   3 | Kaderville previously worked as a founding engineer at Container X, which was acquired by Cisco and became Cisco Container Platform.     |
|   4 | Her background includes AI Ops, autoscaling virtual machines at VMware, and performance prediction research during her PhD.              |
|   5 | The project focuses on AI inferencing using pre-trained large language models rather than training new models.                           |
|   6 | Infrastructure choices prioritize cost-effective GPU instance types that are available despite limited supply on major cloud providers.  |
|   7 | Traditional autoscaling is implemented to adjust Kubernetes worker nodes based on incoming inference workload fluctuations.              |
|   8 | The system supports self-hosting open-source LLMs to handle private or specialized data without sending it to third-party providers.     |
|   9 | VLLM, an open-source project from the University of Berkeley, is used for fast and memory-efficient distributed inference.               |
|  10 | Ray, another Berkeley project, provides the distributed computing framework, specifically using the Ray Serve component for VLLM.        |
|  11 | Microsoft’s Phi-3 model and fine-tuned versions from Aion Labs are utilized to enable function calling and tool calling capabilities.    |
|  12 | Retrieval Augmented Generation (RAG) is used for pointed questions by zeroing in on relevant subsets of private data.                    |
|  13 | Text-to-SQL agents handle knowledge aggregation questions by converting natural language into SQL queries for structured databases.      |
|  14 | A question router using a random forest classifier determines whether to direct queries to the RAG or SQL agent.                         |
|  15 | Phoenix, an open-source project from Arize AI, is used for auto-instrumentation and observability of the AI pipeline.                    |
|  16 | Real data is critical for usability, as AI pipelines require significant time for data preprocessing and cleanup to ensure accuracy.     |
|  17 | Synthetic data was effectively used for question generation to create training data for the question router, achieving 97% accuracy.     |
|  18 | Testing on local models helps iron out Python workflows, but actual LLMs must be integrated early in the delivery pipeline.              |
|  19 | LLMs and inference engines require extensive parameter tuning, including KV cache, context length, and tensor pipeline parallelism.      |
|  20 | Increasing model context length beyond optimal levels can cause significant inference latency and poor performance.                      |
|  21 | RAG systems require careful tuning of parameters like chunk size, as default settings often do not work for specific datasets.           |
|  22 | Kubernetes was chosen for its scalability, allowing rapid scaling from cheap instances to multi-GPU setups for improved inference times. |
|  23 | The team did not use the Model Context Protocol, relying instead on fine-tuned foundational models for tool calling.                     |
|  24 | Python was the primary language for data processing and cleanup, despite the team’s background in Go, due to available GenAI modules.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BkY5J-epi4U/hqdefault.jpg)](https://www.youtube.com/watch?v=BkY5J-epi4U)

[Watch on YouTube](https://www.youtube.com/watch?v=BkY5J-epi4U)
