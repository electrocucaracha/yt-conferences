---
type: Video Note
title: "Simplifying Apache Kafka on Kubernetes With Strimzi - Paolo Patierno & Gantigmaa Selenge, Red Hat"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=sLFmnCyZ89M
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: Paulo Paderno, a software engineer at Red Hat, introduces StreamZy, an open-source project that manages Apache Kafka and Kubernetes.
The main features of StreamZy include Craft Tier Storage, which simplifies metadata management and improves scalability, and Auto Rebalancing on Cluster Scaling, which automates rebalancing and scaling of Kafka clusters.
Additionally, StreamZy is moving towards v1 APIs and will support Gateway API for exposing Kafka clusters outside of Kubernetes.
The project also aims to improve certificate management and is exploring the concept of Stretch Clusters across multiple Kubernetes clusters.
# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | Apache Kafka is a leading distributed event streaming platform that scales horizontally and is highly available.              |
|   2 | StreamZ is an open-source project that manages Apache Kafka and Kubernetes, providing operational simplicity and scalability. |
|   3 | Craft is a feature of StreamZ that removes ZooKeeper dependency for metadata management, simplifying deployment and scaling.  |
|   4 | Craft clusters are more scalable and efficient than ZooKeeper-based clusters.                                                 |
|   5 | Tier storage allows offloading older messages to cheaper storage, reducing costs and improving performance.                   |
|   6 | Auto-rebalancing on cluster scaling reduces manual rebalancing efforts.                                                       |
|   7 | Improved certificate management is being implemented with better integration with cert-manager.                               |
|   8 | Gateway API support is planned for StreamZ, allowing built-in integration with gateway APIs.                                  |
|   9 | Stretch clusters are being discussed, but face challenges due to Kafka's sensitivity to latency.                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=sLFmnCyZ89M)