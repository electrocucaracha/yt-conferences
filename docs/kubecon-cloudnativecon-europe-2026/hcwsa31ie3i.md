---
type: Video Note
title: "Continuous AI Conformance: The kOp... Arnaud Meukam, Janet Kuo, Justin Santa Barbara, Ciprian Hacman"
description: "The video features a panel of Kubernetes experts discussing the need for an AI conformance program, particularly in the context of the open-source KOPS project. They explain that traditional Kubernetes conformance, designed for stateless an..."
resource: https://www.youtube.com/watch?v=hcwsA31ie3I
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a panel of Kubernetes experts discussing the need for an AI conformance program, particularly in the context of the open-source KOPS project.
They explain that traditional Kubernetes conformance, designed for stateless and CPU-bound workloads, is insufficient for the unique requirements of AI workloads, which demand specialized scheduling, networking, and hardware acceleration.
To address fragmentation and ensure reliability, the Kubernetes AI conformance program was established, setting standards for platforms to support AI workloads effectively.
The KOPS team has integrated automated AI conformance testing into their workflow, creating fast-path tests for common configurations like the Nvidia GPU operator, while allowing flexibility for alternative solutions.
Their approach emphasizes transparency, automation, and the development of a centralized, reusable test suite to benefit the broader Kubernetes ecosystem, encouraging other distributions and vendors to adopt and contribute to AI conformance standards.
# Main Points

|   # | Main point                                                                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speakers introduced: Justin Santa Barbara (Google, KOPS maintainer), Arno Mam (CRA technical lead, open source engineer), Cyprien (Microsoft, Kubernetes contributor), Janet (Google, Kubernetes contributor).                     |
|   2 | Topic: AI conformance in Kubernetes, focusing on KOPS and broader ecosystem lessons.                                                                                                                                               |
|   3 | Kubernetes was originally designed for stateless, CPU-bound web services.                                                                                                                                                          |
|   4 | AI workloads introduce new requirements: CPU-intensive workloads, scheduling, topology, networking, and fragmentation due to vendor-specific solutions.                                                                            |
|   5 | Kubernetes conformance is insufficient for AI workloads; need for a faster, AI-specific conformance program.                                                                                                                       |
|   6 | Kubernetes AI Conformance Program announced to set standards for platform capabilities to reliably run AI workloads.                                                                                                               |
|   7 | Pillars of AI conformance: DRA and accelerator support, observability (accelerator metrics), scheduling/orchestration (GAN scheduling, autoscaling), networking (inference gateway), security, and complex AI operator deployment. |
|   8 | Most certified platforms are commercial; goal to have open-source, community-driven distributions (like KOPS) meet the standard.                                                                                                   |
|   9 | KOPS: open-source tool for creating, managing, and upgrading Kubernetes clusters; supports multiple cloud providers.                                                                                                               |
|  10 | KOPS used for Kubernetes conformance and scalability tests (up to 5,000 nodes).                                                                                                                                                    |
|  11 | Aim for KOPS to be among the first open-source distributions to achieve AI conformance.                                                                                                                                            |
|  12 | Automated testing is heavily used due to limited resources; avoids manual toil and increases efficiency.                                                                                                                           |
|  13 | Kubernetes conformance is test-based; AI conformance is capability/outcome-based, making automated testing harder.                                                                                                                 |
|  14 | KOPS implements "fast path" automated tests for common AI conformance approaches (e.g., Nvidia GPU operator).                                                                                                                      |
|  15 | Passing automated tests provides easy AI conformance; alternative approaches require manual review ("slow path").                                                                                                                  |
|  16 | Automation includes test result submission and approval pipelines.                                                                                                                                                                 |
|  17 | Goal: upstream and standardize AI conformance tests for use by other t                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hcwsA31ie3I)