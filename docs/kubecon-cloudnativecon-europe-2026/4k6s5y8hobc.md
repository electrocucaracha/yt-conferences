---
type: Video Note
title: "Evolution or Revolution: Istio as the Network Platform for Cloud Nat... Mitch Connors & Daniel Grimm"
description: "In this STO maintainer track talk, presenters Mitch Connors and Daniel provide an overview of the evolution of the ISTIO project, discussing whether recent changes represent an evolution or a revolution. They recount ISTIO’s history from it..."
resource: https://www.youtube.com/watch?v=4K6s5y8HoBc
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this STO maintainer track talk, presenters Mitch Connors and Daniel provide an overview of the evolution of the ISTIO project, discussing whether recent changes represent an evolution or a revolution.
They recount ISTIO’s history from its 2017 launch, highlighting key milestones such as the move from multiple microservices to a monolithic control plane (ISTIOD), the introduction of canary-based upgrades, and the addition of new proxy implementations like Ztunnel for improved resource utilization and upgrade processes.
The talk covers recent developments, including support for Gateway API inference extensions to better handle large language model workloads, efforts to simplify ingress-only installations, and the growing use of Ztunnel outside ISTIO by projects like Calico and Cilium.
They also detail improvements in multicluster networking, achieving both scalability and end-to-end security through double MTLS tunneling, and announce integration with the Agent Gateway project for agentic networking use cases.
The presenters emphasize the project’s ongoing health, steady contributor engagement, and the increasing impact of power user contributors, inviting more community involvement to address emerging needs and challenges.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk discusses whether changes in the ISTIO project are evolutionary or revolutionary.                                                           |
|   2 | Audience split: about half are new to ISTIO, half want updates on the latest features.                                                               |
|   3 | Presenters: Mitch Connors (Microsoft, ISTIO maintainer since 2018/19) and Daniel (Red Hat, ISTIO since 2019).                                        |
|   4 | Agenda: project history, current health, recent updates, and a 101-level overview.                                                                   |
|   5 | ISTIO 0.1 launched in 2017; original architecture included components like Mixer and Pilot.                                                          |
|   6 | Early goal: decouple routing config from proxy implementation, not just be a control plane for Envoy.                                                |
|   7 | 1.0 release expanded microservices and moved to CRDs (37 in 1.0), added multicluster support.                                                        |
|   8 | Feedback led to consolidating components into ISTIOD (monolithic control plane) for easier upgrades and canary-based rollouts.                       |
|   9 | In 2022, introduced Ztunnel (L4 proxy per node) for MTLS and security, and Waypoint Gateway for L7 features, enabling upgrades without pod restarts. |
|  10 | Project health: sustained high contributor numbers (100+ monthly), 30+ new contributors/month, consistent quarterly releases since 1.2.              |
|  11 | Recent features: Gateway API inference extension for LLM workloads, supporting advanced routing and caching needs.                                   |
|  12 | Lightweight ingress-focused ISTIOD installation profile in development for easier adoption.                                                          |
|  13 | Over 50% of ISTIO users use it only for ingress.                                                                                                     |
|  14 | Ztunnel is being adopted by other projects (e.g., Calico, Cilium) and is easier to maintain/configure.                                               |
|  15 | Multicluster: ambient mode avoids per-pod data sharing, uses east-west gateways with double MTLS tunnels for scalability and security.               |
|  16 | Agent Gateway integration (third proxy) for agentic/LLM workloads, with alpha release in 1.30.                                                       |
|  17 | Power user contributors (end users) are increasingly submitting design docs and PRs.                                                                 |
|  18 | Flat networking can avoid extra hops in multicluster but has scalability/IP limitations.                                                             |
|  19 | East-west gateways are currently the scalable solution for multicluster MTLS.                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4K6s5y8HoBc)