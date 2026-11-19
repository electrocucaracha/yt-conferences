---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 6 - LLM Reasoning"
nav_order: 6
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "Lecture 6 of CME295 introduces LLM reasoning models, which enhance standard language models by generating explicit multi-step reasoning chains before providing final answers to complex problems in ..."
resource: "https://www.youtube.com/watch?v=k5Fh-UgTuCo"
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

Lecture 6 of CME295 introduces LLM reasoning models, which enhance standard language models by generating explicit multi-step reasoning chains before providing final answers to complex problems in math and coding.
The lecture reviews the foundational training pipeline of pre-training, supervised fine-tuning (SFT), and preference tuning, highlighting that while vanilla LLMs excel at text generation, they often lack robust reasoning capabilities and rely on static knowledge.
To address these limitations, the course explains that reasoning models are primarily trained using Reinforcement Learning (RL) with verifiable rewards, such as passing code tests or matching mathematical ground truths, rather than relying solely on human-written reasoning data.
A key algorithm discussed is Group Relative Policy Optimization (GRPO), which differs from Proximal Policy Optimization (PPO) by eliminating the need for a separate value function and instead calculating advantages by comparing the rewards of multiple sampled completions for the same prompt.
The lecture also covers recent extensions to GRPO, such as Dr.
GRPO, which corrects length bias in the loss function to prevent models from generating unnecessarily long responses, and concludes with an analysis of DeepSeek’s R1 pipeline, which combines cold-start SFT, multi-stage RL with formatting and consistency rewards, and knowledge distillation to create efficient, high-performing reasoning models.

# Main Points

|   # | Main point                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture six covers LLM reasoning, building on preference tuning and reinforcement learning foundations from previous lectures.                                                                        |
|   2 | Vanilla LLMs have strengths in code and text generation but suffer from limited reasoning, static knowledge cutoffs, inability to take actions, and difficulty in evaluation.                         |
|   3 | Reasoning is defined as the ability to solve problems through multi-step processes, distinct from simple knowledge retrieval.                                                                         |
|   4 | Reasoning models output a chain of thought before the final answer, leveraging chain-of-thought techniques to decompose complex problems into tractable steps.                                        |
|   5 | The timeline of reasoning models began with OpenAI's o1 preview in September 2024, followed by releases from Google, DeepSeek, and other labs in late 2024 and early 2025.                            |
|   6 | Users are charged for reasoning tokens in addition to output tokens, creating an incentive for models to be efficient in their reasoning length.                                                      |
|   7 | Benchmarks for reasoning include coding tasks like HumanEval and Codeforces, and math tasks like AIME and GSM8K, verified by test cases or ground truth answers.                                      |
|   8 | The pass@k metric estimates the probability that at least one of k attempts succeeds, calculated using sampling without replacement to reduce variance.                                               |
|   9 | Temperature settings influence the diversity of generated solutions; moderate temperatures are typically optimal for balancing quality and diversity in pass@k evaluations.                           |
|  10 | Reinforcement learning is preferred over supervised fine-tuning for training reasoning models because it uses verifiable rewards and avoids the need for high-quality human-written reasoning chains. |
|  11 | GRPO (Group Relative Policy Optimization) is the primary algorithm for reasoning training, differing from PPO by computing advantages based on group rewards rather than a value function.            |
|  12 | GRPO eliminates the need for a separate value model, reducing computational overhead by comparing each completion's reward against the average reward of the group.                                   |
|  13 | A known issue in GRPO is that dividing by output length incentivizes longer responses, as tokens in shorter outputs receive higher weights, leading to increased response length over time.           |
|  14 | Recent modifications like Dr. GRPO and DPO address length bias by equalizing token contributions or removing length normalization to prevent unnecessary verbosity.                                   |
|  15 | DeepSeek's R1-Zero demonstrated that RL with verifiable rewards can improve reasoning performance without prior supervised fine-tuning, though it suffered from language mixing and syntax issues.    |
|  16 | The full DeepSeek R1 pipeline includes a cold-start SFT stage with human-rewritten data, followed by RL with formatting and language consistency rewards.                                             |
|  17 | R1 training involves a second SFT stage mixing reasoning and non-reasoning data, using rejection sampling to ensure high-quality reasoning examples.                                                  |
|  18 | The final stage of R1 training aligns the model for helpfulness and harmlessness, applying rewards to both the reasoning chain and the final answer.                                                  |
|  19 | Distillation allows smaller models to acquire reasoning capabilities by training on the full sequences generated by a larger teacher model, which is more efficient than training from scratch.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/k5Fh-UgTuCo/hqdefault.jpg)](https://www.youtube.com/watch?v=k5Fh-UgTuCo)

[Watch on YouTube](https://www.youtube.com/watch?v=k5Fh-UgTuCo)
