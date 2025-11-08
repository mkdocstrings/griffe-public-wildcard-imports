# griffe-public-wildcard-imports

[![ci](https://github.com/mkdocstrings/griffe-public-wildcard-imports/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe-public-wildcard-imports/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-public-wildcard-imports/)
[![pypi version](https://img.shields.io/pypi/v/griffe-public-wildcard-imports.svg)](https://pypi.org/project/griffe-public-wildcard-imports/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#griffe-public-wildcard-imports:gitter.im)

Mark wildcard imported objects as public.

## Installation

```bash
pip install griffe-public-wildcard-imports
```

## Usage

[Enable](https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions) the `griffe_public_wildcard_imports` extension. Now all objects imported through wildcard imports will be considered public, as per the convention.

```python
# All imported objects are marked as public.
from somewhere import *
```

With MkDocs:

```yaml
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_public_wildcard_imports
```

## Sponsors

<!-- sponsors-start -->
<!-- sponsors-end -->
