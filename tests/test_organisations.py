"""Module with functions to test the member_countries function in countre.

Functions:
    test_all_eu_present: Test function returns all EU members.
    test_all_eu_eea_present: Test function returns all EU or EEa members.
    test_all_nato_present: Test function returns all NATO members.
    test_all_oecd_present: Test function returns all OECD members.
    test_all_opec_present: Test function returns all OPEC members.
    test_default_attribute: Test default attrbute is country name.
"""

import pytest

from countre._organisations import member_countries
from countre.enums import Attribute, Organisation
from country_data.organisations import (
    OECD_ISO3,
    OPEC_ISO3,
    NATO_ISO3,
    EU_ISO3,
    EU_EEA_ISO3,
)


test_data = [
    (Organisation.EU, EU_ISO3),
    (Organisation.EU_EEA, EU_EEA_ISO3),
    (Organisation.NATO, NATO_ISO3),
    (Organisation.OECD, OECD_ISO3),
    (Organisation.OPEC, OPEC_ISO3),
]

test_ids = [pair[0].value for pair in test_data]


@pytest.mark.parametrize(("organisation", "iso3_codes"), test_data, ids=test_ids)
def test_all_members(organisation: Organisation, iso3_codes: list[str]) -> None:
    """Test that all members of an organisation are returned.

    Args:
        organisation: Organisation enum.
        iso3_codes: List of expected ISO3 codes.
    """
    countries = member_countries(organisation, Attribute.ISO3)
    assert sorted(countries) == sorted(iso3_codes)


def test_default_attribute() -> None:
    """Test that the default attribute is the country name."""
    countries = member_countries(Organisation.EU)
    assert sorted(countries)[0] == "Austria"
