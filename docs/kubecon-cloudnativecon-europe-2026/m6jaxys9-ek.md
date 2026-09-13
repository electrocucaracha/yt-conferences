---
layout: default
title:
  Enterprise-Scale Migrations Using Agentic Workflows with Human-in... Alvaro
  Saurin & Jose M Navarro
nav_order: 103
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Albert Saurin and Jose Manuel Navaro, senior software engineers at Adobe,
  described their team's complex migration of an API gateway from an older engineext
  and Lua-based system to a modern stack using Envoy and Argo CD. The migration invol...
resource: https://www.youtube.com/watch?v=m6jAXyS9_Ek
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

Albert Saurin and Jose Manuel Navaro, senior software engineers at Adobe, described their team's complex migration of an API gateway from an older engineext and Lua-based system to a modern stack using Envoy and Argo CD.
The migration involved over 2,600 services across 500+ clusters, handling massive traffic volumes, and required a transparent, failure-free process for users.
To address the scale and complexity, they developed a semi-autonomous workflow using coding agents and custom LLM-based agents: coding agents generated deterministic translation tools for configuration files, while custom agents managed verification, DNS cutover, and monitoring, invoking human engineers only when necessary.
This approach allowed parallel migrations, reduced manual intervention, and ensured reliability by using golden files for regression checks and strict security controls.
The team found that LLMs excelled at generating code but struggled with direct configuration translation, and that agentic workflows enabled efficient, large-scale migrations with minimal downtime and oversight.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Albert Saurin and Jose Manuel Navaro are senior software engineers in Adobe's gateway team.                                                                  |
|   2 | The team is migrating an API gateway from engineext (with Lua) to Envoy and Argo CD.                                                                         |
|   3 | The API gateway handles authentication, authorization, routing, throttling, analytics, and routes traffic to Kubernetes services.                            |
|   4 | Migration involves 2600 services across 500+ clusters, each with multiple environments.                                                                      |
|   5 | Goals: migration must be transparent to users, require no config changes, and have zero downtime.                                                            |
|   6 | Old gateway managed 13 petabytes/month and 40 billion requests/day.                                                                                          |
|   7 | Manual migration of 80% of traffic would take 4.5 to 15 years; automation is necessary.                                                                      |
|   8 | Solution: autonomous migration with engineers involved only when needed.                                                                                     |
|   9 | Migration stages: translate old config, deploy new config, verify service, progressively cut over traffic, deprecate old config.                             |
|  10 | LLMs struggled with direct config translation due to schema differences and non-determinism.                                                                 |
|  11 | Switched to using LLMs to generate deterministic translation code, refined by engineers.                                                                     |
|  12 | Translation process uses logs and golden files to ensure no regressions.                                                                                     |
|  13 | Pros: visibility, parallelization, measurable progress; Cons: corner cases require manual intervention.                                                      |
|  14 | Custom agents automate verification and DNS cutover steps.                                                                                                   |
|  15 | Agents discover endpoints, send HTTP requests, check status, and monitor metrics.                                                                            |
|  16 | DNS traffic split is gradually shifted to the new gateway; agents monitor error rates and roll back if issues arise.                                         |
|  17 | Custom agents built with lang graph framework, using LLMs, tools, and guardrails.                                                                            |
|  18 | Agents interact with Splunk, GitHub, Kubernetes, Argo CD, and Slack.                                                                                         |
|  19 | Engineers approve rollbacks or continuation based on agent recommendations.                                                                                  |
|  20 | Lessons learned: LLMs excel at code generation, not niche tasks; code provides determinism; agents save engineers’ time by handling monitoring and rollouts. |
|  21 | Hundreds of migrations can run in parallel; engineers are only involved in ~10% of cases.                                                                    |
|  22 | Migration tran                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=m6jAXyS9_Ek)
