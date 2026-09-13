---
type: Video Note
title: "From Metal To Apps: LinkedIn’s Kubernetes-based Compute Platform - Ahmet Alp Balkan & Ronak Nathani"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=dDkXFuy45EA
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: The speaker, Ron, discusses LinkedIn's scalable compute platform built from metal bare metal to apps, extending Kubernetes heavily.
The platform consists of three layers: infrastructure as a service, Kubernetes cluster management, and workload platform layer.
LinkedIn uses custom resources, such as LI deployments and stateful sets, to manage applications on top of Kubernetes, with features like auto-scaling, quota systems, and in-house CSI drivers for managing bare metal servers.
The company has successfully migrated over half its stateless fleet to Kubernetes without downtime, and is now planning to federate workloads across multiple clusters.
# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | LinkedIn has over 1 billion members, served by 3,000 services, with 500,000+ servers running on bare metal.                          |
|   2 | The company uses Kubernetes but extends it heavily, not using traditional Kubernetes deployment methods.                             |
|   3 | The infrastructure as a service layer includes an inventory manager, compute broker, and host health remediation.                    |
|   4 | The compute pools are composed of heterogeneous hardware, with node profiles specifying minimum requirements for machines.           |
|   5 | The maintenance orchestrator handles upgrades, kernel updates, and other maintenance tasks.                                          |
|   6 | The company uses a custom stateful controller to manage data systems, integrating with shard managers.                               |
|   7 | Stateless applications use the "alli" deployment custom resource, which includes canary and clone set features.                      |
|   8 | Applications are deployed using Argo CD, with custom resources and logs emitted for monitoring.                                      |
|   9 | The company has implemented quota systems to prevent overuse of resources.                                                           |
|  10 | LinkedIn manages its own data centers globally, with multiple edge networks reducing latency.                                        |
|  11 | The company uses in-house solutions instead of third-party tools like Vunder, choosing open-source components that meet their needs. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dDkXFuy45EA)