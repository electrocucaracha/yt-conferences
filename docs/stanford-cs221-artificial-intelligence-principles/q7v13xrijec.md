---
type: Video Note
title: "Stanford CS221 | Autumn 2025 | Lecture 15: Logic I"
description: "The lecture introduces logic as the final technical topic before moving to AI and society, offering a perspective distinct from probabilistic reasoning. It reviews how logic, particularly propositional logic, serves as a formal language for..."
resource: https://www.youtube.com/watch?v=Q7V13XriJEc
tags: ["stanford-cs221-artificial-intelligence-principles", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The lecture introduces logic as the final technical topic before moving to AI and society, offering a perspective distinct from probabilistic reasoning.
It reviews how logic, particularly propositional logic, serves as a formal language for representing and reasoning about knowledge, defined by syntax (valid formulas), semantics (meaning via models or possible worlds), and inference rules (deriving new formulas).
The instructor explains key concepts such as models, interpretation functions, knowledge bases, and the relationships between entailment, contradiction, and contingency, illustrating how adding information to a knowledge base narrows possible worlds.
The lecture also covers practical operations like "ask" (querying the knowledge base) and "tell" (adding new information), and relates logical reasoning to probabilistic reasoning in Bayesian networks, highlighting differences in expressivity and handling uncertainty.
Finally, the lecture discusses satisfiability, model checking, and inference rules, emphasizing the importance of soundness and completeness in logical systems, and sets the stage for exploring first-order logic in the next session.
# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Logic is the last technical topic before the AI society section of the course.                                                                                          |
|   2 | The course has focused on agents that perceive, act, reason, and learn, with recent emphasis on reasoning.                                                              |
|   3 | Previous reasoning methods included search, MDPs, games, and Bayesian networks for probabilistic reasoning.                                                             |
|   4 | Logical reasoning (propositional and first-order logic) is more primitive than probabilistic reasoning as it does not handle uncertainty.                               |
|   5 | Logic was the dominant AI paradigm before the 1990s; it is deterministic and does not leverage data.                                                                    |
|   6 | Logic provides compact expressivity for representing knowledge.                                                                                                         |
|   7 | Logic is a formal language defined by syntax (valid formulas), semantics (meaning of formulas), and inference rules (deriving new formulas).                            |
|   8 | Syntax: Defines valid expressions using propositional symbols (atomic formulas) and logical connectives (and, or, not, implies, equivalence).                           |
|   9 | Semantics: Assigns meaning to formulas via models (assignments of truth values to symbols).                                                                             |
|  10 | The interpretation function maps formulas and models to true/false values.                                                                                              |
|  11 | The set of models where a formula is true represents its semantics.                                                                                                     |
|  12 | A knowledge base (KB) is a set of formulas; its semantics is the set of models satisfying all formulas in KB.                                                           |
|  13 | Adding formulas to KB shrinks the set of possible models (worlds).                                                                                                      |
|  14 | Entailment: KB entails F if adding F does not shrink the set of models.                                                                                                 |
|  15 | Contradiction: KB contradicts F if adding F results in no possible models.                                                                                              |
|  16 | Contingency: Adding F shrinks the set of models but does not eliminate all models.                                                                                      |
|  17 | Ask and tell operations: Ask queries KB (returns yes, no, or I don't know); tell adds new information (returns already known, contradiction, or learned something new). |
|  18 | Satisfiability: KB is satisfiable if it has at least one model; entailment, contradiction, and contingency can be reduced to satisfiability checks.                     |
|  19 | Model checking and SAT solvers efficiently determine satisfiability.                                                                                                    |
|  20 | Inference rules (e.g., modus ponens) allow deriving n                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Q7V13XriJEc)