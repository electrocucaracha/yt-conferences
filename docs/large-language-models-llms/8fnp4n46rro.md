---
type: Video Note
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 8 - LLM Evaluation"
description: "In this lecture on LLM evaluation, the instructor emphasizes the importance of measuring large language model (LLM) performance to guide improvements. The session begins by recapping previous topics such as retrieval-augmented generation (R..."
resource: https://www.youtube.com/watch?v=8fNP4N46RRo
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture on LLM evaluation, the instructor emphasizes the importance of measuring large language model (LLM) performance to guide improvements.
The session begins by recapping previous topics such as retrieval-augmented generation (RAG), tool calling, and agentic workflows, before focusing on evaluation methods.
Human evaluation is discussed as the gold standard but is limited by subjectivity, cost, and scalability, leading to the use of inter-rater agreement metrics like Cohen’s kappa.
Rule-based metrics such as METEOR, BLEU, and ROUGE are introduced, though they struggle with stylistic variation and limited correlation with human judgment.
The lecture then presents "LLM as a judge," where another LLM evaluates outputs, providing both a score and rationale, but warns of biases like position, verbosity, and self-enhancement.
Best practices include using clear guidelines, binary scales, rationale-first prompting, and calibration with human ratings.
The lecture also covers evaluation dimensions (e.g., usefulness, factuality, safety), methods for factuality assessment, and common failure modes in agentic workflows.
Finally, it surveys benchmark types—knowledge, reasoning, coding, safety, and agentic benchmarks—highlighting their roles, limitations, and the importance of aligning evaluation with real-world needs and avoiding overfitting to benchmarks.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture 8 focuses on LLM evaluation, emphasizing the importance of measuring LLM performance.                                                                                                                                                                                |
|   2 | Recap of previous lecture: discussed LLMs interacting with external systems using RAG (retrieval augmented generation), candidate retrieval, reranking, tool calling, and agentic workflows (combining RAG and tool calling, e.g., AI-assisted coding with ReAct framework). |
|   3 | Evaluation can refer to output quality, coherence, factuality, latency, pricing, uptime, etc.; this lecture focuses on output quality.                                                                                                                                       |
|   4 | Human evaluation is ideal but costly and subjective; interrater agreement metrics (e.g., agreement rate, Cohen’s kappa, Fleiss’ kappa, Krippendorff’s alpha) are used to quantify consistency among raters.                                                                  |
|   5 | Limitations of human ratings: subjectivity, slowness, and expense.                                                                                                                                                                                                           |
|   6 | Rule-based metrics compare LLM outputs to fixed references; common metrics include METEOR, BLEU, and ROUGE, but they struggle with stylistic variation and have limited correlation with human ratings.                                                                      |
|   7 | LLM-as-a-judge: using an LLM to evaluate outputs by providing a rationale and a score; benefits include no need for reference texts or human ratings and interpretability via rationale.                                                                                     |
|   8 | Structured output and constrained decoding can enforce response formats (e.g., JSON).                                                                                                                                                                                        |
|   9 | Two main LLM-as-a-judge setups: single response evaluation and pairwise comparison.                                                                                                                                                                                          |
|  10 | Common biases in LLM-as-a-judge: position bias, verbosity bias, self-enhancement bias; remedies include prompt design, majority voting, using different models for generation and evaluation.                                                                                |
|  11 | Best practices: use clear guidelines, prefer binary scales, output rationale before score, calibrate LLM-judge scores with human ratings, use low temperature for reproducibility.                                                                                           |
|  12 | Evaluation dimensions: task performance (usefulness, factuality, relevance) and response format (tone, style, safety).                                                                                                                                                       |
|  13 | Factuality evaluation: decompose text into facts, check each fact (often binary), aggregate with possible weighting.                                                                                                                                                         |
|  14 | Agentic workflow evaluation: identify failu                                                                                                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8fNP4N46RRo)