---
layout: default
title:
  "CafeGPT: Serving LLMs Like Coffee With Kubernetes - Madhav Jivrajani & Kartik
  Ramesh, UIUC"
nav_order: 38
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Madav and Karthik introduce "Cafe GPT," using a coffee
  shop analogy to explain the process of serving large language model (LLM) inference
  workloads, particularly in Kubernetes environments. They describe how customer requests...
resource: https://www.youtube.com/watch?v=zMArlA0rPsM
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

In this talk, Madav and Karthik introduce "Cafe GPT," using a coffee shop analogy to explain the process of serving large language model (LLM) inference workloads, particularly in Kubernetes environments.
They describe how customer requests are routed and fulfilled, likening the router to a manager, the inference engine to a barista, and GPUs to coffee machines, with the process involving computationally intensive "prefill" and memory-bound "decode" phases.
The speakers discuss the importance of KV caching for efficiency, the challenges of batching and dynamic workloads, and strategies for resource allocation and autoscaling, such as dynamic resource allocation (DRA) and scaling based on queue length, batch size, or KV cache utilization.
They emphasize the need for intelligent load balancing, leveraging Kubernetes features and ecosystem projects like the API Inference Gateway, LLMD, and AI Bricks to optimize performance and resource use.
Ultimately, they reassure the audience that serving LLMs can be approachable and manageable, much like running a well-organized café.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speakers: Madav (grad student at UIU, distributed systems, Kubernetes contributor) and Karthik (grad student at UIUC, ML systems)                    |
|   2 | Talk is not a deep dive into LLM inference or Kubernetes internals, but an overview of how ecosystem parts fit together                              |
|   3 | Cafe GPT analogy: customer (user request), manager (router), barista (LLM inference engine), coffee machine (GPU)                                    |
|   4 | LLM request lifecycle: user input split into tokens, processed through model layers, generating internal states (KV cache)                           |
|   5 | LLMs are auto-regressive: next token generated using previous tokens and internal states, repeated until end-of-sequence token                       |
|   6 | Repeating sequence prefixes causes redundant computation and latency                                                                                 |
|   7 | KV cache (key-value cache) stores hidden states to avoid recomputation, speeding up inference up to 5x but increasing memory use                     |
|   8 | Example: 8B parameter model with 8K context can serve ~24 concurrent requests on a 40GB GPU due to KV cache limits                                   |
|   9 | Two serving phases: prefill (computationally intensive, short), decode (memory bound, long, unpredictable duration)                                  |
|  10 | Customer SLAs: low request latency, low time between tokens, low time to first token                                                                 |
|  11 | Provider goals: high throughput, high machine utilization, support for varying SLAs                                                                  |
|  12 | Novice barista (single-threaded) vs. experienced barista (batching requests for efficiency)                                                          |
|  13 | Batching increases throughput and reduces latency but causes dynamic batch sizes and potential interference between prefill and decode               |
|  14 | Prefill-decode disaggregation: separate machines for prefill (compute-heavy) and decode (memory-heavy) to optimize resources and reduce interference |
|  15 | Kubernetes is the de facto infrastructure platform; inference is a new workload with unique characteristics                                          |
|  16 | Small models ("espresso models") can fit on a single GPU; resource requests can specify full or fractional GPUs (MIG)                                |
|  17 | Static GPU partitioning can cause resource wastage; dynamic resource allocation (DRA) allows on-the-fly GPU partitioning and flexible scheduling     |
|  18 | Autos                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zMArlA0rPsM)
