---
type: Video Note
title: "Project Lightning Talk: Scaling Kubescape to Thousands of Nodes - Matthias Bertschy, Maintainer"
description: "Matias, a maintainer of Cubescape, shares the challenges faced when scaling their Kubernetes security platform to handle 5,000 nodes, each sending large data objects. Initially, their naive approach of having each node agent send full CRDs..."
resource: https://www.youtube.com/watch?v=abVrry6PQdQ
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Matias, a maintainer of Cubescape, shares the challenges faced when scaling their Kubernetes security platform to handle 5,000 nodes, each sending large data objects.
Initially, their naive approach of having each node agent send full CRDs every 10 minutes led to severe lock contention and inefficiency due to simultaneous updates.
Switching to the patch method also failed, as synchronous processing and mutexes could not keep up with the volume and size of data.
Their current solution involves each node agent sending unique CRDs as time series data, allowing the API server to quickly acknowledge and store data, with aggregation handled asynchronously, greatly improving scalability.
Matias concludes by inviting attendees to discuss further ideas at the conference.
# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Matias is a maintainer of Cubescape.                                                                                                                                                          |
|   2 | Faced issues deploying Cubescape to a large cluster with 5,000 nodes, each sending 10MB objects per container periodically.                                                                   |
|   3 | Encountered a "thundering herd" problem due to massive simultaneous data updates.                                                                                                             |
|   4 | Lock contentions from thousands of nodes made traditional Kubernetes storage patterns obsolete.                                                                                               |
|   5 | Cubescape is a CNCF security platform for Kubernetes, providing continuous scanning, deep eBPF runtime observability, and runtime detection using the CL language.                            |
|   6 | Generates large amounts of data stored as container profiles, each profile being tens of megabytes.                                                                                           |
|   7 | Thousands of nodes continuously updating data caused problems with API server logic.                                                                                                          |
|   8 | Could not use etcd for storage due to large object sizes.                                                                                                                                     |
|   9 | Implemented an aggregated API server; node agents send learned profiles to this storage.                                                                                                      |
|  10 | Initial approach: each node agent kept the entire CRD in memory and sent the full object every 10 minutes using the create method—resulted in lock contention and excessive traffic.          |
|  11 | Second approach: used the patch method, where node agents sent JSON patches to the API server—still synchronous and failed due to timeouts and mutex issues.                                  |
|  12 | Current approach: node agents send a unique CRD for each period, treated as a time series; API server saves immediately and acknowledges, with asynchronous aggregation and processing later. |
|  13 | Decoupled write path enabled much better scalability.                                                                                                                                         |
|  14 | Future plan: storage could coordinate to reduce redundant data learning by selecting a subset of learners.                                                                                    |
|  15 | Matias is available at the Cubescape kiosk and Armo booth for further discussion.                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=abVrry6PQdQ)