---
layout: default
title:
  "A Tale of Two KEPs: How the Community is Taming Kubernetes' CrashLoopBackoff
  - Yang Li, Google"
nav_order: 6
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Yang, a technical solutions engineer at Google Cloud, shares his experience
  with Kubernetes' "crash loop backoff" behavior, where containers that repeatedly
  crash are restarted with increasing delays, up to five minutes. This mechanism,
  int...
resource: https://www.youtube.com/watch?v=FlTb383gXbU
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

Yang, a technical solutions engineer at Google Cloud, shares his experience with Kubernetes' "crash loop backoff" behavior, where containers that repeatedly crash are restarted with increasing delays, up to five minutes.
This mechanism, introduced in 2015 without deep benchmarking, has frustrated users who want more control over restart timing for various scenarios, such as task-based workloads, quick recoveries from transient errors, and critical sidecar failures.
Over the years, users resorted to workarounds like custom scripts and forks to bypass the hardcoded delay.
To address these issues, Kubernetes Enhancement Proposal (KEP) 4603 was introduced, allowing cluster operators to configure the maximum backoff period at the node level, with a safe minimum of one second, based on stress testing.
This change, split into two KEPs for safer rollout, gives operators granular control over restart behavior without compromising node stability, and is now available in Kubernetes 1.35.
Yang demonstrates the practical benefits of these changes and emphasizes the importance of balancing user needs with system reliability and the incremental nature of open source improvements.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yang has worked with Kubernetes since 2017 as an application developer, cluster administrator, contributor, and is currently a technical solution engineer at Google Cloud.                    |
|   2 | CrashLoopBackOff means a container is crashing repeatedly; Kubernetes increases restart delays up to five minutes to conserve resources.                                                       |
|   3 | Kubernetes Enhancement Proposals (KEPs) help coordinate non-trivial project changes.                                                                                                           |
|   4 | The five-minute CrashLoopBackOff delay was introduced in 2015 without deep benchmarking, simply to throttle misbehaving containers.                                                            |
|   5 | Delay doubles up to 300 seconds; container must run cleanly for 10 minutes to reset.                                                                                                           |
|   6 | Issue 57291 (opened in 2017) requested making the behavior adjustable; it is the third most reacted-to issue in the core repository.                                                           |
|   7 | Users requested: (1) Success exit (no penalty for exit code 0), (2) Early recovery (faster restart after transient errors), (3) Manual reset for stuck pods.                                   |
|   8 | Workarounds included Bash wrappers, custom reaper operators, and patching Kubernetes to change the hardcoded delay.                                                                            |
|   9 | Three modern user stories where the five-minute delay fails: task isolation (e.g., queue workers), highly coupled workloads (e.g., AI/ML jobs), and critical sidecars (e.g., network proxies). |
|  10 | KEP 4603 (2024) aimed to make CrashLoopBackOff configurable, balancing developer experience and node stability.                                                                                |
|  11 | Alternatives like instant restarts for exit code 0 and a new "rapid" restart policy were rejected due to risks and compatibility issues.                                                       |
|  12 | Stress tests showed a 1-second minimum restart limit is safe for nodes.                                                                                                                        |
|  13 | Kubernetes 1.32 introduced a node-level configuration for max container restart period (minimum 1 second); 1.33 allowed global initial backoff of 1 second and minimum backoff of 1 minute.    |
|  14 | Node-level configuration gives cluster operators control, limiting risk to specific node pools.                                                                                                |
|  15 | KEP 5593 split from KEP 4603 to fast-track node-level setting to beta (available in 1.35).                                                                                                     |
|  16 | Demonstrations showed faster recovery and improved behavior for task i                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FlTb383gXbU)
