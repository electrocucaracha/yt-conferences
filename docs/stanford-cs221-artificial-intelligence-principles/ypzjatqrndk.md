---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 2: Learning I"
nav_order: 13
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  The lecture covers the concepts of tensors, the einsum function, computation
  graphs, gradients, backpropagation, and linear regression in machine learning. It
  begins by explaining tensors as fundamental data structures in modern machine lea...
resource: https://www.youtube.com/watch?v=ypZJaTqrNdk
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

The lecture covers the concepts of tensors, the einsum function, computation graphs, gradients, backpropagation, and linear regression in machine learning.
It begins by explaining tensors as fundamental data structures in modern machine learning, with their order (number of axes) determining their type (scalars, vectors, matrices, etc.), and introduces the einsum function as a flexible tool for expressing a wide range of tensor operations.
The speaker then demonstrates how computation graphs can represent complex functions as compositions of simple operations, enabling efficient calculation of gradients using the backpropagation algorithm, which leverages the chain rule.
The lecture transitions to linear regression, outlining the process of defining a hypothesis class (set of possible predictors), a loss function to measure prediction error, and the use of optimization algorithms like gradient descent to find parameters that minimize the loss.
Throughout, the importance of gradients for guiding parameter updates and the general workflow of supervised learning—defining predictors, evaluating them with loss functions, and optimizing parameters—is emphasized as foundational to machine learning.

# Main Points

|   # | Main point                                                                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduced tensors as fundamental units in machine learning, representing data, parameters, and computations.                                                                                                                    |
|   2 | Explained tensor order: order 0 (scalars), order 1 (vectors), order 2 (matrices), higher orders possible.                                                                                                                        |
|   3 | Discussed inops library for legible tensor computations; axes can be named for clarity.                                                                                                                                          |
|   4 | Demonstrated einsum function as a generalization of matrix multiplication, enabling various tensor operations (identity, sum, elementwise product, dot product, outer product, transpose, matrix-vector/matrix-matrix products). |
|   5 | Emphasized that einsum can express many operations via axis naming and mapping.                                                                                                                                                  |
|   6 | Introduced objective functions mapping tensors to scalars, with gradients indicating how to improve the function (e.g., minimize loss).                                                                                          |
|   7 | Reviewed gradient and partial derivatives: gradient points in direction of greatest increase; negative gradient for minimization.                                                                                                |
|   8 | Illustrated gradients in 1D and 2D cases, both analytically and via code.                                                                                                                                                        |
|   9 | Defined computation graphs: nodes represent values or operations; forward pass computes values, backward pass computes gradients.                                                                                                |
|  10 | Explained backpropagation as an algorithm for efficiently computing gradients using the chain rule on computation graphs.                                                                                                        |
|  11 | Highlighted that modern libraries (e.g., PyTorch) automate this process.                                                                                                                                                         |
|  12 | Outlined supervised learning: predictor maps input to output; training data consists of input-output pairs.                                                                                                                      |
|  13 | Defined hypothesis class as the set of possible predictors (e.g., all linear functions with different parameters).                                                                                                               |
|  14 | Introduced loss function (e.g., squared loss) to measure predictor performance on training data.                                                                                                                                 |
|  15 | Described optimization (e.g., gradient descent) to find parameters minimizing the loss.                                                                                                                                          |
|  16 | Noted that learning rate affects optimization; too high can cause divergence.                                                                                                                                                    |
|  17 | Summarized the machine learning workflow: define hypothesis class, loss function, and optimization algorithm.                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ypZJaTqrNdk)
