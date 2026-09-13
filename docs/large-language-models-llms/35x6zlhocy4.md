---
type: Video Note
title: "Stanford CS224N: NLP with Deep Learning | Spring 2024 | Lecture 10 - Post-training by Archit Sharma"
description: "In this lecture, Archa Sharma, a Stanford PhD student, provides an overview of the post-training processes that transform large pre-trained language models into advanced systems like ChatGPT. She explains how the field has rapidly evolved..."
resource: https://www.youtube.com/watch?v=35X6zlhoCy4
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture, Archa Sharma, a Stanford PhD student, provides an overview of the post-training processes that transform large pre-trained language models into advanced systems like ChatGPT.
She explains how the field has rapidly evolved, with models now trained on trillions of tokens and requiring massive computational resources.
The lecture covers the journey from basic next-token prediction to more sophisticated capabilities through techniques such as zero-shot and few-shot prompting, instruction fine-tuning, and optimizing for human preferences using reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO).
Sharma highlights how scaling up models and data leads to emergent abilities like reasoning, code generation, and creative tasks, but also discusses the challenges of aligning models with user intent, the limitations of supervised fine-tuning, and the complexities of reward modeling.
She concludes by emphasizing the importance of careful data curation and optimization strategies in building models that are both powerful and responsive to human preferences, noting the ongoing progress and challenges in the field.
# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Archa Sharma, PhD student at Stanford, presents on post-training for large language models (LLMs).                                        |
|   2 | LLMs have grown rapidly in size and compute, now trained on over 15 trillion tokens (e.g., Llama 3).                                      |
|   3 | Pre-training teaches models knowledge, syntax, semantics, and some agent-like reasoning, not just text prediction.                        |
|   4 | LLMs can perform tasks like math, code generation, and medical Q&A, emerging as general-purpose assistants.                               |
|   5 | Zero-shot and few-shot in-context learning allow LLMs to perform tasks without explicit fine-tuning, by providing prompts or examples.    |
|   6 | GPT-2 and GPT-3 demonstrated strong zero-shot and few-shot capabilities, outperforming many task-specific models.                         |
|   7 | Chain-of-thought prompting improves multi-step reasoning by showing models how to reason step by step.                                    |
|   8 | Simple prompt engineering (e.g., "let's think step by step") can induce better reasoning in LLMs.                                         |
|   9 | Instruction fine-tuning aligns models with user intent by training on diverse instruction-output pairs across many tasks.                 |
|  10 | Larger models and more data improve instruction-following and task performance.                                                           |
|  11 | Evaluation of LLMs is challenging due to potential data leakage and benchmark limitations.                                                |
|  12 | Instruction fine-tuning is limited by the cost and quality of human-labeled data and struggles with open-ended or creative tasks.         |
|  13 | RLHF (Reinforcement Learning from Human Feedback) directly optimizes for human preferences using reward models trained on human rankings. |
|  14 | Reward models are trained using pairwise comparisons (ranking) rather than absolute scores for better consistency.                        |
|  15 | RLHF can lead to reward hacking if not regularized; KL-divergence penalties prevent models from drifting too far from initial behavior.   |
|  16 | RLHF is complex and resource-intensive; Direct Preference Optimization (DPO) offers a simpler, classification-based alternative.          |
|  17 | DPO achieves similar performance to RLHF and is widely used in open-source and production models (e.g., Llama 3, Mistral).                |
|  18 | RLHF and DPO improve model                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=35X6zlhoCy4)