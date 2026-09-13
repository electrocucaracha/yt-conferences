---
type: Video Note
title: "SIG-Multicluster Intro and Deep Dive - Stephen Kitt, Jeremy Olmsted-Thompson & Laura Lorenz"
description: "The SIG Multicluster session, led by Jeremy Olstead Thompson and Stephen Kit, provided an overview of the group's mission to address the challenges of managing and deploying applications across multiple Kubernetes clusters. The presenters d..."
resource: https://www.youtube.com/watch?v=fjRT6tdsXLU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The SIG Multicluster session, led by Jeremy Olstead Thompson and Stephen Kit, provided an overview of the group's mission to address the challenges of managing and deploying applications across multiple Kubernetes clusters.
The presenters discussed the diversity of multicluster use cases—such as multi-cloud, multi-region, compliance, and performance—and emphasized the importance of building APIs and tools that are flexible, composable, and compatible with existing solutions.
Key projects highlighted included the cluster profile API, work API, placement decision API, MCS API, and the multicluster runtime library, all designed to facilitate resource management, workload placement, and service discovery across clusters.
The group also shared insights from recent user research, identifying major pain points like documentation gaps, observability, operational complexity, and the lack of purpose-built tooling, especially for engineers managing hybrid or multi-cloud environments.
Attendees were encouraged to participate in the SIG by joining meetings, providing feedback, and contributing to ongoing projects to help shape future multicluster solutions.
# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Multicluster focuses on solving challenges of managing and deploying applications across multiple Kubernetes clusters.                                                      |
|   2 | Reasons for adopting multicluster include multi-cloud footprints, multi-region deployments, isolation, compliance, release management, performance, and proximity to customers. |
|   3 | Kubernetes was originally designed with the cluster as the universe, lacking built-in multicluster concepts.                                                                    |
|   4 | SIG aims to recognize ecosystem diversity, environmental constraints, and existing tools, designing APIs that are consistent and composable.                                    |
|   5 | Focus is on solving critical problems, avoiding optional or distracting issues, and providing pluggable building blocks.                                                        |
|   6 | Key projects and APIs:                                                                                                                                                          |
|   7 | Cluster Profile API: Stores information about clusters (names, access, credentials, capabilities).                                                                              |
|   8 | Cluster Self-Profile API: Each cluster knows about itself and its cluster set.                                                                                                  |
|   9 | Work API: Allows management cluster to push resources to member clusters.                                                                                                       |
|  10 | Placement Decision API: Stores decisions about where workloads should go.                                                                                                       |
|  11 | MCS API: Enables services in one cluster to be accessed from another without gateways.                                                                                          |
|  12 | Multicluster Runtime: Library for building controllers that operate across clusters.                                                                                            |
|  13 | Placement Decision API enables separation of workload definition, placement requirements, and actual deployment.                                                                |
|  14 | Example use cases: GPU-aware AI training job placement and progressive rollout across clusters.                                                                                 |
|  15 | User experience research identified main pain points: documentation gaps, discovery challenges, observability, operational complexity, and lack of purpose-built tooling.       |
|  16 | Persona "Alex" represents hybrid engineers managing clusters across multiple environments, facing challenges with tooling, observability, RBAC, and platform differences.       |
|  17 | Community involvement is encouraged: join meetings, provide feedback, share use cases, and help improve projects.                                                               |
|  18 | Open agenda for meetings; anyone can participate, present, or discuss issues.                                                                                                   |
|  19 | Concerns raised ab                                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fjRT6tdsXLU)