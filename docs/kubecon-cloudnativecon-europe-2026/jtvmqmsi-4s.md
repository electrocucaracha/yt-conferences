---
type: Video Note
title: "Stop Flying Blind: Real-Time, Enforceable Cluster-Wide Quotas with Ky... Mariam Fahmy & Adam Crowder"
description: "In this presentation, Adam Crowder from AWS and Mariam Fahmy from Cloudflare discuss implementing dynamic, cluster-wide resource quotas in multi-tenant Kubernetes clusters using Crow and Kyverno. They explain that while Kubernetes natively..."
resource: https://www.youtube.com/watch?v=JtVMQmsI-4s
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Adam Crowder from AWS and Mariam Fahmy from Cloudflare discuss implementing dynamic, cluster-wide resource quotas in multi-tenant Kubernetes clusters using Crow and Kyverno.
They explain that while Kubernetes natively supports resource quotas at the namespace level, it lacks built-in mechanisms for aggregating and enforcing quotas across multiple namespaces or teams.
Crow, a recently open-sourced project, enables the creation of cluster-scoped custom resources and live dashboards by aggregating resource usage, while Kyverno acts as a policy engine to enforce quota limits and block requests that exceed team budgets.
The workflow involves defining a cluster resource quota per team using Crow, which automatically manages quota watchers and Kyverno validating policies to ensure both visibility and enforcement.
Through a live demo, they show how this approach allows platform admins to centrally manage quotas, provides real-time usage dashboards, and prevents teams from exceeding their allocated resources, all without writing custom operators.
The session concludes with a Q&A addressing label trust, Crow’s maturity, and alternative approaches using Kubernetes’ built-in admission controllers.
# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers implementing dynamic cluster-wide resource quotas using Crow and Kyverno.                                                         |
|   2 | Adam Crowder (AWS, EKS) and Mariam Fahmy (Cloudflare, Kyverno maintainer) are the speakers.                                                           |
|   3 | Scenario: Multi-tenant Kubernetes cluster with multiple teams and namespaces.                                                                         |
|   4 | Goal: Enforce cluster-wide resource quotas per team across namespaces.                                                                                |
|   5 | Kubernetes native resource quotas are namespace-scoped; no native way to aggregate or enforce quotas cluster-wide.                                    |
|   6 | Challenges: Aggregating quotas across namespaces, enforcing budgets, and automating management.                                                       |
|   7 | Desired solution features: centralized visibility, enforcement, and automation.                                                                       |
|   8 | Tools used: Crow (for cluster-scoped resource management and aggregation) and Kyverno (for policy enforcement).                                       |
|   9 | Crow: Operator that creates CRDs, manages resources via resource graph definitions (RGDs), supports templating, and maintains live status dashboards. |
|  10 | Kyverno: Kubernetes policy engine for validating, mutating, and generating resources; used here for enforcing resource quota policies.                |
|  11 | Workflow:                                                                                                                                             |
|  12 | Admin creates a cluster resource quota per team using Crow.                                                                                           |
|  13 | Crow generates a watcher for team resource quotas and a Kyverno validating policy.                                                                    |
|  14 | Status object in cluster resource quota acts as a live dashboard showing team usage.                                                                  |
|  15 | Kyverno blocks any resource quota exceeding the team’s budget.                                                                                        |
|  16 | Resource graph definition (RGD) in Crow defines schema (team name, budget, status) and resources (watcher, validating policy).                        |
|  17 | Crow aggregates resource quotas by team label and updates status with total usage.                                                                    |
|  18 | Kyverno validating policy sums existing quotas and checks new requests against the budget, rejecting if exceeded.                                     |
|  19 | Process is scalable: create a new cluster resource quota for each team as needed.                                                                     |
|  20 | Demo shows applying quotas, tracking usage, and enforcement in action.                                                                                |
|  21 | Crow and Kyverno together provide operator-like functionality without custom code.                                                                    |
|  22 | Crow is actively developed, stable, and used in production, thou                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JtVMQmsI-4s)