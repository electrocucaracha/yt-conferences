---
type: Video Note
title: "Defusing the Kubernetes API Performance Minefield - Madhav Jivrajani & Marek Siarkowicz"
description: "Marik Sharkovich, SIG lead of ATC and contributor to API machinery, discusses the challenges of Kubernetes API performance. He highlights the issue of CRDs and operators causing memory spikes due to their lack of scalability testing, leadin..."
resource: https://www.youtube.com/watch?v=SdLLOcNZN5E
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Marik Sharkovich, SIG lead of ATC and contributor to API machinery, discusses the challenges of Kubernetes API performance.
He highlights the issue of CRDs and operators causing memory spikes due to their lack of scalability testing, leading to problems like the one he experienced on GKE where a small cluster's memory spiked 20 times.
To address this, Marik proposes using caching, resource versioning, and list from snapshot features, which are now available in Kubernetes 1.31 and 1.33, respectively.
These features aim to improve performance by reducing allocations and making it easier for users to manage resources without having to write their own API servers.
# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Abusive usage of CRDs can lead to memory spikes and control plane crashes.                                                               |
|   2 | The problem lies in Kubernetes' scalability focusing on its own pipelines and concerns, not testing for external use cases.              |
|   3 | Caching is used to improve performance but has limitations, such as not handling large data or JSON encoding efficiently.                |
|   4 | A new feature called "consistent reads from cache" was introduced in Kubernetes 1.31, which improves caching by using resource versions. |
|   5 | Another feature, "list from snapshot," was introduced in Kubernetes 1.33, which allows for efficient retrieval of cached data.           |
|   6 | Custom JSON encoder implementation improved performance and reduced memory usage.                                                        |
|   7 | CRDs should be used judiciously and scaled testing should be done to ensure compatibility with Kubernetes.                               |
|   8 | Externalizing resources or using a separate API server is an option but requires more management effort.                                 |
|   9 | The custom JSON encoder implementation stitches objects together, detecting the object type and fields before encoding.                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SdLLOcNZN5E)