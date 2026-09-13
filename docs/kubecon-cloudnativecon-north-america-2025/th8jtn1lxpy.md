---
type: Video Note
title: "Agent-Driven MCP for AI Workloads on Kubernetes - Ganeshkumar Ashokavardhanan & Qinghui Zhuang"
description: "In this session, Ganesh Kumar from the Azure Kubernetes Service team discusses the challenges and opportunities of using AI agents to manage AI workloads on Kubernetes, focusing on GPU infrastructure. He shares personal experiences, includi..."
resource: https://www.youtube.com/watch?v=tH8jTN1LXPY
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Ganesh Kumar from the Azure Kubernetes Service team discusses the challenges and opportunities of using AI agents to manage AI workloads on Kubernetes, focusing on GPU infrastructure.
He shares personal experiences, including difficulties in selecting appropriate resources for deploying large models and handling GPU-related incidents, which motivated the exploration of autonomous, agent-driven infrastructure management.
The talk introduces the concept of MCP (Model Control Protocol) as a standardized way for AI agents to interact with external tools and resources, and contrasts the relative maturity of AI coding agents with the complexities and risks of using agents for infrastructure management, such as non-determinism, sparse training data, and higher blast radius for errors.
A live demo illustrates how an AI agent can autonomously deploy a model on Kubernetes by clarifying requirements, selecting resources, generating manifests, and handling errors, though current limitations prevent fully end-to-end production readiness.
The presentation concludes by highlighting key considerations for productionizing such agents—including security, guardrails, context management, and benchmarking—and emphasizes the rapidly evolving nature of this field, encouraging further exploration and development.
# Main Points

|   # | Main point                                                                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on agent-driven MCP for AI workloads on Kubernetes.                                                                                                                                                                   |
|   2 | Ganesh Kumar (Azure Kubernetes Service team) specializes in GPU infrastructure for Kubernetes.                                                                                                                                        |
|   3 | Co-presenter Chinuay works on Kubernetes for AI, maintains Kubernetes AI tool chain operator (CNCF sandbox project).                                                                                                                  |
|   4 | Motivation: Challenges deploying Llama 3 405V model on Kubernetes, including memory, GPU selection, latency, and throughput.                                                                                                          |
|   5 | Production incident: GPU performance degraded after node image/driver upgrade, impacting major user demo.                                                                                                                             |
|   6 | Vision: AI agents autonomously manage infrastructure (configuration, deployment, remediation, monitoring).                                                                                                                            |
|   7 | Audience poll: Most have used AI coding agents; few have used AI agents for infrastructure; average prediction for AI-managed infra is ~7 years.                                                                                      |
|   8 | Agentic terms:                                                                                                                                                                                                                        |
|   9 | Agent: AI-driven loop that plans, decides, acts.                                                                                                                                                                                      |
|  10 | Tools: Operations with typed inputs/outputs.                                                                                                                                                                                          |
|  11 | Context: All content for model inference.                                                                                                                                                                                             |
|  12 | MCP: Protocol for tool/resource discovery; open-source standard for connecting AI apps to external systems.                                                                                                                           |
|  13 | Managing AI infra on Kubernetes involves model selection, packaging, GPU/runtime/OS selection, user estimation, scheduling, autoscaling, cost, and observability.                                                                     |
|  14 | Coding agents benefit from deterministic behavior, abundant training data, and safer changes; infra agents face non-determinism, sparse data, and higher risk.                                                                        |
|  15 | Demo: Agent uses MCP servers (Hugging Face, cloud vendor, kit) to deploy a model on Kubernetes, clarifies requirements, selects GPU, generates manifests, creates node pool, handles errors, verifies deployment, and tests endpoint. |
|  16 | Fully managed GPU node pool is a new Azure feature; agent can discover and use it via documentation search.                                                                                                                           |
|  17 | Productionizing agents requires addressing security (auth, prompt injection), sandboxing, guardrails, context engineering, and memory management.                                                                                     |
|  18 | Current challenges: Reliable chaining of MCP providers, lack of benchmarks for infra agents, context window limitations.                                                                                                              |
|  19 | Field                                                                                                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tH8jTN1LXPY)