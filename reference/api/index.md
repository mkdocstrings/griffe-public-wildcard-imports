# griffe_public_wildcard_imports

griffe-public-wildcard-imports package.

Mark wildcard imported objects as public.

Classes:

- **`PublicWildcardImportsExtension`** – Mark wildcard imported objects as public.

## PublicWildcardImportsExtension

Bases: `Extension`

Mark wildcard imported objects as public.

Methods:

- **`on_alias`** – Mark wildcard imported aliases as public.

### on_alias

```
on_alias(*, alias: Alias, **kwargs: Any) -> None
```

Mark wildcard imported aliases as public.

Source code in `src/griffe_public_wildcard_imports/_internal/extension.py`

```
def on_alias(self, *, alias: griffe.Alias, **kwargs: Any) -> None:  # noqa: ARG002
    """Mark wildcard imported aliases as public."""
    if alias.wildcard_imported:
        alias.public = True
```
