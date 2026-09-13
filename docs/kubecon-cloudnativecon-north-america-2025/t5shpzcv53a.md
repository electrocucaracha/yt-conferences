---
type: Video Note
title: "Tuning GenAI Workloads on Kubernetes: What Actually Works (and Wha... Ishaan Sehgal & Brian Lockwood"
description: "In this presentation, Ean and Brian discuss optimizing generative AI (GenAI) workloads on Kubernetes, focusing on the challenges and solutions for deploying large language models (LLMs) as their sizes and resource demands grow. They introdu..."
resource: https://www.youtube.com/watch?v=t5shPzCV53A
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Ean and Brian discuss optimizing generative AI (GenAI) workloads on Kubernetes, focusing on the challenges and solutions for deploying large language models (LLMs) as their sizes and resource demands grow.
They introduce Kaido, a lightweight Kubernetes controller designed to streamline AI workload deployment across any cloud provider with minimal configuration, and Skyhook, an operator for declaratively modifying host OS settings to better support demanding AI tasks.
Through their collaborative experiments—using Kaido for deployment and Skyhook for OS tuning—they found that while tuning certain Linux parameters did not yield performance improvements for their GPU-bound workloads, the process was made accessible and efficient by these tools.
They emphasize the importance of profiling workloads before tuning, note the limitations of their experiments (such as single-node, single-GPU setups), and highlight additional Skyhook use cases like security and cluster customization.
The session concludes with a discussion on future developments for Skyhook and the growing need for such orchestration tools as AI agents become more prevalent and complex.
# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focused on tuning GenAI workloads on Kubernetes, highlighting what works and what doesn't.                                                                                               |
|   2 | Model sizes for LLMs are rapidly increasing, leading to significant infrastructure and resource challenges.                                                                                         |
|   3 | Kubernetes is preferred for running LLMs when organizations want to own their infrastructure and data, use custom ML frameworks, or require advanced configurations.                                |
|   4 | Kubernetes offers robust community support and tooling, but remains complex even for experts, especially for AI workloads.                                                                          |
|   5 | Kaido is introduced as a Kubernetes controller (CRD) for streamlining AI workload deployment, supporting multiple cloud providers and simplifying ML deployment to about 10 lines of configuration. |
|   6 | Kaido provisions necessary resources (GPU, drivers, CUDA, PyTorch), pulls model weights as OCI artifacts, and exposes endpoints for workloads.                                                      |
|   7 | Examples shown for running inference, fine-tuning (with LoRA/QLoRA adapters), and RAG workloads using Kaido.                                                                                        |
|   8 | Skyhook is introduced as an operator for declaratively modifying host OS settings on Kubernetes nodes.                                                                                              |
|   9 | Skyhook enables actions like cordoning/draining nodes, updating OS packages, configuring kernel settings (e.g., huge pages), and supports lifecycle checks and uninstall/rollback.                  |
|  10 | Skyhook packages are containers that copy scripts to the host and execute them via agents.                                                                                                          |
|  11 | Experiments combined Kaido and Skyhook to test if OS tuning could improve AI workload performance.                                                                                                  |
|  12 | Benchmarks were run using Kaido deployments, with Skyhook used to adjust OS settings (e.g., swappiness, CPU isolation, network, file descriptors).                                                  |
|  13 | Most OS tuning had no positive impact; workloads were GPU-bound, so CPU/kernel tweaks had little effect.                                                                                            |
|  14 | Key lesson: profile workloads before tuning; reliability and stability may benefit more from OS settings than raw performance.                                                                      |
|  15 | Skyhook also used for security, threat detection, SSH agents, and managing cluster-specific tweaks without custom images.                                                                           |
|  16 | Future plans for Skyhook include deployment strat                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=t5shPzCV53A)