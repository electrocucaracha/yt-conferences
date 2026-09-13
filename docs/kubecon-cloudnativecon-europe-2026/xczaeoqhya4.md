---
type: Video Note
title: "Project Lightning Talk: Urunc: The New Kid In The Block Of Sandboxed Container... Charalampos Mainas"
description: "Haralamus, also known as Bobby, introduces Uran C, a CNCF sandbox project designed to address the trade-off between container performance and strong isolation required for scenarios like multi-tenancy and AI sandboxing. Uran C is a CRI-comp..."
resource: https://www.youtube.com/watch?v=XCzaeoqHya4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Haralamus, also known as Bobby, introduces Uran C, a CNCF sandbox project designed to address the trade-off between container performance and strong isolation required for scenarios like multi-tenancy and AI sandboxing.
Uran C is a CRI-compatible runtime that integrates seamlessly with the container ecosystem and focuses on single-application workloads using unikernels or single-application kernels, packaging applications alongside their own kernel within a secure sandbox.
In Kubernetes deployments, Uran C treats sidecar containers as trusted and user containers as untrusted, isolating the latter in either software-based or VM-based sandboxes without needing an agent inside the sandbox.
Performance evaluations show Uran C achieves significantly lower overhead and higher pod density compared to other sandbox runtimes, making it suitable for fast, isolated workloads in microservices, serverless, AI sandboxing, resource-constrained environments, and CI/CD pipelines, with support for BSD workloads as well.
Bobby invites interested users to connect at KubeCon, join community meetings, and find more information on the project's website and GitHub.
# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter is Haralamus (Bobby), creator and maintainer of Uran C.                                                                               |
|   2 | Uran C is a CNCF sandbox project and a CRI-compatible runtime.                                                                                  |
|   3 | Aims to provide stronger isolation for containers, especially in scenarios like multi-tenancy and AI sandboxing.                                |
|   4 | Offers seamless integration with the container ecosystem.                                                                                       |
|   5 | Focuses on single application workloads using unikernels or single application kernels.                                                         |
|   6 | Packages applications alongside a kernel, deploying them in a sandbox within a container.                                                       |
|   7 | Sandbox can be software-based (like Gvisor) or a virtual machine.                                                                               |
|   8 | In Kubernetes, Uran C treats sidecar containers as normal and user containers as untrusted, isolating them in secure sandboxes.                 |
|   9 | No agent is required inside the sandbox.                                                                                                        |
|  10 | Evaluations show Uran C has about 20-28% overhead in cold boot scenarios, compared to 2x overhead in other sandbox runtimes.                    |
|  11 | Density test on Raspberry Pi (8GB RAM): Uran C reached 467 pods, GIS limited to 170, Kata to 302, Uran C up to 430 depending on configuration.  |
|  12 | Suitable for use cases needing fast spawning and isolation: microservices, serverless, AI sandboxing, resource-constrained environments, CI/CD. |
|  13 | Supports BSD workloads.                                                                                                                         |
|  14 | Uran C team available at KubeCon, project pavilion Wednesday 10-1:30, kiosk 24b.                                                                |
|  15 | Community meetings every last Wednesday of the month (postponed during KubeCon).                                                                |
|  16 | More information available on the website, GitHub repository, CNCF Slack workspace, and channel.                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XCzaeoqHya4)