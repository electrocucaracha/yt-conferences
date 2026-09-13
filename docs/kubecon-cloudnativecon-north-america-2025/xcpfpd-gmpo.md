---
type: Video Note
title: "People-first Path To Cell-based Architecture - Martin Jones & Asanka Abeysinghe"
description: "In this talk, the speakers discuss their transition of 60,000 users from a monolithic infrastructure to a Kubernetes-native, cell-based architecture, emphasizing the importance of scalability, autonomy, and aligning technology with organiza..."
resource: https://www.youtube.com/watch?v=XCpfpD_gMpo
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, the speakers discuss their transition of 60,000 users from a monolithic infrastructure to a Kubernetes-native, cell-based architecture, emphasizing the importance of scalability, autonomy, and aligning technology with organizational needs.
They introduce cell-based architecture as a solution to the complexity of managing large numbers of microservices, drawing inspiration from biology to group related components into "cells" with defined boundaries and gateways for controlled communication.
The approach supports decentralized architecture with federated governance, allowing teams to own and manage their domains independently while maintaining central policy control.
Practical examples from the University of Edinburgh illustrate how this model enables clear separation of business logic, easier scaling, versioning, and streamlined migrations.
The speakers also highlight how cell-based architecture facilitates integration of AI and new technologies within enterprise governance, and they provide resources for further exploration and implementation of the concept.
# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Migrated 60,000 people from monolithic infrastructure to Kubernetes-native infrastructure.                                |
|   2 | Goals: enable autonomous work, scalability, and team responsiveness to peak periods.                                      |
|   3 | Agenda: introductions, explanation of cell-based architecture, concepts, practical enterprise use, best practices.        |
|   4 | Asanka Basing: CTO of WSO2, co-author of cell-based architecture (introduced in 2018).                                    |
|   5 | Martin Jones: Integration architect at University of Edinburgh, built integration layer for on-premise and cloud systems. |
|   6 | Emphasis on people: "You don't build a business, you build people and then the people build the business."                |
|   7 | Cell-based architecture emerged to manage complexity as microservices scaled from tens to thousands.                      |
|   8 | Inspired by biology: cells with boundaries (membranes), grouped for proper granularity.                                   |
|   9 | Atomic unit: component (microservice, agent, or workload).                                                                |
|  10 | Each cell has a boundary and a communication controller (gateway).                                                        |
|  11 | Communication managed via gateways: ingress (northbound), egress (southbound), eastbound, and westbound.                  |
|  12 | Domain-driven design and bounded context applied to define cells.                                                         |
|  13 | Decentralized architecture with federated governance: central control plane applies policies, data plane runs workloads.  |
|  14 | Multiple environments (dev, test, prod, staging) managed within data plane.                                               |
|  15 | University example: boundaries drawn around "golden copy" systems, cells align with business domains and capabilities.    |
|  16 | Internal and external connections managed via cell boundaries; clear URL mappings for easy service discovery.             |
|  17 | Migration example: estates integrations moved from on-premise to cloud, enabled parallel testing and quick go-live.       |
|  18 | Benefits: clear separation, internal security, easy service discovery, autoscaling, versioning, log separation.           |
|  19 | Kubernetes implementation: components as pods, namespaces as cells, use of CRDs, eBPF, Cilium.                            |
|  20 | Designed for people: clear team boundaries, ownership, and domain expertise.                                              |
|  21 | One team can own multiple cells; one ce                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XCpfpD_gMpo)