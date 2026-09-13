#!/bin/bash
# Initialize or reconfigure the local QMD (semantic search) index for the conference knowledge bundle.
#
# This script sets up a QMD collection pointing to docs/ and generates vector embeddings
# for all concept documents. It is idempotent—safe to run multiple times (removes and recreates
# the collection if it already exists). Run this once after cloning the repository or when
# resetting the QMD index.
#
# Environment variables:
#   QMD_FORCE_CPU=1  (default) Use CPU backend. Set to 0 if your QMD has stable GPU support.
#
# Usage: make qmd-setup
#
# Requires: qmd (https://github.com/tobi/qmd)

set -euo pipefail

# Avoid a known llama.cpp Metal shutdown crash on some macOS installations.
export QMD_FORCE_CPU="${QMD_FORCE_CPU:-1}"

readonly COLLECTION_NAME='yt-conferences'

#######################################
# @internal
# @description Run a QMD command and report failures.
# @arg $@ string The QMD command and its arguments.
# @stderr A message when the QMD command fails.
# @exitcode 0 If the QMD command succeeds.
# @exitcode 1 If the QMD command fails.
#######################################
run_qmd() {
	if ! qmd "$@"; then
		printf 'QMD command failed: qmd %s\n' "$*" >&2
		return 1
	fi
}

#######################################
# @description Initialize the QMD collection and embeddings.
# @set QMD_FORCE_CPU string Set to use the CPU QMD runtime by default.
# @stdout QMD command output and a completion message.
# @stderr A message when QMD is unavailable.
# @exitcode 0 If the collection is initialized successfully.
# @exitcode 1 If QMD is unavailable or a command fails.
#######################################
main() {
	local root_dir
	local collection_path
	local collection_list

	if ! command -v qmd >/dev/null 2>&1; then
		printf '%s\n' \
			'qmd is required: https://github.com/tobi/qmd' >&2
		return 1
	fi

	root_dir="$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)"
	collection_path="${root_dir}/docs"

	run_qmd init

	collection_list="$(qmd collection list 2>/dev/null || true)"
	if grep -q "^${COLLECTION_NAME}[[:space:]]" <<<"${collection_list}"; then
		run_qmd collection remove "${COLLECTION_NAME}"
	fi
	run_qmd collection add "${collection_path}" --name "${COLLECTION_NAME}"

	run_qmd context add "qmd://${COLLECTION_NAME}" \
		'OKF v0.2 video-note knowledge bundle organized by conference and learning topic.'

	run_qmd update
	run_qmd embed -c "${COLLECTION_NAME}"

	printf 'QMD is ready: collection=%s path=%s\n' \
		"${COLLECTION_NAME}" "${collection_path}"
}

main "$@"
