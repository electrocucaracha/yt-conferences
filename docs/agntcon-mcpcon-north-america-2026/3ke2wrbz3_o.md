---
layout: default
title: "Workshop: Governing Enterprise AI Agents: Tools,... - Shannon Williams & Bill Maxwell, Obot"
nav_order: 122
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Shannon Williams and Bill Maxwell from Obot present a hands-on lab focused on securing agentic AI systems by addressing the "lethal trifecta" of risks: access to private data, exposure to untrusted...'
resource: "https://www.youtube.com/watch?v=3Ke2wRBz3_o"
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

Shannon Williams and Bill Maxwell from Obot present a hands-on lab focused on securing agentic AI systems by addressing the "lethal trifecta" of risks: access to private data, exposure to untrusted sources, and the ability to exfiltrate information.
The session demonstrates how indirect prompt injection and tool poisoning can be exploited through MCP servers, using a vulnerable support server to show how malicious instructions embedded in support tickets or tool descriptions can trick models into leaking sensitive PII.
To mitigate these threats, the presenters implement a defense-in-depth strategy using the Obot platform, which includes curating a vetted catalog of MCP servers, applying least-privilege principles by removing dangerous tools like webhooks and customer data access, and enforcing data filters to redact or block PII such as emails and driver’s licenses before they reach the model.
Additionally, the lab covers endpoint security through Obot Sentry, which discovers shadow AI usage on employee devices, enforces allowed MCP servers, and captures audit logs of local agent activities to ensure comprehensive visibility and control.
The core takeaway is that effective agentic security requires centralized governance, continuous auditing, and layered controls to manage the complex interactions between AI agents, tools, and enterprise data.

# Main Points

|   # | Main point                                                                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , focusing on managing AI integration, risk deterrence, and governance within the MCP ecosystem.                                                                                                                                        |
|   2 | : defining and curating accessible assets (MCP servers, models, APIs, CLIs), controlling agent privileges and execution environments (sandboxes vs. local devices), and implementing robust audit logging.                              |
|   3 | (malicious instructions in tool descriptions), indirect prompt injection (untrusted data sources influencing the model), rugpulls (tools changing behavior over time), cross-server attacks, privilege escalation, and excessive scope. |
|   4 | "Lethal Trifecta" is defined as the combination of access to private data, exposure to untrusted systems, and the ability to exfiltrate data; removing any one of these components mitigates the risk.                                  |
|   5 | , retrieving support tickets, listing customers, and sending webhooks.                                                                                                                                                                  |
|   6 | (SSNs, credit cards) to an external webhook.                                                                                                                                                                                            |
|   7 | ; while some models (like Claude) detect and block high-risk actions, others (like Gemma) may follow malicious instructions, highlighting the need for external controls.                                                               |
|   8 | , inspect payloads, and identify injected instructions, with payload visibility restricted to specific "auditor" roles to protect sensitive data.                                                                                       |
|   9 | "managed" Virtual MCP (VMCP) server that freezes tool definitions and disables risky tools (e.g., sending webhooks, listing customers) to break the Lethal Trifecta.                                                                    |
|  10 | (based on Microsoft Presidio) to redact or block sensitive information such as email addresses and driver's licenses before it reaches the LLM.                                                                                         |
|  11 | (replacing it with placeholders) or block requests entirely if PII is detected, though they require testing against specific datasets to ensure effectiveness.                                                                          |
|  12 | "shadow AI" by deploying Obot Sentry, an endpoint agent that scans local devices to discover installed AI clients, MCP servers, skills, and plugins.                                                                                    |
|  13 | , including shell commands and tool calls, allowing organizations to enforce policies and route local MCP traffic through the central gateway.                                                                                          |
|  14 | , ensuring compliance with organizational security standards.                                                                                                                                                                           |
|  15 | , combining centralized gateways, curated catalogs, identity-based access control, data filtering, and endpoint monitoring to secure agentic workflows.                                                                                 |
|  16 | (IDP) to manage access by team and role, optimizing token usage and ensuring comprehensive audit trails for incident response.                                                                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3Ke2wRBz3_o/hqdefault.jpg)](https://www.youtube.com/watch?v=3Ke2wRBz3_o)

[Watch on YouTube](https://www.youtube.com/watch?v=3Ke2wRBz3_o)
