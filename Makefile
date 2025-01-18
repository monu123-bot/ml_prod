.PHONY: run install clean runner
.DEFAULT_GOAL := runner

run: install
	# Navigate to the src directory and run the application
	cd src; poetry run python runner.py

install: pyproject.toml
	# Install the project dependencies using poetry
	poetry install

clean: 
	# Remove all __pycache__ directories
	rm -rf `find . -type d -name __pycache__`

check:
	# Run flake8 to check code quality in the src directory
	poetry run flake8 src/

runner:
	# Run all necessary tasks in sequence
	check run clean
