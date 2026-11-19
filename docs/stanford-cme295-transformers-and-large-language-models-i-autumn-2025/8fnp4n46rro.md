---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 8 - LLM Evaluation"
nav_order: 8
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "Lecture 8 of CME295 focuses on LLM evaluation, emphasizing that quantifying performance is essential for identifying areas of improvement."
resource: "https://www.youtube.com/watch?v=8fNP4N46RRo"
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

Lecture 8 of CME295 focuses on LLM evaluation, emphasizing that quantifying performance is essential for identifying areas of improvement.
The lecture reviews previous concepts such as Retrieval-Augmented Generation (RAG), tool calling, and agentic workflows before defining evaluation primarily as the assessment of output quality rather than system metrics like latency.
It discusses the limitations of human rating, which is costly and subjective, and rule-based metrics like METEOR and BLEU, which often fail to capture stylistic variations and correlate poorly with human judgment.
Consequently, the lecture introduces "LLM as a Judge" as a scalable alternative that provides interpretable rationales, while addressing specific biases such as position, verbosity, and self-enhancement, and recommending best practices like using binary scales and low temperatures for reproducibility.
The session also details failure modes in agentic tool use, ranging from tool hallucinations to incorrect argument generation, and categorizes standard benchmarks into knowledge (MMLU), reasoning (AIME, PIQA), coding (SWE-bench), safety (HarmBench), and agent-specific tasks (TAO-bench).
Finally, it highlights the importance of avoiding data contamination and using benchmarks to characterize model profiles rather than as absolute measures of quality.

# Main Points

|   # | Main point                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The lecture focuses on LLM evaluation, emphasizing that quantifying performance is essential for identifying areas of improvement.                                                                                          |
|   2 | Previous topics included Retrieval Augmented Generation (RAG), tool calling, and agentic workflows using the ReAct framework.                                                                                               |
|   3 | Evaluation is defined here as quantifying output quality, distinct from system metrics like latency or pricing.                                                                                                             |
|   4 | Human rating is the ideal evaluation method but is impractical due to high costs, slow speed, and subjective inter-rater disagreement.                                                                                      |
|   5 | Inter-rater agreement metrics like Cohen's Kappa adjust for chance agreement to provide a more reliable measure of consistency among human raters.                                                                          |
|   6 | Rule-based metrics such as METEOR, BLEU, and ROUGE compare outputs to references but struggle with stylistic variations and have limited correlation with human judgment.                                                   |
|   7 | LLM-as-a-Judge uses a large language model to evaluate responses, offering benefits like no need for reference texts and the ability to provide explanatory rationales.                                                     |
|   8 | Structured outputs or constrained decoding are used to ensure LLM judges return parseable scores and rationales in a consistent format.                                                                                     |
|   9 | Common biases in LLM-as-a-Judge include position bias, verbosity bias, and self-enhancement bias, which can be mitigated by swapping positions, adjusting prompts, or using different models for generation and evaluation. |
|  10 | Best practices for LLM-as-a-Judge include using binary scales, outputting rationales before scores, calibrating against human ratings, and using low temperature for reproducibility.                                       |
|  11 | Factuality evaluation involves decomposing text into individual facts, verifying each against knowledge bases, and aggregating weighted scores to quantify overall accuracy.                                                |
|  12 | Agentic workflow evaluation requires analyzing failure modes in tool prediction, execution, and result synthesis, such as tool hallucination or incorrect argument usage.                                                   |
|  13 | Tool prediction errors can stem from tool router recall issues, weak model grounding, or unclear API definitions, requiring adjustments to prompts or model capabilities.                                                   |
|  14 | Tool execution failures often involve software bugs or lack of meaningful outputs, which can lead to false confirmations if the model does not receive clear status updates.                                                |
|  15 | Knowledge-based benchmarks like MMLU test factual recall across diverse domains using multiple-choice questions to standardize evaluation.                                                                                  |
|  16 | Reasoning benchmarks such as AIME and PIQA assess mathematical problem-solving and common-sense physical interaction understanding, respectively.                                                                           |
|  17 | Coding benchmarks like SWE-bench evaluate a model's ability to resolve GitHub issues by generating patches that pass existing tests.                                                                                        |
|  18 | Safety benchmarks like HarmBench assess harmful behavior, copyright infringement, and contextual risks, often using classifiers to distinguish between quality and safety failures.                                         |
|  19 | Agent-specific benchmarks like ToolBench simulate user interactions to test tool usage reliability, utilizing metrics like pass-hat-K to ensure consistent success across multiple attempts.                                |
|  20 | Benchmark results should be interpreted alongside cost and other factors to identify the Pareto frontier, while being mindful of data contamination and Goodhart's Law.                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8fNP4N46RRo/hqdefault.jpg)](https://www.youtube.com/watch?v=8fNP4N46RRo)

[Watch on YouTube](https://www.youtube.com/watch?v=8fNP4N46RRo)
