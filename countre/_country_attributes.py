"""Module containing functions to get country attributes.

Functions:
    country_info: Return attribute values for a list of countries.
"""

import re
from typing import Iterable

from countre._regex_dict import data
from countre import enums


def country_info(
    countries: Iterable[str],
    attributes: enums.Attribute | list[enums.Attribute],
    no_match: str = "no match",
) -> list | dict[str, list]:
    """
    Returns attributes for each country in either a list or dictionary.

    Args:
        countries: Iterable of country names, iso2 or iso3 codes to get
            attributes for.
        attributes: An Attribute enum or list of Attribute enums.
        no_match: The value returned for a country if there is no match.
            The default is 'no match'.

    Returns:
        A list of values if only one attribute is provided. A dictionary of
        values if more than one attribute is given. The attributes are the
        keys and the list of values are the values.
    """
    unique_countries = set(countries)

    if isinstance(attributes, list):
        results = {}
        for attribute in attributes:
            unique_data = _get_unique_data(attribute, unique_countries, no_match)
            results[attribute.value] = [unique_data[country] for country in countries]
        return results

    if isinstance(attributes, enums.Attribute):
        unique_data = _get_unique_data(attributes, unique_countries, no_match)
        return [unique_data[country] for country in countries]

    raise TypeError(
        "attributes argument must be Attribute enum or a list of Attribute enums."
    )


def _pattern_match(regex_pattern: str, country: str) -> bool:
    """Check if country matches a given regex pattern.

    Args:
        regex_pattern: The regex pattern.
        country: The name of the country.

    Returns:
        True if country matches the pattern, else False.
    """
    return bool(re.match(regex_pattern, country, re.IGNORECASE))


def _country_generator(country: str, attribute: str):
    """Return a generator expression which yields attribute values.

    Iterate over each regex pattern and yield the attribute value
    for that pattern if the country name matches.

    Args:
        country: The name of the country.
        attribute: The attribute to return value for.

    Returns:
        Generator expression.
    """
    return (
        country_data[attribute]
        for regex_pattern, country_data in data.items()
        if _pattern_match(regex_pattern, country)
    )


def _get_match(country: str, attribute: str, no_match: str) -> str | int | float:
    """Get the attribute value for a country.

    Args:
        country: The name of the country.
        attribute: The attribute to return value for.
        no_match: Value to return when no country match is found.

    Returns:
        The attribute value of the first match. If there are no
        matches, the default no_match value is returned.
    """
    country = country.strip()
    return next(_country_generator(country, attribute), no_match)


def _get_unique_data(
    attribute: enums.Attribute, unique_countries: set, no_match: str
) -> dict[str, str]:
    """Get attribute value for each unique country.

    Args:
        attribute: An Attribute enum.
        unique_countries: Set of unique countries.
        no_match: Value to return when no country match is found.

    Returns:
        Dictionary where the country name is the key and the
        attribute value is the value.
    """
    return {
        country: _get_match(country, attribute.value, no_match)
        for country in unique_countries
    }
