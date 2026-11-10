---
layout: default
title: "Beyond LLMs in a Loop: Building Trusted Agents in Regulated Industries - Lucas Beeler, Aerospike"
nav_order: 1
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Lucas Beeler, a Senior Solutions Architect at Aerospike, presents a framework for building trusted AI agents in regulated industries like healthcare and finance by arguing that intelligent agency i..."
resource: "https://www.youtube.com/watch?v=-n7Lq3bwudg"
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

Lucas Beeler, a Senior Solutions Architect at Aerospike, presents a framework for building trusted AI agents in regulated industries like healthcare and finance by arguing that intelligent agency is distinct from the computational substrate, meaning agents do not necessarily require LLMs.
He defines a trustworthy agent as one that operates under explicitly stated assumptions and accurate environmental perceptions, allowing for the mathematical proof that prohibited behaviors cannot occur, rather than relying solely on statistical backtesting.
The proposed architecture involves using LLMs to generate declarative plan specifications, followed by agentic evidence gathering and rigorous validation using automated reasoning systems like Isabelle to ensure compliance with standards of care or financial regulations.
Beeler illustrates this with a healthcare example where a system assembles a surgical team by verifying credentials and insurance networks, and a finance example demonstrating how simultaneous trading strategies can exceed exposure limits, highlighting the need to verify interactions at risky points.
Finally, he emphasizes that the final stage involves constrained optimization to achieve goals like cost-effectiveness while maintaining an audit trail for accountability in litigation or regulatory investigations.

# Main Points

|   # | Main point                                                                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , Senior Solutions Architect at Aerospike, presented "Beyond LLMs in a Loop," focusing on building trusted agents in regulated industries like healthcare and finance.                                                                      |
|   2 | "agent" is not limited to LLMs; it refers to any system that pursues a delegated objective, observes its environment, and adapts to improve results, as defined by Wooldridge and Jennings (1995).                                          |
|   3 | , which grouped articles by semantic topic without LLMs, demonstrating that intelligent agency is distinct from the computational substrate.                                                                                                |
|   4 | , but integrating them with traditional AI techniques like knowledge representation, theorem provers, and constraint optimization is essential for trust in high-stakes environments.                                                       |
|   5 | , provided the agent has accurate environmental perception and explicitly stated assumptions.                                                                                                                                               |
|   6 | , ensuring systems can survive litigation or regulatory investigations, such as SEC probes in finance or malpractice suits in healthcare.                                                                                                   |
|   7 | , often in XML format, which is then checked against a strong schema.                                                                                                                                                                       |
|   8 | (e.g., SEC rules, exposure limits, or surgeon certifications), followed by a validation stage to ensure compliance.                                                                                                                         |
|   9 | , which interprets the declarative plan specification.                                                                                                                                                                                      |
|  10 | , an illustrative example involves assembling a surgical team that meets standards of care, is in-network with insurance, and is cost-effective, using LLMs to generate specifications and agents to verify credentials via REST endpoints. |
|  11 | (e.g., XML) containing assertions, verification details, issuing authorities, and retrieval methods, maintained for audit purposes rather than simple boolean flags.                                                                        |
|  12 | , checking for self-consistency and consistency with the "world" (e.g., standards of care or SEC rules).                                                                                                                                    |
|  13 | , such as ensuring simultaneous trading strategies do not collectively exceed exposure limits.                                                                                                                                              |
|  14 | (e.g., minimizing cost while meeting care standards), which are often NP-hard, requiring knowledge representation to achieve solutions within a certain percentage of the exact answer.                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-n7Lq3bwudg/hqdefault.jpg)](https://www.youtube.com/watch?v=-n7Lq3bwudg)

[Watch on YouTube](https://www.youtube.com/watch?v=-n7Lq3bwudg)
