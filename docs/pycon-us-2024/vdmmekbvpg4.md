---
layout: default
title: "Talks - Alastair Stanley: Computational Origami"
nav_order: 176
parent: PyCon US 2024
type: Video Note
description: "Ali, an engineer at Bloomberg, presents a personal passion project on computational origami, demonstrating how paper folding can be formalized to solve mathematical problems."
resource: "https://www.youtube.com/watch?v=vdmmeKBvpG4"
youtube_stats:
  view_count: 752
  like_count: 21
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Ali, an engineer at Bloomberg, presents a personal passion project on computational origami, demonstrating how paper folding can be formalized to solve mathematical problems.
He introduces the seven fundamental folding axioms, which allow for the construction of rational numbers and the solution of cubic equations through specific geometric alignments, such as the Belock fold.
To facilitate this, Ali showcases "origametry," a newly released Python library that simulates these folds programmatically, enabling users to calculate roots and perform geometric constructions with precision.
The presentation further explores advanced applications, including a two-fold proof of the irrationality of the square root of two and the use of multifold origami to solve polynomials of any order.
Finally, Ali highlights the physical limits of paper folding by referencing Britney Gallivan’s derivation of an equation for the required paper length, which surprisingly incorporates Pi due to the circular arcs formed during repeated folding.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Origami is the art of paper folding that can be used to construct geometric shapes and solve computational problems.                                  |
|   2 | Folding a strip into a triangle constructs the irrational number square root of two as a length.                                                      |
|   3 | Creating a pentagon from a strip reveals the golden ratio in its diagonal length.                                                                     |
|   4 | Using few folds on square paper allows the construction of various rational fractions, a capability proven by researcher Haga.                        |
|   5 | The presentation formalizes origami operations through seven fundamental folding axioms.                                                              |
|   6 | Axiom 1 allows folding through two points, while Axiom 2 allows folding one point onto another.                                                       |
|   7 | Axiom 3 involves folding one line onto another, which can have multiple solutions depending on line intersection.                                     |
|   8 | Axiom 4 permits folding through a point perpendicular to a line by aligning the line with itself.                                                     |
|   9 | Axiom 5 allows folding a point onto a line such that the fold passes through another point, related to parabolic geometry.                            |
|  10 | Axiom 6, known as the Beloch fold, places one point on a line and a second point on a second line simultaneously.                                     |
|  11 | The Beloch fold can have zero, one, two, or three solutions based on the alignment of associated parabolas.                                           |
|  12 | Axiom 7 involves folding a point onto a line parallel to a second line.                                                                               |
|  13 | Robert Lang proved in 2010 that these seven axioms constitute the complete set of fundamental operations for single-fold origami.                     |
|  14 | The speaker introduced OrigamiGeometry, a new Python library for simulating origami folds computationally.                                            |
|  15 | The library allows users to define points and lines and execute folding axioms to perform calculations.                                               |
|  16 | Addition and subtraction of distances can be achieved using combinations of Axioms 1, 2, and 3.                                                       |
|  17 | The Beloch fold (Axiom 6) is mathematically equivalent to solving cubic equations.                                                                    |
|  18 | By chaining coefficients and applying specific folds, the roots of any general cubic equation can be constructed.                                     |
|  19 | The library outputs the crease lines, which intersect to provide distances corresponding to the cubic equation's roots.                               |
|  20 | Standard single-fold axioms cannot solve quartic or higher-order polynomial equations.                                                                |
|  21 | Multifold origami, where multiple folds are aligned simultaneously, can solve general quartics, quintics, and polynomials of any order.               |
|  22 | Multifold techniques allow for the construction of all real solutions for polynomials of arbitrary degree.                                            |
|  23 | An origami-based proof demonstrates that the square root of two is irrational using only two folds.                                                   |
|  24 | The proof relies on the contradiction of finding smaller integers with the same ratio as the assumed rational representation.                         |
|  25 | Britney Gallivan derived an equation for the paper length required to fold n times, which includes Pi due to circular arcs in the fold cross-section. |
|  26 | Gallivan successfully folded a paper strip in half 12 times, debunking the myth that eight is the limit.                                              |
|  27 | The OrigamiGeometry library currently requires manual plotting of results, though it provides line coefficients for visualization.                    |
|  28 | The speaker encourages community contributions to improve the library's visualization capabilities and functionality.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/vdmmeKBvpG4/hqdefault.jpg)](https://www.youtube.com/watch?v=vdmmeKBvpG4)

[Watch on YouTube](https://www.youtube.com/watch?v=vdmmeKBvpG4)
