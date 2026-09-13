---
layout: default
title: "Stanford CS221 | Autumn 2025 | Lecture 16: Logic II"
nav_order: 7
parent: Stanford Cs221 Artificial Intelligence Principles
type: Video Note
description:
  In this lecture, the instructor introduces first order logic as a more
  expressive and powerful system than propositional logic, capable of representing
  complex statements about the world using objects, predicates, functions, variables,
  and...
resource: https://www.youtube.com/watch?v=x9Mbqu06OVo
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

In this lecture, the instructor introduces first order logic as a more expressive and powerful system than propositional logic, capable of representing complex statements about the world using objects, predicates, functions, variables, and quantifiers.
The lecture explains the syntax and semantics of first order logic, emphasizing the distinction between terms (which denote objects) and formulas (which denote truth values), and describes how models are constructed using a domain of objects and an interpretation function that maps symbols to elements in the domain.
Logical inference in first order logic is discussed, including the use of modus ponens, substitution, and unification to derive new facts, and the limitations of propositionalization when unique names and domain closure do not hold.
The instructor also demonstrates how to translate natural language statements into first order logic expressions, highlighting common pitfalls with quantifiers and the increased expressivity provided by variables and quantifiers.
The lecture concludes by noting that while first order logic is powerful, it cannot express certain statements (such as proportions), which require higher-order logics, and previews upcoming topics on AI and language models.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction to first order logic as a more expressive system than propositional logic                                         |
|   2 | Example knowledge base: facts about Alice, Phoenix, hot cities, students as people, cities as places, and logical implications |
|   3 | Demonstration of inference: using knowledge base to answer questions and perform logical reasoning                             |
|   4 | Review of propositional logic: syntax (symbols, connectives), semantics (models as truth assignments), and inference rules     |
|   5 | Knowledge bases as sets of formulas; entailment, contradiction, and contingency defined by model relationships                 |
|   6 | Satisfiability as a basis for inference; model checking determines satisfiability                                              |
|   7 | Inference rules like modus ponens: deriving new formulas from existing ones                                                    |
|   8 | Soundness and completeness: soundness ensures derived formulas are true; completeness ensures all true formulas can be derived |
|   9 | Limitations of propositional logic: lacks objects, predicates, quantifiers, and variables; not compact for general statements  |
|  10 | Introduction of first order logic: terms (constants, variables, functions), predicates, quantifiers (for all, exists)          |
|  11 | Syntax: terms denote objects; formulas denote truth values; predicates applied to terms return booleans                        |
|  12 | Semantics: models consist of a domain (set of objects) and an interpretation function mapping symbols to domain elements       |
|  13 | Interpretation function recursively evaluates formulas in a given model                                                        |
|  14 | Quantifiers interpreted as iterating over all (for all) or some (exists) objects in the domain                                 |
|  15 | Propositionalization possible under unique names and domain closure assumptions                                                |
|  16 | Definite clauses: formulas of the form (for all x) (a1 ∧ ... ∧ ak) ⇒ b; modus ponens applies to these                          |
|  17 | Substitution: replacing variables with terms in formulas                                                                       |
|  18 | Unification: finding substitutions to make two terms/formulas identical                                                        |
|  19 | Modus ponens with unification enables inference in first order logic                                                           |
|  20 | Complexity: infinite possible formulas if functions are present                                                                |
|  21 | Modus ponens is sound but not complete; comple                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=x9Mbqu06OVo)
