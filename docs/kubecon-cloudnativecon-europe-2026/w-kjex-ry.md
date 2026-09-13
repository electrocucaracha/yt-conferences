---
type: Video Note
title: "Moving Spotify’s Infrastructure Management Up the Stack from Kubebu... Alexander Buck & Tomas Aschan"
description: "In this talk, Thomas and Alex from Spotify discuss their efforts to simplify and improve infrastructure management for both feature and platform teams by developing internal tools such as Declarative Infra, Crow (Cube Resource Orchestrator)..."
resource: https://www.youtube.com/watch?v=W-_kJEX-_RY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Thomas and Alex from Spotify discuss their efforts to simplify and improve infrastructure management for both feature and platform teams by developing internal tools such as Declarative Infra, Crow (Cube Resource Orchestrator), and K-pop (Kubernetes Protobuff Operator).
They explain the challenges faced when managing complex cloud resources and reducing data duplication, using examples like Bigtable and Apache Iceberg integrations.
While previous solutions like custom operators improved the experience for feature teams, they imposed a steep learning curve and maintenance burden on platform developers.
To address this, Spotify introduced Crow for composing and abstracting resources and K-pop for building operators with minimal Kubernetes-specific knowledge, allowing platform teams to focus on business logic.
These tools have significantly improved developer experience and adoption within Spotify, though challenges remain around scaling, observability, and versioning.
The session concludes with a Q&A covering technical details, comparisons to tools like Helm and Crossplane, and future ambitions for open sourcing and further platform improvements.
# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Spotify is moving infrastructure management up the stack with an internal resource management platform called declarative infra.                                      |
|   2 | Declarative infra allows feature teams to configure infrastructure as code in source repositories, turning configuration into cloud resources.                        |
|   3 | The platform serves both feature teams (building Spotify products) and platform teams (building internal developer tools).                                            |
|   4 | Goal: provide a single configuration surface for all infrastructure needs, supporting both off-the-shelf and internal products.                                       |
|   5 | Spotify recently reached the milestone of managing 1 million resources internally.                                                                                    |
|   6 | Data duplication issue: 28% of BigQuery data is duplicated from GCS due to batch processing and SQL use cases.                                                        |
|   7 | Solution: Use Apache Iceberg and Google BigLake to allow BigQuery to query data in GCS, reducing duplication.                                                         |
|   8 | Setting up these solutions requires complex, error-prone YAML configurations and internal API calls.                                                                  |
|   9 | Previous internal solution for Bigtable involved building custom operators and a composition operator ("Spotify Bigtable") to abstract complexity for feature teams.  |
|  10 | While successful for feature teams, building and maintaining these operators was difficult and time-consuming for platform developers.                                |
|  11 | Two main resource types: abstractions/compositions (packaging resources with custom schema) and resources exposing cloud APIs (sometimes requiring custom operators). |
|  12 | Crow (Cube Resource Orchestrator) is used for abstractions/compositions, letting platform developers define resource graphs without deep Kubernetes knowledge.        |
|  13 | K-pop (Kubernetes Protobuff Operator) enables building operators via gRPC services, focusing on business logic and reducing Kubernetes-specific complexity.           |
|  14 | K-pop and Crow together cover over 90% of platform developer use cases at Spotify.                                                                                    |
|  15 | K-pop has improved platform team adoption and reduced the learning curve for exposing products on the platform.                                                       |
|  16 | Future challenges include scaling, observability, fault toleranc                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=W-_kJEX-_RY)