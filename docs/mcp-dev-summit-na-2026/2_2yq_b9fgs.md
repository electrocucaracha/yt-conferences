---
layout: default
title: Installed an MCP Server... Then This Happened
nav_order: 82
parent: MCP Dev Summit NA 2026
type: Video Note
description: 'Cecilia, a product manager at Docker, presents a talk on securing AI agents by addressing common "MCP horror stories," such as unauthorized server installations causing data leaks and autonomous ag...'
resource: "https://www.youtube.com/watch?v=2_2yQ_b9fgs"
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

Cecilia, a product manager at Docker, presents a talk on securing AI agents by addressing common "MCP horror stories," such as unauthorized server installations causing data leaks and autonomous agents inadvertently deleting critical work.
She argues that as AI adoption scales, organizations must answer four key questions regarding permissions, user actions, data flow, and audit trails to prevent these security gaps.
To solve this, she proposes three essentials: an MCP Gateway that acts as a control layer for authentication, policy management, and audit logging; Docker sandboxes that enforce OS-level restrictions on file and network access to limit agent capabilities; and a deployment strategy that integrates seamlessly with existing tech stacks and cloud environments.
This dual-layer approach of gateway controls and sandbox isolation ensures that security is enforced outside the agentic surface, preventing both malicious and unintended actions without requiring organizations to overhaul their infrastructure.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Cecilia, a product manager at Docker, presented MCP horror stories to illustrate risks when AI agents operate without proper governance.                                                 |
|   2 | An intern installed an unauthorized MCP server found online, leading to a data leak of code and API secrets with no audit logs to investigate the incident.                              |
|   3 | An experienced developer using an approved server allowed an autonomous agent to execute tasks without confirmation, resulting in the unintended deletion of branches and unpushed work. |
|   4 | These incidents are preventable by answering four key questions: what is allowed, who is doing what, what is flowing through, and what happened.                                         |
|   5 | Organizations often lack answers to these questions, creating a security gap that can be closed with a control layer, a sandbox, and easy deployment.                                    |
|   6 | The MCP Gateway acts as a control layer between AI agents and MCP servers, enforcing a curated catalog of approved tools to block unauthorized servers.                                  |
|   7 | The gateway handles authentication, ensuring secrets do not reach MCP servers, and manages policy and access control for fine-grained user and agent permissions.                        |
|   8 | Audit logging within the gateway provides a complete track record of actions, policies triggered, and data flow for visibility and compliance.                                           |
|   9 | Sandboxes provide a capability ceiling that defines the maximum actions an agent can perform, controlling file system and network access at the OS level.                                |
|  10 | Docker sandboxes run agents in isolated containers within a micro VM, preventing access to other sessions or hosts and enforcing security outside the agentic surface.                   |
|  11 | Effective deployment requires solutions that adapt to existing environments, supporting local or remote execution and integrating with current tech stacks.                              |
|  12 | The solution must work with existing identity providers, secret managers, observability tools, and various cloud or on-premises infrastructure configurations.                           |
|  13 | Docker offers these three essentials: an MCP Gateway, sandboxes, and an easy deployment method that fits into existing organizational workflows.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/2_2yQ_b9fgs/hqdefault.jpg)](https://www.youtube.com/watch?v=2_2yQ_b9fgs)

[Watch on YouTube](https://www.youtube.com/watch?v=2_2yQ_b9fgs)
