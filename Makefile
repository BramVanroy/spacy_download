# Format source code automatically
style:
	black --line-length 119 --target-version py36 spacy_download
	isort spacy_download

# Control quality
quality:
	black --check --line-length 119 --target-version py36 spacy_download
	isort --check-only spacy_download
	flake8 spacy_download --exclude __pycache__,__init__.py

# Run tests
test:
	pytest tests
