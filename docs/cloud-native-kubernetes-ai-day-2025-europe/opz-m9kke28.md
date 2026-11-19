---
layout: default
title: "Manage Cloud Native LLM Workloads Across Edge and Cloud Seamlessly Using KubeE... Vivian Hu & Fei Xu"
nav_order: 6
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "This presentation introduces a solution for managing cloud-native large language model (LLM) workloads across edge and cloud environments using the Wasmage runtime and the Kubedge project."
resource: "https://www.youtube.com/watch?v=opz-m9KKE28"
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

This presentation introduces a solution for managing cloud-native large language model (LLM) workloads across edge and cloud environments using the Wasmage runtime and the Kubedge project.
The speakers explain that running inference workloads at the edge is critical for real-time decision-making, enhanced privacy, and compliance with data regulations, despite the challenges of limited device resources and fragmented hardware ecosystems.
Wasmage is presented as a lightweight, portable, and secure runtime that allows AI models to run on various hardware accelerators without external dependencies, while Kubedge provides a Kubernetes-based architecture to manage these workloads across unstable networks and diverse devices.
A key component, the Sedna sub-project, facilitates cloud-edge synergy by enabling joint inference, where simple tasks are processed locally on the edge and complex tasks are forwarded to the cloud for higher accuracy.
The session concludes with live demonstrations showing how to deploy LLMs on edge nodes using Wasmage and how to execute joint inference workflows for tasks like helmet detection, illustrating the seamless collaboration between edge and cloud resources.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session focuses on managing cloud-native LLM workloads across edge and cloud using Wasmage and Kubedge.                                  |
|   2 | Inference workloads at the edge are essential for real-time decision making, such as using Whisper for live transcription with low latency.  |
|   3 | Running local AI models enhances privacy by keeping data on the user's machine, aligning with regulations like GDPR.                         |
|   4 | Local deployment allows for domain-specific optimization through fine-tuning or retraining open-source models.                               |
|   5 | Decentralized scalability is achieved by distributing workloads across multiple nodes, preventing single points of failure.                  |
|   6 | Edge devices face challenges due to limited compute, memory, and power, requiring lightweight and high-performance applications.             |
|   7 | Full-size language models cannot run on resource-constrained devices like Raspberry Pi, necessitating smaller models.                        |
|   8 | A balance must be struck between model size and accuracy, with complex tasks handled by the cloud and simple tasks by the edge.              |
|   9 | The fragmented ecosystem of edge devices lacks hardware and operating system standardization.                                                |
|  10 | Wasmage is proposed as a solution because it provides lightweight, portable workloads suitable for resource-limited edge devices.            |
|  11 | Wasmage allows applications to be compiled once and run anywhere across different hardware types like CPUs, GPUs, and TPUs.                  |
|  12 | The Wasmage runtime and API server are under 30 GB, significantly smaller than standard Docker images, with no external Python dependencies. |
|  13 | Wasmage acts as a secure sandbox, isolating applications and supporting Kubernetes for cloud-readiness.                                      |
|  14 | Wasmage supports various AI models including LLMs, Whisper, Stable Diffusion, and embedding models.                                          |
|  15 | The Wasmage API server is fully OpenAI compatible, allowing developers to use standard frameworks for edge applications.                     |
|  16 | Kubedge is a CNCF graduated project that manages workloads across cloud, edge, and device layers.                                            |
|  17 | The Kubedge architecture includes a cloud Kubernetes master, an edge core with a lightweight kubelet, and a device mapper.                   |
|  18 | A component called CodeCall enhances stability for unstable network connections between the cloud and edge.                                  |
|  19 | Sedna is a Kubedge sub-project serving as an edge-cloud synergy AI framework for joint inference and federated learning.                     |
|  20 | Sedna components include a global manager for task coordination, a local controller bridging cloud and edge, and AI workers.                 |
|  21 | The joint inference workflow involves training deep and shallow models, deploying them to cloud and edge respectively.                       |
|  22 | Inference starts with the shallow model at the edge; if confidence is low, the request is forwarded to the cloud large model.                |
|  23 | The JointInferenceService API defines edge workers with shallow models and cloud workers with large models.                                  |
|  24 | A demo demonstrated deploying a 0.5 billion parameter LLM to an edge node using Wasmage on a CPU.                                            |
|  25 | The demo showed running the model with minimal dependencies, using a Wasm file and an embedding model for RAG applications.                  |
|  26 | A second demo showcased edge-cloud joint inference for helmet detection using Kubedge and Sedna.                                             |
|  27 | The helmet detection demo showed that when the edge model failed to recognize a helmet, the request was forwarded to the cloud.              |
|  28 | The cloud model successfully recognized the helmet with higher confidence, demonstrating the synergy between edge and cloud.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/opz-m9KKE28/hqdefault.jpg)](https://www.youtube.com/watch?v=opz-m9KKE28)

[Watch on YouTube](https://www.youtube.com/watch?v=opz-m9KKE28)
