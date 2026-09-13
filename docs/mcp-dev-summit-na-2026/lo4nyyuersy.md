---
layout: default
title:
  Declarative MCP Servers for Secure, Specialized AI Agents - Josh Reini & Reetika
  Roy, Snowflake
nav_order: 14
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this presentation, Josh and Ritika from Snowflake discuss the advantages
  of building specialized agents and MCP servers over using monolithic agents with
  broad tool access. They demonstrate how monolithic agents, which have access to
  man...
resource: https://www.youtube.com/watch?v=Lo4nyYuERsY
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

In this presentation, Josh and Ritika from Snowflake discuss the advantages of building specialized agents and MCP servers over using monolithic agents with broad tool access.
They demonstrate how monolithic agents, which have access to many tools across domains, often struggle to select the right tools, leading to slow responses, increased token usage, and security risks.
By contrast, Snowflake’s approach involves making agents first-class entities with their own identities and layered security policies, enabling granular control over which tools and data each agent and user role can access.
This specialization reduces hallucinations, improves performance, simplifies debugging, and enhances security by limiting the blast radius of potential issues.
The system enforces access controls at multiple layers—agent, server, tool, and data—allowing for precise, auditable, and scalable management of agentic workloads, with coding agents further streamlining the process for security teams.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Building specialized MCP servers and agents leads to faster responses, reduced token bloat, and more secure agents.                                                |
|   2 | Monolithic agents with access to many tools struggle to select the right tools, leading to slow, unpredictable, and sometimes incorrect or hallucinated responses. |
|   3 | More tools increase unpredictability, context window bloat, response time, and cost.                                                                               |
|   4 | Security is harder to enforce when all tools are available in one server.                                                                                          |
|   5 | Specialized agents and MCP servers allow granular access control and easier management.                                                                            |
|   6 | Snowflake’s approach makes the agent a first-class identity with its own security policies, layered with user access controls.                                     |
|   7 | Policies can restrict which tools agents can execute and mask sensitive data at the query layer.                                                                   |
|   8 | Defense in depth is achieved by combining agent and user identities with policies at both levels.                                                                  |
|   9 | Scaling agentic workloads requires specialization at every layer: agent, server, tools, and data.                                                                  |
|  10 | Agent specification defines which servers, tools, and instructions each agent can use; creation/modification is restricted to certain roles.                       |
|  11 | MCP server definition specifies which tools are available through a server; access to servers and tools is independently controlled.                               |
|  12 | Arbback (access control) is enforced at agent, server, tool, and data layers.                                                                                      |
|  13 | Example: HR agent connects to specific servers and tools, with access further restricted by user roles.                                                            |
|  14 | Server declaration acts as a domain boundary; access to a server does not imply access to all its tools.                                                           |
|  15 | Enforcement occurs at four layers: agent, server, tool, and data.                                                                                                  |
|  16 | Coding agents can generate explicit SQL grants for security admins to approve, reducing manual overhead.                                                           |
|  17 | Specialized agents provide more accurate, faster responses and are easier to audit and debug.                                                                      |
|  18 | Monolithic agents have a larger security risk and are harder to manage.                                                                                            |
|  19 | Declarative agent and server specs enable infrastructure-as-code and easy auditing.                                                                                |
|  20 | Arbback is generally applied at                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Lo4nyYuERsY)
