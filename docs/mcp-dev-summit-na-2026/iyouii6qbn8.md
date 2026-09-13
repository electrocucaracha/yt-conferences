---
layout: default
title:
  If You Can Secure It Here, You Can Secure It Anywhere - Milan Williams & Katrina
  Liu, Semgrep
nav_order: 36
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Milan Williams and Katrina from SGrip discuss their experience
  building a secure MCP server as part of their application security platform, which
  helps users detect and fix vulnerabilities in code as soon as possible. They exp...
resource: https://www.youtube.com/watch?v=iYouIi6QBn8
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

In this talk, Milan Williams and Katrina from SGrip discuss their experience building a secure MCP server as part of their application security platform, which helps users detect and fix vulnerabilities in code as soon as possible.
They explain the motivations behind their work, including the increasing number of vulnerabilities, the speed at which attackers exploit them, and the unique threats faced by security companies like theirs.
The team prioritized three non-negotiables: protecting customer environments, ensuring reliable and deterministic vulnerability detection, and minimizing the blast radius in case of compromise.
Katrina outlines key challenges they encountered, such as agent non-determinism, issues with file content accuracy when scanning remotely, and implementing robust authentication, leading them to favor a local server approach while continuing to explore remote solutions.
The presentation concludes with a demonstration of their tool in action and a recommendation to consult their detailed security guide for building safe MCP servers.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation covers security for MCP servers and lessons learned by SGrip/SRAP.                                                                                                      |
|   2 | SGrip is an application security platform focused on finding and fixing vulnerabilities quickly, especially as code is generated.                                                    |
|   3 | Many organizations use SGrip; an open-source version is available.                                                                                                                   |
|   4 | Agenda includes motivations, real-world MCP attacks, threat model, challenges, and key takeaways for securing MCP servers.                                                           |
|   5 | Security teams face an explosion of vulnerabilities and are often overwhelmed and understaffed.                                                                                      |
|   6 | Coding agents prioritize functionality over security, leading to more vulnerabilities.                                                                                               |
|   7 | Attackers can exploit vulnerabilities faster than ever, even low-severity ones.                                                                                                      |
|   8 | SGrip aims to identify vulnerabilities as soon as possible, shifting security left in the development process.                                                                       |
|   9 | Unique threat model: rise in industry-wide MCP toolchain attacks (e.g., MCP remote RCE affecting 400,000+ developers) and targeted attacks by sophisticated groups (e.g., Team PCP). |
|  10 | Three non-negotiables for SGrip’s MCP server:                                                                                                                                        |
|  11 | Protect customer environments and sensitive code.                                                                                                                                    |
|  12 | Ensure reliable, deterministic vulnerability detection.                                                                                                                              |
|  13 | Minimize blast radius with well-scoped authentication and authorization.                                                                                                             |
|  14 | Main feature of MCP server is code scanning via an agentic interface.                                                                                                                |
|  15 | Challenge 1: Non-determinism—agents often do not call scanning tools as expected.                                                                                                    |
|  16 | Solution: Use hooks to trigger scans automatically after tool use events.                                                                                                            |
|  17 | Challenge 2: Agents hallucinate file content when sending to remote servers, leading to inaccurate scans.                                                                            |
|  18 | Solution: Prefer local MCP server to access real file content; experimenting with hooks to improve remote support.                                                                   |
|  19 | Challenge 3: Authentication—must prevent unauthorized access to customer data.                                                                                                       |
|  20 | Local server uses CLI token for authentication.                                                                                                                                      |
|  21 | Remote server aims to use OAuth, but integration with hooks and protocol is still a challenge.                                                                                       |
|  22 | Demo showed real-time vulnerability detection and remediation in generated code.                                                                                                     |
|  23 | Security e                                                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=iYouIi6QBn8)
