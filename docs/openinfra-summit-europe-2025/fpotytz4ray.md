---
layout: default
title: Open Source GenAI on OpenStack Part One LLMs
nav_order: 59
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Marshall, Chief Technologist at Infotren, presents a session on running open-source generative AI models on OpenStack, specifically utilizing the Jetstream cluster and Exosphere frontend."
resource: "https://www.youtube.com/watch?v=FPotYtZ4rAY"
youtube_stats:
  view_count: 125
  like_count: 3
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

Marshall, Chief Technologist at Infotren, presents a session on running open-source generative AI models on OpenStack, specifically utilizing the Jetstream cluster and Exosphere frontend.
The presentation highlights a custom Docker-based framework designed to simplify the deployment of PyTorch, Transformers, and Diffusers, ensuring reproducibility and compatibility with both CUDA and CPU environments.
Key demonstrations include building a search agent that combines web search with local LLMs like Llama 3.1 and GPT-OSS 20B, implementing Retrieval-Augmented Generation (RAG) using RAGBits and ChromaDB to query local documents, and leveraging Vision Language Models (VLMs) for image understanding.
Additionally, the speaker showcases image generation capabilities using Flux and Stable Diffusion, emphasizing that these workloads can be executed on consumer-grade hardware with 24GB of VRAM or high-end H100 GPUs.
The session concludes by promoting the upcoming release of the public GitHub repository, which contains all the code and examples needed for attendees to replicate these demos on their own infrastructure.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The session focuses on running open-source generative AI, including LLMs and VLMs, on OpenStack using the Jetstream cluster.                           |
|   2 | The presentation is a collaboration between the speaker and IU, utilizing hardware loaned by Jetstream team members Mike Low and Julian Pistorius.     |
|   3 | The speaker, Marshall, is the Chief Technologist and VP of AI and Data Science at Infotren, with a background in NIST and OpenStack Scientific SIG.    |
|   4 | Demos are designed to run on 24GB of VRAM, making them accessible for users with consumer-grade GPUs like the RTX 3090 or 4090.                        |
|   5 | The core framework used is CoreAI, a Docker-based solution for building machine learning and computer vision images with PyTorch and OpenCV.           |
|   6 | The setup requires Docker, Docker Compose, Tailscale for secure networking, and an NVIDIA GPU for optimal performance.                                 |
|   7 | Tailscale is used as an overlay VPN to expose services without opening public ports, enhancing security on the OpenStack instance.                     |
|   8 | Ollama is employed to serve local large language models, specifically Llama 3 8B and GPT OSS 20B, within the 24GB VRAM constraint.                     |
|   9 | A search agent demo demonstrates combining web search and web fetch results as context for an LLM to generate answers.                                 |
|  10 | The agent workflow uses Sonar for web search and local models for synthesis, showcasing both manual function calling and native tool calling features. |
|  11 | Retrieval-Augmented Generation (RAG) is demonstrated using the RAGBits framework and Duckling for document parsing.                                    |
|  12 | Documents are ingested, converted into text chunks, and stored in a ChromaDB vector database for semantic search.                                      |
|  13 | The RAG demo processes an Exosphere document and an OpenStack scientific book, retrieving relevant context to answer specific queries.                 |
|  14 | Vision Language Models (VLMs) are introduced using the Google Gemma model to extract and interpret information from images.                            |
|  15 | The VLM demo analyzes an OpenStack architectural diagram, describing components and explaining the underlying concepts.                                |
|  16 | Image generation is demonstrated using Flux, leveraging diffusers and transformers to create images from text prompts.                                 |
|  17 | The speaker emphasizes reproducibility by providing a public GitHub repository with all code and configurations for the demos.                         |
|  18 | The session is part of a two-day talk, with the second day covering video and image generation in more detail.                                         |
|  19 | The speaker encourages community engagement through the OpenStack Scientific SIG and provides links for further resources.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/FPotYtZ4rAY/hqdefault.jpg)](https://www.youtube.com/watch?v=FPotYtZ4rAY)

[Watch on YouTube](https://www.youtube.com/watch?v=FPotYtZ4rAY)
