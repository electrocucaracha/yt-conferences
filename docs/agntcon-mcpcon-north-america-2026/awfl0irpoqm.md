---
layout: default
title: "Shipping an MCP Server Nobody Told You How To: PyPI, the Registry, and the Rough Ed... Mesut Oezdil"
nav_order: 147
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker, a CNCF tech lead and HAMI project member, outlines the process of building, packaging, and shipping an MCP server, using a GPU monitoring server as a practical example."
resource: "https://www.youtube.com/watch?v=AWFL0irpOQM"
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

The speaker, a CNCF tech lead and HAMI project member, outlines the process of building, packaging, and shipping an MCP server, using a GPU monitoring server as a practical example.
Key challenges addressed include verifying ownership, ensuring discoverability, and managing updates, which are resolved by publishing the server to the Python Package Index (PyPI) and registering it in the official MCP Registry.
The presentation emphasizes that docstrings are critical because LLMs rely on these descriptions rather than code to understand and utilize the server’s tools, such as retrieving GPU temperature and utilization.
It also highlights the distinction between the registry, which acts as a verified phone book, and aggregators or clients like Visual Studio Code, which may require manual configuration to discover the server.
Finally, the speaker stresses the importance of proper versioning and authentication on PyPI, noting that changes to the codebase do not automatically update the published snapshot for users unless a new version is explicitly released.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , prove ownership, enable discovery, and handle specification changes.                                                                |
|   2 | : GPU info, utilization, VRAM, temperature, and stats, implemented as Python functions.                                               |
|   3 | ; they must be written for both human and model comprehension.                                                                        |
|   4 | /output using JSON format.                                                                                                            |
|   5 | , released in July, introduces stateless operation (no handshake/session) and replaces the older FastMCP approach.                    |
|   6 | (PyPI) to make it installable via `uvx` or similar tools.                                                                             |
|   7 | ; an MCP Registry acts as a "phone book" to link the package to a verified identity.                                                  |
|   8 | ; third-party aggregators like PulseMCP or Glama are often used for discovery.                                                        |
|   9 | ; MCP tools act as pointers to functions rather than runners.                                                                         |
|  10 | (e.g., pasting `mcp.json`) rather than automatic detection.                                                                           |
|  11 | : changes to code or dependencies require a new version on PyPI, as users install specific snapshots rather than live GitHub updates. |
|  12 | ; losing access prevents version updates, which blocks users from accessing new features or fixes.                                    |
|  13 | , leading to fragmentation across different IDEs and LLM clients.                                                                     |
|  14 | , PyPI integration, and the requirement for the server name to appear in the first line of the readme.                                |
|  15 | , confirming the server’s ability to return real-time hardware data.                                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/AWFL0irpOQM/hqdefault.jpg)](https://www.youtube.com/watch?v=AWFL0irpOQM)

[Watch on YouTube](https://www.youtube.com/watch?v=AWFL0irpOQM)
