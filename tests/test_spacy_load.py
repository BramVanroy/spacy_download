import pytest

from spacy_download.load import load_spacy


def test_download_existing_model(existing_model):
    load_spacy(existing_model)


def test_download_existing_trf_model(existing_trf_model):
    load_spacy(existing_trf_model)


def test_fail_nonexisting_model(non_existing_model):
    with pytest.raises(SystemExit) :
        load_spacy(non_existing_model)
