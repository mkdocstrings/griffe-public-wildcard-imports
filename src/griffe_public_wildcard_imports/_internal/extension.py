from typing import Any

import griffe


class PublicWildcardImportsExtension(griffe.Extension):
    """Mark wildcard imported objects as public."""

    def on_alias(self, *, alias: griffe.Alias, **kwargs: Any) -> None:  # noqa: ARG002
        """Mark wildcard imported aliases as public."""
        if alias.wildcard_imported:
            alias.public = True
