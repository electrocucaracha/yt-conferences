---
type: Video Note
title: "Highly Scalable AI Search Engine and AI Data Lake With Kubernetes and Lance... Lu Qiu & Chanchan Mao"
description: "The presenters discuss the challenges of managing AI data, emphasizing that the key differentiator for AI features is not the models themselves but the data—specifically its volume, velocity, and variety. Traditional data infrastructure str..."
resource: https://www.youtube.com/watch?v=ILolPtZGSXU
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters discuss the challenges of managing AI data, emphasizing that the key differentiator for AI features is not the models themselves but the data—specifically its volume, velocity, and variety.
Traditional data infrastructure struggles with the scale and complexity of modern, multimodal AI data, leading to fragmented systems and reduced productivity.
To address this, they introduce Lance and LanceDB, an open-source, AI-native multimodal lakehouse built on the Lance format, which efficiently stores and manages text, images, videos, and embeddings in a unified system with compute-storage separation and seamless integration with existing open-source tools.
The talk details LanceDB’s technical innovations, such as its columnar storage, user-defined functions for feature engineering, scalable indexing, and support for various search types (full-text, vector, and hybrid), all designed for high scalability and efficient random access.
Real-world use cases from companies like Netflix, Midjourney, and Harvey illustrate how LanceDB enables unified, scalable, and cost-effective AI data management, while its Kubernetes-based architecture ensures autoscaling, strong consistency, and optimized performance for demanding AI workloads.
# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation on building a highly scalable AI search engine and data lake with Kubernetes and LanceDB                                                                                |
|   2 | Differentiation in AI comes from unique enterprise data and its integration with AI features                                                                                         |
|   3 | Three V’s of data in AI: Volume (data size has increased dramatically), Velocity (data generated much faster by models), Variety (multimodal data: text, images, videos, embeddings) |
|   4 | Traditional data infrastructure is not designed for large-scale, multimodal AI data; leads to fragmented systems and reduced productivity                                            |
|   5 | LanceDB and Lance format provide a unified, open-source, multimodal lakehouse for AI data                                                                                            |
|   6 | Store all data types (text, video, audio, sensor data) in a single table on object storage                                                                                           |
|   7 | Incrementally enrich data with new features without copying original data                                                                                                            |
|   8 | Supports compute-storage separation and integrates with open-source tools (Spark, Ray, PyTorch)                                                                                      |
|   9 | Used by companies like Netflix, Databricks, ByteDance, Uber, Midjourney, Runway, Character AI, Hex, Harvey                                                                           |
|  10 | Netflix uses LanceDB to unify petabytes of multimodal data for ML training, content search, and quality metrics                                                                      |
|  11 | Lance format is a columnar, open-source standard for multimodal data, optimized for cloud storage and scalability                                                                    |
|  12 | Eliminates row group concept for better handling of mixed data sizes (e.g., tabular + video)                                                                                         |
|  13 | Supports user-defined functions for feature engineering and data enrichment                                                                                                          |
|  14 | Enables efficient random access and search (full-text, vector/semantic, SQL) via scalable, cloud-based indices                                                                       |
|  15 | Demonstrated hybrid search (keyword + semantic) using a food recipe dataset                                                                                                          |
|  16 | LanceDB supports filters, SQL queries, and agent-based workflows (e.g., with LangChain)                                                                                              |
|  17 | System is autoscaling with Kubernetes; compute and storage are separated for flexibility and cost efficiency                                                                         |
|  18 | Indexer pods optimize read performance and keep indices up to date automatically                                                                                                     |
|  19 | Lance format stores data in compressed blobs with metadata for efficient random access and versioning                                                                                |
|  20 | Consistency is managed via                                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ILolPtZGSXU)