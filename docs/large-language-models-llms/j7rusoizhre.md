---
type: Video Note
title: "Stanford CS224N: NLP w/ DL | Spring 2024 | Lecture 7 - Attention, Final Projects and LLM Intro"
description: "The lecture begins by discussing the evaluation of machine translation systems, highlighting the complexity of the task and the widespread use of the BLEU metric, which measures n-gram overlap between machine-generated and reference transla..."
resource: https://www.youtube.com/watch?v=J7ruSOIzhrE
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The lecture begins by discussing the evaluation of machine translation systems, highlighting the complexity of the task and the widespread use of the BLEU metric, which measures n-gram overlap between machine-generated and reference translations.
The instructor explains the limitations of BLEU, such as its inability to fully capture translation quality due to the diversity of valid translations and potential mismatches in word order.
The lecture then transitions to the concept of attention in neural networks, introduced to address the bottleneck of encoding entire source sentences into a single vector in sequence-to-sequence models.
Attention allows the model to focus on different parts of the input sentence during translation, improving performance and interpretability.
Various forms of attention, including dot product, multiplicative (bilinear), and additive (neural network-based), are described, with the dot product approach being most widely used in modern architectures like Transformers.
The session concludes with guidance on final projects, emphasizing the importance of originality, appropriate baselines, and practical considerations such as computing resources, and encourages students to critically engage with research literature and clearly define their project goals and evaluation methods.
# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Overview of machine translation evaluation, focusing on the BLEU measure as the most common automatic metric.                                                                                   |
|   2 | BLEU evaluates translations by comparing n-gram overlaps (typically up to 4-grams) between machine output and one or more human reference translations.                                         |
|   3 | BLEU includes a penalty for overly short translations to discourage omitting difficult content.                                                                                                 |
|   4 | Human evaluation remains the gold standard due to limitations and biases in automatic metrics.                                                                                                  |
|   5 | Statistical phrase-based machine translation dominated until progress stalled; syntax-based approaches were tried but offered limited improvement.                                              |
|   6 | Neural machine translation (NMT) introduced in 2014-2015, rapidly surpassed previous methods, with BLEU scores reaching 50s and 60s.                                                            |
|   7 | Attention mechanism introduced in 2014 as a key innovation in NMT, allowing models to focus on relevant parts of the source sentence during translation.                                        |
|   8 | Attention addresses the bottleneck of encoding all source information into a single vector and provides interpretability by showing alignment between source and target words.                  |
|   9 | Basic attention computes scores via dot product between encoder and decoder hidden states; more advanced forms include multiplicative (bilinear) and additive (neural network-based) attention. |
|  10 | Transformers use a projected dot product attention in a lower-dimensional space.                                                                                                                |
|  11 | Attention is now a general technique used in many neural architectures beyond translation.                                                                                                      |
|  12 | In RNN-based attention, explicit positional information is generally unnecessary due to sequential encoding.                                                                                    |
|  13 | Final project details: 49% of grade, teams of 1-3, can choose default (BERT-based) or custom projects.                                                                                          |
|  14 | Projects must involve both human language and neural networks.                                                                                                                                  |
|  15 | Emphasis on documenting external code, providing value-add, and including ethical considerations.                                                                                               |
|  16 | Computing resources are limited; students encouraged to use cloud credits, Colab, Kaggle, and Together AI API.                                                                                  |
|  17 | Project proposal requires a critical review of a research                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=J7ruSOIzhrE)