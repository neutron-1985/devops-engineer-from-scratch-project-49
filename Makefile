install:
	uv sync # Install dependencies from pyproject.toml

brain-games:
	uv run brain-games # Run the brain-games script

build:
	uv build # Build the package

package-install:
	uv tool install dist/*.whl # Install the built package
