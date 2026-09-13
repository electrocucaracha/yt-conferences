---
layout: default
title:
  RAG and Fine Tuning With Kubeflow - Francisco Javier Arceo, Red Hat & Andrey
  Velichkevich, Apple
nav_order: 252
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Francisco, a senior principal software engineer at Red Hat, and Shia
  Wong, a member of the Kubeflow community, introduce a talk on retrieval-augmented
  generation (RAG) and fine-tuning in AI projects. They discuss why many AI projects
  fail...
resource: https://www.youtube.com/watch?v=kpQh35r3d24
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Francisco, a senior principal software engineer at Red Hat, and Shia Wong, a member of the Kubeflow community, introduce a talk on retrieval-augmented generation (RAG) and fine-tuning in AI projects.
They discuss why many AI projects fail, often due to model hallucinations, and explain that while RAG helps reduce hallucinations by retrieving relevant data chunks for large language models, fine-tuning—especially of the retriever component—can further improve performance and domain adaptation at a lower cost than full model fine-tuning.
The presenters detail the history of RAG, its original focus on fine-tuning both retriever and generator, and how industry trends shifted toward inference due to the popularity and cost-effectiveness of RAG over fine-tuning.
They demonstrate how tools like Feast (an open-source feature store) and Kubeflow Trainer can be used together to efficiently process data, fine-tune retrieval models, and serve embeddings at scale, even on CPUs.
The session includes a practical example using Wikipedia data, outlines the workflow for fine-tuning retrievers, and highlights the benefits of integrating Feast and Kubeflow for scalable, reproducible AI systems, encouraging community involvement in ongoing development.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Francisco, Senior Principal Software Engineer at Red Hat, with experience in financial institutions, startups, and as a maintainer for Feast and Kubeflow.          |
|   2 | Shia Wong, member of Kubeflow, maintainer of Kubeflow Trainer and SDK, graduate student at Shanghai Jiao Tong University.                                           |
|   3 | The original speaker, Angry, could not present due to internal reasons.                                                                                             |
|   4 | Agenda: why AI projects fail, what is RAG, history and popularity of RAG, fine-tuning models with RAG, using Feast and Kubeflow Trainer, demo, Q&A.                 |
|   5 | AI projects often fail due to hallucinations; hallucination is a feature of generative models.                                                                      |
|   6 | Two main approaches: memorization via training or in-context learning (prompting).                                                                                  |
|   7 | RAG (Retrieval Augmented Generation) helps reduce hallucinations but doesn't eliminate them.                                                                        |
|   8 | Traditional ML focused on fine-tuning; fine-tuning is expensive in the generative AI era.                                                                           |
|   9 | RAG became popular as a cheaper alternative to fine-tuning, especially after OpenAI's ChatGPT launch.                                                               |
|  10 | RAG involves embedding queries and data chunks, using vector similarity search (dot product/cosine similarity), and retrieving top K relevant chunks for LLM input. |
|  11 | RAG was originally about fine-tuning both retriever and generator models (Meta AI, NeurIPS 2020).                                                                   |
|  12 | Fine-tuning the retriever in RAG is cost-effective due to smaller model size (e.g., MiniLM vs. Llama).                                                              |
|  13 | Fine-tuning enables adaptation to domain-specific jargon and improves retrieval quality.                                                                            |
|  14 | Retrieval quality is critical: bad retrieval leads to bad generation.                                                                                               |
|  15 | Fine-tuning retrievers can be done on CPUs and scaled with existing infrastructure.                                                                                 |
|  16 | Feast is an open-source feature store for managing and serving features for ML at scale.                                                                            |
|  17 | Feast supports multiple data stores and treats serving/training as first-class citizens.                                                                            |
|  18 | Kubeflow Trainer is a subproject of Kubeflow for scaling ML code and fine-tuning on Kubernetes.                                                                     |
|  19 | Kubeflow Trainer automates model/data download, fine-tuning, and export to cloud storage.                                                                           |
|  20 | Feast and Kubeflow Trainer i                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kpQh35r3d24)
