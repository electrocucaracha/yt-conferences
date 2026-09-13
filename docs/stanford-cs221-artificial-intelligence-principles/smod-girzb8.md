---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 10: Games I"
nav_order: 1
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  In this lecture, the focus is on games as state-based models, building
  on previous discussions of Markov decision processes (MDPs) and reinforcement learning.
  The instructor introduces the formal structure of games, particularly two-player...
resource: https://www.youtube.com/watch?v=SMOD_GiRzb8
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

In this lecture, the focus is on games as state-based models, building on previous discussions of Markov decision processes (MDPs) and reinforcement learning.
The instructor introduces the formal structure of games, particularly two-player zero-sum games, and explains how game trees represent the sequence of decisions made by agents and opponents.
Key concepts include the evaluation of game states using recurrences such as expected value, expectimax (for optimal play against a fixed opponent), and minimax (for optimal play against an unknown, adversarial opponent).
The lecture also covers computational strategies like alpha-beta pruning to speed up minimax search and the use of evaluation functions for approximate, depth-limited search.
The session concludes by highlighting the importance of understanding optimality relative to opponent strategies and sets the stage for learning evaluation functions in future lectures.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Lecture topic: Games, completing the tour of state-based models after Markov Decision Processes (MDPs) and reinforcement learning          |
|   2 | Example game: Three bins (A, B, C); agent chooses a bin, opponent chooses a number from that bin; agent aims to maximize the chosen number |
|   3 | In games, strategy depends on the opponent’s actions, which are unknown                                                                    |
|   4 | In MDPs, the environment is random/unknown; in games, the environment is an opponent with an unknown strategy                              |
|   5 | Focus on two-player zero-sum games: agent and opponent; agent’s utility = -opponent’s utility                                              |
|   6 | Game formalization: start state, end state check, player function (whose turn), successors mapping (action to state)                       |
|   7 | Game tree: nodes represent states, edges represent actions; agent and opponent alternate turns                                             |
|   8 | Utility is typically assigned at end states (sparse reward problem)                                                                        |
|   9 | Policy: mapping from states to actions; can be deterministic or stochastic                                                                 |
|  10 | Game value: expected utility over all possible rollouts, given policies for both players                                                   |
|  11 | Simulation: sample rollouts to estimate value (Monte Carlo), or compute value exactly via recurrence (can be exponential time)             |
|  12 | Expectimax: finds optimal agent policy against a fixed opponent policy; agent maximizes expected utility, opponent’s actions are averaged  |
|  13 | Minimax: assumes opponent plays optimally to minimize agent’s utility; agent maximizes, opponent minimizes                                 |
|  14 | Minimax value: agent is guaranteed to win if value is 1, opponent if -1                                                                    |
|  15 | Solved games: perfect play outcome is known (e.g., tic-tac-toe); chess and Go are not solved                                               |
|  16 | Minimax is agnostic to opponent’s policy; expectimax is optimal only against a fixed opponent policy                                       |
|  17 | Expected minimax: combines expectation, min, and max nodes (e.g., with random events like coin flips)                                      |
|  18 | Framework can handle multiple players, extra turns, etc., but not imperfect information or non-turn-based games                            |
|  19 | Alpha-beta pruning: speeds up minimax by pruning subtrees that cannot affect the outcome, based on bounds (alpha for max                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SMOD_GiRzb8)
