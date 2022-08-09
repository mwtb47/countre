"""Module with function to test the regex patterns used to match countries.

Functions:
    test_country: Test all versions of a country name are correctly matched.
"""

import pytest

from countre import country_info
from countre.enums import Attribute
from tests.country_names import test_specifications


test_ids = [country["name"] for country in test_specifications]


@pytest.mark.parametrize("country", test_specifications, ids=test_ids)
def test_country(country: dict[str, str | list]) -> None:
    """Test all versions of a country name return expected ISO3 code.

    Args:
        country: Dictionary with test specifications.
    """
    output = country_info(countries=country["test_names"], attributes=Attribute.ISO3)
    assert output == [country["iso3"]] * len(country["test_names"])
