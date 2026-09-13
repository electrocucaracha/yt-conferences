---
layout: default
title:
  "Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs - Peter O'Neill
  & Boris Kurktchiev"
nav_order: 331
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Boris and Peter discuss the limitations of traditional
  VPN-based network security, especially in the context of AI and automation, and
  advocate for identity-based access control using reverse proxies. They explain how
  tools li...
resource: https://www.youtube.com/watch?v=0tq06AAdKWQ
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Boris and Peter discuss the limitations of traditional VPN-based network security, especially in the context of AI and automation, and advocate for identity-based access control using reverse proxies.
They explain how tools like Keycloak (for identity and authorization) and Envoy (as a reverse proxy) can be combined to enforce authentication and authorization at every endpoint, providing granular control and comprehensive audit logging.
Through a live demo, they show how JWTs encapsulate user identity and permissions, enabling precise access decisions and short-lived tokens to reduce risk.
The speakers emphasize that this approach not only improves security and compliance by tying actions to specific identities and intents, but also addresses the challenges posed by both human and machine actors in modern environments.
While acknowledging that VPNs still have a role, they argue that organizations must modernize their security posture by layering identity-aware controls throughout their infrastructure.

# Main Points

|   # | Main point                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on identity-based control with reverse proxies and its importance.                            |
|   2 | Boris (Field CTO, Teleport) and Peter (Sales Engineering Manager, Teleport) are the presenters.                |
|   3 | AI has exposed weaknesses in traditional identity and access control methods.                                  |
|   4 | VPNs act as a single front gate, allowing lateral movement and insufficient control once inside.               |
|   5 | Automation and AI agents increase risks if not properly authorized and authenticated.                          |
|   6 | The proposed solution is to add authentication and authorization to every endpoint, for all users and agents.  |
|   7 | Reverse proxies (using Envoy) can centralize authentication, authorization, and logging for any service.       |
|   8 | Reverse proxies allow legacy systems to benefit from modern security controls without internal changes.        |
|   9 | Audit trails are improved with identity-aware access logs, showing who did what, when, and why.                |
|  10 | The architecture uses open source projects: Keycloak (identity provider) and Envoy (reverse proxy).            |
|  11 | OAuth2 and OpenID Connect (OIDC) are used for identity and authorization.                                      |
|  12 | JWTs (JSON Web Tokens) encapsulate identity information and are passed between services.                       |
|  13 | JWTs are encoded, not encrypted, and should not contain secrets; they have short TTLs to reduce risk.          |
|  14 | The demo shows how endpoints deny access without identity, and allow/deny based on user roles and tokens.      |
|  15 | Audit logs now include detailed identity information, supporting compliance and intent tracking.               |
|  16 | The approach enables zero trust: do not trust the network, trust each authenticated and authorized action.     |
|  17 | Reverse proxies can be used for web apps and TCP traffic, but may require changes to workflows and tooling.    |
|  18 | VPNs are not obsolete but insufficient alone; combining VPNs with endpoint-level authorization is recommended. |
|  19 | Technologies like Spiffy can help secure machine-to-machine connectivity with mTLS.                            |
|  20 | The solution is especially effective for human users; machine users may need additional tools.                 |
|  21 | The demo and code are availab                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0tq06AAdKWQ)
