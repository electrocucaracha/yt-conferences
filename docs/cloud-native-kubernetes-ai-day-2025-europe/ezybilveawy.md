---
layout: default
title: "Panel: Engaging the Kubeflow Community: Building an Enterprise-Ready AI/ML Platform"
nav_order: 7
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "This panel discussion at CubeCon features experts from Apple, NVIDIA, Red Hat, Nutanix, and Canonical who explore the evolution of Kubeflow into a comprehensive, enterprise-ready MLOps platform."
resource: "https://www.youtube.com/watch?v=eZYBILVeaWY"
youtube_stats:
  view_count: 222
  like_count: 4
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

This panel discussion at CubeCon features experts from Apple, NVIDIA, Red Hat, Nutanix, and Canonical who explore the evolution of Kubeflow into a comprehensive, enterprise-ready MLOps platform.
The speakers highlight Kubeflow’s composable architecture, which allows organizations to deploy individual components like the Training Operator, Notebooks, and Pipelines natively on Kubernetes to address specific stages of the machine learning lifecycle, from experimentation to production serving.
A significant focus is placed on the platform's adaptability to Generative AI and Large Language Models, with new initiatives such as the Kubeflow SDK, one-click fine-tuning capabilities, and integrations with tools like Llama Stack to streamline distributed training and inference.
The panel also addresses critical industry challenges, including the complexity of GPU scheduling and inference cold starts, noting that NVIDIA has open-sourced its Run:AI scheduler to enhance these capabilities within the cloud-native ecosystem.
Finally, the speakers emphasize the importance of open governance, community collaboration, and the establishment of conformance standards to ensure Kubeflow remains a vendor-neutral foundation that supports diverse deployment scenarios, from on-premises to hybrid cloud environments.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | CubeFlow is an end-to-end MLOps platform running natively on Kubernetes that covers the entire machine learning lifecycle.                                               |
|   2 | The platform is composable, allowing users to deploy individual components like the Trainer, Notebooks, or Pipelines independently or as a full bundle.                  |
|   3 | Key components include CubeFlow Notebooks for experimentation, the Trainer for distributed training, KServe for model serving, and Pipelines for workflow orchestration. |
|   4 | Andre from Apple and the CubeFlow Steering Committee emphasizes the project's maturity since 2017 and its ability to integrate with existing enterprise platforms.       |
|   5 | Ronin from RunAI (acquired by Nvidia) highlights the use of CubeFlow components like Notebooks, Training Operator, and Pipelines within the RunAI platform.              |
|   6 | RunAI has open-sourced its scheduler, named Kai Scheduler, and is working on integrating it with the CubeFlow ecosystem.                                                 |
|   7 | Yan from Red Hat describes how the company uses CubeFlow as a vendor-neutral foundation for its hybrid cloud AI platform, Open Data Hub.                                 |
|   8 | Red Hat has donated the Model Registry project to the CubeFlow community to help manage model versions and artifacts.                                                    |
|   9 | Jonu from Nutanix notes that the community has grown from a few companies to thousands of contributors, driven by open governance and transparency.                      |
|  10 | The CubeFlow community aims to ensure no single company controls the ecosystem, using transparent decision-making and standardized contribution guidelines.              |
|  11 | Andrea from Canonical addresses enterprise needs such as air-gapped deployments, security, and portability across different Kubernetes distributions.                    |
|  12 | The community is actively working to bridge the gap between ML and cloud-native communities, particularly for GenAI and LLM workloads.                                   |
|  13 | New initiatives include the CubeFlow SDK for Python-based interaction and LLM Blueprints to simplify fine-tuning and serving on Kubernetes.                              |
|  14 | Inference remains a significant challenge, with specific issues like cold start times for GPU-based AI servers requiring specialized solutions.                          |
|  15 | The community is developing a conformance program to define standards for CubeFlow distributions and enable official support from cloud providers.                       |
|  16 | CubeFlow Pipelines are highly extensible, allowing users to integrate various operators and tools like Spark or Ray into custom ML workflows.                            |
|  17 | Documentation gaps are identified as a key area for improvement to make the platform's capabilities more accessible to new users.                                        |
|  18 | The community is planning a survey to gather feedback on component usage and identify the most popular features among users.                                             |
|  19 | Contributors are encouraged to join working groups, provide feedback on GitHub, and engage in the Slack channel to help shape the project's future.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eZYBILVeaWY/hqdefault.jpg)](https://www.youtube.com/watch?v=eZYBILVeaWY)

[Watch on YouTube](https://www.youtube.com/watch?v=eZYBILVeaWY)
