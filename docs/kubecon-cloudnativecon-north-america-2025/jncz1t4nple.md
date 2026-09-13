---
type: Video Note
title: "Building AI/ML Pipelines on Kubernetes - Susan Wu, Ian Chakares, Lu Qiu, Anant Vyas & Lucy Sweet"
description: "The panel discussion, led by Susan Wu and featuring experts from Google, Uber, and Lens DB, focused on building AI/ML pipelines on Kubernetes and the evolving infrastructure to support these workloads. Panelists highlighted how AI/ML worklo..."
resource: https://www.youtube.com/watch?v=jnCZ1T4nPLE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The panel discussion, led by Susan Wu and featuring experts from Google, Uber, and Lens DB, focused on building AI/ML pipelines on Kubernetes and the evolving infrastructure to support these workloads.
Panelists highlighted how AI/ML workloads differ from traditional stateless microservices, requiring massive scale, specialized hardware like GPUs and TPUs, and new features in Kubernetes such as in-place pod scaling, improved scheduling, and support for stateful and high-performance computing (HPC) tasks.
Companies like Uber and Lens DB described their use of Kubernetes to orchestrate complex AI pipelines, leveraging tools like Ray and PyTorch for distributed compute and developing open-source standards for multimodal data storage.
The discussion also covered networking innovations, such as intelligent fabrics and managed offerings like DRA net and GKE inference gateway, which optimize performance for large-scale AI training and inference.
The panel addressed challenges in development and testing environments, resource allocation, and the rise of agentic workloads, with Uber sharing its approach to building and managing internal AI agents and registries.
Overall, the session emphasized Kubernetes’ rapid adaptation to AI/ML needs and the collaborative efforts across the community to make it a robust platform for next-generation workloads.
# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Panelists introduced: Susan Wu (cloud networking PM), Lou (Lens DB data engineer), Ian Chapris (GKE, Google), Lucy (Uber platform engineering, Kubernetes node lifecycle lead)                       |
|   2 | AI/ML workloads on Kubernetes differ from traditional workloads: stateful, massive resource consumption, require specialized hardware (GPUs, TPUs)                                                   |
|   3 | Kubernetes has evolved to support AI/ML and HPC workloads with features like in-place pod vertical scaling, in-place container restarts, improved scheduling, eviction requests, and gang scheduling |
|   4 | Kubernetes clusters now support massive scale (up to 100,000+ nodes on GKE)                                                                                                                          |
|   5 | Specialized hardware (Nvidia GB300, Google Ironwood TPUs) requires Kubernetes to be hardware-aware                                                                                                   |
|   6 | Uber and others use Ray and PyTorch on Kubernetes for distributed ML pipelines; Ray’s integration with PyTorch Foundation noted                                                                      |
|   7 | Lens DB provides a multimodal data storage and compute platform on Kubernetes, supporting various data types and AI frameworks                                                                       |
|   8 | Data retrieval needs for AI/ML are diverse (full-text search, semantic search, SQL); Lens DB aims to unify data formats and retrieval with the open-source Lens format                               |
|   9 | Networking is critical for AI/ML workloads: high-capacity, low-latency fabrics interconnect accelerators; managed DRA net on GKE aligns accelerators and NICs for performance                        |
|  10 | GKE Inference Gateway provides intelligent L7 routing for LLM traffic, optimizing for model placement, cache utilization, and request priority                                                       |
|  11 | Dev/test environments on Kubernetes face challenges with resource allocation and velocity; solutions include autoscaling and dynamic resource allocation (e.g., Ray)                                 |
|  12 | Uber builds agentic workloads as CRDs with custom controllers, internal agent registry, and federated scheduler for multi-cluster placement                                                          |
|  13 | Experimentation with agents is common; agents often defined as chains of operations in Python, scaled via Kubernetes                                                                                 |
|  14 | Networking challenges for agents include authentication, authorization, observability, and managing state and logging                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jnCZ1T4nPLE)