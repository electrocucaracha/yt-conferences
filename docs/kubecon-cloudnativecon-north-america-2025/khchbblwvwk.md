---
layout: default
title:
  "On-Prem Load Balancing Reimagined: Serving 20 Million QPS With Gateway API
  and Envoy... Isaac Wilson"
nav_order: 186
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Isaac Wilson, an engineer at The Trade Desk, discussed the company’s
  migration from an on-premises HAProxy-based load balancing architecture to Kubernetes
  Gateway API with Envoy Gateway. He outlined the limitations of their previous setup...
resource: https://www.youtube.com/watch?v=kHChbblwVwk
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Isaac Wilson, an engineer at The Trade Desk, discussed the company’s migration from an on-premises HAProxy-based load balancing architecture to Kubernetes Gateway API with Envoy Gateway.
He outlined the limitations of their previous setup, including slow rollouts, complex configuration management, limited scalability, and inefficient CPU utilization.
The migration to Envoy Gateway, chosen for its advanced feature set and flexibility, enabled improved traffic distribution through zone-aware routing, simplified onboarding of new services, and significant compute cost savings—over $4 million—by reclaiming underutilized resources.
Wilson emphasized the importance of anticipating failures, benchmarking at production scale, gradual rollouts, and involving multiple teams in such migrations.
He also shared technical lessons learned, such as handling protocol defaults and tuning for high-traffic environments, and described how the new architecture unified their approach across data centers and cloud providers, making it easier for application teams to manage their own traffic routing.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Isaac Wilson, engineer at The Trade Desk, presented on migrating load balancing from on-prem to Kubernetes Gateway API.                                                            |
|   2 | Provided history of Kubernetes adoption at The Trade Desk, starting in 2020, now running 40-50 clusters globally.                                                                  |
|   3 | Old architecture used HAProxy with Consul for service discovery, routing only to local rack backends for performance.                                                              |
|   4 | Challenges with old setup: slow rollouts, strict workload balancing, complex configuration, difficult changes, limited onboarding of new services, and HAProxy thread limitations. |
|   5 | Migration goals: improve rollout speed, simplify configuration, enable easier onboarding, and better utilize hardware.                                                             |
|   6 | Chose Kubernetes Gateway API for advanced controls, role-oriented design, and easier migration between controllers.                                                                |
|   7 | Selected Envoy Gateway for its feature set, low complexity, and ability to patch raw Envoy configuration.                                                                          |
|   8 | Migration strategy: anticipate failure, have rollback plans, understand default behaviors, benchmark at production scale, avoid full cutovers, and involve multiple teams early.   |
|   9 | Noted issues encountered: ALPN default changes affecting HTTP/2 connections, AWS TCP established timeout differences.                                                              |
|  10 | Outcomes: improved traffic distribution with zone-aware routing, better tail latency, improved resource utilization, and significant compute savings (over $4 million).            |
|  11 | Enabled self-service onboarding for new services and easier refactoring to microservices.                                                                                          |
|  12 | Achieved unified architecture across all providers, simplifying experience for application teams.                                                                                  |
|  13 | Migration involved scaling down HAProxy nodes, converting them to Kubernetes nodes, and running Envoy on them.                                                                     |
|  14 | Chose Envoy Gateway over CNI-based gateways for more granular configuration options.                                                                                               |
|  15 | Started implementing Wasm filters for edge traffic shedding; exploring advanced load balancing algorithms like ORCA.                                                               |
|  16 | Envoy proxy sizing: largest nodes have 192 cores, handling ~30k connections/sec, with average response time under 5ms.                                                             |
|  17 | Overprovisi                                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kHChbblwVwk)
