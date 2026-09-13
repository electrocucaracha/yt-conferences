---
type: Video Note
title: "Cloud Native Theater | Istio Day: Running State of the Art Inference... Jackie Maertens and Nili Guy"
description: "In this presentation, Nili from IBM and Jackie from Microsoft discuss the challenges and solutions for running state-of-the-art AI inference workloads using Istio and LMD. They explain that AI inference now constitutes a significant portion..."
resource: https://www.youtube.com/watch?v=dr03NZmau5g
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Nili from IBM and Jackie from Microsoft discuss the challenges and solutions for running state-of-the-art AI inference workloads using Istio and LMD.
They explain that AI inference now constitutes a significant portion of AI workloads, which differ from traditional HTTP requests due to their variable, resource-intensive, and costly nature.
To address these challenges, LMD—a Kubernetes-native distributed inference platform—integrates with Istio and extends the Kubernetes inference gateway with custom resources like inference pools and inference objectives, enabling programmable routing and optimized request scheduling based on workload characteristics and service level objectives (SLOs).
The system uses a pluggable architecture of filters and scorers, particularly leveraging KV cache management to improve efficiency by routing requests to model servers with precomputed data.
Additionally, they describe innovations such as disaggregating prefill and decode stages across different pods and supporting advanced models and multiple target ports, highlighting recent updates and inviting community contributions to the open-source projects.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | AI workloads, especially inference, are becoming a major workload, accounting for nearly 70% of AI tasks.                                                      |
|   2 | Inference requests differ from HTTP requests: they are slower, non-uniform, and 6-9 times more expensive.                                                      |
|   3 | Regular round-robin load balancing is inefficient for inference workloads due to variable resource needs and cost.                                             |
|   4 | Key challenges: variable, resource-heavy requests; SLOs including throughput and time to first token; heterogeneous hardware; and KV cache management.         |
|   5 | KV cache reuse is critical for optimizing inference performance and reducing computation.                                                                      |
|   6 | LMD is a Kubernetes-native distributed inference platform, now a CNCF sandbox project.                                                                         |
|   7 | LMD architecture includes an inference gateway, scheduler, and model servers, with routing based on load and KV cache reuse.                                   |
|   8 | Kubernetes inference gateway is extended with two CRDs: inference pool (label selectors for serving pods) and inference objective (SLO and request treatment). |
|   9 | Istio can serve as the inference gateway controller, configuring resources and routing based on inference pool and objectives.                                 |
|  10 | The inference scheduler (endpoint picker) uses pluggable filters and scorers to select optimal pods, considering load and KV cache matches.                    |
|  11 | KV cache (pre-calculation of prompts) is essential for fast response; routing to servers with relevant cache improves efficiency.                              |
|  12 | Inference can be disaggregated: prefill (compute-bound) and decode (memory-bound) stages can run on separate pods, increasing throughput.                      |
|  13 | LMD supports mixture-of-experts models and distributed inference, exposing multiple ports for fine-grained scheduling.                                         |
|  14 | Istio has been updated to support multiple target ports in inference pools and can now function as a controller for agent gateway.                             |
|  15 | Both LMD and Istio projects are open source and welcome community contributions.                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dr03NZmau5g)