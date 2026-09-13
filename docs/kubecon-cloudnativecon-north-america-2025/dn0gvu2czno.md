---
type: Video Note
title: "Where’s My Pod? End-to-End Tracing for Kubernetes With OpenTelemetry - Artem Tkachuk & JP Phillips"
description: "In this talk at CubeCon, JP and Artem from Netflix’s compute runtime team discuss their migration from a fully custom container data plane to a standard Kubernetes kubelet-based architecture, focusing on how enhanced observability and traci..."
resource: https://www.youtube.com/watch?v=Dn0gvU2Czno
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk at CubeCon, JP and Artem from Netflix’s compute runtime team discuss their migration from a fully custom container data plane to a standard Kubernetes kubelet-based architecture, focusing on how enhanced observability and tracing were critical to the process.
They explain that as Netflix moved all containers to the new runtime, understanding and debugging issues quickly became essential for maintaining user confidence and ensuring a smooth migration.
By instrumenting components such as containerd, CNI, and NRI, and implementing end-to-end and synthetic tracing, the team was able to identify and resolve complex issues—including performance bottlenecks and a subtle bug related to container image media types—while also empowering customers to self-diagnose problems.
The speakers emphasize the value of detailed instrumentation, proactive trace analysis, and open-source collaboration, encouraging others to adopt similar observability practices to improve reliability and user experience in large-scale container environments.
# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Netflix compute runtime team presented at CubeCon about observability and tracing in container orchestration.                                                                                     |
|   2 | The team migrated all Netflix containers from a custom data plane to a Kubernetes kubelet-based data plane within six months.                                                                     |
|   3 | Observability and tracing were critical to ensure user satisfaction and quickly debug issues during and after migration.                                                                          |
|   4 | Titus is Netflix’s container orchestration platform, running hundreds of thousands of pods globally for diverse workloads.                                                                        |
|   5 | The original data plane was fully custom, complex, and hard to maintain; migration aimed to use standard, upstream components.                                                                    |
|   6 | Adoption of kubelet allowed Netflix to contribute to open source, especially with the containerd community.                                                                                       |
|   7 | Deep instrumentation was implemented across components (containerd, NRI plugin, registry, OCI hooks, CNI) for end-to-end tracing.                                                                 |
|   8 | Tracing covers both synchronous (same execution context) and asynchronous (different execution contexts) operations, using propagation and span links.                                            |
|   9 | Customers can access end-to-end traces, enabling self-service debugging and faster issue resolution.                                                                                              |
|  10 | Case studies showed tracing helped identify and fix issues like “phantom spans” (gaps in trace waterfalls) and expensive NRI locks.                                                               |
|  11 | Instrumentation of CNI and NRI components revealed bottlenecks and led to upstream fixes.                                                                                                         |
|  12 | Synthetic traces were created to bridge execution boundaries and drive SLOs for pod launch latency and errors.                                                                                    |
|  13 | Tracing helped diagnose a bug where image layer media types caused intermittent workload failures, leading to a fix in the image publishing system.                                               |
|  14 | Key takeaways: try various instrumentation approaches, add rich attributes to spans, use sampling to control costs, recognize and investigate phantom spans, and integrate tracing into the SDLC. |
|  15 | Encouraged community engagement, open source contributions, and invited attendees to related talks and networking events.                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Dn0gvU2Czno)