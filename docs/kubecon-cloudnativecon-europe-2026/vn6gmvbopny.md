---
type: Video Note
title: "Sponsored Keynote: Inference and Sovereign AI: Scaling Cloud-Nat... Karena Angell & Vincent Caldeira"
description: "The speaker discusses the challenges and solutions involved in scaling generative AI (GenAI) systems while maintaining data sovereignty. As organizations increasingly prioritize sovereign AI and use Kubernetes to scale AI workloads, traditi..."
resource: https://www.youtube.com/watch?v=Vn6gmvbOpNY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the challenges and solutions involved in scaling generative AI (GenAI) systems while maintaining data sovereignty.
As organizations increasingly prioritize sovereign AI and use Kubernetes to scale AI workloads, traditional web application scaling methods prove inadequate due to the heavy, unpredictable demands of AI models.
To address this, the team is building a Kubernetes-native, open-source AI factory that ensures interoperability, avoids vendor lock-in, and supports regulatory compliance, such as the EU AI Act.
Their approach integrates tools like KServe for abstraction and autoscaling, a new API inference gateway for AI-aware load balancing, and LLMD for intelligent, cost-effective distributed inference and resource optimization.
This modular stack transforms standard clusters into efficient, sovereign inference engines by enabling advanced, state-aware scheduling and routing, maximizing GPU performance and minimizing delays.
# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | Generative AI is moving from labs to production systems.                                                                |
|   2 | Scaling AI presents challenges in maintaining data control.                                                             |
|   3 | 79% of organizations view sovereign AI as a top strategic priority.                                                     |
|   4 | 60% of organizations use Kubernetes to scale AI workloads.                                                              |
|   5 | Bridging Kubernetes scalability with data sovereignty is a current challenge.                                           |
|   6 | Scaling GenAI differs from scaling traditional web applications due to heavier, less predictable workloads.             |
|   7 | Traditional traffic routing and load balancing are inadequate for AI, causing delays and inefficiencies.                |
|   8 | Running GenAI at scale requires an AI-aware, cloud-native platform.                                                     |
|   9 | True sovereignty means interoperability and avoiding vendor lock-in, not isolation.                                     |
|  10 | A Kubernetes-native AI factory is being built using an open-source foundation for full stack control.                   |
|  11 | The modular blueprint enables AI deployment in any cloud, at the edge, or in sovereign clouds.                          |
|  12 | The open approach supports regulatory compliance, including the EU AI Act.                                              |
|  13 | A new open-source AI inference stack based on VLM and LLMD is being developed and integrated into Kubernetes.           |
|  14 | KServe is used as a standard abstraction layer for autoscaling and complexity management.                               |
|  15 | Kubernetes enables dynamic scaling and enterprise-grade orchestration for AI.                                           |
|  16 | The new API inference gateway extension provides AI-specific load balancing.                                            |
|  17 | LLMD optimizes distributed resources and delivers cost-effective distributed inference via intelligent scheduling.      |
|  18 | The stack transforms a standard cluster into a sovereign inference engine.                                              |
|  19 | LLMD upgrades Kubernetes with AI routing fabric, using prefix-aware routing and KB cache for efficient prompt handling. |
|  20 | This reduces time to first token and offloads GPU processing.                                                           |
|  21 | LLMD separates compute-heavy prompt reading from memory-bound token generation across the cluster.                      |
|  22 | Advanced state-aware scheduling maximizes GPU performance beyond simple round-robin scaling.                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Vn6gmvbOpNY)