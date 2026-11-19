---
layout: default
title: "Agentic AI for Maintainers: Getting the Most From GitHub Copilot Enterprise - Nate Waddington, CNCF"
nav_order: 11
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Nate Wington, Head of Mentorship and Documentation at the CNCF, presented a new partnership with GitHub that provides Enterprise Copilot access to all CNCF project maintainers."
resource: "https://www.youtube.com/watch?v=x96duUfIJXk"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Nate Wington, Head of Mentorship and Documentation at the CNCF, presented a new partnership with GitHub that provides Enterprise Copilot access to all CNCF project maintainers.
The session detailed three levels of AI autonomy: Agent Mode for real-time pair programming, Coding Agent for asynchronous task execution via issue assignment, and Agentic Workflows for continuous, automated processes like link checking and triage.
Wington emphasized the importance of using AI to augment rather than automate work, citing research that suggests automation can negatively impact junior developer career growth, while augmentation supports stable skill development.
He demonstrated how to configure these tools using natural language instruction files, such as `copilot-instructions` and `agents.md`, to enforce project-specific coding styles, testing requirements, and behavioral constraints.
The talk included real-world examples, such as the CubeStellar project’s successful use of coding agents to merge over 1,900 PRs, and addressed security concerns, noting that while GitHub provides built-in guardrails like secret scanning, human review remains essential for validating AI-generated code and ensuring compliance with Linux Foundation AI policies.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The CNCF has partnered with GitHub to provide Enterprise Copilot access to all CNCF project maintainers, regardless of project maturity stage.                                  |
|   2 | Access to the program is requested through the CNCF service desk, where staff will assist with setup and licensing.                                                             |
|   3 | The presentation emphasizes using AI tools to augment human work rather than automate it, citing research that automation can reduce junior developer career opportunities.     |
|   4 | Agent mode functions as a real-time pair programmer within the editor, suitable for exploring codebases and providing immediate feedback during development.                    |
|   5 | Coding agents operate asynchronously in the cloud, handling well-scoped tasks like bugfixes and documentation updates by creating branches and pull requests.                   |
|   6 | Agentic workflows run continuously via GitHub Actions, capable of triggering on their own to perform repetitive tasks like link checking or cross-repo issue creation.          |
|   7 | Effective use of these tools requires specific prompts, seeding context with specs or issues, and utilizing MCP to connect across repositories.                                 |
|   8 | Copilot instruction files act as house rules for coding style and behavior, with the first 4,000 characters being the most critical for model attention.                        |
|   9 | Agent files define specific permissions and behavioral constraints for different areas of a repository, with the closest agent file taking precedence over root-level rules.    |
|  10 | Security features such as CodeQL checks and secret scanning are built into the agent workflows, but human review remains mandatory for all generated code.                      |
|  11 | The Linux Foundation AI policy states that contributors are responsible for proposed code, and projects may establish stricter internal guidelines for AI usage.                |
|  12 | Non-maintainer contributors can access some tools like code review, or apply for GitHub Pro licenses for open source maintainers to gain broader access.                        |
|  13 | Good first issues should be reserved for human contributors to foster community growth, with AI used as a learning aid rather than a replacement.                               |
|  14 | Real-world examples show high acceptance rates for agent-generated pull requests, with many merged untouched and others serving as useful starting points for human refinement. |
|  15 | Users are advised to start small with simple tasks, iterate on instruction files, and maintain strict oversight to ensure code quality and security.                            |
|  16 | Prompt injection and CI security risks are acknowledged concerns, with GitHub actively working on mitigations and the CNCF offering support for security incidents.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/x96duUfIJXk/hqdefault.jpg)](https://www.youtube.com/watch?v=x96duUfIJXk)

[Watch on YouTube](https://www.youtube.com/watch?v=x96duUfIJXk)
