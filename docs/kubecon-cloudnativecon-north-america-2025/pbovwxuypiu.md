---
layout: default
title:
  "Keynote: How One Line of Code Freed 30,000 CPU Cores: Deep-Diving Fluent Bit
  at Petabyte... F. Ponce"
nav_order: 124
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Fabian, a member of OpenAI's applied observability team, discusses the
  use of open-source technology to process logs at scale. The team uses Fluent Bit
  on every Kubernetes node in their fleet to ingest log files, perform sampling and
  enrich...
resource: https://www.youtube.com/watch?v=pbOvWxuYPIU
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

Fabian, a member of OpenAI's applied observability team, discusses the use of open-source technology to process logs at scale.
The team uses Fluent Bit on every Kubernetes node in their fleet to ingest log files, perform sampling and enrichment, and route them to data stores for querying.
To optimize CPU usage, they discovered that the biggest user of Fluent Bit's CPU time was not string processing as expected, but rather figuring out file sizes before reading logs, which is driven by the "i notify" feature.
Disabling this feature resulted in a 50% drop in CPU usage across their heavily loaded pods, returning approximately 30,000 CPU cores to the Kubernetes cluster.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pbOvWxuYPIU)
