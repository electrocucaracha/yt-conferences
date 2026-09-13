---
type: Video Note
title: "Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen & Vec Sun"
description: "John from the OpenKruise community discusses the challenges and solutions for operating AI workloads, focusing on both training/inference and agent-based applications. He explains that training and inference workloads often require large da..."
resource: https://www.youtube.com/watch?v=0JT8iDDS74k
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

John from the OpenKruise community discusses the challenges and solutions for operating AI workloads, focusing on both training/inference and agent-based applications.
He explains that training and inference workloads often require large datasets, specialized hardware like GPUs, and efficient communication libraries, while agent applications demand rapid sandbox creation and robust file system operations.
John introduces several OpenKruise features, such as in-place updates for faster service upgrades, image prewarming to reduce container startup times, and advanced scheduling tools like pod group disruption budgets to maintain service availability.
He also highlights ongoing work to improve pod group management and container restarts, minimizing downtime and resource waste.
Additionally, John presents the OpenKruise Agent project, which offers fast, persistent sandbox allocation, supports hibernation and checkpointing for efficient resource use, and enables rapid cloning and restoration of agent environments, all aimed at optimizing AI workload operations.
He notes that while image prewarming accelerates container readiness, it may increase local disk usage and I/O load.
# Main Points

|   # | Main point                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction by John from OpenKruise community, maintainer                                                                                                                             |
|   2 | Focus on operating AI workloads using OpenKruise and its subprojects                                                                                                                   |
|   3 | Two main AI application types: training/inference (data-heavy, require GPUs/communication devices), and agent/sandbox (require fast creation, file system operations)                  |
|   4 | Agent sandboxes need sub-second startup, command/file system operations, and support for hibernate/resume                                                                              |
|   5 | In-place update operation: updates containers without deleting pods, reuses resources, saves scheduling/IP/volume mounting costs, enables faster image pulling, keeps sidecars running |
|   6 | In-place update adopted by other projects (e.g., SElinux RBG)                                                                                                                          |
|   7 | Image prewarming: pulls images to nodes before scheduling pods, reducing startup time; supports large images with models/data                                                          |
|   8 | OpenKruise provides ImagePullJob CRD for specifying images, parallelism, and node/label targeting                                                                                      |
|   9 | Advanced CronJob supports scheduled image prewarming using image lists and cron syntax                                                                                                 |
|  10 | Port group disruption budget: proposal to protect groups of pods (not just single pods) from voluntary disruptions, ensuring inference service availability                            |
|  11 | In-place restart for pod groups: only failed pods are rescheduled, healthy pods are restarted in place, reducing resource allocation overhead                                          |
|  12 | Current Kubernetes solution requires watcher sidecar; OpenKruise working on container recreate API to avoid this                                                                       |
|  13 | Introduction of OpenKruise Agent project: sandbox solution for fast allocation, state persistence, and AI-friendly APIs                                                                |
|  14 | Key components: sandbox manager, sandbox gateway (efficient routing), sandbox controller (hibernation/wake-up), extended sandbox lifecycle (pause, snapshot, clone)                    |
|  15 | Warm pool enables sample allocation in ~20ms                                                                                                                                           |
|  16 | Supports command execution and file system operations inside sandbox                                                                                                                   |
|  17 | Pause/resume saves rootfs and memory to shared storage for hibernation                                                                                                                 |
|  18 | Checkpoint allows snapshotting and cloning sandboxes for backup or fast startup                                                                                                        |
|  19 | Commit operation saves container rootfs as ima                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0JT8iDDS74k)