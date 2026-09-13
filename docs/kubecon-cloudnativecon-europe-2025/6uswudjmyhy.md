---
layout: default
title:
  "What's New in Knative Eventing: Security, Discovery, Int... Pierangelo Di
  Pilato & Christoph Stäbler"
nav_order: 369
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The presentation discusses various features and updates in KNative Eventing,
  an open-source project for building event-driven systems. The security features
  include transport encryption via TLS, authentication via OpenID Connect, and author...
resource: https://www.youtube.com/watch?v=6usWUdJMyHY
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The presentation discusses various features and updates in KNative Eventing, an open-source project for building event-driven systems.
The security features include transport encryption via TLS, authentication via OpenID Connect, and authorization via event policies.
These features aim to provide secure event delivery and restrict access to resources.
Additionally, the presentation introduces integration sources and sync, which enable native support for third-party services like AWS SQS.
Event discovery is also discussed, including an API that provides a reference to a resource emitting a particular type of event, along with attributes.
The event transform feature allows declarative transformations of events in JSON expression language.
Finally, the presentation touches on job sync, which enables offloading long-running processing in the background, and multi-tenancy support is discussed as a future plan.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kative Eventing provides three new key security features: transport encryption via TLS, authentication via OpenID Connect, and authorization via event policies. |
|   2 | Transport encryption is enabled through HTTPS endpoints, which can be configured to strict or permissive modes.                                                  |
|   3 | Authentication is done using OpenID Connect, which generates an ODC token for the service account and audience.                                                  |
|   4 | Authorization is implemented using event policies, which specify who can send events to resources.                                                               |
|   5 | Event policies have three main fields: spec.2 (resources protected), spec.from (allowed senders), and filters (optional).                                        |
|   6 | Job sync allows long-running processing in the background by creating a job for each event.                                                                      |
|   7 | Event transform enables declarative transformations of events using a JSON expression language.                                                                  |
|   8 | The broker supports multi-tenancy through shared implementations, but not proper segregation.                                                                    |
|   9 | There is no support for client certificate-based authentication with HTTPS encryption.                                                                           |
|  10 | Label-based authorization (e.g., network policies) is not supported.                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6usWUdJMyHY)
