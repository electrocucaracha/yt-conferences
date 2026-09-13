---
layout: default
title:
  "Kubernetes-Native Agent Discovery: A Unified Registry for MCP Servers and
  Skills - Carlos Santana"
nav_order: 51
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Carlos Santana, a senior specialist solutions architect at AWS, discusses
  using Kubernetes as a platform engineering control plane, focusing on modeling and
  managing agentic workloads through Custom Resource Definitions (CRDs). He introduce...
resource: https://www.youtube.com/watch?v=DKZYsomOjtQ
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Carlos Santana, a senior specialist solutions architect at AWS, discusses using Kubernetes as a platform engineering control plane, focusing on modeling and managing agentic workloads through Custom Resource Definitions (CRDs).
He introduces several projects—KAgent, K8s Agent Sandbox, and Symposium—that leverage CRDs to define agents, models, skills, and secure execution environments, enabling organizations to declaratively compose and manage complex agent-based applications.
Santana highlights the challenges of inconsistent APIs across projects and demonstrates how tools like Crow (Kubernetes Resource Orchestrator) can help unify and abstract these definitions, allowing for flexible composition and adaptation without deep Go programming.
Through YAML-based configurations and live demos, he shows how organizations can deploy, manage, and evolve agentic platforms on Kubernetes, ensuring consistency, security, and ease of integration across diverse workloads and environments.

# Main Points

|   # | Main point                                                                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Carlos Santana is a Senior Specialist Solutions Architect at AWS focusing on Kubernetes and EKS.                                                                                                                    |
|   2 | The talk centers on using Kubernetes as a platform engineering control plane, not just for running workloads but for modeling infrastructure and agentic applications.                                              |
|   3 | Custom Resource Definitions (CRDs) are used to create unified registries for defining cloud or on-premises infrastructure and new agent-based apps.                                                                 |
|   4 | Kubernetes is chosen for agent workloads due to existing skills, production use, security approvals, and ecosystem familiarity.                                                                                     |
|   5 | CRDs are based on OpenAPI v3 and allow modeling of objects, security, access policies, and admission/mutation webhooks.                                                                                             |
|   6 | Three main projects using CRDs for agent modeling were discussed:                                                                                                                                                   |
|   7 | **KAgent (by Solo, CNCF project):** Provides CRDs for agents, models, and MCP servers; supports declarative agent creation, model composition, remote servers, A2A protocol, CLI, and web UI.                       |
|   8 | **K8s Agent Sandbox:** Focuses on securely running agents in sandboxes (e.g., GVisor, Kata Containers, Firecracker); uses CRDs for sandbox claims and warm pools to speed up agent startup.                         |
|   9 | **Symposium (by Alex Jones):** Experimental project with multiple CRDs for running OpenClaw as jobs, skill packs, persona packs, webhooks for policy, channels for communication, and persistent memory for agents. |
|  10 | YAML is the standard syntax for defining resources in Kubernetes.                                                                                                                                                   |
|  11 | There is inconsistency across MCP server registries and CRDs, making composition and discovery challenging.                                                                                                         |
|  12 | **Crow (Kubernetes Resource Orchestrator):** Enables dynamic CRD creation and composition using CEL expressions, allowing abstraction and adaptation of existing CRDs without Go code.                              |
|  13 | Crow supports resource graph definitions (DAGs) for dependency management and status propagation.                                                                                                                   |
|  14 | Demonstrations showed deploying agents, MCP servers, and related resources using YAML and Crow, highlighting unified APIs and abstraction benefits.                                                                 |
|  15 | Unified CRDs allow organizations to switch the                                                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=DKZYsomOjtQ)
