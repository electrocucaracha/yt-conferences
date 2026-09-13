---
layout: default
title: How Much Platform Is Enough Platform? - John Keates, Wehkamp Retail Group
nav_order: 142
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  John, a platform engineer at the VA retail group, shares the company's
  journey in building and evolving their internal software platform to support efficient
  development and operations. He explains that the group, similar to a smaller Targe...
resource: https://www.youtube.com/watch?v=aLx3QlKE6Dc
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

John, a platform engineer at the VA retail group, shares the company's journey in building and evolving their internal software platform to support efficient development and operations.
He explains that the group, similar to a smaller Target in the Netherlands, needed a platform to reduce cognitive load for developers and streamline processes, moving from a fragmented, siloed stack to a more unified, automated system.
Attempts to implement comprehensive solutions like Backstage proved too complex for their team size, leading them to adopt simpler, self-service tools based on templating and automation, which now handle the majority of their needs.
While these solutions lack some advanced features and require ongoing maintenance, they have significantly improved developer experience and release cadence, allowing engineers to focus on building and improving products.
John concludes that while the ideal platform remains aspirational, incremental improvements and right-sized solutions have delivered substantial benefits, and new challenges will always emerge as the organization grows.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | John works at VA retail group in platform engineering and does consulting and community/open source work.                             |
|   2 | VA retail group is a Dutch retailer similar to Target but smaller, with its own logistics, app, site, and supporting software.        |
|   3 | Platform engineering is about building software to help other software, reducing cognitive load for developers.                       |
|   4 | Platforms should be sized appropriately; too little or too much is problematic.                                                       |
|   5 | Historically, VA had siloed teams managing separate stacks, leading to communication issues and high cognitive load.                  |
|   6 | Pre-devops era involved many handoffs, inconsistent documentation, and local optimizations that didn’t help the broader business.     |
|   7 | Marketing department pushed for faster release cycles, leading to adoption of containers and cloud, creating a new IT department.     |
|   8 | Release cadence improved from three times a year to multiple times a day.                                                             |
|   9 | Internal platform now allows developers to write, test, and deploy code without leaving their IDE.                                    |
|  10 | Platform uses CNCF projects like Kubernetes and Argo; developers don’t need deep infrastructure knowledge.                            |
|  11 | Automation and self-service are key; most applications use simple provisioning via Slack and templated YAML.                          |
|  12 | Attempted to implement Backstage as an internal developer portal multiple times, but it was too heavy for the team size and skillset. |
|  13 | Backstage’s collaborative features didn’t fit VA’s small teams; maintaining it was unsustainable.                                     |
|  14 | Simpler internal tools using string templating and Slack-based provisioning proved more effective.                                    |
|  15 | Most software uses standard tools (e.g., Postgres, Kafka, Argo) and templated configurations.                                         |
|  16 | Manual customization is possible via pull requests, with bots automating reviews and deployments.                                     |
|  17 | Documentation and debugging are handled via simple internal tools, not a unified portal.                                              |
|  18 | Backstage was archived, but the concept of platform engineering and golden paths remains valuable.                                    |
|  19 | There’s always a new bottleneck to solve, even as previous                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aLx3QlKE6Dc)
