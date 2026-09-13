---
layout: default
title:
  "Project Lightning Talk: Safe By Design: AI-Powered Auto-Healing For SREs -
  Arik Alon, Maintainer"
nav_order: 288
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Ari, CEO of Robusta and maintainer of Holmes GPT, introduces Holmes GPT
  as an open-source AI SRE agent that connects to various observability data sources
  like Prometheus, Loki, Datadog, and New Relic to assist with incident investigation
  a...
resource: https://www.youtube.com/watch?v=LW8Z8jOGfZE
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

Ari, CEO of Robusta and maintainer of Holmes GPT, introduces Holmes GPT as an open-source AI SRE agent that connects to various observability data sources like Prometheus, Loki, Datadog, and New Relic to assist with incident investigation and remediation.
When an incident occurs, engineers can ask Holmes GPT questions about issues such as pod crashes or latency, and the agent analyzes the data to provide root cause analysis and potential fixes within minutes.
Ari shares a real example where Holmes detected a significant drop in application metrics after a PR merge, identified the root cause as a cache misconfiguration, and automatically opened a PR with a fix.
Holmes operates by following user-defined health checks, querying relevant data sources, and executing remediation steps, which can include opening PRs or triggering automated actions.
The tool is used by multiple companies, has been submitted to the CNCF, and can be integrated with various remediation handlers for flexible incident response.

# Main Points

|   # | Main point                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------- |
|   1 | Ari is the CEO of Robusta and a maintainer of Holmes GPT.                                                   |
|   2 | Holmes GPT is an open-source AI SRE agent.                                                                  |
|   3 | Connects to observability data sources like Prometheus, Loki, Datadog, New Relic, and cloud providers.      |
|   4 | Used for troubleshooting by querying data and providing root cause analysis and fixes.                      |
|   5 | Holmes can perform remediation actions.                                                                     |
|   6 | Holmes is used by many companies and was submitted to CNCF with Microsoft, which uses it for Azure CLI.     |
|   7 | Example incident: After merging a PR, application metrics dropped by 70%.                                   |
|   8 | Holmes detected the incident within minutes and notified via Slack.                                         |
|   9 | Holmes identified deployment version 241 as the cause, with drops in cache hit ratio and increased latency. |
|  10 | Holmes visualized the data and found the root cause: TTL cache set to zero, disabling the cache.            |
|  11 | Holmes opened a PR with a fix for the issue.                                                                |
|  12 | User only needed to review and merge the PR.                                                                |
|  13 | Holmes health checks are defined in human language to specify post-deployment actions.                      |
|  14 | Health checks include monitoring deployment health, logs, latency metrics, and degradation thresholds.      |
|  15 | If an issue is detected, Holmes can attempt a fix or suggest a rollback PR.                                 |
|  16 | Holmes operator executes health checks, queries data sources, analyzes logs, and interacts with GitHub.     |
|  17 | Holmes supports human-in-the-loop remediation and can integrate with other remediation handlers.            |
|  18 | Can trigger GitHub Actions or run kubectl commands for remediation.                                         |
|  19 | Holmes can automate various remediation tasks.                                                              |
|  20 | Contact available at the project pavilion or Robusta booth.                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=LW8Z8jOGfZE)
