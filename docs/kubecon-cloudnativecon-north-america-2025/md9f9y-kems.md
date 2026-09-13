---
type: Video Note
title: "Demonstration of Automatic Kubernetes Network Policies Generation - Boaz Michaely & Adi Sosnovich"
description: "In this presentation, Boaz from Red Hat and Adi from IBM Research discuss the complexities of Kubernetes network policies, highlighting their importance for security but also the challenges users face due to lack of built-in tooling and the..."
resource: https://www.youtube.com/watch?v=MD9f9Y-kems
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Boaz from Red Hat and Adi from IBM Research discuss the complexities of Kubernetes network policies, highlighting their importance for security but also the challenges users face due to lack of built-in tooling and the intricate many-to-many relationships between pods and policies.
They introduce NPARD, an open-source analytical tool developed by IBM and integrated into Red Hat ACS as "rockscuddle netpole," which automates network policy generation, visualizes connectivity, analyzes overexposure, and explains policy effects using static analysis of YAML resources.
Through live demonstrations, they show how the tool generates effective network policies, identifies overexposed connections, and provides detailed explanations for allowed or denied communications.
The team also compares NPARD's analytical approach to large language models (LLMs) for policy generation and analysis, finding that LLMs often produce syntactic errors, incomplete segmentation, or overly permissive policies, and can misinterpret connectivity, especially in complex scenarios.
They conclude that while LLMs have potential, analytical tools like NPARD are currently more reliable, and recommend integrating such tools into development pipelines to improve security posture, with AI serving as a complementary aid rather than a replacement.
Audience questions address tool limitations, such as lack of support for CNI-specific extensions, performance analysis, and gateway APIs, and the presenters emphasize the need for teams to understand their own connectivity requirements and to use exposure analysis to tighten policies.
# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction by Boaz (Red Hat ACS) and Adi (IBM Research)                                                                                                       |
|   2 | Topic: Kubernetes network policies, challenges, and analytical solution (NPARD) developed by IBM Research, integrated into Red Hat ACS as "rockscuddle netpole" |
|   3 | Kubernetes allows all communication by default, which is a security risk                                                                                        |
|   4 | Network policies introduced in 2017 as pod-level firewalls to restrict communication                                                                            |
|   5 | Policies are namespace resources, specify allowed ports/protocols for ingress/egress, and can select pods/namespaces by labels                                  |
|   6 | Policies are additive; once a pod is selected by a policy, all communication is denied by default unless explicitly allowed                                     |
|   7 | Complexity arises from many-to-many relationships between pods and policies, lack of built-in tooling, and YAML specification intricacies                       |
|   8 | No built-in tooling in Kubernetes/OpenShift for network policy management; existing tools are limited and complex                                               |
|   9 | NPARD tool (integrated as rockscuddle netpole) can:                                                                                                             |
|  10 | Generate network policies automatically                                                                                                                         |
|  11 | Visualize connectivity                                                                                                                                          |
|  12 | Analyze overexposure                                                                                                                                            |
|  13 | Identify responsible rules for connectivity                                                                                                                     |
|  14 | Compare differences between projects                                                                                                                            |
|  15 | Tool works by scanning YAML resources, identifying services and connection hints, and generating default-deny policies with tight connections                   |
|  16 | Supports DNS, visualization formats, focused analysis, and advanced rule stack explanations                                                                     |
|  17 | Demo: Generated policies for Google’s online boutique app, validated connectivity, and visualized network map                                                   |
|  18 | Exposure analysis highlights overexposed connections and suggests tightening policies                                                                           |
|  19 | Connectivity diff tool shows changes in allowed connections between policy versions                                                                             |
|  20 | Explainability tool details which rules allow or deny specific connections                                                                                      |
|  21 | AI/LLM experiment: LLMs tested for policy generation and analysis; found syntax errors, incomplete segmentation, and incorrect explanations                     |
|  22 | NPARD outperformed LLMs in accuracy and reliability; LLMs sometimes hallucinated or misunderstood policies                                                      |
|  23 | Combining an                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MD9f9Y-kems)