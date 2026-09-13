---
type: Video Note
title: "Project Lightning Talk: PipeCDv1 Is Here! Leverage The Power Of Plugin Architecture - Khanh Tran"
description: "Kang, a software engineer at Season and maintainer of the PICD project, provides an update on PICD, a GitOps-style progressive delivery platform supporting multiple application platforms such as Kubernetes, Terraform, ECS, Lambda, and GCP C..."
resource: https://www.youtube.com/watch?v=hO3xdy2fiK4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Kang, a software engineer at Season and maintainer of the PICD project, provides an update on PICD, a GitOps-style progressive delivery platform supporting multiple application platforms such as Kubernetes, Terraform, ECS, Lambda, and GCP Cloud Run.
The architecture consists of a control plane managing deployment data and a piped agent, which can run anywhere and now uses a new plug-in system.
With the recent v1 release, platform-specific code has been separated into plug-ins, improving modularity and ease of configuration, and the app configuration abstraction has been rebuilt for better usability.
Migration tools and documentation are available for users upgrading from earlier versions, and several plug-ins, including Kubernetes multicluster support, are in development or already released.
Kang encourages community involvement through meetings, documentation, and the community plug-in repository.
# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kang is a software engineer at Season and maintainer of the PICD project.                                                                                                 |
|   2 | PICD is a GitOps-style progressive delivery platform for consistent deployment and operation across various application platforms.                                        |
|   3 | Before v1, supported platforms included Kubernetes, Terraform, ECS, Lambda, and GCP Cloud Run.                                                                            |
|   4 | PICD consists of two components: the control plane (manages deployment data, provides RPC API and UI) and the agent called piped (a single binary that can run anywhere). |
|   5 | The architecture separates platform and development team scopes.                                                                                                          |
|   6 | PICD v1 has been released in alpha state, adopting a plug-in architecture.                                                                                                |
|   7 | Platform-specific execution code is now separated from the piped core and distributed as plug-ins.                                                                        |
|   8 | Piped and its plug-ins communicate via gRPC protocol.                                                                                                                     |
|   9 | Users configure plug-ins through the piped configuration.                                                                                                                 |
|  10 | The app configuration abstraction has been rebuilt for easier documentation and implementation.                                                                           |
|  11 | A command is available to help users migrate app configurations from v0 to v1.                                                                                            |
|  12 | Most state executors from v0 are now released as plug-ins in v1, including Kubernetes, Terraform, Cloud Run, and Lambda.                                                  |
|  13 | ECS and Kubernetes multicluster plug-ins are in development; the multicluster plug-in will support deploying to multiple clusters at once.                                |
|  14 | v1 documentation and a guide for making piped plug-ins are being developed.                                                                                               |
|  15 | The piped plug-in SDK in Go is released at version 0.3.0.                                                                                                                 |
|  16 | Community-built plug-ins available include OpenTofu, SQL Dev, Azure Function, and Ansible.                                                                                |
|  17 | Community plug-ins are hosted in the PICD community plug-in repository.                                                                                                   |
|  18 | Bi-weekly meetings and a booth are available for those interested in joining or discussing the PICD community.                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hO3xdy2fiK4)