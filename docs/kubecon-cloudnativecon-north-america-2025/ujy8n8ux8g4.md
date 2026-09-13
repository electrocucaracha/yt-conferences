---
type: Video Note
title: "AI Inference Without Boundaries: Dynamic Routing With Multi-Cluster In... Rob Scott & Daneyon Hansen"
description: "In this KubeCon talk, Rob Scott from Google and Damian Hansen from Solo IO discuss the need for multicluster inference gateways in Kubernetes environments, particularly for handling the unique demands of GenAI traffic, which differs signifi..."
resource: https://www.youtube.com/watch?v=UJy8n8uX8G4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this KubeCon talk, Rob Scott from Google and Damian Hansen from Solo IO discuss the need for multicluster inference gateways in Kubernetes environments, particularly for handling the unique demands of GenAI traffic, which differs significantly from traditional web requests due to its larger size and complexity.
They explain that inference gateways, built on the Gateway API inference extension, use an extensible Endpoint Picker (EP) to intelligently route requests to the most suitable model server replica within an inference pool, leveraging real-time metrics for optimal resource utilization.
The speakers detail how multicluster inference gateways extend these concepts across multiple clusters to better manage scarce and expensive GPU resources, using a combination of Gateway API and new inference pool APIs, and describe two routing modes: direct and gateway routing.
They emphasize the flexibility and extensibility of the architecture, allowing for custom EP implementations and metrics-based routing decisions, and address questions about latency, failover, and the differences between EPs and traditional load balancers.
The session concludes with an invitation for community feedback and participation, noting ongoing work to generalize multicluster backend support and the importance of collaboration in evolving these solutions.
# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on multicluster inference gateways.                                                                                                          |
|   2 | Inference gateways address unique GenAI traffic, which is larger and more complex than typical web requests.                                                  |
|   3 | An inference gateway is a proxy/load balancer with an endpoint picker (EP) extension.                                                                         |
|   4 | The EP uses a scheduler with filter and score plugins to select the best model server replica.                                                                |
|   5 | Inference pool is a new resource to logically group compute resources (e.g., GPUs, base models).                                                              |
|   6 | Inference pool API is stable (GA as of 1.0.0 release) and designed to be minimal and adaptable.                                                               |
|   7 | Inference pool uses selectors to discover backend pods and target ports for routing.                                                                          |
|   8 | The EP scrapes backend model server metrics to inform routing decisions.                                                                                      |
|   9 | Inference gateway routes requests to the EP, which selects the optimal backend endpoint.                                                                      |
|  10 | Benchmarks show inference gateways provide more uniform KV cache utilization and lower tail latency than traditional load balancing.                          |
|  11 | Multicluster inference is needed due to GPU scarcity and the inability of a single cluster to handle peak loads.                                              |
|  12 | Gateway API provides L7 routing; multicluster service API enables sharing services across clusters.                                                           |
|  13 | Multicluster inference pools use annotations to export/import inference pools across clusters.                                                                |
|  14 | Endpoint pickers are deployed in each cluster for scalability and real-time metrics collection.                                                               |
|  15 | Cluster selection strategies include round robin, active/passive, and metrics-based approaches.                                                               |
|  16 | Metrics-based selection (e.g., KV cache utilization) is preferred for optimal routing.                                                                        |
|  17 | Two routing modes: direct routing (gateway talks directly to EP and endpoints) and gateway routing (gateway discovers and routes via cluster-local gateways). |
|  18 | Multicluster inference gateways enable optimal GPU resource utilization across clusters.                                                                      |
|  19 | Single cluster inference gateway implementations are GA; multicluster implementations are in progress.                                                        |
|  20 | There is a proposal for a generic multicluster backend to improve scalability.                                                                                |
|  21 | Endpoint picker is designe                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=UJy8n8uX8G4)