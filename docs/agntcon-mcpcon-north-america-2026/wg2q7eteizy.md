---
layout: default
title: "Your AI Agent Installed Malware Because a SKILL.md Told It To - Liran Tal, Snyk"
nav_order: 43
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Liran, a developer advocate and AI security researcher at Snyk, presents a critical analysis of the emerging agent skill security ecosystem, highlighting that the rapid adoption of AI agents has ou..."
resource: "https://www.youtube.com/watch?v=wG2Q7etEIZY"
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

Liran, a developer advocate and AI security researcher at Snyk, presents a critical analysis of the emerging agent skill security ecosystem, highlighting that the rapid adoption of AI agents has outpaced necessary security safeguards.
He explains that agent skills, often implemented as simple Markdown files, pose significant risks because they can contain hidden instructions or malicious code that agents execute autonomously, leading to data exfiltration and system compromise.
Through live demonstrations and real-world examples, such as a malicious Vercel skill that stole environment variables and a "skill scanner" that installed a reverse shell, he illustrates how attackers exploit trust boundaries and the lack of official security models in the agent specification.
The talk emphasizes the "little trifecta" of danger: agents having access to sensitive data, untrusted external content, and the ability to push data out, creating a high-privilege environment vulnerable to prompt injection and typosquatting.
To address these threats, Snyk introduces "Agent Scan," a tool that uses a fine-tuned model to detect malicious intent and deviations from expected behavior, offering a more robust defense than traditional keyword-based scanning methods.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | # Key Points on Agent Skills Security Ecosystem                                                                                                        |
|   2 | :** Liran, developer advocate and AI security researcher at Snyk                                                                                       |
|   3 | :** Conducted security research on npm, Node.js, JavaScript ecosystem; found vulnerabilities in MCP servers; recently focused on toxic skills research |
|   4 | ## Toxic Skills Research Findings                                                                                                                      |
|   5 | ~January-February 2026 with Open Claw/Cloud Bot                                                                                                        |
|   6 | (similar to GitHub/NPMJS)                                                                                                                              |
|   7 | ~4,000 skills analyzed: 1 in 7 was vulnerable, malicious, had prompt injection, or credential theft                                                    |
|   8 | ## Live Demonstration (Gemini CLI)                                                                                                                     |
|   9 | , sending .env file to remote location                                                                                                                 |
|  10 | /hidden within skill.md file                                                                                                                           |
|  11 | ## Skills Structure Beyond Markdown                                                                                                                    |
|  12 | : can be plugins, packages with dependencies                                                                                                           |
|  13 | , static resources, install scripts (install.sh)                                                                                                       |
|  14 | ; not always scanned for vulnerabilities                                                                                                               |
|  15 | (GitHub, Skills.sh, Test Cells Registry)                                                                                                               |
|  16 | ## Security Model Gap                                                                                                                                  |
|  17 | "just read the code" insufficient since no one reads skill Markdown                                                                                    |
|  18 | ## Three-Part Threat Framework ("Triunvirate")                                                                                                         |
|  19 | :** What can agent access/read from system?                                                                                                            |
|  20 | :** Can agent send data to untrusted external locations?                                                                                               |
|  21 | :** Does agent have access to private data (e.g., .env secrets)?                                                                                       |
|  22 | ## Additional Attack Vectors                                                                                                                           |
|  23 | :** Anyone can publish skills with similar names                                                                                                       |
|  24 | :** Skills with hidden dependencies and obfuscated code                                                                                                |
|  25 | :** Agent trusts skill; skill has hidden malicious intent                                                                                              |
|  26 | :** Invisible characters execute malicious commands without detection                                                                                  |
|  27 | :** Malicious skills disguised as security tools (e.g., skill scanner installing reverse shell)                                                        |
|  28 | ## Real Examples                                                                                                                                       |
|  29 | , required non-existent "Open Clock Core" dependency from random repository                                                                            |
|  30 | "Test Skill" executed calculator via hidden characters                                                                                                 |
|  31 | "Skill Defender" skill was actually malware installing reverse shells                                                                                  |
|  32 | ## Approval Fatigue Problem                                                                                                                            |
|  33 | ; cannot realistically approve every action                                                                                                            |
|  34 | (not 100% effective)                                                                                                                                   |
|  35 | /hundreds of bots                                                                                                                                      |
|  36 | ## Detection Challenges                                                                                                                                |
|  37 | /regex-based scanners miss variations and shell tricks                                                                                                 |
|  38 | ## Agent Scan Solution                                                                                                                                 |
|  39 | (Python UVX package)                                                                                                                                   |
|  40 | ## Key Recommendations                                                                                                                                 |
|  41 | (not just regular expression)                                                                                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/wG2Q7etEIZY/hqdefault.jpg)](https://www.youtube.com/watch?v=wG2Q7etEIZY)

[Watch on YouTube](https://www.youtube.com/watch?v=wG2Q7etEIZY)
