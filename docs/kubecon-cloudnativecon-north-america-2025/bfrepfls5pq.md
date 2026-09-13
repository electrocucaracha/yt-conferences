---
type: Video Note
title: "Deep Dive: Handling Kubernetes Memory Pressure & Achievi... Ajay Sundar Karuppasamy, & Itamar Holder"
description: "The speaker, a software engineer at Google, discusses optimizing swap in Kubernetes. They share their experience with stress testing swap on GKE and highlight the importance of kernel tuning and faster storage setups to ensure smooth swap a..."
resource: https://www.youtube.com/watch?v=bFrEPfls5PQ
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a software engineer at Google, discusses optimizing swap in Kubernetes.
They share their experience with stress testing swap on GKE and highlight the importance of kernel tuning and faster storage setups to ensure smooth swap activity.
The speaker emphasizes that early and gradual swapping is better than late and aggressive freezing, and recommends setting parameters such as min free kilobytes and watermark scale factor to control swap aggressiveness.
They also discuss the limitations of Kubernetes eviction and recommend separating swap IO from application or cube system traffic to avoid interference.
# Main Points

|   # | Main point                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------- |
|   1 | Swap can be deployed in two ways: as a partition or with a file.                                         |
|   2 | File-based swap is generally faster and more flexible than partition-based swap.                         |
|   3 | Control plane nodes should not use swap, but single-node clusters may be an exception.                   |
|   4 | Dedicated disks are recommended for swap to separate IO pressure from the main system.                   |
|   5 | The croup knob can prioritize IO access for system-level processes.                                      |
|   6 | System demons should not use swap by default, and it's recommended to disable swap for the system slice. |
|   7 | Swap can be optimized using kernel parameters such as swappiness and watermark scale factor.             |
|   8 | Raising the min watermark creates a larger safety buffer for the kernel.                                 |
|   9 | Widening the watermark scale factor allows for more gradual swap activity.                               |
|  10 | Proper kernel tuning and faster storage setup can help avoid home kill scenarios.                        |
|  11 | Cumulative eviction does not account for swap usage, which can lead to unexpected evictions.             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=bFrEPfls5PQ)