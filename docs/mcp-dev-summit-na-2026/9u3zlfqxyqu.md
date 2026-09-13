---
layout: default
title:
  "Schema To Insight: Architecting Production-Grade Database MCP Tools - Kurtis
  Van Gent & Wenxin Du"
nav_order: 79
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this presentation, Curtis Vanent and Winenzu, maintainers of MCP core
  at Google, discuss best practices for architecting production-grade MCP tools for
  databases, focusing on security and scalability. They outline three common tool
  patte...
resource: https://www.youtube.com/watch?v=9u3ZLfqXYQU
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

In this presentation, Curtis Vanent and Winenzu, maintainers of MCP core at Google, discuss best practices for architecting production-grade MCP tools for databases, focusing on security and scalability.
They outline three common tool patterns: control plane tools for administrative tasks, natural language to SQL tools for developer assistance, and structured SQL tools for secure, deterministic operations—emphasizing the importance of structured tools in production environments.
The speakers highlight the security risks posed by giving agents broad database access, particularly the "lethal trifecta" of access to private data, exposure to untrusted content, and the ability to communicate externally, which can lead to data breaches.
To mitigate these risks, they describe how the MCP toolbox abstracts sensitive connection details, enforces pre-written SQL statements with strict parameter controls, and uses authenticated parameters derived from user tokens to prevent agents from accessing or leaking sensitive information.
A demo of a travel agent application illustrates these security measures in practice, showing how authenticated parameters ensure that agents can only act on behalf of the correct user, thereby safeguarding personal data and reducing the attack surface.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction to architecting production-grade MCP tools by Curtis Vanent and Winenzu, MCP core maintainers at Google.                                                          |
|   2 | Presentation covers: reasons to trust their advice, common MCP tool patterns for databases, and security/guardrails.                                                           |
|   3 | Google offers fully managed MCP services for multiple databases (AlloyDB, Spanner, Cloud SQL, Bigtable, Firestore).                                                            |
|   4 | MCP Toolbox for Databases: open source, 13.5k GitHub stars, 100 contributors, supports 40+ databases, customizable, scalable, secure, production-ready.                        |
|   5 | Over 20 million tool calls processed through MCP services last month.                                                                                                          |
|   6 | Three common MCP tool patterns:                                                                                                                                                |
|   7 | Control plane tools: automate admin tasks (create/clone instances, backups, users).                                                                                            |
|   8 | Natural language to SQL: LLMs generate SQL queries for database exploration, mainly for developer assistance.                                                                  |
|   9 | Structured SQL tools: pre-written, reviewed SQL statements committed as code, ensuring safety and speed.                                                                       |
|  10 | Two main tool usage patterns:                                                                                                                                                  |
|  11 | Build time: developer assistance tools in IDEs/CLIs, broad access, developer-in-the-loop.                                                                                      |
|  12 | Runtime: production application tools, deterministic wrappers, strict boundaries, minimize hallucinations.                                                                     |
|  13 | Security concerns:                                                                                                                                                             |
|  14 | Agents can be tricked into unsafe actions (confused deputy problem/lethal trifecta: access to private data, exposure to untrusted content, ability to communicate externally). |
|  15 | Example: agent leaks executive salaries due to blind execution of untrusted input.                                                                                             |
|  16 | Solution: separate agent, user, and workload identities; restrict agent permissions; distinguish agent vs. application parameters.                                             |
|  17 | Toolbox security improvements:                                                                                                                                                 |
|  18 | Abstract database connection info into a "source" primitive, removing sensitive parameters from agent control.                                                                 |
|  19 | Allow only pre-written, developer-reviewed SQL statements with dynamic parameters.                                                                                             |
|  20 | Type-check parameters to prevent SQL injection.                                                                                                                                |
|  21 | Use authenticated parameters derived from user OIDC tokens, keeping sensitive info away from agents.                                                                           |
|  22 | Demo: travel agent ap                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9u3ZLfqXYQU)
