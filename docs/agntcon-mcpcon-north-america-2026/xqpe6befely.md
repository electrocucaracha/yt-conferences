---
layout: default
title: "Ship Your Most Powerful Agent: 7 Factors for Production Guarantees - Zayne Turner, Workato"
nav_order: 136
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Zane Turner, VP of Developer Relations at Workato, presents an open-source engineering methodology called the "Seven Factors for Production Guarantees" to help enterprises trust agentic AI systems ...'
resource: "https://www.youtube.com/watch?v=XQpE6BefELY"
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

Zane Turner, VP of Developer Relations at Workato, presents an open-source engineering methodology called the "Seven Factors for Production Guarantees" to help enterprises trust agentic AI systems in production.
The framework introduces the concept of an "agentic control plane," a deterministic layer that sits between probabilistic agent reasoning and enterprise outcomes to manage real-world consequences, identity, and regulatory compliance.
Turner outlines seven key factors, including governing operations, enforcing deterministic mutations, using intent-based communication to prevent data leakage, implementing bounded access with zero trust, designing safe retries, establishing recovery contracts, and ensuring observability by design.
He emphasizes that agents cannot be trusted as security deputies and must operate within strict, deterministic boundaries to handle sensitive data and state changes safely.
The methodology is available on GitHub as a set of Markdown principles and antipatterns, inviting industry contributions to refine these best practices for secure agentic deployments.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : The presentation introduces "Seven Factors for Production Guarantees," an open-source engineering methodology by Workato to determine if an agentic system has a robust control plane.                                                                                                                         |
|   2 | : An agentic control plane is a deterministic layer situated between probabilistic agentic intent and enterprise outcomes, ensuring agents are safe for production use with real-world consequences.                                                                                                             |
|   3 | : The methodology assumes every agentic system has a "reasoning layer" (probabilistic, where agents excel) and a "control plane layer" (deterministic, handling enterprise needs like identity, standards, and state management).                                                                                |
|   4 | : Govern Operations**: Enterprise concerns must not defer to agentic protocols. Just because an agent works does not mean the business is protected. Engineers must balance security, latency, and user experience by deciding which operations require strict control plane governance based on risk tolerance. |
|   5 | : Deterministic Mutations**: Models should not directly perform writes, deletes, or updates. Sensitive reads and all mutations must pass through a deterministic layer to ensure audit logging, state reconciliation, and business protection.                                                                   |
|   6 | : Intent-Based Communication**: Tool and API design must avoid leaking implementation details (e.g., raw database IDs) into the model’s context. Tools should use intent-based shapes (e.g., customer email) rather than internal identifiers to improve security and reduce token waste.                        |
|   7 | : Bounded Access**: Agents must never be treated as trusted "deputies" that hold secrets or elevated privileges. Zero-trust principles apply, requiring strict limits on what agents can reach, especially in multi-agent scenarios to prevent "shadow path" antipatterns.                                       |
|   8 | : Safe Retries**: Agents may retry operations at high volumes without understanding return codes. Systems must be designed for idempotency to handle duplicate requests, partial failures, and state rollbacks, as models do not guarantee stopping behavior.                                                    |
|   9 | : Recovery Contracts**: Responses should be structured and contracted to guide agent next steps (e.g., retry, escalate to human) rather than relying on standard HTTP codes. Responses must be fixed in shape to prevent information leakage and limit free-text injection vectors.                              |
|  10 | : Observability by Design**: Systems must provide comprehensive observability for both engineering debugging and business audit compliance. This includes recording intent, outcome, and all touched data to reconstruct events without cobbled-together logs.                                                   |
|  11 | : The framework is available as an open-source repository on GitHub, containing principle descriptions, antipatterns, prior art, and industry examples. It is open for community contributions via issues and pull requests.                                                                                     |
|  12 | : A sample app ("Dewey Resort") demonstrates intent-based interfaces where tools accept user-friendly identifiers (booking codes, emails) instead of internal record IDs, with logic handling verification and lookups behind the scenes.                                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XQpE6BefELY/hqdefault.jpg)](https://www.youtube.com/watch?v=XQpE6BefELY)

[Watch on YouTube](https://www.youtube.com/watch?v=XQpE6BefELY)
