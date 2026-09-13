---
type: Video Note
title: "Simplifying Cloud Native App Testing Across Environments - Laurent Broudoux & Artur Ciocanu"
description: "The video discusses the challenges of deploying cloud-native applications across various environments and introduces tools to enhance resilience, abstraction, and portability without sacrificing developer experience. Using a pizza store app..."
resource: https://www.youtube.com/watch?v=RvTEYp7QyzI
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video discusses the challenges of deploying cloud-native applications across various environments and introduces tools to enhance resilience, abstraction, and portability without sacrificing developer experience.
Using a pizza store application as an example, the presenters demonstrate how Dapper, a CNCF project, abstracts away infrastructure complexities such as service invocation, pub/sub, and security, making applications portable and easier to manage across different technology stacks.
They also introduce Microx, another CNCF project focused on API simulation, mocking, and contract testing, which simplifies local development and testing by providing lightweight simulations of dependent services.
By integrating Dapper and Microx with test containers, developers can efficiently manage dependencies, ensure API conformance, and reduce resource consumption during development.
The session concludes by highlighting how these tools together streamline the development and testing of resilient, portable, and robust cloud-native applications, even when incorporating advanced features like durable workflows and AI-driven processes.
# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussed challenges of deploying cloud native applications across environments (laptop, Kubernetes, cloud providers)                                             |
|   2 | Emphasized need for resilience, abstraction, portability, and maintaining developer experience                                                                    |
|   3 | Demonstrated a cloud native pizza store app with store, kitchen, and delivery microservices communicating via REST APIs and events                                |
|   4 | Application relies on PostgreSQL database and Kafka broker; components require appropriate clients and drivers                                                    |
|   5 | Enterprise transformation requires handling connection pools, security, secrets, caching, resiliency (fault tolerance, retries, circuit breakers)                 |
|   6 | Traditional approach involves integrating multiple libraries for each language stack, leading to complexity                                                       |
|   7 | Introduced Dapr (CNCF project) as a solution for abstraction and portability across clouds, storage, and message brokers                                          |
|   8 | Dapr provides APIs (HTTP/gRPC), optional SDKs for major languages, and a runtime layer decoupled from compute (Kubernetes, on-prem, edge)                         |
|   9 | Dapr codifies distributed application best practices and offers building blocks: pub/sub, actors (virtual actor pattern), workflows (durable execution), and more |
|  10 | Dapr externalizes resiliency policies (circuit breakers, retries, timeouts) via YAML configuration                                                                |
|  11 | Service-to-service invocation in Dapr decouples services and simplifies communication and service discovery                                                       |
|  12 | Dapr enhances security with built-in mTLS for service communication                                                                                               |
|  13 | Dapr abstracts away broker complexity, allowing easy switching between Kafka, RabbitMQ, SQS, etc.                                                                 |
|  14 | Developer experience can suffer from managing many dependencies and complex local environments                                                                    |
|  15 | Testcontainers library enables lightweight containerized dependencies for local development/testing                                                               |
|  16 | Introduced Micro (CNCF project) for API simulation, mocking, and contract testing across REST, GraphQL, gRPC, and event-driven APIs                               |
|  17 | Micro uses artifacts (OpenAPI, gRPC, Postman collections) to generate mocks and validate API conformance                                                          |
|  18 | Both Dapr and Micro have Test                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RvTEYp7QyzI)