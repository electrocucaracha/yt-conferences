---
layout: default
title: "The Autonomous Pipeline: Using Agentic AI to Automate FCRA... - Gokul Prabagaren, CapitalOne"
nav_order: 98
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Google Prabhakaran, a Lead Software Engineer at Capital One, presented a framework for integrating Agentic AI into the API development lifecycle to enhance compliance with the Fair Credit Reporting..."
resource: "https://www.youtube.com/watch?v=DQuw4OfmEck"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Google Prabhakaran, a Lead Software Engineer at Capital One, presented a framework for integrating Agentic AI into the API development lifecycle to enhance compliance with the Fair Credit Reporting Act (FCRA) and data depersonalization.
He outlined a pipeline utilizing four specialized agents to address traditional inefficiencies such as inconsistent manual reviews and under-leveraged OpenAPI specifications.
The first agent, the API Coach, codifies enterprise standards into re-executable rules, allowing engineers to validate their specifications against a consistent baseline before submission, thereby shifting governance left.
The second and third agents, the Change Set Detector and the Develop from Change Set agent, work together to perform semantic diffs on approved specs and automatically generate code, tests, and pull requests for new endpoints, while maintaining a human-in-the-loop for verification.
Finally, the PR Reviewer agent conducts a comprehensive gap analysis against the main branch, applying codified institutional knowledge across nine pillars including security and reliability to ensure consistent, high-quality code reviews.
This automated approach resulted in an 80% reduction in delivery time for the initial endpoint implementation, with expected further efficiency gains in subsequent iterations.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | & Context**: Google Prabhakaran, Lead Software Engineer at Capital One, presented on using Agentic AI for API development, specifically within the context of FCRA compliance and data depersonalization.                                                                                                                               |
|   2 | & Depersonalization**: The Fair Credit Reporting Act (FCRA) protects consumer credit data by defining permissible purposes for access. Depersonalization is the process of stripping personally identifiable information (PII) from data to enable compliant analysis and modeling.                                                     |
|   3 | : Traditional API development involved manual OpenAPI spec reviews by a Center of Excellence (CoE), which was time-consuming, prone to inconsistent human interpretation of rules, and under-leveraged the potential of the specifications.                                                                                             |
|   4 | : API Coach**: This agent codifies enterprise standards (naming conventions, status codes, HTTP verbs, pagination) into re-executable rules. It provides a consistent score and feedback before submission, shifting governance left and augmenting the human review process with "governance as code."                                 |
|   5 | : Change Set Detector**: This agent establishes a moving baseline for approved APIs. It performs a semantic diff (rather than a noisy text diff) to identify meaningful changes, such as new endpoints or payload modifications, producing a delta specification artifact.                                                              |
|   6 | : Develop from Change Set**: Consuming the delta spec from the previous agent, this agent automatically generates code and Gherkin-format tests for new endpoints. It executes the pipeline and raises a Pull Request (PR), moving the task from a "pending" to a "completed" state.                                                    |
|   7 | : The pipeline is split into distinct agents to allow human review of the semantic diff before code generation, ensuring the correct input is fed into the automation.                                                                                                                                                                  |
|   8 | : PR Reviewer**: This agent gathers context, performs a gap analysis between the PR and the main branch, and reviews code against nine pillars (architecture, security, reliability, etc.). It codifies institutional knowledge into consistent rules and includes "stop-the-line" conditions for critical issues like exposed secrets. |
|   9 | : The system eliminates review bias and inconsistency, leverages the OpenAPI spec as a single source of truth, and automates the end-to-end execution from spec to PR.                                                                                                                                                                  |
|  10 | : Implementation on a data depersonalization API resulted in an 80% time reduction in delivering endpoints in the first iteration, with subsequent iterations expected to be even faster due to the established pipeline.                                                                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/DQuw4OfmEck/hqdefault.jpg)](https://www.youtube.com/watch?v=DQuw4OfmEck)

[Watch on YouTube](https://www.youtube.com/watch?v=DQuw4OfmEck)
