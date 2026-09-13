---
layout: default
title: "MCP Vs CLIs: Why Agents Need Purpose-Built Interfaces - Sam Morrow, GitHub"
nav_order: 60
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Sam, a developer involved with GitHub's MCP server and the MCP specification,
  reflects on the ongoing debates surrounding MCP's relevance, noting that despite
  claims of its decline, MCP usage is at an all-time high. He highlights the comple...
resource: https://www.youtube.com/watch?v=ideYDMJKujE
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

Sam, a developer involved with GitHub's MCP server and the MCP specification, reflects on the ongoing debates surrounding MCP's relevance, noting that despite claims of its decline, MCP usage is at an all-time high.
He highlights the complexity of comparing MCP, CLIs, skills, and plugins, emphasizing that each approach has unique trade-offs in areas like token efficiency, security, and execution environment, and that the landscape is rapidly evolving.
Sam discusses the challenges of security, particularly with CLIs and skills, and argues that MCP offers distinct advantages, such as clear user-agent separation and robust access controls, though no solution is perfect.
He cautions against oversimplified hot takes and stresses that the debate is far from settled, with ongoing innovation and experimentation needed to address context management and security for agents.
Ultimately, Sam concludes that MCP is not obsolete, and that the real question is not MCP versus CLI, but how to best adapt these evolving tools to diverse environments and needs.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sam has been building GitHub's MCP server and contributing to the MCP spec for about a year.                                                               |
|   2 | GitHub MCP is about to turn one year old.                                                                                                                  |
|   3 | There is ongoing debate about whether MCP is "dead," but MCP usage is currently at an all-time high.                                                       |
|   4 | GitHub's MCP TypeScript SDK is seeing around 48 million downloads per week.                                                                                |
|   5 | There is significant overlap among users of MCP, CLIs with agents, and agent skills.                                                                       |
|   6 | The debate between MCP and other approaches is often framed poorly and influenced by individual environments.                                              |
|   7 | Key areas of consideration: token efficiency, security/privacy, unique unlocks (e.g., terminal access), and agent execution environment.                   |
|   8 | Token efficiency is crucial due to costs and agent efficacy; issues include tool registration, progressive discovery, prompt caching, skills, and plugins. |
|   9 | Security concerns increase with agent autonomy; enterprises favor MCP for precise control and tool sharing.                                                |
|  10 | The discourse is polarized, with "autonomy maximalists" and enterprise users having different priorities.                                                  |
|  11 | Token costs, model round trips, prompt cache, context window size, and context rot are fundamental constraints.                                            |
|  12 | Different primitives (MCP, skills, subagents, plugins) interact differently with these constraints.                                                        |
|  13 | MCP usage patterns are evolving, including code mode, CLIs, tool search APIs, and lazy invocation via skills.                                              |
|  14 | Comparing CLI, MCP, skills, and plugins directly is often misleading.                                                                                      |
|  15 | The landscape is rapidly changing; static answers are unreliable.                                                                                          |
|  16 | Progressive discovery and lazy loading (e.g., plugins) offer potential but have discovery challenges.                                                      |
|  17 | Security is a major concern, especially with skills and CLIs (e.g., supply chain risks, token leaks, prompt injection).                                    |
|  18 | MCP can offer better security postures (e.g., OAuth flows, encrypted tokens, role-based access controls).                                                  |
|  19 | Sandboxing is possible but difficult; dynamic sandboxes are needed for generalist agents.                                                                  |
|  20 | MCP uniquely distinguishes between user and agent, enabling user-facing                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ideYDMJKujE)
