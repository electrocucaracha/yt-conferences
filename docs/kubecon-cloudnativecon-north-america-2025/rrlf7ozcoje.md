---
type: Video Note
title: "Diagnosing Application Performance With EBPF, Pyroscope, and Kubernetes - Liam Mackie"
description: "Liam, a lead cloud engineer from Octopus Deploy, shares his experience building the Kubernetes monitor, a component that runs in customer clusters to report resource status back to Octopus Deploy. Facing challenges in setting performance ta..."
resource: https://www.youtube.com/watch?v=RrlF7OzCojE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Liam, a lead cloud engineer from Octopus Deploy, shares his experience building the Kubernetes monitor, a component that runs in customer clusters to report resource status back to Octopus Deploy.
Facing challenges in setting performance targets due to limited cluster visibility and diverse customer environments, his team avoided arbitrary resource limits by gathering real-world data and simulating workloads using tools like Quark and Chaos Mesh.
They instrumented their software with Pyroscope, eBPF (via Pixie), and OpenTelemetry to gain deep insights into performance issues, enabling them to identify and fix problems such as memory leaks and mutex contention.
Automated testing and observability became central to their workflow, ensuring reliability across varied use cases and preventing regressions.
Liam concludes by recommending a structured, automated approach to performance engineering—understanding real usage, instrumenting from day one, testing under realistic loads, profiling bottlenecks, setting and validating thresholds, and automating the process—to build robust, maintainable software.
# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Liam is a lead cloud engineer at Octopus Deploy, based in Brisbane, Australia.                                                                             |
|   2 | Has 9 years of Kubernetes experience, currently writes software in Go and C.                                                                               |
|   3 | Built the Kubernetes monitor for Octopus Deploy, which runs in customer clusters and reports resource status via gRPC.                                     |
|   4 | Customers install the monitor using Helm; this complicates performance engineering and debugging due to lack of visibility.                                |
|   5 | Initially struggled with setting resource limits and performance targets due to varied customer environments.                                              |
|   6 | Engaged with Kubernetes engineers globally to understand diverse workloads and cluster types.                                                              |
|   7 | Identified different cluster patterns: large clusters, tiny edge clusters (e.g., Raspberry Pi), CI/CD workloads, game servers, and multi-tenant platforms. |
|   8 | Chose to observe real customer environments before setting performance targets.                                                                            |
|   9 | Selected CPU, memory, and latency as key metrics.                                                                                                          |
|  10 | Created a load test cluster to test scale, load, and duration.                                                                                             |
|  11 | Used Quark (a SIG scheduling project) to simulate Kubernetes workloads for testing.                                                                        |
|  12 | Developed load and stress test suites to validate software under various scenarios.                                                                        |
|  13 | Used Chaos Mesh to simulate failures (network, pod, stress chaos) and validate resilience.                                                                 |
|  14 | Discovered and fixed performance issues through testing and observability.                                                                                 |
|  15 | Instrumented the application with Pyroscope (continuous profiling), eBPF (Pixie), and OpenTelemetry (traces).                                              |
|  16 | Enabled Pyroscope in debug builds and CI for easier performance diagnosis.                                                                                 |
|  17 | Used Pixie for kernel-level observability and live debugging, especially when Pyroscope introduced observer effects.                                       |
|  18 | Used OpenTelemetry traces with Jaeger and Honeycomb for end-to-end latency and performance analysis.                                                       |
|  19 | Identified and fixed a major mutex contention issue causing latency and memory spikes.                                                                     |
|  20 | Automated performance regression testing using Quark, metrics, traces, and profiling data.                                                                 |
|  21 | Developed a five-step framework for other teams: understand characteristics, instrument from                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RrlF7OzCojE)