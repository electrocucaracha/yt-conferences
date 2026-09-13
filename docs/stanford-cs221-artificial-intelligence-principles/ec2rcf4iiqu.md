---
type: Video Note
title: "Stanford CS221 | Autumn 2025 | Lecture 12: Bayesian Networks I"
description: "The lecture begins by reviewing key concepts in artificial intelligence, including perception, reasoning, action, and learning, and distinguishes between model-free and model-based approaches to decision-making. It then introduces Bayesian..."
resource: https://www.youtube.com/watch?v=ec2rCf4iIqU
tags: ["stanford-cs221-artificial-intelligence-principles", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The lecture begins by reviewing key concepts in artificial intelligence, including perception, reasoning, action, and learning, and distinguishes between model-free and model-based approaches to decision-making.
It then introduces Bayesian networks as a structured way to represent and reason about the state of the world under uncertainty, using probability theory and random variables.
The instructor explains fundamental operations such as marginalization and conditioning on probability tables, and demonstrates how joint distributions can be constructed and queried using Bayesian networks, illustrated with examples like the alarm problem and medical diagnosis.
The concept of "explaining away" is highlighted, showing how observing evidence can alter the dependencies between causes.
The lecture also introduces probabilistic programming as an alternative way to define Bayesian networks, and discusses rejection sampling as a method for approximate probabilistic inference, noting its simplicity but inefficiency for rare events.
The session concludes by emphasizing the interpretability, flexibility, and practical advantages of Bayesian networks for handling missing data, incorporating prior knowledge, and enabling causal reasoning, while previewing more efficient inference algorithms for future lectures.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Reviewed course topics: perception, reasoning, action, learning.                                                                                                                                                                                                         |
|   2 | Discussed model-free vs. model-based approaches in AI.                                                                                                                                                                                                                   |
|   3 | Model-free methods: direct, fast, less flexible (e.g., classification, Q-learning).                                                                                                                                                                                      |
|   4 | Model-based methods: require understanding world dynamics, more flexible, support planning.                                                                                                                                                                              |
|   5 | Introduced Bayesian networks as a way to represent and reason about the world under uncertainty.                                                                                                                                                                         |
|   6 | Explained random variables and joint probability distributions.                                                                                                                                                                                                          |
|   7 | Demonstrated marginalization (summing out variables) and conditioning (updating probabilities given evidence).                                                                                                                                                           |
|   8 | Probability tables represented as tensors; computations can use tensor operations.                                                                                                                                                                                       |
|   9 | Probabilistic inference: answering queries about variables given evidence, analogous to SQL queries on a database.                                                                                                                                                       |
|  10 | Introduced the "explaining away" phenomenon: observing an effect and one cause reduces the probability of other causes.                                                                                                                                                  |
|  11 | Outlined four-step procedure for constructing Bayesian networks: 1. Define random variables. 2. Connect variables with directed edges. 3. Specify local conditional probability tables for each variable. 4. Multiply local distributions to get the joint distribution. |
|  12 | Demonstrated Bayesian networks with alarm and medical diagnosis examples.                                                                                                                                                                                                |
|  13 | Highlighted difference between local conditional distributions (defined) and marginal/conditional distributions (derived).                                                                                                                                               |
|  14 | Showed probabilistic inference via marginalization and conditioning.                                                                                                                                                                                                     |
|  15 | Explained rejection sampling: sample from the joint, select samples matching evidence, estimate probabilities.                                                                                                                                                           |
|  16 | Probabilistic programming: representing Bayesian networks as programs that generate samples.                                                                                                                                                                             |
|  17 | Bayesian networks handle missing data, incorporate prior knowledge, provide interpretability, and support causal reasoning.                                                                                                                                              |
|  18 | Summary: Bayesian networks offer a structured way to define joint distributions and perform probabilistic inference; rejection sampling is a simple but inefficient inference method.                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ec2rCf4iIqU)