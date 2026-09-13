#!/bin/bash
# Update pinned GitHub workflow and pre-commit dependency versions.

set -euo pipefail

readonly PINNED_ACTIONS=("austenstone/copilot-cli")

# @description Return success if the action should not be auto-updated.
# @arg $1 string GitHub Action repository name.
# @exitcode 0 If the action is pinned.
# @exitcode 1 If the action can be updated.
is_pinned_action() {
    local action="$1"
    local pinned_action

    for pinned_action in "${PINNED_ACTIONS[@]}"; do
        if [[ ${action} == "${pinned_action}" ]]; then
            return 0
        fi
    done

    return 1
}

# @description Update go-version entries in GitHub workflows.
# @noargs
# @exitcode 0 If versions were updated or no go-version entries exist.
update_go_versions() {
    local go_version
    local workflow_file

    go_version="$(curl -sL https://golang.org/VERSION?m=text | sed -n 's/go//;s/\..$//;1p')"
    if [[ -z ${go_version} ]]; then
        return 0
    fi

    export GO_VERSION="${go_version}"
    while IFS= read -r -d '' workflow_file; do
        perl -0pi -e 's/(^(\s*go-version:\s*)).*/${1}"^$ENV{GO_VERSION}"/mg' \
            "${workflow_file}"
    done < <(find .github/workflows -type f \( -name '*.yml' -o -name '*.yaml' \) -print0)
}

# @description Install uv when the runner image does not already provide it.
# @noargs
# @exitcode 0 If uvx is available after the function completes.
ensure_uvx() {
    if command -v uvx >/dev/null; then
        return 0
    fi

    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="${HOME}/.local/bin:${PATH}"
}

# @description Update pre-commit hook revisions.
# @noargs
# @exitcode 0 If pre-commit autoupdate succeeds.
update_pre_commit() {
    ensure_uvx
    uvx pre-commit autoupdate
}

# @description Update pinned GitHub Action revisions to latest release tags.
# @noargs
# @exitcode 0 If all updatable actions were processed.
update_github_actions() {
    local action
    local commit_hash

    while IFS= read -r action; do
        if [[ -z ${action} ]] || is_pinned_action "${action}"; then
            continue
        fi

        commit_hash="$(git ls-remote "https://github.com/${action}" |
            grep 'refs/tags/[v]\?[0-9][0-9\.]*$' |
            sed 's|refs/tags/||' |
            sort -u -k2 -V |
            tail -1 |
            awk '{ printf "%s # %s\n", $1, $2 }')"
        if [[ -z ${commit_hash} ]]; then
            continue
        fi

        export ACTION="${action}"
        export COMMIT_HASH="${commit_hash}"
        # shellcheck disable=SC2016
        find .github/workflows -type f \( -name '*.yml' -o -name '*.yaml' \) -print0 |
            xargs -0 perl -0pi -e \
                's|uses: \Q$ENV{ACTION}\E\@.*|uses: $ENV{ACTION}\@$ENV{COMMIT_HASH}|g'
    done < <(grep -rhoE 'uses: [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[^[:space:]]+' \
        .github/workflows |
        sed 's/^uses: //; s/@.*//' |
        sort -u)
}

main() {
    trap 'make fmt' EXIT

    update_go_versions
    update_pre_commit
    update_github_actions
}

main "$@"
