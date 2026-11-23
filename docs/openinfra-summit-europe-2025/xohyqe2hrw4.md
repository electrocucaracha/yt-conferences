---
layout: default
title: "Keystone: native federation support, advanced auth security, Rust"
nav_order: 73
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker presents a new Rust-based implementation of Keystone Identity V4, developed to address significant usability and security flaws in the current federation system, which lacks scheme supp..."
resource: "https://www.youtube.com/watch?v=XOHYqE2HRw4"
youtube_stats:
  view_count: 100
  like_count: 3
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

The speaker presents a new Rust-based implementation of Keystone Identity V4, developed to address significant usability and security flaws in the current federation system, which lacks scheme support and requires administrative restarts for changes.
This project, currently hosted on GitHub, introduces hardware security key authentication (such as YubiKeys) to eliminate passwords and prepare for post-quantum cryptography, while also reworking federation to allow domain managers to control identity providers and mappings via API.
The presentation demonstrates advanced features including restricted tokens that prevent privilege escalation and rescope, JWT-based workflow federation for CI/CD systems like GitHub, and fine-grained permissions using Open Policy Agent.
Although service accounts are not yet fully implemented, the architecture supports them through predefined permissions and token restrictions that bind external identities to specific projects or users.
The speaker emphasizes that this new system is not yet a drop-in replacement for Keystone V3 but offers a more secure, flexible, and performant foundation for future OpenStack identity management.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces a new Rust-based identity service for OpenStack Keystone, focusing on security key login, federation, and service accounts.                           |
|   2 | Current Keystone federation is described as unusable due to lack of customer control, required restarts for changes, and poor JWT support.                                        |
|   3 | The new project is implemented in Rust for memory safety and post-quantum cryptography preparation, though it is not yet an official OpenStack project.                           |
|   4 | The solution targets the V4 identity API because V3 has conceptual limitations that prevent proper federation support.                                                            |
|   5 | Security key authentication uses a challenge-response flow where the server sends a challenge, the hardware key signs it, and the server verifies the signature to issue a token. |
|   6 | The CLI supports passwordless login via security keys, eliminating the need for passwords and preparing for post-quantum security.                                                |
|   7 | Federation management is now fully API-driven, allowing domain managers to control identity providers (IdPs) and mappings within their domains.                                   |
|   8 | Shared IdPs allow global authentication sources, while private IdPs can be strictly bound to specific domains for tenant isolation.                                               |
|   9 | Domain binding can be enforced at the IdP level, the mapping level, or through specific claims within the JWT.                                                                    |
|  10 | JWT login is supported for exchanging external tokens for Keystone tokens, enabling integration with systems like GitHub and GitLab.                                              |
|  11 | Workflow federation allows CI/CD pipelines to authenticate without hardcoded secrets by exchanging JWTs for scoped tokens.                                                        |
|  12 | Restricted tokens implement fencing to prevent rescoping into different projects, ensuring service accounts remain bound to specific scopes.                                      |
|  13 | Token restrictions can limit token renewal and rescope capabilities to enhance security for automated workflows.                                                                  |
|  14 | Service accounts are a planned feature for non-human entities, allowing JWT-based authentication without traditional user credentials.                                            |
|  15 | Policies are implemented using Open Policy Agent (OPA) to enable fine-grained permissions beyond standard roles, such as restricting specific API operations.                     |
|  16 | The project aims to support TLS client certificates as a form of two-factor authentication or primary authentication for domain-level security.                                   |
|  17 | Performance tests show improved throughput in Rust compared to Python, though latency improvements are limited by password hashing requirements.                                  |
|  18 | The project is currently on GitHub and invites users to test it and report issues, as it is not yet a drop-in replacement for all Keystone features.                              |
|  19 | Future plans include completing the token restriction API, finalizing service accounts, and implementing IP whitelisting for authentication.                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XOHYqE2HRw4/hqdefault.jpg)](https://www.youtube.com/watch?v=XOHYqE2HRw4)

[Watch on YouTube](https://www.youtube.com/watch?v=XOHYqE2HRw4)
