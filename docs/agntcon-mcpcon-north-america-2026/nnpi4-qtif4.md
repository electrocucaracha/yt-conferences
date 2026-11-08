---
layout: default
title: "Stop Writing Agents, Declare Them: Declarative Agent... - Chris Knuteson, A Place For Mom"
nav_order: 26
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Chris Knutson, Director of Agentic at A Place for Mom, presents a framework for treating AI agents as versioned, declarative artifacts to solve issues of non-determinism and lack of observability i..."
resource: "https://www.youtube.com/watch?v=nNPi4-QtIF4"
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

Chris Knutson, Director of Agentic at A Place for Mom, presents a framework for treating AI agents as versioned, declarative artifacts to solve issues of non-determinism and lack of observability in production environments.
He explains that their previous setup, which relied on dynamic prompt loading from LangFuse, created multiple sources of truth and made it difficult to verify which specific model configurations were actually running.
To address this, the team implemented an AI gateway and a standardized agent spec that bundles the model, prompts, tools, and skills into a single, immutable release artifact managed through Git.
This approach enables predictable deployments, automated CI/CD pipelines, and the ability to roll back to specific versions, while also facilitating cost optimization by routing specialized sub-tasks to cheaper, local hardware models like Ollama.
By integrating this spec-based architecture with AWS Agent Core, the company has achieved improved governance, traceability, and scalability for both internal review agents and customer-facing services, ultimately allowing for safer, more transparent, and more efficient agentic workflows.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                  |
|   2 | , which helps connect families with care services                                                                                                                                             |
|   3 | : Multiple sources of truth existed (Git, LangFuse, prompt packages) with no link to actual execution                                                                                         |
|   4 | : Declare agents as single-version documents using agent specifications                                                                                                                       |
|   5 | , metrics, emergency switches, and PII detection                                                                                                                                              |
|   6 | : label, execution environment, model harness, specification, prompt, skills, tools                                                                                                           |
|   7 | , enabling automated deployment and testing                                                                                                                                                   |
|   8 | ~2,000 reviews delivered                                                                                                                                                                      |
|   9 | : Switched from expensive Opus 4.8 to local Llama instances (ornith 1.5) with orchestrator delegation, saving ~$10k monthly                                                                   |
|  10 | : candidate testing → canary validation → production deployment with revert capability                                                                                                        |
|  11 | : name launches, separate deployment, enable activate/deactivate/revert, maintain third-party control plane visibility, keep authority outside agents, treat agents as reproducible artifacts |
|  12 | : triaging agents for CVE monitoring, improving reviewer, building internal agents, adding linting to specification compiler                                                                  |
|  13 | ; specification may be published on GitHub                                                                                                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/nNPi4-QtIF4/hqdefault.jpg)]("https://www.youtube.com/watch?v=nNPi4-QtIF4")

[Watch on YouTube](https://www.youtube.com/watch?v=nNPi4-QtIF4)
