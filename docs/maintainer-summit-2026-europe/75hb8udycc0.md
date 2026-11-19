---
layout: default
title: "Keynote: Building AI in the Open: How the Cloud Native Community Sha... Moderated by: Mario Fahlandt"
nav_order: 4
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "This keynote addresses the evolving infrastructure required to support AI workloads within the Kubernetes ecosystem, focusing on standardization, efficiency, and observability."
resource: "https://www.youtube.com/watch?v=75hB8udYcc0"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

This keynote addresses the evolving infrastructure required to support AI workloads within the Kubernetes ecosystem, focusing on standardization, efficiency, and observability.
Speakers from the CNCF and various industry partners detailed the progress of the Kubernetes AI Conformance Program, which ensures that AI workloads can run reliably across different platforms by establishing requirements for accelerators, networking, and scheduling.
The presentation highlighted the Dynamic Resource Allocation (DRA) feature, which allows for more flexible device management, and introduced the LLM-D project, a new initiative designed to optimize distributed inference by handling complex tasks like disaggregated serving and multi-node deployments.
Additionally, the session covered the LWS Operator for managing leader-worker pod groups and the role of OpenTelemetry in standardizing AI observability to help debug agent behaviors and reduce operational fragmentation.
A concluding panel discussed the balance between large and small language models, noting that while trends favor larger models for complex tasks, cost efficiency and the rise of reinforcement learning pipelines are driving the adoption of smaller, specialized models for specific enterprise use cases.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Kubernetes AI conformance program was launched to ensure AI workloads run consistently across compliant clusters, covering accelerators, DRA, networking, and scheduling.            |
|   2 | Dynamic Resource Allocation (DRA) became GA, offering a flexible way to advertise and request devices, though Kubernetes does not include built-in DRA drivers.                          |
|   3 | Any CNCF graduated project can create its own conformance program to provide vendors with a standard for compliant software, supported by CNCF legal and branding resources.             |
|   4 | The LMD project addresses the complexity of distributed AI inference by building on proven technologies like the Gateway API inference extension to handle state and variable requests.  |
|   5 | LMD focuses on optimizing disaggregated inference, multi-node deployments, and prefix caching to meet strict latency and throughput SLOs.                                                |
|   6 | Leader Worker Set (LWS) groups pods into logical computing units, facilitating the deployment of LLMs across multiple GPUs and enabling coordinated failure handling.                    |
|   7 | The LWS roadmap includes improvements for gang scheduling, DRA integration, and disaggregated serving to separate compute-bound prefill and memory-bound decode phases.                  |
|   8 | A new disaggregated set operator is being developed to manage rolling updates and maintain the ratio between prefill and decode replicas in LWS deployments.                             |
|   9 | OpenTelemetry is working to standardize AI observability telemetry, addressing fragmentation from new vendors and enabling AI agents to analyze incidents and debug agent behavior.      |
|  10 | Small language models are gaining traction for agentic workflows that dispatch tasks to specialized sub-models, improving GPU utilization compared to single large models.               |
|  11 | GPU partitioning and scheduler hints are being explored to optimize device allocation, as standard device plugins lack cluster-wide visibility for optimal placement.                    |
|  12 | The Himei project aims to implement lightweight GPU partitioning using DRA capabilities, allowing schedulers to interact with drivers for better topology-aware allocation.              |
|  13 | AI adoption is expanding beyond coding to include AI for systems, such as optimizing compilers, runtimes, and troubleshooting cluster issues via AI agents.                              |
|  14 | The industry is shifting from a "hype" phase to realistic cost-efficiency, balancing the use of large frontier models with smaller, fine-tuned models for specific enterprise use cases. |
|  15 | Reinforcement learning pipelines are becoming standardized, enabling the customization of open-source base models for specific tasks to reduce inference costs.                          |
|  16 | Cost attribution remains a challenge, with efforts underway to improve telemetry to understand where expenses arise from inefficient AI conversations or token usage.                    |
|  17 | The agentic pattern is driving rapid token demand and productivity gains across the tech industry, with predictions that it will expand into non-technical enterprise roles.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/75hB8udYcc0/hqdefault.jpg)](https://www.youtube.com/watch?v=75hB8udYcc0)

[Watch on YouTube](https://www.youtube.com/watch?v=75hB8udYcc0)
