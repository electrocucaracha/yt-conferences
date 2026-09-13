---
type: Video Note
title: "Day-2’000 - Migration From Kubeadm+Ansible To ClusterAPI+Talos: A Swiss Bank’s... Clément Nussbaumer"
description: "Clemon Bame, a Swiss software engineer at Post Finance, presented on migrating from Cubadium to Cluster API and Telos. The goal is to keep clusters alive for six years instead of recreating new ones with each release. They use large shared..."
resource: https://www.youtube.com/watch?v=uQ_WN1kuDo0
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Clemon Bame, a Swiss software engineer at Post Finance, presented on migrating from Cubadium to Cluster API and Telos.
The goal is to keep clusters alive for six years instead of recreating new ones with each release.
They use large shared clusters with many namespaces for application teams.
To migrate, they will configure matching, import existing PKI infrastructure, create CRDs, add cluster API nodes, and monitor for edge cases.
A tool has been developed to manage clusters in a disaster recovery scenario by starting a local cluster, installing CRDs and controllers, checking for existing manifests, and provisioning a new management cluster if needed.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=uQ_WN1kuDo0)