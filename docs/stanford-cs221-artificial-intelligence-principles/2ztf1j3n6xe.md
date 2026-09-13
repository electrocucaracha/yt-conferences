---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 7: Markov Decision Processes"
nav_order: 18
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  In this lecture, the instructor introduces Markov Decision Processes
  (MDPs) as a generalization of search problems, highlighting that while search problems
  assume deterministic actions, MDPs account for uncertainty by allowing actions to
  ha...
resource: https://www.youtube.com/watch?v=2ZtF1j3n6XE
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

In this lecture, the instructor introduces Markov Decision Processes (MDPs) as a generalization of search problems, highlighting that while search problems assume deterministic actions, MDPs account for uncertainty by allowing actions to have probabilistic outcomes.
The lecture uses examples such as a "flaky tram" transportation problem and a dice game to illustrate how MDPs model real-world scenarios where outcomes are not certain.
Key concepts covered include the definition of MDPs, the distinction between costs and rewards, the importance of policies (which map states to actions), and the evaluation of policies through rollouts and expected utility, incorporating discount factors to weigh future rewards.
The instructor explains two main algorithms: policy evaluation, which computes the value of a given policy using a recurrence relation and bootstrapping, and value iteration, which finds the optimal policy by maximizing over possible actions at each state.
The lecture concludes by emphasizing the structural similarities between these algorithms and the importance of understanding their underlying recurrences, setting the stage for the next topic on reinforcement learning, where transition probabilities and rewards may be unknown.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Reviewed previous topic: search problems with deterministic actions and costs.                                                                   |
|   2 | Introduced Markov Decision Processes (MDPs) as a generalization of search problems to handle stochastic (uncertain) outcomes.                    |
|   3 | Key difference: In MDPs, actions can lead to multiple possible next states with associated probabilities.                                        |
|   4 | Real-world example: tram can break down with some probability; need to optimize expected time, not just minimum cost.                            |
|   5 | Defined MDP components: states, actions, transition probabilities, rewards, start state, and end condition.                                      |
|   6 | Explained Markov property: future is independent of the past given the current state.                                                            |
|   7 | Compared search problems (costs, deterministic transitions) and MDPs (rewards, probabilistic transitions).                                       |
|   8 | Introduced policies: functions mapping states to actions; solutions to MDPs are policies, not action sequences.                                  |
|   9 | Explained policy evaluation: simulate (roll out) a policy to estimate its expected utility (value).                                              |
|  10 | Introduced discount factor (gamma): determines how much future rewards are valued; utility is the discounted sum of rewards.                     |
|  11 | Discussed Monte Carlo policy evaluation: average utility over multiple rollouts; error decreases with more rollouts.                             |
|  12 | Presented exact policy evaluation using dynamic programming and Q-values: expected value of taking an action and following the policy.           |
|  13 | Explained bootstrapping: iteratively update value estimates for each state until convergence.                                                    |
|  14 | Introduced value iteration: similar to policy evaluation but takes the max over actions to find the optimal policy.                              |
|  15 | Showed that optimal policies for MDPs are deterministic.                                                                                         |
|  16 | Summarized: MDPs generalize search, solutions are policies, utility is expected discounted reward, and value iteration finds the optimal policy. |
|  17 | Next topic: reinforcement learning for unknown transitions and rewards.                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2ZtF1j3n6XE)
