---
type: Video Note
title: "Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kub... Peter H, Adrian R, Radostin S & Viktória S"
description: "In this session, Razin, Peter, and Victoria introduce the Kubernetes Checkpoint Restore Working Group, outlining the background, motivations, and current progress of integrating checkpoint and restore functionality into Kubernetes. Checkpoi..."
resource: https://www.youtube.com/watch?v=lLxrtmpIlMk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Razin, Peter, and Victoria introduce the Kubernetes Checkpoint Restore Working Group, outlining the background, motivations, and current progress of integrating checkpoint and restore functionality into Kubernetes.
Checkpoint restore, originally developed for saving and resuming application states (similar to saving games), has evolved to address use cases such as accelerating application startup, improving fault tolerance, and optimizing resource utilization, particularly for expensive and scarce GPU resources.
The group describes the technical challenges and historical development, including initial implementations in Docker and Podman, and the move toward Kubernetes-native support, with a focus on minimal viable use cases like forensic container checkpointing and warm start scenarios.
They discuss the complexities of designing APIs that balance flexibility, security, and practicality, as well as open questions around pod identity, storage, security, and integration with higher-level Kubernetes objects.
The session concludes with a call for community participation to help shape the feature, address open questions, and ensure the solution meets diverse user needs.
# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Razin (PhD student, University of Oxford), Peter Hunt (Red Hat, SIG Node chair), Victoria (Masaryk University)                                                         |
|   2 | Checkpoint restore allows saving and restoring the state of containers/pods, similar to saving and loading in games                                                                |
|   3 | Concept dates back to 2005; gained traction around 2010; complex to implement, especially in Kubernetes                                                                            |
|   4 | Motivations: Many companies building software stacks around checkpoint restore, especially for GPU resources due to cost and scarcity                                              |
|   5 | Three main use cases:                                                                                                                                                              |
|   6 | Accelerating application startup (e.g., AI agents, Java apps)                                                                                                                      |
|   7 | Fault tolerance for long-running workloads (periodic checkpointing to avoid loss of work)                                                                                          |
|   8 | Optimizing resource utilization (load balancing, non-disruptive preemption, resource reclamation)                                                                                  |
|   9 | Integration history: Started with Docker, then Podman; Google integrated with Borg; now at container-level checkpointing in Kubernetes                                             |
|  10 | Initial focus: Forensic container checkpointing to simplify Kubernetes changes                                                                                                     |
|  11 | Beta version enabled by default in Kubernetes 1.30                                                                                                                                 |
|  12 | Two proof-of-concept implementations: built-in (controller manager modification) and external snapshot                                                                             |
|  13 | Proposed design: User creates a pod checkpoint object; controller processes request and creates checkpoint; restore handled via separate object for security and lifecycle reasons |
|  14 | Three main restore scenarios:                                                                                                                                                      |
|  15 | Warm start (new pods from checkpoint, no IP migration)                                                                                                                             |
|  16 | Suspend/resume (retain pod identity, ideally seamless)                                                                                                                             |
|  17 | Live migration (move pod state to another node)                                                                                                                                    |
|  18 | Prioritizing minimal initial implementation, focusing on warm start use case                                                                                                       |
|  19 | Open questions:                                                                                                                                                                    |
|  20 | Security: Who can checkpoint/restore? How to prevent data leaks?                                                                                                                   |
|  21 | API design: How to support multiple implementations (CRIU, gVisor, etc.)?                                                                                                          |
|  22 | Storage: Where to store checkpoint archives, especially for large GPU memory?                                                                                                      |
|  23 | Namespace migration, policy granularity, integration with higher-level objects (deployments, jobs)                                                                                 |
|  24 | Handling paused state, sidecars, init                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lLxrtmpIlMk)