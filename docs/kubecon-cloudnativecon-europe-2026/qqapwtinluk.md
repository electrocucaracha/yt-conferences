---
type: Video Note
title: "Serverless GPUs in Production: How Cerebrium Built a Globally... Dave Protasowski & Elijah Roussos"
description: "The talk discusses how Cerebrum leverages Knative to deliver serverless GPU capabilities for AI workloads, highlighting the unique challenges of deploying GPU-based applications compared to traditional CPU workloads. Eli from Cerebrum expla..."
resource: https://www.youtube.com/watch?v=QqApwTinlUk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The talk discusses how Cerebrum leverages Knative to deliver serverless GPU capabilities for AI workloads, highlighting the unique challenges of deploying GPU-based applications compared to traditional CPU workloads.
Eli from Cerebrum explains that AI workloads require exclusive access to expensive and non-sharable GPU resources, have large container images leading to slow startup times, and demand precise routing to avoid costly failures.
Cerebrum addresses these issues by customizing Knative’s serving component, implementing direct state propagation and a single state manager to improve readiness and routing accuracy, and introducing features like scaling buffers and user-configurable load balancing.
The team also discusses ongoing improvements in Knative, such as enhanced autoscaling, support for larger clusters, and efforts to reduce container image pull times using lazy loading and image streaming technologies.
The session concludes with updates on Knative’s roadmap and encourages community engagement for further development and feedback.
# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Talk focuses on serverless GPUs in production using Knative on Cerebrum's platform.                                                                                              |
|   2 | Speakers: Eli (founding engineer at Cerebrum) and Dave (Knative maintainer, serving lead, steering committee).                                                                   |
|   3 | Knative simplifies Kubernetes for app developers via functions, serving, and eventing.                                                                                           |
|   4 | Functions: helps bootstrap and build containers, supports HTTP and cloud events.                                                                                                 |
|   5 | Serving: provides high-level abstraction for deploying apps, autoscaling, traffic rollouts, and revision management.                                                             |
|   6 | Eventing: broker abstraction for event sources and triggers, simplifies event-driven app development.                                                                            |
|   7 | AI workloads on GPUs are challenging due to non-sharability, high cost, slow startup, and strict routing requirements.                                                           |
|   8 | GPU workloads require full resource access, are expensive to run idle, and have large container images causing slow cold starts.                                                 |
|   9 | Accurate routing is critical; misrouting leads to failures, not just throttling.                                                                                                 |
|  10 | App development and model development are disjointed; models are large and require separate optimization.                                                                        |
|  11 | Cerebrum provides serverless infrastructure for GPU-based AI workloads, focusing on cost, performance, and data management.                                                      |
|  12 | Kubernetes is used as the orchestration base; Knative adds autoscaling, scale-to-zero, rollouts, and traffic orchestration.                                                      |
|  13 | Knative's default assumptions (CPU workloads, multi-connection tolerance) don't fit GPU workloads well.                                                                          |
|  14 | Issues faced: binary readiness is hard, informer delays in Kubernetes/EKS, readiness drift, costly misrouting, slow service discovery.                                           |
|  15 | Solutions: custom discovery, direct state propagation via qroxy, single state manager for activators, quarantine states for failed pods, global view for activators using Valky. |
|  16 | Achieved fast routing latency (~25ms P90), fewer 502 errors, and improved horizontal scaling.                                                                                    |
|  17 | Additional improvements: in-place cooldown evaluation, scaling buffer, user-configurable load balancing, dashboard.                                                              |
|  18 | Future considerations: GPU-aware routing, KV caching, continuous batching                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QqApwTinlUk)