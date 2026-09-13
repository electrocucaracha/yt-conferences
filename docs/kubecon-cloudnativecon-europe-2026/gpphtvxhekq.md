---
layout: default
title:
  "Project Lightning Talk: How To Add A New Language Feature To OPA - Charlie
  Egan, Maintainer"
nav_order: 269
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Charlie from the OPER project introduces their general-purpose policy
  engine, which allows users to define and enforce policies—such as deployment permissions
  or repository access—using their policy language, Rego. He explains how policies...
resource: https://www.youtube.com/watch?v=gPpHTVxHEKQ
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Charlie from the OPER project introduces their general-purpose policy engine, which allows users to define and enforce policies—such as deployment permissions or repository access—using their policy language, Rego.
He explains how policies are loaded into the Open Policy Agent (OPA), evaluated with structured JSON input, and result in decision outputs, with features like policy reloading and audit logging.
A recent improvement in OPA 1.12 is the addition of string interpolation in Rego, making it easier and more intuitive to construct dynamic messages within policies.
Charlie details the technical steps involved in implementing this feature, including updates to the parser, abstract syntax tree, compiler, and the introduction of a new built-in function for template strings.
He also emphasizes the broader effort required to update the entire OPA ecosystem—such as integrations, editors, documentation, and linting tools—to support and promote this new best practice.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Charlie from the OPER project introduces the general purpose policy engine.                                                                           |
|   2 | OPER allows users to write policies, such as controlling deployment permissions or access to directories in a Git repository.                         |
|   3 | Policies are written in the Rego language.                                                                                                            |
|   4 | Users load policy code into Open Policy Agent (OPA), provide JSON input, and OPA evaluates the policy to produce a decision.                          |
|   5 | OPA handles policy decisions, policy reloading, and audit logs.                                                                                       |
|   6 | A new feature, string interpolation, has been added to make Rego easier and more familiar.                                                            |
|   7 | Previously, handling undefined usernames and string formatting required extra steps; string interpolation simplifies this.                            |
|   8 | String interpolation is introduced in OPA 1.12.                                                                                                       |
|   9 | Adding the feature required updating the parser to recognize new tokens for interpolated strings.                                                     |
|  10 | The abstract syntax tree (AST) was updated with a new node called template string.                                                                    |
|  11 | The compiler was updated to process template strings, converting them into a new built-in function.                                                   |
|  12 | The template string function is implemented in the top-down Rego interpreter, evaluating and concatenating string parts.                              |
|  13 | The change required updates across the OPA ecosystem, including integrations, editors, grammar definitions, tooling, documentation, and linter rules. |
|  14 | String interpolation is now considered a best practice in Rego.                                                                                       |
|  15 | Attendees are invited to visit the OPER kiosk, attend the maintainer track talk, and scan a QR code for more information.                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gPpHTVxHEKQ)
