---
type: Video Note
title: "Where’s All My Memory Gone? Mapping K8s Memory Metrics To Physical Resources - Mahé Tardy"
description: "The speaker discusses mapping Kubernetes memory usage to physical resources. They explain that container memory working set bytes is a metric used behind the scenes, which is actually computed by CAdvisor inside Kublet. The main culprit beh..."
resource: https://www.youtube.com/watch?v=zLHdgl2qxbg
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses mapping Kubernetes memory usage to physical resources.
They explain that container memory working set bytes is a metric used behind the scenes, which is actually computed by CAdvisor inside Kublet.
The main culprit behind this metric is CAdvisor itself, specifically its computation of "current" and "inactive file" statistics from cgroups v2.
These statistics are then subtracted to produce the actual memory usage.
The speaker also touches on the concept of virtual memory, how Linux overcommits memory, and how CAdvisor uses these concepts to compute the container memory working set bytes metric.
# Main Points

|   # | Main point                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------- |
|   1 | The container memory working set bytes is a metric used to track memory usage in Kubernetes.             |
|   2 | It comes from CAdvisor, which uses the CGroup v2 API to collect metrics.                                 |
|   3 | CAdvisor computes the working set by subtracting inactive files from current memory usage.               |
|   4 | Current memory usage is obtained from the cgroup's memory stats.                                         |
|   5 | Inactive files are stored on disk and can be reclaimed when needed.                                      |
|   6 | The out-of-memory killer targets containers with high working sets before those with lower working sets. |
|   7 | Kubernetes uses CGroups to manage resource allocation for containers.                                    |
|   8 | CGroups provide a way to restrict CPU and memory usage for processes.                                    |
|   9 | The kernel exposes memory statistics through read-only files, which can be used to track memory usage.   |
|  10 | Memory is divided into main memory (physical) and virtual memory (which can be reclaimed).               |
|  11 | The container memory working set bytes provides a good enough uristic for actual memory use.             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zLHdgl2qxbg)