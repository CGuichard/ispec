##@ ISpec project Makefile, with utility commands for the project development lifecycle.

PYTHON=python3
PIP=$(PYTHON) -mpip
TOX=$(PYTHON) -mtox

.PHONY: default release clean build install install-dev
.PHONY: format lint test docs security
.PHONY: pre-commit pipeline test-report docs-serve

# ======================================================= #

default: pipeline

release: ## Bump version, create tag and update CHANGELOG.
	@$(PYTHON) -mcommitizen bump --changelog

build: ## Build wheel and tar.gz in 'dist/'.
	@$(PYTHON) -mbuild

install: ## Install in the current python env.
	@$(PIP) install .

install-dev: ## Install in editable mode inside the current python env with dev dependencies.
	@$(PIP) install -e .[dev]

format: ## Format python code.
	@$(TOX) -e $@

lint: ## Lint python source code.
	@$(TOX) -e $@

test: ## Invoke pytest to run automated tests.
	@$(TOX)

docs: ## Build the docs.
	@$(TOX) -e $@

security: ## Security check on project dependencies.
	@$(TOX) -e $@

pre-commit: ## Run pre-commit on all tracked files.
	@$(PYTHON) -mpre_commit run --all-files
	@$(PYTHON) -mpre_commit run --hook-stage push --all-files

pipeline: security format lint test build docs ## Run security, format, lint, test, build and docs.

report: ## Start http server to serve the test report and coverage.
	@printf "# ---------------------------------------------\n"
	@printf "Test report: http://localhost:9000\n"
	@printf "Coverage report: http://localhost:9000/coverage\n"
	@$(PYTHON) -mhttp.server -b 0.0.0.0 -d tests-reports 9000 > /dev/null

serve: ## Start http server to serve the docs.
	@printf "# ---------------------------------------------\n"
	@printf "Docs: http://localhost:8000\n"
	@$(PYTHON) -mhttp.server -b 0.0.0.0 -d docs/build/html 8000 > /dev/null

clean: ## Clean temporary files, like python __pycache__, dist build, docs output, and tests reports.
	@find src tests -regex "^.*\(__pycache__\|\.py[co]\)$$" -delete
	@rm -rf docs/build dist tests-reports .coverage* .*_cache

# ======================================================= #

HELP_COLUMN=11
help: ## Show this help.
	@printf "\033[1m################\n#     Help     #\n################\033[0m\n"
	@awk 'BEGIN {FS = ":.*##@"; printf "\n"} /^##@/ { printf "%s\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n\n  make \033[36m<target>\033[0m\n\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-$(HELP_COLUMN)s\033[0m %s\n", $$1, $$2 } ' $(MAKEFILE_LIST)
	@printf "\n"
