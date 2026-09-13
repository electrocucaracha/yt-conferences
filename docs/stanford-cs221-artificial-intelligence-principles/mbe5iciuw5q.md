---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 3: Learning II"
nav_order: 14
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  In this lecture, the instructor builds on previous discussions of linear
  regression to introduce linear classification, where the goal is to assign discrete
  labels (classes) to inputs rather than predict real-valued outputs. The lecture
  exp...
resource: https://www.youtube.com/watch?v=Mbe5ICIUw5Q
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

In this lecture, the instructor builds on previous discussions of linear regression to introduce linear classification, where the goal is to assign discrete labels (classes) to inputs rather than predict real-valued outputs.
The lecture explains binary and multiclass classification tasks, using examples like image and sentiment classification, and describes how linear classifiers use weight vectors and biases to define decision boundaries that separate classes.
The instructor discusses loss functions, highlighting the limitations of squared loss and zero-one loss for classification, and introduces the logistic loss, which enables effective optimization via gradient descent by providing continuous, differentiable feedback.
For multiclass classification, the lecture covers the use of the softmax function to convert logits into probability distributions and the cross-entropy loss to measure prediction accuracy.
Finally, the instructor explains how to represent text inputs as tensors through tokenization and one-hot encoding, and introduces the bag-of-words representation, noting its simplicity and limitations regarding word order.

# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Linear classification predicts discrete labels (classes) instead of real numbers.                                                                                            |
|   2 | Inputs can be images (as tensors) or text (as strings, later converted to tensors).                                                                                          |
|   3 | Output for classification is one of K choices; for binary classification, outputs are -1 or +1.                                                                              |
|   4 | A predictor maps input to output; in binary classification, prediction is based on the sign of a linear function (logit).                                                    |
|   5 | The decision boundary separates positive and negative classes in input space.                                                                                                |
|   6 | Training data consists of input-output pairs; a learning algorithm uses this data to produce a predictor.                                                                    |
|   7 | The hypothesis class for linear classification consists of all linear functions parameterized by weights and bias.                                                           |
|   8 | Linear classifiers are limited but can be expressive in high dimensions.                                                                                                     |
|   9 | Loss functions measure how well a predictor fits the training data.                                                                                                          |
|  10 | Squared loss (used in regression) is not ideal for classification.                                                                                                           |
|  11 | 0-1 loss counts misclassifications but is not differentiable, making gradient descent ineffective.                                                                           |
|  12 | Logistic loss is introduced as a differentiable alternative, using the logistic (sigmoid) function to map logits to probabilities.                                           |
|  13 | The margin (logit times target label) measures correctness and confidence.                                                                                                   |
|  14 | Logistic loss is defined as the negative log probability of the correct class.                                                                                               |
|  15 | Training loss is the average logistic loss over all examples.                                                                                                                |
|  16 | Gradient descent can optimize logistic loss, unlike 0-1 loss.                                                                                                                |
|  17 | Multiclass classification generalizes binary classification by assigning a weight vector and bias for each class.                                                            |
|  18 | Softmax function converts logits for each class into a probability distribution.                                                                                             |
|  19 | Cross-entropy loss measures the difference between the predicted and target distributions; for one-hot targets, it reduces to negative log probability of the correct class. |
|  20 | Text inputs are converted to tensors via tokenization (splitting into tokens and mapping to indices) and one-hot encoding.                                                   |
|  21 | Bag-of-words representation averages token vectors, ignoring word or                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Mbe5ICIUw5Q)
