---
type: Video Note
title: "Fluent Bit: Smarter Telemetry Routing, Faster Pipelines - Eduardo Silva, Chronosphere"
description: "Eduardo Silva, creator and maintainer of Fluent Bit, opened his conference presentation by discussing the project's history, its evolution from embedded Linux to cloud environments, and its recent organizational change, with Fluent Bit and..."
resource: https://www.youtube.com/watch?v=40gHwYn0bo4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Eduardo Silva, creator and maintainer of Fluent Bit, opened his conference presentation by discussing the project's history, its evolution from embedded Linux to cloud environments, and its recent organizational change, with Fluent Bit and Fluentd now both recognized as top-level CNCF projects under the "Fluent" organization.
He introduced a major new feature: next-generation routing, which allows users to direct log data based on content conditions rather than just source, simplifying configurations and improving performance.
Silva demonstrated this feature with examples and explained how it reduces computing time and CPU usage, referencing a real-world case where OpenAI halved CPU consumption by adjusting configuration.
He also highlighted Fluent Bit's pluggable architecture, support for various input sources (including syslog and Windows event logs), and recent enhancements in security and trace sampling.
During the Q&A, Silva addressed questions about Fluent Bit's role as an aggregator or collector, its multi-threaded processing improvements, Windows support, OTLP attribute modification, AWS integration, and advanced data manipulation capabilities, emphasizing ongoing community engagement and the importance of benchmarking for specific use cases.
# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Eduardo Silva, creator and maintainer of Fluent Bit, presented on the Fluent ecosystem.                                                             |
|   2 | Fluent Bit started in 2015; Fluentd is about 14 years old.                                                                                          |
|   3 | Fluent Bit evolved from embedded Linux to cloud environments, supporting devices from Raspberry Pi to servers.                                      |
|   4 | The Fluent organization has been renamed from "fluentd" to "fluent"; both Fluentd and Fluent Bit are now graduated CNCF projects at the same level. |
|   5 | Fluent Bit has over 15 billion downloads and a large user base.                                                                                     |
|   6 | OpenAI uses Fluent Bit for logging at scale and reduced CPU usage by 50% with a configuration change.                                               |
|   7 | Fluent Bit values: high performance, vendor neutrality, open source, integration with various solutions, and pluggable architecture.                |
|   8 | Data volume is increasing; Fluent Bit aims to handle this efficiently to avoid higher user costs.                                                   |
|   9 | Fluent Bit routes data from sources to destinations using declarative configuration and tags.                                                       |
|  10 | New routing mechanism allows routing based on data content, not just source.                                                                        |
|  11 | Users can define routes with conditions (e.g., field values) to send data to specific outputs.                                                      |
|  12 | Default routes can be set for unmatched data.                                                                                                       |
|  13 | The new routing mechanism simplifies configuration and reduces computing time.                                                                      |
|  14 | Routing logic can persist on disk for reliability if a destination is down.                                                                         |
|  15 | Syslog input collector now supports RFC 6587 for compatibility with many firewalls.                                                                 |
|  16 | Fluent Bit can use Windows certificate stores for secure environments.                                                                              |
|  17 | Fluent Bit supports log, metric, and trace collection, including head and tail sampling for traces.                                                 |
|  18 | Fluent Bit can read/write OTLP and integrate with OpenTelemetry.                                                                                    |
|  19 | Fluent Bit benchmarks show high performance compared to other agents.                                                                               |
|  20 | Multi-threaded architecture allows filters/processors to run on separate threads for better scalability.                                            |
|  21 | Fluent Bit fully supports Windows, including deep event log processing.                                                                             |
|  22 | Content modifier processor allows modification of OTLP attributes and nested fields.                                                                |
|  23 | Fluent Bit works with AWS FireLe                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=40gHwYn0bo4)