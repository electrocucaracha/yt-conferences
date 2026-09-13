---
layout: default
title:
  "From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data
  P... Rainie Li & Ang Zhang"
nav_order: 119
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Rainey, a senior engineering manager at Pinterest, outlines
  how Pinterest built a cost-efficient data processing platform on Kubernetes, known
  as Mocha. The platform ingests and processes large-scale data using a combination
  o...
resource: https://www.youtube.com/watch?v=8P2y_gyHQA8
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

In this talk, Rainey, a senior engineering manager at Pinterest, outlines how Pinterest built a cost-efficient data processing platform on Kubernetes, known as Mocha.
The platform ingests and processes large-scale data using a combination of Apache Kafka, Flink, Spark, and a data lake built on AWS S3 with Apache Iceberg as the metadata layer.
Key challenges addressed include managing resource allocation for critical and non-critical jobs, maximizing cluster utilization during off-peak hours, and leveraging unused reserved capacity from online services.
Pinterest employs customized Kubernetes schedulers like Unicorn and Volcano for advanced scheduling, fair sharing, and topology awareness, and has developed a system to dynamically rebalance EC2 capacity between online and offline workloads.
Solutions such as separating driver and executor node groups, implementing global job scheduling and prioritization, and automatic job routing have improved reliability and resource utilization, with ongoing work to further optimize capacity prediction and utilization using machine learning.

# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Pinterest built a cost-efficient data processing platform on Kubernetes, called Mocha.                                                                                                                         |
|   2 | The platform ingests and processes large-scale data from various sources using APIs, logging agents, and a pub/sub service built on Apache Kafka and Mammq.                                                    |
|   3 | Real-time ingestion is handled by Flink streaming applications, storing raw data in AWS S3 with Apache Iceberg as the metadata layer.                                                                          |
|   4 | Data processing compute platform is built on Kubernetes (EKS), using Flink for streaming and Spark for batch processing.                                                                                       |
|   5 | Supports use cases such as indexing, recommendations, signals, data warehouse, business intelligence, and feature store for model development.                                                                 |
|   6 | Mocha platform architecture has two layers: customer teams (owning engines like Spark, Flink, ML platforms) and the Mocha platform (job submission, quota enforcement, resource management, remote shuffling). |
|   7 | Uses customized Kubernetes schedulers (Unicorn, Volcano) and multiple operators (Spark, Flink, Cube).                                                                                                          |
|   8 | Runs thousands of scheduled batch workloads daily, processing hundreds of petabytes of data.                                                                                                                   |
|   9 | Key challenges: high Spark resource usage, ensuring high-priority jobs meet SLOs, low cluster utilization during off-peak hours, and unused reserved capacity from online services.                            |
|  10 | Resource management uses tiered queues with preemption and historical usage-based guarantees.                                                                                                                  |
|  11 | Customized schedulers enable efficient resource utilization, fair sharing, and advanced scheduling features.                                                                                                   |
|  12 | Unused reserved AWS capacity is leveraged for non-critical Spark jobs via a rebalancing approach using separate clusters for online and offline workloads.                                                     |
|  13 | Through utilization project uses a custom controller to move capacity from online to Spark clusters during off-peak hours, scaling clusters up or down as needed.                                              |
|  14 | Mocha decouples compute and storage with remote shuffling, enabling flexible scaling and unified cluster setup.                                                                                                |
|  15 | Solutions for challenges include static node groups for Spark drivers, balancing disk size and IO throughput, global                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8P2y_gyHQA8)
