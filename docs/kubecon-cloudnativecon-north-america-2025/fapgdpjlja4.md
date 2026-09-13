---
type: Video Note
title: "Resilient by Design: Building Durable AI Agents on Kubernetes - Yaron Schneider, Diagrid"
description: "Iron Schneider, CTO and co-founder of Diagrid and co-creator of the Dapper project, discusses the evolution and challenges of automation in software engineering, particularly within the CNCF ecosystem. He explains how the drive for automati..."
resource: https://www.youtube.com/watch?v=FApGdPJlJA4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Iron Schneider, CTO and co-founder of Diagrid and co-creator of the Dapper project, discusses the evolution and challenges of automation in software engineering, particularly within the CNCF ecosystem.
He explains how the drive for automation has led to increasingly complex systems, culminating in the rise of AI agents that can autonomously use tools and collaborate with other agents to solve problems.
However, this increased autonomy introduces nondeterminism and reliability challenges, especially as agentic workflows scale and interact with external systems, potentially leading to high costs and operational risks.
Schneider introduces Dapper agents, a Python-based, vendor-neutral agentic framework within CNCF, designed to ensure reliable, stateful, and observable execution of both deterministic and nondeterministic workflows, even across distributed Kubernetes environments.
Through demonstrations, he highlights Dapper agents’ capabilities in workflow durability, observability integration, and seamless recovery from failures, emphasizing its suitability for building robust, scalable AI-driven automation.
# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Iron Schneider is CTO and co-founder of Diagrid, co-creator of Dapper and Kea.                                                                              |
|   2 | The talk centers on automation in DevOps, software engineering, and the CNCF ecosystem.                                                                     |
|   3 | Automation has led to a cycle of creating tools to automate previous automation, expanding the CNCF landscape.                                              |
|   4 | Kubernetes automates containers, runtimes, networking, and more; service meshes and tools further automate these layers.                                    |
|   5 | The rise of agents represents the next step in automation, potentially automating jobs themselves.                                                          |
|   6 | Agents gain power by being given autonomy and access to tools, enabling them to reason and act toward goals.                                                |
|   7 | Multi-agent systems allow agents to collaborate, increasing complexity and automation potential.                                                            |
|   8 | More autonomy increases automation and ROI but also raises risk due to nondeterminism.                                                                      |
|   9 | Traditional systems are deterministic; agentic systems introduce nondeterminism, making workflows unpredictable and harder to debug.                        |
|  10 | Reliability and observability are critical for agentic workflows, especially as they scale.                                                                 |
|  11 | Semi-deterministic workflows (e.g., research agents) have known steps but rely on LLMs, introducing some unpredictability.                                  |
|  12 | Both deterministic and nondeterministic workflows require durable execution and automatic failure recovery.                                                 |
|  13 | Dapper agents is an agentic framework in Python, part of CNCF, designed for reliability, durability, and observability at scale.                            |
|  14 | Dapper agents support multi-agent eventing, state hydration, and seamless integration with Kubernetes.                                                      |
|  15 | Dapper provides APIs for workflow orchestration, pub/sub, state management, and service discovery.                                                          |
|  16 | Dapper agents integrate with observability tools like Zipkin, Jaeger, and Phoenix, supporting open standards.                                               |
|  17 | Demonstrations showed Dapper agents' ability to recover from crashes and maintain workflow state in both semi-deterministic and nondeterministic scenarios. |
|  18 | Dapper agents prevent duplicate workflow execution in distributed environments.                                                                             |
|  19 | Dapper supports over 30 databases and                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FApGdPJlJA4)