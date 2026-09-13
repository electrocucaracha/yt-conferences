---
layout: default
title:
  "Securing MCP at Scale: From Principles To Production - Peter Smulovics, Morgan
  Stanley"
nav_order: 80
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker discusses key security challenges in using AI and MCP (Multi-Component
  Protocol) tools, particularly in sensitive environments like banking. Major concerns
  include data leakage, prompt injection, tool poisoning, misconfiguration...
resource: https://www.youtube.com/watch?v=E515s-EwF9M
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

The speaker discusses key security challenges in using AI and MCP (Multi-Component Protocol) tools, particularly in sensitive environments like banking.
Major concerns include data leakage, prompt injection, tool poisoning, misconfiguration, and the amplification of existing vulnerabilities due to AI's nondeterministic behavior.
The speaker emphasizes the importance of applying established security principles such as least privilege, strong authentication, short-lived tokens, input validation, output filtering, and robust observability, while also advocating for treating prompts as untrusted user input.
They highlight the need for governance, ownership tracking, and continuous security practices, noting that current tooling is still evolving, especially for regulated industries.
The future of secure MCP involves zero trust models, policy-as-code, AI firewalls, and capability attestation, with the ultimate goal of shifting from API security to agent security and ensuring that trust is minimized as AI capabilities expand.

# Main Points

|   # | Main point                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------- |
|   1 | Data leakage is a major concern, especially in banking.                                                               |
|   2 | Prompt injection, tool poisoning, and unexpected tool executions are significant risks.                               |
|   3 | User input, including prompts, should not be trusted.                                                                 |
|   4 | Authorization and authentication remain challenging; OAuth misconfigurations are common.                              |
|   5 | Tokens can be reused or leaked, leading to impersonation risks.                                                       |
|   6 | Solutions include short-lived tokens, strong identity controls, and avoiding over-permissioning.                      |
|   7 | Shadow IT and unverified external servers increase loss of control.                                                   |
|   8 | Server registries, approval processes, and technology controls are needed to manage MCP access.                       |
|   9 | Misconfiguration at scale increases the blast radius of incidents.                                                    |
|  10 | AI systems can unintentionally perform unauthorized actions, such as generating keygens.                              |
|  11 | MCP (Multi-Component Protocol) security is hard due to AI nondeterminism and lack of clear permission boundaries.     |
|  12 | Multihop attacks and confused deputy problems are risks in MCP environments.                                          |
|  13 | Implicit trust propagation and invisible execution chains complicate security.                                        |
|  14 | MCP amplifies existing bugs rather than introducing new ones.                                                         |
|  15 | Microsoft’s approach includes least privilege, scoped MCP servers, minimized data access, and limited actions.        |
|  16 | Strong authentication, token validation, secure storage, and isolation/containment are recommended.                   |
|  17 | Prompts must be treated as untrusted; implement prompt shields and input validation.                                  |
|  18 | Tool output filtering is necessary to prevent data leaks.                                                             |
|  19 | Observability and telemetry are critical due to nondeterministic behavior.                                            |
|  20 | Secure MCP architecture includes client host, MCP gateway, isolated servers, centralized identity, and observability. |
|  21 | Security should be enforced at domain boundaries, not the model.                                                      |
|  22 | Continuous security involves inventory, removal of unused servers, and ownership tracking.                            |
|  23 | Governance requires collaboration between platform, application, and security teams.                                  |
|  24 | Future trends: zero trust models, policy as code, AI firewalls,                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=E515s-EwF9M)
