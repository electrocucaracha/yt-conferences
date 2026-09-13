---
layout: default
title:
  "Project Lightning Talk: From Tokens To Partitions: Rethinking Data Distribution
  In... Daniel Blando"
nav_order: 217
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Daniel, a maintainer of Cortex, discusses the challenges faced in scaling
  Prometheus through Cortex, which aims to provide high availability, multi-tenancy,
  and long-term storage by splitting Prometheus into microservices. He focuses on
  the...
resource: https://www.youtube.com/watch?v=hlDqFMdXPQ8
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

Daniel, a maintainer of Cortex, discusses the challenges faced in scaling Prometheus through Cortex, which aims to provide high availability, multi-tenancy, and long-term storage by splitting Prometheus into microservices.
He focuses on the remote write path, explaining how data is distributed via a ring of tokens among microservices called distributors and ingesters, with each time series sharded to three ingesters for replication.
The current token-based approach leads to high downtime risk when two ingesters fail, especially at large scale, as the likelihood of a request failing approaches 100%.
To address this, Cortex is moving to a partition-based system where partitions, not ingesters, hold tokens, ensuring data for each partition is consistently sent to the same set of ingesters, significantly reducing downtime risk to around 10% with 15 partitions.
Daniel concludes by announcing the release of Cortex version 1, highlighting new features like support for Prometheus 3.0 and remote write v2, and invites further engagement with the community.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Daniel is a maintainer of Cortex.                                                                                                          |
|   2 | Cortex is a scalable version of Prometheus, focusing on high availability, multi-tenancy, and long-term storage.                           |
|   3 | Cortex splits Prometheus into multiple microservices for different request types.                                                          |
|   4 | The remote write path in Cortex uses two main microservices: distributor (acts as a proxy and shards data) and ingesters (handle storage). |
|   5 | Communication between distributor and ingesters is managed via a "ring" structure using tokens.                                            |
|   6 | Each ingester owns a part of the ring based on assigned tokens.                                                                            |
|   7 | When a request arrives, the distributor hashes the data and determines which ingester should receive it based on the ring.                 |
|   8 | Requests contain multiple time series, each sharded to three ingesters (replication factor of three).                                      |
|   9 | Success requires two out of three ingesters to confirm receipt.                                                                            |
|  10 | If two ingesters are down, the likelihood of a failed request is nearly 100% due to the token approach.                                    |
|  11 | With large clusters (e.g., 1,000 ingesters, 500 million time series), two ingesters down can cause total downtime.                         |
|  12 | To solve this, Cortex is introducing partitions: tokens are assigned to partitions, and ingesters join partitions.                         |
|  13 | Each partition consistently sends data to the same three ingesters, improving reliability.                                                 |
|  14 | With partitions, if two ingesters are down, only the affected partitions are impacted, reducing overall downtime.                          |
|  15 | In the partition approach, with 15 partitions, the chance of downtime drops to about 10%.                                                  |
|  16 | As the number of partitions and ingesters increases, the chance of downtime decreases further.                                             |
|  17 | Cortex version 1 is being released with new features.                                                                                      |
|  18 | Cortex now supports Prometheus 3.0 remote write v2 and spark format for faster queries and lower latency.                                  |
|  19 | Community engagement is encouraged, with channels available for contact and a kiosk at the pavilion.                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hlDqFMdXPQ8)
