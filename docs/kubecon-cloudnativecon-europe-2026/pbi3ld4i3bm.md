---
layout: default
title:
  "Project Lightning Talk: Scheduling at the Edge of Reason: Multi-Cluster AI
  & OCM - August Simonelli"
nav_order: 290
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker discusses the importance of multicluster management and introduces
  several features of open cluster management (OCM), focusing on dynamic scoring,
  federated learning, and recent project updates. Dynamic scoring is described as
  a...
resource: https://www.youtube.com/watch?v=Pbi3LD4I3BM
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

The speaker discusses the importance of multicluster management and introduces several features of open cluster management (OCM), focusing on dynamic scoring, federated learning, and recent project updates.
Dynamic scoring is described as a framework that automates resource management by deploying agents to clusters, collecting metrics, and using a scoring API to make continuous placement decisions for workloads.
In federated learning, OCM uses the hub as an aggregator to reduce high egress costs at the edge, employing add-ons like Flower and supporting various frameworks through a federated learning CRD that integrates with OCM’s placement logic.
Project updates include alignment with SIGMC’s cluster profile API for easier integration, the release of a Q add-on for batch learning and job management, the stabilization of add-ons at v1 beta 1, and the introduction of CAP 5313 to decouple scheduling from workload dispatch.
The speaker also notes the project’s application for incubation, the release of version 1.3, and invites attendees to see a demo at the project pavilion.

# Main Points

|   # | Main point                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------- |
|   1 | Most attendees manage more than one cluster and more than one type of cluster.                        |
|   2 | Open Cluster Management (OCM) focuses on multicluster management.                                     |
|   3 | Dynamic Scoring is a framework for automating resource management using real-time metrics.            |
|   4 | Agents are deployed as add-ons to clusters to gather data and send it to a scoring API.               |
|   5 | The scoring API evaluates metrics and creates dynamic placement decisions within OCM.                 |
|   6 | Placement decisions are continuously updated and can use any logic, including LLMs.                   |
|   7 | Workloads are sent to an orchestrator, which reads dynamic placement and deploys to clusters.         |
|   8 | Federated learning uses the OCM hub as an aggregator to reduce high egress costs at the edge.         |
|   9 | Flower add-on automates super node lifecycle for federated learning.                                  |
|  10 | Add-ons in OCM enable easy software deployment to managed clusters.                                   |
|  11 | Federated learning logic is abstracted into a CRD that reconciles state into manifest work.           |
|  12 | The system is framework agnostic; supports Flower, Open FL, and others.                               |
|  13 | Placement API uses cluster claim-based scheduling, keeping work within cluster boundaries.            |
|  14 | Project updates include alignment with SIGMC's cluster profile API to serve as a credential source.   |
|  15 | OCM aims to be modular, allowing integration with other projects.                                     |
|  16 | Q add-on simplifies installation and management of Q for batch learning and job management.           |
|  17 | Add-ons have reached v1 beta 1, indicating stability.                                                 |
|  18 | CAP 5313 introduces a placement decision API, decoupling scheduling selection from workload dispatch. |
|  19 | OCM has applied for incubation status.                                                                |
|  20 | OCM released version 1.0 previously and is now at version 1.3.                                        |
|  21 | OCM project is celebrating its fifth anniversary.                                                     |
|  22 | Detailed demo of dynamic scoring with MCP is available at the project pavilion.                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Pbi3LD4I3BM)
