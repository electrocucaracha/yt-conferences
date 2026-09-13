---
type: Video Note
title: "Harmonizing Your Platform Domain With Kubernetes and Custom Resource Definitions - Sebastien Blanc"
description: "In this talk, Sebie, a developer advocate at Port, discusses the role of platform engineering in reducing developers’ cognitive load by shifting complexity to platform teams and enabling self-service capabilities. He emphasizes the importan..."
resource: https://www.youtube.com/watch?v=T_sMX_hxS8k
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Sebie, a developer advocate at Port, discusses the role of platform engineering in reducing developers’ cognitive load by shifting complexity to platform teams and enabling self-service capabilities.
He emphasizes the importance of treating the platform as a product with a well-defined domain model, advocating for Kubernetes as the base platform due to its extensibility through custom resource definitions (CRDs) and the operator pattern.
Sebie demonstrates how CRDs can be used to model and manage platform-specific resources, such as prompts for developers, and shows a live example of creating and deploying a prompt CRD integrated with GitHub Actions, Argo CD, and a developer portal.
He also addresses the challenge of managing multiple operators and CRDs, suggesting abstraction layers or tools like Syntasso’s Kratix to simplify developer experience.
The session concludes with an invitation to further discuss platform engineering and see more product demos at the Port booth.
# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker: Sebie, half French/half Dutch, Java developer, developer advocate at Port, loves HalfLife and cats                                                          |
|   2 | Port is an agentic engineering platform                                                                                                                              |
|   3 | Platform engineering empowers developers (and other platform consumers) by absorbing their cognitive load                                                            |
|   4 | Cognitive load is not destroyed, just shifted from developers to the platform team                                                                                   |
|   5 | Reference to Team Topologies book and importance of team organization in platform engineering                                                                        |
|   6 | Key pillars of platform engineering: self-service for developers and a harmonized platform domain model                                                              |
|   7 | Internal Developer Platform (IDP) requires choosing a base platform (e.g., GitHub, GitLab, homemade, or Kubernetes)                                                  |
|   8 | Speaker recommends Kubernetes as the base platform for IDPs                                                                                                          |
|   9 | Three approaches to building an IDP: generic (vanilla Kubernetes), restrictive (container/source code as a service), or opinionated (default paths with flexibility) |
|  10 | Self-service can be implemented by integrating SaaS operators or custom solutions                                                                                    |
|  11 | Treat your platform as a product with a well-defined domain model and desired state                                                                                  |
|  12 | Kubernetes excels at managing desired state via resources; can be extended with custom resource definitions (CRDs)                                                   |
|  13 | Operator pattern: define custom resources (CRDs) and controllers to manage them                                                                                      |
|  14 | CRDs are Kubernetes resources, persisted like any other, and can be managed via GitOps                                                                               |
|  15 | CRDs allow defining custom kinds and schemas (e.g., a "prompt" resource)                                                                                             |
|  16 | Relationships between CRDs can be expressed via direct references, object references, owner references, or selectors                                                 |
|  17 | Controllers can perform actions inside or outside Kubernetes, including external API calls                                                                           |
|  18 | Demo: Creating and managing "prompt" CRDs for prompt engineering, integrated with Port portal and GitHub Actions                                                     |
|  19 | CRDs can be synced to portals and IDEs for developer self-service                                                                                                    |
|  20 | Managing many CRDs/operators may require abstraction/facades (e.g., operator-of-operators, or using products like Syntasso's Kratix)                                 |
|  21 | Multiple IDPs may exist in organizations;                                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=T_sMX_hxS8k)