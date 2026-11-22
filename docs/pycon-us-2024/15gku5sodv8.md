---
layout: default
title: "Sponsor Presentations - Snowflake's AI research: A look inside our generative AI innovations"
nav_order: 38
parent: PyCon US 2024
type: Video Note
description: 'Yousef, a principal software engineer at Snowflake, presents the development of Arctic, a large language model open-sourced under an Apache 2.0 license that is specifically optimized for "Enterpris...'
resource: "https://www.youtube.com/watch?v=15GKU5SODv8"
youtube_stats:
  view_count: 378
  like_count: 3
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

Yousef, a principal software engineer at Snowflake, presents the development of Arctic, a large language model open-sourced under an Apache 2.0 license that is specifically optimized for "Enterprise intelligence," a combination of SQL generation, coding, and instruction following skills.
The model utilizes a hybrid Mixture of Experts (MoE) architecture with 480 billion total parameters but only 17 billion active parameters, enabling high token efficiency during both training and inference.
To achieve this performance, the team co-designed the system and architecture, utilizing custom kernels and advanced parallelism strategies like expert parallelism to manage communication overhead, resulting in a highly efficient training process that required only 3,000 GPU hours on H100 nodes.
The training data was carefully curated through extensive ablation studies, leveraging high-quality web datasets like RefinedWeb and Common Crawl, alongside specialized enterprise-focused data for coding and SQL, while employing techniques such as topological sorting for code dependencies and MinHash for deduplication.
Arctic is available through various platforms including Snowflake Cortex, Hugging Face, and NVIDIA’s TensorRT-LLM, with the team continuing to share insights through a series of blog posts and contributing to open-source libraries like DeepSpeed and vLLM.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yousef, a principal software engineer at Snowflake, presented the development of Arctic, a large language model open-sourced under the Apache 2 license.                |
|   2 | The model is optimized for "Enterprise intelligence," focusing on SQL generation, coding, and instruction following to meet specific customer needs.                    |
|   3 | Arctic is a mixture-of-experts model with 480 billion total parameters and 17 billion active parameters, achieving high token efficiency during training and inference. |
|   4 | The team used 3,000 GPU hours on H100 nodes and 3.5 trillion tokens to train the model, leveraging co-designed system and architecture optimizations.                   |
|   5 | Pre-training data included web data from RefinedWeb and Common Crawl, coding data from StarCoder and GitHub, and STEM content from OpenWebMath.                         |
|   6 | Data quality was ensured by using RefinedWeb as a high-quality reference set and filtering Common Crawl dumps using KLM perplexity scores and other signals.            |
|   7 | The team discovered that older Common Crawl dumps often yielded higher quality data than recent ones, potentially due to increased web blocking in recent years.        |
|   8 | Coding data was processed by topologically sorting files based on dependencies to improve the model's understanding of code structure.                                  |
|   9 | The model architecture combines a dense Transformer branch with a mixture-of-experts branch in every layer to reduce communication overhead.                            |
|  10 | Training utilized DeepSpeed with ZeRO stage 2 for the dense branch and expert parallelism for the MoE branch to distribute experts across devices.                      |
|  11 | Custom kernels were written for sparse operations, including token routing, load balancing, and data scattering/gathering among experts.                                |
|  12 | Fine-tuning used approximately 1.5 million examples, with a focus on general knowledge, coding, math, and identity questions.                                           |
|  13 | To address expert stability in fine-tuning, multiple examples were packed into single sequences to ensure each expert receives sufficient tokens.                       |
|  14 | The model is available through Snowflake Cortex, Hugging Face, vLLM, DeepSpeed, and NVIDIA TensorRT-LLM.                                                                |
|  15 | A Streamlit chatbot application was built using the Replicate API to allow users to interact with Arctic and test its capabilities.                                     |
|  16 | Safety measures were implemented using Meta's Llama Guard model to classify and filter harmful inputs and outputs.                                                      |
|  17 | The team published a series of blog posts, referred to as a "cookbook," detailing insights on data preparation, architecture, and training optimizations.               |
|  18 | Future work includes optimizing multi-node inference for larger MoE models and collaborating with partners on fine-tuning specific skill sets.                          |
|  19 | The development process involved a team of roughly 20 people and emphasized the importance of sharing research insights to support the open-source community.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/15GKU5SODv8/hqdefault.jpg)](https://www.youtube.com/watch?v=15GKU5SODv8)

[Watch on YouTube](https://www.youtube.com/watch?v=15GKU5SODv8)
