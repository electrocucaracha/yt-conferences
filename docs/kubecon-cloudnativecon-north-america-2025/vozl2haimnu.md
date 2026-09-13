---
layout: default
title:
  Progressive Configuration Delivery for Zero-Downtime Cloud Workloads - Yuxing
  Yuan & Hao Wu
nav_order: 202
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The presentation introduces a new approach to configuration management
  in cloud-native environments, focusing on achieving zero-downtime configuration
  updates through the OpenKruise project. OpenKruise, a CNCF incubating project adopted
  by...
resource: https://www.youtube.com/watch?v=vozl2HAiMNU
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

The presentation introduces a new approach to configuration management in cloud-native environments, focusing on achieving zero-downtime configuration updates through the OpenKruise project.
OpenKruise, a CNCF incubating project adopted by hundreds of companies, offers features like in-place updates and set management to address real-world operational challenges.
The speakers highlight the limitations of current Kubernetes configuration update methods, which are manual, risky, and lack observability, and present ConfigMapSet—a declarative custom resource for versioned, progressive, and observable configuration delivery.
ConfigMapSet enables safe, controlled rollouts, decouples configuration updates from workload lifecycles, and supports multi-version management, rollback, and gradual dependency migration.
The team invites community contributions and outlines future enhancements, including multi-version rollout strategies and package version management for drivers, aiming to make configuration delivery as automated and reliable as application deployment.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presented a new approach to configuration management for zero downtime updates in cloud native environments.                                                                             |
|   2 | Introduced OpenKruise, a CNCF incubating project focused on application automation, with features like in-place updates and set management.                                              |
|   3 | Highlighted OpenKruise’s adoption by hundreds of companies and its ability to solve real-world operational challenges.                                                                   |
|   4 | Explained the significance of the SidecarSet feature, which decouples sidecar container lifecycle from main application containers, enabling independent updates.                        |
|   5 | Cited major cloud outages (AWS, Google Cloud, Alibaba Cloud) caused by configuration issues, emphasizing the need for safer config management.                                           |
|   6 | Identified limitations of current Kubernetes config update methods: require pod restarts, lack active triggers, and have poor observability.                                             |
|   7 | Introduced ConfigMapSet (CMS), a declarative CRD for versioned configuration delivery with traceable versions and progressive rollout policies.                                          |
|   8 | CMS allows configuration updates to be decoupled from workload lifecycle and image versions.                                                                                             |
|   9 | Core principles of CMS:                                                                                                                                                                  |
|  10 | Declarative CRD with human-readable version aliases.                                                                                                                                     |
|  11 | Versioned configuration with a central CMS Hub storing historical versions.                                                                                                              |
|  12 | Progressive rollout by percentage or absolute number of pods.                                                                                                                            |
|  13 | Observable config version per pod.                                                                                                                                                       |
|  14 | Decoupled config and image versions.                                                                                                                                                     |
|  15 | CMS workflow:                                                                                                                                                                            |
|  16 | Manage revisions and prune old versions.                                                                                                                                                 |
|  17 | Synchronize pods to target config versions, restart sidecar containers as needed.                                                                                                        |
|  18 | Update CMS status to show version distribution across pods.                                                                                                                              |
|  19 | CMS supports use cases like progressive config updates, multi-version validation (A/B or canary testing), gradual dependency migration, and versioned model/rule updates for AI systems. |
|  20 | Future enhancements: multi-version rollout, proportional scaling, cross-cluster version control.                                                                                         |
|  21 | Encouraged community participation and contributions.                                                                                                                                    |
|  22 | Mentioned future opportunity for package version management for GPU a                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vozl2HAiMNU)
