# === Makefile ===

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

start:
	source .venv/bin/activate && which python3 && which pip




# Installiert Requirements in der venv
install: requirements.txt
	python -m pip install -r requirements.txt
