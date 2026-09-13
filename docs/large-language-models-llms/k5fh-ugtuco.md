---
type: Video Note
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 6 - LLM Reasoning"
description: "In this lecture, the instructor introduces the concept of reasoning in large language models (LLMs), highlighting its recent emergence and importance. The session begins by reviewing previous lectures on pre-training, fine-tuning, and prefe..."
resource: https://www.youtube.com/watch?v=k5Fh-UgTuCo
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture, the instructor introduces the concept of reasoning in large language models (LLMs), highlighting its recent emergence and importance.
The session begins by reviewing previous lectures on pre-training, fine-tuning, and preference alignment, then transitions to the limitations of "vanilla" LLMs, such as their struggles with multi-step reasoning, static knowledge, lack of action capabilities, and evaluation challenges.
The core of the lecture defines reasoning as the ability to solve complex, often multi-step problems—especially in math and coding—by decomposing them into tractable steps, a process encouraged by techniques like chain-of-thought prompting.
The instructor discusses benchmarks and metrics for evaluating reasoning, such as pass@k, and explains how reinforcement learning (RL), particularly with verifiable rewards, is used to train reasoning models when high-quality reasoning chains are unavailable.
The lecture details the GRPO (Group Relative Policy Optimization) algorithm, which improves upon previous RL methods by comparing multiple completions for the same prompt to compute advantages without needing a value function, and addresses technical challenges like output length inflation and token weighting.
The session concludes with a case study of DeepSeek's R1 model, outlining its multi-stage training pipeline—including pre-training, RL with verifiable and formatting rewards, SFT with curated data, and distillation for smaller models—and demonstrates how these methods yield competitive reasoning performance compared to closed-source alternatives.
# Main Points

|   # | Main point                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture covers LLM reasoning, building on preference tuning from previous lecture.                                                                                                                                           |
|   2 | Recap of model training steps: pre-training (learning structure of text/code), finetuning (making model useful for tasks like question answering), and preference tuning (aligning with human preferences using RHF and RL). |
|   3 | RL setup for LLMs: LLM as agent, environment as token prediction, action as next token, reward from human preferences.                                                                                                       |
|   4 | Loss function in RL stage: advantage maximization (based on rewards), and regularization to prevent model from deviating too much from previous or base (SFT) model.                                                         |
|   5 | PPO and PPO-clip: methods to limit policy updates; PPO-KL penalty uses KL divergence to penalize large changes.                                                                                                              |
|   6 | Vanilla LLMs strengths: strong at text/code generation; weaknesses: limited reasoning, static knowledge, inability to take actions, hard to evaluate outputs.                                                                |
|   7 | Reasoning defined as multi-step problem solving (e.g., math/coding problems), requiring decomposition into steps.                                                                                                            |
|   8 | Chain-of-thought: prompting model to explain reasoning in steps before answering.                                                                                                                                            |
|   9 | Reasoning models output both reasoning chain and answer.                                                                                                                                                                     |
|  10 | Recent timeline: OpenAI’s 01 preview (Sept 2024), Google Gemini 2.0, DeepSeek R1 (Jan 2025), and others.                                                                                                                     |
|  11 | Benchmarks for reasoning: coding (HumanEval, Codeforces, SWBench), math (AIME, GSM8K), using metrics like pass@k (probability at least one of k attempts is correct).                                                        |
|  12 | Pass@k estimation involves sampling multiple outputs and calculating probability at least one is correct.                                                                                                                    |
|  13 | Temperature affects diversity and quality of generated answers; optimal temperature balances both.                                                                                                                           |
|  14 | RL is used to train reasoning models, leveraging verifiable rewards (e.g., passing test cases, correct math answers).                                                                                                        |
|  15 | Challenges: controlling amount of reasoning, context window limitations, incentivizing efficient reasoning.                                                                                                                  |
|  16 | GRPO (Group Relative Policy Optimization): RL algorithm for reasoning models; computes advantage by comparing reward of a completion to group average, no v                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=k5Fh-UgTuCo)