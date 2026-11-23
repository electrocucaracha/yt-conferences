---
layout: default
title: Optimizing the volume restore flow in Cinder using queues
nav_order: 97
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker, representing the largest cloud provider in Southeast Asia, presents a solution to optimize backup restore performance in OpenStack Cinder, noting that restore times were significantly ..."
resource: "https://www.youtube.com/watch?v=_plljSVk21s"
youtube_stats:
  view_count: 66
  like_count: 2
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

The speaker, representing the largest cloud provider in Southeast Asia, presents a solution to optimize backup restore performance in OpenStack Cinder, noting that restore times were significantly slower than backup times despite similar throughput.
The core issue was identified as sequential chunk reading and writing, which caused high latency; the proposed fix involves implementing a queue-based parallel read and write mechanism using the Light library to decouple these operations.
While this approach significantly reduced restore times, it introduced challenges such as error handling issues where failures were masked as successes and failures when using very large chunk sizes.
The speaker also discusses the operational impact of these optimizations, acknowledging that parallel backups can create I/O peaks that temporarily degrade performance for active virtual machines, a common challenge in shared storage environments.
Future work includes applying this method to incremental backups and contributing the code to the upstream Cinder project, while the session concludes with informal discussions about the speaker’s background in Vietnam and the audience member’s experience with OpenStack in Germany.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker works for the largest cloud provider in Southeast Asia, managing over 15 OpenStack clusters with 42 PB of storage.                          |
|   2 | The primary motivation for the project was that backup times were faster than restore times, despite similar traffic throughput.                        |
|   3 | Initial analysis showed that increasing the batch size reduced restore time, but larger sizes caused errors due to backend limitations.                 |
|   4 | The original restore flow was sequential, reading chunks from backup and writing to the volume one by one, which caused slow performance.               |
|   5 | The proposed solution involves enabling parallel read and write operations using a queue between the backup and volume restore processes.               |
|   6 | A custom function was implemented to handle chunk data in the queue, allowing simultaneous reading from backup and writing to the volume.               |
|   7 | The queue implementation required extending the OF brick with offset-based read and write support to accommodate the new parallel workflow.             |
|   8 | One challenge was that the queue library did not propagate errors to the outside, requiring custom exception handling to ensure failures were reported. |
|   9 | Another issue was that using very large chunk sizes caused failures during the restore process.                                                         |
|  10 | The optimization significantly reduced restore time, although it created I/O peaks that could impact other workloads on the storage cluster.            |
|  11 | The same code path is used for both backup and restore operations, meaning the optimization applies to both processes.                                  |
|  12 | The speaker plans to apply this method to incremental backups in future work.                                                                           |
|  13 | The speaker intends to contribute this idea to the Cinder project in the future.                                                                        |
|  14 | The speaker is from Vietnam and works in Hanoi, providing cloud services to various companies and government entities.                                  |
|  15 | The speaker is planning to pursue a master's degree in computer science at a university in Germany.                                                     |
|  16 | The audience member is from Germany, works in cloud computing for a hospital, and is interested in the technical details of the optimization.           |
|  17 | Both speakers discussed the challenges of managing I/O peaks during backup operations to avoid impacting active VM workloads.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_plljSVk21s/hqdefault.jpg)](https://www.youtube.com/watch?v=_plljSVk21s)

[Watch on YouTube](https://www.youtube.com/watch?v=_plljSVk21s)
