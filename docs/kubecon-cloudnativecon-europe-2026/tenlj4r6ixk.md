---
layout: default
title:
  Open Policy Agent. (OPA) Intro & Deep Dive - Charlie Egan & Anders Eknert,
  Apple
nav_order: 228
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speakers welcomed a full audience to the Open Maintainer track, introducing
  themselves as long-time users and maintainers of the Open Policy Agent (OPA) project.
  They provided an overview of OPA as a general-purpose policy engine that s...
resource: https://www.youtube.com/watch?v=TENlj4r6IXk
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speakers welcomed a full audience to the Open Maintainer track, introducing themselves as long-time users and maintainers of the Open Policy Agent (OPA) project.
They provided an overview of OPA as a general-purpose policy engine that standardizes policy expression across various use cases, highlighting its growing adoption in production environments and the importance of community engagement for spreading awareness.
Recent updates include enhancements to the Rego language, such as string interpolation and upcoming support for an "or" keyword, as well as improvements to documentation and interactive examples to aid both human users and generative AI tools.
The team also discussed the evolution of the Regal linter into a full-featured language server, updates to related projects like OPA Control Plane, Gatekeeper, and Conftest, and encouraged users to explore new tools, contribute feedback, and participate in the community.
The session concluded with an invitation for questions and further engagement at the event and online.

# Main Points

|   # | Main point                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------- |
|   1 | Event had a full house; some attendees could not enter and will watch online.                               |
|   2 | Session is the Open Maintainer Track, providing project updates.                                            |
|   3 | Anders: Sixth or seventh KubeCon, OPA maintainer for 5-6 years, started as end user.                        |
|   4 | Charlie: Used OPA since 2019 for Kubernetes admission, became maintainer in 2022.                           |
|   5 | Encouragement for users to get involved in open source projects.                                            |
|   6 | Agenda: Introduction to OPA, community survey updates, Rego language updates, project roadmap.              |
|   7 | OPA is a general-purpose policy engine for expressing policies across various use cases.                    |
|   8 | OPA standardizes policy expression, replacing inconsistent, multi-language approaches.                      |
|   9 | Users write policies in Rego, load them into OPA, and provide structured data (typically JSON).             |
|  10 | OPA reloads policies on updates and produces audit logs for decisions.                                      |
|  11 | Study found significant amount of public policy code on GitHub is written in Rego.                          |
|  12 | Community survey: Most advanced OPA use cases are now in production; trend increasing.                      |
|  13 | Word of mouth and events are primary ways people learn about OPA.                                           |
|  14 | Rego language has seen major updates, including move from version 1 to 2.                                   |
|  15 | New features: contains keyword, not in, improved readability and maintainability.                           |
|  16 | String interpolation added, making it easier to inject values into strings.                                 |
|  17 | Upcoming: or keyword to simplify expressing logical OR in policies.                                         |
|  18 | New site launched with more interactive and built-in function examples.                                     |
|  19 | Feedback form added to site; positive feedback outweighs negative.                                          |
|  20 | Increased use of LLMs for learning and writing Rego; some issues with outdated or hallucinated code.        |
|  21 | Encouragement to provide feedback on generative AI use with Rego.                                           |
|  22 | OPA is primarily a security tool; best practices and learning resources emphasized.                         |
|  23 | Regal tool: linter and language server for Rego, now supports IntelliJ, 107 linter rules, high performance. |
|  24 | OCP (OPA Control Plane): centralized policy management, recent updates include AWS S3 support and Web       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=TENlj4r6IXk)
