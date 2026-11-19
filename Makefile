SUMMARIZER_SOURCE ?= git+https://github.com/electrocucaracha/yt-summarizer.git@561994d3fba4016a5b774e0b0660028d3cd66e80
COLLECTION ?=
PORT ?= 8099
QMD_COLLECTION ?= yt-conferences
export QMD_FORCE_CPU ?= 1
TOOLS := uv run --no-project --python 3.12 --with-requirements requirements-dev.txt

.PHONY: install summarize summarize-dry-run lint fmt check build preview qmd-setup qmd-update qmd-embed qmd-check qmd-mcp template-check template-diff template-update

install:
	uv tool install --python 3.12 "$(SUMMARIZER_SOURCE)"
	uv tool install cruft==2.16.0

summarize:
	python3 scripts/summarize.py $(if $(COLLECTION),--collection "$(COLLECTION)")

summarize-dry-run:
	python3 scripts/summarize.py --dry-run $(if $(COLLECTION),--collection "$(COLLECTION)")

lint:
	$(TOOLS) black --check scripts
	$(TOOLS) isort --check-only scripts
	$(TOOLS) ruff check scripts
	$(TOOLS) pylint scripts
	$(TOOLS) mypy scripts
	$(TOOLS) bandit --recursive --severity-level medium --confidence-level medium scripts

fmt:
	$(TOOLS) isort scripts
	$(TOOLS) black scripts

check:
	kiso check --source=docs

build:
	kiso build --source=docs --destination=public

preview: build
	python3 -m http.server $(PORT) --bind 127.0.0.1 --directory public

qmd-setup:
	qmd init
	qmd collection add "$(CURDIR)/docs" --name "$(QMD_COLLECTION)"
	qmd context add "qmd://$(QMD_COLLECTION)" "OKF video notes organized by playlist and topic."

qmd-update:
	qmd update

qmd-embed:
	qmd embed -c "$(QMD_COLLECTION)"

qmd-check:
	qmd status
	qmd ls "$(QMD_COLLECTION)"

qmd-mcp:
	qmd mcp

template-check:
	cruft check

template-diff:
	cruft diff

template-update:
	cruft update