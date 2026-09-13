---
layout: default
title:
  "Lightning Talk: “Naming Things Is Hard”: A Guide to Naming Using Network Science
  - Nick Travaglini"
nav_order: 210
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Nick, a senior technical customer success manager at Honeycomb.io,
  discusses effective naming strategies for instrumenting software with open telemetry,
  drawing on scientific research to guide best practices. He outlines the p...
resource: https://www.youtube.com/watch?v=vU5v4_P13lE
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

In this talk, Nick, a senior technical customer success manager at Honeycomb.io, discusses effective naming strategies for instrumenting software with open telemetry, drawing on scientific research to guide best practices.
He outlines the problem of creating useful, descriptive names for telemetry data, emphasizing the importance of a shared language within teams for effective debugging.
Nick reviews existing resources, such as OpenTelemetry blogs, and introduces research on how teams develop naming conventions, highlighting a paradox where both fully decentralized and fully centralized approaches can yield strong results.
However, experimental findings suggest that a "connected broker" model—slightly more centralized than decentralized—enables teams to generate effective names quickly and collaboratively, combining the benefits of exploration and synthesis.
He encourages teams to consider this model when naming telemetry elements, while noting that results may vary outside laboratory settings, and invites further discussion and experimentation within the community.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on effective naming when instrumenting with OpenTelemetry.                                                                            |
|   2 | Agenda includes speaker introduction, problem definition, existing resources, scientific research, practical takeaways, and wrap-up.                       |
|   3 | Speaker: Nick, senior technical customer success manager at honeycomb.io.                                                                                  |
|   4 | Problem: OpenTelemetry offers flexibility, but effective naming is crucial for debugging and team collaboration.                                           |
|   5 | Existing resources: OpenTelemetry project provides blogs on naming; recommended to read them.                                                              |
|   6 | Presentation introduces an additional, science-based method for naming.                                                                                    |
|   7 | Scientific research examines how teams create a shared language and effective naming conventions.                                                          |
|   8 | Research paradox: Both totally decentralized and fully centralized teams can produce the best shared language.                                             |
|   9 | Decentralized teams generate names fastest; centralized teams create more descriptive, effective names.                                                    |
|  10 | Hypothesis: Disambiguating "best" horizontally (speed vs. effectiveness) clarifies the paradox.                                                            |
|  11 | Experiment: Groups of five name abstract symbols (tandemss) with varying ambiguity, using different network configurations (decentralized to centralized). |
|  12 | Key finding: The "connected broker" network (slightly more centralized than decentralized) is fastest and as effective as the fully centralized model.     |
|  13 | Practical takeaway: The connected broker model allows teams to explore and synthesize names quickly and effectively.                                       |
|  14 | Recommendation: Consider the connected broker approach when naming in software instrumentation.                                                            |
|  15 | Caveat: Results are from a laboratory experiment; real-world outcomes may differ.                                                                          |
|  16 | Encouragement to try the approach and share results with the community.                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vU5v4_P13lE)
