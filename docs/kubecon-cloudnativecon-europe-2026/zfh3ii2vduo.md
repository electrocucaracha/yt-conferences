---
layout: default
title:
  "Hack Me If You Can: Learning Kubernetes Security Through a Role-P... Aoi Takahashi
  & Keita Mochizuki"
nav_order: 135
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this roleplay-based presentation, Ai Takahashasi and Ka Mosuki introduce
  Kubernetes security concepts by simulating an attack and defense scenario. Ai, acting
  as an engineer, uses AI tools to rapidly build and deploy an e-commerce applic...
resource: https://www.youtube.com/watch?v=zFH3II2vdUo
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

In this roleplay-based presentation, Ai Takahashasi and Ka Mosuki introduce Kubernetes security concepts by simulating an attack and defense scenario.
Ai, acting as an engineer, uses AI tools to rapidly build and deploy an e-commerce application on Kubernetes, but overlooks security best practices, resulting in vulnerabilities in the container image and manifest.
A hacker character exploits a critical vulnerability in the application, gaining root access and escalating privileges due to insecure container configurations, such as running as a privileged container with host PID enabled.
The hero, Moi, then explains how to mitigate such risks by scanning for vulnerabilities, minimizing container image size, using secure manifest settings, and employing tools like admission controllers and policy-based controls.
The presenters emphasize the importance of not blindly trusting AI-generated code, regularly scanning for vulnerabilities, and leveraging both traditional and AI-powered security tools to maintain a secure Kubernetes environment.

# Main Points

|   # | Main point                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session is about learning Kubernetes security through a roleplay battle.                                                            |
|   2 | Presenters: Ai Takahashasi (SRE, Kubernetes doc contributor, author) and Ka Mosuki (software engineer, Kubernetes contributor, author). |
|   3 | Target audience: People familiar with Kubernetes basics and beginners in Kubernetes/container security.                                 |
|   4 | Presentation structure: Three chapters, three characters (Engineer, Hacker, Hero).                                                      |
|   5 | Disclaimer: Do not use AI for malicious attacks.                                                                                        |
|   6 | Engineer uses AI to build and deploy an e-commerce web application on Kubernetes.                                                       |
|   7 | AI generates code, builds container image, pushes to registry, and deploys to Kubernetes.                                               |
|   8 | Engineer merges code without reviewing, trusting AI output.                                                                             |
|   9 | Application architecture: Pods deployed on nodes, exposed via service.                                                                  |
|  10 | Hacker uses AI to investigate the web service, identifies Next.js and React technologies.                                               |
|  11 | AI finds a critical vulnerability (CVE-2025501 and 2) in Next.js and React server components.                                           |
|  12 | Hacker uses AI to create a Python tool to exploit the vulnerability, achieving remote code execution in the container.                  |
|  13 | Hacker discovers the container runs as privileged and as root, allowing node-level attacks.                                             |
|  14 | Hacker executes shutdown command on the node from the container.                                                                        |
|  15 | Attack steps: Exploit vulnerability for RCE in container, escalate to node, perform sensitive operations.                               |
|  16 | Hero explains security issues: vulnerabilities in container image, large attack surface, excessive privileges.                          |
|  17 | AI-generated code can introduce vulnerabilities; do not blindly trust AI output.                                                        |
|  18 | Recommendations: Detect/remove vulnerabilities, keep container images small, use minimal base images and multi-stage builds.            |
|  19 | Use container scanning tools (e.g., Trivy, Kubescape) to detect vulnerabilities and misconfigurations.                                  |
|  20 | Large images increase attack surface; minimal images reduce risk.                                                                       |
|  21 | Use kata debug for inspecting minimal containers.                                                                                       |
|  22 | Container isolation can be weakened by settings like hostPID and privileged: true.                                                      |
|  23 | Avoid unnecessary                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zFH3II2vdUo)
