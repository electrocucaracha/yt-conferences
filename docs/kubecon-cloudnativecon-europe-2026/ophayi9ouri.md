---
type: Video Note
title: "Addressing Non-Deterministic Scheduling: Introducing... Ajay K, Sreeram V, Karthik N & Priyanka S"
description: "The presentation introduces the Node Readiness Controller (NRC), a new Kubernetes SIG Node subproject designed to address nondeterministic node scheduling by ensuring nodes are truly ready before workloads are assigned. The NRC acts as an o..."
resource: https://www.youtube.com/watch?v=oPHayi9ouRI
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation introduces the Node Readiness Controller (NRC), a new Kubernetes SIG Node subproject designed to address nondeterministic node scheduling by ensuring nodes are truly ready before workloads are assigned.
The NRC acts as an out-of-band controller that coordinates between infrastructure components and the scheduler, using custom resource definitions (CRDs) and taints to gate scheduling until all critical components (like CNI plugins or GPU drivers) are fully initialized.
The controller supports both "bootstrap only" and "continuous" enforcement modes, offers dry-run capabilities, and integrates with tools like Cluster Autoscaler and Mutating Admission Policies to avoid conflicts and deadlocks.
Performance testing demonstrated NRC’s high throughput, low latency, and minimal resource usage, making it suitable for production environments.
The team has also implemented security improvements, such as constrained impersonation, and invites community feedback and contributions as they continue to enhance the project’s scalability, usability, and integration with the broader Kubernetes ecosystem.
# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of the Node Readiness Controller (NRC), a new SIG Node subproject to address nondeterministic scheduling in Kubernetes.                                              |
|   2 | NRC was created to solve recurring production issues where nodes reported as "ready" were not actually usable due to incomplete initialization of components like CNI or drivers. |
|   3 | Kubernetes' current node readiness is a low bar; nodes are marked ready if kubelet and basic CNI config are present, regardless of actual component readiness.                    |
|   4 | NRC acts as an out-of-band controller, adding a coordination layer between infrastructure components and the scheduler.                                                           |
|   5 | NRC uses a declarative system: readiness is defined via custom resources (NodeReadinessRule) specifying required conditions and taints.                                           |
|   6 | NRC applies a temporary taint (readiness.k8s.io) to new nodes, preventing scheduling until all specified components report readiness.                                             |
|   7 | Two enforcement modes: "bootstrap only" (taint removed after initial readiness) and "continuous" (taint re-applied if readiness is lost).                                         |
|   8 | Dry run mode allows operators to test rules without affecting scheduling.                                                                                                         |
|   9 | Integration with Cluster Autoscaler: new flag allows autoscaler to ignore NRC taints, preventing unwanted scaling actions.                                                        |
|  10 | Automatic injection of tolerations into DaemonSets via mutating admission policy to avoid deadlocks.                                                                              |
|  11 | NRC is production-ready, with high throughput (500 nodes/sec taint addition/removal) and low resource usage (<50MB memory, <0.25 CPU).                                            |
|  12 | Security improvements: constraint impersonation (Kubernetes 1.36+) limits node status updates to only the node a component runs on.                                               |
|  13 | Three minor releases so far; latest (v0.3.0) includes security and observability enhancements.                                                                                    |
|  14 | Roadmap includes Helm charts, Headlamp UI integration, API efficiency improvements, and further security work.                                                                    |
|  15 | Community involvement encouraged via GitHub, Slack, bi-weekly meetings, and project website.                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oPHayi9ouRI)