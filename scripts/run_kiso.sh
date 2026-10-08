#!/bin/bash
# Run the Kiso CLI against the OKF knowledge bundle in docs/.
#
# Downloads the pinned kiso-cli release (cached between runs) and forwards the
# given command to it, defaulting to `check`.
#
# Environment variables:
#   KISO_VERSION  Release tag to download. Defaults to the pinned version.
#   KISO_CACHE_DIR  Directory where the binary is cached.
#
# Usage: make check | make build
#
# Requires: curl (and java when no native binary exists for the platform).

set -euo pipefail

readonly KISO_VERSION="${KISO_VERSION:-v0.2.6}"
readonly KISO_CACHE_DIR="${KISO_CACHE_DIR:-${XDG_CACHE_HOME:-${HOME}/.cache}/kiso/${KISO_VERSION}}"
readonly KISO_BASE_URL="https://github.com/oak-invest/kiso/releases/download"

#######################################
# @internal
# @description Print the kiso-cli release asset for the current platform.
# @noargs
# @stdout The asset file name, or an empty string when none matches.
# @exitcode 0 Always.
#######################################
kiso_asset() {
	case "$(uname -s)/$(uname -m)" in
	Linux/x86_64) printf 'kiso-cli-linux-x64\n' ;;
	Darwin/arm64) printf 'kiso-cli-macos-arm64\n' ;;
	*) printf '\n' ;;
	esac
}

#######################################
# @internal
# @description Download a release asset when it is not already cached.
# @arg $1 string The release asset name.
# @stderr A message when the download fails.
# @exitcode 0 If the asset is available locally.
# @exitcode 1 If the download fails.
#######################################
download_asset() {
	local asset="$1"
	local target="${KISO_CACHE_DIR}/${asset}"

	if [[ -s ${target} ]]; then
		return 0
	fi

	mkdir -p "${KISO_CACHE_DIR}"
	if ! curl -sSfL -o "${target}.tmp" \
		"${KISO_BASE_URL}/${KISO_VERSION}/${asset}"; then
		printf 'Failed to download %s %s\n' "${asset}" "${KISO_VERSION}" >&2
		rm -f "${target}.tmp"
		return 1
	fi

	chmod +x "${target}.tmp"
	mv "${target}.tmp" "${target}"
}

#######################################
# @description Run kiso-cli against the docs/ OKF bundle.
# @arg $@ string The kiso-cli command and options. Defaults to `check`.
# @stdout The kiso-cli output.
# @stderr A message when a required tool is missing or the download fails.
# @exitcode 0 If kiso-cli succeeds.
# @exitcode 1 If a prerequisite is missing or kiso-cli reports an error.
#######################################
main() {
	local root_dir
	local asset
	local kiso_cmd=()
	local args=("$@")

	if ! command -v curl >/dev/null 2>&1; then
		printf 'curl is required to download kiso-cli\n' >&2
		return 1
	fi

	if [[ ${#args[@]} -eq 0 ]]; then
		args=(check)
	fi

	root_dir="$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)"
	asset="$(kiso_asset)"

	if [[ -n ${asset} ]]; then
		download_asset "${asset}"
		kiso_cmd=("${KISO_CACHE_DIR}/${asset}")
	else
		if ! command -v java >/dev/null 2>&1; then
			printf '%s\n' \
				'No native kiso-cli for this platform and java is not installed' >&2
			return 1
		fi
		download_asset 'kiso-cli.jar'
		kiso_cmd=(java -jar "${KISO_CACHE_DIR}/kiso-cli.jar")
	fi

	"${kiso_cmd[@]}" "${args[@]}" --source="${root_dir}/docs"
}

main "$@"
