---
layout: default
title:
  "Ambient Global Compute: Orchestrating the Non-Elastic Cloud With Kubernetes
  - Jago Macleod, Google"
nav_order: 14
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  JGO Mloud discusses the evolution of public cloud computing, highlighting
  how the industry has shifted from traditional data centers with complex capacity
  planning to the promise of elastic, on-demand cloud resources, and now to a more
  frag...
resource: https://www.youtube.com/watch?v=r-UBNuWkUG8
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

JGO Mloud discusses the evolution of public cloud computing, highlighting how the industry has shifted from traditional data centers with complex capacity planning to the promise of elastic, on-demand cloud resources, and now to a more fragmented and complex environment.
Initially, the cloud offered simplicity and infinite scalability, but the proliferation of specialized hardware (like ARM chips and GPUs), regionalization, and resource constraints have reintroduced challenges similar to those faced in data centers, such as overprovisioning and underutilization.
To address these, modern cloud management now relies on concepts like reserved and spot instances, workload prioritization, and advanced scheduling systems (such as Kubernetes with Q and multiQ), which enable efficient allocation of resources across regions and clusters.
The talk emphasizes the importance of topology-aware and dynamic resource scheduling, abstraction of hardware details for developers, and the use of queues to manage workload priorities and quotas among teams.
Ultimately, while the cloud has not fully come "full circle," it now requires a blend of old and new strategies—leveraging both reserved and burst capacity—to efficiently manage resources in a more complex, multi-cloud, and multi-region world.

# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | The cloud has evolved from physical data centers to elastic, virtualized infrastructure.                                    |
|   2 | Early cloud vision promised simplicity and infinite scalability, hiding infrastructure complexity.                          |
|   3 | Traditional data centers required long-term capacity planning and often resulted in overprovisioning.                       |
|   4 | Virtual machines (VMs) improved utilization and shifted costs from capex to opex.                                           |
|   5 | Cloud migration can lead to unexpected costs and operational challenges, sometimes prompting a return to on-premises.       |
|   6 | Fragmentation has increased: more instance types, architectures (ARM, x86), accelerators (GPUs, TPUs), and regionalization. |
|   7 | Managing cloud resources now requires awareness of machine types, regions, and availability.                                |
|   8 | Reserved instances and committed use discounts help manage costs but can lead to unused capacity.                           |
|   9 | The cloud is experiencing constrained capacity and stockouts, especially with specialized hardware.                         |
|  10 | The focus is shifting from infinite horizontal scaling to vertical scaling in time, prioritizing workloads in a queue.      |
|  11 | Utilization of reserved capacity is now a key concern, resembling data center management.                                   |
|  12 | Kubernetes and similar systems enable workload scheduling across diverse resources and regions.                             |
|  13 | Topology-aware scheduling and dynamic resource allocation (DRA) are becoming more important.                                |
|  14 | Compute classes (e.g., in AWS, Azure) and spot/on-demand instances provide flexibility and cost optimization.               |
|  15 | Workloads are prioritized and scheduled based on quota, urgency, and available resources.                                   |
|  16 | Multi-cluster and multi-region scheduling (e.g., with Q, multiq, Argo) helps route jobs to available capacity.              |
|  17 | Fragmentation and resource constraints require smarter job placement and admission control.                                 |
|  18 | Patterns like global batch computing and elastic platforms on fixed hardware are emerging.                                  |
|  19 | AI and HPC workloads are driving advances in scheduling and resource management.                                            |
|  20 | New caching solutions (e.g., anywhere cache) improve data locality and utilization                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=r-UBNuWkUG8)
