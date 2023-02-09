# History

## 1.1.0 (February 9th, 2023)

Mostly repackaging, but usage remains the same except for `__version__`.

- `setup.py` now pins spacy version to `spacy<4.0.0,>=3.0.0` because it does not work with `spacy<3`
- dev-extras now include `spacy-transformers` to run the tests
- `__version__` variable removed from library files as it was causing import errors during a development install. If
you really need to get the version, there are [other ways](https://stackoverflow.com/a/32965521/1150683) 


## 1.0.0 (April 4th, 2022)

First release!
