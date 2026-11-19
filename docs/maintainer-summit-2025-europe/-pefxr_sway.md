---
layout: default
title: "Redesigning Kubelet Probes - Surya Seetharaman & Dan Winship, Red Hat"
nav_order: 7
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: Surya and Dan from Red Hat’s OpenShift networking team presented an informal talk on redesigning Kubernetes Kubelet probes to address significant limitations in current implementations.
resource: "https://www.youtube.com/watch?v=-pefxR_SwaY"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

Surya and Dan from Red Hat’s OpenShift networking team presented an informal talk on redesigning Kubernetes Kubelet probes to address significant limitations in current implementations.
They identified key problems, including security vulnerabilities where the probe host field allows server-side request forgery, incompatibility with network policies that require host-level exceptions, and failures in dual-stack or multi-network environments where probes cannot target specific IP families or overlapping pod IPs.
To resolve these issues, the speakers proposed several potential solutions, such as leveraging CRI port forwarding, converting network probes to exec probes, introducing a new CRI probing API, or deploying dedicated probing pods or sidecars to handle health checks within the pod’s network namespace.
The discussion emphasized the critical need to maintain backward compatibility and clarify probe semantics, as changing how probes operate could break existing workloads that rely on specific network reachability behaviors.
Audience feedback highlighted concerns about performance overhead, the importance of trusting container runtimes for implementation details, and the complexity of resource accounting for additional probing components, leading to a consensus that a robust solution must balance security, efficiency, and API stability.

# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk addresses problems with Kubelet probes regarding network policies, dual-stack clusters, multi-networks, overlapping pod IPs, and security loopholes.              |
|   2 | Current design assumes Kubelet can always reach pods, requiring network policies to allow host traffic, which conflicts with admin network policy APIs.                    |
|   3 | Dual-stack and multi-network scenarios lack intuitive ways to specify which IP family or interface probes should target.                                                   |
|   4 | Overlapping pod IPs in multi-network setups break Kubelet's assumption of unique pod IPs, requiring workarounds like keeping the default network open for probes.          |
|   5 | The probe host field allows arbitrary endpoints, creating a server-side request forgery risk and non-intuitive behavior when set to localhost.                             |
|   6 | An interim stopgap solution involves Pod Security Admission to restrict or audit the use of the host field in probes.                                                      |
|   7 | Potential solutions include using CRI port forwarding to tunnel probes through gRPC, avoiding pod network traversal.                                                       |
|   8 | Another approach is converting HTTP and TCP probes into exec probes using cURL inside the pod, though this is slow and requires binaries in the image.                     |
|   9 | A lightweight CRI API using nsenter could probe within the namespace without full exec overhead, but is limited to Linux runtimes.                                         |
|  10 | Adding a dedicated probing API to CRI would allow the runtime to handle probes, but risks delaying adoption due to version dependencies.                                   |
|  11 | Launching a dedicated probing pod in the pod network allows specific network policy rules but introduces complexity and security risks if compromised.                     |
|  12 | Attaching an ephemeral sidecar container to each pod for probing avoids CRI changes but creates management and accounting challenges for Kubelet.                          |
|  13 | Changing probe semantics to bypass the pod network may break existing workloads that rely on probes originating from the node IP.                                          |
|  14 | Community feedback emphasizes trusting the container runtime for probe implementation rather than bypassing it with host-level hacks like nsenter.                         |
|  15 | There is a fundamental tension between probes indicating process health versus verifying network reachability, which may require separate mechanisms.                      |
|  16 | Accounting for probe resources is difficult, especially with varying runtime overheads like microVMs, suggesting probes should be decoupled from specific implementations. |
|  17 | The team seeks feedback to refine the design, potentially involving Sig Node contributors, to ensure solutions are compatible with diverse Kubernetes environments.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-pefxR_SwaY/hqdefault.jpg)](https://www.youtube.com/watch?v=-pefxR_SwaY)

[Watch on YouTube](https://www.youtube.com/watch?v=-pefxR_SwaY)
