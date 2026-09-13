---
type: Video Note
title: "Evicted! All the Ways Kubernetes Kills Your Pods (and How To Avoid Them) - Ahmet Alp Balkan"
description: "In this CubeCon presentation, Amad Al Palkin, who leads Kubernetes infrastructure at LinkedIn, discusses the internal mechanisms of Kubernetes that can evict pods and potentially threaten application availability. Drawing from LinkedIn’s la..."
resource: https://www.youtube.com/watch?v=jVwXcuNEDYE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this CubeCon presentation, Amad Al Palkin, who leads Kubernetes infrastructure at LinkedIn, discusses the internal mechanisms of Kubernetes that can evict pods and potentially threaten application availability.
Drawing from LinkedIn’s large-scale, bare-metal Kubernetes deployment, he explains that every major Kubernetes component—such as the API server, kubelet, scheduler, and controller manager—can initiate pod evictions for reasons ranging from resource pressure and node taints to rolling updates and affinity mismatches.
He emphasizes that Kubernetes’ default eviction controls, like Pod Disruption Budgets (PDBs), are limited, especially for stateful workloads, and that many eviction paths do not honor PDBs or allow for graceful termination.
Through a series of demos, he illustrates how different eviction scenarios play out and highlights the importance of understanding and tuning eviction settings, collecting audit logs, and possibly implementing custom eviction policies to maintain reliability.
The talk concludes with practical advice on disaster recovery drills, adjusting toleration and eviction thresholds, and the need for deeper operational awareness when running Kubernetes at scale.
# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation explores Kubernetes internals and how components can evict pods, impacting availability.                                     |
|   2 | Speaker: Amad Al Palkin, leads Kubernetes infrastructure at LinkedIn.                                                                     |
|   3 | LinkedIn runs thousands of microservices and databases on Kubernetes, with a large bare metal fleet.                                      |
|   4 | Kubernetes components can evict pods, posing risks to application availability.                                                           |
|   5 | Eviction defined as Kubernetes stopping an application, not the app exiting on its own.                                                   |
|   6 | Main concerns: evictions risk availability, desire for graceful terminations, challenges with stateful apps, and minimizing pod movement. |
|   7 | Bare metal environments expose node disruptions more than cloud providers.                                                                |
|   8 | Kubernetes offers limited eviction controls; PDBs (Pod Disruption Budgets) have limited expressivity, especially for stateful workloads.  |
|   9 | API server evictions:                                                                                                                     |
|  10 | Pod delete API: deletes pods without PDB checks; controllers decide behavior.                                                             |
|  11 | Pod eviction API: checks PDBs before evicting; used by kubectl drain and cloud providers.                                                 |
|  12 | Kubelet evictions:                                                                                                                        |
|  13 | Node pressure evictions: evicts pods under resource pressure (memory, disk, etc.), ignores PDBs.                                          |
|  14 | Kubelet admission: refuses to run pods if resources or affinity rules aren't met; can terminate pods if node labels change.               |
|  15 | Local storage evictions: pods evicted if ephemeral storage limits are exceeded.                                                           |
|  16 | Scheduler evictions:                                                                                                                      |
|  17 | Pod preemption: evicts lower-priority pods to schedule higher-priority ones; PDBs honored best-effort.                                    |
|  18 | Controller manager evictions:                                                                                                             |
|  19 | Taint-based evictions: no execute taints (e.g., not ready, unreachable) cause pod eviction after toleration period.                       |
|  20 | Pod GC controller: deletes pods if their node object is deleted and doesn't return in 60 seconds.                                         |
|  21 | Eviction interception: possible via webhooks; new features coming for custom eviction policies.                                           |
|  22 | Pod disruption conditions: added before deletion; recommend collecting audit logs and events for debugging.                               |
|  23 | Recommendations: adjust eviction thresholds, perform disaster rec                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jVwXcuNEDYE)