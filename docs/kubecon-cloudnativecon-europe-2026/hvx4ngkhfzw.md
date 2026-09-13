---
type: Video Note
title: "Envoy in the Era of Agentic Workloads - Yan Avlasov, Google & Erica Hughberg, Tetrate"
description: "In this presentation, Erica Huberg and Yan, both maintainers of the Envoy AI Gateway, discuss the evolving challenges and opportunities in networking for agentic AI workloads. They explain how the rise of AI agents, which require complex au..."
resource: https://www.youtube.com/watch?v=HvX4nGkhfZw
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Erica Huberg and Yan, both maintainers of the Envoy AI Gateway, discuss the evolving challenges and opportunities in networking for agentic AI workloads.
They explain how the rise of AI agents, which require complex authorization, observability, and support for rapidly changing protocols, has transformed traditional traffic handling and necessitated new solutions at the proxy layer.
Envoy, with its extensibility through features like dynamic modules and support for languages beyond C++, is positioned as a robust, future-ready foundation for managing AI traffic, enforcing security policies, and enabling fine-grained access control.
The speakers highlight ongoing community efforts to address emerging standards, improve guardrail integration, and support agent-to-agent communication, inviting others to contribute and collaborate.
They conclude by emphasizing Envoy’s adaptability, production maturity, and active community, encouraging participation and showcasing resources to help newcomers get involved.
# Main Points

|   # | Main point                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------- |
|   1 | The talk title was updated to "Envoy, the future ready foundation for agentic AI networking."                 |
|   2 | Presenters: Erica Huberg (Envoy AI gateway maintainer) and Yan (Envoy senior maintainer, 8 years, Google).    |
|   3 | Envoy AI gateway helps manage AI traffic and is maintained by a community.                                    |
|   4 | AI agents now require more complex networking and authorization than traditional API calls.                   |
|   5 | Inference traffic is variable and compute-intensive, similar to past fintech API challenges.                  |
|   6 | Agent actions require authorization and knowledge of available tools, complicating policy enforcement.        |
|   7 | Human-built applications are predictable; agents using LLMs are less so.                                      |
|   8 | Traditional stateless, RESTful APIs are being replaced by more complex, stateful agentic protocols.           |
|   9 | Proxies now need to handle increased, more complex traffic, including reading request bodies.                 |
|  10 | New and evolving standards (e.g., MCP, ADA) and protocols are emerging rapidly.                               |
|  11 | Migration between protocols (e.g., chat completions to responses) is ongoing and challenging.                 |
|  12 | Envoy proxy provides a strong foundation for scalable, reliable AI networking.                                |
|  13 | Security and identity management are more complex with agents (user and agent workload identities).           |
|  14 | Token exchange and authorization policies are evolving (e.g., OpenID Connect, anthropic, octa).               |
|  15 | Observability and auditability are top user requests; open telemetry integration is ongoing.                  |
|  16 | Policy enforcement and guardrails are implemented via Envoy proxy.                                            |
|  17 | Envoy supports extensibility through dynamic modules, allowing filters in Go and Rust.                        |
|  18 | Dynamic modules simplify extending Envoy without external processes or C++ knowledge.                         |
|  19 | Envoy AI gateway is Kubernetes-native but can run standalone; provides unified API for multiple AI providers. |
|  20 | Fine-grained access control (e.g., OpenFGA) can be integrated via dynamic modules.                            |
|  21 | Stateful MCP session handling is complex but supported; feedback is encouraged.                               |
|  22 | Agent-to-agent (A2A) communication is emerging but not yet widespread.                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HvX4nGkhfZw)