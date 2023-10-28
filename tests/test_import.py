"""Test sql-flatmap."""

import sql_flatmap


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(sql_flatmap.__name__, str)
