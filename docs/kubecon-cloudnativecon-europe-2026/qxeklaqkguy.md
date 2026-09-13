---
type: Video Note
title: "What Happens in Kubernetes SIG Scalability: Intro + DeepDive - Wojciech Tyczyński, Google"
description: "Voytech Tachinski, a technical lead for the Kubernetes SIG Scalability, outlines the group's main areas of focus, which include defining and measuring Kubernetes scalability, monitoring for regressions, implementing improvements, and collab..."
resource: https://www.youtube.com/watch?v=QxeklaQkgUY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Voytech Tachinski, a technical lead for the Kubernetes SIG Scalability, outlines the group's main areas of focus, which include defining and measuring Kubernetes scalability, monitoring for regressions, implementing improvements, and collaborating with the community to promote best practices.
He explains that scalability in Kubernetes is a complex, multi-dimensional problem, not limited to cluster size but encompassing factors like node count, pod churn, and resource types.
The SIG uses tools like ClusterLoader and PerfDash for rigorous scalability testing across major cloud providers, emphasizing the importance of real-world cluster validation and encouraging feature owners to contribute tests.
Recent improvements discussed include the watch list feature to reduce memory usage, serving consistent list requests from cache to lower load on etcd, mechanisms to prevent controllers from acting on stale data, opportunistic batching in the scheduler for faster pod placement, and ongoing work to better handle large resource objects.
Tachinski concludes by inviting community participation to help advance scalability efforts.
# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Scalability focuses on five main themes:                                                                                                                                     |
|   2 | Defining Kubernetes scalability and its goals                                                                                                                                    |
|   3 | Monitoring and measuring system performance and scalability                                                                                                                      |
|   4 | Preserving and monitoring for regressions in scalability                                                                                                                         |
|   5 | Making actual scalability improvements                                                                                                                                           |
|   6 | Working with the community on best practices for scalable features                                                                                                               |
|   7 | Scalability should be driven by real user requirements, not optimization for its own sake                                                                                        |
|   8 | Kubernetes scalability is multi-dimensional (nodes, pods, churn, gateways, secrets, etc.)                                                                                        |
|   9 | The "scalability envelope" defines the zone where all scalability SLOs are satisfied                                                                                             |
|  10 | Main SLOs tracked: API call latency and pod startup time                                                                                                                         |
|  11 | SLO definitions are being refined for precision and broader coverage                                                                                                             |
|  12 | Scalability envelope is hard to define precisely due to many interdependent dimensions                                                                                           |
|  13 | Scalability testing is critical; main tool is Cluster Loader (semi-declarative, measures SLOs, integrates with Grafana/Prometheus, uses PerfDash for tracking metrics over time) |
|  14 | Release-blocking scalability tests run on real clusters across AWS, GCP, and Azure                                                                                               |
|  15 | Real cluster testing is necessary; simulated clusters can miss issues                                                                                                            |
|  16 | Running tests on multiple providers helps catch provider-specific regressions                                                                                                    |
|  17 | Feature owners are encouraged to create or adjust scalability tests for their features                                                                                           |
|  18 | Two main categories of recent improvements:                                                                                                                                      |
|  19 | Pushing limits in a single dimension (e.g., more nodes or pods)                                                                                                                  |
|  20 | Increasing reliability at scale (e.g., supporting higher churn at a given scale)                                                                                                 |
|  21 | Key improvements:                                                                                                                                                                |
|  22 | Watch list feature: replaces large list requests with chunked watch requests, reducing API server memory spikes                                                                  |
|  23 | Streaming serialization for list requests: serializes and sends items individually, reducing memory usage                                                                        |
|  24 | Snapshot-able API server: serves consistent list requests from cache, reducing etcd load and improving memory predictability                                                     |
|  25 | Stale controller handling: ensures controllers operate on fresh enough state,                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QxeklaQkgUY)