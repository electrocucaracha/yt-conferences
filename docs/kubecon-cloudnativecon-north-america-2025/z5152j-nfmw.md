---
layout: default
title:
  "Shaping LTS Together: What We’ve Learned the... Nikhita R, Nikhila K, Micah
  H, Jeremy R & Aniket P"
nav_order: 277
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The panel discussion focused on the challenges and lessons learned in
  implementing Long-Term Support (LTS) for Kubernetes, especially as the Kubernetes
  LTS working group is winding down. Panelists from major companies such as Broadcom,
  AWS...
resource: https://www.youtube.com/watch?v=z5152J_nFmw
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

The panel discussion focused on the challenges and lessons learned in implementing Long-Term Support (LTS) for Kubernetes, especially as the Kubernetes LTS working group is winding down.
Panelists from major companies such as Broadcom, AWS, Canonical, and Microsoft highlighted the primary drivers for LTS, including the needs of regulated industries, lengthy validation processes, and the desire for stability and predictable upgrade cycles.
They discussed the complexities of determining support timelines, the importance of aligning support across all releases for consistency, and the difficulties of backporting security fixes and maintaining compatibility with a rapidly evolving ecosystem.
The conversation also addressed misconceptions about the ease of LTS, the significant resource requirements, and the reasons behind the working group’s closure, noting that while the need for LTS remains, much of the responsibility has shifted to vendors’ commercial offerings.
The panel concluded that although the working group is ending, the demand for LTS persists, and future community efforts may arise if needs change.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Kubernetes LTS working group is winding down, but the problems it aimed to solve remain.                                                                                                   |
|   2 | The panel focuses on sharing challenges and patterns in LTS, not comparing vendors or models.                                                                                              |
|   3 | Main drivers for LTS: lengthy end-to-end validation in some industries, regulatory requirements, mission-critical workloads, limited maintenance windows, and conservative upgrade cycles. |
|   4 | Non-connected systems and environments with offline updates also require LTS.                                                                                                              |
|   5 | Past difficulties with Kubernetes upgrades and API changes contribute to demand for LTS.                                                                                                   |
|   6 | Legal compliance and certification timelines often exceed Kubernetes support periods.                                                                                                      |
|   7 | Enterprises face cost factors and have traditional infrastructure upgrade cadences.                                                                                                        |
|   8 | Improving upgrade experience may reduce, but not eliminate, LTS needs, especially for regulated industries.                                                                                |
|   9 | Extended support timelines are influenced by customer expectations, societal cycles, and balancing maintenance complexity.                                                                 |
|  10 | Major vendors have aligned on similar LTS periods; longer support increases maintenance complexity.                                                                                        |
|  11 | Customers expect support for both runtime and add-ons, requiring synchronization of cadences.                                                                                              |
|  12 | Most vendors now support every Kubernetes release with the same LTS term for consistency and flexibility.                                                                                  |
|  13 | Predictability in release cadence is critical for LTS customers.                                                                                                                           |
|  14 | LTS scope is typically limited to security and critical fixes; feature backports are rare and require extra consideration.                                                                 |
|  15 | Backporting can introduce regressions, especially as code diverges from upstream.                                                                                                          |
|  16 | Maintaining LTS involves supporting a minimal set of ecosystem projects; supporting all is impractical.                                                                                    |
|  17 | Upgrade paths for LTS must accommodate infrequent upgrades, skip upgrades, and time-boxed maintenance windows.                                                                             |
|  18 | Supporting multiple LTS versions increases testing complexity and infrastructure costs.                                                                                                    |
|  19 | Misconceptions: backporting patches is straightforward; upgrading dependencies like Go is always easy.                                                                                     |
|  20 | LTS working group is winding down due to lack                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=z5152J_nFmw)
