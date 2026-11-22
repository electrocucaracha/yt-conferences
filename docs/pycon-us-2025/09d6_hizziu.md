---
layout: default
title: "Construyendo un Buscador Multimodal - Elizabeth Fuentes & Camila Hinojosa Añez"
nav_order: 51
parent: PyCon US 2025
type: Video Note
description: "Camila Hinojosa presents a talk on building a multimodal search engine that combines text and images for intelligent retrieval, noting that while AI has a long history, the current boom is driven b..."
resource: "https://www.youtube.com/watch?v=09d6_hIzZIU"
youtube_stats:
  view_count: 138
  like_count: 1
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Camila Hinojosa presents a talk on building a multimodal search engine that combines text and images for intelligent retrieval, noting that while AI has a long history, the current boom is driven by scalable computational power, massive data availability, and the democratization of information.
The presentation explains that Foundation Models process large amounts of unlabeled data and function as APIs that require context to be passed with each prompt, as they do not inherently retain memory.
To personalize these models effectively, the speaker compares various techniques and identifies Retrieval-Augmented Generation (RAG) as the optimal balance of cost, complexity, and quality, allowing models to access external knowledge without retraining.
The core of the project involves converting text, images, and video frames into numerical embeddings stored in vector databases, which are then matched against user queries to generate accurate, context-aware responses.
The implementation utilizes Amazon Bedrock to access diverse AI models and manage data security, with the final code and demonstrations for text-to-text, text-to-image, and video search made available on GitHub for further exploration.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Camila Hinojosa presented on building a multimodal search engine combining text and images for intelligent search.                                      |
|   2 | The AI boom is driven by scalable computational capacity, massive data proliferation, and the democratization of information.                           |
|   3 | Historical context includes the first AI winter in 1964 due to funding cuts, which slowed scientific advances.                                          |
|   4 | Foundation Models process large amounts of unlabeled data and function like APIs that require history in each prompt to maintain context.               |
|   5 | Personalization options include training from scratch, fine-tuning, RAG, and prompt engineering, with RAG being cost-effective and high-quality.        |
|   6 | RAG (Retrieval Augmented Generation) involves retrieving relevant information, augmenting the prompt with context, and generating a response.           |
|   7 | Text-based RAG converts text into numerical embeddings stored in a vector database for semantic search.                                                 |
|   8 | Image-based RAG processes images into base64 strings, converts them to embeddings, and stores them in a vector database.                                |
|   9 | Video search combines image frame processing with audio transcription to create a unified vector database for multimodal retrieval.                     |
|  10 | Challenges in implementation include connecting diverse data sources, infrastructure management, and maintaining data privacy.                          |
|  11 | Amazon Bedrock was used as the primary service to access various foundation models and vector databases via API.                                        |
|  12 | The project code is available on GitHub, demonstrating text-to-text, text-to-image, and video search implementations.                                   |
|  13 | Democratization of information allows global access to knowledge, such as academic papers, regardless of geographic location.                           |
|  14 | Vector databases store numerical vectors rather than tabular data, enabling efficient similarity searches for AI models.                                |
|  15 | Response quality in the RAG system was verified manually using timestamps, with automation identified as a future improvement.                          |
|  16 | The team primarily used Amazon Bedrock and models like Amazon Titan, with open-source alternatives noted as a potential area for further investigation. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/09d6_hIzZIU/hqdefault.jpg)](https://www.youtube.com/watch?v=09d6_hIzZIU)

[Watch on YouTube](https://www.youtube.com/watch?v=09d6_hIzZIU)
