---
type: Video Note
title: "CRI-O: Thriving in a Changing World, One Container at a Time - Ayato Tokubi & Sohan Kunkerkar"
description: "The presenters, San Kerkar and Ayatkobi from Red Hat, discuss the past year of Cryo development at CubeCon, focusing on lessons learned, new features, and future plans. They explain Cryo as a Kubernetes-specific container runtime that empha..."
resource: https://www.youtube.com/watch?v=OjIZ-TH-4FA
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters, San Kerkar and Ayatkobi from Red Hat, discuss the past year of Cryo development at CubeCon, focusing on lessons learned, new features, and future plans.
They explain Cryo as a Kubernetes-specific container runtime that emphasizes security, compliance, and gradual, well-tested feature development.
Key topics include the transition to "crun" as the default runtime for improved performance and lower memory usage, which revealed subtle behavioral differences and edge cases compared to the previous "runc" runtime, highlighting the importance of thorough testing and feature parity.
They introduce the Cryo Credential Provider, which enables secure, namespace-specific image pulls in multi-tenant environments, and outline recent upstream initiatives such as in-place pod vertical scaling, custom container stop signals, and enhanced metrics collection.
A major new feature, OCI volume source, allows mounting OCI images and artifacts directly as container volumes, simplifying data access without extra tools.
The session concludes with a look at Cryo’s roadmap, including expanded artifact support, security enhancements, and improved performance testing, and encourages community feedback and contributions.
# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Session covers lessons and stories from one year of Cryo development.                                                                                  |
|   2 | AI workloads and tools are increasingly integrated with Kubernetes.                                                                                    |
|   3 | Cryo’s philosophy: “one container at a time” to ensure reliability and support business growth.                                                        |
|   4 | Presenters: San Kerkar (Red Hat, Cryo maintainer) and Ayatkobi (Red Hat, Cryo reviewer).                                                               |
|   5 | Agenda: Cryo introduction, lessons learned, Cryo credential provider, upstream signal initiatives, OCI volume image feature demo, future roadmap, Q&A. |
|   6 | Cryo: container runtime for Kubernetes, compliant with CRI, focuses on security, supports OCI image registry, CNCF graduated project.                  |
|   7 | Decision at last KubeCon: made “crun” the default runtime over “runc” for better performance, lower memory, and advanced workload support.             |
|   8 | Lessons learned:                                                                                                                                       |
|   9 | Differences in runtime behavior (e.g., resource accounting, CPU shares/weight calculation).                                                            |
|  10 | Feature parity and behavior consistency are critical.                                                                                                  |
|  11 | Need for deeper, more comprehensive testing, especially for edge cases and lifecycle/teardown.                                                         |
|  12 | Example issue: Masking thermal paths for security led to kernel incompatibility at scale; resolved by using bind mounts.                               |
|  13 | Performance and scale testing are resource-intensive; plan to run such tests on release branches.                                                      |
|  14 | Recent project: Cryo credential provider plugin (based on Kubernetes 1.26 kubelet credential provider).                                                |
|  15 | Enables secure, dynamic image pulls per namespace.                                                                                                     |
|  16 | Credentials are temporary and namespace-scoped.                                                                                                        |
|  17 | Future: service account support, observability, debugging, registry expansion.                                                                         |
|  18 | Upstream signal initiatives:                                                                                                                           |
|  19 | In-place pod vertical scaling (update CPU/memory without restart).                                                                                     |
|  20 | Container stop signals (custom stop signals).                                                                                                          |
|  21 | Pod/container stats collection moved to container runtime for consistency and efficiency.                                                              |
|  22 | Notable feature: OCI volume source (mount OCI images/artifacts as volumes natively in 1.35).                                                           |
|  23 | No need for persistent volumes or extra containers.                                                                                                    |
|  24 | Supports version control, caching, and garbage                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OjIZ-TH-4FA)