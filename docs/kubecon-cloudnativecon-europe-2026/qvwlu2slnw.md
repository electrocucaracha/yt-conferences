---
layout: default
title:
  "SPIFFE Meets OAuth: Federated Identity for Cloud Native Workloads - Yoshiyuki
  Tabata, Hitachi, Ltd."
nav_order: 323
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Yoshik Tabata discusses how Spiffy and OAuth can be
  combined to enable federated identity and secure user authorization across multiple
  trust domains in cloud-native environments. He explains that modern platforms often
  spa...
resource: https://www.youtube.com/watch?v=_qVWLU2sLnw
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

In this session, Yoshik Tabata discusses how Spiffy and OAuth can be combined to enable federated identity and secure user authorization across multiple trust domains in cloud-native environments.
He explains that modern platforms often span multiple Kubernetes clusters and organizations, each with its own security authority, making federated identity challenging, especially for user authorization.
While Spiffy effectively handles workload identity federation, propagating user authorization across trust domains is more complex and cannot be solved by simply passing tokens or using basic token exchange.
Tabata introduces a standards-based approach using OAuth identity and authorization chaining, which combines token exchange and JWT-based authorization grants, allowing each trust domain to independently reissue authorization while securely authenticating workloads with Spiffy credentials.
He demonstrates this approach using Keycloak as the authorization server and Spire as the Spiffy signing authority in a multi-cluster Kubernetes setup, showing how user authorization is safely propagated and reissued across domains without relying on static secrets.
The session concludes with a Q&A, clarifying that the approach is currently experimental and focused on propagating authorization data and workload identity, rather than centralized policy management.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session topic: Spiffy and OAuth for federated identity in cloud native workloads across multiple trust domains                            |
|   2 | Modern platforms have multiple security authorities (trust domains), not a single security boundary                                       |
|   3 | Workload identities and user authorization are issued and evaluated independently in different parts of the system                        |
|   4 | Spiffy issues workload identities; OAuth authorization servers issue tokens with scopes and claims                                        |
|   5 | Trust domain: boundary where identity and authorization decisions are made; across trust domains, nothing is trusted by default           |
|   6 | Spiffy and OAuth define trust domains differently but are treated as the same for simplicity in this talk                                 |
|   7 | Workload identity federation works well with Spiffy using trust bundles; workloads can authenticate across domains without shared secrets |
|   8 | User identity and authorization propagation across trust domains is challenging                                                           |
|   9 | Passing access tokens across trust domains is discouraged; breaks audience constraints and obscures authorization decision origins        |
|  10 | Token exchange alone does not establish trust between domains                                                                             |
|  11 | Secure federated identity requires combining token exchange (RFC 8693) and JWT-based authorization grants (RFC 7523)                      |
|  12 | Identity chaining flow: request crosses trust domains, using token exchange and JWT authorization grants to reissue authorization         |
|  13 | Services must authenticate when exchanging tokens; static client secrets are not scalable                                                 |
|  14 | Spiffy-based client authentication allows cryptographically strong workload identity verification instead of shared secrets               |
|  15 | Authorization server must know what is delegated, for whom, and which workload performed delegation                                       |
|  16 | Demo uses Keycloak (as authorization server) and SPIRE (as Spiffy signing authority) in two Kubernetes clusters (minikube A and B)        |
|  17 | SPIRE servers are federated; Keycloak retrieves trust bundles to verify Spiffy JWTs for client authentication                             |
|  18 | Sample API servers use Envoy filters for token introspection and cross-domain token exchange                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_qVWLU2sLnw)
