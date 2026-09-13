---
type: Video Note
title: "Lightning Talk: Graceful Controller Operations - Jeffrey Ying, Google"
description: "Jeffrey, a software engineer at Google, discusses graceful controller operations within Kubernetes, focusing on the control plane's components. He explains that while the kube-apiserver acts as a hub, the kube-controller-manager and kube-sc..."
resource: https://www.youtube.com/watch?v=qbuAn7pS9bQ
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jeffrey, a software engineer at Google, discusses graceful controller operations within Kubernetes, focusing on the control plane's components.
He explains that while the kube-apiserver acts as a hub, the kube-controller-manager and kube-scheduler serve as the cluster's "brains," and running multiple instances can lead to split-brain scenarios with conflicting states.
To address this, Kubernetes uses leader election with a lease resource, ensuring only one active leader while others remain passive.
Previously, when a leader lost its lease, the process would forcefully exit, causing issues like skipped cleanup and go routine leaks, and requiring a full lease expiration cycle for a new leader to take over.
With the update in version 1.35, the kube-controller-manager now supports graceful leader transitions, allowing safe cleanup and lock release, enabling smoother transitions and serving as a model for other controllers to adopt more robust patterns.
# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jeffrey, a software engineer at Google, discusses graceful controller operations.                                           |
|   2 | The kube-apiserver acts as a hub in the control plane, without opinions on cluster state.                                   |
|   3 | kube-controller-manager and kube-scheduler hold the opinions and are considered the "brain" of the cluster.                 |
|   4 | Multiple control planes are used for reliability.                                                                           |
|   5 | Running multiple controller managers can cause split brain scenarios, leading to disagreements about desired state.         |
|   6 | Leader election is used to solve split brain issues.                                                                        |
|   7 | Multiple instances of kube-scheduler and kube-controller-manager run, but only one is active as leader; others are passive. |
|   8 | Leader election is implemented using a Kubernetes resource called Lease, which acts as a lock.                              |
|   9 | Other instances watch the Lease resource to detect if the leader becomes unhealthy.                                         |
|  10 | In practice, client-go library handles leader election; users specify onStartLeading and onStopLeading callbacks.           |
|  11 | onStartLeading runs the control loop when a controller acquires the lease.                                                  |
|  12 | onStopLeading is called when a leader loses the lease; KCM calls klog flush and exits the process.                          |
|  13 | Another component is expected to restart the process after exit, returning it to passive mode.                              |
|  14 | Forceful exit skips cleanup operations and can cause goroutine leaks.                                                       |
|  15 | Exiting cleans up goroutine leaks but makes it unsafe to release the lock, creating a chicken-and-egg problem.              |
|  16 | When a leader exits, followers must wait for the lease to expire, which can take minutes in large clusters.                 |
|  17 | In version 1.35, KCM was made graceful: cleanup operations are performed and goroutine leaks are fixed.                     |
|  18 | It is now safe to release the lock without direct shutdown.                                                                 |
|  19 | This enables features like voluntary lock release via CLI and allows some components to avoid restarts.                     |
|  20 | Graceful leader transitions are implemented in KCM and serve as a reference for other controllers.                          |
|  21 | Developers are encouraged to adopt this pattern for building better, more graceful controllers.                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qbuAn7pS9bQ)