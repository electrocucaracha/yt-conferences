---
layout: default
title: Dynamic resource sharing and diverse compute platforms for AI  The Slinky Solution
nav_order: 115
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Representatives from Stack HBC presented a solution for dynamic resource sharing in research computing environments, addressing the challenge of balancing diverse workloads such as high-performance..."
resource: "https://www.youtube.com/watch?v=fbLMPA9wz08"
youtube_stats:
  view_count: 53
  like_count: 1
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

Representatives from Stack HBC presented a solution for dynamic resource sharing in research computing environments, addressing the challenge of balancing diverse workloads such as high-performance computing (HPC) and interactive AI applications.
They proposed using the Slurm Operator to run a dynamic partition of a Slurm cluster within Kubernetes, allowing Slurm to function as a standard Kubernetes workload.
This architecture enables the use of Kubernetes preemption mechanisms to automatically evict low-priority Slurm jobs when high-priority interactive workloads, such as Jupyter notebooks, require resources, with the Slurm jobs resuming once the interactive sessions end.
However, the presenters discovered that the default Kubernetes scheduler’s preemption logic was unreliable for this use case due to internal scheduling complexities, leading them to adopt the Apache Unicorn scheduler, which offers more configurable and robust preemption capabilities.
A live proof-of-concept demo successfully demonstrated that this hybrid approach allows for seamless, automated resource reclamation and job resumption without manual intervention, although the team noted that the solution is currently experimental and requires further development for production readiness.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speakers from Stack HBC discuss diverse resource sharing and computing platforms for AI and research solutions.              |
|   2 | Research computing environments face competing demands from batch workloads, interactive notebooks, and containerized services.  |
|   3 | OpenStack provides a reconfigurable infrastructure to support multi-tenancy and diverse scientific use cases.                    |
|   4 | The Dawn system at the University of Cambridge is a large-scale bare-metal OpenStack environment used for AI research.           |
|   5 | Slurm is the de facto standard for batch computing and model training, while Kubernetes is preferred for inference services.     |
|   6 | A key challenge is dynamically sharing finite resources between Slurm and Kubernetes workloads based on demand.                  |
|   7 | The proposed architecture uses Kubernetes as a substrate to run Slurm workloads via the Slurm Operator.                          |
|   8 | The Slurm Operator allows Slurm cluster components to run inside Kubernetes, treating Slurm as a standard workload.              |
|   9 | Standard Kubernetes priority classes were initially used to preempt low-priority Slurm jobs for high-priority interactive tasks. |
|  10 | Testing revealed that standard Kubernetes preemption caused scheduling conflicts and inconsistent resource allocation.           |
|  11 | The Apache Unicorn scheduler was adopted to replace the default Kubernetes scheduler for better preemption control.              |
|  12 | Unicorn allows configurable preemption and can be applied to specific namespaces to manage workload priorities.                  |
|  13 | A proof-of-concept demo showed Slurm nodes being evicted to run Jupyter notebooks and resuming after inactivity.                 |
|  14 | The Slurm Operator maintains database consistency and allows jobs to be requeued if preempted.                                   |
|  15 | Limitations include the need for specific Kubernetes features and potential issues with Slurm resource visibility in containers. |
|  16 | Security trade-offs exist when reducing container isolation to improve Slurm performance within Kubernetes.                      |
|  17 | The solution is not yet production-ready but offers a path to maximizing resource utilization for high-throughput workloads.     |
|  18 | Future work includes performance investigations, integrating high-performance expertise, and exploring alternative schedulers.   |
|  19 | Users can choose between static non-preemptable partitions and dynamic preemptable resources for cost efficiency.                |
|  20 | Checkpointing and graceful shutdown mechanisms are recommended to handle job interruptions effectively.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fbLMPA9wz08/hqdefault.jpg)](https://www.youtube.com/watch?v=fbLMPA9wz08)

[Watch on YouTube](https://www.youtube.com/watch?v=fbLMPA9wz08)
