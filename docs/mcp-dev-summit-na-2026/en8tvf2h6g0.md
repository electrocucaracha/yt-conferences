---
layout: default
title:
  "Keynote: Building a Unified Control Plane for MCP Across Servers, Clients,
  and Teams - Cecilia Liu"
nav_order: 40
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Cecilia, a product manager at Docker, shares real-world "horror stories"
  highlighting the security risks organizations face when using AI agents and MCP
  servers without proper controls. She recounts incidents where an intern unknowingly
  cau...
resource: https://www.youtube.com/watch?v=En8TVF2H6g0
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

Cecilia, a product manager at Docker, shares real-world "horror stories" highlighting the security risks organizations face when using AI agents and MCP servers without proper controls.
She recounts incidents where an intern unknowingly caused a data leak by installing an unauthorized MCP server, and where an experienced developer lost valuable work due to over-trusting an autonomous agent, emphasizing that such issues are increasingly common as AI adoption grows.
Cecilia stresses that these problems are preventable by establishing clear governance through four key questions: what tools are allowed, who is using them, what data is flowing, and what actions have occurred.
She outlines three essential solutions: implementing an MCP gateway to control and audit access, using sandboxes to enforce strict operational boundaries at the OS level, and ensuring easy deployment that integrates with existing tech stacks.
Cecilia concludes by inviting attendees to learn more at Docker’s booth, reiterating that these measures are crucial for preventing security incidents as AI usage scales.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Cecilia, Product Manager at Docker, focuses on MCP gateway and agent security.                                                                                |
|   2 | Shared two "horror stories" about AI agent misuse:                                                                                                            |
|   3 | Story 1: Intern installs unauthorized MCP server without review; leads to data leak with no audit trail.                                                      |
|   4 | Story 2: Experienced developer uses approved MCP server but allows agent full autonomy; agent deletes important work unintentionally.                         |
|   5 | Emphasized that such incidents are increasingly common as AI agent usage grows in organizations.                                                              |
|   6 | Stated that these issues are preventable by answering four key questions:                                                                                     |
|   7 | What is allowed? (Which MCP servers/tools)                                                                                                                    |
|   8 | Who is doing what? (User, tool, client, time)                                                                                                                 |
|   9 | What is flowing through? (Credentials, secrets)                                                                                                               |
|  10 | What happened? (Audit logs, track records)                                                                                                                    |
|  11 | Many organizations lack answers to these questions, creating security gaps.                                                                                   |
|  12 | Proposed three essentials to close the gap:                                                                                                                   |
|  13 | Control layer (MCP gateway)                                                                                                                                   |
|  14 | Sandbox                                                                                                                                                       |
|  15 | Easy deployment                                                                                                                                               |
|  16 | MCP gateway sits between AI agents and MCP servers, enabling governance.                                                                                      |
|  17 | Organizations should use a curated catalog of approved MCP servers/tools.                                                                                     |
|  18 | MCP gateway blocks unapproved servers, handles authentication, policy management, access control, and audit logging.                                          |
|  19 | Fine-grained policies can be set for different user groups and agents.                                                                                        |
|  20 | Gateway alone is insufficient; agents can still act unpredictably.                                                                                            |
|  21 | Sandboxes provide an OS-level capability ceiling, restricting file system and network access.                                                                 |
|  22 | Agents run in isolated containers within a Docker sandbox and microVM for strong isolation.                                                                   |
|  23 | Security should be enforced outside the agent, not relying on agent behavior.                                                                                 |
|  24 | Deployment should be easy and compatible with existing tech stacks, identity providers, secret managers, observability tools, and cloud/on-prem environments. |
|  25 | Recap: Need MCP gateway, sandbox, and easy deployment for secure AI agent operations.                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=En8TVF2H6g0)
