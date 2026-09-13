---
type: Video Note
title: "In-Place Pod Resize in Kubernetes: Dynamic Resource Management Without... Tim Allclair & Mofi Rahman"
description: 'The talk discusses "In-Place Pod Resize" and its benefits for Kubernetes users. In-place pod resize allows for dynamic scaling of pods without restarting them, making it ideal for applications that require continuous availability. The featu...'
resource: https://www.youtube.com/watch?v=HuC4k7fmTBk
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The talk discusses "In-Place Pod Resize" and its benefits for Kubernetes users.
In-place pod resize allows for dynamic scaling of pods without restarting them, making it ideal for applications that require continuous availability.
The feature is currently in beta and has several limitations, including atomicity, limited resource types, and support only for main containers and sidecars.
The talk also touches on the upcoming features of VPA (Vertical Pod Autoscaler), including CPU startup boost, pod-level resources, and dynamic resolocation.
# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | In-place pod resize is a feature that allows scaling pods without deleting and recreating them.                                          |
|   2 | VPA (Vertical Pod Autoscaler) is a tool that can be used for in-place resizing, but it's not enabled by default.                         |
|   3 | The resize policy determines when to restart the pod: CPU does not restart, memory does.                                                 |
|   4 | In-place resizing is atomic, meaning all or nothing.                                                                                     |
|   5 | Currently, only CPU and memory are resizable.                                                                                            |
|   6 | VPA has limitations, including:                                                                                                          |
|   7 | Only main containers and sidecars are supported.                                                                                         |
|   8 | Pod level resources are not supported.                                                                                                   |
|   9 | Memory limit best effort protections are in place.                                                                                       |
|  10 | Ray Autoscaler v2 has native integration with Kubernetes for faster task and actor startup.                                              |
|  11 | In-place resizing is available on a pod basis, but it's still dependent on the controller that works with the deployment or replica set. |
|  12 | There is no plan to extend this feature to PVCs at this time.                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HuC4k7fmTBk)