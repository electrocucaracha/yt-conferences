---
layout: default
title:
  "Keynote: The Future of Cloud Native Is… Agentic - Lin Sun, Head of Open Source,
  Solo.io"
nav_order: 185
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker recounts their experiences attending Cube Con, highlighting
  the rapid growth and increasing complexity of the cloud native ecosystem. They discuss
  the challenges users face in navigating numerous tools and technologies, and expr...
resource: https://www.youtube.com/watch?v=ttGYcUFCok0
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

The speaker recounts their experiences attending Cube Con, highlighting the rapid growth and increasing complexity of the cloud native ecosystem.
They discuss the challenges users face in navigating numerous tools and technologies, and express a desire to make the ecosystem more accessible as it scales to even more users.
Demonstrating the potential of agentic AI, the speaker presents a live demo involving Argo CD, MCP servers, and AI agents to automate application deployment and configuration within Kubernetes, despite encountering network issues.
The presentation also includes an attempt to fly a drone and capture audience engagement using AI, showcasing both successes and technical hiccups.
Concluding, the speaker emphasizes the importance of building and sharing more AI agents and skills openly to drive the future of cloud native technology.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | First CubeCon attended in Seattle 2016, first organized by CNCF                                                                                                        |
|   2 | Initial confusion about Kubernetes concepts like pods, declarative YAML, and Helm                                                                                      |
|   3 | As part of the TOC, surveyed cloud native community leaders and users about pain points                                                                                |
|   4 | Main pain point identified: complexity of the cloud native ecosystem                                                                                                   |
|   5 | Noted impressive growth: cloud native users scaled from 0 to 10 million in under 10 years                                                                              |
|   6 | Questioned how to reach the next 10 million users faster and with less complexity                                                                                      |
|   7 | Belief that agentic AI will play a major role in the future of cloud native                                                                                            |
|   8 | Demonstrated MCP server configuration with Argo CD and GitHub MCP servers running in Kubernetes                                                                        |
|   9 | Showed AI agent exposed as MCP server                                                                                                                                  |
|  10 | Demoed creating an Argo CD application called "demo" using Argo CD MCP server                                                                                          |
|  11 | Encountered and resolved network issues during the demo                                                                                                                |
|  12 | Successfully deployed the demo application with frontend, backend, and dedicated gateway                                                                               |
|  13 | Used AI agent to create an HTTP route from agent gateway proxy to frontend service                                                                                     |
|  14 | AI agent created a pull request (PR) for the HTTP route; audience reviewed and approved the PR                                                                         |
|  15 | Synced the new PR into the cluster using Argo; application running successfully                                                                                        |
|  16 | Attempted to fly a drone on stage and connect to its Wi-Fi; faced network challenges                                                                                   |
|  17 | Managed to fly the drone but camera stream did not work; switched to backup plan using phone camera                                                                    |
|  18 | Captured audience engagement photos and compared them with AI                                                                                                          |
|  19 | Application architecture included frontend through agent gateway, Argo, GitHub, secured with mutual TLS, using SPIFFE and Istio service mesh with ambient (no sidecar) |
|  20 | Showcased Argo CD, MCP server, K agent as MCP server, agent gateway as MCP gateway, and agent scale for HTTP route creation                                            |
|  21 | Encouraged building more MCP servers, AI agents, and skills, and sharing them openly to advance cloud native                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ttGYcUFCok0)
