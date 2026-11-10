---
layout: default
title: "Gating High-Risk Agentic Actions at the Relying Party with Exogenous... - Dominic Forrest, iProov"
nav_order: 74
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Dominic Forrest, CTO of i-Prove, introduces HAPS (Human Approval and Presence Specification), an open-source framework designed to ensure that high-risk actions taken by AI agents are explicitly au..."
resource: "https://www.youtube.com/watch?v=3BUTOTGlxxI"
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

Dominic Forrest, CTO of i-Prove, introduces HAPS (Human Approval and Presence Specification), an open-source framework designed to ensure that high-risk actions taken by AI agents are explicitly authorized by a genuine human.
The system addresses the security risks of agentic AI by requiring a "human-in-the-loop" verification process that binds the specific action, the identity of the approver, and the execution into a single cryptographically signed record.
HAPS utilizes biometric liveness detection to verify that the approver is a real person present at the moment of authorization, preventing spoofing via deepfakes, masks, or replay attacks.
By providing irrefutable proof of consent and execution, the framework allows organizations to grant AI agents broader system access while maintaining strict audit trails and compliance with high identity assurance standards like IAL2.
The specification is available under the Apache 2.0 license on GitHub, offering a vendor-agnostic solution that can integrate with various policy engines and identity providers to secure transactions and system updates.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (ID.me) and border crossings, often without the user’s direct awareness.                                                                                                              |
|   2 | /no authorization; users need assurance that an agent is executing the exact intended action (e.g., specific item, price, itinerary) rather than a similar one.                       |
|   3 | "Human-in-the-loop" is critical for high-risk AI actions to prevent unexpected or security-related errors, requiring a human to verify that the specific action matches their intent. |
|   4 | (Human Approval and Presence Specification), an open-source framework to provide proof that a genuine human authorized a specific AI action at a specific time.                       |
|   5 | :                                                                                                                                                                                     |
|   6 | :** Determining if an action requires an agent-resistant factor that AI cannot bypass.                                                                                                |
|   7 | :** Using biometric liveness (face) as a factor that agents cannot spoof, as they do not have physical faces.                                                                         |
|   8 | :** Ensuring irrefutable audit trails that match the requested action, the approver, the time, and the final execution.                                                               |
|   9 | : the genuine human presence, the specific action being approved, and the exact execution of that action.                                                                             |
|  10 | (Identity Assurance Level 2) compliant, meeting the same standards used by governments for high-value transactions.                                                                   |
|  11 | : it is the right person (face match), it is a real person (not a deepfake or mask), and the person is present right now.                                                             |
|  12 | , requiring facial approval for updates to maintain security while enabling automation.                                                                                               |
|  13 | , with no vendor lock-in; it can integrate with any policy engine, gateway, or biometric provider (e.g., YubiKey, passkeys).                                                          |
|  14 | , with proof-of-concept implementations achievable in as little as one hour.                                                                                                          |
|  15 | , it can also support time-based sessions (e.g., one hour), though this provides proof of authorization scope rather than proof of each individual transaction within that scope.     |
|  16 | , litigation, and law enforcement investigations, having processed hundreds of millions of identities with no known successful frauds against their liveness detection.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3BUTOTGlxxI/hqdefault.jpg)](https://www.youtube.com/watch?v=3BUTOTGlxxI)

[Watch on YouTube](https://www.youtube.com/watch?v=3BUTOTGlxxI)
