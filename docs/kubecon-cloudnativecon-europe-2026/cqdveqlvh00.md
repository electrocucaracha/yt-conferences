---
type: Video Note
title: "From GitOps to AIOps: Evolving RBI's Kubernetes Platform with Cross... Gabor Horvath & Ewald Überall"
description: "In this session, Gabbor War and Evadar from Raiffeisen Bank International describe their team's transition from GitOps to AIOps using Crossplane and Sharded Cargo within their Mercury platform, which supports cloud-native applications acros..."
resource: https://www.youtube.com/watch?v=cqDVeqLvh00
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Gabbor War and Evadar from Raiffeisen Bank International describe their team's transition from GitOps to AIOps using Crossplane and Sharded Cargo within their Mercury platform, which supports cloud-native applications across a large, multi-tenant environment.
They detail the platform's architecture, including its three service offerings—namespace as a service, account as a service, and cluster as a service—and explain the complexities of managing promotions across multiple isolation layers and clusters.
The team highlights their migration from Crossplane v1 to v2 to improve tenant visibility and resource management, outlining a three-step, largely autonomous migration process for customers, but noting the manual, error-prone nature of PR-based migrations.
To address this, they developed an AI-assisted review system that analyzes pull requests and Argo CD application states, providing risk assessments and remediation guidance without automating the migration itself.
The presenters emphasize the importance of treating infrastructure and application promotions differently due to their distinct risks, and advocate for AI as a supportive tool to enhance reliability and scalability in complex, multi-tenant cloud environments.
# Main Points

|   # | Main point                                                                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Gabbor War and Evadar presented their journey from GitOps to AI Ops using Crossplane and Shed Cargo at Raiffeisen Bank International.                                                                                                        |
|   2 | The Mercury team develops a groupwide platform for building and running cloud-native applications, used by over 100 engineers.                                                                                                               |
|   3 | The platform offers three services: Namespace as a Service (shared OKD/OpenShift clusters), Account as a Service (dedicated AWS accounts), and Cluster as a Service (internal platform reuse).                                               |
|   4 | Mercury platform implements three isolation layers: Kubernetes account (isolated namespaces), strict RBAC and network policies, and AWS resources (separate billing and IAM roles).                                                          |
|   5 | Promotion of resources is complex due to multi-tenancy and layered architecture.                                                                                                                                                             |
|   6 | The GitHub stack consists of four layers: GitHub Enterprise (repos for platform, customers, self-service libraries), Cargo (single UI for promotion pipelines), Argo CD (dedicated per cluster), and Crossplane (deployed to every cluster). |
|   7 | Application and infrastructure promotions have different risks: app failures are immediate and visible; infra failures (e.g., Crossplane claims) can be silent, delayed, and costly.                                                         |
|   8 | Requirements for promotion system: isolated execution, differentiated policies for prod/test, centralized visibility, and secure architecture.                                                                                               |
|   9 | Solution: Cargo sharded topology/agent-based architecture with central and local Cargo controllers, each integrating with local Argo CD.                                                                                                     |
|  10 | Crossplane v1 had limitations with namespace visibility; migration to Crossplane v2 enabled namespaced managed resources and better team autonomy.                                                                                           |
|  11 | Migration from v1 to v2 involved a three-step process: enhance claim with migration=true, copy migration spec to XR, use Crossplane import functionality, and cleanup.                                                                       |
|  12 | Manual migration PRs are error-prone and time-consuming; AI agent was introduced to review migration PRs, compare with cluster state, flag risks, and analyze Argo CD failures.                                                              |
|  13 | AI agent provides risk grading (small, medium, high) and remediation step                                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cqDVeqLvh00)