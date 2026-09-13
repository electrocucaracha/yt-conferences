---
type: Video Note
title: "Stanford CS221 | Autumn 2025 | Lecture 9: Policy Gradient"
description: "The lecture continues the discussion on reinforcement learning (RL), moving from basic algorithms to more advanced topics like function approximation and policy-based methods. It reviews the RL setting, where an agent interacts with an envi..."
resource: https://www.youtube.com/watch?v=lOMNskWVeD8
tags: ["stanford-cs221-artificial-intelligence-principles", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The lecture continues the discussion on reinforcement learning (RL), moving from basic algorithms to more advanced topics like function approximation and policy-based methods.
It reviews the RL setting, where an agent interacts with an environment modeled as a Markov Decision Process (MDP), receiving rewards and observations to improve its actions over time.
The lecture distinguishes between model-based and model-free approaches, explaining value-based methods like Q-learning and SARSA, and introduces the challenges of large state spaces, which require function approximation using parameterized models instead of tabular representations.
The instructor then shifts to policy-based methods, particularly policy gradient algorithms, which optimize policies directly by maximizing expected utility through gradient descent, and explains the REINFORCE algorithm as a foundational example.
Techniques for variance reduction, such as using baselines, are discussed to improve learning efficiency, and the lecture concludes by summarizing the three main RL approaches—model-based, value-based, and policy-based—highlighting their similarities in structure and their respective strengths.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Reviewed basic reinforcement learning (RL) concepts and algorithms                                                                                      |
|   2 | RL setting: agent interacts with environment, receives rewards and observations, aims to maximize cumulative reward                                     |
|   3 | Environment modeled as a Markov Decision Process (MDP)                                                                                                  |
|   4 | Discussed Q-learning, SARSA, epsilon-greedy exploration, and learning rate                                                                              |
|   5 | RL algorithm only sees environment through get_action and incorporate_feedback functions                                                                |
|   6 | Policy: fixed mapping from states to actions; RL algorithm updates policy dynamically                                                                   |
|   7 | Defined value functions: v_pi(s), q_pi(s,a), v*, q*                                                                                                     |
|   8 | Model-based RL: estimate MDP, compute optimal policy via value iteration                                                                                |
|   9 | Model-free value-based RL: estimate Q-values directly, derive policy from Q-values                                                                      |
|  10 | General update: move Q(s,a) towards a target using learning rate                                                                                        |
|  11 | On-policy (e.g., SARSA): exploration and estimation policies are the same                                                                               |
|  12 | Off-policy (e.g., Q-learning): estimate optimal policy Q\* using data from any policy                                                                   |
|  13 | Targets: full rollouts (Monte Carlo) vs. bootstrapping (use current Q estimates)                                                                        |
|  14 | Reviewed four algorithms: model-based value iteration, model-free Monte Carlo, SARSA (on-policy, bootstrapping), Q-learning (off-policy, bootstrapping) |
|  15 | Tabular setting: Q-value for every state-action pair; infeasible for large state spaces                                                                 |
|  16 | Function approximation: parameterize Q(s,a) with features and learn parameters (theta)                                                                  |
|  17 | Use linear models or neural networks to map state-action features to Q-values                                                                           |
|  18 | Loss function: squared difference between predicted Q and target                                                                                        |
|  19 | No convergence guarantees with function approximation; may reach local optima                                                                           |
|  20 | Policy-based methods: directly parameterize and optimize the policy (policy gradient)                                                                   |
|  21 | Policy as a probabilistic classifier mapping states to action distributions                                                                             |
|  22 | Imitation learning: train policy from expert demonstrations (supervised learning)                                                                       |
|  23 | Policy gradient: maximize expected utility by sampling trajectories and updating parameters via gradient ascent                                         |
|  24 | REINFORCE algorithm: sample rollouts, weight up                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lOMNskWVeD8)