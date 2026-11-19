---
layout: default
title: "Generation-Verification Asymmetry: The Production Failure Pattern... - Birajendu Sahu, Endor Labs"
nav_order: 57
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Viraj, a Senior Engineering Manager at Endor Labs, presents a talk on the security vulnerabilities inherent in agentic Software Development Life Cycle (SDLC) flows, where AI agents handle coding, r..."
resource: "https://www.youtube.com/watch?v=XFCG5nXfvBQ"
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

Viraj, a Senior Engineering Manager at Endor Labs, presents a talk on the security vulnerabilities inherent in agentic Software Development lifecycle (SDLC) flows, where AI agents handle coding, review, and CI/CD processes.
He demonstrates that while these automated pipelines often pass standard checks and produce clean pull requests, they frequently introduce dependencies with known vulnerabilities, such as RC-level advisories, because the review agents lack concrete evidence of code reachability and rely solely on LLM knowledge.
Citing research that indicates nearly 20% of LLM-generated dependencies are hallucinated and approximately 50% contain vulnerabilities, he argues that current verification methods are insufficient due to a "generation-verification asymmetry," where generating code is cheap but verifying it authoritatively remains difficult.
To address this, he proposes a "verification-first design" that integrates deterministic evidence, such as vulnerability advisories and call graph data, directly into the coding agent’s workflow via MCP integrations or orchestrators, rather than relying on post-hoc reviews or prompt engineering alone.
This approach ensures that agents make informed decisions based on real-world security data, effectively blocking vulnerable packages and applying fixes early in the cycle, a principle he notes can be extended to other areas like license compliance and infrastructure-as-code changes.

# Main Points

|   # | Main point                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | , Viraj, a Senior Engineering Manager at Endor Labs, discusses security vulnerabilities in agentic Software Development lifecycle (SDLC) flows where AI agents handle coding, review, and CI/CD.                         |
|   2 | (e.g., PyYAML 5.3.1) based on existing repository references, passing all standard checks (lint, tests, review) while introducing RC-level advisory vulnerabilities.                                                     |
|   3 | "generation verification asymmetry": code generation is low-cost and fast, but authoritative verification remains difficult because review agents often lack concrete evidence of vulnerability reachability.            |
|   4 | , leading to approvals of vulnerable code because they cannot verify if a vulnerability is actually reachable in the application’s call graph.                                                                           |
|   5 | % of dependencies created by LLMs are hallucinated (non-existent packages), based on a USENIX study of 16 models and 574,000 applications.                                                                               |
|   6 | % of LLM-generated code includes packages with known vulnerabilities, often because models prefer the "latest" version based on outdated training data (typically 3 months old) rather than current security advisories. |
|   7 | , as these methods still lack access to real-time vulnerability databases and reachability evidence.                                                                                                                     |
|   8 | "verification-first design" that integrates an evidence gate (via MCP or plugins) into the CI pipeline before code generation or review.                                                                                 |
|   9 | , including vulnerability advisories and call graph reachability data, directly to the coding agent, allowing it to select safe versions or apply fixes rather than hallucinating or blindly upgrading.                  |
|  10 | , avoiding the need to rewrite entire agentic workflows.                                                                                                                                                                 |
|  11 | , ensuring that blocks are accompanied by actionable fixes rather than just CI failures.                                                                                                                                 |
|  12 | , schema migrations, Terraform/Helm changes, and GitHub Actions.                                                                                                                                                         |
|  13 | , enforcing systems with evidence rather than relying on prompts, and using good evidence to turn security blocks into automated fixes.                                                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XFCG5nXfvBQ/hqdefault.jpg)](https://www.youtube.com/watch?v=XFCG5nXfvBQ)

[Watch on YouTube](https://www.youtube.com/watch?v=XFCG5nXfvBQ)
