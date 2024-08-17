"""griffe-public-wildcard-imports package.

Mark wildcard imported objects as public.
"""

from __future__ import annotations

from griffe_public_wildcard_imports._internals.extension import PublicWildcardImportsExtension

__all__: list[str] = ["PublicWildcardImportsExtension"]
