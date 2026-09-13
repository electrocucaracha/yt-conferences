---
type: Video Note
title: "From Panic To Peace: Making K8s Controller Observability Suck Less - Cat Morris & Derik Evangelista"
description: "The presenters discuss improving Kubernetes controller observability by sharing a four-chapter story, beginning with a Shrek-inspired tale illustrating the challenges of identifying and fixing problems. They recount a real-world debugging e..."
resource: https://www.youtube.com/watch?v=1P76Roya9oQ
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters discuss improving Kubernetes controller observability by sharing a four-chapter story, beginning with a Shrek-inspired tale illustrating the challenges of identifying and fixing problems.
They recount a real-world debugging experience with a user named Sid, highlighting the difficulties of navigating verbose logs, complex commands, and unintuitive interfaces, which prompted them to enhance their product’s usability.
Solutions included introducing a streamlined CLI, developing a graphical user interface for easier information discovery, implementing structured and leveled logging, and reducing unnecessary log output.
They also addressed the need for clearer status indicators, consistent resource conditions, and event emissions to help users trace issues efficiently, drawing inspiration from community feedback and industry expectations.
The talk concludes with the concept of the "observability onion," emphasizing the importance of layered observability—from logs and status to events, metrics, and user interfaces—to support different user personas and ensure a more peaceful, effective debugging experience.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on improving Kubernetes controller observability, moving from panic to peace.                                                      |
|   2 | Story structured in four chapters: fairy tale of finding/fixing a problem, Sid's debugging journey, Victor's expectations, and the observability onion. |
|   3 | Chapter 1 uses Shrek as a metaphor: things seem fine until chaos erupts, highlighting the importance of finding and interpreting information correctly. |
|   4 | Debugging Kubernetes controllers is compared to Shrek’s journey: misdirection, false starts, and the need for better information.                       |
|   5 | Chapter 2 details Sid’s complex debugging process using the product:                                                                                    |
|   6 | Required multiple aliases and long commands.                                                                                                            |
|   7 | Needed to watch logs across changing pods.                                                                                                              |
|   8 | Had to grep for errors, use multiple tabs, and follow a 12-step troubleshooting guide.                                                                  |
|   9 | Logs were verbose and hard to interpret.                                                                                                                |
|  10 | Identified pains: hard platform interaction, confusing information spread across locations, and difficult log interpretation.                           |
|  11 | Solutions implemented:                                                                                                                                  |
|  12 | Improved CLI with simpler, memorable commands.                                                                                                          |
|  13 | Added graphical user interface (GUI) for easier, at-a-glance debugging.                                                                                 |
|  14 | GUI enables users to discover information without heavy documentation.                                                                                  |
|  15 | Log improvements:                                                                                                                                       |
|  16 | Introduced log levels (warning, info, debug, trace) for different personas.                                                                             |
|  17 | Reduced unnecessary reconciliation and log verbosity.                                                                                                   |
|  18 | Added structured logging (e.g., JSON) for better machine and user consumption.                                                                          |
|  19 | Reduced log lines by 67%.                                                                                                                               |
|  20 | Chapter 3: Victor’s review of similar tools highlighted maturity and integration gaps.                                                                  |
|  21 | Improvements made:                                                                                                                                      |
|  22 | Exposed relevant data for different personas.                                                                                                           |
|  23 | Enabled tracing from parent to child resources.                                                                                                         |
|  24 | Enhanced kubectl get/describe output with clear state indicators and consistent status fields.                                                          |
|  25 | Emitted events on state changes.                                                                                                                        |
|  26 | Used common labels and CRD features for easier resource association.                                                                                    |
|  27 | Chapter 4: Observability onion model:                                                                                                                   |
|  28 | Layers: logs → status → events → metrics → traces → interfaces.                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1P76Roya9oQ)