---
layout: default
title: "Make Attackers Cry -- Outsmart them with Deception (Sponsor: Fastly)"
nav_order: 97
parent: PyCon US 2026
type: Video Note
description: 'Rick Horwitz, a sales engineer at Fastly, presents a new cybersecurity strategy titled "Make Attackers Cry," which leverages deception and behavioral economics to defend against automated attacks l...'
resource: "https://www.youtube.com/watch?v=dfJzR1VBmUs"
youtube_stats:
  view_count: 372
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Rick Horwitz, a sales engineer at Fastly, presents a new cybersecurity strategy titled "Make Attackers Cry," which leverages deception and behavioral economics to defend against automated attacks like account takeover (ATO).
Instead of simply blocking malicious traffic, which signals to attackers that they have been detected and allows them to pivot their tactics, Fastly’s next-gen WAF employs a "deception" action that returns a standard "invalid username and password" response even when valid credentials are used.
This approach, referred to as adding "sludge" or friction, is designed to confuse attackers, waste their time and resources, and exploit psychological factors such as frustration and loss aversion described by prospect theory.
The solution is deployed at the edge, requiring no additional infrastructure, and provides valuable observability data on attacker behavior without exposing the organization to the risks associated with traditional honeypots.
By making the attack more costly and confusing, Fastly aims to deter sophisticated bots and credential stuffing attempts while maintaining a seamless experience for legitimate users.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Fastly is a content delivery network, cybersecurity, and edge compute provider.                                                |
|   2 | The presentation introduces "Make Attackers Cry," a new cybersecurity approach using deception.                                |
|   3 | Deception in cybersecurity aims to confuse attackers and make them waste time and resources.                                   |
|   4 | Attackers are human and have psychological limits, emotions, and budgets.                                                      |
|   5 | The goal is to apply "sludge" to attackers to increase their cost and frustration.                                             |
|   6 | Nudge" refers to positive guidance, while "sludge" makes actions difficult for the user.                                       |
|   7 | Attackers incur opportunity, quantitative, qualitative, and psychological costs.                                               |
|   8 | Prospect theory from behavioral economics explains that losses feel more painful than equivalent gains.                        |
|   9 | Traditional honeypots often fail due to high costs, lack of fidelity, and isolation issues.                                    |
|  10 | The "uncanny valley" describes the gap between a fake system and a real one that makes honeypots detectable.                   |
|  11 | Fastly’s new deception action works in-line within the Web Application Firewall (WAF).                                         |
|  12 | Instead of blocking attacks with a 403 error, the system sends a deceptive response.                                           |
|  13 | For account takeover attempts, valid credentials are swapped for fake ones to return an "invalid username and password" error. |
|  14 | This prevents attackers from receiving signals that allow them to pivot or adjust their tactics.                               |
|  15 | The deception feature is triggered by signals such as suspected bad bots, rate limits, or specific paths.                      |
|  16 | A demo showed that valid login attempts were deceived into appearing as failures.                                              |
|  17 | The system provides observability through tags, signals, and forensic analysis data.                                           |
|  18 | Fastly is developing a beta feature to deceive scanners by mimicking vulnerable applications.                                  |
|  19 | The deception feature is part of the standard product and does not require extra hardware or setup.                            |
|  20 | Defense in depth includes client-side protection, DDoS mitigation, caching, and WAF layers.                                    |
|  21 | Client-side protection detects headless bots by checking for video cards in the DOM.                                           |
|  22 | Fastly has approximately 550 terabytes per second of global capacity to absorb DDoS attacks.                                   |
|  23 | The WAF layer uses signals and bot management to secure backend systems.                                                       |
|  24 | The cost of deception is slightly higher than blocking due to additional computing requirements.                               |
|  25 | Deception is enabled via rule-based configuration in the WAF interface.                                                        |
|  26 | Marketing considerations may limit the use of friction for legitimate users.                                                   |
|  27 | The approach aims to gaslight attackers into believing their tools or lists are faulty.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/dfJzR1VBmUs/hqdefault.jpg)](https://www.youtube.com/watch?v=dfJzR1VBmUs)

[Watch on YouTube](https://www.youtube.com/watch?v=dfJzR1VBmUs)
