---
layout: default
title: "One Spec, Ten SDKs, Zero Excuses: Conformance Testing MCP - Paul Carleton, Anthropic"
nav_order: 87
parent: MCP Dev Summit NA 2026
type: Video Note
description: 'Paul, an MCP core maintainer at Anthropic, presented the development of a conformance test suite to address inconsistencies arising from the 567 "must" and "should" statements in the Model Context ...'
resource: "https://www.youtube.com/watch?v=-2zurQpsJzI"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Paul, an MCP core maintainer at Anthropic, presented the development of a conformance test suite to address inconsistencies arising from the 567 "must" and "should" statements in the Model Context Protocol specification.
He explained that divergent interpretations of these rules across the ten official SDKs and custom implementations lead to incompatibilities and significant maintenance burdens, such as the "bug whack-a-mole" effect when fixing issues in one language requires manual verification in others.
To solve this, the team built an SDK-agnostic conformance suite inspired by OpenID Foundation practices, featuring two harness modes that probe client and server implementations against specific scenarios to generate standardized pass/fail checks with direct references to the specification.
This suite has been integrated into an SDK tiering system, where Tier One status requires 100% conformance and rapid security triage, resulting in TypeScript, Python, C#, and Go currently achieving the highest tier.
The presentation concluded with a call to action for the community to improve coverage, noting that while the current suite covers about 100 statements, SEP 2484 proposes making conformance scenarios mandatory for all new specification changes to ensure consistent and correct adoption across the ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The MCP specification contains 567 must and should statements, creating significant opportunities for divergent interpretations and implementation inconsistencies across SDKs. |
|   2 | Divergent implementations lead to incompatibilities, bug reports, and wasted time, undermining the core benefit of a standardized protocol.                                     |
|   3 | A conformance test suite was developed to help SDKs converge on consistent implementations and reduce the burden of maintaining multiple SDKs.                                  |
|   4 | The suite is SDK-agnostic and designed with minimal dependencies, allowing it to test out-of-distribution behaviors that standard SDKs might not handle.                        |
|   5 | Two harness modes exist: one tests a server under test using a client, and the other tests a client under test using specific example servers.                                  |
|   6 | Each test scenario outputs checks with IDs, descriptions, statuses, timestamps, and references to specific specification sections for clarity.                                  |
|   7 | SDK maintainers are expected to implement everything servers and clients to run the suite in CI, preventing regressions and ensuring correct feature implementation.            |
|   8 | SEP authors are expected to write conformance scenarios alongside their specification proposals to clarify language and ensure faster, correct adoption.                        |
|   9 | Server and client operators benefit from increased confidence in SDK compatibility and fewer bugs without needing to build anything themselves.                                 |
|  10 | The conformance suite is purpose-built for SDKs and may not be suitable for testing random live servers, though some scenarios can be used as probes.                           |
|  11 | SDK tiering was introduced via SEP 1730 to enforce compatibility and set quality bars for maintenance, issue triage, and security response.                                     |
|  12 | Tier one requirements include 100% conformance on the latest tests, two-day issue triage, and seven-day P0 security bug triage.                                                 |
|  13 | Current results show TypeScript, Python, C#, and Go as tier one SDKs, with Java and Rust at tier two.                                                                           |
|  14 | Conformance testing has helped identify and fix security issues across the ecosystem, such as invalid issuer handling and DNS rebinding vulnerabilities.                        |
|  15 | The current suite covers approximately 100 of the 567 specification statements, with 266 remaining testable and 200 considered not testable.                                    |
|  16 | SEP 2484 proposes making it mandatory to accompany new specification changes with conformance scenarios or an explanation of why they cannot be tested.                         |
|  17 | The June specification release will be the first to apply the requirement for mandatory conformance scenarios.                                                                  |
|  18 | A new authorization server suite is in progress to test authorization servers in isolation, complementing existing client and server tests.                                     |
|  19 | AI tools are being used to generate test code and SDK pull requests, though human scrutiny is required to ensure scenario accuracy and avoid increasing CI costs.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-2zurQpsJzI/hqdefault.jpg)](https://www.youtube.com/watch?v=-2zurQpsJzI)

[Watch on YouTube](https://www.youtube.com/watch?v=-2zurQpsJzI)
