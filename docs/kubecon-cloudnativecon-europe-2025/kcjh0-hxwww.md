---
layout: default
title:
  "Museum of Weird Bugs: Our Favorites From 8 Years of Service Mesh Debugging
  - Alex Leong, Buoyant"
nav_order: 200
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=Kcjh0-hXwWw
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: Alex Leong, a maintainer on the Link project, presented on bugs found in Linkerd, a service mesh.
The first bug was related to CRDs, where a memory leak caused the policy controller to become overloaded and eventually be killed by Kubernetes.
The second bug involved routing issues due to stale addresses, which could cause the system to deadlock if one client didn't send window updates.
The third bug was a memory leak that required looking at deallocations in addition to allocations, and being careful what is put in map keys.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Linkerd is a service mesh that has been in use for over 8 years.                                                                                               |
|   2 | The linkerd architecture consists of a data plane (where applications run) and a control plane (which manages traffic).                                        |
|   3 | The control plane uses gRPC streaming API to communicate with the data plane.                                                                                  |
|   4 | A memory leak was found in the policy controller, which caused it to consume increasing amounts of memory.                                                     |
|   5 | The issue was caused by a mismatch between the Kubernetes API and the linkerd CRD, leading to an infinite loop where updates were not being sent to the proxy. |
|   6 | Flow control windows in HTTP2 were exploited to block the entire system if one client did not send window updates.                                             |
|   7 | A queue was introduced to isolate blocking behavior and prevent it from affecting other listeners.                                                             |
|   8 | Memory leaks can be caused by incorrect use of map keys, so it's essential to look at deallocations as well as allocations.                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Kcjh0-hXwWw)
