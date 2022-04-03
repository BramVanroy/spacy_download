import sys

import pytest
from spacy.util import run_command


@pytest.fixture
def existing_model() -> str:
    return "en_core_web_sm"


@pytest.fixture
def existing_trf_model() -> str:
    return "en_core_web_trf"


@pytest.fixture
def non_existing_model() -> str:
    return "3n_C0r3_W3b_$m"


@pytest.fixture(autouse=True)
def uninstall_package(existing_model, existing_trf_model):
    # TODO: (maybe) more thorough uninstall, e.g., by collecting pip freeze before every test
    # and after every test, then writing the diff of these to a dummy requirements.txt file
    # and then pip uninstall -r requirements.txt
    cmd = [sys.executable, "-m", "pip", "uninstall"] + [existing_model, existing_trf_model] + ["-y", "-qqq"]
    run_command(cmd)  # uninstall models before
    yield
    run_command(cmd)  # ... and after every function