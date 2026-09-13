---
type: Video Note
title: "Containerd: Project Update and Deep Dive - M. Pavlenko, A. Suda, L. Brehm, S. Karp, J. Zhou"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=5ZWbS01wCMk
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: The Containerd team discussed their latest release, version 2.0, which includes several new features and improvements, such as a stable transfer service, sendbox API, and array feature.
They also announced plans for future releases, including version 2.1, which will include support for FS enhanced reloading file system and image volumes.
Additionally, the team discussed their efforts to improve extensibility, including the introduction of NRI (Node Resource Interface) and snapshoters, which enable users to customize container configuration and storage.
The team also talked about their involvement in other projects, such as Kubernetes and Hyperlite, and how they are working together to advance the state-of-the-art in cloud-native computing.
# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Containerd 2.0:                                                                                                                                                                |
|   2 | Stabilized experimental API                                                                                                                                                    |
|   3 | Addressed technical debt and deprecated features                                                                                                                               |
|   4 | Introduced transfer service, sendbox API, and array                                                                                                                            |
|   5 | Improved image verification plugins                                                                                                                                            |
|   6 | Containerd 2.1:                                                                                                                                                                |
|   7 | Released next month with support for FS enhanced reloading file system                                                                                                         |
|   8 | Supports image volumes and thrush FS/Cg groupoup                                                                                                                               |
|   9 | Enhances user namespace and security features                                                                                                                                  |
|  10 | Shim layer:                                                                                                                                                                    |
|  11 | Runi is the most efficient and cost-effective way to run web assembly workloads in Kubernetes                                                                                  |
|  12 | Web assembly is gaining popularity, with RASM (Run Assembly for Microservices) being a key technology                                                                          |
|  13 | Extensibility:                                                                                                                                                                 |
|  14 | Containerd has an extension point for shims, allowing for customization of runtime environments                                                                                |
|  15 | NRI (Node Resource Interface) enables mutation of container configuration                                                                                                      |
|  16 | Formal verification is being used to ensure shim correctness and performance                                                                                                   |
|  17 | Performance:                                                                                                                                                                   |
|  18 | Runi outperforms other solutions in benchmarking tests                                                                                                                         |
|  19 | Pre-ompilation technique improves performance                                                                                                                                  |
|  20 | Security:                                                                                                                                                                      |
|  21 | Containerd has improved security features, including user namespace and security plugins                                                                                       |
|  22 | Go modules are being addressed with a "go jail" feature to mitigate supply chain attacks                                                                                       |
|  23 | Kubernetes integration: + Containerd is adopted by well-known enterprise distributions of Kubernetes + Containerd is integrated with Kubernetes manager services and ecosystem |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5ZWbS01wCMk)