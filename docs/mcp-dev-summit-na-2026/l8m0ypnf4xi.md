---
layout: default
title: "From Cypher to Conversation: MCP at WestJet - Anton Lysov, WestJet"
nav_order: 28
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker describes how WestJet manages its complex flight scheduling,
  highlighting the challenges unique to the airline industry, such as cabotage rules,
  minimum connection times, and seasonal route availability. Traditionally, schedules...
resource: https://www.youtube.com/watch?v=l8m0YpNf4XI
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

The speaker describes how WestJet manages its complex flight scheduling, highlighting the challenges unique to the airline industry, such as cabotage rules, minimum connection times, and seasonal route availability.
Traditionally, schedules were managed with cumbersome spreadsheets and updated only twice a year, but WestJet now uses a schedule publication service that processes industry-standard SIM files, amenities data, and business rules to generate valid, routable origin-destination pairs.
This data is stored in a Neo4j graph database, which is powerful but requires knowledge of the Cypher query language, limiting access for non-technical staff.
To democratize access, WestJet implemented an MCP-based tool that allows users to ask questions in plain English and receive data-driven answers, enabling teams like scheduling and network planning to optimize connections without technical barriers.
The solution is currently used internally, with considerations for security and data validation ongoing, and leverages state-of-the-art language models to translate natural language queries into Cypher.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | WestJet uses a dedicated service team to manage flight schedules and gate information.                                                                   |
|   2 | Airline scheduling is more complex than bus scheduling, requiring a specialized team and a graph database.                                               |
|   3 | WestJet uses Neo4j as its graph database, with Cypher as the query language.                                                                             |
|   4 | The airline industry has a high failure rate; over 260 Canadian airlines have folded, and every discount airline since 2000 has failed.                  |
|   5 | WestJet started in 1996 with 3 aircraft, 225 employees, and 5 destinations; now has about 200 aircraft, 15,000+ employees, and 100+ destinations.        |
|   6 | WestJet is Canada’s second-largest airline and eighth in North America by frequency.                                                                     |
|   7 | The digital API team builds and maintains microservices for westjet.com, mobile apps, and internal systems, covering pricing, trip info, and scheduling. |
|   8 | The scheduling service powers features like valid origin-destination selection and flight amenities display.                                             |
|   9 | Only 35% of theoretical network routes are routable; 65% are eliminated by business rules.                                                               |
|  10 | Scheduling complexity arises from rules like cabotage, minimum connection times, security, and seasonality.                                              |
|  11 | Historically, schedules were managed with spreadsheets and updated twice a year.                                                                         |
|  12 | WestJet now uses a Schedule Publication Service (SPS) that processes SIM files, amenities data, MCT, and business rules to generate routable data.       |
|  13 | All schedule data is stored in Neo4j as a graph: airports as nodes, flights as edges, with properties for times, equipment, and rules.                   |
|  14 | Accessing this data required Cypher knowledge, which many business users lack.                                                                           |
|  15 | The mission was to democratize access to the flight network graph using MCP, allowing plain English queries.                                             |
|  16 | MCP is a production tool enabling non-technical users to query the network without Cypher.                                                               |
|  17 | The architecture includes a client, custom MCP proxy, Neo4j MCP server, and Kubernetes deployment.                                                       |
|  18 | The schedule optimization team uses the tool to maximize possible connections at airports.                                                               |
|  19 | The proxy layer handles authent                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=l8m0YpNf4XI)
