---
layout: default
title:
  "Project Lightning Talk: Konveyor AI for Every Language and the Future of App
  Moderniza... Shaaf Syed"
nav_order: 272
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Sha discusses the challenges of modernizing legacy enterprise applications,
  such as 30-year-old Enterprise Java Beans, to run on platforms like Kubernetes.
  He introduces the Conveyor community’s approach, which centers on a static code
  anal...
resource: https://www.youtube.com/watch?v=6FNR4jGox9w
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

Sha discusses the challenges of modernizing legacy enterprise applications, such as 30-year-old Enterprise Java Beans, to run on platforms like Kubernetes.
He introduces the Conveyor community’s approach, which centers on a static code analysis engine that supports multiple languages—including Java, Golang, Python, and NodeJS—to identify problematic code and suggest remedies for modernization.
The system integrates with the language server protocol for detailed code insights and leverages large language models to generate meaningful code transformations.
Additionally, Conveyor has implemented agentic AI to automate code fixes and validation, as well as a memory feature that retains organizational code changes to improve future recommendations.
Sha concludes by demonstrating how the tool can convert outdated code, like RMI IOP, into modern REST endpoints, and invites attendees to learn more at the Conveyor kiosk.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sha discusses application modernization, focusing on moving legacy code (e.g., 30-year-old Enterprise Java Beans) to Kubernetes. |
|   2 | Legacy code presents challenges such as stubs, serialization, lack of clustering, and other issues.                              |
|   3 | The Conveyor community addresses application modernization for multiple languages.                                               |
|   4 | Conveyor uses a static code analysis engine to analyze source code (Java, Golang, etc.).                                         |
|   5 | The analysis engine provides guidelines for modifying components (I/O, messaging, transactions) to run on Kubernetes.            |
|   6 | Integration with the Language Server Protocol offers insights into code paths and enables implementation of analysis rules.      |
|   7 | Recent updates added support for C, Golang, Python, and NodeJS.                                                                  |
|   8 | Static code analysis can suggest improvements, such as using secrets and config maps.                                            |
|   9 | Conveyor leverages large language models (LLMs) for code generation and remediation using context engineering.                   |
|  10 | The system can identify problematic code lines and provide remedies for Kubernetes compatibility.                                |
|  11 | The process involves static code analysis, context engineering, LLM-based code generation, and reintegration into the codebase.  |
|  12 | Conveyor includes agents that handle compilation, validation, testing, and iterative issue fixing.                               |
|  13 | Agents help address cascading issues that arise when fixing legacy code.                                                         |
|  14 | A new memory feature saves changes made in the IDE, allowing distributed memory across the organization.                         |
|  15 | Memory enables the system to override previous generations based on user modifications.                                          |
|  16 | Demonstration shows converting RMI/IIOP code to REST endpoints, generating new REST services.                                    |
|  17 | Conveyor offers a kiosk for further questions and provides a QR code for the community project.                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6FNR4jGox9w)
