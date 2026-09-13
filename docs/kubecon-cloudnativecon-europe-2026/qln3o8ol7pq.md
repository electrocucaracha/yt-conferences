---
layout: default
title: "Project Lightning Talk: FluxCD - Gitops For All Sizes - Matheus Pimenta, Maintainer"
nav_order: 263
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Matos Pimementa, a Flux maintainer at Control Plane, introduces Flux
  as a lightweight, Kubernetes-native GitOps tool designed for automating CI/CD pipelines
  with a focus on performance and security. Flux integrates deeply with the Kubernete...
resource: https://www.youtube.com/watch?v=qln3o8Ol7pQ
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Matos Pimementa, a Flux maintainer at Control Plane, introduces Flux as a lightweight, Kubernetes-native GitOps tool designed for automating CI/CD pipelines with a focus on performance and security.
Flux integrates deeply with the Kubernetes security model, offers comprehensive APIs and CRDs, and is trusted by major organizations such as Azure, AWS, and large telcos, with notable projects like Silva built on top of it.
Key features include robust Helm support, native server-side apply, advanced health checks with dependency management, and the recent addition of cell expressions for customizable health assessments.
The Flux Operator project now enables declarative management of Flux itself, including a new UI and MCP server, while recent enhancements also cover agent skills, OCI artifact support, and OpenTelemetry integration for resource tracing.
Pimementa concludes by inviting further discussion and highlighting ongoing improvements to the Flux ecosystem.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Matos Pimementa is a Flux maintainer at Control Plane.                                                                         |
|   2 | The talk focuses on using Flux for DevOps, MLOps, and AIOps in 2026.                                                           |
|   3 | Flux automates CI/CD pipelines and is a GitOps tool that reconciles cluster state from Git.                                    |
|   4 | Designed for performance and security, integrating well with the Kubernetes security model.                                    |
|   5 | Built as a set of Kubernetes controllers with comprehensive APIs and CRDs.                                                     |
|   6 | Flux is lightweight.                                                                                                           |
|   7 | Trusted by large organizations such as Azure, AWS, and major telcos.                                                           |
|   8 | Azure offers a Flux extension in its marketplace.                                                                              |
|   9 | Telco companies use Flux and have built Silva, an open source project for managing workload clusters.                          |
|  10 | Large financial institutions use Flux for its scalability and ability to manage hundreds of clusters declaratively via GitOps. |
|  11 | Flux offers strong Helm support, including deep integration with the Helm SDK and support for Helm 4.                          |
|  12 | Performs drift detection effectively, especially with Helm.                                                                    |
|  13 | Uses Kubernetes server-side apply natively for better resource management with multiple tools.                                 |
|  14 | Provides robust health checks and supports dependency declarations between resources.                                          |
|  15 | Supports cell expressions for custom health checks across different resource types.                                            |
|  16 | Control Plane introduced Flux Operator, an open source project for easier Flux management.                                     |
|  17 | Flux Operator includes a UI for Flux, which has been well received.                                                            |
|  18 | Flux Operator also includes the MCP server.                                                                                    |
|  19 | Recently released agent skills and support for VIP coding.                                                                     |
|  20 | Supports OCI artifacts for software and configuration distribution.                                                            |
|  21 | Released OpenTelemetry integration for tracing Flux resources.                                                                 |
|  22 | Plans for deeper trace correlation and visualization in the future.                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qln3o8Ol7pQ)
