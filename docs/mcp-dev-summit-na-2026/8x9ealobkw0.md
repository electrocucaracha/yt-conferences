---
layout: default
title: MCP vs CLI  OpenAI Engineer Says You Need Both
nav_order: 76
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Nick Cooper, a member of technical staff at Legen Tech, presents an exploratory talk on the evolution of the Model Context Protocol (MCP), framing it not as a static standard but as a high-level la..."
resource: "https://www.youtube.com/watch?v=8X9EalObKw0"
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

Nick Cooper, a member of technical staff at Legen Tech, presents an exploratory talk on the evolution of the Model Context Protocol (MCP), framing it not as a static standard but as a high-level layer in a stack of communication abstractions that ranges from raw electrical signals to HTTP and REST.
He argues that MCP’s primary value lies in its intent-driven design, which shifts API development from generic function calling to creating secure, observable, and efficient interfaces specifically tailored for AI models, thereby reducing token costs and improving context management.
Cooper addresses the debate between Command Line Interfaces (CLIs) and MCPs by suggesting they are complementary rather than competing; while CLIs offer low-level efficiency and existing infrastructure, MCP provides the necessary structure and security standards for agentic interactions, and the most powerful systems will likely combine both.
Looking forward, he envisions MCP evolving into a true agent-to-agent protocol that facilitates delegated work and structured communication between AI entities, moving beyond simple tool invocation.
Finally, Cooper highlights the emerging challenge of identity and discovery in a fragmented ecosystem of MCP servers and clients, urging the community to collaborate on robust standards that make these complex compositions easier to find and utilize.

# Main Points

|   # | Main point                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nick Cooper, a member of technical staff at Legen Tech, presents an exploratory talk on the evolution and future of the Model Context Protocol (MCP).                                                                   |
|   2 | The presentation builds on previous concepts of transformation and composition, where combining simple building blocks creates complex, valuable interactions for users and businesses.                                 |
|   3 | Over the past year, the ecosystem has expanded with gateways, communication systems, and new features like tasks and the MCP UI extension.                                                                              |
|   4 | Protocols are described as languages for communication between systems, with MCP serving as a high-level abstraction that touches on lower layers like standard IO.                                                     |
|   5 | Layers of abstraction and standardization create injection points for security, policy controls, and telemetry, such as the upcoming interceptor feature.                                                               |
|   6 | Efficiency in protocol communication is measured by concepts per second, aiming to minimize token usage since output tokens are more expensive and time-consuming than input.                                           |
|   7 | Early MCP usage focused on function calling, but the explosion of available tools leads to context exhaustion when exposing large amounts to a single model.                                                            |
|   8 | Two emerging patterns for handling tool complexity are shell file system-like invocation and code-like invocation, where tools become functions in languages like TypeScript or Python.                                 |
|   9 | These patterns represent a higher layer of abstraction that improves token efficiency by allowing models to write concise code to filter output and combine commands.                                                   |
|  10 | The debate between CLIs and MCPs is resolved by recognizing that both are necessary; CLIs provide existing capabilities, while MCPs bring AI-specific intent and structure.                                             |
|  11 | MCP is more than just an API; it is an API for AI that encourages developers to consider how models will use tools, ensuring security, observability, and best practices.                                               |
|  12 | MCP standardizes authentication using OAuth 2.1 and defines JSON-encodable schemas, explicitly targeting AI models with vaguely known properties rather than just other developers.                                     |
|  13 | Effective API design for MCP involves creating high-level, intent-driven interfaces that simplify complex functionalities, such as reducing hundreds of email-related tools to simple actions like sending or drafting. |
|  14 | MCP is increasingly viewed as an agent-to-agent protocol, where tools represent abilities, tasks represent delegated work, and messages provide structured communication.                                               |
|  15 | The future of MCP lies in agentic communication, allowing AI-capable entities to interpret intent directly and interact more fluidly without rigid client-side constraints.                                             |
|  16 | A major challenge facing the ecosystem is the discovery of identity, as the vast number of providers, clients, and hosts makes it difficult to find robust, discoverable solutions.                                     |
|  17 | The speaker calls for community participation in MCP discussions to collaboratively develop standards for identity and discovery across the expanding landscape of AI tools.                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8X9EalObKw0/hqdefault.jpg)](https://www.youtube.com/watch?v=8X9EalObKw0)

[Watch on YouTube](https://www.youtube.com/watch?v=8X9EalObKw0)
