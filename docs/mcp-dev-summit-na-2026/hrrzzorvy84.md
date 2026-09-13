---
type: Video Note
title: "Putting the Single Back in Single Sign-On: Cross-App Access for MCP - Paul Carleton & Max Gerber"
description: "In this presentation, Paul Carlton and Max Gerber discuss the challenges of OAuth consent screens in enterprise environments, highlighting how they create unnecessary friction for both end users and IT administrators. They explain that, unl..."
resource: https://www.youtube.com/watch?v=HRrzzORvy84
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Paul Carlton and Max Gerber discuss the challenges of OAuth consent screens in enterprise environments, highlighting how they create unnecessary friction for both end users and IT administrators.
They explain that, unlike consumer scenarios where users control their data, enterprise data is managed by IT admins through workforce identity providers (IDPs) and single sign-on (SSO) systems.
The speakers introduce the IETF draft "identity assertion JWT authorization grant" (ID JAG), also known as cross app access (XAA), which allows IT admins to preconfigure access policies and remove the need for user consent screens by shifting consent decisions to the admin level.
Through live demonstrations, they show how XAA enables seamless, consent-free access to multiple applications, centralizes policy control, and improves auditability and attribution.
The talk concludes by emphasizing that XAA reduces friction, enhances security and manageability, and opens the door to more granular and session-specific access controls in enterprise systems.
# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OAUTH consent screens create friction for end users and are not ideal for enterprise scenarios.                                                                                                 |
|   2 | In enterprises, data is owned and managed by the company, not individual users.                                                                                                                 |
|   3 | IT admins use workforce IDPs (SSO providers) to manage user access and permissions.                                                                                                             |
|   4 | Traditional OAUTH flows lack IT admin visibility and centralized policy control.                                                                                                                |
|   5 | The new IETF draft "identity assertion JWT authorization grant" (ID JAG), also called cross app access (XAA), allows IT admins to control access and removes the need for user consent screens. |
|   6 | XAA enables the workforce IDP to provide consent on behalf of users, streamlining access.                                                                                                       |
|   7 | MCP has adopted XAA as an official authorization extension, with implementations in the TypeScript SDK and more coming.                                                                         |
|   8 | With XAA, IT admins preconfigure trust relationships between MCP clients, workforce IDPs, and authorization servers.                                                                            |
|   9 | End users log in via the workforce IDP; MCP clients obtain credentials and exchange them for access tokens without user interaction.                                                            |
|  10 | Live demos showed XAA flows in both script and real client scenarios (Cloud Code, Cursor, Figma).                                                                                               |
|  11 | XAA eliminates multiple consent screens, reducing friction for both users and IT admins.                                                                                                        |
|  12 | XAA allows for more granular access tokens (e.g., per session or per agent), enabling better attribution and specificity.                                                                       |
|  13 | IT admins gain central visibility, policy control, and revocation capabilities without managing multiple dashboards.                                                                            |
|  14 | XAA is not MCP-specific and can be used in other applications requiring cross-app access.                                                                                                       |
|  15 | Adoption requires changes to clients, IDPs, and authorization servers, but not MCP servers.                                                                                                     |
|  16 | XAA supports configurable token lifetimes and refresh options.                                                                                                                                  |
|  17 | Centralized control in the workforce IDP reduces risk of users selecting incorrect credentials or sharing data inappropriately.                                                                 |
|  18 | Progressive adoption improves the experience as more servers support XAA. Ratings (1-5): 4                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HRrzzORvy84)