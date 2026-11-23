---
layout: default
title: "Hosting Active: Active workloads in OpenStack when a single LB is not enough"
nav_order: 27
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Daniel from CERN presents a lightning talk on hosting active-active workloads in OpenStack, addressing the limitations of single load balancer instances for high-availability and disaster recovery ..."
resource: "https://www.youtube.com/watch?v=ZUFmosevdfk"
youtube_stats:
  view_count: 224
  like_count: 4
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

Daniel from CERN presents a lightning talk on hosting active-active workloads in OpenStack, addressing the limitations of single load balancer instances for high-availability and disaster recovery needs.
He outlines several existing solutions, including DNS round-robin for basic distribution, application-level redirection for offloading heavy bandwidth, and Octavia with OVN for distributed east-west traffic, while noting that north-south traffic often remains bottlenecked at gateway nodes.
The core of the presentation focuses on implementing active-active load balancing with a single IP address using BGP Equal-Cost Multi-Path (ECMP), where the cloud provider manages BGP sessions via route reflectors to scale effectively and maintain control over traffic distribution.
Although these BGP-based proposals offer significant benefits for high availability and multi-data center scenarios, they introduce management complexity and are currently only in the specification or testing phase rather than production use due to API stability concerns.
The talk concludes by emphasizing the need to balance technical capability with maintainability and user requirements when selecting the appropriate load balancing strategy.

# Main Points

|   # | Main point                                                                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker from CERN presents a lightning talk on hosting active-active workloads in OpenStack to address limitations of single load balancers.                                                            |
|   2 | CERN operates 450 load balancers, primarily using the Amphora driver, alongside DNS and Kubernetes-based solutions for specific user needs.                                                                 |
|   3 | Key motivations for multi-active setups include supporting mirror storage and streaming services, distributing DDoS absorption, and enabling business continuity across multiple data centers.              |
|   4 | The presentation highlights three main goals: achieving multi-instance traffic handling, enabling geo-local routing to stay within the same data center, and maintaining high availability with monitoring. |
|   5 | DNS round-robin is identified as a trivial active-active solution but lacks health monitoring and client control, with some top-level domains restricting multiple IPs.                                     |
|   6 | Intelligent DNS with GeoDNS allows local transmission based on location but still lacks full client-side control over load balancing decisions.                                                             |
|   7 | Application-level load balancing, such as using HTTP 303 redirects, can offload heavy bandwidth workloads to other servers but significantly increases latency.                                             |
|   8 | Octavia with the Amphora driver supports active-standby configurations with health monitoring but remains limited to a single traffic path.                                                                 |
|   9 | Using OVN as a load balancer via Octavia distributes east-west traffic across hypervisors using source IP and port hashing.                                                                                 |
|  10 | OVN-based load balancing fails to distribute north-south traffic effectively because external clients always terminate at a single gateway node or virtual router.                                          |
|  11 | BGP Equal-Cost Multi-Path (ECMP) allows forwarding traffic over multiple links using hash-based routing but requires users to manage router control planes.                                                 |
|  12 | Octavia proposals suggest cloud providers control BGP sessions to manage active-active routing, though this approach does not scale well with thousands of load balancers.                                  |
|  13 | Route reflectors can be used as intermediate hosts to aggregate BGP information, simplifying BFD monitoring and allowing admins to control traffic draining and allocation.                                 |
|  14 | The route reflector approach adds management complexity and requires handling BGP session termination and route removal when instances fail.                                                                |
|  15 | A potential future improvement involves extending OVN to support bidirectional multi-chassis routing for north-south traffic, though current OVN load balancing is limited to Layer 4.                      |
|  16 | The speaker notes that these BGP-based solutions are currently in test setups and not yet in production due to API change risks and migration path concerns.                                                |
|  17 | Takeaways emphasize combining existing tools based on user needs while avoiding over-complication to ensure maintainability.                                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZUFmosevdfk/hqdefault.jpg)](https://www.youtube.com/watch?v=ZUFmosevdfk)

[Watch on YouTube](https://www.youtube.com/watch?v=ZUFmosevdfk)
