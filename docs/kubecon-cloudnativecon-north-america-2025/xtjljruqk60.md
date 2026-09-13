---
layout: default
title:
  "Scaling Generative AI: Building Production-Ready LLM Applications - Daniel
  Oh & Kevin Dubois, IBM"
nav_order: 272
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this session, Daniel O and Kevin, both experienced Java developers
  and contributors to CNCF, discuss building production-ready AI applications with
  a focus on open-source tools and improving developer experience. They emphasize
  the impor...
resource: https://www.youtube.com/watch?v=XtJLJRUQk60
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

In this session, Daniel O and Kevin, both experienced Java developers and contributors to CNCF, discuss building production-ready AI applications with a focus on open-source tools and improving developer experience.
They emphasize the importance of integrating AI models, such as LLMs, into traditional applications using frameworks like Quarkus and LangChain4j, demonstrating how developers can quickly set up generative and agentic AI capabilities with minimal code.
The presenters highlight key considerations for production, including prompt engineering, guardrails, observability, and orchestration of multiple agents and tools, particularly in Kubernetes environments.
They showcase a live demo of creating an AI-infused Java application, leveraging Quarkus’s development features and MCP integration, and explain how these tools streamline development and deployment.
Finally, they introduce Open Data Hub as an opinionated platform for scaling AI solutions in production, encouraging developers to experiment locally and then transition to robust, cloud-native infrastructures.

# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Focus on building production-ready AI applications using open source tools and projects                                      |
|   2 | Emphasis on improving developer experience for integrating AI into traditional applications                                  |
|   3 | AI has evolved from conceptual ideas to agentic AI capable of autonomous actions                                             |
|   4 | Distinction between AI models (LLMs, image generation, etc.) and AI applications (Java, Python, JavaScript, etc.)            |
|   5 | Libraries, tools, or platforms are needed to connect AI models with applications                                             |
|   6 | Goal: Enable traditional application developers to integrate AI, not just AI engineers                                       |
|   7 | Steps to integrate LLMs:                                                                                                     |
|   8 | Choose an LLM provider (OpenAI, Gemini, open-source, etc.)                                                                   |
|   9 | Experiment with prompting and adding data                                                                                    |
|  10 | Select appropriate stack/framework (e.g., Java, Python)                                                                      |
|  11 | Use libraries to prompt models and handle responses                                                                          |
|  12 | Manage state, create agents, and operationalize for production                                                               |
|  13 | Java developers can use Quarkus and LangChain4j for AI integration                                                           |
|  14 | Adding dependencies (e.g., Quarkus LangChain4j OpenAI) enables model calls from code                                         |
|  15 | Example: Creating a Kubernetes deployment manifest via AI agent in Java                                                      |
|  16 | Production considerations: prompt engineering, guardrails, observability, fault tolerance, tool calling, agent orchestration |
|  17 | Optimize Java frameworks for Kubernetes scalability                                                                          |
|  18 | Quarkus dev mode offers live coding and integrated dev UI for rapid development                                              |
|  19 | LangChain4j inspired by Python’s LangChain, with unique features for Java                                                    |
|  20 | Demonstrated creating a generative AI agent in Java with minimal code using annotations                                      |
|  21 | System messages (prompts) are crucial for LLM behavior and context                                                           |
|  22 | MCP integration allows tool access and agentic AI behavior                                                                   |
|  23 | Quarkus dev UI provides out-of-the-box chat UI and ecosystem integration (Grafana, Swagger, etc.)                            |
|  24 | Logs, metrics, and traces available for monitoring and observability                                                         |
|  25 | Open Data Hub offers an opinionated platform for AI model training, deployment, and integration                              |
|  26 | Recommended workflow: local experimentation, production deployment                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XtJLJRUQk60)
