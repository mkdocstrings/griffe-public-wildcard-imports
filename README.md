# griffe-public-wildcard-imports

[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-public-wildcard-imports/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-708FCC.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-public-wildcard-imports)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe-public-wildcard-imports:gitter.im)

Mark wildcard imported objects as public.

## Installation

This project is available to sponsors only, through my Insiders program.
See Insiders [explanation](https://mkdocstrings.github.io/griffe-public-wildcard-imports/insiders/)
and [installation instructions](https://mkdocstrings.github.io/griffe-public-wildcard-imports/insiders/installation/).

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
