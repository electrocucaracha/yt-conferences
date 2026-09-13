---
type: Video Note
title: "Extending Kubernetes API: The Hidden Power of Aggregated Server Objects - Amir Malka, ARMO"
description: "The speaker, a software architect at Armo and core maintainer of the open-source security platform Kubescape, discusses the differences between Kubernetes Custom Resource Definitions (CRDs) and aggregated (extension) API servers. He explain..."
resource: https://www.youtube.com/watch?v=ifwNDvRSQWU
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a software architect at Armo and core maintainer of the open-source security platform Kubescape, discusses the differences between Kubernetes Custom Resource Definitions (CRDs) and aggregated (extension) API servers.
He explains that while CRDs are easy to implement and integrate seamlessly with Kubernetes, they have limitations such as etcd storage size constraints, which led Kubescape to develop its own aggregated API server to handle large vulnerability scanning data.
The talk covers the technical journey of building this server, including challenges with storage, memory usage, and the need for optimizations like switching to gRPC, binary encoding, and SQL-based pagination.
The speaker emphasizes the operational risks and maintenance burden of running a custom API server, advising most users to start with CRDs and only consider extension API servers when absolutely necessary.
In the Q&A, he acknowledges the complexity and ongoing challenges of this approach, recommending careful consideration before choosing to extend Kubernetes APIs in this way.
# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is a software architect at Armo, core maintainer of Kubescape, and a KubeCon speaker.                                                                       |
|   2 | Agenda: differences between CRDs and aggregated API servers, how aggregated API servers work, Kubescape use case, production lessons, when to choose each approach. |
|   3 | Kubescape is a security platform covering vulnerability scanning, configuration scanning, and workload behavior monitoring with eBPF.                               |
|   4 | Generates large amounts of data, especially from vulnerability scanning (sbom generation).                                                                          |
|   5 | Initially sent vulnerability scan data to external APIs; open sourcing required keeping data inside the cluster.                                                    |
|   6 | Wanted to keep everything within Kubernetes ecosystem for user familiarity.                                                                                         |
|   7 | Kubernetes API can be extended via CRDs (Custom Resource Definitions) or extension (aggregated) API servers.                                                        |
|   8 | CRDs are easy to implement, lightweight, with built-in validation and RBAC, but have a 1.5MB etcd object size limit.                                                |
|   9 | Aggregated API servers allow full control over storage, discovery, and logic, but have a steep learning curve and high operational cost.                            |
|  10 | Kubescape needed aggregated API server due to large object sizes.                                                                                                   |
|  11 | Started with Kubernetes sample API server project for code generation and wiring.                                                                                   |
|  12 | Implemented custom storage interface and disabled watch API.                                                                                                        |
|  13 | Kubernetes API server routes requests: built-in types → CRDs → aggregated API servers.                                                                              |
|  14 | Aggregated API servers can impact the entire cluster if misused.                                                                                                    |
|  15 | APIService objects define routing and authentication for aggregated APIs.                                                                                           |
|  16 | Authorization checks occur at both Kubernetes API server and external API server.                                                                                   |
|  17 | Each resource type uses a strategy with hooks (prepare for create/update, validate).                                                                                |
|  18 | Kubescape split resource storage into metadata and full object files to optimize memory/CPU.                                                                        |
|  19 | Switched to gRPC and protobuf for communication, improving memory, CPU, and network usage.                                                                          |
|  20 | Changed from JSON to gob encoding, reducing storage by up to 60%.                                                                                                   |
|  21 | Used direct IO to reduce container memory footprint.                                                                                                                |
|  22 | Added pagination                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ifwNDvRSQWU)