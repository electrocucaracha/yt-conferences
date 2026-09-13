---
layout: default
title:
  "Message In, Job Out: Build Event-Driven Workflows in Kubernetes Using... Colin
  Lacy & Grace Brickley"
nav_order: 168
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Colin Lacy and Grace Brickley, software engineers
  at Cisco, demonstrate how their small, cost-conscious disco services startup automates
  customer onboarding using event-driven workflows in Kubernetes with NATS, CloudEv...
resource: https://www.youtube.com/watch?v=IvvuZiTkGZU
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

In this presentation, Colin Lacy and Grace Brickley, software engineers at Cisco, demonstrate how their small, cost-conscious disco services startup automates customer onboarding using event-driven workflows in Kubernetes with NATS, CloudEvents, and Project Speltos.
They explain that NATS serves as a lightweight, high-performance messaging system for asynchronous communication between microservices, while CloudEvents provides a standardized schema for event data, ensuring interoperability across different platforms.
Project Speltos acts as a management plane for Kubernetes resources, enabling reactive provisioning and integration with NATS to trigger automated workflows based on incoming events.
The workflow they showcase automates the creation of customer accounts, user entries, welcome emails, and marketing notifications, leveraging Kubernetes jobs for each step, which allows for retries, scalability, and extensibility.
The solution meets their non-functional requirements by minimizing compute costs, supporting bulk onboarding, and enabling easy workflow extension, all while maximizing automation and supporting multi-cluster management.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on building event-driven workflows in Kubernetes using NATS, CloudEvents, and Project Speltos                                                                                                                                                      |
|   2 | Presenters: Colin Lacy and Grace Brickley, software engineers at Cisco and a disco services startup                                                                                                                                                             |
|   3 | Startup is small, cost-conscious, customer-focused, and relies heavily on automation                                                                                                                                                                            |
|   4 | Tools used:                                                                                                                                                                                                                                                     |
|   5 | NATS: Lightweight, fast, CNCF incubating messaging system for event streaming; supports event storage, consumer tracking, authentication, and arbitrary payloads; enables asynchronous communication and event-driven patterns (fan-in, fan-out, saga)          |
|   6 | CloudEvents: CNCF graduated project; provides a common schema for event data across platforms; transport agnostic; SDKs for major languages; extensible with optional fields                                                                                    |
|   7 | Project Speltos: Open source management plane for Kubernetes resources across clusters; supports up to 127 clusters; uses labels and profiles for resource management; built-in event framework for reactive provisioning; integrates with NATS and CloudEvents |
|   8 | Speltos workflow components:                                                                                                                                                                                                                                    |
|   9 | Secret: Configures Speltos to connect to NATS                                                                                                                                                                                                                   |
|  10 | EventSource: Custom resource to listen to specific NATS streams/subjects                                                                                                                                                                                        |
|  11 | EventTrigger: Defines response to events from EventSource                                                                                                                                                                                                       |
|  12 | ConfigMap: Holds YAML for resources to be applied; supports Golang templating and Sprig functions for dynamic resource creation                                                                                                                                 |
|  13 | Jobs as event handlers:                                                                                                                                                                                                                                         |
|  14 | Step 1: Spin up container, read event context                                                                                                                                                                                                                   |
|  15 | Step 2: Perform work (e.g., create DB entry, send email)                                                                                                                                                                                                        |
|  16 | Step 3: Raise new event to NATS                                                                                                                                                                                                                                 |
|  17 | Jobs are easy to test, scaffold, document, debug; have built-in retries and logging                                                                                                                                                                             |
|  18 | Automated customer onboarding workflow:                                                                                                                                                                                                                         |
|  19 | On new subscription, create customer account and user entries                                                                                                                                                                                                   |
|  20 | Send welcome emails                                                                                                                                                                                                                                             |
|  21 | Create outreach record and notify sales/marketing                                                                                                                                                                                                               |
|  22 | Non-functional requirements: cost efficiency, scalability, extensibility, embedded logic, built-in retries                                                                                                                                                      |
|  23 | Demo: Fully automated onboarding workflow using NATS, CloudEvents, Speltos, and Kubernete                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=IvvuZiTkGZU)
