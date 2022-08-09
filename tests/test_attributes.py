"""Module with function to test Attribute enums.

Functions:
    test_attribute: Test all Attribute enums return the expected value.
"""

import pytest

from countre import country_info
from countre.enums import Attribute


test_attributes = [
    (Attribute.CALLING_CODE, "+46"),
    (Attribute.CAPITAL, "Stockholm"),
    (Attribute.CAPITAL_LATITUDE, 18.0686),
    (Attribute.CAPITAL_LATITUDE_SEXA, "59°19′46″N"),
    (Attribute.CAPITAL_LONGITUDE, 59.3294),
    (Attribute.CAPITAL_LONGITUDE_SEXA, "18°4′7″E"),
    (Attribute.CCTLD, ".se"),
    (Attribute.CONTINENT, "Europe"),
    (Attribute.COUNTRY, "Sweden"),
    (Attribute.COUNTRY_SHORT, "Sweden"),
    (Attribute.COUNTRY_SV, "Sverige"),
    (Attribute.CURRENCY_ISO, "SEK"),
    (Attribute.CURRENCY_NAME, "Swedish krona"),
    (Attribute.CURRENCY_SYMBOL, "kr"),
    (Attribute.EU, True),
    (Attribute.EU_EEA, True),
    (Attribute.FLAG, "🇸🇪"),
    (Attribute.GDP, 627437898887.290039),
    (Attribute.GDP_PER_CAPITA, 60238.9866),
    (Attribute.GDP_PER_CAPITA_PPP, 59323.9646),
    (Attribute.GINI, 30),
    (Attribute.HCI, 0.795),
    (Attribute.HDI, 0.945),
    (Attribute.ISO2, "SE"),
    (Attribute.ISO3, "SWE"),
    (Attribute.ISO_NUMERIC, 752),
    (Attribute.LAND_AREA, 410335),
    (Attribute.LATITUDE, 62.783193),
    (Attribute.LATITUDE_SEXA, "62°46′59.5″N"),
    (Attribute.LONGITUDE, 15.345713),
    (Attribute.LONGITUDE_SEXA, "15°20′44.6″E"),
    (Attribute.NATO, False),
    (Attribute.OECD, True),
    (Attribute.OPEC, False),
    (Attribute.POPULATION, 10415811),
    (Attribute.SUB_REGION, "Northern Europe"),
    (Attribute.TOTAL_AREA, 450295),
    (Attribute.WATER_AREA, 39960),
]

test_ids = [pair[0].value for pair in test_attributes]


@pytest.mark.parametrize(("attribute", "value"), test_attributes, ids=test_ids)
def test_attribute(attribute: Attribute, value: str | int | float | bool) -> None:
    """Test Attribute enum returns the expected value.

    Args:
        attribute: Attribute enum to test.
        value: The expected value for the specified attribute.
    """
    output = country_info(countries=["Sweden"], attributes=attribute)
    assert output == [value]
