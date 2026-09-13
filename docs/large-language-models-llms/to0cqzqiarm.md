---
type: Video Note
title: "Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 11 - Benchmarking by Yann Dubois"
description: "In this lecture, Yan, a third-year PhD student, discusses the importance and challenges of benchmarking and evaluation in machine learning, particularly in natural language processing (NLP). He outlines the different stages of model develop..."
resource: https://www.youtube.com/watch?v=TO0CqzqiArM
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture, Yan, a third-year PhD student, discusses the importance and challenges of benchmarking and evaluation in machine learning, particularly in natural language processing (NLP).
He outlines the different stages of model development—training, development, model selection, and deployment—and emphasizes that each stage requires distinct evaluation metrics, balancing speed, cost, and quality.
Yan distinguishes between close-ended tasks, like classification and entailment, which use standard metrics such as accuracy and F1 score, and open-ended tasks, like summarization and instruction following, which require more complex evaluation methods including content overlap metrics (e.g., BLEU, ROUGE), embedding-based metrics, and increasingly, large language model (LLM)-based and human evaluations.
He highlights the limitations of both automatic and human evaluations, including issues of bias, reproducibility, and the influence of reference quality, and notes the growing use of LLMs like GPT-4 for scalable, consistent evaluation despite their own biases.
Yan also addresses broader challenges such as overfitting, contamination, monoculture in benchmarks (e.g., English-centric datasets), and the lack of incentives to adopt better metrics in academia.
He concludes by urging practitioners to critically examine outputs rather than relying solely on benchmark numbers, and to consider task-specific, robust evaluation strategies.
# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Benchmarking and evaluation are crucial for real-world machine learning and production deployment.                                                                                                 |
|   2 | Performance measurement is needed at every stage: training (loss optimization), development (hyperparameter tuning), model selection, deployment, and publishing.                                  |
|   3 | Different evaluation methods are required at different stages: fast and cheap for training/development, high-quality and trustworthy for deployment, reproducible and standardized for publishing. |
|   4 | Academic benchmarks drive progress; reproducibility and comparability over years are important.                                                                                                    |
|   5 | Two main NLP task types: close-ended (classification, entailment, NER, etc.) and open-ended (summarization, translation, instruction following).                                                   |
|   6 | Close-ended tasks use standard ML metrics: accuracy, precision, recall, F1, ROC, AUC.                                                                                                              |
|   7 | Aggregating metrics across tasks (e.g., SuperGLUE) is common but can be problematic due to metric incompatibility.                                                                                 |
|   8 | Beware of spurious correlations and label quality in benchmarks.                                                                                                                                   |
|   9 | Open-ended tasks are harder to evaluate; standard metrics include content overlap (BLEU, ROUGE), embedding-based (BERTScore), and model-based metrics (BLEURT).                                    |
|  10 | Content overlap metrics have limitations: don't capture semantics, can give false positives/negatives.                                                                                             |
|  11 | Embedding-based and model-based metrics improve semantic evaluation but depend on reference quality.                                                                                               |
|  12 | Reference-based evaluation is being replaced by reference-free methods, especially using LLMs (e.g., GPT-4) as evaluators.                                                                         |
|  13 | Human evaluation is the gold standard but is slow, expensive, inconsistent, and hard to reproduce.                                                                                                 |
|  14 | Human and LLM evaluators both show biases (e.g., preference for longer outputs, list formats, position effects, self-bias).                                                                        |
|  15 | Arena-style evaluation (side-by-side model comparisons, ELO ratings) is now common for LLMs.                                                                                                       |
|  16 | Current LLM evaluation uses perplexity, aggregate benchmarks (e.g., HELM, HuggingFace), and Arena-style comparisons.                                                                               |
|  17 | Challenges: consistency issues, contamination/overfitting, monoculture (English foc                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=TO0CqzqiArM)