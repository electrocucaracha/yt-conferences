---
layout: default
title: "Operational Automation in OpenStack Using LLM and MCP:  Real World AI Agent Use Cases"
nav_order: 16
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation by K Cloud engineers details the implementation of AI agents to automate OpenStack operations, addressing the complexity of resource management and root cause analysis for both us..."
resource: "https://www.youtube.com/watch?v=BsLKbDNJntE"
youtube_stats:
  view_count: 358
  like_count: 8
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

This presentation by K Cloud engineers details the implementation of AI agents to automate OpenStack operations, addressing the complexity of resource management and root cause analysis for both users and operators.
The team evaluated Retrieval-Augmented Generation (RAG) but found it insufficient for real-time state awareness and causal inference, leading them to adopt an Agent AI approach that enables a closed-loop cycle from natural language input to verified execution.
They selected Kagent, a CNCF sandbox project, as the primary framework due to its no-code capabilities, built-in UI, and strong community support, utilizing it to orchestrate specialized agents for OpenStack resource management and observability.
The system integrates with real-time infrastructure via Model Context Protocol (MCP) servers, allowing the AI to query live states from components like Nova and Cinder, and to interact with observability stacks such as Grafana and Prometheus.
Through system prompts and an intent-first analysis approach, the agents minimize unnecessary queries and ensure safe, accurate execution, as demonstrated in live demos where the system successfully created instances, diagnosed configuration errors, and guided users through corrective actions.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces operational automation in OpenStack using AI agents to address challenges in user convenience and operator troubleshooting.                                              |
|   2 | Users face difficulties creating virtual machines due to complex parameter requirements and resource interdependencies, while operators struggle with root cause analysis across diverse components. |
|   3 | Retrieval-Augmented Generation (RAG) was initially considered but found insufficient due to a lack of real-time state awareness and weak root cause inference capabilities.                          |
|   4 | Agent AI was selected as the primary approach because it enables a closed loop from understanding to execution, allowing for automated operational actions and reduced time to resolution.           |
|   5 | The agent AI system integrates with real-time states and external systems, such as Nova, Cinder, Keystone, and observability tools, to ensure decisions are based on verified facts.                 |
|   6 | Core components of the system include a large language model as the brain, system prompts defining behavior rules, and MCP servers connecting to external resources.                                 |
|   7 | The workflow involves receiving user input, making initial LLM calls with context, deciding on tool usage, executing actions via MCP servers, and iterating until a final response is generated.     |
|   8 | Kagent was chosen as the primary tool for building the agent due to its no-code capabilities, built-in UI, and status as a CNCF sandbox project with strong community backing.                       |
|   9 | Kagent is structured around an agent catalog composed of agents, tools, and frameworks, designed for easy installation and execution on Kubernetes.                                                  |
|  10 | The K Cloud Next platform architecture runs OpenStack on Kubernetes with unified networking, supporting an AI automation layer that connects LLMs with infrastructure via MCP servers.               |
|  11 | The observability system utilizes the Cloud Native LGTM stack with OpenTelemetry, collecting data from application, platform, and infrastructure layers into Mimir, Loki, and Tempo.                 |
|  12 | Kagent manages custom resources for agents and remote MCP servers, allowing users to define custom agents like the OpenStack agent alongside built-in ones like the observability agent.             |
|  13 | The main agent acts as a super agent orchestrating the OpenStack and observability agents using the A2A protocol for complex workflows.                                                              |
|  14 | The OpenStack MCP server was developed using Streamable HTTP to enable persistent bidirectional communication, overcoming limitations of standard HTTP for real-time coordination.                   |
|  15 | System prompts define agent behavior, safety policies, and decision-making rules, ensuring stable automation and accurate interpretation of user intent.                                             |
|  16 | An intent-first analysis approach was implemented to classify requests as action or analysis types, reducing unnecessary follow-up questions and improving efficiency.                               |
|  17 | A demo demonstrated creating an instance via natural language, where the agent generated an execution plan, requested confirmation, and attempted creation despite an initial error.                 |
|  18 | The main agent performed automated error analysis by gathering instance details, checking logs, and identifying an incorrect secret configuration as the root cause.                                 |
|  19 | After correcting the Helm chart configuration and redeploying, the agent successfully created the instance, demonstrating the ability to identify, fix, and verify issues.                           |
|  20 | Future plans include adding RAG to the agent for documentation-based reasoning and continuously refining the system to enhance intelligence and reliability.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BsLKbDNJntE/hqdefault.jpg)](https://www.youtube.com/watch?v=BsLKbDNJntE)

[Watch on YouTube](https://www.youtube.com/watch?v=BsLKbDNJntE)
