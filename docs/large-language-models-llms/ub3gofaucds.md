---
layout: default
title: Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 1 - Transformer
nav_order: 1
parent: Large Language Models Llms
type: Video Note
description:
  The transcript is from the introductory lecture of CME 295, a Stanford
  course on transformers and large language models (LLMs), taught by twin brothers
  Afin and Shervin, who have backgrounds in machine learning and industry experience
  at co...
resource: https://www.youtube.com/watch?v=Ub3GoFaUcds
tags:
  - large-language-models-llms
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The transcript is from the introductory lecture of CME 295, a Stanford course on transformers and large language models (LLMs), taught by twin brothers Afin and Shervin, who have backgrounds in machine learning and industry experience at companies like Uber, Google, and Netflix.
The instructors explain the course's goals: to teach the foundational mechanisms behind LLMs, particularly the transformer architecture, and to explore how these models are trained and applied.
They outline the course logistics, grading (midterm and final, no coding or homework), prerequisites (basic ML and linear algebra), and resources such as slides, recordings, a textbook, and a cheat sheet.
The lecture introduces key concepts in natural language processing (NLP), including classification, multi-classification, and generation tasks, and discusses tokenization methods (word, subword, character), word embeddings, and the evolution from RNNs and LSTMs to transformers.
The instructors detail the self-attention mechanism, the structure of the transformer model (encoder, decoder, multi-head attention), and training techniques like label smoothing, concluding with a step-by-step example of how transformers process and generate text.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Course: CME 295 Transformers and Large Language Models, taught by twin brothers Afin and Shervin.                                                         |
|   2 | Both instructors have backgrounds from Salbar (France), MIT, Stanford (ICME), Uber, Google, and Netflix, specializing in NLP and LLMs.                    |
|   3 | The class evolved from annual workshops (2021-2024) to a Stanford course, now in its second instance.                                                     |
|   4 | Course goals:                                                                                                                                             |
|   5 | Learn the underlying mechanisms of transformers and LLMs.                                                                                                 |
|   6 | Understand LLM training and applications.                                                                                                                 |
|   7 | Suitable for those interested in AI/LLMs for research, career, personal projects, or domain applications.                                                 |
|   8 | Prerequisites: Basic ML knowledge (model training, neural networks), linear algebra (matrix multiplication).                                              |
|   9 | Logistics:                                                                                                                                                |
|  10 | Fridays, 3:30–5:20pm; 2 units; letter or credit/no-credit.                                                                                                |
|  11 | Lectures recorded and posted online.                                                                                                                      |
|  12 | Grades: 50% midterm (Oct 24), 50% final (week of Dec 8); no homework.                                                                                     |
|  13 | Slides, recordings, syllabus, and textbook ("Super Study Guide Transformer LLMs") available on the site; VIP cheat sheet on GitHub in multiple languages. |
|  14 | Announcements via Canvas; questions via Canvas ED or email.                                                                                               |
|  15 | Exams focus on concepts, not coding.                                                                                                                      |
|  16 | NLP tasks categorized as:                                                                                                                                 |
|  17 | Classification (e.g., sentiment analysis, intent detection, language detection, topic modeling).                                                          |
|  18 | Multi-classification (e.g., named entity recognition, part-of-speech tagging, parsing).                                                                   |
|  19 | Generation (e.g., machine translation, question answering, summarization, code/poem generation).                                                          |
|  20 | Evaluation metrics: accuracy, precision, recall, F1 score, BLEU, ROUGE, perplexity.                                                                       |
|  21 | Tokenization methods: word-level, subword-level, character-level; trade-offs in OOV risk, sequence length, and computational cost.                        |
|  22 | Word representations: one-hot encoding (orthogonal, not ideal), learned embeddings (e.g., word2vec: CBOW, skip-gram).                                     |
|  23 | Embeddings learned via proxy tasks (e.g., predicting next word); size of embeddings is a trade-off.                                                       |
|  24 | RNNs and LSTMs capture sequence/order but suffer from vanishing gradients and slow computation.                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Ub3GoFaUcds)
