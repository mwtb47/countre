"""Module with functions to test the country_info function in countre.

Functions:
    test_attribute_string_specification: Test specification of single Attribute.
    test_attribute_list_string_specification: Test specification of list of Attributes.
    test_default_no_match: Test default value when no match is found
"""

import pytest

from countre import country_info
from countre.enums import Attribute


def test_attribute_string_specification() -> None:
    """Test that specifiying attributes as a string raises error."""
    with pytest.raises(
        TypeError,
        match="attributes argument must be Attribute enum or a list of Attribute enums.",
    ):
        country_info(countries=["France", "Germany"], attributes="capital")


def test_attribute_list_string_specification() -> None:
    """Test that specifiying attributes as a list of strings raises error."""
    with pytest.raises(
        TypeError,
        match="attributes argument must be Attribute enum or a list of Attribute enums.",
    ):
        country_info(
            countries=["France", "Germany"], attributes=["capital", "population"]
        )


def test_default_no_match() -> None:
    """Test default value for no match is 'no match'."""
    output = country_info(countries=["Mars", "Jupiter"], attributes=Attribute.ISO3)
    assert output == ["no match", "no match"]
