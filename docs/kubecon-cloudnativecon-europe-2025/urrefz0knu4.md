---
type: Video Note
title: "Consistent Volume Group Snapshots, Unraveling the Magic - Leonardo Cecchi, EDB & Xing Yang"
description: "Shining, a principal software engineer at EDB, introduces the concept of volume group snapshots in Kubernetes, which allows for consistent and efficient data protection across multiple volumes. The feature enables users to take a snapshot o..."
resource: https://www.youtube.com/watch?v=urRefZ0KnU4
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Shining, a principal software engineer at EDB, introduces the concept of volume group snapshots in Kubernetes, which allows for consistent and efficient data protection across multiple volumes.
The feature enables users to take a snapshot of all volumes at the same point in time, ensuring that data is restored consistently even if individual volumes are corrupted or lost.
Shining explains how dynamic provisioning and pre-provisioning workflows work with volume group snapshots, highlighting the importance of collaboration between software components for successful implementation.
The feature is currently in beta and aims to be released as a general availability (GA) release in the future.
# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Consistent group snapshot allows taking a snapshot from multiple volumes at the same point in time to ensure right order consistency. |
|   2 | Volume group snapshot feature supports crash consistency and is more efficient than taking one snapshot at a time.                    |
|   3 | The feature introduces three new APIs: volume group snapshot class, volume group snapshot, and volume group snapshot content.         |
|   4 | Dynamic provisioning allows creating a volume group snapshot object with minimal admin effort.                                        |
|   5 | Pre-provisioning requires creating all objects manually.                                                                              |
|   6 | Restore is easy to do using the same process as plain volume snapshots.                                                               |
|   7 | Feature gates are used to enable or disable the feature in beta releases.                                                             |
|   8 | The feature is still in beta and needs implementation from more storage vendors and integration for more Kubernetes applications.     |
|   9 | The demo showed how to use the feature with PostgreSQL, including backing up a database and restoring it quickly.                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=urRefZ0KnU4)