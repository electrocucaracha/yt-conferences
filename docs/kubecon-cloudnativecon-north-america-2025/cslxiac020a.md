---
layout: default
title:
  "UX Research Report: Prometheus and OTel's Resource Attributes. - Victoria
  Nduka & Amy Super"
nav_order: 329
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The presentation detailed a UX research project focused on how Prometheus
  should handle OpenTelemetry resource attributes, led by Victoria Enuka and supported
  by Amy Super and others at Grafana Labs. The research identified four main user
  w...
resource: https://www.youtube.com/watch?v=cSLXIAc020A
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

The presentation detailed a UX research project focused on how Prometheus should handle OpenTelemetry resource attributes, led by Victoria Enuka and supported by Amy Super and others at Grafana Labs.
The research identified four main user workflows for managing resource attributes in Prometheus, including complete mapping, selective attribute promotion, use of a separate target info metric (which users found complex and undesirable), and manual injection via Prometheus configuration.
Survey and interview data revealed that users are generally dissatisfied with the current integration, citing pain points such as complex join operations, the burdens of manual attribute promotion, and inadequate documentation.
Users expect resource attributes to be treated like metric labels—directly queryable and flexible—without the need for complex joins or upfront decisions about which attributes to promote.
Stakeholder interviews highlighted philosophical and technical differences between Prometheus and OpenTelemetry, but also a shared willingness to improve user experience through better collaboration.
Recommendations included prioritizing technical solutions to ease attribute handling, improving documentation with practical examples, and fostering cross-community ideation, with ongoing mentorship programs supporting these efforts.
The session concluded with resources for further engagement and an invitation for questions.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk presents a UX research report on how Prometheus should handle OpenTelemetry resource attributes.                                                                   |
|   2 | Amy Super (product designer at Grafana Labs) and Victoria Enuka (UX designer/researcher) led the project, supported by mentors from Grafana Labs.                           |
|   3 | The project originated from user struggles in the Prometheus community with OpenTelemetry resource attributes, including poor query experience and high cardinality issues. |
|   4 | Research goals: understand user pain points, stakeholder perspectives, and user expectations regarding resource attributes.                                                 |
|   5 | Methods: 7 end user interviews and a survey with 63 responses, providing both qualitative and quantitative data.                                                            |
|   6 | Four main user workflows identified:                                                                                                                                        |
|   7 | Complete mapping: all resource attributes mapped to Prometheus metric labels (used by teams with few storage constraints).                                                  |
|   8 | Selective attribute promotion: users manually choose which attributes to promote as labels.                                                                                 |
|   9 | Target info approach: resource attributes stored in a separate metric, requiring complex join operations (least preferred).                                                 |
|  10 | Manual attribution injection: resource attributes added via Prometheus scrape target definition.                                                                            |
|  11 | User satisfaction is middling; more users are frustrated than satisfied with current integration.                                                                           |
|  12 | Key pain points:                                                                                                                                                            |
|  13 | Complex join operations are challenging for most users.                                                                                                                     |
|  14 | Manual management of attribute promotion is difficult, requires predicting future needs, and changes only affect new data.                                                  |
|  15 | Documentation gaps exist in both Prometheus and OpenTelemetry communities.                                                                                                  |
|  16 | Users do not distinguish between resource attributes and metric labels; expect resource attributes to be directly queryable.                                                |
|  17 | Users want more flexibility and automation in attribute promotion, but still desire some control.                                                                           |
|  18 | Filtering and aggregating by resource attributes is very important (76% rate it as very important).                                                                         |
|  19 | Stakeholders recognize philosophical and technical differences between Prometheus (focused on metrics) and OpenTelemetry (                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cSLXIAc020A)
