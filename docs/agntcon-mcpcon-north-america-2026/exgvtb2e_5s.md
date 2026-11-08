---
layout: default
title: "Anatomy of a Claude Code Plugin, and Lessons Learned on Creating One - Charlie Lin"
nav_order: 89
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Charlie presents a detailed overview of the Rust EXT Review Toolkit, a plugin for coding agents like Claude Code designed to analyze mixed Python and Rust projects."
resource: "https://www.youtube.com/watch?v=EXGVtB2E_5s"
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

Charlie presents a detailed overview of the Rust EXT Review Toolkit, a plugin for coding agents like Claude Code designed to analyze mixed Python and Rust projects.
The plugin utilizes a structured workflow where pre-flight Python scripts gather project metadata from sources like `cargo.lock` and `pyproject.toml`, generating a comprehensive context file that informs subsequent analysis.
It bundles four primary commands—Explore, Health, Migrate, and Hotspot—which dispatch specialized background agents to detect specific issues such as unsafe Rust code, PyO3 API deprecations, panic safety violations, and behavioral parity differences between Rust extensions and pure Python fallbacks.
Each agent classifies findings into categories like "Fix," "Consider," "Policy," or "Acceptable," allowing for nuanced reporting that distinguishes between critical defects and acceptable design trade-offs.
The presentation concludes with key takeaways emphasizing the importance of separating deterministic script-based discovery from AI-driven reasoning to maintain context efficiency, while highlighting the tool’s value in uncovering subtle defects that standard automated scanners might miss.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : The "Rust EXT Review Toolkit" is a Claude Code plugin defined by a JSON marketplace file containing metadata (name, version, owner) and plugin entries. It bundles commands, MCP servers, hooks, agents, and LSP servers.                                                                          |
|   2 | : Commands are defined in Markdown files within a `commands` subdirectory. They include YAML metadata for descriptions, argument type hints, allowed tools, and optional scope limitations to specific subdirectories.                                                                               |
|   3 | : All commands begin with a discovery phase using Python scripts to parse project metadata from `cargo.lock`, `pyproject.toml`, or `setup.py`. This generates a JSON object detailing the PyO3 version, features, build backend, module names, and free-threaded interpreter support.                |
|   4 | : The pre-flight phase optionally runs external tools to gather deeper insights without full compilation:                                                                                                                                                                                            |
|   5 | `cargo metadata`: Identifies PyO3 versions and enabled features.                                                                                                                                                                                                                                     |
|   6 | `clippy`: Standard Rust linter.                                                                                                                                                                                                                                                                      |
|   7 | `cargo geiger`: Lists crates and dependencies containing unsafe code blocks.                                                                                                                                                                                                                         |
|   8 | `cargo expand`: Prints source after macro expansion (e.g., `println!`, `assert!`).                                                                                                                                                                                                                   |
|   9 | `Miri`: Detects memory leaks and undefined behavior.                                                                                                                                                                                                                                                 |
|  10 | : Discovery outputs are combined into a Markdown profile containing the build profile, Rust edition, active features, minimum Python version, and crate/module names. It classifies Rust files as handwritten, generated, or vendored, and lists project-specific idioms to prevent false positives. |
|  11 | : Agents are background specialists defined in Markdown with YAML metadata, tailored prompts, trigger conditions, and classification rules. Findings are categorized into four types:                                                                                                                |
|  12 | : Potential defects requiring correction (e.g., undefined behavior).                                                                                                                                                                                                                                 |
|  13 | : Potential concerns or improvements needing evaluation.                                                                                                                                                                                                                                             |
|  14 | : Design choices or compatibility trade-offs for maintainers.                                                                                                                                                                                                                                        |
|  15 | : Reviewed patterns or likely false positives.                                                                                                                                                                                                                                                       |
|  16 | : Runs all bundled agents for a full or selective project review. Key agents include:                                                                                                                                                                                                                |
|  17 | : Reviews unsafe Rust, raw Python API calls, and pointer ownership.                                                                                                                                                                                                                                  |
|  18 | : Finds mishandled Python errors, swallowed exceptions, and panics.                                                                                                                                                                                                                                  |
|  19 | : Examines Global Interpreter Lock attachment/detachment and object access.                                                                                                                                                                                                                          |
|  20 | : Checks for panics reachable from Python or FFI callbacks.                                                                                                                                                                                                                                          |
|  21 | /Protocol Checkers**: Verify thread safety (Send/Sync) and Python protocol implementations (dunder methods).                                                                                                                                                                                         |
|  22 | & Lifetime Checkers**: Examine module initialization, global state, and reference lifetimes.                                                                                                                                                                                                         |
|  23 | : Detects deprecated/removed APIs and checks stable API compatibility.                                                                                                                                                                                                                               |
|  24 | : Identifies complex functions combining high complexity with unsafe operations.                                                                                                                                                                                                                     |
|  25 | : Identifies behavioral differences between Rust extensions and pure Python fallbacks.                                                                                                                                                                                                               |
|  26 | : Uses commit history and code churn to prioritize risky areas.                                                                                                                                                                                                                                      |
|  27 | : Scores findings from each agent, deducting points for severe issues and mapping results to letter grades. It serves as a summary of the Explore command.                                                                                                                                           |
|  28 | : Assists in targeting newer PyO3 versions or supporting free-threaded Python. It scans for removed/deprecated APIs and non-idiomatic handles using four specific background agents.                                                                                                                 |
|  29 | : Identifies the 10–15 riskiest functions based on safety and correctness. It runs four agents to check for unsafe blocks, cross-boundary panics, `#[pyfunction]` panics, and excessive complexity (branches, loops, unsafe code).                                                                   |
|  30 | :                                                                                                                                                                                                                                                                                                    |
|  31 | /C++ to Rust required rethinking assumptions about PyO3 ownership, lifetimes, and type safety.                                                                                                                                                                                                       |
|  32 | , discovery, scanning, and agent orchestration enhances maintainability.                                                                                                                                                                                                                             |
|  33 | , though this constraint is less relevant with modern models.                                                                                                                                                                                                                                        |
|  34 | , language-specific reasoning, and historical evidence to uncover defects that automated scanners alone may miss.                                                                                                                                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EXGVtB2E_5s/hqdefault.jpg)]("https://www.youtube.com/watch?v=EXGVtB2E_5s")

[Watch on YouTube](https://www.youtube.com/watch?v=EXGVtB2E_5s)
