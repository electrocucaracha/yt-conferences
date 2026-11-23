---
layout: default
title: "Who framed RabbitMQ?"
nav_order: 8
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "OVH Cloud engineers presented a detailed case study on resolving severe RabbitMQ instability in their large-scale OpenStack production environments, which were suffering from RPC timeouts, network ..."
resource: "https://www.youtube.com/watch?v=Uj4elX2OONw"
youtube_stats:
  view_count: 567
  like_count: 16
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

OVH Cloud engineers presented a detailed case study on resolving severe RabbitMQ instability in their large-scale OpenStack production environments, which were suffering from RPC timeouts, network partitions, and excessive queue churn.
The team identified that OpenStack’s Oslo messaging library was misusing RabbitMQ by creating an unsustainable number of queues for fan-out messages, particularly due to Neutron agents, rather than leveraging the broker’s strength in high-volume message throughput.
To address this, they implemented a multi-faceted strategy including upgrading RabbitMQ to version 4.1, switching Apache MPM to the event backend, and fixing race conditions in the PikaMQP library to improve heartbeat reliability.
A critical architectural shift involved migrating from classic HA queues to Quorum Queues and, most significantly, adopting Stream Queues for fan-out topics, which reduced the total queue count by more than half and improved stability.
Although this migration required a complete service shutdown and queue recreation, the result was a more resilient system that aligns with RabbitMQ’s intended design, demonstrating that the root cause of the issues lay in OpenStack’s consumption patterns rather than the broker itself.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OVH Cloud operates large-scale OpenStack regions with over 2,000 compute nodes, facing RabbitMQ stability issues.                                                    |
|   2 | Initial symptoms included RPC timeouts, missed heartbeats, network partitions, and unresponsive clusters requiring full restarts.                                    |
|   3 | Troubleshooting involved improving observability with Prometheus, Grafana, Oslo Metrics, and enhanced logging with unique message IDs.                               |
|   4 | Analysis revealed Neutron agents generated excessive fan-out messages and queues, creating significant load on the broker.                                           |
|   5 | The team identified that OpenStack uses RabbitMQ as a queue broker rather than a message broker, contrary to best practices.                                         |
|   6 | Upgrading RabbitMQ from version 3.8 to 4.1 improved stability and resolved known bugs.                                                                               |
|   7 | Switching the Apache MPM backend from worker to event reduced missed heartbeat errors.                                                                               |
|   8 | Refactoring Oslo Messaging to use native Python threads instead of greenlets improved heartbeat reliability.                                                         |
|   9 | A race condition in the PikaMQ library that prevented correct heartbeat timing was fixed.                                                                            |
|  10 | The team migrated from classic HA queues to Quorum Queues to ensure node-lossless high availability.                                                                 |
|  11 | Introducing a queue manager mechanism in Oslo Messaging allowed predictable queue names, preventing queue churn during agent restarts.                               |
|  12 | Stream Queues were adopted for fan-out topics to share a single queue among multiple consumers, reducing total queue count by more than half.                        |
|  13 | Stream Queues require client-side offset tracking for acknowledgments and policies to limit maximum size and age to prevent disk exhaustion.                         |
|  14 | Multiplexing RPC servers onto shared connections further reduced the number of active TCP connections.                                                               |
|  15 | Migrating to Quorum and Stream Queues requires a full OpenStack service shutdown and queue deletion, resulting in approximately one hour of downtime.                |
|  16 | The community advised against testing RabbitMQ 4's new Capri metadata backend due to ongoing instability.                                                            |
|  17 | Key lessons include staying up-to-date with RabbitMQ versions, fixing OpenStack messaging patterns to reduce queue creation, and engaging with upstream communities. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Uj4elX2OONw/hqdefault.jpg)](https://www.youtube.com/watch?v=Uj4elX2OONw)

[Watch on YouTube](https://www.youtube.com/watch?v=Uj4elX2OONw)
