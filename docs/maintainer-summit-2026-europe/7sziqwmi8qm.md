---
layout: default
title: "Unconference Session: Checkpoint/Restore BoF"
nav_order: 12
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "The speaker presents the current work-in-progress API concept for the Kubernetes Checkpoint Restore working group, focusing on three primary use cases: suspend/resume, live migration, and warm star..."
resource: "https://www.youtube.com/watch?v=7SZIqWmi8QM"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

The speaker presents the current work-in-progress API concept for the Kubernetes Checkpoint Restore working group, focusing on three primary use cases: suspend/resume, live migration, and warm starts for applications like Java.
The proposed architecture introduces a separate checkpoint controller to manage checkpoint objects, decoupling their lifecycle from the pod to allow for persistence and restoration even if the original pod is deleted, while the restore process is integrated into the pod specification.
Key open questions discussed include how to handle different implementations like CRIU and gVisor, the storage and transfer of large checkpoint archives (potentially using artifacts or registries), and security policies regarding who can initiate checkpoints.
The session also addresses the need for controller integration to support higher-level workloads like Deployments or PyTorch jobs, ensuring that checkpointing can be orchestrated across multiple pods while respecting topology constraints.
Finally, the speaker emphasizes that while node-to-node migration is a long-term goal requiring strict hardware and kernel compatibility, the immediate focus is on establishing a robust, in-tree API that allows for flexible, secure, and expressive checkpoint management within the Kubernetes ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Checkpoint Restore working group is exploring three primary use cases: suspend and resume, live migration, and warm start for applications like Java.                                   |
|   2 | The goal is to support controller integration so that workloads like Deployments and JobSets can be checkpointed and restored, not just individual pods.                                    |
|   3 | Multiple implementations exist, including GVisor and CRIU, requiring a pluggable API design to accommodate different checkpoint and restore options.                                        |
|   4 | A key architectural decision is whether checkpoints should be a new field in the Pod object or a separate object, with the current leaning toward a separate object to decouple lifecycles. |
|   5 | Checkpoint archives can be large, especially with GPU memory, raising questions about storage solutions and how to move them between nodes without relying solely on the kubelet.           |
|   6 | Security considerations include defining who is allowed to checkpoint a pod, whether namespace is the correct boundary, and how policy engines should dictate permissions.                  |
|   7 | The current work-in-progress API concept involves a dedicated checkpoint controller to manage checkpoint objects and embedding restore specifications within the Pod spec.                  |
|   8 | This mixed approach allows the checkpoint lifecycle to be detached from the pod, enabling restoration on different nodes or after the original pod is deleted.                              |
|   9 | Restoring a checkpoint currently requires matching the original pod spec closely, with limited ability to change fields like name or namespace to avoid security and compatibility issues.  |
|  10 | Moving checkpoints between nodes is a future goal, requiring validation of kernel versions, dynamic libraries, and hardware compatibility before transfer.                                  |
|  11 | Device management, such as GPU memory and DRA drivers, needs special handling to ensure resources are properly allocated and released during migration.                                     |
|  12 | The API should be robust enough to express node moving in the future, even if the implementation is not immediate, to support long-term scheduling and preemption scenarios.                |
|  13 | Checkpoints could potentially be stored as artifacts in a registry, similar to container images, to simplify transport and enable versioning or base checkpoint updates.                    |
|  14 | Group checkpointing for multiple pods or workloads is a consideration, requiring coordination mechanisms to ensure consistent state across related pods.                                    |
|  15 | The API design aims to be workload-agnostic, focusing on pod-level checkpointing while allowing higher-level controllers to manage the orchestration of checkpoint sets.                    |
|  16 | Topology constraints and hardware requirements must be preserved during restore to ensure compatibility, especially for workloads with specific scheduling needs.                           |
|  17 | Integration with the eviction API is a long-term goal to allow efficient handling of pod evictions by saving state before termination.                                                      |
|  18 | The proposal favors a built-in Kubernetes API over a CRD-based operator to ensure trust, multi-tenancy safety, and direct kubelet interaction.                                              |
|  19 | The checkpoint controller would manage the communication with the CRI implementation to execute checkpoints, while the kubelet handles the actual restore process.                          |
|  20 | Future discussions will cover practical demonstrations of checkpointing with GPU workloads and further refinement of the API structure.                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7SZIqWmi8QM/hqdefault.jpg)](https://www.youtube.com/watch?v=7SZIqWmi8QM)

[Watch on YouTube](https://www.youtube.com/watch?v=7SZIqWmi8QM)
