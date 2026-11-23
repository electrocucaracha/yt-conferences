---
layout: default
title: "ModelPack: An Open Standard for Packaging, Distributing, and Running LLM in CloudNative Environments"
nav_order: 126
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Jo, a software engineer at Ant Group, presents Model Pack, an open-source, vendor-neutral specification designed to standardize the packaging, distribution, and execution of Large Language Models (..."
resource: "https://www.youtube.com/watch?v=eZhiUYtIHjI"
youtube_stats:
  view_count: 44
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Jo, a software engineer at Ant Group, presents Model Pack, an open-source, vendor-neutral specification designed to standardize the packaging, distribution, and execution of Large Language Models (LLMs) in cloud-native environments.
Addressing the challenges of deploying models on infrastructure originally built for containers, Model Pack leverages the OCI artifact specification to treat models as first-class citizens, offering critical capabilities such as version control, immutability, self-hosting, and traceability that are often missing in traditional storage solutions like Hugging Face or object storage.
The presentation details practical tools like the `modelctl` command-line interface and a Kubernetes CSI driver, which allow developers to build, push, pull, and mount model images seamlessly, while integrating with the Dragonfly peer-to-peer system to optimize bandwidth and accelerate model loading in large-scale production clusters.
Furthermore, Model Pack introduces a structured model architecture configuration that views LLMs as modular blocks, enabling efficient partial weight loading for parallelism strategies and reducing code duplication across different inference frameworks.
By extending the proven standards of the container ecosystem to AI workloads, Model Pack aims to create a unified, efficient, and standardized pipeline for managing AI models within the cloud-native landscape.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Model Pack is a vendor-neutral open-source specification for packaging, distributing, and running LLMs in cloud-native environments.                                   |
|   2 | Infrastructure is shifting from container-centric to model-centric, creating challenges because current systems are built for containers, not models.                  |
|   3 | Models are stored in various locations like NFS, object storage, and artifacts, leading to compatibility issues due to different formats and management methods.       |
|   4 | Model Pack is based on the OCI and its artifacts specification, offering standardization similar to container images.                                                  |
|   5 | It provides capabilities such as version control, immutability, self-hosting, and traceability for AI models.                                                          |
|   6 | The OCI specification has been extended to support artifacts, allowing models to be defined as new artifact types while maintaining container ecosystem compatibility. |
|   7 | Model Pack consists of a model image spec and a model runtime spec.                                                                                                    |
|   8 | A model image includes a manifest with config, layers, and annotations, providing a consistent format for packaging AI models.                                         |
|   9 | The config part describes model metadata such as name, architecture, quantization method, and precision.                                                               |
|  10 | Layers contain individual files like model weights and config.json, with each file representing a layer in the image.                                                  |
|  11 | Raw media type is used for model weight files to enable zero-copy reads, reducing I/O costs and speeding up model loading.                                             |
|  12 | Model Control is a command-line tool for managing OCI model artifacts, allowing users to build, push, pull, and run model images.                                      |
|  13 | The Model CSI driver allows models to be mounted and served directly as volumes in Kubernetes, even on older versions.                                                 |
|  14 | Both tools are integrated with the Dragonfly peer-to-peer file distribution system to accelerate model pulling and mounting.                                           |
|  15 | Model files define how to build a model image, similar to Dockerfiles, and can be generated automatically from Hugging Face downloads.                                 |
|  16 | Model images can be pushed to OCI-compatible registries like Harbor, which supports security scanning and container signing.                                           |
|  17 | Models can be pulled using the Model Control pull command or mounted into Kubernetes pods as volumes for convenient deployment.                                        |
|  18 | Dragonfly solves bandwidth issues when many nodes pull models simultaneously by using peer-to-peer distribution and cluster caching.                                   |
|  19 | Model Pack integrates with existing tools like Kubernetes, Harbor, container runtimes, and Dragonfly to create a full model management pipeline.                       |
|  20 | The specification is gaining support from open-source projects including Kubernetes, Harbor, and Dragonfly.                                                            |
|  21 | Model Pack introduces a model architecture config that views LLMs as modular blocks rather than black boxes.                                                           |
|  22 | Transformer architectures are converging, with common blocks like tokenizers, position embeddings, self-attention, normalization, and feed-forward networks.           |
|  23 | Defining models in blocks allows tools and frameworks to reuse logic, improving compatibility and reducing duplicated work.                                            |
|  24 | The self-attention definition includes types like MHA, GQA, and MLA, along with parameters for causal attention and QV merging.                                        |
|  25 | Model Pack enables splitting and loading only necessary weight parts, significantly speeding up startup for large models in pipeline parallelism.                      |
|  26 | It addresses the M+N problem by allowing LM developers, inference engine developers, and infrastructure providers to avoid duplicate implementations.                  |
|  27 | The model runtime spec defines the lifecycle, runtime configuration, and file system layout for running models, though it is still evolving.                           |
|  28 | Model Pack provides a standard, open way to manage AI models in cloud-native environments by adapting container best practices.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eZhiUYtIHjI/hqdefault.jpg)](https://www.youtube.com/watch?v=eZhiUYtIHjI)

[Watch on YouTube](https://www.youtube.com/watch?v=eZhiUYtIHjI)
