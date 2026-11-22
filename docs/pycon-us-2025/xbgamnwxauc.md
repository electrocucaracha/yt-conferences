---
layout: default
title: "Transformando Gafas en Asistentes Inteligentes: Open Source Vision Language Models"
nav_order: 23
parent: PyCon US 2025
type: Video Note
description: "Alejandro Núñez Arroyo, an AI researcher and mechatronics engineer, presents a method for building custom smart glasses that function as personal AI assistants using open-source Vision Language Mod..."
resource: "https://www.youtube.com/watch?v=xbGAmNwxaUc"
youtube_stats:
  view_count: 274
  like_count: 5
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

Alejandro Núñez Arroyo, an AI researcher and mechatronics engineer, presents a method for building custom smart glasses that function as personal AI assistants using open-source Vision Language Models (VLMs).
He argues that relying on closed-source models often fails to capture specific cultural nuances and local data contexts, whereas open models allow users to maintain ownership of their data and customize the technology to their specific needs.
The proposed system utilizes an affordable ESP32-CAM module to capture images, which are then processed by a quantized VLM, such as PaliGemma, running locally on a standard GPU or even a Raspberry Pi.
By converting image patches and text prompts into a shared token space, the model can perform tasks like object detection, segmentation, and contextual description without sending data to the cloud.
Through live demonstrations comparing open-source models with closed alternatives like ChatGPT, the speaker highlights that smaller, locally hosted models can provide precise, culturally relevant responses while ensuring privacy and reducing dependency on external infrastructure.

# Main Points

|   # | Main point                                                                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Alejandro Núñez Arroyo, an AI researcher at Fox, presented a method to build smart glasses using open-source Vision Language Models (VLMs) to create personalized assistants.                                         |
|   2 | The project aims to allow users to own their data and adapt AI tools to specific cultural and contextual needs, addressing limitations of closed models that may not capture local nuances.                           |
|   3 | The system utilizes the SP32 Cam module, which costs under $20, to capture images that are processed by VLMs like PaliGemma to generate text descriptions or answers.                                                 |
|   4 | Multimodal AI combines different data types, such as images and text, allowing models to interpret visual information and respond with text, unlike single-domain NLP or computer vision models.                      |
|   5 | Open-source models offer transparency in training data, customizable architecture for specific hardware constraints, and lower long-term costs compared to closed APIs, though they require local GPU infrastructure. |
|   6 | The technical pipeline involves preprocessing images into patches and converting text into tokens, which are then combined in a shared space for the LLM to process and generate output.                              |
|   7 | Quantization techniques, such as reducing model precision to 4 bits, enable models with billions of parameters to run on modest hardware, such as a 4 GB Nvidia GPU or even a Raspberry Pi.                           |
|   8 | The implementation uses the Transformers library, requiring less than 20 lines of code to load the model, define the processor, and execute inference with image and text inputs.                                     |
|   9 | In a live comparison, the open-source model often provided more precise and preferred responses than a closed model like ChatGPT for specific visual tasks, such as reading signs or identifying objects.             |
|  10 | Future developments include integrating the camera with a server to store and analyze time-series images, allowing users to query their own visual history while maintaining full ownership of the data.              |
|  11 | The speaker highlighted the growing trend of smaller, efficient multimodal models that deliver high performance without requiring massive computational resources, making local AI deployment more accessible.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xbGAmNwxaUc/hqdefault.jpg)](https://www.youtube.com/watch?v=xbGAmNwxaUc)

[Watch on YouTube](https://www.youtube.com/watch?v=xbGAmNwxaUc)
