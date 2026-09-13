---
type: Video Note
title: "Rust Is the Language of AGI - Miley Fu, Second State"
description: "Miley Fu, a CNCF ambassador, presented on behalf of Michael about the use of Rust and WebAssembly in building reliable AI infrastructure, highlighting the CNCF project WasmEdge and its applications in server-side AI inference. She discussed..."
resource: https://www.youtube.com/watch?v=u3iCjz7p8aE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Miley Fu, a CNCF ambassador, presented on behalf of Michael about the use of Rust and WebAssembly in building reliable AI infrastructure, highlighting the CNCF project WasmEdge and its applications in server-side AI inference.
She discussed the popularity of Rust, noting its memory safety, reliability, and suitability for scalable infrastructure, as evidenced by its adoption in projects like X AI.
Miley introduced a voice AI agent demo powered by a Rust server, explaining its architecture, which processes user speech through ASR, LLM, and TTS components, and supports extensibility with additional sensors.
The talk also covered "code mode," a new approach where AI agents generate and execute code (e.g., TypeScript or Rust) to interact with MCP tools in a secure sandbox, reducing token consumption and improving efficiency compared to traditional tool calling.
Miley showcased the open-source Rascoder project, which enables agents to generate, compile, and self-correct Rust code, emphasizing Rust's advantages for AI coding and the potential for fully automated, verifiably correct software generation.
# Main Points

|   # | Main point                                                                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Miley Fu presented on behalf of Michael due to his absence.                                                                                                                                                                                         |
|   2 | Miley is a CNCF ambassador working on the WasmEdge project, using WebAssembly on the server side, including for AI inference.                                                                                                                       |
|   3 | The talk focused on using Rust to build reliable AI infrastructure and recent advancements in AI agents, specifically "code mode."                                                                                                                  |
|   4 | Stack Overflow 2024 survey: Rust has over 80% favorability and is the most beloved language since 2016, but not the most desired due to its steep learning curve.                                                                                   |
|   5 | Rust's compiler enforces correctness and optimization, making it harder to learn but more reliable than Python or JavaScript.                                                                                                                       |
|   6 | Rust is well-suited for AI infrastructure; used by companies like X AI for scalable, reliable, and maintainable systems.                                                                                                                            |
|   7 | Rust's memory safety is a critical advantage, endorsed by the White House for digital infrastructure.                                                                                                                                               |
|   8 | Miley demonstrated two voice AI agent demos powered by a Rust server, with the Echoit agent as an example.                                                                                                                                          |
|   9 | The system supports ESP32 and is being ported to Raspberry Pi; open source firmware is available.                                                                                                                                                   |
|  10 | Workflow: device sends raw voice data via WebSocket; server detects end of speech, calls ASR (voice-to-text), adds chat history and prompt, calls LLM, handles tool calls via MCP server, calls TTS (text-to-speech), streams audio back to device. |
|  11 | The system allows adding sensors (e.g., cameras) and integrating visual data streams.                                                                                                                                                               |
|  12 | Rust enables cross-platform AI inference using WasmEdge runtime.                                                                                                                                                                                    |
|  13 | Traditional AI agents expose MCP tools directly to LLMs, causing excessive token consumption and context window overload.                                                                                                                           |
|  14 | "Code mode" converts MCP tools into programming language APIs (e.g., TypeScript), letting LLMs write code to call tools in a secure sandbox, reducing token usage and improving control flow.                                                       |
|  15 | Code mode implementations: auto-generate SDKs, add SDK docs, provide code-execution MCP tools.                                                                                                                                                      |
|  16 | Rust is uniquely suited for AI code generation due to its strong compiler and verifiable correctness.                                                                                                                                               |
|  17 | Rascoder project: open source                                                                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=u3iCjz7p8aE)