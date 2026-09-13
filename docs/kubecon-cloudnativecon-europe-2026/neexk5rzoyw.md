---
type: Video Note
title: "Scaling the Kubernetes Ecosystem: Uber's Approach to Cluster... Silvio Simunic & Vadim Plakhtinskii"
description: "Vadim and Sylvia present how Uber manages its large-scale Kubernetes clusters, highlighting the challenges and solutions developed for cluster lifecycle management. Initially, cluster provisioning at Uber was a manual, multi-week process in..."
resource: https://www.youtube.com/watch?v=neexk5RZoyw
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Vadim and Sylvia present how Uber manages its large-scale Kubernetes clusters, highlighting the challenges and solutions developed for cluster lifecycle management.
Initially, cluster provisioning at Uber was a manual, multi-week process involving numerous steps, which was inefficient and frustrating for developers.
To address this, their team automated the process by introducing a declarative configuration model using templates and the Starlark language, enabling both static and dynamic configurations to be merged and managed centrally in Git.
They built a custom Kubernetes operator framework to automate cluster provisioning, updates, and decommissioning, ensuring safety through layered approval, quarantine periods, concurrency limits, and integration with Uber’s internal systems.
Their approach emphasizes safety, scalability, and flexibility, allowing for rapid, reliable cluster operations across hundreds of clusters and thousands of nodes, and has significantly reduced manual effort while integrating seamlessly with Uber’s infrastructure.
The team chose to build their own solution due to Uber’s unique requirements and scale, and while they drew inspiration from open source projects, they found existing tools insufficient for their needs.
# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Uber manages over 100 Kubernetes clusters across 15+ zones and regions, supporting 1,000+ engineers and clusters with 5,000–7,000 nodes each.                                           |
|   2 | Previously, cluster provisioning required 15+ manual steps and weeks of work for developers.                                                                                            |
|   3 | The team automated the cluster lifecycle: provisioning, configuration, updates, and decommissioning.                                                                                    |
|   4 | Cluster configuration is split into static (unchanging, e.g., name, zone, type) and dynamic (modifiable during lifecycle) parts.                                                        |
|   5 | Configuration is templated and managed using Starlark, merging static and dynamic configs for each cluster.                                                                             |
|   6 | Automation uses a Kubernetes-native, declarative model with CRDs; a cluster object defines the goal state.                                                                              |
|   7 | A custom operator (Kubernetes Cluster Orchestrator) reconciles cluster state, coordinating multiple controllers for tasks like infra provisioning, control plane setup, and validation. |
|   8 | Steps are modeled as a graph for extensibility and maintainability.                                                                                                                     |
|   9 | Integration with Uber’s internal systems (capacity, deployment, certificates) required resilient patterns (rate limits, retries, cooldowns).                                            |
|  10 | Safe configuration changes are enabled via sharded operators for different environments (dev, staging, production) and CI/CD pipelines.                                                 |
|  11 | Decommissioning uses the same model as provisioning, with finalizers to ensure resource cleanup and multi-layer safety (approvals, quarantine, concurrency limits, rate limiting).      |
|  12 | All configuration is centralized in Git, providing a single source of truth.                                                                                                            |
|  13 | The system was built by a single team of ~4 engineers over 6–12 months.                                                                                                                 |
|  14 | Open source solutions (Cluster API, vCluster, FluxCD) were evaluated but not adopted due to Uber’s scale and custom requirements.                                                       |
|  15 | OS and Kubernetes version upgrades are automated but handled by a separate subsystem.                                                                                                   |
|  16 | Benchmark clusters are used to test changes at production scale.                                                                                                                        |
|  17 | Networking and capacity provisioning are handled by dedicated internal teams.                                                                                                           |
|  18 | Controllers are custom-built and run on a separate, globally distrib                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=neexk5RZoyw)