---
layout: default
title: "Descifrando emociones desde arte a memes - Maria Jose Molina Contreras"
nav_order: 52
parent: PyCon US 2025
type: Video Note
description: "The speaker introduces a multimodal system designed to decipher emotions from art and memes, addressing the common misconception that multimodality is exclusively tied to generative AI."
resource: "https://www.youtube.com/watch?v=-xNWHy6jtz0"
youtube_stats:
  view_count: 96
  like_count: 3
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

The speaker introduces a multimodal system designed to decipher emotions from art and memes, addressing the common misconception that multimodality is exclusively tied to generative AI.
She explains that while the world is perceived through complex, multi-sensory inputs, AI systems benefit from integrating different data types like images and text to better understand context and solve complex problems.
To build her project, she utilized pre-trained models—specifically EfficientNet for image feature extraction and DistilBERT for text processing—rather than training from scratch, due to dataset limitations and cultural representation challenges.
The core of the system employs cross-modal attention to create a bidirectional relationship between visual and textual data, allowing the model to associate specific image features with relevant text tokens.
Finally, she demonstrates how the system outputs emotion classifications using cosine similarity and explores the integration of a local LLM to generate descriptive text, noting the challenges of handling abstract concepts and cultural nuances in meme interpretation.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker introduces the final talk of the block, highlighting an upcoming team photo and a meet-and-greet event for Hispanic-speaking communities where merchandise will be raffle.          |
|   2 | María José Molina Contreras presents a talk on deciphering emotions from art to memes using a multimodal system of images and text.                                                             |
|   3 | The speaker notes that in tech meetups, conversations about multimodality often default to generative AI and LLMs, prompting an inquiry into what people actually understand by the term.       |
|   4 | A survey of the speaker's circle revealed that most associate multimodality with generative models, some with data types or architectures, and a minority admitted not knowing.                 |
|   5 | Multimodal systems are essential because the world is complex, involving multiple senses like sight, smell, and hearing, which the brain integrates to form conclusions.                        |
|   6 | Similar to human perception, AI systems benefit from interpreting different data types to gain better context and solve complex problems more effectively.                                      |
|   7 | Multimodal applications are widespread in healthcare for disease diagnosis, science for genomic data analysis, and commerce for search engines, often without users realizing it.               |
|   8 | Not all use cases require generative AI; non-generative systems offer advantages in efficiency, simpler hardware requirements, and lower deployment costs.                                      |
|   9 | Key challenges in multimodal systems include the complexity of managing diverse data types, high computational costs, data imbalance, and interpretability.                                     |
|  10 | The speaker developed a project to detect emotions in art images, motivated by the difficulty of understanding cultural nuances and memes across different backgrounds.                         |
|  11 | Instead of training a new model, the speaker opted for pre-trained models due to dataset limitations, such as a lack of cultural representation in the available art image libraries.           |
|  12 | The system uses a pre-trained EfficientNet model for image feature extraction, chosen for its optimized scaling and ease of use in PyTorch.                                                     |
|  13 | For text processing, the speaker utilized DistilBERT, a lightweight and efficient transformer model from Hugging Face, to extract features from artist descriptions associated with the images. |
|  14 | The architecture involves aligning image and text features to the same dimensions before applying multi-head attention for cross-modal integration.                                             |
|  15 | Cross-modal attention was selected over early or late fusion strategies because it creates a bidirectional relationship, allowing both image and text to inform each other.                     |
|  16 | The final output uses cosine similarity to match the processed features against a rule-based list of emotions, identifying the top three most likely emotions.                                  |
|  17 | An LLM was integrated as a post-processing step to generate descriptive text, though the speaker noted challenges with the model adding irrelevant information or well-wishes.                  |
|  18 | Testing the system on memes revealed difficulties in detecting abstract or ironic concepts, such as an "allergy to life," resulting in subjective emotion classifications like disgust.         |
|  19 | The speaker emphasizes that while the system provides useful insights, it remains subjective and requires careful prompt engineering to manage LLM outputs effectively.                         |
|  20 | All code, examples, and additional materials from the presentation are available in the speaker's GitHub repository for further exploration.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-xNWHy6jtz0/hqdefault.jpg)](https://www.youtube.com/watch?v=-xNWHy6jtz0)

[Watch on YouTube](https://www.youtube.com/watch?v=-xNWHy6jtz0)
