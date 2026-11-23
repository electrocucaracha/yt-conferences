---
layout: default
title: "StarlingX Edge Orchestration: Managing Critical Workloads at Scale"
nav_order: 36
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Joshua Kraker from Wind River presents an overview of the Starling X project, focusing on edge orchestration and the management of critical workloads at scale, particularly regarding platform and K..."
resource: "https://www.youtube.com/watch?v=ofq6Fk3LMvk"
youtube_stats:
  view_count: 188
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Joshua Kraker from Wind River presents an overview of the Starling X project, focusing on edge orchestration and the management of critical workloads at scale, particularly regarding platform and Kubernetes upgrades.
He explains that Starling X supports mission-critical environments in remote areas with limited skilled operators, necessitating solutions for resource overcommitment where workload demand often exceeds available server capacity.
Current mechanisms for managing this include high availability, resource limits, and quality of service policies, though existing alarms are node-specific rather than system-wide, which can lead to cascading failures during parallel node upgrades if thresholds are not carefully configured.
Kraker also outlines forward-looking proposals, such as policy-driven orchestration that uses workload metadata to automate upgrade scheduling and cloud scaling via factory enrollment, which allows for the rapid deployment of virtual nodes to augment capacity during peak demands or maintenance windows.
The presentation concludes by soliciting community feedback on the interest and necessity of these proposed features to ensure they align with user requirements for operational efficiency and graceful rollback capabilities.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Joshua Kraker from Wind River presents on Starling X edge orchestration and managing critical workloads at scale.                             |
|   2 | Starling X supports mission-critical workloads in remote areas with limited skilled operators, often requiring overcommitted resources.       |
|   3 | Current solutions for resource management include High Availability, resource limits, and Quality of Service mechanisms.                      |
|   4 | Starling X is a complete cloud infrastructure stack integrating Kubernetes, OpenStack, and system management in one system.                   |
|   5 | The platform supports real-time low-latency operations for telecom and medical fields, as well as distributed cloud architectures.            |
|   6 | Distributed cloud features allow a system controller to manage up to 1,000 autonomous subclouds with centralized orchestration.               |
|   7 | Orchestration automates platform and Kubernetes upgrades to reduce operator oversight and improve operational efficiency.                     |
|   8 | Upgrades can be scheduled during specific maintenance windows to avoid disruptions during peak usage periods.                                 |
|   9 | The upgrade process consists of a build phase for system checks and an apply phase for executing control, worker, and storage plane updates.  |
|  10 | Platform and Kubernetes upgrades are linked and executed together, with nodes taken down sequentially or in parallel.                         |
|  11 | Workload migration during upgrades involves live migration or shutdown for OpenStack VMs and cordon/drain for Kubernetes pods.                |
|  12 | Parallel node upgrades are currently limited to 10 nodes, which can cause resource overcommitment issues if not managed carefully.            |
|  13 | Overcommitment arises from remote access needs, cost reduction strategies, workload competition, and time constraints for deployment.         |
|  14 | Node failures during orchestration in remote sites can lead to cascading failures, memory errors, and kernel panics.                          |
|  15 | Manual intervention for remote failures incurs high costs, potential SLA violations, and regulatory risks for operators.                      |
|  16 | Making workloads highly available at the application level is the most flexible solution, shifting responsibility from the platform to users. |
|  17 | Domain-specific solutions like telecom tower overlap and piggybacking on competitor infrastructure provide additional resilience.             |
|  18 | Starling X implements configurable alarms for CPU, memory, and storage thresholds to prevent unsafe operations.                               |
|  19 | Default alarm thresholds are set at 80% for warnings and 90% for management-affecting alerts, but these are per-node rather than per-system.  |
|  20 | OpenStack and Kubernetes provide their own Quality of Service policies, limits, and resource constraints for workload management.             |
|  21 | A proposed forward-looking solution is policy-driven orchestration using workload metadata to inform upgrade actions and scheduling.          |
|  22 | Another proposed feature is geo-redundancy, allowing nodes to be moved between nearby distributed cloud sites to augment capacity.            |
|  23 | Cloud scaling involves using factory enrollment to create cloud images that auto-install and join existing systems as virtual nodes.          |
|  24 | Cloud-based scaling may face legal or policy restrictions when using public cloud providers for private data.                                 |
|  25 | The team seeks community feedback on the interest and necessity of these forward-looking orchestration and scaling features.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ofq6Fk3LMvk/hqdefault.jpg)](https://www.youtube.com/watch?v=ofq6Fk3LMvk)

[Watch on YouTube](https://www.youtube.com/watch?v=ofq6Fk3LMvk)
