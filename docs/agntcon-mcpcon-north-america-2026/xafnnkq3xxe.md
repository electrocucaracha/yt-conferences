---
layout: default
title: "From AI Assistants to Trusted SDLC Agents: FINRA’s Agentic... - Geetha Ramachandran, FINRA"
nav_order: 47
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Geetha Ramachandran, who leads cloud and platform engineering at FINRA, presents a case study on expanding AI capabilities beyond simple code assistance to address the broader Software Development ..."
resource: "https://www.youtube.com/watch?v=xaFnnKq3xxE"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Geetha Ramachandran, who leads cloud and platform engineering at FINRA, presents a case study on expanding AI capabilities beyond simple code assistance to address the broader Software Development lifecycle (SDLC).
Recognizing that FINRA processes massive volumes of market data and oversees thousands of securities firms, the organization sought to use AI agents to handle testing, upgrades, and production maintenance, thereby freeing up engineering capacity for mission-critical business value.
The team implemented a multi-layered architecture comprising a commodity coding agent, a prototype collaboration platform that reduced ideation time from weeks to days, and a robust agent platform featuring standardized MCP servers, a skills registry, and secure runtime environments with explicit agent identities.
To ensure trust and safety in this regulatory environment, FINRA deployed purpose-built SDLC agents for specific tasks like mutation-based test generation and dependency upgrades, all governed by strict guardrails, scoped permissions, and complete telemetry traces that allow humans to verify results before merging.
Adoption was driven through structured initiatives such as "Vibathons" for prototyping and monthly workshops for maintenance, resulting in over 1,400 active users, 634 completed software upgrades, and the generation of more than 50,000 unit tests.
Key lessons learned include the importance of using deterministic tools for verifiable steps, continuously monitoring agent behavior to refine instructions, and ensuring that underlying processes are robust before introducing AI.
Looking ahead, FINRA plans to enhance agent context, implement centralized policy controls, and establish an enterprise-wide AI SDLC camp to standardize these new ways of working.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                        |
|   2 | • FINRA's mission is to protect investors and market integrity by enforcing rules and detecting irregularities in financial markets                 |
|   3 | • FINRA processes up to 1.45 trillion market events daily and manages over 500 petabytes of stored data                                             |
|   4 | • FINRA supervises 630,000 broker-dealers across 3,200 securities firms                                                                             |
|   5 | • Initial AI implementation focused on code assistance in IDE; expanded to full SDLC                                                                |
|   6 | • 1,410 monthly users of AI agents; 6 SDLC agents in production; 634 software updates completed (~66% of tracked progress                           |
|   7 | • Created prototype collaboration platform: ~400 prototypes developed; reduced prototyping time from weeks to days                                  |
|   8 | • Implemented standardized MCP servers providing coherent interface across SDLC tools                                                               |
|   9 | • AI App Store enables users to discover, download and install approved AI tools and solutions                                                      |
|  10 | • Agent identity treated as explicit construct; access can be revoked when necessary                                                                |
|  11 | • Test generation agents use mutation testing approach to generate effective unit tests                                                             |
|  12 | • Dependency and runtime update agents maintain software currency in production                                                                     |
|  13 | • Agents generate pull requests; humans remain in outer loop for verification and merge decisions                                                   |
|  14 | • Three trust requirements: know where agents can reach, see complete telemetry of execution, know who decides after agent completes                |
|  15 | • Implemented Vibathons (24-hour hackathons), skills campaign, and monthly Transformathons for adoption                                             |
|  16 | • DORA scores improved across four indicators; 25 teams reported 1,800 recovered engineering hours                                                  |
|  17 | • Developer perception of SDLC agents improved over 75%                                                                                             |
|  18 | • Key lessons: use deterministic tools for deterministic tasks; observe agent execution; ensure adequate process verification before placing agents |
|  19 | • Future direction: provide agents more knowledge/context; implement centralized policies; refine golden skills set; create AI SDLC training ground |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xaFnnKq3xxE/hqdefault.jpg)](https://www.youtube.com/watch?v=xaFnnKq3xxE)

[Watch on YouTube](https://www.youtube.com/watch?v=xaFnnKq3xxE)
