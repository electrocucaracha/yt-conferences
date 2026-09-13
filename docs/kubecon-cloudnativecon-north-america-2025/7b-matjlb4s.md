---
type: Video Note
title: "No More GPU Cold Starts: Making Serverless ML Inference Truly Real-Time - Nikunj Goyal & Aditi Gupta"
description: "Nikun Goyel and Adidi Gupta discuss the challenges of serverless GPU workloads, focusing on the significant cold start latency that makes real-time inference difficult. They explain that while serverless computing ideally offers zero infras..."
resource: https://www.youtube.com/watch?v=7b-mAtJLb4s
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Nikun Goyel and Adidi Gupta discuss the challenges of serverless GPU workloads, focusing on the significant cold start latency that makes real-time inference difficult.
They explain that while serverless computing ideally offers zero infrastructure management and scales to zero when idle, GPU cold starts can take 15–31 seconds due to multiple layers of initialization, including Kubernetes scheduling, GPU driver setup, CUDA context creation, model weight loading, and memory allocation.
In contrast, CPU-based serverless workloads start much faster.
The speakers demonstrate how each phase contributes to latency and outline practical strategies to reduce cold start times, such as maintaining a pool of warm GPUs, optimizing container images, preloading models and tokenizers, using faster serialization formats like TorchScript or ONNX, and employing lazy loading.
They show that combining these techniques can reduce cold start latency by several seconds, but the optimal approach depends on balancing performance needs and cost constraints.
The session concludes with a Q&A addressing motivators for serverless inference and trade-offs between serialization formats.
# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Serverless GPUs face significant cold start latency, often 15-25 seconds or more, making real-time inference impractical.                                                                |
|   2 | Teams often avoid scale-to-zero and keep GPUs warm, losing cost benefits.                                                                                                                |
|   3 | Cold start latency sources include pod creation, GPU resource binding, driver/runtime setup, CUDA context creation, model weight loading, workspace allocation, and input data transfer. |
|   4 | In a demo, cold start took 31 seconds; container started-to-ready (17s) and ready-to-response (13s) were the main contributors; inference itself was ~500ms.                             |
|   5 | Warm start was much faster (20ms total).                                                                                                                                                 |
|   6 | GPU cold start is slower than CPU due to hardware context setup, driver loading, model transfer, and power state transitions.                                                            |
|   7 | Kubernetes GPU workloads involve device plug-in, Nvidia container runtime, driver initialization, and model loading, each adding latency.                                                |
|   8 | Device plug-in and resource allocation can add seconds, especially on multi-GPU nodes or after node restarts.                                                                            |
|   9 | Nvidia runtime hook injects libraries and checks compatibility, adding further delay.                                                                                                    |
|  10 | CUDA context creation, power state transitions, and model weight transfer (often several GB) are major latency sources.                                                                  |
|  11 | Workspace and memory pool allocation, as well as input data transfer and batching, add further unpredictable latency.                                                                    |
|  12 | Strategies to reduce cold start:                                                                                                                                                         |
|  13 | Maintain a pool of warm GPUs (static, dynamic, or predictive scaling).                                                                                                                   |
|  14 | Kubernetes optimizations: keep at least one replica warm, pre-pull images, schedule on recently used nodes, enable GPU persistent mode.                                                  |
|  15 | Image optimizations: bake model/tokenizer into image, disable tokenizer parallelism, move imports to startup.                                                                            |
|  16 | App runtime: run dummy forward pass at startup, use FP16 for models, pre-warm tokenizers.                                                                                                |
|  17 | Use faster serialization formats (TorchScript, SafeTensors, ONNX) to reduce model load time.                                                                                             |
|  18 | Lazy loading: defer model/tokenizer loading until first request; suitable for non-real-time workloads.                                                                                   |
|  19 | Combining multiple techniques yields                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7b-mAtJLb4s)