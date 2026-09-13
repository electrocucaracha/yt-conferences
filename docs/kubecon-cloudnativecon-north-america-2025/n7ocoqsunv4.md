---
layout: default
title:
  "Project Lightning Talk: Dapr: Start Building Distributed Applications With
  Ease Using... Marc Duiker"
nav_order: 215
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Mark Derer, a community manager for the Deer project, introduces Deer,
  the Distributed Application Runtime, which is a CNCF-graduated project designed
  to simplify building secure and reliable microservices and agentic AI systems through
  bui...
resource: https://www.youtube.com/watch?v=N7ocoqSUNV4
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Mark Derer, a community manager for the Deer project, introduces Deer, the Distributed Application Runtime, which is a CNCF-graduated project designed to simplify building secure and reliable microservices and agentic AI systems through building block APIs.
Deer operates as a sidecar to applications, providing APIs that decouple the application layer from infrastructure, supporting flexibility and portability by allowing configuration with various message brokers, state stores, and secret managers.
A key recent feature is Deer Workflow, a built-in workflow engine that ensures workflow durability and seamless integration with other Deer APIs, supporting multiple programming languages and workflow patterns such as activity chaining and event waiting.
The latest release, version 1.16, adds multi-location workflow support, improved performance, HTTP streaming, identity federation, and enhanced conversation API tooling, while the upcoming 1.17 release will focus on workflow versioning, management tooling, and tracing.
Mark encourages viewers to explore case studies, participate in planning, and connect via shared links or at the project pavilion.

# Main Points

|   # | Main point                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Mark Derer is a Deer community manager presenting on building distributed applications using building block APIs.                                                                            |
|   2 | Deer stands for Distributed Application Runtime and is a graduated CNCF project since November.                                                                                              |
|   3 | Deer has been active for about six years.                                                                                                                                                    |
|   4 | Provides APIs for building secure and reliable microservices and agentic AI systems.                                                                                                         |
|   5 | Used by many large organizations.                                                                                                                                                            |
|   6 | Developer surveys report an average of 30% development time saved using Deer versus not using Dapper.                                                                                        |
|   7 | Deer runs as a sidecar next to applications, offering APIs accessible from the application.                                                                                                  |
|   8 | Dapper decouples the application layer from underlying infrastructure.                                                                                                                       |
|   9 | Supports configuring with various message brokers, secrets, and state management systems via GML files.                                                                                      |
|  10 | Enhances flexibility and portability of applications and architecture.                                                                                                                       |
|  11 | Recent major feature: Deer Workflow, a built-in workflow engine in the sidecar.                                                                                                              |
|  12 | Deer Workflow uses durable execution, saving workflow state to a compatible state store.                                                                                                     |
|  13 | Ensures workflows resume and complete even after application or node failures.                                                                                                               |
|  14 | Workflows are authored in code (C, Java, Python, Go, JavaScript).                                                                                                                            |
|  15 | Supports workflow patterns: activity chaining, fan out/fan in, recurring tasks, waiting for external events.                                                                                 |
|  16 | Deapper Agents is a Python library for building agentic systems, using Deer Workflow for reliability.                                                                                        |
|  17 | Current Deer release is 1.16 (September), adding multi-location workflow support, improved workflow performance, HTTP streaming, Identity Federation, and extended Conversation API tooling. |
|  18 | Next release 1.17 is scheduled for January, focusing on workflow versioning, better management tooling, and improved workflow tracing.                                                       |
|  19 | Feedback on planning can be given via Deer issue tracker.                                                                                                                                    |
|  20 | 11 Deer case studies are published on the CNCF website.                                                                                                                                      |
|  21 | Project team members will be available at the project pavilion.                                                                                                                              |
|  22 | QR code shared for accessing slide deck, links, and connecting with Mark.                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=N7ocoqSUNV4)
