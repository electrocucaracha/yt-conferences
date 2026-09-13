---
type: Video Note
title: "Optimizing LLM Inference for the Rest of Us - Abdel Sghiouar, Google"
description: "In this talk, Abdel, a developer advocate at Google, discusses strategies for running large language models (LLMs) on Kubernetes, particularly for those without access to unlimited cloud resources. He explains that as LLMs grow in size and..."
resource: https://www.youtube.com/watch?v=xLum3amp6h0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Abdel, a developer advocate at Google, discusses strategies for running large language models (LLMs) on Kubernetes, particularly for those without access to unlimited cloud resources.
He explains that as LLMs grow in size and complexity, challenges arise in terms of hardware requirements, storage, and efficient deployment, especially when models exceed the capacity of single GPUs or hosts.
Abdel outlines three main layers of optimization: the model itself (such as quantization to reduce memory footprint), the serving engine (choosing compatible and efficient model servers), and the underlying infrastructure (with a focus on accelerator management and networking).
He highlights open-source tools like Spiegel for image caching and Kubernetes features such as device plug-ins and Dynamic Resource Allocation (DRA) for better hardware utilization.
Networking considerations are also addressed, including the need for advanced routing and load balancing tailored to LLM workloads, with projects like the Gateway API inference extension and LLMD offering solutions for more intelligent traffic management.
Throughout, Abdel emphasizes that optimizing LLMs on Kubernetes is a multi-dimensional challenge requiring coordinated improvements across storage, compute, and networking layers.
# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | Talk focuses on running large language models (LLMs) on Kubernetes for users without unlimited GPU access.               |
|   2 | LLMs are growing in size and complexity, requiring multiple GPUs or hosts for deployment.                                |
|   3 | Inference is the process after training, involving complex pipelines inside the model.                                   |
|   4 | Serving engines are required to run inference, similar to web servers for web apps.                                      |
|   5 | Quantization affects model precision and memory requirements; lower precision reduces memory footprint.                  |
|   6 | Context window determines how many tokens a model can process at once; larger windows are needed for chat scenarios.     |
|   7 | LLM deployment scenarios: single host/single accelerator, single host/multi-accelerator, multi-host/multi-accelerator.   |
|   8 | Deployment options: bare metal/VM, Kubernetes, or fully managed platforms; Kubernetes offers flexibility and automation. |
|   9 | Reasons to run models locally: regulation, trust, latency, customization, privacy, cost.                                 |
|  10 | Kubernetes community is adding features to better support AI/LLM workloads.                                              |
|  11 | Key Kubernetes advantages: automation, scalability, advanced device management, multi-cloud support.                     |
|  12 | LLM workloads differ from web apps due to size, hardware needs, and traffic patterns.                                    |
|  13 | Three optimization layers: model (quantization, parameters), server engine (throughput), infrastructure (accelerators).  |
|  14 | Pre-warming, caching, and pre-loading models can improve performance.                                                    |
|  15 | Autoscaling is challenging due to large container/model sizes.                                                           |
|  16 | Popular model servers: VLLM, Hugging Face TGI, Nvidia NIM, Triton, Ray Serve, Jetstream, Ollama.                         |
|  17 | Compatibility between model, server engine, and accelerator must be checked.                                             |
|  18 | Important metrics: time to first token, normalized time per output token, request latency, throughput.                   |
|  19 | Storage challenges: large container and model sizes slow autoscaling.                                                    |
|  20 | Tools: Spiegel (image mirroring across nodes), Docker containers as volumes, preloading/caching models on nodes.         |
|  21 | Accelerator management: device plugins assign GPUs, but lack spe                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=xLum3amp6h0)