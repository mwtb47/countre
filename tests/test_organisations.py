"""Module with functions to test the member_countries function in countre.

Functions:
    test_all_eu_present: Test function returns all EU members.
    test_all_eu_eea_present: Test function returns all EU or EEa members.
    test_all_nato_present: Test function returns all NATO members.
    test_all_oecd_present: Test function returns all OECD members.
    test_all_opec_present: Test function returns all OPEC members.
    test_default_attribute: Test default attrbute is country name.
"""

from countre._organisations import member_countries
from countre.enums import Attribute, Organisation
from country_data.organisations import (
    OECD_ISO3,
    OPEC_ISO3,
    NATO_ISO3,
    EU_ISO3,
    EU_EEA_ISO3,
)


def test_all_eu_present() -> None:
    """Test that all EU members are returned."""
    countries = member_countries(Organisation.EU, Attribute.ISO3)
    assert sorted(countries) == sorted(EU_ISO3)


def test_all_eu_eea_present() -> None:
    """Test that all EU or EEA members are returned."""
    countries = member_countries(Organisation.EU_EEA, Attribute.ISO3)
    assert sorted(countries) == sorted(EU_EEA_ISO3)


def test_all_nato_present() -> None:
    """Test that all NATO members are returned."""
    countries = member_countries(Organisation.NATO, Attribute.ISO3)
    assert sorted(countries) == sorted(NATO_ISO3)


def test_all_oecd_present() -> None:
    """Test that all OECD members are returned."""
    countries = member_countries(Organisation.OECD, Attribute.ISO3)
    assert sorted(countries) == sorted(OECD_ISO3)


def test_all_opec_present() -> None:
    """Test that all OPEC members are returned."""
    countries = member_countries(Organisation.OPEC, Attribute.ISO3)
    assert sorted(countries) == sorted(OPEC_ISO3)


def test_default_attribute() -> None:
    """Test that the default attribute is the country name."""
    countries = member_countries(Organisation.EU)
    assert sorted(countries)[0] == "Austria"
