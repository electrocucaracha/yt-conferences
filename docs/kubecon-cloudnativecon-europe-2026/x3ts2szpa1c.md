---
layout: default
title:
  "Tutorial: Building Intelligent Apps with RAG on Kube... Cedric C, Natale V,
  Christopher N & Legare K"
nav_order: 379
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The workshop introduces participants to building Retrieval-Augmented
  Generation (RAG) systems using open source tools such as Kubeflow, Kafka, KNative,
  and vector databases on top of Kubernetes and OpenShift. Attendees learn how to
  automate...
resource: https://www.youtube.com/watch?v=x3tS2SzpA1c
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The workshop introduces participants to building Retrieval-Augmented Generation (RAG) systems using open source tools such as Kubeflow, Kafka, KNative, and vector databases on top of Kubernetes and OpenShift.
Attendees learn how to automate data pipelines that ingest unstructured data (like PDFs or ServiceNow tickets), convert it into structured embeddings using tools like Dockling, and store it in a vector database for efficient semantic search and retrieval by large language models (LLMs).
The hands-on lab guides users through setting up event-driven pipelines—triggered by file uploads to object storage (MinIO) and managed via Kafka and KNative—to automate data ingestion and model serving, with JupyterHub used for experimentation and interaction.
The session emphasizes the importance of data preparation, storage, and retrieval in making AI applications effective, and provides support through an integrated AI assistant and live facilitators.
All workshop materials and instructions are available online, and participants are encouraged to contribute feedback and improvements via GitHub.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Workshop focuses on building a RAG (Retrieval-Augmented Generation) system using open source projects on Kubernetes.             |
|   2 | Components include Kubeflow, Kafka, KNative, JupyterHub, vector databases, and Dockling for PDF data extraction.                 |
|   3 | Workshop demonstrates combining these tools to enable question-answering over locked-away data (PDFs, ServiceNow tickets, etc.). |
|   4 | Participants will get hands-on experience with data pipelines, vector databases, and Jupyter notebooks for data retrieval.       |
|   5 | RAG systems allow LLMs to answer questions by retrieving and summarizing relevant data sources.                                  |
|   6 | Fine-tuning and prompt engineering are discussed as methods to customize LLM responses.                                          |
|   7 | Architecture is cloud-native, containerized, and runs on OpenShift (Kubernetes distribution).                                    |
|   8 | Data must be prepared in text formats (markdown, JSON) for LLMs.                                                                 |
|   9 | Pipelines automate data ingestion and embedding into vector databases for retrieval.                                             |
|  10 | Kubeflow automates AI tasks such as data processing, validation, and deployment.                                                 |
|  11 | Event-driven pipelines use MinIO for object storage, Kafka for event streaming, and KNative Eventing for serverless triggers.    |
|  12 | Dockling is used to convert PDFs to structured data locally.                                                                     |
|  13 | KServe is used for model deployment and serving.                                                                                 |
|  14 | JupyterHub provides a containerized Python environment for interacting with models and data.                                     |
|  15 | Vector databases store text embeddings for fast semantic search and retrieval.                                                   |
|  16 | LangChain is used to abstract database and model connections for prompt construction.                                            |
|  17 | Workshop includes two main units: a 101 primer (unit 2) and an advanced Kafka integration (unit 3).                              |
|  18 | Lab is web-based; users are assigned to multi-tenant Kubernetes clusters with unique credentials.                                |
|  19 | AI assistant is available for troubleshooting; human assistants can help if needed.                                              |
|  20 | Lab materials and instructions are available on GitHub; clusters are available for the day.                                      |
|  21 | Feedback and contributions to the workshop are encouraged via GitHub.                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=x3tS2SzpA1c)
