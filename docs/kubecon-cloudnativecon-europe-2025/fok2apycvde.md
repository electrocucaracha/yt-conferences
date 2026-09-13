---
layout: default
title:
  "Project Lightning Talk: Transforming your Application Behavior to Kubernetes
  Ob... Matthias Bertschy"
nav_order: 265
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Matias, co-maintainer of Cubscape, discusses the evolution of their static
  scanner project from its inception in 2021 to reaching incubation status this year.
  Initially focused on scanning cluster resources against security frameworks, they...
resource: https://www.youtube.com/watch?v=fok2apYcVdE
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

Matias, co-maintainer of Cubscape, discusses the evolution of their static scanner project from its inception in 2021 to reaching incubation status this year.
Initially focused on scanning cluster resources against security frameworks, they expanded to include eBPF (Extended Berkeley Packet Filter) capabilities to monitor application behavior and store it as a CRD (Custom Resource Definition) in the Kubernetes API.
However, this expansion led to significant issues due to the large size of the data, prompting modifications such as using files and SQL-like databases, sending diffs instead of full objects, and replacing JSON with gRPC, resulting in improved performance and reduced memory usage.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fok2apYcVdE)
