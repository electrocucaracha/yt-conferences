---
type: Video Note
title: "Leveling up with Radius: Custom Resources and Headlamp Integration for R... Nuno Guedes & Will Tsai"
description: "Will, a principal product manager at Microsoft Azure’s open source incubations team, introduces Radius as an application platform designed to enable developers to define portable applications deployable across multiple cloud providers, abst..."
resource: https://www.youtube.com/watch?v=MTFkMRngf3M
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Will, a principal product manager at Microsoft Azure’s open source incubations team, introduces Radius as an application platform designed to enable developers to define portable applications deployable across multiple cloud providers, abstracting infrastructure concerns through resource types and recipes.
This separation of concerns allows developers to focus on application logic while operators manage infrastructure implementations, resulting in a stable interface and flexible, environment-specific deployments.
Will demonstrates deploying a sample application across local, Azure, and AWS environments using the same application definition, highlighting Radius’s ability to provision appropriate resources without code changes.
Nuno from Millennium BCP shares how the bank leverages Radius to meet compliance and legacy requirements by creating custom resource types and implementations, achieving clear separation of responsibilities and lifecycle management.
The team also integrates Radius with familiar tools like Headlamp for day-two operations and emphasizes that while Radius orchestrates deployments and maintains state, it relies on integrations with other tools for features like drift detection and reconciliation.
# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Will is a principal product manager on the Microsoft Azure open source incubations team; Nuno is head of public cloud at Millennium BCP.                                                            |
|   2 | Azure's open source incubations team works to solve industry-wide problems, shipping open source code and partnering with CNCF for open governance.                                                 |
|   3 | Radius is an application platform for defining portable applications deployable across different platforms and cloud providers.                                                                     |
|   4 | Radius operates on four pillars: resource types (abstract interfaces for developers), infrastructure recipes (concrete implementations for operators), environments, and a universal control plane. |
|   5 | Developers focus on application logic using resource types, while operators manage infrastructure via recipes, enabling clear separation of concerns.                                               |
|   6 | Radius allows building APIs in front of infrastructure, providing stable, developer-friendly interfaces while operators manage underlying templates (e.g., Terraform, Bicep).                       |
|   7 | Applications can be deployed across multiple environments (local, Azure, AWS) without modifying application definitions or source code.                                                             |
|   8 | Radius provides a rich application graph showing deployed resources and their interdependencies.                                                                                                    |
|   9 | The universal control plane enables platform- and API-driven infrastructure management, future-proofing applications against infrastructure changes.                                                |
|  10 | Millennium BCP uses Radius to support compliance, legacy systems, and IT ecosystem integration by creating custom resource types and implementations.                                               |
|  11 | The approach provides clear separation of concerns, stable contracts (interfaces), and flexible, frequently updated implementations (recipes).                                                      |
|  12 | Custom resource types enable integration with systems like CMDB, ITSM, and observability baselines.                                                                                                 |
|  13 | Terraform recipes allow targeting additional environments such as GCP and private cloud.                                                                                                            |
|  14 | Millennium BCP developed a Headlamp plugin for Radius to provide a familiar UI for operators, integrating Radius resource management into existing workflows.                                       |
|  15 | Radius acts as                                                                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MTFkMRngf3M)