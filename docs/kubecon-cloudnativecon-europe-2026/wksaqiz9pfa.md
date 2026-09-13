---
type: Video Note
title: "Platform Engineering 2.0: Just-Enough Kubernetes and AI-Native DevOps - Shweta Vohra, Booking.com"
description: 'In this talk, Shuah, lead architect at Booking.com, explores the true meaning of platform engineering, emphasizing that the term "platform" is often misunderstood and misapplied across organizations. Drawing from personal experience, Shuah...'
resource: https://www.youtube.com/watch?v=WksAqIZ9PFA
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Shuah, lead architect at Booking.com, explores the true meaning of platform engineering, emphasizing that the term "platform" is often misunderstood and misapplied across organizations.
Drawing from personal experience, Shuah explains that a real platform is not merely a collection of tools but a system that provides stability, clear integration, and consistency, enabling users and developers to work more efficiently.
Using examples like Netflix and Linux, Shuah illustrates how successful platforms abstract complexity and deliver capabilities rather than just technology.
The talk introduces the "V arise" model, outlining five essential platform qualities: adaptability, repeatability, integrability, self-sufficiency, and ecosystem enablement.
Shuah contrasts platform engineering 1.0, which focused on scaling infrastructure and often led to increased complexity, with platform engineering 2.0, which centers on scaling capabilities, reducing cognitive load, and exposing only necessary infrastructure details to developers.
The session concludes with practical advice, a discussion of lean infrastructure using K3S clusters, and a reminder that not every organization needs a platform—only those with foundational needs that can simplify and empower their ecosystem.
# Main Points

|   # | Main point                                                                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Platform engineering is widely discussed, but definitions vary across organizations.                                                                                                                              |
|   2 | Simply calling something a platform does not make it function as one.                                                                                                                                             |
|   3 | Many organizations struggle with platforms that add complexity instead of simplifying.                                                                                                                            |
|   4 | True platforms provide stability, clear integration, and consistency.                                                                                                                                             |
|   5 | Examples of effective platforms: Netflix (enables creators and partners without exposing complexity), Linux (integrable, foundational, and widely adopted).                                                       |
|   6 | Platform engineering starts with a core business need, followed by platform strategy, business models, user experience, technology strategy, tool integration, design, architecture, development, and operations. |
|   7 | The V ARISE model defines five key platform parameters: adaptable, repeatable, integrable, self-sufficient, and ecosystem enabling.                                                                               |
|   8 | All five V ARISE parameters are necessary for a true platform.                                                                                                                                                    |
|   9 | Platform engineering 1.0 focused on standardizing infrastructure, often leading to increased complexity and overexposure to tools like Kubernetes.                                                                |
|  10 | In platform engineering 2.0, developers express intent, and the platform translates it into actions, exposing only necessary capabilities.                                                                        |
|  11 | Kubernetes should be an engine, not the user interface; "just enough Kubernetes" is the goal.                                                                                                                     |
|  12 | Exposure model levels: full control, templates, golden paths, automation/capabilities.                                                                                                                            |
|  13 | Platform engineering 2.0 architecture: developer expresses intent, platform control plane automates workflows, infrastructure engine delivers capabilities.                                                       |
|  14 | Lean infrastructure is achieved using K3S clusters ("cells") that are disposable and easily replaced.                                                                                                             |
|  15 | Ambient mesh replaces sidecar-heavy service mesh, reducing operational overhead.                                                                                                                                  |
|  16 | Gateway API enables intent-based routing and deployment.                                                                                                                                                          |
|  17 | Platform 2.0 focuses on scaling capabilities, not clusters, and closing the operational loop with automation.                                                                                                     |
|  18 | Not every organization needs a platform; only pursue if foundational value can be created.                                                                                                                        |
|  19 | Self-sufficiency means th                                                                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=WksAqIZ9PFA)