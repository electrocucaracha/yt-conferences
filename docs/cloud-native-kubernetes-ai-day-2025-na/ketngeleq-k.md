---
type: Video Note
title: "Panel: AI Infra Best Practices: Enterprise Do’s and Don’ts - Madhuri Yechuri & Andrew Leung"
description: "The discussion centers on Uber’s extensive experience building and operating AI infrastructure, particularly on Kubernetes, for both predictive models and emerging LLM-based use cases. Andrew Le Young from Uber explains that Uber’s AI power..."
resource: https://www.youtube.com/watch?v=KETngElEQ_k
tags: ["cloud-native-kubernetes-ai-day-2025-na", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The discussion centers on Uber’s extensive experience building and operating AI infrastructure, particularly on Kubernetes, for both predictive models and emerging LLM-based use cases.
Andrew Le Young from Uber explains that Uber’s AI powers key features such as ride ETAs, fraud detection, Uber Eats ranking, and merchant tools, with workloads spanning training, inference, and batch processing.
Uber primarily uses Ray for training, Spark for ETL, and Nvidia Triton for serving, running these workloads on dedicated Kubernetes clusters that are segregated by hardware type (GPU vs.
CPU) and function (training vs.
serving).
The company has migrated from on-prem data centers to a multicloud strategy, which introduces challenges in data and compute locality, disaster recovery, and GPU resource fungibility across providers and hardware types.
Uber’s lessons include the importance of disaggregating CPU and GPU tasks to improve utilization, building platform-agnostic metrics for observability, and preparing for a diverse accelerator ecosystem.
Key advice for enterprises is to carefully consider the placement of data lakes relative to compute, avoid hardware and cluster silos, and design infrastructure for flexibility and efficient resource sharing as AI workloads and hardware diversity grow.
# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Uber has been running AI workloads on Kubernetes for over 10 years, starting with the Michelangelo platform.                                                    |
|   2 | Andrew Le Young leads Uber’s compute platform team, focusing on revamping their GPU stack.                                                                      |
|   3 | Uber uses AI for user-facing experiences: ride ETAs, fraud detection, financial post-processing, Uber Eats ranking, and merchant ad campaigns.                  |
|   4 | Both training and inference workloads are supported, including predictive models and LLM-based use cases for internal and external products.                    |
|   5 | Training is almost exclusively run on Ray; batch workloads may use Spark or Ray depending on the use case.                                                      |
|   6 | Model serving uses Nvidia Triton for predictive models and VLM for internal LLM use cases.                                                                      |
|   7 | Uber migrated from an in-house container platform to Kubernetes over the past three years.                                                                      |
|   8 | Separate Kubernetes infrastructures exist for batch workloads and microservices; inference services are deployed like other internal microservices.             |
|   9 | GPU and CPU workloads are segregated at the cluster level, leading to siloed capacity; efforts are underway to reorganize hardware mapping.                     |
|  10 | Training, serving, and batch infrastructures are separated and do not share clusters.                                                                           |
|  11 | Uber is moving from on-prem data centers to a multicloud strategy, with data lakes and compute in different cloud providers.                                    |
|  12 | GPU capacity is scarce and expensive; workload placement considers cloud provider strengths and data locality.                                                  |
|  13 | Kubernetes clusters are treated as fault domains and scaling units; workloads are dispersed to satisfy fault tolerance and capacity.                            |
|  14 | Disaster recovery for GPU workloads is complex due to cost, scarcity, and hardware specificity; pre-planned capacity and creative fallback strategies are used. |
|  15 | Ray infrastructure spans multiple Kubernetes clusters; distributed training across clusters is emerging for larger models.                                      |
|  16 | Preference is for clusters as scaling units rather than special-purpose; asymmetry in cluster sizes can cause operational challenges.                           |
|  17 | Architectural split between CPU a                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=KETngElEQ_k)