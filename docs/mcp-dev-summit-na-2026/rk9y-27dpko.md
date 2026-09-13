---
type: Video Note
title: "Combine Skills and MCP To Close the Context Gap - Pedro Rodrigues, Supabase"
description: "Pedro, an AI tooling engineer at Superbase, delivered a talk at the MCP Dev Summit addressing the ongoing debate between MCP (an integration protocol with tools, resources, and prompts) and skills (folders containing instructions, scripts..."
resource: https://www.youtube.com/watch?v=Rk9y-27dpko
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Pedro, an AI tooling engineer at Superbase, delivered a talk at the MCP Dev Summit addressing the ongoing debate between MCP (an integration protocol with tools, resources, and prompts) and skills (folders containing instructions, scripts, and resources).
He clarified that MCP and skills serve different purposes: MCP focuses on integrating agents with services, while skills help manage context and guide agents through progressive disclosure of information.
Using Superbase as a case study, Pedro demonstrated that combining MCP with skills leads to more robust and secure agent behavior, particularly by incentivizing agents to consult up-to-date documentation and implement best practices, such as security features.
Benchmarking showed that agents using both MCP and skills outperformed those using either alone, though at the cost of more steps and token usage.
Pedro concluded that the main challenge is context management rather than tool capability, and encouraged further discussion on efficient skill distribution within the ecosystem.
# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Majority of audience familiar with Superbase; Superbase gear available                                                                                            |
|   2 | Presentation built as a NextJS app, not Google Slides                                                                                                             |
|   3 | Speaker: Pedro, AI tooling engineer at Superbase, co-founder of Lisbon AI Week, second-time MCP Dev Summit speaker                                                |
|   4 | MCP (Multi-agent Communication Protocol) is an integration protocol with three primitives: tools (actions), resources (context), and prompts (templates)          |
|   5 | MCP features: OAuth, multiple transports, sampling, elicitation                                                                                                   |
|   6 | Skills are folders containing instructions, scripts, and resources; skill.md is the main file, can reference scripts and assets                                   |
|   7 | Skills load only necessary context; agent loads skill name/description first, then instructions if relevant                                                       |
|   8 | Tools (MCP) vs Scripts (Skills):                                                                                                                                  |
|   9 | Tools: typed arguments, isolated, no credential access, remote execution, schema bloat possible                                                                   |
|  10 | Scripts: no schema, instant iteration, agent can author, needs shell access, portability issues                                                                   |
|  11 | Resources (MCP) vs References (Skills):                                                                                                                           |
|  12 | Resources: app-driven, standardized, remote access, dynamic content, underused                                                                                    |
|  13 | References: agent-friendly, offline, agent can author, no structure                                                                                               |
|  14 | Prompts (MCP) vs skill.md:                                                                                                                                        |
|  15 | Prompts: underused, user-invoked, static                                                                                                                          |
|  16 | skill.md: agent-invoked, rich content, conditional logic, multiple workflows                                                                                      |
|  17 | MCP solves integration; Skills solve context saturation via progressive disclosure                                                                                |
|  18 | MCP = pilot, Skills = co-pilot; both needed, not competitors                                                                                                      |
|  19 | Superbase exposes MCP server with 20+ tools; developing Superbase-specific skill to guide agents, incentivize doc search, enforce security, and provide workflows |
|  20 | Experiment: Agent with only MCP ignored doc search, created insecure Postgres view; with skill, agent searched docs, used security flag, produced secure solution |
|  21 | Benchmarks: MCP + skill outperformed others for Superbase/Postgres tasks; more turns/tokens but better results                                                    |
|  22 | Key learnings: MCP alone insufficient; agents default to training data; skills guide agents to up-to-date docs and                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Rk9y-27dpko)