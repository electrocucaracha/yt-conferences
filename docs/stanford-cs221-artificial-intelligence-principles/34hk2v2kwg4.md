---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 8: Reinforcement Learning"
nav_order: 19
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  The lecture begins by reviewing Markov Decision Processes (MDPs), which
  are defined by states, actions, transition probabilities, rewards, end conditions,
  and a discount factor, and visualized as graphs with state and chance nodes. The
  solu...
resource: https://www.youtube.com/watch?v=34Hk2v2kwg4
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

The lecture begins by reviewing Markov Decision Processes (MDPs), which are defined by states, actions, transition probabilities, rewards, end conditions, and a discount factor, and visualized as graphs with state and chance nodes.
The solution to an MDP is a policy mapping states to actions, and algorithms like policy evaluation and value iteration are used to compute the value of policies and find optimal ones.
The focus then shifts to reinforcement learning (RL), where the agent does not know the MDP in advance and must learn by interacting with the environment, receiving feedback, and updating its policy dynamically.
The lecture introduces four RL algorithms: model-based value iteration (which estimates the MDP from experience and then computes the optimal policy), model-free Monte Carlo (which estimates Q-values directly from rollouts), SARSA (which updates Q-values during rollouts using bootstrapping), and Q-learning (which estimates optimal Q-values off-policy).
The key distinction is that model-based methods explicitly estimate the environment, while model-free methods learn action values directly, and the lecture concludes by noting that future sessions will address RL in large or continuous state spaces.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Reviewed Markov Decision Processes (MDPs): defined by start state, actions, transition probabilities, rewards, end test, and discount factor.            |
|   2 | Example: Flaky tram MDP with states 1 to 10; actions are walk (deterministic) or tram (probabilistic).                                                   |
|   3 | MDPs visualized as graphs with state nodes (agent decisions) and chance nodes (nature's outcomes).                                                       |
|   4 | Solution to an MDP is a policy: maps states to actions; must handle randomness.                                                                          |
|   5 | Policy evaluation: computes expected utility (discounted sum of rewards) for a given policy.                                                             |
|   6 | Value iteration: computes optimal policy by maximizing expected utility over actions.                                                                    |
|   7 | Partial application in code: allows defining policies as functions with some arguments fixed.                                                            |
|   8 | Reinforcement Learning (RL): agent interacts with unknown environment, receives rewards and observations, learns optimal policy through trial and error. |
|   9 | RL agent: has get_action (chooses action) and incorporate_feedback (updates internal state/policy).                                                      |
|  10 | Difference between policy and agent: policy is static; agent can update policy dynamically using feedback.                                               |
|  11 | Model-based RL: agent estimates the MDP from experience, then uses value iteration to compute optimal policy.                                            |
|  12 | Exploration policy (e.g., random actions) is used to gather data; exploitation policy is used after learning.                                            |
|  13 | Transition counts are used to estimate probabilities in the learned MDP.                                                                                 |
|  14 | Model-free RL: bypasses explicit MDP estimation, directly estimates Q-values (expected utility of state-action pairs).                                   |
|  15 | Epsilon-greedy policy: with probability ε, explores randomly; otherwise, exploits best-known action.                                                     |
|  16 | Monte Carlo method: estimates Q-values by averaging returns from rollouts.                                                                               |
|  17 | SARSA: updates Q-values incrementally using bootstrapping (reward plus discounted estimate of next Q-value).                                             |
|  18 | Q-learning: off-policy algorithm; updates Q-values towards reward plus discounted max Q-value of next state.                                             |
|  19 | Model-free methods can update before episode ends and do not require full MDP knowledge.                                                                 |
|  20 | Next top                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=34Hk2v2kwg4)
