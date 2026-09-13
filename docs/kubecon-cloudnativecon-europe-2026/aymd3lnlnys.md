---
type: Video Note
title: "Kubeflow in Cloud Native AI: Orchestrati... Johnu G, Valentina S, Antonin S, Alexander P & Michael Z"
description: "The session introduces Kubeflow as a comprehensive, cloud-native AI platform designed to simplify and scale machine learning workflows on Kubernetes. Maintainers from various organizations discuss Kubeflow’s modular components, including to..."
resource: https://www.youtube.com/watch?v=AYmD3LNlNYs
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session introduces Kubeflow as a comprehensive, cloud-native AI platform designed to simplify and scale machine learning workflows on Kubernetes.
Maintainers from various organizations discuss Kubeflow’s modular components, including tools for data preparation, model training, hyperparameter optimization, model registry, and inference, all accessible through a unified Python SDK.
Notable updates include the upcoming Notebooks 2.0 for improved user experience, enhanced model registry integration, distributed training capabilities, and new features in the inference platform to support generative AI and LLM workloads.
Kubeflow Pipelines has transitioned to SeaweedFS for artifact storage, introduced Kubernetes-native resource management, and is moving toward a more streamlined, plugin-based architecture.
The session concludes with an invitation to join the Kubeflow community, access technical resources, and participate in upcoming events and demos.
# Main Points

|   # | Main point                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session introduces Kubeflow in cloud native AI, focusing on agentic AI and LLM ops.                                                                                                                                         |
|   2 | Presenters are maintainers and engineers from READ, Newanics, Capital One, and other organizations.                                                                                                                         |
|   3 | Kubeflow is a foundation of tools for AI platforms on Kubernetes, supporting LLM ops, GenAI, and various use cases.                                                                                                         |
|   4 | Aims to simplify workflows for data scientists, AI engineers, and platform engineers, ensuring portability and scalability.                                                                                                 |
|   5 | Key components: Spark Operator, Trainer, Katib (hyperparameter optimization), KServe (model serving), Pipelines, Model Registry, Notebooks.                                                                                 |
|   6 | Typical workflow: data preparation (Spark), feature store, model development (Notebooks), automation (Pipelines), training, fine-tuning, serving (KServe), optimization (Katib).                                            |
|   7 | Notebooks 2.0 is in development, focusing on simplicity, customization, and resource control for platform engineers.                                                                                                        |
|   8 | Unified Python SDK provides access to all Kubeflow components, supports local and remote execution, and integrates with popular ML frameworks.                                                                              |
|   9 | Model Registry offers a central interface for managing models, metadata, and artifacts, with deep integration with KServe and secure supply chain features.                                                                 |
|  10 | Kubeflow Trainer enables distributed training and fine-tuning, advanced scheduling, and real-time job progress tracking.                                                                                                    |
|  11 | Katib provides Kubernetes-native AutoML, hyperparameter optimization, and neural network search.                                                                                                                            |
|  12 | Spark Operator supports scalable data processing with Apache Spark, including interactive development and integration with Notebooks.                                                                                       |
|  13 | KServe is a Kubernetes-native, hardware-agnostic inference platform supporting predictive and generative use cases, with advanced autoscaling, cache management, and LLM-specific features.                                 |
|  14 | Kubeflow Pipelines is a workflow orchestration engine with a Python SDK and web UI; recent updates include switching to SeaweedFS, Kubernetes-native resources, multi-architecture support, and improved artifact handling. |
|  15 | Upcoming features: reduced pod usage per component, n                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=AYmD3LNlNYs)