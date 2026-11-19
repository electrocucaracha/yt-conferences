---
layout: default
title: "From Agent to Infrastructure: The Goose Development Kit - Steve Lee, Block"
nav_order: 73
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Steve Lee, lead of the Spiral organization within Block Inc., presented the evolution of the Goose agent and the upcoming Goose Development Kit (GDK)."
resource: "https://www.youtube.com/watch?v=ISFzl170ocs"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Steve Lee, lead of the Spiral organization within Block Inc., presented the evolution of the Goose agent and the upcoming Goose Development Kit (GDK).
He explained that while Goose began as a standalone application, the team is shifting focus to providing an SDK that allows developers, startups, and enterprises to build custom AI experiences on top of the core engine.
The GDK supports extensive provider integration, including over 50 models, and offers two primary interfaces: the Agent Client Protocol (ACP) for isolated processes and a Rust API for embedded applications, with bindings planned for other languages.
Lee highlighted significant architectural improvements, such as the transition from a traditional agent loop to a state machine, which enhances reliability for long-running tasks and simplifies third-party customization.
Additionally, he emphasized the project’s commitment to open intelligence values, including privacy, accessibility, and decentralization, demonstrated through robust local model support and the integration of Mesh LLM, a peer-to-peer inference network.
A live demo showcased a Signal messenger fork using GDK and Mesh LLM to perform inference with Bitcoin micro-payments, illustrating the convergence of open-source AI, decentralized compute, and financial infrastructure.
Lee concluded by inviting the community to contribute to the project and noting that Spiral offers grants to support the development of open intelligence tools.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (GDK) Overview**: Block’s Spiral organization is launching the Goose Development Kit (GDK), an SDK allowing developers to build custom AI applications on top of the Goose core engine. The MVP is targeted for release by Thanksgiving.                                                                                            |
|   2 | : Goose was donated to the Linux Foundation and is part of the AAIF alongside Anthropic and OpenAI. The core development team moved to Spiral, a Block initiative focused exclusively on open-source public goods, to ensure neutral governance.                                                                                    |
|   3 | : Spiral defines "open intelligence" through four pillars: open source/standards, decentralization (avoiding provider lock-in), privacy (local execution of sensitive data), and accessibility (running on smaller, less expensive hardware).                                                                                       |
|   4 | : GDK supports two primary integration methods:                                                                                                                                                                                                                                                                                     |
|   5 | (Agent Client Protocol)**: Ideal for running agents in separate processes, on remote machines, or for applications requiring a common interface across multiple agent harnesses.                                                                                                                                                    |
|   6 | : Enables embedding the agent directly into an application binary, offering lower-level control and suitability for constrained or embedded environments.                                                                                                                                                                           |
|   7 | : While the core is Rust, bindings are available for Kotlin and Python, with Swift, Go, and TypeScript support expected.                                                                                                                                                                                                            |
|   8 | : Goose is optimized for small, local models to enhance privacy, reduce latency, lower costs, and enable offline functionality. Features include automatic hardware capability detection and the ability to embed open-weight models directly into the application binary.                                                          |
|   9 | : Goose recently transitioned from a traditional agent loop to a state machine architecture. This allows long-running tasks to persist state without keeping processes alive, enabling resumption after interruptions and simplifying third-party hook integration without requiring core team involvement for every customization. |
|  10 | : Benchmarks using Terminal Bench 4.0 with a constant model showed Goose is significantly more cost-effective than competitors, with OpenCode 18% more expensive, Codex 31% more expensive, and Hermes 75% more expensive per trial.                                                                                                |
|  11 | : GDK supports Mesh LLM, a peer-to-peer inference network. This allows users to tap into a decentralized network of compute nodes (laptops, servers, TEEs) for inference, paying via Bitcoin Lightning for compute resources.                                                                                                       |
|  12 | (MHS)**: Goose supports Anthropic’s Model Hardware Standard (MHS), demonstrated by a use case where Goose monitored a robotic arm, detected an error, corrected the program, and redeployed it to fix the physical action.                                                                                                          |
|  13 | : A demo showcased an agent embedded in a Signal fork, using Mesh LLM for inference and a Bitcoin Lightning wallet for micro-payments, illustrating the integration of open intelligence, decentralized compute, and Bitcoin.                                                                                                       |
|  14 | : Spiral offers grants for open intelligence projects, including ideas for GDK, Mesh LLM, or other initiatives that promote secure, open, and accessible AI.                                                                                                                                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ISFzl170ocs/hqdefault.jpg)](https://www.youtube.com/watch?v=ISFzl170ocs)

[Watch on YouTube](https://www.youtube.com/watch?v=ISFzl170ocs)
