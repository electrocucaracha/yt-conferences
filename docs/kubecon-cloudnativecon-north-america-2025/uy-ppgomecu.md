---
layout: default
title: "Project Lightning Talk: Kubewarden: The Universal Policy Engine For Kubernetes"
nav_order: 225
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Robert introduces Kuborton, a universal policy engine for Kubernetes,
  explaining that policies in this context are configurations managing other configurations
  or runtime behaviors within a Kubernetes cluster. Kuborton aims to be universal...
resource: https://www.youtube.com/watch?v=Uy-PpGOMEcU
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

Robert introduces Kuborton, a universal policy engine for Kubernetes, explaining that policies in this context are configurations managing other configurations or runtime behaviors within a Kubernetes cluster.
Kuborton aims to be universal by supporting pre-existing policies from various sources, such as RIO, Kyverno, and Artifact Hub, and by accommodating user-created policies in multiple languages like .NET, Go, and Rust, all compiled into small binaries using WebAssembly.
The project considers different user personas—consumers, developers, operators, and integrators—and adopts a GitOps approach to policy management.
Kuborton extends policy enforcement beyond Kubernetes clusters to virtual machines and edge use cases, addressing the need for policies everywhere.
Robert invites interested individuals to get involved with the project, mentioning an upcoming alpha release of a new SBOM scanner and offering further discussion at the project pavilion.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Robert, CNF ambassador, project Helm maintainer, Kuborton contributor                                                  |
|   2 | Topic: Kuborton, the universal policy engine for Kubernetes                                                                       |
|   3 | Definition of policy: configurations managing other configurations or runtime behaviors                                           |
|   4 | Policy engine: tool enforcing rules and guidelines for creation and management of Kubernetes objects                              |
|   5 | Universal policy engine goal: meet diverse user needs by supporting various policy types and sources                              |
|   6 | Supports pre-existing policies (e.g., RIO, Kyverno, Artifact Hub, custom RIGO policies)                                           |
|   7 | User personas: consumers (policy enforcements), developers (policy creators), operators (policy operators), integrator developers |
|   8 | Supports multiple programming languages: .NET, Go, Rust                                                                           |
|   9 | Policies compiled into small binaries using WebAssembly (WASM)                                                                    |
|  10 | GitOps approach for policy management                                                                                             |
|  11 | "Policies everywhere" concept: enforce policies in clusters, VMs, and edge use cases, not limited to Kubernetes                   |
|  12 | Universal policy agent enables writing and enforcing policies wherever needed                                                     |
|  13 | Invitation to get started with Kuborton via QR code                                                                               |
|  14 | Project seeking adopters, contributors, and maintainers                                                                           |
|  15 | Presenter available at the Kuborton kiosk in the project pavilion                                                                 |
|  16 | Announcement: new SBOM scanner coming in alpha soon                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Uy-PpGOMEcU)
