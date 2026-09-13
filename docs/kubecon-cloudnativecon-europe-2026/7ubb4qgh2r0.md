---
type: Video Note
title: "Amplifying End User Voices: Platform Architects on the... Rajas K, Zach S, Kevin K, Elias T & Dawn C"
description: "The panel discussion brought together platform architects and engineers from companies like Broadcom, Google, Nvidia, and Amazon to share user feedback and challenges in the Kubernetes and cloud native ecosystem. Key issues raised included..."
resource: https://www.youtube.com/watch?v=7uBB4qgh2R0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The panel discussion brought together platform architects and engineers from companies like Broadcom, Google, Nvidia, and Amazon to share user feedback and challenges in the Kubernetes and cloud native ecosystem.
Key issues raised included the need for better node abstraction, especially as AI workloads require scheduling and managing resources across multiple nodes and GPUs, and the growing demand for features like gang scheduling and integrated support for complex workloads.
Panelists emphasized the importance of extensibility in Kubernetes, drawing clear boundaries between what belongs in core Kubernetes and what should remain in the broader ecosystem, with mechanisms in core and policies in the ecosystem.
They discussed the challenges of configuration complexity, incident response, and the gap between the ideal and current states of enterprise platform teams, highlighting the need for upstream-first contributions and reusable community tools.
Looking ahead, the panelists predicted increased focus on confidential computing, agentic primitives, and simplifying platform management, while also identifying technical debt areas such as the Kubelet and API machinery as priorities for future improvement.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Panel gathers platform architects working with Kubernetes to discuss user feedback and ecosystem evolution.                                                    |
|   2 | Panelists: Rajas (Broadcom), Don (Google), Kevin Clus (Nvidia), Zach Shepard (Broadcom), Ellis Tarn (Amazon EKS).                                              |
|   3 | Key user requests:                                                                                                                                             |
|   4 | Node abstraction and automation, especially for AI workloads (Don).                                                                                            |
|   5 | Gang scheduling of pods and integrated support for multi-node/rack-scale workloads (Kevin).                                                                    |
|   6 | Simplicity and ease of use for end users (Zach).                                                                                                               |
|   7 | Improved support for AI workloads spanning multiple nodes and GPUs, breaking existing Kubernetes primitives (Ellis).                                           |
|   8 | DRA and Carpenter projects emerged from user needs; DRA evolved from vendor-specific black boxes to more transparent, integrated solutions.                    |
|   9 | Inference workloads require scheduling across many GPUs and hosts, demanding low-latency networking and coordinated scheduling.                                |
|  10 | Kubernetes core should focus on mechanisms; policies and differentiators belong in the ecosystem (Don).                                                        |
|  11 | Cluster API cited as a good example of extensibility and separation between core and ecosystem.                                                                |
|  12 | Incident response: upstream-first mindset, but downstream patches when urgent; reusable tools like etcd diagnosis/recovery developed for community benefit.    |
|  13 | Platform teams face challenges with configuration drift, security, version sprawl, and operational complexity.                                                 |
|  14 | Reference architectures, benchmarks, and conformance tests are needed to help standardize solutions for different workloads.                                   |
|  15 | Ecosystem is maturing projects outside core (e.g., Crow, Terraform, Helm) before potential inclusion in Kubernetes core.                                       |
|  16 | Upcoming focus areas: confidential computing, agentic primitives, improved scheduling for disaggregated inference workloads, and keeping pace with innovation. |
|  17 | Technical debt: Kublet and API machinery identified as areas needing redesign for maintainability and extensibility.                                           |
|  18 | Projects mentioned: Cluster API, Workloads Foundation, DRA, Crow, Carpenter, etcd diagnosis/recovery.                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7uBB4qgh2R0)