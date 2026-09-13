---
layout: default
title:
  "Smarter Together: Orchestrating Multi-Agent AI Systems... Ana Maria Lopez
  Moreno & Sharon Camacho"
nav_order: 283
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Sharon Camacho and Anna Lopez discuss the challenges
  and solutions involved in integrating multiple AI agents developed by different
  teams across various cloud platforms, such as Azure and GCP. They highlight the
  diffi...
resource: https://www.youtube.com/watch?v=JnybchLqKXc
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

In this presentation, Sharon Camacho and Anna Lopez discuss the challenges and solutions involved in integrating multiple AI agents developed by different teams across various cloud platforms, such as Azure and GCP.
They highlight the difficulties of connecting isolated, monolithic AI systems and propose a collaborative, orchestrated architecture using Kubernetes, agent-to-agent protocols, and MCP (Model Context Protocol) to enable seamless communication and tool sharing among agents.
Their approach involves using agent cards to specify each agent’s skills, allowing an orchestrator to route user requests to the appropriate agents, and leveraging containers for scalability and flexibility.
They demonstrate their solution with a multi-agent system deployed on Azure Kubernetes Services, featuring agents with different functionalities and a simple user interface for interaction.
The presenters also emphasize the importance of managing the lifecycle and versioning of agents and prompts, drawing parallels to machine learning model management, and outline future steps to improve deployment pipelines, environment management, and generative AI operations.

# Main Points

|   # | Main point                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion on integrating multiple AI agents developed by different teams, frameworks, and clouds.                                      |
|   2 | Goal: Centralize and enable agents to work smarter together.                                                                            |
|   3 | Presenters: Sharon Kamacho (Data Scientist) and Anna Lopez (Microsoft Senior Partner Solution Architect, Data & AI).                    |
|   4 | Challenge: Connecting isolated, monolithic AI systems across fragmented cloud environments (GCP, AWS, Azure).                           |
|   5 | Focus on collaborative systems over smarter individual models.                                                                          |
|   6 | Orchestrator introduced to manage user requests and coordinate agent responses across clouds.                                           |
|   7 | Architecture allows easy addition of new agents and functionalities without starting from scratch.                                      |
|   8 | Utilizes Kubernetes to combine agents (data, reasoning, action agents) using agent-to-agent and MCP protocols.                          |
|   9 | Agent-to-agent protocol: Directs requests to specific agents based on agent cards specifying skills and capabilities.                   |
|  10 | MCP protocol: Agents share tools from a central server/marketplace, not individually owned.                                             |
|  11 | Containers provide scalability and resource allocation per agent.                                                                       |
|  12 | Architecture supports multicloud, microservices, and independent error handling.                                                        |
|  13 | Demo uses Azure Kubernetes Services, Microsoft Agent Framework, and a Streamlit user interface.                                         |
|  14 | Orchestrator uses Azure Bot Services for message management; integrates agents in Azure and GCP.                                        |
|  15 | Agents include a travel agent (using MCP), currency and planning tools, burger and pizza agents in GCP (using agent-to-agent protocol). |
|  16 | Infrastructure as code pipeline currently deploys only to Azure; future plans to support Google Cloud.                                  |
|  17 | Plans to implement generative AI ops and manage agent lifecycle across development, staging, and production environments.               |
|  18 | Challenges: Standardizing agent card JSON formats and task endpoints across clouds.                                                     |
|  19 | Emphasis on versioning prompts, agent cards, and code for lifecycle management.                                                         |
|  20 | Testing includes unit tests for MCP, orchestrator, and service bus.                                                                     |
|  21 | Importance of managing agent environments and data sources fo                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JnybchLqKXc)
