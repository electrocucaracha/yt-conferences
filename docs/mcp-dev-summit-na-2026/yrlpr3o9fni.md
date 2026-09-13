---
type: Video Note
title: "Demistifying Client ID Metadata Documents in MCP - Den Delimarsky, Anthropic"
description: "Dan from Anthropic discussed recent updates to the Model Context Protocol (MCP), focusing on improvements to client authorization and registration. Initially, MCP lacked guidance on authorization, leading to complex and unscalable solutions..."
resource: https://www.youtube.com/watch?v=YRLPR3o9fnI
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Dan from Anthropic discussed recent updates to the Model Context Protocol (MCP), focusing on improvements to client authorization and registration.
Initially, MCP lacked guidance on authorization, leading to complex and unscalable solutions like dynamic client registration (DCR), which introduced issues such as unbounded growth, silent expiry, and impersonation risks.
The new approach, SIMD (client ID metadata documents), allows each client to host a JSON metadata file at a domain they control, simplifying validation and reducing the need for complex registration flows.
This method addresses previous problems by ensuring one metadata document per client, making impersonation harder and management easier for both developers and authorization servers.
SIMD is now the recommended method in the MCP specification, with DCR still supported but planned for deprecation, and further enhancements to MCP are in development to improve security and developer experience.
# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Dan from Anthropic discussed recent updates to the Model Context Protocol (MCP) specification.                                 |
|   2 | Early MCP versions lacked official authorization guidance, requiring developers to build their own solutions.                  |
|   3 | Dynamic Client Registration (DCR) was introduced but led to issues:                                                            |
|   4 | Unbounded client growth due to open registration endpoints.                                                                    |
|   5 | Silent expiry of clients, making it hard to track active clients.                                                              |
|   6 | Impersonation risks, as clients could claim any identity in metadata.                                                          |
|   7 | Complexity in implementation, especially with identity providers lacking support.                                              |
|   8 | Proposal introduced for SIMD (Client ID Metadata Documents):                                                                   |
|   9 | Each client hosts a JSON metadata file at a domain they control.                                                               |
|  10 | Metadata includes client ID, name, URI, and redirect URIs.                                                                     |
|  11 | Trust is established via DNS verification of the domain.                                                                       |
|  12 | Simplifies client validation and reduces impersonation risk.                                                                   |
|  13 | Only one metadata document per client, eliminating unbounded growth.                                                           |
|  14 | No silent expiry, as metadata persists with the domain.                                                                        |
|  15 | SIMD is now the recommended approach in the MCP spec (since November update).                                                  |
|  16 | DCR remains supported but is planned for deprecation; pre-registered clients continue to work.                                 |
|  17 | Authorization servers can enforce security measures:                                                                           |
|  18 | Only accept HTTP 200 responses for metadata.                                                                                   |
|  19 | Restrict metadata file size.                                                                                                   |
|  20 | Ensure redirect URIs match client ID origins.                                                                                  |
|  21 | Major clients (Cloud.AI, Cloud Code, VS Code) support SIMD; work ongoing with others.                                          |
|  22 | Authorization servers can reason over and restrict trusted domains and URIs.                                                   |
|  23 | Additional proposals in progress: Demonstrated Proof of Possession (DEOP), workload identity federation, and cross-app access. |
|  24 | Developers are encouraged to provide feedback; new spec update expected in June.                                               |
|  25 | SIMD aims to simplify MCP client/server development and improve security.                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=YRLPR3o9fnI)