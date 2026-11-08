---
layout: default
title: "Shipping Agent Skills Safely: CI/CD, Evals, and Guardrails - Michael Larson, Christensen Solutions"
nav_order: 14
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: The speaker advocates for treating AI skills as standard software by implementing CI/CD pipelines and rigorous evaluations to ensure reliability and security.
resource: "https://www.youtube.com/watch?v=gE7VpVmyLpo"
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

The speaker advocates for treating AI skills as standard software by implementing CI/CD pipelines and rigorous evaluations to ensure reliability and security.
This approach addresses critical issues such as the potential for skills to deliver malicious attacks, the instability of models over time, and the high costs associated with using frontier models without proper testing.
By establishing version control, review processes, and automated testing with deterministic assertions, developers can verify that skills function correctly across different models and environments.
The talk highlights practical tools like Promptfoo for setting up evaluations and using LLMs as judges to handle non-deterministic outputs, while also emphasizing the importance of package managers for vetting skills in enterprise settings.
Ultimately, the speaker argues that continuous evaluation and cross-platform testing are essential for maintaining high-quality, secure, and cost-effective AI skills.

# Main Points

|   # | Main point                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                  |
|   2 | • Presentation focuses on safely distributing AI skills through CI/CD channels and evaluations                |
|   3 | • Speaker has 19+ years software engineering experience                                                       |
|   4 | • AI skills are widely used but their functionality reliability is unclear                                    |
|   5 | • Models change constantly, making it difficult to ensure skills continue working                             |
|   6 | • Skills can contain executable code and are targets for malicious attacks and backdoors                      |
|   7 | • Developers are high-value targets for attackers seeking to compromise software                              |
|   8 | • AI model costs can be excessive; need to evaluate if cheaper models could work                              |
|   9 | • Solution: treat skills like standard software with version control, testing, review processes, and releases |
|  10 | • Evaluations are like unit tests; write deterministic assertions to verify expected skill results            |
|  11 | • Use CI/CD processes to compare versions and monitor performance over time                                   |
|  12 | • Constantly reevaluate skills as models change                                                               |
|  13 | • Include adversarial test cases to simulate real-world scenarios                                             |
|  14 | • Use PromptFoo for creating YAML configuration files for skill evaluations                                   |
|  15 | • JAV can be used as a judge for evaluations at very low cost                                                 |
|  16 | • Evaluations can run in production environments to verify skill performance                                  |
|  17 | • Skills should be distributed as packages through official package managers and stores, not as files         |
|  18 | • Test skills across multiple platforms (Windows, Mac, Linux) since agents are cross-platform                 |
|  19 | • Use automated stack analysis and security scanners in CI/CD pipelines                                       |
|  20 | • For non-deterministic outputs, use an LLM as a judge to evaluate results                                    |
|  21 | • Most models can help quickly set up evaluations with examples of good and bad results                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/gE7VpVmyLpo/hqdefault.jpg)]("https://www.youtube.com/watch?v=gE7VpVmyLpo")

[Watch on YouTube](https://www.youtube.com/watch?v=gE7VpVmyLpo)
