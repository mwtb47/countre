"""Module containing function to return organisation member information..

Functions:
    member_countries: Return attribute of member countries of an organisation.
"""


from countre._regex_dict import data
from countre import enums


def member_countries(
    organisation: enums.Organisation,
    attribute: enums.Attribute = enums.Attribute.COUNTRY,
) -> list[str]:
    """
    Return a list containing organisation member countries.

    Select an Attribute enum to return for each of the member
    countries in the selected organisation.

    Args:
        organisation: An Organisation enum.
        attribute: An Attribute enum selecting the attribute to
            return. Use COUNTRY, COUNTRY_SHORT, ISO2 OR IS3 to
            get member country names or codes.

    Returns:
        A list of the selected attribute for the member countries.
    """
    return [
        country_data[attribute.value]
        for country_data in data.values()
        if country_data[organisation.value]
    ]
