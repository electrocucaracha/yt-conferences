---
type: Video Note
title: "Beyond the Sandbox: Security at the Host Layer - Lorenzo Verna & Pietro Valfrè, Denied"
description: "The speakers discuss their innovative approach to behavioral authorization for AI agents, emphasizing the need for new security models as agents evolve from simple assistants to autonomous entities capable of real-world actions. Traditional..."
resource: https://www.youtube.com/watch?v=jTkKzNUT1fw
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speakers discuss their innovative approach to behavioral authorization for AI agents, emphasizing the need for new security models as agents evolve from simple assistants to autonomous entities capable of real-world actions.
Traditional authorization methods, such as resource-based controls and sandboxing, are insufficient because they lack visibility into agent behavior and cannot effectively control what agents do with their access.
Their solution involves embedding authorization policies directly within the agent, enabling interception and evaluation of every tool call based on content and context, rather than just identity or scope.
This approach uses a layered evaluation strategy, starting with deterministic rules and escalating to model-based assessments as needed, and supports integration with various external tools for enhanced policy enforcement.
The system also provides audit trails and policy recommendations, allowing for iterative refinement and greater control over agent actions, with the goal of creating a horizontal authorization layer compatible with any agent framework.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Behavioral authorization system designed specifically for agents                                                                                   |
|   2 | Focus on controlling agent actions, not just protecting resources from external threats                                                            |
|   3 | Shift from traditional authorization to setting boundaries around agents to authorize outgoing actions                                             |
|   4 | Enforcement point moves inside the agent, not just in front of resources                                                                           |
|   5 | Evaluation must inspect the full request payload, not just metadata                                                                                |
|   6 | Enhanced visibility by intercepting all agent tool calls and actions                                                                               |
|   7 | Policies and rules are integrated as part of the agent’s design                                                                                    |
|   8 | Traditional approaches like sandboxing, resource scopes, and server-side gateways have blind spots, lacking full behavioral control and visibility |
|   9 | Instructions are not reliable for security as they are not auditable and can be overwritten                                                        |
|  10 | New approach provides global visibility, content-aware inspection, and decision isolation by decoupling evaluation from agent execution            |
|  11 | Every tool call is intercepted, evaluated, and responded to (allow, deny, or obligation)                                                           |
|  12 | Three-layer evaluation strategy: deterministic (Rego), LLM-based content classification, and model-based policy evaluation                         |
|  13 | Escalation system automatically chooses the appropriate evaluation layer based on request complexity                                               |
|  14 | Policy authoring is iterative: observe agent actions, log and analyze them, and suggest policies based on actual tool call schemas                 |
|  15 | System supports integration with various agent frameworks and external evaluation tools                                                            |
|  16 | Policies are always logged and auditable; models can be plugged in for custom evaluations (e.g., PII detection)                                    |
|  17 | Default-deny approach; new tools must be explicitly authorized                                                                                     |
|  18 | System can recommend or draft policy templates based on observed agent behavior                                                                    |
|  19 | Aim to provide an “auto mode” for authorization applicable to any agent framework                                                                  |
|  20 | Open to feedback and early user onboarding; integrations and SDKs are available and open source                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jTkKzNUT1fw)