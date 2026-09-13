---
layout: default
title:
  "Generalizing Kubernetes Controller Sharding: Patterns That Wo... Motohiro
  Otsuka & Tomoyuki Nakamura"
nav_order: 133
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Tommoakamra and Moto Hiroka discuss their experience
  generalizing command control sharding within a large-scale internal Kubernetes-based
  platform at Li Corporation. They emphasize that sharding is an architectural dec...
resource: https://www.youtube.com/watch?v=7qsOwyE_uOo
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

In this presentation, Tommoakamra and Moto Hiroka discuss their experience generalizing command control sharding within a large-scale internal Kubernetes-based platform at Li Corporation.
They emphasize that sharding is an architectural decision about replication boundaries, not a simple feature or performance hack, and that the choice of sharding axis must align with the dominant dimension of the system’s architecture.
Their initial attempt at namespace-level sharding led to severe resource amplification and operational issues due to the multiplicative effect of manager instances per namespace, prompting a pivot to label-based sharding for the app operator and cluster-based sharding for the deploy operator.
This revised approach respected Kubernetes API semantics, fixed manager count per process, and stabilized shard identity, resulting in predictable resource usage and improved system stability.
The speakers conclude with five general principles for sharding: work within API design, keep manager count fixed, choose sharding axis based on architecture, stabilize shard identity, and prioritize operational risk, noting that the optimal sharding method depends on the dominant dimension of a given architecture.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sharding is an architectural decision about replication boundaries, not a feature or performance hack.                                                    |
|   2 | The system at Li Corporation operates at 66,000 pods, 5,000 nodes, 3,000 namespaces, and 500,000 managed objects.                                         |
|   3 | Scaling issues appeared as longer synchronization and reconcile latency, not out-of-memory errors.                                                        |
|   4 | Most Kubernetes controllers use a single active reader and shared cache, efficient for vertical scaling but not horizontally elastic.                     |
|   5 | Kubernetes Controller Sharding (KCS) enables horizontal scalability by assigning resources to shards using consistent hashing.                            |
|   6 | KCS assigns parent and child resources to the same shard using owner references; deeper dependency chains are not automatically supported.                |
|   7 | Initial design used namespace-level sharding, with one manager per namespace, expecting efficiency.                                                       |
|   8 | In practice, manager instantiation cost per namespace was high, leading to resource amplification and memory/CPU saturation.                              |
|   9 | Namespace sharding caused a multiplication of manager instances (from 41 to 120,000), resulting in catastrophic resource usage.                           |
|  10 | The main cost driver was cache and manager replication per namespace.                                                                                     |
|  11 | Kubernetes lacks a native arbitrary namespace set watch primitive, limiting sharding flexibility.                                                         |
|  12 | Recent Kubernetes development (K5866) introduces hash range sharding for REST and watch operations, initially supporting UID-based sharding.              |
|  13 | KCS is not a full graph partitioner; it is a distributed ownership layer, not a distributed cache framework.                                              |
|  14 | The team pivoted to split the operator into app operator (label-based sharding, one manager per pod) and deploy operator (sharded by data plane cluster). |
|  15 | Pivoted architecture fixed manager count per process and used label-based sharding, making resource usage predictable and bounded.                        |
|  16 | Issues encountered: orphaned resources without owner references were not reconciled; rolling updates changed shard identity, causing API server overload. |
|  17 | Fixes included adoption logic for orphan                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7qsOwyE_uOo)
