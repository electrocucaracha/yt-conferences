---
type: Video Note
title: "[Keynote] Revolutionizing Travel with AI How We Built the Turkish Airlines MCP"
description: "The speaker, delivering their first major international speech, introduces Turkish Airlines’ pioneering development of an MCP (Multi-Channel Platform) server, highlighting the airline’s status as a global leader and its commitment to techno..."
resource: https://www.youtube.com/watch?v=KWvkPFnHwlM
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, delivering their first major international speech, introduces Turkish Airlines’ pioneering development of an MCP (Multi-Channel Platform) server, highlighting the airline’s status as a global leader and its commitment to technological innovation through its subsidiary, Turkish Technology.
The MCP enables users to interact with Turkish Airlines services via chat interfaces, allowing for tasks such as flight searches, booking, checking flight status, and accessing promotions, all authenticated through the airline’s frequent flyer program using the latest OAuth 2.1 standard.
The team faced challenges related to security, governance, and adapting new authentication protocols, which they addressed by leveraging existing APIs, Cloudflare for security, and rate limiting.
Future plans include expanding MCP functionalities to allow more interactive features like seat selection and disruption management, as well as enhancing the UI and integrating with internal tools.
The speaker also mentions their open-source contributions, such as the Takeoff UI library, and efforts to deploy secure, on-premise LLMs for enterprise use, emphasizing the importance of empowering users with innovative tools.
# Main Points

|   # | Main point                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker's first international speech to a large audience                                                               |
|   2 | Thanks Shannon for the opportunity                                                                                     |
|   3 | Turkish Airlines is the airline flying to the most countries globally                                                  |
|   4 | Fleet of 500+ aircraft, aiming for 800; carries ~9 million passengers annually                                         |
|   5 | Turkish Technology provides tech for Turkish Airlines and aims to serve the whole airline industry                     |
|   6 | Digital Lab team focuses on innovation and emerging technologies                                                       |
|   7 | MCP (Multi-Channel Platform) server built by Turkish Airlines; first in the airline industry                           |
|   8 | Experimented with Apple Vision Pro and collaborations with startups                                                    |
|   9 | MCP development began after OAuth specification release; now fully live and testable                                   |
|  10 | Belief that chat is the new user interface                                                                             |
|  11 | MCP allows users to ask questions and get flight recommendations with booking links prefilled                          |
|  12 | Use cases: searching flights, checking flight status, booking details, check-in status, promotions, city guides        |
|  13 | OAuth used for authentication via Smiles frequent flyer program                                                        |
|  14 | Security and governance were major challenges; concerns about data leaks                                               |
|  15 | Used existing mobile and web APIs, proxied through MCP; secured with Cloudflare and rate limiting by frequent flyer ID |
|  16 | MCP is end-user focused, requiring login with frequent flyer ID                                                        |
|  17 | Implemented OAuth 2.1 despite lack of enterprise support, using Cloudflare Worker platform and SDK                     |
|  18 | Current MCP features are read-only; working on enabling actions like check-in and seat selection                       |
|  19 | Developing disruption management to suggest new flights automatically                                                  |
|  20 | Working on rendering UI through MCP for better customer experience                                                     |
|  21 | Developed Takeoff UI and Takeoff UI MCP, open-source UI libraries for the airline industry                             |
|  22 | Deployed on-premise LLMs (e.g., Q3) for internal use, enabling secure AI-powered tools for employees                   |
|  23 | Integrated MCPs with internal platforms like Atlassian for workflow automation                                         |
|  24 | Challenges remain in centrally managing MCPs in enterprise applications                                                |
|  25 | Emphasis on empowering people with the right tools to                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=KWvkPFnHwlM)