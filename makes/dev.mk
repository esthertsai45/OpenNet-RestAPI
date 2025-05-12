.PHONY: format
format:
	isort --atomic --profile black module tests
	black module tests

.PHONY: check
check:
	flake8 module tests --max-line-length 140
	black --check module tests
	mypy --ignore-missing-imports --check-untyped-defs --no-namespace-packages module tests
