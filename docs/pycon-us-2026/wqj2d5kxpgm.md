---
layout: default
title: "The Agent That Turned On-Call Chaos Into a Single Slack Thread - Angelik Laboy Torres"
nav_order: 12
parent: PyCon US 2026
type: Video Note
description: "Angel Clavo Torres presents a solution to the chaos of on-call engineering by introducing an AI agent that automates incident response within Slack."
resource: "https://www.youtube.com/watch?v=WQJ2d5KXpGM"
youtube_stats:
  view_count: 161
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

Angel Clavo Torres presents a solution to the chaos of on-call engineering by introducing an AI agent that automates incident response within Slack.
The agent autonomously gathers context from tools like Datadog and PagerDuty, analyzes metrics, and provides a clear hypothesis for resolution, such as recommending a rollback, while tagging the appropriate on-duty engineer.
Unlike deterministic Python scripts that follow a fixed sequence, this agent uses natural language instructions and specific tools to make contextual decisions, distinguishing between simple tasks and complex scenarios requiring human judgment.
Built on the Retour platform, the system utilizes webhooks to trigger workflows, Python code blocks for precise data processing, and a root cause analyzer that acts as a digital runbook to ensure accuracy.
The presentation concludes by demonstrating how this setup creates an auditable trail of decisions, reduces unnecessary human intervention, and allows for version control of the agent’s logic, ultimately making on-call duties more efficient and less disruptive.

# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces an AI agent designed to automate incident response and reduce Slack chaos for engineering teams.                                               |
|   2 | Traditional on-call workflows involve high context switching, requiring engineers to manually check Datadog, Amazon, and ticketing systems like Linear or Jira.            |
|   3 | The proposed solution consolidates incident context, metrics, and recommended actions into a single Slack message to streamline the process.                               |
|   4 | The agent autonomously researches the issue, provides a hypothesis, tags the responsible person, and suggests specific actions such as rolling back to a previous version. |
|   5 | An agent is defined as an autonomous system that uses tools to achieve a goal, differing from deterministic Python scripts by its ability to adapt to variable contexts.   |
|   6 | The presenter uses the Retour platform to build the agent, which allows for visual workflow creation and agent configuration via natural language instructions.            |
|   7 | Effective agent creation requires defining a clear character or role, similar to directing an actor, to ensure the AI behaves within expected boundaries.                  |
|   8 | Operational constraints are explicitly set to prevent destructive actions, requiring human approval for escalations or rollbacks to maintain accountability.               |
|   9 | The agent's tone is customized to be concise and use engineering vocabulary, avoiding unnecessary fluff for technical teams.                                               |
|  10 | The platform supports multiple AI models, including Anthropic, AWS, and ChatGPT, allowing users to select the most suitable model for their needs.                         |
|  11 | Tools are defined with specific names, descriptions, and parameters, functioning like Python functions to ensure precise data handling.                                    |
|  12 | Python code blocks are integrated into the workflow to perform accurate calculations and data cleaning, reducing the risk of AI hallucinations.                            |
|  13 | Resources act as pre-configured API connections, enabling seamless access to data sources without repetitive setup for each new agent.                                     |
|  14 | A root cause analyzer acts as a digital runbook, applying predefined rules to determine appropriate responses based on incident severity.                                  |
|  15 | The system posts formatted updates to Slack and creates audit trails in Linear, ensuring visibility and accountability for all decisions made.                             |
|  16 | Webhooks are used to trigger the agent automatically when incidents occur in PagerDuty, avoiding the inefficiency of timer-based polling.                                  |
|  17 | The platform supports version control by connecting to GitHub, allowing users to track changes, view history, and debug specific issues in production.                     |
|  18 | The agent can be invoked via API, though the visual interface is recommended for easier configuration and management of complex workflows.                                 |
|  19 | The ultimate goal is to reduce unnecessary on-call burden by providing clear, actionable insights and maintaining a comprehensive record of incident resolution.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WQJ2d5KXpGM/hqdefault.jpg)](https://www.youtube.com/watch?v=WQJ2d5KXpGM)

[Watch on YouTube](https://www.youtube.com/watch?v=WQJ2d5KXpGM)
