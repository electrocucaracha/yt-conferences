---
layout: default
title:
  "From Chaos To Clarity: How MCP Transforms Incident Response - Sebastian Villanelo
  & Rocío Bayon"
nav_order: 27
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The video discusses the challenges engineers face when responding to
  incidents, particularly the productivity loss caused by constant context switching
  between multiple tools and platforms. To address this, the presenters introduce
  MCP apps...
resource: https://www.youtube.com/watch?v=T8sx0-JP1DM
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

The video discusses the challenges engineers face when responding to incidents, particularly the productivity loss caused by constant context switching between multiple tools and platforms.
To address this, the presenters introduce MCP apps, which integrate incident management workflows directly into the developer’s IDE, such as Visual Studio Code, allowing access to alerts, logs, timelines, and response actions in one place.
They demonstrate how the new system leverages PagerDuty’s advanced agents—including SR, describe, chief, and insights agents—to automate triage, retrieve relevant data, and suggest next steps, all while keeping a human in the loop for accountability and critical decisions.
The solution also supports cloud desktop environments and includes features like service dependency graphs and on-call compensation reports.
Ultimately, the presenters emphasize that MCP apps reduce burnout, speed up incident resolution, and help engineers maintain focus, with future plans for multi-agent workflows and ongoing community involvement.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Developers often face interruptions from incident alerts, leading to context switching and reduced productivity.                      |
|   2 | Context switching between tools (Slack, PagerDuty, GitHub, etc.) increases the risk of mistakes and makes it harder to recover focus. |
|   3 | The team aimed to centralize incident context within the developer’s IDE to minimize tool-switching.                                  |
|   4 | They built an integration that brings alerts, logs, timelines, and response workflows directly into the IDE.                          |
|   5 | The solution uses MCP apps and integrates PagerDuty Advanced agents (Describe, Chief, Insights, SR).                                  |
|   6 | The SR agent retrieves logs, runbooks, and incident context from various sources (e.g., Elasticsearch, CloudWatch, Confluence).       |
|   7 | All actions performed in the MCP app are recorded in the incident audit trail for accountability.                                     |
|   8 | The architecture involves an MCP server that discovers and enables MCP apps in the IDE.                                               |
|   9 | The system reduces cognitive load and keeps the human responder in the loop for critical actions.                                     |
|  10 | Incident triage, analysis, and resolution can be performed directly in Visual Studio Code or Cloud Desktop.                           |
|  11 | The incident command center MCP app provides a unified view for triage, logs, alerts, and actions.                                    |
|  12 | The SR agent suggests next steps and summarizes incidents based on retrieved data.                                                    |
|  13 | The integration supports multiple log vendors and service dependency visualization.                                                   |
|  14 | An on-call compensation report tracks responder hours, including business hours and holidays.                                         |
|  15 | MCP apps are currently experimental and available under the PagerDuty MCP server.                                                     |
|  16 | Future plans include multi-agent workflows, where agents coordinate actions and humans supervise.                                     |
|  17 | Benefits include reduced burnout, faster incident resolution, and improved developer focus.                                           |
|  18 | Community participation is encouraged via documentation, live streams, and feedback.                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=T8sx0-JP1DM)
