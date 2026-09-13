---
type: Video Note
title: "Project Lightning Talk: Optimize Sidecarless Service Mesh With A Brand-New Rust-Base... Zengzeng Yao"
description: "Yaoenzen from Huawei introduces a new approach to optimizing service mesh performance using Kmesh, an eBPF-based traffic management engine, and Orion, a Rust-based proxy. Traditional sidecar service meshes have issues such as tight applicat..."
resource: https://www.youtube.com/watch?v=knX673N1jKM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Yaoenzen from Huawei introduces a new approach to optimizing service mesh performance using Kmesh, an eBPF-based traffic management engine, and Orion, a Rust-based proxy.
Traditional sidecar service meshes have issues such as tight application coupling, high resource overhead, and increased latency.
Kmesh addresses these by offering kernel-native and dual-engine modes, with the latter offloading L4 processing to the kernel and handling L7 tasks in user space for a balance of performance and versatility.
Orion, developed in Rust for memory safety and efficiency, replaces Envoy as the L7 waypoint proxy, implementing only essential APIs and filters to remain lightweight and maintainable.
Benchmarks show Orion achieves 2–4 times higher throughput and significantly lower latency than Envoy, and it integrates natively with Kmesh, aiming to deliver a high-performance, safe, and streamlined service mesh solution without legacy complexity.
# Main Points

|   # | Main point                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Traditional sidecar mesh introduces heavy trade-offs: tight application coupling, high resource overhead, and added latency.                                                                          |
|   2 | Kmesh is an eBPF-based service mesh traffic management engine for high performance and low overhead.                                                                                                  |
|   3 | Kmesh offers two modes: kernel-native for best performance and dual engine mode for versatility.                                                                                                      |
|   4 | Dual engine mode offloads L4 processing to the kernel and keeps L7 in user space for balanced performance.                                                                                            |
|   5 | eBPF handles L4 at native speeds; complex L7 tasks are routed to the waypoint proxy only when necessary.                                                                                              |
|   6 | Currently, Envoy is used as the waypoint proxy but presents three challenges: written in C++ (memory safety risks), heavy and complex due to legacy code, and not designed for deep eBPF integration. |
|   7 | Huawei developed Orion, a high-performance, memory-safe proxy implemented in Rust.                                                                                                                    |
|   8 | Orion uses high-quality open source components and implements only essential APIs and filters.                                                                                                        |
|   9 | Orion is lightweight, simple to maintain, and highly performant due to its focused design.                                                                                                            |
|  10 | Benchmarks show Orion delivers 2x to 4x higher performance and significantly lower latency compared to Envoy.                                                                                         |
|  11 | Orion is designed as a purpose-built, Rust-based replacement for Envoy as the L7 waypoint proxy in Kmesh.                                                                                             |
|  12 | Orion’s advantages over Envoy: better performance, memory safety, lighter footprint, and optimized for Kmesh use cases.                                                                               |
|  13 | Orion is already running in real Kmesh clusters and integrates natively with the Kmesh eBPF layer.                                                                                                    |
|  14 | Next steps include performance tuning and production hardening.                                                                                                                                       |
|  15 | The combination of Kmesh (L4 via eBPF) and Orion (L7) achieves high performance at all layers without C++ safety risks.                                                                               |
|  16 | Invitation to join the Kmesh community.                                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=knX673N1jKM)