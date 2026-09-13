---
layout: default
title:
  "MCP: The Gateway to Real-Time Human–AI Collaboration in Jupyter at Scale -
  Jake Diamond-Reivich"
nav_order: 63
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Jake from the Jupyter open source governing board introduces Jupyter
  AI v3, which was launched the previous day and brings significant new features to
  the Jupyter ecosystem. The main highlight is the adoption of the Agent Client Protocol
  (A...
resource: https://www.youtube.com/watch?v=NPcY4ccny7E
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Jake from the Jupyter open source governing board introduces Jupyter AI v3, which was launched the previous day and brings significant new features to the Jupyter ecosystem.
The main highlight is the adoption of the Agent Client Protocol (ACP), enabling users to integrate and customize AI agent personas—such as Claude, Codeex, and Gemini—directly within Jupyter Lab through a new chat interface.
These AI agents can write, debug, and edit notebook cells, access files, kernels, Git, and terminals, and can be easily configured or extended by users to suit specific needs.
The demo showcases how agents like Claude can generate entire notebooks, install necessary packages, and interact with users, all while respecting permission settings.
Jake emphasizes the flexibility and security of running Jupyter locally, the ease of integrating multiple agents, and the potential for community-built custom personas, making Jupyter Lab a powerful, AI-enabled IDE for individuals and organizations alike.

# Main Points

|   # | Main point                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------- |
|   1 | Jake from the Jupyter open source governing board presented.                                                        |
|   2 | Jupyter AI v3 launched yesterday; it's open source and in early stages.                                             |
|   3 | Jupyter AI v3 introduces Agent Client Protocol (ACP), enabling AI agent personas inside Jupyter.                    |
|   4 | Users can create custom AI personas or use existing ones like Claude, Codeex, Gemini.                               |
|   5 | AI personas can write, debug, and edit notebook cells, reducing manual notebook creation.                           |
|   6 | Agents have full tool access: files, kernels, Git, terminal, all agent-controlled via ACP.                          |
|   7 | Installing an agent’s Python package (e.g., Claude) enables its use in Jupyter with no extra setup.                 |
|   8 | Jupyter Lab Chat is a new interface allowing interaction with multiple AI personas simultaneously.                  |
|   9 | Users can define custom personas (e.g., data science assistant, Markdown expert) and have them collaborate.         |
|  10 | Persona creation involves defining personality, available tools, and message handlers; easy to package and publish. |
|  11 | ACP provides a registry of available tools (cells, terminal, kernel, Git) for agents.                               |
|  12 | ACP brings command-line tools and agents into the Jupyter environment for granular control.                         |
|  13 | Demo showed Claude agent generating a sample notebook, installing packages, and creating visualizations.            |
|  14 | Agents request user permission before accessing tools.                                                              |
|  15 | Jupyter AI v3 is installed via pip; features available out of the box.                                              |
|  16 | ACP detects available agents and tools automatically; minimal configuration needed.                                 |
|  17 | Enterprise/cloud integration possible via API keys; more work needed for large-scale platforms.                     |
|  18 | No out-of-the-box custom personas yet, but community contributions encouraged.                                      |
|  19 | Jupyter Lab/Hub is widely used in education and industry; ACP makes it AI agent agnostic.                           |
|  20 | Security: Jupyter can run fully locally; ACP allows granular control over agent tool access.                        |
|  21 | Custom personas can be restricted (e.g., tutor persona that doesn’t write code).                                    |
|  22 | Jupyter AI features may not work out-of-the-box on platforms like Databricks.                                       |
|  23 | Jake is open to feedback and ques                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=NPcY4ccny7E)
