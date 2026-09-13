---
layout: default
title:
  How We Moved Spotify To a Proxyless gRPC Service Mesh - Erik Lindblad & Erica
  Manno, Spotify
nav_order: 123
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Spotify's service discovery system, Nameless, was facing limitations
  with DNS, including response size limits and uncertainty in service registration
  times. To address these issues, Spotify evaluated market-leading service mesh solutions
  an...
resource: https://www.youtube.com/watch?v=2_ECK6v_yXc
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

Spotify's service discovery system, Nameless, was facing limitations with DNS, including response size limits and uncertainty in service registration times.
To address these issues, Spotify evaluated market-leading service mesh solutions and ultimately decided to extend its existing infrastructure instead of adopting a new one.
The team implemented XDS (X Discovery Service), a universal data plane API that allows for proxyless gRPC services, enabling more efficient and scalable service discovery.
The rollout was gradual, with less critical services being targeted first, and included features like traffic splitting, zone-aware routing, and dependency graphs.
While there were challenges, including complexity and flaky bootstrapping logic, the XDS implementation has proven successful, delivering improved scalability and reliability for Spotify's service network.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2_ECK6v_yXc)
