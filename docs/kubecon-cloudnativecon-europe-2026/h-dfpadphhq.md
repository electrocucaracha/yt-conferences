---
type: Video Note
title: "WG-Batch Updates: What’s New and What Is Next? - Yuki Iwai, CyberAgent, Inc. & Kevin Hannon, Red Hat"
description: "The presentation provides an update from the Kubernetes Batch Working Group, led by Yuki and Kevin, focusing on enhancements for batch workloads such as AI, ML, and data analytics. The group aims to reduce fragmentation in Kubernetes by imp..."
resource: https://www.youtube.com/watch?v=H_dfPaDpHHQ
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation provides an update from the Kubernetes Batch Working Group, led by Yuki and Kevin, focusing on enhancements for batch workloads such as AI, ML, and data analytics.
The group aims to reduce fragmentation in Kubernetes by improving APIs (like job and job set), scheduling primitives, tooling for cluster utilization, and support for specialized hardware.
Recent updates include the graduation of pod replacement policy, mutable pod resources and scheduling directives for suspended jobs, and the enablement of workload with job.
The JobSet project has introduced features like execution ordering, volume claim policies, failure policies, and in-place restarts to better support distributed workloads.
The Q scheduler, a second-level scheduler for AI workloads, now supports advanced topology-aware scheduling algorithms and API upgrades, with future plans for extended resource and elastic job support.
The team is also working on workload-aware scheduling and gang scheduling APIs to simplify group-based scheduling and improve support for complex AI workloads, encouraging community involvement and integration with these new features.
# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Yuki (CyberAgent, chair of batch tracking group) and Kevin (Red Hat, senior software engineer, chair of working group batch)                                |
|   2 | Batch tracking group focuses on enhancing Kubernetes support for batch roles (AI/ML, data analytics, CI, etc.)                                                                        |
|   3 | Goals: reduce fragmentation, improve batch APIs (job, job set), develop work queuing/scheduling primitives, tooling for cluster utilization, support specialized hardware (GPUs/TPUs) |
|   4 | Job updates:                                                                                                                                                                          |
|   5 | Pod replacement policy graduated to GA in 1.34; two strategies: "terminating or failed" (default), "failed" (new, prevents replacement if previous pods exist)                        |
|   6 | Mutable pod resources for suspended jobs: allows changing pod spec resource requests/limits when job is suspended                                                                     |
|   7 | Mutable scheduling directives for suspended jobs: enables resetting job status start time with one API call                                                                           |
|   8 | Enable workload with job: auto-creates workload and pod group resources for jobs (currently supports non-erratic index jobs)                                                          |
|   9 | JobSet updates:                                                                                                                                                                       |
|  10 | Supports multiple templates for distributed workloads (AI/HPC/ML)                                                                                                                     |
|  11 | "DependsOn" feature for execution ordering (e.g., data/model download before training)                                                                                                |
|  12 | Volume claim policies at job set level for persistent/temporary storage                                                                                                               |
|  13 | Failure policy: toggles job restarts based on conditions/exit codes, supports in-place restarts                                                                                       |
|  14 | Q (AI workload scheduler):                                                                                                                                                            |
|  15 | Sits in front of kube-scheduler, manages resource allocation, supports fair sharing, machine flavor preferences                                                                       |
|  16 | Implements scheduling algorithms: best fit, capacity, balance placement, multi-layer topology                                                                                         |
|  17 | API graduation from v1beta1 to v1beta2; migration steps outlined                                                                                                                      |
|  18 | Supports node taints, eviction, reassignment, and multi-queue functionalities                                                                                                         |
|  19 | Upcoming: DIA extended resource support, elastic job support, multi-area topology, atomic preemption, feature graduations                                                             |
|  20 | Workload aware scheduling:                                                                                                                                                            |
|  21 | Introduced workload and pod group APIs for group-based/gang scheduling                                                                                                                |
|  22 | Supports min count, status, re                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=H_dfPaDpHHQ)