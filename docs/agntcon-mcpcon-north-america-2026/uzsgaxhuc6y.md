---
layout: default
title: "Bridging Agentic Reasoning and Deterministic Execution - Marcio Klepacz, ComparaCAR"
nav_order: 155
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Marcio argues that using non-deterministic AI agents for routine, repetitive tasks like website deployment is inefficient and risky, citing a real-world incident where an agent took a site down dur..."
resource: "https://www.youtube.com/watch?v=UZsgAXhuc6Y"
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

Marcio argues that using non-deterministic AI agents for routine, repetitive tasks like site deployment is inefficient and risky, citing a real-world incident where an agent took a site down during a standard deploy.
He proposes a hybrid approach where agents are used for exploration, planning, and writing Directed Acyclic Graphs (DAGs), while deterministic orchestrators handle the actual execution of defined workflows.
This method ensures reliability, observability, and cost efficiency by allowing tasks to run on schedules without consuming tokens for every execution.
In a live demonstration using the Gust orchestrator, Marcio showed how an agent can generate a DAG to scrape car offers, validate the code, and set up a daily schedule, illustrating how agents can bridge the gap between flexible reasoning and rigid, repeatable processes.
The presentation concludes by emphasizing that replacing LLM calls with deterministic code for known steps results in better, more predictable outcomes, encouraging developers to identify which parts of their agentic workflows can be converted into reusable, deterministic scripts.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , resulting in the site going down because the agent re-reasoned through known steps instead of executing a fixed script.                          |
|   2 | % of its deployments are now made through AI agents, highlighting a trend of using non-deterministic tools for deterministic tasks.                |
|   3 | (checking commits, running tests, linting, building, deploying) are known, fixed steps that do not require LLM reasoning for execution.            |
|   4 | , planning, and investigating failures, but inefficient for executing predefined, repetitive policies.                                             |
|   5 | (DAGs) provide a deterministic workflow structure where steps flow in one direction without loops, defined in files like YAML or code.             |
|   6 | , fixed retry policies, timeouts, deterministic outcomes, and unique run IDs for better observability and debugging.                               |
|   7 | , validate, and trigger the DAG, while the orchestrator handles execution.                                                                         |
|   8 | , CLI for validation, and MCP (Model Context Protocol) for interactions like triggering runs and reading logs.                                     |
|   9 | , ensuring critical business data is updated reliably.                                                                                             |
|  10 | , an agent (Claude) was used to generate a DAG for fetching data, which included an approval gate for human verification before execution.         |
|  11 | , the agent is no longer needed for routine execution; the workflow can be scheduled to run automatically, saving tokens and ensuring consistency. |
|  12 | , runtime secrets for security, and the ability to embed other agents or LLMs within specific tasks for conditional logic.                         |
|  13 | , making fixes, and restarting the process, after which the system returns to deterministic operation.                                             |
|  14 | , including Gust, Apache Airflow, Dexter, and Dagu, though the specific syntax for defining tasks varies between them.                             |
|  15 | , but replace them with deterministic code (DAGs) for repetitive execution to ensure reliability and cost-efficiency.                              |
|  16 | , deterministic workflows.                                                                                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UZsgAXhuc6Y/hqdefault.jpg)](https://www.youtube.com/watch?v=UZsgAXhuc6Y)

[Watch on YouTube](https://www.youtube.com/watch?v=UZsgAXhuc6Y)
