---
layout: default
title: "There Is No Loading State: Real-Time Tool Calling for Voice Agents - Amanda Martin"
nav_order: 91
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker from Vapi emphasizes that designing voice agent conversations requires a fundamentally different approach than web development, as users have a single thread of attention and no visual ..."
resource: "https://www.youtube.com/watch?v=cmJcGbLhNyo"
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

The speaker from Vapi emphasizes that designing voice agent conversations requires a fundamentally different approach than web development, as users have a single thread of attention and no visual context to fill pauses.
Research indicates that natural conversation pauses are approximately 200 milliseconds, and longer silences are perceived negatively as system failures, making it critical to manage latency and tool call wait times effectively.
The presentation demonstrates that simply repeating generic "one moment" messages during tool calls degrades the user experience; instead, developers should use system prompts to allow agents to answer informational questions from their knowledge base while asynchronous tool calls run in the background.
This strategy keeps the conversation moving forward, confirms updated user inputs, and prevents the agent from appearing broken or unresponsive.
Additionally, the speaker advises that agents should always keep the caller in control of ending the interaction to leave a positive final impression, and recommends using AI voice simulations in CI/CD pipelines to rigorously test edge cases like interruptions, errors, and long-running processes before deployment.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , including deployment, tools, and monitoring.                                                                                               |
|   2 | ; pauses longer than this are perceived negatively as the agent being broken.                                                                |
|   3 | ; developers must design specific responses for delays, errors, and long-running processes.                                                  |
|   4 | (e.g., "One moment, please") degrade user experience, especially in longer calls with multiple tool calls.                                   |
|   5 | (e.g., "Checking availability for Wednesday") to provide context during processing.                                                          |
|   6 | , avoid repetition, and confirm updated user inputs.                                                                                         |
|   7 | , allowing the agent to answer informational questions from its knowledge base while a tool call is still running.                           |
|   8 | , appending the tool result once it returns to keep the conversation flowing.                                                                |
|   9 | , manageable chunks because users cannot process large amounts of data (like full calendars) via audio alone.                                |
|  10 | ; abrupt goodbyes negatively impact the overall user perception of the interaction.                                                          |
|  11 | (AI callers) should be used to test end-to-end scenarios, including interruptions and error handling, and integrated into CI/CD pipelines.   |
|  12 | , such as unusually long call durations, and to iterate on the design.                                                                       |
|  13 | "loading state," requiring constant engagement to prevent user frustration.                                                                  |
|  14 | : the LLM brain should be fast for real-time interaction, while heavier tasks can be offloaded to backend processes or more powerful models. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/cmJcGbLhNyo/hqdefault.jpg)]("https://www.youtube.com/watch?v=cmJcGbLhNyo")

[Watch on YouTube](https://www.youtube.com/watch?v=cmJcGbLhNyo)
