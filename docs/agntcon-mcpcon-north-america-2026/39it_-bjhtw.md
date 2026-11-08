---
layout: default
title: "Counting Tokens Before They Hatch: Predicting Agent Costs Before... - Kirah Sapong, Together AI"
nav_order: 3
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Kira Sapon, founder of Supermodel Labs, presents a method for predicting Large Language Model (LLM) output token sizes prior to generation to help manage agent costs."
resource: "https://www.youtube.com/watch?v=39It_-bjhtw"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Kira Sapon, founder of Supermodel Labs, presents a method for predicting Large Language Model (LLM) output token sizes prior to generation to help manage agent costs.
She explains that while input length is a poor predictor of response size, semantic embeddings derived from the prompt provide significantly better predictive signals by capturing meaning and context.
Using a regression model trained on the Zephyr 7B dataset, her research demonstrates that embeddings allow for rough estimates of output size, with half of predictions falling within 30% of the actual token count, though accuracy decreases for very short or very long responses.
Sapon highlights that agents consume vastly more tokens than chatbots due to looping and retrying, making pre-generation cost estimation crucial for budgeting and task planning.
She concludes by suggesting future improvements, such as developing universal predictors that generalize across different model families and exploring range-based estimates to better account for the inherent variability in open-ended versus closed-ended queries.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , founder of Supermodel Labs, presented research on predicting LLM agent token costs before generation to help teams reduce expenses in hybrid environments.                  |
|   2 | ; the goal was to train a model to replicate this intuition using only the prompt.                                                                                            |
|   3 | : Tokens (approx. 0.75 words), Embeddings (semantic numerical representations of content), and Regression (predicting continuous numerical values).                           |
|   4 | (e.g., 42x more for a trip planning task) due to looping and retrying, making cost a primary constraint rather than speed.                                                    |
|   5 | ,246 prompt-response pairs to train a regression model targeting output token counts.                                                                                         |
|   6 | : input length only, embeddings only, and a combination of both.                                                                                                              |
|   7 | , as similar-length prompts can yield vastly different response lengths.                                                                                                      |
|   8 | , improving Spearman rank correlation closer to +1.                                                                                                                           |
|   9 | , approximately 50% of predictions fell within 30% of actual output sizes, and two-thirds fell within 50%.                                                                    |
|  10 | : it underestimated very long outputs (>1,000 tokens) and overestimated very short outputs (<100 tokens).                                                                     |
|  11 | (e.g., "Tell me about AI") resulted in higher prediction errors, while factual or specific prompts (e.g., "Write a Python trie") yielded more accurate estimates.             |
|  12 | , but a proposed workflow involves routing steps to models based on capability and remaining budget.                                                                          |
|  13 | , exploring alternative model structures (e.g., transformers), and adding features like tool calls and hyperparameters.                                                       |
|  14 | , acknowledging that estimates will always have some margin of error.                                                                                                         |
|  15 | &A highlighted potential for using embeddings to predict tool calls and suggested estimating output as a range rather than a single number to better account for variability. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/39It_-bjhtw/hqdefault.jpg)]("https://www.youtube.com/watch?v=39It_-bjhtw")

[Watch on YouTube](https://www.youtube.com/watch?v=39It_-bjhtw)
