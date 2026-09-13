---
layout: default
title:
  Sovereign Identities for Your Cloud Native Architecture... Alexander Schwartz
  & Sebastian Łaskawiec
nav_order: 338
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk at KubeCon, Alexander Schwarz and Sebastian Wascavis discuss
  implementing sovereign identities in cloud-native architectures using Keycloak,
  focusing on secure single sign-on (SSO) and resource access delegation via OpenID
  Conn...
resource: https://www.youtube.com/watch?v=7q4oTEfrz1o
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

In this talk at KubeCon, Alexander Schwarz and Sebastian Wascavis discuss implementing sovereign identities in cloud-native architectures using Keycloak, focusing on secure single sign-on (SSO) and resource access delegation via OpenID Connect.
They explain how Keycloak manages user credentials, issues short-lived tokens, and supports integration with various identity providers and enterprise systems like LDAP.
The presenters demonstrate traditional client authentication using client secrets, then showcase more secure and streamlined approaches using client assertions and Kubernetes service account tokens, eliminating the need for confidential secrets.
They highlight recent and upcoming Keycloak features, such as standard token exchange, JWT authorization grants, improved observability, fine-grained admin permissions, and automated user lifecycle workflows.
The session concludes with a Q&A covering advanced configurations, multi-cluster setups, and future roadmap items like organization roles and enhanced proxy documentation.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction to sovereign identities in cloud native architecture using Keycloak                                                                                      |
|   2 | Single sign-on (SSO) enables one identity and delegated resource access                                                                                               |
|   3 | OpenID Connect is the primary protocol used                                                                                                                           |
|   4 | Keycloak issues short-lived tokens to keep credentials secure                                                                                                         |
|   5 | Digital sovereignty is achieved by self-hosting identity systems                                                                                                      |
|   6 | Open source Keycloak allows influence over roadmap and features                                                                                                       |
|   7 | Keycloak setup: download container, connect to database, configure services                                                                                           |
|   8 | Users authenticate via Keycloak and receive tokens to access services                                                                                                 |
|   9 | Services can validate tokens directly or via Keycloak introspection                                                                                                   |
|  10 | Keycloak supports integration with SAML, OpenID Connect, LDAP, and other providers                                                                                    |
|  11 | Features include passkeys, 2FA, user self-registration, password recovery                                                                                             |
|  12 | Recent updates: standard token exchange, JWT authorization grants, 2FA recovery codes, passkey support, new guides for AI integration, and user lifecycle workflows   |
|  13 | Upcoming: full support for user lifecycle workflows (automated deactivation, onboarding, etc.)                                                                        |
|  14 | Fine-grained admin permissions allow delegation of resource administration                                                                                            |
|  15 | Enhanced observability: integrated OpenTelemetry for tracing, improved logging, metrics, and Grafana dashboards                                                       |
|  16 | Trust and federation improvements: reuse of tokens, not credentials; JWT authorization grants for federated authentication                                            |
|  17 | Spiffe support for non-human identities; Kubernetes service account tokens can be used for authentication                                                             |
|  18 | Demo covered three confidential client authentication methods: client secret, client assertions (service account tokens), and machine-to-machine (client credentials) |
|  19 | Configuration steps for client secret and federated JWT clients in Keycloak admin console                                                                             |
|  20 | Limitations: Kubernetes rotates tokens every 10 minutes; cross-cluster authentication requires trusted CAs and unique issuer URLs                                     |
|  21 | Keycloak 26.6 release: full support for JWT authorization grant, federated client authentication, workflows, organization groups, rolling                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7q4oTEfrz1o)
