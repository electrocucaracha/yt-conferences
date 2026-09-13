---
type: Video Note
title: "Project Lightning Talk: Making Kubescape Storage Scale From Small and Mid-Size To... Ben Hirschberg"
description: "Ben, CTO and co-founder of Armo and a maintainer of the CNCF project Cubescape, discusses the challenges faced in scaling Cubescape, a Kubernetes security platform that scans for vulnerabilities and configuration issues, generates network p..."
resource: https://www.youtube.com/watch?v=0SxXulvdMMs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Ben, CTO and co-founder of Armo and a maintainer of the CNCF project Cubescape, discusses the challenges faced in scaling Cubescape, a Kubernetes security platform that scans for vulnerabilities and configuration issues, generates network policies, and profiles applications.
As Cubescape produces large amounts of data, the team debated how best to expose this data—either through custom resources or an aggregated API server within Kubernetes.
They encountered significant difficulties with Kubernetes API features such as listing and watching large objects, patching complex nested objects, and handling unintended API usage by other tools, which led to performance issues and even cluster crashes at scale.
To address these, they limited list operations to metadata, restricted or deprecated the watch feature, avoided resource versioning, and restructured object patching by aggregating smaller subobjects, thereby improving scalability and stability.
Ben concludes by inviting attendees interested in Kubernetes security to connect with the Cubescape team at the event.
# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ben is CTO and co-founder of Armo and a maintainer of the Cubescape CNCF project.                                                                                             |
|   2 | Cubescape is a CNCF project in incubation, serving as a security platform for Kubernetes.                                                                                     |
|   3 | Cubescape scans for vulnerabilities, configuration issues, generates network policies, SECCOMP profiles, performs runtime threat detection, and creates application profiles. |
|   4 | The project produces large amounts of data and considered how users could access it: via a custom API server or as Kubernetes API objects.                                    |
|   5 | Chose to publish data as Kubernetes API objects, considering storage as CRDs or via an aggregated API server.                                                                 |
|   6 | Aggregated API server allows creating a custom API server within the Kubernetes cluster, integrating with Kubernetes tools.                                                   |
|   7 | Faced scaling challenges with large clusters and huge data objects (e.g., 100MB SBOMs).                                                                                       |
|   8 | Listing large objects in Kubernetes API was problematic; original API concepts were not designed for such large data.                                                         |
|   9 | The "watch" feature in Kubernetes API was difficult to support for large, infrequently changing objects, and not always needed for security use cases.                        |
|  10 | Patching complex, deeply nested, or large objects was challenging and hard to implement efficiently.                                                                          |
|  11 | Unintentional users (e.g., Argo CD, resource quota manager) made unexpected API requests, causing issues and even crashing clusters at scale.                                 |
|  12 | To address these, Cubescape aligned APIs to their use cases:                                                                                                                  |
|  13 | Listing now returns only metadata, not full objects; full objects require specific requests.                                                                                  |
|  14 | The "watch" feature is very limited and will eventually be deprecated.                                                                                                        |
|  15 | Resource versioning is no longer supported.                                                                                                                                   |
|  16 | Custom object logic replaces patching; objects are built from smaller subobjects to avoid complex patching.                                                                   |
|  17 | Implemented request queuing to prevent blocking and issues from other components.                                                                                             |
|  18 | Invited attendees to visit the project pavilion and connect with the team.                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0SxXulvdMMs)