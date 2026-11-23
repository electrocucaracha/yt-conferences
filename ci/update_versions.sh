#!/bin/bash
# Update pinned GitHub Actions and the Kiso CLI version used by scripts/run_kiso.sh.

set -euo pipefail

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

	update_kiso_version
	update_github_actions
}

main "$@"
