install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

update:
	uv tool install --force dist/hexlet_code-0.1.0.tar.gz

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest