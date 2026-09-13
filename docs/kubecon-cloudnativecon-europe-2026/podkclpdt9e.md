---
type: Video Note
title: "Project Lightning Talk: Run Your Data Layer In K8s With Vitess - Matt Lord, Maintainer"
description: "The speaker introduces themselves as a test maintainer at Planet Scale and discusses the challenges and solutions related to scaling MySQL databases, particularly in Kubernetes environments. They highlight Vitess, a CNCF project designed to..."
resource: https://www.youtube.com/watch?v=podkclpdT9E
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces themselves as a test maintainer at Planet Scale and discusses the challenges and solutions related to scaling MySQL databases, particularly in Kubernetes environments.
They highlight Vitess, a CNCF project designed to help scale MySQL from a single instance to hundreds or thousands of nodes while maintaining the appearance of a single database to users.
Key features of Vitess include compatibility, sharding, materializations for data locality, cluster management, online schema changes, backup and recovery, load shedding, and query consolidation.
The speaker notes that many popular services already use Vitess indirectly and encourages the audience to consider using it directly.
They emphasize the importance of automated recovery, mentioning VTORC for orchestration and the operator for infrastructure management in Kubernetes, and conclude by demonstrating how easily a Vitess cluster can be installed and managed.
# Main Points

|   # | Main point                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter is a test maintainer at Planet Scale.                                                                        |
|   2 | Presentation focuses on Vitess and its use with MySQL databases.                                                       |
|   3 | Audience includes users currently or previously using MySQL.                                                           |
|   4 | Vitess is a CNCF project designed to help scale MySQL.                                                                 |
|   5 | Many organizations run everything in Kubernetes except their database, often using RDS outside the cluster.            |
|   6 | Vitess allows scaling from a single MySQL instance to hundreds or thousands of nodes.                                  |
|   7 | To users, Vitess presents as a single MySQL database instance.                                                         |
|   8 | Key features of Vitess:                                                                                                |
|   9 | MySQL compatibility for seamless user experience.                                                                      |
|  10 | Sharding and resharding of data.                                                                                       |
|  11 | Materializations to regain data locality.                                                                              |
|  12 | Advanced cluster management.                                                                                           |
|  13 | Online schema changes coordinated across nodes.                                                                        |
|  14 | Backup and recovery capabilities.                                                                                      |
|  15 | Load shedding and back pressure handling.                                                                              |
|  16 | Query consolidation to optimize hot row access.                                                                        |
|  17 | Vitess is used indirectly by many popular services (Slack, GitHub PRs, Square terminals, Shopify, Uber).               |
|  18 | Automated recovery is a major benefit when scaling data layers.                                                        |
|  19 | Two main components for automated recovery:                                                                            |
|  20 | VTORC (orchestration component) monitors and maintains cluster health.                                                 |
|  21 | Operator manages infrastructure in Kubernetes.                                                                         |
|  22 | Vitess is designed for graceful failover and degradation, resulting in higher latency instead of errors during issues. |
|  23 | Vitess enables scaling data layers without needing to scale data teams.                                                |
|  24 | Example provided for installing the Vitess operator and setting up a cluster using the Vitess repo.                    |
|  25 | Presenter encourages attendees to visit the booth for follow-up questions.                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=podkclpdT9E)