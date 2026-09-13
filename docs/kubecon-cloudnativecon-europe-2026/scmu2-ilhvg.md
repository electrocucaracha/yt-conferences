---
type: Video Note
title: "Cloud Native Theater | EnvoyCon: The Next Generation of Envoy Extensibility: Dynami... Rohit Agrawal"
description: "Rohit Agarval, a software engineer at Databricks and Envoy maintainer, discusses the evolution of Envoy's extensibility, highlighting the transition from Lua scripting to WASM filters, Golang HTTP filters, and most recently, dynamic modules..."
resource: https://www.youtube.com/watch?v=ScMu2-ILhvg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Rohit Agarval, a software engineer at Databricks and Envoy maintainer, discusses the evolution of Envoy's extensibility, highlighting the transition from Lua scripting to WASM filters, Golang HTTP filters, and most recently, dynamic modules.
Dynamic modules, introduced in June 2024, allow developers to write in-process extensions in Rust or Golang using a stable C API, eliminating the serialization overhead and latency associated with previous approaches but requiring trust in the modules due to the lack of sandboxing.
Rohit shares internal Databricks use cases where dynamic modules significantly reduced latency and configuration size, such as real-time audit logging and dynamic RBAC policy updates, and removed the need for sidecars in Kubernetes deployments.
He notes that dynamic modules have led to up to 50x config size reduction and 5x faster startup times, and expresses the team's goal to expand dynamic module support across all Envoy extension points.
In the Q&A, Rohit addresses language preferences, future contribution models, and the possibility of officially maintained dynamic modules, emphasizing the flexibility and ongoing development of this extensibility approach.
# Main Points

|   # | Main point                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Talk focused on Envoy extensibility, particularly dynamic modules.                                                                                                                                         |
|   2 | No live demo due to reduced talk time.                                                                                                                                                                     |
|   3 | Presenter: Rohit Agarval, software engineer at Databricks, Envoy maintainer.                                                                                                                               |
|   4 | Early Envoy extensibility (2017): Lua scripting for lightweight tasks.                                                                                                                                     |
|   5 | 2019: WASM introduced, enabling multi-language, sandboxed runtime for filters and loggers, but added serialization overhead and latency.                                                                   |
|   6 | Jan 2023: Golang HTTP filters introduced; requests for more Golang filter types followed.                                                                                                                  |
|   7 | June 2024: Work began on dynamic modules, starting with HTTP dynamic module filter.                                                                                                                        |
|   8 | Dynamic modules architecture: C++ core, stable C API, official Rust and Golang SDKs.                                                                                                                       |
|   9 | Modules run in-process with Envoy, enabling zero-copy data access and low latency.                                                                                                                         |
|  10 | Trade-off: No sandboxing; modules have same privileges as Envoy, requiring trust.                                                                                                                          |
|  11 | Envoy 1.37: Dynamic modules support for UDP/TCP listener filters, network filters, HTTP filters, upstream bridges, input matchers, access loggers, bootstrap, load balancing policies, cluster extensions. |
|  12 | Use case 1: Audit logging latency reduced by replacing disk-based JSON logging and external Golang process with in-process Rust access logger sending directly to Kafka.                                   |
|  13 | Use case 2: Dynamic RBAC policies updated in real time via Rust module, eliminating large config updates and reducing latency from minutes to real time.                                                   |
|  14 | Use case 3: Sidecar functionality (e.g., load balancing, access logging) moved into modules, removing need for sidecar containers and reducing latency.                                                    |
|  15 | Results: Up to 50x config size reduction, 5x startup time reduction, improved CPU/memory usage (pending further testing).                                                                                  |
|  16 | Future plans: Expand dynamic modules to tracing and all extension points; encourage community contributions and feedback.                                                                                  |
|  17 | Discussion: Rust preferred internally for memory safety; Go also supported.                                                                                                                                |
|  18 | Potential for official, quality-stamped dynamic modules repository reviewed by maintainers.                                                                                                                |
|  19 | Possible shift from C++ extensions to dynamic modules for                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ScMu2-ILhvg)