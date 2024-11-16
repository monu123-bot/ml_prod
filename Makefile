.PHONY: run install clean runner
.DEFAULD_GOAL:=runner
run: install
   cd src; poetry run python runner.py
install: pyproject.toml
    poetry install
clean: 
	rm -rf `find d -name __pycache__`
runner:
	run clean