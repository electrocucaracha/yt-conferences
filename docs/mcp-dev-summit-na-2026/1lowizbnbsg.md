---
layout: default
title:
  "From 60 Minutes To 60 Seconds: Production MCP Workflows for Healthcare Billing
  - Andrew Espira"
nav_order: 25
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Andre Spira, co-founder of Custod, discusses the challenges in healthcare
  billing, emphasizing that the main issue is not data availability but the lack of
  an orchestration layer to streamline information for billers and providers. He expla...
resource: https://www.youtube.com/watch?v=1lOWizbNBSg
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Andre Spira, co-founder of Custod, discusses the challenges in healthcare billing, emphasizing that the main issue is not data availability but the lack of an orchestration layer to streamline information for billers and providers.
He explains that medical billers face inefficiencies due to scattered data and complex payer rules, leading to frequent claim denials and lengthy appeals.
Custod’s RCM platform addresses these problems by building a knowledge layer and using APIs and agents to aggregate and deliver relevant billing information in a single prompt, reducing manual effort and errors.
The system includes security layers and agent orchestration to ensure data privacy and accurate tool selection, with mechanisms for human review and feedback loops to improve model performance.
Spira also highlights ongoing efforts to enhance security, integrate payer rules, and open source their protocols to benefit the broader community.

# Main Points

|   # | Main point                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------- |
|   1 | Healthcare billing faces a 60-minute problem due to lack of an orchestration layer for data integration.          |
|   2 | Medical billers struggle with multiple tabs, PDFs, and code lookups for claims.                                   |
|   3 | Claim rejections require billers to research error codes and reasons.                                             |
|   4 | Custod is an RCM platform building a knowledge layer (RCI) for healthcare data.                                   |
|   5 | The platform uses AI and machine learning for claim lifecycle management, risk assessment, and denial prediction. |
|   6 | Insurers act as gatekeepers, making it difficult for providers to access necessary billing information.           |
|   7 | Eligibility checks, prior authorization, and coding are manual and time-consuming.                                |
|   8 | Claim denials can take 45-50 days to appeal, often due to small errors.                                           |
|   9 | Insurers use models to detect errors and increase claim denials.                                                  |
|  10 | Custod aims to provide billers with integrated information via a single click.                                    |
|  11 | The platform uses APIs to pull data from CMS and other sources, consolidating payer rules hidden in PDFs.         |
|  12 | MCPS APIs allow billers to retrieve correct codes and modifiers efficiently.                                      |
|  13 | Agents synthesize data, match codes, and retrieve information without making predictions.                         |
|  14 | Agents are used for tool selection and data retrieval, not for user feedback or reasoning.                        |
|  15 | Integration of MCPS into workflows and multi-tenant architecture are key challenges.                              |
|  16 | Agents should not access PHI; guardrails and validation are implemented to prevent unauthorized access.           |
|  17 | Agents can attempt to bypass guardrails as they learn more context.                                               |
|  18 | A reasoning layer tracks agent decisions and tool usage.                                                          |
|  19 | The workflow includes a security layer, agent orchestrator, and Sentinel (governing agent).                       |
|  20 | Security layer analyzes prompts and blocks unauthorized data requests.                                            |
|  21 | Sentinel flags cases for human review when necessary.                                                             |
|  22 | Audit trails and metrics monitor agent actions and confidence levels.                                             |
|  23 | Machine learning thresholds determine if agent responses are acceptable.                                          |
|  24 | Feedback loops improve agent performance over time.                                                               |
|  25 | Web craw Ratings (1-5): 3                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1lOWizbNBSg)
