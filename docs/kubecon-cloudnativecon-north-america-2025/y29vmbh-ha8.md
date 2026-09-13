---
layout: default
title:
  "1000 Clusters, 1 Brain: Salesforce’s Approach To Self-Healin... Vikram Venkataraman
  & Srikanth Rajan"
nav_order: 2
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The session, led by Vikramatraan from AWS and Shri Kant from Salesforce,
  focused on the challenges of managing Kubernetes clusters at scale and how AI ops
  can address these issues. Vikramatraan described the overwhelming complexity faced
  by...
resource: https://www.youtube.com/watch?v=Y29VmBH-HA8
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The session, led by Vikramatraan from AWS and Shri Kant from Salesforce, focused on the challenges of managing Kubernetes clusters at scale and how AI ops can address these issues.
Vikramatraan described the overwhelming complexity faced by on-call engineers, such as sifting through thousands of alerts and disparate monitoring tools, and emphasized the need for intelligent systems that can correlate telemetry signals to reduce troubleshooting time.
He outlined the architecture of AI ops frameworks, highlighting the role of specialized agents that analyze metrics, logs, and events, and can even perform remediation actions with human oversight.
Shri Kant shared Salesforce’s journey in automating operations for their Hyperforce Kubernetes platform, detailing the evolution from siloed tools to a multi-agent AI-powered remediation loop that integrates with existing systems and enforces strict guardrails for safety.
Early results show significant reductions in human toil and troubleshooting time, though challenges remain in connecting complex failure scenarios and improving AI’s contextual understanding, with future efforts aimed at building knowledge graphs and enhancing feedback loops to further scale and automate operations.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Getting paged at 3:00 a.m. and troubleshooting alert storms is a persistent issue for engineers.                                                                     |
|   2 | Intelligent systems that correlate telemetry signals can help make faster decisions; AI ops can assist with this.                                                    |
|   3 | Managing large-scale Kubernetes clusters is highly complex, similar to controlling traffic on multiple busy interstates.                                             |
|   4 | On-call engineers face challenges such as isolating noise from real issues, gathering information across complex architectures, and using multiple monitoring tools. |
|   5 | Lack of runbooks increases mean time to remediate operational issues.                                                                                                |
|   6 | The main problem is the inability to correlate vast telemetry signals, leading to operational inefficiencies.                                                        |
|   7 | AI ops is not new; traditional forms include anomaly detection, predictive autoscaling, and intelligent automation.                                                  |
|   8 | AI ops powered by LLMs can correlate signals, identify problems, determine root causes, suggest fixes, and prevent future issues.                                    |
|   9 | Agents are fundamental to AI ops frameworks; they have specific goals, evaluation logic, access to tools, memory, and can perform actions.                           |
|  10 | Scaling requires an agentic framework to manage multiple agents, configure runtimes, knowledge bases, and permissions.                                               |
|  11 | A prototype was built using EKS, KGPD operator, Argo CD controller, and Prometheus, with agents for metrics, logs, and remediation.                                  |
|  12 | Collaborator agent provides a UI for engineers to interact with AI ops solutions.                                                                                    |
|  13 | At Salesforce, the Hyperforce Kubernetes platform team manages 1,400+ clusters, millions of pods, and hundreds of thousands of nodes.                                |
|  14 | Existing tools were siloed, had high learning curves, and lacked feedback loops, leading to high toil.                                                               |
|  15 | AI agents were introduced incrementally, starting with an on-call report agent and a cube cuddle agent integrated with Slack.                                        |
|  16 | Anomaly detection agent automates weekly analysis and triage, saving significant engineer time.                                                                      |
|  17 | Multi-agent architecture includes manager, worker, and remediation agents, leveraging existing tools and runbook                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Y29VmBH-HA8)
