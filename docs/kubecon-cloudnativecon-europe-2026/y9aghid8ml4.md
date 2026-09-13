---
layout: default
title:
  "18 Bluetooth Controllers Walk into a Bar: Observability & R... Simon Schrottner
  & Manuel Timelthaler"
nav_order: 4
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this CubeCon talk, the presenters describe their experience enhancing
  observability and runtime configuration for a real-time, acceleration-based party
  game using CNCF tools. The game, played with PlayStation Move controllers and running...
resource: https://www.youtube.com/watch?v=Y9agHID8Ml4
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this CubeCon talk, the presenters describe their experience enhancing observability and runtime configuration for a real-time, acceleration-based party game using CNCF tools.
The game, played with PlayStation Move controllers and running on a Raspberry Pi, initially lacked visibility into issues due to its open-source, monitorless setup.
By refactoring the codebase into a microservices architecture with gRPC and integrating tools like OpenTelemetry, Prometheus, and feature flagging via Flexd, they achieved detailed insights such as player lifespans, connection quality, and real-time metrics.
They discuss challenges with data collection intervals, metric density, and system resource constraints, ultimately finding that pushing metrics and careful label management enabled near real-time observability even on limited hardware.
The speakers encourage the community to apply cloud-native observability tools to real-time and IoT systems, share their findings, and contribute improvements, highlighting the potential for broader applications beyond traditional cloud environments.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation at CubeCon about observability and runtime configuration for a real-time party game using CNCF tools                |
|   2 | The game uses PlayStation Move controllers as motion sensors; players try to protect their "egg" while making others lose theirs |
|   3 | Game is open source, runs on a Raspberry Pi, and has no monitor or UI                                                            |
|   4 | Initial challenges included lack of observability and difficulty debugging issues at conferences                                 |
|   5 | Decided to add observability using OpenTelemetry and feature flagging (OpenFeature)                                              |
|   6 | Refactored the game into a microservices architecture with gRPC for better instrumentation                                       |
|   7 | Deployed an observability stack (collector, backend, feature flag proxy) on the Raspberry Pi                                     |
|   8 | Achieved spans and traces for game events, enabling deeper insights (e.g., player lifetimes)                                     |
|   9 | Raspberry Pi handled the overengineered stack and up to 32 controllers at 60 fps without issues                                  |
|  10 | Used Prometheus for metrics; default 60-second scrape interval was too slow for short games                                      |
|  11 | Switched to pushing metrics for near real-time data (down to 300-500 ms intervals)                                               |
|  12 | Higher data density required careful tuning; pushing metrics was resource intensive                                              |
|  13 | OpenTelemetry SDK and collector allowed buffer and batching configuration for efficiency                                         |
|  14 | Adding high-cardinality labels (e.g., game ID) caused performance issues in Prometheus and Grafana                               |
|  15 | VictoriaMetrics offered better performance for high-density, low-cardinality data                                                |
|  16 | Feature flags enabled fault injection (e.g., port drops, disconnects, acceleration spikes) for testing                           |
|  17 | Dashboards provided visibility into controller status, connection quality, battery, and acceleration data                        |
|  18 | Observability tools helped identify issues like disconnects and unrealistic acceleration spikes                                  |
|  19 | Documentation for CNCF observability tools is cloud-native focused; more IoT and real-time examples needed                       |
|  20 | Call to action: try CNCF tools on real-time/IoT systems, document findings, and contribute back                                  |
|  21 | Game is based on an old PlayStation 2 title, now open                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Y9agHID8Ml4)
