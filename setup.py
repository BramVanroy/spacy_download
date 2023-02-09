from pathlib import Path
from setuptools import find_packages, setup


setup(
    name="spacy_download",
    version="1.1.0",
    description="Download and load spaCy models on-the-fly.",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    keywords="nlp spacy spacy-extension",
    package_dir={"": "src"},
    packages=find_packages("src"),
    url="https://github.com/BramVanroy/spacy_download",
    author="Bram Vanroy",
    author_email="bramvanroy@hotmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Text Processing",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Bug Reports": "https://github.com/BramVanroy/spacy_download/issues",
        "Source": "https://github.com/BramVanroy/spacy_download",
    },
    python_requires=">=3.6",
    install_requires=["spacy<4.0.0,>=3.0.0"],
    extras_require={"dev": ["pytest", "flake8", "isort", "black", "pygments", "spacy-transformers"]},
)
