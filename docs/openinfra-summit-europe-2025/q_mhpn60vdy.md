---
layout: default
title: "The Fast and the Curious: Building Scalable AI Platforms with Kubernetes and OpenStack"
nav_order: 53
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The first presentation, delivered by Bat from Mirantis, explores the synergy between Kubernetes and OpenStack to address the growing demands of AI infrastructure."
resource: "https://www.youtube.com/watch?v=q_Mhpn60vDY"
youtube_stats:
  view_count: 146
  like_count: 3
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

The first presentation, delivered by Bat from Mirantis, explores the synergy between Kubernetes and OpenStack to address the growing demands of AI infrastructure.
Bat highlights that while hyperscalers offer availability, they present significant challenges regarding cost, GPU scarcity, vendor lock-in, and data sovereignty.
To mitigate these issues, the session introduces Cordant, an open-source platform built on Cluster API and k0s, which enables centralized management of Kubernetes clusters on OpenStack.
By utilizing a single YAML file for cluster deployment and service management, Cordant simplifies the provisioning of AI-ready environments, such as those with NVIDIA GPU operators, while providing integrated observability and state management through tools like Flux and Prometheus.
The second presentation, by Sulosan Acharya from Rackspace, focuses on "talking with your infrastructure" by leveraging AI agents and Large Language Models (LLMs) to automate OpenStack operations.
Acharya explains that while LLMs are powerful prediction engines, they lack specific infrastructure context, necessitating the use of AI agents that can interface with APIs, logs, and documentation.
The proposed solution involves fine-tuning models like GPT-4 or Llama for specific OpenStack tasks and integrating Retrieval-Augmented Generation (RAG) to ground responses in curated knowledge bases.
This architecture allows users to perform complex actions, such as provisioning instances or troubleshooting build failures, through natural language commands, effectively creating a "Jarvis-like" system for cloud management.
However, the speaker emphasizes the critical need for robust security guardrails, strict access controls, and validation pipelines to ensure trust and safety when deploying autonomous agents in production environments.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes provides a common centralized control plane across multiple cloud providers, enabling ecosystem success despite potentially superior vendor-specific technologies.                 |
|   2 | AI infrastructure requires efficiency, scalability, and sovereignty, with hyperscalers facing challenges in GPU availability, vendor lock-in, high costs, and data compliance.                |
|   3 | OpenStack is a proven solution for on-premises infrastructure, supporting scenarios from extreme edge deployments to large-scale data centers.                                                |
|   4 | Cordant is an open-source platform based on Cluster API that automates Kubernetes infrastructure provisioning, state management, and observability.                                           |
|   5 | Cordant simplifies operations by centralizing cluster and service configurations into a single YAML file, reducing the need for multiple complex files.                                       |
|   6 | The Cordant catalog offers over 70 open-source applications and supports private Helm charts for deploying services like the NVIDIA GPU operator.                                             |
|   7 | A live demo demonstrated provisioning a Kubernetes cluster on OpenStack via OVH Cloud, including the installation of GPU drivers and scheduling AI workloads.                                 |
|   8 | AI agents combined with Large Language Models (LLMs) can automate infrastructure management by interpreting user intent and executing API calls.                                              |
|   9 | LLMs alone are insufficient for infrastructure tasks because they lack specific context and may hallucinate, requiring agents to provide grounding and state management.                      |
|  10 | Effective AI agent implementation involves fine-tuning models for specific tools, integrating Retrieval-Augmented Generation (RAG) for domain knowledge, and defining precise function calls. |
|  11 | Rackspace developed a platform to manage OpenStack and Kubernetes using AI agents, allowing users to provision instances and troubleshoot issues via natural language.                        |
|  12 | Security and trust are critical challenges, requiring policy guardrails, access controls, and validation pipelines to ensure agents operate within pre-approved boundaries.                   |
|  13 | The future of infrastructure operations is moving toward cognitive, collaborative systems that reduce manual effort and enhance troubleshooting capabilities.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/q_Mhpn60vDY/hqdefault.jpg)](https://www.youtube.com/watch?v=q_Mhpn60vDY)

[Watch on YouTube](https://www.youtube.com/watch?v=q_Mhpn60vDY)
