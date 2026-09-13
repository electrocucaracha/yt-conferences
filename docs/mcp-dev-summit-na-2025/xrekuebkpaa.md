---
type: Video Note
title: "[Session] Multi Agent Collaboration in MCP with Nicholas Aldridge from AWS"
description: "Nick Aldridge, a principal engineer at AWS, shares his frustrating experience with airline booking systems to illustrate the need for better automation and agent-based interactions. He introduces the concept of inter-agent communication usi..."
resource: https://www.youtube.com/watch?v=XreKuebKpaA
tags: ["mcp-dev-summit-na-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Nick Aldridge, a principal engineer at AWS, shares his frustrating experience with airline booking systems to illustrate the need for better automation and agent-based interactions.
He introduces the concept of inter-agent communication using MCP (Message Control Protocol), explaining how agents and tools can interact within this framework to automate complex tasks like flight booking.
Aldridge demonstrates practical implementations using Spring AI and discusses the benefits of using MCP for agent integration, such as ease of use, shared primitives, and the blurring distinction between agents and tools.
He identifies areas for improvement in MCP, including better support for asynchronous communication, resource sharing, richer capability discovery, and more intuitive abstractions for developers.
Aldridge encourages the community to contribute to MCP’s development and provides resources for further engagement.
# Main Points

|   # | Main point                                                                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Attempted to change a flight via airline app; encountered a bug that canceled the original flight.                                                                                                                                |
|   2 | Spent three hours on the phone with the airline; experienced multiple booking errors (wrong direction, wrong dates, wrong destination).                                                                                           |
|   3 | Expressed desire for AI assistants to handle flight bookings without user intervention.                                                                                                                                           |
|   4 | Introduced as Nick Aldridge, principal engineer at AWS on the generative AI team, MCP steering committee member.                                                                                                                  |
|   5 | Topic: Inter-agent communication on MCP (Multi-Client Protocol).                                                                                                                                                                  |
|   6 | Proposed modeling airline booking as agent-to-agent interaction using MCP.                                                                                                                                                        |
|   7 | Described standard MCP diagram with new agent semantics and agent skills.                                                                                                                                                         |
|   8 | Demonstrated a sequence diagram for a simple status update request using agents and tools.                                                                                                                                        |
|   9 | Used Spring AI framework in Java to build and expose airline agent as an MCP tool.                                                                                                                                                |
|  10 | Showed more complex inter-agent interactions, including agents with multiple skills and resource population.                                                                                                                      |
|  11 | Listed reasons to use MCP for agents: ease of integration, blurring lines between agents and tools, strong primitives (transport, auth), existing functionality (sampling, cancellation, streaming), and extensible abstractions. |
|  12 | Identified areas for improvement in MCP for agents:                                                                                                                                                                               |
|  13 | Async communication: current persistent connections have reliability, scalability, and operational challenges.                                                                                                                    |
|  14 | Proposed client polling and event-driven architectures for better async workflows.                                                                                                                                                |
|  15 | Resource sharing: current resources lack state, structure, and reference passing; proposed task-based resource model with status tracking.                                                                                        |
|  16 | Capability discovery: tool annotations lack important metadata (streaming, stateful/stateless, sync/async); suggested richer annotation infrastructure.                                                                           |
|  17 | Better abstractions: recommended libraries to model tasks, agents, conversations, models, tool/skill managers for easier agent development.                                                                                       |
|  18 | Encouraged community participation via Discord, blog, and GitHub PRs.                                                                                                                                                             |
|  19 | Concluded that MCP supports agent-to-agent co                                                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XreKuebKpaA)