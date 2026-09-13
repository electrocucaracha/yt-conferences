---
description: "Google Shell Style Guide practices for repository Bash scripts."
applyTo: "**/*.sh"
---

# Shell Script Rules

Follow the [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
for every Bash script in this repository.

## Interpreter and Structure

- Use `#!/bin/bash` for executable scripts.
- Keep scripts small and use a structured language when control flow becomes
  non-trivial or the script grows beyond roughly 100 lines.
- Put a concise file-header comment immediately after the shebang.
- Put constants and exported environment variables near the top of the file.
- Use a `main` function for scripts that contain other functions, and call
  `main "$@"` as the final non-comment line.
- Declare function-local variables with `local`.
- Use lowercase `snake_case` for functions and variables.
- Use uppercase `SNAKE_CASE` for constants and exported environment variables.

## Function Docstrings

- Document every non-trivial function immediately above its definition with
  `shdoc` annotations.
- Start the docstring with `@description` and describe the function's behavior.
- Document inputs with `@arg`, or use `@noargs` when there are no arguments.
- Document meaningful standard output with `@stdout` and diagnostics with
  `@stderr`.
- Document each meaningful return status with `@exitcode`.
- Use `@set` for globals changed by a function and `@see` for related
  functions or documentation.
- Mark implementation-only helpers with `@internal` so `shdoc` omits them
  from generated public documentation.
- Generate Markdown documentation with `shdoc script.sh > script.md` when a
  script's functions form a reusable interface.

Example:

```bash
# @description Print a greeting for a name.
# @arg $1 string The name to greet.
# @stdout The greeting.
# @exitcode 0 If the greeting was printed.
# @exitcode 1 If no name was provided.
say_hello() {
  ...
}
```

## Formatting and Quoting

- Use two spaces for indentation and no tabs.
- Keep lines at 80 characters when practical.
- Put `; then` and `; do` on the same line as their control statement.
- Use `$(...)` for command substitution, never backticks.
- Prefer `${variable}` and always quote variable and command substitutions.
- Use Bash arrays for lists of arguments instead of constructing command strings.
- Prefer `[[ ... ]]` for tests and `(( ... ))` for arithmetic.
- Use `"$@"` when forwarding all positional arguments.

## Reliability and Validation

- Enable appropriate strict options, normally `set -euo pipefail`.
- Check important command return values directly and print actionable errors to
  `STDERR`.
- Use functions for repeated error handling instead of duplicating messages.
- Avoid `eval`, aliases, unsafe wildcard expansion, and pipelines into `while`.
- Run ShellCheck on every changed shell script.
- Preserve intentional JSON or machine-readable output on `STDOUT`; send
  diagnostic messages to `STDERR`.

Keep these instructions focused on recurring shell conventions; consult the
[official guide](https://google.github.io/styleguide/shellguide.html) for detail.