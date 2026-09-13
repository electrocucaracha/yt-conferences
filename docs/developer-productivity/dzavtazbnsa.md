---
layout: default
title: Building HTTP API SDKs that Really Are a Kit • Darrel Miller • GOTO 2019
nav_order: 13
parent: Developer Productivity
type: Video Note
description:
  Darrell Miller, a Microsoft program manager, discusses building HTTP
  API SDKs, which he believes should be flexible enough to allow developers to pick
  and choose the parts they want to use. He argues that current SDKs are often inflexible
  a...
resource: https://www.youtube.com/watch?v=dzaVtAZBnsA
tags:
  - developer-productivity
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Darrell Miller, a Microsoft program manager, discusses building HTTP API SDKs, which he believes should be flexible enough to allow developers to pick and choose the parts they want to use.
He argues that current SDKs are often inflexible and limited, making it difficult for developers to build commercial products.
To address this, Darrell's team has developed a new approach to SDKs, including middleware, response handlers, and tasks, which provide more flexibility and choice for developers.
The goal is to create a "kit" that allows developers to build their own solutions without having to rebuild everything from scratch.
By making SDKs optional and providing choices, Darrell hopes to encourage usage and adoption of these kits.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | There are over 2000 APIs in the Microsoft Graph, serving 50 different service teams.                                                                 |
|   2 | The goal of building SDKs for the Microsoft Graph is to provide a kit that developers can use to build their own applications.                       |
|   3 | The current SDKs have limited flexibility and are designed primarily for a single use case.                                                          |
|   4 | To encourage usage, SDKs should be made more flexible and allow developers to pick and choose the parts they want to use.                            |
|   5 | Middleware is a key concept in building flexible SDKs, allowing developers to add cross-cutting concerns without modifying the underlying API.       |
|   6 | The Microsoft Graph team has developed a client factory that helps create native HTTP clients with middleware pre-configured.                        |
|   7 | Response handlers are used to encapsulate behavior for handling HTTP responses and can be customized for different scenarios.                        |
|   8 | Tasks are a way to abstract away common API patterns, allowing developers to achieve specific goals without writing custom code.                     |
|   9 | The Microsoft Graph team is working on making SDKs more accessible and flexible, with a focus on community engagement and feedback. Ratings (1-5): 2 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dzaVtAZBnsA)
