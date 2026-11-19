---
layout: default
title: The MCP Features Bloomberg Built for High Stakes Financial AI
nav_order: 80
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Anya, a product group lead at Bloomberg, discusses the critical importance of building trustworthy infrastructure for AI applications in the high-stakes financial sector."
resource: "https://www.youtube.com/watch?v=z6SuFQYClQI"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Anya, a product group lead at Bloomberg, discusses the critical importance of building trustworthy infrastructure for AI applications in the high-stakes financial sector.
She explains that while Bloomberg has integrated AI for over 15 years, the recent launch of their Agent AI application, Ask B, has necessitated a focus on three core principles: deriving answers from trusted sources, providing transparent attribution for verification, and solving real user problems.
To achieve this, Bloomberg emphasizes the need for robust runtime visibility and controls, noting that standard Model Context Protocol (MCP) implementations often lack the necessary out-of-the-box guardrails and governance required for production reliability.
The speaker highlights two specific MCP contributions developed through the financial services interest group: the Interceptor framework, which allows for the validation and transformation of messages to prevent risks like market manipulation or data leakage, and variants, which enable a single MCP server to expose optimized tool versions for different models or agents.
By implementing these mechanisms, Bloomberg aims to make AI systems more predictable, controllable, and efficient, ultimately ensuring that financial AI remains both helpful to users and harmless to markets.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Anya from Bloomberg discusses the infrastructure and developer tooling powering the company's AI applications.                                                      |
|   2 | Bloomberg serves buy-side and sell-side financial clients who require trusted information for high-stakes, regulated decisions.                                     |
|   3 | The company emphasizes building trustworthy AI infrastructure to ensure viability in production environments.                                                       |
|   4 | Trustworthy AI is defined by three principles: deriving answers from trusted sources, providing transparent attribution, and solving real user problems.            |
|   5 | The release of the Ask B Agent AI application transformed customer interaction with the Bloomberg terminal through a conversational interface.                      |
|   6 | Infrastructure requirements include high availability, runtime visibility, controls, and the ability for platform teams to enable continuous improvement.           |
|   7 | MCP provides foundational connectivity but lacks out-of-the-box guardrails, correctness, governance, and production reliability.                                    |
|   8 | Financial AI risks include disclosure of non-public information, unauthorized transactions, market manipulation, and hallucinated narratives.                       |
|   9 | The Interceptor framework enables messages to be intercepted, validated, and transformed at various protocol lifecycle extension points.                            |
|  10 | Interceptors function similarly to Kubernetes webhooks, consisting of validators that inspect and block unsafe payloads and mutators that transform or redact data. |
|  11 | This framework allows for deterministic execution of controls, ensuring citations and verifying actions as they cross system boundaries.                            |
|  12 | Variants allow an MCP server to expose multiple parallel versions of the same tools optimized for different models, agents, or contexts.                            |
|  13 | Using variants avoids the need to build separate MCP servers or create generic tools that do not serve specific agents optimally.                                   |
|  14 | Variants improve system predictability, controllability, and evolvability while reducing duplication and noisy evaluation results.                                  |
|  15 | These concepts are being formalized through MCP community standards, specifically SEP 1763 for model availability and SAP 2053 for variants.                        |
|  16 | Bloomberg encourages involvement in the MCP community and the financial services interest group to shape these standards.                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/z6SuFQYClQI/hqdefault.jpg)](https://www.youtube.com/watch?v=z6SuFQYClQI)

[Watch on YouTube](https://www.youtube.com/watch?v=z6SuFQYClQI)
