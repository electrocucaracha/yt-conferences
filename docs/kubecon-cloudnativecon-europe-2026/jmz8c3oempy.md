---
layout: default
title:
  How Many Spark Applications Can Your Etcd Really Handle? - João Soares & João
  Azevedo, Feedzai
nav_order: 141
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Jean Asveu and Jean Swage from FISA discuss their
  experience scaling Spark applications for real-time fraud detection in a Kubernetes
  environment. They describe the challenges of their previous setup, which involved
  ma...
resource: https://www.youtube.com/watch?v=jmz8c3oEmPY
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

In this presentation, Jean Asveu and Jean Swage from FISA discuss their experience scaling Spark applications for real-time fraud detection in a Kubernetes environment.
They describe the challenges of their previous setup, which involved managing numerous independent clusters without multi-tenancy, leading to operational inefficiencies and a heavy burden on platform teams.
Transitioning to Kubernetes, they implemented Spark as a service with a serverless user experience, self-service capabilities, and strong workload isolation using Volcano for gang scheduling and hierarchical queues.
However, they encountered significant scalability issues due to the accumulation and lifecycle of Kubernetes objects, which strained etcd storage and API server performance, especially with high object churn and large custom resources.
To address this, they leveraged the Kubernetes API aggregation layer to offload high-churn Spark application objects to a custom in-memory API server, reducing etcd storage usage by 45% while increasing throughput.
Their key lessons emphasize minimizing custom resource size, limiting status updates, and using aggregation for high-churn workloads, with long-term retention handled outside etcd.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation on handling Spark applications at CubeCon by Jean Asveu and Jean Swage.                                                                   |
|   2 | FISA manages data infrastructure as a service in a Kubernetes ecosystem.                                                                               |
|   3 | FISA's real-time fraud detection platform processes 90 billion events and $83 trillion in payments annually.                                           |
|   4 | Spark is used for batch processing, feature engineering, and model training.                                                                           |
|   5 | Delays in Spark applications can degrade transaction scoring and miss fraud.                                                                           |
|   6 | Over 150 production YARN clusters, isolated per client/use case.                                                                                       |
|   7 | 4,000 Spark applications launched daily (3 per minute), number is growing.                                                                             |
|   8 | Previous setup: independent clusters per client/use case, lack of resource efficiency, no multi-tenancy, operational burden, frequent SRE involvement. |
|   9 | Strategic shift to Kubernetes consolidation for a single operational model and cloud-native, cost-efficient infrastructure.                            |
|  10 | Spark as a service on Kubernetes has three main requirements:                                                                                          |
|  11 | Serverless experience with single API/UI entry point.                                                                                                  |
|  12 | Self-service for users, minimal platform team involvement.                                                                                             |
|  13 | Multi-tenancy with workload isolation, security, and guarantees.                                                                                       |
|  14 | User-facing layer: API and UI for job tracking, submissions, and history server replay.                                                                |
|  15 | Orchestration layer: users submit jobs referencing a virtual Spark cluster; system creates necessary Kubernetes resources.                             |
|  16 | Core resource is the Kubeflow SparkApplication object; submission handled by a separate Kubernetes job for scalability and security.                   |
|  17 | Gang scheduling via Volcano pod groups ensures drivers and executors are scheduled together.                                                           |
|  18 | Event timelines exported to object storage for job replay in UI.                                                                                       |
|  19 | Volcano used for batch scheduling, providing gang scheduling, priority, preemption, and hierarchical queues for multi-tenancy.                         |
|  20 | Each Spark job submission creates about 15 Kubernetes objects, totaling 700KB manifest size per 150KB payload.                                         |
|  21 | Accumulation of objects impacts etcd storage; 1,000 concurrent apps ≈ 15,000 objects, nearing 2GB etcd threshold.                                      |
|  22 | High object churn in                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jmz8c3oEmPY)
