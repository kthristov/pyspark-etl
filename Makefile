APP_NAME ?= $$(cat pyproject.toml| grep name | cut -d" " -f3 | sed  's/"//g')
VERSION_NO ?= $$(poetry version --short)

SRC_WITH_DEPS ?= src_with_deps

src_dir := src/$(package)
test_dir := tests/

.PHONY: lint
lint: $(virtualenv_dir)
	poetry update
	poetry install --no-ansi -vvv
	poetry run flake8 $(src_dir) 
	poetry run isort .
	poetry run mypy $(src_dir) 
	terraform fmt -recursive

test: 
	export PYARROW_IGNORE_TIMEZONE=1
	poetry install --no-ansi -vvv
	poetry build
	poetry run pytest --cov=$(src_dir) --cov-branch --cov-fail-under 85

build: clean lint test
	echo "Packaging Code and Dependencies for ${APP_NAME}-${VERSION_NO}"
	# TODO

deploy:
	echo "Deploying Code and Dependencies for ${APP_NAME}-${VERSION_NO}"
	# TODO

clean:
	rm -Rf ./dist
	rm -Rf ./${SRC_WITH_DEPS}
	rm -f requirements.txt
