---
type: Video Note
title: "Spark on Kubernetes, a Practical Guide - Damon Cortesi, Airbnb"
description: "Damon Cortezy, a staff software engineer at Airbnb, discusses the company's journey with Spark on Kubernetes. They migrated 38% of their production workload to Kubernetes in just a month, after starting the project over a year ago. The deci..."
resource: https://www.youtube.com/watch?v=ejJ6A0sIdbw
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Damon Cortezy, a staff software engineer at Airbnb, discusses the company's journey with Spark on Kubernetes.
They migrated 38% of their production workload to Kubernetes in just a month, after starting the project over a year ago.
The decision to use Spark on Kubernetes was driven by flexibility, compute optimization, and observability.
Key considerations included choosing between Helm, Argo, or Flux for cluster management, selecting a shuffle service (Kelliborn), and implementing a custom logging solution using OpenTelemetry.
The team used Airflow for ramping up the migration process without disrupting users.
They also leveraged Argo CD for deploying configurations stored in Git.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ejJ6A0sIdbw)