# Download and load spaCy models on-the-fly

A tiny drop-in replacement for `spacy.load()` that automatically downloads a model when it is not currently installed.

```shell
pip install spacy_download
```

Usage is identical to [`spacy.load()`](https://spacy.io/api/top-level/#spacy.load), meaning that you can also exclude
or disable pipeline components. Example:

```python
from spacy_download import load_spacy

# Will download the model if it isn't installed yet
nlp = load_spacy("en_core_web_sm", exclude=["parser", "tagger"])  
```

Under the hood, the package makes use of spaCy's capability to import models as modules, rather than using spaCy's
built-in loader. This allows us to first download a model with `pip` and then load it as a module.

**Note**: if you are using transformer models, you still need to install `spacy-transformers` yourself!

**WARNING**: loading models on the fly can be useful, but it is
[not an officially supported feature](https://github.com/explosion/spaCy/discussions/10608). It should work fine with
the official models at the time of writing, but I cannot guarantee that this will always be the case.
Use at your own risk.
