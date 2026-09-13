---
layout: default
title:
  Do You Trust Your PodDisruptionBudgets? You Shouldn’t! - Kārlis Akots Gribulis,
  Saxo Bank
nav_order: 94
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Carlo Sakos Gribbles, a container platform engineer at Saxo Bank, discusses
  the intricacies and limitations of Kubernetes Pod Disruption Budgets (PDBs). He
  explains that while PDBs are designed to maintain application stability during volun...
resource: https://www.youtube.com/watch?v=yRc4yr7CQh4
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

Carlo Sakos Gribbles, a container platform engineer at Saxo Bank, discusses the intricacies and limitations of Kubernetes Pod Disruption Budgets (PDBs).
He explains that while PDBs are designed to maintain application stability during voluntary disruptions by specifying minimum available or maximum unavailable pods, they have significant gaps: PDBs only apply to eviction API calls and are bypassed by direct pod deletions, restarts, and involuntary disruptions such as hardware failures or network issues.
Through demonstrations, he shows how pod priorities can override PDBs, and how certain kubectl drain flags can ignore them entirely.
Carlo emphasizes that PDBs are most effective during node drains but should not be solely relied upon; instead, they should be used alongside resource requests, pod replication, topology constraints, update strategies, and priority classes to ensure high availability.
He concludes by advising caution and awareness of PDB limitations, likening them to "Swiss cheese" with many holes, and encourages further learning on workload prioritization in Kubernetes.

# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker: Carlo Sakos Gribbles, container platform engineer at Saxo Bank, with prior experience at Accenture and Vox.                                                         |
|   2 | Saxo Bank: Founded in 1992, $100B client assets, 1.5M clients, 70,000 financial instruments, designated CFI bank.                                                            |
|   3 | Pod Disruption Budgets (PDBs): Protect pods during voluntary disruptions; two settings—minimum available or maximum unavailable (cannot set both).                           |
|   4 | PDBs apply only to eviction API calls, not to delete API calls; delete bypasses PDBs.                                                                                        |
|   5 | PDBs do not protect against involuntary disruptions (hardware failure, hypervisor failure, node deletion, kernel panic, network partition, resource exhaustion, spot nodes). |
|   6 | Involuntary disruptions still count against PDBs; Kubernetes tries not to go further in depth if possible.                                                                   |
|   7 | Voluntary disruptions: Triggered by user/service account actions (image/resource updates, deployment/controller deletion, scaling, node updates, cluster autoscaler).        |
|   8 | PDBs can be problematic if set to maxUnavailable=0 or minAvailable=100%—can block cluster updates and node drains.                                                           |
|   9 | Ways to bypass PDBs:                                                                                                                                                         |
|  10 | Disable eviction flag in kubectl drain (uses delete API).                                                                                                                    |
|  11 | Force flag (removes unmanaged pods).                                                                                                                                         |
|  12 | Grace period flag (after timeout, deletes pods directly).                                                                                                                    |
|  13 | Pod priorities (priority classes): Higher priority pods can preempt lower priority pods, ignoring PDBs.                                                                      |
|  14 | Default pod priority is zero if not specified.                                                                                                                               |
|  15 | Preemption can be disabled per priority class or pod.                                                                                                                        |
|  16 | PDBs are ignored during restarts, image/resource updates, and delete calls; only respected during node drains.                                                               |
|  17 | Quality of Service (QoS): BestEffort, Burstable, Guaranteed—affects eviction under node resource pressure, not scheduling.                                                   |
|  18 | Recommendations:                                                                                                                                                             |
|  19 | Set resource requests appropriately.                                                                                                                                         |
|  20 | Use pod replication with topology spread constraints, pod anti-affinity, node affinity.                                                                                      |
|  21 | Tune update strategy to match PDB expectations.                                                                                                                              |
|  22 | Use priority classes and QoS for critical workloads.                                                                                                                         |
|  23 | PDBs are useful but have limitations; do not blindly trust                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yRc4yr7CQh4)
