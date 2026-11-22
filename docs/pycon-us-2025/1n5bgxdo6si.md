---
layout: default
title: "A new safe external debugger interface for CPython - Pablo Galindo Salgado & Ivona Stojanovic"
nav_order: 101
parent: PyCon US 2025
type: Video Note
description: "Pablo Galindo Salgado and Ivona Estojano presented a new safe external debugger interface for CPython, introduced via PEP 678, which allows external tools to execute code in running Python processe..."
resource: "https://www.youtube.com/watch?v=1N5BgXdO6SI"
youtube_stats:
  view_count: 1425
  like_count: 33
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Pablo Galindo Salgado and Ivona Estojano presented a new safe external debugger interface for CPython, introduced via PEP 678, which allows external tools to execute code in running Python processes without crashing them.
They contrasted this approach with traditional debugging methods, which often require killing and restarting processes or using unsafe native system calls that can lead to deadlocks and data corruption.
The new mechanism utilizes a `remote_exec` function that communicates with the interpreter through a shared memory structure, ensuring that code execution only occurs at safe points within the evaluation loop to maintain process stability.
This feature is enabled by default in Python 3.14 and provides a secure foundation for advanced debugging tools, including a new remote PDB mode that allows users to inspect live applications without interruption.
The speakers emphasized that this innovation marks a significant shift from "pre-MRI" debugging practices to a modern, safe standard, enabling developers to inspect memory, change logging levels, and analyze internal states of production systems in real time.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The presentation introduces a new safe external debugger interface for CPython, referred to as Python's MRI moment, which allows debugging without killing or restarting processes.        |
|   2 | Traditional Python debugging often requires terminating a process and restarting it with a debugger attached, which is inefficient and unreliable for reproducing issues.                  |
|   3 | Native debugging tools like GDB use system calls such as ptrace to attach to processes, but this can cause crashes due to unsafe operations like calling malloc while locks are held.      |
|   4 | Existing profilers and inspectors use process_vm_readv to observe memory safely but cannot modify process state or execute code.                                                           |
|   5 | PEP 678 introduces a remote_exec function that allows external tools to execute Python scripts in a running process safely.                                                                |
|   6 | The mechanism relies on the interpreter reaching a safe point, such as an eval breaker, before executing the requested script to avoid corrupting internal state.                          |
|   7 | Communication between the debugger and interpreter uses a shared memory box located via the py_runtime structure, which is found using binary metadata and /proc/maps.                     |
|   8 | The py_debug_offsets structure provides a schema to locate specific fields, including the remote debugger pending call flag and the script path offset.                                    |
|   9 | Using a file path for the script instead of raw code adds a security layer, as attackers would need OS-level write permissions to inject malicious code.                                   |
|  10 | The feature is enabled by default in Python 3.14 but can be disabled via the PYTHON_DISABLE_REMOTE_DEBUG environment variable, a command-line flag, or a compile-time option.              |
|  11 | Python 3.14 includes remote PDB, allowing users to attach to a running process with pdb -p <pid> to inspect variables and call functions without stopping the program.                     |
|  12 | This capability enables advanced debugging tasks such as changing log levels on the fly, dumping internal state, inspecting live objects, and forcing garbage collection.                  |
|  13 | Windows implementation follows the same core logic but faces additional challenges with path handling and PDB integration, which were addressed by Matt Wankowski.                         |
|  14 | Performance impact is negligible because the check for pending remote execution is integrated into the existing eval breaker loop, which is already optimized by branch predictors.        |
|  15 | Interaction with C extensions depends on the extension checking for signals via Py_CheckSignals, ensuring that remote execution requests are handled when the interpreter regains control. |
|  16 | Exceptions raised within the remote script are treated as unraisable errors, printed to stderr, and do not propagate to the main application code.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1N5BgXdO6SI/hqdefault.jpg)](https://www.youtube.com/watch?v=1N5BgXdO6SI)

[Watch on YouTube](https://www.youtube.com/watch?v=1N5BgXdO6SI)
