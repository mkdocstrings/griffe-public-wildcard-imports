"""Test extension."""

import griffe


def test_extension() -> None:
    """Wildcard imported objects are marked as public."""
    with griffe.temporary_visited_package(
        "package",
        {
            "__init__.py": "from package.module import *",
            "module.py": "def f(): ...\nclass C: ...",
        },
        resolve_aliases=True,
        extensions=griffe.load_extensions("griffe_public_wildcard_imports"),
    ) as package:
        assert package["f"].public
        assert package["f"].is_public
        assert package["C"].public
        assert package["C"].is_public
