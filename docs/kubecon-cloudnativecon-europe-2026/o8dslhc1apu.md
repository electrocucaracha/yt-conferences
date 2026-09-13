---
type: Video Note
title: "Project Lightning Talk: What's New And Exciting In Kagent? - Peter Jausovec, Maintainer"
description: "Peter, a maintainer from Solo, introduces K agent, an open-source framework for running AI agents in Kubernetes, which has been part of the CNCF since last year and has seen over 130 releases, 2,400 stars, and more than 100 contributors. K..."
resource: https://www.youtube.com/watch?v=O8DslhC1ApU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Peter, a maintainer from Solo, introduces K agent, an open-source framework for running AI agents in Kubernetes, which has been part of the CNCF since last year and has seen over 130 releases, 2,400 stars, and more than 100 contributors.
K agent consists of a Go controller, database, UI, CLI, and several CRDs, allowing users to deploy agents either declaratively—by specifying instructions, tools, skills, and models—or by building custom agents using ADK, Langraph, or QAI and running them as Docker images.
The framework supports multiple AI models, including OpenAI, Anthropic, Azure, AWS Bedrock, Colama, and AI gateways, and offers features like prompt templates, tool selection, and integration with MCP servers for tool discovery.
Recent enhancements include human-in-the-loop functionality, long-term memory storage, built-in prompts and templates, Python and Go runtime options, git-based skill fetching, distributed tracing, and voice support.
Peter invites viewers to try K agent, join the community, and attend their upcoming talk at Contrifest.
# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Peter is a maintainer of K agent from Solo.                                                                                          |
|   2 | K agent is an incubating open source project under CNCF since last year.                                                             |
|   3 | Over 130 releases, 2,400 stars, and more than 100 contributors.                                                                      |
|   4 | K agent is a framework for running AI agents in Kubernetes.                                                                          |
|   5 | Architecture includes a Go controller, database, UI, and CLI.                                                                        |
|   6 | Provides CRDs for agent creation and deployment in Kubernetes.                                                                       |
|   7 | Two agent creation options: declarative (no code, just instructions) and BYO (build your own using ADK, langraph, QAI, or crew AAI). |
|   8 | Supports multiple AI models: OpenAI, Anthropic, Azure, AWS Bedrock, Colama, and AI gateways.                                         |
|   9 | Agents can be built as Docker images.                                                                                                |
|  10 | CRDs allow model selection, system message definition, and prompt templates reuse.                                                   |
|  11 | Tools can be selected for agents via CRDs.                                                                                           |
|  12 | MCP server CRD allows pointing to existing MCP servers; tools are auto-discovered.                                                   |
|  13 | Model config CRD specifies provider, model, and Kubernetes secret for API key.                                                       |
|  14 | Weekly and bi-weekly contributor meetings; active Discord community.                                                                 |
|  15 | Recent features added:                                                                                                               |
|  16 | Human-in-the-loop for agent input confirmation or free-form input.                                                                   |
|  17 | Long-term memory storage.                                                                                                            |
|  18 | Built-in prompts and templates.                                                                                                      |
|  19 | Python and Go runtime selection for declarative agents.                                                                              |
|  20 | Git-based skill fetching and OCI image support.                                                                                      |
|  21 | Distributed tracing and 8-way trace propagation.                                                                                     |
|  22 | Voice support.                                                                                                                       |
|  23 | K agent can be tried at kagent.dev.                                                                                                  |
|  24 | Upcoming talk at Contrifest, G107, 2:30 p.m.                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=O8DslhC1ApU)