# griffe-public-wildcard-imports

Mark wildcard imported objects as public.

## Installation

```
pip install griffe-public-wildcard-imports
```

## Usage

[Enable](https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions) the `griffe_public_wildcard_imports` extension. Now all objects imported through wildcard imports will be considered public, as per the convention.

```
# All imported objects are marked as public.
from somewhere import *
```

With MkDocs:

```
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_public_wildcard_imports
```

## Sponsors
