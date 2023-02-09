# Format source code automatically
style:
	black --line-length 119 --target-version py36 src/spacy_download
	isort src/spacy_download

# Control quality
quality:
	black --check --line-length 119 --target-version py36 src/spacy_download
	isort --check-only src/spacy_download
	flake8 src/spacy_download --exclude __pycache__,__init__.py

# Run tests
test:
	pytest tests
