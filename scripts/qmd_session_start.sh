#!/bin/bash
# Refresh the QMD semantic search index at the start of a Copilot coding session.
#
# This hook ensures the knowledge base index is up-to-date before Copilot begins.
# If the index is stale (you've edited concept documents since last indexing),
# this refresh brings it current for accurate semantic search results.
#
# Gracefully handles missing QMD installation or directory navigation issues—
# always exits 0 to avoid blocking session startup.
#
# Outputs JSON context for integration with session logging.
#
# Called by: VS Code Copilot session lifecycle hooks
#

set -euo pipefail

#######################################
# @description Refresh the QMD index at session start, reporting success or issues.
# @noargs
# @stdout JSON context describing the refresh result.
# @exitcode 0 Always, including when QMD is unavailable or refresh fails (non-blocking).
#######################################
main() {
    local root_dir

    if ! command -v qmd >/dev/null 2>&1; then
        printf '%s\n' \
            '{"additionalContext":"QMD is not installed; the knowledge index was not refreshed."}'
        return 0
    fi

    root_dir="$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)"
    if ! cd "${root_dir}"; then
        printf '%s\n' \
            '{"additionalContext":"Unable to enter the repository; the knowledge index was not refreshed."}'
        return 0
    fi

    export QMD_FORCE_CPU="${QMD_FORCE_CPU:-1}"

    if qmd update >/dev/null 2>&1; then
        printf '%s\n' \
            '{"additionalContext":"QMD index refreshed for the docs knowledge bundle."}'
    else
        printf '%s\n' \
            '{"additionalContext":"QMD index refresh failed; continue with caution because search results may be stale."}'
    fi
}

main "$@"
