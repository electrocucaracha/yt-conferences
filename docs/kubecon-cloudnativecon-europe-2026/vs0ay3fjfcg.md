---
type: Video Note
title: "Dynamic Mocking for Event-Driven APIs: A Cloud Native Approa... Harshvardhan Parmar & Anushka Saxena"
description: "The speaker introduces the challenge of testing event-driven APIs, noting that unlike REST APIs, event-driven systems are more complex and difficult to mock due to their real-time, unpredictable nature. Static mocks fail to replicate real-w..."
resource: https://www.youtube.com/watch?v=vS0AY3FJfcg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces the challenge of testing event-driven APIs, noting that unlike REST APIs, event-driven systems are more complex and difficult to mock due to their real-time, unpredictable nature.
Static mocks fail to replicate real-world behavior, leading to the need for dynamic mocking solutions.
The presentation demonstrates how the cloud-native tool Micros can be used within Kubernetes environments to create dynamic mocks for event-driven APIs using async API specifications.
Through a live demo, the speaker shows how Micros imports async API files, generates both static and dynamic mocks using mock templates, and enables realistic integration testing by simulating producer-consumer interactions.
The session concludes by inviting feedback and contributions to the Micros community, emphasizing the tool’s ease of use and its alignment with cloud-native development practices.
# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on dynamic mocking for event-driven APIs using the cloud-native tool Micros Micro                            |
|   2 | Co-speaker Harshwadin unable to attend due to visa issues; Anushka Sakina presenting                                      |
|   3 | Anushka is a software application developer apprentice at Google; disclaimer that the talk is not related to her employer |
|   4 | Event-driven architectures are increasingly common in production systems                                                  |
|   5 | Testing event-driven APIs is more complex than testing REST APIs                                                          |
|   6 | Static mocks for event-driven systems are insufficient; they cannot replicate real-time, unpredictable behavior           |
|   7 | Static mocks can lead to stale data and unrealistic testing scenarios                                                     |
|   8 | Need for dynamic mocks that simulate real-time producer-consumer interactions and stateful message flows                  |
|   9 | AsyncAPI provides API specs for event-driven APIs, similar to OpenAPI for REST                                            |
|  10 | Micros Micro is a Kubernetes-native, lightweight tool for dynamic mocking of event-driven APIs                            |
|  11 | Micros supports multiple protocols and integrates with Kubernetes clusters                                                |
|  12 | Demo: AsyncAPI spec file created for an order-based event-driven API (order creation, payment processing, order shipping) |
|  13 | Micros can import AsyncAPI spec files and generate live mocks directly from the specs                                     |
|  14 | Initial mocks use hardcoded values from the spec; not dynamic                                                             |
|  15 | Upgraded AsyncAPI spec with dynamic mocking support using "mock templates" (functions to generate random values)          |
|  16 | Mock templates allow dynamic generation of payloads (e.g., random order IDs)                                              |
|  17 | Micros enables dynamic mocks to be generated and consumed in real time within Kubernetes                                  |
|  18 | Micros facilitates spec-driven development and simplifies testing of event-driven APIs in cloud-native environments       |
|  19 | Community is encouraged to contribute, provide feedback, and explore the Micros GitHub repo                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vS0AY3FJfcg)