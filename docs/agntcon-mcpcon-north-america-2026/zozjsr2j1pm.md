---
layout: default
title: "Configured for Autonomy: Making Enterprise Agents Useful and Safe at Scale- V. Bhalodia & C. Silver"
nav_order: 142
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Casey and Vyas from OpenAI’s agent security team present a defense-in-depth strategy for securing internal agent deployments, emphasizing that agents must be constrained to prevent the "lethal trif...'
resource: "https://www.youtube.com/watch?v=Zozjsr2j1pM"
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

Casey and Vyas from OpenAI’s agent security team present a defense-in-depth strategy for securing internal agent deployments, emphasizing that agents must be constrained to prevent the "lethal trifecta" of accessing sensitive data, communicating externally, and consuming untrusted content.
They detail the use of sandboxes as a foundational layer that controls file system, network, and process execution, alongside credential management techniques that use placeholders and proxies to ensure models never see plain-text secrets.
To manage user attention, they introduce an LLM reviewer that acts as a non-deterministic control layer, filtering benign permission prompts and only escalating high-risk actions to humans, thereby reducing alert fatigue while maintaining security.
The discussion further covers the challenges of authorization and identity, advocating for narrow-scoped service accounts over broad delegated access, and highlighting the need for source systems to distinguish between human and agent actions for better audit logging and granular control.
Finally, they address the critical importance of monitoring and log correlation at scale, utilizing agentic reviewers for tiered triage and deterministic rules to halt malicious behavior, ensuring that human intervention is reserved for the most critical security incidents.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : The OpenAI Agent Security team secures internal agent deployments, designs security primitives, and advises customers on agent deployment.                                                        |
|   2 | : Frontier labs must write and deploy code rapidly while maintaining safety, requiring robust security primitives for agent harnesses.                                                              |
|   3 | : Unsafe agent behavior occurs when three conditions are met: access to sensitive data, ability to communicate externally, and consumption of untrusted content (e.g., prompt injection via email). |
|   4 | : Relying on a single control is insufficient; a layered approach is required to protect agents that need all three trifecta conditions for utility.                                                |
|   5 | : Sandboxes are the foundation of defense, controlling three key areas:                                                                                                                             |
|   6 | : Restricting read/write access to specific directories.                                                                                                                                            |
|   7 | : Using allow/deny lists to restrict domain access (e.g., internal domains only).                                                                                                                   |
|   8 | : Controlling executable commands.                                                                                                                                                                  |
|   9 | :                                                                                                                                                                                                   |
|  10 | : Ensure models never see credentials in plain text to prevent leakage via tool calls, logs, or memory.                                                                                             |
|  11 | : Use placeholders in agent requests. A sandbox proxy validates the request against policy and replaces the placeholder with the real credential only if the domain is authorized.                  |
|  12 | : Routine permission prompts lead to users blindly clicking "yes" or disabling sandboxes.                                                                                                           |
|  13 | :                                                                                                                                                                                                   |
|  14 | : An LLM-based reviewer acts as a non-deterministic control layer to filter benign requests against enterprise policy.                                                                              |
|  15 | : Saves human attention for high-risk decisions. In testing, it denied 7 out of 720 requests, allowing the agent to find safer alternatives in 4 cases and requiring human approval in only 3.      |
|  16 | : Blocked over 99% of simulated prompt injection attempts (RCE, secret theft) and over 90% of destructive actions (data deletion/tampering).                                                        |
|  17 | & Identity**:                                                                                                                                                                                       |
|  18 | : Agents lack human discretion; if authorized, they will use access, making authorization boundaries critical.                                                                                      |
|  19 | : Agents acting on behalf of users via OAuth/MCP can inadvertently access sensitive data they shouldn't.                                                                                            |
|  20 | : Provide static, granular controls but are difficult to provision and manage at scale (e.g., two accounts per user).                                                                               |
|  21 | :                                                                                                                                                                                                   |
|  22 | : Users should know they are interacting with an agent, not a human.                                                                                                                                |
|  23 | : Essential for audit logging and incident response to distinguish agent vs. human actions.                                                                                                         |
|  24 | : Source systems (e.g., Gmail) can enforce agent-specific boundaries (e.g., agents cannot send emails outside the organization).                                                                    |
|  25 | & Log Correlation**:                                                                                                                                                                                |
|  26 | : Correlating logs across compute, network, and source systems is difficult, especially on endpoints without clear workload identities.                                                             |
|  27 | : Monitoring thousands of agents generates massive log volumes, making human review infeasible.                                                                                                     |
|  28 | :                                                                                                                                                                                                   |
|  29 | : Layer 1 categorizes alerts and collects relevant logs; Layer 2 assesses severity and determines if human involvement is needed.                                                                   |
|  30 | : Deterministic rules trigger actions like cutting inference access, killing compute, or revoking connector access.                                                                                 |
|  31 | :                                                                                                                                                                                                   |
|  32 | (sandbox, network proxy) are critical but have gaps that agents will exploit.                                                                                                                       |
|  33 | ; LLM reviewers should filter noise to optimize human focus on critical events.                                                                                                                     |
|  34 | , with service accounts and narrow-scoped tasking being current best practices.                                                                                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Zozjsr2j1pM/hqdefault.jpg)](https://www.youtube.com/watch?v=Zozjsr2j1pM)

[Watch on YouTube](https://www.youtube.com/watch?v=Zozjsr2j1pM)
