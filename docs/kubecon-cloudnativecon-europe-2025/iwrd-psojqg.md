---
layout: default
title:
  Pushing the Limits of Prometheus at Etsy - Chris Leavoy, Etsy & Bryan Boreham,
  Grafana Labs
nav_order: 277
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The talk discusses the challenges of operating Prometheus at scale, specifically
  with Etsy's largest server, which monitors millions of metrics and handles 5 million
  samples per second during peak periods. The team faced issues with data re...
resource: https://www.youtube.com/watch?v=IWrd-pSojqg
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

The talk discusses the challenges of operating Prometheus at scale, specifically with Etsy's largest server, which monitors millions of metrics and handles 5 million samples per second during peak periods.
The team faced issues with data retention, compaction, and garbage collection, which were impacting performance.
To address these issues, they made several changes, including disabling compaction, tuning remote right for required throughput, and adjusting garbage collection settings.
These changes resulted in improved performance and allowed the server to handle increased traffic during Black Friday without crashing.
The team also highlighted the importance of monitoring metrics, limiting query scrapes, and considering alternative configurations, such as using multiple scrape instances with different configs.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=IWrd-pSojqg)
