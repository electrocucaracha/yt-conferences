---
layout: default
title: "The Ultimate Guide to Vibe Engineering with Streamlit (Sponsor: Snowflake)"
nav_order: 101
parent: PyCon US 2026
type: Video Note
description: 'The presentation introduces "vibe engineering," a concept coined by Andrej Karpathy that evolves beyond simple AI-assisted coding by integrating engineering principles and structured specifications...'
resource: "https://www.youtube.com/watch?v=gQYbNR6IrJg"
youtube_stats:
  view_count: 393
  like_count: 2
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

The presentation introduces "vibe engineering," a concept coined by Andrej Karpathy that evolves beyond simple AI-assisted coding by integrating engineering principles and structured specifications into the development workflow.
The speaker highlights Streamlit Agent Skills, a GitHub repository containing markdown-based instructions that teach LLMs best practices for building consistent, maintainable Streamlit applications, thereby reducing the need for iterative prompting.
A key component of this approach is the use of a `streamlit.md` specification file, which acts as a detailed blueprint for the app’s purpose, data sources, and UI requirements, allowing developers to "one-shot" the creation of complex applications with higher accuracy.
The session includes a live demonstration of using the Cortex Code CLI to generate a project management dashboard and showcases pre-built examples, such as a fraud detection dashboard and a machine learning predictor, illustrating how these tools enable rapid prototyping and interactive data visualization.
Finally, the speaker emphasizes that while AI accelerates code generation, the focus should shift toward refining user experience and leveraging shared specifications to ensure reproducibility and collaboration across teams.

# Main Points

|   # | Main point                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Andrej Karpathy coined the term "vibe coding" for conversing with AI to generate code and later introduced "vibe engineering" to describe using engineering principles where AI is part of the tech stack. |
|   2 | The session focuses on an ultimate guide to vibe engineering with Streamlit, covering principles for building applications agentically.                                                                    |
|   3 | Cortex Code CLI is introduced as a tool similar to Claude Code but designed for data, offering awareness of Snowflake database schemas, roles, and policies.                                               |
|   4 | Streamlit agent skills are available in a GitHub repository and consolidate best practices into skill.md files to guide AI coding assistants.                                                              |
|   5 | The workflow involves using a streamlit.md file as a spec or plan that the AI agent reads to create the application, aiming for a one-shot result that is 80% complete.                                    |
|   6 | Agent skills function like cooking recipes for LLMs, providing instructions on layout, session state, and available functions to ensure consistent and maintainable app structures.                        |
|   7 | Without agent skills, AI may recreate patterns from scratch, resulting in inconsistent app structures and requiring iterative prompting to achieve desired outcomes.                                       |
|   8 | The Streamlit agent skills repository includes nine dashboard templates, eight theme templates, and over 17 sub-skills for building complex, feature-rich applications.                                    |
|   9 | Specific skills cover building chatbots, multi-page apps, managing session state for app memory, and optimizing performance through caching and fragment loading.                                          |
|  10 | Streamlit apps offer high customizability, including branding colors, custom fonts, Material icons, and direct LaTeX rendering for academic or technical content.                                          |
|  11 | The anatomy of a skill.md file includes headings, rules, and guardrails that encode best practices, reducing the need for developers to manually implement complex features.                               |
|  12 | AI harnesses trigger specific skills based on user prompts, such as invoking a chatbot skill when asked to add a chatbot or a performance skill when the app is slow.                                      |
|  13 | Users can create custom skills for missing functionalities and contribute them to the repository to automate specific workflows.                                                                           |
|  14 | The agentic workflow consists of four steps: providing intent, routing the agent to the relevant skill, generating code, and iterating based on feedback.                                                  |
|  15 | Spec-driven development using streamlit.md provides a blueprint for the LLM, resulting in a more reliable starting point compared to ad-hoc vibe coding.                                                   |
|  16 | Vibe coding democratizes development for domain experts but suffers from non-determinism, where the same prompt can yield vastly different results.                                                        |
|  17 | Providing a concrete spec ensures that 80% of the time the generated app is similar to the desired outcome, reducing the need for extensive iteration.                                                     |
|  18 | Markdown files like agents.md, skill.md, and streamlit.md serve as sources of truth for AI, with agents.md storing project rules and long-term memory for the AI.                                          |
|  19 | The streamlit.md file acts as a portable spec that can be shared with team members to reproduce an application, compressing long conversations into a single document.                                     |
|  20 | A live demo demonstrated building a project management app with milestones, capacity planning, and GitLab integration using the spec-driven approach.                                                      |
|  21 | Pre-generated examples included a fraud detection dashboard with interactive charts and a machine learning predictor app with real-time parameter sliders.                                                 |
|  22 | The speaker noted that while app creation is becoming easier, refining the user experience and ensuring usability remains a critical and time-consuming aspect of development.                             |
|  23 | Streamlit is open source and free to use, with a version on the Snowflake platform offering additional governance features.                                                                                |
|  24 | Testing Streamlit apps can be done using the app test directory in the GitHub repository or by using Playwright, with AI capable of writing these tests.                                                   |
|  25 | A free Streamlit AI Hack Night event was announced with prizes including a mechanical keyboard and a Transformer Lego set.                                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/gQYbNR6IrJg/hqdefault.jpg)](https://www.youtube.com/watch?v=gQYbNR6IrJg)

[Watch on YouTube](https://www.youtube.com/watch?v=gQYbNR6IrJg)
