from importlib import import_module

from spacy import Language
from spacy.cli import download


def load_spacy(model_name: str, **kwargs) -> Language:
    """Load a spaCy model, download it if it has not been installed yet.
    :param model_name: the model name, e.g., en_core_web_sm
    :param kwargs: options passed to the spaCy loader, such as component exclusion, as you
    would with spacy.load()
    :return: an initialized spaCy Language
    :raises: SystemExit: if the model_name cannot be downloaded
    """
    try:
        model_module = import_module(model_name)
    except ModuleNotFoundError:
        download(model_name)
        model_module = import_module(model_name)

    return model_module.load(**kwargs)
