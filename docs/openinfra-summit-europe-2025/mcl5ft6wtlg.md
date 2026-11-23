---
layout: default
title: "Help! I need to use ansible, but all I have is some scripts!"
nav_order: 62
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Emma Foley, a senior software engineer on the OpenStack observability team, presents a beginner-friendly guide for converting Bash scripts into Ansible playbooks."
resource: "https://www.youtube.com/watch?v=Mcl5FT6wTLg"
youtube_stats:
  view_count: 117
  like_count: 3
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Emma Foley, a senior software engineer on the OpenStack observability team, presents a beginner-friendly guide for converting Bash scripts into Ansible playbooks.
She emphasizes that while wrapping scripts in a single `shell` task is a valid starting point, the goal is to incrementally improve the code by leveraging Ansible’s native features.
Key techniques include using `set_fact` to manage environment variables, `register` to capture and reuse command outputs, and `ansible-lint` to identify errors and suggest better modules.
Foley demonstrates how to replace generic shell commands with specific Ansible modules, such as using `assert` and `fail` for custom success and failure conditions, and implementing `retry` and `until` loops to handle flaky dependencies more efficiently than simple sleep commands.
She concludes by recommending that users write small, "dumb" test playbooks to verify module behavior and behavior changes, ensuring that the resulting Ansible code is not only functional but also more robust and maintainable than its Bash counterparts.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation focuses on converting Bash scripts into Ansible playbooks using a beginner-friendly, incremental approach.                     |
|   2 | The speaker is a senior software engineer on the OpenStack observability team with five years of experience writing and teaching Ansible.       |
|   3 | The goal is to move from manual script execution to automated, verifiable Ansible tasks, starting with a single shell task.                     |
|   4 | Basic Ansible concepts include modules, tasks, and playbooks, where playbooks are YAML files containing plays and tasks.                        |
|   5 | Ansible documentation is highly recommended, particularly the examples at the end of module pages, which are more helpful than parameter lists. |
|   6 | Ansible-lint is a useful tool for identifying errors, enforcing style, and suggesting better modules to use.                                    |
|   7 | Advanced topics like variable precedence, roles, and complex project structures are not required for this initial conversion process.           |
|   8 | Five key modules are introduced: shell, command, assert, fail, and debug.                                                                       |
|   9 | The shell module allows running scripts with output redirection and variable setting but is slower than the command module.                     |
|  10 | The command module is faster but does not support output redirection or pipes.                                                                  |
|  11 | The assert module checks if conditions are met and allows custom success and failure messages.                                                  |
|  12 | The fail module always fails a task and is used with 'when' conditions to stop execution based on specific criteria.                            |
|  13 | The debug module functions like a print statement to output messages or variables for troubleshooting.                                          |
|  14 | Environment variables from Bash scripts should be converted to Ansible variables using the 'set_fact' module to avoid repetition.               |
|  15 | Variables can be referenced in strings using the double curly brace templating syntax.                                                          |
|  16 | The 'register' keyword captures the output of a task into a structured variable for later use.                                                  |
|  17 | Registered outputs from shell or command modules include standard out and standard error, accessible as strings or lists of lines.              |
|  18 | Splitting large shell scripts into individual tasks improves addressability and allows for better error handling.                               |
|  19 | Idempotency is lost when using shell or command modules, but can be partially restored with specific parameters.                                |
|  20 | Custom failure and change conditions can be added to tasks to control playbook execution based on specific outputs.                             |
|  21 | The 'block', 'rescue', and 'always' structure provides try-except-finally functionality for error handling and cleanup.                         |
|  22 | Writing test playbooks is an effective way to verify that Ansible modules behave as expected compared to shell commands.                        |
|  23 | The 'assert' module is preferred over 'fail' when explicit success conditions need to be validated.                                             |
|  24 | Using 'stdout_lines' length is a better substitution for 'wc -l' in shell scripts, providing clearer failure output.                            |
|  25 | String searching in outputs can be done using the 'in' operator or the 'search' filter.                                                         |
|  26 | The 'pause' module is not recommended for waiting; instead, use 'retry', 'delay', and 'until' for resilient waiting mechanisms.                 |
|  27 | Retry' and 'delay' allow tasks to attempt execution multiple times with a set interval between attempts.                                        |
|  28 | The 'until' parameter defines a success condition that stops retries early if met.                                                              |
|  29 | Failed_when' and 'changed_when' parameters allow for custom logic on task status and state changes.                                             |
|  30 | Common modules for replacing shell commands include Git, apt, and yum, which offer built-in idempotency and features.                           |
|  31 | The 'when' parameter allows for conditional execution of tasks based on variable states.                                                        |
|  32 | Ansible documentation is accessible via the 'ansible-doc' command-line tool with customizable output formats.                                   |
|  33 | The speaker encourages using small, incremental steps to learn Ansible and improve existing playbooks.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Mcl5FT6wTLg/hqdefault.jpg)](https://www.youtube.com/watch?v=Mcl5FT6wTLg)

[Watch on YouTube](https://www.youtube.com/watch?v=Mcl5FT6wTLg)
