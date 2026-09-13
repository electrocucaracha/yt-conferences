---
layout: default
title:
  "Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Vi... Fan Zhang,
  Kevin Klues & Alay Patel"
nav_order: 72
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Fan Fan Jang, Kevin Clues, and Ali Patel from Nvidia
  discuss their work on enabling cloud-native virtualization for the GB200 GPU platform,
  focusing on making a single VM behave like a complete compute tray with accura...
resource: https://www.youtube.com/watch?v=jtnRFgu4tdI
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

In this presentation, Fan Fan Jang, Kevin Clues, and Ali Patel from Nvidia discuss their work on enabling cloud-native virtualization for the GB200 GPU platform, focusing on making a single VM behave like a complete compute tray with accurate device locality and NUMA topology for AI workloads.
They detail the technical challenges of virtualizing the GB200’s coherent architecture, including mandatory nested translation, memory backing with Extended GPU Memory (EGM), and precise topology mapping, all of which are essential for performance and correctness.
The team explains how they adapted Kubernetes and KubeVirt to support these requirements, including custom patches, container runtime considerations, and handling complex NUMA configurations.
They introduce Nvidia’s solution for multi-node GPU communication using NVLink and Kubernetes abstractions like compute domains, which simplify user experience by automating the setup of multi-node GPU ensembles.
Finally, they address the unique challenges of orchestrating IMX daemons within VMs, proposing current manual solutions and outlining ongoing efforts to further streamline and automate this process for users.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nvidia team presented on cloud-native virtualization for GPU data centers and AI factories.                                                                                                   |
|   2 | Goal: Make one VM on GB200 behave like one compute tray.                                                                                                                                      |
|   3 | GB200 compute tray: two Grace ARM CPUs, each connected to two Blackwell GPUs via NVLink C2C (900 GB/s bidirectional bandwidth).                                                               |
|   4 | VM must reflect host’s NUMA and device locality for AI workload performance and stability.                                                                                                    |
|   5 | Grace virtualization differs due to system coherence; not just GPU passthrough.                                                                                                               |
|   6 | Three key virtualization components:                                                                                                                                                          |
|   7 | Translation: Nested translation with SMMUv3; guest owns stage one, host enforces stage two.                                                                                                   |
|   8 | Memory backing: Uses Extended GPU Memory (EGM); EGM regions are reserved, hidden from host, mapped into guest; VGM only supported at compute tray boundary (all GPUs must be passed through). |
|   9 | Topology: NUMA and device topology must match host; guest ACPI and NUMA relationships carefully constructed.                                                                                  |
|  10 | Nvidia delivered customized libvirt/qemu patches (available on GitHub).                                                                                                                       |
|  11 | Cloud-native virtualization (KubeVirt) introduces more layers and constraints than bare metal.                                                                                                |
|  12 | Four contracts for enablement:                                                                                                                                                                |
|  13 | Boot: VM must boot reliably with four GPUs and high-speed IO; large PCIe BAR mapping required.                                                                                                |
|  14 | Container: Memory lock and process capabilities matter; missing CAP_IPC_LOCK can cause failures.                                                                                              |
|  15 | Kubernetes: NUMA topology complexity (34 NUMA nodes, only 2 CPU NUMA); topology manager can hang; improvements tracked via Kubernetes CAP.                                                    |
|  16 | Grace platform parity: Guest must reflect real Grace platform semantics; NUMA planner aligns constraints.                                                                                     |
|  17 | Single-node VM on GB200 compute tray achieved; GPU/CPU data traffic uses NVLink C2C for high bandwidth.                                                                                       |
|  18 | Scaling beyond single node: Multi-node NVLink and compute domains.                                                                                                                            |
|  19 | Compute domain abstraction (via DRA driver) allows users to declare multi-node connectivity in Kubernetes.                                                                                    |
|  20 | IMX daemons coordinate GPU communication across nodes; standard Kubernetes scheduling applies.                                                                                                |
|  21 | For VMs, IMX daemon must run inside guest; challenges includ                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jtnRFgu4tdI)
