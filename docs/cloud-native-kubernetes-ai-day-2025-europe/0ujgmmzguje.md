---
layout: default
title: "The State of GenAI & ML in the Cloud Native Ecosystem - Alejandro Saucedo & Bartosz Ocytko, Zalando"
nav_order: 2
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "At CubeCon, Alejandro Saledo and Bartosh from Zalando presented on the state of Generative AI and Machine Learning within the cloud-native ecosystem, highlighting the rapid evolution from simple RA..."
resource: "https://www.youtube.com/watch?v=0uJGmMZGUJE"
youtube_stats:
  view_count: 1882
  like_count: 31
  channel_subscriber_count: 141000
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

At CubeCon, Alejandro Saledo and Bartosh from Zalando presented on the state of Generative AI and Machine Learning within the cloud-native ecosystem, highlighting the rapid evolution from simple RAG patterns to complex agentic systems.
They discussed key challenges such as the explosion of tools, security risks like prompt injection and data poisoning, and the difficulty of managing multiple model providers and API keys.
The speakers emphasized a shift from model-centric to data-centric architectures, advocating for the use of Kubernetes-native abstractions, such as Custom Resource Definitions (CRDs) and MCP servers, to standardize interfaces and orchestrate workflows.
They also addressed the need for robust observability, security guardrails, and the redefinition of roles, such as the emerging "AI Engineer," to manage the complexity of these systems.
Finally, they advised practitioners to exercise restraint, noting that not every problem requires an AI or agentic solution, and recommended resources like Chip Huyen’s book on AI engineering for further learning.

# Main Points

|   # | Main point                                                                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation discusses the state of Generative AI and Machine Learning within the cloud-native ecosystem, highlighting the rapid explosion of tools and the resulting complexity for developers.          |
|   2 | Zalando, a leading European fashion organization with 51 million active customers, utilizes AI for forecasting, pricing, search, and generative use cases like virtual try-ons and conversational assistants. |
|   3 | The AI market is valued at nearly 400 billion dollars and is projected to grow fivefold over five years, with 100 million workers currently in the AI space.                                                  |
|   4 | Retrieval-Augmented Generation (RAG) serves as a foundational pattern for building agentic systems, evolving from simple knowledge access to complex multi-step workflows.                                    |
|   5 | Challenges in model selection include the difficulty of validating if new models provide better performance or revenue contributions without extensive A/B testing.                                           |
|   6 | Generative UI allows models to determine the most appropriate interface components for user experience, such as selecting a map component for ZIP code inputs.                                                |
|   7 | Security risks in agentic systems include prompt injection, tool misuse with wrong parameters, and rogue agents that may attempt jailbreaks or enter endless loops burning tokens.                            |
|   8 | Developers should focus 80% of their time on use case workflows and context collection rather than building underlying infrastructure or model hubs.                                                          |
|   9 | Architectural thinking must shift from model-centric to data-centric systems, where data flow, contracts, and business value define the system's success.                                                     |
|  10 | Cloud-native tools like Kagent, LangChain, and LangGraph are emerging to manage agent orchestration, while Custom Resource Definitions (CRDs) help abstract LLM and agent configurations in Kubernetes.       |
|  11 | MCP servers and routers are becoming standard infrastructure components for enabling agents to interact with services, storage, and cloud-based models.                                                       |
|  12 | Traditional Machine Learning remains relevant for tasks like sentiment analysis and classification, requiring robust MLOps stacks with tools like Ray, Airflow, and Kubeflow.                                 |
|  13 | Hardware scheduling for heterogeneous resources like GPUs and TPUs is addressed by projects such as Kueue and Volcano, which enable priority queuing and resource allocation.                                 |
|  14 | Observability for agentic systems requires specific tools like Langfuse to handle LLM-specific debugging, reproducibility, and drift detection beyond traditional microservice monitoring.                    |
|  15 | Security threats in the AI space include data poisoning via AI crawlers, memory poisoning, remote code execution, and identity spoofing, necessitating new vulnerability taxonomies.                          |
|  16 | The role of the AI Engineer is still being defined, moving away from the "unicorn" expectation toward segregated roles and responsibilities within the agentic development lifecycle.                         |
|  17 | A key best practice is recognizing that not all problems require AI or agents; solutions should be chosen based on specific business value rather than applying AI as a universal hammer.                     |
|  18 | Recommended resources for understanding AI engineering foundations include Chip Huyen's book on AI engineering and Sebastian Raschka's work on LLMs.                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0uJGmMZGUJE/hqdefault.jpg)](https://www.youtube.com/watch?v=0uJGmMZGUJE)

[Watch on YouTube](https://www.youtube.com/watch?v=0uJGmMZGUJE)
