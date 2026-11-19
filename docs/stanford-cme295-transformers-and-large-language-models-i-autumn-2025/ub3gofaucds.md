---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 1 - Transformer"
nav_order: 1
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "In the introductory lecture for Stanford’s CME 295 course on Transformers and Large Language Models, instructors Afshin and Shirvin outline the curriculum’s focus on understanding the underlying me..."
resource: "https://www.youtube.com/watch?v=Ub3GoFaUcds"
tags:
  - stanford-cme295-transformers-and-large-language-models-i-autumn-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T20:43:47+00:00
---

# Summary

In the introductory lecture for Stanford’s CME 295 course on Transformers and Large Language Models, instructors Afshin and Shirvin outline the curriculum’s focus on understanding the underlying mechanisms of LLMs, their training processes, and practical applications.
The session begins with a high-level overview of Natural Language Processing (NLP) tasks, categorizing them into classification, multi-classification, and generation, while discussing appropriate evaluation metrics such as precision, recall, and BLEU.
The instructors then explain the foundational steps of text processing, including tokenization strategies like word, subword, and character-level splitting, and the evolution of token representations from one-hot encodings to learned embeddings via proxy tasks like word2vec.
They address the limitations of Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) models, specifically regarding vanishing gradients and sequential processing bottlenecks, which led to the development of the attention mechanism.
Finally, the lecture details the architecture of the Transformer model introduced in the 2017 paper "Attention Is All You Need," explaining how self-attention, multi-head attention, and the encoder-decoder structure enable efficient, parallelizable processing of text for tasks such as machine translation.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The course CME 295 covers Transformers and Large Language Models, taught by twin brothers with backgrounds in NLP and industry experience at Uber, Google, and Netflix.                     |
|   2 | The class aims to teach the underlying mechanisms of LLMs, specifically the Transformer architecture, and how these models are trained and applied.                                         |
|   3 | Prerequisites include basic machine learning concepts, neural networks, and linear algebra, such as matrix multiplication.                                                                  |
|   4 | The course meets every Friday from 3:30 to 5:20, is worth two units, and offers letter or credit/non-credit options.                                                                        |
|   5 | Grading consists of a 50% midterm exam on October 24 and a 50% final exam in the week of December 8, with no homework assignments.                                                          |
|   6 | Slides, recordings, and the syllabus are available on the course site, while announcements and questions are handled via Canvas and the Ed tab.                                             |
|   7 | NLP tasks are categorized into classification (e.g., sentiment analysis), multi-classification (e.g., named entity recognition), and generation (e.g., machine translation).                |
|   8 | Classification tasks are evaluated using metrics like accuracy, precision, recall, and F1 score to handle imbalanced datasets effectively.                                                  |
|   9 | Multi-classification tasks like NER are evaluated at the token or entity level rather than the sentence level.                                                                              |
|  10 | Generation tasks are evaluated using reference-based metrics like BLEU and ROUGE, or reference-free metrics like perplexity.                                                                |
|  11 | Tokenization involves splitting text into units called tokens, with methods including word-level, subword-level, and character-level approaches.                                            |
|  12 | Subword tokenization is preferred for balancing vocabulary size and handling out-of-vocabulary (OOV) tokens, while character-level is robust to misspellings but computationally expensive. |
|  13 | One-hot encoding is a naive token representation method that results in orthogonal vectors, limiting the ability to measure semantic similarity.                                            |
|  14 | Word embeddings like Word2vec use proxy tasks such as continuous bag of words or skip-gram to learn meaningful vector representations from context.                                         |
|  15 | Recurrent Neural Networks (RNNs) process text sequentially using hidden states to capture word order but suffer from vanishing gradients and slow training.                                 |
|  16 | Long Short-Term Memory (LSTM) networks improve upon RNNs by adding cell states to better handle long-range dependencies.                                                                    |
|  17 | The attention mechanism, introduced in 2014, allows models to focus on relevant parts of the input sequence, addressing long-range dependency issues.                                       |
|  18 | The Transformer architecture, introduced in 2017 in the paper "Attention Is All You Need," relies entirely on self-attention mechanisms.                                                    |
|  19 | Self-attention uses Query, Key, and Value projections to compute relationships between tokens, enabling parallel processing and efficient hardware utilization.                             |
|  20 | Multi-head attention performs multiple attention computations in parallel with different projection matrices to capture diverse relationships between tokens.                               |
|  21 | The Transformer encoder processes input text using self-attention and feed-forward layers to create context-aware representations.                                                          |
|  22 | The Transformer decoder generates output text using masked self-attention, cross-attention with encoder outputs, and feed-forward layers.                                                   |
|  23 | Positional encodings are added to token embeddings to provide information about the order of tokens in the sequence.                                                                        |
|  24 | Label smoothing is a technique used to improve model generalization by adjusting the target probability distribution during training.                                                       |
|  25 | The end-to-end process involves tokenization, embedding with positional encodings, encoding, and iterative decoding until an end-of-sequence token is generated.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Ub3GoFaUcds/hqdefault.jpg)](https://www.youtube.com/watch?v=Ub3GoFaUcds)

[Watch on YouTube](https://www.youtube.com/watch?v=Ub3GoFaUcds)
