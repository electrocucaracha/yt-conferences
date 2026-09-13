---
type: Video Note
title: "Knative Project Update - Dave Protasowski, Independent"
description: "Dave, a full-time Knative maintainer and serving lead, provides an update on the Knative project, highlighting its role in simplifying Kubernetes for app developers through three main components: functions, serving, and eventing. He demonst..."
resource: https://www.youtube.com/watch?v=lV16ujEiLIs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Dave, a full-time Knative maintainer and serving lead, provides an update on the Knative project, highlighting its role in simplifying Kubernetes for app developers through three main components: functions, serving, and eventing.
He demonstrates how Knative Functions enables easy creation, local testing, and deployment of serverless functions in various languages, while Knative Serving allows for rapid deployment, autoscaling (including scale-to-zero), traffic splitting, and revision tracking of containerized applications.
The eventing component is showcased through a demo where decoupled services process and respond to events, illustrating flexible integrations and routing.
Dave also introduces an experimental integration with the Model Context Protocol (MCP), showing how Knative services can dynamically register as tools for AI workflows.
The presentation concludes with project updates, including Knative’s recent graduation, new features like Gateway API support, OpenTelemetry migration, enhanced security, and community engagement opportunities.
# Main Points

|   # | Main point                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------- |
|   1 | Dave is a full-time Knative maintainer, serving lead, and on the steering committee.                  |
|   2 | Knative aims to simplify Kubernetes for app developers, focusing on functions, serving, and eventing. |
|   3 | Knative Functions:                                                                                    |
|   4 | Helps bootstrap functions with templates for multiple languages (Java, Python, Node, Go, etc.).       |
|   5 | Supports HTTP and CloudEvents.                                                                        |
|   6 | Functions can be built and run locally or deployed remotely.                                          |
|   7 | No strong opinions on handler code; supports cloud events for routing/filtering.                      |
|   8 | Can build without Docker using host builder for some languages.                                       |
|   9 | Knative Serving:                                                                                      |
|  10 | Deploys containers that scale up/down, including to zero (serverless).                                |
|  11 | Simple deployment: just need a container image.                                                       |
|  12 | Supports automatic TLS with domain names.                                                             |
|  13 | Allows traffic splitting between revisions (e.g., 50/50).                                             |
|  14 | Supports container concurrency settings and autoscaling based on request load.                        |
|  15 | Tracks changes via revisions; can roll back traffic to previous revisions.                            |
|  16 | Presents a simple interface for app developers, hiding Kubernetes complexity.                         |
|  17 | Knative Eventing:                                                                                     |
|  18 | Decouples services using events via brokers and triggers.                                             |
|  19 | Supports integration with external sources (e.g., AWS events).                                        |
|  20 | Can target both Knative and regular Kubernetes services.                                              |
|  21 | Demonstrated event-driven workflow: intake, structuring, lookup, and apology services.                |
|  22 | Everything is declarative; supports persistent messaging with Kafka, Rabbit, NATS.                    |
|  23 | Knative building blocks can be integrated with new technologies (e.g., MCP server demo).              |
|  24 | Knative is now a graduated CNCF project.                                                              |
|  25 | Many adopters, including Niantic (Pokémon Go).                                                        |
|  26 | Serving: Gateway API improvements, migration to OpenTelemetry.                                        |
|  27 | Eventing: Supports authentication/authorization, reply/request-reply, OpenTelemetry migration.        |
|  28 | Functions: Funi CLI can run as MCP server.                                                            |
|  29 | Operator now supports Helm and Operator Hub installation.                                             |
|  30 | Updated threat model and admin docs.                                                                  |
|  31 | Community: Slack, mailing list, kative.dev for involvemen                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lV16ujEiLIs)