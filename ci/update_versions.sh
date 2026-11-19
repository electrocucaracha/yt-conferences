#!/bin/bash
# Update pinned GitHub workflow, pre-commit, and Kiso CLI versions.

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

# @description Update the pinned Kiso CLI release.
# @noargs
# @exitcode 0 If a release tag was found or no matching tag exists.
update_kiso_version() {
	local kiso_version

	kiso_version="$(git ls-remote --tags https://github.com/oak-invest/kiso |
		grep -E 'refs/tags/v?[0-9]+(\.[0-9]+)*(\^\{\})?$' |
		awk '{ print $2 }' |
		sed -E 's|refs/tags/||; s/\^\{\}$//' |
		sort -Vu |
		tail -1 || true)"
	if [[ -z ${kiso_version} ]]; then
		return 0
	fi

	export KISO_VERSION="${kiso_version}"
	perl -0pi -e \
		's/(readonly KISO_VERSION="\$\{KISO_VERSION:-)[^}]+(\}")/${1}$ENV{KISO_VERSION}${2}/' \
		scripts/run_kiso.sh
}

# @description Update pinned GitHub Action revisions to latest release tags.
# @noargs
# @exitcode 0 If all updatable actions were processed.
update_github_actions() {
	ensure_uvx
	uv run --no-project --with git+https://github.com/electrocucaracha/gh-updater.git gh-updater .
}

main() {
	trap 'make fmt' EXIT

	update_go_versions
	update_pre_commit
	update_kiso_version
	update_github_actions
}

main "$@"
