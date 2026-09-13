---
layout: default
title:
  "Cloud Native Theater | Data on Kubernetes Day: Tuning Elastic on Kube... Luuk
  Stolk and Artur Gromek"
nav_order: 56
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Arthur Groc and Luke Stalk from ING describe their experience
  tuning the Elastic Stack on Kubernetes within ING’s large-scale, OpenShift-based
  private cloud infrastructure. They detail the challenges faced when performance
  iss...
resource: https://www.youtube.com/watch?v=LFuEq70lZdo
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

In this talk, Arthur Groc and Luke Stalk from ING describe their experience tuning the Elastic Stack on Kubernetes within ING’s large-scale, OpenShift-based private cloud infrastructure.
They detail the challenges faced when performance issues emerged in their Elasticsearch deployments, specifically a drop in indexing rates and write timeout errors that were not immediately visible in cluster metrics.
Through extensive troubleshooting with Portworx engineers and the use of stress testing tools, they identified the storage layer—rather than Kubernetes or Elasticsearch configuration—as the primary bottleneck, with replication overhead and non-optimized volume options contributing to the slowdown.
By implementing Portworx’s new features such as journal devices, autojournal profiles, and optimized storage classes (favoring replica one), as well as remounting volumes and updating configurations, they were able to nearly double write performance and restore onboarding for new customers.
The speakers emphasize the importance of context-aware testing and monitoring, noting that synthetic benchmarks did not always align with real-world application performance, and reflect on the valuable lessons learned throughout their two-year optimization journey.

# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Arthur Groc and Luke Stalk from ING presented on tuning Elastic on Kubernetes.                                                           |
|   2 | ING operates in over 100 countries, with 30 million customers and 60,000 employees.                                                      |
|   3 | ING’s main Kubernetes platform, the ING Container Hosting Platform (ICP), is based on OpenShift and runs in the ING Private Cloud (IPC). |
|   4 | ICP offers multi-tenant clusters for stateless workloads and dedicated clusters for stateful workloads.                                  |
|   5 | Zero trust privilege access model is enforced; no direct write access to clusters.                                                       |
|   6 | ICP provides namespace-as-a-service, integrated with Azure DevOps for application deployment.                                            |
|   7 | ICP has grown to thousands of teams, namespaces, and nearly 65,000 pods, with 100% uptime and zero security breaches.                    |
|   8 | Stateless workloads use ephemeral storage; stateful workloads (like Elastic Stack) use persistent storage via Portworx.                  |
|   9 | Elastic Stack offering uses OpenShift, the official Elasticsearch operator, Portworx for storage, and ingests data from Kafka.           |
|  10 | Four large OpenShift clusters: 44 worker nodes (96 CPU, 1.5TB memory each), 800 namespaces, 2.7PB storage.                               |
|  11 | Elastic Stack architecture includes redundancy at Elastic, Portworx, and RAID 5 storage layers.                                          |
|  12 | Performance issues were first detected by Elastic engineers: indexing rate dropped, write timeout errors increased.                      |
|  13 | Cluster metrics did not initially reflect the performance issues, making troubleshooting difficult.                                      |
|  14 | Onboarding of new customers was paused during investigation.                                                                             |
|  15 | Troubleshooting involved Portworx engineers, FIO, and IoT tools; storage layer showed long IO latency.                                   |
|  16 | Isolated test environments and Elastic stress test tools were used to reproduce and analyze issues.                                      |
|  17 | Tested various configurations: Portworx replication (replica 1 vs 2), RAID 5 vs RAID 10, SSD vs NVMe, bare metal vs virtualized storage. |
|  18 | Replica 1 consistently outperformed replica 2 due to lower replication overhead.                                                         |
|  19 | Portworx features tested: journal device, autojournal profile, no discard, out of a stream.                                              |
|  20 | Autojournal profile p                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=LFuEq70lZdo)
