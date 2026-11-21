---
layout: default
title: "Live process manipulation with Python 3.14's zero overhead debugging interface - Savannah Ostrowski"
nav_order: 22
parent: PyCon US 2026
type: Video Note
description: "At PyCon, a CPython core developer and FastAPI Labs engineer presented a talk on `sys.remote_exec`, a new feature in Python 3.14 that allows code execution within a running interpreter process with..."
resource: "https://www.youtube.com/watch?v=CnDFc4azdbU"
youtube_stats:
  view_count: 393
  like_count: 7
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

At PyCon, a CPython core developer and FastAPI Labs engineer presented a talk on `sys.remote_exec`, a new feature in Python 3.14 that allows code execution within a running interpreter process without restarting it.
The speaker explained how this API, built on the remote debugging attachment protocol (PEP 768), safely injects scripts at bytecode-level safe points, enabling live inspection of application state, such as database connection pools and global variables, without interrupting the target process.
To demonstrate practical utility, the speaker introduced "Debug Wand," an open-source CLI tool that leverages `sys.remote_exec` to inject `debugpy` into containerized applications running on Kubernetes, Docker, or Podman.
This tool automates the complex process of discovering the correct worker process, injecting the debugger, and setting up port forwarding, thereby providing a seamless editor-based debugging experience with breakpoints and variable inspection for live containers.
The presentation also addressed security concerns, noting that `sys.remote_exec` requires specific OS-level permissions like `sys_ptrace` and same-user access, ensuring it does not create a new attack surface but rather functions as a standard debugger interface.
Finally, the speaker highlighted practical challenges, such as managing multiple processes in frameworks like Uvicorn or Gunicorn, and encouraged the community to explore this primitive for broader use cases beyond debugging, including hot configuration changes and state inspection.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker introduces sys.remote_exec, a new feature in Python 3.14 that allows executing code in a running interpreter without restarting the process. |
|   2 | This feature addresses the difficulty of debugging containerized applications where traditional breakpoints and restarts are impractical or destructive to state. |
|   3 | Sys.remote_exec requires only a process ID and a script path, executing the script in a fresh scope with access to the target process's live modules and global state. |
|   4 | The mechanism relies on the remote debugging attachment protocol introduced in PEP 768, which uses the eval breaker to safely inject code at interpreter safe points. |
|   5 | This approach is safer than older tools like Pyrasite because it operates at the bytecode level rather than interrupting C code execution randomly. |
|   6 | The speaker built a tool called Debug Wand, a CLI that wraps the complexity of discovering containers, finding the correct process, and injecting debugpy. |
|   7 | Debug Wand works with Kubernetes, Docker, and Podman, allowing users to attach a full editor debugging experience to live processes with a single command. |
|   8 | The tool utilizes the Debug Adapter Protocol (DAP) and debugpy to provide breakpoints, stepping, and variable inspection without modifying application code. |
|   9 | Security considerations include requiring the same user permissions as the target process, enabling specific OS capabilities like sys_ptrace, and using audit hooks to log or block execution. |
|  10 | The script executed via sys.remote_exec must be a real file on disk, which allows for better security auditing and control compared to passing strings directly. |
|  11 | A key challenge is identifying the correct process to attach to, as applications like Uvicorn or Gunicorn spawn multiple processes such as watchers and workers. |
|  12 | Uvicorn's reload mode complicates debugging because restarting the worker changes the process ID, requiring tools to monitor and re-inject debugpy automatically. |
|  13 | The speaker emphasizes that sys.remote_exec is a general-purpose primitive useful for state inspection, hot configuration changes, and one-off investigations beyond just debugging. |
|  14 | Debug Wand is open source and available on GitHub and PyPI, with the underlying technology being integrated into FastAPI Cloud. |
|  15 | The speaker encourages the community to explore building further tooling on top of sys.remote_exec and thanks the core developers who implemented PEP 768. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CnDFc4azdbU/hqdefault.jpg)](https://www.youtube.com/watch?v=CnDFc4azdbU)

[Watch on YouTube](https://www.youtube.com/watch?v=CnDFc4azdbU)
