---
type: Video Note
title: "Platform Mesh: Breaking API Lock-In for True Multi-Cloud Service... Mirza Kopic & Mangirdas Judeikis"
description: "Ma Kopich from SAP and MJ from Clyiso introduce Platform Mesh, a toolkit designed to address the complexities of building and managing platforms across heterogeneous environments with multiple providers and administrative domains. They high..."
resource: https://www.youtube.com/watch?v=43X0_U3cc-Y
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Ma Kopich from SAP and MJ from Clyiso introduce Platform Mesh, a toolkit designed to address the complexities of building and managing platforms across heterogeneous environments with multiple providers and administrative domains.
They highlight the challenges of vendor and API lock-in, fragmentation, and the burden placed on platform engineers to manage diverse, opinionated management APIs.
Platform Mesh leverages existing CNCF projects like KCP, Qbind, and multicluster runtime to create a unified approach using the Kubernetes resource model, enabling orchestration and lifecycle management of services across clusters and providers.
A key feature discussed is the Resource Broker, which abstracts and automates the migration and management of resources between providers without exposing complexity to users, demonstrated through a live example of certificate management.
The presenters emphasize the importance of abstraction layers and reusable APIs to simplify integration for both platform users and service providers, inviting further discussion and collaboration at their project booths.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Ma Kopich (SAP) and MJ (Clyiso) are developers working on Platform Mesh.                                                                                     |
|   2 | Platform Mesh is a project under the Neonos Foundation, also present at the KCP pavilion.                                                                    |
|   3 | Platform Mesh is a toolkit for building custom platforms, leveraging CNCF projects.                                                                          |
|   4 | It integrates with KCP, Qbind, and multicluster runtime for Kubernetes API management and multicluster support.                                              |
|   5 | The main problem addressed is the fragmentation and complexity caused by multiple providers' opinionated management APIs, leading to vendor and API lock-in. |
|   6 | Platform engineers bear the burden of integrating and understanding diverse APIs from different providers.                                                   |
|   7 | Platform Mesh aims to use the Kubernetes resource model to orchestrate not just workloads but also APIs and services.                                        |
|   8 | The project seeks to provide a consistent way to consume services across multi-provider, multi-cluster environments.                                         |
|   9 | The resource broker in Platform Mesh addresses lifecycle management and migration of resources between providers.                                            |
|  10 | The platform supports dynamic switching of resources (e.g., from sustainable to performant compute) without manual intervention.                             |
|  11 | The architecture is based on lightweight control planes using KCP workspaces, enabling multi-tenancy and API orchestration.                                  |
|  12 | APIs from external providers can be integrated via API sync agent, multicluster runtime, or Qbind.                                                           |
|  13 | The resource broker enables claims and providers to be managed dynamically, supporting migration, provisioning, and deprovisioning.                          |
|  14 | The approach hides implementation details from users, maintaining a seamless user experience during resource migration.                                      |
|  15 | The demo showed dynamic migration of a certificate resource between internal and external providers without object deletion or recreation.                   |
|  16 | Platform Mesh uses KCP and KRM to provide polymorphic APIs and an abstraction layer for simplifying multi-provider integration.                              |
|  17 | The team encourages feedback and questions, and invites attendees to visit their booth for more information.                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=43X0_U3cc-Y)