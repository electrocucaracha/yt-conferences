---
type: Video Note
title: "Tailor Made: Dynamic Fine-Grained Authorization for API Traffic - Erica Hughberg & Andres Aguiar"
description: "In this presentation, the speakers discuss the challenges of implementing real-time, fine-grained authorization for API traffic, particularly in complex environments where both internal and external resources must be protected. They highlig..."
resource: https://www.youtube.com/watch?v=A1FXOwUmA6M
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, the speakers discuss the challenges of implementing real-time, fine-grained authorization for API traffic, particularly in complex environments where both internal and external resources must be protected.
They highlight the limitations of traditional token-based approaches, such as delayed revocation of access, and introduce a solution that combines Envoy’s dynamic modules with OpenFGA, a graph-based permission database.
Through a live demo, they show how permissions can be updated instantly and propagated in real time, enabling immediate changes to user and agent access without waiting for token expiration.
The integration allows for both coarse-grained checks at the gateway and fine-grained authorization decisions, all while maintaining high performance and scalability.
The presenters emphasize the flexibility and creativity enabled by this approach, encourage community involvement, and note that both Envoy and OpenFGA are open source projects.
# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation combines API traffic experience with security and authorization challenges.                                                                                        |
|   2 | OAuth had limitations, especially with immediate access revocation.                                                                                                             |
|   3 | Need for real-time authorization changes, especially in fintech and when routing API traffic to external resources.                                                             |
|   4 | Importance of contextual, real-time, fine-grained authorization (who, what, when, which resource).                                                                              |
|   5 | Auditability is crucial: knowing who accessed what and when, and ensuring revocations are applied.                                                                              |
|   6 | Coarse-grained authorization (token validity, claims) is typically handled at the gateway; fine-grained authorization (specific resource access) is handled in the application. |
|   7 | Envoy’s new dynamic modules make it easier to extend with new filters, such as for OpenFGA.                                                                                     |
|   8 | OpenFGA enables real-time, fine-grained authorization decisions using a graph-based model.                                                                                      |
|   9 | Demo showed users and agents with different access levels, updated in real time via OpenFGA.                                                                                    |
|  10 | Permission changes propagate instantly, with low latency (e.g., 4ms round trip in demo).                                                                                        |
|  11 | OpenFGA model allows direct and team-based permissions for users, agents, and resources.                                                                                        |
|  12 | Envoy AI Gateway integrates with OpenFGA via a dynamic module (composer), enabling authorization checks at the gateway.                                                         |
|  13 | Configuration is extensible and can fail closed if OpenFGA is unreachable.                                                                                                      |
|  14 | Metadata and previous filters in Envoy can provide context for authorization checks (e.g., quotas, rate limits).                                                                |
|  15 | OpenFGA centralizes permission data, enabling fast, fine-grained checks at the gateway without additional database lookups.                                                     |
|  16 | Both Envoy and OpenFGA are open source and have active communities.                                                                                                             |
|  17 | Presenters: Erica Hubber (Tetrate, Envoy AI Gateway maintainer) and Andreas (Okta, OpenFGA maintainer).                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=A1FXOwUmA6M)