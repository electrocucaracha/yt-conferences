---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 11: Games II"
nav_order: 2
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  The lecture begins by reviewing two-player zero-sum games and the minmax
  principle, emphasizing how game trees alternate between maximizing and minimizing
  nodes. It then connects these concepts to reinforcement learning, specifically discuss.
resource: https://www.youtube.com/watch?v=9CKRoKFdS5Y
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

The lecture begins by reviewing two-player zero-sum games and the minmax principle, emphasizing how game trees alternate between maximizing and minimizing nodes.
It then connects these concepts to reinforcement learning, specifically discussing value-based methods like SARSA and TD learning, which estimate Q-values and state values, respectively, and how these can be used to derive policies.
The lecture explains the motivation for using reinforcement learning in games—not due to unknown dynamics, but because the state space is often too large for exact methods like value iteration.
The instructor details how TD learning can be adapted for games, including self-play and function approximation, and illustrates these ideas with historical examples such as Samuel’s checkers, Tesauro’s TD-Gammon, and AlphaGo Zero.
The lecture then shifts to simultaneous games, introducing payoff matrices, mixed strategies, and the minimax theorem, which guarantees optimal strategies for both players in zero-sum settings.
Finally, it covers non-zero-sum games and Nash equilibria, highlighting their existence and stability, and concludes by encouraging further study in game theory.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Reviewed two-player zero sum games and the minmax principle for solving them.                                                                                          |
|   2 | Minimax search can be sped up with alpha-beta pruning, which uses lower and upper bounds to prune branches.                                                            |
|   3 | Evaluation functions can be used for approximate game evaluation, incorporating domain knowledge.                                                                      |
|   4 | Proposed learning evaluation functions using reinforcement learning, specifically TD learning.                                                                         |
|   5 | In value-based reinforcement learning, Vπ(s) is the expected utility from state s under policy π; Q-values add the action argument.                                    |
|   6 | SARSA is an on-policy algorithm updating Q-values using immediate and estimated future rewards (bootstrapping).                                                        |
|   7 | Q-values can be used to derive a policy by taking the action with the highest Q-value.                                                                                 |
|   8 | In MDPs, knowing transitions allows computing policies from V-values; in RL, Q-values are needed if transitions are unknown.                                           |
|   9 | For games, transitions and rewards are usually known, but state spaces are too large for value iteration, so RL with function approximation is used.                   |
|  10 | TD learning estimates Vπ(s) from experience, using bootstrapping and function approximation (e.g., value networks).                                                    |
|  11 | In games, self-play is used: both agent and opponent use the same value function, but agent maximizes and opponent minimizes.                                          |
|  12 | Example: Backgammon uses feature vectors for states and linear or neural value functions.                                                                              |
|  13 | Historical examples: Samuel’s checkers (1959, self-play, linear features), Tesauro’s TD-Gammon (1992, neural net, self-play), AlphaGo Zero (2017, deep RL, self-play). |
|  14 | Introduced simultaneous games (e.g., rock-paper-scissors), where both players move at the same time.                                                                   |
|  15 | Defined pure and mixed strategies; mixed strategies are distributions over actions.                                                                                    |
|  16 | Game value is computed as the expected payoff over both players’ strategies.                                                                                           |
|  17 | Minimax theorem (von Neumann, 1928): In simultaneous two-player zero sum games, max-min and min-max values are equal when using mixed strategies.                      |
|  18 | In nonzero sum games (e.g., Prisoner’s Dilemma), Nash equilibrium replace                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9CKRoKFdS5Y)
