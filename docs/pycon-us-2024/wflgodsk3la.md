---
layout: default
title: "Talks - Chahak Mehta: LSP Demystified - How towrite an LSP server in Python"
nav_order: 195
parent: PyCon US 2024
type: Video Note
description: "Chahak, a software engineer at Arch Labs, presents a talk on demystifying the Language Server Protocol (LSP) by sharing his experience building a MySQL language server using Python."
resource: "https://www.youtube.com/watch?v=WflGodsk3LA"
youtube_stats:
  view_count: 810
  like_count: 22
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Chahak, a software engineer at Arch Labs, presents a talk on demystifying the Language Server Protocol (LSP) by sharing his experience building a MySQL language server using Python.
He explains that LSP, introduced by Microsoft in 2016, provides a unified framework that decouples language-specific features like autocomplete and diagnostics from specific editors, allowing a single server implementation to support multiple clients such as Visual Studio Code, Emacs, and Vim.
The core of the system involves parsing code into an Abstract Syntax Tree (AST) using libraries like SQLFluff to enable context-aware smart autocomplete and linting, which are then communicated to the editor via JSON-RPC messages.
Chahak demonstrates how this architecture allows for advanced capabilities, including displaying function documentation on hover, executing live SQL queries, and switching database connections directly within the editor, all with minimal client-side code.
He concludes by noting that the LSP specification is highly extensible, supporting complex operations like code refactoring and custom actions, and shares that his implementation is available as a Python package on GitHub.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is a software engineer at Arch Labs who built a MySQL language server using Python.                                   |
|   2 | The Language Server Protocol (LSP) provides a unified framework to decouple language features from specific editors.              |
|   3 | LSP allows implementing features once on the server-side, enabling all compatible clients to use them automatically.              |
|   4 | The protocol uses JSON-RPC for communication between the development tool and the language server.                                |
|   5 | LSP was introduced by Microsoft in 2016 and later became an open standard with Red Hat.                                           |
|   6 | The server processes code by converting it into an Abstract Syntax Tree (AST) using language grammars.                            |
|   7 | SQLFluff is a Python library used to parse and lex SQL queries for the language server.                                           |
|   8 | Linting errors are identified on the AST and sent to the client via the textDocument/publishDiagnostics method.                   |
|   9 | Smart autocomplete is context-aware, suggesting table names or column names based on the cursor position in the AST.              |
|  10 | Documentation for symbols can be displayed through autocomplete suggestions or the hover capability.                              |
|  11 | Code actions allow for custom commands such as running queries, formatting code, or organizing imports.                           |
|  12 | The client-side implementation is minimal, requiring only a small patch to support the new language server.                       |
|  13 | The demo showed live query execution, explanation, and connection switching directly within the editor.                           |
|  14 | The server runs in stdio mode using the pylsp library and is distributed as a Python package.                                     |
|  15 | Performance is managed by debouncing requests, such as triggering autocomplete only after specific keystrokes.                    |
|  16 | The code is available on GitHub, with the server file defining capabilities and a separate file handling completions.             |
|  17 | LSP supports complex refactorings like renaming variables by leveraging the precise locations in the AST.                         |
|  18 | The protocol is extensible, allowing language-specific actions like executing SQL queries or Python-specific import organization. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WflGodsk3LA/hqdefault.jpg)](https://www.youtube.com/watch?v=WflGodsk3LA)

[Watch on YouTube](https://www.youtube.com/watch?v=WflGodsk3LA)
