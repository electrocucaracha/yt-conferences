---
layout: default
title: "From Toil To Triumph: Harnessing Agentic AI To Streamline Infrastructure as Code - Jodee Varney"
nav_order: 11
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "Jod, a product manager at Cisco’s Outshift team, presents a talk on applying Agentic AI to reduce toil in Infrastructure as Code (IaC) workflows, specifically focusing on OpenTofu and Terraform pul..."
resource: "https://www.youtube.com/watch?v=y0xOnbV862k"
youtube_stats:
  view_count: 556
  like_count: 17
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

Jod, a product manager at Cisco’s Outshift team, presents a talk on applying Agentic AI to reduce toil in Infrastructure as Code (IaC) workflows, specifically focusing on OpenTofu and Terraform pull request reviews.
The core challenge addressed is the complexity of managing large codebases, module creep, and policy consistency, where existing generic AI tools often fail to provide consistent or high-quality insights.
To solve this, the team developed a hierarchical multi-agent system using LangGraph, which employs a supervisor to route tasks to specialized agents for code review, documentation, and static analysis, thereby avoiding the limitations of monolithic prompts.
The system is evaluated against over 700 historical pull requests to measure performance, with plans to further refine it by adding user instructions and breaking down complex review tasks into more granular agents.
Additionally, the speaker highlights the launch of "Agency," a new open-source collective aimed at creating an "Internet of Agents" that enables the discovery, interoperability, and reuse of specialized AI agents across different ecosystems, moving beyond siloed, runtime-bound implementations.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on applying Agentic AI to Infrastructure as Code (IaC) using OpenTofu and Terraform to reduce user toil in GitOps workflows.                                                  |
|   2 | Agentic applications are viewed as standard workloads that require resource management, while also serving as tools to aid in operational tasks.                                               |
|   3 | A new open source collective called Agency has launched to support the "Internet of Agents," aiming to enable interoperability among vast quantities of AI agents.                             |
|   4 | The primary use case involves inserting AI agents into the pull request review stage of a GitOps workflow to provide recommendations while keeping humans in the loop.                         |
|   5 | Key user pain points include module creep, duplicate logic, inconsistent policy application, and the difficulty of managing large codebases with complex dependencies.                         |
|   6 | Agents are defined as software acting autonomously within defined boundaries, often orchestrated by frameworks like LangGraph, Crew, or AutoGen.                                               |
|   7 | An agentic approach breaks problems into task-specific agents, allowing for the selection of optimal foundation models and reduced hallucination through targeted context.                     |
|   8 | Challenges in building agentic systems include determining the number of agents required, defining task specificity, and managing resource costs compared to monolithic prompts.               |
|   9 | Experimentation showed that monolithic prompts for code review yielded inconsistent results, leading to a hypothesis that task-specific agents with consolidated responses improve robustness. |
|  10 | The current system version (V2) uses a hierarchical approach with a supervisor agent routing tasks to seven specialized agents, including a PR title reviewer and code consolidator.           |
|  11 | A parallel Service Request (SR) team built agents for self-service workflows, such as deploying sandboxes and generating Kubernetes deployment code with multiple reflection steps.            |
|  12 | The system is tested against a copy of a production environment containing over 700 pull requests to assess performance without disrupting the live repository.                                |
|  13 | Demonstrations showed the system successfully identifying duplicate AWS resources and improving pull request descriptions based on minimal input from Jira tickets.                            |
|  14 | The orchestration layer uses LangGraph, with deterministic tools like static analyzers integrated to provide initial feedback to code reviewer agents.                                         |
|  15 | Evaluation methods involve categorizing pull requests by problem area and using both LLMs and human evaluators to measure the quality of agent responses.                                      |
|  16 | Key learnings include the necessity of a router or supervisor agent for easy system extension and the high effort required to tune highly specialized agents.                                  |
|  17 | There is a strong desire to reuse agents from a shared ecosystem to avoid rebuilding specialized components, promoting the concept of an open, interoperable agent network.                    |
|  18 | The Agency collective seeks contributions to specifications and architecture, encouraging users to publish, discover, and compose agents for collaborative infrastructure tasks.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/y0xOnbV862k/hqdefault.jpg)](https://www.youtube.com/watch?v=y0xOnbV862k)

[Watch on YouTube](https://www.youtube.com/watch?v=y0xOnbV862k)
