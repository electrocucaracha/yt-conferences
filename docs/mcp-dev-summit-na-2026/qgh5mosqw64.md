---
type: Video Note
title: "The Seven Deadly Sins With MCP - Ricardo Ferreira, Redis"
description: "Ricardo Ferrer, leading the developer relations team at Radius, introduces a presentation focused on common pitfalls in MCP (Multi-Cloud Protocol) implementations, emphasizing that most issues arise not from the protocol itself but from rec..."
resource: https://www.youtube.com/watch?v=qgH5mOsQw64
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Ricardo Ferrer, leading the developer relations team at Radius, introduces a presentation focused on common pitfalls in MCP (Multi-Cloud Protocol) implementations, emphasizing that most issues arise not from the protocol itself but from recurring engineering habits and backend API design flaws.
Drawing from a taxonomy paper analyzing thousands of GitHub issues, Ferrer notes that none of the MCP-related problems were due to the protocol, but rather to unintentional, widespread practices such as excessive backend intimacy, granting overly broad permissions, poor error handling, inefficient retries, returning unnecessarily large payloads, over-abstracting metadata, and duplicating services without governance.
He categorizes these issues into "deadly sins"—lust, greed, sloth, wrath, gluttony, pride, and envy—grouped by their impact on security, operations, and long-term technical debt.
Through code examples and audience interaction, Ferrer illustrates how these patterns, though often trivial and familiar, can lead to significant production failures if left unchecked, and he encourages intentional, explicit engineering practices to mitigate them.
He concludes by inviting attendees to explore his related blog series and connect for further discussion.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ricardo Ferrer from Radius, leading the developer relations team.                                                                      |
|   2 | Presentation focuses on MCP (not Radius), sharing experiences and lessons learned.                                                     |
|   3 | Previous sessions discussed MCP protocol design; this session focuses on recognizing signs of bad MCP implementations.                 |
|   4 | Common industry pattern: middleware/protocols often blamed for failures, but root causes usually lie in backend API/capability design. |
|   5 | Problems often surface at the layer visible to consumers, not where they originate.                                                    |
|   6 | Many failures are due to common engineering practices, not intentional bad code.                                                       |
|   7 | Referenced a taxonomy paper analyzing 3,282 GitHub issues; 47 MCP-related, none due to protocol flaws.                                 |
|   8 | Problems are categorized into three types:                                                                                             |
|   9 | Security sins (lust, greed): Can cause production failures if not fixed.                                                               |
|  10 | Operational sins: Affect trustworthiness and reliability.                                                                              |
|  11 | Design sins: Lead to long-term technical debt.                                                                                         |
|  12 | Seven "deadly sins" in MCP implementations:                                                                                            |
|  13 | Lust: Too much intimacy with backend (e.g., excessive permissions or access).                                                          |
|  14 | Greed: Granting too much power (e.g., unrestricted file system access).                                                                |
|  15 | Sloth: Lack of care in error handling (e.g., generic errors, poor propagation).                                                        |
|  16 | Wrath: Excessive force (e.g., aggressive retries without backoff, causing potential DOS).                                              |
|  17 | Gluttony: Too much waste (e.g., returning unnecessary or excessive data).                                                              |
|  18 | Pride: Over-abstraction or automation, leading to inflexible or non-portable solutions.                                                |
|  19 | Envy: Duplicating existing solutions without governance, causing namespace clashes.                                                    |
|  20 | Fixes are usually simple but often overlooked due to their triviality.                                                                 |
|  21 | Emphasized intentionality, explicitness, and governance in MCP implementations.                                                        |
|  22 | Shared resources: blog series and taxonomy paper for further study.                                                                    |
|  23 | Encouraged connecting on LinkedIn for further discussion.                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qgH5mOsQw64)