install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

lint:
	uv run ruff check

update:
	uv tool install --force dist/hexlet_code-0.1.0.tar.gz

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest