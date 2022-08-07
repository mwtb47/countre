"""Module with enums for attributes and organisations.

Classes:
    Attribute: Class with attribute enums.
    Organisation: Class with organisation enums.
"""

from enum import Enum


class Attribute(Enum):
    """Class containing enums for country attributes."""

    CALLING_CODE = "calling_code"
    """The calling code."""

    CAPITAL = "capital_city"
    """The name of the capital city."""

    CAPITAL_LATITUDE = "capital_latitude"
    """The capital city's latitude in decimal form."""

    CAPITAL_LATITUDE_SEXA = "capital_latitude_sexa"
    """The capital city's latitude in sexagesimal form."""

    CAPITAL_LONGITUDE = "capital_longitude"
    """The capital city's longitude in decimal form."""

    CAPITAL_LONGITUDE_SEXA = "capital_longitude_sexa"
    """The capital city's longitude in sexagesimal form."""

    CCTLD = "ccTLD"
    """The country code top-level domain."""

    CONTINENT = "continent"
    """The continent the country is a part of."""

    COUNTRY = "country"
    """The name of the country."""

    COUNTRY_SHORT = "country_short"
    """The short name of the country."""

    COUNTRY_SV = "country_sv"
    """The name of the country in Swedish."""

    CURRENCY_ISO = "currency_iso"
    """The ISO code for the currency."""

    CURRENCY_NAME = "currency_name"
    """The name of the currency."""

    CURRENCY_SYMBOL = "currency_symbol"
    """The symbol of the currency."""

    EU = "EU"
    """Boolean indicating if a country is a member of the EU or not."""

    EU_EEA = "EU_EEA"
    """Boolean indicating if a country is a member of the EU or EEA, or not."""

    FLAG = "flag"
    """The flag emoji."""

    GDP = "gdp_2021"
    """The GDP in constant USD (WOrld Bank 2021)."""

    GDP_PER_CAPITA = "gdp_per_capita_2021"
    """The GDP per capita in constant USD (World Bank 2021)."""

    GDP_PER_CAPITA_PPP = "gdp_per_capita_ppp_2021"
    """The GDP per capita PPP in constant USD (World Bank 2021)."""

    GINI = "gini"
    """The Gini coefficient."""

    HCI = "hci"
    """World Bank's Human Capital Index."""

    HDI = "hdi"
    """United Nations Development Programme's Human Development Index."""

    ISO2 = "iso2"
    """The ISO2 code."""

    ISO3 = "iso3"
    """The ISO3 code."""

    ISO_NUMERIC = "iso_numeric"
    """The ISO numeric code."""

    LAND_AREA = "land_area"
    """The land area (km^2)."""

    LATITUDE = "latitude"
    """The latitude in decimal form."""

    LATITUDE_SEXA = "latitude_sexa"
    """The latitude in sexagesimal form."""

    LONGITUDE = "longitude"
    """The longitude in decimal form."""

    LONGITUDE_SEXA = "longitude_sexa"
    """The longitude in sexagesimal form."""

    NATO = "NATO"
    """Boolean indicating if a country is a member of the NATO or not."""

    OECD = "OECD"
    """Boolean indicating if a country is a member of the OECD or not."""

    OPEC = "OPEC"
    """Boolean indicating if a country is a member of the OPEC or not."""

    POPULATION = "population"
    """The population (World Bank 2021)."""

    SUB_REGION = "sub_region"
    """The sub-region the country is a part of."""

    TOTAL_AREA = "total_area"
    """The total area, including land and water (km^2)."""

    WATER_AREA = "water_area"
    """The water area (km^2)."""


class Organisation(Enum):
    """Class containing enums for organisations."""

    EU = "EU"
    """The European Union."""

    EU_EEA = "EU_EEA"
    """The European Union and the European Economic Area."""

    NATO = "NATO"
    """The North Atlantic Treaty Organization."""

    OECD = "OECD"
    """The Organisation for Economic Co-operation and Development."""

    OPEC = "OPEC"
    """The Organization of the Petroleum Exporting Countries."""
