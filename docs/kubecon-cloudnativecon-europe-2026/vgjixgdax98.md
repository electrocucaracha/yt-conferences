---
type: Video Note
title: "Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karma... Sung Yun & Antoine Marthey"
description: "In this presentation, S and Antoine from Bloomberg detail the evolution of their managed Trino and Iceberg data platform from a single-cluster, governance-focused architecture to a highly available, multi-cluster deployment designed for res..."
resource: https://www.youtube.com/watch?v=vGjiXGdax98
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, S and Antoine from Bloomberg detail the evolution of their managed Trino and Iceberg data platform from a single-cluster, governance-focused architecture to a highly available, multi-cluster deployment designed for resilience and disaster recovery.
Initially, their platform required service owners and query users to manage high availability and failover themselves, exposing zone-specific endpoints and pushing complexity onto users.
To address this, they introduced a federated Trino API server backed by a stretched etcd cluster, enabling a unified API and centralized state management across multiple Kubernetes clusters.
Using Karmada, an open-source multi-cluster Kubernetes management system, they orchestrate Trino deployments and aggregate cluster statuses, while the Trino Gateway provides a single, highly available query endpoint that intelligently routes requests and handles backend health and failover.
The new architecture abstracts away zone details, automates recovery, and simplifies user workflows, with ongoing plans to expand to more data centers, implement autoscaling, enhance query logging, and enforce resource groups.
The Q&A addressed deployment strategies, disaster recovery validation, integration with managed services, and technical details of their stretched etcd and multi-cluster setup.
# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Bloomberg's managed Trino and Iceberg platform evolved from a single-cluster, governance-focused architecture to a multi-cluster, high-availability design. |
|   2 | The platform serves two main personas: Trino service owners (engineering teams) and query users (analysts, engineers, applications).                        |
|   3 | Previous architecture required users to handle high availability (HA) and disaster recovery (DR) themselves, exposing zone-specific endpoints.              |
|   4 | New architecture provides a unified Trino API endpoint, abstracting away availability zones and handling HA/DR at the platform level.                       |
|   5 | Introduced a Trino API server backed by a stretched etcd cluster as the single source of truth for Trino resources.                                         |
|   6 | Multiple Trino service controller replicas run for HA, with Kubernetes leader election ensuring only one active reconciler.                                 |
|   7 | Carmata (an open-source multi-cluster Kubernetes management system) is used to propagate Trino deployments across member clusters.                          |
|   8 | Carmata monitors Trino deployments and recreates pods in case of failures, ensuring resilience.                                                             |
|   9 | Status aggregation across clusters is handled via a Lua script in Carmata, updating the Trino service status for users.                                     |
|  10 | Trino Gateway acts as a load balancer and proxy, routing queries to healthy Trino pods across clusters.                                                     |
|  11 | Gateway automatically registers/deregisters Trino pods as they scale or recover from failures.                                                              |
|  12 | In case of gateway or pod failures, traffic is rerouted to healthy components; state is preserved in the external etcd.                                     |
|  13 | Trino service owners deploy via a single manifest and unified API; query users access a single, highly available endpoint.                                  |
|  14 | Plans include expanding to more data centers, implementing HPA-driven scaling, logging query metadata, and enforcing resource groups.                       |
|  15 | Blue/green deployments and rolling updates are currently user-managed; future improvements are planned.                                                     |
|  16 | Disaster recovery is validated via end-to-end tests and Trino Gateway's health checks.                                                                      |
|  17 | Carmata is managed as a service at Bloomberg;                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vGjiXGdax98)