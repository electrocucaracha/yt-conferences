---
type: Video Note
title: "Slinky Expanded: Slurm, Kubernetes, and DRA - Praveen Krishna, Google & Marlow Warnicke, SchedMD LLC"
description: "Marlo Boricki from Nvidia and Pravin from Google present Slinky, a set of tools designed to integrate Slurm—a leading high-performance computing workload manager—with Kubernetes environments. They focus on Slurm Bridge, which enables Slurm..."
resource: https://www.youtube.com/watch?v=Gy2_BwETo3M
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Marlo Boricki from Nvidia and Pravin from Google present Slinky, a set of tools designed to integrate Slurm—a leading high-performance computing workload manager—with Kubernetes environments.
They focus on Slurm Bridge, which enables Slurm to act as a backend scheduler for Kubernetes by translating pod resource requests into Slurm jobs, allowing both Slurm and Kubernetes workloads to run simultaneously on the same nodes.
The discussion highlights the development of the CPU DRA (Dynamic Resource Allocation) driver, which provides fine-grained, expressive CPU resource allocation within Kubernetes, addressing limitations of the default kubelet CPU management by allowing users to specify detailed CPU requirements such as core type, NUMA node, or socket.
The architecture leverages DRA and NRI (Node Resource Interface) plugins to enforce resource assignments and prevent interference between containers.
Recent advancements now allow for more flexible resource sharing, support for multiple device plugins, and improved integration between Slurm and Kubernetes, with ongoing community efforts to expand capabilities and tighter ecosystem integration.
The session concludes with a live demo, audience Q&A, and an invitation for feedback and collaboration as the tools continue to evolve.
# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Slurm is a leading high performance computing workload manager, used by most top 500 computers and AI/ML training workloads.                  |
|   2 | Slurm manages job scheduling, resource assignment, and scales beyond 15,000 nodes.                                                            |
|   3 | Slinky is a set of tools; main ones are slurm operator and slurm bridge.                                                                      |
|   4 | Slurm bridge turns the slurm controller into a backend for Kubernetes scheduling.                                                             |
|   5 | Pod resources are translated into slurm placeholder jobs, determining pod placement and resource holding.                                     |
|   6 | Slurm bridge leverages the Kubernetes scheduler framework and workload API.                                                                   |
|   7 | Bridge nodes can run both kubelet and slurmd; previously, nodes could only run one type of job.                                               |
|   8 | CPU DRA driver uses Dynamic Resource Allocation (DRA) to manage CPUs in Kubernetes.                                                           |
|   9 | DRA allows flexible, expressive hardware resource requests, including specific CPU types, NUMA nodes, sockets, and L3 cache.                  |
|  10 | CPU DRA driver is deployed as a DaemonSet, scans hardware, and publishes resource slices for resource claims.                                 |
|  11 | Static CPU policy in kubelet must be disabled to avoid resource conflicts with CPU DRA driver.                                                |
|  12 | Two resource representation modes: individual (each CPU as a device, for slurm use cases) and group (logical blocks by topology or property). |
|  13 | DRA enables matching pods to resources based on detailed attributes (e.g., GPU, NIC, CPU on same NUMA node).                                  |
|  14 | Node-level architecture: DRA kubelet plugin prepares resource claims; NRI plugin enforces allocations and manages shared CPUs.                |
|  15 | Slurm bridge with DRA allows kubelet to own nodes, removing need for slurmd everywhere.                                                       |
|  16 | External node support and DRA support added to slurm; multiple pods per node now possible (alpha).                                            |
|  17 | Supported drivers: CPU DRA driver, GPU example driver, NVIDIA GPU driver (alpha).                                                             |
|  18 | Live demo showed resource claims for CPU and GPU assigned by slurm.                                                                           |
|  19 | Slurm creates resource claims with exact CPUs, DRA driver enforces them via NRI and cgroups.                                                  |
|  20 | Slurm is close to being a first-class citizen in Kubernetes; networking alignment is pending.                                                 |
|  21 | S                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Gy2_BwETo3M)