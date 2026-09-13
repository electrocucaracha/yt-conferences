---
type: Video Note
title: "Project Lightning Talk: Konveyor: Mining Developer Wisdom to Modernize Legacy Apps... Jonah Sussman"
description: "Jonah Susman introduces Conveyor, a tool designed to accelerate large-scale application migrations by addressing the challenges of legacy code, such as technical debt, security risks, maintenance costs, and skill gaps. He explains that trad..."
resource: https://www.youtube.com/watch?v=urPCD5uMFk0
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jonah Susman introduces Conveyor, a tool designed to accelerate large-scale application migrations by addressing the challenges of legacy code, such as technical debt, security risks, maintenance costs, and skill gaps.
He explains that traditional migrations are repetitive and inefficient, especially when dealing with numerous applications.
Conveyor streamlines the migration process by using static analysis rules written in plain English, which can be applied across multiple applications to flag issues and generate actionable reports through an operator UI.
The platform also features Conveyor AI (Kai), an AI-powered layer that helps plan and propose fixes, learns from developer feedback, and stores results to improve future migrations.
Overall, Conveyor aims to automate and expedite modernization efforts, and interested users can find more information on GitHub or connect via Kubernetes Slack.
# Main Points

|   # | Main point                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------ |
|   1 | Jonah Susman introduces Conveyor and its role in accelerating large-scale migrations.                              |
|   2 | Legacy code presents challenges: technical debt, security risks, higher maintenance costs, and skill gaps.         |
|   3 | Migrating individual applications is repetitive and inefficient, especially with many apps.                        |
|   4 | Conveyor analyzes migration experiences and identifies common patterns, forming a unified migration experience.    |
|   5 | Typical migration steps: surface information, analyze applications, make decisions, plan work, perform migration.  |
|   6 | Conveyor is designed to accelerate migrations for multiple applications.                                           |
|   7 | Core feature: static analysis rules written in YAML, flagging code issues across many applications.                |
|   8 | New rules created during migration are automatically applied to all relevant apps.                                 |
|   9 | Operator UI displays migration status and generates reports to aid decision-making.                                |
|  10 | Conveyor AI (Kai) is an AI-powered, vendor-neutral layer introduced to assist with planning and proposing fixes.   |
|  11 | Kai agents help with work planning and propose automated fixes, targeting later migration steps.                   |
|  12 | Agents are grounded by static tools; developers can accept or reject proposed fixes.                               |
|  13 | Kai stores agent outcomes as hints, enabling learning from previous acceptances or rejections.                     |
|  14 | The system accelerates migration by reusing solutions for similar issues across applications.                      |
|  15 | Conveyor components: static analysis rules, operator UI, and AI-generated fixes.                                   |
|  16 | Conveyor aims to automate repetitive migration tasks and multiply organizational knowledge.                        |
|  17 | Project is available on GitHub at github.com/conveyor.                                                             |
|  18 | Additional information and support available at kiosk 1A (Tuesday 10:45–3) and on Kubernetes Slack (conveyor dev). |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=urPCD5uMFk0)