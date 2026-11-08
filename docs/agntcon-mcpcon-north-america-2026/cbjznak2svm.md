---
layout: default
title: "Beyond Scopes: Governing What Agents Are Actually Allowed to Do - Pavan Kulkarni, WorkOS"
nav_order: 135
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Pawan, an engineering manager at WorkOS, presents a solution to the growing challenge of authorizing AI agents that require broad access to enterprise systems while maintaining strict control over ..."
resource: "https://www.youtube.com/watch?v=CBjzNAK2SVM"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Pawan, an engineering manager at WorkOS, presents a solution to the growing challenge of authorizing AI agents that require broad access to enterprise systems while maintaining strict control over their actions.
He argues that traditional static permissions and OAuth scopes are insufficient because they lack the contextual awareness of specific business policies, leading to potential errors where agents might perform destructive or unauthorized actions based on incomplete information.
To address this, WorkOS has developed Airlock, a gateway system that sits between agents and company resources to evaluate every request against both deterministic rules and non-deterministic agentic execution policies.
Airlock uses intent tokens to track an agent’s original task and ensures that each tool call aligns with the specific responsibility of that job, allowing the system to automatically approve, deny, or escalate actions to human reviewers based on complex business logic.
By enforcing these guardrails at the gateway level and providing a robust audit trail, Airlock aims to prevent the "YOLO mode" of unchecked agent access while avoiding the fatigue of manual approvals, thereby enabling safe and scalable deployment of AI agents in enterprise environments.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , as static permissions often lack business context.                                                                                         |
|   2 | , serving over 3,000 customers with features like SSO, directory sync, and audit logs.                                                       |
|   3 | , lose track of original instructions, or ignore business policies, leading to catastrophic errors with broad access.                        |
|   4 | , such as distinguishing between a minor UI fix and a critical billing change.                                                               |
|   5 | —manual approval for every action or "YOLO mode" auto-approval—lead to approval fatigue or uncontrolled agent behavior.                      |
|   6 | , a gateway that sits between agents and company resources to enforce policies by approving, denying, or escalating actions to humans.       |
|   7 | "intent tokens," which are signed, short-lived references that tie an agent’s task to its original intent and specific tool calls.           |
|   8 | (strict API/tool restrictions) with non-deterministic agentic execution (evaluating complex runtime business rules).                         |
|   9 | (e.g., deleting databases), while non-deterministic checks handle complex business logic (e.g., verifying ticket references before refunds). |
|  10 | ’s decision-making process.                                                                                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CBjzNAK2SVM/hqdefault.jpg)]("https://www.youtube.com/watch?v=CBjzNAK2SVM")

[Watch on YouTube](https://www.youtube.com/watch?v=CBjzNAK2SVM)
