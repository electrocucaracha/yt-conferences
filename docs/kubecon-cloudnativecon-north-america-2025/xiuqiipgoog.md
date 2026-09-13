---
layout: default
title:
  Optimizing Multi-Agent LLM Workloads With AMD GPUs and Kueue - Yuchen Fama,
  Jodie Su & Zhiming Shen
nav_order: 193
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The presentation, led by representatives from Cognality, AMD, and AXeller,
  focused on optimizing large language model (LLM) serving stacks through cross-layer
  collaboration, particularly addressing the challenge of maximizing GPU utilizatio...
resource: https://www.youtube.com/watch?v=XiuqiIpGoOg
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

The presentation, led by representatives from Cognality, AMD, and AXeller, focused on optimizing large language model (LLM) serving stacks through cross-layer collaboration, particularly addressing the challenge of maximizing GPU utilization for heterogeneous AI workloads.
The speakers described how static GPU allocation leads to resource waste and proposed consolidating GPUs into a shared Kubernetes-managed cluster, leveraging the Q scheduling system for priority, quota, and preemption management.
They demonstrated how fine-grained GPU fractionalization—dividing GPU memory at the gigabyte level and virtualizing GPUs—enables multiple agents and background tasks to efficiently share high-end AMD GPUs, such as the MI325, without sacrificing latency or performance.
A live demo illustrated how agentic workflows, using prompt chaining across three agents, could be run alongside background jobs by dynamically allocating fractional GPU resources, thereby improving overall cluster efficiency.
The session concluded with a Q&A clarifying that the approach generalizes to any Kubernetes-managed resource and that GPU partitioning can be as fine as 1 GB of memory or 1% compute power, with strict enforcement of resource limits by the fractional GPU solution.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speakers represent different layers of the AI serving stack: model application, hardware acceleration, and infrastructure orchestration.   |
|   2 | AI workloads are heterogeneous, with varying model sizes, input/output shapes, and unpredictable traffic bursts.                           |
|   3 | Agentic workflows fall into two patterns: human-controlled deterministic chaining and LLM-controlled dynamic planning.                     |
|   4 | Most production systems use deterministic prompt chaining and structured output.                                                           |
|   5 | Main problem addressed: freeing up GPU resources to pack more workloads, such as collocating agents on the same AMD GPU.                   |
|   6 | Solution: fine-grained GPU fractionalization at the gigabyte level, combined with Q for quota, priority, and preemption.                   |
|   7 | GPUs are expensive and often in short supply; static allocation leads to waste.                                                            |
|   8 | Pooling GPUs into a shared cluster and using Kubernetes for scheduling increases utilization.                                              |
|   9 | Different workloads have competing priorities (latency-sensitive agentic workflows vs. batch processing/training).                         |
|  10 | Q provides priority scheduling, minimum quota guarantees, and borrowing limits for fair resource sharing.                                  |
|  11 | GPU fractionalization allows dividing GPU memory among agents, consolidating workloads, and freeing GPUs for other tasks.                  |
|  12 | Demo uses three AMD MI325 GPUs with high memory bandwidth and capacity, supporting multi-user GPU virtualization.                          |
|  13 | Two workloads demonstrated: agentic workflow (three agents in a prompt chain) and a GPU-intensive background task.                         |
|  14 | Kubernetes setup includes Q and AMD GPU/memory fractionalization software.                                                                 |
|  15 | Agentic workflow: image input processed by three agents (image captioning, reasoning, planning), each with different compute/memory needs. |
|  16 | Demo shows before/after: dedicated GPU per agent (wasteful) vs. fractional GPU (all agents on one GPU, background tasks run concurrently). |
|  17 | Fractional GPU resource defined as 1GB units in Kubernetes; Q manages quotas and preemption.                                               |
|  18 | Fractional GPU solution ensures agents only allocate their assigned memory, prev                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XiuqiIpGoOg)
