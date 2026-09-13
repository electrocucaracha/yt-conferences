---
layout: default
title:
  Smoothed and Anchored Rate Calculation in PromQL - Björn Rabenstein, Grafana
  Labs
nav_order: 335
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  "Bern from Kofana Labs discusses recent advancements in Prometheus rate
  calculation, introducing two new experimental methods: anchored and smooth rate
  calculations. He explains the limitations of the classic rate function, such as
  incomplet..."
resource: https://www.youtube.com/watch?v=iN5vQjDuiWc
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

Bern from Kofana Labs discusses recent advancements in Prometheus rate calculation, introducing two new experimental methods: anchored and smooth rate calculations.
He explains the limitations of the classic rate function, such as incomplete graph coverage, reliance on extrapolation, lack of composability, and confusing heuristics, which motivated the development of these new approaches.
The anchored rate method provides integer results by directly comparing the last sample in the range with the last sample before the range, improving graph coverage and requiring only one sample within the range.
The smooth rate method uses linear interpolation between samples before and after the range, offering better statistical properties, resilience to missing data, and perfect graph coverage, but requires data from the future and may underestimate current rates.
Both methods are available as experimental features in Prometheus 3.7, with users encouraged to try them via feature flags.
Bern emphasizes that these changes were carefully considered to avoid user confusion and that feedback will determine the future of the classic rate function.

# Main Points

|   # | Main point                                                                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Bern from Kofana Labs discusses new rate calculation methods in Prometheus.                                                                                                                                                                  |
|   2 | Traditional rate calculation in PromQL uses range selectors and is the most used function.                                                                                                                                                   |
|   3 | Rate, increase, and delta functions are similar but have differences in handling counters and gauges.                                                                                                                                        |
|   4 | Current rate implementation only looks inside the selected range, requiring two samples within the range.                                                                                                                                    |
|   5 | Issues with current method: hard to get full coverage in graphing, returns nothing if only one sample in range, requires extrapolation, produces non-integer values, uses complex heuristics for series start/end, and is not composable.    |
|   6 | Motivation for change: distributed PromQL engines, need for composability, and user feedback.                                                                                                                                                |
|   7 | Two new methods introduced: anchored rate and smooth rate, using a modifier keyword instead of new function names.                                                                                                                           |
|   8 | Anchored rate: takes last sample in range and last sample before range, calculates direct difference, returns integer values, works with single point in range, gives good graphing coverage, but has variable delay based on scrape timing. |
|   9 | Smooth rate: uses interpolation between samples before/after range, produces non-integer values, works with zero points in range, gives perfect graphing coverage, but needs data from the future and requires query offset.                 |
|  10 | Both methods are experimental, introduced in Prometheus 3.7, behind a feature flag (promql extended range selectors).                                                                                                                        |
|  11 | Not yet compatible with native histograms; support planned.                                                                                                                                                                                  |
|  12 | Smooth rate is resilient to missing data and statistical noise.                                                                                                                                                                              |
|  13 | Both new methods improve coverage and composability, and remove reliance on heuristics for series boundaries.                                                                                                                                |
|  14 | Classic rate calculation remains for now; future deprecation possible depending on user feedback.                                                                                                                                            |
|  15 | Feature flag may allow smooth rate as default if widely adopted.                                                                                                                                                                             |
|  16 | Strong user demand, especially from Grafana users, for anchored rate.                                                                                                                                                                        |
|  17 | Lessons learned: careful introduction of fundamental changes, use of feature flags, and importance of use                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=iN5vQjDuiWc)
