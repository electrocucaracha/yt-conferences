---
layout: default
title: "World's First Undoable Notebook - Zhaoheng Li"
nav_order: 38
parent: PyCon US 2025
type: Video Note
description: Dr.
resource: "https://www.youtube.com/watch?v=SX9wlj-EG7U"
youtube_stats:
  view_count: 571
  like_count: 5
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

Dr.
Billy Lee presents "Ku," a novel checkpointing system for computational notebooks that addresses the critical issue of non-persistent session states and the inability to undo irreversible cell executions.
By introducing the concept of "co-variables," which treat reference-sharing variables as single entities, the system enables accurate delta detection and incremental storage of state changes without breaking shared references or incurring the high storage costs of full-state dumps.
Ku allows users to undo specific cell executions, create named checkpoints, and restore session states after kernel crashes by leveraging a versioning model similar to Git, while also handling unserializable data through cell replay.
The presentation includes a live demonstration of these features within Jupyter Lab, showcasing how users can recover dropped data frame columns and revert to previous model states.
Lee concludes by discussing ongoing work on object-level deduplication and a visual GUI, while acknowledging current limitations regarding external state changes and the need for better integration with broader software engineering practices.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presenter introduces Ku, a notebook checkpointing system designed to allow users to undo cell executions and restore session states.                                |
|   2 | Notebooks maintain session state in memory, which is non-persistent and can be lost if the kernel crashes or the session disconnects.                                   |
|   3 | Current notebooks do not record past states, making it impossible to undo irreversible actions like dropping data frame columns or overwriting variables.               |
|   4 | Existing solutions include rerunning all cells, which is time-consuming and may not restore the exact previous state due to code changes.                               |
|   5 | Dumping the entire session state after every cell execution is generalizable but results in excessive storage usage due to large checkpoint files.                      |
|   6 | OS-level checkpointing using tools like CRIU allows incremental storage but fails with complex workloads involving GPUs or multiprocessing and is platform-specific.    |
|   7 | Manual storage of change data is incremental and native but requires significant expertise to correctly identify and save variables without breaking shared references. |
|   8 | The proposed system automates the detection and storage of change data by treating reference-sharing variables as single entities called co-variables.                  |
|   9 | Co-variables preserve shared references and simplify delta detection by ensuring that hidden updates to related variables are captured as a single unit.                |
|  10 | The system incrementally maintains co-variable tracking reference graphs using live analysis to identify which variables are modified by each cell execution.           |
|  11 | Variable accesses and assignments are captured by patching the getter and setter methods of the notebook session state dictionary.                                      |
|  12 | Checkpoints are managed similarly to Git commits, where each cell execution creates a timestamped delta that inherits unchanged variables from previous states.         |
|  13 | The system supports incremental checkout by computing the difference between source and target states and loading only the necessary data changes.                      |
|  14 | Unserializable data, such as objects containing generators, is handled by replaying the specific cell code that created the variable.                                   |
|  15 | A live demo demonstrated undoing a cell execution that dropped data frame columns and restoring the session state after a kernel crash.                                 |
|  16 | The system allows users to create named checkpoints, or commits, to save specific states and return to them later via checkout.                                         |
|  17 | Future work includes object-level deduplication to reduce storage costs and the development of a GUI called Tissue Board for visualizing execution branches.            |
|  18 | The system is currently integrated with Jupyter Lab and Jupyter Notebook but is compatible with other platforms that use the IPython kernel.                            |
|  19 | A limitation of the system is that it does not track changes occurring outside the notebook session state, such as external API calls or file system modifications.     |
|  20 | Objects that do not support pickling are treated as terminal objects and restored via cell replay rather than direct serialization.                                     |
|  21 | The system assumes that objects remain consistent before and after pickling, which may be a limitation for objects that change during serialization.                    |
|  22 | Monkey patching of the namespace successfully captures variable references even within locally defined functions and complex control flows.                             |
|  23 | Changes to cell code text are not logged as state changes, and the system focuses on restoring variable states rather than code history.                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/SX9wlj-EG7U/hqdefault.jpg)](https://www.youtube.com/watch?v=SX9wlj-EG7U)

[Watch on YouTube](https://www.youtube.com/watch?v=SX9wlj-EG7U)
