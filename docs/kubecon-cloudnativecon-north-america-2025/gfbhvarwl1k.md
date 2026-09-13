---
type: Video Note
title: "Tutorial: Intelligent Failure: Using AI To Push Your Cluster To the Br... James Ilse & Michael Levan"
description: "In this tutorial, James Isles and Michael Leavon from Solo discuss practical approaches to deploying and managing AI agents in production environments, with a focus on Kubernetes clusters. They introduce key concepts such as large language..."
resource: https://www.youtube.com/watch?v=gFBhVarWL1k
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this tutorial, James Isles and Michael Leavon from Solo discuss practical approaches to deploying and managing AI agents in production environments, with a focus on Kubernetes clusters.
They introduce key concepts such as large language models (LLMs), agents, and the Model Context Protocol (MCP), explaining how agents interact with LLMs and MCP servers to extend functionality and automate tasks.
The presenters emphasize the importance of security, observability, and layered defenses—drawing parallels to historical fortification strategies—to protect AI workloads from common vulnerabilities like prompt injection and unauthorized access.
They demonstrate open-source tools such as Kagent and Agent Gateway, which facilitate scalable, declarative agent deployment and provide mechanisms for monitoring, rate limiting, and prompt guarding.
Throughout, they stress the need for careful permission management, community-driven tool sharing, and ongoing vigilance as the AI landscape rapidly evolves, highlighting both the opportunities and risks of integrating AI into production systems.
# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tutorial focuses on using AI to manage clusters and AI in production.                                                                                                                 |
|   2 | Presenters: James Isles (Solo) and Michael Leavon (Solo, Ria Group).                                                                                                                  |
|   3 | James has extensive experience as a field engineer and SRE, working with many companies on AI production issues.                                                                      |
|   4 | Many companies want to put AI into production but face significant challenges, especially around security and adoption.                                                               |
|   5 | Early attempts at load testing systems failed due to brittleness and lack of adoption; AI can help smooth these issues by interpreting human language and integrating into pipelines. |
|   6 | AI adoption is pressured by leadership, but failure rates are high; less than 5% of AI workloads are in production.                                                                   |
|   7 | Common issues: Shadow IT, unsecured servers, agents with excessive privileges, prompt injection attacks, and data exfiltration.                                                       |
|   8 | Security can be improved with gateways, service mesh, prompt guards, and network isolation.                                                                                           |
|   9 | Defense in depth is essential; multiple layers of security are needed, not just perimeter defenses.                                                                                   |
|  10 | Real-world incidents include leaked API keys and high bills due to lack of governance and authentication.                                                                             |
|  11 | AI components explained: datasets, models, LLMs, clients, agents, MCP servers.                                                                                                        |
|  12 | MCP (Model Context Protocol) is a new standard for giving agents tools; exposes functions to extend agent knowledge.                                                                  |
|  13 | Service mesh (e.g., Istio) is increasingly important for observability, security, and controlling agent actions.                                                                      |
|  14 | Agent gateway and K gateway are used for secure, observable, and performant AI networking.                                                                                            |
|  15 | AI gateways must handle stateful, context-aware traffic, not just stateless microservices.                                                                                            |
|  16 | K agent is used to host and scale agents declaratively in Kubernetes.                                                                                                                 |
|  17 | Demo showed using K agent to diagnose and fix Kubernetes pod issues, monitor token usage, and scale deployments.                                                                      |
|  18 | Limiting the number of MCP tools per agent reduces hallucinations.                                                                                                                    |
|  19 | Observability tools (e.g., Kali) provide metrics and traces for AI workloads.                                                                                                         |
|  20 | Prompt guards in agent gateway can block dang                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gFBhVarWL1k)