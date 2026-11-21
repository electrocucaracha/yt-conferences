---
layout: default
title: "Anatomy of a Phishing Campaign - Mike Fiedler"
nav_order: 84
parent: PyCon US 2026
type: Video Note
description: "Mike Fiedler, PyPI’s sole safety and security engineer, detailed a significant phishing campaign from July 2025 that targeted package maintainers to compromise the open-source supply chain."
resource: "https://www.youtube.com/watch?v=uXW1qeUS6Yw"
youtube_stats:
  view_count: 240
  like_count: 5
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

Mike Fiedler, PyPI’s sole safety and security engineer, detailed a significant phishing campaign from July 2025 that targeted package maintainers to compromise the open-source supply chain.
Attackers used a man-in-the-middle proxy to intercept credentials and session cookies, allowing them to upload malicious code, such as a Windows-targeted DLL, into popular packages like `num2words` to infect downstream users.
The incident response highlighted the limitations of Time-Based One-Time Passwords (TOTP), which can be intercepted by such proxies, and emphasized the superior security of WebAuthn (passkeys), which are cryptographically bound to the legitimate domain and thus resistant to phishing.
Fiedler advised users to immediately adopt WebAuthn, pin exact package versions and hashes, and implement dependency cool-downs to mitigate the risk of rapid malware propagation.
He also stressed the critical need for sustained financial support for open-source security infrastructure, noting that while PyPI has improved defenses, the burden of security remains a shared responsibility between the platform, maintainers, and end users.

# Main Points

|   # | Main point                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Mike Fiedler, the sole PyPI safety and security engineer, presented a detailed analysis of a major phishing campaign that targeted PyPI maintainers in July 2025.                            |
|   2 | PyPI serves over 9 petabytes of data daily at peak, with over 900 new projects added per day, making it a high-value target for attackers seeking multiplicative impact.                     |
|   3 | Attackers exploited the ease of phishing maintainers to compromise upstream packages, which then proliferates malware through CI pipelines and production deployments to a vast user base.   |
|   4 | The phishing emails were crafted to mimic legitimate PyPI notifications, leveraging open-source code to replicate the interface and using metadata or GitHub profiles to identify targets.   |
|   5 | Instead of building a fake site, attackers used a proxy service to intercept traffic, rewriting URLs to appear as pypi.org while capturing credentials and session cookies.                  |
|   6 | The proxy relayed login attempts to the real PyPI backend, allowing attackers to obtain valid session cookies that granted access for approximately eight hours.                             |
|   7 | The initial detection occurred via a user report on a weekend, leading to a delayed response due to the lack of a 24/7 security operations center at PyPI.                                   |
|   8 | Attackers compromised the num2words library by injecting a malicious _build.py file containing a compiled DLL, targeting Windows users with a scavenger loader payload.                      |
|   9 | The attackers made a coding error in version 0.5.15, quickly releasing a patched version 0.5.16, while maintainers failed to invalidate the specific API token used by the attacker.         |
|  10 | The ultimate target was not num2words itself, but larger downstream dependencies like the Transformers library, which does not pin to exact versions, allowing the malware to spread.        |
|  11 | Response efforts included revoking attacker tokens, yanking malicious versions, notifying compromised users, and coordinating with other ecosystems like npm and RubyGems.                   |
|  12 | Many infrastructure vendors initially failed to act on abuse reports, viewing the issue as non-urgent or outside their scope, highlighting the challenges in cross-vendor incident response. |
|  13 | Two-factor authentication via TOTP is vulnerable to man-in-the-middle proxy attacks, as the six-digit code can be captured and used within its 30-second validity window.                    |
|  14 | WebAuthn (passkeys) is recommended as a superior alternative because it uses cryptographic validation tied to the specific domain, making it immune to proxy-based phishing.                 |
|  15 | A new defense was implemented in November 2025 requiring email confirmation for TOTP logins from unrecognized IP addresses to mitigate proxy attacks.                                        |
|  16 | Attackers launched a second campaign two months later using a PyPI mirror domain, demonstrating the persistent and evolving nature of these threats.                                         |
|  17 | Users are advised to move to WebAuthn immediately, hover over links to verify URLs, and avoid using long-lived API tokens in favor of trusted publishing mechanisms.                         |
|  18 | Pinning exact package versions and hashes is critical for consumers to prevent installing malicious updates, as optimistic version pinning leaves systems vulnerable.                        |
|  19 | Maintainers should adopt dependency cool-down periods to allow time for security evaluation before updating packages, reducing the risk of immediate exploitation.                           |
|  20 | The security of the open-source ecosystem relies on financial support for dedicated security personnel, as volunteer efforts are insufficient for professional incident response.            |
|  21 | Attackers are difficult to identify due to the use of VPNs and spoofed user agents, requiring reliance on security partners for pattern fingerprinting and attribution.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/uXW1qeUS6Yw/hqdefault.jpg)](https://www.youtube.com/watch?v=uXW1qeUS6Yw)

[Watch on YouTube](https://www.youtube.com/watch?v=uXW1qeUS6Yw)
