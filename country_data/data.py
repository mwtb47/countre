"""Script to create a csv file containing all country data.

Save a csv files with the following columns:

    'calling_code': Country calling code.
    'capital_city': Capital city.
    'capital_latitude': Decimal latitude of capital city.
    'capital_latitude_sexa': Sexagesimal latitude of capital city.
    'capital_longitude': decimal Longitude of capital city.
    'capital_longitude_sexa': Sexagesimal longitude of capital city.
    'ccTLD': Country code top-level domain.
    'continent': Continent country is located in.
    'country': Name of country.
    'country_short': Short version of country name.
    'country_sv': Country name in Swedish.
    'currency_iso': ISO code of the official currency.
    'currency_name': Name of the official currency.
    'currency_symbol': Symbol of the official currency.
    'EU': EU member True / False.
    'EU_EEA': EU / EEA member True / False.
    'flag': Flag emoji.
    'gdp_2021': Nominal gdp in $ (World Bank 2021).
    'gdp_per_capita_2021': Nominal gdp per capita in $ (World Bank 2021).
    'gdp_per_capita_ppp_2021': PPP gdp per capita in $ (World Bank 2021).
    'gini': Gini coefficient.
    'hci': Human Capital Index.
    'hdi': Human Development Index.
    'iso2': Two letter country code.
    'iso3': Three letter country code.
    'iso_numeric': Numerical country identifier.
    'land_area': Land area in km^2.
    'latitude': Latitiude of approximate centre point of country.
    'latitude_sexa': Sexagesimal latitiude of approximate centre point
        of country.
    'longitude': Longitude of approximate centre point of country.
    'longitude_sexa': Sexagesimal longitude of approximate centre point
        of country.
    'NATO': NATO member True / False
    'OECD': OECD member True / False
    'OPEC': OPEC member True / False
    'population_2021': 2021 population (World Bank).
    'sub_region': Sub-region of continent country is located in.
    'total_area': Total area in km^2.
    'water_area': Water area in km^2.

Email: mwt.barnes@outlook.com
"""

import pandas as pd
import numpy as np
import world_bank_data as wb

from organisations import EU_ISO3, EU_EEA_ISO3, NATO_ISO3, OECD_ISO3, OPEC_ISO3


def get_wb_data(metric: str, name: str) -> pd.DataFrame:
    """Retreive data from World Bank and return a DataFrame.

    Args:
        metric: World Bank code for the metric.
        name: Column name for the metric.

    Returns:
        DataFrame with fetched data.
    """
    return (
        pd.DataFrame(
            wb.get_series(metric, mrv=1, id_or_value="id", simplify_index=True)
        )
        .reset_index()
        .rename(columns={"Country": "iso3", metric: name})
    )


def add_organisation_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add indicators for OECD, EU, and EU/EEA membership."""
    df["EU"] = np.where(df["iso3"].isin(EU_ISO3), True, False)
    df["EU_EEA"] = np.where(df["iso3"].isin(EU_EEA_ISO3), True, False)
    df["NATO"] = np.where(df["iso3"].isin(NATO_ISO3), True, False)
    df["OECD"] = np.where(df["iso3"].isin(OECD_ISO3), True, False)
    df["OPEC"] = np.where(df["iso3"].isin(OPEC_ISO3), True, False)
    return df


def read_additional_data() -> list[pd.DataFrame]:
    """Read additional data and return a list of DataFrames.

    Returns:
        A list of DataFrames.
    """
    filenames = [
        "cctld",
        "calling_codes",
        "coordinates",
        "continents",
        "flag_emojis",
        "areas",
        "capital_cities",
        "currencies",
        "gini",
        "undp_hdi",
        "countries_sv",
    ]
    additional_data = [
        pd.read_csv(f"country_data/data/{filename}.csv") for filename in filenames
    ]

    # World Bank data
    additional_data.append(get_wb_data("SP.POP.TOTL", "population"))
    additional_data.append(get_wb_data("NY.GDP.MKTP.CD", "gdp_2021"))
    additional_data.append(get_wb_data("NY.GDP.PCAP.CD", "gdp_per_capita_2021"))
    additional_data.append(get_wb_data("NY.GDP.PCAP.PP.CD", "gdp_per_capita_ppp_2021"))
    additional_data.append(get_wb_data("HD.HCI.OVRL", "hci"))

    return additional_data


def format_df(df: pd.DataFrame) -> pd.DataFrame:
    """Format DataFrame and add organisation indicators.

    Args:
        df: The DataFrame to format.

    Returns:
        Formatted DataFrame.
    """
    df[["latitude", "longitude"]] = round(df[["latitude", "longitude"]], 6)
    df[["gdp_per_capita_2021", "gdp_per_capita_ppp_2021"]] = round(
        df[["gdp_per_capita_2021", "gdp_per_capita_ppp_2021"]], 4
    )
    df["hci"] = round(df["hci"], 3)

    # OECD, EU, EU/EEA booleans
    df = add_organisation_indicators(df)

    return df[
        [
            "calling_code",
            "capital_city",
            "capital_latitude",
            "capital_latitude_sexa",
            "capital_longitude",
            "capital_longitude_sexa",
            "ccTLD",
            "continent",
            "country",
            "country_short",
            "country_sv",
            "currency_iso",
            "currency_name",
            "currency_symbol",
            "EU",
            "EU_EEA",
            "flag",
            "gdp_2021",
            "gdp_per_capita_2021",
            "gdp_per_capita_ppp_2021",
            "gini",
            "hci",
            "hdi",
            "iso2",
            "iso3",
            "iso_numeric",
            "land_area",
            "latitude",
            "latitude_sexa",
            "longitude",
            "longitude_sexa",
            "NATO",
            "OECD",
            "OPEC",
            "population",
            "sub_region",
            "total_area",
            "water_area",
        ]
    ]


def main():
    """Merge all the DataFrames and save to a csv."""
    df = pd.read_csv(
        "country_data/data/ISO_countries.csv",
        dtype={"iso_numeric": str},
        keep_default_na=False,
        na_values=[""],
    )

    # Merge all data frames
    additional_data = read_additional_data()
    for data in additional_data:
        df = df.merge(data, on="iso3", how="left")

    df = format_df(df)
    df.to_csv("country_data/countries_summary_data.csv", index=False)


if __name__ == "__main__":
    main()
