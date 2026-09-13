---
type: Video Note
title: 'Capabilities, APIs, and Experiences: Blueprints To Bu... Kyle Penfound & Mauricio "Salaboy" Salatino'
description: "In this talk, Kyle discusses the challenges and strategies involved in building modular, interoperable platforms, particularly in the context of Kubernetes and the broader cloud-native ecosystem. He emphasizes that while the Kubernetes API..."
resource: https://www.youtube.com/watch?v=tvgMu1yTo20
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Kyle discusses the challenges and strategies involved in building modular, interoperable platforms, particularly in the context of Kubernetes and the broader cloud-native ecosystem.
He emphasizes that while the Kubernetes API has enabled a vast ecosystem of tools, the lack of unified interfaces and interoperability between these tools makes platform building complex and risky.
Kyle introduces the concept of thinking about platforms as "sandwiches"—where components can be easily swapped or modified—rather than "soups," where everything is mixed together and hard to change.
He highlights the importance of focusing on capabilities rather than specific tools, advocating for the use of common interfaces within categories of platform components to enable flexibility and easier upgrades.
Kyle demonstrates these ideas with a demo using Dagger and references the Kenoi project, which provides reference architectures and an IDP builder for modular platform construction, concluding that standard APIs and modular design lead to healthier, more adaptable platforms.
# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focuses on building interoperable, modular platforms using capabilities, APIs, and experiences.                                      |
|   2 | Modular platforms allow easier management, replacement, and upgrading of components.                                                            |
|   3 | Kubernetes has unified cloud infrastructure APIs, enabling a vast ecosystem of tools.                                                           |
|   4 | The current landscape is overwhelming; choosing the right tools is challenging and risky.                                                       |
|   5 | Main challenges in building modular platforms:                                                                                                  |
|   6 | Tools lack unified management interfaces.                                                                                                       |
|   7 | Tools are not interoperable; swapping components is difficult.                                                                                  |
|   8 | Abstractions are leaky, making replacement and integration hard.                                                                                |
|   9 | These challenges reduce iteration speed and make platform maintenance complex.                                                                  |
|  10 | Analogy: Platforms should be like sandwiches (components easily swapped) rather than soups (components hard to separate).                       |
|  11 | Platform users need capabilities, not specific tools.                                                                                           |
|  12 | Platform builders should focus on providing capabilities via tools, allowing tool replacement as long as capabilities remain.                   |
|  13 | Tools expose inconsistent APIs, complicating integration.                                                                                       |
|  14 | The platform experience is defined by the collection of capabilities provided.                                                                  |
|  15 | Unified interfaces for tool categories enable modularity and easier component swapping.                                                         |
|  16 | Reference to the CNOE (Kenui) project, which provides reference architectures for modular internal developer platforms based on capabilities.   |
|  17 | Kenui maps capabilities to tools and evaluates best practices and technology choices.                                                           |
|  18 | Demo using Dagger to build a platform builder that wraps tools with a common interface for management (install, uninstall, configure, upgrade). |
|  19 | Emphasis on abstraction layers to manage diverse tools through a unified interface.                                                             |
|  20 | Standard APIs within tool categories lead to a healthier, more compatible ecosystem.                                                            |
|  21 | Encouragement to build platforms as sandwiches (modular, swappable components).                                                                 |
|  22 | Kenui’s IDP builder is a production-ready implementation of these concepts.                                                                     |
|  23 | Final points: focus on capabilities, use standard APIs, and                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tvgMu1yTo20)