---
layout: default
title: "Breaking the Agentic Loop - Multi-Turn Exploits Against... - Bar Kaduri, Capsule Security"
nav_order: 28
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "In this conference session, Bar, Head of Research at Capsule Security, explores the security vulnerabilities inherent in AI agents by demonstrating how seemingly benign individual actions can combi..."
resource: "https://www.youtube.com/watch?v=OUhHjBS-XAA"
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

In this conference session, Bar, Head of Research at Capsule Security, explores the security vulnerabilities inherent in AI agents by demonstrating how seemingly benign individual actions can combine to create dangerous credential leakage paths.
He explains that attackers exploit the "agentic loop"—the cycle of planning, acting, and observing—by breaking down malicious goals into small, harmless-looking steps or steering conversations to bypass guardrails, a technique illustrated through demos involving tool chaining, conversation manipulation, and memory poisoning in tools like Cursor.
To counter these threats, the speaker advocates for the implementation of deterministic "agentic hooks" that intercept agent actions before they occur, using small language models (SLMs) to verify intent and context against organizational policies.
He highlights a defense mechanism using a fine-tuned Nvidia Nemotron 4B model that achieved approximately 97% accuracy in blocking attacks while maintaining a low false-positive rate.
Finally, he introduces an ongoing initiative within the OWASP GenAI Security Project to standardize these hooks across different AI harnesses, aiming to create a unified framework for defenders to secure AI agents effectively.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                   |
|   2 | : reading documents (allowed), accessing credentials (allowed), sending requests (allowed) - but combined create credential exfiltration route |
|   3 | : Bar, Head of Research at Capsule Security, 14 years in cybersecurity                                                                         |
|   4 | , leading Agent Control Standard (ACS) under GenAI Security Project                                                                            |
|   5 | , memory, and capabilities can split malicious actions across multiple steps                                                                   |
|   6 | : plan → act → observe → update state → repeat                                                                                                 |
|   7 | : multiple messages directing conversation; splitting task into innocent-seeming fragments                                                     |
|   8 | : single step causing multi-step distribution; conversation direction; tool chaining; environment injection                                    |
|   9 | (Nvidia), Nemo Tron 4B, and Agent Lab frameworks                                                                                               |
|  10 | (attacker knows infrastructure)                                                                                                                |
|  11 | : diagnostic work combined with credential theft in single request                                                                             |
|  12 | : hidden instructions in readme file; SSH key exfiltrated; memory contamination across sessions                                                |
|  13 | : benign tool chaining (most effective), pretexting, trusted-looking outbound traffic, persistence                                             |
|  14 | : agentic hooks at control points in agent loops                                                                                               |
|  15 | (SLM) placed in hooks to assess intent and policy alignment                                                                                    |
|  16 | ~97% accuracy with Nemotron 4B defending against attacks                                                                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/OUhHjBS-XAA/hqdefault.jpg)](https://www.youtube.com/watch?v=OUhHjBS-XAA)

[Watch on YouTube](https://www.youtube.com/watch?v=OUhHjBS-XAA)
