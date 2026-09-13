---
type: Video Note
title: "Maximizing the Launch Reliability: Ensuring Stable Application Lift-off and Orbi... Hiroshi Hayakawa"
description: "Hiroshi, a product owner at LY Corporation’s private cloud division, presents on improving application launch reliability on Kubernetes, drawing from extensive experience managing large-scale platforms. He outlines the importance of launch..."
resource: https://www.youtube.com/watch?v=vTmImF_mibY
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Hiroshi, a product owner at LY Corporation’s private cloud division, presents on improving application launch reliability on Kubernetes, drawing from extensive experience managing large-scale platforms.
He outlines the importance of launch reliability for production applications and details practical techniques, including tuning both container and application parameters—such as adjusting CPU and memory allocations and optimizing language runtime settings—to mitigate performance issues during startup.
Hiroshi emphasizes ensuring applications are fully initialized before accepting traffic, recommending the use of Kubernetes probes and initialization strategies like pre-filling connection pools and warming up applications.
He also discusses the new Kubernetes feature, "impress port resize," which allows dynamic resource adjustment without restarting containers, noting its potential benefits and current limitations, especially with Java applications.
The session concludes with a summary of best practices and an invitation for community feedback on further automating resource scaling after startup.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Hiroshi is a product owner at LY Corporation, managing an internal developer platform on Kubernetes.                                                 |
|   2 | LY Corporation operates a large-scale Kubernetes-based platform for various internet services.                                                       |
|   3 | The presentation focuses on improving application launch reliability and stability on Kubernetes.                                                    |
|   4 | Three main sections: defining launch reliability, practical techniques for improvement, and exploring the Kubernetes "impress resize" feature.       |
|   5 | Application startup on Kubernetes involves pod scheduling, resource setup, container start, application initialization, and reaching a stable state. |
|   6 | Common startup issues include repeated crashes and restarts, often triggered by minor code changes or high traffic.                                  |
|   7 | Startup failures are unpredictable and can occur due to performance degradation or changing external conditions.                                     |
|   8 | Applications perform below maximum capacity immediately after startup due to initialization load, garbage collection, and cache loading.             |
|   9 | To prevent startup failures, minimize the impact of these factors through tuning.                                                                    |
|  10 | Tuning is needed at both container and application levels:                                                                                           |
|  11 | Container level: Set higher CPU and memory limits/requests in Kubernetes manifests for startup stability.                                            |
|  12 | Setting requests equal to limits guarantees resource availability but may reduce overall node utilization.                                           |
|  13 | Quality of service and eviction priority are affected by resource settings.                                                                          |
|  14 | Application level: Be aware of cgroups effects on language runtimes (e.g., Java, Go).                                                                |
|  15 | For Java, increase heap memory allocation and carefully select garbage collection algorithms.                                                        |
|  16 | Ensure applications are fully initialized before serving traffic:                                                                                    |
|  17 | Use startup and readiness probes to delay traffic until initialization completes.                                                                    |
|  18 | Pre-fill database and thread pools during initialization.                                                                                            |
|  19 | Optionally, use warm-up traffic to trigger runtime optimizations (e.g., JIT compilation).                                                            |
|  20 | The "impress port resize" feature allows changing resource allocations without restartin                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vTmImF_mibY)