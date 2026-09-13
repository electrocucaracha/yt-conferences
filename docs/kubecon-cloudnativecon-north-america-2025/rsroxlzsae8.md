---
type: Video Note
title: "Rage Against the Machine: Fighting AI Complexity With Kubernetes Simplicity - Paul Yu & Sachi Desai"
description: "In this session, the presenters discuss simplifying the integration of AI, specifically large language models (LLMs), into applications using Kubernetes. They highlight the challenges of grounding LLMs with accurate, context-specific data..."
resource: https://www.youtube.com/watch?v=RsROxLzsAe8
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, the presenters discuss simplifying the integration of AI, specifically large language models (LLMs), into applications using Kubernetes.
They highlight the challenges of grounding LLMs with accurate, context-specific data, noting that traditional approaches like fine-tuning or building retrieval-augmented generation (RAG) pipelines can be complex and resource-intensive.
The CNCF sandbox project Kaido is introduced as a Kubernetes-native toolchain operator that streamlines the deployment and management of AI workloads, including inference, fine-tuning, and RAG, through declarative workspaces and minimal YAML configuration.
A live demo showcases how Kaido enables developers to quickly set up context-aware AI applications—such as a CubeCon session planner—by abstracting away infrastructure complexity and supporting flexible routing to different models and endpoints.
The session concludes by emphasizing Kaido’s ability to consolidate disparate AI tools and frameworks into a scalable, efficient, and developer-friendly Kubernetes workflow, encouraging attendees to experiment with the demo and contribute to the project.
# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session titled "Rage Against the Machine: Fighting AI Complexity with Kubernetes Simplicity"                                                    |
|   2 | AI is now widely integrated into daily life, but often provides inaccurate or fabricated responses                                              |
|   3 | Fine-tuning LLMs for better context is costly and requires ML expertise                                                                         |
|   4 | Retrieval Augmented Generation (RAG) pipelines offer a more efficient way to ground LLMs with real data                                         |
|   5 | RAG involves embedding knowledge bases, storing vectors, and retrieving relevant data for LLM queries                                           |
|   6 | Implementing RAG adds infrastructure complexity (vector databases, embedding models, retrievers)                                                |
|   7 | Kubernetes AI Toolchain Operator (Kaido) simplifies deploying AI workloads on Kubernetes                                                        |
|   8 | Kaido provides Kubernetes-native declarative workspaces for inference, fine-tuning, and RAG pipelines                                           |
|   9 | Supports GPU-backed inference, containerized model weights, and OpenAI-compatible endpoints                                                     |
|  10 | Kaido supports multiple serving engines (VLM, Hugging Face Transformers) and tool calling for external APIs                                     |
|  11 | RAG pipelines can be orchestrated in Kaido with as little as 16 lines of YAML                                                                   |
|  12 | Demo application: Chat app for CubeCon session schedule, deployed on Kubernetes using Kaido                                                     |
|  13 | Architecture: Next.js frontend, FastAPI agent service, observability via Grafana, Redis for chat history, Kaito gateway for model-aware routing |
|  14 | Headlamp plugin for Kaido enables easy workspace management and model deployment                                                                |
|  15 | Gateway API inference extension routes requests to appropriate model pools based on request body                                                |
|  16 | RAG engine custom resource deploys retrieval and indexing services, integrating with inference services                                         |
|  17 | Minimal code changes needed to add RAG functionality; just update config and routing                                                            |
|  18 | Data ingestion: Download CubeCon schedule, convert to JSON, index with Argo workflow                                                            |
|  19 | Kaido enables context-aware, scalable AI apps with Kubernetes-native constructs and minimal YAML                                                |
|  20 | RAG allows use of lower-intensity compute (CPU) for embedding models                                                                            |
|  21 | Inference gateway decouples data retrieval from inference logic, sup                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RsROxLzsAe8)