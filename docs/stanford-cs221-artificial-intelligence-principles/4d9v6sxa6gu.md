---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 14: Bayesian Networks and Learning"
nav_order: 5
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  The lecture reviews Bayesian networks, which define joint probability
  distributions over sets of variables using directed acyclic graphs, with each node
  representing a random variable and associated local conditional distributions. It
  cover...
resource: https://www.youtube.com/watch?v=4d9V6Sxa6gU
tags:
  - stanford-cs221-artificial-intelligence-principles
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The lecture reviews Bayesian networks, which define joint probability distributions over sets of variables using directed acyclic graphs, with each node representing a random variable and associated local conditional distributions.
It covers probabilistic inference methods, including exact inference, rejection sampling, and Gibbs sampling, and explains conditional independence using graphical criteria.
The main focus is on learning the parameters of Bayesian networks from fully observed data by counting occurrences of variable assignments and normalizing to estimate probabilities, with examples scaling from simple to more complex networks and introducing parameter sharing to reduce the number of parameters.
The lecture also discusses maximum likelihood estimation as the underlying principle for parameter learning, Laplace smoothing to address overfitting with limited data, and the expectation-maximization (EM) algorithm for handling partially observed data by iteratively estimating hidden variables and updating parameters.
The session concludes by emphasizing the importance of parameter sharing, smoothing, and EM in practical Bayesian network learning, and previews a shift to logic-based reasoning in future lectures.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Reviewed Bayesian networks as a way to define joint distributions over variables using directed acyclic graphs.                                                  |
|   2 | Each node has a local conditional distribution given its parents; multiply these to get the joint distribution.                                                  |
|   3 | Probabilistic inference involves querying the network, e.g., computing the probability of a burglary given the alarm.                                            |
|   4 | Discussed exact inference (marginalization and normalization), rejection sampling, and Gibbs sampling as inference algorithms.                                   |
|   5 | Conditional independence: Two variables are conditionally independent given a third if all paths between them are blocked according to specific graphical rules. |
|   6 | Independence can be determined by analyzing the network structure and conditioning on certain variables.                                                         |
|   7 | Learning Bayesian network parameters from data involves counting occurrences and normalizing to estimate probabilities.                                          |
|   8 | In fully observed settings, each example provides assignments to all variables; parameters are the local conditional distributions.                              |
|   9 | For one variable: count occurrences of each value and normalize.                                                                                                 |
|  10 | For two variables: count occurrences of each value and each conditional pair, then normalize.                                                                    |
|  11 | For three or more variables: count occurrences for each local conditional distribution, considering parent assignments.                                          |
|  12 | Parameter sharing allows multiple nodes to use the same conditional distribution, reducing the number of parameters.                                             |
|  13 | Hidden Markov Models (HMMs) use parameter sharing for transitions and emissions across time steps.                                                               |
|  14 | General estimation procedure: for each parameter, count occurrences of each configuration and normalize.                                                         |
|  15 | Maximum likelihood estimation (MLE): count and normalize is the closed-form solution for fully observed data.                                                    |
|  16 | Laplace (additive) smoothing: add pseudo-counts to avoid zero probabilities and reduce overfitting.                                                              |
|  17 | Expectation Maximization (EM) handles partially observed data by iteratively estimating missing values and updating parameters.                                  |
|  18 | EM alternates between estimating hidden                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4d9V6Sxa6gU)
