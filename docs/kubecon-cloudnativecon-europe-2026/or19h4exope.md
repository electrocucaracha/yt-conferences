---
layout: default
title:
  "SIG API Machinery: SIG Updates and Deep Dive in the AI/ML Era - Stefan Schimanski,
  NVIDIA"
nav_order: 315
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker provides an update on the SIG API Machinery, focusing on
  recent and upcoming changes that support AI and ML workloads in Kubernetes. The
  talk highlights improvements in API server mechanics, such as mutating admission
  policies n...
resource: https://www.youtube.com/watch?v=Or19H4ExOPE
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

The speaker provides an update on the SIG API Machinery, focusing on recent and upcoming changes that support AI and ML workloads in Kubernetes.
The talk highlights improvements in API server mechanics, such as mutating admission policies now being generally available, and new features like static manifest directories for admission configurations.
A major focus is on scaling the API server to handle very large clusters, as required by AI workloads, through a trilogy of changes: caching quorum reads, streaming list responses, and enabling paging from cache using B-tree snapshots.
These enhancements significantly reduce memory usage and improve performance, allowing Kubernetes to support clusters much larger than previously tested.
Additional features like watch-based streaming and controller sharding are discussed, along with ongoing work to optimize for large pod specs and deduplicate data.
Users are advised to update both their Kubernetes clusters and client libraries to benefit from these improvements, most of which are enabled by default in version 1.35 and later.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | SIG API Machinery focuses on API server mechanics: versioning, serialization, REST mechanics, resource definitions, OpenAPI, CRDs, admission, client and controller mechanics. |
|   2 | Does not own API reviews, most controllers, deployments, kubectl, or etcd.                                                                                                     |
|   3 | Kubernetes 1.35 released; 1.36 expected in April.                                                                                                                              |
|   4 | Mutating Admission Policy is now GA: allows embedded admission logic without webhooks, supports JSON patches and config map references.                                        |
|   5 | New feature: static manifest directory for admission, enabling manifests on disk for managed service providers; manifests are not visible in the cluster.                      |
|   6 | AI/ML workloads require scaling Kubernetes clusters far beyond previous limits (e.g., 100,000+ nodes, millions of pods).                                                       |
|   7 | API server list/read performance improvements are critical for large clusters.                                                                                                 |
|   8 | Three main improvements ("trilogy"):                                                                                                                                           |
|   9 | Consistent reads from cache: API server waits for cache to be up-to-date with etcd before serving quorum reads, reducing etcd load.                                            |
|  10 | Streaming encoding: API server streams list responses element-by-element, reducing memory usage and latency.                                                                   |
|  11 | Paging from cache: B-tree snapshotting enables consistent paging from cache, avoiding time travel and reducing memory spikes.                                                  |
|  12 | Watch list: new streaming method for informers, sends initial list as watch events, now default in client-go and controller-runtime.                                           |
|  13 | All major improvements are GA or default in Kubernetes 1.35+; no client changes needed except updating client-go and cluster version.                                          |
|  14 | Sharding support (alpha): hash-based partitioning of watch requests to distribute load across controllers.                                                                     |
|  15 | Future ideas: optimize for large pod specs, deduplicate pod spec data, improve managed fields memory usage, make priority/fairness aware of object size.                       |
|  16 | SIG API Machinery meets biweekly; contributions and feedback are welcome.                                                                                                      |
|  17 | To benefit from new features: update Kubernetes cluster and client-go to recent versions (1.35+).                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Or19H4ExOPE)
