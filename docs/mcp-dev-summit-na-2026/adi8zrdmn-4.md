---
type: Video Note
title: "Threat Modeling Authorization in MCP - Sarah Cecchetti, OpenID Foundation"
description: 'The speaker, Sarah Jetty, discusses threat modeling and authorization challenges in Multi-Component Protocols (MCP), using "The Cat in the Hat Comes Back" as a metaphor for sub-agent delegation and the risks of unattenuated permissions. She...'
resource: https://www.youtube.com/watch?v=ADI8zrdmN_4
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, Sarah Jetty, discusses threat modeling and authorization challenges in Multi-Component Protocols (MCP), using "The Cat in the Hat Comes Back" as a metaphor for sub-agent delegation and the risks of unattenuated permissions.
She outlines four key attacks: silent tool injection, malicious elicitation, uncontrolled delegation, and sampling exfiltration, each illustrating vulnerabilities where MCP servers or sub-agents can gain excessive or unintended access.
To address these, she recommends making MCP a one-way flow to prevent data exfiltration, implementing signed server metadata to prevent unauthorized tool changes, requiring fine-grained authorization details for sub-agents, and adding an escalation response for tools when permissions are insufficient.
The talk emphasizes the need for cryptographically verifiable credentials and selective disclosure to strengthen trust and control in agent interactions, and encourages participation in the OpenID Foundation’s AI identity management group for further collaboration and improvement.
# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Topic: Threat modeling in authorization for MCP (Multi-Agent Control Plane)                                                  |
|   2 | Literature review found earliest metaphor for sub-agent spawning in "The Cat in the Hat Comes Back" (1958)                   |
|   3 | Metaphor: Cat spawns sub-agents without attenuated permissions, leading to chaos                                             |
|   4 | Three contributors: Sarah Jetty, AI Management Community Group, research assistant Claudrey Hepern (OpenClaw implementation) |
|   5 | Four main attacks discussed:                                                                                                 |
|   6 | Silent tool injection: MCP server silently updates tools, gaining new permissions without user awareness or consent          |
|   7 | Malicious elicitation: Malicious MCP server elicits sensitive information from users, exploiting trust in LLMs               |
|   8 | Uncontrolled delegation: Sub-agents inherit full permissions, leading to over-permissioning and lack of context              |
|   9 | Sampling exfiltration: Data flows from LLM/human/session to MCP server, enabling sensitive data exfiltration                 |
|  10 | Recommendations:                                                                                                             |
|  11 | Make OAUTH and MCP a one-way street; remove sampling and elicitation from spec                                               |
|  12 | Require signed server metadata to pin tool definitions and versions, enabling consent for changes                            |
|  13 | Enable fine-grained policies and attenuated permissions for sub-agents using authorization details                           |
|  14 | Add an "escalate" response in addition to allow/deny for tools, enabling orchestrating agent to replan permissions           |
|  15 | Summary of attack mitigations:                                                                                               |
|  16 | Silent tool injection: solved by signed server metadata                                                                      |
|  17 | Malicious elicitation: solved by enforcing one-way flow                                                                      |
|  18 | Uncontrolled delegation: solved by authorization details and escalation                                                      |
|  19 | Chat history exfiltration: solved by one-way flow                                                                            |
|  20 | Actions for audience:                                                                                                        |
|  21 | Join OpenID Foundation AI Identity Management Community Group                                                                |
|  22 | Experiment with Cedar, OPA, Zanzibar, Opus 4.6 for policy modeling                                                           |
|  23 | Read "Solving the Bottom Turtle" for cryptographic identity philosophy                                                       |
|  24 | Discussion on verifiable credentials and selective disclosure for agent and server authentication                            |
|  25 | Suggestion for third-party attestation of server metadata (no                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ADI8zrdmN_4)