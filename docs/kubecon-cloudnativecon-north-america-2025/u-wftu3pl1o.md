---
layout: default
title:
  SIG-Multicluster Intro and Deep Dive - Stephen Kitt, Pavanipriya Sajja & Jeremy
  Olmsted-Thompson
nav_order: 269
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The SIG Multicluster session, led by Jeremy, Stephen, and Pawani Priya
  Saja, provided an overview of the group's mission to simplify working with multiple
  Kubernetes clusters, acknowledging the growing prevalence and complexity of multiclus...
resource: https://www.youtube.com/watch?v=u_WfTU3pL1o
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

The SIG Multicluster session, led by Jeremy, Stephen, and Pawani Priya Saja, provided an overview of the group's mission to simplify working with multiple Kubernetes clusters, acknowledging the growing prevalence and complexity of multicluster environments.
The team detailed several key projects and APIs, such as the Cluster Profile API, About API, Work API, Placement Decision API, Multicluster Services API (MCS), and the Multicluster Runtime library, all designed to enhance interoperability, consistency, and flexibility across diverse deployment scenarios.
Findings from a user experience survey of 150 engineers highlighted common motivations for multicluster setups—including infrastructure flexibility, isolation, business unit autonomy, regional redundancy, and environment separation—as well as major challenges like workload management, observability, operational complexity, and time management.
Engineers expressed a desire for increased automation, flexible architectures, and improved user experiences, with recommendations focusing on better documentation, centralized monitoring, AI-driven automation, operational training, and developer-centric tools.
The session concluded with an invitation for community feedback and participation, updates on API adoption and maturity, and a discussion on the evolving needs driven by AI and the importance of maintaining a familiar Kubernetes experience in multicluster operations.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Multicluster focuses on making it easier to work with multiple Kubernetes clusters.                                                                       |
|   2 | The group recognizes the diversity of cluster environments (public cloud, private cloud, edge, hybrid).                                                       |
|   3 | Emphasis on compatibility and consistency with existing APIs and products.                                                                                    |
|   4 | Provides composable building blocks for flexible multicluster solutions.                                                                                      |
|   5 | Hosted projects include: Cluster Profile API, About API, Work API, Placement Decision API, Multicluster Services API (MCS), and Multicluster Runtime library. |
|   6 | Cluster Profile API stores information and credentials about clusters in a set.                                                                               |
|   7 | About API allows member clusters to publish information about themselves.                                                                                     |
|   8 | Work API enables pushing workloads to member clusters.                                                                                                        |
|   9 | Placement Decision API standardizes workload placement decisions.                                                                                             |
|  10 | MCS API allows services to be published and consumed across clusters.                                                                                         |
|  11 | Multicluster Runtime extends controller-runtime for multicluster reconciliation.                                                                              |
|  12 | User research survey received 150 responses from engineers (platform, DevOps, SRE, software, cloud).                                                          |
|  13 | Top reasons for running multiclusters: infrastructure flexibility, isolation, business unit ownership, regional redundancy, environment separation.           |
|  14 | Main challenges: workload management (51%), observability (39%), operational complexity (25%), time management (10%).                                         |
|  15 | Engineers face issues with stateful workloads, upgrades, configs, resource distribution, network complexity, context switching, and manual failover.          |
|  16 | Desired improvements: AI/automation for routine tasks, flexible architecture, simplified UX, dashboard as code, specialized hardware support.                 |
|  17 | Most engineers manage 1-10 clusters/month; single cloud is common, but alternatives are growing.                                                              |
|  18 | Multi-tenant models are preferred; automated failover is favored.                                                                                             |
|  19 | Tools: ArgoCD and Rancher popular for small deployments; FluxCD and custom controllers scale with cluster count.                                              |
|  20 | Five research areas: documentation gap, centralized monitoring, AI-driven automation, operational comp                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=u_WfTU3pL1o)
