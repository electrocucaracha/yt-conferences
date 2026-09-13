---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 6: Search II"
nav_order: 17
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  The transcript reviews the concept of search problems, emphasizing the
  need for search algorithms to solve complex tasks requiring reasoning. It introduces
  uniform cost search (UCS), also known as Dijkstra's algorithm, which finds the minim...
resource: https://www.youtube.com/watch?v=4Iu4KPVbnAY
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

The transcript reviews the concept of search problems, emphasizing the need for search algorithms to solve complex tasks requiring reasoning.
It introduces uniform cost search (UCS), also known as Dijkstra's algorithm, which finds the minimum-cost path in graphs with non-negative edge costs by expanding nodes in order of increasing past cost using a priority queue.
The transcript explains the correctness of UCS and contrasts it with dynamic programming, noting that UCS can handle cycles while dynamic programming cannot.
It then introduces the A\* (A-star) algorithm, which augments UCS with a heuristic function estimating future cost, allowing for more efficient search by prioritizing nodes likely to lead to the goal.
The importance of heuristic consistency is discussed to ensure optimality, and the concept of constructing heuristics via problem relaxation is presented, where constraints are removed to make the problem easier and the relaxed solution provides a valid heuristic.
The lecture concludes by summarizing that both UCS and A\* are exact algorithms for finding minimum-cost paths, with A\* leveraging domain knowledge through heuristics to improve efficiency, and hints at future topics involving non-deterministic actions.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Search is needed for solving complex problems requiring reasoning.                                                                                                 |
|   2 | A search problem is defined by a start state, successor function (actions and resulting states), action costs, and a goal test.                                    |
|   3 | The objective is to find a solution minimizing total action cost.                                                                                                  |
|   4 | Four algorithms reviewed: exhaustive search, dynamic programming (exhaustive with caching), best-of-n (sampling), and beam search (truncating possible solutions). |
|   5 | Dynamic programming computes future cost (minimum cost from a state to the end) using recurrence, requiring acyclic graphs.                                        |
|   6 | Cycles in search problems cause issues for dynamic programming (infinite loops, undefined costs).                                                                  |
|   7 | Uniform Cost Search (UCS), also known as Dijkstra’s algorithm, handles cycles with non-negative costs by computing past cost (minimum cost from start to a state). |
|   8 | UCS processes states in order of increasing past cost using a priority queue.                                                                                      |
|   9 | States are partitioned into explored, frontier, and unexplored.                                                                                                    |
|  10 | UCS guarantees finding the minimum cost path if all costs are non-negative.                                                                                        |
|  11 | UCS expands states uniformly from the start, without knowledge of the end state.                                                                                   |
|  12 | Limitation: UCS explores many unnecessary states far from the goal.                                                                                                |
|  13 | A\* (A-star) search improves UCS by adding a heuristic function estimating future cost to the end state.                                                           |
|  14 | A\* orders states by past cost plus heuristic; heuristic must be consistent (modified edge costs non-negative, h(goal)=0).                                         |
|  15 | Consistency ensures A\* finds the optimal path.                                                                                                                    |
|  16 | Heuristics are often constructed as future costs of relaxed problems (problems with fewer constraints).                                                            |
|  17 | Relaxations can be: removing walls (grid), allowing unlimited tram rides, or permitting tile overlaps (puzzle).                                                    |
|  18 | Combining multiple heuristics by taking their maximum yields a consistent heuristic.                                                                               |
|  19 | UCS and A\* are exact algorithms for graphs with cycles and non-negative costs.                                                                                    |
|  20 | Next topic: search with non-deterministic actions (Markov Decision Processes).                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4Iu4KPVbnAY)
