---
type: Video Note
title: "Audit-Ready Kubernetes: How Chase UK Leveraged Policy as Code for Co... Jim Bugwadia & Nischay Goyal"
description: "The video discusses how platform engineers can automate the process of making Kubernetes clusters audit-ready, particularly in highly regulated environments like banking. The speakers, Jim Beuia from Nirmata and Nisha from JP Morgan Chase U..."
resource: https://www.youtube.com/watch?v=B01BQ60PLqM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video discusses how platform engineers can automate the process of making Kubernetes clusters audit-ready, particularly in highly regulated environments like banking.
The speakers, Jim Beuia from Nirmata and Nisha from JP Morgan Chase UK, outline the challenges of balancing rapid development with strict compliance requirements, emphasizing the need for standardized environments, enforceable guardrails, and unified reporting.
They describe their transition from manual, inconsistent compliance processes to adopting Kyverno, a Kubernetes-native policy engine that simplifies policy creation, integrates reporting and exception management, and supports automation across the resource lifecycle.
By implementing Kyverno, Chase UK achieved significant improvements in compliance, automation, and reporting, enabling developers and security teams to collaborate more effectively and reducing engineering effort.
The speakers also share key learnings, such as the importance of testing policies in CI, starting enforcement early, and clearly distinguishing between policy exceptions and skipped resources.
# Main Points

|   # | Main point                                                                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Focus: Automating Kubernetes cluster audit readiness for regulated environments.                                                                                                                                                 |
|   2 | Key challenges: Balancing speed and compliance, lack of standardized compliance frameworks, manual and inconsistent reporting, and ad hoc requirements.                                                                          |
|   3 | Audit readiness requirements: Standardized environments, enforced guardrails (not just recommendations), policy rollout across all clusters, developer enablement, and unified reporting for all stakeholders.                   |
|   4 | Initial solutions evaluated: OPA with Gatekeeper, custom in-house solutions, Kverno policy engine (selected), and other policy engines.                                                                                          |
|   5 | Early issues: Limited expertise in Rego, loss of domain knowledge, lack of reporting, and unclear resource ownership.                                                                                                            |
|   6 | Kverno advantages: Kubernetes-native, YAML-based policies, integrated reporting (Open Reports), multiple policy modes (enforce, audit, warning), first-class exception management, and automation across the resource lifecycle. |
|   7 | Kverno policy types: Validation, mutation, generation, cleanup (deletion), and automation for resource lifecycle.                                                                                                                |
|   8 | Reporting: Real-time dashboards in Grafana, filtering by category, namespace, or policy, detailed failure information for engineers, and performance metrics (latency <20ms).                                                    |
|   9 | Implementation at Chase UK: Kverno as admission controller in every cluster, Prometheus/Thanos for metrics, Grafana for dashboards, and policy enforcement from cluster creation.                                                |
|  10 | Results: Migrated from OPA to Kverno, increased from 4 to 46 policies, enabled culture shift to shared policy ownership, 25% automation, significant engineering time saved, improved audit outcomes.                            |
|  11 | Learnings: Always test policies in CI, prefer enforcement mode over audit mode for new policies, clearly define policy scope vs. exceptions, and ensure all compliance processes are automated and auditable.                    |
|  12 | Kverno supports use cases beyond security/compliance, including operations and optimization.                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=B01BQ60PLqM)