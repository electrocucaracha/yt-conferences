---
type: Video Note
title: "Mission Abort: Intercepting Dangerous Deletes Before Helm Hits Apply - Payal Godhani, Oracle"
description: 'P Gdani from Oracle Cloud Infrastructure discusses the importance of safeguarding Kubernetes resources and preventing "7-2" incidents in production. He shares a personal experience where a Helm deployment accidentally deleted 18 load balanc...'
resource: https://www.youtube.com/watch?v=9-IJHdVNgO4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

P Gdani from Oracle Cloud Infrastructure discusses the importance of safeguarding Kubernetes resources and preventing "7-2" incidents in production.
He shares a personal experience where a Helm deployment accidentally deleted 18 load balancers, causing significant business impact.
To address this issue, Oracle developed a framework called Helmiff, which runs during planning time to visualize changes and prevent potential disruptions.
The framework uses three-way helm diff to capture live state information and provides a risk assessment tool to identify critical resources that need attention.
By adopting this framework, Oracle has seen a significant decrease in 7-2 incidents and restored confidence among SRRES executing deployments.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9-IJHdVNgO4)