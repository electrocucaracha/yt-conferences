---
layout: default
title: "The Most Bizarre Software Bugs in History - Mia Bajić"
nav_order: 35
parent: PyCon US 2025
type: Video Note
description: "Mia presents a compelling overview of some of the most bizarre and costly software bugs in history, illustrating how minor coding errors can lead to catastrophic failures."
resource: "https://www.youtube.com/watch?v=gM2J5plaDmw"
youtube_stats:
  view_count: 1797
  like_count: 36
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Mia presents a compelling overview of some of the most bizarre and costly software bugs in history, illustrating how minor coding errors can lead to catastrophic failures.
She details the Boeing 737 Max disaster, where a flawed MCAS system relying on a single sensor caused two fatal crashes, highlighting the dangers of single points of failure and inadequate pilot training.
The talk also covers the NASA Mars Climate Orbiter, which was destroyed due to a simple unit conversion error between imperial and metric systems, emphasizing the critical need for integration testing and clear communication between teams.
Other examples include a Google Safe Browsing typo that marked all sites as dangerous, an Amazon pricing algorithm loop that listed a book for $23.7 million, and a Linux script error that deleted a user’s entire operating system.
Through these cases, Mia argues that software failures are often the result of compounded issues, such as the "Swiss cheese model," and stresses the importance of treating spreadsheets and scripts as production code, handling edge cases, and maintaining rigorous testing protocols to build more resilient systems.

# Main Points

|   # | Main point                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lion Air Flight 610 crashed in 2018 due to the Maneuvering Characteristics Augmentation System (MCAS) forcing the nose down based on faulty data from a single angle of attack sensor.    |
|   2 | Boeing developed MCAS to compensate for the 737 Max's shifted center of gravity caused by larger engines, avoiding the need for extensive pilot retraining.                               |
|   3 | The FAA delegated parts of the 737 Max certification process to Boeing, resulting in a lack of independent safety evaluation and subsequent fraud charges.                                |
|   4 | Post-crash fixes included using two sensors, limiting MCAS activation, improving pilot training, and adding persistent warnings.                                                          |
|   5 | The Swiss cheese model illustrates how failures occur when multiple independent safeguards, such as software flaws, human error, and mechanical issues, align simultaneously.             |
|   6 | In 2009, a Google engineer’s typo of a forward slash in the malware registry caused all search results to be flagged as dangerous for 40 minutes.                                         |
|   7 | NASA’s Mars Climate Orbiter was destroyed in 1999 because one team used imperial units while the other used metric units, leading to a navigation error of 4.45 times the intended value. |
|   8 | The incident highlighted the critical need for integration tests and standardized units across interacting systems to prevent misinterpretation of data.                                  |
|   9 | A Sun Microsystems employee named Steve Null disappeared from databases because the system interpreted the string "null" as a null value rather than a name.                              |
|  10 | Edge cases in user inputs, such as names like "ABCDE" or "Robert; DROP TABLE Students," can cause unexpected system behavior or data loss if not properly sanitized.                      |
|  11 | In 2011, an Amazon pricing algorithm loop between two sellers caused a book on fly genetics to be listed for $23.7 million instead of its actual value.                                   |
|  12 | Excel autocorrected gene names like "March 5" to dates, contributing to errors in 19.6% of genome research studies analyzed in 2016.                                                      |
|  13 | Approximately 90% of business spreadsheets contain errors, with 24% of those containing formulas having at least one mistake.                                                             |
|  14 | JP Morgan lost $6 billion due to a spreadsheet error where the sum of rates was divided instead of averaged, incorrectly lowering the calculated Value at Risk.                           |
|  15 | Spreadsheets should be treated as production software, requiring rigorous testing and validation to prevent costly financial miscalculations.                                             |
|  16 | A missing space in a Linux install script command caused it to delete the entire user directory instead of a specific folder, wiping out the operating system.                            |
|  17 | Software bugs can sometimes become features or popular elements, as seen in the Civilization game where a designed "bug" increased player engagement.                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/gM2J5plaDmw/hqdefault.jpg)](https://www.youtube.com/watch?v=gM2J5plaDmw)

[Watch on YouTube](https://www.youtube.com/watch?v=gM2J5plaDmw)
