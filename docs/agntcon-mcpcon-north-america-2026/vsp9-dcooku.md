---
layout: default
title: "Workshop: Break the Lethal Trifecta: Designing Access Boundaries Agents Can... Z. Turner & C. Miller"
nav_order: 150
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'This workshop, presented by Zay Turner and Chris Miller from Marcato, focuses on securing AI agents by addressing the "lethal trifecta" of prompt injection, access to private data, and external com...'
resource: "https://www.youtube.com/watch?v=vsP9-DCOokU"
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

This workshop, presented by Zay Turner and Chris Miller from Marcato, focuses on securing AI agents by addressing the "lethal trifecta" of prompt injection, access to private data, and external communication capabilities.
Participants use an intentionally vulnerable open-source banking application to explore security flaws across three stations: unauthorized money transfers, leakage of internal data, and privilege escalation via hardcoded passphrases.
The session demonstrates that relying solely on system prompts for security is ineffective, as models can be manipulated to bypass instructions and expose sensitive information or execute unauthorized actions.
To mitigate these risks, the presenters advocate for implementing a "control plane" that enforces business logic and security policies outside the model’s context, ensuring that tools are shaped by intent rather than exposing raw implementation details.
By structurally separating permissions and sanitizing data outputs, organizations can limit the blast radius of potential attacks and prevent agents from acting as trusted entities with excessive agency.

# Main Points

|   # | Main point                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | "lethal trifecta" of AI agent vulnerabilities.                                                                                                                                                        |
|   2 | (untrusted content), access to private data, and the ability to externally communicate or exfiltrate data.                                                                                            |
|   3 | "Dewey Bank" app where transaction memos serve as the vector for prompt injection attacks.                                                                                                            |
|   4 | "deputy" (trusted entity) because it is structurally susceptible to confusion and manipulation.                                                                                                       |
|   5 | ; the broken version lacks business logic, allowing the model to decide transactions, while the fixed version enforces strict validation rules and trusted payee lists.                               |
|   6 | ; the broken version exposes internal database IDs and implementation details in responses, while the fixed version sanitizes outputs to hide internal structures.                                    |
|   7 | ; the broken version relies on a passphrase in the prompt to unlock support agent capabilities, while the fixed version structurally removes support tools from the customer-facing server namespace. |
|   8 | , as prompts are easily bypassed and do not constitute a robust security boundary.                                                                                                                    |
|   9 | "control plane" is defined as the layer that sits between model intent and business consequences, ensuring that models cannot own or execute high-risk actions without validation.                    |
|  10 | , meaning tools should abstract away internal details and limit the surface area exposed to the model.                                                                                                |
|  11 | , making structural separation of permissions critical.                                                                                                                                               |
|  12 | , including shaping tools by intent, enforcing bounded tool limits, and preventing models from making business decisions.                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/vsP9-DCOokU/hqdefault.jpg)]("https://www.youtube.com/watch?v=vsP9-DCOokU")

[Watch on YouTube](https://www.youtube.com/watch?v=vsP9-DCOokU)
