---
layout: default
title: "Ceph: Open Storage for VMs, Containers, and the Future Cloud"
nav_order: 23
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Dan Vandersteer from the Ceph Foundation presented at the Open Infrastructure Summit, highlighting Ceph’s evolution as a unified, general-purpose storage solution that supports object, block, and f..."
resource: "https://www.youtube.com/watch?v=9kR3mrFZg6U"
youtube_stats:
  view_count: 277
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

Dan Vandersteer from the Ceph Foundation presented at the Open Infrastructure Summit, highlighting Ceph’s evolution as a unified, general-purpose storage solution that supports object, block, and file protocols.
He noted that while public telemetry reports two exabytes of usage, the actual installed base is likely significantly higher, representing only a small fraction of the total global storage infrastructure and indicating a massive opportunity for growth.
A key focus of the talk was the recent completion of the "Ceph Tentacle" release, which introduces optimized erasure coding performance to address historical inefficiencies where reading small data segments required accessing entire stripes across multiple disks.
By collaborating with IBM to re-optimize these processes, the new version allows users to enable fast erasure coding on existing pools, doubling the sustainable IOPS capacity from approximately 40,000 to over 80,000 before latency increases.
Vandersteer concluded by encouraging community participation and promoting the upcoming CephCon event in Vancouver, emphasizing that the project is still in its early stages of capturing the broader market.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dan Vandersteer from the Ceph Foundation presented at the Open Infrastructure Summit.                                             |
|   2 | Ceph and OpenStack grew together and drove open infrastructure in the 2010s.                                                      |
|   3 | Ceph is classified as unified storage, offering general-purpose object, block, and file solutions.                                |
|   4 | Public telemetry shows two exabytes of Ceph usage, with estimates suggesting the real number could be between 20 and 50 exabytes. |
|   5 | The speaker highlighted a specific performance issue with erasure coding in block storage.                                        |
|   6 | Previous versions required reading entire stripes, including all disks, to access small data segments like 200 bytes.             |
|   7 | This inefficiency resulted in high IOPS and latency due to suboptimal read and write operations.                                  |
|   8 | The Ceph Tentacle version, expected to be version 20, introduces fast erasure coding optimizations.                               |
|   9 | These optimizations allow users to enable fast erasure coding on existing pools without data migration.                           |
|  10 | Performance tests show that the previous version hit a latency wall at approximately 40,000 IOPS.                                 |
|  11 | The new Tentacle version supports 80,000 to 100,000 IOPS before latency increases significantly.                                  |
|  12 | The project is financially supported by 16 to 17 different organizations.                                                         |
|  13 | CephCon is scheduled to take place in Vancouver the following week.                                                               |
|  14 | The speaker noted that current Ceph adoption represents a small fraction of total installed storage infrastructure.               |
|  15 | There is a significant opportunity for Ceph to make a larger impact in the storage market.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/9kR3mrFZg6U/hqdefault.jpg)](https://www.youtube.com/watch?v=9kR3mrFZg6U)

[Watch on YouTube](https://www.youtube.com/watch?v=9kR3mrFZg6U)
