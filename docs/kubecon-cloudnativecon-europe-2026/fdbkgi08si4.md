---
layout: default
title:
  "Cloud Native Theater | Cloud Native University: AI + Kubernetes: What Beginners...
  Michael Forrester"
nav_order: 44
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker discusses the evolving landscape of AI workloads and Kubernetes,
  emphasizing that while AI is rapidly being integrated into workflows, most organizations
  are leveraging existing, generally trained models and platforms like Kuber...
resource: https://www.youtube.com/watch?v=FdBkGi08SI4
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses the evolving landscape of AI workloads and Kubernetes, emphasizing that while AI is rapidly being integrated into workflows, most organizations are leveraging existing, generally trained models and platforms like Kubernetes rather than building custom solutions.
Key Kubernetes features such as Device Resource Assignment (DRA), in-place pod resizing, and gang scheduling are highlighted as important advancements for efficiently managing AI workloads.
The speaker recommends focusing on a core set of technologies—including Kubernetes scheduling, distributed training, and model serving tools like Kserve and KNative—while cautioning beginners to be mindful of security concerns with agent-based infrastructure.
A free, structured learning path is provided via a public repository, encouraging practitioners to build foundational knowledge and reassuring them that existing skills in infrastructure, monitoring, and security remain highly relevant in the AI era.
The overall message is to stay calm, focus on learning a few new tools, and recognize that most of the necessary expertise is already in place.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk covers a narrow, opinionated set of technologies for AI workloads on Kubernetes.                                                                                                       |
|   2 | General-purpose, broadly trained AI models often outperform narrowly trained models in specific domains.                                                                                        |
|   3 | Most people use existing AI models and platforms rather than building their own.                                                                                                                |
|   4 | Kubernetes is a major platform for running AI workloads.                                                                                                                                        |
|   5 | Nvidia has contributed features to Kubernetes, such as Device Resource Reporting API (DRRA), enabling GPU fractionation and customization.                                                      |
|   6 | In-place pod resize and gang scheduling are important Kubernetes features for AI workloads.                                                                                                     |
|   7 | Gang scheduling ensures distributed jobs only run when all required resources are available.                                                                                                    |
|   8 | The recommended learning path includes: adapting Kubernetes for AI workloads, fair scheduling and topology awareness (e.g., Q, Volcano, Kai), distributed training, and long-running inference. |
|   9 | Kserve, KNative, LMMD, Gateway API, Kerve, and other tools are highlighted for model serving and deployment.                                                                                    |
|  10 | Gateway API is working on routing model-to-model traffic.                                                                                                                                       |
|  11 | Labs and repos use CPU-based models; GPU is not required for initial learning.                                                                                                                  |
|  12 | The Agentic AI Foundation (Linux Foundation) is driving adoption of projects like MCP, Goose, and agents.mmd.                                                                                   |
|  13 | Beginners should focus on MCP servers; operators should focus on Kubernetes features and scheduling.                                                                                            |
|  14 | Caution is advised before deploying AI agents in production due to security concerns.                                                                                                           |
|  15 | Docker has released microVMs for agent isolation; agents can escape traditional sandboxes.                                                                                                      |
|  16 | After mastering core Kubernetes features, explore KAgent, Toolhive, and Agent Gateway.                                                                                                          |
|  17 | The cloud-native-ai-lab repo provides a free, structured learning path for AI on Kubernetes.                                                                                                    |
|  18 | Existing skills in platforms, tooling, monitoring, and security remain relevant for AI workloads.                                                                                               |
|  19 | Adapting to AI workloads mainly requires learning a few new tools and concepts; most existing knowledge is still applicable.                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FdBkGi08SI4)
