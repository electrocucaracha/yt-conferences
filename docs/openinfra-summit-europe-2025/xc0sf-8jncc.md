---
layout: default
title: Talking with Your Infrastructure  AI Agents for OpenStack and Kubernetes Infra
nav_order: 29
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'Sashan Acharia from Rackspace presents a high-level overview of "Talking with Your Infrastructure," a project aimed at using AI agents to automate and simplify the management of OpenStack and Kuber...'
resource: "https://www.youtube.com/watch?v=xC0sf-8JnCc"
youtube_stats:
  view_count: 214
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

Sashan Acharia from Rackspace presents a high-level overview of "Talking with Your Infrastructure," a project aimed at using AI agents to automate and simplify the management of OpenStack and Kubernetes environments.
The presentation explains that while Large Language Models (LLMs) are powerful prediction engines, they lack specific context and reasoning capabilities, making them insufficient for infrastructure tasks without additional support.
To address this, the solution integrates AI agents that act as a cognitive layer, utilizing function calling, Retrieval-Augmented Generation (RAG) for domain-specific knowledge, and fine-tuned models to execute precise API calls and troubleshoot issues.
A live demonstration showcases the system’s ability to list regions, check cluster health, create new instances, and retrieve specific troubleshooting steps from a curated knowledge base.
The talk concludes by highlighting critical integration challenges, such as ensuring security, trust boundaries, multi-tenancy, and policy enforcement, while emphasizing the goal of creating a collaborative, Jarvis-like AI system for infrastructure operations.

# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The presentation introduces AI agents for managing infrastructure like OpenStack and Kubernetes, aiming to create a Jarvis-like system for automated operations.                                 |
|   2 | Large Language Models (LLMs) function as prediction engines that predict the next token in a sequence, relying on context windows for short-term memory rather than true reasoning.              |
|   3 | LLMs are not a source of truth and can provide incorrect information, so they must be used with caution in troubleshooting and operational tasks.                                                |
|   4 | A simple LLM wrapper is insufficient for infrastructure management because it lacks specific context and domain knowledge required for accurate actions.                                         |
|   5 | AI agents act as autonomous software that interfaces with infrastructure APIs, documents, and logs to reason with context and execute specific actions.                                          |
|   6 | The agent workflow involves a handover agent routing user queries to specialized agents, such as OpenStack or Kubernetes agents, which then query relevant APIs and return results.              |
|   7 | Initial attempts using simple function calls were error-prone, and adding Retrieval-Augmented Generation (RAG) introduced challenges related to data quality and document structure.             |
|   8 | The final effective strategy involves fine-tuning LLMs like GPT-4 or Llama on specific infrastructure data to improve function calling accuracy and context understanding.                       |
|   9 | Model selection is critical, requiring models that are effective at function calling and small enough to run on limited GPU resources, such as two GPUs.                                         |
|  10 | RAG integration requires a properly structured vector database and high-quality domain documentation to provide accurate context to the LLM.                                                     |
|  11 | The system architecture includes a frontend interface, a handover agent, specialized infrastructure agents, and a backend that manages API calls and data retrieval.                             |
|  12 | Function definitions must specify required parameters, such as instance name and region, allowing the agent to execute commands like creating an OpenStack instance.                             |
|  13 | The agent flow processes user input through the handover agent to the specific infrastructure agent, which calls the LLM to determine the correct function and parameters.                       |
|  14 | RAG enables the system to retrieve verified answers from curated knowledge bases, such as Rackspace cloud documentation, for troubleshooting specific issues.                                    |
|  15 | Integration challenges include ensuring security, trust boundaries, data silos, multi-tenancy, and scalability across multiple regions and clusters.                                             |
|  16 | Policy guardrails and validation pipelines are necessary to ensure agents operate within pre-approved boundaries and provide accurate, safe responses.                                           |
|  17 | Key takeaways emphasize the importance of data unification, trust and safety measures, and building cognitive, collaborative AI systems for infrastructure management.                           |
|  18 | Live demonstrations showed the agent successfully listing regions, checking Kubernetes cluster health, creating OpenStack instances, and retrieving troubleshooting steps from a knowledge base. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xC0sf-8JnCc/hqdefault.jpg)](https://www.youtube.com/watch?v=xC0sf-8JnCc)

[Watch on YouTube](https://www.youtube.com/watch?v=xC0sf-8JnCc)
