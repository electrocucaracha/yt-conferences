---
type: Video Note
title: "Dancing With the Pods: Live Migration of a Database Fleet While Serving... Jayme Bird & Manish Gill"
description: 'The speaker discusses the migration of their company''s database from a traditional stateful set approach to a new "make before break" architecture using ClickHouse. This involves adding capacity in terms of extra replicas and then taking aw...'
resource: https://www.youtube.com/watch?v=ufY_JFPpzRI
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the migration of their company's database from a traditional stateful set approach to a new "make before break" architecture using ClickHouse.
This involves adding capacity in terms of extra replicas and then taking away the existing capacity, allowing for fast vertical scaling without downtime.
The migration was complex due to the need to maintain zero downtime, handle DNS issues, and preserve system tables that contain query history.
To address these challenges, the team implemented a custom migration controller using Temporal, which handled tasks such as syncing catalog metadata, creating new replicas, and managing zone balance.
The migration was successful, with thousands of customers migrated without downtime, and has improved the company's ability to scale and handle high traffic.
# Main Points

|   # | Main point                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------- |
|   1 | ClickHouse is an open-source column-oriented distributed database.                                          |
|   2 | Autoscaling in Kubernetes requires pod evictions, which can be slow and disruptive.                         |
|   3 | The "make before break" approach involves adding capacity before removing old replicas, reducing downtime.  |
|   4 | This approach was implemented using multiple stateful sets to manage different replicas.                    |
|   5 | A migration controller was created to handle the transition from one stateful set to another.               |
|   6 | Challenges included zone balancing, DNS issues, and losing system tables during the migration process.      |
|   7 | Solutions included zone pinning, DNS resolution fixes, and a new disk type for storing system tables on S3. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ufY_JFPpzRI)