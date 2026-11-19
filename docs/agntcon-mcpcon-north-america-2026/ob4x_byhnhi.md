---
layout: default
title: "Don't Route What You Can't Redact: Sensitivity-Aware LLM Routing - C. Nuland & G. Ableidinger"
nav_order: 151
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Grace Whitinger and Christopher Newlan from Red Hat presented a framework for sensitivity-aware LLM routing designed to optimize cost, data sovereignty, and latency in enterprise environments."
resource: "https://www.youtube.com/watch?v=OB4x_byHNhI"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Grace Whitinger and Christopher Newlan from Red Hat presented a framework for sensitivity-aware LLM routing designed to optimize cost, data sovereignty, and latency in enterprise environments.
They argued that relying solely on frontier models leads to unnecessary spending, compliance risks, and latency issues, advocating instead for a multi-dimensional routing strategy that considers both request complexity and data sensitivity.
The solution utilizes LLM DSC, a lightweight 23-million-parameter classifier that operates with a median latency of 3 milliseconds, to label requests before the Praxis AI gateway routes them to appropriate model tiers.
To address data sovereignty, the architecture integrates redaction tools like Presidio and Glider, which mask sensitive information such as PII before requests cross trust boundaries to external SaaS models, allowing for secure processing and subsequent reapplication of data upon return.
This multi-tiered approach, which combines semantic routing with traditional egress guardrails, has achieved approximately 99% accuracy in internal tests and is specifically engineered to handle high-volume traffic in regulated industries like healthcare and banking.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** Enterprises route requests to avoid unnecessary spend on expensive SaaS models for simple tasks, ensure data sovereignty for sensitive information, address safety gaps in single-model configurations, and prevent latency sprawl caused by complex requests blocking lightweight models.           |
|   2 | :** Instead of blind load balancing, semantic routing uses a small classifier model to analyze request content, determining complexity, confidence, and provenance before passing the decision to a policy engine for actual routing.                                                                    |
|   3 | :** An open-source semantic classifier incubated in the LLM D project. It features 23 million parameters, runs on CPU with a median latency of ~3 milliseconds, and provides auditable decisions including classifier ID and model revision.                                                             |
|   4 | :** An open-source AI-native proxy that executes the routing based on LLM DSC’s classification. Unlike traditional Envoy-based proxies that rely on headers, Praxis inspects the request body content, enabling routing across multi-cloud and hybrid boundaries without relying on GPU metrics.         |
|   5 | :** The combined process of classification by LLM DSC and routing by Praxis achieves an end-to-end latency of approximately 14 milliseconds, designed to handle tens of thousands of requests per minute for high-load environments like banking and healthcare.                                         |
|   6 | & Data Sovereignty:** Routing solely on complexity can breach trust boundaries by sending sensitive PII (e.g., salaries, medical data) to external models, violating regulations like GDPR, HIPAA, and PDC.                                                                                              |
|   7 | :** The architecture evolves from single-dimension complexity routing to a multi-dimensional matrix that considers both complexity and sensitivity (public, confidential, restricted) to determine the appropriate model tier.                                                                           |
|   8 | :** To protect data sovereignty, sensitive information is redacted before requests cross trust boundaries to external SaaS models. This is achieved using Presidio (heuristic/pattern-based) and Glider (relational model-based) to replace PII with placeholders (e.g., "John Doe" becomes "Person 1"). |
|   9 | :** The redaction process is two-way; once the response returns from the external model, the original sensitive data is re-applied at the ingress point, allowing secure use of external models for computation.                                                                                         |
|  10 | :** The solution is not a standalone fix for data sovereignty but a layer within a multi-tiered security strategy that includes traditional network policies, scanning, and egress guardrails.                                                                                                           |
|  11 | :** Internal tests show ~99% accuracy in the overall pipeline and ~90% confidence in routing decisions, achieved through fine-tuning and synthetic data generation.                                                                                                                                      |
|  12 | :** LLM DSC operates as a separate gRPC service or sidecar, allowing it to scale independently from the routing proxy. This decoupling is preferred over integrated solutions (like VLLM Semantic Router) to optimize Kubernetes resource usage and scaling for classification tasks.                    |
|  13 | :** LLM DSC’s ~3ms classification is significantly faster than alternative decision models (e.g., Jev, Switchyard), which typically range from 80ms to 300ms, making it suitable for high-throughput, low-latency enterprise requirements.                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/OB4x_byHNhI/hqdefault.jpg)](https://www.youtube.com/watch?v=OB4x_byHNhI)

[Watch on YouTube](https://www.youtube.com/watch?v=OB4x_byHNhI)
