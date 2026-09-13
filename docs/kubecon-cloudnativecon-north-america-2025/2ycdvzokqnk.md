---
type: Video Note
title: "LLMs on Kubernetes: Squeeze 5x GPU Efficiency With Cache, Route, Repea... Yuhan Liu & Suraj Deshmukh"
description: "In this talk, Suraj from Microsoft and Yuan from the University of Chicago discuss optimizing large language model (LLM) inference on Kubernetes, focusing on improving GPU efficiency through KV cache management. They explain that inference..."
resource: https://www.youtube.com/watch?v=2YCDvZokqnk
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Suraj from Microsoft and Yuan from the University of Chicago discuss optimizing large language model (LLM) inference on Kubernetes, focusing on improving GPU efficiency through KV cache management.
They explain that inference involves generating text token by token, which consumes significant GPU memory, especially as prompt lengths and concurrent requests increase.
The speakers introduce LM Cache, an open-source caching layer that offloads KV cache data from GPU memory to CPU or remote storage, reducing redundant computation and significantly improving throughput and time to first token (TTFT).
Benchmark results show that LM Cache can increase throughput by up to 5x across various models and inference engines, such as VLM and SGLAN.
The talk also covers advanced techniques like KV cache-aware routing and prefill-decode disaggregation, which further enhance efficiency in distributed and scalable LLM deployments on Kubernetes.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | LLM inference on Kubernetes involves running models as microservices, generating text token by token, consuming GPU memory.                                  |
|   2 | Key metrics to optimize: throughput (tokens/sec) and time to first token (TTFT).                                                                             |
|   3 | Popular inference engines: VLLM (most common), SGLang, Nvidia TensorRT.                                                                                      |
|   4 | Each client request sends the full chat context as JSON to the inference engine, causing prompt size and GPU KV cache usage to grow.                         |
|   5 | GPU memory is used for model weights (always resident), KV cache (grows with requests), and system overhead.                                                 |
|   6 | KV cache is metadata generated during the prefill phase and used in the decode phase for each request.                                                       |
|   7 | Vanilla approach recomputes KV cache for repeated or long prompts, increasing TTFT and GPU workload.                                                         |
|   8 | Optimization: Offload KV cache from GPU to tiered storage (CPU memory, NVMe, remote storage) to free GPU for active generation.                              |
|   9 | LM Cache (open source) acts as a caching layer between inference engine and storage, offloading KV cache and reducing redundant computation.                 |
|  10 | LM Cache supports VLLM and SGLang, storing hot caches in GPU, warm in CPU, and cold in remote storage.                                                       |
|  11 | Benchmarks show LM Cache improves throughput by 2x–5x and reduces TTFT and inter-token latency (ITL) across various model sizes (Llama 3 8B, 70B, Qwen 32B). |
|  12 | In distributed inference with multiple replicas, KV cache-aware routing directs requests to replicas with relevant cached KV, further reducing TTFT.         |
|  13 | KV cache-aware routing is implemented in VLLM Production Stack, an open-source Kubernetes-native deployment with smart routing and autoscaling.              |
|  14 | Demo: KV cache-aware router identifies and routes repeated requests to replicas with cached KV, improving efficiency.                                        |
|  15 | Prefill/decode disaggregation: Separate prefill and decode phases on different GPUs, scaling them independently for lower service-level violation rates.     |
|  16 | Demo: Prefill engine generates and transfers KV cache to decode engine using NATS, enabling efficient disaggregation.                                        |
|  17 | LM Cache integration with SGLang                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2YCDvZokqnk)