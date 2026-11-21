---
layout: default
title: "Running Large Language Models on Laptops... - Aayush Kumar JVS"
nav_order: 60
parent: PyCon US 2026
type: Video Note
description: "At PyCon US, Ayush Kumar presented a talk on practical quantization techniques for running large language models (LLMs) on laptops, building upon his master’s thesis research."
resource: "https://www.youtube.com/watch?v=CynFICT4BXk"
youtube_stats:
  view_count: 355
  like_count: 9
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

At PyCon US, Ayush Kumar presented a talk on practical quantization techniques for running large language models (LLMs) on laptops, building upon his master’s thesis research.
He explained that quantization reduces the memory footprint of model weights and activations, enabling the execution of massive models like Llama 4 on consumer hardware without requiring high-end GPUs such as Nvidia A100s.
Kumar detailed various methods, including QLoRA, K-means clustering, and the GGUF format, while emphasizing the critical trade-off between reduced bit precision and model accuracy, measured by perplexity.
He highlighted that context length often consumes more memory than the model weights themselves, necessitating careful calculation of VRAM requirements for specific use cases.
In response to audience questions, Kumar recommended 8-bit quantization as a "sweet spot" for balancing performance and accuracy, noting that models like Llama generally respond better to quantization than others like Gemma or Qwen.
The session concluded by reinforcing the accessibility of open-source quantized models available on platforms like Hugging Face, allowing developers to deploy efficient AI solutions locally.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Nvidia and Anaconda sponsored the PyCon AI track, offering resources like Spark DGX and local inference models. |
|   2 | Quantization reduces model weight and activation precision to lower memory footprint and enable LLMs on laptops. |
|   3 | QLoRA, developed by Tim Dettmers, uses quantization to facilitate lower-rank adaptations for efficient model training. |
|   4 | K-bit quantization utilizes K-means clustering to group weights, preserving relationships and minimizing error in critical components. |
|   5 | Different quantization levels (S, M, L, XL) compress varying degrees of model layers, trading off accuracy for size. |
|   6 | Lower bit quantization, such as 2-bit, significantly degrades image and text quality compared to 16-bit or 8-bit versions. |
|   7 | Major AI companies release LLMs, and open-source developers provide quantized versions on platforms like Hugging Face. |
|   8 | GGUF and GGML are unified formats created by Georgi Gerganov for running quantized LLMs efficiently on local hardware. |
|   9 | Bits and Bytes is a Python library supporting 8-bit block-wise quantization, easily installed via pip. |
|  10 | Popular quantized models are provided by researchers like Unsloth, Tim Dobbins, and Butowski for free access. |
|  11 | Perplexity measures model confidence and error; high perplexity indicates poor performance and confusion. |
|  12 | Choosing the right quantization depends on model size, use case, and the balance between accuracy and memory constraints. |
|  13 | Context length is often more critical than model weights for memory usage, requiring careful calculation of KV cache size. |
|  14 | VRAM requirements can be calculated using parameter count, bits per weight, and context length to determine feasibility. |
|  15 | Quantized LLMs are accessible via applications like LLaMA CPP, LM Studio, Ollama, and Local AI. |
|  16 | The speaker’s thesis applied quantization techniques to mental health datasets, evaluating accuracy and memory trade-offs. |
|  17 | Quantization-aware training (AWQ) is preferred by the speaker as it quantizes weights during training for better stability. |
|  18 | 8-bit quantization was identified as the sweet spot for balancing memory savings and high accuracy in the speaker’s research. |
|  19 | Models like LLaMA performed better under quantization compared to Gemma and Qwen, which showed higher perplexity. |
|  20 | Sequential training of multiple LLMs allows researchers to compare memory footprint and accuracy across different models. |
|  21 | The open-source community has made it easier for developers to run large models locally without specialized hardware. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CynFICT4BXk/hqdefault.jpg)](https://www.youtube.com/watch?v=CynFICT4BXk)

[Watch on YouTube](https://www.youtube.com/watch?v=CynFICT4BXk)
