---
layout: default
title:
  Deploying MCP at Scale Without Skipping Compliance - Becky Brooks, MCP Manager
  by Usercentrics
nav_order: 16
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Becky, an MCP manager at Usercentrics, discusses the challenges
  and best practices for scaling MCP (Model Control Protocol) while maintaining compliance,
  particularly in light of emerging regulations like the EU AI Act. She ou...
resource: https://www.youtube.com/watch?v=cjsr-HKiZok
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Becky, an MCP manager at Usercentrics, discusses the challenges and best practices for scaling MCP (Model Control Protocol) while maintaining compliance, particularly in light of emerging regulations like the EU AI Act.
She outlines her experience launching an MCP gateway and highlights the rapid evolution of MCP from an internal tool to critical infrastructure subject to regulatory scrutiny.
Becky explains that while MCP itself is not explicitly mentioned in the EU AI Act, many of the systems it enables fall under its scope, especially in high-risk industries such as healthcare, finance, and law enforcement, requiring strict compliance and transparency.
She emphasizes that best practices for MCP deployment—such as robust data governance (ensuring PII never reaches models), comprehensive audit logs, and strong cybersecurity measures—are not only regulatory requirements but essential for responsible scaling.
Becky concludes by advocating for the use of MCP gateways to provide necessary guardrails, observability, and policy enforcement, enabling organizations to implement MCP securely and compliantly at scale.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Becky, MCP Manager at Usercentrics, discusses scaling MCP while maintaining compliance.                                                            |
|   2 | Agenda includes overview, scaling challenges, regulations (EU AI Act), and best practices.                                                         |
|   3 | MCP Manager was launched after recognizing integration technology disruption; acquired by Usercentrics in January.                                 |
|   4 | Usercentrics specializes in data consent, now focusing on AI workflows.                                                                            |
|   5 | MCP has rapidly evolved from internal tool to critical infrastructure in under 500 days.                                                           |
|   6 | Scaling MCP is challenging: protocol adoption differs from organizational implementation.                                                          |
|   7 | Key challenges: security exposure, lack of visibility, insufficient logs, privacy concerns, complex configurations.                                |
|   8 | EU AI Act: MCP not explicitly mentioned, but systems enabled by MCP are covered.                                                                   |
|   9 | Compliance requirements depend on deployment, not protocol.                                                                                        |
|  10 | EU AI Act uses a tiered system:                                                                                                                    |
|  11 | Level 4 (prohibited): enforcement started, includes intimate image generation, biometric surveillance, manipulation, social scoring.               |
|  12 | Level 3 (high risk): strict regulation for sectors like finance, healthcare, HR, education, law enforcement, critical infrastructure.              |
|  13 | Level 2 (transparency): enforcement starts later this year, requires disclosure of AI-generated content in consumer-facing workflows.              |
|  14 | US and other regions (Australia, some US states) are developing similar AI regulations.                                                            |
|  15 | Organizations with AI products or deployments in the EU, especially in regulated industries, must comply.                                          |
|  16 | Compliance requirements often align with MCP best practices.                                                                                       |
|  17 | Eight requirements for high-risk AI systems; focus on three:                                                                                       |
|  18 | Data governance: prevent PII from reaching models; use filtering/redaction (e.g., regex, Microsoft Presidio, custom DLP).                          |
|  19 | Audit logs: must be structured, include contextual metadata, and be suitable for external stakeholders/regulators.                                 |
|  20 | Accuracy and cybersecurity: every server is a potential attack surface; use guardrails and monitoring (e.g., alerts for tool description changes). |
|  21 | MCP gatewa                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cjsr-HKiZok)
