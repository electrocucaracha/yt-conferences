---
type: Video Note
title: "Make GenAI Production-Ready With Kubernetes Patterns - Roland Huss, Red Hat & Bilgin Ibryam, Diagrid"
description: "In this session, the speakers introduce themselves as experts in Kubernetes and generative AI, highlighting their collaborative work on books about Kubernetes patterns and running generative AI workloads. They explain how traditional Kubern..."
resource: https://www.youtube.com/watch?v=tLK5jyhQOgA
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, the speakers introduce themselves as experts in Kubernetes and generative AI, highlighting their collaborative work on books about Kubernetes patterns and running generative AI workloads.
They explain how traditional Kubernetes patterns—such as controller, init container, stateful service, batch job, and daemon service—can be adapted to support the unique requirements of large language models (LLMs), including challenges related to model size, GPU requirements, and initialization times.
The discussion covers emerging patterns specific to generative AI, such as efficient model data initialization using persistent volumes, model cars, and the new image volume type in Kubernetes 1.35, which streamlines mounting large model data.
They also address advanced request routing for LLMs, emphasizing the need for state-aware routing based on model load and cache, and introduce prefix-aware and split-phase routing for improved efficiency.
Finally, they discuss the retrieval augmented generation (RAG) pattern, demonstrating how Kubernetes primitives support complex AI pipelines, and encourage attendees to consult their books for further details.
# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Rulen Hus (Red Hat, AI, co-author of books) and Bill Gin Ibraham (DIG grid, Dapper project).                                        |
|   2 | Two books discussed: one on Kubernetes patterns, one on running generative AI (GenAI) on Kubernetes; both available for free download.                        |
|   3 | The session blends concepts from both books, focusing on applying Kubernetes patterns to GenAI workloads.                                                     |
|   4 | Recap of traditional Kubernetes patterns: controller, init container, stateful service, batch job, daemon service.                                            |
|   5 | Models differ from web apps: large, read-only trained data; require GPU nodes and specific runtimes; operational challenges.                                  |
|   6 | KServe project implements controller pattern for model services, automating deployments, scaling, and routing.                                                |
|   7 | GenAI workloads use similar patterns as traditional apps but at larger scale and with different resource requirements (e.g., GPU, longer startup).            |
|   8 | Predictable demand pattern: declare CPU, memory, and GPU needs; use affinities or dynamic resource allocation for flexibility.                                |
|   9 | Automated placement pattern: manage workload placement on heterogeneous clusters; protect GPU nodes using taints.                                             |
|  10 | Sidecar and adapter patterns: provide unified API access to LLMs (e.g., via Dapper, OpenAI API).                                                              |
|  11 | Some patterns change in GenAI context:                                                                                                                        |
|  12 | Init container now handles large model data movement.                                                                                                         |
|  13 | Immutable configuration pattern shifts to managing model weights.                                                                                             |
|  14 | Health probe duration increases; checks model loading and warming.                                                                                            |
|  15 | Declarative deployment must account for long-running requests and startup times.                                                                              |
|  16 | Batch job pattern may use gang scheduling for fine-tuning tasks.                                                                                              |
|  17 | New patterns for GenAI:                                                                                                                                       |
|  18 | Model data initialization pattern: strategies for handling large model data (init container, persistent volume, model baked into OCI image, direct download). |
|  19 | Model car pattern: sidecar container keeps model data accessible via shared process namespace; workaround for direct image mounting.                          |
|  20 | Image volume types (Kubernetes 1.35+): directly mount OCI im                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tLK5jyhQOgA)