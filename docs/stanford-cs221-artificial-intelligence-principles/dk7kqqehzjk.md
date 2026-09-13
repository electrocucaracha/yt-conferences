---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 13: Bayesian Networks and Gibbs Sampling"
nav_order: 4
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  The lecture continues the discussion on Bayesian networks, focusing on
  representing uncertainty and performing probabilistic inference. After reviewing
  the structure of Bayesian networks—defining variables, constructing a dependency
  graph...
resource: https://www.youtube.com/watch?v=Dk7Kqqehzjk
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

The lecture continues the discussion on Bayesian networks, focusing on representing uncertainty and performing probabilistic inference.
After reviewing the structure of Bayesian networks—defining variables, constructing a dependency graph, and specifying local conditional probability tables—the instructor explains how to compute joint and conditional probabilities, using the alarm example with burglary and earthquake as causes.
The lecture contrasts exact inference, which is computationally expensive for large networks, with approximate methods like rejection sampling and Gibbs sampling.
Rejection sampling is simple but inefficient when evidence is rare, while Gibbs sampling incrementally updates variables to always satisfy evidence, making it more efficient in some cases but less effective when variables are highly correlated.
The concept of the Markov blanket is introduced to optimize Gibbs sampling by focusing only on relevant variables.
The lecture concludes with an introduction to conditional independence in Bayesian networks, showing how the network’s graph structure can reveal when variables are independent or conditionally independent, and outlines a graphical procedure for determining these relationships.
Next, the course will address learning the parameters of Bayesian networks.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Reviewed Bayesian networks as a way to represent uncertainties in the world.                                                                             |
|   2 | Bayesian networks defined through four steps: identify variables, define a graph, specify local conditional distributions, and use probability tables.   |
|   3 | Joint distribution is the product of all local conditional distributions.                                                                                |
|   4 | Probabilistic inference involves computing the probability of query variables given evidence.                                                            |
|   5 | Exact inference requires forming the joint distribution, conditioning on evidence, marginalizing out irrelevant variables, and normalizing.              |
|   6 | Exact inference is computationally expensive for large networks due to exponential growth in possible assignments.                                       |
|   7 | Probabilistic programs can generate samples from the joint distribution.                                                                                 |
|   8 | Rejection sampling: generate samples, keep those matching evidence, estimate probabilities from accepted samples.                                        |
|   9 | Rejection sampling is inefficient when evidence is rare, as most samples are rejected.                                                                   |
|  10 | Gibbs sampling: starts with an assignment satisfying evidence, iteratively updates one variable at a time conditioned on others.                         |
|  11 | Gibbs sampling is a Markov Chain Monte Carlo (MCMC) method; samples are dependent but always satisfy evidence.                                           |
|  12 | Gibbs sampling can be more efficient than rejection sampling, especially when evidence is rare.                                                          |
|  13 | Gibbs sampling updates variables using their conditional distribution given the Markov blanket (parents and children).                                   |
|  14 | Markov blanket optimization reduces computation by focusing only on relevant variables.                                                                  |
|  15 | Rejection sampling struggles with rare evidence; Gibbs sampling struggles with highly correlated variables.                                              |
|  16 | Conditional independence in Bayesian networks can be analyzed using graph structure.                                                                     |
|  17 | Independence: two variables are independent if their joint probability equals the product of their marginals.                                            |
|  18 | Conditional independence: two variables are conditionally independent given a third if their conditional joint equals the product of their conditionals. |
|  19 | Graph algorithms can determine (condit                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Dk7Kqqehzjk)
