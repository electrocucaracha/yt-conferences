---
type: Video Note
title: "Taming Rollout Risks in Distributed Web Apps: A Location-Aware Gradual Deployment... Angela Victorio"
description: "Angela Victoria, a technical lead at JP Morgan Chase and former American Airlines developer, discusses best practices for deploying software updates with minimal risk, drawing on her experience with CI/CD pipelines and Kubernetes. She empha..."
resource: https://www.youtube.com/watch?v=-fhXEJD-ycs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Angela Victoria, a technical lead at JP Morgan Chase and former American Airlines developer, discusses best practices for deploying software updates with minimal risk, drawing on her experience with CI/CD pipelines and Kubernetes.
She emphasizes the importance of gradual rollouts, such as canary deployments and feature flags, to reduce the blast radius of potential defects and make releases less stressful.
Angela demonstrates two approaches: percentage-based traffic splitting using service mesh tools like Istio, and more granular, location-based rollouts for scenarios like airport kiosks, where random selection could disproportionately impact smaller sites.
She highlights the need for robust monitoring, immediate rollback strategies, and careful timing when deploying updates, and advises decoupling changes to avoid downtime.
Angela concludes by addressing questions about rollout timing and visibility, noting that deployment progress should be clearly communicated to developers through pipeline tools.
# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Angela Victoria is a technical lead at JP Morgan Chase, previously at American Airlines.                                            |
|   2 | Experience includes software development, CI/CD pipelines, and Kubernetes.                                                          |
|   3 | Kubernetes helps eliminate downtime during deployment, but software bugs can still occur.                                           |
|   4 | Emphasizes reducing deployment blast radius to minimize user impact.                                                                |
|   5 | Advocates for canary deployments and gradual rollouts to limit risk.                                                                |
|   6 | Feature flags and code logic can control rollout percentages or enable features in specific regions.                                |
|   7 | Traffic splitting can be achieved via DNS or deploying to select clusters/regions before full rollout.                              |
|   8 | Demo 1: Uses Istio service mesh for weighted routing (e.g., 50/50, 10/90) between version 1 (blue) and version 2 (green) of an app. |
|   9 | Automated scripts can incrementally adjust rollout percentages.                                                                     |
|  10 | Demo 2: Location-based rollout for kiosks (e.g., in airports or stores) using request headers and configuration profiles.           |
|  11 | Profiles allow granular control, assigning specific machines to new versions.                                                       |
|  12 | Automated scripts can assign a percentage (e.g., 20%) of machines to the new version, avoiding random risk in small locations.      |
|  13 | Monitoring is essential: compare metrics (failure rate, latency) between old and new versions.                                      |
|  14 | Immediate rollback scripts are necessary for both rollout methods.                                                                  |
|  15 | Gradual rollouts increase deployment time; frequency and increments should be planned.                                              |
|  16 | Warns against tightly coupled deployments (data layer, backend, UI) that require simultaneous release, as this can cause downtime.  |
|  17 | Recommends backward compatibility and decoupling changes for flexible deployments.                                                  |
|  18 | Rollout timing varies; higher risk changes are rolled out more slowly, with manual checkpoints.                                     |
|  19 | Deployment status visibility can be provided in CI/CD pipelines, showing rollout percentages and stages.                            |
|  20 | Encourages making deployment data visible to developers.                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-fhXEJD-ycs)