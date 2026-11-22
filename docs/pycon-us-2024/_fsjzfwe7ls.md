---
layout: default
title: "Sponsor Presentations - No Data? No Problem: Zero-Data Model Training Foundational Models (Covalent)"
nav_order: 39
parent: PyCon US 2024
type: Video Note
description: "Santosh Kumar and ARA from Agnostic presented Covalent, an open-source infrastructure platform designed to simplify the development of production-ready AI applications by abstracting complex high-p..."
resource: "https://www.youtube.com/watch?v=_FSJzFWE7ls"
youtube_stats:
  view_count: 363
  like_count: 1
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Santosh Kumar and ARA from Agnostic presented Covalent, an open-source infrastructure platform designed to simplify the development of production-ready AI applications by abstracting complex high-performance computing (HPC) and cloud orchestration into pure Python.
The speakers demonstrated how to build a "zero-data model foundry" startup idea within a single Jupyter notebook, where a user prompt triggers a workflow that uses a large LLM to generate synthetic training data, fine-tunes a smaller model like TinyLlama using Low-Rank Adaptation (LoRA), and deploys the resulting model as a scalable API endpoint.
This process eliminates the need for manual infrastructure management, such as configuring Kubernetes, Docker, or GPU clusters, by allowing developers to define tasks and services with simple decorators that automatically handle resource allocation, autoscaling, and distributed storage across various cloud providers.
The live demo showcased the system’s ability to handle diverse use cases, including detecting movie spoilers, correcting grammatical errors, and translating text into emojis, all while maintaining a serverless architecture that optimizes costs by only charging for active compute time.
By unifying the agility of modern container orchestration with the power of HPC, Covalent enables developers to rapidly iterate on complex AI workflows, such as multi-agent data quality checks and tiered user services, without rewriting underlying infrastructure code.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces Covalent, an open-source platform by Agnostic that enables building production-ready AI applications directly from Python.                                          |
|   2 | The core challenge addressed is the difficulty of combining High Performance Computing (HPC) infrastructure with the scalability and agility of general cloud compute.                          |
|   3 | Covalent abstracts complex infrastructure management, allowing users to deploy models and run simulations without manually configuring Kubernetes, Docker, or Terraform.                        |
|   4 | The platform uses three main components: Electrons (one-off tasks like fine-tuning), Services (persistent endpoints for inference), and Lattices (workflows that orchestrate these components). |
|   5 | A live demo demonstrated building an "LLM Foundry" startup idea where a user prompt triggers the generation of synthetic data, fine-tuning of a smaller model, and deployment of a new API.     |
|   6 | The workflow utilizes a large Llama model to generate fine-tuning data, which is then used to train a smaller TinyLlama model via Low-Rank Adaptation (LoRA).                                   |
|   7 | Resources are managed through Executors, which specify compute requirements such as GPU types (H100, L40), memory, and time limits for each task or service.                                    |
|   8 | Covalent supports distributed volumes that act like local file paths in Python but are stored in the cloud, allowing seamless data sharing between different compute environments.              |
|   9 | The platform enables serverless high-compute execution, meaning users only pay for the compute time actually used for calculations rather than idle development time.                           |
|  10 | The demo showed the fine-tuned model successfully detecting spoilers in movie reviews and correcting grammatical errors in text.                                                                |
|  11 | Covalent allows for multi-cloud and on-premises deployment, enabling users to fine-tune on one provider (e.g., GCP) and deploy on another (e.g., AWS) using the same code.                      |
|  12 | The system supports auto-scaling for inference services, dynamically spinning up GPU instances to handle incoming API requests.                                                                 |
|  13 | Users can define custom runtime environments that are automatically converted into Docker images and distributed across regions.                                                                |
|  14 | The platform facilitates iterative experimentation with high-compute tasks, such as molecular simulations, by providing real-time feedback and shared state.                                    |
|  15 | Covalent Cloud provides a managed pool of GPUs, while the open-source version allows users to bring their own compute resources.                                                                |
|  16 | The architecture supports tiered user experiences by simply swapping executor resources, such as using cheaper GPUs for basic tiers and high-end GPUs for advanced tiers.                       |
|  17 | Future features include "recipes" that package complex workflows into single-line commands for easier deployment.                                                                               |
|  18 | The platform originated from research in heterogeneous computing, specifically the orchestration of quantum and classical computers.                                                            |
|  19 | Covalent enables the creation of multi-agent systems to validate data quality and model performance before final deployment.                                                                    |
|  20 | The entire application demonstrated in the talk was built and deployed within a single Jupyter notebook using standard Python syntax.                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_FSJzFWE7ls/hqdefault.jpg)](https://www.youtube.com/watch?v=_FSJzFWE7ls)

[Watch on YouTube](https://www.youtube.com/watch?v=_FSJzFWE7ls)
