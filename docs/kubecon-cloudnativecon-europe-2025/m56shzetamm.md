---
layout: default
title:
  "Beyond CloudEvents: Endpoints, Messages, Schemas – CNCF XRegistry - Manuel
  Ottlik, HDI Global SE"
nav_order: 24
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=M56SHzETAmM
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: Man Lotle, a product owner for cloud native platforms at HDI Global, discusses Cloud Events Registry (X Registry), a project aimed at harmonizing metadata across event-driven architectures.
The X Registry provides a vendor-agnostic specification for managing metadata about resources, allowing for interoperability and reducing schema repetition.
Man demonstrates the registry's capabilities using a todo list example, showcasing how it can be used to manage events, schemas, and endpoints.
The X Registry is currently in its RC1 stage, with plans for further development and release in the near future.

# Main Points

|   # | Main point                                                                |
| --: | ------------------------------------------------------------------------- |
|   1 | Cloud Events:                                                             |
|   2 | Defines common metadata for events                                        |
|   3 | Defines protocol and broker-independent headers                           |
|   4 | Has nine SDKs, six protocol bindings (AMQP, Kafka, HTTP, MQTT)            |
|   5 | Allows breaking change-free schema updates                                |
|   6 | Has a structured mode for non-binary data                                 |
|   7 | X Registry:                                                               |
|   8 | Extensible registry specification for managing metadata about resources   |
|   9 | Defines three entities: message definitions, schema groups, and endpoints |
|  10 | Provides a vendor-agnostic registry specification                         |
|  11 | Has a reference implementation (XR registry/server) and CLI               |
|  12 | Allows registering postboxes for event delivery                           |
|  13 | Use Cases:                                                                |
|  14 | Harmonizing metadata across integration products                          |
|  15 | Reducing schema repetition                                                |
|  16 | Connecting metadata from separate systems                                 |
|  17 | Roadmap:                                                                  |
|  18 | Released RC1, with plans for RC2 and final release in two months          |
|  19 | Filed for CNCF sandbox application last month                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=M56SHzETAmM)
