---
layout: default
title: Enhancing Container Security with Kata Containers and eBPF at Ant Group
nav_order: 87
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation outlines a solution for enhancing container security by combining Kata Containers with eBPF to address the limitations of traditional node-level security modules."
resource: "https://www.youtube.com/watch?v=MMqf2nyZdXU"
youtube_stats:
  view_count: 79
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

This presentation outlines a solution for enhancing container security by combining Kata Containers with eBPF to address the limitations of traditional node-level security modules.
The speaker explains that conventional approaches, which rely on kernel modules or eBPF loaded into the host kernel, create significant risks, including kernel dependency issues, large attack surfaces, and conflicts when different workloads on the same node require contradictory security policies.
By utilizing Kata Containers, which run containers inside lightweight virtual machines with isolated guest kernels, the proposed architecture allows eBPF programs to be loaded into the guest kernel, ensuring strong security, resource, and fault isolation without impacting the host or other containers.
The system employs a security agent that watches for policy changes via Kubernetes, dynamically loading eBPF programs to enforce rules such as drift prevention, process blocking, and network access control, while using a shared ring buffer between the guest and host to minimize performance overhead.
A live demo demonstrated the effective blocking of unauthorized processes and network ports, and performance data confirmed that the overhead introduced by eBPF enforcement is negligible, with only minor increases in TCP/UDP latency and CPU utilization.
Finally, the speaker noted that this solution has been documented in a white paper adopted by the Kata Containers community and the eBPF Foundation, highlighting its practical application in securing diverse workloads such as AI tasks, batch computing, and online services.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Container security is divided into static scanning for malicious images and runtime auditing for active threats.                                                            |
|   2 | Traditional security methods using kernel modules or eBPF on the host kernel create conflicts when multiple services with different security policies run on the same node. |
|   3 | Host-level security approaches suffer from kernel dependency, large attack surfaces, and difficulty enforcing individual policies for different container workloads.        |
|   4 | Kata Containers uses virtual machines to embed containers, providing security, resource, and fault isolation through separate guest kernels.                                |
|   5 | Loading eBPF programs into the guest kernel prevents host kernel impact and allows for dynamic loading and unloading of security policies.                                  |
|   6 | EBPF offers benefits including verified security, flexibility for online changes, low overhead due to user-space execution, and programmability for complex logic.          |
|   7 | The architecture involves a security agent on each node that watches for policy changes from a server and applies them to specific Kata Containers.                         |
|   8 | EBPF programs are loaded into the guest kernel to enforce policies, with logs shared between guest and host via a ring buffer to minimize CPU overhead.                     |
|   9 | Security policies include drift prevention to block downloaded programs, process blocking for specific binaries, and network restrictions on ports and domains.             |
|  10 | A live demo demonstrated that applying policies successfully blocked wget execution, script downloads, and access to port 80 while allowing whitelisted domains.            |
|  11 | EBPF implementation uses TC programs for IP and port filtering, LSM programs for file access control, and syscall tracing for process monitoring.                           |
|  12 | Drift prevention ensures only pre-scanned programs within the container image can execute, blocking malicious scripts downloaded at runtime.                                |
|  13 | Performance tests showed minimal impact on TCP and UDP connection times when eBPF programs and policies are enforced in the guest kernel.                                   |
|  14 | CPU utilization increased by less than one percent when eBPF security policies were active compared to a baseline without eBPF.                                             |
|  15 | Program execution time remained largely unchanged, indicating that eBPF enforcement adds negligible overhead to container workloads.                                        |
|  16 | A white paper detailing the use of Kata Containers for security has been published in the Kata community and adopted by the eBPF Foundation.                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/MMqf2nyZdXU/hqdefault.jpg)](https://www.youtube.com/watch?v=MMqf2nyZdXU)

[Watch on YouTube](https://www.youtube.com/watch?v=MMqf2nyZdXU)
